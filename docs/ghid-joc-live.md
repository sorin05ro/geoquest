# Jocul live pe telefoane: ce trebuie făcut o singură dată

Jocul live are nevoie de un „releu” pe internet, prin care tabla și telefoanele își trimit mesaje. GeoQuest folosește pentru asta **Supabase Realtime**, cu servere în UE.

- Nu se creează nicio bază de date. Pe releu trec doar porecla, avatarul și răspunsurile din timpul jocului, iar după joc nu rămâne nimic salvat.
- Fără acest pas, jocul live merge doar în **mod demonstrație**: pe un singur calculator, în mai multe ferestre.
- Turul geografic (fără telefoane) merge oricum, fără internet.

## Pasul 1. Creează proiectul (gratuit)

1. Intră pe supabase.com și fă-ți cont (poți folosi contul GitHub).
2. Apasă **New project**.
   - Numele: `geoquest`.
   - Parola bazei de date: una lungă, pe care o păstrezi (nu o vei folosi în aplicație).
   - **Region: Central EU (Frankfurt)**. E important pentru GDPR: datele rămân în UE.
   - Planul gratuit (Free) e suficient.
3. Așteaptă 1–2 minute până se pregătește proiectul.

## Pasul 2. Copiază adresa și cheia publică

1. În proiect, deschide **Project Settings** (rotița din stânga jos), apoi secțiunea cu cheile API (**API Keys**) și cea cu datele proiectului (**Data API** sau **API**).
2. Copiază:
   - **Project URL**, de forma `https://abcdefgh.supabase.co`;
   - cheia publică pentru browser: **Publishable key** (începe cu `sb_publishable_`) sau, în proiectele mai vechi, cheia **anon public**.
3. **Nu** copia cheia secretă (`secret` / `service_role`). Ea nu trebuie pusă niciodată în aplicație.

## Pasul 3. Pune-le în aplicație

Deschide cu Notepad fișierul `public/config/live.json` și completează:

```json
{
  "supabaseUrl": "https://abcdefgh.supabase.co",
  "supabaseAnonKey": "sb_publishable_..."
}
```

Salvează, apoi publică modificarea ca de obicei (GitHub Desktop → Commit → Push). Cheia publică e făcută să stea în browser, deci poate fi în depozitul public.

## Pasul 4. Încearcă

1. Pe calculatorul de la tablă: **Profil → Sunt profesor → Joc live cu telefoane**. Alege clasa și lecțiile, apoi **Deschide sala de joc**.
2. Dacă nu mai apare caseta „Mod demonstrație”, releul funcționează.
3. Scanează codul QR cu un telefon, alege o poreclă și apasă **Intră**. Porecla trebuie să apară pe tablă în câteva secunde.

## Dacă nu merge

- **„Nu m-am putut conecta la serverul jocului”**: verifică adresa și cheia (fără spații în plus, cu ghilimele).
- **Telefoanele nu apar pe tablă**:
  - În Supabase, la **Realtime → Settings**, verifică dacă sunt permise canalele publice. Dacă e bifat doar accesul la canale private, debifează.
  - Telefoanele și tabla au nevoie de internet în timpul jocului.
- **Proiectul a fost pus pe pauză**: pe planul gratuit, Supabase poate pune pe pauză un proiect nefolosit o vreme. Îl repornești din panou, cu **Restore project**.

## Cum se joacă

| Pe tablă | Pe telefon |
| --- | --- |
| Profesorul alege clasa (sau două clase reunite), lecțiile sau Expediția Polară, numărul de echipe și de întrebări. | Elevul scanează codul QR, scrie o poreclă (nu numele real), alege un avatar și clasa. |
| Tabla arată întrebarea, harta și timpul. | Telefonul arată variantele A–D (cu simboluri ▲ ◆ ● ■) sau harta pe care pune pionul. |
| După fiecare întrebare: răspunsul corect, câți au ales fiecare variantă, scorul echipelor. La Expediția Polară, harta colectivă se descoperă. | Elevul vede dacă a răspuns corect și câte puncte a adus echipei. Poate trimite reacții: 👍 🤔 🎉 😮. |
| La final: clasamentul echipelor. Primii 5 exploratori apar doar dacă profesorul bifează clasamentul individual. | Locul echipei; locul personal doar dacă e activat clasamentul individual. |

**Punctajul:** 500 de puncte pentru răspunsul corect, plus până la 500 pentru viteză. Scorul unei echipe e media membrilor, ca echipele mai mici să nu fie dezavantajate.
