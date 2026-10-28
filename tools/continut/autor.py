"""Cadru compact pentru scrierea conținutului GeoQuest.

Fiecare lecție (nivel) se scrie așa:

    L = Lectie(5, "V-S17-...", "Titlu", "Întrebarea de la Descoperă",
               [("Titlu card", "Text card"), ...], stiaica="...", ref="...")
    L.a(1, "1.1 2.3", "Enunț?", "răspunsul corect", ["greșit 1", "greșit 2", "greșit 3"], "Explicația pentru greșeală.")
    L.l(2, "1.1", "Completează.", "Text cu [răspuns] și [altul].", ["capcană"], "Explicație.")
    L.s(2, "1.2", "Asociază.", [("stânga", "dreapta"), ...], "Explicație.")
    L.o(2, "4.2", "Ordonează.", ["primul", "al doilea", ...], "Criteriul", "Explicație.")
    L.p(2, "2.1", "Atinge pe hartă X.", "lume", lat, lon, "X", toleranta_km, "Explicație.")
    L.e(2, "2.1", "Pune etichetele.", [("id", "Etichetă", lat, lon), ...], "Explicație.", harta="lume")
    L.d(2, "2.1", "Ce e marcat?", "lume", lat, lon, "corect", ["greșit"...], "Explicație.")
    L.g(3, "2.3", "Citește graficul.", grafic, "corect", ["greșit"...], "Explicație.")

Varianta corectă se scrie mereu prima; aplicația amestecă variantele.
Competențele se scriu scurt ("1.1 2.3"); prefixul clasei (V-, VI-...) se pune automat.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "public", "content")
ROMAN = {5: "V", 6: "VI", 7: "VII", 8: "VIII"}
LAUDE = ["Corect.", "Exact.", "Bravo!", "Da, așa e.", "Foarte bine.", "Perfect."]


class Lectie:
    def __init__(self, clasa, id, titlu, intrebare, invata, stiaica=None, ref=None, prefix=None, schema=None, tip="nivel"):
        self.clasa, self.id, self.titlu, self.tip = clasa, id, titlu, tip
        self.R = ROMAN[clasa]
        self.prefix = prefix or id.split("-")[0] + id.split("-")[1].replace("S0", "").replace("S", "")
        self.nr = 0
        self.itemi = []
        self.n = {"id": id, "tip": tip, "titlu": titlu, "descopera": {"intrebare": intrebare}, "invata": []}
        if schema:
            self.n["descopera"]["schema"] = schema
        for c in invata:
            card = {"titlu": c[0], "text": c[1]}
            if len(c) > 2 and c[2]:
                card["schema"] = c[2]
            self.n["invata"].append(card)
        if stiaica:
            self.n["stiaiCa"] = stiaica
        if ref:
            self.n["referintaProfesor"] = ref

    # ------------------------------------------------------------ utilitare
    def _comp(self, s):
        return [f"{self.R}-{c}" for c in s.split()]

    def _add(self, tip, dif, comp, enunt, date, gresit, ok=None, ind=None, surse=None, id=None):
        self.nr += 1
        iid = id or f"{self.prefix}-{self.nr:02d}"
        x = {"id": iid, "nivel": self.id, "competente": self._comp(comp), "tip": tip, "dificultate": dif, "enunt": enunt,
             "date": date, "feedback": {"corect": ok or LAUDE[self.nr % len(LAUDE)], "gresit": gresit}}
        if ind:
            x["indiciu"] = ind
        if surse:
            x["surse"] = surse
        self.itemi.append(x)
        return iid

    # ------------------------------------------------------------ tipuri de itemi
    def a(self, dif, comp, enunt, corect, gresite, expl, schema=None, ev=None, **kw):
        d = {"variante": [corect, *gresite], "corect": 0}
        if schema:
            d["schema"] = schema
        if ev:
            d["evidentiat"] = ev
        return self._add("alegere", dif, comp, enunt, d, expl, **kw)

    def adev(self, dif, comp, afirmatie, adevarat, expl, **kw):
        """Adevărat/fals ca grilă cu două variante."""
        v = ["Adevărat", "Fals"] if adevarat else ["Fals", "Adevărat"]
        return self._add("alegere", dif, comp, f"Adevărat sau fals? {afirmatie}", {"variante": v, "corect": 0}, expl, **kw)

    def l(self, dif, comp, enunt, text, capcane, expl, **kw):
        raspunsuri = []

        def inloc(m):
            raspunsuri.append(m.group(1).strip())
            return "{" + str(len(raspunsuri) - 1) + "}"
        import re
        t = re.sub(r"\[([^\]]+)\]", inloc, text)
        return self._add("lacunar", dif, comp, enunt, {"text": t, "raspunsuri": raspunsuri, "distractori": capcane}, expl, **kw)

    def s(self, dif, comp, enunt, perechi, expl, **kw):
        return self._add("asociaza", dif, comp, enunt, {"perechi": [list(p) for p in perechi]}, expl, **kw)

    def o(self, dif, comp, enunt, elemente, criteriu, expl, **kw):
        return self._add("ordoneaza", dif, comp, enunt, {"elemente": elemente, "criteriu": criteriu}, expl, **kw)

    def p(self, dif, comp, enunt, harta, lat, lon, nume, tol, expl, **kw):
        return self._add("pin", dif, comp, enunt, {"harta": harta, "tinta": {"lat": lat, "lon": lon, "nume": nume}, "toleranta": tol}, expl, **kw)

    def e(self, dif, comp, enunt, tinte, expl, harta=None, schema=None, distr=None, **kw):
        d = {"tinte": [{"id": t[0], "eticheta": t[1], **({"lat": t[2], "lon": t[3]} if len(t) > 2 else {})} for t in tinte]}
        if harta:
            d["harta"] = harta
        if schema:
            d["schema"] = schema
        if distr:
            d["distractori"] = distr
        return self._add("etichete", dif, comp, enunt, d, expl, **kw)

    def d(self, dif, comp, enunt, harta, lat, lon, corect, gresite, expl, **kw):
        return self._add("denumeste", dif, comp, enunt, {"harta": harta, "punct": {"lat": lat, "lon": lon}, "variante": [corect, *gresite], "corect": 0}, expl, **kw)

    def ds(self, dif, comp, enunt, schema, ev, corect, gresite, expl, **kw):
        return self._add("denumeste", dif, comp, enunt, {"schema": schema, "evidentiat": ev, "variante": [corect, *gresite], "corect": 0}, expl, **kw)

    def g(self, dif, comp, enunt, grafic, corect, gresite, expl, **kw):
        return self._add("grafic", dif, comp, enunt, {"grafic": grafic, "variante": [corect, *gresite], "corect": 0}, expl, **kw)


def grafic(tip, titlu, date, unitate=None, sursa=None):
    g = {"tip": tip, "titlu": titlu, "date": [{"eticheta": a, "valoare": b} for a, b in date]}
    if unitate:
        g["unitate"] = unitate
    if sursa:
        g["sursa"] = sursa
    return g


class Expeditie(Lectie):
    """O expediție: pași cu text, itemi (scriși după fiecare pas) și, opțional, o cerință pentru Jurnalul exploratorului."""

    def __init__(self, clasa, id, titlu, intrebare, ref=None, prefix=None):
        super().__init__(clasa, id, titlu, intrebare, [("Ce faci în expediție", "Urmezi pașii, rezolvi sarcinile și notezi în Jurnalul exploratorului ce ai descoperit.")], ref=ref, prefix=prefix, tip="expeditie")
        self.n["pasi"] = []
        self._ultim = 0

    def pas(self, titlu, text, jurnal=None, foto=False):
        """Închide un pas: itemii scriși de la pasul anterior până acum intră în el."""
        noi = [i["id"] for i in self.itemi[self._ultim:]]
        self._ultim = len(self.itemi)
        p = {"titlu": titlu, "text": text}
        if noi:
            p["itemi"] = noi
        if jurnal:
            p["jurnal"] = {"cerinta": jurnal, **({"foto": True} if foto else {})}
        self.n["pasi"].append(p)


class Unitate:
    def __init__(self, clasa, fisier, nume):
        self.clasa, self.fisier, self.nume = clasa, fisier, nume
        self.lectii = []
        self.boss = []

    def add(self, *lectii):
        self.lectii.extend(lectii)
        return self

    def json(self):
        out = {"clasa": self.clasa, "unitate": self.nume, "niveluri": [l.n for l in self.lectii], "itemi": [i for l in self.lectii for i in l.itemi]}
        if self.boss:
            out["boss"] = self.boss
        return out

    def scrie(self):
        os.makedirs(f"{ROOT}/clasa-{self.clasa}", exist_ok=True)
        with open(f"{ROOT}/clasa-{self.clasa}/{self.fisier}", "w", encoding="utf-8") as f:
            json.dump(self.json(), f, ensure_ascii=False, indent=1)
        return {"fisier": self.fisier, "niveluri": [l.id for l in self.lectii], "boss": [b["id"] for b in self.boss]}


def extinde(fisier_existent_items, lectie):
    """Pentru lecțiile din MVP: păstrează itemii existenți și continuă numerotarea."""
    lectie.itemi = [i for i in fisier_existent_items if i["nivel"] == lectie.id] + lectie.itemi
    return lectie


def existent(clasa, fisier, id, prefix):
    """O lecție scrisă deja (în MVP), încărcată din fișierul generat, ca să i se adauge itemi noi cu numerotare continuă."""
    c = json.load(open(f"{ROOT}/clasa-{clasa}/{fisier}", encoding="utf-8"))
    n = next(x for x in c["niveluri"] if x["id"] == id)
    L = Lectie.__new__(Lectie)
    L.clasa, L.id, L.titlu, L.tip, L.R, L.prefix = clasa, id, n["titlu"], n["tip"], ROMAN[clasa], prefix
    L.n = n
    L.itemi = [i for i in c["itemi"] if i["nivel"] == id]
    L.nr = len(L.itemi)
    return L
