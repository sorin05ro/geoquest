import { useEffect, useMemo, useState } from 'react';
import { useApp } from '../state';
import { amesteca, continutClasa, type ContinutIncarcat } from '../content';
import { Exercitiu } from '../engine/Exercitiu';
import { saptamanaDeblocata } from '../calendar/calendar';
import type { Clasa, Item } from '../types';

const ECHIPE = ['Echipa Nord', 'Echipa Sud', 'Echipa Est', 'Echipa Vest'];

/** Turul geografic (evaluare orală la tablă): 2–4 echipe se succed, scorul e pe echipă. */
export function Tabla() {
  const { cal, azi, mergi, profil } = useApp();
  const [clasa, setClasa] = useState<Clasa>(profil?.clasa ?? 5);
  const [c, setC] = useState<ContinutIncarcat>();
  const [alese, setAlese] = useState<Set<string>>(new Set());
  const [nrEchipe, setNrEchipe] = useState(2);
  const [runde, setRunde] = useState(8);
  const [cronometru, setCronometru] = useState(true);
  const [joc, setJoc] = useState<{ itemi: Item[]; k: number; scor: number[] } | null>(null);
  const [timp, setTimp] = useState(30);

  useEffect(() => {
    document.documentElement.dataset.mod = 'tabla';
    return () => { delete document.documentElement.dataset.mod; };
  }, []);
  useEffect(() => {
    continutClasa(clasa).then((x) => {
      setC(x);
      const s = saptamanaDeblocata(cal, clasa, azi);
      setAlese(new Set([...x.niveluri.values()].filter((n) => (cal.niveluri.find((q) => q.id === n.id)?.saptamana ?? 99) === s).map((n) => n.id)));
    });
  }, [clasa]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => {
    if (!joc || !cronometru) return;
    setTimp(30);
    const t = setInterval(() => setTimp((x) => Math.max(0, x - 1)), 1000);
    return () => clearInterval(t);
  }, [joc?.k, cronometru]); // eslint-disable-line react-hooks/exhaustive-deps

  const niveluri = useMemo(() => (c ? [...c.niveluri.values()].filter((n) => n.tip === 'nivel') : []), [c]);

  const porneste = () => {
    const pool = [...c!.itemi.values()].filter((i) => alese.has(i.nivel) && i.tip !== 'ordoneaza');
    setJoc({ itemi: amesteca(pool).slice(0, runde * nrEchipe), k: 0, scor: Array(nrEchipe).fill(0) });
  };

  if (!joc) {
    return (
      <div className="stiva mod-tabla">
        <h1>Turul geografic</h1>
        <p>Proiectează pe tablă. Echipele răspund pe rând, la tablă. Fără telefoane, fără note individuale.</p>
        <div className="card stiva">
          <div className="rand" role="group" aria-label="Clasa">
            {([5, 6, 7, 8] as Clasa[]).map((k) => (
              <button key={k} className="varianta" style={{ minWidth: 110, textAlign: 'center' }} aria-pressed={clasa === k} onClick={() => setClasa(k)}>
                a {({ 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' } as const)[k]}-a
              </button>
            ))}
          </div>
          <fieldset className="stiva" style={{ border: 0, padding: 0 }}>
            <legend><b>Lecțiile din joc</b></legend>
            {niveluri.length === 0 && <p className="eticheta-mica">Pentru această clasă, conținutul vine în Etapa 4.</p>}
            {niveluri.map((n) => (
              <label key={n.id} className="rand">
                <input type="checkbox" style={{ width: 28, height: 28 }} checked={alese.has(n.id)}
                  onChange={(e) => setAlese((s) => { const x = new Set(s); if (e.target.checked) x.add(n.id); else x.delete(n.id); return x; })} />
                {n.titlu}
              </label>
            ))}
          </fieldset>
          <div className="rand">
            <label className="camp"><span>Echipe</span>
              <select value={nrEchipe} onChange={(e) => setNrEchipe(Number(e.target.value))}>{[2, 3, 4].map((n) => <option key={n}>{n}</option>)}</select>
            </label>
            <label className="camp"><span>Runde pe echipă</span>
              <select value={runde} onChange={(e) => setRunde(Number(e.target.value))}>{[3, 5, 8, 10].map((n) => <option key={n}>{n}</option>)}</select>
            </label>
            <label className="rand"><input type="checkbox" style={{ width: 28, height: 28 }} checked={cronometru} onChange={(e) => setCronometru(e.target.checked)} /> Cronometru de 30 s</label>
          </div>
          <div className="rand">
            <button className="buton secundar" onClick={() => mergi({ e: profil ? 'harta' : 'profesor' })}>Înapoi</button>
            <button className="buton" disabled={alese.size === 0} onClick={porneste}>Pornește turul</button>
            <button className="buton secundar" onClick={() => document.documentElement.requestFullscreen?.()}>Ecran complet</button>
          </div>
        </div>
      </div>
    );
  }

  const echipa = joc.k % nrEchipe;
  if (joc.k >= joc.itemi.length) {
    const max = Math.max(...joc.scor);
    return (
      <div className="stiva mod-tabla" style={{ textAlign: 'center' }}>
        <h1>Turul s-a încheiat</h1>
        <div className="scor-echipe">
          {joc.scor.map((s, i) => <div key={i} className={`echipa ${s === max ? 'activa' : ''}`}>{ECHIPE[i]}<b>{s} puncte</b></div>)}
        </div>
        <p>Împreună ați răspuns corect la {joc.scor.reduce((a, b) => a + b, 0) / 10} întrebări. Bravo, exploratori!</p>
        <div className="rand" style={{ justifyContent: 'center' }}>
          <button className="buton secundar" onClick={() => setJoc(null)}>Alt tur</button>
          <button className="buton" onClick={() => mergi({ e: profil ? 'harta' : 'profesor' })}>Închide</button>
        </div>
      </div>
    );
  }
  return (
    <div className="stiva mod-tabla">
      <div className="scor-echipe" aria-live="polite">
        {joc.scor.map((s, i) => <div key={i} className={`echipa ${i === echipa ? 'activa' : ''}`}>{ECHIPE[i]}<b>{s} puncte</b></div>)}
        {cronometru && <div className="echipa" aria-label={`Timp rămas: ${timp} secunde`}>Timp<b>0:{String(timp).padStart(2, '0')}</b></div>}
      </div>
      <div className="card">
        <p className="eticheta-mica">Întrebarea {joc.k + 1} din {joc.itemi.length} · răspunde {ECHIPE[echipa]}</p>
        <Exercitiu key={joc.itemi[joc.k].id} item={joc.itemi[joc.k]} textContinua="Următoarea echipă" onGata={(r) => {
          setJoc((j) => j && { ...j, k: j.k + 1, scor: j.scor.map((s, i) => (i === echipa && r.corect ? s + 10 : s)) });
        }} />
      </div>
    </div>
  );
}
