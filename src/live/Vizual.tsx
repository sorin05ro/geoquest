import { geoAzimuthalEqualArea, geoGraticule10, geoPath } from 'd3-geo';
import { feature } from 'topojson-client';
import type { FeatureCollection } from 'geojson';
import { useEffect, useState } from 'react';
import { MapView } from '../maps/MapView';
import { Schema } from '../maps/Scheme';
import { DesenGrafic } from '../engine/Grafic';
import { incarca } from '../content';
import type { Punct } from '../types';
import { SIMBOLURI, type ItemPublic } from './protocol';

/** Partea vizuală a unei întrebări (hartă, schemă sau grafic), afișată pe tablă. */
export function VizualIntrebare({ it, tinta }: { it: ItemPublic; tinta?: Punct }) {
  if (it.grafic) return <DesenGrafic g={it.grafic} />;
  if (it.schema) return <Schema id={it.schema} evidentiat={it.evidentiat} />;
  if (it.harta) {
    return (
      <MapView
        harta={it.harta} eticheta="Harta întrebării"
        overlay={(p) => (
          <>
            {it.punct && (() => { const [x, y] = p([it.punct.lon, it.punct.lat]) ?? [0, 0]; return <g><circle cx={x} cy={y} r="18" fill="none" stroke="var(--pion)" strokeWidth="4" /><circle cx={x} cy={y} r="5" fill="var(--pion)" /></g>; })()}
            {tinta && (() => { const [x, y] = p([tinta.lon, tinta.lat]) ?? [0, 0]; return <g><circle cx={x} cy={y} r="16" fill="none" stroke="var(--ok)" strokeWidth="5" /><text x={x + 20} y={y + 7} fontSize="22" fontWeight="700" fill="var(--text)" style={{ paintOrder: 'stroke', stroke: 'var(--hartie)', strokeWidth: 5 }}>{tinta.nume}</text></g>; })()}
          </>
        )}
      />
    );
  }
  return null;
}

/** Butoanele de răspuns: simbol + literă + text (nu doar culoare). */
export function VarianteLive({ variante, ales, corect, distributie, onAlege, dezactivat }: {
  variante: string[]; ales?: number | null; corect?: number; distributie?: number[]; onAlege?: (i: number) => void; dezactivat?: boolean;
}) {
  const total = distributie?.reduce((a, b) => a + b, 0) ?? 0;
  return (
    <div className="variante">
      {variante.map((v, i) => {
        const cls = corect === undefined ? '' : i === corect ? 'corect' : i === ales ? 'gresit' : '';
        return (
          <button key={i} className={`varianta ${cls}`} aria-pressed={ales === i} disabled={dezactivat || !onAlege} onClick={() => onAlege?.(i)}
            style={{ display: 'flex', gap: 12, alignItems: 'center', minHeight: 72 }}>
            <span aria-hidden="true" style={{ fontSize: '1.3em', color: 'var(--mare-2)' }}>{SIMBOLURI.at(i)}</span>
            <b>{String.fromCharCode(65 + i)}.</b>
            <span style={{ flex: 1 }}>{v}</span>
            {distributie && <span className="eticheta-mica">{distributie.at(i) ?? 0}{total ? ` (${Math.round(((distributie.at(i) ?? 0) / total) * 100)} %)` : ''}</span>}
          </button>
        );
      })}
    </div>
  );
}

/** Harta polară colectivă: fiecare răspuns corect al clasei ridică ceața de pe o bucată din Antarctica. */
export function HartaPolara({ dezvaluite, total }: { dezvaluite: number; total: number }) {
  const [tari, setTari] = useState<FeatureCollection>();
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    incarca<any>('content/harti/lume-110m.json').then((t) => setTari(feature(t, t.objects.countries) as unknown as FeatureCollection));
  }, []);
  const W = 420;
  const proj = geoAzimuthalEqualArea().rotate([0, 90]).clipAngle(50).fitExtent([[10, 10], [W - 10, W - 10]], { type: 'Sphere' });
  const path = geoPath(proj);
  const n = 6, c = W / n;
  // ordine împrăștiată, dar mereu aceeași (17 și 37 sunt prime între ele)
  // doar celulele care ating cercul hărții contează
  const celule = Array.from({ length: n * n }, (_, i) => i)
    .filter((i) => Math.hypot((i % n + 0.5) * c - W / 2, (Math.floor(i / n) + 0.5) * c - W / 2) < W / 2 - 10 + c * 0.35);
  const ordine = [...celule].sort((a, b) => ((a * 17) % 37) - ((b * 17) % 37));
  const vazute = new Set(ordine.slice(0, Math.round((dezvaluite / Math.max(1, total)) * celule.length)));
  const proc = Math.round((vazute.size / celule.length) * 100);
  return (
    <figure style={{ margin: 0, textAlign: 'center' }}>
      <svg viewBox={`0 0 ${W} ${W}`} style={{ width: '100%', maxWidth: 420 }} role="img" aria-label={`Harta polară colectivă, descoperită ${proc} %`}>
        <circle cx={W / 2} cy={W / 2} r={W / 2 - 10} fill="var(--apa)" />
        <path d={path(geoGraticule10()) ?? ''} fill="none" stroke="var(--linie)" strokeWidth="0.6" />
        {tari?.features.map((f, i) => <path key={i} d={path(f) ?? ''} fill={f.properties?.name === 'Antarctica' ? 'var(--hartie)' : 'var(--campie-pal)'} stroke="var(--mare-2)" strokeWidth="0.8" />)}
        <circle cx={W / 2} cy={W / 2} r="5" fill="var(--pion)" />
        <defs><clipPath id="cerc-polar"><circle cx={W / 2} cy={W / 2} r={W / 2 - 10} /></clipPath></defs>
        <g clipPath="url(#cerc-polar)">
          {celule.map((i) => !vazute.has(i) && (
            <rect key={i} x={(i % n) * c} y={Math.floor(i / n) * c} width={c + 0.5} height={c + 0.5} fill="var(--ceata)" opacity=".94" />
          ))}
        </g>
      </svg>
      <figcaption><b>Harta Polară: {proc} % descoperită</b><br /><span className="eticheta-mica">Fiecare răspuns corect al clasei ridică ceața de pe o bucată.</span></figcaption>
    </figure>
  );
}

