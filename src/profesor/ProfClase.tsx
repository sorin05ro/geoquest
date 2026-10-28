import { useEffect, useMemo, useState } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { useApp } from '../state';
import { citesteSetare, db, scrieSetare } from '../db/db';
import { formatData } from '../calendar/calendar';
import { continutClasa } from '../content';
import type { Clasa, Tema } from '../types';
import { codClasaNou, codeazaTema } from './sumar';

const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };
export const numeClasa = (clasa: number, litera?: string) => `a ${ROMAN[clasa]}-a${litera ? ` ${litera}` : ''}`;
export const adresa = (hash: string) => `${location.origin}${location.pathname}#${hash}`;

/** Cod QR (SVG) generat local; biblioteca se încarcă doar aici. */
export function QR({ text, marime = 220 }: { text: string; marime?: number }) {
  const [svg, setSvg] = useState('');
  useEffect(() => { import('qrcode').then((Q) => Q.toString(text, { type: 'svg', margin: 1 })).then(setSvg); }, [text]);
  return <div role="img" aria-label="Cod QR" style={{ width: marime, height: marime, background: '#fff', padding: 6, borderRadius: 10, flex: 'none' }} dangerouslySetInnerHTML={{ __html: svg }} />;
}

export function Copiaza({ text, eticheta = 'Copiază linkul' }: { text: string; eticheta?: string }) {
  const [ok, setOk] = useState(false);
  return (
    <button className="buton secundar mic" onClick={async () => {
      try { await navigator.clipboard.writeText(text); setOk(true); setTimeout(() => setOk(false), 2000); } catch { prompt('Copiază linkul:', text); }
    }}>{ok ? 'Copiat' : eticheta}</button>
  );
}

