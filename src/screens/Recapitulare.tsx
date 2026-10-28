import { useEffect, useMemo, useState } from 'react';
import { useApp } from '../state';
import { amesteca } from '../content';
import { Exercitiu, type Rezultat } from '../engine/Exercitiu';
import { inregistreazaRaspuns } from '../game/progres';
import { alegeRecapitulare, notaOrientativa, stapanire, stareItemi, type StareItem } from '../game/recapitulare';
import { adaugaXP, db } from '../db/db';
import { Geo } from '../ui/Geo';
import type { Item } from '../types';

type Sesiune = { titlu: string; itemi: Item[]; test: boolean };

/**
 * Recapitularea pentru Evaluarea Națională (clasa a VIII-a): stăpânirea pe unități,
 * recapitulare pe unitate (feedback imediat) și test de recapitulare (20 de itemi, feedback la final, notă orientativă).
 */
export function Recapitulare() {
  const { continut, cal, profil, azi, deblocate, mergi } = useApp();
  const [stare, setStare] = useState<Map<string, StareItem> | null>(null);
  const [ses, setSes] = useState<Sesiune | null>(null);
  const [k, setK] = useState(0);
  const [rez, setRez] = useState<Rezultat[]>([]);

  useEffect(() => { db.raspunsuri.toArray().then((r) => setStare(stareItemi(r))); }, [ses]);

  // unitățile clasei, în ordinea calendarului, cu itemii lecțiilor deja deschise
  const unitati = useMemo(() => {
    if (!continut || !profil) return [];
    const ordine: string[] = [];
    const nivPeUnit = new Map<string, Set<string>>();
    for (const n of cal.niveluri.filter((x) => x.clasa === profil.clasa).sort((a, b) => a.saptamana - b.saptamana)) {
      if (!deblocate.has(n.id)) continue;
      if (!nivPeUnit.has(n.unitate)) { nivPeUnit.set(n.unitate, new Set()); ordine.push(n.unitate); }
      nivPeUnit.get(n.unitate)!.add(n.id);
    }
    const toti = [...continut.itemi.values()];
    return ordine.map((u) => ({ unitate: u, itemi: toti.filter((i) => nivPeUnit.get(u)!.has(i.nivel)) })).filter((u) => u.itemi.length);
  }, [continut, profil, deblocate]); // eslint-disable-line react-hooks/exhaustive-deps

  if (!stare) return null;
  const totiItemii = unitati.flatMap((u) => u.itemi);
  const gresiti = totiItemii.filter((i) => stare.get(i.id)?.ultimulCorect === false);

  const porneste = (titlu: string, itemi: Item[], cate: number, test: boolean) => {
    setSes({ titlu, itemi: alegeRecapitulare(itemi, stare, cate, amesteca), test });
    setK(0); setRez([]);
  };

  if (ses && k < ses.itemi.length) {
    return (
      <div className="stiva">
        <div className="rand">
          <button className="buton-icon" onClick={() => setSes(null)} aria-label="Înapoi la recapitulare">✕</button>
          <b style={{ flex: 1 }}>{ses.titlu} · {k + 1} din {ses.itemi.length}</b>
        </div>
        <div className="card">
          <Exercitiu key={ses.itemi[k].id} item={ses.itemi[k]} feedbackImediat={!ses.test} onGata={async (r) => {
            await inregistreazaRaspuns(cal, profil!.clasa, ses.itemi[k], r, azi);
            setRez((x) => [...x, r]);
            setK(k + 1);
          }} />
        </div>
      </div>
    );
  }

  if (ses) {
    const corecte = rez.filter((r) => r.corect).length;
    const nota = notaOrientativa(corecte, ses.itemi.length);
    return (
      <div className="stiva">
        <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
          <Geo marime={88} stare={corecte / ses.itemi.length >= 0.5 ? 'bucuros' : 'gandeste'} />
          <h1>{ses.test ? 'Testul de recapitulare s-a încheiat' : 'Recapitulare încheiată'}</h1>
          <p>{corecte} răspunsuri corecte din {ses.itemi.length}.</p>
          {ses.test && <p>Nota orientativă: <b>{nota.toFixed(2).replace('.', ',')}</b> (cu un punct din oficiu). E doar pentru tine, ca să vezi unde ești.</p>}
          <button className="buton" onClick={async () => { await adaugaXP(corecte * 2, 'recapitulare EN', azi); setSes(null); }}>Înapoi la recapitulare</button>
        </div>
        {ses.test && (
          <div className="card">
            <h2>Ce ai greșit</h2>
            {corecte === ses.itemi.length && <p>Nimic. Bravo!</p>}
            <ul className="stiva" style={{ paddingLeft: 18 }}>
              {ses.itemi.map((it, i) => !rez[i]?.corect && <li key={it.id}><b>{it.enunt}</b><br />{it.feedback.gresit}</li>)}
            </ul>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="stiva">
      <div className="rand">
        <button className="buton-icon" onClick={() => mergi({ e: 'harta' })} aria-label="Înapoi la hartă">✕</button>
        <h1 style={{ margin: 0, flex: 1 }}>Recapitulare pentru Evaluarea Națională</h1>
      </div>
      <div className="card rand" style={{ gap: 16 }}>
        <Geo stare="gandeste" />
        <p style={{ margin: 0, flex: 1 }}>Reiei geografia României, unitate cu unitate. Bara arată ce ai rezolvat corect ultima dată. Începem cu ce ai greșit și cu ce n-ai încercat încă.</p>
      </div>
      <div className="rand">
        <button className="buton" disabled={!totiItemii.length} onClick={() => porneste('Test de recapitulare', totiItemii, 20, true)}>Test de recapitulare (20 de întrebări)</button>
        <button className="buton secundar" disabled={!gresiti.length} onClick={() => porneste('Greșelile mele', gresiti, 10, false)}>Greșelile mele ({gresiti.length})</button>
      </div>
      {unitati.map((u) => {
        const p = Math.round(stapanire(u.itemi, stare) * 100);
        return (
          <div key={u.unitate} className="card stiva">
            <div className="rand" style={{ justifyContent: 'space-between' }}>
              <b>{u.unitate}</b>
              <span className="eticheta-mica">{p} % stăpânit · {u.itemi.length} întrebări</span>
            </div>
            <div role="progressbar" aria-valuenow={p} aria-valuemin={0} aria-valuemax={100} aria-label={`Stăpânire: ${u.unitate}`}
              style={{ height: 12, borderRadius: 6, background: 'var(--ceata)', overflow: 'hidden' }}>
              <div style={{ width: `${p}%`, height: '100%', background: p >= 80 ? 'var(--campie)' : p >= 50 ? 'var(--podis)' : 'var(--munte)' }} />
            </div>
            <button className="buton mic" onClick={() => porneste(u.unitate, u.itemi, 10, false)}>Recapitulează (10 întrebări)</button>
          </div>
        );
      })}
      {!unitati.length && <p>Încă nu sunt lecții deschise de recapitulat.</p>}
    </div>
  );
}
