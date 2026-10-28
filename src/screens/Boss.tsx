import { useMemo, useState } from 'react';
import { useApp } from '../state';
import { amesteca } from '../content';
import { Exercitiu, type Rezultat } from '../engine/Exercitiu';
import { inregistreazaRaspuns, terminaNivel } from '../game/progres';
import { XP } from '../game/rules';
import { citesteSetare, scrieSetare, db } from '../db/db';
import { Geo } from '../ui/Geo';
import type { Item } from '../types';

/** Dificultatea de pornire aleasă de Busola de start (T₀), după procentul de răspunsuri corecte. */
export function dificultateDinBusola(scor: number): 1 | 2 | 3 {
  return scor >= 0.8 ? 3 : scor >= 0.5 ? 2 : 1;
}

/**
 * Testele clasei, pe același ecran:
 * - T₀, Busola de start: fără notă, cu feedback imediat; rezultatul alege dificultatea de pornire;
 * - T₁–T₅, Boss-urile: 15 itemi mixți din unitate, feedback abia la final, o reluare;
 * - Tf, Marea Expediție: 20 de itemi din tot anul.
 */
export function Boss({ id }: { id: string }) {
  const { continut, cal, profil, azi, mergi } = useApp();
  const b = continut?.boss.find((x) => x.id === id);
  const eBusola = b?.test === 'T0';
  const eFinal = b?.test === 'Tf';
  const total = eFinal ? 20 : 15;
  const itemi = useMemo(() => {
    if (!b || !continut) return [];
    const toti = [...continut.itemi.values()].filter((i) => b.niveluri.includes(i.nivel) || b.itemiSuplimentari?.includes(i.id));
    // câte un item din fiecare nivel, apoi restul, dificultăți amestecate
    const peNivel = b.niveluri.map((n) => amesteca(toti.filter((i) => i.nivel === n)));
    const ales: Item[] = [];
    for (let r = 0; ales.length < total && r < 30; r++) for (const l of amesteca(peNivel)) if (l[r] && ales.length < total) ales.push(l[r]);
    return ales;
  }, [b?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const [start, setStart] = useState(false);
  const [k, setK] = useState(0);
  const [rez, setRez] = useState<Rezultat[]>([]);
  const [final, setFinal] = useState(false);
  const [incercari, setIncercari] = useState<number | null>(null);

  if (!b) return <p>Boss-ul se pregătește.</p>;
  if (incercari === null) { citesteSetare<number>(`boss-${id}`, 0).then(setIncercari); return null; }

  const scor = rez.length ? rez.filter((r) => r.corect).length / rez.length : 0;

  if (!start && eBusola) {
    return (
      <div className="card stiva">
        <div className="rand"><Geo stare="bucuros" /><h1 style={{ margin: 0 }}>Busola de start</h1></div>
        <p>{itemi.length} întrebări din ce ai învățat anul trecut. Nu primești notă și nu poți pierde nimic.</p>
        <p>După răspunsurile tale, Geo alege cât de grele să fie exercițiile la început. Apoi se potrivesc singure, pe parcurs.</p>
        <div className="rand">
          <button className="buton secundar" onClick={() => mergi({ e: 'harta' })}>Mai târziu</button>
          <button className="buton" onClick={() => setStart(true)}>Pornește busola</button>
        </div>
      </div>
    );
  }

  if (!start) {
    return (
      <div className="card stiva">
        <div className="rand"><Geo stare="gandeste" /><h1 style={{ margin: 0 }}>{b.titlu}</h1></div>
        <p>{itemi.length} întrebări din {eFinal ? 'tot anul' : 'toată unitatea'}. Afli rezultatele la final, cu explicații pentru fiecare greșeală.</p>
        <p>{eFinal ? `La cel puțin jumătate de răspunsuri corecte câștigi ${XP.mareExpeditie} XP și insigna de explorator al anului.` : `La cel puțin jumătate de răspunsuri corecte câștigi ${XP.boss} XP și cartonașul unității. Regiunea următoare se deschide oricum după calendar.`}</p>
        {incercari >= 2 && <p className="feedback nu">Ai folosit cele două încercări. Exersează nivelurile unității; profesorul îți poate da o încercare nouă.</p>}
        <div className="rand">
          <button className="buton secundar" onClick={() => mergi({ e: 'harta' })}>Mai târziu</button>
          <button className="buton" disabled={incercari >= 2} onClick={async () => { await scrieSetare(`boss-${id}`, incercari + 1); setStart(true); }}>
            {incercari === 1 ? 'Încearcă din nou' : 'Începe'}
          </button>
        </div>
      </div>
    );
  }

  if (final && eBusola) {
    const d = dificultateDinBusola(scor);
    return (
      <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
        <Geo marime={88} stare="bucuros" />
        <h1>Busola e reglată</h1>
        <p>Ai răspuns corect la {rez.filter((r) => r.corect).length} din {rez.length} întrebări.</p>
        <p>{d === 3 ? 'Pornești cu exerciții mai provocatoare.' : d === 2 ? 'Pornești cu exerciții de nivel mediu.' : 'Pornești cu exerciții ușoare, ca să prinzi curaj. Vor crește odată cu tine.'}</p>
        <button className="buton" onClick={() => mergi({ e: 'harta' })}>La hartă</button>
      </div>
    );
  }

  if (final) {
    return (
      <div className="stiva">
        <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
          <Geo marime={88} stare={scor >= 0.5 ? 'bucuros' : 'gandeste'} />
          <h1>{scor >= 0.5 ? (eFinal ? 'Marea Expediție e completă!' : 'Boss învins!') : 'Mai e puțin'}</h1>
          <p>{rez.filter((r) => r.corect).length} răspunsuri corecte din {rez.length} ({Math.round(scor * 100)} %).</p>
          {scor >= 0.5 ? <p>+{eFinal ? XP.mareExpeditie : XP.boss} XP. {eFinal ? 'Insigna de explorator al anului e a ta.' : 'Cartonașul unității e în colecția ta.'}</p> : <p>Greșelile au intrat în misiunile zilnice. Le repeți, apoi încerci din nou.</p>}
        </div>
        <div className="card">
          <h2>Ce ai greșit</h2>
          {itemi.every((_, i) => rez[i]?.corect) && <p>Nimic. Bravo!</p>}
          <ul className="stiva" style={{ paddingLeft: 18 }}>
            {itemi.map((it, i) => !rez[i]?.corect && (
              <li key={it.id}><b>{it.enunt}</b><br />{it.feedback.gresit}</li>
            ))}
          </ul>
        </div>
        <button className="buton" onClick={() => mergi({ e: 'harta' })}>Înapoi la hartă</button>
      </div>
    );
  }

  return (
    <div className="card">
      <p className="eticheta-mica">{b.titlu} · {k + 1} din {itemi.length}</p>
      <Exercitiu key={itemi[k].id} item={itemi[k]} feedbackImediat={eBusola} onGata={async (r) => {
        await inregistreazaRaspuns(cal, profil!.clasa, itemi[k], r, azi);
        const toate = [...rez, r];
        setRez(toate);
        if (k + 1 < itemi.length) { setK(k + 1); return; }
        const s = toate.filter((x) => x.corect).length / toate.length;
        if (eBusola) {
          await db.profil.update('eu', { dificultate: dificultateDinBusola(s) });
          await terminaNivel(id, s, 0, azi, XP.nivelTerminat);
        } else if (s >= 0.5) await terminaNivel(id, s, 0, azi, eFinal ? XP.mareExpeditie : XP.boss);
        setFinal(true);
      }} />
    </div>
  );
}
