import { useEffect, useMemo, useRef, useState } from 'react';
import { useApp } from '../state';
import { amesteca, continutClasa, incarca } from '../content';
import type { Clasa, Item, Punct } from '../types';
import { deschideCanal, type Canal } from './canal';
import {
  NUME_ECHIPE, REACTII, TIPURI_LIVE, alegeEchipa, pinNou, publica, puncte, scorPin, scoruriEchipe,
  type ItemPublic, type Jucator, type Mesaj, type StareSesiune,
} from './protocol';
import { VarianteLive, VizualColectiv, VizualIntrebare } from './Vizual';

type IdEveniment = 'expeditia-polara' | 'patrula-verde';
const NUME_EVENIMENT: Record<IdEveniment, string> = { 'expeditia-polara': 'Expediția Polară', 'patrula-verde': 'Patrula Verde' };
type Sursa = { tip: 'lectii'; niveluri: string[] } | { tip: 'eveniment'; id: IdEveniment };
interface Pregatit { pub: ItemPublic; corect?: number; tinta?: Punct; toleranta?: number }

const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };

/** Jocul live, pe tablă: setări → lobby cu QR → întrebări → rezultate → final. */
export function Gazda() {
  const { mergi, scoala, cal, azi } = useApp();
  const [clase, setClase] = useState<Clasa[]>([5]);
  const [itemiClasa, setItemiClasa] = useState<Record<number, Item[]>>({});
  const [niveluri, setNiveluri] = useState<Record<number, { id: string; titlu: string }[]>>({});
  const [sursa, setSursa] = useState<Sursa>({ tip: 'lectii', niveluri: [] });
  const [nrEchipe, setNrEchipe] = useState(2);
  const [nrIntrebari, setNrIntrebari] = useState(10);
  const [secunde, setSecunde] = useState(30);
  const [individual, setIndividual] = useState(scoala.clasamentIndividual);
  const [s, setS] = useState<StareSesiune | null>(null);
  const [eroare, setEroare] = useState('');
  const [tipCanal, setTipCanal] = useState<'supabase' | 'local'>();
  const [qr, setQr] = useState('');
  const [reactii, setReactii] = useState<{ r: string; k: number }[]>([]);
  const canal = useRef<Canal | null>(null);
  const intrebari = useRef<Pregatit[]>([]);
  const raspunsuri = useRef(new Map<string, { v: number | Punct; ramas: number }>());
  const start = useRef(0);
  const stareRef = useRef<StareSesiune | null>(null);
  stareRef.current = s;

  useEffect(() => {
    document.documentElement.dataset.mod = 'tabla';
    return () => { delete document.documentElement.dataset.mod; canal.current?.inchide(); };
  }, []);

  // conținutul claselor alese
  useEffect(() => {
    clase.forEach((c) => {
      if (itemiClasa[c]) return;
      continutClasa(c).then((x) => {
        setItemiClasa((m) => ({ ...m, [c]: [...x.itemi.values()].filter((i) => TIPURI_LIVE.has(i.tip)) }));
        setNiveluri((m) => ({ ...m, [c]: [...x.niveluri.values()].filter((n) => n.tip === 'nivel').map((n) => ({ id: n.id, titlu: n.titlu })) }));
      });
    });
  }, [clase]); // eslint-disable-line react-hooks/exhaustive-deps

  // lecțiile săptămânii curente, bifate implicit
  useEffect(() => {
    if (sursa.tip !== 'lectii' || sursa.niveluri.length) return;
    const sapt = Math.max(...clase.map((c) => cal.planificare.filter((p) => p.clasa === c && cal.saptamani[p.saptamana - 1].de <= azi && p.niveluri.length).at(-1)?.saptamana ?? 0));
    const ids = clase.flatMap((c) => (niveluri[c] ?? []).filter((n) => (cal.niveluri.find((q) => q.id === n.id)?.saptamana ?? 99) <= sapt).slice(-2).map((n) => n.id));
    if (ids.length) setSursa({ tip: 'lectii', niveluri: ids });
  }, [niveluri]); // eslint-disable-line react-hooks/exhaustive-deps

  const trimiteStare = (st: StareSesiune) => {
    const ramas = st.faza === 'intrebare' ? Math.max(0, st.durataMs - (Date.now() - start.current)) : undefined;
    canal.current?.trimite({ t: 'stare', s: { ...st, ramasMs: ramas } });
  };
  const actualizeaza = (f: (x: StareSesiune) => StareSesiune) => {
    setS((x) => { if (!x) return x; const n = f(x); trimiteStare(n); return n; });
  };

  // mesaje de la telefoane
  const laMesaj = (m: Mesaj) => {
    const st = stareRef.current;
    if (!st) return;
    if (m.t === 'cer-stare') trimiteStare(st);
    if (m.t === 'intra') {
      actualizeaza((x) => {
        if (x.jucatori.some((j) => j.id === m.id)) return x;
        const porecla = m.porecla.replace(/[<>]/g, '').slice(0, 24) || 'Explorator';
        const j: Jucator = { id: m.id, porecla, avatar: m.avatar.slice(0, 4), clasa: m.clasa, echipa: alegeEchipa(x.jucatori, x.echipe.length), scor: 0 };
        return { ...x, jucatori: [...x.jucatori, j] };
      });
    }
    if (m.t === 'raspuns' && st.faza === 'intrebare' && m.k === st.k && !raspunsuri.current.has(m.id)) {
      raspunsuri.current.set(m.id, { v: m.v, ramas: Math.max(0, st.durataMs - (Date.now() - start.current)) });
      setS((x) => x && { ...x, raspunsuri: raspunsuri.current.size });
      if (raspunsuri.current.size >= st.jucatori.length) setTimeout(() => arataRezultat(), 400);
    }
    if (m.t === 'reactie' && REACTII.includes(m.r)) {
      const k = Date.now() + Math.random();
      setReactii((r) => [...r.slice(-11), { r: m.r, k }]);
      setTimeout(() => setReactii((r) => r.filter((x) => x.k !== k)), 3500);
    }
  };
  const laMesajRef = useRef(laMesaj);
  laMesajRef.current = laMesaj;

  // retrimite starea periodic (pentru cine intră târziu sau pierde conexiunea)
  useEffect(() => {
    if (!s) return;
    const t = setInterval(() => stareRef.current && trimiteStare(stareRef.current), 2500);
    return () => clearInterval(t);
  }, [s?.pin]); // eslint-disable-line react-hooks/exhaustive-deps

  // cronometrul întrebării
  const [, tick] = useState(0);
  useEffect(() => {
    if (s?.faza !== 'intrebare') return;
    const t = setInterval(() => {
      tick((x) => x + 1);
      if (Date.now() - start.current >= (stareRef.current?.durataMs ?? 0)) { clearInterval(t); arataRezultat(); }
    }, 250);
    return () => clearInterval(t);
  }, [s?.faza, s?.k]); // eslint-disable-line react-hooks/exhaustive-deps

  const pregatesteIntrebari = async (): Promise<Pregatit[]> => {
    let pool: { it: Item; clasa: number }[] = [];
    if (sursa.tip === 'eveniment') {
      const ev = await incarca<{ itemi: (Item & { clase: number[] })[] }>(`content/evenimente/${sursa.id}.json`);
      pool = ev.itemi.filter((i) => i.clase.some((c) => clase.includes(c as Clasa))).map((it) => ({ it, clasa: it.clase.length === 1 ? it.clase[0] : 0 }));
    } else {
      for (const c of clase) pool.push(...(itemiClasa[c] ?? []).filter((i) => sursa.niveluri.includes(i.nivel)).map((it) => ({ it, clasa: c })));
    }
    // la clase reunite, întrebările alternează între clase
    const peClase = clase.map((c) => amesteca(pool.filter((p) => p.clasa === c)));
    const comune = amesteca(pool.filter((p) => p.clasa === 0));
    const alese: typeof pool = [];
    for (let r = 0; alese.length < nrIntrebari && r < 50; r++) {
      for (const l of peClase) if (l[r] && alese.length < nrIntrebari) alese.push(l[r]);
      if (comune[r] && alese.length < nrIntrebari) alese.push(comune[r]);
    }
    return alese.map(({ it, clasa }) => publica(it, amesteca, clase.length > 1 && clasa ? clasa : undefined));
  };

  const porneste = async () => {
    setEroare('');
    try {
      intrebari.current = await pregatesteIntrebari();
      if (!intrebari.current.length) { setEroare('Lecțiile alese nu au încă întrebări potrivite pentru jocul live.'); return; }
      const pin = pinNou();
      const c = await deschideCanal(pin);
      canal.current = c;
      setTipCanal(c.tip);
      c.asculta((m) => laMesajRef.current(m));
      const url = `${location.origin}${location.pathname}#live=${pin}`;
      const QR = await import('qrcode');
      setQr(await QR.toString(url, { type: 'svg', margin: 1, errorCorrectionLevel: 'M' }));
      const titlu = sursa.tip === 'eveniment' ? NUME_EVENIMENT[sursa.id] : clase.length > 1 ? `Clase reunite: ${clase.map((x) => `a ${ROMAN[x]}-a`).join(' + ')}` : `Clasa a ${ROMAN[clase[0]]}-a`;
      const st: StareSesiune = {
        pin, titlu, faza: 'lobby', k: -1, total: intrebari.current.length,
        echipe: NUME_ECHIPE.slice(0, nrEchipe).map((nume) => ({ nume, scor: 0 })), jucatori: [],
        durataMs: secunde * 1000, clasamentIndividual: individual, clase,
        ...(sursa.tip === 'eveniment' ? { hartaColectiva: { dezvaluite: 0, total: 0, tema: sursa.id === 'patrula-verde' ? 'verde' as const : 'polara' as const } } : {}),
      };
      setS(st); trimiteStare(st);
    } catch (e) {
      setEroare(e instanceof Error ? e.message : String(e));
    }
  };

  const intrebareUrm = () => {
    const st = stareRef.current!;
    const k = st.k + 1;
    if (k >= intrebari.current.length) { actualizeaza((x) => ({ ...x, faza: 'final', intrebare: undefined, rezultat: undefined })); return; }
    raspunsuri.current = new Map();
    start.current = Date.now();
    actualizeaza((x) => ({ ...x, faza: 'intrebare', k, intrebare: intrebari.current[k].pub, raspunsuri: 0, rezultat: undefined }));
  };

  const arataRezultat = () => {
    const st = stareRef.current;
    if (!st || st.faza !== 'intrebare') return;
    const q = intrebari.current[st.k];
    const castig: Record<string, number> = {};
    const distributie = q.pub.variante ? q.pub.variante.map(() => 0) : undefined;
    let corecte = 0;
    for (const [id, { v, ramas }] of raspunsuri.current) {
      let c = 0;
      if (typeof v === 'number') { if (distributie && v >= 0 && v < distributie.length) distributie[v]++; c = v === q.corect ? 1 : 0; }
      else if (q.tinta && q.toleranta) c = scorPin(v, q.tinta, q.toleranta);
      if (c >= 1) corecte++;
      castig[id] = puncte(c, ramas, st.durataMs);
    }
    actualizeaza((x) => {
      const jucatori = x.jucatori.map((j) => ({ ...j, scor: j.scor + (castig[j.id] ?? 0) }));
      const sc = scoruriEchipe(jucatori, x.echipe.length);
      return {
        ...x, faza: 'rezultat', jucatori, echipe: x.echipe.map((e, i) => ({ ...e, scor: sc[i] })),
        rezultat: { corect: q.corect, tinta: q.tinta, distributie, castig },
        ...(x.hartaColectiva ? { hartaColectiva: { ...x.hartaColectiva, dezvaluite: x.hartaColectiva.dezvaluite + corecte, total: x.hartaColectiva.total + Math.max(1, x.jucatori.length) } } : {}),
      };
    });
  };

  const top = useMemo(() => (s ? [...s.jucatori].sort((a, b) => b.scor - a.scor).slice(0, 5) : []), [s]);

  // ---------------------------------------------------------------- setări
  if (!s) {
    const toateNiv = clase.flatMap((c) => (niveluri[c] ?? []).map((n) => ({ ...n, clasa: c })));
    return (
      <div className="stiva mod-tabla">
        <h1>Joc live</h1>
        <p>Elevii intră de pe telefon cu codul QR și răspund. Tabla arată întrebarea, harta și scorul pe echipe.</p>
        <div className="card stiva">
          <fieldset className="stiva" style={{ border: 0, padding: 0 }}>
            <legend><b>Clasa sau clasele reunite (cel mult două)</b></legend>
            <div className="rand">
              {([5, 6, 7, 8] as Clasa[]).map((k) => (
                <button key={k} className="varianta" style={{ minWidth: 110, textAlign: 'center' }} aria-pressed={clase.includes(k)}
                  onClick={() => { setSursa((x) => (x.tip === 'lectii' ? { tip: 'lectii', niveluri: [] } : x)); setClase((c) => (c.includes(k) ? (c.length > 1 ? c.filter((x) => x !== k) : c) : [...c.slice(-1), k].sort())); }}>
                  a {ROMAN[k]}-a
                </button>
              ))}
            </div>
          </fieldset>
          <fieldset className="stiva" style={{ border: 0, padding: 0 }}>
            <legend><b>Întrebările</b></legend>
            <label className="bifa"><input type="radio" name="sursa" checked={sursa.tip === 'eveniment' && sursa.id === 'expeditia-polara'} onChange={() => setSursa({ tip: 'eveniment', id: 'expeditia-polara' })} /> Expediția Polară (Școala Altfel), cu harta colectivă</label>
            <label className="bifa"><input type="radio" name="sursa" checked={sursa.tip === 'eveniment' && sursa.id === 'patrula-verde'} onChange={() => { setSursa({ tip: 'eveniment', id: 'patrula-verde' }); setClase((c) => (c.length === 2 ? c : c[0] === 5 || c[0] === 7 ? [5, 7] : [6, 8])); }} /> Patrula Verde (Săptămâna verde), cu pădurea colectivă</label>
            {sursa.tip === 'eveniment' && sursa.id === 'patrula-verde' && <PlanPatrula />}
            <label className="bifa"><input type="radio" name="sursa" checked={sursa.tip === 'lectii'} onChange={() => setSursa({ tip: 'lectii', niveluri: [] })} /> Din lecții:</label>
            {sursa.tip === 'lectii' && toateNiv.length === 0 && <p className="eticheta-mica">Clasele alese nu au încă lecții cu conținut (vin în Etapa 4).</p>}
            {sursa.tip === 'lectii' && toateNiv.map((n) => (
              <label key={n.id} className="bifa" style={{ paddingLeft: 36 }}>
                <input type="checkbox" checked={sursa.niveluri.includes(n.id)}
                  onChange={(e) => setSursa((x) => x.tip === 'lectii' ? { tip: 'lectii', niveluri: e.target.checked ? [...x.niveluri, n.id] : x.niveluri.filter((y) => y !== n.id) } : x)} />
                {clase.length > 1 && <b>{ROMAN[n.clasa]}:</b>} {n.titlu}
              </label>
            ))}
          </fieldset>
          <div className="rand">
            <label className="camp"><span>Echipe</span><select value={nrEchipe} onChange={(e) => setNrEchipe(Number(e.target.value))}>{[2, 3, 4].map((n) => <option key={n}>{n}</option>)}</select></label>
            <label className="camp"><span>Întrebări</span><select value={nrIntrebari} onChange={(e) => setNrIntrebari(Number(e.target.value))}>{[5, 8, 10, 15].map((n) => <option key={n}>{n}</option>)}</select></label>
            <label className="camp"><span>Secunde</span><select value={secunde} onChange={(e) => setSecunde(Number(e.target.value))}>{[20, 30, 45].map((n) => <option key={n}>{n}</option>)}</select></label>
          </div>
          <label className="bifa"><input type="checkbox" checked={individual} onChange={(e) => setIndividual(e.target.checked)} /> Arată clasamentul individual (doar primii 5 și locul fiecăruia, pe telefonul lui)</label>
          {eroare && <p className="feedback nu" role="alert">{eroare}</p>}
          <div className="rand">
            <button className="buton secundar" onClick={() => mergi({ e: 'profesor' })}>Înapoi</button>
            <button className="buton" disabled={sursa.tip === 'lectii' && !sursa.niveluri.length} onClick={porneste}>Deschide sala de joc</button>
          </div>
        </div>
      </div>
    );
  }

  // ---------------------------------------------------------------- joc
  const q = s.k >= 0 ? intrebari.current[s.k] : undefined;
  const ramas = s.faza === 'intrebare' ? Math.max(0, Math.ceil((s.durataMs - (Date.now() - start.current)) / 1000)) : 0;
  const url = `${location.origin}${location.pathname}#live=${s.pin}`;
  const scoruri = (
    <div className="scor-echipe" aria-live="polite">
      {s.echipe.map((e, i) => (
        <div key={i} className="echipa">{e.nume} <span className="eticheta-mica">({s.jucatori.filter((j) => j.echipa === i).length})</span><b>{e.scor} p</b></div>
      ))}
      {s.faza === 'intrebare' && <div className="echipa activa">Timp<b>0:{String(ramas).padStart(2, '0')}</b></div>}
    </div>
  );

  return (
    <div className="stiva mod-tabla">
      <div className="rand" style={{ justifyContent: 'space-between' }}>
        <h1 style={{ margin: 0 }}>{s.titlu}</h1>
        <div className="rand">
          <span className="eticheta-mica">PIN <b style={{ fontSize: '1.4em', letterSpacing: '.1em' }}>{s.pin}</b></span>
          <button className="buton secundar mic" onClick={() => document.documentElement.requestFullscreen?.()}>Ecran complet</button>
          <button className="buton secundar mic" onClick={() => { canal.current?.inchide(); mergi({ e: 'profesor' }); }}>Închide jocul</button>
        </div>
      </div>
      {tipCanal === 'local' && (
        <p className="feedback nu"><strong>Mod demonstrație</strong>Serverul jocului nu e configurat, așa că pot intra doar alte ferestre deschise pe acest calculator. Pentru telefoane, urmează docs/ghid-joc-live.md.</p>
      )}

      {s.faza === 'lobby' && (
        <div className="rand" style={{ alignItems: 'flex-start' }}>
          <div className="card" style={{ flex: '0 0 auto', textAlign: 'center' }}>
            <div style={{ width: 300, height: 300, background: '#fff', padding: 8, borderRadius: 12 }} dangerouslySetInnerHTML={{ __html: qr }} aria-label="Cod QR pentru intrarea în joc" role="img" />
            <p className="eticheta-mica" style={{ maxWidth: 300, wordBreak: 'break-all', margin: '8px auto 0' }}>{url}</p>
          </div>
          <div className="card stiva" style={{ flex: 1, minWidth: 280 }}>
            <h2>Scanează codul sau intră cu PIN-ul {s.pin}</h2>
            <p>Alege o poreclă, nu numele tău real. {s.jucatori.length ? `Au intrat ${s.jucatori.length} exploratori.` : 'Așteptăm primii exploratori…'}</p>
            <div className="rand">
              {s.echipe.map((e, i) => (
                <div key={i} className="echipa" style={{ minWidth: 200 }}>
                  <b style={{ fontSize: '1em' }}>{e.nume}</b>
                  {s.jucatori.filter((j) => j.echipa === i).map((j) => <div key={j.id}>{j.avatar} {j.porecla}</div>)}
                </div>
              ))}
            </div>
            <button className="buton" disabled={!s.jucatori.length} onClick={intrebareUrm}>Începe ({s.total} întrebări)</button>
          </div>
        </div>
      )}

      {(s.faza === 'intrebare' || s.faza === 'rezultat') && q && (
        <>
          {scoruri}
          <div className="card stiva">
            <p className="eticheta-mica" style={{ margin: 0 }}>
              Întrebarea {s.k + 1} din {s.total}{q.pub.pentruClasa ? ` · pentru clasa a ${ROMAN[q.pub.pentruClasa]}-a` : ''}
              {s.faza === 'intrebare' && ` · au răspuns ${s.raspunsuri ?? 0} din ${s.jucatori.length}`}
            </p>
            <p className="enunt" style={{ fontSize: '1.3em', margin: 0 }}>{q.pub.enunt}</p>
            <div className="rand" style={{ alignItems: 'flex-start', flexWrap: 'wrap' }}>
              {(q.pub.harta || q.pub.schema || q.pub.grafic) && (
                <div style={{ flex: '1 1 520px', maxWidth: 900 }}><VizualIntrebare it={q.pub} tinta={s.faza === 'rezultat' ? q.tinta : undefined} /></div>
              )}
              {q.pub.variante && (
                <div style={{ flex: '1 1 420px' }}>
                  <VarianteLive variante={q.pub.variante} corect={s.faza === 'rezultat' ? q.corect : undefined} distributie={s.faza === 'rezultat' ? s.rezultat?.distributie : undefined} />
                </div>
              )}
              {q.pub.tip === 'pin' && s.faza === 'intrebare' && <p style={{ flex: '1 1 300px' }}>Pune pionul pe harta de pe telefon.</p>}
            </div>
            <div className="rand" style={{ justifyContent: 'flex-end' }}>
              {s.faza === 'intrebare'
                ? <button className="buton secundar" onClick={arataRezultat}>Oprește timpul</button>
                : <button className="buton" onClick={intrebareUrm} autoFocus>{s.k + 1 < s.total ? 'Următoarea întrebare' : 'Vezi clasamentul'}</button>}
            </div>
          </div>
          {s.faza === 'rezultat' && s.hartaColectiva && <div className="card"><VizualColectiv {...s.hartaColectiva} /></div>}
        </>
      )}

      {s.faza === 'final' && (
        <div className="stiva" style={{ textAlign: 'center' }}>
          <h2>Clasamentul echipelor</h2>
          <div className="scor-echipe">
            {[...s.echipe].map((e, i) => ({ ...e, i })).sort((a, b) => b.scor - a.scor).map((e, loc) => (
              <div key={e.i} className={`echipa ${loc === 0 ? 'activa' : ''}`}>Locul {loc + 1}: {e.nume}<b>{e.scor} p</b></div>
            ))}
          </div>
          {s.clasamentIndividual && (
            <div className="card" style={{ textAlign: 'left' }}>
              <h3>Primii 5 exploratori</h3>
              <ol>{top.map((j) => <li key={j.id}>{j.avatar} {j.porecla}: {j.scor} p</li>)}</ol>
            </div>
          )}
          {s.hartaColectiva && <div className="card"><VizualColectiv {...s.hartaColectiva} /></div>}
          <div className="rand" style={{ justifyContent: 'center' }}>
            <button className="buton secundar" onClick={() => { canal.current?.inchide(); setS(null); }}>Joc nou</button>
            <button className="buton" onClick={() => { canal.current?.inchide(); mergi({ e: 'profesor' }); }}>Închide</button>
          </div>
        </div>
      )}

      <div aria-hidden="true" style={{ position: 'fixed', right: 24, bottom: 24, display: 'flex', flexDirection: 'column-reverse', gap: 4, fontSize: 40, pointerEvents: 'none' }}>
        {reactii.map((r) => <span key={r.k}>{r.r}</span>)}
      </div>
    </div>
  );
}

