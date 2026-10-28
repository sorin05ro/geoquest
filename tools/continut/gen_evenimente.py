"""Expediția Polară – evenimentul de Școala Altfel (16–22.12.2026). Itemi pentru jocul live, pe clase."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_common import ROOT, alegere, denumeste, pin

N = "ev-expeditia-polara"
S_ICE = ["ESA – Antarctica (2019): calota conține aproximativ 90 % din gheața lumii", "LEARNZ – Antarctic Ice: peste 90 % din gheața lumii"]
S_AMUNDSEN = ["Guinness World Records – First person to reach the South Pole", "Scientific American – Amundsen Becomes First to Reach South Pole, December 14, 1911"]
S_RACOVITA = ["Wikipedia – Emil Racoviță (expediția Belgica, 1897–1899)", "Agerpres, 13.05.2025 – expoziția despre expediția antarctică Belgica 1897–1899"]
S_BUCURA = ["Wikipedia – Bucura Lake (cel mai mare lac glaciar din România)", "Adevărul – „cel mai întins lac glaciar din România”"]

def ev(x, clase):
    x["clase"] = clase
    return x

T = [5, 6, 7, 8]
itemi = [
 # ---------------- pentru toate clasele
 ev(pin("P01", N, [], 1, "Atinge pe hartă Polul Sud.", "lume", -89.5, 0, "Polul Sud", 1200, "Corect: e în mijlocul Antarcticii.", "Polul Sud e în marginea de jos a hărții, în Antarctica."), T),
 ev(alegere("P02", N, [], 1, "Ce continent este acoperit aproape în întregime de gheață?", ["Antarctica", "Europa", "Australia", "Africa"],
   "Corect.", "Antarctica e acoperită aproape în întregime de o calotă de gheață.", surse=S_ICE), T),
 ev(alegere("P03", N, [], 2, "Ce parte din gheața lumii se află în Antarctica?", ["aproximativ 90 %", "aproximativ 10 %", "aproximativ jumătate", "aproximativ un sfert"],
   "Corect: în jur de 90 %.", "Calota Antarcticii conține aproximativ 90 % din gheața lumii.", surse=S_ICE), T),
 ev(alegere("P04", N, [], 1, "Pe ce continent trăiesc pinguinii imperiali?", ["Antarctica", "Europa", "America de Nord", "Asia"],
   "Corect.", "Pinguinii imperiali trăiesc doar în Antarctica și în apele din jurul ei."), T),
 ev(alegere("P05", N, [], 1, "Unde trăiesc urșii polari?", ["în regiunea arctică, în jurul Polului Nord", "în Antarctica", "în Sahara", "în pădurea amazoniană"],
   "Corect.", "Urșii polari trăiesc în Arctica. În Antarctica nu există urși polari."), T),
 ev(alegere("P06", N, [], 2, "Prin ce se deosebește Arctica de Antarctica?",
   ["Arctica e un ocean înghețat înconjurat de uscat; Antarctica e un continent acoperit de gheață", "Arctica e un continent; Antarctica e un ocean", "sunt același loc", "Arctica e în emisfera sudică"],
   "Corect.", "În nord e Oceanul Arctic, înghețat, înconjurat de continente. În sud e un continent: Antarctica."), T),
 ev(alegere("P07", N, [], 2, "Cine a ajuns primul la Polul Sud, în decembrie 1911?", ["Roald Amundsen", "Cristofor Columb", "Emil Racoviță", "Ferdinand Magellan"],
   "Corect: norvegianul Roald Amundsen, pe 14 decembrie 1911.", "Primul om la Polul Sud a fost norvegianul Roald Amundsen, pe 14 decembrie 1911.", surse=S_AMUNDSEN), T),
 ev(alegere("P08", N, [], 2, "Ce savant român a participat la expediția Belgica (1897–1899), în Antarctica?", ["Emil Racoviță", "Grigore Antipa", "Simion Mehedinți", "Nicolae Iorga"],
   "Corect: biologul Emil Racoviță.", "Emil Racoviță a fost biologul expediției Belgica, condusă de belgianul Adrien de Gerlache.", surse=S_RACOVITA), T),
 ev(pin("P09", N, [], 2, "Atinge pe hartă Groenlanda, insula acoperită în mare parte de gheață.", "lume", 72, -40, "Groenlanda", 900,
   "Corect.", "Groenlanda e în nordul Oceanului Atlantic, la nord-est de America de Nord."), T),
 # ---------------- clasa a V-a: ghețarii și zona rece
 ev(alegere("P10", N, ["V-1.1"], 1, "Cum se numește un bloc mare de gheață desprins dintr-un ghețar, care plutește pe mare?", ["aisberg", "dună", "atol", "fiord"],
   "Corect.", "Blocurile de gheață care plutesc pe mare se numesc aisberguri."), [5]),
 ev(alegere("P11", N, ["V-1.2"], 2, "Gheața ghețarilor și a aisbergurilor este formată din apă...", ["dulce", "sărată", "de mare", "minerală"],
   "Corect.", "Ghețarii se formează din zăpadă tasată, deci gheața lor e de apă dulce."), [5]),
 ev(alegere("P12", N, ["V-3.2"], 2, "Ce este ziua polară?", ["perioada în care Soarele nu apune deloc, zile la rând", "o zi foarte rece de iarnă", "ziua în care se topește gheața", "noaptea cu aurore"],
   "Corect.", "În regiunile polare, vara, Soarele rămâne deasupra orizontului zile sau luni la rând."), [5]),
 ev(denumeste("P13", N, ["V-2.1"], 1, "Cum se numește continentul marcat pe hartă?", ["Antarctica", "Australia", "Africa", "America de Sud"],
   "Corect.", "Continentul de la Polul Sud e Antarctica.", harta="lume", punct={"lat": -80, "lon": 30}), [5]),
 # ---------------- clasa a VI-a: nordul Europei
 ev(alegere("P14", N, ["VI-2.1"], 2, "Care dintre aceste țări are teritoriu la nord de Cercul Polar de Nord?", ["Norvegia", "Italia", "Grecia", "Portugalia"],
   "Corect.", "Nordul Norvegiei (ca și al Suediei și Finlandei) trece de Cercul Polar de Nord."), [6]),
 ev(pin("P15", N, ["VI-2.1"], 2, "Atinge pe hartă Islanda, țara insulară cu vulcani și ghețari.", "lume", 64.9, -18.6, "Islanda", 500,
   "Corect.", "Islanda e în nordul Oceanului Atlantic, între Groenlanda și Norvegia."), [6]),
 ev(alegere("P16", N, ["VI-3.3"], 2, "Ce popor din nordul Scandinaviei crește în mod tradițional reni?", ["samii", "bascii", "bretonii", "tirolezii"],
   "Corect.", "Samii trăiesc în nordul Norvegiei, Suediei, Finlandei și Rusiei; mulți cresc reni."), [6]),
 ev(alegere("P17", N, ["VI-1.1"], 2, "Cum se numesc golfurile lungi și înguste, cu maluri abrupte, săpate de ghețari pe țărmul Norvegiei?", ["fiorduri", "delte", "lagune", "estuare"],
   "Corect.", "Fiordurile sunt văi glaciare inundate de mare."), [6]),
 # ---------------- clasa a VII-a: Antarctica
 ev(alegere("P18", N, ["VII-3.3"], 2, "Ce animale trăiesc pe țărmurile Antarcticii?", ["pinguini și foci", "urși polari și reni", "lei și zebre", "cămile și scorpioni"],
   "Corect.", "Pe țărmurile Antarcticii trăiesc pinguini și foci; urșii polari și renii sunt în nord."), [7]),
 ev(alegere("P19", N, ["VII-4.4"], 3, "Pentru ce este folosită Antarctica, conform tratatului internațional semnat de mai multe țări?", ["pentru cercetare științifică pașnică", "pentru baze militare", "pentru minerit", "pentru orașe noi"],
   "Corect.", "Tratatul asupra Antarcticii o rezervă cercetării științifice și scopurilor pașnice."), [7]),
 ev(alegere("P20", N, ["VII-2.1"], 2, "În ce emisferă se află Antarctica?", ["în emisfera sudică", "în emisfera nordică", "pe Ecuator", "jumătate în nord, jumătate în sud"],
   "Corect.", "Antarctica e în jurul Polului Sud, deci în emisfera sudică."), [7]),
 # ---------------- clasa a VIII-a: urmele ghețarilor în Carpați
 ev(alegere("P21", N, ["VIII-1.1"], 2, "Care este cel mai întins lac glaciar din România?", ["Lacul Bucura", "Lacul Sfânta Ana", "Lacul Razim", "Lacul Snagov"],
   "Corect: Bucura, în Munții Retezat.", "Lacul Bucura, din Munții Retezat, e cel mai întins lac glaciar din România.", surse=S_BUCURA), [8]),
 ev(pin("P22", N, ["VIII-2.1"], 2, "Atinge pe hartă Munții Retezat, unde se află Lacul Bucura.", "romania", 45.36, 22.88, "Munții Retezat", 50,
   "Corect.", "Munții Retezat sunt în vestul Carpaților Meridionali."), [8]),
 ev(alegere("P23", N, ["VIII-2.2"], 2, "Ce forme de relief au lăsat ghețarii de altădată în munții înalți ai României?", ["circuri (căldări) și văi glaciare", "dune de nisip", "delte", "vulcani noroioși"],
   "Corect.", "Ghețarii au săpat circuri glaciare (căldări), în care s-au format lacuri, și văi glaciare."), [8]),
 ev(alegere("P24", N, ["VIII-3.1"], 3, "De ce nu mai există ghețari în Carpați astăzi?", ["clima s-a încălzit după ultima glaciațiune", "munții au devenit mai înalți", "a crescut nivelul mării", "ghețarii au fost topiți de oameni"],
   "Corect.", "Ghețarii din Carpați s-au topit când clima s-a încălzit, după ultima glaciațiune."), [8]),
]

os.makedirs(f"{ROOT}/evenimente", exist_ok=True)
json.dump({"id": "expeditia-polara", "nume": "Expediția Polară", "eveniment": "scoala-altfel", "itemi": itemi},
          open(f"{ROOT}/evenimente/expeditia-polara.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(itemi), "itemi pentru Expediția Polară")
