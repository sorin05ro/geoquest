import { useEffect, useMemo, useState } from 'react';
import { useLiveQuery } from 'dexie-react-hooks';
import { useApp } from '../state';
import { db } from '../db/db';
import { continutClasa, incarcaCompetente, nivelMinimal } from '../content';
import { Exercitiu } from '../engine/Exercitiu';
import { MapView } from '../maps/MapView';
import type { Clasa, FisierContinut, Harta, Item, TipItem } from '../types';
import { lacunarDinParanteze, valideazaItem } from './valideaza';

type TipEditor = Extract<TipItem, 'alegere' | 'lacunar' | 'asociaza' | 'ordoneaza' | 'pin'>;
const TIPURI: { tip: TipEditor; nume: string }[] = [
  { tip: 'alegere', nume: 'Grilă (o variantă corectă)' },
  { tip: 'lacunar', nume: 'Text lacunar' },
  { tip: 'asociaza', nume: 'Asociază perechi' },
  { tip: 'ordoneaza', nume: 'Ordonează' },
  { tip: 'pin', nume: 'Localizează pe hartă' },
];
const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };

interface Formular {
  clasa: Clasa; nivel: string; tip: TipEditor; dificultate: 1 | 2 | 3; competente: string[]; enunt: string;
  variante: string[]; textLacunar: string; capcane: string; perechi: [string, string][]; elemente: string; criteriu: string;
  harta: Harta; tinta: { lat: number; lon: number } | null; numeLoc: string; toleranta: number;
  corect: string; gresit: string; indiciu: string; surse: string; id?: string;
}
const gol = (clasa: Clasa): Formular => ({
  clasa, nivel: '', tip: 'alegere', dificultate: 1, competente: [], enunt: '',
  variante: ['', '', '', ''], textLacunar: '', capcane: '', perechi: [['', ''], ['', ''], ['', '']], elemente: '', criteriu: 'De la primul la ultimul',
  harta: 'romania', tinta: null, numeLoc: '', toleranta: 40, corect: 'Corect.', gresit: '', indiciu: '', surse: '',
});

function construiesteItem(f: Formular): Item {
  const baza = {
    id: f.id ?? `P-${f.clasa}-${crypto.randomUUID().slice(0, 6)}`, nivel: f.nivel, competente: f.competente, dificultate: f.dificultate,
    enunt: f.enunt.trim(), feedback: { corect: f.corect.trim(), gresit: f.gresit.trim() },
    ...(f.indiciu.trim() ? { indiciu: f.indiciu.trim() } : {}),
    ...(f.surse.trim() ? { surse: f.surse.split('\n').map((s) => s.trim()).filter(Boolean) } : {}),
  };
  switch (f.tip) {
    case 'alegere': return { ...baza, tip: 'alegere', date: { variante: f.variante.map((v) => v.trim()), corect: 0 } };
    case 'lacunar': {
      const { text, raspunsuri } = lacunarDinParanteze(f.textLacunar);
      return { ...baza, tip: 'lacunar', date: { text, raspunsuri, distractori: f.capcane.split(',').map((x) => x.trim()).filter(Boolean) } };
    }
    case 'asociaza': return { ...baza, tip: 'asociaza', date: { perechi: f.perechi.filter(([a, b]) => a.trim() || b.trim()).map(([a, b]) => [a.trim(), b.trim()]) } };
    case 'ordoneaza': return { ...baza, tip: 'ordoneaza', date: { elemente: f.elemente.split('\n').map((x) => x.trim()).filter(Boolean), criteriu: f.criteriu.trim() } };
    case 'pin': return { ...baza, tip: 'pin', date: { harta: f.harta, tinta: { lat: f.tinta?.lat ?? NaN, lon: f.tinta?.lon ?? NaN, nume: f.numeLoc.trim() }, toleranta: f.toleranta } };
  }
}

function formularDinItem(it: Item & { clasa: number }): Formular {
  const f: Formular = { ...gol(it.clasa as Clasa), id: it.id, nivel: it.nivel, dificultate: it.dificultate, competente: it.competente, enunt: it.enunt,
    corect: it.feedback.corect, gresit: it.feedback.gresit, indiciu: it.indiciu ?? '', surse: (it.surse ?? []).join('\n'), tip: it.tip as TipEditor };
  if (it.tip === 'alegere') f.variante = [...it.date.variante];
  if (it.tip === 'lacunar') { let i = 0; f.textLacunar = it.date.text.replace(/\{\d+\}/g, () => `[${it.date.raspunsuri[i++]}]`); f.capcane = it.date.distractori.join(', '); }
  if (it.tip === 'asociaza') f.perechi = it.date.perechi.map((p) => [...p] as [string, string]);
  if (it.tip === 'ordoneaza') { f.elemente = it.date.elemente.join('\n'); f.criteriu = it.date.criteriu; }
  if (it.tip === 'pin') { f.harta = it.date.harta; f.tinta = { lat: it.date.tinta.lat, lon: it.date.tinta.lon }; f.numeLoc = it.date.tinta.nume ?? ''; f.toleranta = it.date.toleranta; }
  return f;
}

