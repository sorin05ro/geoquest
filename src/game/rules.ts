// Regulile de joc. Valorile vin din planul aprobat (Etapa 0) și se calibrează în Etapa 5.

export const XP = {
  corect: { 1: 5, 2: 10, 3: 15 } as Record<1 | 2 | 3, number>,
  corectareGreseala: 10, // item greșit anterior, rezolvat corect la repetare
  nivelTerminat: 20,
  misiuneaZilei: 15,
  expeditie: 50,
  boss: 100, // scor de cel puțin 50 %
  mareExpeditie: 200,
} as const;

export function xpRaspuns(dificultate: 1 | 2 | 3, cuIndiciu: boolean, eraGresit: boolean): number {
  const baza = XP.corect[dificultate];
  return (cuIndiciu ? Math.floor(baza / 2) : baza) + (eraGresit ? XP.corectareGreseala : 0);
}

export const RANGURI = [
  { nume: 'Cercetaș', prag: 0, premiu: 'Busola de bază și avatarul inițial' },
  { nume: 'Cartograf', prag: 500, premiu: 'Rama de profil „hartă”' },
  { nume: 'Explorator', prag: 1500, premiu: 'Ștampile noi pe pașaport' },
  { nume: 'Navigator', prag: 3000, premiu: 'Teme de culoare pentru hartă' },
  { nume: 'Geograf', prag: 5000, premiu: 'Titlul afișat în modul clasă' },
  { nume: 'Mare Geograf', prag: 8000, premiu: 'Cartonaș de colecție special cu Geo' },
] as const;

export function rang(xp: number) {
  let i = 0;
  for (let k = 0; k < RANGURI.length; k++) if (xp >= RANGURI[k].prag) i = k;
  const urm = RANGURI[i + 1];
  const progres = urm ? (xp - RANGURI[i].prag) / (urm.prag - RANGURI[i].prag) : 1;
  return { index: i, ...RANGURI[i], urmator: urm ?? null, progres };
}

/** 1 stea = nivel parcurs; 2 = cel puțin 80 % corect; 3 = cel puțin 95 % corect, fără indicii. */
export function stele(scor: number, indicii: number): 1 | 2 | 3 {
  if (scor >= 0.95 && indicii === 0) return 3;
  if (scor >= 0.8) return 2;
  return 1;
}

/** Dificultate adaptivă: +1 după 3 corecte la rând, −1 după 2 greșite la rând. */
export function ajusteazaDificultate(curenta: 1 | 2 | 3, ultimele: boolean[]): 1 | 2 | 3 {
  const n = ultimele.length;
  if (n >= 3 && ultimele.slice(-3).every(Boolean)) return Math.min(3, curenta + 1) as 1 | 2 | 3;
  if (n >= 2 && ultimele.slice(-2).every((x) => !x)) return Math.max(1, curenta - 1) as 1 | 2 | 3;
  return curenta;
}

/** Cutiile Leitner: revenire după 1, 3, 7, 14 zile de școală. */
export const INTERVALE_LEITNER = { 1: 1, 2: 3, 3: 7, 4: 14 } as const;

export function urmatoareaCutie(cutie: 1 | 2 | 3 | 4, corect: boolean): 1 | 2 | 3 | 4 | 'iese' {
  if (!corect) return 1;
  if (cutie === 4) return 'iese';
  return (cutie + 1) as 2 | 3 | 4;
}

/**
 * Seria zilnică blândă: contează doar zilele de școală. `zileActive` = zile de școală (ISO) cu activitate,
 * `zileScoala` = toate zilele de școală până azi, în ordine. Zilele de protecție (una la 5 zile active, max. 2)
 * acoperă golurile.
 */
export function calculeazaSerie(zileScoala: string[], zileActive: Set<string>, azi: string) {
  let serie = 0;
  let protectii = 0;
  let folosite = 0;
  let activeLaRand = 0;
  for (const zi of zileScoala) {
    if (zi > azi) break;
    if (zileActive.has(zi)) {
      serie++;
      activeLaRand++;
      if (activeLaRand % 5 === 0 && protectii < 2) protectii++;
    } else if (zi === azi) {
      // azi încă nu s-a terminat: seria nu se rupe
    } else if (protectii > 0) {
      protectii--;
      folosite++;
    } else {
      serie = 0;
      activeLaRand = 0;
    }
  }
  return { serie, protectii, folosite };
}

export interface ConditieInsigna {
  niveluri?: string[];
  steleMinime?: 1 | 2 | 3;
  expeditii?: string[];
  boss?: string;
  scorBoss?: number;
}

export interface Insigna {
  id: string;
  nume: string;
  clasa: number;
  competenta: string;
  descriere: string;
  icon: string;
  conditie: ConditieInsigna;
}

export function insignaCastigata(
  ins: Insigna,
  steleNivel: (id: string) => number,
  expeditieTerminata: (id: string) => boolean,
  scorBoss: (id: string) => number,
): boolean {
  const c = ins.conditie;
  if (c.niveluri && !c.niveluri.every((n) => steleNivel(n) >= (c.steleMinime ?? 1))) return false;
  if (c.expeditii && !c.expeditii.every(expeditieTerminata)) return false;
  if (c.boss && scorBoss(c.boss) < (c.scorBoss ?? 0.5)) return false;
  return true;
}
