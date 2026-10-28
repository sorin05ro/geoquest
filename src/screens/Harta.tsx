import { useLiveQuery } from 'dexie-react-hooks';
import { useEffect, useMemo, useState } from 'react';
import { useApp } from '../state';
import { citesteSetare, db } from '../db/db';
import { incarca } from '../content';
import { modENDisponibil, type ConfigEN } from '../game/recapitulare';
import { dataDeblocare, formatData, randuriClasa, saptamanaDeblocata, stareZi } from '../calendar/calendar';
import { Geo } from '../ui/Geo';
import { rang } from '../game/rules';
import type { Calendar, Clasa } from '../types';

const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };
export const LUMI: Record<Clasa, string> = {
  5: 'Lumea 1 · Terra, planeta noastră',
  6: 'Lumea 2 · Oameni și Europa',
  7: 'Lumea 3 · Continentele îndepărtate',
  8: 'Lumea 4 · România',
};

export interface Nod {
  id: string;
  tip: 'nivel' | 'expeditie' | 'boss' | 'busola' | 'mare-expeditie' | 'eveniment';
  titlu: string;
  sapt: number;
  unitate: string;
}

/** Nodurile hărții-aventură, în ordinea calendarului, grupate pe unități (regiuni). */
export function noduriClasa(cal: Calendar, clasa: Clasa): { unitate: string; noduri: Nod[] }[] {
  const R = ROMAN[clasa];
  const grupe: { unitate: string; noduri: Nod[] }[] = [];
  const titluNivel = new Map(cal.niveluri.map((n) => [n.id, n.titlu]));
  for (const r of randuriClasa(cal, clasa)) {
    if (r.eveniment) {
      const ev = cal.evenimente.find((e) => e.id === r.eveniment)!;
      const ultim = grupe.at(-1);
      if (ultim && !ultim.noduri.some((n) => n.id === `ev-${ev.id}`)) {
        ultim.noduri.push({ id: `ev-${ev.id}`, tip: 'eveniment', titlu: ev.nume ?? '', sapt: r.saptamana, unitate: ultim.unitate });
      }
      continue;
    }
    if (!r.unitate) continue;
    let g = grupe.at(-1);
    const cheie = r.unitate.replace(/\s+/g, ' ');
    if (!g || g.unitate !== cheie) { g = { unitate: cheie, noduri: [] }; grupe.push(g); }
    if (r.tipEveniment.includes('busola')) g.noduri.push({ id: `${R}-T0`, tip: 'busola', titlu: 'Busola de start', sapt: r.saptamana, unitate: cheie });
    for (const id of r.niveluri) {
      const t = cal.niveluri.find((n) => n.id === id)!;
      g.noduri.push({ id, tip: t.tip, titlu: titluNivel.get(id) ?? id, sapt: r.saptamana, unitate: cheie });
    }
    if (r.test) {
      g.noduri.push({
        id: `${R}-${r.test}`, tip: r.test === 'Tf' ? 'mare-expeditie' : 'boss',
        titlu: r.test === 'Tf' ? 'Marea Expediție' : `Boss ${r.test.replace('T', 'T')}`, sapt: r.saptamana, unitate: cheie,
      });
    }
  }
  return grupe.filter((g) => g.noduri.length);
}

const scurt = (s: string, n = 26) => {
  const t = s.replace(/^Aplicații? practice?(\/studii de caz)?:\s*/i, 'Expediție: ').replace(/^Studiu de caz:\s*/i, 'Studiu: ');
  return t.length > n ? t.slice(0, n - 1).trimEnd() + '…' : t;
};

/** Contur de insulă determinist, cu curbe de nivel. */
function insula(cx: number, cy: number, rx: number, ry: number, seed: number, scala = 1) {
  const pts: string[] = [];
  const n = 14;
  for (let i = 0; i < n; i++) {
    const a = (i / n) * Math.PI * 2;
    const j = 1 + 0.12 * Math.sin(seed * 3.1 + i * 1.7) + 0.06 * Math.cos(seed + i * 2.9);
    pts.push(`${(cx + Math.cos(a) * rx * j * scala).toFixed(1)},${(cy + Math.sin(a) * ry * j * scala).toFixed(1)}`);
  }
  // curbă închisă netezită
  const p = pts.map((s) => s.split(',').map(Number));
  let d = `M${((p[0][0] + p[n - 1][0]) / 2).toFixed(1)},${((p[0][1] + p[n - 1][1]) / 2).toFixed(1)}`;
  for (let i = 0; i < n; i++) {
    const a = p[i], b = p[(i + 1) % n];
    d += ` Q${a[0]},${a[1]} ${((a[0] + b[0]) / 2).toFixed(1)},${((a[1] + b[1]) / 2).toFixed(1)}`;
  }
  return d + 'Z';
}

