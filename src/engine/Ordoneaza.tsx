import { useEffect, useState } from 'react';
import type { ItemOrdoneaza } from '../types';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

/** Tipul 7 (și 11) – Ordonează / succesiunea etapelor. Elementele sunt scrise în JSON în ordinea corectă. */
export function Ordoneaza({ item, verificat, onScor }: PropsTip<ItemOrdoneaza>) {
  const n = item.date.elemente.length;
  const [ordine, setOrdine] = useState<number[]>([]);
  const [atins, setAtins] = useState(false);

  useEffect(() => {
    let o = amesteca([...Array(n).keys()]);
    if (o.every((v, i) => v === i)) o = [...o.slice(1), o[0]];
    setOrdine(o); setAtins(false); onScor(null);
  }, [item.id]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (!atins || !ordine.length) return;
    const bune = ordine.filter((v, i) => v === i).length;
    onScor(bune === n ? 1 : bune / n * 0.5);
  }, [ordine, atins]); // eslint-disable-line react-hooks/exhaustive-deps

  const muta = (i: number, dir: -1 | 1) => {
    const j = i + dir;
    if (j < 0 || j >= n) return;
    const o = [...ordine];
    [o[i], o[j]] = [o[j], o[i]];
    setOrdine(o); setAtins(true);
  };

  return (
    <div className="stiva">
      <p className="eticheta-mica">{item.date.criteriu}. Mută elementele cu săgețile.</p>
      <ol className="lista-ordonare">
        {ordine.map((v, i) => {
          const stare = verificat ? (v === i ? 'var(--ok)' : 'var(--gresit)') : undefined;
          return (
            <li key={v} style={stare ? { borderColor: stare } : undefined}>
              <span className="insemn" aria-hidden="true">{i + 1}</span>
              <span>{item.date.elemente[v]}</span>
              <button className="buton-icon" disabled={verificat || i === 0} onClick={() => muta(i, -1)} aria-label={`Mută „${item.date.elemente[v]}” mai sus`}>▲</button>
              <button className="buton-icon" disabled={verificat || i === n - 1} onClick={() => muta(i, 1)} aria-label={`Mută „${item.date.elemente[v]}” mai jos`}>▼</button>
            </li>
          );
        })}
      </ol>
      {!atins && !verificat && <button className="buton secundar mic" onClick={() => setAtins(true)}>E deja în ordinea bună</button>}
      {verificat && ordine.some((v, i) => v !== i) && (
        <p className="eticheta-mica">Ordinea corectă: {item.date.elemente.join(' → ')}</p>
      )}
    </div>
  );
}
