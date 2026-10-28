import { describe, expect, it } from 'vitest';
import { alegeEchipa, publica, puncte, scorPin, scoruriEchipe, type Jucator } from './protocol';
import type { Item } from '../types';

const inversat = <T,>(a: T[]) => [...a].reverse();

describe('jocul live', () => {
  it('itemul public nu conține răspunsul, iar gazda păstrează indexul corect după amestecare', () => {
    const it: Item = {
      id: 'x', nivel: 'n', competente: [], tip: 'alegere', dificultate: 1, enunt: '?',
      date: { variante: ['bun', 'a', 'b', 'c'], corect: 0 }, feedback: { corect: '', gresit: '' },
    };
    const { pub, corect } = publica(it, inversat);
    expect(pub.variante).toEqual(['c', 'b', 'a', 'bun']);
    expect(corect).toBe(3);
    expect(JSON.stringify(pub)).not.toContain('"corect"');
  });
  it('punctaj: 500 + viteză; greșit = 0; pin aproape = jumătate', () => {
    expect(puncte(1, 30000, 30000)).toBe(1000);
    expect(puncte(1, 0, 30000)).toBe(500);
    expect(puncte(0, 30000, 30000)).toBe(0);
    expect(puncte(0.5, 15000, 30000)).toBe(375);
    expect(scorPin({ lat: 45.38, lon: 27.06 }, { lat: 45.38, lon: 27.06 }, 30)).toBe(1);
    expect(scorPin({ lat: 45.0, lon: 27.06 }, { lat: 45.38, lon: 27.06 }, 30)).toBe(0.5); // ~42 km
    expect(scorPin({ lat: 44.43, lon: 26.1 }, { lat: 45.38, lon: 27.06 }, 30)).toBe(0);
  });
  it('echipele se completează echilibrat, iar scorul echipei e media membrilor', () => {
    const j: Jucator[] = [];
    for (let i = 0; i < 5; i++) j.push({ id: String(i), porecla: '', avatar: '', echipa: alegeEchipa(j, 2), scor: 0 });
    expect(j.map((x) => x.echipa)).toEqual([0, 1, 0, 1, 0]);
    j[0].scor = 900; j[2].scor = 600; j[4].scor = 0; j[1].scor = 800;
    expect(scoruriEchipe(j, 2)).toEqual([500, 400]);
  });
});
