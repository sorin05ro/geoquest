import { describe, expect, it } from 'vitest';
import { lacunarDinParanteze, valideazaItem } from './valideaza';
import type { Item } from '../types';

const baza = { id: 'P1', nivel: 'n', competente: ['V-1.1'], dificultate: 1 as const, enunt: 'Completează.', feedback: { corect: 'Bravo', gresit: 'Răspunsul e est.' } };
const valide = new Set(['V-1.1']);

describe('editorul de conținut', () => {
  it('transformă parantezele drepte în spații de completat', () => {
    expect(lacunarDinParanteze('Soarele răsare la [est] și apune la [ vest ].')).toEqual({ text: 'Soarele răsare la {0} și apune la {1}.', raspunsuri: ['est', 'vest'] });
  });
  it('acceptă un item corect', () => {
    const it: Item = { ...baza, tip: 'lacunar', date: { text: 'Răsare la {0}.', raspunsuri: ['est'], distractori: ['vest'] } };
    expect(valideazaItem(it, valide)).toEqual([]);
  });
  it('semnalează sedilele, competențele inexistente și variantele lipsă', () => {
    const it: Item = { ...baza, competente: ['V-9.9'], enunt: 'Pe ce ţară?', tip: 'alegere', date: { variante: ['a', ''], corect: 0 } };
    const e = valideazaItem(it, valide);
    expect(e.some((x) => x.includes('sedilă'))).toBe(true);
    expect(e.some((x) => x.includes('V-9.9'))).toBe(true);
    expect(e.some((x) => x.includes('variantele'))).toBe(true);
  });
});
