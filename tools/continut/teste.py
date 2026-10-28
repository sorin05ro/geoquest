"""Testele fiecărei clase: Busola de start (T₀, recapitularea anului trecut), Boss-urile T₁–T₅ și Marea Expediție (Tf).

Boss-urile iau itemi din lecțiile unității, după calendar: toate lecțiile de după testul anterior, până la săptămâna testului.
"""
import json
import os
from autor import Lectie, Unitate, ROMAN

CAL = json.load(open(os.path.join(os.path.dirname(__file__), "..", "..", "public", "calendar", "2026-2027.json"), encoding="utf-8"))
TITLURI = {"T1": "Boss T₁", "T2": "Boss T₂", "T3": "Boss T₃", "T4": "Boss T₄", "T5": "Boss T₅"}


def busola(clasa):
    R = ROMAN[clasa]
    B = Lectie(clasa, f"{R}-T0", "Busola de start", "Ce îți amintești de anul trecut?",
               [("Busola de start", "Câteva întrebări din ce ai învățat anul trecut. Nu primești notă: rezultatul alege cât de grele vor fi exercițiile tale la început.")],
               prefix=f"{R}T0")
    if clasa == 5:
        # recapitulare: geografia României din clasa a IV-a
        B.a(1, "1.1", "Care este capitala României?", "București", ["Cluj-Napoca", "Iași", "Buzău"], "Capitala României e Bucureștiul.")
        B.p(1, "2.1", "Atinge pe hartă Bucureștiul.", "romania", 44.43, 26.10, "București", 40, "Bucureștiul e în sudul țării, în Câmpia Română.")
        B.a(1, "2.1", "Ce mare scaldă țărmul de est al României?", "Marea Neagră", ["Marea Mediterană", "Marea Baltică", "Marea Roșie"], "La est, România are ieșire la Marea Neagră.")
        B.a(1, "2.1", "Ce fluviu formează o mare parte din granița de sud a României?", "Dunărea", ["Mureșul", "Oltul", "Prutul"], "Dunărea curge în sudul țării, pe granița cu Serbia și Bulgaria.")
        B.a(2, "2.1", "Ce munți străbat România ca un arc?", "Carpații", ["Alpii", "Himalaya", "Balcanii"], "Carpații formează un arc prin mijlocul țării.")
        B.a(1, "2.1", "Pe ce continent se află România?", "Europa", ["Asia", "Africa", "America de Nord"], "România e în sud-estul Europei Centrale.")
        B.a(2, "1.1", "În ce județ se află orașul nostru, Râmnicu Sărat?", "Buzău", ["Vrancea", "Brăila", "Prahova"], "Râmnicu Sărat e în județul Buzău.")
        B.a(2, "2.1", "Ce unitate de relief se află acolo unde Dunărea se varsă în Marea Neagră?", "Delta Dunării", ["Câmpia de Vest", "Munții Apuseni", "Podișul Moldovei"], "Delta Dunării e la vărsarea fluviului în mare.")
        B.o(1, "4.2", "Ordonează formele de relief de la cea mai înaltă la cea mai joasă.", ["munții", "dealurile", "câmpiile"], "De la înalt la jos", "Munții sunt cei mai înalți, câmpiile cele mai joase.")
        B.a(2, "2.1", "Cu ce țară se învecinează România la sud, peste Dunăre?", "Bulgaria", ["Ungaria", "Ucraina", "Republica Moldova"], "La sud, peste Dunăre, e Bulgaria.")
        B.l(1, "1.1", "Completează.", "Soarele răsare la [est] și apune la [vest].", ["nord", "sud"], "Soarele răsare în partea de est și apune în partea de vest.")
        B.a(2, "2.1", "Ce râu formează granița cu Republica Moldova?", "Prutul", ["Siretul", "Oltul", "Jiul"], "Prutul curge pe granița de est, cu Republica Moldova.")
        B.p(2, "2.1", "Atinge pe hartă Marea Neagră.", "romania", 44.0, 30.0, "Marea Neagră", 120, "Marea Neagră e în estul țării, la est de Dobrogea.")
        B.a(1, "1.1", "Cum se numește desenul micșorat al unui teritoriu, văzut de sus?", "harta", ["fotografia", "globul", "busola"], "Harta reprezintă micșorat un teritoriu, văzut de sus.")
        B.a(2, "1.1", "Ce anotimp urmează după iarnă?", "primăvara", ["vara", "toamna", "iarna"], "Ordinea anotimpurilor: primăvara, vara, toamna, iarna.")
    elif clasa == 6:
        B.s(1, "1.1", "Asociază geosfera cu ce cuprinde.", [("litosfera", "rocile"), ("atmosfera", "aerul"), ("hidrosfera", "apa"), ("biosfera", "viețuitoarele")], "Lito = piatră, atmo = aer, hidro = apă, bio = viață.")
        B.o(1, "1.1", "Ordonează straturile Pământului de la suprafață spre centru.", ["scoarța", "mantaua", "nucleul extern", "nucleul intern"], "Spre centru", "Scoarța, mantaua, nucleul extern, nucleul intern.")
        B.a(1, "1.1", "Ce mișcare a Pământului produce ziua și noaptea?", "rotația", ["revoluția", "eclipsa", "mareea"], "Rotația în jurul axei dă ziua și noaptea.")
        B.a(2, "2.1", "Ce paralelă împarte Pământul în emisfera nordică și sudică?", "Ecuatorul", ["Tropicul Racului", "Cercul Polar de Nord", "meridianul Greenwich"], "Ecuatorul are latitudinea 0°.")
        B.a(2, "2.1", "Prin ce oraș trece meridianul de 0° (de origine)?", "Greenwich (Londra)", ["Paris", "București", "New York"], "Meridianul de origine trece prin Greenwich, lângă Londra.")
        B.p(1, "2.1", "Atinge pe hartă Oceanul Pacific.", "lume", 0, -150, "Oceanul Pacific", 4500, "Pacificul e cel mai mare ocean.")
        B.p(2, "2.1", "Atinge pe hartă Africa.", "lume", 5, 20, "Africa", 1800, "Africa e la sud de Europa.")
        B.a(2, "1.1", "Cum se numește magma ajunsă la suprafață?", "lavă", ["cenușă", "rocă sedimentară", "nor"], "Magma ieșită la suprafață se numește lavă.")
        B.a(2, "1.1", "Care este cel mai mare ocean?", "Pacific", ["Atlantic", "Indian", "Arctic"], "Pacificul e cel mai mare ocean.")
        B.a(2, "3.3", "Ce zonă de vegetație e tipică pentru zona caldă, umedă, de lângă Ecuator?", "pădurea ecuatorială", ["tundra", "taigaua", "stepa"], "La Ecuator, căldura și ploile dau pădurea ecuatorială.")
        B.a(1, "1.1", "Cu ce aparat măsurăm temperatura aerului?", "termometrul", ["barometrul", "pluviometrul", "busola"], "Termometrul măsoară temperatura.")
        B.a(2, "1.1", "Ce sunt ghețarii?", "mase mari de gheață care se mișcă încet", ["lacuri înghețate iarna", "nori de gheață", "ape subterane"], "Ghețarii sunt mase de gheață formate din zăpadă tasată, care se deplasează lent.")
        B.l(2, "1.1", "Completează.", "Locul din adânc unde se produce un cutremur se numește [hipocentru], iar punctul de deasupra lui, la suprafață, [epicentru].", ["crater"], "Hipocentrul e în adânc, epicentrul la suprafață.")
        B.a(2, "3.2", "De ce avem anotimpuri?", "axa Pământului e înclinată, iar Pământul se rotește în jurul Soarelui", ["Pământul se apropie și se depărtează de Lună", "Soarele se stinge iarna", "norii acoperă Soarele"], "Înclinarea axei și revoluția schimbă unghiul razelor de-a lungul anului.")
        B.a(1, "1.1", "Ce este un râu?", "o apă curgătoare care pornește de la izvor și se varsă într-un alt râu, lac sau mare", ["o apă stătătoare", "un ghețar", "un val de mare"], "Râul curge de la izvor până la gura de vărsare.")
    elif clasa == 7:
        B.a(1, "2.1", "Care este capitala Franței?", "Paris", ["Lyon", "Bruxelles", "Roma"], "Capitala Franței e Parisul.")
        B.p(2, "2.1", "Atinge pe hartă Munții Alpi.", "lume", 46.5, 10, "Munții Alpi", 600, "Alpii sunt în centrul Europei (Franța, Italia, Elveția, Austria).")
        B.a(2, "2.1", "Ce fluviu trece prin mai multe capitale europene, printre care Viena, Budapesta și Belgrad?", "Dunărea", ["Rinul", "Volga", "Sena"], "Dunărea trece prin Viena, Bratislava, Budapesta și Belgrad.")
        B.a(2, "2.1", "Care este cel mai lung fluviu din Europa?", "Volga", ["Dunărea", "Rinul", "Nistrul"], "Volga, din Rusia, e cel mai lung fluviu european.")
        B.a(1, "1.1", "Ce înseamnă UE?", "Uniunea Europeană", ["Unitatea Economică", "Uniunea Estică", "Universitatea Europeană"], "UE = Uniunea Europeană, din care face parte și România.")
        B.a(2, "1.1", "Ce este densitatea populației?", "numărul de locuitori pe un kilometru pătrat", ["numărul de orașe dintr-o țară", "numărul de copii dintr-o familie", "înălțimea clădirilor"], "Densitatea = locuitori / km².")
        B.a(2, "2.1", "Ce peninsulă cuprinde Spania și Portugalia?", "Peninsula Iberică", ["Peninsula Italică", "Peninsula Scandinavă", "Peninsula Balcanică"], "Spania și Portugalia sunt în Peninsula Iberică.")
        B.p(2, "2.1", "Atinge pe hartă Peninsula Scandinavă.", "lume", 63, 15, "Peninsula Scandinavă", 700, "Peninsula Scandinavă e în nordul Europei (Norvegia, Suedia).")
        B.a(2, "1.1", "Ce sunt resursele naturale regenerabile?", "resurse care se refac, ca energia Soarelui, vântul, apa", ["resurse care se termină, ca petrolul", "fabricile", "orașele"], "Regenerabile: Soare, vânt, apă. Neregenerabile: petrol, cărbune, gaze.")
        B.a(2, "2.1", "Ce mare desparte Europa de Africa?", "Marea Mediterană", ["Marea Nordului", "Marea Baltică", "Marea Neagră"], "Mediterana e între sudul Europei și nordul Africii.")
        B.a(2, "1.1", "Care sector al economiei cuprinde comerțul, transporturile și turismul?", "serviciile", ["agricultura", "industria", "mineritul"], "Comerțul, transporturile, turismul, educația, sănătatea sunt servicii.")
        B.a(1, "2.1", "Care este capitala Italiei?", "Roma", ["Milano", "Veneția", "Napoli"], "Capitala Italiei e Roma.")
        B.a(2, "2.1", "Ce munți separă Europa de Asia, în Rusia?", "Munții Ural", ["Munții Carpați", "Munții Alpi", "Munții Pirinei"], "Limita convențională dintre Europa și Asia trece pe Munții Ural.")
        B.a(2, "3.3", "Ce zonă de vegetație acoperă nordul Rusiei și al Scandinaviei, cu păduri de conifere?", "taigaua", ["stepa", "savana", "pădurea ecuatorială"], "Taigaua e pădurea de conifere a zonei reci-temperate.")
        B.a(1, "2.1", "Care este capitala Germaniei?", "Berlin", ["München", "Hamburg", "Viena"], "Capitala Germaniei e Berlinul.")
    else:
        B.p(1, "2.1", "Atinge pe hartă Munții Himalaya.", "lume", 28, 85, "Munții Himalaya", 900, "Himalaya e în Asia, la nord de India.")
        B.a(1, "2.1", "Pe ce continent se află deșertul Sahara?", "Africa", ["Asia", "Australia", "America de Sud"], "Sahara e în nordul Africii.")
        B.a(2, "2.1", "Ce fluviu are cel mai mare debit din lume și curge prin pădurea ecuatorială din America de Sud?", "Amazonul", ["Nilul", "Mississippi", "Gangele"], "Amazonul are cel mai mare debit din lume.")
        B.a(2, "2.1", "Ce munți străbat vestul Americii de Sud, de la nord la sud?", "Munții Anzi", ["Munții Stâncoși", "Munții Atlas", "Munții Ural"], "Anzii sunt partea sudică a sistemului cordiliero-andin.")
        B.p(2, "2.1", "Atinge pe hartă Australia.", "lume", -25, 134, "Australia", 1200, "Australia e în emisfera sudică, între Oceanul Indian și Pacific.")
        B.a(1, "1.1", "Ce sunt musonii?", "vânturi care își schimbă direcția de la vară la iarnă și aduc ploi abundente vara", ["vulcani", "râuri subterane", "deșerturi"], "Musonii sunt specifici sudului și estului Asiei.")
        B.a(2, "2.1", "Ce fluviu traversează Egiptul și se varsă în Marea Mediterană?", "Nilul", ["Congo", "Niger", "Zambezi"], "Nilul curge prin Egipt și formează o deltă la Mediterana.")
        B.a(2, "1.1", "Care este cel mai populat continent?", "Asia", ["Africa", "Europa", "America de Nord"], "Asia are mai mult de jumătate din populația lumii.")
        B.a(2, "3.3", "Ce animal e simbolul unicității faunei australiene?", "cangurul", ["elefantul", "tigrul", "ursul polar"], "Marsupialele, ca cangurul și koala, trăiesc mai ales în Australia.")
        B.a(1, "2.1", "Pe ce continent se află Polul Sud?", "Antarctica", ["Australia", "America de Sud", "Africa"], "Polul Sud e în mijlocul Antarcticii.")
        B.a(2, "2.1", "Ce strâmtoare desparte Asia de America de Nord?", "Strâmtoarea Bering", ["Strâmtoarea Gibraltar", "Canalul Suez", "Canalul Panama"], "Strâmtoarea Bering e între Rusia (Asia) și Alaska (America de Nord).")
        B.a(2, "1.1", "Ce este riftul african?", "un șir de fracturi ale scoarței în estul Africii, cu lacuri și vulcani", ["un deșert", "un fluviu", "o pădure"], "Riftul est-african e o zonă în care scoarța se rupe, cu lacuri adânci și vulcani.")
        B.a(2, "2.1", "Ce canal leagă Oceanul Atlantic de Oceanul Pacific prin America Centrală?", "Canalul Panama", ["Canalul Suez", "Canalul Dunăre–Marea Neagră", "Canalul Mânecii"], "Canalul Panama scurtează drumul navelor dintre Atlantic și Pacific.")
        B.a(1, "2.1", "Care este capitala Japoniei?", "Tokyo", ["Beijing", "Seul", "Osaka"], "Capitala Japoniei e Tokyo.")
        B.a(2, "4.4", "Ce problemă de mediu afectează pădurea amazoniană?", "defrișarea", ["înghețul", "cutremurele", "aisbergurile"], "Defrișările reduc pădurea amazoniană și biodiversitatea.")
    return B


