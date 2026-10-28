// Scheme desenate pentru GeoQuest (originale, nu copiate din manuale).
// Fiecare schemă are zone cu id, ca să poată fi evidențiate sau folosite ca ținte pentru etichete.

import type { ReactNode } from 'react';

export interface ZonaSchema { id: string; x: number; y: number }
export interface DefSchema { viewBox: string; eticheta: string; zone: ZonaSchema[]; desen: (ev?: string) => ReactNode }

const ev = (id: string, e?: string) => (e === id ? { stroke: 'var(--pion)', strokeWidth: 5 } : {});

export const SCHEME: Record<string, DefSchema> = {
  'structura-interna': {
    viewBox: '0 0 400 300',
    eticheta: 'Secțiune prin Pământ: scoarța, mantaua, nucleul extern și nucleul intern',
    zone: [
      { id: 'scoarta', x: 330, y: 60 }, { id: 'manta', x: 300, y: 110 },
      { id: 'nucleu-extern', x: 250, y: 170 }, { id: 'nucleu-intern', x: 200, y: 230 },
    ],
    desen: (e) => (
      <g>
        <circle cx="200" cy="300" r="250" fill="var(--munte)" {...ev('scoarta', e)} />
        <circle cx="200" cy="300" r="238" fill="#e0703a" {...ev('manta', e)} />
        <circle cx="200" cy="300" r="135" fill="#f2a93b" {...ev('nucleu-extern', e)} />
        <circle cx="200" cy="300" r="70" fill="#ffd866" {...ev('nucleu-intern', e)} />
      </g>
    ),
  },
  'fund-oceanic': {
    viewBox: '0 0 600 260',
    eticheta: 'Profil prin marginea unui continent și fundul oceanului',
    zone: [
      { id: 'platforma', x: 120, y: 92 }, { id: 'abrupt', x: 205, y: 150 },
      { id: 'campie-abisala', x: 330, y: 214 }, { id: 'dorsala', x: 450, y: 150 }, { id: 'groapa', x: 560, y: 245 },
    ],
    desen: (e) => (
      <g>
        <rect width="600" height="260" fill="var(--apa)" />
        <rect width="600" height="70" fill="var(--hartie)" />
        <path d="M0 50 L60 52 L80 70 L180 82 L230 200 L400 205 L430 160 L455 120 L480 160 L520 205 L545 255 L570 205 L600 200 L600 260 L0 260 Z" fill="var(--munte)" opacity=".85" />
        <path d="M0 50 L60 52 L80 70" stroke="var(--campie)" strokeWidth="6" fill="none" />
        <g fill="none">
          <path d="M80 70 L180 82" stroke="transparent" strokeWidth="18" {...ev('platforma', e)} />
          <path d="M180 82 L230 200" stroke="transparent" strokeWidth="18" {...ev('abrupt', e)} />
          <path d="M230 200 L400 205" stroke="transparent" strokeWidth="18" {...ev('campie-abisala', e)} />
          <path d="M430 160 L455 120 L480 160" stroke="transparent" strokeWidth="18" {...ev('dorsala', e)} />
          <path d="M520 205 L545 255 L570 205" stroke="transparent" strokeWidth="18" {...ev('groapa', e)} />
        </g>
        <line x1="0" y1="70" x2="600" y2="70" stroke="var(--mare-2)" strokeDasharray="6 6" />
        <text x="10" y="28" fontSize="14" fill="var(--text-2)">uscat</text>
        <text x="300" y="100" fontSize="14" fill="var(--mare)">ocean</text>
      </g>
    ),
  },
  vulcan: {
    viewBox: '0 0 400 300',
    eticheta: 'Secțiune printr-un vulcan',
    zone: [
      { id: 'camera', x: 200, y: 270 }, { id: 'cos', x: 200, y: 180 }, { id: 'crater', x: 200, y: 88 },
      { id: 'con', x: 290, y: 190 }, { id: 'nor', x: 260, y: 30 },
    ],
    desen: (e) => (
      <g>
        <rect width="400" height="300" fill="var(--apa)" />
        <rect y="240" width="400" height="60" fill="var(--munte)" opacity=".5" />
        <path d="M40 240 L180 92 L220 92 L360 240 Z" fill="var(--munte)" {...ev('con', e)} />
        <rect x="192" y="96" width="16" height="160" fill="#e0703a" {...ev('cos', e)} />
        <ellipse cx="200" cy="268" rx="70" ry="20" fill="#e0703a" {...ev('camera', e)} />
        <path d="M180 92 Q200 108 220 92" fill="#f2a93b" {...ev('crater', e)} />
        <g {...ev('nor', e)}>
          <circle cx="210" cy="50" r="22" fill="var(--ceata)" /><circle cx="240" cy="36" r="18" fill="var(--ceata)" />
          <circle cx="270" cy="30" r="14" fill="var(--ceata)" />
        </g>
      </g>
    ),
  },
  busola: {
    viewBox: '0 0 300 300',
    eticheta: 'Roza vânturilor cu punctele cardinale și intermediare',
    zone: [
      { id: 'N', x: 150, y: 40 }, { id: 'NE', x: 228, y: 72 }, { id: 'E', x: 260, y: 150 }, { id: 'SE', x: 228, y: 228 },
      { id: 'S', x: 150, y: 260 }, { id: 'SV', x: 72, y: 228 }, { id: 'V', x: 40, y: 150 }, { id: 'NV', x: 72, y: 72 },
    ],
    desen: (e) => (
      <g>
        <circle cx="150" cy="150" r="140" fill="var(--suprafata)" stroke="var(--linie)" strokeWidth="2" />
        <path d="M150 20 L168 150 L150 280 L132 150 Z" fill="var(--mare)" />
        <path d="M150 20 L168 150 L132 150 Z" fill="var(--pion)" />
        <path d="M20 150 L150 132 L280 150 L150 168 Z" fill="var(--mare-2)" opacity=".7" />
        <path d="M58 58 L157 143 L242 242 L143 157 Z M242 58 L157 157 L58 242 L143 143 Z" fill="var(--ceata)" opacity=".8" />
        <circle cx="150" cy="150" r="8" fill="var(--hartie)" stroke="var(--mare)" strokeWidth="3" />
        {e && <circle cx={SCHEME_BUSOLA_POZ[e]?.[0]} cy={SCHEME_BUSOLA_POZ[e]?.[1]} r="18" fill="none" stroke="var(--pion)" strokeWidth="5" />}
      </g>
    ),
  },
  'umbra-amiaza': {
    viewBox: '0 0 400 220',
    eticheta: 'Un băț înfipt în pământ la prânz, în emisfera nordică, cu umbra lui',
    zone: [{ id: 'umbra', x: 200, y: 150 }, { id: 'soare', x: 330, y: 60 }],
    desen: (e) => (
      <g>
        <rect width="400" height="160" fill="var(--apa)" /><rect y="160" width="400" height="60" fill="var(--campie-pal)" />
        <circle cx="330" cy="50" r="28" fill="var(--podis)" {...ev('soare', e)} />
        <line x1="200" y1="160" x2="200" y2="80" stroke="var(--munte)" strokeWidth="6" />
        <path d="M200 160 L80 172" stroke="#7a8794" strokeWidth="10" strokeLinecap="round" {...ev('umbra', e)} />
      </g>
    ),
  },
};

const SCHEME_BUSOLA_POZ: Record<string, [number, number]> = {
  N: [150, 40], NE: [228, 72], E: [260, 150], SE: [228, 228], S: [150, 260], SV: [72, 228], V: [40, 150], NV: [72, 72],
};

export function Schema({ id, evidentiat, children }: { id: string; evidentiat?: string; children?: ReactNode }) {
  const s = SCHEME[id];
  if (!s) return null;
  return (
    <svg viewBox={s.viewBox} className="harta-ex" role="img" aria-label={s.eticheta}>
      {s.desen(evidentiat)}
      {children}
    </svg>
  );
}
