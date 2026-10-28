import json, os

ROOT = __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "..", "public", "content")

SURSE = {
    "INTERIOR": ["University of Alaska Fairbanks, Geophysical Institute – Earth's Layers (ATEP 58)", "ZME Science – Layers of the Earth"],
    "EVEREST": ["Al Jazeera, 8.12.2020 – anunțul Nepal–China: 8 848,86 m", "The Himalayan Times, 8.12.2020"],
    "RELIEF_RO": ["ICPDR – Romania: Facts & Figures (31 % munți, 36 % dealuri și podișuri, 33 % câmpii)", "manualele de geografie clasa a VIII-a"],
    "MACIN": ["Wikipedia – Munții Măcinului (Țuțuiatu, 467 m)", "Parcul Național Munții Măcinului – Traseul Țuțuiatu (parcmacin.ro)"],
    "DELTA_ANI": ["Radio Constanța, 1.09.2021 (HG 983/1990; UNESCO 1991)", "Euronews România – Ziua Deltei Dunării (1990)", "ESA – Pământul văzut din spațiu: Delta Dunării (UNESCO 1991)"],
    "CHILIA": ["Wikipedia – Chilia branch (aproximativ jumătate din debit; graniță România–Ucraina)", "manualele de geografie clasa a VIII-a"],
}

def item(id, nivel, comp, tip, dif, enunt, date, ok, gresit, indiciu=None, surse=None, ref=None):
    x = {"id": id, "nivel": nivel, "competente": comp, "tip": tip, "dificultate": dif, "enunt": enunt,
         "date": date, "feedback": {"corect": ok, "gresit": gresit}}
    if indiciu: x["indiciu"] = indiciu
    if surse: x["surse"] = surse
    if ref: x["referintaProfesor"] = ref
    return x

def alegere(id, nivel, comp, dif, enunt, variante, ok, gresit, schema=None, ev=None, **kw):
    d = {"variante": variante, "corect": 0}
    if schema: d["schema"] = schema
    if ev: d["evidentiat"] = ev
    return item(id, nivel, comp, "alegere", dif, enunt, d, ok, gresit, **kw)

def denumeste(id, nivel, comp, dif, enunt, variante, ok, gresit, harta=None, punct=None, schema=None, ev=None, **kw):
    d = {"variante": variante, "corect": 0}
    if harta: d["harta"] = harta; d["punct"] = punct
    if schema: d["schema"] = schema; d["evidentiat"] = ev
    return item(id, nivel, comp, "denumeste", dif, enunt, d, ok, gresit, **kw)

def pin(id, nivel, comp, dif, enunt, harta, lat, lon, nume, tol, ok, gresit, **kw):
    return item(id, nivel, comp, "pin", dif, enunt, {"harta": harta, "tinta": {"lat": lat, "lon": lon, "nume": nume}, "toleranta": tol}, ok, gresit, **kw)

def etichete(id, nivel, comp, dif, enunt, tinte, ok, gresit, harta=None, schema=None, distractori=None, **kw):
    d = {"tinte": tinte}
    if harta: d["harta"] = harta
    if schema: d["schema"] = schema
    if distractori: d["distractori"] = distractori
    return item(id, nivel, comp, "etichete", dif, enunt, d, ok, gresit, **kw)

def ordoneaza(id, nivel, comp, dif, enunt, elemente, criteriu, ok, gresit, **kw):
    return item(id, nivel, comp, "ordoneaza", dif, enunt, {"elemente": elemente, "criteriu": criteriu}, ok, gresit, **kw)

def asociaza(id, nivel, comp, dif, enunt, perechi, ok, gresit, **kw):
    return item(id, nivel, comp, "asociaza", dif, enunt, {"perechi": perechi}, ok, gresit, **kw)

def lacunar(id, nivel, comp, dif, enunt, text, rasp, distr, ok, gresit, **kw):
    return item(id, nivel, comp, "lacunar", dif, enunt, {"text": text, "raspunsuri": rasp, "distractori": distr}, ok, gresit, **kw)

def grafic(id, nivel, comp, dif, enunt, g, variante, ok, gresit, **kw):
    return item(id, nivel, comp, "grafic", dif, enunt, {"grafic": g, "variante": variante, "corect": 0}, ok, gresit, **kw)

def scrie(clasa, fisier, unitate, niveluri, itemi, boss=None):
    os.makedirs(f"{ROOT}/clasa-{clasa}", exist_ok=True)
    out = {"clasa": clasa, "unitate": unitate, "niveluri": niveluri, "itemi": itemi}
    if boss: out["boss"] = boss
    with open(f"{ROOT}/clasa-{clasa}/{fisier}", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return {"fisier": fisier, "niveluri": [n["id"] for n in niveluri], "boss": [b["id"] for b in (boss or [])]}
