// Verifică tot conținutul și scrie docs/acoperire-competente.md.
// Rulare: npm run check-content
import { readFileSync, writeFileSync, existsSync } from 'node:fs';

const R = (p) => JSON.parse(readFileSync(new URL('../' + p, import.meta.url), 'utf-8'));
const cal = R('public/calendar/2026-2027.json');
const comp = R('public/content/competente.json');
const insigne = R('public/content/insigne.json').insigne;
const erori = [];
const avertismente = [];
const nivCal = new Map(cal.niveluri.map((n) => [n.id, n]));
const ids = new Set();
const peNivel = new Map();
const itemiToti = [];
const CEDILE = /[şţŞŢ]/;
const bossuri = [];

for (const clasa of [5, 6, 7, 8]) {
  const f = `public/content/clasa-${clasa}/index.json`;
  if (!existsSync(new URL('../' + f, import.meta.url))) continue;
  for (const { fisier } of R(f).fisiere) {
    const cale = `public/content/clasa-${clasa}/${fisier}`;
    const txt = readFileSync(new URL('../' + cale, import.meta.url), 'utf-8');
    if (CEDILE.test(txt)) erori.push(`${cale}: conține ş/ţ cu sedilă`);
    const c = JSON.parse(txt);
    for (const n of c.niveluri) {
      if (!nivCal.has(n.id) && !/-T0$/.test(n.id)) erori.push(`${cale}: nivelul ${n.id} nu există în calendar`);
      for (const p of n.pasi ?? []) for (const i of p.itemi ?? []) if (!c.itemi.some((x) => x.id === i)) erori.push(`${n.id}: pasul „${p.titlu}” cere itemul inexistent ${i}`);
    }
    for (const it of c.itemi) {
      const e = (m) => erori.push(`${it.id}: ${m}`);
      if (ids.has(it.id)) e('id duplicat');
      ids.add(it.id);
      if (!c.niveluri.some((n) => n.id === it.nivel)) e(`nivel necunoscut ${it.nivel}`);
      for (const k of it.competente) if (!comp[String(clasa)][k]) e(`competență inexistentă ${k}`);
      if (![1, 2, 3].includes(it.dificultate)) e('dificultate invalidă');
      if (!it.feedback?.corect || !it.feedback?.gresit) e('lipsește feedback-ul');
      const d = it.date;
      switch (it.tip) {
        case 'alegere': case 'denumeste': case 'grafic':
          if (!(d.variante?.length >= 2) || d.corect < 0 || d.corect >= d.variante.length) e('variante/corect invalid');
          if (new Set(d.variante).size !== d.variante.length) e('variante duplicate');
          break;
        case 'pin': if (!(d.toleranta > 0) || Math.abs(d.tinta.lat) > 90) e('țintă invalidă'); break;
        case 'etichete': if (new Set(d.tinte.map((t) => t.eticheta)).size !== d.tinte.length) e('etichete duplicate'); break;
        case 'ordoneaza': if (d.elemente.length < 3) e('prea puține elemente'); break;
        case 'asociaza':
          if (new Set(d.perechi.map((p) => p[1])).size !== d.perechi.length) e('perechi cu același răspuns în dreapta');
          break;
        case 'lacunar': {
          const k = (d.text.match(/\{\d+\}/g) ?? []).length;
          if (k !== d.raspunsuri.length) e(`${k} spații goale, dar ${d.raspunsuri.length} răspunsuri`);
          if (d.distractori.some((x) => d.raspunsuri.includes(x))) e('distractor egal cu un răspuns');
          break;
        }
        default: e(`tip necunoscut ${it.tip}`);
      }
      itemiToti.push({ ...it, clasa });
      if (!peNivel.has(it.nivel)) peNivel.set(it.nivel, []);
      peNivel.get(it.nivel).push(it);
    }
    for (const b of c.boss ?? []) bossuri.push(b);
  }
}
for (const b of bossuri) {
  const fara = b.niveluri.filter((n) => !peNivel.has(n));
  if (fara.length === b.niveluri.length) erori.push(`${b.id}: niciun nivel al lui nu are itemi`);
  else if (fara.length) avertismente.push(`${b.id}: ${fara.length} din ${b.niveluri.length} niveluri încă fără itemi`);
}
// evenimente (jocul live)
for (const cale of ['public/content/evenimente/expeditia-polara.json', 'public/content/evenimente/patrula-verde.json']) {
  const txt = readFileSync(new URL('../' + cale, import.meta.url), 'utf-8');
  if (CEDILE.test(txt)) erori.push(`${cale}: conține ş/ţ cu sedilă`);
  for (const it of JSON.parse(txt).itemi) {
    if (!['alegere', 'denumeste', 'pin', 'grafic'].includes(it.tip)) erori.push(`${it.id}: tipul ${it.tip} nu merge în jocul live`);
    if (!it.clase?.length) erori.push(`${it.id}: lipsesc clasele`);
    for (const k of it.competente) if (!Object.values(comp).some((c) => typeof c === 'object' && c[k])) erori.push(`${it.id}: competență inexistentă ${k}`);
    if (it.date.variante && new Set(it.date.variante).size !== it.date.variante.length) erori.push(`${it.id}: variante duplicate`);
    if (ids.has(it.id)) erori.push(`${it.id}: id duplicat`);
    ids.add(it.id);
  }
}
for (const [n, l] of peNivel) {
  const niv = nivCal.get(n);
  if (niv?.tip === 'nivel' && l.length < 30) avertismente.push(`${n}: ${l.length} itemi (ținta: 30)`);
  if (niv?.tip === 'nivel' && l.length < 12) erori.push(`${n}: doar ${l.length} itemi (minimum 12)`);
  if (niv?.tip === 'nivel' && new Set(l.map((x) => x.dificultate)).size < 3) erori.push(`${n}: nu are toate cele 3 dificultăți`);
}
for (const i of insigne) for (const n of i.conditie.niveluri ?? []) if (!nivCal.has(n)) erori.push(`insigna ${i.id}: nivel inexistent ${n}`);

