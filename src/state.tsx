import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { db, citesteSetare } from './db/db';
import { continutClasa, incarcaCalendar, incarcaInsigne, incarcaScoala, type ConfigScoala, type ContinutIncarcat } from './content';
import { isoLocal, niveluriDeblocate, type Suprascrieri } from './calendar/calendar';
import type { Calendar, Profil, Tema } from './types';
import type { Insigna } from './game/rules';

export type Ecran =
  | { e: 'harta' } | { e: 'nivel'; id: string; n?: number } | { e: 'boss'; id: string } | { e: 'misiune' }
  | { e: 'profil' } | { e: 'recapitulare' } | { e: 'tabla' } | { e: 'profesor' } | { e: 'intrare' } | { e: 'live-gazda' } | { e: 'prezentare' } | { e: 'trimite-raport'; pin?: string };

interface Stare {
  cal: Calendar;
  scoala: ConfigScoala;
  insigne: Insigna[];
  profil: Profil | undefined;
  continut: ContinutIncarcat | undefined;
  azi: string;
  supr: Suprascrieri;
  deblocate: Set<string>;
  teme: Tema[];
  xp: number;
  ecran: Ecran;
  mergi: (e: Ecran) => void;
  reincarca: () => void;
}

const Ctx = createContext<Stare | null>(null);
export const useApp = () => useContext(Ctx)!;

export function AppProvider({ children }: { children: ReactNode }) {
  const [baza, setBaza] = useState<{ cal: Calendar; scoala: ConfigScoala; insigne: Insigna[] }>();
  const [eroare, setEroare] = useState<string>();
  const [continut, setContinut] = useState<ContinutIncarcat>();
  const [ecran, setEcran] = useState<Ecran>({ e: 'harta' });
  const [versiune, setVersiune] = useState(0);
  const [azi, setAzi] = useState(isoLocal(new Date()));
  const [supr, setSupr] = useState<Suprascrieri>({ deblocate: [], blocate: [] });

  const profil = useLiveQuery(() => db.profil.get('eu'), [], null as unknown as Profil | undefined);
  const xp = useLiveQuery(async () => { let s = 0; await db.xp.each((e) => { s += e.xp; }); return s; }, [], 0);
  const teme = useLiveQuery(() => db.teme.toArray(), [], [] as Tema[]);

  useEffect(() => {
    // o planificare importată de profesor pe acest dispozitiv are prioritate față de cea publicată
    Promise.all([citesteSetare<Calendar | null>('calendarLocal', null).then((c) => c ?? incarcaCalendar()), incarcaScoala(), incarcaInsigne()])
      .then(([cal, scoala, insigne]) => setBaza({ cal, scoala, insigne }))
      .catch((e) => setEroare(String(e?.message ?? e)));
  }, []);

  useEffect(() => {
    (async () => {
      const simulata = await citesteSetare<string | null>('dataSimulata', null);
      setAzi(simulata ?? isoLocal(new Date()));
      if (profil) setSupr(await citesteSetare<Suprascrieri>(`suprascrieri-${profil.clasa}`, { deblocate: [], blocate: [] }));
    })();
  }, [versiune, profil?.clasa]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (profil?.clasa) continutClasa(profil.clasa).then(setContinut);
  }, [profil?.clasa, versiune]);

  const mergi = useCallback((e: Ecran) => { setEcran(e); window.scrollTo(0, 0); }, []);
  const reincarca = useCallback(() => setVersiune((v) => v + 1), []);

  if (eroare) return <main className="continut"><h1>GeoQuest nu a pornit</h1><p role="alert">{eroare}</p><p>Deschide aplicația o dată cu internet, ca să se salveze pentru folosire offline.</p></main>;
  if (!baza || profil === (null as unknown)) return <main className="continut" aria-busy="true"><p>Se încarcă harta…</p></main>;

  const deblocate = profil ? niveluriDeblocate(baza.cal, profil.clasa, azi, supr) : new Set<string>();
  // temele primite deschid lecțiile lor, chiar dacă în calendar vin mai târziu
  for (const t of teme) if (t.clasa === profil?.clasa) t.niveluri.forEach((n) => deblocate.add(n));
  return (
    <Ctx.Provider value={{ ...baza, profil, continut, azi, supr, deblocate, teme, xp: xp ?? 0, ecran, mergi, reincarca }}>
      {children}
    </Ctx.Provider>
  );
}
