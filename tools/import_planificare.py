#!/usr/bin/env python3
"""Importă planificarea calendaristică (.docx) și generează public/calendar/2026-2027.json.

Utilizare:
    python3 tools/import_planificare.py [cale/planificare.docx]

Tabelele din .docx trebuie să aibă coloanele:
    Unitatea de învățare | Competențe specifice | Conținuturi | Nr. ore alocate | Săptămâna | Observații/Evaluare
Câte un tabel pe clasă, în ordinea V, VI, VII, VIII.
Corecturile confirmate de profesor sunt în tools/corecturi.json.
"""
import datetime as dt
import json
import re
import sys
import unicodedata
from pathlib import Path

import docx

ROOT = Path(__file__).resolve().parent.parent
DOCX = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tools" / "planificare.docx"
CORECTURI = json.loads((ROOT / "public" / "config" / "corecturi.json").read_text(encoding="utf-8"))
OUT = ROOT / "public" / "calendar" / "2026-2027.json"

ROMAN = {5: "V", 6: "VI", 7: "VII", 8: "VIII"}
CLASE = [5, 6, 7, 8]

# ---------------------------------------------------------------- an școlar
AN = {
    "an": "2026-2027",
    "sursa": "OMEC nr. 3194/09.02.2026; vacanța mobilă: decizia ISJ Buzău",
    "intervale": [
        {"nr": 1, "de": "2026-09-07", "pana": "2026-10-23"},
        {"nr": 2, "de": "2026-11-02", "pana": "2026-12-22"},
        {"nr": 3, "de": "2027-01-11", "pana": "2027-02-26"},
        {"nr": 4, "de": "2027-03-08", "pana": "2027-04-23"},
        {"nr": 5, "de": "2027-05-05", "pana": "2027-06-18"},
    ],
    "vacante": [
        {"nume": "Vacanța de toamnă", "de": "2026-10-24", "pana": "2026-11-01"},
        {"nume": "Vacanța de iarnă", "de": "2026-12-23", "pana": "2027-01-10"},
        {"nume": "Vacanța mobilă", "de": "2027-02-27", "pana": "2027-03-07"},
        {"nume": "Vacanța de primăvară", "de": "2027-04-24", "pana": "2027-05-04"},
        {"nume": "Vacanța de vară", "de": "2027-06-19", "pana": "2027-09-12"},
    ],
    # zile libere legale care cad în zile de curs
    "zileLibere": [
        {"data": "2026-11-30", "nume": "Sfântul Andrei"},
        {"data": "2026-12-01", "nume": "Ziua Națională a României"},
        {"data": "2027-06-01", "nume": "Ziua Copilului"},
    ],
    "evenimente": [
        {"id": "scoala-altfel", "nume": "Școala Altfel – Expediția Polară", "de": "2026-12-16", "pana": "2026-12-22"},
        {"id": "saptamana-verde", "nume": "Săptămâna verde – Patrula Verde", "de": "2027-04-19", "pana": "2027-04-23"},
    ],
    # ultima zi de cursuri diferită pe clase (confirmat de profesor)
    "ultimaZi": {"5": "2027-06-18", "6": "2027-06-18", "7": "2027-06-18", "8": "2027-06-11"},
}


def d(s):
    return dt.date.fromisoformat(s)


def build_weeks():
    """S1 = luni 7.09.2026; se numără doar săptămânile cu cel puțin o zi de curs."""
    weeks = []
    monday = d("2026-09-07")
    nr = 0
    end = d("2027-06-18")
    while monday <= end:
        days = [monday + dt.timedelta(i) for i in range(5)]
        interval = None
        zile_curs = []
        for day in days:
            for iv in AN["intervale"]:
                if d(iv["de"]) <= day <= d(iv["pana"]):
                    interval = iv["nr"]
                    zile_curs.append(day)
        if zile_curs:
            nr += 1
            libere = [z["data"] for z in AN["zileLibere"] if d(z["data"]) in zile_curs]
            weeks.append({
                "nr": nr,
                "de": zile_curs[0].isoformat(),
                "pana": zile_curs[-1].isoformat(),
                "interval": interval,
                "zileCurs": len(zile_curs) - len(libere),
                "zileLibere": libere,
            })
        monday += dt.timedelta(7)
    return weeks


# ---------------------------------------------------------------- utilitare
def ascii_slug(text, words=4):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9 ]+", " ", t).lower().split()
    stop = {"si", "de", "la", "a", "ale", "al", "in", "pe", "cu", "unor", "lor", "ei", "o", "un"}
    t = [w for w in t if w not in stop]
    return "-".join(t[:words]) or "nivel"


