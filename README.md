# GeoQuest

Geografie pentru clasele V–VIII, ca o expediție. Aplicație web instalabilă (PWA), care merge și offline, construită după programa școlară (OMEN 3393/2017) și după planificarea calendaristică 2026–2027 a prof. Negraru Sorin (Școala Gimnazială Nr. 6, Râmnicu Sărat).

- **Publicare:** `docs/ghid-publicare.md`
- **Jocul live pe telefoane (Supabase UE):** `docs/ghid-joc-live.md`
- **Modul profesor (clase, teme, rezultate, editor, import):** `docs/ghid-profesor.md`
- **Scheme de date:** `docs/scheme-date.md`
- **Neconcordanțe:** `docs/discrepante.md`
- **Acoperirea competențelor:** `docs/acoperire-competente.md` (se generează cu `npm run check-content`)
- **Surse și licențe ale hărților:** `public/content/harti/ATRIBUIRI.md`

## Conținutul

Tot anul 2026–2027, pentru toate cele patru clase: **3 334 de itemi în 130 de niveluri** (V: 673, VI: 656, VII: 933, VIII: 1 069), cu 30 de itemi pe fiecare lecție, plus expedițiile, Busola de start, Boss-urile T₁–T₅ și Marea Expediție. Evenimentele: Expediția Polară (Școala Altfel) și Patrula Verde (Săptămâna verde). Faptele numerice au sursa și anul afișate; datele imaginare din grafice sunt marcate „date imaginare”.

Conținutul se scrie în Python, în `tools/continut/` (câte un modul pe unitate: `v_u3_litosfera.py`, `viii_u4_populatie.py` etc.), și se generează cu `python3 tools/continut/genereaza.py`, apoi se verifică cu `npm run check-content`.

## Comenzi

| Comandă | Ce face |
| --- | --- |
| `npm install` | instalează dependențele (o dată) |
| `npm run dev` | pornește aplicația local |
| `npm test` | rulează testele (calendar, reguli de joc) |
| `npm run check-content` | verifică tot conținutul și reface tabelul de acoperire |
| `npm run calendar` | regenerează calendarul din `tools/planificare.docx` (se poate face și din aplicație: Modul profesor → Planificare) |
| `npm run build` | construiește versiunea de publicat în `dist/` |

## Confidențialitate

Elevii intră cu poreclă și avatar, fără nume, e-mail sau fotografii ale lor. Tot progresul stă pe dispozitiv (IndexedDB). Excepțiile le pornește profesorul: în jocul live și la colectarea rezultatelor, porecla, avatarul și rezultatele trec printr-un canal Supabase din UE, fără să fie salvate pe server. Rapoartele ajung doar pe calculatorul profesorului.
