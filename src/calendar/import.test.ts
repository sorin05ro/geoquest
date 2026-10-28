import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { genereazaCalendar, slugAscii, tabeleDinCsv, tabeleDinDocx, type StructuraAn } from './import';
import type { Calendar } from '../types';

const cal: Calendar = JSON.parse(readFileSync('public/calendar/2026-2027.json', 'utf-8'));
const comp = JSON.parse(readFileSync('public/content/competente.json', 'utf-8'));
const corecturi = JSON.parse(readFileSync('public/config/corecturi.json', 'utf-8'));
const an: StructuraAn = { an: cal.an, intervale: cal.intervale, vacante: cal.vacante, zileLibere: cal.zileLibere, evenimente: cal.evenimente, ultimaZi: cal.ultimaZi };

describe('importul planificării în aplicație', () => {
  it('din .docx dă exact același calendar ca scriptul Python', () => {
    const tabele = tabeleDinDocx(new Uint8Array(readFileSync('tools/planificare.docx')));
    expect(tabele).toHaveLength(4);
    const nou = genereazaCalendar(tabele, an, comp, corecturi);
    expect(nou.saptamani).toEqual(cal.saptamani);
    expect(nou.niveluri).toEqual(cal.niveluri);
    expect(nou.planificare).toEqual(cal.planificare);
    expect(nou.observatii).toEqual(cal.observatii);
  });
  it('slug-ul ignoră diacriticele și cuvintele de legătură', () => {
    expect(slugAscii('Vulcanii și cutremurele')).toBe('vulcanii-cutremurele');
    expect(slugAscii('Terra – o planetă a Sistemului Solar')).toBe('terra-planeta-sistemului-solar');
  });
  it('acceptă și CSV, cu intervale de competențe și conținuturi despărțite cu |', () => {
    const csv = 'clasa;unitate;competente;continuturi;ore;saptamana;evaluare\n'
      + '5;Terra – o planetă în mișcare;1.1 – 2.2;Globul geografic și harta | Mișcările Pământului;2;5 – 6;T₁ (test secvențial)\n';
    const c = genereazaCalendar(tabeleDinCsv(csv), an, comp);
    const r6 = c.planificare.find((p) => p.clasa === 5 && p.saptamana === 6)!;
    expect(r6.competente).toEqual(['V-1.1', 'V-1.2', 'V-2.1', 'V-2.2']);
    expect(r6.test).toBe('T1');
    expect(c.niveluri.map((n) => n.id)).toEqual(['V-S05-globul-geografic-harta', 'V-S06-miscarile-pamantului']);
  });
});
