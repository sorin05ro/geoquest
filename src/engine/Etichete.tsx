import { useEffect, useMemo, useRef, useState } from 'react';
import type { ItemEtichete } from '../types';
import { MapView } from '../maps/MapView';
import { SCHEME, Schema } from '../maps/Scheme';
import { amesteca } from '../content';
import type { PropsTip } from './Exercitiu';

/**
 * Tipul 3 – Plasează etichetele. Merge în două feluri, cu orice dispozitiv:
 * atingi eticheta, apoi ținta; sau tragi eticheta peste țintă.
 */
export function Etichete({ item, verificat, onScor }: PropsTip<ItemEtichete>) {
  const d = item.date;
  const jetoane = useMemo(
    () => amesteca([...d.tinte.map((t) => t.eticheta), ...(d.distractori ?? [])]),
    [item.id], // eslint-disable-line react-hooks/exhaustive-deps
  );
  const [plasate, setPlasate] = useState<Record<string, string>>({});
  const [selectat, setSelectat] = useState<string | null>(null);
  const [trag, setTrag] = useState<{ text: string; x: number; y: number } | null>(null);
  const startTrag = useRef<{ x: number; y: number; text: string } | null>(null);

  useEffect(() => { setPlasate({}); setSelectat(null); }, [item.id]);
  useEffect(() => {
    const n = Object.keys(plasate).length;
    if (n < d.tinte.length) { onScor(null); return; }
    const ok = d.tinte.filter((t) => plasate[t.id] === t.eticheta).length;
    onScor(ok / d.tinte.length);
  }, [plasate]); // eslint-disable-line react-hooks/exhaustive-deps

  const pune = (tinta: string, text: string) => {
    if (verificat) return;
    setPlasate((p) => {
      const nou = { ...p };
      for (const k of Object.keys(nou)) if (nou[k] === text) delete nou[k];
      nou[tinta] = text;
      return nou;
    });
    setSelectat(null);
  };
  const atingeTinta = (id: string) => {
    if (verificat) return;
    if (selectat) pune(id, selectat);
    else if (plasate[id]) setPlasate((p) => { const n = { ...p }; delete n[id]; return n; });
  };

  const folosite = new Set(Object.values(plasate));

  const marcaj = (id: string, x: number, y: number, nr: number) => {
    const text = plasate[id];
    const t = d.tinte.find((q) => q.id === id)!;
    const stare = verificat ? (text === t.eticheta ? 'var(--ok)' : 'var(--gresit)') : text ? 'var(--mare)' : 'var(--pion)';
    return (
      <g
        key={id} data-tinta={id} role="button" tabIndex={0} className="nod"
        aria-label={`Ținta ${nr}${text ? `: ${text}` : ', liberă'}`}
        onClick={() => atingeTinta(id)} onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && atingeTinta(id)}
      >
        <circle cx={x} cy={y} r="22" fill="transparent" />
        <circle className="nod-cerc" cx={x} cy={y} r="13" fill="var(--hartie)" stroke={stare} strokeWidth="4" />
        <text x={x} y={y + 5} textAnchor="middle" fontSize="14" fontWeight="700" fill="var(--text)">{nr}</text>
        {(text || verificat) && (
          <text
            x={x + 18} y={y - 14} fontSize="17" fontWeight="700" fill={stare}
            style={{ paintOrder: 'stroke', stroke: 'var(--hartie)', strokeWidth: 5 }}
          >
            {verificat && text !== t.eticheta ? `${t.eticheta}${text ? ` (nu ${text})` : ''}` : text}
          </text>
        )}
      </g>
    );
  };

  // tragerea etichetelor (Pointer Events: deget, mouse, creion)
  const jos = (e: React.PointerEvent, text: string) => {
    if (verificat) return;
    startTrag.current = { x: e.clientX, y: e.clientY, text };
    (e.target as Element).setPointerCapture?.(e.pointerId);
  };
  const misca = (e: React.PointerEvent) => {
    const s = startTrag.current;
    if (!s) return;
    if (trag || Math.hypot(e.clientX - s.x, e.clientY - s.y) > 10) setTrag({ text: s.text, x: e.clientX, y: e.clientY });
  };
  const sus = (e: React.PointerEvent) => {
    const s = startTrag.current;
    startTrag.current = null;
    if (!s) return;
    if (trag) {
      setTrag(null);
      const el = document.elementsFromPoint(e.clientX, e.clientY).map((x) => x.closest('[data-tinta]')).find(Boolean);
      const id = el?.getAttribute('data-tinta');
      if (id) pune(id, s.text);
    } else {
      setSelectat((x) => (x === s.text ? null : s.text));
    }
  };

  const zone = d.schema ? SCHEME[d.schema]?.zone ?? [] : [];
  return (
    <div className="stiva">
      {d.harta ? (
        <MapView
          harta={d.harta} eticheta="Hartă mută cu ținte numerotate"
          overlay={(p) => d.tinte.map((t, i) => { const [x, y] = p([t.lon!, t.lat!]) ?? [0, 0]; return marcaj(t.id, x, y, i + 1); })}
        />
      ) : d.schema ? (
        <Schema id={d.schema}>
          {d.tinte.map((t, i) => { const z = zone.find((q) => q.id === t.id); return z ? marcaj(t.id, z.x, z.y, i + 1) : null; })}
        </Schema>
      ) : null}
      <div className="rand" role="group" aria-label="Etichete de plasat">
        {jetoane.map((j) => (
          <button
            key={j} className={`jeton ${folosite.has(j) ? 'folosit' : ''}`} aria-pressed={selectat === j} disabled={verificat}
            onPointerDown={(e) => jos(e, j)} onPointerMove={misca} onPointerUp={sus}
            onKeyDown={(e) => (e.key === 'Enter' || e.key === ' ') && (e.preventDefault(), setSelectat((x) => (x === j ? null : j)))}
          >
            {j}
          </button>
        ))}
      </div>
      <p className="eticheta-mica">
        {selectat ? `Acum atinge ținta pentru „${selectat}”.` : 'Atinge o etichetă, apoi ținta ei. Sau trage eticheta peste țintă.'}
      </p>
      {trag && <div className="jeton fantoma" style={{ left: trag.x, top: trag.y }}>{trag.text}</div>}
    </div>
  );
}
