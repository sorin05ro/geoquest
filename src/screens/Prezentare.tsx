import { geoGraticule10, geoPath } from 'd3-geo';
import { useEffect, useMemo, useRef, useState } from 'react';
import { useApp } from '../state';
import { DIM, MapView } from '../maps/MapView';
import { continutClasa } from '../content';
import type { Clasa, Harta } from '../types';

interface PunctHarta { nume: string; lat: number; lon: number; clasa: number }

/** Harta de prezentare pentru predare, pe tablă: zoom (rotița, degetele sau butoanele), deplasare, straturi. */
export function Prezentare() {
  const { mergi } = useApp();
  const [harta, setHarta] = useState<Harta>('romania');
  const [retea, setRetea] = useState(true);
  const [ape, setApe] = useState(true);
  const [puncteAfis, setPuncteAfis] = useState(true);
  const [puncte, setPuncte] = useState<PunctHarta[]>([]);
  const [W, H] = DIM[harta];
  const [vb, setVb] = useState({ x: 0, y: 0, w: W, h: H });
  const pointeri = useRef(new Map<number, { x: number; y: number }>());
  const cutie = useRef<HTMLDivElement>(null);

  useEffect(() => { setVb({ x: 0, y: 0, w: DIM[harta][0], h: DIM[harta][1] }); }, [harta]);
  useEffect(() => {
    document.documentElement.dataset.mod = 'tabla';
    return () => { delete document.documentElement.dataset.mod; };
  }, []);
  // punctele din lecții: țintele itemilor de tip pin și etichete, fără duplicate
  useEffect(() => {
    Promise.all(([5, 6, 7, 8] as Clasa[]).map(continutClasa)).then((toate) => {
      const m = new Map<string, PunctHarta>();
      toate.forEach((c, i) => c.itemi.forEach((it) => {
        if (it.tip === 'pin') m.set(it.date.tinta.nume ?? it.id, { nume: it.date.tinta.nume ?? '', lat: it.date.tinta.lat, lon: it.date.tinta.lon, clasa: 5 + i });
        if (it.tip === 'etichete' && it.date.harta) it.date.tinte.forEach((t) => t.lat !== undefined && m.set(t.eticheta, { nume: t.eticheta, lat: t.lat, lon: t.lon!, clasa: 5 + i }));
      }));
      setPuncte([...m.values()]);
    });
  }, []);

  const zoom = (f: number, cx = vb.x + vb.w / 2, cy = vb.y + vb.h / 2) => {
    setVb((v) => {
      const w = Math.min(W, Math.max(W / 12, v.w * f));
      const h = w * (H / W);
      const x = Math.min(W - w, Math.max(0, cx - (cx - v.x) * (w / v.w)));
      const y = Math.min(H - h, Math.max(0, cy - (cy - v.y) * (h / v.h)));
      return { x, y, w, h };
    });
  };
  const laSvg = (clientX: number, clientY: number) => {
    const r = cutie.current!.getBoundingClientRect();
    return { x: vb.x + ((clientX - r.left) / r.width) * vb.w, y: vb.y + ((clientY - r.top) / r.height) * vb.h };
  };
  const jos = (e: React.PointerEvent) => { (e.target as Element).setPointerCapture?.(e.pointerId); pointeri.current.set(e.pointerId, { x: e.clientX, y: e.clientY }); };
  const misca = (e: React.PointerEvent) => {
    const p = pointeri.current;
    const vechi = p.get(e.pointerId);
    if (!vechi) return;
    const r = cutie.current!.getBoundingClientRect();
    if (p.size === 1) {
      const dx = ((e.clientX - vechi.x) / r.width) * vb.w, dy = ((e.clientY - vechi.y) / r.height) * vb.h;
      setVb((v) => ({ ...v, x: Math.min(W - v.w, Math.max(0, v.x - dx)), y: Math.min(H - v.h, Math.max(0, v.y - dy)) }));
    } else if (p.size === 2) {
      const [a, b] = [...p.values()];
      const altul = [...p.entries()].find(([k]) => k !== e.pointerId)![1];
      const d0 = Math.hypot(a.x - b.x, a.y - b.y);
      const d1 = Math.hypot(e.clientX - altul.x, e.clientY - altul.y);
      const c = laSvg((e.clientX + altul.x) / 2, (e.clientY + altul.y) / 2);
      if (d1 > 0) zoom(d0 / d1, c.x, c.y);
    }
    p.set(e.pointerId, { x: e.clientX, y: e.clientY });
  };
  const sus = (e: React.PointerEvent) => { pointeri.current.delete(e.pointerId); };

  const k = vb.w / W; // cât de mult e mărit
  const vizibile = useMemo(() => puncte, [puncte]);

  return (
    <div className="stiva mod-tabla">
      <div className="rand" style={{ justifyContent: 'space-between' }}>
        <h1 style={{ margin: 0 }}>Harta de prezentare</h1>
        <div className="rand">
          <button className="buton secundar mic" onClick={() => document.documentElement.requestFullscreen?.()}>Ecran complet</button>
          <button className="buton secundar mic" onClick={() => mergi({ e: 'profesor' })}>Închide</button>
        </div>
      </div>
      <div className="rand">
        <div className="rand" role="group" aria-label="Harta">
          <button className="varianta" aria-pressed={harta === 'romania'} onClick={() => setHarta('romania')}>România</button>
          <button className="varianta" aria-pressed={harta === 'lume'} onClick={() => setHarta('lume')}>Lumea</button>
        </div>
        <label className="bifa"><input type="checkbox" checked={puncteAfis} onChange={(e) => setPuncteAfis(e.target.checked)} /> Locuri din lecții</label>
        {harta === 'romania' && <label className="bifa"><input type="checkbox" checked={ape} onChange={(e) => setApe(e.target.checked)} /> Râuri și lacuri</label>}
        {harta === 'lume' && <label className="bifa"><input type="checkbox" checked={retea} onChange={(e) => setRetea(e.target.checked)} /> Paralele și meridiane</label>}
      </div>
      <div ref={cutie} style={{ position: 'relative', touchAction: 'none' }}
        onPointerDown={jos} onPointerMove={misca} onPointerUp={sus} onPointerCancel={sus}
        onWheel={(e) => { const c = laSvg(e.clientX, e.clientY); zoom(e.deltaY > 0 ? 1.2 : 1 / 1.2, c.x, c.y); }}>
        <MapView
          harta={harta} retea={retea} ape={ape} viewBox={`${vb.x} ${vb.y} ${vb.w} ${vb.h}`}
          eticheta={`Harta ${harta === 'lume' ? 'lumii' : 'României'}, mărită de ${Math.round(1 / k * 10) / 10} ori`}
          overlay={(p) => (
            <>
              {harta === 'romania' && retea && <path d={geoPath(p)(geoGraticule10()) ?? ''} fill="none" stroke="var(--linie)" strokeWidth={0.6 * k} />}
              {puncteAfis && vizibile.map((pt) => {
                const xy = p([pt.lon, pt.lat]);
                if (!xy) return null;
                const [x, y] = xy;
                if (x < 0 || y < 0 || x > W || y > H) return null;
                return (
                  <g key={pt.nume + pt.clasa}>
                    <circle cx={x} cy={y} r={6 * k} fill="var(--pion)" stroke="var(--hartie)" strokeWidth={2 * k} />
                    <text x={x + 9 * k} y={y + 5 * k} fontSize={15 * k} fontWeight="700" fill="var(--text)"
                      style={{ paintOrder: 'stroke', stroke: 'var(--hartie)', strokeWidth: 4 * k }}>{pt.nume}</text>
                  </g>
                );
              })}
            </>
          )}
        />
        <div style={{ position: 'absolute', right: 12, top: 12, display: 'flex', flexDirection: 'column', gap: 8 }}>
          <button className="buton-icon" onClick={() => zoom(1 / 1.5)} aria-label="Mărește">+</button>
          <button className="buton-icon" onClick={() => zoom(1.5)} aria-label="Micșorează">−</button>
          <button className="buton-icon" onClick={() => setVb({ x: 0, y: 0, w: W, h: H })} aria-label="Toată harta">⤢</button>
        </div>
      </div>
      <p className="eticheta-mica">Mărești cu două degete, cu rotița sau cu butoanele; muți harta trăgând de ea. Straturile de relief, climă și populație vin odată cu datele lor (Etapa 4–5).</p>
    </div>
  );
}
