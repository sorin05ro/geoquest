import { useMemo, useState } from 'react';
import { useApp } from '../state';
import { amesteca, itemiNivel } from '../content';
import { Exercitiu, citesteCuVoce, type Rezultat } from '../engine/Exercitiu';
import { inregistreazaRaspuns, terminaNivel } from '../game/progres';
import { XP } from '../game/rules';
import { Schema } from '../maps/Scheme';
import { Geo } from '../ui/Geo';
import { db } from '../db/db';
import type { ContinutNivel, Item } from '../types';

type Faza = 'descopera' | 'invata' | 'exerseaza' | 'aplica' | 'stele';
const FAZE: Faza[] = ['descopera', 'invata', 'exerseaza', 'aplica', 'stele'];
const NUME: Record<Faza, string> = { descopera: 'Descoperă', invata: 'Învață', exerseaza: 'Exersează', aplica: 'Aplică', stele: 'Stele' };

/** Alege itemii unui nivel: 6 la exersare (în jurul dificultății elevului) și 1 mai greu la „Aplică”. */
export function alegeItemi(toti: Item[], dif: 1 | 2 | 3) {
  const amestecati = amesteca(toti);
  const aplica = amestecati.find((i) => i.dificultate === 3) ?? amestecati.find((i) => i.dificultate === 2) ?? amestecati[0];
  const rest = amestecati.filter((i) => i !== aplica);
  const prioritate = (i: Item) => Math.abs(i.dificultate - dif) + (i.dificultate === 3 && dif === 1 ? 1 : 0);
  const exersare = [...rest].sort((a, b) => prioritate(a) - prioritate(b)).slice(0, 6).sort((a, b) => a.dificultate - b.dificultate);
  return { exersare, aplica };
}

export function Nivel({ id }: { id: string }) {
  const { continut, profil, mergi } = useApp();
  const niv = continut?.niveluri.get(id);
  if (!continut || !niv) {
    return (
      <div className="stiva card">
        <Geo stare="gandeste" />
        <h1>Nivelul se pregătește</h1>
        <p>Geo încă desenează harta pentru această lecție. Revino curând.</p>
        <button className="buton" onClick={() => mergi({ e: 'harta' })}>Înapoi la hartă</button>
      </div>
    );
  }
  return niv.tip === 'expeditie' ? <Expeditie niv={niv} /> : <Lectie niv={niv} dif={profil!.dificultate} />;
}

