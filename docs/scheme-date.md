# Schemele de date

Tot conținutul stă în fișiere JSON, separat de cod. Fișierele se verifică automat cu `npm run check-content`.

## Unde stă fiecare lucru

| Fișier | Ce conține |
| --- | --- |
| `public/calendar/2026-2027.json` | Săptămânile S1–S36, vacanțele, zilele libere, evenimentele și planificarea pe clase. Se generează din `.docx` cu `npm run calendar`. |
| `public/content/competente.json` | Formulările exacte ale competențelor specifice (programa 2017). |
| `public/content/clasa-N/index.json` | Lista fișierelor de conținut ale clasei. |
| `public/content/clasa-N/uX-....json` | Nivelurile, itemii și boss-urile unei unități. |
| `public/content/insigne.json` | Insignele și condițiile lor. |
| `public/config/scoala.json` | Școala, clasele, manualul, modul Evaluare Națională. |
| `public/config/orizont-local.json` | Datele orizontului local (doar cu surse oficiale). |
| `public/config/corecturi.json` | Corecturile confirmate de profesor, aplicate la fiecare import de planificare. |
| `public/config/live.json` | Adresa și cheia publică Supabase pentru jocul live și colectare. |
| `public/content/clasa-N/profesor.json` | (opțional) itemii creați în editorul profesorului; se încarcă automat dacă există. |
| `public/content/evenimente/*.json` | Întrebările evenimentelor (Expediția Polară). |
| `tools/continut/*.py` | Sursa din care am generat conținutul MVP (opțional: poți edita direct JSON-ul). |

## Un item

```json
{
  "id": "V13-07",
  "nivel": "V-S13-vulcanii-cutremurele",
  "competente": ["V-1.1"],
  "tip": "alegere",
  "dificultate": 2,
  "enunt": "Cum se numește punctul de la suprafață aflat chiar deasupra hipocentrului?",
  "date": { "variante": ["epicentru", "crater", "camera magmatică", "dorsală"], "corect": 0 },
  "feedback": { "corect": "Corect.", "gresit": "Epicentrul e la suprafață, deasupra hipocentrului." },
  "indiciu": "opțional",
  "surse": ["opțional, obligatoriu pentru cifre"]
}
```

## Câmpul `date`, pe tipuri

| Tip | Nr. în catalog | `date` |
| --- | --- | --- |
| `pin` | 1 | `{ "harta": "lume" \| "romania", "tinta": { "lat", "lon", "nume" }, "toleranta": km }` |
| `denumeste` | 2 | `{ "harta", "punct": { "lat", "lon" } }` sau `{ "schema", "evidentiat" }`, plus `"variante"`, `"corect"` |
| `etichete` | 3 | `{ "harta" sau "schema", "tinte": [{ "id", "eticheta", "lat", "lon" }], "distractori"? }` |
| `ordoneaza` | 7 și 11 | `{ "elemente": [în ordinea corectă], "criteriu" }`; aplicația le amestecă |
| `asociaza` | 8 | `{ "perechi": [["stânga", "dreapta"], ...] }`; răspunsurile din dreapta trebuie să fie diferite |
| `lacunar` | 9 | `{ "text": "... {0} ... {1}", "raspunsuri": [...], "distractori": [...] }` |
| `grafic` | 12 | `{ "grafic": { "tip": "bare" \| "profil" \| "structura", "titlu", "unitate", "date": [{ "eticheta", "valoare" }], "sursa" }, "variante", "corect" }` |
| `alegere` | grilă | `{ "variante", "corect", "schema"? }` |

`"corect"` e numărul variantei corecte, de la 0. Aplicația amestecă singură variantele.

Schemele desenate disponibile (`"schema"`): `structura-interna`, `fund-oceanic`, `vulcan`, `busola`, `umbra-amiaza`.
