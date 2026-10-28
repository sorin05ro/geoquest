import { Fragment, useEffect, useMemo, useState } from 'react';
import type { ItemLacunar } from '../types';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

/** Tipul 9 – Text lacunar. Spațiile goale se scriu în text ca {0}, {1} ... */
export function Lacunar({ item, verificat, onScor }: PropsTip<ItemLacunar>) {
  const { text, raspunsuri, distractori } = item.date;
  const bucati = useMemo(() => text.split(/\{(\d+)\}/), [text]);
  const banca = useMemo(() => amesteca([...raspunsuri, ...distractori]), [item.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [completat, setCompletat] = useState<(string | null)[]>([]);
  const [activ, setActiv] = useState(0);

  useEffect(() => { setCompletat(raspunsuri.map(() => null)); setActiv(0); }, [item.id]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => {
    if (!completat.length || completat.some((c) => c === null)) { onScor(null); return; }
    onScor(completat.filter((c, i) => c === raspunsuri[i]).length / raspunsuri.length);
  }, [completat]); // eslint-disable-line react-hooks/exhaustive-deps

  const alege = (cuv: string) => {
    if (verificat) return;
    setCompletat((c) => {
      const n = c.map((x) => (x === cuv ? null : x));
      n[activ] = cuv;
      const urm = n.findIndex((x) => x === null);
      setActiv(urm === -1 ? activ : urm);
      return n;
    });
  };

  return (
    <div className="stiva">
      <p style={{ lineHeight: 2.4 }}>
        {bucati.map((b, i) => {
          if (i % 2 === 0) return <Fragment key={i}>{b}</Fragment>;
          const k = Number(b);
          const v = completat[k];
          const stil = verificat ? { borderColor: v === raspunsuri[k] ? 'var(--ok)' : 'var(--gresit)' } : activ === k ? { borderColor: 'var(--pion)' } : undefined;
          return (
            <button key={i} className="slot" style={stil} onClick={() => setActiv(k)} disabled={verificat}
              aria-label={`Spațiul ${k + 1}: ${v ?? 'gol'}`}>
              {verificat && v !== raspunsuri[k] ? <><s>{v}</s>&nbsp;{raspunsuri[k]}</> : (v ?? '…')}
            </button>
          );
        })}
      </p>
      <div className="rand" role="group" aria-label="Cuvinte de folosit">
        {banca.map((c) => (
          <button key={c} className={`jeton ${completat.includes(c) ? 'folosit' : ''}`} onClick={() => alege(c)} disabled={verificat}>{c}</button>
        ))}
      </div>
    </div>
  );
}
