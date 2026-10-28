// Importul planificării calendaristice (.docx sau CSV) direct în aplicație.
// E aceeași logică ca în tools/import_planificare.py; testul import.test.ts verifică faptul că rezultatele coincid.

import { unzipSync, strFromU8 } from 'fflate';
import type { Calendar, Clasa, NivelCalendar, RandPlanificare, Saptamana, TipEveniment } from '../types';

export type Tabel = string[][]; // rânduri → celule (text, cu \n între paragrafe)

export interface StructuraAn {
  an: string;
  sursa?: string;
  intervale: Calendar['intervale'];
  vacante: Calendar['vacante'];
  zileLibere: Calendar['zileLibere'];
  evenimente: Calendar['evenimente'];
  ultimaZi: Record<string, string>;
}

export interface Corecturi { note?: string[]; competenteAdaugate?: Record<string, string[]> }

const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };
const CLASE: Clasa[] = [5, 6, 7, 8];

// ---------------------------------------------------------------- citirea fișierelor

const ENT: Record<string, string> = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'" };
const decod = (s: string) => s.replace(/&(amp|lt|gt|quot|apos);|&#(\d+);|&#x([0-9a-f]+);/gi, (_, e, d, h) => (e ? ENT[e] : String.fromCodePoint(d ? Number(d) : parseInt(h, 16))));

function textParagraf(p: string): string {
  let out = '';
  const re = /<w:t(?:\s[^>]*)?>([\s\S]*?)<\/w:t>|<w:br\b[^>]*\/>|<w:cr\b[^>]*\/>|<w:tab\b[^>]*\/>/g;
  for (let m = re.exec(p); m; m = re.exec(p)) {
    if (m[1] !== undefined) out += decod(m[1]);
    else if (m[0].startsWith('<w:tab')) out += '\t';
    else out += '\n';
  }
  return out;
}

/** Extrage tabelele din document.xml al unui .docx (fără bibliotecă de XML, ca să meargă și offline, și în teste). */
export function tabeleDinDocx(bytes: Uint8Array): Tabel[] {
  const fis = unzipSync(bytes, { filter: (f) => f.name === 'word/document.xml' });
  const xml = strFromU8(fis['word/document.xml']);
  const tabele: Tabel[] = [];
  for (const tbl of xml.match(/<w:tbl>[\s\S]*?<\/w:tbl>/g) ?? []) {
    const randuri: Tabel = [];
    for (const tr of tbl.match(/<w:tr[\s>][\s\S]*?<\/w:tr>/g) ?? []) {
      const celule = (tr.match(/<w:tc[\s>][\s\S]*?<\/w:tc>/g) ?? []).map((tc) =>
        (tc.match(/<w:p[\s>][\s\S]*?<\/w:p>|<w:p\/>/g) ?? []).map(textParagraf).join('\n').trim());
      randuri.push(celule);
    }
    tabele.push(randuri);
  }
  return tabele;
}

/** CSV cu „;”: clasa;unitate;competente;continuturi;ore;saptamana;evaluare. Conținuturile se despart cu „|”. */
export function tabeleDinCsv(text: string): Tabel[] {
  const linii = text.replace(/^﻿/, '').split(/\r?\n/).filter((l) => l.trim());
  const sep = linii[0].includes(';') ? ';' : ',';
  const parse = (l: string) => {
    const out: string[] = []; let cur = ''; let q = false;
    for (let i = 0; i < l.length; i++) {
      const ch = l[i];
      if (q) { if (ch === '"' && l[i + 1] === '"') { cur += '"'; i++; } else if (ch === '"') q = false; else cur += ch; }
      else if (ch === '"') q = true; else if (ch === sep) { out.push(cur); cur = ''; } else cur += ch;
    }
    out.push(cur);
    return out.map((x) => x.trim());
  };
  const cap = ['Unitatea de învățare', 'Competențe specifice', 'Conținuturi', 'Nr. ore alocate', 'Săptămâna', 'Observații/Evaluare'];
  const pe: Record<number, Tabel> = { 5: [cap], 6: [cap], 7: [cap], 8: [cap] };
  for (const l of linii.slice(1)) {
    const [clasa, unitate, comp, cont, ore, sapt, ev] = parse(l);
    const c = Number(clasa);
    if (!pe[c]) continue;
    pe[c].push([unitate, comp, (cont ?? '').split('|').map((x) => x.trim()).join('\n'), ore, sapt, (ev ?? '').split('|').map((x) => x.trim()).join('\n')]);
  }
  return CLASE.map((c) => pe[c]);
}

export const SABLON_CSV = '﻿clasa;unitate;competente;continuturi;ore;saptamana;evaluare\r\n'
  + '5;Terra – o planetă a Universului;1.1, 1.2, 2.1;Universul și Sistemul Solar | Terra – o planetă a Sistemului Solar;2;2 – 3;Evaluare orală\r\n'
  + '5;Terra – o planetă în mișcare;1.1 – 4.3;Globul geografic și harta;1;5;T₁ (test secvențial)\r\n';

// ---------------------------------------------------------------- utilitare (identice cu scriptul Python)

const zi = (s: string) => new Date(s + 'T12:00:00Z');
const iso = (d: Date) => d.toISOString().slice(0, 10);
const plus = (d: Date, n: number) => new Date(d.getTime() + n * 86400000);

export function construiesteSaptamani(an: StructuraAn): Saptamana[] {
  const out: Saptamana[] = [];
  let luni = zi(an.intervale[0].de);
  const fin = zi(an.intervale[an.intervale.length - 1].pana);
  let nr = 0;
  while (luni <= fin) {
    const zile = [0, 1, 2, 3, 4].map((i) => plus(luni, i));
    let interval: number | null = null;
    const curs: string[] = [];
    for (const z of zile) for (const iv of an.intervale) if (iv.de <= iso(z) && iso(z) <= iv.pana) { interval = iv.nr; curs.push(iso(z)); }
    if (curs.length) {
      nr++;
      const libere = an.zileLibere.filter((x) => curs.includes(x.data)).map((x) => x.data);
      out.push({ nr, de: curs[0], pana: curs[curs.length - 1], interval: interval!, zileCurs: curs.length - libere.length, zileLibere: libere });
    }
    luni = plus(luni, 7);
  }
  return out;
}

const STOP = new Set(['si', 'de', 'la', 'a', 'ale', 'al', 'in', 'pe', 'cu', 'unor', 'lor', 'ei', 'o', 'un']);
export function slugAscii(text: string, cuvinte = 4): string {
  const t = text.normalize('NFKD').replace(/[^\x00-\x7f]/g, '').replace(/[^a-zA-Z0-9 ]+/g, ' ').toLowerCase().split(/\s+/).filter((w) => w && !STOP.has(w));
  return t.slice(0, cuvinte).join('-') || 'nivel';
}

function listaCompetente(brut: string, clasa: Clasa, competente: Record<string, Record<string, string>>): string[] {
  const raw = brut.replace(/[–—]/g, '-');
  const toate = Object.keys(competente[String(clasa)]).map((k) => k.split('-')[1].split('.').map(Number) as [number, number]);
  const cmp = (a: [number, number], b: [number, number]) => a[0] - b[0] || a[1] - b[1];
  const out: [number, number][] = [];
  const re = /(\d)\.(\d)\.?\s*(?:-\s*(\d)\.(\d)\.?)?/g;
  for (let m = re.exec(raw); m; m = re.exec(raw)) {
    const a: [number, number] = [Number(m[1]), Number(m[2])];
    if (m[3] === undefined) out.push(a);
    else { const b: [number, number] = [Number(m[3]), Number(m[4])]; out.push(...toate.filter((c) => cmp(a, c) <= 0 && cmp(c, b) <= 0)); }
  }
  const vazut = new Set<string>();
  return out.map(([x, y]) => `${ROMAN[clasa]}-${x}.${y}`).filter((k) => (vazut.has(k) ? false : (vazut.add(k), true)));
}

const COD_EVAL: [string, string][] = [
  ['T₀', 'T0'], ['T₁', 'T1'], ['T₂', 'T2'], ['T₃', 'T3'], ['T₄', 'T4'], ['T₅', 'T5'], ['Tf', 'Tf'],
  ['Probe practice', 'PP'], ['Evaluare orală', 'EO'], ['Portofoliu', 'P'],
  ['Autoevaluare/Interevaluare', 'AE/IE'], ['Autoevaluare', 'AE'], ['Interevaluare', 'IE'],
  ['Consolidare', 'C'], ['Probă scrisă', 'PS'],
];
function coduriEvaluare(brut: string): string[] {
  const raw = brut.replace('Autoevaluare/ / Interevaluare', 'Autoevaluare/Interevaluare');
  const out: string[] = [];
  for (const [ac, cod] of COD_EVAL) {
    if (!raw.includes(ac)) continue;
    if ((cod === 'AE' || cod === 'IE') && out.includes('AE/IE')) continue;
    out.push(cod);
  }
  return out;
}

interface RandBrut { unitate: string; competenteBrut: string; continuturi: string[]; ore: number; saptamani: number[]; evaluareBrut: string }

function randuriTabel(t: Tabel): RandBrut[] {
  const out: RandBrut[] = [];
  for (const c of t.slice(1)) {
    if (c.length < 6 || !/\d/.test(c[4])) continue;
    const [unit, comp, cont, ore, sapt, ev] = c;
    const nums = (sapt.match(/\d+/g) ?? []).map(Number);
    out.push({
      unitate: unit.replace(/\n/g, ' ').replace(/\s+/g, ' ').trim(),
      competenteBrut: comp.replace(/\n/g, ' / '),
      continuturi: cont.split('\n').filter((x) => x.trim()).map((x) => x.replace(/\s+/g, ' ').trim()),
      ore: Number((ore.match(/\d+/) ?? ['0'])[0]),
      saptamani: nums.length ? Array.from({ length: nums[nums.length - 1] - nums[0] + 1 }, (_, i) => nums[0] + i) : [],
      evaluareBrut: ev.replace(/\n/g, ' / '),
    });
  }
  return out;
}

/** Generează calendarul (aceeași structură ca public/calendar/2026-2027.json) din tabelele planificării, câte unul pe clasă (V–VIII). */
export function genereazaCalendar(tabele: Tabel[], an: StructuraAn, competente: Record<string, Record<string, string>>, corecturi: Corecturi = {}, din = 'planificare'): Calendar {
  const saptamani = construiesteSaptamani(an);
  const peNr = new Map(saptamani.map((s) => [s.nr, s]));
  const probleme: string[] = [];
  const planificare: RandPlanificare[] = [];
  const niveluri: NivelCalendar[] = [];

  CLASE.forEach((clasa, ti) => {
    const t = tabele[ti];
    if (!t) return;
    const R = ROMAN[clasa];
    const ultima = an.ultimaZi[String(clasa)];
    for (const row of randuriTabel(t)) {
      let comps = listaCompetente(row.competenteBrut, clasa, competente);
      const valide = new Set(Object.keys(competente[String(clasa)]));
      for (const b of comps.filter((c) => !valide.has(c))) probleme.push(`Clasa ${R}, S${row.saptamani[0]}: competența ${b} nu există în programă; eliminată.`);
      comps = comps.filter((c) => valide.has(c));
      for (const c of corecturi.competenteAdaugate?.[`${clasa}:${row.saptamani[0]}`] ?? []) if (!comps.includes(c)) comps.push(c);
      comps.sort((a, b) => { const [x, y] = a.split('-')[1].split('.').map(Number); const [u, v] = b.split('-')[1].split('.').map(Number); return x - u || y - v; });

      const sapt = row.saptamani.filter((s) => peNr.has(s) && peNr.get(s)!.de <= ultima);
      const coduri = coduriEvaluare(row.evaluareBrut);
      const ePP = coduri.includes('PP');
      type Fel = 'portal' | 'recapitulare' | 'expeditie' | 'nivel';
      const elemente: [Fel, string][] = row.continuturi.map((c) => {
        const low = c.toLowerCase();
        const ultimul = low.split(/\s+/).at(-1);
        if (low.includes('(recapitulare)') || low.endsWith('- recapitulare') || ultimul === 'recapitulare') return ['portal', c];
        if (low.startsWith('recapitulare')) return ['recapitulare', c];
        if (ePP || low.startsWith('aplica') || low.startsWith('studiu de caz')) return ['expeditie', c];
        return ['nivel', c];
      });
      const lectii = elemente.filter(([k]) => k !== 'recapitulare');
      const recap = elemente.filter(([k]) => k === 'recapitulare');
      const n = lectii.length, nw = sapt.length;
      const plasate: [number | null, Fel, string][] = lectii.map(([k, c], i) => [nw ? sapt[Math.min(nw - 1, Math.floor((i * nw) / n))] : null, k, c]);
      for (const [k, c] of recap) plasate.push([nw ? sapt[nw - 1] : null, k, c]);

      for (const s of sapt) {
        const aici = plasate.filter(([w]) => w === s).map(([, k, c]) => [k, c] as [Fel, string]);
        const ev: TipEveniment[] = [];
        if (s === sapt[0] && coduri.includes('T0')) ev.push('busola');
        for (const [k] of aici) if ((k === 'portal' || k === 'expeditie') && !ev.includes(k)) ev.push(k);
        if (s === sapt[nw - 1]) {
          for (const c of ['T1', 'T2', 'T3', 'T4', 'T5']) if (coduri.includes(c)) ev.push('boss');
          if (coduri.includes('Tf')) ev.push('mare-expeditie');
        }
        const ids: string[] = [];
        for (const [k, c] of aici) {
          if (k !== 'nivel' && k !== 'expeditie') continue;
          const id = `${R}-S${String(s).padStart(2, '0')}-${slugAscii(c)}`;
          ids.push(id);
          niveluri.push({ id, clasa, saptamana: s, unitate: row.unitate, titlu: c, tip: k === 'expeditie' ? 'expeditie' : 'nivel', competente: comps });
        }
        const test = ['T1', 'T2', 'T3', 'T4', 'T5', 'Tf'].find((c) => coduri.includes(c));
        planificare.push({
          clasa, saptamana: s, interval: peNr.get(s)!.interval, unitate: row.unitate,
          continuturi: aici.map(([, c]) => c), niveluri: ids, competente: comps,
          ore: row.saptamani.length ? Math.floor(row.ore / row.saptamani.length) : row.ore,
          evaluare: coduri,
          tipEveniment: ev.length ? ev : aici.some(([k]) => k === 'recapitulare') ? ['recapitulare'] : aici.length ? ['nivel'] : ['continuare'],
          ...(test && s === sapt[nw - 1] ? { test } : {}),
        });
      }
    }
  });

  const acoperite = new Set(planificare.map((p) => `${p.clasa}:${p.saptamana}`));
  for (const clasa of CLASE) {
    for (const w of saptamani) {
      if (w.de > an.ultimaZi[String(clasa)] || acoperite.has(`${clasa}:${w.nr}`)) continue;
      const ev = an.evenimente.find((e) => e.de <= w.pana && e.pana >= w.de);
      planificare.push({
        clasa, saptamana: w.nr, interval: w.interval, unitate: null, continuturi: [], niveluri: [], competente: [], ore: 0, evaluare: [],
        tipEveniment: ev ? ['eveniment'] : ['fara-ore'], ...(ev ? { eveniment: ev.id } : {}),
      });
    }
  }
  planificare.sort((a, b) => a.clasa - b.clasa || a.saptamana - b.saptamana);
  for (const w of saptamani) {
    if (w.zileCurs < 5) probleme.push(`S${w.nr} (${w.de} – ${w.pana}): doar ${w.zileCurs} zile de curs (${w.zileLibere.length ? 'zi liberă legală' : 'săptămână incompletă'}).`);
  }
  return {
    ...an, saptamani, planificare, niveluri, observatii: probleme,
    ...({ generat: { din, corecturi: corecturi.note ?? [] } } as object),
  } as Calendar;
}
