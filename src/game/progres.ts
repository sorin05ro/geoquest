import { db, adaugaXP } from '../db/db';
import type { Calendar, Clasa, Item } from '../types';
import { adunaZileScoala, esteZiDeScoala, saptamaniClasa } from '../calendar/calendar';
import { INTERVALE_LEITNER, XP, ajusteazaDificultate, calculeazaSerie, insignaCastigata, stele, urmatoareaCutie, xpRaspuns, type Insigna } from './rules';
import type { Rezultat } from '../engine/Exercitiu';

/** Salvează un răspuns, acordă XP și actualizează repetarea spațiată. Întoarce XP-ul câștigat. */
export async function inregistreazaRaspuns(cal: Calendar, clasa: Clasa, item: Item, r: Rezultat, azi: string): Promise<number> {
  const cutie = await db.leitner.get(item.id);
  await db.raspunsuri.add({
    item: item.id, nivel: item.nivel, corect: r.corect, partial: r.scor, indiciu: r.indiciu, durataMs: r.durataMs, data: azi,
  });
  let xp = 0;
  if (r.corect) xp = xpRaspuns(item.dificultate, r.indiciu, !!cutie);
  else if (r.scor >= 0.5) xp = Math.floor(XP.corect[item.dificultate] / 2);
  await adaugaXP(xp, `item ${item.id}`, azi);

  // Leitner: greșelile intră în cutia 1; corect la repetare urcă o cutie
  if (!r.corect || cutie) {
    const urm = urmatoareaCutie(cutie?.cutie ?? 1, r.corect && !!cutie);
    if (urm === 'iese') await db.leitner.delete(item.id);
    else await db.leitner.put({ item: item.id, cutie: urm, urmatoarea: adunaZileScoala(cal, clasa, azi, INTERVALE_LEITNER[urm]) });
  }

  // dificultate adaptivă
  const p = await db.profil.get('eu');
  if (p) {
    const ultime = (await db.raspunsuri.orderBy('id').reverse().limit(3).toArray()).reverse().map((x) => x.corect);
    const d = ajusteazaDificultate(p.dificultate, ultime);
    if (d !== p.dificultate) await db.profil.update('eu', { dificultate: d });
  }
  return xp;
}

export async function terminaNivel(nivel: string, scor: number, indicii: number, azi: string, bonus: number = XP.nivelTerminat) {
  const s = stele(scor, indicii);
  const vechi = await db.nivele.get(nivel);
  if (!vechi) await adaugaXP(bonus, `nivel ${nivel}`, azi);
  if (!vechi || s > vechi.stele || scor > vechi.scor) {
    await db.nivele.put({ nivel, stele: Math.max(s, vechi?.stele ?? 0) as 1 | 2 | 3, scor: Math.max(scor, vechi?.scor ?? 0), indicii, terminat: azi });
  }
  return { stele: s, primaData: !vechi };
}

export async function itemiDeRepetat(azi: string): Promise<string[]> {
  return (await db.leitner.where('urmatoarea').belowOrEqual(azi).toArray()).map((c) => c.item);
}

export async function serie(cal: Calendar, clasa: Clasa, azi: string) {
  const active = new Set((await db.raspunsuri.toArray()).map((r) => r.data));
  const zile: string[] = [];
  for (const s of saptamaniClasa(cal, clasa)) {
    if (s.de > azi) break;
    const d0 = new Date(s.de + 'T12:00:00');
    for (let i = 0; i < 7; i++) {
      const z = new Date(d0.getTime() + i * 86400000).toISOString().slice(0, 10);
      if (z > s.pana) break;
      if (esteZiDeScoala(cal, clasa, z)) zile.push(z);
    }
  }
  return calculeazaSerie(zile, active, azi);
}

export async function insigneCastigate(insigne: Insigna[]) {
  const niv = new Map((await db.nivele.toArray()).map((n) => [n.nivel, n]));
  return insigne.filter((i) => insignaCastigata(
    i,
    (id) => niv.get(id)?.stele ?? 0,
    (id) => niv.has(id),
    (id) => niv.get(id)?.scor ?? 0,
  ));
}