function Lectie({ niv, dif }: { niv: ContinutNivel; dif: 1 | 2 | 3 }) {
  const { continut, cal, profil, azi, mergi } = useApp();
  const { exersare, aplica } = useMemo(() => alegeItemi(itemiNivel(continut!, niv.id), dif), [niv.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [faza, setFaza] = useState<Faza>('descopera');
  const [card, setCard] = useState(0);
  const [k, setK] = useState(0);
  const [rez, setRez] = useState<Rezultat[]>([]);
  const [xpCastigat, setXp] = useState(0);
  const [final, setFinal] = useState<{ stele: number; primaData: boolean } | null>(null);

  const raspuns = async (item: Item, r: Rezultat) => {
    const xp = await inregistreazaRaspuns(cal, profil!.clasa, item, r, azi);
    setXp((x) => x + xp);
    const toate = [...rez, r];
    setRez(toate);
    if (faza === 'exerseaza' && k + 1 < exersare.length) { setK(k + 1); return; }
    if (faza === 'exerseaza') { setFaza('aplica'); return; }
    // final
    const scor = toate.reduce((s, x) => s + (x.corect ? 1 : x.scor * 0.5), 0) / toate.length;
    const indicii = toate.filter((x) => x.indiciu).length;
    const f = await terminaNivel(niv.id, scor, indicii, azi);
    if (f.primaData) setXp((x) => x + XP.nivelTerminat);
    setFinal(f);
    setFaza('stele');
  };

  const idx = FAZE.indexOf(faza);
  return (
    <div className="stiva">
      <div className="rand">
        <button className="buton-icon" onClick={() => mergi({ e: 'harta' })} aria-label="Înapoi la hartă">✕</button>
        <div style={{ flex: 1 }}>
          <div className="eticheta-mica">{niv.titlu}</div>
          <div className="pasi" aria-label={`Pasul ${idx + 1} din 5: ${NUME[faza]}`}>
            {FAZE.map((f, i) => <i key={f} className={i < idx ? 'facut' : i === idx ? 'acum' : ''} />)}
          </div>
        </div>
      </div>

      {faza === 'descopera' && (
        <div className="card stiva">
          <h2>{NUME.descopera}</h2>
          {niv.descopera.schema && <Schema id={niv.descopera.schema} />}
          <div className="rand" style={{ alignItems: 'flex-start', flexWrap: 'nowrap' }}>
            <Geo stare="gandeste" />
            <p style={{ fontSize: '1.15em' }}>{niv.descopera.intrebare}</p>
          </div>
          <p className="eticheta-mica">Gândește-te puțin. Răspunsul îl afli în pasul următor.</p>
          <button className="buton" onClick={() => setFaza('invata')} autoFocus>Află</button>
        </div>
      )}

      {faza === 'invata' && (
        <div className="card stiva">
          <h2>{niv.invata[card].titlu}</h2>
          {niv.invata[card].schema && <Schema id={niv.invata[card].schema!} />}
          {niv.invata[card].text.split('\n').map((p, i) => <p key={i}>{p}</p>)}
          {card === niv.invata.length - 1 && niv.stiaiCa && (
            <p className="feedback ok"><strong>Știai că…</strong>{niv.stiaiCa}</p>
          )}
          <div className="rand" style={{ justifyContent: 'space-between' }}>
            <button className="buton secundar mic" onClick={() => citesteCuVoce(niv.invata[card].titlu + '. ' + niv.invata[card].text)}>Citește-mi</button>
            <span className="eticheta-mica">{card + 1} / {niv.invata.length}</span>
            {card + 1 < niv.invata.length
              ? <button className="buton" onClick={() => setCard(card + 1)}>Mai departe</button>
              : <button className="buton" onClick={() => setFaza('exerseaza')}>Exersează</button>}
          </div>
        </div>
      )}

      {faza === 'exerseaza' && exersare[k] && (
        <div className="card">
          <p className="eticheta-mica">{NUME.exerseaza} · {k + 1} din {exersare.length} · +{xpCastigat} XP</p>
          <Exercitiu key={exersare[k].id} item={exersare[k]} onGata={(r) => raspuns(exersare[k], r)} />
        </div>
      )}

      {faza === 'aplica' && aplica && (
        <div className="card">
          <p className="eticheta-mica">{NUME.aplica}: provocarea nivelului</p>
          <Exercitiu key={aplica.id} item={aplica} onGata={(r) => raspuns(aplica, r)} textContinua="Vezi stelele" />
        </div>
      )}

      {faza === 'stele' && final && (
        <div className="card stiva" style={{ textAlign: 'center', alignItems: 'center' }}>
          <Geo marime={96} stare="bucuros" />
          <h2>Nivel parcurs!</h2>
          <div className="stele" aria-label={`${final.stele} stele din 3`}>
            {[1, 2, 3].map((s) => <span key={s} className={s <= final.stele ? '' : 'goala'}>★</span>)}
          </div>
          <p>Ai răspuns corect la {rez.filter((r) => r.corect).length} din {rez.length} și ai câștigat {xpCastigat} XP.</p>
          {final.stele < 3 && <p className="eticheta-mica">3 stele: cel puțin 95 % corect, fără indicii. Poți relua nivelul oricând.</p>}
          <div className="rand" style={{ justifyContent: 'center' }}>
            <button className="buton secundar" onClick={() => mergi({ e: 'nivel', id: niv.id, n: Date.now() })}>Reia nivelul</button>
            <button className="buton" onClick={() => mergi({ e: 'harta' })} autoFocus>Înapoi la hartă</button>
          </div>
        </div>
      )}
    </div>
  );
}

function Expeditie({ niv }: { niv: ContinutNivel }) {
  const { continut, cal, profil, azi, mergi } = useApp();
  const pasi = niv.pasi ?? [];
  const [p, setP] = useState(0);
  const [k, setK] = useState(0);
  const [text, setText] = useState('');
  const [foto, setFoto] = useState<File | null>(null);
  const [rez, setRez] = useState<Rezultat[]>([]);
  const [gata, setGata] = useState(false);
  const pas = pasi[p];
  const itemi = (pas?.itemi ?? []).map((id) => continut!.itemi.get(id)).filter(Boolean) as Item[];

  const urmPas = async () => {
    if (pas.jurnal) await db.jurnal.add({ nivel: niv.id, pas: p, text, foto: foto ?? undefined, data: azi });
    setText(''); setFoto(null); setK(0);
    if (p + 1 < pasi.length) { setP(p + 1); return; }
    const scor = rez.length ? rez.filter((r) => r.corect).length / rez.length : 1;
    await terminaNivel(niv.id, scor, rez.filter((r) => r.indiciu).length, azi, XP.expeditie);
    setGata(true);
  };

  if (gata) {
    return (
      <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
        <div className="stampila">EXPEDIȚIE<br />ÎNCHEIATĂ</div>
        <h2>{niv.titlu.replace(/^Aplicații? practice?(\/studii de caz)?:\s*/i, '')}</h2>
        <p>Ai primit {XP.expeditie} XP. Ce ai scris în Jurnalul exploratorului îl poate vedea profesorul.</p>
        <button className="buton" onClick={() => mergi({ e: 'harta' })} autoFocus>Înapoi la hartă</button>
      </div>
    );
  }

  return (
    <div className="stiva">
      <div className="rand">
        <button className="buton-icon" onClick={() => mergi({ e: 'harta' })} aria-label="Înapoi la hartă">✕</button>
        <div style={{ flex: 1 }}>
          <div className="eticheta-mica">Expediție · pasul {p + 1} din {pasi.length}</div>
          <div className="pasi">{pasi.map((_, i) => <i key={i} className={i < p ? 'facut' : i === p ? 'acum' : ''} />)}</div>
        </div>
      </div>
      <div className="card stiva">
        <h2>{pas.titlu}</h2>
        {pas.text.split('\n').map((t, i) => <p key={i}>{t}</p>)}
        {itemi[k] && <Exercitiu key={itemi[k].id} item={itemi[k]} onGata={async (r) => {
          await inregistreazaRaspuns(cal, profil!.clasa, itemi[k], r, azi);
          setRez((x) => [...x, r]);
          setK(k + 1);
        }} />}
        {k >= itemi.length && pas.jurnal && (
          <div className="stiva">
            <label className="camp"><span><b>Jurnalul exploratorului:</b> {pas.jurnal.cerinta}</span>
              <textarea rows={4} value={text} onChange={(e) => setText(e.target.value)} />
            </label>
            {pas.jurnal.foto && (
              <label className="camp"><span>Fotografia lucrării tale (opțional; fără persoane în imagine)</span>
                <input type="file" accept="image/*" capture="environment" onChange={(e) => setFoto(e.target.files?.[0] ?? null)} />
              </label>
            )}
          </div>
        )}
        {k >= itemi.length && (
          <div className="rand" style={{ justifyContent: 'flex-end' }}>
            <button className="buton" onClick={urmPas} disabled={!!pas.jurnal && text.trim().length < 10}>
              {p + 1 < pasi.length ? 'Pasul următor' : 'Încheie expediția'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
