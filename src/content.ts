import type { Calendar, Clasa, ContinutNivel, FisierContinut, IndexContinut, Item } from './types';
import type { Insigna } from './game/rules';
import { db } from './db/db';

const BASE = import.meta.env.BASE_URL;
const cache = new Map<string, Promise<unknown>>();

export function incarca<T>(cale: string): Promise<T> {
  if (!cache.has(cale)) {
    cache.set(cale, fetch(BASE + cale).then((r) => {
      if (!r.ok) throw new Error(`Nu am putut încărca ${cale} (${r.status})`);
      return r.json();
    }));
  }
  return cache.get(cale) as Promise<T>;
}

export const incarcaCalendar = () => incarca<Calendar>('calendar/2026-2027.json');
export const incarcaCompetente = () => incarca<Record<string, Record<string, string>>>('content/competente.json');
export const incarcaInsigne = () => incarca<{ insigne: Insigna[] }>('content/insigne.json').then((x) => x.insigne);

export interface ConfigScoala {
  scoala: string;
  localitate: string;
  judet: string;
  clase: { clasa: Clasa; litere: string[]; manual: string }[];
  modEvaluareNationala: { activ: boolean; deLaSaptamana: number };
  clasamentIndividual: boolean;
}
export const incarcaScoala = () => incarca<ConfigScoala>('config/scoala.json');

/** Nivel minimal pentru lecțiile care au doar itemi creați de profesor. */
export function nivelMinimal(n: { id: string; titlu: string; tip: 'nivel' | 'expeditie' }): ContinutNivel {
  return {
    id: n.id, tip: 'nivel', titlu: n.titlu,
    descopera: { intrebare: `Ce îți amintești din lecția „${n.titlu}”?` },
    invata: [{ titlu: n.titlu, text: 'Exercițiile acestui nivel au fost pregătite de profesorul tău, pentru lecția de la clasă. Recitește notițele, apoi exersează.' }],
  };
}

/**
 * Tot conținutul unei clase: fișierele publicate, apoi `profesor.json` (dacă există, publicat din editor)
 * și itemii creați în editor pe acest dispozitiv.
 */
export async function continutClasa(clasa: Clasa) {
  const niveluri = new Map<string, ContinutNivel>();
  const itemi = new Map<string, Item>();
  const boss: NonNullable<FisierContinut['boss']> = [];
  const adauga = (f: FisierContinut) => {
    f.niveluri.forEach((n) => niveluri.set(n.id, n));
    f.itemi.forEach((i) => itemi.set(i.id, i));
    boss.push(...(f.boss ?? []));
  };
  try {
    const index = await incarca<IndexContinut>(`content/clasa-${clasa}/index.json`);
    (await Promise.all(index.fisiere.map((f) => incarca<FisierContinut>(`content/clasa-${clasa}/${f.fisier}`)))).forEach(adauga);
  } catch { /* clasa nu are încă fișiere publicate */ }
  try { adauga(await incarca<FisierContinut>(`content/clasa-${clasa}/profesor.json`)); } catch { /* opțional */ }
  try {
    const locali = await db.itemiProfesor.where('clasa').equals(clasa).toArray();
    if (locali.length) {
      const cal = await incarcaCalendar();
      for (const it of locali) {
        const { clasa: _c, ...item } = it; // eslint-disable-line @typescript-eslint/no-unused-vars
        itemi.set(item.id, item as Item);
        if (!niveluri.has(item.nivel)) {
          const nc = cal.niveluri.find((n) => n.id === item.nivel);
          if (nc) niveluri.set(nc.id, nivelMinimal(nc));
        }
      }
    }
  } catch { /* fără IndexedDB (de exemplu, în teste) */ }
  return { niveluri, itemi, boss };
}

export type ContinutIncarcat = Awaited<ReturnType<typeof continutClasa>>;

export function itemiNivel(c: ContinutIncarcat, nivel: string): Item[] {
  return [...c.itemi.values()].filter((i) => i.nivel === nivel);
}

/** Amestecă determinist (pentru teste) sau aleator. */
export function amesteca<T>(arr: T[], seed?: number): T[] {
  const a = [...arr];
  let s = seed ?? Math.floor(Math.random() * 1e9);
  const rnd = () => ((s = (s * 1103515245 + 12345) % 2147483648) / 2147483648);
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
