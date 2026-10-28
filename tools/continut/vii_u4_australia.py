from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VII-a, ediția 2024 (manuale.edu.ro), lecția „{}”"
S_AU = ["Geoscience Australia – Area of Australia / Australia's size", "Encyclopaedia Britannica – Australia"]
S_ABS = ["Australian Bureau of Statistics (ABS) – National, state and territory population", "ONU (UN DESA) – World Population Prospects 2024"]
S_KOSC = ["Geoscience Australia – Highest Mountains (Mount Kosciuszko 2 228 m)", "Encyclopaedia Britannica – Mount Kosciuszko"]
S_EYRE = ["Geoscience Australia – Landforms: Lake Eyre (Kati Thanda), −15 m", "Encyclopaedia Britannica – Lake Eyre"]
S_GBR = ["UNESCO World Heritage Centre – Great Barrier Reef", "Great Barrier Reef Marine Park Authority (gbrmpa.gov.au)"]
S_ULURU = ["UNESCO World Heritage Centre – Uluṟu-Kata Tjuṯa National Park", "Parks Australia – Uluṟu-Kata Tjuṯa"]
S_MK = ["U.S. Geological Survey – Mauna Kea", "Encyclopaedia Britannica – Mauna Kea"]
S_ANT = ["British Antarctic Survey – Antarctica fact file", "National Snow and Ice Data Center (NSIDC) – Quick facts on ice sheets"]
S_VINSON = ["Encyclopaedia Britannica – Vinson Massif", "Wikipedia – Vinson Massif"]
S_TRAT = ["Secretariatul Tratatului Antarctic (ats.aq) – The Antarctic Treaty", "Encyclopaedia Britannica – Antarctic Treaty"]
S_WMO = ["WMO – World Weather and Climate Extremes Archive", "NOAA NCEI – Global extremes"]
S_RAC = ["Institutul de Speologie „Emil Racoviță” – biografie", "Wikipedia – Belgian Antarctic Expedition"]


