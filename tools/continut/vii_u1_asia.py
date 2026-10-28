from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VII-a, ediția 2024 (manuale.edu.ro), lecția „{}”"
S_ASIA = ["Encyclopaedia Britannica – Asia", "Wikipedia – Asia"]
S_EV = ["Al Jazeera, 8.12.2020 – anunțul Nepal–China: 8 848,86 m", "The Himalayan Times, 8.12.2020"]
S_MM = ["Encyclopaedia Britannica – Dead Sea", "Wikipedia – Dead Sea"]
S_YANG = ["Encyclopaedia Britannica – Yangtze River", "Wikipedia – Yangtze"]
S_BAIKAL = ["UNESCO World Heritage Centre – Lake Baikal", "Encyclopaedia Britannica – Lake Baikal"]
S_POP = ["ONU (UN DESA) – World Population Prospects 2024", "Our World in Data – Population by continent"]
S_INDIA = ["UN DESA – Policy Brief nr. 153: India overtakes China (aprilie 2023)", "BBC News, 24.04.2023"]
S_ORASE = ["ONU (UN DESA) – World Urbanization Prospects 2025", "Al Jazeera, 26.11.2025 – Jakarta now the world's largest city"]
S_MAWS = ["Guinness World Records – Wettest place (average annual rainfall): Mawsynram", "Encyclopaedia Britannica – Mawsynram"]


