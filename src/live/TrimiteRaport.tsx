import { useEffect, useRef, useState } from 'react';
import { useApp } from '../state';
import { db, totalXP } from '../db/db';
import { Geo } from '../ui/Geo';
import { construiesteSumar, citesteCodClasa } from '../profesor/sumar';
import { deschideCanal, type Canal } from './canal';

/** Elevul trimite profesorului rezumatul progresului (doar porecla, codul clasei și rezultatele). */
export function TrimiteRaport({ pinInitial }: { pinInitial?: string }) {
  const { profil, continut, mergi } = useApp();
  const [pin, setPin] = useState(pinInitial ?? '');
  const [cod, setCod] = useState(profil?.codClasa ?? '');
  const [stare, setStare] = useState<'gata' | 'trimit' | 'trimis' | 'eroare'>('gata');
  const [mesaj, setMesaj] = useState('');
  const canal = useRef<Canal | null>(null);
  useEffect(() => () => canal.current?.inchide(), []);

  if (!profil) {
    return (
      <div className="card stiva">
        <Geo stare="gandeste" />
        <p>Ca să trimiți rezultatele, intră mai întâi în aplicație: alege clasa și porecla.</p>
        <button className="buton" onClick={() => { location.hash = ''; mergi({ e: 'intrare' }); }}>Intră în aplicație</button>
      </div>
    );
  }

  const codValid = citesteCodClasa(cod);
  const trimite = async () => {
    setStare('trimit'); setMesaj('');
    try {
      if (codValid && cod.toUpperCase() !== profil.codClasa) await db.profil.update('eu', { codClasa: cod.toUpperCase() });
      const [raspunsuri, nivele, teme, xp] = await Promise.all([db.raspunsuri.toArray(), db.nivele.toArray(), db.teme.toArray(), totalXP()]);
      const competenteItem = new Map([...(continut?.itemi.values() ?? [])].map((i) => [i.id, i.competente]));
      const sumar = construiesteSumar(raspunsuri, nivele, competenteItem, teme, xp);
      const c = await deschideCanal(pin);
      canal.current = c;
      const id = crypto.randomUUID();
      const confirmat = new Promise<void>((ok) => c.asculta((m) => { if (m.t === 'primit' && m.id === id) ok(); }));
      const r = { cod: cod.toUpperCase(), porecla: profil.porecla, avatar: profil.avatar, clasa: profil.clasa, sumar };
      let incercari = 0;
      const t = setInterval(() => { if (++incercari > 10) clearInterval(t); else c.trimite({ t: 'raport', id, r }); }, 1500);
      c.trimite({ t: 'raport', id, r });
      await Promise.race([confirmat, new Promise((_, nu) => setTimeout(() => nu(new Error('Calculatorul profesorului nu a răspuns. Verifică PIN-ul și încearcă din nou.')), 16000))]);
      clearInterval(t);
      setStare('trimis');
    } catch (e) {
      setStare('eroare');
      setMesaj(e instanceof Error ? e.message : String(e));
    }
  };

  if (stare === 'trimis') {
    return (
      <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
        <Geo marime={88} stare="bucuros" />
        <h1>Rezultatele au ajuns la profesor</h1>
        <p>Profesorul vede doar porecla ta și ce ai exersat. Progresul rămâne și pe telefonul tău.</p>
        <button className="buton" onClick={() => { location.hash = ''; mergi({ e: 'harta' }); }}>Înapoi la hartă</button>
      </div>
    );
  }
  return (
    <div className="bun-venit">
      <div className="rand" style={{ flexWrap: 'nowrap' }}><Geo marime={72} /><h1 style={{ margin: 0 }}>Trimite rezultatele profesorului</h1></div>
      <p>Se trimit: porecla „{profil.porecla}”, nivelurile terminate, stelele și cât de bine stai pe fiecare competență. Numele tău nu apare nicăieri.</p>
      <label className="camp"><span>Codul clasei (de pe tablă, ex. 5A-K7QM)</span>
        <input value={cod} onChange={(e) => setCod(e.target.value.toUpperCase())} maxLength={8} autoComplete="off" />
      </label>
      <label className="camp"><span>PIN-ul colectării (de pe tablă)</span>
        <input inputMode="numeric" value={pin} onChange={(e) => setPin(e.target.value.replace(/\D/g, ''))} maxLength={6} autoComplete="off" />
      </label>
      {cod && !codValid && <p className="feedback nu">Codul clasei arată ca 5A-K7QM: cifra clasei, litera, o liniuță și 4 caractere.</p>}
      {codValid && codValid.clasa !== profil.clasa && <p className="feedback nu">Codul e pentru clasa a {codValid.clasa}-a, dar tu ești înscris la a {profil.clasa}-a. Verifică pe tablă.</p>}
      {mesaj && <p className="feedback nu" role="alert">{mesaj}</p>}
      <div className="rand">
        <button className="buton secundar" onClick={() => { location.hash = ''; mergi({ e: 'harta' }); }}>Renunță</button>
        <button className="buton" style={{ flex: 1 }} disabled={!codValid || codValid.clasa !== profil.clasa || pin.length !== 6 || stare === 'trimit'} onClick={trimite}>
          {stare === 'trimit' ? 'Se trimite…' : 'Trimite'}
        </button>
      </div>
    </div>
  );
}
