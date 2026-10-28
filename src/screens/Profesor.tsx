import { useEffect, useState } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { useApp } from '../state';
import { citesteSetare, db, scrieSetare } from '../db/db';
import { formatData } from '../calendar/calendar';
import { ProfCalendar } from '../profesor/ProfCalendar';
import { ProfClase } from '../profesor/ProfClase';
import { ProfRezultate } from '../profesor/ProfRezultate';
import { ProfEditor } from '../profesor/ProfEditor';
import { ProfPlanificare } from '../profesor/ProfPlanificare';

async function hash(t: string) {
  const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode('geoquest:' + t));
  return [...new Uint8Array(b)].map((x) => x.toString(16).padStart(2, '0')).join('');
}

const FILE = [
  { id: 'calendar', nume: 'Calendar' },
  { id: 'clase', nume: 'Clase și teme' },
  { id: 'rezultate', nume: 'Rezultate' },
  { id: 'continut', nume: 'Conținut' },
  { id: 'planificare', nume: 'Planificare' },
  { id: 'jurnal', nume: 'Jurnal' },
] as const;
type Fila = (typeof FILE)[number]['id'];

// PIN-ul rămâne valabil cât e deschisă aplicația, ca să nu-l tastezi la fiecare schimbare de ecran
let deblocatInSesiune = false;

/** Modul profesor: PIN, apoi file pentru calendar, clase și teme, rezultate, conținut, planificare, jurnal. */
export function Profesor() {
  const { cal, mergi, profil } = useApp();
  const [intrat, setIntrat] = useState(deblocatInSesiune);
  const [pinSalvat, setPinSalvat] = useState<string | null | undefined>(undefined);
  const [pin, setPin] = useState('');
  const [mesaj, setMesaj] = useState('');
  const [fila, setFila] = useState<Fila>('calendar');
  const jurnal = useLiveQuery(() => db.jurnal.toArray(), [], []);

  useEffect(() => { citesteSetare<string | null>('pinProfesor', null).then(setPinSalvat); }, []);
  useEffect(() => { citesteSetare<Fila>('filaProfesor', 'calendar').then(setFila); }, []);
  const alegeFila = (f: Fila) => { setFila(f); scrieSetare('filaProfesor', f); };

  if (pinSalvat === undefined) return null;
  if (!intrat) {
    return (
      <form className="bun-venit" onSubmit={async (e) => {
        e.preventDefault();
        if (pin.length < 4) { setMesaj('PIN-ul are cel puțin 4 cifre.'); return; }
        const h = await hash(pin);
        if (pinSalvat === null) { await scrieSetare('pinProfesor', h); deblocatInSesiune = true; setIntrat(true); return; }
        if (h === pinSalvat) { deblocatInSesiune = true; setIntrat(true); } else setMesaj('PIN greșit. Încearcă din nou.');
      }}>
        <h1>Modul profesor</h1>
        <p>{pinSalvat === null ? 'Alege un PIN de profesor pentru acest dispozitiv (cel puțin 4 cifre).' : 'Introdu PIN-ul de profesor.'}</p>
        <label className="camp"><span>PIN</span>
          <input type="password" inputMode="numeric" autoComplete="off" value={pin} onChange={(e) => setPin(e.target.value.replace(/\D/g, ''))} autoFocus />
        </label>
        {mesaj && <p role="alert" className="feedback nu">{mesaj}</p>}
        <div className="rand">
          <button type="button" className="buton secundar" onClick={() => mergi({ e: profil ? 'harta' : 'intrare' })}>Înapoi</button>
          <button className="buton">{pinSalvat === null ? 'Salvează PIN-ul' : 'Intră'}</button>
        </div>
      </form>
    );
  }

  const titlu = (id: string) => cal.niveluri.find((n) => n.id === id)?.titlu ?? id;
  return (
    <div className="stiva">
      <div className="rand antet-profesor" style={{ justifyContent: 'space-between' }}>
        <h1 style={{ margin: 0 }}>Modul profesor</h1>
        <div className="rand">
          <button className="buton" onClick={() => mergi({ e: 'live-gazda' })}>Joc live cu telefoane</button>
          <button className="buton secundar" onClick={() => mergi({ e: 'tabla' })}>Turul geografic (fără telefoane)</button>
          <button className="buton secundar" onClick={() => mergi({ e: 'prezentare' })}>Harta de prezentare</button>
          <button className="buton secundar" onClick={() => { deblocatInSesiune = false; mergi({ e: profil ? 'harta' : 'intrare' }); }}>Ieși</button>
        </div>
      </div>
      <div className="file" role="tablist" aria-label="Secțiuni">
        {FILE.map((f) => <button key={f.id} role="tab" aria-selected={fila === f.id} onClick={() => alegeFila(f.id)}>{f.nume}</button>)}
      </div>
      <div role="tabpanel">
        {fila === 'calendar' && <ProfCalendar />}
        {fila === 'clase' && <ProfClase />}
        {fila === 'rezultate' && <ProfRezultate />}
        {fila === 'continut' && <ProfEditor />}
        {fila === 'planificare' && <ProfPlanificare />}
        {fila === 'jurnal' && (
          <div className="card stiva">
            <h2>Jurnalul exploratorului (acest dispozitiv)</h2>
            <p className="eticheta-mica">Aici apar lucrările din expedițiile făcute pe acest dispozitiv (de exemplu, tableta clasei).</p>
            {jurnal.length === 0 && <p className="eticheta-mica">Încă nu sunt intrări.</p>}
            {jurnal.map((j) => (
              <div key={j.id} className="feedback ok">
                <strong>{titlu(j.nivel).slice(0, 60)} · {formatData(j.data)}</strong>
                <p>{j.text}</p>
                {j.foto && <img src={URL.createObjectURL(j.foto)} alt="Lucrarea elevului" style={{ maxWidth: 240, borderRadius: 8 }} />}
                <label className="bifa"><input type="checkbox" checked={!!j.validat} onChange={(e) => db.jurnal.update(j.id!, { validat: e.target.checked })} /> Validat de profesor</label>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
