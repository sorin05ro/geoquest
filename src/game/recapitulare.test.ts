import { describe, expect, it } from 'vitest';
import { alegeRecapitulare, modENDisponibil, notaOrientativa, stapanire, stareItemi } from './recapitulare';
import type { Item, Raspuns } from '../types';

const item = (id: string, nivel: string): Item => ({
  id, nivel, competente: [], tip: 'alegere', dificultate: 1, enunt: id,
  date: { variante: ['a', 'b'], corect: 0 }, feedback: { corect: 'da', gresit: 'nu' },
} as Item);
const r = (itemId: string, corect: boolean, data: string, id = 0): Raspuns => ({ id, item: itemId, nivel: 'n', corect, indiciu: false, durataMs: 1000, data } as Raspuns);
const fara = <T,>(a: T[]) => a;

describe('modul Evaluare Națională', () => {
  it('apare doar la clasa a VIII-a, de la săptămâna stabilită', () => {
    const cfg = { activ: true, deLaSaptamana: 28 };
    expect(modENDisponibil(7, cfg, 30)).toBe(false);
    expect(modENDisponibil(8, cfg, 27)).toBe(false);
    expect(modENDisponibil(8, cfg, 28)).toBe(true);
    expect(modENDisponibil(8, cfg, 10, null, true)).toBe(true);
  });
  it('profesorul îl poate opri sau porni pe dispozitiv', () => {
    expect(modENDisponibil(8, { activ: true, deLaSaptamana: 28 }, 30, false)).toBe(false);
    expect(modENDisponibil(8, { activ: false, deLaSaptamana: 28 }, 30, true)).toBe(true);
  });
  it('ultimul răspuns decide starea itemului', () => {
    const s = stareItemi([r('a', false, '2027-03-01', 1), r('a', true, '2027-03-02', 2), r('b', true, '2027-03-01', 3), r('b', false, '2027-03-05', 4)]);
    expect(s.get('a')).toEqual({ incercari: 2, ultimulCorect: true });
    expect(s.get('b')?.ultimulCorect).toBe(false);
  });
  it('stăpânirea numără doar itemii știuți ultima dată', () => {
    const itemi = [item('a', 'n1'), item('b', 'n1'), item('c', 'n2'), item('d', 'n2')];
    const s = stareItemi([r('a', true, '2027-03-01'), r('b', false, '2027-03-01')]);
    expect(stapanire(itemi, s)).toBe(0.25);
  });
  it('recapitularea începe cu greșelile, apoi cu itemii noi, din niveluri diferite', () => {
    const itemi = [item('a', 'n1'), item('b', 'n1'), item('c', 'n2'), item('d', 'n3')];
    const s = stareItemi([r('a', true, '2027-03-01'), r('b', false, '2027-03-01')]);
    const ales = alegeRecapitulare(itemi, s, 3, fara);
    expect(ales.map((i) => i.id)).toEqual(['b', 'c', 'd']);
  });
  it('nota orientativă are un punct din oficiu', () => {
    expect(notaOrientativa(0, 20)).toBe(1);
    expect(notaOrientativa(20, 20)).toBe(10);
    expect(notaOrientativa(10, 20)).toBe(5.5);
  });
});
