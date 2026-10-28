import { useEffect, useState } from 'react';
import { useApp } from '../state';
import { citesteSetare, scrieSetare } from '../db/db';
import { formatData, niveluriDeblocate, randuriClasa, saptamanaDeblocata, type Suprascrieri } from '../calendar/calendar';
import type { Clasa } from '../types';

/** Fila „Calendar”: data de probă, calendarul pe clase, deblocarea manuală, observațiile din planificare. */
export function ProfCalendar() {
  const { cal, azi, reincarca, profil, continut } = useApp();
  const [clasa, setClasa] = useState<Clasa>(profil?.clasa ?? 5);
  const [supr, setSupr] = useState<Suprascrieri>({ deblocate: [], blocate: [] });
  const [data, setData] = useState('');
  useEffect(() => { citesteSetare<Suprascrieri>(`suprascrieri-${clasa}`, { deblocate: [], blocate: [] }).then(setSupr); }, [clasa]);
  useEffect(() => { citesteSetare<string | null>('dataSimulata', null).then((d) => setData(d ?? '')); }, []);
  const [modEN, setModEN] = useState<boolean | null>(null);
  useEffect(() => { citesteSetare<boolean | null>('modEN', null).then(setModEN); }, []);

  const s = saptamanaDeblocata(cal, clasa, azi);
  const deschise = niveluriDeblocate(cal, clasa, azi, supr);
  const seteaza = async (id: string, mod: 'deblocheaza' | 'blocheaza' | 'implicit') => {
    const n: Suprascrieri = { deblocate: supr.deblocate.filter((x) => x !== id), blocate: supr.blocate.filter((x) => x !== id) };
    if (mod === 'deblocheaza') n.deblocate.push(id);
    if (mod === 'blocheaza') n.blocate.push(id);
    setSupr(n); await scrieSetare(`suprascrieri-${clasa}`, n); reincarca();
  };
  const titlu = (id: string) => cal.niveluri.find((n) => n.id === id)?.titlu ?? id;

  return (
    <div className="stiva">

      <div className="card stiva">
        <h2>Recapitularea pentru Evaluarea Națională (clasa a VIII-a)</h2>
        <p>Implicit, modul urmează fișierul <code>config/scoala.json</code> (activ de la săptămâna 28). Aici îl poți porni sau opri pe acest dispozitiv, de exemplu pentru tablă.</p>
        <div className="rand">
          {([[null, 'Ca în configurație'], [true, 'Pornit'], [false, 'Oprit']] as const).map(([v, t]) => (
            <label key={String(v)} className="bifa"><input type="radio" name="modEN" checked={modEN === v} onChange={async () => { setModEN(v); await scrieSetare('modEN', v); reincarca(); }} /> {t}</label>
          ))}
        </div>
      </div>

      <div className="card stiva">
        <h2>Data aplicației</h2>
        <p className="eticheta-mica">Pentru probă: alege o dată și vezi ce se deblochează. Lasă gol pentru data de azi.</p>
        <div className="rand">
          <input type="date" className="camp" value={data} onChange={(e) => setData(e.target.value)} style={{ minHeight: 48, borderRadius: 12, border: '2px solid var(--linie)', padding: '0 12px' }} />
          <button className="buton mic" onClick={async () => { await scrieSetare('dataSimulata', data || null); reincarca(); }}>Aplică</button>
          <button className="buton secundar mic" onClick={async () => { setData(''); await scrieSetare('dataSimulata', null); reincarca(); }}>Azi</button>
        </div>
        <p>Data folosită acum: <b>{formatData(azi)}</b>.</p>
      </div>

      <div className="card stiva">
        <h2>Calendarul clasei</h2>
        <div className="rand" role="group" aria-label="Clasa">
          {([5, 6, 7, 8] as Clasa[]).map((k) => (
            <button key={k} className="varianta" style={{ minWidth: 90, textAlign: 'center' }} aria-pressed={clasa === k} onClick={() => setClasa(k)}>
              a {({ 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' } as const)[k]}-a
            </button>
          ))}
        </div>
        <p className="eticheta-mica">
          Deblocarea manuală se salvează pe acest dispozitiv (de exemplu, calculatorul de la tablă).
          Ca un elev să lucreze înainte, dă-i lecția ca temă: tema deschide nivelurile ei și pe telefonul lui.
        </p>
        <div style={{ overflowX: 'auto' }}>
          <table className="tabel">
            <thead><tr><th>S</th><th>Perioada</th><th>Ce se predă</th><th>Evaluare</th><th>Niveluri</th></tr></thead>
            <tbody>
              {randuriClasa(cal, clasa).map((r) => {
                const sa = cal.saptamani[r.saptamana - 1];
                return (
                  <tr key={r.saptamana} style={r.saptamana === s ? { background: 'var(--apa)' } : undefined}>
                    <td><b>S{r.saptamana}</b>{r.saptamana === s && <><br /><span className="eticheta-mica">acum</span></>}</td>
                    <td className="eticheta-mica">{formatData(sa.de).replace(/ \d{4}$/, '')} – {formatData(sa.pana).replace(/ \d{4}$/, '')}{sa.zileCurs < 5 && <><br />{sa.zileCurs} zile de curs</>}</td>
                    <td>{r.eveniment ? <i>{cal.evenimente.find((e) => e.id === r.eveniment)?.nume}</i> : r.continuturi.join(' · ') || <span className="eticheta-mica">continuare</span>}</td>
                    <td className="eticheta-mica">{r.evaluare.join(', ')}</td>
                    <td>
                      {r.niveluri.map((id) => {
                        const des = deschise.has(id);
                        const are = continut && profil?.clasa === clasa ? continut.niveluri.has(id) : undefined;
                        return (
                          <div key={id} className="stiva" style={{ gap: 4, marginBottom: 6 }}>
                            <span className="eticheta-mica">{titlu(id).slice(0, 40)}{are === false ? ' (conținut în pregătire)' : ''}</span>
                            <span className="rand" style={{ gap: 6 }}>
                              {des
                                ? <button className="buton secundar mic" onClick={() => seteaza(id, 'blocheaza')}>Blochează</button>
                                : <button className="buton mic" onClick={() => seteaza(id, 'deblocheaza')}>Deblochează</button>}
                              {(supr.deblocate.includes(id) || supr.blocate.includes(id)) && <button className="buton secundar mic" onClick={() => seteaza(id, 'implicit')}>După calendar</button>}
                            </span>
                          </div>
                        );
                      })}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      <div className="card stiva">
        <h2>Observații din planificare</h2>
        <ul>{cal.observatii.map((o) => <li key={o}>{o}</li>)}</ul>
      </div>

    </div>
  );
}