/** Fila „Clase și teme”. */
export function ProfClase() {
  const { scoala, cal, azi } = useApp();
  const clase = useLiveQuery(() => db.clase.toArray(), [], []);
  const [teme, setTeme] = useState<Tema[]>([]);
  const [arata, setArata] = useState<string | null>(null);
  const [cod, setCod] = useState('');
  const [niveluri, setNiveluri] = useState<string[]>([]);
  const [termen, setTermen] = useState('');
  const [titlu, setTitlu] = useState('');
  const [cuContinut, setCuContinut] = useState<Set<string>>(new Set());

  useEffect(() => { citesteSetare<Tema[]>('temeProfesor', []).then(setTeme); }, []);
  const grupe = scoala.clase.flatMap((c) => (c.litere.length ? c.litere : ['']).map((l) => ({ clasa: c.clasa, litera: l })));
  const clasaTemei = clase.find((c) => c.cod === cod);
  useEffect(() => {
    if (clasaTemei) continutClasa(clasaTemei.clasa).then((x) => setCuContinut(new Set(x.niveluri.keys())));
  }, [clasaTemei?.clasa]); // eslint-disable-line react-hooks/exhaustive-deps

  const genereaza = async () => {
    const existente = new Set(clase.map((c) => `${c.clasa}${c.litera}`));
    for (const g of grupe) if (!existente.has(`${g.clasa}${g.litera}`)) await db.clase.put({ cod: codClasaNou(g.clasa as Clasa, g.litera), clasa: g.clasa as Clasa, litera: g.litera, creat: azi });
  };
  const lectii = useMemo(() => (clasaTemei ? cal.niveluri.filter((n) => n.clasa === clasaTemei.clasa) : []), [clasaTemei, cal]);

  const creeazaTema = async () => {
    if (!clasaTemei) return;
    const t: Tema = {
      id: crypto.randomUUID().slice(0, 8), clasa: clasaTemei.clasa, cod: clasaTemei.cod, niveluri, termen, creat: azi,
      titlu: titlu.trim() || lectii.filter((l) => niveluri.includes(l.id)).map((l) => l.titlu).join(', ').slice(0, 80),
    };
    const n = [t, ...teme];
    setTeme(n); await scrieSetare('temeProfesor', n);
    setNiveluri([]); setTitlu(''); setArata(`tema=${codeazaTema(t)}`);
  };
  const stergeTema = async (id: string) => { const n = teme.filter((t) => t.id !== id); setTeme(n); await scrieSetare('temeProfesor', n); };

  return (
    <div className="stiva">
      {arata && (
        <div className="card stiva mod-tabla" style={{ alignItems: 'center', textAlign: 'center' }}>
          <QR text={adresa(arata)} marime={360} />
          <p style={{ wordBreak: 'break-all', maxWidth: 900 }}>{adresa(arata)}</p>
          <div className="rand"><Copiaza text={adresa(arata)} /><button className="buton" onClick={() => setArata(null)}>Închide</button></div>
        </div>
      )}

      <div className="card stiva">
        <h2>Codurile claselor</h2>
        <p className="eticheta-mica">Elevul scrie codul (sau scanează codul QR) o singură dată. Codul doar grupează rapoartele pe clase; nu cere cont, e-mail sau nume.</p>
        {clase.length < grupe.length && <button className="buton" onClick={genereaza}>Generează codurile claselor</button>}
        <table className="tabel">
          <thead><tr><th>Clasa</th><th>Cod</th><th /></tr></thead>
          <tbody>
            {[...clase].sort((a, b) => a.clasa - b.clasa || a.litera.localeCompare(b.litera)).map((c) => (
              <tr key={c.cod}>
                <td>{numeClasa(c.clasa, c.litera)}</td>
                <td><b style={{ fontSize: '1.2em', letterSpacing: '.08em' }}>{c.cod}</b></td>
                <td className="rand" style={{ gap: 6 }}>
                  <button className="buton secundar mic" onClick={() => setArata(`clasa=${c.cod}`)}>Arată QR pe tablă</button>
                  <Copiaza text={adresa(`clasa=${c.cod}`)} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="card stiva">
        <h2>Temă nouă</h2>
        <p className="eticheta-mica">Tema pleacă printr-un link sau un cod QR (pe tablă sau pe grupul clasei). Când elevul îl deschide, lecțiile temei i se deblochează și apar la Misiuni, cu termenul.</p>
        <div className="rand">
          <label className="camp"><span>Clasa</span>
            <select value={cod} onChange={(e) => { setCod(e.target.value); setNiveluri([]); }}>
              <option value="">Alege clasa</option>
              {clase.map((c) => <option key={c.cod} value={c.cod}>{numeClasa(c.clasa, c.litera)}</option>)}
            </select>
          </label>
          <label className="camp"><span>Termen</span>
            <input type="date" value={termen} min={azi} onChange={(e) => setTermen(e.target.value)} />
          </label>
          <label className="camp" style={{ flex: 1, minWidth: 220 }}><span>Titlu (opțional)</span>
            <input value={titlu} maxLength={80} onChange={(e) => setTitlu(e.target.value)} placeholder="ex. Recapitulare pentru T₂" />
          </label>
        </div>
        {!clase.length && <p className="eticheta-mica">Generează întâi codurile claselor.</p>}
        {clasaTemei && (
          <fieldset className="stiva" style={{ border: 0, padding: 0, maxHeight: 340, overflow: 'auto' }}>
            <legend><b>Lecțiile temei</b> <span className="eticheta-mica">(doar cele cu exerciții se pot alege)</span></legend>
            {lectii.map((l) => (
              <label key={l.id} className="bifa" style={{ opacity: cuContinut.has(l.id) ? 1 : 0.5 }}>
                <input type="checkbox" disabled={!cuContinut.has(l.id)} checked={niveluri.includes(l.id)}
                  onChange={(e) => setNiveluri((n) => (e.target.checked ? [...n, l.id] : n.filter((x) => x !== l.id)))} />
                S{l.saptamana} · {l.titlu}
              </label>
            ))}
          </fieldset>
        )}
        <button className="buton" disabled={!clasaTemei || !niveluri.length || !termen} onClick={creeazaTema}>Creează tema</button>
      </div>

      <div className="card stiva">
        <h2>Temele date</h2>
        {!teme.length && <p className="eticheta-mica">Încă nu ai dat teme.</p>}
        {teme.map((t) => (
          <div key={t.id} className="rand" style={{ justifyContent: 'space-between', borderBottom: '1px solid var(--linie)', paddingBottom: 8 }}>
            <div><b>{t.titlu}</b><br /><span className="eticheta-mica">{numeClasa(t.clasa, clase.find((c) => c.cod === t.cod)?.litera)} · {t.niveluri.length} lecții · termen {formatData(t.termen)}{t.termen < azi ? ' (expirat)' : ''}</span></div>
            <div className="rand" style={{ gap: 6 }}>
              <button className="buton secundar mic" onClick={() => setArata(`tema=${codeazaTema(t)}`)}>Arată QR</button>
              <Copiaza text={adresa(`tema=${codeazaTema(t)}`)} />
              <button className="buton secundar mic" onClick={() => stergeTema(t.id)}>Șterge</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