// tabelul de acoperire: competență → niveluri → număr de itemi → săptămâni
let md = '# Acoperirea competențelor specifice\n\nGenerat automat de `npm run check-content`. Coloana „În planificare” arată săptămânile în care competența apare în planificarea calendaristică; „Itemi” arată câți itemi din aplicație o exersează acum.\n';
for (const clasa of [5, 6, 7, 8]) {
  md += `\n## Clasa a ${({ 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' })[clasa]}-a\n\n| Competența | În planificare (săptămâni) | Niveluri cu itemi | Itemi |\n| --- | --- | --- | --- |\n`;
  for (const [cod, text] of Object.entries(comp[String(clasa)])) {
    const sapt = cal.planificare.filter((p) => p.clasa === clasa && p.competente.includes(cod)).map((p) => p.saptamana);
    const its = itemiToti.filter((i) => i.competente.includes(cod));
    const sNiv = its.map((i) => nivCal.get(i.nivel)?.saptamana);
    const niv = [...new Set(sNiv.filter((x) => x !== undefined))].sort((a, b) => a - b).map((s) => `S${s}`).concat(sNiv.includes(undefined) ? ['Busola (T₀)'] : []);
    md += `| **${cod}** ${text} | ${compact(sapt)} | ${niv.join(', ') || '—'} | ${its.length || '—'} |\n`;
  }
}
function compact(a) {
  if (!a.length) return '—';
  const out = []; let s = a[0], p = a[0];
  for (const x of a.slice(1).concat([null])) { if (x === p + 1) { p = x; continue; } out.push(s === p ? `S${s}` : `S${s}–${p}`); s = p = x; }
  return out.join(', ');
}
writeFileSync(new URL('../docs/acoperire-competente.md', import.meta.url), md);

console.log(`${itemiToti.length} itemi în ${peNivel.size} niveluri.`);
if (avertismente.length && process.argv.includes('--detalii')) console.log(avertismente.map((x) => '  · ' + x).join('\n'));
if (erori.length) { console.error(erori.map((x) => '  ✗ ' + x).join('\n')); process.exit(1); }
console.log('Conținut valid. Tabelul de acoperire: docs/acoperire-competente.md');