def unitate():
    # ================================================================ S30a Australia și Oceania – caracterizare
    A = Lectie(7, "VII-S30-australia-oceania-caracterizare-geografica", "Australia și Oceania – caracterizare geografică",
               "Poate o țară să fie și continent?",
               [("Australia – un continent-țară", "Australia e cel mai mic continent (aproximativ 7,7 milioane km²) și singurul ocupat în întregime de un singur stat: Commonwealth of Australia. Se află în emisferele sudică și estică, între Oceanul Indian (vest) și Oceanul Pacific (est).\nE străbătută de Tropicul Capricornului. Țărmuri: Golful Carpentaria, Peninsula Cape York, insula Tasmania la sud."),
                ("Oceania", "Oceania cuprinde mii de insule din Oceanul Pacific, grupate în trei regiuni: Melanezia („insulele negre”: Noua Guinee, Fiji, Insulele Solomon), Micronezia („insulele mici”: Guam, Insulele Marshall) și Polinezia („multe insule”: Hawaii, Noua Zeelandă, Samoa, Tahiti, Insula Paștelui).\nÎmpreună, Australia și Oceania sunt adesea studiate ca un singur continent, numit și Oceania."),
                ("Izolare", "Australia și Oceania sunt foarte departe de celelalte continente. Această izolare explică plantele și animalele unice și faptul că au fost printre ultimele regiuni descoperite de europeni.")],
               stiaica="Numele „Australia” vine din latinescul „Terra Australis”, adică „Pământul de Sud”.",
               ref=REF.format("Australia și Oceania – caracterizare geografică"), prefix="VII30a")
    A.a(1, "2.1", "Care e cel mai mic continent?", "Australia", ["Europa", "Antarctica", "America de Sud"], "Australia are aproximativ 7,7 milioane km².", surse=S_AU)
    A.a(2, "1.1", "De ce Australia e numită „continent-țară”?", "pentru că întregul continent e ocupat de un singur stat", ["pentru că are multe țări mici", "pentru că e o insulă mică", "pentru că nu are capitală"], "Commonwealth of Australia.")
    A.a(2, "2.1", "În ce emisfere se află Australia?", "sudică și estică", ["nordică și vestică", "nordică și estică", "sudică și vestică"], "E la sud de Ecuator și la est de meridianul de 0°.")
    A.a(2, "2.1", "Ce tropic străbate Australia?", "Tropicul Capricornului", ["Tropicul Racului", "Cercul Polar de Sud", "Ecuatorul"], "Tropicul Capricornului trece prin centrul Australiei.")
    A.e(2, "2.1", "Pune pe hartă oceanele din jurul Australiei.", [("ind", "Oceanul Indian", -25, 95), ("pac", "Oceanul Pacific", -20, 170)], "Indian la vest, Pacific la est.", harta="lume")
    A.s(2, "2.1", "Asociază regiunea Oceaniei cu înțelesul numelui.", [("Melanezia", "insulele negre"), ("Micronezia", "insulele mici"), ("Polinezia", "multe insule")], "Numele vin din greacă.")
    A.s(2, "2.1", "Asociază insula sau arhipelagul cu regiunea Oceaniei.", [("Noua Guinee", "Melanezia"), ("Guam", "Micronezia"), ("Hawaii", "Polinezia – nordul triunghiului"), ("Noua Zeelandă", "Polinezia – sud-vestul triunghiului")], "Cele trei regiuni.")
    A.p(2, "2.1", "Atinge pe hartă Tasmania.", "lume", -42, 146.6, "Tasmania", 400, "Tasmania e la sud de Australia.")
    A.p(2, "2.1", "Atinge pe hartă Noua Guinee.", "lume", -6, 143, "Noua Guinee", 600, "Noua Guinee e la nord de Australia.")
    A.p(2, "2.1", "Atinge pe hartă Noua Zeelandă.", "lume", -41, 174, "Noua Zeelandă", 600, "Noua Zeelandă e la sud-est de Australia.")
    A.p(3, "2.1", "Atinge pe hartă Hawaii.", "lume", 20.5, -157, "Hawaii", 500, "Hawaii e în mijlocul Pacificului de Nord.")
    A.p(3, "2.1", "Atinge pe hartă Insula Paștelui.", "lume", -27.1, -109.4, "Insula Paștelui", 500, "Insula Paștelui aparține statului Chile.")
    A.a(2, "2.1", "Ce insulă e cea mai mare din Oceania?", "Noua Guinee", ["Tasmania", "Hawaii", "Fiji"], "A doua insulă ca mărime din lume, după Groenlanda.")
    A.a(2, "2.1", "Ce golf mare pătrunde în nordul Australiei?", "Golful Carpentaria", ["Golful Mexic", "Golful Persic", "Golful Guineei"], "La est de el e Peninsula Cape York.")
    A.a(2, "1.2", "Ce explică plantele și animalele unice ale Australiei?", "izolarea îndelungată de celelalte continente", ["clima polară", "vulcanii activi", "apropierea de Europa"], "Speciile au evoluat separat milioane de ani.")
    A.adev(2, "1.2", "Australia e ocupată de mai multe state.", False, "Fals: de un singur stat.")
    A.adev(2, "2.1", "Hawaii fac parte din Polinezia.", True, "Adevărat: Hawaii sunt statul cu numărul 50 al SUA.")
    A.l(2, "2.1", "Completează.", "Australia e scăldată de Oceanul [Indian] la vest și de Oceanul [Pacific] la est.", ["Atlantic", "Arctic"], "Indian și Pacific.")
    A.l(2, "1.1", "Completează.", "Cea mai mare insulă din Oceania este [Noua Guinee]; insula de la sudul Australiei este [Tasmania].", ["Fiji", "Madagascar"], "Noua Guinee, Tasmania.")
    A.d(2, "2.1", "Ce peninsulă din nordul Australiei e marcată pe hartă?", "lume", -13, 142.8, "Cape York", ["Arnhem Land", "Malacca", "Kamciatka"], "Cape York e cel mai nordic punct al Australiei.")
    A.o(3, "2.2 3.1 4.2", "Ordonează locurile de la vest la est.", ["Perth", "Australia centrală (Uluru)", "Sydney", "Noua Zeelandă", "Tahiti"], "De la vest la est", "De la Oceanul Indian spre Pacificul central.")
    A.g(3, "2.3 4.1", "Graficul compară suprafețele (milioane km², rotunjit). De câte ori e mai mare Antarctica decât Australia?", grafic("bare", "Suprafața (milioane km², rotunjit)", [("Antarctica", 14), ("Europa", 10), ("Australia", 7.7)], "milioane km²", "Encyclopaedia Britannica; Geoscience Australia"), "de aproape 2 ori", ["de 10 ori", "la fel", "de 2 ori mai mică"], "14 : 7,7 ≈ 1,8.", surse=S_AU)
    A.a(2, "1.1", "Ce înseamnă „Terra Australis”?", "Pământul de Sud", ["Pământul de Est", "Insula Mare", "Țara Caldă"], "Așa se numea în hărțile vechi un continent sudic imaginat.")
    A.a(3, "4.3", "Compară Australia cu Groenlanda.", "Australia e considerată continent; Groenlanda e insulă, deși ambele sunt mari mase de uscat înconjurate de apă", ["Groenlanda e continent", "Australia e insulă", "sunt identice"], "Australia e mult mai mare.")
    A.a(2, "2.1", "Ce strâmtoare desparte Australia de Noua Guinee?", "Strâmtoarea Torres", ["Strâmtoarea Bass", "Strâmtoarea Bering", "Strâmtoarea Drake"], "Strâmtoarea Bass desparte Australia de Tasmania.")
    A.a(2, "2.1", "Ce strâmtoare desparte Australia de Tasmania?", "Strâmtoarea Bass", ["Strâmtoarea Torres", "Strâmtoarea Malacca", "Strâmtoarea Gibraltar"], "Bass e la sud de Melbourne.")
    A.a(2, "1.2", "Cine a cartografiat coasta de est a Australiei, în 1770?", "James Cook", ["Cristofor Columb", "Vasco da Gama", "Amundsen"], "Cook a revendicat-o pentru Marea Britanie.")
    A.a(2, "2.1", "Ce linie importantă trece prin Pacific, unde se schimbă data calendaristică?", "linia de schimbare a datei (aproape de meridianul de 180°)", ["Ecuatorul", "meridianul de 0°", "Tropicul Racului"], "Când treci linia, sari o zi sau o repeți.")
    A.a(2, "2.1", "Ce stat insular din Melanezia e cunoscut pentru rugby și plaje?", "Fiji", ["Hawaii", "Tasmania", "Japonia"], "Fiji are peste 300 de insule.")
    A.a(3, "2.2", "De ce Polinezia se întinde pe o suprafață oceanică uriașă, dar are puțin uscat?", "e formată din insule mici, foarte îndepărtate între ele", ["e un continent", "e un deșert", "e acoperită de gheață"], "Triunghiul Polinezian: Hawaii – Noua Zeelandă – Insula Paștelui.")

    # ================================================================ S30b Australia – caracterizare generală
    B = Lectie(7, "VII-S30-australia-caracterizare-geografica-generala", "Australia – caracterizare geografică generală",
               "De ce cei mai mulți australieni locuiesc pe țărm?",
               [("Relieful", "Australia e cel mai jos și mai plat continent locuit. În vest: Podișul Australiei de Vest (vechi, deșertic); în centru: câmpii joase și Lacul Eyre (Kati Thanda), cel mai jos punct, la aproximativ 15 m sub nivelul mării; în est: Marea Cumpănă a Apelor (Great Dividing Range), cu vârful Kosciuszko (2 228 m).\nUluru, un monolit uriaș de gresie din centrul Australiei, e un loc sfânt pentru aborigeni."),
                ("Clima și apele", "Australia e cel mai uscat continent locuit: aproape o treime din suprafață e deșert. Clima e tropicală în nord, deșertică în centru și vest, mediteraneeană în sud-vest și sud, temperată în sud-est.\nRâuri puține: Murray și Darling formează cel mai mare sistem hidrografic. Multe râuri seacă vara (creek-uri). Marele Bazin Artezian are apă subterană folosită în ferme."),
                ("Populația și economia", "Australia are aproximativ 27 de milioane de locuitori, după ABS, concentrați pe țărmurile de est și sud-est: Sydney, Melbourne, Brisbane, Adelaide, Perth. Capitala e Canberra.\nPrimii locuitori sunt aborigenii, prezenți de zeci de mii de ani. Economie: minereuri (fier, cărbune, aur, bauxită, litiu), creșterea oilor (lână) și vitelor, grâu, turism.")],
               stiaica="Australia are mai multe oi decât oameni: de câteva ori mai multe.",
               ref=REF.format("Australia – caracterizare geografică generală"), prefix="VII30b")
    B.a(1, "2.1", "Care e cel mai înalt vârf al Australiei?", "Kosciuszko (2 228 m)", ["Uluru", "Everest", "Mauna Kea"], "Kosciuszko e în Alpii Australieni.", surse=S_KOSC)
    B.a(2, "2.1", "Care e cel mai jos punct al Australiei?", "Lacul Eyre (Kati Thanda), la aproximativ 15 m sub nivelul mării", ["Marea Moartă", "Valea Morții", "Uluru"], "Lacul Eyre se umple cu apă doar rar.", surse=S_EYRE)
    B.a(2, "2.1", "Ce este Uluru?", "un monolit uriaș de gresie, loc sfânt pentru aborigeni", ["un vulcan activ", "un lac", "un oraș"], "Uluru e în centrul Australiei.", surse=S_ULURU)
    B.a(2, "2.2", "De ce Australia e cel mai uscat continent locuit?", "o mare parte se află în zona tropicală de presiune ridicată, unde aerul coboară și e uscat", ["pentru că e la pol", "pentru că plouă tot anul", "pentru că are ghețari"], "Aproape o treime e deșert.")
    B.a(2, "2.1", "Ce râuri formează cel mai mare sistem hidrografic al Australiei?", "Murray și Darling", ["Nil și Congo", "Amazon și Orinoco", "Gange și Indus"], "Bazinul Murray–Darling e o zonă agricolă importantă.")
    B.a(2, "2.2", "Ce este Marele Bazin Artezian?", "o uriașă rezervă de apă subterană folosită în ferme", ["un deșert", "un lac sărat", "un munte"], "Apa iese singură la suprafață prin foraje.")
    B.a(2, "2.1", "Care e capitala Australiei?", "Canberra", ["Sydney", "Melbourne", "Perth"], "Canberra a fost construită ca un compromis între Sydney și Melbourne.")
    B.a(2, "3.2", "Câți locuitori are Australia, aproximativ?", "27 de milioane", ["2,7 milioane", "270 de milioane", "2,7 miliarde"], "După Biroul Australian de Statistică.", surse=S_ABS)
    B.a(2, "2.2", "Unde trăiesc cei mai mulți australieni?", "pe țărmurile de est și sud-est", ["în deșertul central", "în nordul tropical", "pe Uluru"], "Acolo clima e mai blândă și există apă.")
    B.s(2, "3.3", "Asociază orașul cu poziția lui.", [("Sydney", "sud-est, pe Pacific"), ("Perth", "sud-vest, pe Oceanul Indian"), ("Darwin", "nord, în zona tropicală"), ("Canberra", "sud-est, capitala")], "Orașele Australiei.")
    B.s(2, "3.2", "Asociază climatul cu regiunea Australiei.", [("tropical", "nord"), ("deșertic", "centru și vest"), ("mediteranean", "sud-vest"), ("temperat", "sud-est și Tasmania")], "Climatele Australiei.")
    B.p(2, "2.1", "Atinge pe hartă Uluru.", "lume", -25.34, 131.04, "Uluru", 400, "Uluru e în centrul Australiei.", surse=S_ULURU)
    B.p(2, "2.1", "Atinge pe hartă Sydney.", "lume", -33.87, 151.21, "Sydney", 300, "Sydney e cel mai mare oraș al Australiei.")
    B.p(3, "2.1", "Atinge pe hartă Perth.", "lume", -31.95, 115.86, "Perth", 300, "Perth e pe coasta de vest.")
    B.p(3, "2.1", "Atinge pe hartă Lacul Eyre.", "lume", -28.4, 137.3, "Lacul Eyre", 400, "Lacul Eyre e în Australia de Sud.", surse=S_EYRE)
    B.a(2, "3.3", "Cine sunt aborigenii?", "primii locuitori ai Australiei, prezenți de zeci de mii de ani", ["coloniști englezi", "turiști", "imigranți recenți din Asia"], "Au una dintre cele mai vechi culturi continue din lume.")
    B.a(2, "3.3", "Ce animal crescut în Australia dă lână?", "oaia (rasa merinos)", ["cangurul", "koala", "emu"], "Australia e un mare producător de lână.")
    B.a(2, "3.3", "Ce minereuri exportă mult Australia?", "fier, cărbune, aur, bauxită, litiu", ["cafea", "cacao", "banane"], "Mineritul e foarte important.")
    B.adev(2, "2.2", "Australia e un continent foarte muntos și înalt.", False, "Fals: e cel mai jos și mai plat continent locuit.")
    B.adev(2, "2.2", "Multe râuri din Australia seacă în perioadele uscate.", True, "Adevărat: se numesc creek-uri.")
    B.l(2, "2.1", "Completează.", "Capitala Australiei este [Canberra], iar cel mai mare oraș este [Sydney].", ["Perth", "Darwin"], "Canberra, Sydney.")
    B.l(2, "2.2", "Completează.", "Lanțul muntos din estul Australiei se numește Marea Cumpănă a [Apelor]; cel mai înalt vârf este [Kosciuszko].", ["Munților", "Uluru"], "Great Dividing Range.")
    B.g(3, "2.3 4.1", "Diagrama arată precipitațiile anuale în trei orașe australiene (valori aproximative). Unde plouă cel mai puțin?", grafic("bare", "Precipitații anuale (valori aproximative)", [("Darwin (nord)", 1700), ("Sydney (est)", 1200), ("Alice Springs (centru)", 290)], "l/m²", "Bureau of Meteorology (Australia) – climate statistics"), "la Alice Springs, în centru", ["la Darwin", "la Sydney", "egal"], "Centrul e deșertic.", surse=["Bureau of Meteorology (bom.gov.au) – Climate statistics for Australian locations", "Encyclopaedia Britannica – Alice Springs"])
    B.a(3, "4.3", "De ce în Australia oamenii trăiesc pe țărm, iar în Egipt pe valea unui fluviu?", "în ambele cazuri oamenii se adună unde găsesc apă și climă potrivită", ["în Australia e interzis în interior", "Egiptul nu are țărm", "fără motiv"], "Apa decide răspândirea populației.")
    B.d(2, "2.1", "Ce oraș australian, al doilea ca mărime, e marcat pe hartă?", "lume", -37.81, 144.96, "Melbourne", ["Adelaide", "Brisbane", "Hobart"], "Melbourne e în sud-est.")
    B.a(2, "4.4", "Ce fenomene extreme lovesc des Australia?", "seceta și incendiile de vegetație", ["avalanșele", "viscolul polar", "erupțiile vulcanice zilnice"], "Incendiile din 2019–2020 au fost devastatoare.")
    B.a(2, "3.3", "Ce clădire din Sydney e în patrimoniul UNESCO?", "Opera din Sydney", ["Turnul Eiffel", "Colosseumul", "Big Ben"], "Opera are acoperișul în formă de pânze.")
    B.a(2, "3.3", "Ce limbă oficială are Australia?", "engleza", ["franceza", "spaniola", "germana"], "Australia a fost colonie britanică.")
    B.a(3, "3.2", "De ce Australia e importantă pentru mașinile electrice?", "e unul dintre cei mai mari producători de litiu, folosit în baterii", ["produce benzină", "are cele mai multe fabrici de mașini", "nu are importanță"], "Litiul e un metal-cheie al tranziției energetice.")
    B.a(2, "2.2", "Ce înseamnă „outback”?", "interiorul vast, uscat și slab populat al Australiei", ["un cartier din Sydney", "o plajă", "un munte"], "Outback-ul acoperă cea mai mare parte a continentului.")

    # ================================================================ S31a Oceania
    O = Lectie(7, "VII-S31-oceania-particularitati-geografice", "Oceania – particularități geografice",
               "Cum se formează o insulă de corali?",
               [("Tipuri de insule", "Insule continentale: bucăți desprinse din continente, mari și cu relief variat (Noua Guinee, Noua Zeelandă, Tasmania).\nInsule vulcanice: formate de vulcani ieșiți din ocean (Hawaii, Samoa, Tahiti).\nInsule coraliere (atoli): inele de recif de corali în jurul unei lagune, foarte joase (Tuvalu, Kiribati, Insulele Marshall). Ele se formează în jurul unui vulcan care s-a scufundat încet."),
                ("Noua Zeelandă și Papua Noua Guinee", "Noua Zeelandă are două insule mari, cu munți înalți (Alpii Sudici, vârful Aoraki/Mount Cook), vulcani, gheizere și fiorduri. Primii locuitori au fost maorii.\nPapua Noua Guinee are munți înalți, păduri tropicale și peste 800 de limbi – una dintre cele mai mari diversități lingvistice."),
                ("Hawaii și Pacificul", "Mauna Kea, în Hawaii, are 4 207 m deasupra mării, dar măsurat de la baza lui de pe fundul oceanului depășește 10 000 m – mai mult decât Everest.\nStatele insulare mici sunt amenințate de creșterea nivelului mării.")],
               stiaica="Recifele de corali sunt construite de animale minuscule, polipii de corali, care își fac schelete de calcar.",
               ref=REF.format("Oceania – particularități geografice"), prefix="VII31a")
    O.s(1, "1.1", "Asociază tipul de insulă cu exemplul.", [("continentală", "Noua Guinee"), ("vulcanică", "Hawaii"), ("coralieră (atol)", "Tuvalu"), ("continentală, cu fiorduri", "Noua Zeelandă")], "Tipuri de insule.")
    O.a(1, "1.1", "Ce este un atol?", "un inel de recif de corali în jurul unei lagune", ["un vulcan activ", "un ghețar", "un fluviu"], "Atolii sunt foarte joși.")
    O.o(3, "1.2 3.1 4.2", "Ordonează cum se formează un atol.", ["un vulcan iese din ocean și formează o insulă", "coralii cresc pe țărmul insulei", "vulcanul se scufundă încet", "recifele cresc în sus", "rămâne un inel de corali în jurul unei lagune"], "Formarea atolului", "Explicația lui Charles Darwin.")
    O.a(1, "1.2", "Cine construiește recifele de corali?", "polipii de corali, animale mici cu schelet de calcar", ["peștii", "vulcanii", "oamenii"], "Recifele cresc foarte încet.")
    O.a(2, "2.1", "Cine au fost primii locuitori ai Noii Zeelande?", "maorii", ["aborigenii", "inuiții", "incașii"], "Maorii au sosit cu canoe, din Polinezia.")
    O.a(2, "2.2", "Ce fenomene geotermale sunt frecvente în Noua Zeelandă?", "gheizere și izvoare termale", ["tornade", "taifunuri", "furtuni de nisip"], "Rotorua e cunoscută pentru gheizere.")
    O.a(2, "2.1", "Care e cel mai înalt vârf al Noii Zeelande?", "Aoraki/Mount Cook", ["Mauna Kea", "Kosciuszko", "Uluru"], "Aoraki e în Alpii Sudici.")
    O.a(2, "3.3", "Ce țară are peste 800 de limbi?", "Papua Noua Guinee", ["Noua Zeelandă", "Australia", "Fiji"], "Una dintre cele mai mari diversități lingvistice din lume.")
    O.a(2, "2.1", "Ce vulcan din Hawaii depășește 10 000 m măsurat de la baza de pe fundul oceanului?", "Mauna Kea", ["Fuji", "Etna", "Kilimanjaro"], "Are 4 207 m deasupra mării.", surse=S_MK)
    O.p(2, "2.1", "Atinge pe hartă Papua Noua Guinee.", "lume", -6.5, 145, "Papua Noua Guinee", 500, "Ocupă estul insulei Noua Guinee.")
    O.p(2, "2.1", "Atinge pe hartă Tahiti.", "lume", -17.65, -149.4, "Tahiti", 500, "Tahiti e în Polinezia Franceză.")
    O.p(3, "2.1", "Atinge pe hartă Tuvalu, un stat format din atoli.", "lume", -8.5, 179.2, "Tuvalu", 600, "Tuvalu e în Pacificul central.")
    O.p(3, "2.1", "Atinge pe hartă Fiji.", "lume", -17.8, 178, "Fiji", 500, "Fiji e în Melanezia.")
    O.a(2, "4.4", "De ce statele formate din atoli sunt în pericol?", "sunt foarte joase, iar nivelul mării crește", ["sunt prea înalte", "au prea mulți vulcani", "sunt acoperite de gheață"], "Tuvalu, Kiribati, Maldive sunt amenințate.")
    O.adev(2, "1.2", "Atolii sunt insule foarte înalte, cu munți.", False, "Fals: sunt foarte joși, de câțiva metri.")
    O.adev(2, "2.2", "Noua Zeelandă are și vulcani, și ghețari, și fiorduri.", True, "Adevărat: relief foarte variat.")
    O.l(2, "1.1", "Completează.", "Inelul de corali din jurul unei lagune se numește [atol]; insulele Hawaii sunt de origine [vulcanică].", ["fiord", "glaciară"], "Atol, vulcanică.")
    O.l(2, "3.3", "Completează.", "Primii locuitori ai Noii Zeelande sunt [maorii]; capitala Noii Zeelande este [Wellington].", ["aborigenii", "Auckland"], "Maori, Wellington.")
    O.g(3, "2.3 4.1", "Graficul arată altitudinea maximă a trei state insulare imaginare. Care e cel mai amenințat de creșterea nivelului mării?", grafic("bare", "Altitudinea maximă (state imaginare)", [("insula A", 4), ("insula B", 1200), ("insula C", 2500)], "m"), "insula A", ["insula B", "insula C", "niciuna"], "Doar 4 m deasupra mării.")
    O.a(3, "4.3", "Compară Hawaii cu Tuvalu.", "Hawaii sunt insule vulcanice înalte; Tuvalu e format din atoli foarte joși", ["sunt identice", "Tuvalu e mai înalt", "Hawaii sunt atoli"], "Origini diferite.")
    O.d(2, "2.1", "Ce stat insular, cu două insule mari, e marcat pe hartă?", "lume", -41, 174, "Noua Zeelandă", ["Tasmania", "Fiji", "Samoa"], "Insula de Nord și Insula de Sud.")
    O.a(2, "3.3", "Ce statui uriașe de piatră se află pe Insula Paștelui?", "statuile moai", ["piramidele", "sfinxul", "Statuia Libertății"], "Au fost sculptate de populația rapa nui.")
    O.a(2, "3.3", "Ce înseamnă „haka”?", "un dans ritual maori, cunoscut din rugby", ["o insulă", "un vulcan", "o pasăre"], "Echipa All Blacks îl execută înainte de meciuri.")
    O.a(2, "2.1", "Ce oraș e cel mai mare din Noua Zeelandă?", "Auckland", ["Wellington", "Sydney", "Suva"], "Capitala e Wellington.")
    O.a(2, "3.3", "Ce resursă e importantă pentru economia multor insule din Pacific?", "pescuitul și turismul", ["mineritul de cărbune", "industria oțelului", "petrolul din abundență"], "Plajele și recifele atrag turiști.")
    O.a(2, "3.3", "Ce animal crescut în Noua Zeelandă e foarte numeros?", "oaia", ["cămila", "bizonul", "lama"], "Noua Zeelandă exportă lână și carne de miel.")
    O.a(2, "3.3", "Ce pasăre fără zbor e simbolul Noii Zeelande?", "kiwi", ["emu", "struțul", "pinguinul imperial"], "Neozeelandezii sunt numiți și „kiwi”.")
    O.a(3, "2.2", "De ce în Noua Zeelandă se produc cutremure?", "se află la granița dintre placa australiană și placa pacifică", ["e pe un atol", "e în mijlocul unei plăci stabile", "e la pol"], "Ca Japonia, e în Cercul de Foc.")
    O.a(2, "2.1", "Din ce stat face parte Hawaii?", "SUA", ["Australia", "Japonia", "Noua Zeelandă"], "Hawaii e al 50-lea stat al SUA, din 1959.")
    O.a(2, "4.4", "Ce poate face lumea pentru statele insulare amenințate?", "reducerea emisiilor de gaze cu efect de seră și ajutor pentru adaptare", ["nimic", "creșterea poluării", "mutarea oceanului"], "Încetinirea încălzirii climei e esențială.")

    # ================================================================ S31b Antarctica
    N = Lectie(7, "VII-S31-antarctica-elemente-identitate-geografica", "Antarctica – elemente de identitate geografică",
               "Al cui e continentul de gheață?",
               [("Continentul alb", "Antarctica e continentul din jurul Polului Sud, cu aproximativ 14 milioane km², aproape în întregime acoperit de o calotă de gheață groasă în medie de aproape 2 km. Aici se află aproximativ 90 % din gheața Pământului și aproape 70 % din apa dulce.\nE scăldată de Oceanul de Sud (Antarctic), format din apele sudice ale Atlanticului, Pacificului și Indianului."),
                ("Cel mai rece, uscat și vânturos", "La stația rusă Vostok s-a măsurat −89,2 °C, pe 21 iulie 1983, cea mai scăzută temperatură înregistrată pe Pământ. Interiorul primește foarte puține precipitații – de aceea Antarctica e considerată cel mai mare deșert.\nCel mai înalt vârf: Masivul Vinson (4 892 m). Există și vulcani, ca Erebus."),
                ("Viață și cooperare", "Pe țărmuri și în ocean trăiesc pinguini, foci, balene, păsări marine; la baza lanțului trofic e krillul.\nAntarctica nu aparține nimănui: Tratatul Antarctic (semnat în 1959) o rezervă păcii și cercetării științifice. Aici lucrează doar cercetători, în stații. România are stația Law-Racoviță, în colaborare cu Australia; Emil Racoviță a participat la expediția „Belgica” (1897–1899).")],
               stiaica="Pinguinul imperial, cel mai mare pinguin, clocește ouăle iarna, pe gheață: masculii le țin pe labe luni întregi, la temperaturi de −40 °C.",
               ref=REF.format("Antarctica – elemente de identitate geografică"), prefix="VII31b")
    N.a(1, "2.1", "Ce continent se află în jurul Polului Sud?", "Antarctica", ["Australia", "America de Sud", "Africa"], "Antarctica e continentul de gheață.")
    N.a(2, "3.1", "Ce parte din gheața Pământului se află în Antarctica?", "aproximativ 90 %", ["aproximativ 10 %", "aproximativ 50 %", "toată"], "Calota antarctică e cea mai mare masă de gheață.", surse=S_ANT)
    N.a(2, "3.1", "Ce grosime medie are calota de gheață a Antarcticii?", "aproape 2 km", ["2 m", "20 m", "20 km"], "În unele locuri depășește 4 km.", surse=S_ANT)
    N.a(2, "4.2", "Unde s-a măsurat cea mai scăzută temperatură de pe Pământ?", "la stația Vostok, în Antarctica (−89,2 °C)", ["la Oimiakon (−67 °C)", "la Polul Nord", "pe Everest"], "Pe 21 iulie 1983.", surse=S_WMO)
    N.a(2, "1.2", "De ce Antarctica e considerată cel mai mare deșert?", "pentru că interiorul primește foarte puține precipitații", ["pentru că e plină de nisip", "pentru că e foarte caldă", "pentru că nu are gheață"], "Deșert înseamnă puține precipitații, nu neapărat căldură.")
    N.a(2, "2.1", "Care e cel mai înalt vârf din Antarctica?", "Masivul Vinson (4 892 m)", ["Erebus", "Everest", "Aconcagua"], "Vinson e în Munții Ellsworth.", surse=S_VINSON)
    N.a(2, "3.4", "Ce prevede Tratatul Antarctic?", "Antarctica e rezervată păcii și cercetării științifice", ["Antarctica aparține unei singure țări", "e permisă exploatarea minieră liberă", "e o bază militară"], "Semnat în 1959.", surse=S_TRAT)
    N.a(2, "3.4", "Ce stație de cercetare are România în Antarctica?", "Law-Racoviță, în colaborare cu Australia", ["Vostok", "McMurdo", "Amundsen–Scott"], "Poartă numele lui Emil Racoviță.")
    N.a(2, "3.4", "La ce expediție a participat Emil Racoviță?", "expediția belgiană „Belgica” (1897–1899)", ["expediția lui Amundsen", "expediția lui Scott", "Apollo 11"], "Prima expediție care a iernat în Antarctica.", surse=S_RAC)
    N.s(2, "3.3", "Asociază viețuitoarea cu rolul ei.", [("krillul", "hrana de bază pentru multe animale"), ("pinguinul imperial", "pasăre care nu zboară, clocește pe gheață"), ("balena albastră", "cel mai mare animal, se hrănește cu krill"), ("foca Weddell", "mamifer care trăiește sub gheață")], "Viața din Antarctica.")
    N.a(2, "2.1", "Ce ocean înconjoară Antarctica?", "Oceanul de Sud (Antarctic)", ["Oceanul Arctic", "Oceanul Indian de Nord", "Marea Mediterană"], "E format din apele sudice ale celorlalte oceane.")
    N.p(2, "2.1", "Atinge pe hartă Antarctica.", "lume", -80, 30, "Antarctica", 1500, "Antarctica e în jurul Polului Sud.")
    N.p(3, "2.1", "Atinge pe hartă Peninsula Antarctică, cea mai apropiată de America de Sud.", "lume", -68, -64, "Peninsula Antarctică", 700, "Peninsula se îndreaptă spre Țara de Foc.")
    N.p(3, "2.1", "Atinge pe hartă zona stației Vostok, unde s-a măsurat −89,2 °C.", "lume", -78.46, 106.84, "Vostok", 700, "Vostok e în interiorul Antarcticii de Est.", surse=S_WMO)
    N.a(2, "1.2", "Cine a ajuns primul la Polul Sud?", "Roald Amundsen, în 1911", ["Robert Scott, în 1912", "Emil Racoviță, în 1898", "James Cook, în 1770"], "Expediția lui Scott a ajuns la o lună după.")
    N.adev(2, "3.4", "Antarctica aparține unei singure țări.", False, "Fals: Tratatul Antarctic suspendă revendicările teritoriale.", surse=S_TRAT)
    N.adev(2, "3.3", "În Antarctica trăiesc urși polari.", False, "Fals: urșii polari trăiesc în Arctica; în Antarctica sunt pinguini.")
    N.adev(2, "1.2", "Antarctica are cea mai mare rezervă de apă dulce de pe Pământ, sub formă de gheață.", True, "Adevărat: aproape 70 % din apa dulce.", surse=S_ANT)
    N.l(2, "2.1", "Completează.", "Cea mai scăzută temperatură, −89,2 °C, s-a măsurat la stația [Vostok]; cel mai înalt vârf al Antarcticii este Masivul [Vinson].", ["McMurdo", "Erebus"], "Vostok, Vinson.", surse=S_WMO)
    N.l(2, "3.4", "Completează.", "Tratatul [Antarctic] a fost semnat în anul [1959].", ["Arctic", "1911"], "Tratatul Antarctic, 1959.", surse=S_TRAT)
    N.g(3, "2.3 4.1", "Graficul compară temperaturile minime record în trei locuri. Cu câte grade e mai rece recordul de la Vostok decât cel din România (Bod)?", grafic("bare", "Temperaturi minime record", [("Vostok (Antarctica)", -89.2), ("Oimiakon/Verhoiansk (Siberia)", -67.8), ("Bod (România)", -38.5)], "°C", "WMO; ANM"), "cu 50,7 grade", ["cu 38,5 grade", "cu 127,7 grade", "cu 21,4 grade"], "−38,5 − (−89,2) = 50,7.", surse=S_WMO)
    N.a(3, "4.3", "Compară Antarctica cu Arctica.", "Antarctica e un continent acoperit de gheață; Arctica e un ocean înghețat înconjurat de continente", ["sunt amândouă continente", "Arctica e un continent", "sunt identice"], "Diferență fundamentală.")
    N.a(2, "4.4", "De ce e important ca gheața Antarcticii să nu se topească?", "topirea ei ar crește mult nivelul oceanului planetar", ["ar face Pământul mai rece", "ar crea noi deșerturi doar în Antarctica", "nu ar avea niciun efect"], "Calota conține o cantitate uriașă de apă.")
    N.a(2, "3.3", "Ce studiază cercetătorii în Antarctica?", "clima trecutului din gheață, viața în condiții extreme, stratul de ozon, meteoriții", ["doar pinguinii", "nimic", "turismul de masă"], "Carotele de gheață arată clima de acum sute de mii de ani.")
    N.a(2, "3.3", "Ce s-a descoperit deasupra Antarcticii în anii '80?", "„gaura” din stratul de ozon", ["un nou continent", "o pădure tropicală", "un vulcan activ în Australia"], "Protocolul de la Montreal (1987) a interzis multe dintre substanțele care o produceau.")
    N.a(2, "2.1", "Ce vulcan activ se află în Antarctica?", "Erebus", ["Etna", "Fuji", "Kilimanjaro"], "Erebus are un lac de lavă.")
    N.d(2, "2.1", "Ce peninsulă a Antarcticii, cu multe stații de cercetare, e marcată pe hartă?", "lume", -68, -64, "Peninsula Antarctică", ["Țara de Foc", "Tasmania", "Capul Horn"], "E cea mai „caldă” parte a Antarcticii.")
    N.a(2, "4.4", "Ce reguli au turiștii care vizitează Antarctica?", "nu lasă deșeuri, nu ating animalele și păstrează distanța față de ele", ["pot vâna foci", "pot lua ouă de pinguin", "pot construi case"], "Mediul antarctic e foarte fragil.")
    N.a(3, "1.2", "De ce în Antarctica există zile și nopți polare?", "pentru că e dincolo de Cercul Polar de Sud, iar axa Pământului e înclinată", ["pentru că e lângă Ecuator", "pentru că Luna o acoperă", "fără motiv"], "Vara Soarele nu apune, iarna nu răsare.")
    N.a(2, "3.3", "Cum se numesc blocurile de gheață plate desprinse din platformele de gheață antarctice?", "aisberguri tabulare", ["morene", "dune", "fiorduri"], "Unele au sute de kilometri pătrați.")

    # ================================================================ S32 Expediție: unicitatea biogeografică australiană
    E = Expeditie(7, "VII-S32-studiu-caz-unicitatea-biogeografica", "Expediție: animalele unice ale Australiei",
                  "De ce cangurul și ornitorincul trăiesc doar în Australia?",
                  ref=REF.format("Studiu de caz: Unicitatea biogeografică australiană"))
    E.s(1, "4.1", "Asociază animalul cu ce îl face unic.", [("cangurul", "marsupial: puiul crește în marsupiu"), ("ornitorincul", "mamifer care depune ouă"), ("koala", "se hrănește aproape doar cu frunze de eucalipt"), ("emu", "pasăre mare care nu zboară")], "Fauna unică a Australiei.")
    E.a(2, "4.1", "Ce sunt marsupialele?", "mamifere ai căror pui cresc într-o pungă (marsupiu)", ["păsări care nu zboară", "pești de recif", "insecte"], "Cangurul, koala, vombatul.")
    E.pas("1. Fișa animalelor", "Alege 3 animale australiene unice și fă pentru fiecare o fișă: unde trăiește, ce mănâncă, de ce e special.",
          jurnal="Scrie fișele celor 3 animale.")
    E.a(2, "4.4", "De ce Australia are animale care nu există altundeva?", "s-a desprins de celelalte continente acum zeci de milioane de ani, iar speciile au evoluat izolat", ["pentru că e cea mai rece", "pentru că a fost populată recent", "pentru că animalele au fost aduse de oameni"], "Izolarea geografică.")
    E.a(2, "4.4", "Ce problemă au produs iepurii aduși în Australia de europeni?", "s-au înmulțit enorm și au distrus vegetația", ["au dispărut imediat", "au ajutat agricultura", "au mâncat cangurii"], "Speciile invazive dăunează celor locale.")
    E.pas("2. Specii invazive", "Află ce s-a întâmplat cu iepurii, broasca-țestoasă de trestie (cane toad) sau pisicile sălbatice în Australia.",
          jurnal="Scrie ce specie invazivă ai ales și ce probleme a produs.")
    E.a(2, "4.4", "Ce amenință Marea Barieră de Corali?", "încălzirea apei, care produce albirea coralilor", ["răcirea apei", "prea mulți pești", "zăpada"], "Marea Barieră e în patrimoniul UNESCO.", surse=S_GBR)
    E.pas("3. Marea Barieră de Corali", "Caută informații despre Marea Barieră de Corali: cât de lungă e, ce trăiește acolo, ce o amenință. Folosește site-ul UNESCO sau al Autorității Parcului Marin.",
          jurnal="Notează 3 informații și sursa.")
    E.pas("4. Posterul", "Realizează un poster „Australia – un continent unic”, cu harta, animalele alese și o soluție pentru protecția lor.",
          jurnal="Fotografiază posterul.", foto=True)

    return Unitate(7, "u4-australia-antarctica.json", "Australia și Oceania. Antarctica").add(A, B, O, N, E)