def unitate(clasa):
    R = ROMAN[clasa]
    niv = [n for n in CAL["niveluri"] if n["clasa"] == clasa]
    randuri = sorted([p for p in CAL["planificare"] if p["clasa"] == clasa and p.get("test")], key=lambda p: p["saptamana"])
    boss = []
    anterior = 0
    for p in randuri:
        t = p["test"]
        if t == "Tf":
            ids = [n["id"] for n in niv]
            boss.append({"id": f"{R}-Tf", "test": "Tf", "titlu": "Marea Expediție: toată lumea ta", "saptamana": p["saptamana"], "niveluri": ids})
        else:
            ids = [n["id"] for n in niv if anterior < n["saptamana"] <= p["saptamana"]]
            boss.append({"id": f"{R}-{t}", "test": t, "titlu": f"{TITLURI[t]}: {p['unitate']}", "saptamana": p["saptamana"], "niveluri": ids})
            anterior = p["saptamana"]
    B = busola(clasa)
    boss.insert(0, {"id": f"{R}-T0", "test": "T0", "titlu": "Busola de start", "saptamana": 1, "niveluri": [f"{R}-T0"]})
    u = Unitate(clasa, "teste.json", "Teste: Busola de start, Boss-uri, Marea Expediție").add(B)
    u.boss = boss
    return u
