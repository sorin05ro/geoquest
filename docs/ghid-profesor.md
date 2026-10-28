# Modul profesor: ghid scurt

Intri din **Profil → Sunt profesor** (sau de pe primul ecran, înainte de a alege clasa) și tastezi PIN-ul. PIN-ul rămâne valabil până apeși „Ieși” sau închizi aplicația.

Tot ce vezi aici stă **doar pe acest calculator**: clasele, temele, rapoartele, itemii creați de tine. Lucrează de preferință pe același calculator (cel de la clasă sau laptopul tău).

## 1. Clase și teme

**Codurile claselor**
1. Apasă **Generează codurile claselor**. Fiecare clasă (a V-a A, a V-a B…) primește un cod, de exemplu `5A-K7QM`.
2. La prima oră: **Arată QR pe tablă**. Elevii scanează codul cu telefonul; aplicația le alege singură clasa.
3. Elevii care au deja aplicația pot scrie codul în **Profil → Trimite rezultatele profesorului**.

Codul doar grupează rapoartele pe clase. Nu cere cont, e-mail sau nume.

**Teme cu termen**
1. Alege clasa, termenul și lecțiile (se pot alege doar lecțiile care au exerciții).
2. **Creează tema** → apare codul QR și linkul. Proiectează-l sau trimite linkul pe grupul clasei.
3. Când elevul deschide linkul, tema apare pe harta lui, cu termenul și progresul („2 din 3 lecții”). Lecțiile temei se deschid chiar dacă în calendar vin mai târziu.

## 2. Rezultate

1. În clasă, după ce elevii au lucrat: **Deschide colectarea**. Pe tablă apare un cod QR cu un PIN.
2. Elevii scanează codul (sau intră în **Profil → Trimite rezultatele profesorului**) și apasă **Trimite**.
3. Pe tablă crește numărul de rapoarte primite. La final: **Încheie colectarea**.

**Ce trimite elevul:** porecla, avatarul, codul clasei, XP-ul, nivelurile terminate cu stele, câte răspunsuri corecte are pe fiecare competență, itemii greșiți și progresul la teme. Nimic altceva.

**Panoul pe competențe:**
- Un rând pe elev (ultimul raport primit) și o coloană pe competență, cu procentul de răspunsuri corecte.
- Culoarea doar întărește cifra. O celulă goală înseamnă că elevul nu a exersat încă acea competență.
- Ultimul rând arată media clasei. Coloanele T₁…Tf arată scorul la Boss-uri.
- Dedesubt: **itemii greșiți de cei mai mulți elevi** (bune de reluat la oră) și **temele**: câți au terminat, câți au început.

**Export:**
- **Descarcă CSV (Excel)**: se deschide direct în Excel, cu diacriticele corecte.
- **Tipărește / PDF**: alege „Salvare ca PDF” în fereastra de tipărire. Bun pentru dosarul comisiei metodice sau pentru catalog.

**Ștergere:** la final de an, șterge rapoartele fiecărei clase (GDPR).

Fără serverul jocului live configurat (`docs/ghid-joc-live.md`), colectarea merge doar în modul demonstrație.

## 3. Conținut (editorul de itemi)

1. Alege clasa și lecția. Competențele din planificare se propun singure; le poți schimba.
2. Alege tipul: grilă, text lacunar (răspunsurile între paranteze drepte: `Soarele răsare la [est].`), asociere, ordonare sau localizare pe hartă (atingi harta în locul corect).
3. Scrie feedback-ul pentru greșeală: explică răspunsul corect, nu doar „greșit”.
4. **Previzualizează**: vezi exercițiul exact cum îl vede elevul. Aplicația te anunță dacă lipsește ceva sau dacă ai scris ş/ţ cu sedilă.
5. **Salvează itemul.** Pe acest dispozitiv îl vezi imediat în lecție. Poți crea lecții și pentru clasele a VI-a și a VII-a, care încă nu au conținut publicat.

**Ca itemii să ajungă la elevi:**
1. **Descarcă profesor.json** pentru clasa respectivă.
2. Pune fișierul în proiect, în `public/content/clasa-N/` (N = 5, 6, 7 sau 8).
3. Publică (GitHub Desktop: Commit, apoi Push).

## 4. Planificare

Alegi planificarea `.docx` (sau un CSV după șablon). Aplicația arată:
- câte săptămâni, lecții și teste are fiecare clasă;
- ce diferă față de calendarul publicat;
- ce observații a găsit (competențe inexistente, săptămâni scurte).

**Folosește pe acest dispozitiv** e pentru probă. **Descarcă calendarul** îți dă fișierul de pus în locul lui `public/calendar/2026-2027.json`, ca să ajungă la toți.

Corecturile confirmate (de exemplu, competențele adăugate la Africa) stau în `public/config/corecturi.json` și se aplică la fiecare import.

## 5. Calendar și jurnal

- **Calendar**: ce se predă în fiecare săptămână și ce e deblocat. Poți debloca sau bloca manual o lecție (doar pe acest dispozitiv). Poți alege și o dată de probă.
- **Jurnal**: lucrările din expedițiile făcute pe acest dispozitiv, cu bifa „Validat de profesor”.


## 6. Testele pe hartă: Busola, Boss-urile, Marea Expediție

- **Busola de start (T₀)**, în prima săptămână: 15 întrebări din anul trecut, fără notă, cu răspunsul corect arătat imediat. Procentul de răspunsuri corecte alege dificultatea de pornire a elevului (80 % sau mai mult: grea; 50–79 %: medie; sub 50 %: ușoară). Apoi dificultatea se potrivește singură.
- **Boss-urile T₁–T₅**, în săptămânile testelor din planificare: 15 întrebări din lecțiile predate de la testul anterior. Rezultatele apar la final, cu explicații. Două încercări; poți da una nouă din fila Rezultate.
- **Marea Expediție (Tf)**: 20 de întrebări din tot anul.

## 7. Recapitularea pentru Evaluarea Națională (clasa a VIII-a)

Pe harta elevilor de-a VIII-a apare cartea „Recapitulare pentru Evaluarea Națională”, de la săptămâna 28 (din `public/config/scoala.json`, câmpul `modEvaluareNationala`). Elevul vede, pe fiecare unitate deja predată, cât a rezolvat corect ultima dată și poate:
- recapitula o unitate (10 întrebări, întâi cele greșite, apoi cele neîncercate);
- relua „Greșelile mele”;
- da un test de recapitulare de 20 de întrebări, cu notă orientativă (1–10, un punct din oficiu), vizibilă doar lui.

Din fila Calendar poți porni sau opri modul pe dispozitivul tău (de exemplu, pentru tablă), indiferent de configurație.

## 8. Patrula Verde (Săptămâna verde, miercuri, 21.04.2027)

În **Joc live cu telefoane**, alege „Patrula Verde”. Clasele se aleg automat grupate (a V-a + a VII-a sau a VI-a + a VIII-a). Sub alegere se deschide **Planul activității**: 5 ateliere pentru 1,5–2 ore (jocul live cu pădurea colectivă, harta verde a școlii din fotografiile dronei, etichete pentru plante la imprimanta 3D, patrula în teren, angajamentul clasei), cu regulile de siguranță pentru dronă. Pe tablă, la fiecare răspuns corect al clasei, în curtea școlii crește un copac.
