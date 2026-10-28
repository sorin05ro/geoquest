import type { Item } from '../types';

const CEDILE = /[şţŞŢ]/;

/** Aceleași reguli ca tools/verifica-continut.mjs, pentru itemii scriși în editor. Întoarce problemele, în cuvinte simple. */
export function valideazaItem(it: Item, competenteValide: Set<string>): string[] {
  const e: string[] = [];
  if (!it.enunt.trim()) e.push('Scrie enunțul.');
  if (!it.competente.length) e.push('Alege cel puțin o competență.');
  for (const c of it.competente) if (!competenteValide.has(c)) e.push(`Competența ${c} nu există în programa clasei.`);
  if (!it.feedback.corect.trim() || !it.feedback.gresit.trim()) e.push('Scrie ambele mesaje de feedback; cel pentru greșeală explică răspunsul corect.');
  if (CEDILE.test(JSON.stringify(it))) e.push('Textul are ş sau ţ cu sedilă; folosește ș și ț cu virgulă.');
  const d = it.date as Record<string, unknown>;
  switch (it.tip) {
    case 'alegere': {
      const v = (d.variante as string[]).map((x) => x.trim());
      if (v.filter(Boolean).length < 2 || v.some((x) => !x)) e.push('Completează toate variantele.');
      if (new Set(v).size !== v.length) e.push('Variantele trebuie să fie diferite.');
      break;
    }
    case 'lacunar': {
      const k = ((d.text as string).match(/\{\d+\}/g) ?? []).length;
      if (!k) e.push('Pune cel puțin un cuvânt între paranteze drepte, ca să devină spațiu de completat.');
      if ((d.distractori as string[]).some((x) => (d.raspunsuri as string[]).includes(x))) e.push('Un cuvânt-capcană e identic cu un răspuns.');
      break;
    }
    case 'asociaza': {
      const p = d.perechi as [string, string][];
      if (p.length < 3 || p.some(([a, b]) => !a.trim() || !b.trim())) e.push('Completează cel puțin 3 perechi întregi.');
      if (new Set(p.map((x) => x[1])).size !== p.length) e.push('Răspunsurile din coloana dreaptă trebuie să fie diferite.');
      break;
    }
    case 'ordoneaza': {
      const el = d.elemente as string[];
      if (el.length < 3) e.push('Scrie cel puțin 3 elemente, câte unul pe rând.');
      if (new Set(el).size !== el.length) e.push('Elementele trebuie să fie diferite.');
      break;
    }
    case 'pin': {
      const t = d.tinta as { lat: number; lon: number; nume?: string } | undefined;
      if (!t || !Number.isFinite(t.lat)) e.push('Atinge harta ca să alegi locul corect.');
      if (!t?.nume?.trim()) e.push('Scrie numele locului.');
      break;
    }
    default: break;
  }
  return e;
}

/** „Soarele răsare la [est] și apune la [vest].” → text cu {0}, {1} și lista răspunsurilor. */
export function lacunarDinParanteze(text: string): { text: string; raspunsuri: string[] } {
  const raspunsuri: string[] = [];
  const t = text.replace(/\[([^\]]+)\]/g, (_, w: string) => { raspunsuri.push(w.trim()); return `{${raspunsuri.length - 1}}`; });
  return { text: t, raspunsuri };
}
