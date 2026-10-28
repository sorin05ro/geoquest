// Protocolul jocului live. Gazda (tabla) e singura care știe răspunsurile corecte și calculează punctajul.
// Pe canal circulă doar porecle și avatare; nimic nu se salvează pe server.

import type { Grafic, Harta, Item, Punct, Raport } from '../types';
import { distantaKm } from '../maps/MapView';

export interface Jucator { id: string; porecla: string; avatar: string; clasa?: number; echipa: number; scor: number }
export interface Echipa { nume: string; scor: number }

/** Itemul așa cum îl vede telefonul: fără răspunsul corect. */
export interface ItemPublic {
  id: string;
  tip: 'alegere' | 'denumeste' | 'grafic' | 'pin';
  enunt: string;
  variante?: string[];
  harta?: Harta;
  punct?: Punct;
  schema?: string;
  evidentiat?: string;
  grafic?: Grafic;
  pentruClasa?: number;
}

export type Faza = 'lobby' | 'intrebare' | 'rezultat' | 'final';

export interface StareSesiune {
  pin: string;
  titlu: string;
  faza: Faza;
  k: number;
  total: number;
  echipe: Echipa[];
  jucatori: Jucator[];
  intrebare?: ItemPublic;
  /** milisecunde rămase în momentul trimiterii (nu ora exactă: ceasurile telefoanelor diferă) */
  ramasMs?: number;
  durataMs: number;
  raspunsuri?: number;
  rezultat?: { corect?: number; tinta?: Punct; distributie?: number[]; castig: Record<string, number> };
  clasamentIndividual: boolean;
  clase: number[];
  hartaColectiva?: { dezvaluite: number; total: number; tema?: 'polara' | 'verde' };
}

export type Mesaj =
  | { t: 'stare'; s: StareSesiune }
  | { t: 'intra'; id: string; porecla: string; avatar: string; clasa?: number }
  | { t: 'raspuns'; id: string; k: number; v: number | Punct }
  | { t: 'reactie'; id: string; r: string }
  | { t: 'cer-stare' }
  // colectarea rezultatelor: elevul trimite rezumatul, calculatorul profesorului confirmă
  | { t: 'raport'; id: string; r: Omit<Raport, 'id' | 'primit'> }
  | { t: 'primit'; id: string }
  | { t: 'colectare'; titlu: string };

export const REACTII = ['👍', '🤔', '🎉', '😮'];
export const NUME_ECHIPE = ['Echipa Nord', 'Echipa Sud', 'Echipa Est', 'Echipa Vest'];
export const SIMBOLURI = ['▲', '◆', '●', '■'];
export const TIPURI_LIVE = new Set(['alegere', 'denumeste', 'grafic', 'pin']);

/** Transformă un item în varianta publică; amestecă variantele și întoarce și maparea (doar pentru gazdă). */
export function publica(item: Item, amesteca: <T>(a: T[]) => T[], pentruClasa?: number): { pub: ItemPublic; corect?: number; tinta?: Punct; toleranta?: number } {
  const baza = { id: item.id, enunt: item.enunt, pentruClasa };
  if (item.tip === 'pin') {
    return { pub: { ...baza, tip: 'pin', harta: item.date.harta }, tinta: item.date.tinta, toleranta: item.date.toleranta };
  }
  if (item.tip === 'alegere' || item.tip === 'denumeste' || item.tip === 'grafic') {
    const d = item.date as { variante: string[]; corect: number };
    const ordine = amesteca(d.variante.map((_, i) => i));
    const pub: ItemPublic = { ...baza, tip: item.tip, variante: ordine.map((i) => d.variante[i]) };
    if (item.tip === 'denumeste') Object.assign(pub, { harta: item.date.harta, punct: item.date.punct, schema: item.date.schema, evidentiat: item.date.evidentiat });
    if (item.tip === 'alegere') Object.assign(pub, { schema: item.date.schema, evidentiat: item.date.evidentiat });
    if (item.tip === 'grafic') pub.grafic = item.date.grafic;
    return { pub, corect: ordine.indexOf(d.corect) };
  }
  throw new Error(`Tipul ${item.tip} nu se joacă live`);
}

/** Punctaj: 500 pentru răspuns corect + până la 500 pentru viteză. Pin aproape (până la 2× toleranța): jumătate. */
export function puncte(corect: number, ramasMs: number, durataMs: number): number {
  if (corect <= 0) return 0;
  const viteza = Math.max(0, Math.min(1, ramasMs / durataMs));
  return Math.round((500 + 500 * viteza) * corect);
}

export function scorPin(v: Punct, tinta: Punct, toleranta: number): number {
  const d = distantaKm(v, tinta);
  return d <= toleranta ? 1 : d <= toleranta * 2 ? 0.5 : 0;
}

/** Echipa cu cei mai puțini membri primește jucătorul nou (echipe mixte, echilibrate). */
export function alegeEchipa(jucatori: Jucator[], nrEchipe: number): number {
  const n = Array(nrEchipe).fill(0);
  for (const j of jucatori) n[j.echipa]++;
  return n.indexOf(Math.min(...n));
}

/** Scorul echipei = media punctelor membrilor, ca echipele mici să nu fie dezavantajate. */
export function scoruriEchipe(jucatori: Jucator[], nrEchipe: number): number[] {
  return Array.from({ length: nrEchipe }, (_, e) => {
    const m = jucatori.filter((j) => j.echipa === e);
    return m.length ? Math.round(m.reduce((s, j) => s + j.scor, 0) / m.length) : 0;
  });
}

export function pinNou(): string {
  return String(Math.floor(100000 + Math.random() * 900000));
}