def comp_list(raw, clasa):
    """'1.1., 1.2. / 2.1. – 2.3.' -> ['V-1.1', 'V-1.2', 'V-2.1', ...]"""
    raw = raw.replace("–", "-").replace("—", "-")
    out = []
    for m in re.finditer(r"(\d)\.(\d)\.?\s*(?:-\s*(\d)\.(\d)\.?)?", raw):
        a, b, c, e = m.groups()
        if c is None:
            out.append((int(a), int(b)))
        else:
            out.extend(expand_range((int(a), int(b)), (int(c), int(e)), clasa))
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x)
            res.append(f"{ROMAN[clasa]}-{x[0]}.{x[1]}")
    return res


COMPETENTE = json.loads((ROOT / "public" / "content" / "competente.json").read_text(encoding="utf-8"))


def expand_range(start, end, clasa):
    allc = [tuple(map(int, k.split("-")[1].split("."))) for k in COMPETENTE[str(clasa)]]
    return [c for c in allc if start <= c <= end]


def weeks_of(raw):
    nums = [int(x) for x in re.findall(r"\d+", raw)]
    return list(range(nums[0], nums[-1] + 1))


EVAL_MAP = [
    (r"T₀", "busola"), (r"T₁", "boss"), (r"T₂", "boss"), (r"T₃", "boss"), (r"T₄", "boss"), (r"T₅", "boss"),
    (r"Tf", "mare-expeditie"), (r"Probe practice", "expeditie"),
]
EVAL_CODES = [
    ("T₀", "T0"), ("T₁", "T1"), ("T₂", "T2"), ("T₃", "T3"), ("T₄", "T4"), ("T₅", "T5"), ("Tf", "Tf"),
    ("Probe practice", "PP"), ("Evaluare orală", "EO"), ("Portofoliu", "P"),
    ("Autoevaluare/Interevaluare", "AE/IE"), ("Autoevaluare", "AE"), ("Interevaluare", "IE"),
    ("Consolidare", "C"), ("Probă scrisă", "PS"),
]


def eval_codes(raw):
    raw = raw.replace("Autoevaluare/ / Interevaluare", "Autoevaluare/Interevaluare")
    codes = []
    for needle, code in EVAL_CODES:
        if needle in raw:
            if code in ("AE", "IE") and "AE/IE" in codes:
                continue
            if code == "AE" and "Autoevaluare/" in raw and "Interevaluare" not in raw:
                pass
            codes.append(code)
    return codes


# ---------------------------------------------------------------- import
def parse_table(t, clasa):
    rows = []
    for r in t.rows[1:]:
        cells, prev = [], None
        for c in r.cells:
            if c._tc is prev:
                continue
            prev = c._tc
            cells.append(c.text.strip())
        if len(cells) < 6 or not re.search(r"\d", cells[4]):
            continue
        unit, comp, cont, ore, sapt, ev = cells[:6]
        rows.append({
            "unitate": re.sub(r"\s+", " ", unit.replace("\n", " ")).strip(),
            "competenteBrut": comp.replace("\n", " / "),
            "continuturi": [re.sub(r"\s+", " ", x).strip() for x in cont.split("\n") if x.strip()],
            "ore": int(re.findall(r"\d+", ore)[0]),
            "saptamani": weeks_of(sapt),
            "evaluareBrut": ev.replace("\n", " / "),
        })
    return rows