/** Pădurea colectivă a Patrulei Verzi: fiecare răspuns corect al clasei face să crească un copac în curtea școlii. */
export function PadureVerde({ dezvaluite, total }: { dezvaluite: number; total: number }) {
  const W = 420, H = 260, n = 30;
  // locuri fixe, împrăștiate, pentru copaci (aceeași ordine la fiecare joc)
  const locuri = Array.from({ length: n }, (_, i) => {
    const r = (i * 17) % 37;
    return { x: 26 + ((r * 53) % 368), y: 110 + ((r * 29) % 120), s: 0.75 + ((r * 7) % 5) / 10 };
  }).sort((a, b) => a.y - b.y);
  const cate = Math.round((dezvaluite / Math.max(1, total)) * n);
  const ordine = locuri.map((_, i) => i).sort((a, b) => ((a * 17) % 37) - ((b * 17) % 37));
  const crescuti = new Set(ordine.slice(0, cate));
  const proc = Math.round((cate / n) * 100);
  return (
    <figure style={{ margin: 0, textAlign: 'center' }}>
      <svg viewBox={`0 0 ${W} ${H}`} style={{ width: '100%', maxWidth: 420 }} role="img" aria-label={`Pădurea colectivă, ${cate} copaci din ${n}`}>
        <rect width={W} height={H} rx="14" fill="var(--apa)" opacity=".35" />
        <path d={`M0 ${H * 0.42} Q ${W * 0.3} ${H * 0.32} ${W * 0.55} ${H * 0.4} T ${W} ${H * 0.36} V ${H} H 0 Z`} fill="var(--campie-pal)" />
        <rect x={W / 2 - 46} y={H * 0.2} width="92" height="44" fill="var(--hartie)" stroke="var(--mare-2)" strokeWidth="2" />
        <path d={`M${W / 2 - 54} ${H * 0.2} L${W / 2} ${H * 0.08} L${W / 2 + 54} ${H * 0.2} Z`} fill="var(--munte)" />
        <text x={W / 2} y={H * 0.2 + 28} textAnchor="middle" fontSize="13" fontWeight="700" fill="var(--text)">ȘCOALA</text>
        {locuri.map((l, i) => (
          <g key={i} transform={`translate(${l.x} ${l.y}) scale(${l.s})`}>
            {crescuti.has(i) ? (
              <>
                <rect x="-3" y="0" width="6" height="16" fill="var(--munte)" />
                <circle cx="0" cy="-8" r="14" fill="var(--campie)" stroke="var(--mare-2)" strokeWidth="1" />
                <circle cx="-7" cy="-2" r="8" fill="var(--campie)" />
                <circle cx="7" cy="-2" r="8" fill="var(--campie)" />
              </>
            ) : (
              <circle cx="0" cy="12" r="3" fill="var(--munte)" opacity=".6" />
            )}
          </g>
        ))}
      </svg>
      <figcaption><b>Pădurea Patrulei Verzi: {cate} copaci ({proc} %)</b><br /><span className="eticheta-mica">Fiecare răspuns corect al clasei plantează un copac.</span></figcaption>
    </figure>
  );
}

/** Vizualul colectiv al evenimentului: harta polară sau pădurea verde. */
export function VizualColectiv({ dezvaluite, total, tema }: { dezvaluite: number; total: number; tema?: 'polara' | 'verde' }) {
  return tema === 'verde' ? <PadureVerde dezvaluite={dezvaluite} total={total} /> : <HartaPolara dezvaluite={dezvaluite} total={total} />;
}
