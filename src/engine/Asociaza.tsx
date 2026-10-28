import { useEffect, useMemo, useState } from 'react';
import type { ItemAsociaza } from '../types';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

/** Tipul 8 – Asociază perechi. Perechile se marchează cu număr, nu doar cu culoare. */
export function Asociaza({ item, verificat, onScor }: PropsTip<ItemAsociaza>) {
  const p = item.date.perechi;
  const dreapta = useMemo(() => amesteca(p.map((_, i) => i)), [item.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [legaturi, setLegaturi] = useState<Record<number, number>>({}); // stânga -> dreapta
  const [stanga, setStanga] = useState<number | null>(null);

  useEffect(() => { setLegaturi({}); setStanga(null); }, [item.id]);
  useEffect(() => {
    const k = Object.keys(legaturi).length;
    if (k < p.length) { onScor(null); return; }
    const ok = Object.entries(legaturi).filter(([a, b]) => Number(a) === b).length;
    onScor(ok / p.length);
  }, [legaturi]); // eslint-disable-line react-hooks/exhaustive-deps

  const nrPereche = (st: number) => Object.keys(legaturi).map(Number).sort((a, b) => a - b).indexOf(st) + 1;
  const stangaDin = (dr: number) => Object.entries(legaturi).find(([, b]) => b === dr)?.[0];

  const alegeDreapta = (dr: number) => {
    if (verificat) return;
    if (stanga === null) {
      const s = stangaDin(dr);
      if (s !== undefined) setLegaturi((l) => { const n = { ...l }; delete n[Number(s)]; return n; });
      return;
    }
    setLegaturi((l) => {
      const n = { ...l };
      for (const k of Object.keys(n)) if (n[Number(k)] === dr) delete n[Number(k)];
      n[stanga] = dr;
      return n;
    });
    setStanga(null);
  };

  const cls = (ok: boolean | null) => (ok === null ? '' : ok ? 'corect' : 'gresit');
  return (
    <div className="stiva">
      <div className="perechi">
        <div className="coloana" role="group" aria-label="Coloana A">
          {p.map(([a], i) => {
            const leg = legaturi[i];
            return (
              <button
                key={i} className={`varianta ${verificat ? cls(leg === i) : ''}`} aria-pressed={stanga === i} disabled={verificat}
                onClick={() => setStanga((s) => (s === i ? null : i))}
              >
                {leg !== undefined && <span className="insemn">{nrPereche(i)}</span>}{a}
              </button>
            );
          })}
        </div>
        <div className="coloana" role="group" aria-label="Coloana B">
          {dreapta.map((j) => {
            const s = stangaDin(j);
            return (
              <button
                key={j} className={`varianta ${verificat && s !== undefined ? cls(Number(s) === j) : ''}`} disabled={verificat}
                onClick={() => alegeDreapta(j)}
              >
                {s !== undefined && <span className="insemn">{nrPereche(Number(s))}</span>}{p[j][1]}
              </button>
            );
          })}
        </div>
      </div>
      <p className="eticheta-mica">
        {stanga !== null ? `Alege perechea pentru „${p[stanga][0]}”.` : 'Atinge un element din stânga, apoi perechea lui din dreapta.'}
      </p>
      {verificat && Object.entries(legaturi).some(([a, b]) => Number(a) !== b) && (
        <ul className="eticheta-mica">{p.map(([a, b]) => <li key={a}>{a} – {b}</li>)}</ul>
      )}
    </div>
  );
}
