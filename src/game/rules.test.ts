import { describe, expect, it } from 'vitest';
import { ajusteazaDificultate, calculeazaSerie, rang, stele, urmatoareaCutie, xpRaspuns } from './rules';

describe('XP și ranguri', () => {
  it('XP pe dificultate, la jumătate cu indiciu, bonus pentru corectarea greșelii', () => {
    expect(xpRaspuns(1, false, false)).toBe(5);
    expect(xpRaspuns(3, false, false)).toBe(15);
    expect(xpRaspuns(2, true, false)).toBe(5);
    expect(xpRaspuns(2, false, true)).toBe(20);
  });
  it('rangurile au pragurile din plan', () => {
    expect(rang(0).nume).toBe('Cercetaș');
    expect(rang(499).nume).toBe('Cercetaș');
    expect(rang(500).nume).toBe('Cartograf');
    expect(rang(8000).nume).toBe('Mare Geograf');
    expect(rang(1000).progres).toBeCloseTo(0.5);
  });
});

describe('stele și dificultate', () => {
  it('1–3 stele', () => {
    expect(stele(0.5, 0)).toBe(1);
    expect(stele(0.8, 2)).toBe(2);
    expect(stele(0.96, 1)).toBe(2);
    expect(stele(1, 0)).toBe(3);
  });
  it('urcă după 3 corecte, coboară după 2 greșite', () => {
    expect(ajusteazaDificultate(1, [true, true, true])).toBe(2);
    expect(ajusteazaDificultate(3, [true, true, true])).toBe(3);
    expect(ajusteazaDificultate(2, [true, false, false])).toBe(1);
    expect(ajusteazaDificultate(2, [false, true])).toBe(2);
  });
  it('Leitner: greșit → cutia 1; corect în cutia 4 → iese', () => {
    expect(urmatoareaCutie(3, false)).toBe(1);
    expect(urmatoareaCutie(2, true)).toBe(3);
    expect(urmatoareaCutie(4, true)).toBe('iese');
  });
});

describe('seria zilnică blândă', () => {
  const zile = ['2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-09', '2026-11-10'];
  it('5 zile active dau o zi de protecție care acoperă un gol', () => {
    const active = new Set(['2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-10']);
    expect(calculeazaSerie(zile, active, '2026-11-10')).toMatchObject({ serie: 6, folosite: 1 });
  });
  it('fără protecție, golul rupe seria', () => {
    const active = new Set(['2026-11-02', '2026-11-04']);
    expect(calculeazaSerie(zile.slice(0, 3), active, '2026-11-04').serie).toBe(1);
  });
  it('ziua de azi, încă neterminată, nu rupe seria', () => {
    const active = new Set(['2026-11-02', '2026-11-03']);
    expect(calculeazaSerie(zile.slice(0, 3), active, '2026-11-04').serie).toBe(2);
  });
});
