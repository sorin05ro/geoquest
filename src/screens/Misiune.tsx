import { useEffect, useState } from 'react';
import { useApp } from '../state';
import { amesteca } from '../content';
import { Exercitiu } from '../engine/Exercitiu';
import { inregistreazaRaspuns, itemiDeRepetat } from '../game/progres';
import { XP } from '../game/rules';
import { adaugaXP, citesteSetare, scrieSetare } from '../db/db';
import { esteZiDeScoala, saptamanaDeblocata } from '../calendar/calendar';
import { Geo } from '../ui/Geo';
import type { Item } from '../types';

/** Misiunea zilei: 5 itemi, întâi cei de repetat, apoi din lecțiile deschise ale săptămânii. */
export function Misiune() {
  const { continut, cal, profil, azi, deblocate, mergi } = useApp();
  const [itemi, setItemi] = useState<Item[] | null>(null);
  const [k, setK] = useState(0);
  const [corecte, setCorecte] = useState(0);
  const [bonus, setBonus] = useState<number | null>(null);

  useEffect(() => {
    if (!continut) return;
    (async () => {
      const repetat = (await itemiDeRepetat(azi)).map((id) => continut.itemi.get(id)).filter(Boolean) as Item[];
      const s = saptamanaDeblocata(cal, profil!.clasa, azi);
      const disponibili = [...continut.itemi.values()].filter((i) => deblocate.has(i.nivel));
      const recente = disponibili.filter((i) => (cal.niveluri.find((n) => n.id === i.nivel)?.saptamana ?? 0) >= s - 1);
      const lista = [...amesteca(repetat).slice(0, 3)];
      for (const i of amesteca(recente.length ? recente : disponibili)) if (lista.length < 5 && !lista.includes(i)) lista.push(i);
      setItemi(lista);
    })();
  }, [continut]); // eslint-disable-line react-hooks/exhaustive-deps

  if (!itemi) return null;
  if (!itemi.length) {
    return (
      <div className="card stiva">
        <Geo stare="gandeste" />
        <h1>Încă nu e nimic de exersat</h1>
        <p>Misiunile apar când se deschide prima lecție cu exerciții. Uită-te pe hartă ce urmează.</p>
        <button className="buton" onClick={() => mergi({ e: 'harta' })}>Înapoi la hartă</button>
      </div>
    );
  }
  if (k >= itemi.length) {
    return (
      <div className="card stiva" style={{ alignItems: 'center', textAlign: 'center' }}>
        <Geo marime={88} stare="bucuros" />
        <h1>Misiune îndeplinită</h1>
        <p>{corecte} din {itemi.length} corecte.{bonus ? ` Bonusul zilei: +${bonus} XP.` : ''}</p>
        <button className="buton" onClick={() => mergi({ e: 'harta' })} autoFocus>Înapoi la hartă</button>
      </div>
    );
  }
  return (
    <div className="stiva">
      <div className="rand">
        <button className="buton-icon" onClick={() => mergi({ e: 'harta' })} aria-label="Înapoi la hartă">✕</button>
        <b style={{ flex: 1 }}>Misiunea zilei · {k + 1} din {itemi.length}</b>
      </div>
      <div className="card">
        <Exercitiu key={itemi[k].id} item={itemi[k]} onGata={async (r) => {
          await inregistreazaRaspuns(cal, profil!.clasa, itemi[k], r, azi);
          if (r.corect) setCorecte((c) => c + 1);
          if (k + 1 === itemi.length) {
            const ultima = await citesteSetare<string | null>('misiune-zi', null);
            if (ultima !== azi && esteZiDeScoala(cal, profil!.clasa, azi)) {
              await adaugaXP(XP.misiuneaZilei, 'misiunea zilei', azi);
              await scrieSetare('misiune-zi', azi);
              setBonus(XP.misiuneaZilei);
            }
          }
          setK(k + 1);
        }} />
      </div>
    </div>
  );
}
