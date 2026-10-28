import { geoMercator, geoNaturalEarth1, geoPath, geoGraticule10, type GeoProjection } from 'd3-geo';
import { feature } from 'topojson-client';
import type { FeatureCollection } from 'geojson';
import { useEffect, useMemo, useRef, useState, type ReactNode } from 'react';
import { incarca } from '../content';
import type { Harta } from '../types';

interface DateHarta { tari: FeatureCollection; ape?: FeatureCollection }

async function incarcaHarta(h: Harta): Promise<DateHarta> {
  if (h === 'lume') {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const topo = await incarca<any>('content/harti/lume-110m.json');
    return { tari: feature(topo, topo.objects.countries) as unknown as FeatureCollection };
  }
  const [tari, ape] = await Promise.all([
    incarca<FeatureCollection>('content/harti/romania-50m.geojson'),
    incarca<FeatureCollection>('content/harti/romania-ape-10m.geojson'),
  ]);
  return { tari, ape };
}

export const DIM: Record<Harta, [number, number]> = { lume: [800, 420], romania: [800, 560] };

export function useProiectie(h: Harta, date?: DateHarta): GeoProjection | null {
  return useMemo(() => {
    if (!date) return null;
    const [w, hgt] = DIM[h];
    if (h === 'lume') return geoNaturalEarth1().fitExtent([[8, 8], [w - 8, hgt - 8]], { type: 'Sphere' });
    const ro = date.tari.features.find((f) => f.properties?.id === 'RO')!;
    return geoMercator().fitExtent([[40, 30], [w - 40, hgt - 30]], ro);
  }, [h, date]);
}

export interface MapProps {
  harta: Harta;
  eticheta: string;
  onPick?: (lon: number, lat: number) => void;
  overlay?: (p: GeoProjection) => ReactNode;
  className?: string;
  /** suprascrie viewBox-ul (pentru zoom și deplasare) */
  viewBox?: string;
  /** straturi opționale: rețeaua geografică și apele */
  retea?: boolean;
  ape?: boolean;
}

/** Hartă mută SVG. Funcționează identic cu degetul, mouse-ul și creionul tablei (Pointer Events). */
export function MapView({ harta, eticheta, onPick, overlay, className, viewBox, retea = true, ape = true }: MapProps) {
  const [date, setDate] = useState<DateHarta>();
  const [eroare, setEroare] = useState<string>();
  const ref = useRef<SVGSVGElement>(null);
  useEffect(() => { incarcaHarta(harta).then(setDate).catch((e) => setEroare(String(e.message ?? e))); }, [harta]);
  const proj = useProiectie(harta, date);
  const [w, h] = DIM[harta];

  if (eroare) return <p role="alert">Harta nu s-a putut încărca. Verifică internetul și încearcă din nou.</p>;
  if (!date || !proj) return <div className="harta-ex" style={{ aspectRatio: `${w}/${h}` }} aria-busy="true" />;
  const path = geoPath(proj);

  const pick = (e: React.PointerEvent<SVGSVGElement>) => {
    if (!onPick || !ref.current) return;
    const pt = ref.current.createSVGPoint();
    pt.x = e.clientX; pt.y = e.clientY;
    const loc = pt.matrixTransform(ref.current.getScreenCTM()!.inverse());
    const ll = proj.invert?.([loc.x, loc.y]);
    if (ll && Number.isFinite(ll[0])) onPick(ll[0], ll[1]);
  };

  return (
    <svg
      ref={ref} viewBox={viewBox ?? `0 0 ${w} ${h}`} className={className ?? 'harta-ex'} role="img" aria-label={eticheta}
      onPointerUp={pick} style={{ cursor: onPick ? 'crosshair' : 'default' }}
    >
      {harta === 'lume' && <path d={path({ type: 'Sphere' }) ?? ''} fill="var(--apa)" />}
      {harta === 'lume' && retea && <path d={path(geoGraticule10()) ?? ''} fill="none" stroke="var(--linie)" strokeWidth={0.5} />}
      {harta === 'romania' && <rect width={w} height={h} fill="var(--apa)" />}
      <g>
        {date.tari.features.map((f, i) => {
          const ro = f.properties?.id === 'RO';
          return (
            <path
              key={i} d={path(f) ?? ''}
              fill={harta === 'romania' ? (ro ? 'var(--podis-pal)' : 'var(--hartie)') : 'var(--campie-pal)'}
              stroke={ro ? 'var(--munte)' : 'var(--linie)'} strokeWidth={ro ? 1.6 : 0.6} vectorEffect="non-scaling-stroke"
            />
          );
        })}
      </g>
      {date.ape && ape && (
        <g fill="none">
          {date.ape.features.map((f, i) => (
            <path
              key={i} d={path(f) ?? ''}
              stroke="var(--mare-2)" strokeWidth={f.properties?.tip === 'lac' ? 0.6 : 1.4} vectorEffect="non-scaling-stroke"
              fill={f.properties?.tip === 'lac' ? 'var(--apa)' : 'none'}
            />
          ))}
        </g>
      )}
      {overlay?.(proj)}
    </svg>
  );
}

/** Distanța în km între două puncte (formula haversine). */
export function distantaKm(a: { lat: number; lon: number }, b: { lat: number; lon: number }): number {
  const R = 6371;
  const rad = Math.PI / 180;
  const dLat = (b.lat - a.lat) * rad;
  const dLon = (b.lon - a.lon) * rad;
  const s = Math.sin(dLat / 2) ** 2 + Math.cos(a.lat * rad) * Math.cos(b.lat * rad) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(s));
}