/** Fila „Conținut”: editorul de itemi. Itemii se salvează pe acest dispozitiv și se pot descărca pentru publicare. */
export function ProfEditor() {
  const { cal, reincarca } = useApp();
  const [f, setF] = useState<Formular>(gol(5));
  const [comp, setComp] = useState<Record<string, Record<string, string>>>({});
  const [previzualizare, setPrevizualizare] = useState<Item | null>(null);
  const [probleme, setProbleme] = useState<string[]>([]);
  const [salvat, setSalvat] = useState('');
  const ale = useLiveQuery(() => db.itemiProfesor.toArray(), [], []);
  useEffect(() => { incarcaCompetente().then(setComp); }, []);
  const s = (x: Partial<Formular>) => { setF((v) => ({ ...v, ...x })); setPrevizualizare(null); setSalvat(''); };

  const lectii = useMemo(() => cal.niveluri.filter((n) => n.clasa === f.clasa && n.tip === 'nivel'), [cal, f.clasa]);
  const compClasa = comp[String(f.clasa)] ?? {};
  const nivelAles = lectii.find((l) => l.id === f.nivel);

  const verifica = () => {
    const it = construiesteItem(f);
    const e = valideazaItem(it, new Set(Object.keys(compClasa)));
    if (!f.nivel) e.unshift('Alege lecția (nivelul) din care face parte itemul.');
    setProbleme(e);
    return e.length ? null : it;
  };
  const salveaza = async () => {
    const it = verifica();
    if (!it) return;
    await db.itemiProfesor.put({ ...it, clasa: f.clasa });
    reincarca();
    setPrevizualizare(null);
    setSalvat(`Salvat: ${it.id}. Îl vezi în lecția „${nivelAles?.titlu}” pe acest dispozitiv.`);
    setF({ ...gol(f.clasa), nivel: f.nivel, competente: f.competente, tip: f.tip });
  };
  const descarcaClasa = async (clasa: Clasa) => {
    const itemi = ale.filter((i) => i.clasa === clasa).map(({ clasa: _c, ...i }) => i as Item); // eslint-disable-line @typescript-eslint/no-unused-vars
    const publicate = await continutClasa(clasa);
    const niveluri = [...new Set(itemi.map((i) => i.nivel))]
      .filter((id) => !publicate.niveluri.has(id) || publicate.niveluri.get(id)!.invata[0]?.text.startsWith('Exercițiile acestui nivel'))
      .map((id) => nivelMinimal(cal.niveluri.find((n) => n.id === id)!));
    const fis: FisierContinut = { clasa, unitate: 'Itemi creați de profesor', niveluri, itemi };
    const url = URL.createObjectURL(new Blob([JSON.stringify(fis, null, 1)], { type: 'application/json' }));
    const a = document.createElement('a'); a.href = url; a.download = 'profesor.json'; a.click();
  };

  return (
    <div className="stiva">
      <div className="card stiva">
        <h2>{f.id ? `Modifici itemul ${f.id}` : 'Item nou'}</h2>
        <div className="rand">
          <label className="camp"><span>Clasa</span>
            <select value={f.clasa} onChange={(e) => s({ clasa: Number(e.target.value) as Clasa, nivel: '', competente: [] })}>
              {[5, 6, 7, 8].map((c) => <option key={c} value={c}>a {ROMAN[c]}-a</option>)}
            </select>
          </label>
          <label className="camp" style={{ flex: 1, minWidth: 240 }}><span>Lecția (nivelul)</span>
            <select value={f.nivel} onChange={(e) => { const l = lectii.find((x) => x.id === e.target.value); s({ nivel: e.target.value, competente: f.competente.length ? f.competente : (l?.competente ?? []).slice(0, 2) }); }}>
              <option value="">Alege lecția</option>
              {lectii.map((l) => <option key={l.id} value={l.id}>S{l.saptamana} · {l.titlu.slice(0, 70)}</option>)}
            </select>
          </label>
        </div>
        <div className="rand">
          <label className="camp"><span>Tipul exercițiului</span>
            <select value={f.tip} onChange={(e) => s({ tip: e.target.value as TipEditor })}>{TIPURI.map((t) => <option key={t.tip} value={t.tip}>{t.nume}</option>)}</select>
          </label>
          <label className="camp"><span>Dificultate</span>
            <select value={f.dificultate} onChange={(e) => s({ dificultate: Number(e.target.value) as 1 | 2 | 3 })}><option value={1}>1 – ușor</option><option value={2}>2 – mediu</option><option value={3}>3 – greu</option></select>
          </label>
        </div>
        <fieldset className="stiva" style={{ border: 0, padding: 0 }}>
          <legend><b>Competențe specifice</b> {nivelAles && <span className="eticheta-mica">(din planificare: {nivelAles.competente.map((c) => c.split('-')[1]).join(', ')})</span>}</legend>
          <div className="rand" style={{ gap: 6 }}>
            {Object.entries(compClasa).map(([c, t]) => (
              <label key={c} className="bifa" title={t} style={{ minWidth: 80 }}>
                <input type="checkbox" checked={f.competente.includes(c)} onChange={(e) => s({ competente: e.target.checked ? [...f.competente, c] : f.competente.filter((x) => x !== c) })} />
                {c.split('-')[1]}
              </label>
            ))}
          </div>
        </fieldset>
        <label className="camp"><span>Enunțul</span><textarea rows={2} value={f.enunt} onChange={(e) => s({ enunt: e.target.value })} /></label>

        {f.tip === 'alegere' && f.variante.map((v, i) => (
          <label key={i} className="camp"><span>{i === 0 ? 'Varianta corectă' : `Variantă greșită ${i}`}</span>
            <input value={v} onChange={(e) => s({ variante: f.variante.map((x, j) => (j === i ? e.target.value : x)) })} />
          </label>
        ))}
        {f.tip === 'lacunar' && (
          <>
            <label className="camp"><span>Textul, cu răspunsurile între paranteze drepte</span>
              <textarea rows={3} value={f.textLacunar} placeholder="Soarele răsare la [est] și apune la [vest]." onChange={(e) => s({ textLacunar: e.target.value })} />
            </label>
            <label className="camp"><span>Cuvinte-capcană, despărțite prin virgulă</span><input value={f.capcane} placeholder="nord, sud" onChange={(e) => s({ capcane: e.target.value })} /></label>
          </>
        )}
        {f.tip === 'asociaza' && (
          <div className="stiva">
            {f.perechi.map(([a, b], i) => (
              <div key={i} className="rand">
                <input aria-label={`Stânga ${i + 1}`} className="camp" style={{ flex: 1, minHeight: 44, borderRadius: 10, border: '2px solid var(--linie)', padding: '0 10px' }} value={a}
                  onChange={(e) => s({ perechi: f.perechi.map((p, j) => (j === i ? [e.target.value, p[1]] : p)) })} />
                <span aria-hidden="true">↔</span>
                <input aria-label={`Dreapta ${i + 1}`} className="camp" style={{ flex: 1, minHeight: 44, borderRadius: 10, border: '2px solid var(--linie)', padding: '0 10px' }} value={b}
                  onChange={(e) => s({ perechi: f.perechi.map((p, j) => (j === i ? [p[0], e.target.value] : p)) })} />
              </div>
            ))}
            {f.perechi.length < 6 && <button className="buton secundar mic" onClick={() => s({ perechi: [...f.perechi, ['', '']] })}>Adaugă o pereche</button>}
          </div>
        )}
        {f.tip === 'ordoneaza' && (
          <>
            <label className="camp"><span>Elementele, câte unul pe rând, în ordinea corectă (aplicația le amestecă)</span>
              <textarea rows={5} value={f.elemente} onChange={(e) => s({ elemente: e.target.value })} />
            </label>
            <label className="camp"><span>Criteriul</span><input value={f.criteriu} onChange={(e) => s({ criteriu: e.target.value })} placeholder="De la cel mai lung la cel mai scurt" /></label>
          </>
        )}
        {f.tip === 'pin' && (
          <div className="stiva">
            <div className="rand" role="group" aria-label="Harta">
              <button className="varianta" aria-pressed={f.harta === 'romania'} onClick={() => s({ harta: 'romania', tinta: null })}>România</button>
              <button className="varianta" aria-pressed={f.harta === 'lume'} onClick={() => s({ harta: 'lume', tinta: null, toleranta: 500 })}>Lumea</button>
            </div>
            <MapView harta={f.harta} eticheta="Atinge locul corect" onPick={(lon, lat) => s({ tinta: { lat: Math.round(lat * 1000) / 1000, lon: Math.round(lon * 1000) / 1000 } })}
              overlay={(p) => f.tinta && (() => { const [x, y] = p([f.tinta.lon, f.tinta.lat]) ?? [0, 0]; return <circle cx={x} cy={y} r="10" fill="var(--pion)" stroke="var(--hartie)" strokeWidth="3" />; })()} />
            <div className="rand">
              <label className="camp" style={{ flex: 1 }}><span>Numele locului</span><input value={f.numeLoc} onChange={(e) => s({ numeLoc: e.target.value })} /></label>
              <label className="camp"><span>Acceptat până la (km)</span><input type="number" min={5} max={3000} value={f.toleranta} onChange={(e) => s({ toleranta: Number(e.target.value) })} /></label>
            </div>
            {f.tinta && <p className="eticheta-mica">Coordonate: {f.tinta.lat}° N, {f.tinta.lon}° E. Verifică locul exact într-un atlas.</p>}
          </div>
        )}

        <label className="camp"><span>Mesaj la răspuns corect</span><input value={f.corect} onChange={(e) => s({ corect: e.target.value })} /></label>
        <label className="camp"><span>Mesaj la greșeală (explică răspunsul corect)</span><textarea rows={2} value={f.gresit} onChange={(e) => s({ gresit: e.target.value })} /></label>
        <label className="camp"><span>Indiciu (opțional)</span><input value={f.indiciu} onChange={(e) => s({ indiciu: e.target.value })} /></label>
        <label className="camp"><span>Surse pentru cifre și date (opțional, câte una pe rând)</span><textarea rows={2} value={f.surse} onChange={(e) => s({ surse: e.target.value })} /></label>

        {probleme.length > 0 && <div className="feedback nu" role="alert"><strong>De corectat</strong><ul style={{ margin: 0 }}>{probleme.map((p) => <li key={p}>{p}</li>)}</ul></div>}
        {salvat && <p className="feedback ok" role="status">{salvat}</p>}
        <div className="rand">
          <button className="buton secundar" onClick={() => { const it = verifica(); if (it) setPrevizualizare(it); }}>Previzualizează</button>
          <button className="buton" onClick={salveaza}>{f.id ? 'Salvează modificările' : 'Salvează itemul'}</button>
          {f.id && <button className="buton secundar" onClick={() => setF(gol(f.clasa))}>Renunță</button>}
        </div>
      </div>

      {previzualizare && (
        <div className="card">
          <p className="eticheta-mica">Așa îl vede elevul:</p>
          <Exercitiu key={JSON.stringify(previzualizare)} item={previzualizare} onGata={() => setPrevizualizare(null)} textContinua="Închide previzualizarea" />
        </div>
      )}

      <div className="card stiva">
        <h2>Itemii tăi ({ale.length})</h2>
        <p className="eticheta-mica">
          Sunt salvați pe acest dispozitiv. Ca să ajungă la elevi: descarcă fișierul clasei, pune-l în folderul proiectului ca
          public/content/clasa-N/profesor.json (N = 5, 6, 7 sau 8) și publică (GitHub Desktop: Commit, apoi Push).
        </p>
        <div className="rand">
          {([5, 6, 7, 8] as Clasa[]).map((c) => ale.some((i) => i.clasa === c) && (
            <button key={c} className="buton secundar mic" onClick={() => descarcaClasa(c)}>Descarcă profesor.json pentru a {ROMAN[c]}-a</button>
          ))}
        </div>
        <table className="tabel">
          <tbody>
            {ale.map((i) => (
              <tr key={i.id}>
                <td>{i.enunt}<br /><span className="eticheta-mica">{i.id} · a {ROMAN[i.clasa]}-a · {TIPURI.find((t) => t.tip === i.tip)?.nume} · dificultate {i.dificultate} · {i.competente.join(', ')}</span></td>
                <td className="rand" style={{ gap: 6 }}>
                  <button className="buton secundar mic" onClick={() => { setF(formularDinItem(i)); window.scrollTo(0, 0); }}>Modifică</button>
                  <button className="buton secundar mic" onClick={async () => { if (confirm('Ștergi itemul?')) { await db.itemiProfesor.delete(i.id); reincarca(); } }}>Șterge</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
