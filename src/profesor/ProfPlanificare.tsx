import { useState } from 'react';
import { useApp } from '../state';
import { citesteSetare, scrieSetare } from '../db/db';
import { incarca, incarcaCompetente } from '../content';
import { SABLON_CSV, genereazaCalendar, tabeleDinCsv, tabeleDinDocx, type Corecturi } from '../calendar/import';
import type { Calendar } from '../types';

const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };

function descarca(nume: string, text: string, tip: string) {
  const url = URL.createObjectURL(new Blob([text], { type: tip }));
  const a = document.createElement('a'); a.href = url; a.download = nume; a.click();
}

/** Fila „Planificare”: importul planificării (.docx sau CSV), direct în aplicație. */
export function ProfPlanificare() {
  const { cal, reincarca } = useApp();
  const [nou, setNou] = useState<Calendar | null>(null);
  const [eroare, setEroare] = useState('');
  const [nume, setNume] = useState('');
  const [local, setLocal] = useState<boolean | null>(null);
  if (local === null) citesteSetare<Calendar | null>('calendarLocal', null).then((c) => setLocal(!!c));

  const incarcaFisier = async (f: File) => {
    setEroare(''); setNou(null); setNume(f.name);
    try {
      const [comp, corecturi] = await Promise.all([incarcaCompetente(), incarca<Corecturi>('config/corecturi.json').catch(() => ({}))]);
      const tabele = f.name.toLowerCase().endsWith('.docx') ? tabeleDinDocx(new Uint8Array(await f.arrayBuffer())) : tabeleDinCsv(await f.text());
      if (tabele.length < 4) throw new Error(`Am găsit ${tabele.length} tabele; planificarea trebuie să aibă câte un tabel pentru fiecare clasă (V, VI, VII, VIII), în această ordine.`);
      const an = { an: cal.an, intervale: cal.intervale, vacante: cal.vacante, zileLibere: cal.zileLibere, evenimente: cal.evenimente, ultimaZi: cal.ultimaZi };
      const c = genereazaCalendar(tabele, an, comp as Record<string, Record<string, string>>, corecturi, f.name);
      if (!c.niveluri.length) throw new Error('Nu am găsit lecții. Verifică dacă tabelul are coloanele: unitate | competențe | conținuturi | ore | săptămâna | evaluare.');
      setNou(c);
    } catch (e) { setEroare(e instanceof Error ? e.message : String(e)); }
  };

  const rezumat = (c: Calendar, clasa: number) => {
    const r = c.planificare.filter((p) => p.clasa === clasa);
    return { saptamani: r.length, lectii: c.niveluri.filter((n) => n.clasa === clasa).length, teste: r.filter((p) => p.test).map((p) => `${p.test} (S${p.saptamana})`).join(', ') };
  };
  const diferente = nou ? nou.planificare.filter((p) => JSON.stringify(p) !== JSON.stringify(cal.planificare.find((q) => q.clasa === p.clasa && q.saptamana === p.saptamana))).length : 0;

  return (
    <div className="stiva">
      <div className="card stiva">
        <h2>Importă planificarea</h2>
        <p>Alege fișierul .docx al planificării (câte un tabel pe clasă, în ordinea V, VI, VII, VIII, cu coloanele unitate | competențe | conținuturi | ore | săptămâna | evaluare) sau un fișier CSV după șablon.</p>
        <p className="eticheta-mica">Structura anului (intervale, vacanțe, zile libere) rămâne cea din {cal.an}. Pentru alt an școlar se schimbă în tools/import_planificare.py.</p>
        <div className="rand">
          <label className="buton">Alege fișierul<input type="file" accept=".docx,.csv" className="ascuns" onChange={(e) => e.target.files?.[0] && incarcaFisier(e.target.files[0])} /></label>
          <button className="buton secundar mic" onClick={() => descarca('sablon-planificare.csv', SABLON_CSV, 'text/csv;charset=utf-8')}>Descarcă șablonul CSV</button>
        </div>
        {local && (
          <p className="feedback nu"><strong>Pe acest dispozitiv folosești o planificare importată</strong>
            <button className="buton secundar mic" onClick={async () => { await scrieSetare('calendarLocal', null); setLocal(false); location.reload(); }}>Revino la calendarul publicat</button>
          </p>
        )}
        {eroare && <p className="feedback nu" role="alert">{eroare}</p>}
      </div>

      {nou && (
        <div className="card stiva">
          <h2>Rezultatul importului: {nume}</h2>
          <table className="tabel">
            <thead><tr><th>Clasa</th><th>Săptămâni</th><th>Lecții</th><th>Teste</th></tr></thead>
            <tbody>
              {[5, 6, 7, 8].map((c) => { const r = rezumat(nou, c); return <tr key={c}><td>a {ROMAN[c]}-a</td><td>{r.saptamani}</td><td>{r.lectii}</td><td className="eticheta-mica">{r.teste}</td></tr>; })}
            </tbody>
          </table>
          <p>{diferente ? `${diferente} săptămâni diferă de calendarul publicat acum.` : 'Identic cu calendarul publicat acum.'}</p>
          {nou.observatii.length > 0 && <><h3>Observații</h3><ul>{nou.observatii.map((o) => <li key={o}>{o}</li>)}</ul></>}
          <p className="eticheta-mica">
            „Folosește pe acest dispozitiv” schimbă calendarul doar aici (bun pentru probă). Ca să ajungă la elevi, descarcă fișierul, pune-l în proiect
            în locul lui public/calendar/2026-2027.json și publică. Atenție: dacă se schimbă lecțiile, se schimbă și id-urile nivelurilor din conținut.
          </p>
          <div className="rand">
            <button className="buton" onClick={async () => { await scrieSetare('calendarLocal', nou); reincarca(); location.reload(); }}>Folosește pe acest dispozitiv</button>
            <button className="buton secundar" onClick={() => descarca('2026-2027.json', JSON.stringify(nou, null, 1), 'application/json')}>Descarcă calendarul</button>
          </div>
        </div>
      )}
    </div>
  );
}
