from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VII-a, ediția 2024 (manuale.edu.ro), lecția „{}”"
S_AM = ["Encyclopaedia Britannica – North America / South America", "Wikipedia – North America / South America"]
S_ACON = ["Encyclopaedia Britannica – Aconcagua", "Wikipedia – Aconcagua"]
S_DENALI = ["U.S. Geological Survey (USGS), 2015 – Denali: 20 310 ft (6 190 m)", "National Park Service – Denali National Park"]
S_AMAZ = ["Encyclopaedia Britannica – Amazon River", "Wikipedia – Amazon River"]
S_MISS = ["Encyclopaedia Britannica – Mississippi River", "National Park Service – Mississippi River Facts"]
S_SUP = ["Encyclopaedia Britannica – Lake Superior", "U.S. EPA – Great Lakes Facts and Figures"]
S_TITI = ["Encyclopaedia Britannica – Lake Titicaca", "Wikipedia – Lake Titicaca"]
S_ANGEL = ["Encyclopaedia Britannica – Angel Falls", "Wikipedia – Angel Falls"]
S_BADW = ["National Park Service – Death Valley: Badwater Basin (−282 ft / −86 m)", "Encyclopaedia Britannica – Death Valley"]
S_WMO = ["WMO – World Weather and Climate Extremes Archive", "NOAA NCEI – Global extremes"]
S_PANAMA = ["Autoritatea Canalului Panama (pancanal.com) – istoric", "Encyclopaedia Britannica – Panama Canal"]
S_POP = ["ONU (UN DESA) – World Population Prospects 2024", "U.S. Census Bureau / IBGE (Brazilia) – recensăminte"]
S_UNESCO = ["UNESCO World Heritage Centre – lista patrimoniului mondial (whc.unesco.org)", "Encyclopaedia Britannica – Machu Picchu"]


