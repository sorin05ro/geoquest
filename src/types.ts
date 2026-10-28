// Tipurile de date ale aplicației GeoQuest. Schema e documentată și în docs/scheme-date.md.

export type Clasa = 5 | 6 | 7 | 8;

export interface Saptamana {
  nr: number;
  de: string; // ISO, prima zi de curs
  pana: string; // ISO, ultima zi de curs
  interval: number;
  zileCurs: number;
  zileLibere: string[];
}

export type TipEveniment =
  | 'nivel' | 'continuare' | 'expeditie' | 'busola' | 'boss' | 'mare-expeditie'
  | 'portal' | 'recapitulare' | 'eveniment' | 'fara-ore';

export interface RandPlanificare {
  clasa: Clasa;
  saptamana: number;
  interval: number;
  unitate: string | null;
  continuturi: string[];
  niveluri: string[];
  competente: string[];
  ore: number;
  evaluare: string[];
  tipEveniment: TipEveniment[];
  test?: string;
  eveniment?: string;
}

export interface NivelCalendar {
  id: string;
  clasa: Clasa;
  saptamana: number;
  unitate: string;
  titlu: string;
  tip: 'nivel' | 'expeditie';
  competente: string[];
}

export interface Perioada { nume?: string; id?: string; de: string; pana: string }

export interface Calendar {
  an: string;
  intervale: { nr: number; de: string; pana: string }[];
  vacante: Perioada[];
  zileLibere: { data: string; nume: string }[];
  evenimente: Perioada[];
  ultimaZi: Record<string, string>;
  saptamani: Saptamana[];
  planificare: RandPlanificare[];
  niveluri: NivelCalendar[];
  observatii: string[];
}

// ---------------------------------------------------------------- conținut

export type TipItem =
  | 'pin' | 'denumeste' | 'etichete' | 'ordoneaza' | 'asociaza' | 'lacunar' | 'grafic' | 'alegere';

export interface Punct { lat: number; lon: number; nume?: string }

export interface ItemBaza {
  id: string;
  nivel: string;
  competente: string[];
  tip: TipItem;
  dificultate: 1 | 2 | 3;
  enunt: string;
  feedback: { corect: string; gresit: string };
  indiciu?: string;
  xp?: number;
  surse?: string[];
  referintaProfesor?: string;
}

export type Harta = 'lume' | 'romania';

export interface ItemPin extends ItemBaza { tip: 'pin'; date: { harta: Harta; tinta: Punct; toleranta: number } }
export interface ItemDenumeste extends ItemBaza {
  tip: 'denumeste';
  date: { harta?: Harta; punct?: Punct; schema?: string; evidentiat?: string; variante: string[]; corect: number };
}
export interface ItemEtichete extends ItemBaza {
  tip: 'etichete';
  date: { harta?: Harta; schema?: string; tinte: { id: string; eticheta: string; lat?: number; lon?: number }[]; distractori?: string[] };
}
export interface ItemOrdoneaza extends ItemBaza { tip: 'ordoneaza'; date: { elemente: string[]; criteriu: string } }
export interface ItemAsociaza extends ItemBaza { tip: 'asociaza'; date: { perechi: [string, string][] } }
export interface ItemLacunar extends ItemBaza { tip: 'lacunar'; date: { text: string; raspunsuri: string[]; distractori: string[] } }
export interface Grafic {
  tip: 'bare' | 'profil' | 'structura';
  titlu: string;
  unitate?: string;
  date: { eticheta: string; valoare: number }[];
  sursa?: string;
}
export interface ItemGrafic extends ItemBaza { tip: 'grafic'; date: { grafic: Grafic; variante: string[]; corect: number } }
export interface ItemAlegere extends ItemBaza { tip: 'alegere'; date: { schema?: string; evidentiat?: string; variante: string[]; corect: number } }

export type Item =
  | ItemPin | ItemDenumeste | ItemEtichete | ItemOrdoneaza | ItemAsociaza | ItemLacunar | ItemGrafic | ItemAlegere;

export interface PasExpeditie {
  titlu: string;
  text: string;
  itemi?: string[]; // id-uri de itemi
  jurnal?: { cerinta: string; foto?: boolean };
}

export interface ContinutNivel {
  id: string;
  titlu: string;
  tip: 'nivel' | 'expeditie';
  descopera: { intrebare: string; schema?: string; imagine?: string };
  invata: { titlu: string; text: string; schema?: string }[];
  stiaiCa?: string;
  pasi?: PasExpeditie[]; // doar la expediții
  referintaProfesor?: string;
}

export interface FisierContinut {
  clasa: Clasa;
  unitate: string;
  niveluri: ContinutNivel[];
  itemi: Item[];
  boss?: { id: string; test: string; titlu: string; saptamana: number; niveluri: string[]; itemiSuplimentari?: string[] }[];
}

export interface IndexContinut {
  clasa: Clasa;
  fisiere: { fisier: string; niveluri: string[]; boss?: string[] }[];
}

// ---------------------------------------------------------------- progres

export interface Profil {
  id: 'eu';
  porecla: string;
  avatar: string;
  clasa: Clasa;
  litera?: string;
  creat: string;
  dificultate: 1 | 2 | 3;
  /** codul clasei primit de la profesor (ex. 5A-K7QM); doar grupează rapoartele */
  codClasa?: string;
}

export interface ClasaProfesor { cod: string; clasa: Clasa; litera: string; creat: string }

export interface Tema {
  id: string;
  titlu: string;
  clasa: Clasa;
  cod?: string;
  niveluri: string[];
  termen: string;
  creat: string;
}

/** Rezumatul progresului pe care elevul îl trimite profesorului (fără nume reale). */
export interface SumarProgres {
  xp: number;
  niveluri: Record<string, { stele: number; scor: number }>;
  competente: Record<string, { c: number; t: number }>;
  greseli: Record<string, number>;
  teme: Record<string, number>; // tema → niveluri terminate
  ultimaActivitate: string | null;
  raspunsuri: number;
}

export interface Raport {
  id?: number;
  cod: string;
  porecla: string;
  avatar: string;
  clasa: Clasa;
  primit: string;
  sumar: SumarProgres;
}

export interface RezultatNivel {
  nivel: string;
  stele: 0 | 1 | 2 | 3;
  scor: number; // 0..1
  indicii: number;
  terminat: string;
}

export interface Raspuns {
  id?: number;
  item: string;
  nivel: string;
  corect: boolean;
  partial?: number;
  indiciu: boolean;
  durataMs: number;
  data: string;
}

export interface CutieLeitner { item: string; cutie: 1 | 2 | 3 | 4; urmatoarea: string }

export interface EvenimentXP { id?: number; data: string; xp: number; motiv: string }

export interface IntrareJurnal { id?: number; nivel: string; pas: number; text: string; foto?: Blob; data: string; validat?: boolean }