type PlanAtelier = { titlu: string; minute: number; tehnologie: string[]; descriere: string; rezultat: string; siguranta?: string[] };
type Plan = { zi: string; durata: string; grupe: { clase: number[]; titlu: string }[]; ateliere: PlanAtelier[]; pentruGrupe: Record<string, string>; surse: string[] };

/** Planul atelierelor Patrulei Verzi, pentru profesor. */
function PlanPatrula() {
  const [plan, setPlan] = useState<Plan>();
  useEffect(() => { incarca<{ plan: Plan }>('content/evenimente/patrula-verde.json').then((e) => setPlan(e.plan)); }, []);
  if (!plan) return null;
  return (
    <details className="card" style={{ paddingLeft: 36 }}>
      <summary><b>Planul activității (miercuri, {plan.zi.split('-').reverse().join('.')}, {plan.durata})</b></summary>
      <p>{plan.grupe.map((g) => g.titlu).join(' · ')}</p>
      <ol className="stiva">
        {plan.ateliere.map((a) => (
          <li key={a.titlu}>
            <b>{a.titlu}</b> ({a.minute} min) – <i>{a.tehnologie.join(', ')}</i>
            <br />{a.descriere}<br /><span className="eticheta-mica">Rezultat: {a.rezultat}</span>
            {a.siguranta && <ul>{a.siguranta.map((x) => <li key={x}>{x}</li>)}</ul>}
          </li>
        ))}
      </ol>
      {Object.entries(plan.pentruGrupe).map(([k, v]) => <p key={k}><b>Clasele {k.replace('-', ' + ')}:</b> {v}</p>)}
      <p className="eticheta-mica">Reguli pentru dronă: {plan.surse.join('; ')}.</p>
    </details>
  );
}