def unitate():
    # ================================================================ S23a Poziția geografică
    P = Lectie(7, "VII-S23-caracterizare-geografica-pozitia-geografica", "America de Nord și America de Sud – poziția geografică",
               "De ce Columb credea că a ajuns în India?",
               [("Două continente", "America de Nord (aproximativ 24 de milioane km²) și America de Sud (aproximativ 18 milioane km²) se află în emisfera vestică. Sunt legate prin Istmul Panama, prin care s-a săpat Canalul Panama (deschis în 1914).\nAmerica de Nord se întinde de la Oceanul Arctic până la Istmul Panama. America de Sud e străbătută de Ecuator și se termină la Capul Horn."),
                ("Oceane și mări", "Oceanul Atlantic la est, Oceanul Pacific la vest, Oceanul Arctic la nordul Americii de Nord. Mări și golfuri: Golful Mexic, Marea Caraibilor, Golful Hudson, Golful Alaska.\nStrâmtoarea Bering desparte America de Nord de Asia; Strâmtoarea Drake desparte America de Sud de Antarctica."),
                ("Țărmuri", "America de Nord are țărmuri crestate, cu multe peninsule (Alaska, Labrador, Florida, California, Yucatán) și insule (Groenlanda – cea mai mare insulă de pe Pământ, Arhipelagul Arctic Canadian, Antilele).\nAmerica de Sud are țărmuri puțin crestate; în sud are fiorduri și Țara de Foc.")],
               stiaica="Groenlanda e cea mai mare insulă de pe Pământ. Geografic aparține Americii de Nord, dar politic face parte din Regatul Danemarcei.",
               ref=REF.format("Caracterizare geografică – Poziția geografică"), prefix="VII23a")
    P.a(1, "2.1", "În ce emisferă se află cele două Americi?", "emisfera vestică", ["emisfera estică", "doar emisfera sudică", "pe Ecuator, în întregime"], "La vest de meridianul de 0°.")
    P.a(2, "2.1", "Ce leagă America de Nord de America de Sud?", "Istmul Panama", ["Strâmtoarea Bering", "Strâmtoarea Drake", "Istmul Suez"], "Prin istm s-a săpat Canalul Panama.")
    P.a(2, "2.2", "Când a fost deschis Canalul Panama?", "în 1914", ["în 1492", "în 1869", "în 2001"], "Canalul leagă Atlanticul de Pacific.", surse=S_PANAMA)
    P.a(2, "2.1", "Care e cea mai mare insulă de pe Pământ?", "Groenlanda", ["Madagascar", "Marea Britanie", "Cuba"], "Groenlanda ține de Regatul Danemarcei.")
    P.a(2, "2.1", "Ce strâmtoare desparte America de Sud de Antarctica?", "Strâmtoarea Drake", ["Strâmtoarea Bering", "Strâmtoarea Gibraltar", "Strâmtoarea Magellan"], "E una dintre cele mai furtunoase mări.")
    P.e(2, "2.1", "Pune pe hartă oceanele din jurul celor două Americi.", [("atl", "Oceanul Atlantic", 20, -40), ("pac", "Oceanul Pacific", 10, -120), ("arc", "Oceanul Arctic", 80, -100)], "Atlantic la est, Pacific la vest, Arctic la nord.", harta="lume")
    P.p(2, "2.1", "Atinge pe hartă Canalul Panama.", "lume", 9.1, -79.7, "Canalul Panama", 300, "Canalul e în Panama, în America Centrală.", surse=S_PANAMA)
    P.p(2, "2.1", "Atinge pe hartă Golful Mexic.", "lume", 25, -90, "Golful Mexic", 600, "Golful Mexic e între SUA, Mexic și Cuba.")
    P.p(2, "2.1", "Atinge pe hartă Groenlanda.", "lume", 72, -40, "Groenlanda", 900, "Groenlanda e la nord-est de Canada.")
    P.p(3, "2.1", "Atinge pe hartă Capul Horn.", "lume", -55.98, -67.27, "Capul Horn", 500, "Capul Horn e la capătul sudic al Americii de Sud.")
    P.p(3, "2.1", "Atinge pe hartă Peninsula Florida.", "lume", 28, -81.5, "Florida", 400, "Florida e în sud-estul SUA.")
    P.s(2, "2.1", "Asociază peninsula cu țara.", [("Alaska", "SUA – în nord-vest"), ("Labrador", "Canada"), ("Yucatán", "Mexic"), ("Florida", "SUA – în sud-est")], "Peninsulele Americii de Nord.")
    P.a(2, "2.1", "Ce linie imaginară importantă străbate America de Sud?", "Ecuatorul", ["Cercul Polar de Nord", "meridianul de 0°", "Tropicul Racului"], "Ecuatorul trece prin Ecuador, Columbia, Brazilia.")
    P.a(2, "2.1", "Ce țară sud-americană poartă numele unei linii imaginare?", "Ecuador", ["Peru", "Chile", "Bolivia"], "Ecuador înseamnă „ecuator” în spaniolă.")
    P.a(2, "2.1", "Ce golf mare pătrunde în nordul Canadei?", "Golful Hudson", ["Golful Mexic", "Golful Biscaya", "Golful Persic"], "Golful Hudson îngheață iarna.")
    P.adev(2, "2.2", "Țărmurile Americii de Sud sunt mai crestate decât ale Americii de Nord.", False, "Fals: America de Nord are țărmuri mult mai crestate.")
    P.adev(2, "2.2", "America de Sud e mai mică decât America de Nord.", True, "Adevărat: aproximativ 18 față de 24 de milioane km².", surse=S_AM)
    P.l(2, "2.1", "Completează.", "Cele două Americi sunt legate prin Istmul [Panama]; America de Nord e despărțită de Asia prin Strâmtoarea [Bering].", ["Suez", "Drake"], "Panama, Bering.")
    P.l(2, "2.1", "Completează.", "Cea mai mare insulă de pe Pământ este [Groenlanda]; capătul sudic al Americii de Sud e Capul [Horn].", ["Cuba", "Bunei Speranțe"], "Groenlanda, Horn.")
    P.d(2, "2.1", "Ce insulă mare din Marea Caraibilor e marcată pe hartă?", "lume", 21.5, -79, "Cuba", ["Jamaica", "Haiti", "Puerto Rico"], "Cuba e cea mai mare insulă din Antile.")
    P.d(3, "2.1", "Ce peninsulă e marcată pe hartă?", "lume", 64, -153, "Alaska", ["Labrador", "Kamciatka", "Florida"], "Alaska e statul nordic al SUA.")
    P.o(3, "2.2 3.1 4.2", "Ordonează de la nord la sud.", ["Golful Hudson", "Marile Lacuri", "Golful Mexic", "Canalul Panama", "Ecuatorul", "Capul Horn"], "De la nord la sud", "De la Arctic spre Antarctica.")
    P.g(3, "2.3 4.1", "Graficul compară suprafețele (milioane km², rotunjit). Cu cât e mai mare America de Nord decât America de Sud?", grafic("bare", "Suprafața (milioane km², rotunjit)", [("America de Nord", 24), ("America de Sud", 18)], "milioane km²", "Encyclopaedia Britannica"), "cu aproximativ 6 milioane km²", ["cu 42 de milioane km²", "sunt egale", "cu 1 milion km²"], "24 − 18 = 6.", surse=S_AM)
    P.a(2, "1.2", "De ce Canalul Panama e important pentru comerț?", "scurtează mult drumul vapoarelor între Atlantic și Pacific", ["produce electricitate", "aduce apă de băut în SUA", "oprește uraganele"], "Vapoarele nu mai ocolesc America de Sud.")
    P.a(3, "4.3", "Compară poziția Americii de Sud cu a Africii.", "ambele sunt străbătute de Ecuator; America de Sud e în emisfera vestică, Africa în ambele", ["America de Sud e la pol", "Africa e toată în emisfera vestică", "niciuna nu are Ecuator"], "Asemănări climatice datorate Ecuatorului.")
    P.a(2, "2.1", "Ce arhipelag se află în Marea Caraibilor?", "Antilele", ["Filipinele", "Hawaii", "Maldivele"], "Cuba, Haiti, Jamaica, Puerto Rico fac parte din Antile.")
    P.a(2, "2.1", "Ce țară e cea mai mare din America de Nord?", "Canada", ["SUA", "Mexic", "Groenlanda"], "Canada e a doua țară ca mărime din lume.")
    P.a(2, "1.2", "De ce continentul se numește „America”?", "după numele navigatorului Amerigo Vespucci", ["după numele lui Columb", "după un râu", "după un munte"], "Vespucci a înțeles că e o „Lume Nouă”, nu Asia.")
    P.a(2, "2.1", "Ce insule, în Atlanticul de Sud, aparțin Regatului Unit?", "Insulele Falkland (Malvine)", ["Galápagos", "Hawaii", "Bermude"], "Sunt revendicate și de Argentina.")
    P.a(2, "2.1", "Ce arhipelag din Pacific, aparținând Ecuadorului, l-a inspirat pe Charles Darwin?", "Galápagos", ["Hawaii", "Antilele", "Falkland"], "Speciile unice au ajutat la teoria evoluției.")

    # ================================================================ S23b Relieful. Cordilieri-Anzi
    R = Lectie(7, "VII-S23-relieful-caracteristici-generale-sistemul", "Relieful Americilor. Sistemul cordiliero-andin",
               "Care e cel mai lung lanț de munți de pe uscat?",
               [("Sistemul cordiliero-andin", "Pe marginea vestică a celor două Americi se întinde un lanț uriaș de munți tineri: Cordilierii în America de Nord și Anzii în America de Sud. Anzii (aproximativ 7 000 km) sunt cel mai lung lanț de munți de pe uscat.\nS-au format prin coborârea plăcilor oceanice ale Pacificului sub plăcile continentale (subducție). De aceea aici sunt mulți vulcani și cutremure – Cercul de Foc al Pacificului."),
                ("Vârfuri și podișuri", "Cel mai înalt vârf din America de Sud și din emisfera vestică: Aconcagua (6 961 m), în Anzii argentinieni. Cel mai înalt din America de Nord: Denali (6 190 m), în Alaska.\nÎntre lanțurile munților sunt podișuri înalte: Podișul Mexicului, Altiplano (Bolivia, Peru), Marele Bazin (SUA)."),
                ("Estul Americilor", "La est sunt munți vechi (Apalași), podișuri vechi (Podișul Labrador, Podișul Braziliei, Podișul Guyanelor) și câmpii mari: Marile Câmpii și Câmpia Mississippi (America de Nord), Câmpia Amazonului, Câmpia Orinoco, Pampasul (America de Sud).\nValea Morții (SUA), la 86 m sub nivelul mării, e cel mai jos punct al Americii de Nord.")],
               stiaica="Marele Canion al râului Colorado, din SUA, are pe alocuri adâncimi de aproximativ 1 800 m; straturile lui de roci arată aproape două miliarde de ani de istorie a Pământului.",
               ref=REF.format("Relieful – caracteristici generale. Sistemul muntos cordiliero-andin"), prefix="VII23b")
    R.a(1, "2.1", "Care e cel mai lung lanț de munți de pe uscat?", "Anzii", ["Himalaya", "Alpii", "Uralii"], "Anzii au aproximativ 7 000 km.")
    R.a(2, "2.1", "Care e cel mai înalt vârf din America de Sud?", "Aconcagua (6 961 m)", ["Denali", "Chimborazo", "Kilimanjaro"], "Aconcagua e în Argentina.", surse=S_ACON)
    R.a(2, "2.1", "Care e cel mai înalt vârf din America de Nord?", "Denali (6 190 m)", ["Aconcagua", "Mount Whitney", "Popocatépetl"], "Denali e în Alaska.", surse=S_DENALI)
    R.a(2, "1.2", "Cum s-au format Anzii și Cordilierii?", "prin coborârea plăcilor oceanice sub plăcile continentale (subducție)", ["din ghețari", "din dune de nisip", "din coralieri"], "De aceea au vulcani și cutremure.")
    R.a(2, "2.2", "De ce vestul celor două Americi are mulți vulcani și cutremure?", "pentru că face parte din Cercul de Foc al Pacificului", ["pentru că e deșert", "pentru că e plat", "pentru că e lângă Polul Sud"], "Zonă de subducție.")
    R.s(2, "2.1", "Asociază unitatea de relief cu tipul ei.", [("Anzii", "munți tineri"), ("Apalașii", "munți vechi"), ("Podișul Braziliei", "podiș vechi"), ("Pampasul", "câmpie")], "Relieful celor două Americi.")
    R.s(2, "2.1", "Asociază unitatea de relief cu țara.", [("Marele Canion", "SUA"), ("Aconcagua", "Argentina"), ("Altiplano", "Bolivia și Peru"), ("Denali", "SUA (Alaska)")], "Locuri celebre.")
    R.p(2, "2.1", "Atinge pe hartă Munții Anzi.", "lume", -15, -72, "Anzii", 700, "Anzii sunt pe toată latura vestică a Americii de Sud.")
    R.p(2, "2.1", "Atinge pe hartă Munții Stâncoși (Cordilierii, SUA).", "lume", 42, -110, "Munții Stâncoși", 700, "Munții Stâncoși sunt în vestul SUA și Canadei.")
    R.p(2, "2.1", "Atinge pe hartă Aconcagua.", "lume", -32.65, -70.01, "Aconcagua", 400, "Aconcagua e în Argentina, lângă granița cu Chile.", surse=S_ACON)
    R.p(3, "2.1", "Atinge pe hartă Marele Canion.", "lume", 36.1, -112.1, "Marele Canion", 400, "Marele Canion e în statul Arizona.")
    R.p(3, "2.1", "Atinge pe hartă Munții Apalași.", "lume", 37, -81, "Apalașii", 600, "Apalașii sunt în estul SUA.")
    R.a(2, "2.1", "Ce munți vechi se află în estul SUA?", "Apalașii", ["Munții Stâncoși", "Anzii", "Sierra Nevada"], "Sunt munți vechi, erodați.")
    R.a(2, "2.1", "Care e cel mai jos punct al Americii de Nord?", "Valea Morții (−86 m)", ["Marele Canion", "Golful Mexic", "Lacul Superior"], "Badwater, în Valea Morții.", surse=S_BADW)
    R.a(2, "2.1", "Ce podiș înalt se află între două lanțuri ale Anzilor, în Bolivia și Peru?", "Altiplano", ["Podișul Braziliei", "Podișul Labrador", "Marele Bazin"], "Pe Altiplano e Lacul Titicaca.")
    R.a(2, "2.1", "Ce câmpie întinsă se află în Argentina?", "Pampasul", ["Marile Câmpii", "Câmpia Amazonului", "Câmpia Orinoco"], "Pampasul e o mare zonă agricolă.")
    R.adev(2, "2.2", "Munții din vestul Americilor sunt tineri, iar cei din est sunt vechi.", True, "Adevărat: Anzii și Cordilierii sunt tineri; Apalașii, vechi.")
    R.adev(2, "2.2", "Aconcagua e un vârf din Munții Stâncoși.", False, "Fals: e în Anzi, în Argentina.")
    R.l(2, "2.1", "Completează.", "Cel mai înalt vârf din America de Sud este [Aconcagua], iar din America de Nord este [Denali].", ["Everest", "Whitney"], "Aconcagua, Denali.")
    R.l(2, "1.2", "Completează.", "Râul [Colorado] a săpat Marele Canion; Munții [Apalași] sunt munți vechi din estul SUA.", ["Mississippi", "Anzi"], "Colorado, Apalași.")
    R.g(3, "2.3 4.1", "Profilul schematic arată relieful de la vest la est prin America de Sud, la latitudinea Perului. Unde e altitudinea cea mai mare?", grafic("profil", "Profil schematic: Pacific – Anzi – Amazonia – Atlantic", [("țărmul Pacificului", 0), ("Anzii", 6000), ("Altiplano", 3800), ("Câmpia Amazonului", 150), ("Podișul Braziliei", 900), ("țărmul Atlanticului", 0)], "m"), "în Anzi", ["în Câmpia Amazonului", "pe țărmul Atlanticului", "în Podișul Braziliei"], "Munții tineri sunt la vest.")
    R.o(3, "4.2 3.1", "Ordonează vârfurile de la cel mai înalt la cel mai jos.", ["Everest", "Aconcagua", "Denali", "Kilimanjaro", "Mont Blanc"], "Altitudine, descrescător", "8 848,86 / 6 961 / 6 190 / 5 895 / aproximativ 4 805 m.", surse=S_ACON)
    R.a(3, "4.3", "Compară Anzii cu Himalaya.", "ambii sunt munți tineri, dar Himalaya s-a format prin ciocnirea a două continente, iar Anzii prin subducția unei plăci oceanice", ["sunt munți vechi", "s-au format din ghețari", "sunt identici"], "Două tipuri de margini de plăci.")
    R.d(2, "2.1", "Ce munți vechi, foarte erodați, din estul Canadei și SUA, sunt marcați pe hartă?", "lume", 40, -78, "Apalașii", ["Munții Stâncoși", "Sierra Nevada", "Anzii"], "Apalașii au cărbune.")
    R.a(2, "2.1", "Ce câmpie mare se află între Munții Stâncoși și Mississippi?", "Marile Câmpii", ["Pampasul", "Câmpia Amazonului", "Câmpia Orinoco"], "Marile Câmpii sunt o zonă agricolă uriașă.")
    R.a(2, "2.1", "Ce vulcan mexican e activ, lângă Ciudad de México?", "Popocatépetl", ["Denali", "Aconcagua", "Fuji"], "Popocatépetl înseamnă „muntele care fumegă”.")
    R.a(2, "4.4", "Ce fenomen periculos amenință orașe ca San Francisco?", "cutremurele (falia San Andreas)", ["avalanșele de nisip", "taifunurile de zăpadă", "erupțiile de gheață"], "Falia San Andreas e granița dintre două plăci.")
    R.a(2, "2.2", "De ce Podișul Braziliei are altitudini mici, deși e vechi?", "pentru că a fost erodat milioane de ani", ["pentru că e tânăr", "pentru că e sub mare", "pentru că e vulcanic"], "Reliefurile vechi sunt tocite.")
    R.a(2, "2.1", "Ce vulcan din Ecuador, pe Ecuator, are vârful cel mai îndepărtat de centrul Pământului?", "Chimborazo", ["Aconcagua", "Denali", "Popocatépetl"], "Din cauza turtirii Pământului la poli.")
    R.a(2, "2.1", "Ce formă de relief a fost săpată de râul Colorado?", "Marele Canion", ["Valea Morții", "Golful Mexic", "Marile Lacuri"], "Un canion e o vale foarte adâncă cu pereți abrupți.")

    # ================================================================ S24a Hidrografia
    H = Lectie(7, "VII-S24-hidrografia-caracteristici-generale-fluvii", "Americile – hidrografia. Fluvii și lacuri",
               "Ce fluviu duce mai multă apă decât următoarele câteva fluvii mari la un loc?",
               [("Fluviile", "Amazonul e fluviul cu cea mai mare cantitate de apă și cu cel mai mare bazin hidrografic de pe Pământ; are peste 1 000 de afluenți. Lungimea lui, aproximativ 6 400 km, îl face al doilea sau chiar primul ca lungime, după metoda de măsurare.\nAlte fluvii: Mississippi–Missouri (SUA, spre Golful Mexic), Sfântul Laurențiu (din Marile Lacuri spre Atlantic), Mackenzie și Yukon (spre nord), Colorado, Orinoco, Paraná."),
                ("Lacurile", "Marile Lacuri (Superior, Michigan, Huron, Erie, Ontario), la granița SUA–Canada, formează cea mai mare suprafață de apă dulce de pe Pământ. Lacul Superior e cel mai mare lac de apă dulce ca suprafață. Între Erie și Ontario sunt Cascadele Niagara.\nLacul Titicaca (aproximativ 3 810 m altitudine), în Anzi, e cel mai înalt lac navigabil mare."),
                ("Cascadele", "Salto Angel (Venezuela), cu o cădere de 979 m, e cea mai înaltă cascadă de pe Pământ. Iguazú (la granița Argentinei cu Brazilia) e un șir de sute de cascade.")],
               stiaica="Gura de vărsare a Amazonului e atât de largă și duce atâta apă încât, la zeci de kilometri în largul Atlanticului, apa mării e aproape dulce.",
               ref=REF.format("Hidrografia – caracteristici generale. Fluvii și lacuri"), prefix="VII24a")
    H.a(1, "2.1", "Ce fluviu are cea mai mare cantitate de apă de pe Pământ?", "Amazonul", ["Nilul", "Mississippi", "Dunărea"], "Amazonul are și cel mai mare bazin.", surse=S_AMAZ)
    H.a(2, "2.1", "Unde se varsă Amazonul?", "în Oceanul Atlantic", ["în Oceanul Pacific", "în Golful Mexic", "în Marea Caraibilor"], "Amazonul curge de la Anzi spre est.")
    H.a(2, "2.1", "Unde se varsă Mississippi?", "în Golful Mexic", ["în Oceanul Pacific", "în Marile Lacuri", "în Golful Hudson"], "Mississippi formează o deltă lângă New Orleans.", surse=S_MISS)
    H.a(2, "2.1", "Ce fluviu duce apa Marilor Lacuri spre Atlantic?", "Sfântul Laurențiu", ["Mississippi", "Colorado", "Yukon"], "Fluviul trece pe lângă Montréal și Québec.")
    H.s(2, "2.1", "Asociază lacul sau cascada cu țara.", [("Lacul Titicaca", "Peru și Bolivia"), ("Salto Angel", "Venezuela"), ("Cascada Iguazú", "Argentina și Brazilia"), ("Cascadele Niagara", "SUA și Canada")], "Ape celebre.")
    H.a(2, "2.1", "Care e cel mai mare lac de apă dulce ca suprafață?", "Lacul Superior", ["Lacul Titicaca", "Lacul Baikal", "Lacul Victoria"], "Superior e unul dintre Marile Lacuri.", surse=S_SUP)
    H.a(2, "2.1", "Care e cea mai înaltă cascadă de pe Pământ?", "Salto Angel (979 m)", ["Niagara", "Iguazú", "Victoria"], "Salto Angel e în Venezuela.", surse=S_ANGEL)
    H.a(2, "2.1", "La ce altitudine se află Lacul Titicaca?", "aproximativ 3 810 m", ["aproximativ 381 m", "la nivelul mării", "aproximativ 8 000 m"], "E cel mai înalt lac navigabil mare.", surse=S_TITI)
    H.e(2, "2.1", "Pune pe hartă Marile Lacuri.", [("sup", "Lacul Superior", 47.7, -87.5), ("mic", "Lacul Michigan", 44, -87), ("hur", "Lacul Huron", 44.8, -82.4), ("eri", "Lacul Erie", 42.2, -81.2), ("ont", "Lacul Ontario", 43.7, -77.9)], "De la vest la est: Superior, Michigan, Huron, Erie, Ontario.", harta="lume")
    H.p(2, "2.1", "Atinge pe hartă vărsarea Amazonului.", "lume", -0.5, -50, "vărsarea Amazonului", 400, "Amazonul se varsă în Atlantic, în nordul Braziliei.", surse=S_AMAZ)
    H.p(2, "2.1", "Atinge pe hartă Delta Mississippi.", "lume", 29.2, -89.3, "Delta Mississippi", 400, "Lângă New Orleans.", surse=S_MISS)
    H.p(3, "2.1", "Atinge pe hartă Lacul Titicaca.", "lume", -15.8, -69.4, "Lacul Titicaca", 300, "Titicaca e la granița Peru–Bolivia.", surse=S_TITI)
    H.p(3, "2.1", "Atinge pe hartă Cascadele Niagara.", "lume", 43.08, -79.07, "Niagara", 300, "Între Lacul Erie și Lacul Ontario.")
    H.a(2, "2.2", "De ce Amazonul are atât de multă apă?", "bazinul lui primește ploi abundente tot anul, pe Ecuator", ["se topesc ghețari uriași", "e alimentat de mare", "nu are afluenți"], "Peste 1 000 de afluenți.")
    H.a(2, "2.2", "Cum s-au format Marile Lacuri?", "ghețarii uriași au săpat depresiuni care s-au umplut cu apă", ["prin erupții vulcanice", "le-au săpat oamenii", "din meteoriți"], "Sunt lacuri glaciare.")
    H.adev(2, "2.2", "Marile Lacuri au apă sărată.", False, "Fals: sunt cea mai mare suprafață de apă dulce de pe Pământ.")
    H.adev(2, "3.3", "Fluviul Mississippi e o cale de transport importantă în SUA.", True, "Adevărat: pe el circulă șlepuri cu cereale și mărfuri.")
    H.l(2, "2.1", "Completează.", "Între lacurile Erie și Ontario se află Cascadele [Niagara]; cea mai înaltă cascadă din lume este [Salto Angel].", ["Victoria", "Iguazú"], "Niagara, Salto Angel.")
    H.l(2, "2.1", "Completează.", "Amazonul se varsă în Oceanul [Atlantic], iar Mississippi în Golful [Mexic].", ["Pacific", "Hudson"], "Atlantic, Mexic.")
    H.g(3, "2.3 4.1", "Graficul compară debitul mediu al unor fluvii (mii m³/s, valori rotunjite). De câte ori e mai mare debitul Amazonului decât al Mississippi?", grafic("bare", "Debit mediu (mii m³/s, valori rotunjite)", [("Amazon", 209), ("Congo", 41), ("Mississippi", 17), ("Dunărea", 6.5)], "mii m³/s", "Encyclopaedia Britannica; ICPDR"), "de aproximativ 12 ori", ["de 2 ori", "la fel", "de 100 de ori"], "209 : 17 ≈ 12.", surse=S_AMAZ)
    H.o(3, "4.2 3.1", "Ordonează Marile Lacuri de la vest la est.", ["Superior", "Michigan", "Huron", "Erie", "Ontario"], "De la vest la est", "Apa curge de la Superior spre Ontario, apoi pe Sfântul Laurențiu.")
    H.d(2, "2.1", "Ce fluviu sud-american e marcat pe hartă, în Venezuela?", "lume", 8, -64, "Orinoco", ["Amazon", "Paraná", "Magdalena"], "Orinoco se varsă în Atlantic printr-o deltă.")
    H.a(2, "2.1", "Ce fluviu din Alaska curge spre Marea Bering?", "Yukon", ["Mackenzie", "Colorado", "Ohio"], "Yukon traversează Canada și Alaska.")
    H.a(2, "4.4", "De ce râul Colorado nu mai ajunge uneori la mare?", "apa lui e folosită aproape în întregime pentru orașe și irigații", ["s-a înghețat", "l-a acoperit un vulcan", "s-a schimbat clima brusc"], "Barajele și irigațiile îl secătuiesc.")
    H.a(2, "3.3", "Ce baraj mare de pe Paraná, între Brazilia și Paraguay, produce multă energie?", "Itaipu", ["Hoover", "Assuan", "Porțile de Fier"], "Itaipu e una dintre cele mai mari hidrocentrale.")
    H.a(2, "2.1", "Ce oraș mare e la vărsarea Mississippi?", "New Orleans", ["New York", "Chicago", "Los Angeles"], "New Orleans e un port important.")
    H.a(3, "2.2", "De ce Amazonul nu formează o deltă clasică, ca Nilul?", "curenții și mareele puternice ale Atlanticului împrăștie aluviunile", ["pentru că nu are aluviuni", "pentru că se varsă în Pacific", "pentru că e înghețat"], "La gura Amazonului sunt insule mari, ca Marajó.")
    H.a(2, "2.1", "Ce oraș canadian e pe fluviul Sfântul Laurențiu?", "Montréal", ["Vancouver", "Calgary", "Edmonton"], "Montréal e un mare port fluvial.")
    H.a(2, "3.4", "Ce cascadă celebră e în patrimoniul UNESCO, la granița Argentinei cu Brazilia?", "Iguazú", ["Niagara", "Salto Angel", "Victoria"], "Parcul Iguazú e patrimoniu natural.", surse=S_UNESCO)
    H.a(2, "2.1", "În ce țară e cea mai mare parte a bazinului Amazonului?", "Brazilia", ["Argentina", "Chile", "Mexic"], "Amazonul izvorăște din Anzii peruani.")

    # ================================================================ S24b Clima și biogeografia
    C = Lectie(7, "VII-S24-diferentieri-climatice-biogeografice", "Americile – climă, vegetație și faună",
               "Cum pot exista în aceeași Americă și cel mai uscat deșert, și cea mai mare pădure tropicală?",
               [("Clima", "Americile se întind de la Arctic aproape până la Antarctica, deci au aproape toate climatele: polar și subpolar (nordul Canadei, Alaska), temperat (SUA, Canada de Sud, Argentina), subtropical și mediteranean (California, centrul Chile), tropical-deșertic (Mexic de nord, Atacama), ecuatorial (Amazonia).\nÎn America de Nord, relieful (munți la vest și la est, câmpii la mijloc) lasă aerul rece din nord și cel cald din sud să se întâlnească: apar tornade puternice. Pe țărmul Golfului Mexic lovesc uraganele."),
                ("Extreme", "Deșertul Atacama (Chile) e unul dintre cele mai uscate locuri de pe Pământ: în unele zone nu a plouat ani la rând.\nÎn Valea Morții (SUA) s-a înregistrat oficial cea mai ridicată temperatură a aerului: 56,7 °C, pe 10 iulie 1913."),
                ("Vegetația și fauna", "Tundra (nordul Canadei): reni (caribu), boi moscați, urși polari. Taigaua: urși grizzly, elani, castori. Preriile (stepa nord-americană), azi cultivate; bizonii. Deșerturile: cactuși uriași (saguaro), șerpi cu clopoței. Pădurea amazoniană (cea mai mare pădure tropicală): jaguari, maimuțe, papagali, anaconde, leneși. Pampasul: ierburi; Anzii: lame, alpaca, condori.")],
               stiaica="Pădurea amazoniană e numită uneori „plămânul planetei”, dar și ea respiră: o mare parte din oxigenul pe care îl produce e consumat chiar de pădure.",
               ref=REF.format("Diferențieri climatice și biogeografice"), prefix="VII24b")
    C.s(1, "2.2", "Asociază climatul cu regiunea.", [("polar", "nordul Canadei"), ("mediteranean", "California și centrul Chile"), ("tropical-deșertic", "Atacama"), ("ecuatorial", "Amazonia")], "Climatele Americilor.")
    C.a(1, "2.2", "Ce deșert din Chile e unul dintre cele mai uscate locuri de pe Pământ?", "Atacama", ["Sahara", "Gobi", "Kalahari"], "În unele zone nu a plouat ani la rând.")
    C.a(1, "4.2", "Unde s-a înregistrat cea mai ridicată temperatură a aerului de pe Pământ?", "în Valea Morții, SUA (56,7 °C)", ["în Sahara", "în Atacama", "în Amazonia"], "Pe 10 iulie 1913.", surse=S_WMO)
    C.a(2, "2.2", "De ce în SUA apar multe tornade?", "aerul rece din nord și cel cald și umed din sud se întâlnesc deasupra câmpiilor", ["pentru că e deșert", "pentru că e lângă pol", "pentru că sunt vulcani"], "Câmpiile centrale sunt numite „Aleea tornadelor”.")
    C.a(2, "2.2", "Ce furtuni tropicale lovesc țărmul Golfului Mexic?", "uraganele", ["musonii", "viscolele", "harmattanul"], "Uraganele se formează deasupra apelor calde ale oceanului.")
    C.s(2, "3.3", "Asociază animalul cu zona.", [("jaguarul", "pădurea amazoniană"), ("bizonul", "preria"), ("lama", "Anzii"), ("caribu", "tundra")], "Fauna Americilor.")
    C.a(2, "3.3", "Ce animale din Anzi sunt crescute pentru lână?", "lama și alpaca", ["bizonul și elanul", "jaguarul și puma", "castorul și ratonul"], "Lâna de alpaca e foarte fină.")
    C.a(2, "3.3", "Ce sunt preriile?", "întinderi cu ierburi din centrul Americii de Nord, azi în mare parte cultivate", ["păduri tropicale", "deșerturi de gheață", "munți înalți"], "Pe prerii trăiau milioane de bizoni.")
    C.a(2, "3.3", "Care e cea mai mare pădure tropicală de pe Pământ?", "pădurea amazoniană", ["pădurea Congo", "taigaua", "pădurea din Borneo"], "Amazonia se întinde în nouă țări.")
    C.a(2, "3.3", "Ce cactus uriaș e simbolul deșerturilor din sud-vestul SUA și Mexic?", "saguaro", ["baobabul", "molidul", "bambusul"], "Saguaro poate trăi peste 150 de ani.")
    C.p(2, "2.1", "Atinge pe hartă deșertul Atacama.", "lume", -24, -69.5, "Atacama", 500, "Atacama e în nordul Chile.")
    C.p(2, "2.1", "Atinge pe hartă Valea Morții.", "lume", 36.5, -117, "Valea Morții", 400, "Valea Morții e în California.", surse=S_BADW)
    C.p(3, "2.1", "Atinge pe hartă Pampasul argentinian.", "lume", -35, -62, "Pampasul", 600, "Pampasul e în jurul orașului Buenos Aires.")
    C.a(2, "4.4", "Ce amenință pădurea amazoniană?", "defrișările pentru pășuni, culturi de soia și exploatarea lemnului", ["zăpada", "frigul polar", "lipsa ploii totală"], "Incendiile sunt folosite pentru curățarea terenului.")
    C.a(2, "3.3", "Ce animal din taiga construiește baraje pe râuri?", "castorul", ["jaguarul", "lama", "condorul"], "Castorul e simbolul Canadei.")
    C.adev(2, "2.2", "În America de Nord, munții orientați de la nord la sud lasă aerul rece și cel cald să circule liber prin câmpiile centrale.", True, "Adevărat: de aceea apar tornade și ierni geroase până în sud.")
    C.adev(2, "3.3", "Lamele trăiesc în pădurea amazoniană.", False, "Fals: trăiesc în Anzi, la altitudini mari.")
    C.l(2, "2.2", "Completează.", "Cel mai uscat deșert e [Atacama], iar cea mai mare pădure tropicală e pădurea [amazoniană].", ["Sahara", "siberiană"], "Atacama, amazoniană.")
    C.l(2, "3.3", "Completează.", "Pe prerii trăiau milioane de [bizoni]; în Anzi zboară [condorul].", ["pinguini", "vulturul pleșuv"], "Bizoni, condor.")
    C.g(3, "2.3 4.1", "Graficul arată suprafața defrișată anual într-o zonă imaginară din Amazonia. Ce observi?", grafic("profil", "Suprafață defrișată pe an (date imaginare)", [("2016", 8), ("2018", 9), ("2020", 12), ("2022", 11), ("2024", 7)], "mii km²"), "defrișarea a crescut până în 2020, apoi a scăzut", ["a crescut mereu", "a scăzut mereu", "a fost aceeași"], "Politicile de protecție pot reduce defrișările.")
    C.a(3, "4.3", "Compară clima Californiei cu cea a Chile centrale.", "ambele au climat mediteranean, pe țărmul Pacificului, în emisfere diferite", ["sunt polare", "sunt ecuatoriale", "nu au nimic în comun"], "Simetrie față de Ecuator.")
    C.a(2, "2.2", "De ce Atacama e atât de uscat?", "curentul rece al Perului răcește aerul, iar Anzii opresc ploile din est", ["pentru că e lângă Ecuator și plouă", "pentru că e muntos și umed", "pentru că bate musonul"], "Două bariere împotriva ploii.")
    C.d(2, "2.1", "Ce stat american, cu climat mediteranean și pădurile de sequoia, e marcat pe hartă?", "lume", 37, -120, "California", ["Texas", "Florida", "Alaska"], "California e pe țărmul Pacificului.")
    C.a(2, "3.3", "Ce copaci uriași, printre cei mai înalți din lume, cresc în California?", "sequoia", ["baobabii", "palmierii", "mestecenii"], "Unele sequoia au peste 100 m.")
    C.a(2, "3.3", "Ce pasăre e simbolul SUA?", "vulturul pleșuv", ["condorul", "papagalul", "colibri"], "Apare pe stema SUA.")
    C.a(2, "3.3", "Ce animal lent trăiește în copacii pădurii amazoniene?", "leneșul", ["bizonul", "lama", "elanul"], "Leneșul coboară foarte rar din copac.")
    C.a(2, "3.3", "Ce șarpe uriaș trăiește în apele Amazoniei?", "anaconda", ["cobra regală", "vipera", "șarpele cu clopoței"], "Anaconda verde e unul dintre cei mai grei șerpi.")
    C.a(3, "2.2", "De ce în Canada iernile sunt mai reci decât în Europa, la aceeași latitudine?", "Canada e expusă aerului arctic, iar țărmul estic e răcit de curentul rece al Labradorului", ["pentru că e mai aproape de Ecuator", "pentru că are Golfstromul", "fără motiv"], "Europa de Vest e încălzită de Golfstrom.")
    C.a(2, "4.4", "Ce poate face lumea pentru protejarea Amazoniei?", "arii protejate, oprirea defrișărilor ilegale, sprijinirea popoarelor indigene", ["mai multe incendii", "mai multe drumuri prin pădure", "nimic"], "Popoarele indigene protejează pădurea.")
    C.a(2, "3.3", "Ce pasăre mică poate zbura și înapoi și pe loc, în America?", "colibri", ["condorul", "pinguinul", "struțul"], "Colibri bate din aripi foarte repede.")

    # ================================================================ S25 Diversitatea umană
    D = Lectie(7, "VII-S25-elemente-diversitate-umana-etnica", "Americile – diversitatea umană",
               "De ce în America de Sud se vorbește spaniola și portugheza?",
               [("Popoarele", "Primii locuitori au venit din Asia, peste Strâmtoarea Bering, acum peste 15 000 de ani. Ei au creat mari civilizații: mayașii (Peninsula Yucatán), aztecii (Mexic), incașii (Anzi).\nDupă 1492 au venit europenii (spanioli, portughezi, englezi, francezi), apoi africanii aduși cu forța ca sclavi. Mai târziu au venit imigranți din toată lumea. Din amestecul lor au rezultat metișii și mulatrii."),
                ("Limbi și religii", "Limbi: engleza (SUA, Canada), franceza (Québec, Haiti), spaniola (Mexic și cea mai mare parte a Americii de Sud), portugheza (Brazilia). Se vorbesc și limbi indigene: quechua, guarani, aymara, nahuatl.\nReligia majoritară e creștinismul: catolic în America Latină și Québec, protestant mai ales în SUA și Canada."),
                ("America Latină și America Anglo-Saxonă", "America Latină cuprinde țările unde se vorbesc limbi romanice (spaniola, portugheza, franceza): Mexic, America Centrală, Caraibe, America de Sud. America Anglo-Saxonă: SUA și Canada.")],
               stiaica="Machu Picchu, orașul incaș construit pe un munte din Anzii peruani, a fost înscris în patrimoniul UNESCO în 1983.",
               ref=REF.format("Elemente de diversitate umană"))
    D.a(1, "3.3", "De unde au venit primii locuitori ai Americilor?", "din Asia, peste Strâmtoarea Bering", ["din Europa, cu Columb", "din Africa, pe mare", "din Australia"], "Acum peste 15 000 de ani.")
    D.s(2, "3.3", "Asociază civilizația cu regiunea.", [("mayașii", "Peninsula Yucatán"), ("aztecii", "Podișul Mexicului"), ("incașii", "Anzi (Peru)")], "Marile civilizații precolumbiene.")
    D.a(2, "3.3", "Ce limbă se vorbește în Brazilia?", "portugheza", ["spaniola", "engleza", "franceza"], "Brazilia a fost colonie portugheză.")
    D.a(2, "3.3", "Ce limbă se vorbește în Mexic?", "spaniola", ["portugheza", "engleza", "franceza"], "Mexicul are cei mai mulți vorbitori de spaniolă din lume.")
    D.a(2, "3.3", "În ce provincie canadiană se vorbește mai ales franceza?", "Québec", ["Ontario", "Alberta", "Columbia Britanică"], "Canada are două limbi oficiale.")
    D.a(2, "3.3", "Ce înseamnă America Latină?", "țările americane unde se vorbesc limbi romanice (spaniolă, portugheză, franceză)", ["SUA și Canada", "doar Brazilia", "insulele din Pacific"], "Limbile provin din latină.")
    D.a(2, "3.3", "Ce limbă indigenă e vorbită de milioane de oameni în Anzi?", "quechua", ["swahili", "hindi", "zulu"], "Era limba Imperiului Incaș.")
    D.a(2, "3.3", "Ce religie e majoritară în America Latină?", "creștinismul catolic", ["islamul", "budismul", "hinduismul"], "Adus de spanioli și portughezi.")
    D.a(2, "3.3", "Cine sunt metișii?", "urmașii din amestecul europenilor cu populațiile indigene", ["urmașii doar ai europenilor", "imigranți asiatici", "popoare din Arctica"], "Sunt majoritari în multe țări din America Latină.")
    D.p(2, "2.1", "Atinge pe hartă Machu Picchu.", "lume", -13.16, -72.55, "Machu Picchu", 400, "Machu Picchu e în Anzii peruani.", surse=S_UNESCO)
    D.p(2, "2.1", "Atinge pe hartă Peninsula Yucatán, unde au trăit mayașii.", "lume", 20, -89, "Yucatán", 400, "Yucatán e în sud-estul Mexicului.")
    D.p(3, "2.1", "Atinge pe hartă Québec.", "lume", 47, -71.5, "Québec", 700, "Québec e în estul Canadei.")
    D.adev(2, "3.3", "În toată America de Sud se vorbește portugheza.", False, "Fals: portugheza doar în Brazilia; în majoritatea celorlalte țări, spaniola.")
    D.adev(2, "3.3", "Africanii au fost aduși în America cu forța, ca sclavi, între secolele XVI și XIX.", True, "Adevărat: comerțul cu sclavi a marcat istoria Americilor.")
    D.l(2, "3.3", "Completează.", "În Brazilia se vorbește [portugheza], iar în Argentina [spaniola].", ["engleza", "franceza"], "Moștenirea colonială.")
    D.l(2, "3.4", "Completează.", "Orașul incaș [Machu Picchu] e în Anzii din [Peru].", ["Teotihuacan", "Mexic"], "Machu Picchu, Peru.", surse=S_UNESCO)
    D.g(3, "2.3 4.1", "Graficul arată (schematic) limbile principale vorbite în cele două Americi. Ce limbă au cei mai mulți vorbitori?", grafic("structura", "Limbi principale în Americi (aproximativ)", [("spaniola", 42), ("engleza", 35), ("portugheza", 20), ("altele", 3)], "%"), "spaniola", ["engleza", "portugheza", "franceza"], "Spaniola e vorbită în cele mai multe țări.", surse=["Instituto Cervantes – El español: una lengua viva (2024)", "Ethnologue – languages of the Americas"])
    D.a(3, "4.3", "Compară colonizarea Americii de Nord cu a Americii de Sud.", "nordul a fost colonizat mai ales de englezi și francezi, sudul de spanioli și portughezi", ["toată America a fost colonizată de englezi", "nicio parte nu a fost colonizată", "sudul de englezi, nordul de spanioli"], "De aici diferențele de limbă și religie.")
    D.a(2, "3.4", "Ce piramide mari construite de azteci și de popoarele dinaintea lor sunt lângă Ciudad de México?", "Teotihuacan", ["Gizeh", "Machu Picchu", "Chichén Itzá"], "Piramida Soarelui e una dintre cele mai mari.")
    D.a(2, "3.4", "Ce oraș mayaș din Yucatán, cu piramida Kukulcán, e în patrimoniul UNESCO?", "Chichén Itzá", ["Machu Picchu", "Cuzco", "Teotihuacan"], "Chichén Itzá e în Mexic.", surse=S_UNESCO)
    D.a(2, "3.3", "Ce sărbătoare mexicană îi onorează pe cei dragi care au murit?", "Ziua Morților (Día de Muertos)", ["Halloween", "Crăciunul", "Ziua Recunoștinței"], "E în patrimoniul imaterial UNESCO.")
    D.a(2, "3.3", "Ce dans e simbolul Argentinei?", "tangoul", ["samba", "flamenco", "valsul"], "Tangoul s-a născut la Buenos Aires.")
    D.a(2, "3.3", "Ce dans și carnaval sunt simbolul Braziliei?", "samba și Carnavalul de la Rio", ["tangoul", "polka", "Călușul"], "Carnavalul de la Rio e celebru în lume.")
    D.d(2, "2.1", "Ce țară, cu cea mai mare populație vorbitoare de spaniolă, e marcată pe hartă?", "lume", 23.6, -102.5, "Mexic", ["Spania", "Argentina", "Columbia"], "Mexicul are peste 120 de milioane de locuitori.")
    D.a(2, "3.3", "Cum se numesc popoarele indigene din Arctica americană?", "inuiți", ["incași", "azteci", "mayași"], "Inuiții trăiesc în Canada, Alaska și Groenlanda.")
    D.a(2, "3.3", "Ce înseamnă „indigen”?", "care trăiește de la început într-un loc, înaintea colonizatorilor", ["venit recent", "turist", "străin"], "Popoarele indigene au drepturi speciale protejate.")
    D.a(3, "1.2", "De ce SUA sunt numite „țară a imigranților”?", "cei mai mulți locuitori sunt urmașii unor oameni veniți din toată lumea", ["pentru că nimeni nu s-a născut acolo", "pentru că e interzis să te naști acolo", "pentru că nu au popoare indigene"], "Diversitatea etnică e foarte mare.")
    D.a(2, "3.3", "Ce limbă oficială are Haiti, alături de creola haitiană?", "franceza", ["spaniola", "portugheza", "engleza"], "Haiti a fost colonie franceză.")
    D.a(2, "3.4", "Ce oraș din Peru a fost capitala Imperiului Incaș?", "Cuzco", ["Lima", "Quito", "La Paz"], "Cuzco e în patrimoniul UNESCO.", surse=S_UNESCO)

    D.a(2, "3.3", "Ce sărbătoare americană, din noiembrie, are rădăcini în primii coloniști englezi?", "Ziua Recunoștinței (Thanksgiving)", ["Ziua Morților", "Carnavalul", "Anul Nou Chinezesc"], "Se sărbătorește în SUA și Canada.")

    # ================================================================ S26a Harta politică. Contraste
    K = Lectie(7, "VII-S26-harta-politica-contraste-teritoriale", "Americile – harta politică. Contraste între state",
               "Ce deosebește SUA de Haiti, deși sunt pe același continent?",
               [("Statele", "America de Nord cuprinde: Canada, SUA, Mexic, statele Americii Centrale (Guatemala, Costa Rica, Panama etc.) și ale Caraibelor (Cuba, Jamaica, Haiti, Republica Dominicană). Groenlanda ține de Danemarca.\nAmerica de Sud are 12 state independente: Brazilia (cel mai mare), Argentina, Peru, Columbia, Bolivia, Venezuela, Chile, Paraguay, Ecuador, Guyana, Uruguay, Surinam; Guyana Franceză aparține Franței."),
                ("Contraste", "SUA și Canada sunt țări foarte dezvoltate, cu venituri mari. Multe state din America Latină sunt în dezvoltare, cu mari diferențe între bogați și săraci. Haiti e cea mai săracă țară din emisfera vestică.\nBrazilia, Mexicul, Argentina și Chile au economii mari, dar și regiuni sărace."),
                ("Organizații", "Statele colaborează în organizații: OSA (Organizația Statelor Americane), Mercosur (piața comună din sudul Americii de Sud), acordul comercial dintre SUA, Mexic și Canada.")],
               stiaica="Chile are o formă foarte alungită: lung de peste 4 000 km, dar lat, în medie, de doar aproximativ 180 km.",
               ref=REF.format("Harta politică și contraste teritoriale între state"), prefix="VII26a")
    K.s(1, "2.1", "Asociază statul cu capitala.", [("SUA", "Washington"), ("Canada", "Ottawa"), ("Mexic", "Ciudad de México"), ("Cuba", "Havana")], "Capitale nord-americane.")
    K.s(1, "2.1", "Asociază statul cu capitala.", [("Brazilia", "Brasília"), ("Argentina", "Buenos Aires"), ("Peru", "Lima"), ("Chile", "Santiago")], "Capitale sud-americane.")
    K.a(1, "2.1", "Care e cel mai mare stat din America de Sud?", "Brazilia", ["Argentina", "Peru", "Chile"], "Brazilia ocupă aproape jumătate din continent.")
    K.a(2, "2.1", "Câte state independente are America de Sud?", "12", ["3", "27", "54"], "Guyana Franceză aparține Franței.")
    K.a(2, "2.1", "Care e capitala Braziliei?", "Brasília", ["Rio de Janeiro", "São Paulo", "Salvador"], "Brasília a fost construită în anii 1950 ca o capitală nouă.")
    K.a(2, "2.1", "Care e capitala Canadei?", "Ottawa", ["Toronto", "Montréal", "Vancouver"], "Toronto e cel mai mare oraș.")
    K.a(2, "4.3", "Ce țară din emisfera vestică are cele mai mici venituri?", "Haiti", ["Canada", "SUA", "Chile"], "Haiti a fost lovită și de cutremure puternice.")
    K.a(2, "4.3", "Ce state americane sunt foarte dezvoltate?", "SUA și Canada", ["Haiti și Bolivia", "Honduras și Nicaragua", "Paraguay și Guyana"], "Venituri mari, economie diversificată.")
    K.a(2, "1.1", "Ce este Mercosur?", "o piață comună a unor state din sudul Americii de Sud", ["un munte", "un fluviu", "un oraș"], "Membri: Brazilia, Argentina, Uruguay, Paraguay și alții.")
    K.p(2, "2.1", "Atinge pe hartă Chile.", "lume", -30, -71, "Chile", 900, "Chile e o fâșie lungă între Anzi și Pacific.")
    K.p(2, "2.1", "Atinge pe hartă Brazilia.", "lume", -10, -52, "Brazilia", 1200, "Brazilia e în estul Americii de Sud.")
    K.p(3, "2.1", "Atinge pe hartă Haiti.", "lume", 19, -72.5, "Haiti", 300, "Haiti ocupă vestul insulei Hispaniola.")
    K.p(3, "2.1", "Atinge pe hartă Washington.", "lume", 38.9, -77, "Washington", 300, "Washington e pe coasta de est a SUA.")
    K.adev(2, "4.3", "Toate statele americane au același nivel de dezvoltare.", False, "Fals: contrastele sunt mari, de la SUA la Haiti.")
    K.adev(2, "2.1", "Brasília e capitala Braziliei, nu Rio de Janeiro.", True, "Adevărat: din 1960.")
    K.l(2, "2.1", "Completează.", "Capitala SUA este [Washington], iar capitala Argentinei este [Buenos Aires].", ["New York", "Córdoba"], "Washington, Buenos Aires.")
    K.l(2, "2.1", "Completează.", "Cel mai mare stat al Americii de Sud este [Brazilia]; cel mai alungit stat este [Chile].", ["Argentina", "Peru"], "Brazilia, Chile.")
    K.g(3, "2.3 4.1", "Graficul compară speranța de viață în trei țări americane (ani, valori rotunjite). Ce arată?", grafic("bare", "Speranța de viață (ani, valori rotunjite)", [("Canada", 82), ("Brazilia", 76), ("Haiti", 64)], "ani", "Banca Mondială – Life expectancy at birth"), "contraste mari între țări", ["toate au aceeași speranță de viață", "Haiti are cea mai mare", "Brazilia are cea mai mică"], "Diferența Canada–Haiti e de aproximativ 18 ani.", surse=["Banca Mondială – Life expectancy at birth, total (years)", "OMS – Global Health Observatory"])
    K.o(3, "2.2 3.1 4.2", "Ordonează capitalele de la nord la sud.", ["Ottawa", "Washington", "Ciudad de México", "Lima", "Santiago"], "De la nord la sud", "De la Canada spre Chile.")
    K.d(2, "2.1", "Ce stat fără ieșire la mare, din Anzi, e marcat pe hartă?", "lume", -17, -65, "Bolivia", ["Peru", "Paraguay", "Ecuador"], "Bolivia are două capitale: La Paz (sediul guvernului) și Sucre.")
    K.a(3, "4.3", "De ce în multe țări latino-americane există diferențe mari între bogați și săraci?", "moștenirea colonială, pământul concentrat în mâinile puținora și acces inegal la educație", ["pentru că toți sunt bogați", "pentru că nu au resurse", "pentru că e frig"], "Inegalitatea e o problemă importantă.")
    K.a(2, "2.1", "Ce state din America Centrală sunt cunoscute pentru natură și ecoturism?", "Costa Rica", ["Haiti", "Cuba", "Groenlanda"], "Costa Rica protejează peste un sfert din teritoriu.")
    K.a(2, "2.1", "Ce stat sud-american e străbătut de Ecuator și îi poartă numele?", "Ecuador", ["Peru", "Chile", "Uruguay"], "Capitala, Quito, e aproape de Ecuator.")
    K.a(2, "2.1", "Ce teritoriu din America de Sud aparține Franței?", "Guyana Franceză", ["Surinam", "Guyana", "Falkland"], "Aici e baza spațială europeană de la Kourou.")
    K.a(2, "4.3", "Prin ce se deosebesc SUA de Mexic?", "SUA au venituri medii mult mai mari și o economie mai diversificată", ["Mexicul e mai bogat", "sunt identice", "SUA nu au industrie"], "Granița SUA–Mexic e una dintre cele mai traversate.")
    K.a(2, "1.1", "Ce înseamnă stat federal, ca SUA sau Brazilia?", "un stat format din mai multe state sau provincii care au propriile guverne", ["un stat fără guvern", "o colonie", "un oraș-stat"], "SUA au 50 de state.")
    K.a(2, "2.1", "Câte state are SUA?", "50", ["13", "27", "100"], "Alaska și Hawaii au fost ultimele, în 1959.")
    K.a(2, "2.1", "Ce stat sud-american e cel mai mic ca suprafață, cu capitala la Paramaribo?", "Surinam", ["Uruguay", "Paraguay", "Ecuador"], "Surinamul a fost colonie olandeză.")
    K.a(3, "4.3", "Ce au în comun Canada și Brazilia?", "sunt state foarte mari, cu resurse bogate și populație concentrată pe o mică parte din teritoriu", ["sunt mici", "au aceeași limbă", "sunt în aceeași emisferă nord–sud"], "Canada în sud, Brazilia pe coasta de est.")

    K.a(2, "2.1", "Ce țară din Caraibe împarte insula Hispaniola cu Haiti?", "Republica Dominicană", ["Cuba", "Jamaica", "Puerto Rico"], "Hispaniola e a doua insulă ca mărime din Antile.")

    # ================================================================ S26b Forme de aglomerare urbană
    U = Lectie(7, "VII-S26-forme-aglomerare-urbana", "Americile – forme de aglomerare urbană",
               "Ce este o megalopolă?",
               [("Urbanizare puternică", "Americile sunt foarte urbanizate: în SUA, Canada, Argentina, Chile, Brazilia, peste 8 din 10 oameni trăiesc la oraș.\nMari orașe: New York, Los Angeles, Chicago, Toronto, Ciudad de México, São Paulo, Rio de Janeiro, Buenos Aires, Lima, Bogotá."),
                ("Forme de aglomerare", "Aglomerarea urbană: un oraș mare și localitățile lipite de el. Zona metropolitană: orașul și împrejurimile legate prin navetă.\nMegalopola: un șir de orașe mari care se unesc între ele. Exemplul clasic e „BosWash”, de la Boston la Washington (prin New York, Philadelphia, Baltimore), pe coasta de est a SUA."),
                ("Probleme", "Orașele latino-americane au crescut foarte repede; la margine au apărut cartiere sărace: favelas în Brazilia, villas miseria în Argentina. Probleme: trafic, poluare, criminalitate, lipsa locuințelor.\nOrașele din SUA s-au extins mult în suburbii, ceea ce crește folosirea mașinii.")],
               stiaica="Ciudad de México e construit pe locul fostei capitale aztece Tenochtitlan, ridicată pe o insulă dintr-un lac. Din această cauză, unele clădiri se scufundă încet în solul moale.",
               ref=REF.format("Forme de aglomerare urbană"), prefix="VII26b")
    U.a(1, "1.1", "Ce este o megalopolă?", "un șir de orașe mari care s-au unit între ele", ["un sat mare", "un oraș mic", "un parc național"], "Exemplu: BosWash, în SUA.")
    U.a(2, "2.1", "Ce orașe formează megalopola BosWash?", "Boston, New York, Philadelphia, Baltimore, Washington", ["Los Angeles și San Francisco", "Toronto și Montréal", "Rio și São Paulo"], "Pe coasta de est a SUA.")
    U.s(2, "1.1", "Asociază forma de aglomerare cu definiția.", [("aglomerare urbană", "orașul și localitățile lipite de el"), ("zonă metropolitană", "orașul și împrejurimile legate prin navetă"), ("megalopolă", "șir de orașe mari unite"), ("suburbie", "cartier de locuințe la marginea orașului")], "Forme urbane.")
    U.a(2, "3.3", "Ce sunt favelele?", "cartiere sărace de la marginea orașelor din Brazilia", ["cartiere de lux", "parcuri", "centre de afaceri"], "Favelele de pe dealurile din Rio sunt cunoscute.")
    U.s(2, "2.1", "Asociază orașul cu țara.", [("São Paulo", "Brazilia"), ("Toronto", "Canada"), ("Bogotá", "Columbia"), ("Chicago", "SUA")], "Orașe mari ale Americilor.")
    U.p(2, "2.1", "Atinge pe hartă New York.", "lume", 40.7, -74, "New York", 300, "New York e pe coasta de est a SUA.")
    U.p(2, "2.1", "Atinge pe hartă Ciudad de México.", "lume", 19.43, -99.13, "Ciudad de México", 300, "Capitala Mexicului e pe un podiș înalt.")
    U.p(2, "2.1", "Atinge pe hartă São Paulo.", "lume", -23.55, -46.63, "São Paulo", 300, "São Paulo e cel mai mare oraș al Braziliei.")
    U.p(3, "2.1", "Atinge pe hartă Buenos Aires.", "lume", -34.6, -58.38, "Buenos Aires", 300, "Buenos Aires e pe estuarul La Plata.")
    U.p(3, "2.1", "Atinge pe hartă Los Angeles.", "lume", 34.05, -118.24, "Los Angeles", 300, "Los Angeles e pe coasta Pacificului.")
    U.a(2, "3.3", "Ce problemă apare când orașele se extind mult în suburbii?", "oamenii folosesc mult mașina, deci crește traficul și poluarea", ["dispar mașinile", "orașele devin mai mici", "nu apare nicio problemă"], "Distanțele mari descurajează mersul pe jos.")
    U.a(2, "3.2", "De ce orașele din America Latină au crescut foarte repede?", "migrația masivă de la sat la oraș", ["pentru că satele au dispărut într-o zi", "pentru că nu se nasc copii", "pentru că e interzis la sat"], "Oamenii caută muncă și servicii.")
    U.a(2, "3.3", "Ce oraș american e cunoscut pentru Hollywood și industria filmului?", "Los Angeles", ["Chicago", "Boston", "Houston"], "Hollywood e un cartier din Los Angeles.")
    U.a(2, "3.3", "Ce oraș american e un mare centru financiar, cu bursa de pe Wall Street?", "New York", ["Washington", "Miami", "Seattle"], "Wall Street e în Manhattan.")
    U.adev(2, "3.3", "În SUA și Canada majoritatea oamenilor trăiesc la oraș.", True, "Adevărat: peste 8 din 10.")
    U.adev(2, "3.3", "Favelele sunt cartiere de lux.", False, "Fals: sunt cartiere sărace.")
    U.l(2, "1.1", "Completează.", "Un șir de orașe mari unite se numește [megalopolă]; cartierele sărace din Brazilia se numesc [favele].", ["suburbie", "pampasuri"], "Megalopolă, favele.")
    U.l(2, "2.1", "Completează.", "Cel mai mare oraș al Braziliei este [São Paulo], iar cel mai mare oraș al Canadei este [Toronto].", ["Brasília", "Ottawa"], "São Paulo, Toronto.")
    U.g(3, "2.3 4.1", "Graficul arată ponderea populației urbane în trei țări americane (valori rotunjite). Care e cea mai urbanizată?", grafic("bare", "Populația urbană (valori rotunjite)", [("Argentina", 92), ("SUA", 83), ("Haiti", 59)], "%", "Banca Mondială – Urban population (% of total)"), "Argentina", ["SUA", "Haiti", "sunt egale"], "Peste 9 din 10 argentinieni trăiesc la oraș.", surse=["Banca Mondială – Urban population (% of total population)", "ONU – World Urbanization Prospects"])
    U.o(3, "2.2 3.1 4.2", "Ordonează orașele megalopolei BosWash de la nord la sud.", ["Boston", "New York", "Philadelphia", "Baltimore", "Washington"], "De la nord la sud", "De-a lungul coastei de est.")
    U.a(3, "4.3", "Compară o suburbie din SUA cu o favelă din Brazilia.", "suburbia are case individuale și servicii; favela are locuințe improvizate și servicii puține", ["sunt identice", "favela e mai bogată", "suburbia e un sat"], "Contraste urbane.")
    U.d(2, "2.1", "Ce oraș, al treilea ca mărime din SUA, pe Lacul Michigan, e marcat pe hartă?", "lume", 41.88, -87.63, "Chicago", ["Detroit", "Toronto", "Cleveland"], "Chicago e un mare nod de transport.")
    U.a(2, "3.4", "Ce statuie e simbolul orașului Rio de Janeiro?", "statuia lui Hristos Mântuitorul", ["Statuia Libertății", "Turnul Eiffel", "Colosseumul"], "Statuia e pe muntele Corcovado.")
    U.a(2, "3.4", "Ce statuie e simbolul orașului New York?", "Statuia Libertății", ["statuia lui Hristos Mântuitorul", "Big Ben", "Partenonul"], "A fost un dar al Franței, în 1886.")
    U.a(2, "4.4", "Ce soluție a folosit orașul Curitiba (Brazilia) pentru trafic?", "un sistem rapid de autobuze pe benzi speciale", ["interzicerea autobuzelor", "mai multe autostrăzi prin centru", "închiderea parcurilor"], "Exemplul a fost copiat în multe orașe.")
    U.a(2, "3.2", "De ce Ciudad de México are probleme cu poluarea aerului?", "e într-o depresiune înconjurată de munți, unde aerul poluat stagnează", ["e lângă ocean", "plouă mult", "are prea puține mașini"], "Relieful influențează calitatea aerului.")
    U.a(2, "3.3", "Ce înseamnă „zgârie-nori”?", "clădiri foarte înalte, cu multe etaje", ["case mici", "poduri", "tuneluri"], "Primul a fost construit la Chicago, în 1885.")
    U.a(2, "1.1", "Ce este o suburbie?", "un cartier de locuințe la marginea orașului", ["centrul orașului", "un sat izolat", "un port"], "Mulți americani locuiesc în suburbii.")
    U.a(3, "4.4", "Cum pot orașele mari să devină mai prietenoase cu mediul?", "transport public, piste de biciclete, parcuri și clădiri eficiente energetic", ["mai multe mașini", "tăierea parcurilor", "închiderea metroului"], "Orașe verzi.")

    U.a(2, "2.1", "Pe ce estuar se află Buenos Aires?", "Río de la Plata", ["Amazon", "Orinoco", "Mississippi"], "Pe celălalt mal e Montevideo, capitala Uruguayului.")

    # ================================================================ S27 Diferențieri economice
    X = Lectie(7, "VII-S27-diferentieri-economice-regionale", "Americile – diferențieri economice regionale",
               "Ce produse din Americi ajung pe masa ta?",
               [("America de Nord", "SUA au cea mai mare economie din lume: industrie de vârf (aeronautică, IT, automobile, farmaceutică), agricultură mecanizată (porumb, soia, grâu), servicii (finanțe, divertisment). Silicon Valley (California) e centrul mondial al IT-ului.\nCanada: resurse (petrol, lemn, minereuri), agricultură (grâu), servicii. Mexic: petrol, industrie de automobile, turism."),
                ("America Latină", "Brazilia: soia, cafea, trestie de zahăr, carne de vită, minereu de fier, avioane; a doua economie mare a Americilor după SUA.\nArgentina: cereale și carne din Pampas. Chile: cupru (cel mai mare producător mondial). Venezuela: petrol. Peru: cupru, argint, aur. Columbia: cafea, flori. America Centrală și Caraibe: banane, trestie de zahăr, turism."),
                ("Contraste", "Regiunile foarte dezvoltate (nord-estul SUA, California, sud-estul Braziliei) contrastează cu regiuni sărace (nord-estul Braziliei, zonele rurale din Anzi, Haiti).\nComerțul leagă Americile de lume: Canalul Panama e una dintre cele mai importante rute maritime.")],
               stiaica="Chile produce aproximativ un sfert din cuprul lumii, după datele USGS; mina de la Chuquicamata e una dintre cele mai mari mine la suprafață.",
               ref=REF.format("Diferențieri economice regionale"))
    X.s(1, "3.3", "Asociază țara cu produsul principal.", [("Chile", "cupru"), ("Brazilia", "cafea și soia"), ("Venezuela", "petrol"), ("Argentina", "carne de vită și cereale")], "Resurse și produse ale Americii Latine.")
    X.a(1, "3.3", "Ce țară are cea mai mare economie din lume?", "SUA", ["Brazilia", "Canada", "Mexic"], "SUA au cea mai mare economie, urmate de China.")
    X.a(1, "3.3", "Ce este Silicon Valley?", "o regiune din California, centrul mondial al companiilor de IT", ["o vale cu nisip", "o mină de siliciu", "un parc național"], "Aici sunt sediile multor companii tehnologice.")
    X.a(2, "3.3", "Ce țară e cel mai mare producător de cupru din lume?", "Chile", ["Canada", "Argentina", "Mexic"], "Aproximativ un sfert din producția mondială.", surse=["U.S. Geological Survey – Mineral Commodity Summaries 2025: Copper", "Encyclopaedia Britannica – Chile: economy"])
    X.a(2, "3.3", "Ce țară e un mare exportator de cafea și soia?", "Brazilia", ["Canada", "Chile", "Cuba"], "Brazilia e cel mai mare producător de cafea.")
    X.a(2, "3.3", "Ce produc mai ales țările din America Centrală?", "banane, cafea, trestie de zahăr", ["petrol și diamante", "lemn de taiga", "grâu de tundră"], "Clima tropicală permite aceste culturi.")
    X.a(2, "3.3", "Ce resurse are Canada?", "petrol, lemn, minereuri, grâu, apă dulce", ["cafea și cacao", "banane", "nimic"], "Canada e bogată în resurse naturale.")
    X.a(2, "3.3", "Ce industrie e importantă în Mexic, lângă granița cu SUA?", "industria de automobile și de asamblare", ["creșterea renilor", "pescuitul de balene", "mineritul de diamante"], "Fabricile exportă spre SUA.")
    X.p(2, "2.1", "Atinge pe hartă Silicon Valley (San Francisco).", "lume", 37.4, -122, "Silicon Valley", 300, "Silicon Valley e la sud de San Francisco.")
    X.p(3, "2.1", "Atinge pe hartă mina de cupru Chuquicamata (nordul Chile).", "lume", -22.3, -68.9, "Chuquicamata", 400, "Mina e în deșertul Atacama.")
    X.a(2, "3.3", "Ce animale se cresc pe scară largă în Pampas?", "vitele (pentru carne)", ["renii", "cămilele", "lamele"], "Argentina e cunoscută pentru carnea de vită.")
    X.a(2, "4.3", "Ce regiune a Braziliei e mai săracă?", "nord-estul", ["sud-estul (São Paulo)", "Rio de Janeiro", "Brasília"], "Seceta și moștenirea plantațiilor au lăsat sărăcie.")
    X.adev(2, "3.3", "Economia SUA se bazează numai pe agricultură.", False, "Fals: industrie de vârf și servicii.")
    X.adev(2, "3.3", "Brazilia produce și exportă avioane.", True, "Adevărat: compania Embraer.")
    X.l(2, "3.3", "Completează.", "Cel mai mare producător de cupru e [Chile], iar cel mai mare producător de cafea e [Brazilia].", ["Canada", "Mexic"], "Chile, Brazilia.")
    X.l(2, "3.3", "Completează.", "Centrul mondial al IT-ului e [Silicon Valley], în statul [California].", ["Wall Street", "Texas"], "Silicon Valley, California.")
    X.g(3, "2.3 4.1", "Graficul arată venitul mediu pe locuitor în trei țări americane (mii dolari, valori rotunjite). Câte ori e mai mare în SUA decât în Brazilia?", grafic("bare", "PIB pe locuitor (mii dolari, valori rotunjite)", [("SUA", 85), ("Brazilia", 10), ("Haiti", 2)], "mii dolari", "Banca Mondială – GDP per capita"), "de aproximativ 8 ori", ["la fel", "de 2 ori", "de 85 de ori"], "85 : 10 ≈ 8.", surse=["Banca Mondială – GDP per capita (current US$)", "FMI – World Economic Outlook database"])
    X.a(3, "4.3", "Compară economia SUA cu cea a Haitiului.", "SUA au industrie, tehnologie și servicii de vârf; Haiti are agricultură de subzistență și venituri foarte mici", ["sunt identice", "Haiti e mai dezvoltat", "SUA nu au industrie"], "Contrastele economice.")
    X.d(2, "2.1", "Ce țară, mare producătoare de cafea și flori, e marcată pe hartă?", "lume", 4.5, -74, "Columbia", ["Venezuela", "Ecuador", "Peru"], "Columbia e în nord-vestul Americii de Sud.")
    X.a(2, "3.3", "Ce înseamnă „agricultură de subzistență”?", "oamenii cultivă doar cât le trebuie pentru propria familie", ["agricultură pentru export", "agricultură mecanizată", "agricultură în seră"], "E frecventă în zonele sărace.")
    X.a(2, "3.3", "Ce mare producție agricolă are Midwest-ul american?", "porumb și soia (Corn Belt)", ["banane", "cafea", "cacao"], "Corn Belt = „centura porumbului”.")
    X.a(2, "3.3", "Ce industrie e importantă la Detroit?", "industria de automobile", ["industria cafelei", "pescuitul", "mineritul cuprului"], "Detroit e numit „Motor City”.")
    X.a(2, "4.4", "Ce efect are cultivarea soiei în Brazilia asupra mediului?", "poate duce la defrișarea pădurilor și a savanei", ["crește pădurea", "răcește clima", "nu are efecte"], "Se caută soia certificată, fără defrișări.")
    X.a(2, "3.3", "Ce domeniu economic e foarte important în Caraibe?", "turismul", ["mineritul cărbunelui", "industria oțelului", "creșterea renilor"], "Plaje, soare, croaziere.")
    X.a(3, "3.3", "De ce Canalul Panama e important pentru economia mondială?", "prin el trec mii de vapoare pe an între Atlantic și Pacific, scurtând drumul", ["produce petrol", "e un port de pescuit", "e o atracție doar pentru turiști"], "Prin canal trec, în fiecare an, mii de vapoare.", surse=S_PANAMA)
    X.a(2, "3.3", "Ce țară e un mare producător de petrol în America de Sud?", "Venezuela", ["Uruguay", "Paraguay", "Chile"], "Venezuela are mari rezerve de petrol.")
    X.a(2, "3.3", "Ce fruct tropical se exportă mult din Ecuador și America Centrală?", "banana", ["mărul", "pera", "prunele"], "Ecuador e un mare exportator de banane.")
    X.a(2, "3.3", "Ce fac companiile de divertisment din Los Angeles?", "filme, seriale, muzică", ["oțel", "cafea", "automobile"], "Hollywood e capitala filmului.")
    X.a(3, "4.4", "Cum pot țările Americii Latine să reducă dependența de exportul de materii prime?", "prin prelucrarea lor în țară, educație și industrii noi", ["prin exportul mai mult de materii prime brute", "prin închiderea școlilor", "nu pot face nimic"], "Valoarea adăugată crește veniturile.")
    X.a(2, "3.3", "Ce țară e un mare exportator de grâu din America de Nord, alături de SUA?", "Canada", ["Mexic", "Cuba", "Guatemala"], "Preriile canadiene sunt o zonă de cereale.")

    # ================================================================ S28 Expediție
    E = Expeditie(7, "VII-S28-aplicatii-practice-studii-caz", "Expediție: de la Alaska la Țara de Foc",
                  "Ce ai vedea dacă ai călători pe uscat de la nordul la sudul Americilor?",
                  ref=REF.format("Aplicații practice/studii de caz: Particularități geografice ale unor state"))
    E.o(1, "4.1 3.1 4.2", "Ordonează țările pe drumul de la nord la sud.", ["Canada", "SUA", "Mexic", "Panama", "Peru", "Chile"], "De la nord la sud", "Drumul Panamerican leagă aceste țări.")
    E.pas("1. Traseul", "Pe o hartă, trasează un drum de la Alaska până în Țara de Foc. Notează țările prin care treci.")
    E.s(2, "4.4", "Asociază etapa călătoriei cu peisajul.", [("Alaska", "tundră și ghețari"), ("Marile Câmpii", "culturi de porumb"), ("Amazonia", "pădure tropicală"), ("Patagonia", "stepă rece și vânt")], "Peisaje de la nord la sud.")
    E.pas("2. Peisajele", "Alege 4 opriri pe traseu și descrie peisajul fiecăreia: relief, climă, vegetație.",
          jurnal="Fă un tabel cu cele 4 opriri: relief, climă, vegetație, un animal.")
    E.a(2, "4.4", "Ce problemă de mediu ai întâlni în Amazonia?", "defrișarea", ["topirea calotei antarctice", "deșertificarea Saharei", "poluarea Mării Negre"], "Pădurea e tăiată pentru pășuni și culturi.")
    E.pas("3. Statul ales", "Alege un stat de pe traseu și găsește o particularitate geografică și o problemă de mediu. Propune o soluție.",
          jurnal="Scrie particularitatea, problema și soluția.")
    E.pas("4. Jurnalul de călătorie", "Scrie o pagină de jurnal ca și cum ai fi făcut călătoria: ce ai văzut, ce te-a surprins.",
          jurnal="Fotografiază pagina sau desenul.", foto=True)

    return Unitate(7, "u3-america.json", "America de Nord și America de Sud").add(P, R, H, C, D, K, U, X, E)
