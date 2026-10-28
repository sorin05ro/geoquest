from autor import Lectie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_SUPR = ["Institutul Național de Statistică (INS) – Anuarul Statistic al României, cap. „Geografie”", "Encyclopaedia Britannica – Romania"]
S_EXTR = ["INS – Anuarul Statistic al României: coordonatele punctelor extreme", "Wikipedia (ro) – Puncte extreme ale României"]
S_UE = ["Uniunea Europeană – Țările UE: România (european-union.europa.eu)", "Ministerul Afacerilor Externe – România în UE"]
S_DUN = ["ICPDR – Danube Basin facts", "Administrația Fluvială a Dunării de Jos – Dunărea pe teritoriul României"]
RS = (45.38, 27.05)


def unitate():
    # ================================================================ S1 Poziția geografică
    P = Lectie(8, "VIII-S01-pozitia-geografica-elemente-definitorii", "România – poziția geografică. Statele vecine",
               "Dacă ai explica unui elev din Japonia unde e România, ce ai spune?",
               [("Poziția pe glob și în Europa", "România se află în emisfera nordică și în emisfera estică, la jumătatea distanței dintre Ecuator și Polul Nord: paralela de 45° N trece prin țara noastră. Meridianul de 25° E o străbate și el.\nÎn Europa, România e în partea central-sud-estică, la nord de Peninsula Balcanică, pe cursul inferior al Dunării și la Marea Neagră."),
                ("Suprafață și puncte extreme", "România are 238 397 km², după INS, fiind una dintre țările mijlocii ale Europei.\nPuncte extreme: nord – Horodiștea (județul Botoșani); sud – Zimnicea (județul Teleorman); vest – Beba Veche (județul Timiș); est – Sulina (județul Tulcea)."),
                ("Vecinii", "România se învecinează cu: Ucraina (la nord și la est), Republica Moldova (la est, pe Prut), Bulgaria (la sud, în mare parte pe Dunăre), Serbia (la sud-vest, pe Dunăre) și Ungaria (la vest). La sud-est are ieșire la Marea Neagră.\nGranițele urmează în multe locuri râuri: Prutul, Dunărea, Tisa.")],
               stiaica="Paralela de 45° N trece prin România, chiar prin sudul județului Buzău: suntem la jumătatea drumului dintre Ecuator și Polul Nord.",
               ref=REF.format("Poziția geografică. Elemente definitorii și consecințe. Statele vecine"))
    P.a(1, "1.1", "În ce emisfere se află România?", "nordică și estică", ["sudică și vestică", "nordică și vestică", "sudică și estică"], "La nord de Ecuator, la est de Greenwich.")
    P.a(1, "2.1", "Ce paralelă importantă trece prin România?", "paralela de 45° N", ["Ecuatorul", "Tropicul Racului", "Cercul Polar de Nord"], "Suntem la jumătatea distanței Ecuator–Pol.")
    P.a(2, "1.1", "Ce suprafață are România?", "238 397 km²", ["23 839 km²", "2 383 970 km²", "100 000 km²"], "După INS.", surse=S_SUPR)
    P.s(2, "2.1", "Asociază punctul extrem cu localitatea.", [("nord", "Horodiștea"), ("sud", "Zimnicea"), ("vest", "Beba Veche"), ("est", "Sulina")], "Punctele extreme ale României.", surse=S_EXTR)
    P.s(2, "2.1", "Asociază punctul extrem cu județul.", [("Horodiștea", "Botoșani"), ("Zimnicea", "Teleorman"), ("Beba Veche", "Timiș"), ("Sulina", "Tulcea")], "Județele punctelor extreme.", surse=S_EXTR)
    P.e(2, "2.1", "Pune pe hartă punctele extreme ale României.", [("n", "Horodiștea (N)", 48.27, 26.6), ("s", "Zimnicea (S)", 43.65, 25.37), ("v", "Beba Veche (V)", 46.13, 20.32), ("e", "Sulina (E)", 45.16, 29.66)], "Nord în Botoșani, sud în Teleorman, vest în Timiș, est în Tulcea.", harta="romania", surse=S_EXTR)
    P.a(1, "2.1", "Câți vecini are România?", "cinci", ["trei", "șapte", "doi"], "Ucraina, Republica Moldova, Bulgaria, Serbia, Ungaria.")
    P.s(2, "2.1", "Asociază vecinul cu poziția lui față de România.", [("Ucraina", "nord și est"), ("Republica Moldova", "est"), ("Bulgaria", "sud"), ("Ungaria", "vest")], "Vecinii României.")
    P.a(2, "2.1", "Ce râu formează granița cu Republica Moldova?", "Prutul", ["Siretul", "Mureșul", "Oltul"], "Prutul e graniță pe toată lungimea dintre cele două state.")
    P.a(2, "2.1", "Ce fluviu formează cea mai mare parte a graniței cu Bulgaria?", "Dunărea", ["Prutul", "Tisa", "Nistrul"], "Dunărea desparte Câmpia Română de Podișul Prebalcanic.")
    P.a(2, "2.1", "Ce vecin are România la sud-vest, peste Dunăre?", "Serbia", ["Ungaria", "Bulgaria", "Ucraina"], "La Porțile de Fier, Dunărea e graniță cu Serbia.")
    P.a(2, "2.1", "Ce râu formează o mică porțiune din granița cu Ucraina, în nord?", "Tisa", ["Oltul", "Jiul", "Argeșul"], "Tisa curge prin Maramureș, la graniță.")
    P.a(2, "2.1", "Cu ce vecin are România granița doar pe uscat, fără râu mare?", "Ungaria", ["Republica Moldova", "Bulgaria", "Serbia"], "Granița de vest traversează Câmpia de Vest.")
    P.p(2, "2.1", "Atinge pe harta României Horodiștea, punctul extrem nordic.", "romania", 48.27, 26.6, "Horodiștea", 50, "Horodiștea e în nordul județului Botoșani.", surse=S_EXTR)
    P.p(2, "2.1", "Atinge pe harta României Sulina, punctul extrem estic.", "romania", 45.16, 29.66, "Sulina", 40, "Sulina e la vărsarea brațului Sulina în mare.", surse=S_EXTR)
    P.p(3, "2.1", "Atinge pe harta României Beba Veche, punctul extrem vestic.", "romania", 46.13, 20.32, "Beba Veche", 40, "Beba Veche e în vestul județului Timiș, lângă Ungaria și Serbia.", surse=S_EXTR)
    P.p(3, "2.1", "Atinge pe harta României Zimnicea, punctul extrem sudic.", "romania", 43.65, 25.37, "Zimnicea", 40, "Zimnicea e pe Dunăre, în județul Teleorman.", surse=S_EXTR)
    P.p(2, "2.1", "Atinge pe harta României orașul nostru, Râmnicu Sărat, aproape de paralela de 45° N.", "romania", RS[0], RS[1], "Râmnicu Sărat", 35, "Râmnicu Sărat e în nord-estul județului Buzău.")
    P.adev(2, "1.2", "România are ieșire la Oceanul Atlantic.", False, "Fals: are ieșire la Marea Neagră, o mare aproape închisă.")
    P.adev(2, "1.2", "România se află la jumătatea distanței dintre Ecuator și Polul Nord.", True, "Adevărat: paralela de 45° N o traversează.")
    P.l(2, "2.1", "Completează.", "Punctul extrem nordic e [Horodiștea], iar cel estic e [Sulina].", ["Zimnicea", "Beba Veche"], "Nord și est.", surse=S_EXTR)
    P.l(2, "2.1", "Completează.", "Granița cu Republica Moldova urmează râul [Prut], iar granița cu Bulgaria urmează în mare parte [Dunărea].", ["Siret", "Tisa"], "Prut și Dunăre.")
    P.a(2, "3.3", "Ce consecință are poziția la paralela de 45° pentru climă?", "climă temperată, cu patru anotimpuri", ["climă ecuatorială", "climă polară", "climă deșertică"], "Poziția mijlocie între Ecuator și pol.")
    P.a(2, "3.3", "Ce consecință are poziția României față de Oceanul Atlantic?", "influențele oceanice scad de la vest spre est, iar cele continentale cresc", ["oceanul încălzește doar Dobrogea", "nu are nicio consecință", "toată țara are climă oceanică"], "Vestul e mai umed, estul mai uscat.")
    P.g(3, "2.2", "Graficul compară suprafața unor țări europene (mii km², valori rotunjite). Unde se situează România?", grafic("bare", "Suprafața (mii km², valori rotunjite)", [("Franța", 552), ("Polonia", 313), ("România", 238), ("Ungaria", 93), ("Bulgaria", 111)], "mii km²", "Eurostat / INS"), "e o țară de mărime mijlocie: mai mică decât Franța și Polonia, mai mare decât Ungaria și Bulgaria", ["e cea mai mare", "e cea mai mică", "e egală cu Franța"], "România are 238 de mii km².", surse=S_SUPR)
    P.o(3, "2.1", "Ordonează vecinii României în sensul acelor de ceasornic, pornind de la nord.", ["Ucraina (nord)", "Republica Moldova (est)", "Bulgaria (sud)", "Serbia (sud-vest)", "Ungaria (vest)"], "În sensul acelor de ceasornic", "Ocolim granița pornind de la nord.")
    P.d(2, "2.1", "Ce stat vecin e marcat pe hartă, la est de Prut?", "lume", 47, 28.5, "Republica Moldova", ["Ucraina", "Bulgaria", "Ungaria"], "Republica Moldova e între România și Ucraina.")
    P.a(3, "4.3", "Compară poziția României cu cea a Ungariei.", "România are ieșire la mare și e străbătută de Carpați; Ungaria nu are ieșire la mare și e mai ales câmpie", ["Ungaria are ieșire la Marea Neagră", "sunt identice", "România nu are munți"], "Poziția influențează economia și clima.")
    P.a(2, "1.1", "Ce meridian important trece prin România?", "meridianul de 25° E", ["meridianul de 0°", "meridianul de 180°", "meridianul de 90° V"], "Trece prin centrul țării, prin Țara Făgărașului.")
    P.a(2, "4.4", "Ce avantaj aduce ieșirea la Marea Neagră?", "comerț maritim prin portul Constanța, turism, pescuit, resurse din platformă", ["nu aduce niciun avantaj", "aduce doar inundații", "oprește comerțul"], "Constanța e cel mai mare port de la Marea Neagră.")

    # ================================================================ S2 Țară carpatică, dunăreană, pontică, central-europeană
    T = Lectie(8, "VIII-S02-romania-tara-carpatica-dunareana", "România – țară carpatică, dunăreană, pontică și central-europeană",
               "Ce trei elemente naturale definesc România?",
               [("Țară carpatică", "Carpații formează „coloana vertebrală” a României: un arc care ocupă aproximativ o treime din suprafață și în jurul căruia se dispun, în trepte, dealurile, podișurile și câmpiile. Peste jumătate din lanțul Carpaților se află pe teritoriul României."),
                ("Țară dunăreană și pontică", "Dunărea curge aproximativ 1 075 km pe teritoriul sau la granița României, cea mai lungă porțiune dintre toate țările străbătute; aici își are și delta. Aproape toate râurile țării ajung în Dunăre.\nPontică înseamnă „de la Marea Neagră” (Pontus Euxinus, la romani). România are un litoral de aproximativ 245 km."),
                ("Țară central-europeană", "Prin poziție, istorie și cultură, România e legată de Europa Centrală; e și la răscruce cu Europa de Est și Europa de Sud-Est (Balcani). E membră a Uniunii Europene din 2007 și a NATO din 2004.")],
               stiaica="Numele antic al Mării Negre era Pontus Euxinus, adică „marea ospitalieră”. De aici vine cuvântul „pontic”.",
               ref=REF.format("România – țară carpatică, dunăreană, pontică și central-europeană"))
    T.a(1, "1.1", "De ce România e numită „țară carpatică”?", "pentru că Carpații o străbat ca un arc, în centrul țării", ["pentru că are cei mai înalți munți din Europa", "pentru că nu are munți", "pentru că e la mare"], "Carpații sunt „coloana vertebrală” a țării.")
    T.a(1, "1.1", "Ce înseamnă „țară pontică”?", "țară cu ieșire la Marea Neagră", ["țară cu poduri", "țară cu munți", "țară fără apă"], "Pontus Euxinus = Marea Neagră.")
    T.a(2, "1.1", "De ce România e numită „țară dunăreană”?", "Dunărea are cea mai lungă porțiune pe teritoriul sau la granița României și aici își are delta", ["Dunărea izvorăște din România", "Dunărea trece doar prin București", "Dunărea se varsă în Oceanul Atlantic"], "Aproximativ 1 075 km.", surse=S_DUN)
    T.a(2, "3.3", "Ce parte din lanțul Carpaților se află în România?", "peste jumătate", ["o zecime", "tot lanțul", "nimic"], "Restul e în Slovacia, Polonia, Ucraina, Cehia, Ungaria, Austria, Serbia.")
    T.a(2, "3.3", "Ce lungime are litoralul românesc, aproximativ?", "245 km", ["24 km", "2 450 km", "1 075 km"], "De la Sulina la Vama Veche.")
    T.a(2, "4.2", "Unde se termină litoralul românesc la sud?", "la Vama Veche, la granița cu Bulgaria", ["la Constanța", "la Sulina", "la Mangalia, fără graniță"], "La nord, litoralul pornește de la brațul Chilia.")
    T.s(2, "1.2", "Asociază denumirea cu explicația.", [("carpatică", "străbătută de arcul Carpaților"), ("dunăreană", "străbătută de Dunăre, cu delta ei"), ("pontică", "cu ieșire la Marea Neagră"), ("central-europeană", "legată de Europa Centrală prin poziție și istorie")], "Elementele care definesc România.")
    T.a(2, "3.3", "De ce aproape toate râurile României ajung în Dunăre?", "pentru că Dunărea e colectorul principal, în sudul și estul țării, unde relieful e cel mai jos", ["pentru că așa au fost săpate de oameni", "pentru că Dunărea e la nord", "nu ajung"], "Rețeaua hidrografică e radiară și converge spre Dunăre.")
    T.a(2, "4.3", "Ce dispunere are relieful României în jurul Carpaților?", "în trepte concentrice: munți, apoi dealuri și podișuri, apoi câmpii", ["fără nicio ordine", "toți munții la mare", "câmpiile în centru"], "Relieful e dispus în amfiteatru.")
    T.a(2, "1.2", "Din ce an e România membră a NATO?", "2004", ["1990", "2007", "2020"], "Iar din UE din 2007.")
    T.a(2, "1.2", "Din ce an e România membră a Uniunii Europene?", "2007", ["2004", "1918", "2012"], "1 ianuarie 2007.", surse=S_UE)
    T.p(2, "2.1", "Atinge pe harta României Delta Dunării.", "romania", 45.1, 29.3, "Delta Dunării", 50, "Delta e în nord-estul Dobrogei.")
    T.p(2, "2.1", "Atinge pe harta României Vama Veche, la capătul sudic al litoralului.", "romania", 43.75, 28.58, "Vama Veche", 40, "La granița cu Bulgaria.")
    T.p(3, "2.1", "Atinge pe harta României Porțile de Fier, unde Dunărea intră în țară.", "romania", 44.67, 22.53, "Porțile de Fier", 50, "Defileul Dunării, la granița cu Serbia.")
    T.adev(2, "1.2", "Dunărea izvorăște din Munții Carpați.", False, "Fals: izvorăște din Pădurea Neagră, în Germania.")
    T.adev(2, "3.3", "Carpații ocupă aproximativ o treime din suprafața României.", True, "Adevărat.")
    T.l(2, "1.1", "Completează.", "România e țară [carpatică], dunăreană și [pontică].", ["alpină", "atlantică"], "Trei elemente naturale.")
    T.l(2, "4.2", "Completează.", "Litoralul românesc are aproximativ [245] km, de la Sulina până la [Vama Veche].", ["1 075", "Constanța"], "Litoralul.")
    T.g(3, "2.2", "Graficul arată lungimea Dunării în câteva țări (km, valori aproximative, inclusiv granițele). Unde are cea mai lungă porțiune?", grafic("bare", "Lungimea Dunării pe teritoriu sau la graniță (aproximativ)", [("România", 1075), ("Serbia", 588), ("Ungaria", 417), ("Germania", 687), ("Austria", 350)], "km", "ICPDR"), "în România", ["în Germania", "în Ungaria", "în Austria"], "România are cea mai lungă porțiune.", surse=S_DUN)
    T.a(3, "4.3", "Ce înseamnă că România e la „răscruce” între Europa Centrală, de Est și de Sud-Est?", "e la întâlnirea acestor regiuni, cu influențe din toate", ["e izolată", "e în Europa de Vest", "e în Asia"], "Poziție de legătură.")
    T.d(2, "2.1", "Ce munți, „coloana vertebrală” a României, sunt marcați pe hartă?", "romania", 45.6, 24.7, "Carpații Meridionali", ["Munții Apuseni", "Munții Măcinului", "Carpații Orientali"], "Punctul e în Munții Făgăraș.")
    T.a(2, "3.3", "Ce rol au avut Carpații în istoria României?", "au oferit adăpost, păduri, pășuni și au fost un spațiu de legătură între provinciile românești", ["au despărțit complet românii", "nu au avut niciun rol", "au fost deșertul țării"], "Păstoritul și transhumanța i-au legat pe români.")
    T.a(2, "1.2", "Ce canal leagă Dunărea de portul Constanța?", "Canalul Dunăre–Marea Neagră", ["Canalul Suez", "Canalul Bega", "Canalul Panama"], "Scurtează drumul spre mare.")
    T.a(2, "3.3", "Ce înseamnă „Pontus Euxinus”?", "numele antic al Mării Negre", ["un munte", "un râu din Banat", "un oraș dacic"], "Grecii și romanii îl foloseau.")
    T.a(2, "4.2", "Ce orașe-port românești sunt la Marea Neagră?", "Constanța, Mangalia, Midia", ["Galați, Brăila", "Iași, Suceava", "Cluj, Oradea"], "Galați și Brăila sunt porturi dunărene.")
    T.a(2, "4.2", "Ce orașe-port românești mari sunt pe Dunăre?", "Galați, Brăila, Tulcea", ["Constanța, Mangalia", "Brașov, Sibiu", "Iași, Botoșani"], "Pe Dunărea maritimă pot urca nave maritime.")
    T.a(3, "4.4", "De ce Dunărea e importantă pentru economia României?", "transport, energie (Porțile de Fier), apă pentru irigații, pescuit, turism", ["nu are importanță", "doar pentru înot", "doar pentru inundații"], "Dunărea e o axă economică.")
    T.a(2, "4.1", "Ce stat european are cea mai mare parte a Carpaților, după suprafață?", "România", ["Polonia", "Slovacia", "Ucraina"], "Arcul carpatic românesc e cel mai întins.")
    T.a(2, "1.2", "Ce înseamnă că relieful României e dispus „în amfiteatru”?", "treptele de relief coboară de la munți spre câmpii, ca băncile unui amfiteatru", ["că e plat", "că are forma unui cerc perfect", "că e sub mare"], "Munți – dealuri și podișuri – câmpii.")
    T.a(2, "4.2", "Ce județ al României are ieșire și la Dunăre, și la Marea Neagră?", "Constanța (și Tulcea)", ["Buzău", "Cluj", "Bihor"], "Dobrogea e între Dunăre și mare.")

    return Unitate(8, "u1-pozitie.json", "Poziția geografică").add(P, T)
