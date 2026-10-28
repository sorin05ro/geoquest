import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import type { Calendar } from '../types';
import {
  adunaZileScoala, esteZiDeScoala, niveluriDeblocate, saptamanaDeblocata, saptamaniClasa, stareZi,
} from './calendar';

const cal: Calendar = JSON.parse(readFileSync('public/calendar/2026-2027.json', 'utf-8'));

describe('structura anului școlar 2026–2027', () => {
  it('are 36 de săptămâni, S1 = 7.09.2026, S36 = 14–18.06.2027', () => {
    expect(cal.saptamani).toHaveLength(36);
    expect(cal.saptamani[0].de).toBe('2026-09-07');
    expect(cal.saptamani[35]).toMatchObject({ nr: 36, de: '2027-06-14', pana: '2027-06-18' });
  });
  it('intervalele: S8 = 2.11, S16 = 11.01, S23 = 8.03, S30 = 5.05', () => {
    const de = (n: number) => cal.saptamani[n - 1].de;
    expect(de(8)).toBe('2026-11-02');
    expect(de(16)).toBe('2027-01-11');
    expect(de(23)).toBe('2027-03-08');
    expect(de(30)).toBe('2027-05-05');
  });
  it('clasa a VIII-a are 35 de săptămâni (termină pe 11.06.2027)', () => {
    expect(saptamaniClasa(cal, 8)).toHaveLength(35);
    expect(saptamaniClasa(cal, 5)).toHaveLength(36);
    expect(cal.planificare.filter((p) => p.clasa === 8 && p.saptamana === 36)).toHaveLength(0);
  });
  it('fiecare clasă are câte un rând pe săptămână', () => {
    for (const c of [5, 6, 7] as const) expect(cal.planificare.filter((p) => p.clasa === c)).toHaveLength(36);
  });
  it('testele sunt în săptămânile din planificare', () => {
    const t = (c: number, s: number) => cal.planificare.find((p) => p.clasa === c && p.saptamana === s)?.test;
    expect(t(5, 7)).toBe('T1');
    expect(t(5, 13)).toBe('T2');
    expect(t(8, 11)).toBe('T2');
    expect(t(8, 32)).toBe('T5');
    expect(t(8, 35)).toBe('Tf');
    expect(t(6, 36)).toBe('Tf');
  });
  it('competența inexistentă VIII-3.5 a fost eliminată', () => {
    expect(cal.planificare.some((p) => p.competente.includes('VIII-3.5'))).toBe(false);
  });
});

describe('săptămâna curentă și deblocarea', () => {
  it('în vacanța de toamnă (28.10.2026) e deblocat până la S7', () => {
    const s = stareZi(cal, 5, '2026-10-28');
    expect(s.tip).toBe('vacanta');
    expect(saptamanaDeblocata(cal, 5, '2026-10-28')).toBe(7);
  });
  it('luni 16.11.2026 = S10 (lansarea MVP)', () => {
    expect(saptamanaDeblocata(cal, 5, '2026-11-16')).toBe(10);
    const ids = niveluriDeblocate(cal, 5, '2026-11-16');
    expect(ids.has('V-S10-caracteristici-generale-importanta')).toBe(true);
    expect(ids.has('V-S11-structura-interna-terrei')).toBe(false);
  });
  it('sâmbătă 21.11.2026 rămâne S10, dar nu e zi de școală', () => {
    expect(stareZi(cal, 8, '2026-11-21').tip).toBe('weekend');
    expect(saptamanaDeblocata(cal, 8, '2026-11-21')).toBe(10);
    expect(esteZiDeScoala(cal, 8, '2026-11-21')).toBe(false);
  });
  it('1 decembrie e zi liberă legală în S12', () => {
    const s = stareZi(cal, 5, '2026-12-01');
    expect(s).toMatchObject({ tip: 'curs', ziLibera: 'Ziua Națională a României' });
    expect(esteZiDeScoala(cal, 5, '2026-12-01')).toBe(false);
  });
  it('Școala Altfel (17.12.2026) e eveniment, în S14', () => {
    expect(stareZi(cal, 7, '2026-12-17')).toMatchObject({ tip: 'eveniment', eveniment: 'scoala-altfel' });
  });
  it('Săptămâna verde (20.04.2027) e eveniment, în S29', () => {
    const s = stareZi(cal, 6, '2027-04-20');
    expect(s.tip).toBe('eveniment');
    expect(saptamanaDeblocata(cal, 6, '2027-04-20')).toBe(29);
  });
  it('14.06.2027: a V-a e în S36, a VIII-a a terminat', () => {
    expect(saptamanaDeblocata(cal, 5, '2027-06-14')).toBe(36);
    expect(stareZi(cal, 8, '2027-06-14').tip).toBe('final');
  });
  it('înainte de 7.09.2026 nu e nimic deblocat', () => {
    expect(saptamanaDeblocata(cal, 6, '2026-09-01')).toBe(0);
  });
  it('profesorul poate debloca un nivel din viitor și bloca unul curent', () => {
    const ids = niveluriDeblocate(cal, 5, '2026-11-16', {
      deblocate: ['V-S11-structura-interna-terrei'], blocate: ['V-S10-caracteristici-generale-importanta'],
    });
    expect(ids.has('V-S11-structura-interna-terrei')).toBe(true);
    expect(ids.has('V-S10-caracteristici-generale-importanta')).toBe(false);
  });
  it('repetarea spațiată sare peste vacanțe: vineri 18.12 + 1 zi de școală = 21.12', () => {
    expect(adunaZileScoala(cal, 5, '2026-12-18', 1)).toBe('2026-12-21');
    expect(adunaZileScoala(cal, 5, '2026-12-22', 1)).toBe('2027-01-11');
  });
});
