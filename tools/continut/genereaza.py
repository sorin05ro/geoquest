"""Generează tot conținutul GeoQuest: unitățile, testele (Busola, Boss-urile, Marea Expediție) și indexurile.

Rulare: python3 tools/continut/genereaza.py
"""
import importlib
import json
import os
import subprocess
import sys

AICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AICI)
from autor import ROOT, ROMAN  # noqa: E402

MODULE = {
    5: ["v_u1_univers", "v_u2_miscare", "v_u3_litosfera", "v_u4_atmosfera", "v_u5_hidrosfera", "v_u6_biosfera", "v_u7_zone"],
    6: ["vi_u1_cunoastere", "vi_u2_antroposfera", "vi_u3_europa", "vi_u4_contemporana"],
    7: ["vii_u1_asia", "vii_u2_africa", "vii_u3_america", "vii_u4_australia", "vii_u5_mediu"],
    8: ["viii_u1_pozitie", "viii_u2_relief", "viii_u3_clima_ape", "viii_u4_populatie", "viii_u5_economie", "viii_u6_regiuni", "viii_u7_mediu_europa"],
}
# conținutul scris în MVP (Etapa 1) are generatoarele lui; îl rulăm întâi
VECHI = ["gen_clasa5", "gen_clasa8", "gen_evenimente", "gen_patrula"]


def main():
    for v in VECHI:
        subprocess.run([sys.executable, os.path.join(AICI, f"{v}.py")], check=True, stdout=subprocess.DEVNULL)
    for clasa, module in MODULE.items():
        for m in module:
            u = importlib.import_module(m).unitate()
            u.scrie()
    # testele
    import teste
    for clasa in (5, 6, 7, 8):
        u = teste.unitate(clasa)
        if u:
            u.scrie()
    # indexurile: toate fișierele clasei, în afară de index.json și profesor.json
    for clasa in (5, 6, 7, 8):
        d = f"{ROOT}/clasa-{clasa}"
        if not os.path.isdir(d):
            continue
        fis = []
        for f in sorted(os.listdir(d)):
            if not f.endswith(".json") or f in ("index.json", "profesor.json"):
                continue
            c = json.load(open(f"{d}/{f}", encoding="utf-8"))
            fis.append({"fisier": f, "niveluri": [n["id"] for n in c["niveluri"]], "boss": [b["id"] for b in c.get("boss", [])]})
        json.dump({"clasa": clasa, "fisiere": fis}, open(f"{d}/index.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = sum(len(json.load(open(f"{d}/{x['fisier']}", encoding="utf-8"))["itemi"]) for x in fis)
        print(f"Clasa a {ROMAN[clasa]}-a: {len(fis)} fișiere, {n} itemi")


if __name__ == "__main__":
    main()
