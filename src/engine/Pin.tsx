import { useEffect, useState } from 'react';
import type { ItemPin } from '../types';
import { MapView, distantaKm } from '../maps/MapView';
import type { PropsTip } from './Exercitiu';

/** Tipul 1 – Localizează pe hartă: atinge locul cerut; punctaj după distanță. */
export function Pin({ item, verificat, onScor }: PropsTip<ItemPin>) {
  const [ales, setAles] = useState<{ lon: number; lat: number } | null>(null);
  const { tinta, toleranta, harta } = item.date;
  useEffect(() => setAles(null), [item.id]);

  const alege = (lon: number, lat: number) => {
    if (verificat) return;
    setAles({ lon, lat });
    const d = distantaKm({ lat, lon }, tinta);
    onScor(d <= toleranta ? 1 : d <= toleranta * 2 ? 0.5 : 0);
  };
  const dist = ales ? Math.round(distantaKm(ales, tinta)) : null;

  return (
    <div>
      <MapView
        harta={harta} onPick={alege}
        eticheta={`Hartă mută (${harta === 'lume' ? 'lumea' : 'România'}). Atinge locul cerut.`}
        overlay={(p) => (
          <>
            {ales && (() => {
              const [x, y] = p([ales.lon, ales.lat]) ?? [0, 0];
              return <g><path d={`M${x} ${y} l-10 -24 a10 10 0 1 1 20 0 z`} fill="var(--pion)" stroke="var(--hartie)" strokeWidth="2" /></g>;
            })()}
            {verificat && (() => {
              const [x, y] = p([tinta.lon, tinta.lat]) ?? [0, 0];
              return (
                <g>
                  <circle cx={x} cy={y} r="14" fill="none" stroke="var(--ok)" strokeWidth="4" />
                  <text x={x + 18} y={y + 6} fontSize="20" fontWeight="700" fill="var(--text)" style={{ paintOrder: 'stroke', stroke: 'var(--hartie)', strokeWidth: 5 }}>{tinta.nume}</text>
                </g>
              );
            })()}
          </>
        )}
      />
      <p className="eticheta-mica" aria-live="polite">
        {!ales ? 'Atinge harta în locul potrivit. Poți schimba alegerea până apeși „Verifică”.'
          : verificat ? `Ai fost la aproximativ ${dist} km de ${tinta.nume}.` : 'Pionul e pus. Apasă „Verifică”.'}
      </p>
    </div>
  );
}
