import { useEffect, useMemo, useState } from 'react';
import type { ItemAlegere, ItemDenumeste } from '../types';
import { MapView } from '../maps/MapView';
import { Schema } from '../maps/Scheme';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

function Variante({ variante, corect, verificat, onScor, id }: {
  variante: string[]; corect: number; verificat: boolean; onScor: (s: number | null) => void; id: string;
}) {
  const ordine = useMemo(() => amesteca(variante.map((_, i) => i)), [id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [ales, setAles] = useState<number | null>(null);
  useEffect(() => setAles(null), [id]);
  return (
    <div className="variante" role="group" aria-label="Variante de răspuns">
      {ordine.map((i) => {
        const cls = verificat ? (i === corect ? 'corect' : i === ales ? 'gresit' : '') : '';
        return (
          <button
            key={i} className={`varianta ${cls}`} aria-pressed={ales === i} disabled={verificat}
            onClick={() => { setAles(i); onScor(i === corect ? 1 : 0); }}
          >
            {variante[i]}
          </button>
        );
      })}
    </div>
  );
}

/** Tipul 2 – Denumește elementul indicat pe harta mută sau pe schemă. */
export function Denumeste({ item, verificat, onScor }: PropsTip<ItemDenumeste>) {
  const d = item.date;
  return (
    <div className="stiva">
      {d.harta && d.punct && (
        <MapView
          harta={d.harta} eticheta="Hartă mută cu un element evidențiat"
          overlay={(p) => {
            const [x, y] = p([d.punct!.lon, d.punct!.lat]) ?? [0, 0];
            return (
              <g>
                <circle cx={x} cy={y} r="18" fill="none" stroke="var(--pion)" strokeWidth="4" />
                <circle cx={x} cy={y} r="5" fill="var(--pion)" />
              </g>
            );
          }}
        />
      )}
      {d.schema && <Schema id={d.schema} evidentiat={d.evidentiat} />}
      <Variante variante={d.variante} corect={d.corect} verificat={verificat} onScor={onScor} id={item.id} />
    </div>
  );
}

/** Grilă simplă (o singură variantă corectă), opțional cu schemă. */
export function Alegere({ item, verificat, onScor }: PropsTip<ItemAlegere>) {
  return (
    <div className="stiva">
      {item.date.schema && <Schema id={item.date.schema} evidentiat={item.date.evidentiat} />}
      <Variante variante={item.date.variante} corect={item.date.corect} verificat={verificat} onScor={onScor} id={item.id} />
    </div>
  );
}
