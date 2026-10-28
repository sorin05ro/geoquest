"""Patrula Verde – evenimentul Săptămânii verzi (19–23.04.2027, activitatea are loc miercuri, 21.04.2027).

Clasele lucrează grupate: V + VII și VI + VIII. O activitate durează 1,5–2 ore.
Tehnologie disponibilă la școală: calculatoare, tabla interactivă, imprimanta 3D, drona.

Fișierul conține: itemii pentru jocul live (pe clase), planul atelierelor pentru profesor și regulile de siguranță.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_common import ROOT, alegere, denumeste, pin

N = "ev-patrula-verde"
S_FAO = ["FAO – International Year of Soils 2015: Soils are a non-renewable resource", "FAO – Healthy soils are the basis for healthy food production"]
S_UNEP = ["UNEP – Our planet is drowning in plastic pollution", "OECD – Global Plastics Outlook (2022)"]
S_N2000 = ["Agenția Europeană de Mediu (EEA) – Natura 2000 barometer", "Ministerul Mediului – Rețeaua Natura 2000 în România"]
S_BERCA = ["Euronews România – Buzău, județul vulcanilor noroioși", "Adevărul (ediția Buzău) – Vulcanii Noroioși"]
S_GEOPARC = ["UNESCO – Global Geoparks: Buzău Land (2022)", "Asociația Ținutul Buzăului (geoparc)"]
S_AACR = ["Autoritatea Aeronautică Civilă Română (AACR) – Drone: categoria deschisă", "Regulamentul de punere în aplicare (UE) 2019/947 – operarea dronelor"]
S_ZIUA = ["ONU – International Mother Earth Day, 22 aprilie", "Earth Day Network – History of Earth Day (1970)"]


def ev(x, clase):
    x["clase"] = clase
    return x


T = [5, 6, 7, 8]
itemi = [
    # ---------------- pentru toate clasele
    ev(alegere("G01", N, [], 1, "Ce zi a Pământului se sărbătorește în fiecare an pe 22 aprilie?", ["Ziua Pământului", "Ziua Apei", "Ziua Pădurii", "Ziua Mării Negre"],
               "Corect.", "Ziua Pământului se sărbătorește pe 22 aprilie, din 1970.", surse=S_ZIUA), T),
    ev(alegere("G02", N, [], 1, "În ce container se pune o sticlă de plastic goală?", ["galben (plastic și metal)", "verde (sticlă)", "albastru (hârtie)", "maro (biodegradabile)"],
               "Corect.", "Plasticul și metalul merg la galben."), T),
    ev(alegere("G03", N, [], 1, "În ce container se pune un borcan de sticlă?", ["verde", "galben", "albastru", "maro"],
               "Corect.", "Sticla merge la containerul verde."), T),
    ev(alegere("G04", N, [], 1, "Ce deșeu se poate pune la compost?", ["cojile de cartofi", "o baterie", "o pungă de plastic", "un bec"],
               "Corect.", "Resturile vegetale se descompun și devin îngrășământ."), T),
    ev(alegere("G05", N, [], 2, "Cât durează formarea unui strat de sol de 1 cm?", ["sute de ani, până la o mie de ani", "o zi", "o lună", "un an"],
               "Corect.", "De aceea solul trebuie protejat.", surse=S_FAO), T),
    ev(alegere("G06", N, [], 2, "Unde se duc bateriile uzate?", ["la punctele speciale de colectare", "la gunoiul menajer", "în compost", "în râu"],
               "Corect.", "Bateriile conțin metale toxice."), T),
    ev(pin("G07", N, [], 2, "Atinge pe hartă Râmnicu Sărat, orașul Patrulei Verzi.", "romania", 45.38, 27.05, "Râmnicu Sărat", 35,
           "Corect.", "Râmnicu Sărat e în nord-estul județului Buzău."), T),
    ev(pin("G08", N, [], 2, "Atinge pe hartă Vulcanii Noroioși de la Berca–Pâclele, rezervație naturală din județul Buzău.", "romania", 45.35, 26.7, "Vulcanii Noroioși", 35,
           "Corect.", "Sunt în Subcarpații Buzăului.", surse=S_BERCA), T),
    ev(alegere("G09", N, [], 2, "Ce geoparc recunoscut de UNESCO se află în județul Buzău?", ["Ținutul Buzăului", "Țara Hațegului", "Delta Dunării", "Munții Apuseni"],
               "Corect.", "Geoparcul Ținutul Buzăului e recunoscut de UNESCO din 2022.", surse=S_GEOPARC), T),
    ev(alegere("G10", N, [], 2, "Ce faci cu apa când te speli pe dinți?", ["închizi robinetul cât timp periezi", "lași robinetul deschis", "folosești apă caldă mereu", "umpli cada"],
               "Corect.", "Economisești mulți litri pe zi."), T),
    ev(alegere("G11", N, [], 2, "Ce plantă ajută cel mai mult albinele în curtea școlii?", ["florile locale, care înfloresc pe rând, din primăvară până toamna", "iarba tunsă foarte scurt", "gazonul artificial", "pietrișul"],
               "Corect.", "Florile locale dau hrană polenizatorilor."), T),
    ev(alegere("G12", N, [], 3, "De ce plasticul aruncat în râu e o problemă pentru mare?", ["râul îl duce în mare, unde se rupe în microplastice", "plasticul se dizolvă imediat", "plasticul devine nisip curat", "plasticul hrănește peștii"],
               "Corect.", "Microplasticele ajung în hrana animalelor.", surse=S_UNEP), T),
    # ---------------- clasa a V-a: geosfere și mediul apropiat
    ev(alegere("G20", N, ["V-3.3"], 1, "Ce faptă protejează hidrosfera?", ["nu arunci gunoaie în râu", "speli mașina în pârâu", "lași robinetul deschis", "arunci uleiul în chiuvetă"], "Corect.", "Apele curate depind de noi."), [5]),
    ev(alegere("G21", N, ["V-3.3"], 2, "Ce rol au rădăcinile copacilor pe o pantă?", ["țin solul și opresc eroziunea", "fac solul să alunece", "usucă râurile", "nu au rol"],
               "Corect.", "Pădurea apără solul."), [5]),
    ev(alegere("G22", N, ["V-4.3"], 2, "Ce poluează aerul din jurul școlii?", ["mașinile lăsate cu motorul pornit și arderea frunzelor", "copacii", "florile", "ploaia"],
               "Corect.", "Arderile poluează aerul."), [5]),
    ev(alegere("G23", N, ["V-1.1"], 2, "Cum se numește îngrășământul natural obținut din resturi de legume și frunze?", ["compost", "plastic", "nisip", "cărbune"], "Corect.", "Compostul îmbogățește solul."), [5]),
    # ---------------- clasa a VI-a: Europa și resursele
    ev(alegere("G30", N, ["VI-3.2"], 2, "Ce țară europeană e cunoscută pentru numărul mare de biciclete în orașe?", ["Țările de Jos", "Islanda", "Malta", "Albania"],
               "Corect.", "Amsterdam are mai multe biciclete decât locuitori."), [6]),
    ev(alegere("G31", N, ["VI-3.2"], 2, "Ce resursă regenerabilă folosește cel mai mult Norvegia pentru electricitate?", ["apa (hidrocentralele)", "cărbunele", "petrolul ars", "lemnul"],
               "Corect.", "Norvegia are munți și multă apă."), [6]),
    ev(alegere("G32", N, ["VI-4.3"], 2, "Ce înseamnă „dezvoltare durabilă”?", ["să folosim resursele fără să le stricăm pentru generațiile viitoare", "să consumăm cât mai repede", "să nu mai folosim nicio resursă", "să tăiem pădurile pentru case"],
               "Corect.", "Grija pentru viitor."), [6]),
    ev(alegere("G33", N, ["VI-3.2"], 2, "Care dintre aceste resurse este neregenerabilă?", ["petrolul", "vântul", "energia Soarelui", "apa râurilor"], "Corect.", "Petrolul s-a format în milioane de ani și se termină."), [6]),
    # ---------------- clasa a VII-a: mediul global
    ev(alegere("G40", N, ["VII-4.4"], 2, "Ce acord internațional din 2015 urmărește limitarea încălzirii globale?", ["Acordul de la Paris", "Tratatul Antarctic", "Protocolul de la Montreal", "Tratatul de la Roma"],
               "Corect.", "Ținta e mult sub 2 °C, încercând 1,5 °C."), [7]),
    ev(alegere("G41", N, ["VII-4.4"], 2, "Ce pădure tropicală e amenințată cel mai mult de defrișări?", ["pădurea amazoniană", "taigaua siberiană", "Pădurea Neagră", "pădurea Letea"],
               "Corect.", "Amazonia pierde suprafețe mari în fiecare an."), [7]),
    ev(denumeste("G42", N, ["VII-2.1"], 2, "Ce zonă, amenințată de deșertificare, e marcată pe hartă?", ["Sahelul", "Siberia", "Amazonia", "Alpii"],
                 "Corect.", "Sahelul e la sudul Saharei.", harta="lume", punct={"lat": 15, "lon": 5}), [7]),
    ev(alegere("G43", N, ["VII-4.4"], 3, "De ce gheața Antarcticii e importantă pentru tot Pământul?", ["topirea ei ar ridica mult nivelul oceanului", "ea încălzește oceanele", "nu are importanță", "produce petrol"],
               "Corect.", "Calota conține aproximativ 90 % din gheața lumii."), [7]),
    # ---------------- clasa a VIII-a: mediul României
    ev(alegere("G50", N, ["VIII-4.4"], 2, "Ce parte din teritoriul României e în rețeaua Natura 2000?", ["aproape un sfert", "aproape nimic", "toată țara", "jumătate exact"],
               "Corect.", "Situri pentru specii și habitate protejate.", surse=S_N2000), [8]),
    ev(alegere("G51", N, ["VIII-4.4"], 2, "Ce problemă de mediu e frecventă în Subcarpații Buzăului?", ["alunecările de teren, agravate de defrișări", "erupțiile de lavă", "tsunami-urile", "avalanșele de nisip"],
               "Corect.", "Pădurea și drenajul reduc riscul."), [8]),
    ev(alegere("G52", N, ["VIII-3.2"], 2, "Ce energie regenerabilă e cea mai potrivită pentru acoperișul școlii?", ["panourile solare", "o termocentrală pe cărbune", "o hidrocentrală", "un reactor nuclear"],
               "Corect.", "Panourile fotovoltaice pot reduce factura și emisiile."), [8]),
    ev(alegere("G53", N, ["VIII-4.4"], 3, "Ce soluție reduce alunecările de teren de pe o pantă de lângă un sat?", ["împădurirea și drenarea apei", "tăierea copacilor", "construirea de case pe pantă", "aratul de sus în jos"], "Corect.", "Pădurea și drenajul stabilizează versantul."), [8]),
]

# ---------------- planul atelierelor (pentru profesor)
plan = {
    "zi": "2027-04-21",
    "durata": "1,5–2 ore pentru fiecare grup",
    "grupe": [
        {"clase": [5, 7], "titlu": "Grupul 1: clasele a V-a și a VII-a"},
        {"clase": [6, 8], "titlu": "Grupul 2: clasele a VI-a și a VIII-a"},
    ],
    "ateliere": [
        {"titlu": "1. Jocul live „Patrula Verde”", "minute": 20, "tehnologie": ["tabla interactivă", "telefoanele elevilor sau calculatoarele"],
         "descriere": "Porniți jocul live cu clasele grupate. La fiecare răspuns corect, în pădurea colectivă de pe tablă mai crește un copac.",
         "rezultat": "Pădurea colectivă a grupului."},
        {"titlu": "2. Misiunea dronei: harta verde a școlii", "minute": 30, "tehnologie": ["drona (pilotată doar de profesor)", "calculatoarele"],
         "descriere": "Profesorul face fotografii verticale ale curții, de la înălțime mică. Elevii identifică pe fotografii: zone verzi, zone betonate, locuri cu deșeuri, copaci. Pe calculator, desenează pe imagine (sau pe hârtie de calc pe tablă) zonele și estimează, cu un caroiaj, ce parte din curte e verde.",
         "rezultat": "Harta verde a școlii, cu procentul de spațiu verde.",
         "siguranta": ["Drona e pilotată doar de un adult instruit, în condițiile AACR pentru categoria deschisă.", "Zborul se face doar deasupra curții școlii, cu elevii în afara zonei de zbor.", "Nu se fotografiază persoane; fotografiile nu se publică fără acordul direcțiunii.", "Nu se zboară pe vânt puternic sau ploaie."]},
        {"titlu": "3. Imprimanta 3D: etichete pentru copaci și plante", "minute": 30, "tehnologie": ["imprimanta 3D", "calculatoarele"],
         "descriere": "Elevii scriu pe calculator textul etichetelor (numele plantei, rolul ei: umbră, hrană pentru albine, protecția solului). Profesorul tipărește 3D etichete simple, din PLA, pentru copacii și plantele din curte. Cei mari (VII, VIII) pot proiecta forma etichetei într-un program gratuit de modelare 3D.",
         "rezultat": "Etichete montate pe plantele din curtea școlii."},
        {"titlu": "4. Patrula în teren", "minute": 25, "tehnologie": ["mănuși", "saci de gunoi pe culori", "telefonul profesorului pentru fotografii"],
         "descriere": "Elevii strâng deșeurile din curte (cu mănuși), le sortează pe culori și le cântăresc. Montează etichetele tipărite. Notează în Jurnalul exploratorului ce au găsit.",
         "rezultat": "Kilograme de deșeuri colectate, pe tipuri."},
        {"titlu": "5. Concluzii și angajamentul clasei", "minute": 15, "tehnologie": ["tabla interactivă"],
         "descriere": "Pe tablă: harta verde, pădurea colectivă și cantitatea de deșeuri. Fiecare grup scrie un angajament pentru restul anului (de exemplu, un colț pentru albine sau o zi fără mașini lângă școală).",
         "rezultat": "Angajamentul Patrulei Verzi, afișat în clasă."},
    ],
    "pentruGrupe": {
        "5-7": "Cei de-a V-a lucrează pe geosfere (aer, apă, sol, viețuitoare); cei de-a VII-a explică legătura cu problemele globale (defrișări, deșertificare, schimbări climatice). În ateliere, perechile se fac dintr-un elev de-a V-a și unul de-a VII-a.",
        "6-8": "Cei de-a VI-a lucrează pe resurse și dezvoltare durabilă în Europa; cei de-a VIII-a pe problemele de mediu ale României și ale județului Buzău. Elevii de-a VIII-a conduc echipele mixte la harta dronei.",
    },
    "surse": S_AACR,
}

out = {"id": "patrula-verde", "nume": "Patrula Verde", "eveniment": "saptamana-verde", "plan": plan, "itemi": itemi}
os.makedirs(f"{ROOT}/evenimente", exist_ok=True)
json.dump(out, open(f"{ROOT}/evenimente/patrula-verde.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"Patrula Verde: {len(itemi)} itemi, {len(plan['ateliere'])} ateliere")
