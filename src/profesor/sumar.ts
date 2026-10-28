// Funcții fără stare pentru modul profesor: rezumatul progresului, codurile de clasă, linkurile de temă, exportul CSV.

import type { Clasa, Raport, Raspuns, RezultatNivel, SumarProgres, Tema } from '../types';

/** Rezumatul trimis de elev. `competenteItem` leagă fiecare item de competențele lui. */
export function construiesteSumar(
  raspunsuri: Raspuns[], nivele: RezultatNivel[], competenteItem: Map<string, string[]>, teme: Tema[], xp: number,
): SumarProgres {
  const competente: SumarProgres['competente'] = {};
  const greseli: SumarProgres['greseli'] = {};
  for (const r of raspunsuri) {
    for (const c of competenteItem.get(r.item) ?? []) {
      competente[c] ??= { c: 0, t: 0 };
      competente[c].t++;
      if (r.corect) competente[c].c++;
    }
    if (!r.corect) greseli[r.item] = (greseli[r.item] ?? 0) + 1;
  }
  const niveluri: SumarProgres['niveluri'] = {};
  for (const n of nivele) niveluri[n.nivel] = { stele: n.stele, scor: Math.round(n.scor * 100) / 100 };
  const temeOut: SumarProgres['teme'] = {};
  for (const t of teme) temeOut[t.id] = t.niveluri.filter((n) => niveluri[n]).length;
  const ultima = raspunsuri.reduce<string | null>((m, r) => (!m || r.data > m ? r.data : m), null);
  return { xp, niveluri, competente, greseli, teme: temeOut, ultimaActivitate: ultima, raspunsuri: raspunsuri.length };
}

// ---------------------------------------------------------------- coduri de clasă

const ALFABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // fără 0/O și 1/I, ușor de citit de pe tablă

export function codClasaNou(clasa: Clasa, litera: string, rnd: () => number = Math.random): string {
  let s = '';
  for (let i = 0; i < 4; i++) s += ALFABET[Math.floor(rnd() * ALFABET.length)];
  return `${clasa}${litera || ''}-${s}`;
}

/** „5A-K7QM” → { clasa: 5, litera: 'A' }. Întoarce null dacă nu arată ca un cod de clasă. */
export function citesteCodClasa(cod: string): { clasa: Clasa; litera: string } | null {
  const m = cod.trim().toUpperCase().match(/^([5-8])([A-Z]?)-([A-Z2-9]{4})$/);
  return m ? { clasa: Number(m[1]) as Clasa, litera: m[2] } : null;
}

// ---------------------------------------------------------------- teme prin link

function b64url(s: string) {
  const bytes = new TextEncoder().encode(s);
  let bin = '';
  bytes.forEach((b) => { bin += String.fromCharCode(b); });
  return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}
function dinB64url(s: string) {
  const bin = atob(s.replace(/-/g, '+').replace(/_/g, '/'));
  return new TextDecoder().decode(Uint8Array.from(bin, (c) => c.charCodeAt(0)));
}

export function codeazaTema(t: Tema): string {
  return b64url(JSON.stringify([t.id, t.titlu, t.clasa, t.cod ?? '', t.niveluri, t.termen, t.creat]));
}

export function decodeazaTema(s: string): Tema | null {
  try {
    const [id, titlu, clasa, cod, niveluri, termen, creat] = JSON.parse(dinB64url(s));
    if (typeof id !== 'string' || !Array.isArray(niveluri) || !/^\d{4}-\d{2}-\d{2}$/.test(termen)) return null;
    return { id, titlu: String(titlu).slice(0, 80), clasa, cod: cod || undefined, niveluri: niveluri.map(String).slice(0, 20), termen, creat };
  } catch { return null; }
}

// ---------------------------------------------------------------- panoul pe competențe

export interface RandPanou { porecla: string; avatar: string; cod: string; primit: string; xp: number; stele: number; terminate: number; procente: Record<string, number | null> }

/** Un rând pe elev (ultimul raport primit de la fiecare poreclă din clasă). */
export function randuriPanou(rapoarte: Raport[], competente: string[]): RandPanou[] {
  const ultim = new Map<string, Raport>();
  for (const r of rapoarte) {
    const k = `${r.cod}|${r.porecla}`;
    const v = ultim.get(k);
    if (!v || r.primit >= v.primit) ultim.set(k, r);
  }
  return [...ultim.values()].sort((a, b) => a.porecla.localeCompare(b.porecla, 'ro')).map((r) => ({
    porecla: r.porecla, avatar: r.avatar, cod: r.cod, primit: r.primit, xp: r.sumar.xp,
    stele: Object.values(r.sumar.niveluri).reduce((s, n) => s + n.stele, 0),
    terminate: Object.keys(r.sumar.niveluri).length,
    procente: Object.fromEntries(competente.map((c) => {
      const x = r.sumar.competente[c];
      return [c, x && x.t ? Math.round((x.c / x.t) * 100) : null];
    })),
  }));
}

export function celeMaiGresite(rapoarte: Raport[], n = 10): { item: string; elevi: number; greseli: number }[] {
  const m = new Map<string, { elevi: number; greseli: number }>();
  for (const r of rapoarte) for (const [item, g] of Object.entries(r.sumar.greseli)) {
    const x = m.get(item) ?? { elevi: 0, greseli: 0 };
    x.elevi++; x.greseli += g;
    m.set(item, x);
  }
  return [...m.entries()].map(([item, x]) => ({ item, ...x })).sort((a, b) => b.elevi - a.elevi || b.greseli - a.greseli).slice(0, n);
}

/** CSV cu „;” (Excel în română) și BOM, ca diacriticele să apară corect. */
export function csvPanou(randuri: RandPanou[], competente: string[], teste: string[], rapoarte: Raport[]): string {
  const esc = (v: unknown) => { const s = String(v ?? ''); return /[;"\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };
  const cap = ['Poreclă', 'Cod clasă', 'Raport primit', 'XP', 'Niveluri terminate', 'Stele', ...competente.map((c) => `${c} (%)`), ...teste.map((t) => `${t} (%)`)];
  const linii = randuri.map((r) => {
    const rap = rapoarte.filter((x) => x.porecla === r.porecla && x.cod === r.cod).sort((a, b) => b.primit.localeCompare(a.primit))[0];
    return [r.porecla, r.cod, r.primit, r.xp, r.terminate, r.stele,
      ...competente.map((c) => r.procente[c] ?? ''),
      ...teste.map((t) => { const s = rap?.sumar.niveluri[t]?.scor; return s === undefined ? '' : Math.round(s * 100); })];
  });
  return '﻿' + [cap, ...linii].map((l) => l.map(esc).join(';')).join('\r\n');
}