def main():
    document = docx.Document(str(DOCX))
    weeks = build_weeks()
    assert len(weeks) == 36, len(weeks)
    week_by_nr = {w["nr"]: w for w in weeks}
    probleme = []
    planificare = []
    niveluri = []

    for clasa, table in zip(CLASE, document.tables):
        R = ROMAN[clasa]
        last_day = d(AN["ultimaZi"][str(clasa)])
        for row in parse_table(table, clasa):
            comps = comp_list(row["competenteBrut"], clasa)
            valid = set(COMPETENTE[str(clasa)])
            bad = [c for c in comps if c not in valid]
            for b in bad:
                probleme.append(f"Clasa {R}, S{row['saptamani'][0]}: competența {b} nu există în programă; eliminată.")
            comps = [c for c in comps if c in valid]
            key = f"{clasa}:{row['saptamani'][0]}"
            for c in CORECTURI.get("competenteAdaugate", {}).get(key, []):
                if c not in comps:
                    comps.append(c)
            comps.sort(key=lambda x: tuple(map(int, x.split("-")[1].split("."))))

            sapt = [s for s in row["saptamani"] if s in week_by_nr and d(week_by_nr[s]["de"]) <= last_day]
            codes = eval_codes(row["evaluareBrut"])
            is_pp = "PP" in codes
            continuturi = row["continuturi"]

            # fiecare conținut devine un nivel; recapitulările și „Recapitulare și evaluare” devin evenimente
            items = []
            for c in continuturi:
                low = c.lower()
                if "(recapitulare)" in low or low.endswith("- recapitulare") or "recapitulare" == low.split()[-1]:
                    items.append(("portal", c))
                elif low.startswith("recapitulare"):
                    items.append(("recapitulare", c))
                elif is_pp or low.startswith("aplica") or low.startswith("studiu de caz"):
                    items.append(("expeditie", c))
                else:
                    items.append(("nivel", c))

            # distribuie conținuturile pe săptămâni, în ordine
            lessons = [it for it in items if it[0] != "recapitulare"]
            recaps = [it for it in items if it[0] == "recapitulare"]
            n, nw = len(lessons), len(sapt)
            placed = []
            for i, (kind, c) in enumerate(lessons):
                w = sapt[min(nw - 1, (i * nw) // n)] if nw else None
                placed.append((w, kind, c))
            for kind, c in recaps:
                placed.append((sapt[-1] if nw else None, kind, c))

            for s in sapt:
                here = [(k, c) for (w, k, c) in placed if w == s]
                evts = []
                if s == sapt[0] and "T0" in codes:
                    evts.append("busola")
                for k, _ in here:
                    if k in ("portal", "expeditie") and k not in evts:
                        evts.append(k)
                if s == sapt[-1]:
                    for code in ("T1", "T2", "T3", "T4", "T5"):
                        if code in codes:
                            evts.append("boss")
                    if "Tf" in codes:
                        evts.append("mare-expeditie")
                nivel_ids = []
                for k, c in here:
                    if k in ("nivel", "expeditie"):
                        lid = f"{R}-S{s:02d}-{ascii_slug(c)}"
                        nivel_ids.append(lid)
                        niveluri.append({
                            "id": lid, "clasa": clasa, "saptamana": s, "unitate": row["unitate"],
                            "titlu": c, "tip": "expeditie" if k == "expeditie" else "nivel", "competente": comps,
                        })
                boss_code = next((c for c in ("T1", "T2", "T3", "T4", "T5", "Tf") if c in codes), None)
                planificare.append({
                    "clasa": clasa,
                    "saptamana": s,
                    "interval": week_by_nr[s]["interval"],
                    "unitate": row["unitate"],
                    "continuturi": [c for (k, c) in here],
                    "niveluri": nivel_ids,
                    "competente": comps,
                    "ore": row["ore"] // len(row["saptamani"]) if row["saptamani"] else row["ore"],
                    "evaluare": codes,
                    "tipEveniment": evts or (["recapitulare"] if any(k == "recapitulare" for k, _ in here)
                                             else ["nivel"] if here else ["continuare"]),
                    **({"test": boss_code} if boss_code and s == sapt[-1] else {}),
                })

    # săptămâni fără ore (Școala Altfel, Săptămâna verde etc.)
    acoperite = {(p["clasa"], p["saptamana"]) for p in planificare}
    for clasa in CLASE:
        last_day = d(AN["ultimaZi"][str(clasa)])
        for w in weeks:
            if d(w["de"]) > last_day:
                continue
            if (clasa, w["nr"]) not in acoperite:
                ev = next((e for e in AN["evenimente"] if d(e["de"]) <= d(w["pana"]) and d(e["pana"]) >= d(w["de"])), None)
                planificare.append({
                    "clasa": clasa, "saptamana": w["nr"], "interval": w["interval"], "unitate": None,
                    "continuturi": [], "niveluri": [], "competente": [], "ore": 0, "evaluare": [],
                    "tipEveniment": ["eveniment"] if ev else ["fara-ore"],
                    **({"eveniment": ev["id"]} if ev else {}),
                })
    planificare.sort(key=lambda p: (p["clasa"], p["saptamana"]))

    for w in weeks:
        if w["zileCurs"] < 5:
            motiv = "zi liberă legală" if w["zileLibere"] else "săptămână incompletă"
            probleme.append(f"S{w['nr']} ({w['de']} – {w['pana']}): doar {w['zileCurs']} zile de curs ({motiv}).")

    out = {**AN, "saptamani": weeks, "planificare": planificare, "niveluri": niveluri,
           "generat": {"din": DOCX.name, "corecturi": CORECTURI.get("note", [])}, "observatii": probleme}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK: {len(weeks)} săptămâni, {len(planificare)} rânduri, {len(niveluri)} niveluri → {OUT.relative_to(ROOT)}")
    for p in probleme:
        print("  !", p)


if __name__ == "__main__":
    main()
