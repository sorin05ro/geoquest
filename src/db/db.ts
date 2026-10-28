import Dexie, { type Table } from 'dexie';
import type { ClasaProfesor, CutieLeitner, EvenimentXP, IntrareJurnal, Item, Profil, Raport, Raspuns, RezultatNivel, Tema } from '../types';

/** Toate datele stau doar pe acest dispozitiv (IndexedDB). Rapoartele ajung la profesor doar când elevul le trimite. */
export class GeoDB extends Dexie {
  profil!: Table<Profil, string>;
  nivele!: Table<RezultatNivel, string>;
  raspunsuri!: Table<Raspuns, number>;
  leitner!: Table<CutieLeitner, string>;
  xp!: Table<EvenimentXP, number>;
  jurnal!: Table<IntrareJurnal, number>;
  setari!: Table<{ cheie: string; valoare: unknown }, string>;
  // elev: temele primite; profesor: clasele, rapoartele colectate și itemii creați în editor
  teme!: Table<Tema, string>;
  clase!: Table<ClasaProfesor, string>;
  rapoarte!: Table<Raport, number>;
  itemiProfesor!: Table<Item & { clasa: number }, string>;

  constructor() {
    super('geoquest');
    this.version(1).stores({
      profil: 'id',
      nivele: 'nivel',
      raspunsuri: '++id, item, nivel, data',
      leitner: 'item, urmatoarea',
      xp: '++id, data',
      jurnal: '++id, nivel',
      setari: 'cheie',
    });
    this.version(2).stores({
      teme: 'id, termen',
      clase: 'cod, clasa',
      rapoarte: '++id, cod, clasa, [cod+porecla]',
      itemiProfesor: 'id, clasa, nivel',
    });
  }
}

export const db = new GeoDB();

export async function citesteSetare<T>(cheie: string, implicit: T): Promise<T> {
  const r = await db.setari.get(cheie);
  return (r?.valoare as T) ?? implicit;
}

export async function scrieSetare(cheie: string, valoare: unknown) {
  await db.setari.put({ cheie, valoare });
}

export async function totalXP(): Promise<number> {
  let s = 0;
  await db.xp.each((e) => { s += e.xp; });
  return s;
}

export async function adaugaXP(xp: number, motiv: string, data: string) {
  if (xp > 0) await db.xp.add({ xp, motiv, data });
}

/** Șterge tot progresul de pe acest dispozitiv (cerut la final de an sau la schimbarea elevului). */
export async function stergeTot() {
  await db.delete();
  location.reload();
}