const FUNDAL = ['var(--campie-pal)', 'var(--podis-pal)', 'var(--campie-pal)', 'var(--podis-pal)'];
const CONTUR = ['var(--campie)', 'var(--podis)', 'var(--munte)', 'var(--campie)'];

export function Harta() {
  const { cal, profil, azi, deblocate, continut, mergi, xp, teme } = useApp();
  const rezultate = useLiveQuery(() => db.nivele.toArray(), [], []);
  const clasa = profil!.clasa;
  const grupe = useMemo(() => noduriClasa(cal, clasa), [cal, clasa]);
  const stare = stareZi(cal, clasa, azi);
  const sCurenta = saptamanaDeblocata(cal, clasa, azi);
  const [cfgEN, setCfgEN] = useState<{ cfg?: ConfigEN; supr: boolean | null }>({ supr: null });
  useEffect(() => {
    Promise.all([incarca<{ modEvaluareNationala?: ConfigEN }>('config/scoala.json').catch(() => ({} as { modEvaluareNationala?: ConfigEN })), citesteSetare<boolean | null>('modEN', null)])
      .then(([c, supr]) => setCfgEN({ cfg: c.modEvaluareNationala, supr }));
  }, []);
  const enDisponibil = modENDisponibil(clasa, cfgEN.cfg, sCurenta, cfgEN.supr, stare.tip === 'final');
  const steleDe = new Map(rezultate.map((r) => [r.nivel, r.stele]));
  const r = rang(xp);

  // geometria hărții: noduri în zigzag, insule în spatele fiecărei unități
  const W = 360, pas = 92;
  let y = 70;
  const layout = grupe.map((g, gi) => {
    const y0 = y;
    const noduri = g.noduri.map((n, i) => {
      const x = W / 2 + Math.sin((i + gi * 2) * 1.15) * 95;
      const pos = { ...n, x, y };
      y += pas;
      return pos;
    });
    const y1 = y - pas;
    y += 70;
    return { ...g, noduri, y0, y1, gi };
  });
  const H = y;
  const toate = layout.flatMap((g) => g.noduri);

  const statusNod = (n: Nod) => {
    if (n.tip === 'eveniment') return 'eveniment';
    const deblocat = n.tip === 'nivel' || n.tip === 'expeditie' ? deblocate.has(n.id) : n.sapt <= sCurenta;
    if (!deblocat) return 'ceata';
    if (steleDe.has(n.id)) return 'facut';
    const eTest = n.tip === 'boss' || n.tip === 'busola' || n.tip === 'mare-expeditie';
    const areContinut = eTest ? continut?.boss.some((b) => b.id === n.id) : continut?.niveluri.has(n.id);
    if (!areContinut) return 'pregatire';
    return n.sapt === sCurenta ? 'acum' : 'disponibil';
  };

  const deschide = (n: Nod) => {
    const s = statusNod(n);
    if (s === 'ceata' || s === 'eveniment' || s === 'pregatire') return;
    const eTest = n.tip === 'boss' || n.tip === 'busola' || n.tip === 'mare-expeditie';
    mergi(eTest ? { e: 'boss', id: n.id } : { e: 'nivel', id: n.id });
  };

  const mesajCalendar = (() => {
    switch (stare.tip) {
      case 'vacanta': return `${stare.nume}. Seria ta e în pauză. ${stare.urmatoarea ? `Ne vedem pe ${formatData(stare.urmatoarea.de)}.` : ''}`;
      case 'eveniment': return stare.eveniment === 'scoala-altfel' ? 'Săptămâna Școala Altfel: Expediția Polară.' : 'Săptămâna verde: Patrula Verde.';
      case 'inainte': return `Anul școlar începe pe ${formatData(stare.urmatoarea.de)}.`;
      case 'final': return 'Anul școlar s-a încheiat. Toată lumea e deschisă pentru recapitulare.';
      case 'curs': return stare.ziLibera ? `Azi e zi liberă: ${stare.ziLibera}.` : `Săptămâna ${stare.saptamana.nr} din 36.`;
      case 'weekend': return `Weekend. Săptămâna ${stare.saptamana.nr} rămâne deschisă.`;
    }
  })();

  return (
    <div className="stiva">
      <div className="rand" style={{ justifyContent: 'space-between' }}>
        <div>
          <h1 style={{ marginBottom: 2 }}>{LUMI[clasa]}</h1>
          <p className="eticheta-mica" style={{ margin: 0 }}>{mesajCalendar}</p>
        </div>
        <button className="rand card" style={{ padding: '8px 14px', border: 0, cursor: 'pointer' }} onClick={() => mergi({ e: 'profil' })}
          aria-label={`Rangul tău: ${r.nume}, ${xp} XP. Deschide profilul.`}>
          <span style={{ fontSize: 28 }} aria-hidden="true">{profil!.avatar}</span>
          <span style={{ textAlign: 'left' }}><b>{r.nume}</b><br /><span className="eticheta-mica">{xp} XP</span></span>
        </button>
      </div>

      <button className="misiune" onClick={() => mergi({ e: 'misiune' })}>
        <Geo />
        <span>
          <b>Misiunea zilei</b><br />
          <span className="eticheta-mica">3–5 minute: lecția săptămânii și ce ai greșit data trecută.</span>
        </span>
      </button>

      {enDisponibil && (
        <button className="misiune" style={{ borderLeft: '6px solid var(--munte)' }} onClick={() => mergi({ e: 'recapitulare' })}>
          <span aria-hidden="true" style={{ fontSize: 40 }}>🎓</span>
          <span>
            <b>Recapitulare pentru Evaluarea Națională</b><br />
            <span className="eticheta-mica">Toată geografia României, pe unități, cu test de recapitulare.</span>
          </span>
        </button>
      )}

      {teme.filter((t) => t.clasa === clasa && t.termen >= azi).map((t) => {
        const gata = t.niveluri.filter((n) => steleDe.has(n)).length;
        const urm = t.niveluri.find((n) => !steleDe.has(n) && continut?.niveluri.has(n));
        return (
          <div key={t.id} className="card rand" style={{ justifyContent: 'space-between', borderLeft: '6px solid var(--podis)' }}>
            <div>
              <b>Temă: {t.titlu}</b><br />
              <span className="eticheta-mica">până pe {formatData(t.termen)} · {gata} din {t.niveluri.length} lecții terminate</span>
            </div>
            {urm ? <button className="buton mic" onClick={() => mergi({ e: 'nivel', id: urm })}>Continuă tema</button> : <span className="stampila" style={{ width: 56, height: 56, fontSize: 10 }}>GATA</span>}
          </div>
        );
      })}

      <div className="harta-aventura">
        <svg viewBox={`0 0 ${W} ${H}`} role="group" aria-label={`Harta-aventură: ${grupe.length} regiuni`}>
          <defs>
            <pattern id="ceata" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
              <rect width="10" height="10" fill="var(--ceata)" /><line x1="0" y1="0" x2="0" y2="10" stroke="var(--hartie)" strokeWidth="3" opacity=".5" />
            </pattern>
          </defs>
          {layout.map((g) => {
            const cy = (g.y0 + g.y1) / 2;
            const ry = (g.y1 - g.y0) / 2 + 58;
            const parcurs = g.noduri.some((n) => statusNod(n) !== 'ceata');
            return (
              <g key={g.unitate} opacity={parcurs ? 1 : 0.6}>
                <path d={insula(W / 2, cy, 165, ry, g.gi + 1)} fill={parcurs ? FUNDAL[g.gi % 4] : 'url(#ceata)'} />
                {[0.82, 0.62].map((s) => (
                  <path key={s} d={insula(W / 2, cy, 165, ry, g.gi + 1, s)} fill="none" stroke={CONTUR[g.gi % 4]} strokeWidth="1.2" opacity=".55" />
                ))}
                <text x="16" y={g.y0 - 34} className="regiune-eticheta" fontSize="15">{scurt(g.unitate, 40)}</text>
              </g>
            );
          })}
          <path
            d={toate.map((n, i) => `${i ? 'L' : 'M'}${n.x.toFixed(1)} ${n.y}`).join(' ')}
            fill="none" stroke="var(--mare)" strokeWidth="3" strokeDasharray="2 9" strokeLinecap="round" opacity=".6"
          />
          {toate.map((n) => {
            const s = statusNod(n);
            const st = steleDe.get(n.id) ?? 0;
            const boss = n.tip === 'boss' || n.tip === 'mare-expeditie';
            const r0 = boss ? 30 : n.tip === 'eveniment' ? 20 : 26;
            const fill = s === 'facut' ? 'var(--campie)' : s === 'ceata' ? 'var(--ceata)' : s === 'eveniment' ? 'var(--podis)' : 'var(--suprafata)';
            const stroke = s === 'acum' ? 'var(--pion)' : boss ? 'var(--munte)' : 'var(--mare)';
            const data = dataDeblocare(cal, n.sapt);
            const desc = s === 'ceata' ? `în ceață, se deschide pe ${data ? formatData(data) : ''}`
              : s === 'facut' ? `terminat, ${st} stele` : s === 'pregatire' ? 'conținut în pregătire' : s === 'acum' ? 'lecția săptămânii' : 'deschis';
            const simbol = n.tip === 'expeditie' ? '⛺' : n.tip === 'boss' ? '⚔' : n.tip === 'mare-expeditie' ? '🏁' : n.tip === 'busola' ? '🧭' : n.tip === 'eveniment' ? '★' : '';
            const clic = s !== 'ceata' && s !== 'eveniment' && s !== 'pregatire';
            return (
              <g
                key={n.id} className={clic ? 'nod' : 'nod-ceata'} role={clic ? 'button' : 'img'} tabIndex={clic ? 0 : -1}
                aria-label={`S${n.sapt}: ${n.titlu}, ${desc}`}
                onClick={() => deschide(n)} onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && (e.preventDefault(), deschide(n))}
              >
                {s === 'acum' && <circle cx={n.x} cy={n.y} r={r0 + 9} fill="none" stroke="var(--pion)" strokeWidth="3" strokeDasharray="4 5" />}
                <circle className="nod-cerc" cx={n.x} cy={n.y} r={r0} fill={fill} stroke={stroke} strokeWidth={s === 'pregatire' ? 2 : 3.5}
                  strokeDasharray={s === 'ceata' || s === 'pregatire' ? '5 5' : undefined} />
                <text x={n.x} y={n.y + 7} textAnchor="middle" fontSize={simbol ? 20 : 15} fontWeight="700"
                  fill={s === 'facut' ? 'var(--hartie)' : 'var(--text)'}>{simbol || `S${n.sapt}`}</text>
                {(() => {
                  const stanga = n.x > W / 2;
                  const tx = stanga ? n.x - r0 - 8 : n.x + r0 + 8;
                  const loc = stanga ? tx - 6 : W - tx - 6;
                  const max = Math.max(8, Math.floor(loc / 7.2));
                  const sub = s === 'facut' ? '★'.repeat(st) + '☆'.repeat(3 - st) : s === 'ceata' && data ? `din ${formatData(data).replace(/ \d{4}$/, '')}` : s === 'pregatire' ? 'în pregătire' : s === 'eveniment' ? `S${n.sapt}` : '';
                  const st2 = { paintOrder: 'stroke' as const, stroke: 'var(--apa)', strokeWidth: 4 };
                  return (
                    <>
                      <text x={tx} y={n.y - 2} textAnchor={stanga ? 'end' : 'start'} fontSize="12.5" fontWeight="700" fill="var(--text)" style={st2}>{scurt(n.titlu, max)}</text>
                      <text x={tx} y={n.y + 15} textAnchor={stanga ? 'end' : 'start'} fontSize="11.5" fill="var(--text-2)" style={st2}>{sub}</text>
                    </>
                  );
                })()}
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}
