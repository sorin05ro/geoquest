import { useState } from 'react';
import { useApp } from '../state';
import { db } from '../db/db';
import { isoLocal } from '../calendar/calendar';
import { Geo } from '../ui/Geo';
import type { Clasa } from '../types';
import { citesteCodClasa } from '../profesor/sumar';

const AVATARE = ['🦉', '🦊', '🐻', '🦅', '🐺', '🦌', '🐢', '🐬'];
const SUGESTII = ['Busola Iute', 'Vulturul Carpatin', 'Exploratorul Nordului', 'Harta Vie', 'Cartograful Curios', 'Valul Albastru'];

/** Onboarding în 2 ecrane: clasa, apoi porecla și avatarul. Fără nume reale. */
export function Intrare() {
  const { scoala, mergi, cal, azi } = useApp();
  // dacă elevul a venit din codul QR al clasei (#clasa=5A-K7QM), clasa e deja aleasă
  const codDinLink = (() => { const m = location.hash.match(/^#clasa=([^&]*)/); return m ? decodeURIComponent(m[1]).toUpperCase() : null; })();
  const dinLink = codDinLink ? citesteCodClasa(codDinLink) : null;
  const [pas, setPas] = useState(0);
  const [clasa, setClasa] = useState<Clasa | null>(dinLink?.clasa ?? null);
  const [litera, setLitera] = useState<string>(dinLink?.litera ?? '');
  const [porecla, setPorecla] = useState(SUGESTII[Math.floor(Math.random() * SUGESTII.length)]);
  const [avatar, setAvatar] = useState(AVATARE[0]);

  const start = async () => {
    await db.profil.put({
      id: 'eu', porecla: porecla.trim().slice(0, 24), avatar, clasa: clasa!, litera, creat: isoLocal(new Date()), dificultate: 1,
      ...(dinLink && dinLink.clasa === clasa ? { codClasa: codDinLink! } : {}),
    });
    // primul exercițiu în sub 30 de secunde: deschidem direct lecția săptămânii, dacă are conținut
    const s = cal.planificare.filter((p) => p.clasa === clasa && p.niveluri.length && cal.saptamani[p.saptamana - 1].de <= azi).at(-1);
    mergi(s ? { e: 'nivel', id: s.niveluri[0] } : { e: 'harta' });
  };

  const clase = scoala.clase;
  return (
    <div className="bun-venit">
      {pas === 0 && (
        <>
          <div className="rand" style={{ flexWrap: 'nowrap' }}>
            <Geo marime={84} />
            <div><h1 style={{ margin: 0 }}>Salut, explorator!</h1><p style={{ margin: 0 }}>{dinLink ? `Eu sunt Geo. Intri în clasa cu codul ${codDinLink}.` : 'Eu sunt Geo. În ce clasă ești?'}</p></div>
          </div>
          <div className="variante" role="group" aria-label="Clasa">
            {clase.map((c) => (
              <button key={c.clasa} className="varianta" aria-pressed={clasa === c.clasa} onClick={() => { setClasa(c.clasa); setLitera(c.litere[0] ?? ''); }}>
                <b>Clasa a {({ 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' } as const)[c.clasa]}-a</b>
              </button>
            ))}
          </div>
          {clasa && (clase.find((c) => c.clasa === clasa)?.litere.length ?? 0) > 1 && (
            <div className="rand" role="group" aria-label="Litera clasei">
              {clase.find((c) => c.clasa === clasa)!.litere.map((l) => (
                <button key={l} className="varianta" style={{ minWidth: 72, textAlign: 'center' }} aria-pressed={litera === l} onClick={() => setLitera(l)}>{l}</button>
              ))}
            </div>
          )}
          <button className="buton" disabled={!clasa} onClick={() => setPas(1)}>Mai departe</button>
          <button className="buton secundar mic" onClick={() => mergi({ e: 'profesor' })}>Sunt profesor</button>
        </>
      )}
      {pas === 1 && (
        <>
          <h1>Alege-ți numele de explorator</h1>
          <label className="camp"><span>Poreclă (nu folosi numele tău real)</span>
            <input value={porecla} onChange={(e) => setPorecla(e.target.value)} maxLength={24} autoComplete="off" />
          </label>
          <div className="avatare" role="group" aria-label="Avatar">
            {AVATARE.map((a) => <button key={a} className="avatar" aria-pressed={avatar === a} onClick={() => setAvatar(a)} aria-label={`Avatar ${a}`}>{a}</button>)}
          </div>
          <div className="rand">
            <button className="buton secundar" onClick={() => setPas(0)}>Înapoi</button>
            <button className="buton" style={{ flex: 1 }} disabled={porecla.trim().length < 2} onClick={start}>Pornește în expediție</button>
          </div>
        </>
      )}
    </div>
  );
}
