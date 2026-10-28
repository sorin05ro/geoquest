import { useEffect, useMemo, useState } from 'react';
import type { Grafic, ItemGrafic } from '../types';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

const CULORI = ['var(--munte)', 'var(--podis)', 'var(--campie)', 'var(--mare-2)', 'var(--pion)'];
const HASURI = ['', 'url(#h1)', 'url(#h2)', 'url(#h3)', 'url(#h4)'];

/** Desenează un grafic simplu (bare, profil, structură %) din date. Valorile sunt scrise și ca text. */
export function DesenGrafic({ g }: { g: Grafic }) {
  const W = 640, H = 300, st = 60, jos = 50, sus = 40;
  const max = Math.max(...g.date.map((d) => d.valoare)) * 1.1;
  const y = (v: number) => H - jos - (v / max) * (H - jos - sus);
  const bw = (W - st - 20) / g.date.length;
  const defs = (
    <defs>
      <pattern id="h1" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="var(--podis)" /><line x1="0" y1="0" x2="0" y2="8" stroke="var(--suprafata)" strokeWidth="3" /></pattern>
      <pattern id="h2" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="var(--campie)" /><circle cx="4" cy="4" r="1.6" fill="var(--suprafata)" /></pattern>
      <pattern id="h3" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="var(--mare-2)" /><line x1="0" y1="4" x2="8" y2="4" stroke="var(--suprafata)" strokeWidth="2" /></pattern>
      <pattern id="h4" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="8" height="8" fill="var(--pion)" /><line x1="0" y1="0" x2="0" y2="8" stroke="var(--suprafata)" strokeWidth="3" /></pattern>
    </defs>
  );

  if (g.tip === 'structura') {
    const tot = g.date.reduce((s, d) => s + d.valoare, 0);
    let x = st;
    const lat = W - st - 20;
    return (
      <figure style={{ margin: 0 }}>
        <svg viewBox={`0 0 ${W} 200`} className="harta-ex" style={{ background: 'var(--suprafata)' }} role="img" aria-label={`${g.titlu}: ${g.date.map((d) => `${d.eticheta} ${d.valoare}${g.unitate ?? ''}`).join(', ')}`}>
          {defs}
          <text x={st} y="30" fontSize="18" fontWeight="700" fill="var(--text)">{g.titlu}</text>
          {g.date.map((d, i) => {
            const w = (d.valoare / tot) * lat;
            const el = (
              <g key={i}>
                <rect x={x} y="56" width={w} height="60" fill={i === 0 ? CULORI[0] : HASURI[i % HASURI.length]} stroke="var(--suprafata)" strokeWidth="2" />
                <text x={x + w / 2} y="92" textAnchor="middle" fontSize="18" fontWeight="700" fill="var(--hartie)" style={{ paintOrder: 'stroke', stroke: 'var(--text)', strokeWidth: 3 }}>{d.valoare}{g.unitate}</text>
                <text x={x + w / 2} y="146" textAnchor="middle" fontSize="15" fill="var(--text)">{d.eticheta}</text>
              </g>
            );
            x += w;
            return el;
          })}
          {g.sursa && <text x={st} y="186" fontSize="12" fill="var(--text-2)">Sursa: {g.sursa}</text>}
        </svg>
      </figure>
    );
  }

  const pts = g.date.map((d, i) => [st + bw * i + bw / 2, y(d.valoare)] as const);
  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="harta-ex" style={{ background: 'var(--suprafata)' }} role="img"
      aria-label={`${g.titlu}: ${g.date.map((d) => `${d.eticheta} ${d.valoare} ${g.unitate ?? ''}`).join(', ')}`}>
      {defs}
      <text x={st} y="24" fontSize="17" fontWeight="700" fill="var(--text)">{g.titlu}</text>
      <line x1={st} y1={H - jos} x2={W - 10} y2={H - jos} stroke="var(--text-2)" />
      <line x1={st} y1={sus - 6} x2={st} y2={H - jos} stroke="var(--text-2)" />
      {g.unitate && <text x={st - 8} y={sus - 12} textAnchor="end" fontSize="13" fill="var(--text-2)">{g.unitate}</text>}
      {g.tip === 'bare' && g.date.map((d, i) => (
        <g key={i}>
          <rect x={st + bw * i + bw * 0.18} y={y(d.valoare)} width={bw * 0.64} height={H - jos - y(d.valoare)} fill={i % 2 ? HASURI[(i % 4) + 1] : CULORI[i % CULORI.length]} rx="4" />
          <text x={pts[i][0]} y={y(d.valoare) - 6} textAnchor="middle" fontSize="14" fontWeight="700" fill="var(--text)">{d.valoare.toLocaleString('ro-RO')}</text>
        </g>
      ))}
      {g.tip === 'profil' && (
        <>
          <path d={`M${st} ${H - jos} ${pts.map((p) => `L${p[0]} ${p[1]}`).join(' ')} L${W - 10} ${H - jos} Z`} fill="var(--podis-pal)" stroke="var(--munte)" strokeWidth="3" />
          {pts.map((p, i) => <g key={i}><circle cx={p[0]} cy={p[1]} r="5" fill="var(--munte)" /><text x={p[0]} y={p[1] - 10} textAnchor="middle" fontSize="13" fill="var(--text)">{g.date[i].valoare}</text></g>)}
        </>
      )}
      {g.date.map((d, i) => (
        <text key={i} x={pts[i][0]} y={H - jos + 20} textAnchor="middle" fontSize="13" fill="var(--text)">{d.eticheta}</text>
      ))}
      {g.sursa && <text x={st} y={H - 8} fontSize="12" fill="var(--text-2)">Sursa: {g.sursa}</text>}
    </svg>
  );
}

/** Tipul 12 – Citește graficul / profilul. */
export function GraficEx({ item, verificat, onScor }: PropsTip<ItemGrafic>) {
  const d = item.date;
  const ordine = useMemo(() => amesteca(d.variante.map((_, i) => i)), [item.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [ales, setAles] = useState<number | null>(null);
  useEffect(() => setAles(null), [item.id]);
  return (
    <div className="stiva">
      <DesenGrafic g={d.grafic} />
      <div className="variante">
        {ordine.map((i) => (
          <button key={i} disabled={verificat} aria-pressed={ales === i}
            className={`varianta ${verificat ? (i === d.corect ? 'corect' : i === ales ? 'gresit' : '') : ''}`}
            onClick={() => { setAles(i); onScor(i === d.corect ? 1 : 0); }}>
            {d.variante[i]}
          </button>
        ))}
      </div>
    </div>
  );
}
