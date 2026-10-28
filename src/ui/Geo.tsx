/** Geo, bufnița-cartograf: mascota originală a aplicației. */
export function Geo({ marime = 56, stare = 'normal' }: { marime?: number; stare?: 'normal' | 'bucuros' | 'gandeste' }) {
  const ochi = stare === 'bucuros'
    ? <><path d="M30 44 q6 -7 12 0" /><path d="M58 44 q6 -7 12 0" /></>
    : <><circle cx="36" cy="44" r="5" fill="var(--mare)" stroke="none" /><circle cx="64" cy="44" r="5" fill="var(--mare)" stroke="none" /></>;
  return (
    <svg className="geo" width={marime} height={marime} viewBox="0 0 100 100" aria-hidden="true">
      {/* corp */}
      <path d="M50 12 C76 12 86 34 86 58 C86 82 70 94 50 94 C30 94 14 82 14 58 C14 34 24 12 50 12 Z" fill="var(--munte)" />
      <path d="M28 20 L22 6 L38 16 Z M72 20 L78 6 L62 16 Z" fill="var(--munte)" />
      {/* burta cu curbe de nivel */}
      <path d="M50 52 C68 52 74 66 74 76 C74 88 62 92 50 92 C38 92 26 88 26 76 C26 66 32 52 50 52 Z" fill="var(--podis-pal)" />
      <g fill="none" stroke="var(--podis)" strokeWidth="2">
        <path d="M36 70 C42 77 58 77 64 70" /><path d="M41 79 C46 84 54 84 59 79" />
      </g>
      {/* fața */}
      <circle cx="36" cy="44" r="13" fill="var(--hartie)" />
      <circle cx="64" cy="44" r="13" fill="var(--hartie)" />
      <g fill="none" stroke="var(--mare)" strokeWidth="3" strokeLinecap="round">{ochi}</g>
      <path d="M46 54 L50 62 L54 54 Z" fill="var(--podis)" />
      {/* pionul de hartă ținut sub aripă */}
      {stare === 'gandeste'
        ? <text x="78" y="22" fontSize="22" fill="var(--pion)" fontWeight="700">?</text>
        : <path d="M84 52 l-6 -14 a6 6 0 1 1 12 0 z" fill="var(--pion)" />}
    </svg>
  );
}
