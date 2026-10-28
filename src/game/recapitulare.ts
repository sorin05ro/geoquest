import type { Item, Raspuns } from '../types';

/** Configurația modului de recapitulare pentru Evaluarea Națională (din public/config/scoala.json). */
export interface ConfigEN {
  activ: boolean;
  deLaSaptamana: number;
}

/**
 * Modul e disponibil doar la clasa a VIII-a, dacă e activ (în configurație sau pornit de profesor pe acest dispozitiv)
 * și dacă s-a ajuns la săptămâna stabilită. După încheierea anului rămâne deschis.
 */
export function modENDisponibil(clasa: number, cfg: ConfigEN | undefined, saptamana: number, suprascriere?: boolean | null, anTerminat = false): boolean {
  if (clasa !== 8) return false;
  const activ = suprascriere ?? cfg?.activ ?? false;
  if (!activ) return false;
  return anTerminat || saptamana >= (cfg?.deLaSaptamana ?? 28);
}

export interface StareItem {
  incercari: number;
  ultimulCorect: boolean | null;
}

/** Ultima stare a fiecărui item, din istoricul răspunsurilor (cel mai recent răspuns contează). */
export function stareItemi(raspunsuri: Raspuns[]): Map<string, StareItem> {
  const m = new Map<string, StareItem>();
  const sortate = [...raspunsuri].sort((a, b) => (a.data < b.data ? -1 : a.data > b.data ? 1 : (a.id ?? 0) - (b.id ?? 0)));
  for (const r of sortate) {
    const s = m.get(r.item) ?? { incercari: 0, ultimulCorect: null };
    s.incercari += 1;
    s.ultimulCorect = r.corect;
    m.set(r.item, s);
  }
  return m;
}

/**
 * Cât de bine stăpânește elevul un grup de itemi, între 0 și 1:
 * itemii rezolvați corect ultima dată / toți itemii grupului. Itemii neîncercați trag media în jos.
 */
export function stapanire(itemi: Item[], stare: Map<string, StareItem>): number {
  if (!itemi.length) return 0;
  return itemi.filter((i) => stare.get(i.id)?.ultimulCorect === true).length / itemi.length;
}

/**
 * Alege itemii unei recapitulări: întâi cei greșiți ultima dată, apoi cei neîncercați, apoi cei știuți,
 * fiecare grup amestecat. Dacă e dat `peGrup`, încearcă să ia itemi din cât mai multe niveluri.
 */
export function alegeRecapitulare(itemi: Item[], stare: Map<string, StareItem>, cate: number, amesteca: <T>(a: T[]) => T[]): Item[] {
  const gresiti = amesteca(itemi.filter((i) => stare.get(i.id)?.ultimulCorect === false));
  const noi = amesteca(itemi.filter((i) => !stare.has(i.id)));
  const stiuti = amesteca(itemi.filter((i) => stare.get(i.id)?.ultimulCorect === true));
  const ordine = [...gresiti, ...noi, ...stiuti];
  // împrăștie pe niveluri: o trecere cu câte un item pe nivel, apoi restul
  const ales: Item[] = [];
  const folositeNiv = new Set<string>();
  for (const i of ordine) if (ales.length < cate && !folositeNiv.has(i.nivel)) { ales.push(i); folositeNiv.add(i.nivel); }
  for (const i of ordine) if (ales.length < cate && !ales.includes(i)) ales.push(i);
  return ales;
}

/** Nota orientativă a unui test de recapitulare (scala 1–10, cu un punct din oficiu), ca la evaluările școlare. */
export function notaOrientativa(corecte: number, total: number): number {
  if (!total) return 1;
  return Math.round((1 + (9 * corecte) / total) * 100) / 100;
}
