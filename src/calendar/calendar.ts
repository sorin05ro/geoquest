import type { Calendar, Clasa, RandPlanificare, Saptamana } from '../types';

/** Data locală (Europe/Bucharest pe dispozitivul elevului) ca șir ISO YYYY-MM-DD. */
export function isoLocal(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const z = String(d.getDate()).padStart(2, '0');
  return `${y}-${m}-${z}`;
}

export type Stare =
  | { tip: 'inainte'; urmatoarea: Saptamana }
  | { tip: 'curs'; saptamana: Saptamana; ziLibera?: string }
  | { tip: 'weekend'; saptamana: Saptamana }
  | { tip: 'vacanta'; nume: string; ultima: Saptamana | null; urmatoarea: Saptamana | null }
  | { tip: 'eveniment'; saptamana: Saptamana; eveniment: string }
  | { tip: 'final'; ultima: Saptamana };

const cuprinde = (de: string, pana: string, zi: string) => de <= zi && zi <= pana;

/** Ultima zi de cursuri pentru o clasă (a VIII-a termină mai devreme). */
export function ultimaZi(cal: Calendar, clasa: Clasa): string {
  return cal.ultimaZi[String(clasa)] ?? cal.saptamani[cal.saptamani.length - 1].pana;
}

/** Săptămânile de curs ale unei clase (a VIII-a nu are S36). */
export function saptamaniClasa(cal: Calendar, clasa: Clasa): Saptamana[] {
  const fin = ultimaZi(cal, clasa);
  return cal.saptamani.filter((s) => s.de <= fin);
}

/** Starea calendarului pentru o zi și o clasă. */
export function stareZi(cal: Calendar, clasa: Clasa, zi: string): Stare {
  const sapt = saptamaniClasa(cal, clasa);
  const prima = sapt[0];
  const ultima = sapt[sapt.length - 1];
  if (zi < prima.de) return { tip: 'inainte', urmatoarea: prima };
  if (zi > ultimaZi(cal, clasa)) return { tip: 'final', ultima };

  const vac = cal.vacante.find((v) => cuprinde(v.de, v.pana, zi));
  if (vac) {
    const ult = [...sapt].reverse().find((s) => s.pana < zi) ?? null;
    const urm = sapt.find((s) => s.de > zi) ?? null;
    return { tip: 'vacanta', nume: vac.nume ?? 'Vacanță', ultima: ult, urmatoarea: urm };
  }
  // săptămâna curentă = ultima săptămână începută
  const curenta = [...sapt].reverse().find((s) => s.de <= zi)!;
  const ev = cal.evenimente.find((e) => cuprinde(e.de, e.pana, zi));
  if (ev && cuprinde(curenta.de, curenta.pana, zi)) {
    return { tip: 'eveniment', saptamana: curenta, eveniment: ev.id ?? '' };
  }
  if (cuprinde(curenta.de, curenta.pana, zi)) {
    const zl = cal.zileLibere.find((z) => z.data === zi);
    const weekendZi = new Date(zi + 'T12:00:00').getDay();
    if (weekendZi === 0 || weekendZi === 6) return { tip: 'weekend', saptamana: curenta };
    return { tip: 'curs', saptamana: curenta, ...(zl ? { ziLibera: zl.nume } : {}) };
  }
  return { tip: 'weekend', saptamana: curenta };
}

/** Numărul ultimei săptămâni deblocate (0 înainte de început). */
export function saptamanaDeblocata(cal: Calendar, clasa: Clasa, zi: string): number {
  const s = stareZi(cal, clasa, zi);
  switch (s.tip) {
    case 'inainte': return 0;
    case 'final': return s.ultima.nr;
    case 'vacanta': return s.ultima?.nr ?? 0;
    default: return s.saptamana.nr;
  }
}

/** E zi de școală? (pentru seria zilnică și repetarea spațiată) */
export function esteZiDeScoala(cal: Calendar, clasa: Clasa, zi: string): boolean {
  const s = stareZi(cal, clasa, zi);
  return (s.tip === 'curs' && !s.ziLibera) || s.tip === 'eveniment';
}

/** Adaugă n zile de școală la o dată (zilele fără școală nu se numără). */
export function adunaZileScoala(cal: Calendar, clasa: Clasa, zi: string, n: number): string {
  let d = new Date(zi + 'T12:00:00');
  let ramase = n;
  let paza = 0;
  while (ramase > 0 && paza < 400) {
    d = new Date(d.getTime() + 86400000);
    const iso = isoLocal(d);
    if (esteZiDeScoala(cal, clasa, iso)) ramase--;
    if (iso > ultimaZi(cal, clasa)) { ramase--; }
    paza++;
  }
  return isoLocal(d);
}

export interface Suprascrieri { deblocate: string[]; blocate: string[] }

/** Ce niveluri sunt deblocate pentru o clasă, la o dată, cu suprascrierile profesorului. */
export function niveluriDeblocate(cal: Calendar, clasa: Clasa, zi: string, supr?: Suprascrieri): Set<string> {
  const pana = saptamanaDeblocata(cal, clasa, zi);
  const ids = new Set<string>();
  for (const n of cal.niveluri) if (n.clasa === clasa && n.saptamana <= pana) ids.add(n.id);
  for (const id of supr?.deblocate ?? []) ids.add(id);
  for (const id of supr?.blocate ?? []) ids.delete(id);
  return ids;
}

export function randuriClasa(cal: Calendar, clasa: Clasa): RandPlanificare[] {
  return cal.planificare.filter((p) => p.clasa === clasa);
}

/** Data (ISO) la care se deblochează săptămâna nr. */
export function dataDeblocare(cal: Calendar, nr: number): string | undefined {
  return cal.saptamani.find((s) => s.nr === nr)?.de;
}

export function formatData(iso: string): string {
  const [y, m, d] = iso.split('-').map(Number);
  const luni = ['ian.', 'feb.', 'mar.', 'apr.', 'mai', 'iun.', 'iul.', 'aug.', 'sept.', 'oct.', 'nov.', 'dec.'];
  return `${d} ${luni.at(m - 1)} ${y}`;
}
