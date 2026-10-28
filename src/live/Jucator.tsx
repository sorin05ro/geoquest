import { useEffect, useRef, useState } from 'react';
import { useApp } from '../state';
import { MapView } from '../maps/MapView';
import { Geo } from '../ui/Geo';
import type { Punct } from '../types';
import { deschideCanal, type Canal } from './canal';
import { REACTII, SIMBOLURI, type Mesaj, type StareSesiune } from './protocol';
import { VarianteLive } from './Vizual';

const AVATARE = ['🦉', '🦊', '🐻', '🦅', '🐺', '🦌', '🐢', '🐬'];
const ROMAN: Record<number, string> = { 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII' };

function idJucator(pin: string) {
  const cheie = `geoquest-live-${pin}`;
  try {
    const v = sessionStorage.getItem(cheie);
    if (v) return v;
    const nou = crypto.randomUUID();
    sessionStorage.setItem(cheie, nou);
    return nou;
  } catch { return crypto.randomUUID(); }
}

/** Jocul live, pe telefonul elevului. Se deschide din codul QR (adresa se termină cu #live=PIN). */
export function Jucator({ pinInitial }: { pinInitial: string }) {
  const { profil } = useApp();
  const [pin, setPin] = useState(pinInitial);
  const [porecla, setPorecla] = useState(profil?.porecla ?? '');
  const [avatar, setAvatar] = useState(profil?.avatar ?? AVATARE[0]);
  const [clasa, setClasa] = useState<number | undefined>(profil?.clasa);
  const [intrat, setIntrat] = useState(false);
  const [s, setS] = useState<StareSesiune | null>(null);
  const [eroare, setEroare] = useState('');
  const [ales, setAles] = useState<{ k: number; v: number | Punct } | null>(null);
  const [punctPin, setPunctPin] = useState<Punct | null>(null);
  const [termen, setTermen] = useState(0);
  const [, tick] = useState(0);
  const canal = useRef<Canal | null>(null);
  const id = useRef('');

  useEffect(() => () => canal.current?.inchide(), []);
  useEffect(() => {
    if (s?.faza !== 'intrebare') return;
    const t = setInterval(() => tick((x) => x + 1), 500);
    return () => clearInterval(t);
  }, [s?.faza]);

  const eu = s?.jucatori.find((j) => j.id === id.current);

  // retrimite cererea de intrare până apare în listă
  useEffect(() => {
    if (!intrat || eu) return;
    const t = setInterval(() => canal.current?.trimite({ t: 'intra', id: id.current, porecla, avatar, clasa }), 2000);
    return () => clearInterval(t);
  }, [intrat, !!eu]); // eslint-disable-line react-hooks/exhaustive-deps

  const intra = async () => {
    setEroare('');
    try {
      id.current = idJucator(pin);
      const c = await deschideCanal(pin);
      canal.current = c;
      c.asculta((m: Mesaj) => {
        if (m.t !== 'stare') return;
        setS((vechi) => {
          if (m.s.faza === 'intrebare' && (vechi?.k !== m.s.k || vechi?.faza !== 'intrebare')) {
            setTermen(Date.now() + (m.s.ramasMs ?? m.s.durataMs));
            setPunctPin(null);
          }
          return m.s;
        });
      });
      c.trimite({ t: 'intra', id: id.current, porecla: porecla.trim(), avatar, clasa });
      c.trimite({ t: 'cer-stare' });
      setIntrat(true);
    } catch (e) {
      setEroare(e instanceof Error ? e.message : String(e));
    }
  };

  const raspunde = (v: number | Punct) => {
    if (!s || ales?.k === s.k) return;
    setAles({ k: s.k, v });
    canal.current?.trimite({ t: 'raspuns', id: id.current, k: s.k, v });
  };
  const reactioneaza = (r: string) => canal.current?.trimite({ t: 'reactie', id: id.current, r });

  if (!intrat) {
    return (
      <div className="bun-venit">
        <div className="rand" style={{ flexWrap: 'nowrap' }}><Geo marime={72} /><h1 style={{ margin: 0 }}>Intră în joc</h1></div>
        <label className="camp"><span>PIN-ul de pe tablă</span>
          <input inputMode="numeric" autoComplete="off" maxLength={6} value={pin} onChange={(e) => setPin(e.target.value.replace(/\D/g, ''))} />
        </label>
        <label className="camp"><span>Poreclă (nu numele tău real)</span>
          <input value={porecla} onChange={(e) => setPorecla(e.target.value)} maxLength={24} autoComplete="off" />
        </label>
        <div className="avatare" role="group" aria-label="Avatar">
          {AVATARE.map((a) => <button key={a} className="avatar" aria-pressed={avatar === a} onClick={() => setAvatar(a)} aria-label={`Avatar ${a}`}>{a}</button>)}
        </div>
        <div className="rand" role="group" aria-label="Clasa ta">
          {[5, 6, 7, 8].map((c) => <button key={c} className="varianta" style={{ minWidth: 72, textAlign: 'center' }} aria-pressed={clasa === c} onClick={() => setClasa(c)}>a {ROMAN[c]}-a</button>)}
        </div>
        {eroare && <p className="feedback nu" role="alert">{eroare}</p>}
        <button className="buton" disabled={pin.length !== 6 || porecla.trim().length < 2} onClick={intra}>Intră</button>
      </div>
    );
  }

  const echipa = eu ? s?.echipe[eu.echipa] : undefined;
  const antet = (
    <div className="rand" style={{ justifyContent: 'space-between' }}>
      <span><span style={{ fontSize: 28 }} aria-hidden="true">{avatar}</span> <b>{porecla}</b></span>
      {echipa && <span className="eticheta-mica">{echipa.nume} · {eu?.scor ?? 0} p</span>}
    </div>
  );
  const reactii = (
    <div className="rand" role="group" aria-label="Reacții" style={{ justifyContent: 'center' }}>
      {REACTII.map((r) => <button key={r} className="buton-icon" onClick={() => reactioneaza(r)} aria-label={`Trimite reacția ${r}`} style={{ fontSize: 24 }}>{r}</button>)}
    </div>
  );

  if (!s || !eu) {
    return <div className="stiva">{antet}<div className="card stiva" style={{ alignItems: 'center' }}><Geo stare="gandeste" /><p>Mă conectez la sala de joc {pin}…</p></div></div>;
  }

  if (s.faza === 'lobby') {
    return (
      <div className="stiva">{antet}
        <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
          <Geo marime={88} stare="bucuros" />
          <h2>Ești în {echipa?.nume}!</h2>
          <p>Uită-te la tablă. Jocul începe când e gata profesorul.</p>
        </div>
        {reactii}
      </div>
    );
  }

  if (s.faza === 'intrebare' && s.intrebare) {
    const it = s.intrebare;
    const dat = ales?.k === s.k;
    const sec = Math.max(0, Math.ceil((termen - Date.now()) / 1000));
    return (
      <div className="stiva">{antet}
        <div className="rand" style={{ justifyContent: 'space-between' }}>
          <span className="eticheta-mica">Întrebarea {s.k + 1} din {s.total}</span>
          <b aria-live="off">{sec} s</b>
        </div>
        <p className="enunt" style={{ margin: 0 }}>{it.enunt}</p>
        {dat ? (
          <div className="card stiva" style={{ alignItems: 'center' }}><Geo stare="gandeste" /><p>Răspuns trimis. Așteaptă rezultatul pe tablă.</p></div>
        ) : it.tip === 'pin' && it.harta ? (
          <>
            <MapView harta={it.harta} eticheta="Atinge locul cerut" onPick={(lon, lat) => setPunctPin({ lat, lon })}
              overlay={(p) => punctPin && (() => { const [x, y] = p([punctPin.lon, punctPin.lat]) ?? [0, 0]; return <path d={`M${x} ${y} l-10 -24 a10 10 0 1 1 20 0 z`} fill="var(--pion)" stroke="var(--hartie)" strokeWidth="2" />; })()} />
            <button className="buton" disabled={!punctPin} onClick={() => punctPin && raspunde(punctPin)}>Trimite</button>
          </>
        ) : it.variante ? (
          <div className="stiva">
            {it.variante.map((v, i) => (
              <button key={i} className="varianta" style={{ minHeight: 64, display: 'flex', gap: 12, alignItems: 'center' }} onClick={() => raspunde(i)}>
                <span aria-hidden="true" style={{ fontSize: '1.4em', color: 'var(--mare-2)' }}>{SIMBOLURI.at(i)}</span><b>{String.fromCharCode(65 + i)}.</b> {v}
              </button>
            ))}
          </div>
        ) : null}
      </div>
    );
  }

  if (s.faza === 'rezultat') {
    const castig = s.rezultat?.castig[id.current];
    const raspuns = ales?.k === s.k ? ales.v : undefined;
    return (
      <div className="stiva">{antet}
        <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
          <Geo marime={80} stare={castig ? 'bucuros' : 'gandeste'} />
          <h2>{raspuns === undefined ? 'Nu ai răspuns la timp' : castig ? `Corect! +${castig} p` : 'Nu de data asta'}</h2>
          {s.intrebare?.variante && s.rezultat?.corect !== undefined && (
            <VarianteLive variante={s.intrebare.variante} corect={s.rezultat.corect} ales={typeof raspuns === 'number' ? raspuns : null} dezactivat />
          )}
          {s.rezultat?.tinta && <p>Locul corect: {s.rezultat.tinta.nume}</p>}
        </div>
        {reactii}
      </div>
    );
  }

  // final
  const locEchipa = [...s.echipe].sort((a, b) => b.scor - a.scor).findIndex((e) => e.nume === echipa?.nume) + 1;
  const locIndividual = [...s.jucatori].sort((a, b) => b.scor - a.scor).findIndex((j) => j.id === id.current) + 1;
  return (
    <div className="stiva">{antet}
      <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
        <Geo marime={96} stare="bucuros" />
        <h2>{echipa?.nume} e pe locul {locEchipa}!</h2>
        <p>Ai adus echipei {eu.scor} puncte.{s.clasamentIndividual ? ` Ești pe locul ${locIndividual} din ${s.jucatori.length}.` : ''}</p>
      </div>
      {reactii}
    </div>
  );
}
