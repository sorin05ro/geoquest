import { useLiveQuery } from 'dexie-react-hooks';
import { useEffect, useState } from 'react';
import { useApp } from '../state';
import { db, citesteSetare, scrieSetare, stergeTot } from '../db/db';
import { RANGURI, rang } from '../game/rules';
import { insigneCastigate, serie } from '../game/progres';
import { Geo } from '../ui/Geo';
import { LUMI } from './Harta';

export function aplicaSetariAfisare(s: { tema?: string; concentrare?: boolean; tabla?: boolean }) {
  const r = document.documentElement;
  if (s.tema && s.tema !== 'auto') r.dataset.tema = s.tema; else delete r.dataset.tema;
  r.dataset.concentrare = s.concentrare ? '1' : '0';
  if (s.tabla) r.dataset.mod = 'tabla'; else delete r.dataset.mod;
}

export function Profil() {
  const { profil, xp, insigne, cal, azi, mergi } = useApp();
  const nivele = useLiveQuery(() => db.nivele.toArray(), [], []);
  const [castigate, setCastigate] = useState<Set<string>>(new Set());
  const [s, setS] = useState({ serie: 0, protectii: 0 });
  const [afisare, setAfisare] = useState<{ tema?: string; concentrare?: boolean; tabla?: boolean }>({});
  const r = rang(xp);

  useEffect(() => {
    insigneCastigate(insigne).then((l) => setCastigate(new Set(l.map((i) => i.id))));
    serie(cal, profil!.clasa, azi).then(setS);
    citesteSetare('afisare', {}).then(setAfisare);
  }, [nivele.length]); // eslint-disable-line react-hooks/exhaustive-deps

  const schimba = async (x: typeof afisare) => {
    const n = { ...afisare, ...x };
    setAfisare(n); aplicaSetariAfisare(n); await scrieSetare('afisare', n);
  };
  const ale = insigne.filter((i) => i.clasa === profil!.clasa);
  const totalStele = nivele.reduce((a, n) => a + n.stele, 0);

  return (
    <div className="stiva">
      <div className="card rand">
        <span style={{ fontSize: 54 }} aria-hidden="true">{profil!.avatar}</span>
        <div style={{ flex: 1, minWidth: 180 }}>
          <h1 style={{ margin: 0 }}>{profil!.porecla}</h1>
          <p className="eticheta-mica" style={{ margin: 0 }}>{LUMI[profil!.clasa]}</p>
        </div>
        <Geo stare="bucuros" />
      </div>

      <div className="card stiva">
        <h2>Rang: {r.nume}</h2>
        <div className="bara-progres" role="progressbar" aria-valuenow={Math.round(r.progres * 100)} aria-valuemin={0} aria-valuemax={100}>
          <i style={{ width: `${r.progres * 100}%` }} />
        </div>
        <p className="eticheta-mica">{xp} XP{r.urmator ? ` · încă ${r.urmator.prag - xp} XP până la ${r.urmator.nume}` : ' · rangul cel mai înalt'}</p>
        <ol className="rand" style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '.85em' }}>
          {RANGURI.map((x, i) => <li key={x.nume} style={{ opacity: i <= r.index ? 1 : 0.45 }}>{i <= r.index ? '●' : '○'} {x.nume}</li>)}
        </ol>
      </div>

      <div className="rand">
        <div className="card" style={{ flex: 1 }}><b style={{ fontSize: '1.6em' }}>{s.serie}</b><br /><span className="eticheta-mica">zile de școală la rând{s.protectii ? ` · ${s.protectii} zile de protecție` : ''}</span></div>
        <div className="card" style={{ flex: 1 }}><b style={{ fontSize: '1.6em' }}>{totalStele}</b><br /><span className="eticheta-mica">stele câștigate</span></div>
        <div className="card" style={{ flex: 1 }}><b style={{ fontSize: '1.6em' }}>{nivele.length}</b><br /><span className="eticheta-mica">niveluri parcurse</span></div>
      </div>

      <div className="card stiva">
        <h2>Insigne</h2>
        <p className="eticheta-mica">Fiecare insignă arată o competență din programă pe care ai demonstrat-o.</p>
        {ale.map((i) => (
          <div key={i.id} className={`insigna ${castigate.has(i.id) ? '' : 'blocata'}`}>
            <span className="icon" aria-hidden="true">{i.icon}</span>
            <div><b>{i.nume}</b> <span className="eticheta-mica">· competența {i.competenta}</span><br /><span className="eticheta-mica">{i.descriere}</span></div>
          </div>
        ))}
      </div>

      <div className="card stiva">
        <h2>Afișare</h2>
        <label className="camp"><span>Tema</span>
          <select value={afisare.tema ?? 'auto'} onChange={(e) => schimba({ tema: e.target.value })}>
            <option value="auto">Ca dispozitivul</option><option value="luminoasa">Luminoasă</option><option value="intunecata">Întunecată</option>
          </select>
        </label>
        <label className="bifa"><input type="checkbox" checked={!!afisare.concentrare} onChange={(e) => schimba({ concentrare: e.target.checked })} /> Mod concentrare (fără animații)</label>
        <label className="bifa"><input type="checkbox" checked={!!afisare.tabla} onChange={(e) => schimba({ tabla: e.target.checked })} /> Text și butoane mari (tablă interactivă)</label>
      </div>

      <div className="card stiva">
        <h2>Datele tale</h2>
        <p className="eticheta-mica">Progresul tău stă doar pe acest dispozitiv. Nu trimitem nimic pe internet.</p>
        <button className="buton secundar" onClick={() => { if (confirm('Ștergi tot progresul de pe acest dispozitiv? Nu se poate anula.')) stergeTot(); }}>Șterge progresul de pe acest dispozitiv</button>
      </div>
      <div className="card stiva">
        <h2>Clasa ta</h2>
        <p className="eticheta-mica">{profil!.codClasa ? `Codul clasei: ${profil!.codClasa}.` : 'Încă nu ai codul clasei. Îl primești de la profesor (pe tablă).'} Când profesorul deschide colectarea, trimiți de aici progresul tău, doar cu porecla.</p>
        <button className="buton" onClick={() => mergi({ e: 'trimite-raport' })}>Trimite rezultatele profesorului</button>
      </div>
      <button className="buton secundar" onClick={() => mergi({ e: 'profesor' })}>Sunt profesor</button>
    </div>
  );
}
