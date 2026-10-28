import { describe, expect, it } from 'vitest';
import { celeMaiGresite, citesteCodClasa, codClasaNou, codeazaTema, construiesteSumar, csvPanou, decodeazaTema, randuriPanou } from './sumar';
import type { Raport, Raspuns, Tema } from '../types';

const r = (item: string, corect: boolean, data = '2026-11-16'): Raspuns => ({ item, nivel: 'n', corect, indiciu: false, durataMs: 1000, data });

describe('rezumatul elevului', () => {
  it('numără corectele pe competențe, greșelile și temele', () => {
    const comp = new Map([['a', ['V-1.1']], ['b', ['V-1.1', 'V-2.1']]]);
    const tema: Tema = { id: 't1', titlu: 'Tema', clasa: 5, niveluri: ['N1', 'N2'], termen: '2026-11-20', creat: '2026-11-16' };
    const s = construiesteSumar([r('a', true), r('b', false), r('b', true, '2026-11-17')], [{ nivel: 'N1', stele: 2, scor: 0.85, indicii: 0, terminat: '2026-11-17' }], comp, [tema], 120);
    expect(s.competente['V-1.1']).toEqual({ c: 2, t: 3 });
    expect(s.competente['V-2.1']).toEqual({ c: 1, t: 2 });
    expect(s.greseli).toEqual({ b: 1 });
    expect(s.teme).toEqual({ t1: 1 });
    expect(s.ultimaActivitate).toBe('2026-11-17');
  });
});

describe('coduri de clasă și teme', () => {
  it('codul de clasă se generează și se citește', () => {
    const c = codClasaNou(5, 'A', () => 0.5);
    expect(c).toMatch(/^5A-[A-Z2-9]{4}$/);
    expect(citesteCodClasa(c)).toEqual({ clasa: 5, litera: 'A' });
    expect(citesteCodClasa('7-ABCD')).toEqual({ clasa: 7, litera: '' });
    expect(citesteCodClasa('9A-ABCD')).toBeNull();
    expect(citesteCodClasa('5A-AB0D')).toBeNull();
  });
  it('tema trece prin link fără să se piardă nimic, inclusiv diacriticele', () => {
    const t: Tema = { id: 'x1', titlu: 'Recapitulare: Câmpia Română și Delta', clasa: 8, cod: '8A-K7QM', niveluri: ['VIII-S10-campia-romana'], termen: '2026-11-27', creat: '2026-11-20' };
    expect(decodeazaTema(codeazaTema(t))).toEqual(t);
    expect(decodeazaTema('nu-e-tema')).toBeNull();
  });
});

describe('panoul profesorului', () => {
  const rap = (porecla: string, primit: string, c: number, t: number, greseli: Record<string, number> = {}): Raport => ({
    cod: '5A-K7QM', porecla, avatar: '🦉', clasa: 5, primit,
    sumar: { xp: 100, niveluri: { N1: { stele: 3, scor: 1 }, 'V-T2': { stele: 2, scor: 0.8 } }, competente: { 'V-1.1': { c, t } }, greseli, teme: {}, ultimaActivitate: primit, raspunsuri: t },
  });
  it('păstrează ultimul raport al fiecărui elev și calculează procentele', () => {
    const rows = randuriPanou([rap('Busola', '2026-11-16', 1, 4), rap('Busola', '2026-11-20', 3, 4), rap('Arcaș', '2026-11-20', 0, 0)], ['V-1.1', 'V-2.1']);
    expect(rows.map((x) => x.porecla)).toEqual(['Arcaș', 'Busola']);
    expect(rows[1].procente).toEqual({ 'V-1.1': 75, 'V-2.1': null });
    expect(rows[0].procente['V-1.1']).toBeNull();
  });
  it('itemii greșiți de cei mai mulți elevi apar primii', () => {
    const top = celeMaiGresite([rap('A', 'd', 0, 1, { x: 1, y: 3 }), rap('B', 'd', 0, 1, { x: 2 })]);
    expect(top[0]).toEqual({ item: 'x', elevi: 2, greseli: 3 });
  });
  it('CSV-ul are BOM, separator „;” și coloanele de test', () => {
    const rows = randuriPanou([rap('Valul; Albastru', '2026-11-20', 1, 2)], ['V-1.1']);
    const csv = csvPanou(rows, ['V-1.1'], ['V-T2'], [rap('Valul; Albastru', '2026-11-20', 1, 2)]);
    expect(csv.startsWith('﻿Poreclă;')).toBe(true);
    expect(csv).toContain('"Valul; Albastru";5A-K7QM;2026-11-20;100;2;5;50;80');
  });
});