def unitate():
    # ================================================================ S2 Asia – poziție
    P = Lectie(7, "VII-S02-caracterizare-geografica-pozitia-geografica", "Asia – poziția geografică",
               "Cum poate un singur continent să aibă și deșerturi fierbinți, și tundră înghețată?",
               [("Cel mai mare continent", "Asia e cel mai mare continent: aproximativ 44 de milioane km², aproape o treime din uscatul Pământului. Se află în emisfera nordică și în cea mai mare parte în emisfera estică.\nSe întinde de la Oceanul Arctic (nord) până dincolo de Ecuator, în insulele Indoneziei (sud), și de la Munții Ural (vest) până la Oceanul Pacific (est)."),
                ("Limite și vecini", "La nord: Oceanul Arctic. La est: Oceanul Pacific. La sud: Oceanul Indian. La vest: Europa (Munții Ural, râul Ural, Marea Caspică, Munții Caucaz, Marea Neagră, strâmtorile Bosfor și Dardanele) și Africa (Istmul Suez, Marea Roșie).\nStrâmtoarea Bering desparte Asia de America de Nord."),
                ("Țărmurile", "Peninsule mari: Arabia (cea mai mare din lume), Asia Mică (Anatolia), Hindustan (India), Indochina, Malacca, Coreea, Kamciatka.\nInsule și arhipelaguri: Japonia, Filipine, Indonezia (cel mai mare arhipelag), Sri Lanka, Taiwan, Sahalin.")],
               stiaica="Rusia are 11 fusuri orare: când la Moscova e seară, la Vladivostok e deja dimineața zilei următoare.",
               ref=REF.format("Asia – poziția geografică"))
    P.a(1, "1.1", "Care e cel mai mare continent?", "Asia", ["Africa", "America de Nord", "Europa"], "Asia are aproximativ 44 de milioane km².", surse=S_ASIA)
    P.a(2, "3.1", "Ce suprafață are Asia, aproximativ?", "44 de milioane km²", ["4 milioane km²", "10 milioane km²", "100 de milioane km²"], "Asia ocupă aproape o treime din uscat.", surse=S_ASIA)
    P.e(2, "2.1", "Pune pe hartă oceanele care scaldă Asia.", [("arc", "Oceanul Arctic", 78, 100), ("pac", "Oceanul Pacific", 30, 160), ("ind", "Oceanul Indian", -10, 80)], "Arctic la nord, Pacific la est, Indian la sud.", harta="lume")
    P.a(2, "2.1", "Ce strâmtoare desparte Asia de America de Nord?", "Strâmtoarea Bering", ["Strâmtoarea Gibraltar", "Bosforul", "Strâmtoarea Malacca"], "Bering e între Siberia și Alaska.")
    P.a(2, "2.1", "Ce desparte Asia de Africa?", "Istmul Suez și Marea Roșie", ["Munții Ural", "Strâmtoarea Bering", "Marea Caspică"], "Prin Istmul Suez s-a săpat Canalul Suez.")
    P.a(2, "2.1", "Care e cea mai mare peninsulă din lume?", "Peninsula Arabia", ["Peninsula Scandinavă", "Peninsula Indochina", "Peninsula Kamciatka"], "Arabia e în sud-vestul Asiei.")
    P.a(2, "2.1", "Care e cel mai mare arhipelag din lume?", "Indonezia (Arhipelagul Malaez)", ["Japonia", "Filipine", "Marea Britanie"], "Indonezia are mii de insule.")
    P.p(2, "2.1", "Atinge pe hartă Peninsula Arabia.", "lume", 23, 46, "Peninsula Arabia", 800, "Arabia e între Marea Roșie și Golful Persic.")
    P.p(2, "2.1", "Atinge pe hartă Peninsula Hindustan (India).", "lume", 18, 78, "Hindustan", 700, "Hindustanul e în sudul Asiei.")
    P.p(2, "2.1", "Atinge pe hartă Japonia.", "lume", 36, 138, "Japonia", 600, "Japonia e un arhipelag în estul Asiei.")
    P.p(3, "2.1", "Atinge pe hartă Strâmtoarea Bering.", "lume", 66, -169, "Strâmtoarea Bering", 500, "Bering e între Rusia și Alaska.")
    P.p(3, "2.1", "Atinge pe hartă Peninsula Indochina.", "lume", 15, 104, "Indochina", 700, "Indochina e între India și China.")
    P.s(2, "2.1", "Asociază peninsula cu țara sau regiunea.", [("Arabia", "Arabia Saudită"), ("Hindustan", "India"), ("Asia Mică", "Turcia"), ("Coreea", "Coreea de Nord și Coreea de Sud")], "Peninsulele Asiei.")
    P.a(2, "2.2", "În ce emisfere se află cea mai mare parte a Asiei?", "în emisfera nordică și în emisfera estică", ["în emisfera sudică", "în emisfera vestică", "doar pe Ecuator"], "Doar câteva insule ale Indoneziei sunt la sud de Ecuator.")
    P.a(3, "2.3", "De ce Asia are climate atât de diferite?", "pentru că se întinde pe foarte multe latitudini, de la zona rece la cea ecuatorială, și are interior foarte îndepărtat de ocean", ["pentru că e mică", "pentru că e toată pe Ecuator", "pentru că nu are munți"], "Întinderea mare explică diversitatea.")
    P.adev(2, "1.2", "Asia e scăldată de patru oceane.", False, "Fals: de trei oceane – Arctic, Pacific și Indian.")
    P.adev(2, "1.2", "Asia și Europa formează împreună Eurasia.", True, "Adevărat: nu sunt despărțite de ocean.")
    P.l(2, "2.1", "Completează.", "Asia e despărțită de America de Nord prin Strâmtoarea [Bering] și de Africa prin Istmul [Suez].", ["Gibraltar", "Panama"], "Bering și Suez.")
    P.l(2, "2.1", "Completează.", "Cea mai mare peninsulă a lumii este [Arabia], iar cel mai mare arhipelag este [Indonezia].", ["Kamciatka", "Japonia"], "Arabia și Indonezia.")
    P.d(2, "2.1", "Ce insulă mare e marcată pe hartă?", "lume", 7.8, 80.7, "Sri Lanka", ["Madagascar", "Taiwan", "Sahalin"], "Sri Lanka e la sud de India.")
    P.d(3, "2.1", "Ce peninsulă e marcată pe hartă?", "lume", 56, 160, "Kamciatka", ["Coreea", "Malacca", "Arabia"], "Kamciatka e în extremul est al Rusiei, cu mulți vulcani.")
    P.o(3, "2.2 3.1 4.2", "Ordonează aceste locuri de la vest la est.", ["Turcia", "Arabia Saudită", "India", "China", "Japonia"], "De la vest la est", "De la Asia Mică spre Pacific.")
    P.a(2, "3.3", "Ce înseamnă „fus orar”?", "o zonă a Pământului în care se folosește aceeași oră", ["un tip de climă", "un munte", "un râu"], "Rusia are 11 fusuri orare.")
    P.a(2, "2.1", "Ce mare internă se află la granița dintre Europa și Asia?", "Marea Caspică", ["Marea Roșie", "Marea Chinei de Sud", "Marea Arabiei"], "Caspica e cel mai mare lac de pe Pământ.")
    P.a(2, "2.1", "Ce oraș se întinde pe ambele maluri ale Bosforului, în Europa și în Asia?", "Istanbul", ["Ankara", "Teheran", "Bagdad"], "Bosforul desparte cele două continente.")
    P.g(3, "2.3 4.1", "Graficul compară suprafața continentelor (milioane km², valori rotunjite). Cu cât e mai mare Asia decât Africa?", grafic("bare", "Suprafața continentelor", [("Asia", 44), ("Africa", 30), ("America de Nord", 24), ("Europa", 10)], "milioane km²", "Encyclopaedia Britannica"), "cu aproximativ 14 milioane km²", ["cu aproximativ 4 milioane km²", "cu aproximativ 34 de milioane km²", "sunt egale"], "44 − 30 = 14 milioane km².", surse=S_ASIA)
    P.a(2, "2.1", "Ce țară asiatică se întinde și în Europa?", "Rusia (și Turcia)", ["China", "India", "Japonia"], "Rusia și Turcia sunt state transcontinentale.")
    P.a(3, "4.3", "Compară poziția Japoniei cu a Mongoliei.", "Japonia e insulară, la ocean; Mongolia e în interiorul continentului, fără ieșire la mare", ["sunt amândouă insule", "Mongolia e pe țărm", "Japonia e în deșert"], "Poziția față de ocean influențează clima și economia.")
    P.a(2, "2.1", "Ce canal leagă Marea Mediterană de Marea Roșie?", "Canalul Suez", ["Canalul Panama", "Canalul Dunăre–Marea Neagră", "Canalul Mânecii"], "Canalul Suez scurtează drumul Europa–Asia.")
    P.a(2, "2.1", "Ce peninsulă e la sud de Indochina, cu Singapore la capăt?", "Malacca", ["Coreea", "Kamciatka", "Arabia"], "Strâmtoarea Malacca e o cale maritimă foarte circulată.")

    # ================================================================ S3 Relieful. Himalaya
    R = Lectie(7, "VII-S03-relieful-caracteristici-generale-unitati", "Asia – relieful. Munții Himalaya",
               "Cum s-au format cei mai înalți munți ai lumii?",
               [("Caracteristici", "Asia are cea mai mare altitudine medie dintre continente, dacă nu socotim calota de gheață a Antarcticii. Aici se află și cel mai înalt punct de pe uscat – vârful Everest (8 848,86 m) – și cel mai jos – țărmul Mării Moarte (aproximativ 430 m sub nivelul mării).\nÎn centru se află munți și podișuri foarte înalte: Himalaya, Karakorum, Pamir, Tian Shan, Podișul Tibet („acoperișul lumii”)."),
                ("Munții Himalaya", "Himalaya s-a format prin ciocnirea plăcii indiene cu placa eurasiatică. Ciocnirea continuă și azi, așa că munții încă se înalță, iar în regiune se produc cutremure.\nÎn Himalaya sunt 10 dintre cele 14 vârfuri de peste 8 000 m. Everest e la granița Nepalului cu China."),
                ("Alte unități", "Câmpii: Câmpia Siberiei de Vest, Câmpia Chinei de Est, Câmpia Indo-Gangetică, Câmpia Mesopotamiei. Podișuri: Siberiei Centrale, Deccan, Iran, Arabiei. Deșerturi: Gobi, Taklamakan, Rub al-Khali.\nVulcani activi: Kamciatka, Japonia (Fuji, care nu a mai erupt din 1707, dar e considerat activ), Indonezia – în Cercul de Foc al Pacificului.")],
               stiaica="Pe vârful Everest s-au găsit fosile de animale marine: rocile de acolo s-au format pe fundul unui ocean vechi, înainte să fie împinse în sus.",
               ref=REF.format("Relieful – caracteristici generale, unități majore. Munții Himalaya"))
    R.a(1, "2.1", "Care e cel mai înalt vârf de pe Pământ?", "Everest (8 848,86 m)", ["K2", "Elbrus", "Aconcagua"], "Măsurătoarea comună Nepal–China din 2020.", surse=S_EV)
    R.a(2, "2.1", "La granița căror țări se află Everest?", "Nepal și China", ["India și Pakistan", "Japonia și Coreea", "Mongolia și Rusia"], "Everest e în Himalaya.")
    R.a(2, "1.2", "Cum s-au format Munții Himalaya?", "prin ciocnirea plăcii indiene cu placa eurasiatică", ["din erupții vulcanice", "din depuneri de nisip", "de ghețari"], "Ciocnirea continuă, iar munții cresc încet.")
    R.a(2, "2.1", "Care e cel mai jos punct de pe uscat?", "țărmul Mării Moarte", ["Valea Morții", "Delta Dunării", "Depresiunea Caspică"], "Marea Moartă e la aproximativ 430 m sub nivelul mării.", surse=S_MM)
    R.a(2, "1.1", "Ce podiș e numit „acoperișul lumii”?", "Podișul Tibet", ["Podișul Deccan", "Podișul Iran", "Podișul Arabiei"], "Tibetul are altitudini medii de peste 4 000 m.")
    R.s(2, "2.1", "Asociază unitatea de relief cu tipul ei.", [("Himalaya", "munți"), ("Tibet", "podiș"), ("Câmpia Indo-Gangetică", "câmpie"), ("Gobi", "deșert")], "Unități majore ale Asiei.")
    R.p(2, "2.1", "Atinge pe hartă Munții Himalaya.", "lume", 28.5, 85, "Himalaya", 600, "Himalaya e la nordul Indiei.")
    R.p(2, "2.1", "Atinge pe hartă vârful Everest.", "lume", 27.99, 86.93, "Everest", 300, "Everest e între Nepal și Tibet (China).", surse=S_EV)
    R.p(2, "2.1", "Atinge pe hartă deșertul Gobi.", "lume", 43, 105, "Gobi", 700, "Gobi e în Mongolia și nordul Chinei.")
    R.p(3, "2.1", "Atinge pe hartă Marea Moartă.", "lume", 31.5, 35.5, "Marea Moartă", 300, "Marea Moartă e între Israel, Palestina și Iordania.", surse=S_MM)
    R.p(3, "2.1", "Atinge pe hartă Podișul Tibet.", "lume", 32, 88, "Tibet", 700, "Tibetul e la nord de Himalaya.")
    R.a(2, "2.2", "De ce în Himalaya se produc des cutremure?", "pentru că plăcile tectonice continuă să se ciocnească", ["pentru că sunt vulcani mulți", "pentru că plouă mult", "pentru că sunt prea mulți turiști"], "Mișcarea plăcilor produce tensiuni în roci.")
    R.a(2, "2.1", "Ce munți vulcanici se află în Japonia?", "Fuji", ["Everest", "Ural", "Altai"], "Fuji e simbolul Japoniei.")
    R.a(2, "2.2", "De ce Japonia și Indonezia au mulți vulcani?", "pentru că se află în Cercul de Foc al Pacificului", ["pentru că sunt în deșert", "pentru că sunt la pol", "pentru că au câmpii mari"], "Marginile Pacificului sunt zone de subducție.")
    R.a(2, "2.1", "Ce câmpie e străbătută de Gange?", "Câmpia Indo-Gangetică", ["Câmpia Siberiei de Vest", "Câmpia Mesopotamiei", "Câmpia Chinei de Est"], "E una dintre cele mai populate regiuni din lume.")
    R.a(2, "2.1", "Ce câmpie se află între Tigru și Eufrat?", "Câmpia Mesopotamiei", ["Câmpia Indo-Gangetică", "Câmpia Chinei de Est", "Câmpia Turanului"], "Mesopotamia înseamnă „între râuri”.")
    R.adev(2, "1.2", "Munții Himalaya încă se înalță, foarte încet.", True, "Adevărat: ciocnirea plăcilor continuă.")
    R.adev(2, "1.2", "Asia are altitudinea medie cea mai mică dintre continente.", False, "Fals: Asia are una dintre cele mai mari altitudini medii.")
    R.l(2, "2.1", "Completează.", "Cel mai înalt vârf, [Everest], se află în Munții [Himalaya].", ["K2", "Karakorum"], "Everest, Himalaya.", surse=S_EV)
    R.l(2, "1.1", "Completează.", "Podișul [Tibet] e numit „acoperișul lumii”, iar Podișul [Deccan] ocupă Peninsula Hindustan.", ["Iran", "Gobi"], "Tibet, Deccan.")
    R.o(3, "4.2 3.1", "Ordonează vârfurile de la cel mai înalt la cel mai jos.", ["Everest", "K2", "Elbrus", "Fuji", "Moldoveanu"], "Altitudine, descrescător", "Everest 8 848,86 m, K2 8 611 m, Elbrus 5 642 m, Fuji 3 776 m, Moldoveanu 2 544 m.", surse=["Encyclopaedia Britannica – K2 / Mount Fuji / Mount Elbrus", "Wikipedia – List of highest mountains on Earth"])
    R.g(3, "2.3 4.1", "Profilul arată altitudinea de-a lungul unei linii de la Câmpia Gangelui spre Tibet (valori aproximative). Unde e altitudinea cea mai mare?", grafic("profil", "Profil schematic: Câmpia Gangelui – Himalaya – Tibet", [("Câmpia Gangelui", 100), ("poalele Himalayei", 1500), ("creasta Himalayei", 8000), ("Podișul Tibet", 4500)], "m"), "pe creasta Himalayei", ["în Câmpia Gangelui", "în Podișul Tibet", "la poalele munților"], "Creasta e mult deasupra podișului.")
    R.a(3, "3.3", "Ce înseamnă „munții de peste 8 000 m”?", "cele 14 vârfuri ale lumii care depășesc 8 000 m, toate în Asia", ["toți munții din Europa", "vulcanii din Japonia", "munții din Africa"], "Himalaya și Karakorum au toți acești giganți.")
    R.a(2, "3.4", "Cine au fost primii oameni care au urcat pe Everest, în 1953?", "Edmund Hillary și Tenzing Norgay", ["Neil Armstrong și Buzz Aldrin", "Columb și Magellan", "Amundsen și Scott"], "Pe 29 mai 1953.")
    R.d(2, "2.1", "Ce deșert e marcat pe hartă, în sudul Peninsulei Arabia?", "lume", 20, 50, "Rub al-Khali", ["Gobi", "Taklamakan", "Thar"], "Rub al-Khali („Sfertul gol”) e unul dintre cele mai mari deșerturi de nisip.")
    R.a(3, "4.3", "Ce legătură e între relieful Himalayei și clima Indiei?", "munții opresc aerul rece din nord și obligă aerul umed al musonului să se descarce", ["nu e nicio legătură", "munții aduc deșertul", "munții produc zăpadă în câmpie"], "Relieful influențează clima.")
    R.a(2, "2.1", "Ce munți despart Siberia de Europa?", "Uralii", ["Himalaya", "Altai", "Tian Shan"], "Uralii sunt granița convențională.")
    R.a(2, "4.4", "De ce turismul pe Everest pune probleme mediului?", "pe munte rămân multe deșeuri lăsate de expediții", ["nu pune nicio problemă", "topește Himalaya", "produce cutremure"], "Se organizează acțiuni de curățare.")
    R.a(2, "2.1", "Ce podiș mare ocupă cea mai mare parte a Peninsulei Arabia?", "Podișul Arabiei", ["Podișul Deccan", "Podișul Tibet", "Podișul Siberiei Centrale"], "E un podiș deșertic.")

    R.a(2, "2.1", "Ce munți, cu vârful K2, se află la nord-vest de Himalaya?", "Karakorum", ["Ural", "Altai", "Caucaz"], "K2 (8 611 m) e al doilea vârf al lumii.")

    # ================================================================ S4 Hidrografia
    H = Lectie(7, "VII-S04-hidrografia-caracteristici-generale-fluvii", "Asia – hidrografia. Fluvii și lacuri",
               "De ce cele mai vechi civilizații au apărut pe malul fluviilor din Asia?",
               [("Fluviile", "Fluviile Asiei pornesc mai ales din munții și podișurile din centru și curg spre trei oceane.\nSpre Pacific: Yangtze (Chang Jiang, cel mai lung fluviu din Asia, aproximativ 6 300 km), Huang He (Fluviul Galben), Amur, Mekong. Spre Indian: Gange, Indus, Brahmaputra, Tigru și Eufrat (prin Golful Persic). Spre Arctic: Obi, Enisei, Lena, care îngheață iarna.\nUnele râuri nu ajung la ocean (bazine endoreice): Amu-Daria și Sîr-Daria spre Marea Aral."),
                ("Lacurile", "Marea Caspică e cel mai mare lac de pe Pământ. Baikal (1 642 m) e cel mai adânc lac și cea mai mare rezervă de apă dulce lichidă de la suprafață. Marea Moartă e foarte sărată. Marea Aral s-a micșorat mult din cauza irigațiilor."),
                ("Importanța apelor", "Pe Tigru și Eufrat a apărut civilizația Mesopotamiei; pe Indus, civilizația Indusului; pe Huang He, civilizația chineză.\nFluviile asigură apă pentru irigații (orez), energie (Barajul Trei Defileuri, pe Yangtze, cea mai mare hidrocentrală din lume) și transport.")],
               stiaica="În Marea Moartă apa e atât de sărată încât poți pluti pe ea ca pe o saltea, fără să înoți.",
               ref=REF.format("Hidrografia – caracteristici generale. Fluvii și lacuri"))
    H.a(1, "2.1", "Care e cel mai lung fluviu din Asia?", "Yangtze (Chang Jiang)", ["Gange", "Obi", "Mekong"], "Yangtze are aproximativ 6 300 km.", surse=S_YANG)
    H.a(2, "2.1", "În ce țară curge Yangtze?", "China", ["India", "Rusia", "Vietnam"], "Yangtze traversează China de la vest la est.")
    H.a(2, "2.1", "Care e cel mai adânc lac de pe Pământ?", "Baikal", ["Marea Caspică", "Marea Moartă", "Marea Aral"], "Baikal are 1 642 m.", surse=S_BAIKAL)
    H.a(2, "2.1", "Care e cel mai mare lac de pe Pământ ca suprafață?", "Marea Caspică", ["Baikal", "Marea Aral", "Balhaș"], "Caspica are apă ușor sărată.")
    H.s(2, "2.1", "Asociază fluviul cu oceanul în care ajunge.", [("Yangtze", "Pacific (Marea Chinei de Est)"), ("Gange", "Indian (Golful Bengal)"), ("Obi", "Arctic"), ("Mekong", "Pacific (Marea Chinei de Sud)")], "Fluviile Asiei curg spre trei oceane.")
    H.s(2, "3.3", "Asociază fluviul cu civilizația veche.", [("Tigru și Eufrat", "Mesopotamia"), ("Indus", "civilizația Indusului"), ("Huang He", "civilizația chineză veche")], "Civilizațiile au apărut lângă apă.")
    H.p(2, "2.1", "Atinge pe hartă Lacul Baikal.", "lume", 53.5, 108, "Baikal", 400, "Baikal e în sudul Siberiei.", surse=S_BAIKAL)
    H.p(2, "2.1", "Atinge pe hartă vărsarea Gangelui.", "lume", 22, 90, "Delta Gangelui", 500, "Gangele și Brahmaputra formează o deltă uriașă în Golful Bengal.")
    H.p(3, "2.1", "Atinge pe hartă vărsarea fluviului Yangtze.", "lume", 31.4, 121.8, "vărsarea Yangtze", 400, "Yangtze se varsă lângă Shanghai.", surse=S_YANG)
    H.p(3, "2.1", "Atinge pe hartă Marea Aral.", "lume", 45, 60, "Marea Aral", 500, "Aral e între Kazahstan și Uzbekistan.")
    H.a(2, "4.4", "De ce s-a micșorat Marea Aral?", "pentru că apa râurilor care o alimentau a fost folosită pentru irigații", ["din cauza unui vulcan", "din cauza unui tsunami", "pentru că s-a umplut cu gheață"], "E unul dintre cele mai mari dezastre ecologice provocate de om.")
    H.a(2, "3.2", "De ce râurile din Siberia produc inundații primăvara?", "pentru că se topesc întâi în sud, iar gheața din nord blochează apa", ["pentru că plouă tropical", "pentru că marea urcă", "pentru că sunt vulcani"], "Obi, Enisei și Lena curg spre nord.")
    H.a(2, "3.2", "Ce hidrocentrală, cea mai mare din lume, e pe Yangtze?", "Trei Defileuri", ["Porțile de Fier", "Itaipu", "Hoover"], "Barajul Trei Defileuri e în China.")
    H.a(2, "1.1", "Ce înseamnă un bazin endoreic?", "un bazin ale cărui ape nu ajung la ocean", ["un lac de munte", "un râu foarte lung", "o deltă"], "Apele se adună în lacuri interioare, ca Marea Caspică sau Aral.")
    H.a(2, "2.1", "Ce fluviu e sfânt pentru hinduși?", "Gange", ["Yangtze", "Lena", "Eufrat"], "Credincioșii se scaldă în Gange la Varanasi.")
    H.a(2, "2.1", "Ce fluviu chinez e numit „Fluviul Galben”?", "Huang He", ["Yangtze", "Amur", "Mekong"], "Culoarea vine de la mâlul galben (loess).")
    H.adev(2, "3.2", "Fluviile Siberiei, care curg spre Oceanul Arctic, îngheață iarna.", True, "Adevărat: iernile sunt foarte geroase.")
    H.adev(2, "1.2", "Marea Moartă e un lac cu apă dulce.", False, "Fals: e unul dintre cele mai sărate lacuri din lume.")
    H.l(2, "2.1", "Completează.", "Cel mai adânc lac este [Baikal], iar cel mai mare lac este Marea [Caspică].", ["Aral", "Moartă"], "Baikal și Caspica.")
    H.l(2, "3.3", "Completează.", "Între fluviile [Tigru] și Eufrat a apărut civilizația [Mesopotamiei].", ["Gange", "Egiptului"], "Mesopotamia = „între râuri”.")
    H.o(3, "4.2 3.1", "Ordonează fluviile după lungime, descrescător.", ["Yangtze", "Huang He", "Mekong", "Gange"], "Lungime, descrescător", "Yangtze ~6 300 km, Huang He ~5 460 km, Mekong ~4 350 km, Gange ~2 500 km.", surse=["Encyclopaedia Britannica – Yangtze / Huang He / Mekong / Ganges", "Wikipedia – List of rivers of Asia"])
    H.g(3, "2.3 4.1", "Graficul arată suprafața Mării Aral în ani diferiți (valori aproximative). Ce s-a întâmplat?", grafic("profil", "Suprafața Mării Aral (aproximativ)", [("1960", 68), ("1990", 36), ("2010", 14)], "mii km²", "NASA Earth Observatory – The Shrinking Aral Sea"), "lacul s-a micșorat foarte mult", ["lacul a crescut", "a rămas la fel", "a dispărut în 1960"], "Irigațiile au secat afluenții.", surse=["NASA Earth Observatory – World of Change: Shrinking Aral Sea", "Encyclopaedia Britannica – Aral Sea"])
    H.d(2, "2.1", "Ce lac mare e marcat pe hartă?", "lume", 42, 51, "Marea Caspică", ["Baikal", "Marea Aral", "Balhaș"], "Caspica e la granița Europei cu Asia.")
    H.a(2, "3.2", "La ce folosesc fluviile Asiei pentru agricultură?", "irigarea orezăriilor și a câmpurilor", ["la extragerea petrolului", "la creșterea renilor", "la nimic"], "Orezul are nevoie de multă apă.")
    H.a(3, "4.3", "De ce delta Gangelui e foarte populată, deși se inundă des?", "solurile aluviale sunt foarte fertile și pot da mai multe recolte de orez pe an", ["pentru că nu plouă niciodată", "pentru că e deșert", "pentru că e la pol"], "Fertilitatea atrage oamenii.")
    H.a(2, "2.1", "Ce fluviu traversează mai multe țări din Indochina (Laos, Thailanda, Cambodgia, Vietnam)?", "Mekong", ["Yangtze", "Indus", "Lena"], "Mekong se varsă în Marea Chinei de Sud.")
    H.a(2, "3.4", "De ce Baikalul e în patrimoniul UNESCO?", "pentru apa foarte curată și speciile unice, care nu trăiesc nicăieri altundeva", ["pentru că e sărat", "pentru că e mic", "pentru că e artificial"], "Foca de Baikal trăiește doar aici.", surse=S_BAIKAL)
    H.a(2, "2.1", "Prin ce țară curge Indusul, în cea mai mare parte?", "Pakistan", ["India", "China", "Iran"], "Indusul izvorăște din Tibet și se varsă în Marea Arabiei.")
    H.a(2, "2.2", "De ce Marea Moartă e atât de sărată?", "apa se evaporă puternic, iar sarea rămâne, pentru că lacul nu are scurgere", ["pentru că e legată de ocean", "pentru că plouă mult", "pentru că e foarte adâncă și rece"], "Clima caldă și uscată concentrează sarea.")

    H.a(2, "2.1", "Ce fluvii din Siberia curg spre Oceanul Arctic?", "Obi, Enisei, Lena", ["Gange, Indus", "Tigru, Eufrat", "Mekong, Yangtze"], "Toate trei îngheață iarna.")

    # ================================================================ S5 Clima. Musonii
    C = Lectie(7, "VII-S05-diferentieri-climatice-musonii", "Asia – diferențieri climatice. Musonii",
               "De ce în India plouă torențial vara, dar aproape deloc iarna?",
               [("Climatele Asiei", "Asia are aproape toate tipurile de climă: ecuatorial (Indonezia, Malaysia), musonic (India, Asia de Sud-Est, estul Chinei), tropical deșertic (Arabia), temperat continental (Siberia, Mongolia, cu ierni foarte geroase), subpolar și polar (nordul Siberiei), montan (Himalaya, Tibet).\nLa Oimiakon (Siberia) s-au măsurat temperaturi sub −67 °C, printre cele mai scăzute din emisfera nordică."),
                ("Musonii", "Musonii sunt vânturi care își schimbă direcția de la un anotimp la altul.\nVara, uscatul Asiei se încălzește puternic; aerul umed de deasupra Oceanului Indian e atras spre continent și aduce ploi abundente (musonul de vară).\nIarna, uscatul se răcește; aerul rece și uscat bate dinspre continent spre ocean (musonul de iarnă), deci plouă puțin."),
                ("Urmări", "Musonul de vară aduce apa pentru orezării, dar și inundații. Dacă întârzie, apare seceta.\nLa Mawsynram și Cherrapunji, în nord-estul Indiei, cade una dintre cele mai mari cantități de ploaie din lume, în medie peste 11 000 l/m² pe an.")],
               stiaica="Cuvântul „muson” vine din arabul „mawsim”, care înseamnă „anotimp”.",
               ref=REF.format("Diferențieri climatice. Musonii"))
    C.a(1, "1.1", "Ce sunt musonii?", "vânturi care își schimbă direcția de la un anotimp la altul", ["vânturi care bat mereu din aceeași direcție", "ploi de gheață", "curenți oceanici"], "Musonul de vară vine dinspre ocean, cel de iarnă dinspre continent.")
    C.a(2, "2.2", "De ce musonul de vară aduce ploi?", "pentru că bate dinspre ocean, cu aer umed, spre uscatul încălzit", ["pentru că vine din deșert", "pentru că vine de la pol", "pentru că e rece și uscat"], "Aerul umed urcă pe uscat și se descarcă.")
    C.a(2, "2.2", "De ce iarna, în India, plouă puțin?", "pentru că musonul de iarnă bate dinspre continentul rece și uscat", ["pentru că bate dinspre ocean", "pentru că ninge peste tot", "pentru că e foarte cald"], "Aerul continental e uscat.")
    C.o(3, "2.2 3.1 4.2", "Ordonează cum se formează musonul de vară.", ["vara, uscatul Asiei se încălzește puternic", "aerul cald de deasupra uscatului urcă", "aerul umed de pe Oceanul Indian e atras spre uscat", "aerul umed urcă pe munți și se răcește", "cad ploi abundente"], "Formarea musonului", "Diferența de temperatură uscat–ocean pune aerul în mișcare.")
    C.s(2, "2.1", "Asociază regiunea cu climatul.", [("Indonezia", "ecuatorial"), ("India", "musonic"), ("Peninsula Arabia", "tropical deșertic"), ("Siberia", "temperat continental excesiv și subpolar")], "Climatele Asiei.")
    C.a(2, "3.1", "Unde se află unul dintre cele mai ploioase locuri de pe Pământ?", "la Mawsynram, în nord-estul Indiei", ["în Sahara", "în Siberia", "în Arabia"], "Peste 11 000 l/m² pe an, în medie.", surse=S_MAWS)
    C.a(2, "2.2", "De ce Siberia are ierni atât de geroase?", "pentru că e foarte departe de ocean și la latitudini mari", ["pentru că e la Ecuator", "pentru că are vulcani", "pentru că plouă mult"], "Continentalismul face iernile extreme.")
    C.p(2, "2.1", "Atinge pe hartă India, țara musonilor.", "lume", 21, 78, "India", 900, "India e în sudul Asiei.")
    C.p(3, "2.1", "Atinge pe hartă Oimiakon, în Siberia, unul dintre cele mai reci locuri locuite.", "lume", 63.5, 142.8, "Oimiakon", 800, "Oimiakon e în Republica Saha (Iakutia), Rusia.")
    C.g(3, "2.3 4.1", "Diagrama arată precipitațiile lunare la o stație imaginară din India. Când cad cele mai multe ploi?", grafic("bare", "Precipitații lunare (stație imaginară, climat musonic)", [("I", 5), ("II", 10), ("III", 15), ("IV", 30), ("V", 120), ("VI", 450), ("VII", 600), ("VIII", 500), ("IX", 300), ("X", 80), ("XI", 15), ("XII", 5)], "l/m²"), "vara (iunie–septembrie)", ["iarna", "primăvara devreme", "uniform tot anul"], "Musonul de vară aduce aproape toată ploaia anului.")
    C.g(3, "2.3 4.1", "La aceeași stație imaginară, cât plouă în iulie comparativ cu ianuarie?", grafic("bare", "Precipitații lunare (stație imaginară, climat musonic)", [("I", 5), ("II", 10), ("III", 15), ("IV", 30), ("V", 120), ("VI", 450), ("VII", 600), ("VIII", 500), ("IX", 300), ("X", 80), ("XI", 15), ("XII", 5)], "l/m²"), "de 120 de ori mai mult", ["de 2 ori mai mult", "la fel", "de 10 ori mai puțin"], "600 : 5 = 120.")
    C.a(2, "3.3", "De ce musonul e important pentru agricultura Indiei?", "aduce apa pentru orez și alte culturi", ["aduce zăpadă", "oprește ploile", "aduce petrol"], "Recoltele depind de ploile musonice.")
    C.a(2, "4.4", "Ce probleme poate aduce musonul?", "inundații, alunecări de teren și, dacă întârzie, secetă", ["doar beneficii", "cutremure", "erupții"], "Musonul e esențial, dar și periculos.")
    C.a(2, "2.2", "Ce climat are Peninsula Arabia?", "tropical deșertic, foarte cald și uscat", ["ecuatorial", "musonic", "polar"], "Arabia e unul dintre cele mai uscate locuri.")
    C.a(2, "2.2", "Ce climat au insulele Indoneziei?", "ecuatorial: cald și umed tot anul", ["polar", "temperat continental", "deșertic"], "Indonezia e pe Ecuator.")
    C.adev(2, "2.2", "Musonii bat tot anul din aceeași direcție.", False, "Fals: își schimbă direcția vara și iarna.")
    C.adev(2, "2.2", "Climatul Tibetului e rece, deși e la latitudinea Africii de Nord.", True, "Adevărat: altitudinea mare face clima rece.")
    C.l(2, "1.1", "Completează.", "Vânturile care își schimbă direcția după anotimp se numesc [musoni]; vara ei aduc [ploi].", ["alizee", "secetă"], "Musonii.")
    C.l(2, "2.2", "Completează.", "Siberia are ierni geroase, pentru că e departe de [ocean]; Arabia e foarte uscată, cu climat [deșertic].", ["munte", "ecuatorial"], "Continentalism și deșert.")
    C.a(2, "2.2", "Ce sunt taifunurile?", "cicloni tropicali puternici din vestul Pacificului (Filipine, China, Japonia)", ["vânturi reci din Siberia", "furtuni de nisip", "ploi de gheață"], "Taifun e numele uraganului în Asia de Est.")
    C.a(3, "4.3", "Compară vara la Mumbai cu vara la Riad.", "la Mumbai plouă foarte mult (muson); la Riad e foarte cald și uscat (deșert)", ["sunt identice", "la Riad plouă mai mult", "la Mumbai e zăpadă"], "Musonic față de deșertic.")
    C.d(2, "2.1", "Ce țară insulară, lovită des de taifunuri, e marcată pe hartă?", "lume", 12.5, 122, "Filipine", ["Japonia", "Indonezia", "Sri Lanka"], "Filipinele sunt în vestul Pacificului.")
    C.a(2, "2.2", "Ce înseamnă climat temperat continental excesiv?", "diferențe foarte mari între vară și iarnă, cu puține precipitații", ["cald și ploios tot anul", "frig tot anul", "ploi doar iarna"], "E climatul Mongoliei și al Siberiei de Sud.")
    C.a(2, "3.2", "Ce temperatură minimă s-a măsurat în zona Oimiakon–Verhoiansk?", "sub −67 °C", ["−10 °C", "−30 °C", "0 °C"], "Sunt cele mai reci locuri locuite din emisfera nordică.", surse=["Encyclopaedia Britannica – Oymyakon", "WMO – Verkhoyansk record −67,8 °C (1892)"])
    C.a(3, "2.2", "De ce Himalaya are rol de barieră climatică?", "oprește aerul rece din nord să ajungă în India și reține ploile musonice pe versantul sudic", ["nu are niciun rol", "aduce deșertul în India", "răcește oceanul"], "Versantul sudic e ploios; Tibetul, la nord, e uscat.")
    C.a(2, "3.4", "Ce oraș din India e cunoscut pentru ploile musonice?", "Mumbai", ["Riad", "Ulan Bator", "Novosibirsk"], "Mumbai primește ploi torențiale vara.")
    C.a(2, "2.2", "Ce climat e în nordul Siberiei, pe țărmul Oceanului Arctic?", "polar și subpolar", ["ecuatorial", "musonic", "mediteranean"], "Acolo e tundra.")
    C.a(2, "2.2", "Ce climat e pe țărmul estic al Mediteranei (Liban, Israel)?", "mediteranean", ["polar", "musonic", "ecuatorial"], "Veri calde și uscate, ierni blânde.")
    C.a(3, "3.3", "De ce în Asia de Sud-Est se pot face două sau trei recolte de orez pe an?", "pentru că e cald tot anul și există apă din abundență", ["pentru că e frig", "pentru că e deșert", "pentru că nu plouă"], "Clima permite culturi continue.")

    C.a(2, "2.2", "Ce climat are Japonia, în cea mai mare parte?", "temperat, cu influențe musonice și oceanice", ["deșertic", "polar", "ecuatorial"], "Japonia are patru anotimpuri și ploi multe.")

    # ================================================================ S6 Contraste biogeografice
    B = Lectie(7, "VII-S06-contraste-biogeografice", "Asia – contraste biogeografice",
               "Unde poți întâlni în Asia tigri, panda și urși polari?",
               [("Zone de vegetație", "De la nord la sud: tundra (nordul Siberiei), taigaua (cea mai mare pădure de conifere din lume, în Siberia), pădurile de amestec și de foioase, stepa (Kazahstan, Mongolia), deșerturile (Gobi, Arabia, Thar), pădurile musonice (India, Indochina), pădurile ecuatoriale (Indonezia, Malaysia).\nPe munții înalți, vegetația se etajează cu altitudinea."),
                ("Fauna", "Tundra: reni, vulpi polare. Taigaua: urs brun, tigrul siberian (Amur), râs. Stepa și deșertul: cămila bactriană (cu două cocoașe), calul sălbatic Przewalski. Pădurile musonice și ecuatoriale: tigrul bengalez, elefantul asiatic, rinocerul, urangutanul (Borneo, Sumatra). Munții Chinei: panda uriaș."),
                ("Protecție", "Multe specii asiatice sunt amenințate de defrișări, braconaj și extinderea plantațiilor (de exemplu, palmierul de ulei în Indonezia). Se înființează parcuri naționale și rezervații.")],
               stiaica="Urangutan înseamnă în limba malaeză „omul pădurii”. El trăiește doar în insulele Borneo și Sumatra.",
               ref=REF.format("Contraste biogeografice"))
    B.o(2, "2.2 3.1 4.2", "Ordonează zonele de vegetație ale Asiei de la nord la sud.", ["tundra", "taigaua", "stepa", "deșertul", "pădurea musonică", "pădurea ecuatorială"], "De la nord la sud", "De la Oceanul Arctic spre Ecuator.")
    B.s(1, "3.3", "Asociază animalul cu zona în care trăiește.", [("tigrul siberian", "taiga"), ("cămila bactriană", "deșertul Gobi"), ("urangutanul", "pădurea ecuatorială din Borneo"), ("renul", "tundra")], "Fauna Asiei.")
    B.a(1, "3.3", "Unde trăiește panda uriaș?", "în pădurile de bambus din munții Chinei", ["în Siberia", "în Arabia", "în Japonia"], "Panda se hrănește aproape doar cu bambus.")
    B.a(1, "3.3", "Unde trăiește urangutanul?", "în Borneo și Sumatra", ["în Siberia", "în India", "în Mongolia"], "Doar în aceste două insule.")
    B.a(2, "1.1", "Ce este taigaua siberiană?", "cea mai mare pădure de conifere din lume", ["un deșert", "o savană", "o tundră"], "Taigaua acoperă mare parte din Siberia.")
    B.a(2, "3.3", "Câte cocoașe are cămila bactriană din Asia?", "două", ["una", "trei", "niciuna"], "Dromaderul, din Africa și Arabia, are una.")
    B.p(2, "2.1", "Atinge pe hartă insula Borneo, unde trăiește urangutanul.", "lume", 0.5, 114, "Borneo", 600, "Borneo e împărțită între Indonezia, Malaysia și Brunei.")
    B.p(3, "2.1", "Atinge pe hartă Mongolia, cu stepe și deșertul Gobi.", "lume", 47, 103, "Mongolia", 700, "Mongolia e între Rusia și China.")
    B.a(2, "3.3", "Ce tigru trăiește în pădurile Indiei?", "tigrul bengalez", ["tigrul siberian", "tigrul de zăpadă", "jaguarul"], "Tigrul bengalez e animalul național al Indiei.")
    B.a(2, "4.4", "Ce amenință pădurile ecuatoriale din Indonezia?", "defrișarea pentru plantații de palmier de ulei", ["prea multe ploi", "zăpada", "vulcanii stinși"], "Defrișările distrug habitatul urangutanului.")
    B.a(2, "3.3", "Ce vegetație e tipică pentru Kazahstan și Mongolia?", "stepa", ["pădurea ecuatorială", "tundra", "pădurea musonică"], "Ierburi întinse, aproape fără copaci.")
    B.a(2, "3.3", "Ce animal e simbolul Fondului Mondial pentru Natură (WWF)?", "panda uriaș", ["tigrul", "elefantul", "urangutanul"], "Panda a devenit un simbol al protecției naturii.")
    B.adev(2, "3.3", "În Asia trăiesc atât tigri, cât și reni.", True, "Adevărat: tigri în sud și în taiga, reni în tundră.")
    B.adev(2, "3.3", "Elefanții asiatici trăiesc în tundra Siberiei.", False, "Fals: trăiesc în pădurile calde din India și Asia de Sud-Est.")
    B.l(2, "3.3", "Completează.", "Pădurea de conifere din Siberia se numește [taiga]; în pădurile de bambus din China trăiește [panda].", ["savană", "renul"], "Taiga și panda.")
    B.l(2, "3.3", "Completează.", "Cămila asiatică cu două cocoașe se numește cămilă [bactriană]; urangutanul trăiește în [Borneo] și Sumatra.", ["dromader", "Japonia"], "Bactriană, Borneo.")
    B.a(3, "4.3", "Compară taigaua cu pădurea ecuatorială.", "taigaua are puține specii de conifere și ierni lungi; pădurea ecuatorială are foarte multe specii și e caldă tot anul", ["sunt identice", "taigaua are mai multe specii", "pădurea ecuatorială are ierni lungi"], "Clima explică diferențele.")
    B.a(2, "3.3", "Ce plantă e importantă în pădurile musonice și se folosește la construcții?", "bambusul (și tecul)", ["cactusul", "lichenul", "molidul"], "Bambusul crește foarte repede.")
    B.d(2, "2.1", "Ce insulă indoneziană, unde trăiesc urangutani și tigri, e marcată pe hartă?", "lume", 0, 102, "Sumatra", ["Java", "Borneo", "Sri Lanka"], "Sumatra e în vestul Indoneziei.")
    B.a(2, "3.3", "Ce animal sălbatic, rudă a calului, trăiește în stepele Mongoliei?", "calul Przewalski", ["zebra", "cămila", "renul"], "A fost reintrodus în natură în Mongolia.")
    B.a(2, "3.3", "Ce animal trăiește în munții înalți ai Asiei centrale (Himalaya)?", "leopardul zăpezilor", ["leul", "zebra", "cangurul"], "Are blană deasă și coadă lungă.")
    B.a(3, "2.2", "De ce în Asia există o asemenea varietate de peisaje?", "pentru că se întinde de la Arctic la Ecuator și are munți foarte înalți", ["pentru că e mică", "pentru că e plată", "pentru că e toată la Ecuator"], "Latitudinea și altitudinea creează diversitatea.")
    B.a(2, "4.4", "Ce pot face oamenii pentru protejarea tigrilor?", "parcuri naționale, oprirea braconajului și a defrișărilor", ["vânătoare liberă", "tăierea pădurilor", "construirea de autostrăzi prin rezervații"], "Numărul tigrilor scade din cauza omului.")
    B.a(2, "3.3", "Ce vegetație se află la poalele Himalayei, pe versantul sudic?", "păduri musonice și subtropicale", ["tundră", "deșert", "taiga"], "Versantul sudic e cald și ploios.")
    B.g(3, "2.3 4.1", "Graficul arată numărul de specii de mamifere în trei regiuni imaginare. Ce regiune e, probabil, pădurea ecuatorială?", grafic("bare", "Specii de mamifere (date imaginare)", [("regiunea A", 40), ("regiunea B", 320), ("regiunea C", 110)], "specii"), "regiunea B", ["regiunea A", "regiunea C", "toate"], "Pădurea ecuatorială are cea mai mare biodiversitate.")
    B.a(2, "3.3", "Ce animal mare din Asia are urechi mai mici decât ruda lui din Africa?", "elefantul asiatic", ["girafa", "rinocerul alb", "zebra"], "Elefantul asiatic e domesticit în India și Thailanda.")
    B.a(2, "4.4", "Ce problemă a apărut în Delta Gangelui, în pădurea de mangrove Sundarbans?", "creșterea nivelului mării și furtunile amenință mangrovele și tigrii", ["e acoperită de zăpadă", "a devenit deșert", "e plină de vulcani"], "Sundarbans e patrimoniu UNESCO.")
    B.a(2, "3.3", "Ce sunt mangrovele?", "păduri de copaci care cresc în apa sărată de pe țărmurile calde", ["păduri de conifere", "ierburi de stepă", "plante de deșert"], "Mangrovele apără țărmul de valuri.")
    B.a(2, "3.3", "Ce animal din tundra Siberiei e crescut de popoarele nordului?", "renul", ["cămila", "vaca", "lama"], "Renii dau carne, lapte, blană și transport.")
    B.a(3, "4.3", "De ce în Gobi trăiesc puține animale, iar în Borneo foarte multe?", "Gobi e uscat și cu ierni geroase; Borneo e cald și umed tot anul", ["Gobi e mai cald", "Borneo e un deșert", "nu e nicio diferență"], "Apa și căldura susțin viața.")

    # ================================================================ S7 Expediție: un stat asiatic
    E = Expeditie(7, "VII-S07-aplicatii-practice-studii-caz", "Expediție: un stat al Asiei",
                  "Ce face Japonia, India sau China unice?",
                  ref=REF.format("Aplicații practice/studii de caz: Particularități geografice ale unor state"))
    E.a(1, "4.1", "Care e primul pas într-un studiu de caz despre un stat?", "aleg statul și îl localizez pe hartă", ["scriu concluziile", "fac o prezentare fără date", "copiez un text"], "Localizarea e baza oricărei caracterizări.")
    E.pas("1. Alege statul", "Alege un stat din Asia: Japonia, India, China, Arabia Saudită, Indonezia sau altul. Localizează-l pe hartă.")
    E.a(2, "4.2", "Ce particularitate geografică are Japonia?", "e un arhipelag vulcanic, cu cutremure frecvente", ["e un deșert", "nu are ieșire la mare", "e acoperită de taiga"], "Japonia e în Cercul de Foc al Pacificului.")
    E.a(2, "4.2", "Ce particularitate geografică are Arabia Saudită?", "e aproape toată deșert și are rezerve mari de petrol", ["e acoperită de gheață", "are musoni puternici", "are cele mai mari lacuri"], "Deșertul Rub al-Khali e în sudul ei.")
    E.pas("2. Particularitățile", "Găsește 3 particularități ale statului ales: una despre natură, una despre populație, una despre economie. Notează sursa fiecărei informații.",
          jurnal="Scrie cele 3 particularități și sursele lor.")
    E.s(2, "4.2", "Asociază statul asiatic cu un element unic.", [("Japonia", "trenurile de mare viteză Shinkansen"), ("India", "cea mai numeroasă populație"), ("China", "Marele Zid"), ("Nepal", "vârful Everest")], "Fiecare stat are ceva special.")
    E.pas("3. Harta tematică", "Desenează harta statului cu relieful principal, un râu, capitala și o resursă importantă.",
          jurnal="Fotografiază harta.", foto=True)
    E.pas("4. Prezentarea", "Prezintă statul colegilor în 2 minute. Încheie cu o întrebare pentru ei.",
          jurnal="Scrie întrebarea pe care ai pus-o și ce au răspuns colegii.")

    # ================================================================ S8 Diversitatea umană
    D = Lectie(7, "VII-S08-elemente-diversitate-umana-diversitate", "Asia – diversitatea umană",
               "În câte religii mari ale lumii și-au avut originea în Asia?",
               [("Populația", "În Asia trăiesc aproape 6 din 10 oameni ai planetei – aproximativ 4,8 miliarde de locuitori, după ONU. India și China au fiecare peste 1,4 miliarde de locuitori.\nPopulația e foarte densă în câmpiile și deltele marilor fluvii (Gange, Yangtze), pe țărmuri și în Japonia, și foarte rară în Siberia, deșerturi și Tibet."),
                ("Diversitatea etnică și lingvistică", "În Asia trăiesc sute de popoare și se vorbesc mii de limbi: chineza (cea mai vorbită limbă maternă din lume), hindi, bengali, japoneza, araba, persana, turca, indoneziana.\nScrierile sunt și ele diverse: caractere chinezești, alfabetul arab, devanagari (hindi), alfabetul coreean."),
                ("Diversitatea religioasă", "Toate marile religii ale lumii au apărut în Asia: iudaismul, creștinismul și islamul (în Orientul Apropiat), hinduismul și budismul (în India).\nAstăzi: islamul în Asia de Sud-Vest, Indonezia, Pakistan; hinduismul în India și Nepal; budismul în China, Japonia, Thailanda, Tibet; creștinismul în Filipine.")],
               stiaica="Indonezia, o țară cu mii de insule, e țara cu cei mai mulți musulmani din lume.",
               ref=REF.format("Elemente de diversitate umană"))
    D.a(1, "3.1", "Câți oameni trăiesc în Asia, aproximativ?", "4,8 miliarde", ["480 de milioane", "48 de milioane", "48 de miliarde"], "Aproape 6 din 10 oameni ai planetei.", surse=S_POP)
    D.a(2, "3.1", "Ce două țări asiatice au fiecare peste 1,4 miliarde de locuitori?", "India și China", ["Japonia și Coreea", "Rusia și Mongolia", "Indonezia și Filipine"], "Din 2023, India e pe primul loc.", surse=S_INDIA)
    D.a(2, "2.2", "Unde e cel mai densă populația Asiei?", "în câmpiile și deltele marilor fluvii", ["în Siberia", "în Tibet", "în deșertul Gobi"], "Agricultura irigată a atras oamenii.")
    D.a(2, "3.3", "Ce religii au apărut în India?", "hinduismul și budismul", ["islamul și creștinismul", "iudaismul și creștinismul", "șintoismul și taoismul"], "Budismul s-a răspândit apoi în China și Japonia.")
    D.a(2, "3.3", "Ce religii au apărut în Orientul Apropiat?", "iudaismul, creștinismul și islamul", ["hinduismul și budismul", "șintoismul", "confucianismul"], "Ierusalimul e un oraș sfânt pentru toate trei.")
    D.s(2, "3.3", "Asociază țara cu religia majoritară.", [("India", "hinduism"), ("Indonezia", "islam"), ("Thailanda", "budism"), ("Filipine", "creștinism (catolic)")], "Diversitate religioasă.")
    D.a(2, "3.3", "Ce țară are cei mai mulți musulmani din lume?", "Indonezia", ["Arabia Saudită", "Turcia", "Iran"], "Indonezia are peste 200 de milioane de musulmani.")
    D.a(2, "3.3", "Ce limbă e cea mai vorbită limbă maternă din lume?", "chineza (mandarina)", ["engleza", "spaniola", "hindi"], "Chineza mandarină are cei mai mulți vorbitori nativi.")
    D.s(2, "3.3", "Asociază limba cu scrierea ei.", [("chineza", "caractere (ideograme)"), ("araba", "alfabet arab, de la dreapta la stânga"), ("hindi", "scriere devanagari"), ("coreeana", "alfabet coreean (hangul)")], "Scrieri diferite.")
    D.p(2, "2.1", "Atinge pe hartă Ierusalim, oraș sfânt pentru trei religii.", "lume", 31.78, 35.22, "Ierusalim", 300, "Ierusalimul e în Orientul Apropiat.")
    D.p(3, "2.1", "Atinge pe hartă Mecca, orașul sfânt al islamului.", "lume", 21.42, 39.83, "Mecca", 400, "Mecca e în vestul Arabiei Saudite.")
    D.adev(2, "3.3", "Toate marile religii ale lumii au apărut în Asia.", True, "Adevărat: iudaismul, creștinismul, islamul, hinduismul, budismul.")
    D.adev(2, "2.2", "Siberia e una dintre cele mai dens populate regiuni ale Asiei.", False, "Fals: e foarte slab populată din cauza frigului.")
    D.l(2, "3.3", "Completează.", "Budismul a apărut în [India] și s-a răspândit în China și [Japonia].", ["Arabia", "Turcia"], "India, Japonia.")
    D.l(2, "3.1", "Completează.", "Asia are aproximativ [4,8] miliarde de locuitori; cea mai populată țară este [India].", ["1,5", "China"], "4,8 miliarde; India.", surse=S_POP)
    D.g(3, "2.3 4.1", "Graficul arată populația continentelor (miliarde, valori rotunjite). Ce observi?", grafic("bare", "Populația continentelor (2024, rotunjit)", [("Asia", 4.8), ("Africa", 1.5), ("Europa", 0.74), ("America", 1.05), ("Oceania", 0.05)], "miliarde", "ONU – World Population Prospects 2024"), "Asia are mai mulți locuitori decât toate celelalte continente la un loc", ["Africa are cei mai mulți locuitori", "Europa are cei mai mulți", "sunt egale"], "4,8 față de aproximativ 3,3 miliarde.", surse=S_POP)
    D.a(2, "3.3", "Ce înseamnă diversitate culturală?", "existența mai multor culturi, cu tradiții, limbi și obiceiuri diferite", ["toți oamenii sunt la fel", "o singură limbă", "o singură religie"], "Asia e un exemplu de diversitate.")
    D.a(2, "3.3", "Ce sărbătoare marchează Anul Nou în China?", "Anul Nou Chinezesc (Festivalul Primăverii)", ["Crăciunul", "Diwali", "Ramadanul"], "Se sărbătorește în ianuarie sau februarie.")
    D.a(2, "3.3", "Ce sărbătoare hindusă e numită „festivalul luminilor”?", "Diwali", ["Ramadan", "Hanuka", "Paștele"], "Diwali se sărbătorește toamna.")
    D.a(3, "4.3", "De ce Japonia are populație îmbătrânită, iar Afganistanul are mulți tineri?", "în Japonia se nasc puțini copii și oamenii trăiesc mult; în Afganistan natalitatea e mare", ["Japonia are natalitate foarte mare", "Afganistanul nu are copii", "sunt identice"], "Diferențe de dezvoltare și tradiții.")
    D.d(2, "2.1", "Ce țară, cu cea mai mare populație musulmană, e marcată pe hartă?", "lume", -2, 118, "Indonezia", ["Malaysia", "Filipine", "Thailanda"], "Indonezia e un arhipelag uriaș.")
    D.a(2, "3.3", "Ce popor trăiește în Tibet?", "tibetanii, majoritar budiști", ["arabii", "japonezii", "turcii"], "Lhasa e orașul principal al Tibetului.")
    D.a(2, "2.2", "Ce regiune a Asiei are populație foarte rară, din cauza altitudinii?", "Podișul Tibet", ["Câmpia Gangelui", "Delta Yangtze", "Japonia"], "Altitudinea și frigul limitează locuirea.")
    D.a(3, "3.3", "De ce în India se vorbesc foarte multe limbi?", "pentru că e o țară uriașă, cu multe popoare și istorii diferite", ["pentru că e mică", "pentru că toți au venit recent", "pentru că așa e legea"], "India are 22 de limbi recunoscute în Constituție.")
    D.a(2, "3.3", "Ce religie e specifică Japoniei, alături de budism?", "șintoismul", ["hinduismul", "islamul", "iudaismul"], "Șintoismul venerează spiritele naturii.")
    D.a(2, "3.4", "Ce monument din India e un mausoleu din marmură albă, în patrimoniul UNESCO?", "Taj Mahal", ["Marele Zid", "Angkor Wat", "Petra"], "Taj Mahal e la Agra.")
    D.a(2, "3.4", "Ce monument uriaș se află în China?", "Marele Zid Chinezesc", ["Taj Mahal", "Petra", "Borobudur"], "Marele Zid e în patrimoniul UNESCO.")
    D.a(2, "3.4", "Ce templu mare din Cambodgia e în patrimoniul UNESCO?", "Angkor Wat", ["Taj Mahal", "Petra", "Marele Zid"], "Angkor Wat apare și pe steagul Cambodgiei.")
    D.a(3, "4.3", "Ce au în comun Ierusalimul și Mecca?", "sunt orașe sfinte, vizitate de pelerini", ["sunt capitale ale aceleiași țări", "sunt în Japonia", "sunt pe malul Gangelui"], "Pelerinajul e important în religiile Asiei.")

    D.a(2, "3.3", "În ce țară se află orașul Varanasi, pe Gange, sfânt pentru hinduși?", "India", ["Nepal", "Pakistan", "Bangladesh"], "Varanasi e unul dintre cele mai vechi orașe locuite continuu.")

    # ================================================================ S9 Harta politică și aglomerările urbane
    A = Lectie(7, "VII-S09-harta-politica-marile-aglomerari", "Asia – harta politică și marile aglomerări urbane",
               "Care sunt cele mai mari orașe ale lumii și de ce sunt aproape toate în Asia?",
               [("Statele Asiei", "Asia are aproape 50 de state. Cele mai mari ca suprafață: Rusia (partea asiatică), China, India, Kazahstan, Arabia Saudită. State insulare: Japonia, Filipine, Indonezia, Sri Lanka, Singapore, Maldive.\nRegiuni: Asia de Est (China, Japonia, Coreea), Asia de Sud-Est (Indonezia, Vietnam, Thailanda), Asia de Sud (India, Pakistan, Bangladesh), Asia de Sud-Vest / Orientul Mijlociu (Turcia, Iran, Arabia Saudită, Israel), Asia Centrală (Kazahstan, Uzbekistan), Asia de Nord (Siberia)."),
                ("Marile aglomerări urbane", "Asia are cele mai multe megaorașe (peste 10 milioane de locuitori). După raportul ONU din 2025, primele trei aglomerări urbane ale lumii sunt Jakarta, Dhaka și Tokyo. Alte megaorașe: Shanghai, Beijing, Delhi, Mumbai, Manila, Karachi, Seul.\nAglomerările cresc rapid prin migrația de la sat la oraș."),
                ("Probleme și soluții", "Marile orașe au trafic aglomerat, poluare, cartiere sărace (mahalale), lipsă de apă curată. Soluții: metrou, trenuri rapide, locuințe sociale, parcuri.")],
               stiaica="Singapore e un oraș-stat: întreaga țară e un singur oraș, construit pe o insulă de la capătul Peninsulei Malacca.",
               ref=REF.format("Harta politică și marile aglomerări umane"))
    A.s(1, "2.1", "Asociază statul cu capitala.", [("China", "Beijing"), ("Japonia", "Tokyo"), ("India", "New Delhi"), ("Turcia", "Ankara")], "Capitale asiatice.")
    A.s(1, "2.1", "Asociază statul cu capitala.", [("Indonezia", "Jakarta"), ("Coreea de Sud", "Seul"), ("Iran", "Teheran"), ("Thailanda", "Bangkok")], "Alte capitale asiatice.")
    A.a(1, "3.1", "Care sunt primele trei aglomerări urbane ale lumii, după raportul ONU din 2025?", "Jakarta, Dhaka, Tokyo", ["Paris, Londra, Berlin", "New York, Los Angeles, Chicago", "Moscova, Istanbul, Roma"], "Toate trei sunt în Asia.", surse=S_ORASE)
    A.a(2, "1.1", "Ce este un oraș-stat?", "o țară formată dintr-un singur oraș", ["un oraș fără locuitori", "un sat mare", "o capitală de provincie"], "Singapore e un oraș-stat.")
    A.p(2, "2.1", "Atinge pe hartă Singapore.", "lume", 1.35, 103.82, "Singapore", 400, "Singapore e la capătul Peninsulei Malacca.")
    A.p(2, "2.1", "Atinge pe hartă Dhaka (Bangladesh).", "lume", 23.8, 90.4, "Dhaka", 400, "Dhaka e în delta Gangelui.", surse=S_ORASE)
    A.p(2, "2.1", "Atinge pe hartă Shanghai.", "lume", 31.23, 121.47, "Shanghai", 400, "Shanghai e la vărsarea fluviului Yangtze.")
    A.p(3, "2.1", "Atinge pe hartă Mumbai.", "lume", 19.08, 72.88, "Mumbai", 400, "Mumbai e pe țărmul vestic al Indiei.")
    A.p(3, "2.1", "Atinge pe hartă Seul.", "lume", 37.57, 126.98, "Seul", 300, "Seul e capitala Coreei de Sud.")
    A.a(2, "3.2", "De ce cresc atât de repede orașele asiatice?", "mulți oameni se mută de la sat la oraș pentru muncă", ["pentru că se nasc doar la oraș copii", "pentru că satele sunt interzise", "pentru că e mai frig la sat"], "Migrația rural–urban.")
    A.a(2, "4.4", "Ce problemă au multe megaorașe asiatice?", "poluarea aerului și traficul aglomerat", ["lipsa totală de oameni", "prea mult spațiu liber", "prea puține clădiri"], "Delhi și Dhaka au aer foarte poluat iarna.")
    A.a(2, "1.1", "Ce sunt mahalalele (slums)?", "cartiere sărace, cu locuințe improvizate și servicii puține", ["cartiere de lux", "parcuri", "zone industriale moderne"], "Apar când orașul crește mai repede decât infrastructura.")
    A.a(2, "2.1", "Care e capitala Japoniei?", "Tokyo", ["Kyoto", "Osaka", "Seul"], "Tokyo e și una dintre cele mai mari aglomerări ale lumii.")
    A.a(2, "2.1", "Ce stat asiatic e cel mai mare ca suprafață, după Rusia?", "China", ["India", "Kazahstan", "Mongolia"], "China are aproximativ 9,6 milioane km².")
    A.a(2, "2.1", "Ce stat din Asia Centrală e cel mai mare stat fără ieșire la ocean din lume?", "Kazahstan", ["Mongolia", "Afganistan", "Nepal"], "Kazahstanul are țărm doar la Marea Caspică, un lac.")
    A.adev(2, "3.2", "Cele mai multe megaorașe ale lumii sunt în Asia.", True, "Adevărat: populația numeroasă și urbanizarea rapidă.", surse=S_ORASE)
    A.adev(2, "2.1", "Jakarta e capitala Japoniei.", False, "Fals: Jakarta e capitala Indoneziei; capitala Japoniei e Tokyo.")
    A.l(2, "2.1", "Completează.", "Capitala Chinei este [Beijing], iar capitala Indiei este [New Delhi].", ["Shanghai", "Mumbai"], "Beijing și New Delhi.")
    A.l(2, "1.1", "Completează.", "Un oraș cu peste 10 milioane de locuitori se numește [megaoraș]; o țară formată dintr-un singur oraș se numește [oraș-stat].", ["sat", "provincie"], "Megaoraș, oraș-stat.")
    A.o(3, "4.3 3.1 4.2", "Ordonează orașele de la vest la est.", ["Istanbul", "Teheran", "Mumbai", "Dhaka", "Shanghai", "Tokyo"], "De la vest la est", "De la Bosfor la Pacific.")
    A.d(2, "2.1", "Ce capitală e marcată pe hartă?", "lume", 39.9, 116.4, "Beijing", ["Shanghai", "Seul", "Tokyo"], "Beijing e în nordul Chinei.")
    A.d(3, "2.1", "Ce megaoraș e marcat pe hartă?", "lume", 28.6, 77.2, "Delhi", ["Mumbai", "Karachi", "Dhaka"], "Delhi e în nordul Indiei.")
    A.g(3, "2.3 4.1", "Graficul arată populația a trei aglomerări urbane după ONU (2025, milioane, rotunjit). Cu cât depășește Jakarta Tokyo?", grafic("bare", "Populația aglomerărilor urbane (2025, rotunjit)", [("Jakarta", 42), ("Dhaka", 37), ("Tokyo", 33)], "milioane", "ONU – World Urbanization Prospects 2025"), "cu aproximativ 9 milioane", ["cu 1 milion", "cu 42 de milioane", "sunt egale"], "42 − 33 = 9 milioane.", surse=S_ORASE)
    A.a(2, "4.4", "Ce soluție a ales Tokyo pentru transportul a milioane de oameni?", "o rețea foarte mare de metrou și trenuri", ["mai multe căruțe", "fără transport public", "doar mașini personale"], "Transportul public e foarte eficient.")
    A.a(2, "2.1", "Ce stat asiatic are capitala Riad?", "Arabia Saudită", ["Iran", "Irak", "Iordania"], "Riad e în centrul Peninsulei Arabia.")
    A.a(2, "2.1", "Ce stat insular din Oceanul Indian e format din atoli?", "Maldive", ["Japonia", "Sri Lanka", "Filipine"], "Maldivele sunt foarte joase, amenințate de creșterea nivelului mării.")
    A.a(3, "3.3", "De ce Indonezia a hotărât să-și mute capitala din Jakarta?", "pentru că Jakarta e foarte aglomerată și se scufundă treptat", ["pentru că Jakarta e prea mică", "pentru că e la pol", "pentru că nu are mare"], "Noua capitală, Nusantara, se construiește în Borneo.", surse=["BBC News – Indonesia's new capital Nusantara", "Reuters – Indonesia capital relocation"])
    A.a(2, "2.1", "Care e capitala Turciei?", "Ankara", ["Istanbul", "Izmir", "Antalya"], "Istanbul e cel mai mare oraș, dar capitala e Ankara.")
    A.a(2, "3.2", "Ce oraș asiatic e un mare centru financiar, cu zgârie-nori, fost colonie britanică?", "Hong Kong", ["Lhasa", "Ulan Bator", "Kabul"], "Hong Kong e o regiune administrativă specială a Chinei.")

    A.a(1, "2.1", "Pe ce continent se află China?", "Asia", ["Europa", "Africa", "Australia"], "China e în estul Asiei.")

    # ================================================================ S10 Resursele naturale
    N = Lectie(7, "VII-S10-resursele-naturale", "Asia – resursele naturale",
               "De ce Orientul Mijlociu e atât de important pentru economia lumii?",
               [("Resurse energetice", "Asia de Sud-Vest (Golful Persic: Arabia Saudită, Iran, Irak, Kuweit, Emiratele Arabe Unite, Qatar) are cele mai mari rezerve de petrol și gaze naturale din lume.\nCărbune: China (cel mai mare producător), India, Indonezia. Siberia are petrol, gaze și cărbune. Hidroenergie: China (Trei Defileuri), India."),
                ("Resurse minerale", "Fier: China, India. Staniu: Malaysia, Indonezia, China. Metale rare (pentru electronice): China. Pietre prețioase: Myanmar, Sri Lanka.\nSiberia are aur, diamante și nichel."),
                ("Resurse ale solului, apei și pădurilor", "Soluri fertile în câmpiile aluviale ale fluviilor (orez, grâu). Păduri: taigaua (lemn), pădurile tropicale (lemn de esență tare, cauciuc).\nApa e o resursă prețioasă în Orientul Mijlociu: aici se folosesc instalații de desalinizare a apei de mare.")],
               stiaica="În țările din Golful Persic, o mare parte din apa potabilă se obține desalinizând apa mării.",
               ref=REF.format("Resursele naturale"))
    N.a(1, "2.1", "Ce regiune a Asiei are cele mai mari rezerve de petrol?", "zona Golfului Persic", ["Siberia de Nord", "Japonia", "Tibetul"], "Arabia Saudită, Iran, Irak, Kuweit, EAU.")
    N.s(2, "3.3", "Asociază resursa cu țara.", [("petrolul", "Arabia Saudită"), ("cărbunele", "China"), ("staniul", "Malaysia"), ("ceaiul", "Sri Lanka")], "Resurse ale Asiei.")
    N.a(2, "2.1", "Ce țară e cel mai mare producător de cărbune din lume?", "China", ["Japonia", "Arabia Saudită", "Nepal"], "China folosește mult cărbune pentru electricitate.")
    N.a(2, "3.2", "Ce face o instalație de desalinizare?", "scoate sarea din apa mării, ca să poată fi băută", ["produce petrol", "face sare de bucătărie doar", "răcește aerul"], "E folosită în țările deșertice.")
    N.a(2, "3.2", "De ce țările din Golful Persic folosesc desalinizarea?", "pentru că au foarte puțină apă dulce", ["pentru că au prea multă apă dulce", "pentru că plouă mult", "pentru că au ghețari"], "Deșertul nu are râuri permanente.")
    N.p(2, "2.1", "Atinge pe hartă Golful Persic.", "lume", 27, 51, "Golful Persic", 500, "Golful Persic e între Arabia și Iran.")
    N.p(3, "2.1", "Atinge pe hartă Arabia Saudită.", "lume", 24, 45, "Arabia Saudită", 800, "Arabia Saudită ocupă cea mai mare parte a Peninsulei Arabia.")
    N.a(2, "3.3", "Ce resurse are Siberia?", "petrol, gaze, cărbune, aur, diamante, lemn", ["cafea și cacao", "banane", "orez"], "Siberia e bogată, dar greu de exploatat din cauza frigului.")
    N.a(2, "3.2", "Ce resursă dau pădurile tropicale din Asia de Sud-Est?", "lemn de esență tare și cauciuc natural", ["petrol", "cărbune", "sare"], "Arborele de cauciuc a fost adus din America de Sud.")
    N.a(2, "3.3", "Ce țară asiatică produce multe metale rare folosite în telefoane?", "China", ["Mongolia", "Nepal", "Bhutan"], "Metalele rare sunt esențiale pentru electronice.")
    N.a(2, "3.2", "Ce resursă e foarte importantă pentru agricultura din Asia musonică?", "apa (ploile musonice și fluviile)", ["petrolul", "zăpada", "nisipul"], "Orezul are nevoie de multă apă.")
    N.adev(2, "3.2", "Țările din Golful Persic au rezerve uriașe de petrol, dar puțină apă dulce.", True, "Adevărat: de aceea folosesc desalinizarea.")
    N.adev(2, "3.2", "Japonia are rezerve uriașe de petrol și cărbune.", False, "Fals: Japonia are puține resurse și importă mult.")
    N.l(2, "3.2", "Completează.", "Cele mai mari rezerve de petrol sunt în jurul Golfului [Persic]; China e cel mai mare producător de [cărbune].", ["Bengal", "aur"], "Golful Persic, cărbune.")
    N.l(2, "3.2", "Completează.", "Scoaterea sării din apa mării se numește [desalinizare]; resursele care se termină sunt [neregenerabile].", ["irigare", "regenerabile"], "Desalinizare, neregenerabile.")
    N.g(3, "2.3 4.1", "Graficul arată, pentru o țară imaginară din Golf, structura exporturilor. Ce produs domină?", grafic("structura", "Exporturi (țară imaginară)", [("petrol și gaze", 75), ("produse chimice", 15), ("altele", 10)], "%"), "petrolul și gazele", ["produsele chimice", "altele", "egal"], "75 % din exporturi.")
    N.a(3, "4.3", "Compară resursele Japoniei cu cele ale Arabiei Saudite.", "Japonia are puține resurse, dar industrie avansată; Arabia Saudită are mult petrol", ["Japonia are mult petrol", "Arabia Saudită are păduri tropicale", "sunt identice"], "Dezvoltarea nu depinde doar de resurse.")
    N.a(2, "4.4", "Ce problemă de mediu aduce exploatarea cărbunelui în China?", "poluarea aerului", ["topirea gheții din Arctica direct", "creșterea pădurilor", "răcirea climei"], "Arderea cărbunelui produce smog.")
    N.a(2, "3.3", "Ce țară asiatică e cunoscută pentru ceai?", "China (și India, Sri Lanka)", ["Rusia", "Mongolia", "Kazahstan"], "Ceaiul crește pe dealuri ploioase.")
    N.d(2, "2.1", "Ce țară bogată în petrol, din Golf, e marcată pe hartă?", "lume", 32, 53, "Iran", ["Irak", "Turcia", "Afganistan"], "Iranul e la nord de Golful Persic.")
    N.a(2, "3.2", "Ce resursă energetică regenerabilă folosește China cel mai mult, după hidroenergie?", "energia solară și eoliană", ["petrolul", "cărbunele", "uraniul"], "China are cele mai multe panouri solare din lume.")
    N.a(3, "3.2", "De ce exploatarea resurselor din Siberia e costisitoare?", "frigul extrem, solul înghețat și distanțele mari", ["pentru că e deșert cald", "pentru că e prea populată", "pentru că plouă tropical"], "Infrastructura e greu de construit.")
    N.a(2, "3.3", "Ce sunt OPEC?", "organizația țărilor exportatoare de petrol", ["o echipă de fotbal", "o organizație a fermierilor", "o bancă europeană"], "Multe țări din Golful Persic sunt membre.")
    N.a(2, "3.2", "Ce sol fertil se găsește în nordul Chinei, adus de vânt?", "loessul", ["nisipul de deșert", "solul de tundră", "argila vulcanică"], "Loessul dă culoarea galbenă fluviului Huang He.")
    N.a(2, "3.2", "Ce resursă oferă mările pentru Japonia?", "pește și fructe de mare", ["petrol din abundență", "cărbune", "aur"], "Japonia are o mare flotă de pescuit.")
    N.a(2, "4.4", "Ce pot face țările din Golf ca să fie pregătite pentru epuizarea petrolului?", "dezvoltă turismul, finanțele și energia solară", ["nimic", "consumă mai mult petrol", "închid porturile"], "Diversificarea economiei.")
    N.a(2, "3.3", "Ce resursă prețioasă se extrage în Siberia (Iakutia)?", "diamantele", ["cafeaua", "bananele", "orezul"], "Iakutia e una dintre cele mai mari zone de diamante.")
    N.a(3, "3.2", "De ce petrolul s-a format în jurul Golfului Persic?", "acolo, în trecut, au fost mări în care s-au depus resturi de viețuitoare, transformate în milioane de ani", ["pentru că e deșert acum", "pentru că a fost adus de oameni", "pentru că acolo plouă mult"], "Petrolul e un combustibil fosil.")
    N.a(2, "3.2", "Ce resursă pentru construcții dau pădurile de bambus?", "material ușor și rezistent pentru case și schele", ["petrol", "metal", "sticlă"], "Bambusul e folosit pe scară largă în Asia.")

    N.a(2, "3.2", "Ce țări asiatice au mari hidrocentrale?", "China și India", ["Arabia Saudită și Kuweit", "Qatar și Bahrain", "Maldive și Singapore"], "Au fluvii mari care coboară din munți.")

    # ================================================================ S11 Activitățile economice
    T = Lectie(7, "VII-S11-activitatile-economice-contraste-economice", "Asia – activități economice. Contraste regionale",
               "Cum se poate ca în aceeași Asie să existe și roboți de ultimă generație, și agricultură cu bivoli?",
               [("Agricultura", "Orezul e cultura principală în Asia musonică (China, India, Indonezia, Bangladesh, Vietnam, Thailanda). Se mai cultivă: grâu (China, India), ceai (China, India, Sri Lanka), bumbac, trestie de zahăr, cauciuc, palmier de ulei, condimente.\nÎn multe zone agricultura folosește încă munca manuală și animale de tracțiune."),
                ("Industria", "Japonia și Coreea de Sud au industrie de vârf: automobile, electronice, roboți, nave. China a devenit „fabrica lumii”: produce o mare parte din bunurile vândute pe Pământ. India e puternică în IT și industria farmaceutică.\nȚările din Golful Persic au industrie petrolieră și petrochimică."),
                ("Contraste", "Unele țări asiatice sunt foarte dezvoltate (Japonia, Coreea de Sud, Singapore, Emiratele Arabe Unite), altele sunt în dezvoltare rapidă (China, India, Vietnam), iar altele au încă venituri mici (Afganistan, Nepal, Myanmar).\nȘi în aceeași țară sunt diferențe mari între orașele de pe țărm și satele din interior.")],
               stiaica="Trenul japonez Shinkansen, numit și „trenul-glonț”, circulă din 1964 și a fost primul tren de mare viteză din lume.",
               ref=REF.format("Activitățile economice. Contraste economice regionale"))
    T.a(1, "3.3", "Care e principala cultură agricolă în Asia musonică?", "orezul", ["cartoful", "ovăzul", "secara"], "Orezul are nevoie de căldură și apă.")
    T.s(2, "3.3", "Asociază țara cu produsul agricol.", [("Sri Lanka", "ceai"), ("Indonezia", "ulei de palmier"), ("Thailanda", "orez"), ("India", "bumbac și condimente")], "Agricultura asiatică.")
    T.s(2, "3.3", "Asociază țara cu industria cunoscută.", [("Japonia", "automobile și roboți"), ("Coreea de Sud", "electronice și nave"), ("China", "„fabrica lumii”"), ("India", "IT și medicamente")], "Industria asiatică.")
    T.a(2, "3.3", "Ce țară e numită „fabrica lumii”?", "China", ["Nepal", "Mongolia", "Laos"], "China produce o mare parte din bunurile lumii.")
    T.a(2, "3.3", "Ce domeniu economic s-a dezvoltat foarte mult în India, la Bangalore?", "IT-ul (informatica)", ["mineritul cărbunelui", "creșterea renilor", "pescuitul de balene"], "Bangalore e numit „Silicon Valley-ul Indiei”.")
    T.a(2, "3.3", "Ce este Shinkansen?", "trenul japonez de mare viteză", ["un templu", "un munte", "un fluviu"], "Circulă din 1964.")
    T.p(2, "2.1", "Atinge pe hartă Coreea de Sud.", "lume", 36, 128, "Coreea de Sud", 300, "Coreea de Sud e în sudul Peninsulei Coreea.")
    T.p(3, "2.1", "Atinge pe hartă Vietnamul.", "lume", 16, 107, "Vietnam", 500, "Vietnamul e pe țărmul estic al Indochinei.")
    T.a(2, "3.3", "Ce țări asiatice sunt foarte dezvoltate economic?", "Japonia, Coreea de Sud, Singapore", ["Afganistan, Nepal", "Myanmar, Laos", "Yemen, Tadjikistan"], "Au venituri mari și industrie avansată.")
    T.a(2, "3.3", "Ce țări asiatice au încă venituri mici?", "Afganistan, Nepal", ["Japonia, Singapore", "Coreea de Sud", "Emiratele Arabe Unite"], "Contrastele economice din Asia sunt foarte mari.")
    T.a(2, "3.2", "De ce orezăriile sunt pe terase pe dealurile din Asia de Sud-Est?", "pentru că terasele păstrează apa și opresc eroziunea", ["pentru că e mai frumos", "pentru că orezul crește doar pe munte", "pentru că e interzis în câmpie"], "Terasele de orez sunt și patrimoniu cultural.")
    T.adev(2, "3.3", "În Asia există atât țări foarte bogate, cât și țări foarte sărace.", True, "Adevărat: contrastele economice sunt mari.")
    T.adev(2, "3.3", "Japonia produce în principal cărbune și petrol.", False, "Fals: Japonia are industrie de vârf, dar importă resursele.")
    T.l(2, "3.3", "Completează.", "Japonia e cunoscută pentru industria de [automobile] și roboți, iar China e numită „[fabrica] lumii”.", ["cafea", "grădina"], "Automobile, fabrica.")
    T.l(2, "3.3", "Completează.", "Principala cultură din Asia musonică este [orezul]; ceaiul se cultivă mult în [Sri Lanka].", ["porumbul", "Mongolia"], "Orez, Sri Lanka.")
    T.g(3, "2.3 4.1", "Graficul arată venitul mediu pe locuitor în trei țări asiatice imaginare. Ce observi?", grafic("bare", "Venit mediu pe locuitor (țări imaginare)", [("țara A", 45000), ("țara B", 12000), ("țara C", 1500)], "dolari/an"), "diferențe foarte mari între țări", ["toate au același venit", "țara C e cea mai bogată", "țara B e cea mai săracă"], "Țara A are de 30 de ori venitul țării C.")
    T.a(3, "4.3", "Compară agricultura din Japonia cu cea din Nepal.", "Japonia are agricultură mecanizată; în Nepal se lucrează mult manual, pe terase", ["Nepalul are mai multe tractoare", "sunt identice", "Japonia nu are agricultură"], "Nivelul de dezvoltare face diferența.")
    T.a(2, "3.3", "Ce oraș din Emiratele Arabe Unite are cea mai înaltă clădire din lume?", "Dubai (Burj Khalifa)", ["Riad", "Teheran", "Kabul"], "Burj Khalifa are 828 m.", surse=["Encyclopaedia Britannica – Burj Khalifa", "Council on Tall Buildings and Urban Habitat (CTBUH) – Burj Khalifa"])
    T.a(2, "3.3", "De ce Dubai a dezvoltat turismul și finanțele?", "ca să nu depindă doar de petrol", ["pentru că nu are deșert", "pentru că are multă ploaie", "pentru că e la pol"], "Diversificarea economiei.")
    T.d(2, "2.1", "Ce țară, cu industrie de automobile și electronice, e marcată pe hartă?", "lume", 36, 138, "Japonia", ["Coreea de Sud", "Taiwan", "Filipine"], "Japonia e un arhipelag.")
    T.a(2, "3.3", "Ce produse fabricate în Asia folosești probabil zilnic?", "telefonul, calculatorul, hainele", ["nimic", "doar mâncarea", "doar mobila românească"], "Multe produse electronice și textile sunt fabricate în Asia.")
    T.a(2, "3.3", "Ce animal de tracțiune se folosește în orezăriile din Asia de Sud-Est?", "bivolul de apă", ["renul", "cămila", "lama"], "Bivolul lucrează în apă și noroi.")
    T.a(2, "3.2", "Ce porturi asiatice sunt printre cele mai mari din lume?", "Shanghai și Singapore", ["Kabul și Ulan Bator", "Lhasa și Katmandu", "Astana și Tașkent"], "Prin ele trec cele mai multe containere.")
    T.a(3, "3.3", "De ce multe fabrici s-au mutat în Asia în ultimele decenii?", "pentru costuri mai mici de producție și multă forță de muncă", ["pentru că în Asia nu există oameni", "pentru că e mai frig", "pentru că nu există porturi"], "Globalizarea a schimbat harta industriei.")
    T.a(2, "3.4", "Ce terase de orez sunt în patrimoniul UNESCO?", "terasele de orez din Cordilierele Filipinelor", ["podgoriile din Franța", "câmpurile din Bărăgan", "pădurile din Siberia"], "Au peste 2 000 de ani.", surse=["UNESCO World Heritage Centre – Rice Terraces of the Philippine Cordilleras", "Encyclopaedia Britannica – Banaue rice terraces"])
    T.a(2, "3.3", "Ce țară e cel mai mare producător de ulei de palmier?", "Indonezia", ["Japonia", "Mongolia", "Kazahstan"], "Plantațiile au înlocuit păduri tropicale.")
    T.a(3, "4.4", "De ce uleiul de palmier e controversat?", "plantațiile au dus la tăierea pădurilor tropicale și la scăderea numărului de urangutani", ["e prea scump", "nu se folosește nicăieri", "crește doar în deșert"], "Se caută certificări pentru ulei produs fără defrișări.")
    T.a(2, "3.3", "Ce înseamnă că o țară e „în dezvoltare rapidă”?", "economia ei crește repede, dar mulți oameni au încă venituri mici", ["e cea mai bogată din lume", "nu are economie", "nu crește deloc"], "China, India, Vietnam sunt exemple.")
    T.a(2, "3.3", "Ce industrie e importantă în Coreea de Sud, la Ulsan?", "construcția de nave și automobile", ["creșterea oilor", "cultura cafelei", "mineritul diamantelor"], "Coreea de Sud e unul dintre cei mai mari constructori de nave.")

    T.a(2, "3.3", "Ce mărci de automobile sunt japoneze?", "Toyota, Honda, Nissan", ["Dacia, Renault", "BMW, Audi", "Fiat, Ferrari"], "Japonia e unul dintre cei mai mari producători de mașini.")

    # ================================================================ S12 Asia în lumea contemporană
    X = Lectie(7, "VII-S12-asia-lumea-contemporana", "Asia în lumea contemporană",
               "Ce rol joacă Asia în lumea de azi?",
               [("Puterea economică", "Asia are o pondere tot mai mare în economia lumii. China e a doua economie a lumii, după SUA. Japonia, India și Coreea de Sud sunt și ele printre cele mai mari economii.\nAsia produce o mare parte din electronice, mașini, haine și jucării și e un centru mondial al comerțului maritim."),
                ("Organizații și cooperare", "Țările asiatice colaborează în organizații regionale, precum ASEAN (Asociația Națiunilor din Asia de Sud-Est). Multe sunt membre ale ONU, ale G20 și ale altor organizații mondiale."),
                ("Provocări", "Asia se confruntă cu: poluarea aerului în orașele mari, lipsa apei în Orientul Mijlociu și Asia Centrală, conflicte în unele regiuni, inegalități mari între bogați și săraci, efectele schimbărilor climatice (creșterea nivelului mării în Bangladesh și Maldive, topirea ghețarilor din Himalaya).")],
               stiaica="Ghețarii din Himalaya alimentează fluvii de care depind sute de milioane de oameni; de aceea regiunea e numită uneori „al treilea pol” al Pământului.",
               ref=REF.format("Asia în lumea contemporană"))
    X.a(1, "3.3", "Ce economie asiatică e a doua din lume, după SUA?", "China", ["Mongolia", "Nepal", "Laos"], "China a crescut foarte repede după 1980.")
    X.a(2, "3.3", "Ce este ASEAN?", "o organizație a țărilor din Asia de Sud-Est", ["o bancă europeană", "un munte", "o echipă de fotbal"], "ASEAN promovează cooperarea economică.")
    X.a(2, "4.4", "Ce țară asiatică e amenințată de creșterea nivelului mării, fiind foarte joasă?", "Maldive (și Bangladesh)", ["Mongolia", "Nepal", "Afganistan"], "Insulele Maldive sunt la doar câțiva metri deasupra mării.")
    X.a(2, "4.4", "De ce sunt importanți ghețarii din Himalaya?", "alimentează fluvii de care depind sute de milioane de oameni", ["produc petrol", "opresc cutremurele", "nu au importanță"], "Gange, Indus, Brahmaputra, Yangtze pornesc din această regiune.")
    X.a(2, "1.1", "De ce Himalaya e numită „al treilea pol”?", "pentru că are cea mai mare cantitate de gheață după Antarctica și Arctica", ["pentru că e la Polul Nord", "pentru că e cea mai rece", "pentru că are pinguini"], "Rezerva de gheață e uriașă.")
    X.s(2, "3.3", "Asociază provocarea cu regiunea.", [("lipsa apei", "Orientul Mijlociu"), ("creșterea nivelului mării", "Bangladesh și Maldive"), ("poluarea aerului", "marile orașe din China și India"), ("topirea ghețarilor", "Himalaya")], "Provocările Asiei.")
    X.a(2, "3.3", "Ce produse exportă Asia în toată lumea?", "electronice, mașini, haine, jucării", ["doar petrol", "doar cafea", "doar lemn"], "Asia e un mare exportator.")
    X.p(2, "2.1", "Atinge pe hartă Maldive.", "lume", 3.2, 73.2, "Maldive", 500, "Maldivele sunt în Oceanul Indian, la sud-vest de India.")
    X.p(3, "2.1", "Atinge pe hartă Bangladesh.", "lume", 23.7, 90.4, "Bangladesh", 400, "Bangladesh e în delta Gangelui.")
    X.adev(2, "3.3", "Asia are un rol tot mai mic în economia lumii.", False, "Fals: rolul Asiei crește.")
    X.adev(2, "4.4", "Schimbările climatice afectează și Asia, prin topirea ghețarilor și creșterea nivelului mării.", True, "Adevărat.")
    X.l(2, "3.3", "Completează.", "Organizația țărilor din Asia de Sud-Est se numește [ASEAN]; a doua economie a lumii este [China].", ["UE", "Japonia"], "ASEAN, China.")
    X.l(2, "4.4", "Completează.", "Insulele [Maldive] și delta din [Bangladesh] sunt amenințate de creșterea nivelului mării.", ["Japonia", "Mongolia"], "Maldive, Bangladesh.")
    X.g(3, "2.3 4.1", "Graficul arată (schematic) ponderea a trei regiuni în producția industrială a lumii, în două momente imaginare. Ce s-a schimbat?", grafic("bare", "Ponderea în producția industrială (exemplu imaginar, %)", [("Asia – atunci", 25), ("Asia – acum", 50), ("Europa – atunci", 35), ("Europa – acum", 20)], "%"), "ponderea Asiei a crescut, iar a Europei a scăzut", ["Europa a crescut", "nu s-a schimbat nimic", "Asia a scăzut"], "Industria s-a mutat spre Asia.")
    X.a(3, "4.3", "De ce Asia are un rol mare în comerțul mondial?", "are populație uriașă, multe fabrici și porturi mari", ["pentru că e mică", "pentru că nu are porturi", "pentru că nu produce nimic"], "Rutele maritime spre Asia sunt cele mai circulate.")
    X.a(2, "3.3", "Ce strâmtoare asiatică e una dintre cele mai circulate rute maritime?", "Strâmtoarea Malacca", ["Strâmtoarea Bering", "Bosforul", "Strâmtoarea Gibraltar"], "Leagă Oceanul Indian de Pacific.")
    X.a(2, "3.3", "Ce înseamnă „Noul Drum al Mătăsii”?", "un proiect al Chinei de drumuri, căi ferate și porturi care leagă Asia de Europa și Africa", ["un drum medieval de mătase", "un râu", "un munte"], "Drumul Mătăsii era o rută comercială veche.")
    X.a(2, "3.4", "Ce era Drumul Mătăsii în Evul Mediu?", "o rută comercială pe uscat între China și Europa", ["un canal", "o cale ferată", "o rută aeriană"], "Pe el circulau mătase, condimente, idei.")
    X.d(2, "2.1", "Ce strâmtoare, foarte circulată, e marcată pe hartă?", "lume", 2.5, 101.5, "Strâmtoarea Malacca", ["Strâmtoarea Bering", "Strâmtoarea Hormuz", "Bosforul"], "Malacca e între Sumatra și Peninsula Malacca.")
    X.a(2, "4.4", "Ce soluții adoptă orașele chineze contra poluării?", "autobuze electrice, energie solară, închiderea centralelor vechi pe cărbune", ["mai multe centrale pe cărbune", "tăierea parcurilor", "interzicerea transportului public"], "Unele orașe au cele mai multe autobuze electrice din lume.")
    X.a(3, "4.3", "De ce în Orientul Mijlociu apa poate produce tensiuni între state?", "pentru că râurile mari (Tigru, Eufrat, Iordan) trec prin mai multe țări, iar apa e puțină", ["pentru că e prea multă apă", "pentru că plouă tropical", "pentru că sunt ghețari"], "Împărțirea apei e o problemă politică.")
    X.a(2, "3.3", "Ce țări asiatice fac parte din G20 (cele mai mari economii)?", "China, Japonia, India, Coreea de Sud, Indonezia, Arabia Saudită, Turcia", ["Nepal și Laos", "Bhutan și Maldive", "Mongolia și Brunei"], "Asia are multe economii mari.")
    X.a(2, "4.4", "Ce poți face tu pentru ca produsele cumpărate să fie mai prietenoase cu mediul?", "folosești lucrurile mai mult timp, le repari și reciclezi electronicele vechi", ["arunci telefonul la gunoi menajer", "cumperi un telefon nou în fiecare lună", "arzi deșeurile electronice"], "Electronicele conțin metale valoroase.")
    X.a(2, "3.3", "Ce țară asiatică e cunoscută pentru filme și muzică ce au devenit populare în toată lumea (K-pop)?", "Coreea de Sud", ["Mongolia", "Kazahstan", "Yemen"], "Cultura e și ea o forță economică.")
    X.a(3, "3.3", "De ce India e considerată o putere în creștere?", "are populație foarte numeroasă și tânără, IT dezvoltat și economie în creștere rapidă", ["are cea mai mică populație", "nu are industrie", "are climă polară"], "India e una dintre cele mai mari economii.")
    X.a(2, "3.3", "Ce mare eveniment sportiv au organizat Beijingul și Tokyo?", "Jocurile Olimpice", ["Turul Franței", "Wimbledon", "Cupa Davis"], "Tokyo (1964, 2021), Beijing (2008, 2022 iarnă).")
    X.a(2, "4.4", "Ce problemă de sănătate apare în orașele foarte poluate?", "boli respiratorii", ["oameni mai sănătoși", "mai puține boli", "nicio problemă"], "Aerul poluat afectează plămânii.")
    X.a(2, "3.3", "De ce multe companii europene au fabrici în Asia?", "pentru costuri mai mici și pentru a fi aproape de piețele mari asiatice", ["pentru că în Europa nu există fabrici", "pentru că Asia e mai mică", "fără motiv"], "Globalizarea leagă economiile.")
    X.a(3, "4.4", "Ce înseamnă „dezvoltare durabilă” pentru Asia?", "creștere economică fără să distrugă mediul și fără să lase oameni în urmă", ["creștere cu orice preț", "oprirea oricărei dezvoltări", "doar exploatarea petrolului"], "Echilibrul economie–mediu–oameni.")

    X.a(2, "3.3", "Ce înseamnă globalizare?", "legăturile tot mai strânse dintre economiile, culturile și oamenii din toată lumea", ["izolarea țărilor", "oprirea comerțului", "un tip de climă"], "Produsele, banii și informațiile circulă repede între continente.")

    return Unitate(7, "u1-asia.json", "Asia").add(P, R, H, C, B, E, D, A, N, T, X)
