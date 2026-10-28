import { Suspense, lazy, useEffect, useState } from 'react';
import { AppProvider, useApp, type Ecran } from './state';
import { Harta } from './screens/Harta';
import { Nivel } from './screens/Nivel';
import { Boss } from './screens/Boss';
import { Misiune } from './screens/Misiune';
import { Profil, aplicaSetariAfisare } from './screens/Profil';
import { Intrare } from './screens/Intrare';
import { Tabla } from './screens/Tabla';
import { Recapitulare } from './screens/Recapitulare';
import { citesteSetare, db } from './db/db';
import { citesteCodClasa, decodeazaTema } from './profesor/sumar';
import { formatData } from './calendar/calendar';

// ecranele pentru clasă se încarcă doar când e nevoie de ele
const Gazda = lazy(() => import('./live/Gazda').then((m) => ({ default: m.Gazda })));
const Jucator = lazy(() => import('./live/Jucator').then((m) => ({ default: m.Jucator })));
const Prezentare = lazy(() => import('./screens/Prezentare').then((m) => ({ default: m.Prezentare })));
const Profesor = lazy(() => import('./screens/Profesor').then((m) => ({ default: m.Profesor })));
const TrimiteRaport = lazy(() => import('./live/TrimiteRaport').then((m) => ({ default: m.TrimiteRaport })));
const Incarcare = () => <p aria-busy="true">Se încarcă…</p>;

function pinDinAdresa() {
  const m = location.hash.match(/^#live=(\d{0,6})/);
  return m ? m[1] : null;
}
function dinAdresa(cheie: string) {
  const m = location.hash.match(new RegExp(`^#${cheie}=([^&]*)`));
  return m ? decodeURIComponent(m[1]) : null;
}

const ICON = {
  harta: <path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2zm0 2.2 6 2v11.6l-6-2V6.2z" fill="currentColor" />,
  misiune: <path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm4.2 5.8-2.5 6-6 2.4 2.5-6 6-2.4zM12 11a1 1 0 1 0 0 2 1 1 0 0 0 0-2z" fill="currentColor" />,
  profil: <path d="M12 12a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5z" fill="currentColor" />,
};

function Ecrane() {
  const { ecran, profil, mergi } = useApp();
  const [pinLive, setPinLive] = useState(pinDinAdresa());
  const [anunt, setAnunt] = useState('');
  useEffect(() => { citesteSetare('afisare', {}).then(aplicaSetariAfisare); }, []);
  useEffect(() => {
    const f = () => setPinLive(pinDinAdresa());
    window.addEventListener('hashchange', f);
    return () => window.removeEventListener('hashchange', f);
  }, []);

  // linkuri primite de la profesor: #clasa=COD, #tema=..., #colectare=PIN
  useEffect(() => {
    const cod = dinAdresa('clasa');
    const tema = dinAdresa('tema');
    const colectare = dinAdresa('colectare');
    if (cod && profil) {
      const c = citesteCodClasa(cod);
      if (c && c.clasa === profil.clasa) { db.profil.update('eu', { codClasa: cod.toUpperCase(), ...(c.litera ? { litera: c.litera } : {}) }); setAnunt(`Te-ai înscris în clasa cu codul ${cod.toUpperCase()}.`); }
      else setAnunt(`Codul ${cod} nu e pentru clasa ta. Verifică pe tablă.`);
      history.replaceState(null, '', location.pathname);
    }
    if (tema && profil) {
      const t = decodeazaTema(tema);
      if (t && t.clasa === profil.clasa) {
        db.teme.put(t);
        setAnunt(`Temă nouă: ${t.titlu}, până pe ${formatData(t.termen)}. Lecțiile ei sunt deschise pe hartă.`);
      } else setAnunt(t ? `Tema e pentru clasa a ${t.clasa}-a, nu pentru clasa ta.` : 'Linkul temei nu e complet. Cere-l din nou profesorului.');
      history.replaceState(null, '', location.pathname);
      mergi({ e: 'harta' });
    }
    if (colectare !== null) { history.replaceState(null, '', location.pathname); mergi({ e: 'trimite-raport', pin: colectare }); }
  }, [!!profil]); // eslint-disable-line react-hooks/exhaustive-deps

  if (pinLive !== null) return <main className="continut"><Suspense fallback={<Incarcare />}><Jucator pinInitial={pinLive} /></Suspense></main>;
  if (ecran.e === 'live-gazda') return <main className="continut"><Suspense fallback={<Incarcare />}><Gazda /></Suspense></main>;
  if (ecran.e === 'prezentare') return <main className="continut"><Suspense fallback={<Incarcare />}><Prezentare /></Suspense></main>;

  if (ecran.e === 'profesor') return <main className="continut"><Suspense fallback={<Incarcare />}><Profesor /></Suspense></main>;
  if (ecran.e === 'trimite-raport') return <main className="continut"><Suspense fallback={<Incarcare />}><TrimiteRaport pinInitial={ecran.pin} /></Suspense></main>;
  if (ecran.e === 'tabla') return <main className="continut"><Tabla /></main>;
  if (!profil) return <main className="continut"><Intrare /></main>;

  const tab: Ecran['e'] = ecran.e;
  const nav = (e: 'harta' | 'misiune' | 'profil', eticheta: string) => (
    <button onClick={() => mergi({ e } as Ecran)} aria-current={tab === e ? 'page' : undefined}>
      <svg viewBox="0 0 24 24" aria-hidden="true">{ICON[e]}</svg>{eticheta}
    </button>
  );
  return (
    <>
      <main className="continut">
        {anunt && (
          <p className="feedback ok" role="status" style={{ display: 'flex', gap: 12, alignItems: 'center', justifyContent: 'space-between' }}>
            <span>{anunt}</span><button className="buton secundar mic" onClick={() => setAnunt('')}>Am înțeles</button>
          </p>
        )}
        {ecran.e === 'harta' && <Harta />}
        {ecran.e === 'nivel' && <Nivel key={ecran.id + (ecran.n ?? '')} id={ecran.id} />}
        {ecran.e === 'boss' && <Boss key={ecran.id} id={ecran.id} />}
        {ecran.e === 'misiune' && <Misiune />}
        {ecran.e === 'profil' && <Profil />}
        {ecran.e === 'recapitulare' && <Recapitulare />}
        {ecran.e === 'intrare' && <Harta />}
      </main>
      <nav className="meniu-jos" aria-label="Meniu">
        {nav('harta', 'Hartă')}
        {nav('misiune', 'Misiunea zilei')}
        {nav('profil', 'Profil')}
      </nav>
    </>
  );
}

export default function App() {
  return (
    <div className="aplicatie">
      <AppProvider><Ecrane /></AppProvider>
    </div>
  );
}
