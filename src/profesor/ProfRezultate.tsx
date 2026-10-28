import { useEffect, useMemo, useRef, useState } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { useApp } from '../state';
import { citesteSetare, db } from '../db/db';
import { formatData } from '../calendar/calendar';
import { continutClasa, incarcaCompetente, type ContinutIncarcat } from '../content';
import { deschideCanal, type Canal } from '../live/canal';
import { pinNou } from '../live/protocol';
import type { Clasa, Tema } from '../types';
import { celeMaiGresite, csvPanou, randuriPanou } from './sumar';
import { Copiaza, QR, adresa, numeClasa } from './ProfClase';

const nivelCaldura = (p: number | null) => (p === null ? '' : p < 40 ? 'h0' : p < 60 ? 'h1' : p < 80 ? 'h2' : 'h3');

function descarca(nume: string, continut: string, tip = 'text/csv;charset=utf-8') {
  const url = URL.createObjectURL(new Blob([continut], { type: tip }));
  const a = document.createElement('a');
  a.href = url; a.download = nume; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/** Colectarea rezultatelor: elevii trimit rezumatul de pe telefon; calculatorul îl salvează local. */
function Colectare() {
  const { azi } = useApp();
  const [pin, setPin] = useState<string | null>(null);
  const [primite, setPrimite] = useState<string[]>([]);
  const [eroare, setEroare] = useState('');
  const [tip, setTip] = useState<'supabase' | 'local'>();
  const canal = useRef<Canal | null>(null);
  const vazute = useRef(new Set<string>());
  useEffect(() => () => canal.current?.inchide(), []);

  const porneste = async () => {
    setEroare('');
    try {
      const p = pinNou();
      const c = await deschideCanal(p);
      canal.current = c; setTip(c.tip);
      c.asculta(async (m) => {
        if (m.t !== 'raport') return;
        if (!vazute.current.has(m.id)) {
          vazute.current.add(m.id);
          const r = m.r;
          await db.rapoarte.add({
            cod: String(r.cod).slice(0, 8), porecla: String(r.porecla).replace(/[<>]/g, '').slice(0, 24), avatar: String(r.avatar).slice(0, 4),
            clasa: r.clasa, primit: azi, sumar: r.sumar,
          });
          setPrimite((x) => [...x, `${r.avatar} ${r.porecla} (${r.cod})`]);
        }
        c.trimite({ t: 'primit', id: m.id });
      });
      setPin(p);
    } catch (e) { setEroare(e instanceof Error ? e.message : String(e)); }
  };
  const opreste = () => { canal.current?.inchide(); canal.current = null; setPin(null); setPrimite([]); };

  if (!pin) {
    return (
      <div className="card stiva">
        <h2>Colectează rezultatele</h2>
        <p>Deschide colectarea pe calculatorul de la tablă. Elevii scanează codul și apasă „Trimite”. Rapoartele se salvează doar pe acest calculator.</p>
        {eroare && <p className="feedback nu">{eroare}</p>}
        <button className="buton" onClick={porneste}>Deschide colectarea</button>
      </div>
    );
  }
  return (
    <div className="card stiva mod-tabla">
      {tip === 'local' && <p className="feedback nu"><strong>Mod demonstrație</strong>Fără serverul configurat (docs/ghid-joc-live.md) pot trimite doar alte ferestre de pe acest calculator.</p>}
      <div className="rand" style={{ alignItems: 'flex-start' }}>
        <QR text={adresa(`colectare=${pin}`)} marime={300} />
        <div className="stiva" style={{ flex: 1, minWidth: 260 }}>
          <h2 style={{ margin: 0 }}>Trimite-ți rezultatele: PIN {pin}</h2>
          <p className="eticheta-mica" style={{ wordBreak: 'break-all' }}>{adresa(`colectare=${pin}`)}</p>
          <p><b>{primite.length}</b> rapoarte primite</p>
          <ul style={{ columns: 2, margin: 0 }}>{primite.map((p, i) => <li key={i}>{p}</li>)}</ul>
          <div className="rand"><Copiaza text={adresa(`colectare=${pin}`)} /><button className="buton" onClick={opreste}>Încheie colectarea</button></div>
        </div>
      </div>
    </div>
  );
}

/** Fila „Rezultate”: panoul pe competențe, din rapoartele colectate. */
export function ProfRezultate() {
  const clase = useLiveQuery(() => db.clase.toArray(), [], []);
  const toate = useLiveQuery(() => db.rapoarte.toArray(), [], []);
  const [cod, setCod] = useState('');
  const [comp, setComp] = useState<Record<string, Record<string, string>>>({});
  const [cont, setCont] = useState<ContinutIncarcat>();
  const [teme, setTeme] = useState<Tema[]>([]);
  useEffect(() => { incarcaCompetente().then(setComp); citesteSetare<Tema[]>('temeProfesor', []).then(setTeme); }, []);

  const coduri = useMemo(() => [...new Set([...clase.map((c) => c.cod), ...toate.map((r) => r.cod)])].sort(), [clase, toate]);
  useEffect(() => { if (!cod && coduri.length) setCod(coduri[0]); }, [coduri]); // eslint-disable-line react-hooks/exhaustive-deps
  const clasa = (clase.find((c) => c.cod === cod)?.clasa ?? toate.find((r) => r.cod === cod)?.clasa) as Clasa | undefined;
  useEffect(() => { if (clasa) continutClasa(clasa).then(setCont); }, [clasa]);

  const rapoarte = toate.filter((r) => r.cod === cod);
  const competente = clasa ? Object.keys(comp[String(clasa)] ?? {}) : [];
  const randuri = randuriPanou(rapoarte, competente);
  const teste = cont?.boss.map((b) => b.id) ?? [];
  const gresite = celeMaiGresite(randuri.map((r) => rapoarte.filter((x) => x.porecla === r.porecla).sort((a, b) => b.primit.localeCompare(a.primit))[0]));
  const temeClasa = teme.filter((t) => t.cod === cod);
  const media = (c: string) => {
    const v = randuri.map((r) => r.procente[c]).filter((x): x is number => x !== null);
    return v.length ? Math.round(v.reduce((a, b) => a + b, 0) / v.length) : null;
  };
  const numeCod = (c: string) => { const k = clase.find((x) => x.cod === c); return k ? `${numeClasa(k.clasa, k.litera)} (${c})` : c; };

  return (
    <div className="stiva">
      <div className="nu-tipari"><Colectare /></div>

      <div className="card stiva">
        <div className="rand" style={{ justifyContent: 'space-between' }}>
          <h2 style={{ margin: 0 }}>Panoul pe competențe</h2>
          <div className="rand nu-tipari">
            <select value={cod} onChange={(e) => setCod(e.target.value)} style={{ minHeight: 44, borderRadius: 10 }} aria-label="Clasa">
              {coduri.map((c) => <option key={c} value={c}>{numeCod(c)}</option>)}
            </select>
            <button className="buton secundar mic" disabled={!randuri.length} onClick={() => descarca(`geoquest-${cod}.csv`, csvPanou(randuri, competente, teste, rapoarte))}>Descarcă CSV (Excel)</button>
            <button className="buton secundar mic" disabled={!randuri.length} onClick={() => window.print()}>Tipărește / PDF</button>
          </div>
        </div>
        {!randuri.length ? (
          <p className="eticheta-mica">Încă nu ai rapoarte pentru această clasă. Deschide colectarea în clasă, după ce elevii au lucrat.</p>
        ) : (
          <>
            <p className="eticheta-mica">{numeCod(cod)} · {randuri.length} elevi · procent de răspunsuri corecte pe fiecare competență. Celulele goale: competența nu a fost încă exersată.</p>
            <div style={{ overflowX: 'auto' }}>
              <table className="tabel caldura">
                <thead>
                  <tr><th>Elev</th>{competente.map((c) => <th key={c} title={comp[String(clasa)]?.[c]}>{c.split('-')[1]}</th>)}<th>XP</th><th>Stele</th>{teste.map((t) => <th key={t}>{t.split('-')[1]}</th>)}</tr>
                </thead>
                <tbody>
                  {randuri.map((r) => (
                    <tr key={r.porecla}>
                      <td><span aria-hidden="true">{r.avatar}</span> {r.porecla}<br /><span className="eticheta-mica">{formatData(r.primit)}</span></td>
                      {competente.map((c) => <td key={c} className={nivelCaldura(r.procente[c])}>{r.procente[c] ?? ''}</td>)}
                      <td>{r.xp}</td><td>{r.stele}</td>
                      {teste.map((t) => {
                        const s = rapoarte.filter((x) => x.porecla === r.porecla).sort((a, b) => b.primit.localeCompare(a.primit))[0]?.sumar.niveluri[t]?.scor;
                        return <td key={t} className={nivelCaldura(s === undefined ? null : Math.round(s * 100))}>{s === undefined ? '' : Math.round(s * 100)}</td>;
                      })}
                    </tr>
                  ))}
                  <tr><td><b>Media clasei</b></td>{competente.map((c) => <td key={c} className={nivelCaldura(media(c))}><b>{media(c) ?? ''}</b></td>)}<td colSpan={2 + teste.length} /></tr>
                </tbody>
              </table>
            </div>
            <p className="eticheta-mica legenda">
              <span className="h0">sub 40 %</span> <span className="h1">40–59 %</span> <span className="h2">60–79 %</span> <span className="h3">80 % sau mai mult</span>
            </p>
          </>
        )}
      </div>

      {!!randuri.length && (
        <div className="card stiva">
          <h2>Itemii greșiți de cei mai mulți elevi</h2>
          <table className="tabel">
            <thead><tr><th>Item</th><th>Competențe</th><th>Elevi care au greșit</th></tr></thead>
            <tbody>
              {gresite.map((g) => {
                const it = cont?.itemi.get(g.item);
                return <tr key={g.item}><td>{it?.enunt ?? g.item}<br /><span className="eticheta-mica">{g.item}</span></td><td>{it?.competente.join(', ')}</td><td>{g.elevi} din {randuri.length}</td></tr>;
              })}
            </tbody>
          </table>
        </div>
      )}

      {!!temeClasa.length && !!randuri.length && (
        <div className="card stiva">
          <h2>Temele clasei</h2>
          <table className="tabel">
            <thead><tr><th>Tema</th><th>Termen</th><th>Au terminat</th><th>Au început</th></tr></thead>
            <tbody>
              {temeClasa.map((t) => {
                const ultim = randuri.map((r) => rapoarte.filter((x) => x.porecla === r.porecla).sort((a, b) => b.primit.localeCompare(a.primit))[0]);
                const gata = ultim.filter((r) => (r.sumar.teme[t.id] ?? 0) >= t.niveluri.length).length;
                const inceput = ultim.filter((r) => (r.sumar.teme[t.id] ?? 0) > 0).length;
                return <tr key={t.id}><td>{t.titlu}</td><td>{formatData(t.termen)}</td><td>{gata} din {randuri.length}</td><td>{inceput}</td></tr>;
              })}
            </tbody>
          </table>
        </div>
      )}

      <div className="card stiva nu-tipari">
        <h2>Ștergerea datelor</h2>
        <p className="eticheta-mica">La final de an (sau oricând), șterge rapoartele unei clase de pe acest calculator.</p>
        <button className="buton secundar" disabled={!rapoarte.length} onClick={async () => {
          if (confirm(`Ștergi toate cele ${rapoarte.length} rapoarte ale clasei ${numeCod(cod)}? Nu se poate anula.`)) await db.rapoarte.where('cod').equals(cod).delete();
        }}>Șterge rapoartele clasei</button>
      </div>
    </div>
  );
}
