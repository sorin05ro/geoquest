# Cum publici GeoQuest pe internet (GitHub Pages)

> **Stare (28.10.2026):** aplicația e publicată la https://sorin05ro.github.io/geoquest/, din depozitul `sorin05ro/geoquest`. Orice modificare urcată în ramura `main` se publică singură, prin ramura `gh-pages`. Pașii de mai jos sunt pentru o instalare nouă.

Nu trebuie să scrii cod. Faci asta o singură dată; după aceea, orice modificare salvată se publică singură în 2–3 minute.

## Ce îți trebuie

- contul tău GitHub;
- aplicația gratuită **GitHub Desktop** (desktop.github.com), instalată pe calculator;
- folderul `geoquest` din `Desktop\App Geografie`.

## Pasul 1. Creează depozitul (o singură dată)

1. Deschide GitHub Desktop și intră în contul tău (File → Options → Accounts → Sign in).
2. Alege **File → Add local repository…** și selectează folderul `geoquest`.
3. GitHub Desktop îți spune că folderul nu e încă un depozit. Apasă **create a repository**, apoi **Create repository**.
4. Apasă **Publish repository** (sus). Lasă numele `geoquest`. **Debifează** „Keep this code private” (GitHub Pages gratuit cere depozit public; în el nu sunt date despre elevi). Apasă **Publish repository**.

## Pasul 2. Pornește publicarea (o singură dată)

1. Pe github.com, deschide depozitul `geoquest`.
2. **Settings → Pages**. La „Source”, alege **Deploy from a branch**, ramura **gh-pages**, folderul **/ (root)** (ramura apare după prima publicare).
3. Înapoi pe pagina depozitului: **Add file → Create new file**. Ca nume scrie exact `.github/workflows/publicare.yml` (barele creează singure folderele).
4. Deschide pe calculator fișierul `docs/publicare.yml` cu Notepad, copiază tot textul și lipește-l în pagina GitHub. Apasă **Commit changes…**, apoi din nou **Commit changes**.
5. În GitHub Desktop apasă **Fetch origin**, apoi **Pull origin**, ca fișierul nou să ajungă și pe calculator.
6. Mergi la tabul **Actions**: publicarea a pornit singură. După 2–3 minute, în **Settings → Pages** apare adresa aplicației, de forma `https://numele-tau.github.io/geoquest/`.

## Pasul 3. Dă adresa elevilor

- Generează un cod QR din adresă (de exemplu, din meniul de partajare al browserului Chrome) și proiectează-l pe tablă.
- Pe telefon, elevii deschid adresa în Chrome și aleg **Adaugă pe ecranul de pornire**. De atunci GeoQuest merge și fără internet.
- Pe tabla interactivă, deschide adresa și apasă **Ecran complet** din Turul geografic.

## Cum modifici ceva mai târziu

1. Modifici un fișier (de exemplu, un item din `public/content/clasa-5/u3-litosfera.json`).
2. În GitHub Desktop scrii un rând scurt la „Summary” (ex. „Corectez itemul V13-07”), apeși **Commit to main**, apoi **Push origin**.
3. În 2–3 minute, modificarea e online. Înainte de publicare, aplicația își verifică singură conținutul; dacă găsește o greșeală (de exemplu, o competență inexistentă), publicarea se oprește și în tabul Actions vezi ce trebuie corectat.

## Dacă vrei să o rulezi pe calculatorul tău

Instalează Node.js (nodejs.org, versiunea LTS), apoi, într-o fereastră de comandă deschisă în folderul `geoquest`:

```
npm install
npm run dev
```

Deschide adresa afișată (de obicei http://localhost:5173).

## Calendarul pentru alt an sau altă școală

Pune noua planificare `.docx` (cu același tabel: unitate | competențe | conținuturi | ore | săptămâna | evaluare) în `tools/planificare.docx` și rulează `npm run calendar` (are nevoie de Python 3 și de pachetul `python-docx`). Datele intervalelor și vacanțelor se schimbă în `tools/import_planificare.py`, în secțiunea „an școlar”.
