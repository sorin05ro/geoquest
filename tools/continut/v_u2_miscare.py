from autor import Lectie, Unitate, existent, grafic

REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"
NASA = ["NASA – Earth Fact Sheet (nssdc.gsfc.nasa.gov)", "Wikipedia – Axial tilt / Earth's rotation"]


def unitate():
    # ================================================================ S5 Globul, harta, coordonatele
    G = Lectie(5, "V-S05-globul-geografic-harta-coordonate", "Globul geografic și harta. Coordonate geografice",
               "Cum poți spune unui prieten din altă țară exact unde te afli, fără adresă?",
               [("Globul și harta", "Globul geografic e un model micșorat al Pământului, cu forma lui sferică. Harta e o reprezentare micșorată și plană a unui teritoriu, văzut de sus.\nOrice hartă are: titlu, legendă (explică semnele convenționale), scară de proporție și orientare (nordul, de obicei sus)."),
                ("Rețeaua de paralele și meridiane", "Paralelele sunt cercuri imaginare paralele cu Ecuatorul. Meridianele sunt semicercuri care unesc cei doi poli. Meridianul de origine (0°) trece prin Greenwich, lângă Londra.\nLatitudinea arată cât de departe e un loc de Ecuator, spre nord sau spre sud (0°–90°). Longitudinea arată cât de departe e un loc de meridianul de origine, spre est sau spre vest (0°–180°). Împreună sunt coordonatele geografice."),
                ("Scara de proporție", "Scara arată de câte ori a fost micșorat terenul. La scara 1:100 000, 1 cm pe hartă înseamnă 100 000 cm = 1 km în realitate.\nScara poate fi numerică (1:100 000) sau grafică (o riglă desenată pe hartă).")],
               stiaica="Un loc de pe Ecuator, la longitudinea 0°, se află în Golful Guineei, în Oceanul Atlantic. Uneori e numit în glumă „Insula Nimănui”.",
               ref=REF.format("Globul geografic și harta. Coordonate geografice"))
    G.a(1, "1.1", "Ce este globul geografic?", "un model micșorat al Pământului, de formă sferică", ["o hartă a orașului", "un instrument de orientare", "o fotografie din satelit"], "Globul păstrează forma sferică a Pământului.")
    G.a(1, "1.1", "Ce este harta?", "o reprezentare micșorată și plană a unui teritoriu, văzut de sus", ["o fotografie făcută de pe stradă", "un model sferic", "un tabel cu date"], "Harta e plană și micșorată; globul e sferic.")
    G.s(1, "1.1 2.3", "Asociază elementul hărții cu rolul lui.", [("titlul", "spune ce arată harta"), ("legenda", "explică semnele convenționale"), ("scara", "arată de câte ori e micșorat terenul"), ("săgeata nordului", "arată orientarea")], "Titlu, legendă, scară, orientare: elementele obligatorii ale hărții.")
    G.a(1, "1.1", "Ce sunt paralelele?", "cercuri imaginare paralele cu Ecuatorul", ["semicercuri de la un pol la altul", "râuri", "granițe între țări"], "Paralelele sunt paralele cu Ecuatorul; meridianele unesc polii.")
    G.a(1, "1.1", "Ce sunt meridianele?", "semicercuri imaginare care unesc Polul Nord cu Polul Sud", ["cercuri paralele cu Ecuatorul", "linii de-a lungul țărmurilor", "drumuri pe hartă"], "Meridianele merg de la un pol la altul.")
    G.a(2, "2.1", "Prin ce localitate trece meridianul de origine (0°)?", "Greenwich, lângă Londra", ["Paris", "București", "Roma"], "Meridianul de origine trece prin observatorul de la Greenwich.")
    G.l(2, "1.1 2.1", "Completează.", "Latitudinea se măsoară de la [Ecuator] spre nord sau spre sud, iar longitudinea de la meridianul de [origine] spre est sau spre vest.", ["Polul Nord", "schimbare"], "Latitudinea pornește de la Ecuator, longitudinea de la meridianul de 0°.")
    G.a(2, "2.1", "Între ce valori poate fi latitudinea?", "0° și 90° (nordică sau sudică)", ["0° și 180°", "0° și 360°", "0° și 45°"], "Latitudinea maximă e 90°, la poli.")
    G.a(2, "2.1", "Între ce valori poate fi longitudinea?", "0° și 180° (estică sau vestică)", ["0° și 90°", "0° și 360°", "0° și 60°"], "Longitudinea merge până la 180° spre est sau spre vest.")
    G.p(2, "2.1", "Atinge punctul cu coordonatele 0° latitudine, 0° longitudine.", "lume", 0, 0, "0°, 0° (Golful Guineei)", 700, "Punctul 0°, 0° e la intersecția Ecuatorului cu meridianul de origine, în Golful Guineei.", ind="Caută unde se întâlnește Ecuatorul cu meridianul care trece prin Londra.")
    G.p(3, "2.1", "Atinge punctul cu coordonatele 45° latitudine nordică, 25° longitudine estică.", "lume", 45, 25, "45° N, 25° E (România)", 500, "Punctul 45° N, 25° E se află în România: paralela de 45° și meridianul de 25° trec prin țara noastră.")
    G.p(2, "2.1", "Atinge pe hartă Greenwich (Londra), prin care trece meridianul de origine.", "lume", 51.48, 0, "Greenwich", 500, "Greenwich e în sud-estul Angliei, lângă Londra.")
    G.a(1, "2.2", "Ce arată scara de proporție?", "de câte ori a fost micșorat terenul pe hartă", ["înălțimea munților", "temperatura", "direcția nordului"], "Scara arată raportul dintre distanța de pe hartă și cea reală.")
    G.a(2, "2.2 3.1", "La scara 1:100 000, cât înseamnă în realitate 1 cm de pe hartă?", "1 km", ["100 m", "10 km", "100 km"], "100 000 cm = 1 000 m = 1 km.", ind="Transformă 100 000 cm în metri, apoi în kilometri.")
    G.a(2, "2.2 3.1", "La scara 1:100 000, două sate sunt la 5 cm pe hartă. Ce distanță e între ele în realitate?", "5 km", ["500 m", "50 km", "0,5 km"], "1 cm = 1 km, deci 5 cm = 5 km.")
    G.a(3, "2.2 3.1", "La scara 1:50 000, distanța pe hartă e 4 cm. Cât e în realitate?", "2 km", ["20 km", "200 m", "4 km"], "1 cm = 50 000 cm = 500 m; 4 × 500 m = 2 000 m = 2 km.")
    G.a(3, "2.2 3.1", "Două orașe sunt la 30 km. Pe o hartă la scara 1:1 000 000, la ce distanță apar?", "3 cm", ["30 cm", "0,3 cm", "300 cm"], "1 cm = 1 000 000 cm = 10 km; 30 km : 10 km = 3 cm.")
    G.a(2, "2.2", "Ce hartă are scara cea mai mare (arată cele mai multe detalii)?", "harta orașului, la scara 1:10 000", ["harta lumii, la scara 1:50 000 000", "harta Europei, la scara 1:10 000 000", "harta României, la scara 1:1 000 000"], "Cu cât numărul de după „1:” e mai mic, cu atât scara e mai mare și harta mai detaliată.")
    G.s(2, "2.3", "Asociază tipul de hartă cu ce arată.", [("harta fizică", "relieful și apele"), ("harta politică", "statele și granițele"), ("harta climatică", "temperaturile și precipitațiile"), ("harta turistică", "obiectivele de vizitat")], "Fiecare hartă tematică arată un singur tip de informație principală.")
    G.a(1, "2.3", "Pe harta fizică, ce culoare arată de obicei câmpiile?", "verde", ["maro închis", "alb", "roșu"], "Verdele arată zonele joase; galbenul și maroul, zonele tot mai înalte; albastrul, apele.")
    G.o(2, "2.3", "Ordonează culorile hărții fizice de la zonele cele mai joase la cele mai înalte.", ["verde", "galben", "maro deschis", "maro închis"], "De la jos la sus", "Verde (câmpii), galben (dealuri, podișuri), maro (munți), tot mai închis cu altitudinea.")
    G.a(2, "2.1", "Ce paralelă importantă trece prin România?", "paralela de 45° N", ["Ecuatorul", "Tropicul Racului", "Cercul Polar de Nord"], "Paralela de 45° N trece prin România, la jumătatea distanței dintre Ecuator și Polul Nord.")
    G.a(3, "2.1", "Un loc are latitudinea 0°. Unde se află?", "pe Ecuator", ["la Polul Nord", "pe meridianul Greenwich", "la Tropicul Racului"], "Latitudinea 0° înseamnă Ecuatorul.")
    G.a(3, "2.1", "Un loc are latitudinea 90° N. Unde se află?", "la Polul Nord", ["pe Ecuator", "la Greenwich", "în România"], "90° N e latitudinea maximă: Polul Nord.")
    G.adev(1, "1.2", "Globul păstrează forma Pământului mai bine decât harta.", True, "Adevărat: globul e sferic, ca Pământul; harta e plană și deformează.")
    G.adev(2, "2.1", "Toate meridianele au aceeași lungime.", True, "Adevărat: toate merg de la un pol la altul.")
    G.adev(2, "2.1", "Toate paralelele au aceeași lungime.", False, "Fals: cea mai lungă e Ecuatorul; spre poli paralelele se micșorează.")
    G.a(2, "4.3", "Vrei să găsești un loc cu GPS-ul. Ce îți arată telefonul?", "coordonatele geografice ale locului", ["doar numele străzii", "temperatura", "scara hărții"], "GPS-ul calculează latitudinea și longitudinea.")
    G.l(3, "2.2 3.1", "Completează.", "Pe o hartă la scara 1:200 000, 1 cm reprezintă [2] km, iar 3 cm reprezintă [6] km.", ["20", "60"], "1 cm = 200 000 cm = 2 km; 3 cm = 6 km.")
    G.a(1, "2.3", "Ce culoare au mările și oceanele pe hartă?", "albastru", ["verde", "maro", "galben"], "Apele se reprezintă cu albastru.")

    # ================================================================ S6 Mișcările Pământului
    M = Lectie(5, "V-S06-miscarile-pamantului-consecintele", "Mișcările Pământului și consecințele lor",
               "De ce e zi în România când în America e încă noapte? Și de ce avem iarnă și vară?",
               [("Rotația", "Pământul se rotește în jurul axei sale, de la vest spre est, în aproximativ 24 de ore.\nConsecințe: alternanța zilei cu noaptea; mișcarea aparentă a Soarelui pe cer (răsare la est, apune la vest); orele diferite în locuri diferite. Pământul e împărțit în 24 de fusuri orare, fiecare de câte 15° longitudine (o oră)."),
                ("Revoluția", "Pământul se rotește în jurul Soarelui în aproximativ 365 de zile și 6 ore. La fiecare 4 ani, cele 4 sferturi de zi formează o zi în plus: anul bisect are 366 de zile (29 februarie).\nAxa Pământului e înclinată (aproximativ 23,5°). De aceea, în timpul anului, razele Soarelui cad diferit pe cele două emisfere: așa apar anotimpurile."),
                ("Solstiții și echinocții", "Solstițiul de vară (în jurul lui 21 iunie): cea mai lungă zi din emisfera nordică. Solstițiul de iarnă (în jurul lui 21–22 decembrie): cea mai scurtă zi.\nEchinocțiile (în jurul lui 20–21 martie și 22–23 septembrie): ziua e egală cu noaptea peste tot pe Pământ.")],
               stiaica="La Polul Nord, vara, Soarele nu apune deloc timp de câteva luni (ziua polară), iar iarna nu răsare (noaptea polară).",
               ref=REF.format("Mișcările Pământului și consecințele lor"))
    M.a(1, "1.1", "În jurul a ce se rotește Pământul în mișcarea de rotație?", "în jurul axei sale", ["în jurul Soarelui", "în jurul Lunii", "în jurul lui Jupiter"], "Rotația e în jurul axei; revoluția, în jurul Soarelui.")
    M.a(1, "3.1", "Cât durează, aproximativ, o rotație completă a Pământului?", "24 de ore", ["365 de zile", "o lună", "o săptămână"], "O rotație durează aproximativ o zi, 24 de ore.", surse=NASA)
    M.a(1, "3.1", "Cât durează o revoluție a Pământului în jurul Soarelui?", "aproximativ 365 de zile și 6 ore", ["24 de ore", "30 de zile", "100 de zile"], "O revoluție durează un an: aproximativ 365 de zile și 6 ore.", surse=NASA)
    M.a(1, "3.2", "Ce produce alternanța zilei cu noaptea?", "rotația Pământului", ["revoluția Pământului", "mișcarea Lunii", "norii"], "Rotația face ca fiecare loc să fie pe rând luminat și în umbră.")
    M.a(2, "3.2", "Ce produce succesiunea anotimpurilor?", "revoluția Pământului și înclinarea axei", ["rotația Pământului", "distanța față de Lună", "vânturile"], "Datorită axei înclinate, în timpul revoluției razele cad diferit pe emisfere.")
    M.a(2, "1.2", "În ce sens se rotește Pământul?", "de la vest spre est", ["de la est spre vest", "de la nord spre sud", "de la sud spre nord"], "Pământul se rotește de la vest la est; de aceea Soarele pare că răsare la est.")
    M.a(2, "3.2", "De ce pare că Soarele răsare la est?", "Pământul se rotește de la vest spre est", ["Soarele se mișcă în jurul Pământului", "estul e mai cald", "Luna împinge Soarele"], "Mișcarea Soarelui pe cer e aparentă: de fapt, se rotește Pământul.")
    M.a(2, "3.1", "Câte fusuri orare are Pământul?", "24", ["12", "360", "7"], "24 de fusuri, câte unul pentru fiecare oră a zilei.")
    M.a(3, "3.1", "Câte grade de longitudine are un fus orar?", "15°", ["1°", "24°", "30°"], "360° : 24 de ore = 15° pe oră.", ind="Împarte 360° la 24.")
    M.a(3, "3.1 4.3", "La București e ora 12:00. Într-un loc aflat cu două fusuri orare mai la vest, cât e ora?", "10:00", ["14:00", "12:00", "11:00"], "Spre vest ora scade: cu două fusuri mai la vest e cu 2 ore mai devreme.")
    M.a(3, "3.1 4.3", "La Londra e ora 10:00. La București, cu două fusuri mai la est, cât e ora?", "12:00", ["8:00", "10:00", "11:00"], "Spre est ora crește: +2 ore.")
    M.a(2, "3.1", "Câte zile are un an bisect?", "366", ["365", "364", "360"], "Anul bisect are 366 de zile, cu 29 februarie.")
    M.a(2, "3.2", "De ce avem an bisect la fiecare 4 ani?", "cele 6 ore în plus din fiecare an se adună într-o zi întreagă", ["Pământul se oprește o zi", "Luna întârzie", "așa a hotărât fiecare țară"], "4 × 6 ore = 24 de ore = o zi în plus.")
    M.a(2, "3.1", "Cu cât e înclinată, aproximativ, axa Pământului?", "23,5°", ["90°", "45°", "0°"], "Axa e înclinată cu aproximativ 23,5° (23,44°).", surse=NASA)
    M.s(2, "1.1", "Asociază data (aproximativă) cu momentul anului, în emisfera nordică.", [("21 iunie", "solstițiul de vară"), ("21–22 decembrie", "solstițiul de iarnă"), ("20–21 martie", "echinocțiul de primăvară"), ("22–23 septembrie", "echinocțiul de toamnă")], "Solstițiile: iunie și decembrie. Echinocțiile: martie și septembrie.")
    M.a(2, "1.2", "Ce se întâmplă la echinocțiu?", "ziua e egală cu noaptea peste tot pe Pământ", ["e cea mai lungă zi", "e cea mai lungă noapte", "Soarele nu răsare"], "La echinocțiu, ziua și noaptea au câte 12 ore.")
    M.a(2, "1.2", "Când e cea mai lungă zi a anului în România?", "în jurul lui 21 iunie (solstițiul de vară)", ["în jurul lui 21 decembrie", "pe 1 ianuarie", "pe 1 martie"], "La solstițiul de vară ziua e cea mai lungă în emisfera nordică.")
    M.a(3, "3.2", "Când e vară în România, ce anotimp e în Australia?", "iarnă", ["tot vară", "primăvară", "toamnă"], "Emisferele au anotimpuri opuse: Australia e în emisfera sudică.")
    M.a(2, "1.1", "Cum se numește perioada de luni de zile în care Soarele nu apune, la poli?", "ziua polară", ["noaptea polară", "echinocțiul", "eclipsa"], "Ziua polară: Soarele nu apune; noaptea polară: Soarele nu răsare.")
    M.o(2, "1.2", "Ordonează anotimpurile, începând cu primăvara.", ["primăvara", "vara", "toamna", "iarna"], "Ordinea din an", "Primăvara, vara, toamna, iarna.")
    M.o(3, "1.2 2.3", "Ordonează momentele anului, începând cu luna martie.", ["echinocțiul de primăvară", "solstițiul de vară", "echinocțiul de toamnă", "solstițiul de iarnă"], "În ordinea calendarului", "Martie, iunie, septembrie, decembrie.")
    M.l(2, "1.1", "Completează.", "Pământul se rotește în jurul [axei] sale în aproximativ 24 de ore și în jurul [Soarelui] în aproximativ un an.", ["Lunii", "Ecuatorului"], "Rotația: în jurul axei. Revoluția: în jurul Soarelui.")
    M.adev(1, "3.2", "Când în România e zi, pe partea opusă a Pământului e noapte.", True, "Adevărat: jumătate din Pământ e luminată, cealaltă e în umbră.")
    M.adev(2, "3.2", "Anotimpurile apar pentru că Pământul se apropie și se depărtează mult de Soare.", False, "Fals: anotimpurile apar din cauza înclinării axei, nu a distanței.")
    M.a(2, "1.1", "Ce fus orar are România iarna (ora de iarnă)?", "UTC+2 (cu 2 ore înaintea Londrei)", ["UTC+0", "UTC−2", "UTC+5"], "România are ora Europei de Est: UTC+2 iarna, UTC+3 vara.")
    M.s(3, "3.2", "Asociază mișcarea cu consecința ei.", [("rotația", "ziua și noaptea"), ("revoluția și înclinarea axei", "anotimpurile"), ("rotația, de la vest la est", "Soarele răsare la est"), ("diferența de longitudine", "ore diferite în locuri diferite")], "Rotația: zi/noapte și mișcarea aparentă a Soarelui. Revoluția: anotimpurile.")
    M.a(3, "3.2 4.3", "De ce zborul de la București la New York „câștigă” ore pe ceas?", "zbori spre vest, spre fusuri orare cu ora mai mică", ["avionul zboară mai repede decât timpul", "ceasul se strică în avion", "la New York e alt an"], "Spre vest, fiecare fus orar are cu o oră mai puțin.")
    M.l(3, "3.1", "Completează.", "Un fus orar are [15] grade de longitudine, iar diferența dintre două fusuri vecine este de o [oră].", ["24", "zi"], "360° : 24 = 15° pe oră.")
    M.a(1, "1.1", "Cum se numește mișcarea Pământului în jurul Soarelui?", "revoluție", ["rotație", "eclipsă", "maree"], "Revoluția e mișcarea pe orbită, în jurul Soarelui.")
    M.a(2, "3.2", "La Ecuator, cum variază lungimea zilei de-a lungul anului?", "rămâne aproape egală cu noaptea tot anul", ["vara e zi tot timpul", "iarna e noapte tot timpul", "se schimbă foarte mult"], "La Ecuator ziua și noaptea au aproape 12 ore tot anul.")

    # ================================================================ S8 Orientarea: completare până la 30 de itemi
    O = existent(5, "u2-miscare.json", "V-S08-orientarea-spatiul-terestru-elemente", "V8")
    O.a(1, "1.1", "Ce arată punctul cardinal opus nordului?", "sudul", ["estul", "vestul", "nord-estul"], "Nordul și sudul sunt opuse; la fel estul și vestul.")
    O.a(2, "2.1", "Stai cu fața spre est. Ce ai în spate?", "vestul", ["nordul", "sudul", "estul"], "Estul și vestul sunt opuse.")
    O.a(2, "2.1", "Stai cu fața spre sud. Ce ai la stânga?", "estul", ["vestul", "nordul", "sudul"], "Cu fața spre sud, estul e la stânga și vestul la dreapta.", ind="Imaginează-ți că te întorci cu spatele la nord.")
    O.a(2, "1.2", "Ce direcție arată umbra ta dimineața, la răsărit?", "spre vest", ["spre est", "spre nord", "spre sud"], "Dimineața Soarele e la est, deci umbra cade spre vest.")
    O.a(2, "1.2", "Ce direcție arată umbra ta seara, la apus?", "spre est", ["spre vest", "spre nord", "spre sud"], "Seara Soarele e la vest, deci umbra cade spre est.")
    O.ds(2, "2.1", "Ce punct cardinal e evidențiat pe roza vânturilor?", "busola", "E", "est", ["vest", "nord", "sud-est"], "Punctul evidențiat e la dreapta nordului: estul.")
    O.ds(2, "2.1", "Ce punct intermediar e evidențiat pe roza vânturilor?", "busola", "SV", "sud-vest", ["sud-est", "nord-vest", "nord-est"], "Între sud și vest e sud-vestul.")
    O.a(2, "1.1", "În ce constelație se află Steaua Polară?", "Ursa Mică (Carul Mic)", ["Orion", "Casiopeea", "Leul"], "Steaua Polară e la capătul „oiștii” Carului Mic.")
    O.a(3, "4.3", "Te-ai rătăcit noaptea, cerul e senin. Cum găsești Steaua Polară?", "prelungești de 5 ori latura din spate a Carului Mare", ["cauți cea mai roșie stea", "te uiți spre sud", "cauți Luna"], "Cele două stele din spatele Carului Mare arată spre Steaua Polară.")
    O.o(2, "2.1", "Ordonează direcțiile în sensul acelor de ceasornic, începând cu nordul.", ["nord", "est", "sud", "vest"], "În sensul acelor de ceasornic", "Nord, est, sud, vest.")
    O.o(3, "2.1", "Ordonează direcțiile intermediare în sensul acelor de ceasornic, începând cu nord-estul.", ["nord-est", "sud-est", "sud-vest", "nord-vest"], "În sensul acelor de ceasornic", "NE, SE, SV, NV.")
    O.l(2, "1.1", "Completează.", "Busola are un ac [magnetic], al cărui capăt colorat arată spre [nord].", ["de lemn", "sud"], "Acul magnetic se orientează spre nord.")
    O.a(2, "4.3", "Ce poate strica funcționarea unei busole?", "obiectele de fier sau magneții din apropiere", ["lumina Soarelui", "vântul", "ploaia"], "Fierul și magneții atrag acul și dau o direcție greșită.")
    O.adev(2, "1.2", "Soarele răsare exact la est în fiecare zi a anului.", False, "Fals: exact la est răsare doar la echinocții; vara răsare spre nord-est, iarna spre sud-est.")
    O.s(2, "1.1 2.1", "Asociază mijlocul de orientare cu momentul în care îl folosești.", [("Soarele", "ziua, pe cer senin"), ("Steaua Polară", "noaptea, pe cer senin"), ("busola", "oricând, departe de fier"), ("GPS-ul", "cu telefon și semnal de la sateliți")], "Fiecare mijloc are condițiile lui.")

    # ================================================================ expediția S9 rămâne cea din MVP
    E = existent(5, "u2-miscare.json", "V-S09-aplicatii-practice-masurarea-timpului", "V9")
    return Unitate(5, "u2-miscare.json", "Terra – o planetă în mișcare").add(G, M, O, E)
