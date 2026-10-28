from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_FOND = ["INS – Anuarul Statistic al României: fondul funciar după modul de folosință", "Ministerul Agriculturii și Dezvoltării Rurale – fond funciar"]
S_EURO = ["Eurostat – Crop production in EU standard humidity (apro_cpsh1)", "Ministerul Agriculturii și Dezvoltării Rurale – producții vegetale"]
S_CNE = ["Nuclearelectrica – CNE Cernavodă (nuclearelectrica.ro)", "World Nuclear Association – Nuclear Power in Romania"]
S_PDF = ["Hidroelectrica – Porțile de Fier I (hidroelectrica.ro)", "Encyclopaedia Britannica – Iron Gate"]
S_DACIA = ["Automobile Dacia – istoric (dacia.ro)", "Encyclopaedia Britannica – Dacia (automobile)"]
S_PORT = ["Compania Națională Administrația Porturilor Maritime Constanța (portofconstantza.com)", "Encyclopaedia Britannica – Constanța"]
S_UNESCO = ["UNESCO World Heritage Centre – Romania: properties inscribed", "Ministerul Culturii – Monumente UNESCO din România"]
S_COM = ["INS – Comerțul internațional cu bunuri (comunicate lunare)", "Eurostat – International trade in goods by partner"]
RS = (45.38, 27.05)


def unitate():
    # ================================================================ S28a Fondul funciar agricol
    F = Lectie(8, "VIII-S28-agricultura-fondul-funciar-agricol", "Agricultura – fondul funciar agricol",
               "Cât din suprafața României e teren agricol?",
               [("Fondul funciar", "Fondul funciar este totalitatea terenurilor unei țări, după modul de folosință: terenuri agricole, păduri, ape, construcții, drumuri.\nÎn România, aproximativ 61 % din suprafață e teren agricol, iar aproximativ 28 % e acoperit de păduri, după INS."),
                ("Terenul agricol", "Terenul agricol cuprinde: teren arabil (cel mai întins, în câmpii și podișuri), pășuni și fânețe (la deal și munte), vii și livezi (pe dealuri și în Subcarpați).\nCele mai fertile soluri sunt cernoziomurile din Câmpia Română, Câmpia de Vest, Dobrogea și Câmpia Moldovei."),
                ("Probleme și soluții", "Probleme: eroziunea solului pe pante, alunecările, secetele, salinizarea, fărâmițarea terenurilor în multe parcele mici.\nSoluții: irigații, perdele forestiere, terasarea pantelor, comasarea terenurilor, agricultura ecologică.")],
               stiaica="România are una dintre cele mai mari suprafețe de teren arabil din Uniunea Europeană.",
               ref=REF.format("Agricultura – Fondul funciar agricol – potențial și valorificare"), prefix="VIII28a")
    F.a(1, "1.1", "Ce este fondul funciar?", "totalitatea terenurilor unei țări, după modul de folosință", ["banii pentru agricultură", "o fabrică", "un tip de sol"], "Agricol, forestier, ape, construcții.")
    F.a(2, "3.1", "Ce parte din suprafața României e teren agricol?", "aproximativ 61 %", ["aproximativ 6 %", "aproximativ 90 %", "aproximativ 25 %"], "După INS.", surse=S_FOND)
    F.a(2, "3.1", "Ce parte din suprafața României e acoperită de păduri?", "aproximativ 28 %", ["aproximativ 2 %", "aproximativ 70 %", "aproximativ 50 %"], "După INS.", surse=S_FOND)
    F.s(2, "1.2", "Asociază categoria de teren agricol cu relieful în care predomină.", [("arabil", "câmpii și podișuri"), ("pășuni și fânețe", "dealuri înalte și munți"), ("vii", "dealuri însorite, Subcarpați"), ("livezi", "dealuri și depresiuni subcarpatice")], "Categoriile de folosință.")
    F.a(2, "1.2", "Ce categorie de teren agricol e cea mai întinsă?", "terenul arabil", ["viile", "livezile", "pășunile alpine"], "În câmpii și podișuri.")
    F.a(2, "2.1", "Unde sunt cele mai fertile soluri ale României?", "în Câmpia Română, Câmpia de Vest, Dobrogea, Câmpia Moldovei (cernoziomuri)", ["pe vârfurile munților", "în Delta Dunării", "în Munții Apuseni"], "Cernoziomul e foarte bogat în humus.")
    F.a(2, "4.1", "Ce problemă afectează solurile de pe pante?", "eroziunea și alunecările de teren", ["prea mult humus", "înghețul permanent", "vulcanii"], "Pantele trebuie protejate.")
    F.a(2, "4.1", "Ce înseamnă comasarea terenurilor?", "unirea parcelelor mici în suprafețe mai mari, ușor de lucrat cu mașini", ["împărțirea terenului în bucăți mici", "abandonarea terenului", "betonarea"], "Fărâmițarea e o problemă a agriculturii românești.")
    F.a(2, "4.1", "La ce folosesc perdelele forestiere?", "protejează câmpurile de vânt, reduc eroziunea și păstrează umezeala", ["umbresc doar drumurile", "produc petrol", "nu au rol"], "Mai ales în Bărăgan și Dobrogea.")
    F.a(2, "2.2", "De ce în Bărăgan și Dobrogea sunt necesare irigațiile?", "plouă puțin și verile sunt secetoase", ["plouă prea mult", "sunt munți", "solul e înghețat"], "Seceta reduce recoltele.")
    F.p(2, "2.1", "Atinge pe harta României Bărăganul, mare zonă agricolă.", "romania", 44.6, 27.3, "Bărăgan", 60, "În estul Câmpiei Române.")
    F.p(3, "2.1", "Atinge pe harta României Câmpia de Vest.", "romania", 46.2, 21.3, "Câmpia de Vest", 70, "La granița cu Ungaria.")
    F.adev(2, "1.2", "Pădurile ocupă cea mai mare parte din fondul funciar al României.", False, "Fals: terenul agricol ocupă cea mai mare parte.", surse=S_FOND)
    F.adev(2, "4.1", "Terasele pe pante reduc eroziunea solului.", True, "Adevărat.")
    F.l(2, "1.1", "Completează.", "Aproximativ 61 % din suprafața țării e teren [agricol]; cel mai întins e terenul [arabil].", ["forestier", "viticol"], "Fond funciar.", surse=S_FOND)
    F.l(2, "4.1", "Completează.", "Unirea parcelelor mici se numește [comasare]; protecția câmpurilor de vânt se face cu perdele [forestiere].", ["fărâmițare", "de ceață"], "Soluții.")
    F.g(3, "2.3", "Graficul arată fondul funciar al României (aproximativ, după INS). Ce categorie e a doua ca mărime?", grafic("structura", "Fondul funciar (aproximativ)", [("agricol", 61), ("păduri", 28), ("ape", 4), ("construcții și drumuri", 5), ("altele", 2)], "%", "INS – Anuarul Statistic"), "pădurile", ["apele", "construcțiile", "terenul agricol"], "Agricol ~61 %, păduri ~28 %.", surse=S_FOND)
    F.g(3, "2.3", "Din același grafic: de câte ori e mai mare terenul agricol decât cel acoperit de păduri?", grafic("structura", "Fondul funciar (aproximativ)", [("agricol", 61), ("păduri", 28), ("ape", 4), ("construcții și drumuri", 5), ("altele", 2)], "%", "INS – Anuarul Statistic"), "de aproximativ 2 ori", ["de 10 ori", "la fel", "de 2 ori mai mic"], "61 : 28 ≈ 2.", surse=S_FOND)
    F.a(3, "4.1", "Compară folosința terenurilor la câmpie cu cea la munte.", "la câmpie predomină terenul arabil; la munte, pădurile și pășunile", ["la munte predomină arabilul", "sunt identice", "la câmpie predomină pădurile"], "Relieful decide folosința.")
    F.d(2, "2.1", "Ce regiune agricolă cu soluri fertile, între Dunăre și mare, e marcată pe hartă?", "romania", 44.3, 28.2, "Dobrogea", ["Banatul", "Oltenia", "Maramureșul"], "Dobrogea are cernoziomuri.")
    F.a(2, "4.1", "Ce înseamnă salinizarea solului?", "acumularea sărurilor în sol, care îl face nefertil", ["îmbogățirea cu humus", "înghețarea solului", "spălarea solului de ploi"], "Apare în zone cu irigații greșite sau lacuri sărate.")
    F.a(2, "3.3", "Ce înseamnă agricultura ecologică?", "agricultura fără pesticide și îngrășăminte chimice de sinteză", ["agricultura doar cu mașini", "agricultura în seră", "agricultura fără apă"], "Produsele au un logo special UE.")
    F.a(2, "1.2", "Ce sunt fânețele?", "terenuri cu iarbă cosită pentru fân", ["terenuri cu vii", "lacuri", "păduri de conifere"], "Fânul hrănește animalele iarna.")
    F.a(2, "2.2", "De ce la munte terenul arabil e puțin?", "pantele sunt mari, solurile subțiri și clima rece", ["e prea cald", "e prea plat", "e prea mult soare"], "Se cresc animale.")
    F.a(3, "4.1", "Cum ajută satelitul agricultorii?", "arată starea culturilor, umezeala solului și ajută agricultura de precizie", ["face ploaie", "ară terenul", "nu ajută"], "Programul european Copernicus.")
    F.a(2, "3.3", "Ce culturi se fac în livezile din Subcarpații Buzăului?", "pruni, meri, cireși", ["bananieri", "portocali", "măslini"], "Pomicultura e tradițională.")
    F.a(2, "2.2", "Ce culoare are cernoziomul?", "negru", ["alb", "roșu", "galben"], "Bogat în humus.")
    F.a(2, "4.1", "Ce măsură reduce efectele secetei?", "irigațiile și soiurile rezistente la secetă", ["tăierea perdelelor forestiere", "arderea miriștilor", "aratul în pantă"], "Adaptare la climă.")
    F.a(2, "1.2", "Ce înseamnă „arabil”?", "teren care poate fi arat și cultivat", ["teren cu păduri", "teren cu ape", "teren cu clădiri"], "Grâu, porumb, floarea-soarelui.")
    F.a(3, "4.1", "De ce arderea miriștilor (a resturilor de pe câmp) e interzisă?", "poluează aerul, distruge viața din sol și poate produce incendii", ["îmbogățește solul", "e o tradiție obligatorie", "nu are efecte"], "Resturile pot fi încorporate în sol.")

    # ================================================================ S28b Regiunile agricole
    R = Lectie(8, "VIII-S28-regiunile-agricole-elemente-specifice", "Regiunile agricole ale României",
               "Ce se cultivă în jurul orașului nostru?",
               [("Culturile", "Cerealele ocupă cea mai mare suprafață: porumb, grâu, orz – mai ales în Câmpia Română, Câmpia de Vest, Dobrogea, Câmpia Moldovei. România e printre cei mai mari producători de porumb și floarea-soarelui din Uniunea Europeană.\nPlante tehnice: floarea-soarelui, rapița, soia, sfecla de zahăr. Cartoful – în depresiunile din Carpați (Țara Bârsei) și în nordul Moldovei. Legume – în luncile râurilor și lângă orașe (Vidra, Matca)."),
                ("Vița-de-vie și pomii", "Podgorii: Dealu Mare și Pietroasele (Buzău–Prahova), Cotnari, Odobești, Panciu (Vrancea), Murfatlar, Recaș, Jidvei, Drăgășani.\nLivezi: pruni (Argeș, Vâlcea), meri (Suceava, Maramureș), cireși, caiși (Dobrogea)."),
                ("Zootehnia", "Bovine – în zonele cu pășuni (Carpați, Subcarpați, nordul Moldovei). Ovine – România are unul dintre cele mai mari efective de oi din UE; pe pășunile alpine și în Dobrogea. Porcine și păsări – lângă orașe și în câmpie, în ferme mari. Apicultura – în toată țara.")],
               stiaica="Comuna Matca din județul Galați e cunoscută ca „capitala serelor” pentru legume timpurii.",
               ref=REF.format("Regiunile agricole – elemente specifice"), prefix="VIII28b")
    R.a(1, "2.1", "Ce cultură ocupă cea mai mare suprafață în România?", "cerealele (porumb, grâu)", ["cafeaua", "orezul", "ceaiul"], "Câmpiile sunt grânarul țării.")
    R.a(2, "3.1", "Pentru ce culturi e România printre cei mai mari producători din UE?", "porumb și floarea-soarelui", ["măsline și citrice", "orez și ceai", "cafea și cacao"], "După Eurostat.", surse=S_EURO)
    R.s(2, "2.1", "Asociază cultura cu zona.", [("porumb și grâu", "Câmpia Română"), ("cartof", "Țara Bârsei"), ("legume timpurii", "Matca (Galați)"), ("caiși", "Dobrogea")], "Regiuni agricole.")
    R.s(2, "2.1", "Asociază podgoria cu județul.", [("Pietroasele", "Buzău"), ("Cotnari", "Iași"), ("Murfatlar", "Constanța"), ("Odobești", "Vrancea")], "Podgorii.")
    R.a(2, "2.1", "Ce podgorie cunoscută e în județul Buzău?", "Pietroasele (Dealu Mare)", ["Cotnari", "Murfatlar", "Recaș"], "Pe dealurile subcarpatice.")
    R.a(2, "2.1", "Unde se cultivă mult cartoful?", "în depresiunea Țara Bârsei (Brașov) și în nordul Moldovei", ["în Delta Dunării", "pe litoral", "în Bărăgan, fără irigații"], "Clima mai răcoroasă.")
    R.a(2, "2.1", "Ce pomi fructiferi predomină în Argeș și Vâlcea?", "prunii", ["portocalii", "lămâii", "bananierii"], "Țuica și magiunul.")
    R.a(2, "2.2", "Ce animale se cresc mai ales pe pășunile alpine?", "oile (și vacile)", ["cămilele", "renii", "lamele"], "Transhumanța.")
    R.a(2, "3.3", "Ce înseamnă zootehnie?", "creșterea animalelor", ["cultivarea legumelor", "pescuitul în mare", "extragerea cărbunelui"], "Bovine, ovine, porcine, păsări.")
    R.a(2, "3.3", "Ce înseamnă apicultură?", "creșterea albinelor", ["creșterea peștilor", "cultivarea viței", "creșterea oilor"], "România produce multă miere de salcâm.")
    R.p(2, "2.1", "Atinge pe harta României podgoria Cotnari.", "romania", 47.36, 26.93, "Cotnari", 35, "În județul Iași.")
    R.p(2, "2.1", "Atinge pe harta României podgoria Murfatlar.", "romania", 44.17, 28.41, "Murfatlar", 35, "În județul Constanța.")
    R.p(3, "2.1", "Atinge pe harta României Pietroasele (Buzău).", "romania", 45.1, 26.57, "Pietroasele", 35, "În Subcarpații Buzăului; aici s-a găsit și tezaurul „Cloșca cu puii de aur”.")
    R.adev(2, "2.2", "Vița-de-vie se cultivă mai ales pe dealurile însorite.", True, "Adevărat.")
    R.adev(2, "2.1", "Orezul e principala cultură a României.", False, "Fals: cerealele principale sunt porumbul și grâul.")
    R.l(2, "2.1", "Completează.", "Podgoria din județul Buzău se numește [Pietroasele]; în Dobrogea e podgoria [Murfatlar].", ["Cotnari", "Recaș"], "Podgorii.")
    R.l(2, "3.3", "Completează.", "Creșterea animalelor se numește [zootehnie]; creșterea albinelor se numește [apicultură].", ["pomicultură", "viticultură"], "Ramuri agricole.")
    R.g(3, "2.3", "Graficul arată suprafața cultivată cu principalele culturi într-un județ imaginar de câmpie. Ce cultură domină?", grafic("structura", "Suprafața cultivată (județ imaginar)", [("porumb", 40), ("grâu", 30), ("floarea-soarelui", 20), ("legume", 5), ("altele", 5)], "%"), "porumbul", ["grâul", "floarea-soarelui", "legumele"], "40 % din suprafață.")
    R.a(3, "4.1", "Compară agricultura din Bărăgan cu cea din Maramureș.", "Bărăganul are culturi mari de cereale; Maramureșul are pășuni, fânețe și creșterea animalelor", ["Maramureșul are mai multe cereale", "sunt identice", "Bărăganul are păduri de molid"], "Relieful și clima fac diferența.")
    R.d(2, "2.1", "Ce județ cu podgoriile Odobești și Panciu e marcat pe hartă?", "romania", 45.8, 27.0, "Vrancea", ["Buzău", "Galați", "Bacău"], "Vrancea e vecin cu Buzău.")
    R.a(2, "2.1", "Ce cultură tehnică dă ulei comestibil și e foarte răspândită în câmpie?", "floarea-soarelui", ["cartoful", "prunul", "via"], "Și rapița.")
    R.a(2, "2.1", "Ce cultură tehnică dă zahăr?", "sfecla de zahăr", ["porumbul", "floarea-soarelui", "grâul"], "Se cultivă în Transilvania, Moldova.")
    R.a(2, "3.3", "Ce produse agricole exportă mult România?", "cereale (grâu, porumb) și semințe de floarea-soarelui", ["cafea", "banane", "orez"], "Prin portul Constanța.")
    R.a(2, "2.1", "Ce zonă din jurul Bucureștiului e cunoscută pentru legume?", "Vidra (Ilfov)", ["Sinaia", "Predeal", "Sulina"], "Legumicultură pentru piața capitalei.")
    R.a(2, "2.2", "De ce legumele se cultivă des în luncile râurilor?", "solurile sunt fertile și apa pentru irigat e aproape", ["e mai frig", "nu e apă", "sunt munți"], "Luncile sunt bune pentru grădinărit.")
    R.a(2, "3.3", "Ce tezaur de aur s-a descoperit la Pietroasele (Buzău)?", "„Cloșca cu puii de aur”", ["Tezaurul de la Sânnicolau Mare", "Tezaurul lui Decebal", "Coroana de oțel"], "Descoperit în 1837.")
    R.a(2, "3.3", "Ce animal e crescut mult în Dobrogea și pe pășunile alpine?", "oaia", ["bivolul de apă", "cămila", "renul"], "România are unul dintre cele mai mari efective de oi din UE.")
    R.a(2, "4.1", "Ce cultură se face în jurul Râmnicului Sărat?", "cereale în câmpie și pomi și vii pe dealurile din nord-vest", ["orez și ceai", "bumbac", "cafea"], "Contact deal–câmpie.")
    R.a(2, "2.2", "Ce înseamnă „podgorie”?", "regiune cu multe vii", ["regiune cu păduri", "regiune cu mine", "regiune cu lacuri"], "Dealu Mare, Cotnari etc.")
    R.a(3, "3.3", "De ce în jurul marilor orașe sunt multe ferme de legume, lapte și păsări?", "produsele sunt vândute repede pe piața mare a orașului", ["pentru că e mai frig", "pentru că e interzis la sat", "fără motiv"], "Agricultura periurbană.")

    # ================================================================ S28c Valorificarea produselor agricole
    V = Lectie(8, "VIII-S28-valorificarea-produselor-agricole-traditie", "Valorificarea produselor agricole – tradiție și modernitate",
               "Ce produse tradiționale românești sunt protejate în Uniunea Europeană?",
               [("Industria alimentară", "Produsele agricole sunt prelucrate în industria alimentară: morărit și panificație (făină, pâine), lapte și brânzeturi, carne, uleiuri, zahăr, conserve, vinuri și băuturi.\nFabricile se află lângă zonele de producție sau lângă marii consumatori (orașele)."),
                ("Produse tradiționale", "Unele produse românești sunt protejate în UE ca produse tradiționale sau cu indicație geografică: Magiunul de prune Topoloveni, Salamul de Sibiu, Telemeaua de Ibănești, Cârnații de Pleșcoi (Buzău), Novac afumat din Țara Bârsei și altele.\nPiețele țărănești și târgurile păstrează tradițiile."),
                ("Modernitate", "Agricultura modernă folosește tractoare și combine, irigații prin picurare, sere, drone și imagini satelitare. Crește agricultura ecologică. Fondurile europene ajută fermierii tineri.")],
               stiaica="Cârnații de Pleșcoi, din județul Buzău, sunt protejați în Uniunea Europeană ca indicație geografică.",
               ref=REF.format("Valorificarea produselor agricole – tradiție și modernitate"), prefix="VIII28c")
    V.a(1, "1.1", "Ce ramură industrială prelucrează produsele agricole?", "industria alimentară", ["industria metalurgică", "industria energetică", "industria chimică grea"], "Pâine, lapte, ulei, zahăr.")
    V.s(2, "1.2", "Asociază produsul agricol cu produsul obținut.", [("grâul", "făină și pâine"), ("laptele", "brânză"), ("floarea-soarelui", "ulei"), ("sfecla de zahăr", "zahăr")], "Valorificarea.")
    V.s(2, "3.3", "Asociază produsul tradițional cu zona.", [("Cârnații de Pleșcoi", "Buzău"), ("Magiunul de Topoloveni", "Argeș"), ("Salamul de Sibiu", "Sibiu"), ("Telemeaua de Ibănești", "Mureș")], "Produse protejate.")
    V.a(2, "3.3", "Ce produs din județul Buzău e protejat în UE?", "Cârnații de Pleșcoi", ["Magiunul de Topoloveni", "Salamul de Sibiu", "Telemeaua de Ibănești"], "Indicație geografică protejată.", surse=["Comisia Europeană – eAmbrosia: Cârnați de Pleșcoi (IGP)", "Ministerul Agriculturii – produse cu indicație geografică"])
    V.a(2, "3.3", "Ce înseamnă un produs cu „indicație geografică protejată”?", "un produs legat de o anumită zonă, al cărui nume nu poate fi folosit de alții", ["un produs fabricat oriunde", "un produs interzis", "un produs importat"], "Protejează tradiția locală.")
    V.a(2, "4.1", "De ce fabricile de lapte sunt adesea lângă zonele cu pășuni?", "laptele se strică repede și trebuie prelucrat aproape", ["pentru că e mai frumos", "pentru că e lângă mare", "fără motiv"], "Materia primă perisabilă.")
    V.a(2, "4.1", "De ce fabricile de pâine sunt lângă orașe?", "pâinea se consumă proaspătă, aproape de cumpărători", ["grâul crește în oraș", "pentru că e mai frig", "fără motiv"], "Aproape de consumator.")
    V.a(2, "3.3", "Ce tehnologie modernă se folosește în agricultură?", "irigarea prin picurare, drone, imagini satelitare", ["plugul de lemn tras de boi", "secera", "nicio tehnologie"], "Agricultura de precizie.")
    V.a(2, "3.3", "Ce sunt piețele țărănești?", "piețe unde producătorii locali își vând direct produsele", ["supermarketuri", "fabrici", "bursa"], "Produse locale, proaspete.")
    V.a(2, "3.3", "Ce ajută tinerii fermieri să-și înceapă afacerea?", "fondurile europene pentru dezvoltare rurală", ["taxele mari", "interzicerea agriculturii", "nimic"], "Programe de sprijin.")
    V.p(2, "2.1", "Atinge pe harta României Pleșcoi (Buzău).", "romania", 45.27, 26.65, "Pleșcoi", 30, "Comuna Berca, județul Buzău.")
    V.p(3, "2.1", "Atinge pe harta României Topoloveni (Argeș).", "romania", 44.81, 25.08, "Topoloveni", 30, "Județul Argeș.")
    V.adev(2, "3.3", "Produsele tradiționale nu au nicio protecție legală.", False, "Fals: unele sunt protejate la nivel european.")
    V.adev(2, "4.1", "Agricultura modernă poate folosi drone pentru a urmări culturile.", True, "Adevărat.")
    V.l(2, "3.3", "Completează.", "Din județul Buzău sunt protejați Cârnații de [Pleșcoi]; din Argeș, magiunul de [Topoloveni].", ["Sibiu", "Ibănești"], "Produse protejate.")
    V.l(2, "1.2", "Completează.", "Din lapte se obține [brânza], iar din floarea-soarelui se obține [uleiul].", ["făina", "zahărul"], "Valorificarea produselor.")
    V.g(3, "2.3", "Graficul arată numărul de ferme ecologice într-o regiune imaginară. Ce tendință observi?", grafic("profil", "Ferme ecologice (regiune imaginară)", [("2015", 120), ("2018", 210), ("2021", 340), ("2024", 480)], "ferme"), "crește numărul fermelor ecologice", ["scade", "rămâne la fel", "dispar"], "Cererea pentru produse ecologice crește.")
    V.o(2, "4.1", "Ordonează drumul brânzei de la stână la masă.", ["oile sunt mulse la stână", "laptele e dus la fabrică sau prelucrat la stână", "se face brânza", "brânza e vândută în piață sau magazin", "ajunge pe masa ta"], "De la stână la masă", "Valorificarea produselor agricole.")
    V.a(3, "4.1", "Compară o stână tradițională cu o fermă modernă de lapte.", "stâna lucrează manual, sezonier, la munte; ferma modernă are mulgătoare mecanice și răcire, tot anul", ["sunt identice", "stâna e mai mecanizată", "ferma nu produce lapte"], "Tradiție și modernitate.")
    V.d(2, "2.1", "Ce oraș, cunoscut pentru salamul care îi poartă numele, e marcat pe hartă?", "romania", 45.79, 24.15, "Sibiu", ["Brașov", "Alba Iulia", "Mediaș"], "Sibiu e în sudul Transilvaniei.")
    V.a(2, "3.3", "Ce înseamnă „de la fermă la consumator”?", "produsele ajung direct de la producător la cumpărător, cu puțini intermediari", ["produsele sunt importate", "produsele sunt aruncate", "produsele sunt vândute doar în străinătate"], "Lanțuri scurte de aprovizionare.")
    V.a(2, "3.3", "Ce băutură tradițională se face din prune?", "țuica (și pălinca)", ["vinul", "berea", "ceaiul"], "Livezile de pruni.")
    V.a(2, "4.1", "De ce morile și silozurile sunt lângă zonele de cereale?", "cerealele se depozitează și se macină aproape de locul recoltării", ["pentru că e lângă munte", "pentru că e lângă pădure", "fără motiv"], "Costuri mai mici de transport.")
    V.a(2, "3.3", "Ce produs dulce tradițional se face din fructe, fără zahăr adăugat, la Topoloveni?", "magiunul", ["mierea", "dulceața de trandafiri", "ciocolata"], "Primul produs românesc protejat în UE (2011).")
    V.a(2, "3.3", "Ce produs apicol de calitate exportă România?", "mierea de salcâm", ["cafeaua", "cacaoa", "ceaiul verde"], "Salcâmul înflorește în mai.")
    V.a(3, "4.1", "De ce e importantă păstrarea rețetelor tradiționale?", "fac parte din identitatea locală și atrag turiști", ["nu sunt importante", "sunt interzise", "sunt toate identice"], "Patrimoniu gastronomic.")
    V.a(2, "3.3", "Ce sunt serele?", "construcții acoperite unde plantele cresc protejate, chiar și iarna", ["păduri", "mine", "lacuri"], "Legume timpurii.")
    V.a(2, "4.1", "Ce problemă au micii producători?", "greutăți în a-și vinde produsele la prețuri bune", ["prea mulți cumpărători", "nu au produse", "nu au pământ deloc"], "Asociațiile de producători ajută.")
    V.a(2, "3.3", "Ce înseamnă „agroturism”?", "turism în gospodării rurale, cu produse de casă", ["turism la fabrici", "turism în aeroporturi", "turism doar la mare"], "Leagă agricultura de turism.")

    V.a(2, "3.3", "Ce brânză tradițională de oaie se maturează în coajă de brad?", "brânza de burduf în coajă de brad", ["parmezanul", "camembertul", "mozzarella"], "Tradiție din Bran și Mărginimea Sibiului.")

    # ================================================================ S30a Resursele naturale și industria
    I = Lectie(8, "VIII-S30-resursele-naturale-industria", "Resursele naturale și industria",
               "Ce resurse are subsolul României?",
               [("Resurse energetice", "Petrol: în Subcarpați (Prahova, Dâmbovița, Bacău – Moinești), Podișul Getic, Câmpia Română, platforma continentală a Mării Negre.\nGaze naturale: în Depresiunea Colinară a Transilvaniei (Mediaș, Sărmășel), în Moldova, Muntenia și în Marea Neagră (zăcământul Neptun Deep, în dezvoltare).\nCărbune: huilă în Depresiunea Petroșani (Valea Jiului); lignit în Oltenia (Rovinari, Motru)."),
                ("Resurse minerale", "Minereuri: în Munții Apuseni (aur, argint – Roșia Montană, Baia de Arieș), în Maramureș (minereuri neferoase), în Banat (fier, în trecut). Sare: Slănic, Turda, Praid, Ocnele Mari, Târgu Ocna. Roci de construcție: marmură (Ruschița), granit (Măcin), calcar (cimentării)."),
                ("Industria", "Ramuri importante: energetică, metalurgică (Galați – oțel; Slatina – aluminiu), construcții de mașini (automobile, vagoane, nave), chimică și petrochimică (Ploiești, Pitești, Năvodari – Petromidia), materiale de construcții, lemnului și mobilei, alimentară, textilă, electronică.")],
               stiaica="Primul oraș din lume cu iluminat public pe bază de petrol lampant a fost Bucureștiul, în 1857. În același an, România a fost prima țară cu producție de petrol înregistrată oficial.",
               ref=REF.format("Resursele naturale și industria"), prefix="VIII30a")
    I.s(1, "2.1", "Asociază resursa cu zona.", [("gazele naturale", "Depresiunea Transilvaniei"), ("huila", "Valea Jiului"), ("lignitul", "Oltenia"), ("aurul", "Munții Apuseni")], "Resurse ale subsolului.")
    I.s(1, "2.1", "Asociază salina cu județul.", [("Slănic", "Prahova"), ("Turda", "Cluj"), ("Praid", "Harghita"), ("Ocnele Mari", "Vâlcea")], "Saline.")
    I.a(1, "2.1", "Unde se extrage petrol în România?", "în Subcarpați, Podișul Getic, Câmpia Română și în Marea Neagră", ["doar în Delta Dunării", "în Munții Retezat", "nu se extrage"], "Prahova e un vechi județ petrolier.")
    I.a(2, "2.1", "Ce zăcământ mare de gaze din Marea Neagră e în dezvoltare?", "Neptun Deep", ["Sărmășel", "Mediaș", "Rovinari"], "Unul dintre cele mai mari din UE.")
    I.a(2, "2.1", "Unde se află principalul bazin de huilă?", "în Depresiunea Petroșani (Valea Jiului)", ["în Dobrogea", "în Delta Dunării", "în Bărăgan"], "Exploatarea e în declin.")
    I.a(2, "2.1", "Unde se extrage lignit pentru termocentrale?", "în Oltenia (Rovinari, Motru)", ["în Maramureș", "în Delta", "pe litoral"], "Exploatare la suprafață, în cariere.")
    I.a(2, "3.3", "Ce oraș are cel mai mare combinat siderurgic (oțel) al României?", "Galați", ["Brașov", "Sibiu", "Suceava"], "Pe Dunăre, cu acces la minereu importat.")
    I.a(2, "3.3", "Ce oraș are o mare fabrică de aluminiu?", "Slatina", ["Constanța", "Iași", "Bistrița"], "Alro Slatina.")
    I.a(2, "3.3", "Ce oraș e un centru important al industriei petrochimice?", "Ploiești", ["Sinaia", "Sighișoara", "Sulina"], "Rafinăriile Petrobrazi și Petrotel.")
    I.a(2, "3.3", "Ce rafinărie mare e pe litoral, la Năvodari?", "Petromidia", ["Petrobrazi", "Petrotel", "Arpechim"], "Lângă Constanța.")
    I.a(2, "3.3", "Ce rocă de construcție se extrage la Ruschița?", "marmura", ["sarea", "cărbunele", "nisipul"], "Marmura de Ruschița, Caraș-Severin.")
    I.p(2, "2.1", "Atinge pe harta României Valea Jiului (Petroșani).", "romania", 45.41, 23.37, "Petroșani", 35, "În sudul județului Hunedoara.")
    I.p(2, "2.1", "Atinge pe harta României Ploiești.", "romania", 44.94, 26.02, "Ploiești", 30, "Capitala petrolului românesc.")
    I.p(3, "2.1", "Atinge pe harta României Mediaș, centru al gazelor naturale.", "romania", 46.16, 24.35, "Mediaș", 30, "În Depresiunea Transilvaniei.")
    I.adev(2, "3.3", "România a fost prima țară cu producție de petrol înregistrată oficial, în 1857.", True, "Adevărat.", surse=["Encyclopaedia Britannica – Ploiești / Romanian petroleum industry", "Muzeul Național al Petrolului, Ploiești"])
    I.adev(2, "2.1", "Gazele naturale se extrag mai ales în Delta Dunării.", False, "Fals: mai ales în Depresiunea Transilvaniei și în Marea Neagră.")
    I.l(2, "2.1", "Completează.", "Huila se extrage în Valea [Jiului], iar lignitul în [Oltenia].", ["Prahovei", "Dobrogea"], "Cărbunele.")
    I.l(2, "3.3", "Completează.", "Oțelul se produce la [Galați], iar aluminiul la [Slatina].", ["Ploiești", "Sinaia"], "Metalurgia.")
    I.g(3, "2.3", "Graficul arată producția de cărbune într-un bazin imaginar. Ce tendință observi?", grafic("profil", "Producția de cărbune (bazin imaginar)", [("1990", 40), ("2000", 25), ("2010", 18), ("2020", 8), ("2024", 4)], "milioane t"), "producția scade puternic", ["crește", "rămâne la fel", "se dublează"], "Închiderea minelor și tranziția energetică.")
    I.a(3, "4.1", "De ce minele de cărbune se închid treptat?", "cărbunele poluează mult, iar UE trece la energie curată; multe mine nu mai sunt rentabile", ["s-a terminat tot cărbunele lumii", "e interzis să mai muncești", "fără motiv"], "Tranziția energetică.")
    I.d(2, "2.1", "Ce oraș-port cu combinat siderurgic e marcat pe hartă?", "romania", 45.44, 28.05, "Galați", ["Brăila", "Tulcea", "Constanța"], "Galați e pe Dunăre.")
    I.a(2, "3.3", "Ce problemă a apărut în Valea Jiului după închiderea minelor?", "lipsa locurilor de muncă și plecarea oamenilor", ["prea multe locuri de muncă", "prea mulți turiști", "nicio problemă"], "Reconversie profesională, turism, energie nouă.")
    I.a(2, "4.1", "Ce înseamnă industrie extractivă?", "industria care scoate resursele din subsol", ["industria care face mobilă", "industria de software", "industria textilă"], "Mine, cariere, sonde.")
    I.a(2, "4.1", "Ce înseamnă industrie prelucrătoare?", "industria care transformă materiile prime în produse", ["industria care extrage petrol", "agricultura", "turismul"], "Metalurgie, mașini, alimentară etc.")
    I.a(2, "3.3", "Ce industrie folosește lemnul din Carpați?", "industria lemnului și a mobilei", ["industria aluminiului", "industria petrolieră", "industria pescuitului"], "Fabrici de mobilă în Suceava, Bistrița, Maramureș.")
    I.a(3, "4.1", "De ce resursele de aur din Apuseni au fost exploatate din Antichitate?", "erau la suprafață sau aproape, în munți accesibili", ["erau în mare", "au fost aduse de romani din Spania", "nu au fost exploatate"], "Galeriile romane de la Roșia Montană.")
    I.a(2, "3.3", "Ce salină e una dintre cele mai vizitate atracții turistice din Transilvania?", "Salina Turda", ["Salina Slănic", "Salina Praid", "Salina Ocnele Mari"], "Are un parc de distracții subteran.")
    I.a(2, "3.3", "Ce industrie e importantă la Buzău?", "industria metalurgică ușoară, alimentară și a materialelor de construcții", ["construcția de nave maritime", "mineritul aurului", "industria aeronautică"], "Buzău are o industrie diversificată.")
    I.a(2, "4.1", "Ce înseamnă „reconversia” unei zone industriale?", "transformarea ei pentru alte activități (servicii, turism, energie curată)", ["construirea de noi mine", "abandonarea totală", "nimic"], "Ex.: muzee în foste mine.")

    I.a(2, "2.1", "Ce oraș din Bacău e un vechi centru petrolier?", "Moinești", ["Sulina", "Vama Veche", "Sinaia"], "În Subcarpații Moldovei.")

    # ================================================================ S30b Industria energetică
    E = Lectie(8, "VIII-S30-industria-energetica-energiei-electrice", "Industria energetică și a energiei electrice",
               "De unde vine curentul electric din priza ta?",
               [("Centralele", "Hidrocentrale: Porțile de Fier I și II (pe Dunăre), pe Bistrița (Stejaru, lacul Izvorul Muntelui), Argeș (Vidraru), Lotru (Ciunget), Olt, Sebeș.\nCentrala nucleară de la Cernavodă: două reactoare, care produc aproximativ o cincime din electricitatea țării.\nTermocentrale pe cărbune (Rovinari, Turceni – Oltenia) și pe gaze (București, Brazi)."),
                ("Energia regenerabilă", "Parcuri eoliene – mai ales în Dobrogea (Fântânele–Cogealac, unul dintre cele mai mari parcuri eoliene pe uscat din Europa). Panouri solare – în sud și în Dobrogea, pe acoperișuri.\nBiomasă, energie geotermală (Oradea, Beiuș)."),
                ("Mixul energetic", "România are un mix energetic variat, cu o pondere importantă a surselor care nu emit dioxid de carbon (hidro, nuclear, eolian, solar). Cărbunele scade, iar sursele regenerabile cresc.")],
               stiaica="Parcul eolian de la Fântânele–Cogealac, din Dobrogea, are sute de turbine și a fost la inaugurare unul dintre cele mai mari parcuri eoliene pe uscat din Europa.",
               ref=REF.format("Industria energetică și a energiei electrice"), prefix="VIII30b")
    E.s(2, "2.1", "Asociază centrala cu locul.", [("hidrocentrala Porțile de Fier I", "Dunăre"), ("centrala nucleară", "Cernavodă"), ("termocentrala pe lignit", "Rovinari"), ("parcul eolian", "Fântânele–Cogealac")], "Centralele României.")
    E.a(1, "2.1", "Unde se află singura centrală nucleară a României?", "la Cernavodă", ["la Rovinari", "la Porțile de Fier", "la Ploiești"], "Pe Canalul Dunăre–Marea Neagră.", surse=S_CNE)
    E.a(2, "3.1", "Câte reactoare funcționează la Cernavodă?", "două", ["unul", "cinci", "zece"], "Se pregătesc unitățile 3 și 4.", surse=S_CNE)
    E.a(2, "3.1", "Ce parte din electricitatea României produce centrala de la Cernavodă?", "aproximativ o cincime", ["aproape toată", "o sutime", "jumătate"], "Aproximativ 18–20 %.", surse=S_CNE)
    E.a(2, "2.1", "Care e cea mai mare hidrocentrală a României?", "Porțile de Fier I", ["Vidraru", "Stejaru", "Lotru"], "Pe Dunăre, din 1972.", surse=S_PDF)
    E.a(2, "2.2", "De ce parcurile eoliene sunt mai ales în Dobrogea?", "acolo bate des vânt puternic, iar terenul e deschis", ["acolo e cărbune", "acolo sunt munți înalți", "acolo plouă mult"], "Condiții bune pentru turbine.")
    E.a(2, "2.2", "De ce hidrocentralele sunt construite pe râuri de munte?", "apa coboară de la înălțime și are multă energie", ["pentru că apa e caldă", "pentru că e la mare", "fără motiv"], "Diferența de nivel produce energie.")
    E.a(2, "2.1", "Unde sunt marile termocentrale pe lignit?", "în Oltenia (Rovinari, Turceni)", ["în Delta Dunării", "în Maramureș", "pe litoral"], "Aproape de carierele de lignit.")
    E.a(2, "3.3", "Ce sursă de energie e geotermală?", "căldura din interiorul Pământului (apă fierbinte din adânc)", ["vântul", "Soarele", "cărbunele"], "Folosită la Oradea și Beiuș.")
    E.a(2, "3.3", "Care surse de energie nu emit dioxid de carbon la producere?", "hidro, nuclear, eolian, solar", ["cărbune și gaze", "petrol", "lemn ars"], "Surse „curate”.")
    E.p(2, "2.1", "Atinge pe harta României Cernavodă.", "romania", 44.34, 28.03, "Cernavodă", 30, "În județul Constanța.", surse=S_CNE)
    E.p(2, "2.1", "Atinge pe harta României Fântânele–Cogealac, parcul eolian.", "romania", 44.55, 28.55, "Fântânele–Cogealac", 35, "În Dobrogea centrală.")
    E.p(3, "2.1", "Atinge pe harta României Rovinari.", "romania", 44.92, 23.17, "Rovinari", 30, "În județul Gorj.")
    E.adev(2, "3.3", "Energia eoliană și solară sunt surse regenerabile.", True, "Adevărat.")
    E.adev(2, "3.3", "România produce toată electricitatea din cărbune.", False, "Fals: are un mix variat; cărbunele e în scădere.")
    E.l(2, "2.1", "Completează.", "Centrala nucleară e la [Cernavodă], iar cea mai mare hidrocentrală la Porțile de [Fier].", ["Rovinari", "Aur"], "Energia României.", surse=S_CNE)
    E.l(2, "3.3", "Completează.", "Energia produsă de vânt se numește [eoliană], iar cea din căldura Pământului se numește [geotermală].", ["solară", "nucleară"], "Tipuri de energie.")
    E.g(3, "2.3", "Graficul arată (schematic) mixul energetic al unei țări imaginare asemănătoare României. Ce surse produc împreună cea mai mare parte?", grafic("structura", "Producția de electricitate (țară imaginară)", [("hidro", 30), ("nuclear", 20), ("eolian și solar", 18), ("gaze", 17), ("cărbune", 15)], "%"), "hidro și nuclear", ["cărbune și gaze", "doar cărbunele", "doar solarul"], "50 % din producție.")
    E.a(3, "4.1", "De ce scade folosirea cărbunelui?", "cărbunele poluează cel mai mult și produce mult CO₂; UE trece la surse curate", ["pentru că e prea ieftin", "pentru că e regenerabil", "fără motiv"], "Tranziția energetică.")
    E.d(2, "2.1", "Ce baraj pe Argeș, în Munții Făgăraș, e marcat pe hartă?", "romania", 45.37, 24.63, "Vidraru", ["Stejaru", "Porțile de Fier", "Lotru"], "Barajul Vidraru, din 1966.")
    E.a(2, "4.1", "Ce poți face acasă pentru a economisi energie?", "becuri LED, stingi lumina, scoți încărcătoarele din priză", ["lași totul aprins", "deschizi geamul cu caloriferul pornit", "folosești aparate vechi"], "Eficiență energetică.")
    E.a(2, "3.3", "Ce sunt panourile fotovoltaice?", "panouri care transformă lumina Soarelui în electricitate", ["turbine de vânt", "baraje", "reactoare"], "Pe acoperișuri și în parcuri solare.")
    E.a(2, "3.3", "Ce înseamnă „mix energetic”?", "combinația de surse din care o țară produce energie", ["un singur tip de centrală", "un amestec de combustibili în mașină", "o rețea de drumuri"], "Hidro, nuclear, eolian, gaze etc.")
    E.a(2, "2.1", "Ce hidrocentrală mare e pe Bistrița, lângă Ceahlău?", "Stejaru (lacul Izvorul Muntelui)", ["Vidraru", "Porțile de Fier", "Ciunget"], "Una dintre primele mari hidrocentrale.")
    E.a(2, "2.1", "Ce hidrocentrală subterană mare e pe Lotru?", "Ciunget (Lotru)", ["Vidraru", "Stejaru", "Porțile de Fier"], "Centrala e săpată în munte.")
    E.a(3, "4.1", "Compară o hidrocentrală cu o termocentrală pe cărbune.", "hidrocentrala folosește apa, nu poluează aerul; termocentrala arde cărbune și poluează", ["sunt identice", "hidrocentrala poluează mai mult", "termocentrala folosește vântul"], "Impact diferit asupra mediului.")
    E.a(2, "3.3", "Ce înseamnă „prosumator”?", "o persoană care și produce energie (de exemplu, cu panouri solare), și consumă", ["un tip de centrală", "un furnizor de gaze", "un muncitor la mină"], "Tot mai mulți români au panouri pe casă.")
    E.a(2, "4.1", "Ce dezavantaj are energia solară?", "nu se produce noaptea și scade iarna", ["poluează mult", "folosește cărbune", "e radioactivă"], "Se folosesc baterii de stocare.")
    E.a(2, "3.3", "Ce oraș folosește apa geotermală pentru încălzirea locuințelor?", "Oradea", ["Constanța", "Iași", "Suceava"], "Și Beiuș.")

    E.a(2, "1.2", "Ce înseamnă „sursă regenerabilă de energie”?", "o sursă care se reface sau nu se termină (apă, vânt, Soare)", ["cărbunele", "petrolul", "gazele naturale"], "Spre deosebire de combustibilii fosili.")

    # ================================================================ S30c Industria construcțiilor de mașini
    M = Lectie(8, "VIII-S30-industria-constructiilor-masini", "Industria construcțiilor de mașini",
               "Unde se fabrică mașinile Dacia?",
               [("Ce produce", "Industria construcțiilor de mașini produce automobile, camioane, autobuze, vagoane și locomotive, nave, avioane și elicoptere, utilaje agricole, mașini-unelte, echipamente electrice și electronice.\nE una dintre cele mai importante ramuri pentru exporturile României."),
                ("Centre principale", "Automobile: Mioveni (Dacia, din 1968) și Craiova (Ford). Componente auto: Timișoara, Sibiu, Arad, Brașov, Pitești, Cluj.\nVagoane: Arad, Caracal. Nave: Galați, Constanța, Mangalia, Tulcea, Brăila. Elicoptere și avioane: Brașov (Ghimbav), Craiova, Bacău. Utilaje și rulmenți: Brașov, Bârlad. Echipamente electrice: București, Craiova."),
                ("Factori de localizare", "Fabricile se localizează după: forță de muncă calificată, tradiție industrială, căi de transport (autostrăzi, porturi), apropierea de piață și furnizori, investiții străine.")],
               stiaica="Primul automobil Dacia 1100 a ieșit de pe banda uzinei de la Mioveni (Colibași) în 1968, urmat în 1969 de celebra Dacia 1300.",
               ref=REF.format("Industria construcțiilor de mașini"), prefix="VIII30c")
    M.a(1, "2.1", "Unde se fabrică automobilele Dacia?", "la Mioveni (Argeș)", ["la Craiova", "la Galați", "la Brașov"], "Din 1968.", surse=S_DACIA)
    M.a(2, "2.1", "Unde se fabrică automobile Ford în România?", "la Craiova", ["la Mioveni", "la Arad", "la Constanța"], "Uzina din Oltenia.")
    M.s(2, "2.1", "Asociază produsul cu centrul industrial.", [("automobile Dacia", "Mioveni"), ("nave", "Galați"), ("vagoane", "Arad"), ("elicoptere", "Brașov (Ghimbav)")], "Centre ale industriei.")
    M.a(2, "2.1", "Ce orașe-port construiesc nave?", "Galați, Constanța, Mangalia, Tulcea", ["Sibiu, Brașov", "Cluj, Oradea", "Iași, Suceava"], "Șantiere navale.")
    M.a(2, "3.3", "De ce industria construcțiilor de mașini e importantă pentru România?", "e una dintre ramurile cu cele mai mari exporturi", ["nu exportă nimic", "e cea mai poluantă", "nu are muncitori"], "Automobile și componente auto.")
    M.s(2, "4.1", "Asociază factorul de localizare cu exemplul.", [("port la apă", "șantierele navale de la Galați"), ("tradiție industrială", "Brașov"), ("autostradă și forță de muncă", "fabricile de componente din Timișoara"), ("investiții străine", "Ford Craiova")], "De ce fabricile sunt acolo unde sunt.")
    M.a(2, "3.3", "În ce an a fost produsă prima Dacia la Mioveni?", "1968", ["1918", "1990", "2007"], "Dacia 1100.", surse=S_DACIA)
    M.a(2, "2.1", "Ce oraș are o tradiție de fabricare a camioanelor și tractoarelor?", "Brașov", ["Constanța", "Sulina", "Suceava"], "Uzinele Steagul Roșu și Tractorul (azi alte activități).")
    M.a(2, "2.1", "Ce oraș din vest are fabrici de componente auto și electronice?", "Timișoara", ["Botoșani", "Vaslui", "Tulcea"], "Și Arad, Oradea.")
    M.p(2, "2.1", "Atinge pe harta României Mioveni.", "romania", 44.95, 24.94, "Mioveni", 30, "Lângă Pitești.", surse=S_DACIA)
    M.p(2, "2.1", "Atinge pe harta României Craiova.", "romania", 44.32, 23.8, "Craiova", 30, "În Oltenia.")
    M.p(3, "2.1", "Atinge pe harta României Arad, centru de construcție a vagoanelor.", "romania", 46.18, 21.32, "Arad", 30, "Pe Mureș.")
    M.adev(2, "3.3", "Automobilele Dacia se exportă în multe țări europene.", True, "Adevărat.")
    M.adev(2, "2.1", "Navele se construiesc mai ales în orașele de munte.", False, "Fals: în porturi (Galați, Constanța, Mangalia, Tulcea).")
    M.l(2, "2.1", "Completează.", "Dacia se produce la [Mioveni], iar Ford la [Craiova].", ["Brașov", "Arad"], "Industria auto.")
    M.l(2, "2.1", "Completează.", "Vagoanele se fac la [Arad], iar elicopterele la [Brașov].", ["Galați", "Sulina"], "Alte produse.")
    M.g(3, "2.3", "Graficul arată structura exporturilor unei țări imaginare. Ce grupă de produse domină?", grafic("structura", "Exporturi (țară imaginară)", [("mașini și echipamente de transport", 45), ("produse agricole", 15), ("metale", 10), ("chimice", 10), ("altele", 20)], "%"), "mașinile și echipamentele de transport", ["produsele agricole", "metalele", "produsele chimice"], "Aproape jumătate din exporturi.")
    M.a(3, "4.1", "De ce fabricile de componente auto s-au dezvoltat mult în vestul țării?", "aproape de granița cu UE, cu autostrăzi spre vest și forță de muncă calificată", ["pentru că e la mare", "pentru că sunt mine de aur", "fără motiv"], "Accesibilitate spre piețele europene.")
    M.d(2, "2.1", "Ce oraș cu șantier naval, pe Dunăre, la intrarea în Deltă, e marcat pe hartă?", "romania", 45.18, 28.8, "Tulcea", ["Galați", "Brăila", "Giurgiu"], "Șantierul naval Vard Tulcea.")
    M.a(2, "3.3", "Ce sunt mașinile-unelte?", "mașini care prelucrează alte piese (strunguri, freze)", ["mașini de oraș", "jucării", "tractoare"], "Baza industriei.")
    M.a(2, "3.3", "Ce înseamnă „automobil electric”?", "un automobil care funcționează cu baterii, fără benzină", ["un automobil pe cărbune", "un automobil cu cai", "un tren"], "Dacia produce și modele electrice.")
    M.a(2, "3.3", "Ce industrie cere mult oțel și aluminiu?", "construcțiile de mașini", ["turismul", "agricultura ecologică", "serviciile bancare"], "Legături între ramuri.")
    M.a(2, "4.1", "Ce înseamnă „investiție străină”?", "o companie din altă țară construiește o fabrică sau cumpără una în România", ["un împrumut de la prieteni", "un concurs", "un tip de taxă"], "Ex.: Renault la Dacia, Ford la Craiova.")
    M.a(2, "3.3", "Ce industrie de mașini e importantă la Bârlad?", "rulmenții", ["navele", "avioanele", "vagoanele"], "Rulmenți pentru mașini și utilaje.")
    M.a(3, "4.1", "Ce avantaj are o fabrică de nave la Galați față de una la Sibiu?", "Galați e pe Dunărea maritimă, deci navele pot fi lansate direct pe apă", ["Sibiu e la mare", "Galați e la munte", "nu e niciun avantaj"], "Localizare lângă apă.")
    M.a(2, "3.3", "Ce oraș din Moldova are o fabrică de avioane (aeronautică)?", "Bacău", ["Botoșani", "Vaslui", "Piatra Neamț"], "Aerostar Bacău.")
    M.a(2, "4.1", "Ce înseamnă „forță de muncă calificată”?", "muncitori și ingineri bine pregătiți pentru o anumită meserie", ["oameni fără pregătire", "mașini", "roboți doar"], "Școlile profesionale și universitățile tehnice.")
    M.a(2, "3.3", "Ce sunt roboții industriali?", "mașini automate care fac operații repetitive în fabrici", ["jucării", "mașini de curse", "tractoare"], "Folosiți în uzinele de automobile.")
    M.a(3, "4.1", "De ce un parc industrial e construit lângă o autostradă?", "pentru transportul rapid al materiilor prime și al produselor", ["pentru priveliște", "pentru că e interzis altundeva", "fără motiv"], "Accesibilitate.")

    M.a(2, "2.1", "Ce oraș are o tradiție în construcția de autobuze și camioane, în trecut (Roman)?", "Brașov", ["Constanța", "Tulcea", "Mangalia"], "Uzina ROMAN Brașov.")

    # ================================================================ S31a Căile de comunicație și transporturile
    T = Lectie(8, "VIII-S31-serviciile-caile-comunicatie-transporturile", "Serviciile – căile de comunicație și transporturile",
               "Cum ajungi cel mai repede de la Râmnicu Sărat la București?",
               [("Transportul rutier și feroviar", "Drumurile europene și naționale leagă toate orașele. Autostrăzi: A1 (București – Pitești – Sibiu – Deva – Arad – Nădlac), A2 (București – Constanța), A3 (București – Ploiești; Transilvania), A0 (centura Bucureștiului), A7 (Autostrada Moldovei, în construcție, pe lângă Buzău și Râmnicu Sărat), A10 și altele.\nCăile ferate au peste 10 000 km; marile noduri: București, Brașov, Ploiești, Craiova, Cluj, Iași. Râmnicu Sărat e pe magistrala București – Buzău – Focșani – Suceava."),
                ("Transportul naval și aerian", "Transportul maritim prin portul Constanța, cel mai mare de la Marea Neagră. Transportul fluvial pe Dunăre (Galați, Brăila, Giurgiu, Drobeta) și pe Canalul Dunăre–Marea Neagră.\nTransport aerian: aeroportul Henri Coandă (Otopeni), apoi Cluj, Timișoara, Iași, Sibiu, Suceava, Constanța."),
                ("Alte transporturi", "Prin conducte se transportă petrol și gaze naturale. Rețelele de telecomunicații și internetul rapid sunt și ele căi de comunicație moderne.")],
               stiaica="Canalul Dunăre–Marea Neagră, deschis în 1984, scurtează drumul navelor spre portul Constanța cu aproximativ 400 km față de ocolul prin Deltă.",
               ref=REF.format("Serviciile – Căile de comunicație și transporturile"), prefix="VIII31a")
    T.s(2, "2.1", "Asociază autostrada cu traseul.", [("A1", "București – Pitești – Sibiu – Arad"), ("A2", "București – Constanța"), ("A3", "București – Ploiești"), ("A0", "centura Bucureștiului")], "Autostrăzi.")
    T.a(1, "2.1", "Ce autostradă leagă Bucureștiul de Constanța?", "A2 (Autostrada Soarelui)", ["A1", "A3", "A7"], "Trece podurile de la Fetești–Cernavodă.")
    T.a(2, "2.1", "Ce autostradă în construcție va trece pe lângă Buzău și Râmnicu Sărat?", "A7 (Autostrada Moldovei)", ["A1", "A2", "A10"], "Leagă Ploieștiul de nordul Moldovei.")
    T.a(2, "2.1", "Pe ce magistrală feroviară se află Râmnicu Sărat?", "București – Buzău – Focșani – Suceava", ["București – Constanța", "București – Craiova – Timișoara", "Cluj – Oradea"], "Leagă Muntenia de Moldova.")
    T.a(2, "2.1", "Care e cel mai mare port maritim al României?", "Constanța", ["Galați", "Brăila", "Mangalia"], "Cel mai mare de la Marea Neagră.", surse=S_PORT)
    T.a(2, "2.1", "Care e cel mai mare aeroport al României?", "Henri Coandă (Otopeni)", ["Traian Vuia (Timișoara)", "Avram Iancu (Cluj)", "Mihail Kogălniceanu (Constanța)"], "Lângă București.")
    T.a(2, "3.1", "În ce an a fost deschis Canalul Dunăre–Marea Neagră?", "1984", ["1918", "1950", "2007"], "Lung de 64 km.")
    T.a(2, "2.2", "Ce se transportă prin conducte?", "petrol și gaze naturale", ["cereale", "pasageri", "mobilă"], "Transport continuu și ieftin.")
    T.s(2, "3.1", "Asociază tipul de transport cu avantajul lui.", [("aerian", "cel mai rapid pe distanțe mari"), ("naval", "cel mai ieftin pentru mărfuri grele"), ("feroviar", "multe mărfuri și pasageri, poluează puțin"), ("rutier", "ajunge oriunde, din ușă în ușă")], "Avantajele transporturilor.")
    T.p(2, "2.1", "Atinge pe harta României portul Constanța.", "romania", 44.17, 28.65, "Constanța", 30, "La Marea Neagră.", surse=S_PORT)
    T.p(2, "2.1", "Atinge pe harta României Brașov, mare nod feroviar.", "romania", 45.66, 25.61, "Brașov", 30, "La curbura Carpaților.")
    T.p(3, "2.1", "Atinge pe harta României Nădlac, unde A1 iese spre Ungaria.", "romania", 46.17, 20.75, "Nădlac", 35, "La granița de vest.")
    T.adev(2, "2.2", "Transportul naval e cel mai ieftin pentru mărfurile grele.", True, "Adevărat.")
    T.adev(2, "2.1", "Râmnicu Sărat nu are cale ferată.", False, "Fals: e pe magistrala București – Suceava.")
    T.l(2, "2.1", "Completează.", "Autostrada București – Constanța este [A2]; autostrada care va lega Muntenia de Moldova este [A7].", ["A1", "A3"], "Autostrăzi.")
    T.l(2, "2.1", "Completează.", "Cel mai mare port este [Constanța]; cel mai mare aeroport este [Henri Coandă].", ["Galați", "Traian Vuia"], "Noduri de transport.", surse=S_PORT)
    T.g(3, "2.3", "Graficul arată timpul de călătorie Râmnicu Sărat – București cu diferite mijloace (valori aproximative). Care e cel mai rapid pe uscat?", grafic("bare", "Timp aproximativ de călătorie Râmnicu Sărat – București", [("autoturism", 2), ("tren", 2.5), ("autocar", 2.7), ("bicicletă", 9)], "ore"), "autoturismul", ["trenul", "autocarul", "bicicleta"], "Valorile depind de trafic și orar.")
    T.o(3, "2.1", "Ordonează orașele pe magistrala feroviară, de la București spre nord.", ["București", "Ploiești", "Buzău", "Râmnicu Sărat", "Focșani", "Bacău", "Suceava"], "De la sud la nord", "Magistrala 500.")
    T.a(3, "4.1", "Compară transportul pe Dunăre cu cel rutier pentru cereale.", "pe Dunăre e mai ieftin și poluează mai puțin, dar e mai lent; pe șosea e mai rapid, dar mai scump", ["sunt identice", "rutier e mereu mai ieftin", "Dunărea e mai rapidă"], "Alegerea depinde de marfă.")
    T.d(2, "2.1", "Ce oraș-nod rutier și feroviar, vecin cu Râmnicu Sărat, e marcat pe hartă?", "romania", 45.15, 26.82, "Buzău", ["Ploiești", "Focșani", "Brăila"], "Buzău e la intersecția drumurilor spre Moldova, Brașov și Brăila.")
    T.a(2, "4.1", "Ce mijloc de transport e cel mai prietenos cu mediul pentru distanțe lungi?", "trenul electric", ["avionul", "autoturismul cu benzină", "camionul"], "Emisii mici pe pasager.")
    T.a(2, "2.1", "Ce drum spectaculos traversează Munții Făgăraș?", "Transfăgărășanul (DN7C)", ["A2", "DN1", "A7"], "Deschis doar vara.")
    T.a(2, "2.1", "Pe unde trece DN1, cel mai circulat drum național?", "București – Ploiești – Valea Prahovei – Brașov", ["București – Constanța", "Iași – Suceava", "Cluj – Oradea"], "Spre Transilvania.")
    T.a(2, "3.1", "Ce lungime are rețeaua de căi ferate a României?", "peste 10 000 km", ["aproximativ 100 km", "aproximativ 1 000 000 km", "aproximativ 500 km"], "Una dintre cele mai întinse din UE.", surse=["INS – Transporturi: lungimea liniilor de cale ferată", "CFR SA – rețeaua feroviară"])
    T.a(2, "3.1", "Ce coridor paneuropean de transport urmează Dunărea?", "Coridorul VII (Rin–Main–Dunăre)", ["Coridorul I", "Coridorul X", "niciunul"], "Leagă Marea Nordului de Marea Neagră.")
    T.a(2, "4.1", "Ce înseamnă „nod de transport”?", "un loc unde se întâlnesc mai multe căi de comunicație", ["un drum fără ieșire", "un munte", "un lac"], "Ex.: București, Brașov, Buzău.")
    T.a(2, "3.1", "De ce Brașovul are un aeroport nou (Ghimbav)?", "pentru a lega mai bine centrul țării, cu turism și industrie, de alte orașe", ["pentru că e la mare", "pentru că nu are drumuri", "fără motiv"], "Deschis în 2023.", surse=["Aeroportul Internațional Brașov-Ghimbav (brasovairport.ro)", "Wikipedia (ro) – Aeroportul Internațional Brașov-Ghimbav"])
    T.a(2, "3.1", "Ce infrastructură digitală e o cale de comunicație modernă?", "rețelele de internet rapid și telefonie mobilă", ["drumurile de pământ", "căruțele", "poșta cu porumbei"], "România are internet foarte rapid.")
    T.a(2, "4.1", "Ce problemă au drumurile din zonele de munte?", "alunecări de teren, căderi de pietre, zăpezi iarna", ["prea mult soare", "lipsa vehiculelor", "nicio problemă"], "Ex.: DN10 pe Valea Buzăului.")

    T.a(2, "2.1", "Ce pod lung leagă Brăila de Dobrogea peste Dunăre, din 2023?", "podul suspendat de la Brăila", ["Podul Prieteniei Giurgiu–Ruse", "Podul Calafat–Vidin", "Podul de la Cernavodă"], "Scurtează drumul spre Tulcea.")

    # ================================================================ S31b Comerțul
    C = Lectie(8, "VIII-S31-comertul", "Comerțul",
               "Ce produse exportă România și de unde vin lucrurile din magazinele noastre?",
               [("Comerțul interior", "Comerțul interior înseamnă vânzarea-cumpărarea de bunuri în țară: magazine, supermarketuri, piețe, târguri, comerț online.\nCentrele comerciale mari sunt în marile orașe; în localitățile mici sunt piețe și magazine de cartier."),
                ("Comerțul exterior", "Exportul înseamnă vânzarea produselor în alte țări; importul – cumpărarea din alte țări. România exportă mai ales mașini și echipamente, automobile și componente auto, echipamente electrice, cereale și semințe, metale, mobilă.\nImportă mașini și echipamente, produse chimice și medicamente, combustibili, alimente. România importă mai mult decât exportă (deficit comercial)."),
                ("Partenerii", "Majoritatea comerțului exterior se face cu țări din Uniunea Europeană, în piața unică. Principalul partener e Germania; urmează Italia, Ungaria, Franța, Polonia. Din afara UE: Turcia, China.")],
               stiaica="Piața unică a Uniunii Europene permite ca mărfurile să circule între statele membre fără taxe vamale și fără controale la graniță.",
               ref=REF.format("Comerțul"), prefix="VIII31b")
    C.a(1, "1.1", "Ce înseamnă export?", "vânzarea produselor în alte țări", ["cumpărarea din alte țări", "comerțul în țară", "transportul local"], "Opusul importului.")
    C.a(1, "1.1", "Ce înseamnă import?", "cumpărarea produselor din alte țări", ["vânzarea în alte țări", "producția în țară", "depozitarea"], "Ex.: banane, cafea.")
    C.a(2, "1.2", "Care e principalul partener comercial al României?", "Germania", ["China", "SUA", "Brazilia"], "După INS și Eurostat.", surse=S_COM)
    C.a(2, "3.1", "Ce produse exportă mult România?", "automobile și componente auto, mașini, echipamente electrice, cereale", ["cafea și cacao", "petrol în cantități uriașe", "banane"], "Industria auto e principalul exportator.", surse=S_COM)
    C.a(2, "3.1", "Ce înseamnă deficit comercial?", "importurile sunt mai mari decât exporturile", ["exporturile sunt mai mari", "nu există comerț", "comerțul e egal"], "România are deficit comercial.", surse=S_COM)
    C.s(2, "1.2", "Asociază forma de comerț cu exemplul.", [("comerț interior", "cumpărături în supermarketul din oraș"), ("export", "Dacia vândută în Franța"), ("import", "banane aduse din Ecuador"), ("comerț online", "comandă pe internet")], "Forme de comerț.")
    C.a(2, "1.2", "Ce înseamnă piața unică a UE?", "mărfurile circulă între statele membre fără taxe vamale", ["o piață dintr-un singur oraș", "o piață de legume", "un magazin online"], "Libera circulație a mărfurilor.")
    C.a(2, "1.2", "Cu ce grup de țări face România cea mai mare parte a comerțului?", "statele Uniunii Europene", ["țările din Africa", "țările din America de Sud", "țările din Oceania"], "Aproximativ trei sferturi.", surse=S_COM)
    C.a(2, "3.1", "Ce produse importă România?", "mașini și echipamente, produse chimice, medicamente, combustibili", ["doar cereale", "doar automobile Dacia", "nimic"], "Importurile sunt variate.")
    C.a(2, "4.1", "De ce România importă banane și cafea?", "nu se pot cultiva în clima ei", ["sunt mai ieftine de cultivat aici", "e obligatoriu", "fără motiv"], "Clima temperată.")
    C.p(2, "2.1", "Atinge pe harta României portul Constanța, poarta comerțului maritim.", "romania", 44.17, 28.65, "Constanța", 30, "Pe aici trec cerealele exportate.", surse=S_PORT)
    C.p(3, "2.1", "Atinge pe harta României vama Nădlac, poarta rutieră spre vest.", "romania", 46.17, 20.75, "Nădlac", 35, "Pe aici trec multe camioane cu mărfuri.")
    C.adev(2, "3.1", "România exportă mai mult decât importă.", False, "Fals: importă mai mult (deficit comercial).", surse=S_COM)
    C.adev(2, "1.2", "Comerțul online crește foarte mult în România.", True, "Adevărat.")
    C.l(2, "1.1", "Completează.", "Vânzarea în alte țări se numește [export]; cumpărarea din alte țări se numește [import].", ["tranzit", "vamă"], "Comerț exterior.")
    C.l(2, "1.2", "Completează.", "Principalul partener comercial al României este [Germania]; cele mai multe schimburi se fac cu Uniunea [Europeană].", ["China", "Africană"], "Partenerii.", surse=S_COM)
    C.g(3, "2.3", "Graficul arată (schematic) exporturile și importurile unei țări imaginare în trei ani. În ce situație e țara?", grafic("bare", "Comerț exterior (țară imaginară, miliarde euro)", [("export 2022", 90), ("import 2022", 115), ("export 2024", 95), ("import 2024", 120)], "miliarde euro"), "are deficit comercial (importă mai mult)", ["are excedent", "comerțul e echilibrat", "nu are comerț"], "Importurile depășesc exporturile.")
    C.o(2, "4.1", "Ordonează drumul unei mașini Dacia exportate în Franța.", ["e asamblată la Mioveni", "e transportată pe tren sau camion", "trece granița", "ajunge la un dealer din Franța", "e cumpărată de un client"], "Drumul exportului", "Producție, transport, vânzare.")
    C.a(3, "4.1", "Ce avantaje are pentru România apartenența la piața unică?", "acces la un mare număr de cumpărători, fără taxe vamale", ["nu are niciun avantaj", "închide granițele", "interzice exporturile"], "Comerț mai ușor.")
    C.d(2, "2.1", "Ce țară, principalul partener comercial al României, e marcată pe hartă?", "lume", 51, 10.5, "Germania", ["Franța", "Polonia", "Austria"], "Germania e cea mai mare economie a UE.")
    C.a(2, "3.1", "Ce produse agricole exportă România prin portul Constanța?", "cereale și semințe oleaginoase", ["cafea", "ceai", "banane"], "Grâu, porumb, floarea-soarelui.")
    C.a(2, "1.2", "Ce este un centru comercial (mall)?", "o clădire mare cu multe magazine, restaurante și cinematografe", ["o fabrică", "o școală", "o piață de animale"], "În marile orașe.")
    C.a(2, "1.2", "Ce sunt târgurile tradiționale?", "piețe periodice, cu produse locale și meșteșuguri", ["bănci", "fabrici", "aeroporturi"], "Târgul de la Râmnicu Sărat, de exemplu.")
    C.a(2, "4.1", "Ce înseamnă „produs local”?", "produs în zona în care e vândut", ["produs importat din altă țară", "produs fabricat în China", "produs fără etichetă"], "Susține economia locală.")
    C.a(3, "4.1", "De ce cumpărarea de produse locale poate ajuta mediul?", "transportul e mai scurt, deci poluarea e mai mică", ["produsele locale sunt mereu mai scumpe", "nu ajută", "crește poluarea"], "Amprenta de carbon mai mică.")
    C.a(2, "1.2", "Ce țară din afara UE e un partener comercial important al României?", "Turcia (și China)", ["Australia", "Argentina", "Canada"], "Prin Marea Neagră și pe uscat.", surse=S_COM)
    C.a(2, "3.1", "Ce înseamnă „balanță comercială”?", "diferența dintre exporturi și importuri", ["un cântar în magazin", "un tip de taxă", "o bancă"], "Pozitivă = excedent; negativă = deficit.")
    C.a(2, "1.2", "Ce înseamnă „vamă”?", "locul unde se controlează mărfurile și persoanele la graniță", ["un magazin", "un port turistic", "o fabrică"], "În UE, controalele vamale interne au fost eliminate.")
    C.a(2, "4.1", "Ce poți verifica pe eticheta unui produs?", "țara de origine, ingredientele, data expirării", ["numele vânzătorului", "culoarea magazinului", "nimic"], "Consumator informat.")

    C.a(2, "1.2", "Ce înseamnă „comerț electronic”?", "cumpărarea și vânzarea de produse pe internet", ["comerțul cu electronice doar", "comerțul la piață", "comerțul prin poștă cu scrisori"], "Crește rapid în România.")

    # ================================================================ S32 Turismul
    U = Lectie(8, "VIII-S32-turismul-potential-valorificare-economica", "Turismul – potențial și valorificare",
               "Ce i-ai arăta unui turist străin în România?",
               [("Potențialul natural", "Munții: Valea Prahovei (Sinaia, Bușteni, Predeal), Poiana Brașov, Transfăgărășanul, Retezat, Apuseni, Ceahlău. Litoralul: Mamaia, Eforie, Costinești, Neptun, Mangalia, Vama Veche. Delta Dunării. Stațiuni balneare cu ape minerale și termale: Băile Herculane, Băile Felix, Sovata, Slănic Moldova, Covasna, Techirghiol, Băile Govora.\nObiective naturale: peșteri (Scărișoara, Urșilor), chei (Bicaz, Turzii), Vulcanii Noroioși, sfinxul și Babele din Bucegi."),
                ("Potențialul cultural", "Mănăstirile din Bucovina, cu picturi exterioare; bisericile de lemn din Maramureș; satele cu biserici fortificate; cetățile dacice; orașele medievale (Sibiu, Sighișoara, Brașov); castelele Bran și Peleș; Mănăstirea Horezu; Palatul Culturii din Iași; Ateneul Român. Multe sunt în patrimoniul mondial UNESCO."),
                ("Forme de turism", "Turism montan și de sporturi de iarnă, de litoral, balnear, cultural și religios, rural și agroturism, ecoturism (Delta, parcuri naționale), de afaceri, de aventură.\nProbleme: infrastructură insuficientă în unele zone, sezonalitatea litoralului. Soluții: promovare, drumuri, turism tot anul.")],
               stiaica="Castelul Peleș, din Sinaia, a fost unul dintre primele castele din Europa cu electricitate produsă de propria centrală, la sfârșitul secolului al XIX-lea.",
               ref=REF.format("Turismul – potențial și valorificare economică"))
    U.s(2, "3.3", "Asociază stațiunea cu tipul de turism.", [("Poiana Brașov", "sporturi de iarnă"), ("Mamaia", "litoral"), ("Băile Herculane", "balnear"), ("Sirnea", "rural")], "Forme de turism.")
    U.s(2, "3.3", "Asociază obiectivul cultural cu regiunea.", [("mănăstirile pictate", "Bucovina"), ("bisericile de lemn", "Maramureș"), ("cetățile dacice", "Munții Orăștiei"), ("Castelul Bran", "Țara Bârsei")], "Obiective culturale.", surse=S_UNESCO)
    U.a(1, "2.1", "Ce stațiune montană e cunoscută pentru Castelul Peleș?", "Sinaia", ["Mamaia", "Sovata", "Sulina"], "Pe Valea Prahovei.")
    U.a(2, "3.3", "Ce înseamnă turism balnear?", "turism pentru tratament, cu ape minerale, termale și nămoluri", ["turism la mare doar pentru plajă", "turism la schi", "turism în orașe"], "Herculane, Felix, Sovata, Techirghiol.")
    U.a(2, "3.3", "Ce înseamnă ecoturism?", "turism în natură, care respectă mediul și comunitățile locale", ["turism în fabrici", "turism cu mașini de teren peste tot", "turism în mall"], "Delta, parcuri naționale.")
    U.a(2, "3.3", "Ce obiectiv cultural din Bucovina e cunoscut pentru „albastrul de Voroneț”?", "Mănăstirea Voroneț", ["Castelul Bran", "Cetatea Sighișoara", "Ateneul Român"], "Biserică pictată, patrimoniu UNESCO.", surse=S_UNESCO)
    U.a(2, "3.3", "Ce castel e asociat cu legenda lui Dracula?", "Castelul Bran", ["Castelul Peleș", "Castelul Corvinilor", "Palatul Culturii"], "Atrage turiști din toată lumea.")
    U.a(2, "3.3", "Ce problemă are turismul de litoral?", "sezonalitatea: e aglomerat vara și aproape gol iarna", ["e prea frig vara", "nu are plaje", "nu are hoteluri deloc"], "Soluție: turism balnear tot anul.")
    U.a(2, "3.3", "Ce obiectiv turistic natural din județul Buzău e unic?", "Vulcanii Noroioși", ["Peștera Scărișoara", "Cheile Bicazului", "Lacul Sfânta Ana"], "Rezervație naturală la Berca–Pâclele.")
    U.p(2, "2.1", "Atinge pe harta României Sinaia.", "romania", 45.35, 25.55, "Sinaia", 30, "Pe Valea Prahovei.")
    U.p(2, "2.1", "Atinge pe harta României Băile Herculane.", "romania", 44.88, 22.41, "Băile Herculane", 30, "Pe Valea Cernei.")
    U.p(2, "2.1", "Atinge pe harta României Sighișoara.", "romania", 46.22, 24.79, "Sighișoara", 30, "Cetate medievală, patrimoniu UNESCO.", surse=S_UNESCO)
    U.p(3, "2.1", "Atinge pe harta României Mănăstirea Voroneț.", "romania", 47.52, 25.86, "Voroneț", 35, "Lângă Gura Humorului.", surse=S_UNESCO)
    U.adev(2, "3.3", "România are obiective înscrise în patrimoniul mondial UNESCO.", True, "Adevărat: Delta, bisericile pictate, Sighișoara, cetățile dacice și altele.", surse=S_UNESCO)
    U.adev(2, "3.3", "Turismul balnear se practică doar vara.", False, "Fals: se poate practica tot anul.")
    U.l(2, "3.3", "Completează.", "Castelul [Peleș] e în Sinaia; Castelul [Bran] e asociat cu legenda lui Dracula.", ["Corvinilor", "Hunedoara"], "Castele.")
    U.l(2, "3.3", "Completează.", "Turismul pentru tratament se numește turism [balnear]; turismul în natură, responsabil, se numește [ecoturism].", ["urban", "industrial"], "Forme de turism.")
    U.g(3, "2.3", "Graficul arată numărul de turiști pe luni într-o stațiune imaginară de litoral. Ce observi?", grafic("bare", "Turiști pe lună (stațiune imaginară de litoral)", [("ian.", 2), ("apr.", 5), ("iun.", 40), ("iul.", 90), ("aug.", 95), ("sept.", 25), ("nov.", 3)], "mii"), "turismul e concentrat vara (sezonalitate)", ["turiștii vin egal tot anul", "iarna vin cei mai mulți", "nu vin turiști"], "Iulie și august au cei mai mulți turiști.")
    U.o(3, "2.1", "Ordonează stațiunile de pe Valea Prahovei de la sud la nord.", ["Sinaia", "Bușteni", "Azuga", "Predeal"], "De la sud la nord", "Pe DN1 spre Brașov.")
    U.a(3, "4.1", "Compară turismul din Delta Dunării cu cel din Poiana Brașov.", "în Deltă e ecoturism și observarea păsărilor, vara; în Poiana Brașov sunt sporturi de iarnă", ["sunt identice", "în Deltă se schiază", "Poiana Brașov e pe mare"], "Forme diferite de turism.")
    U.d(2, "2.1", "Ce oraș cu Palatul Culturii, mare centru cultural din Moldova, e marcat pe hartă?", "romania", 47.16, 27.59, "Iași", ["Suceava", "Bacău", "Botoșani"], "Iași a fost capitala Moldovei.")
    U.a(2, "3.3", "Ce sunt Babele și Sfinxul?", "forme de relief din Bucegi, modelate de vânt și îngheț", ["statui antice", "peșteri", "lacuri"], "Atracții turistice.")
    U.a(2, "3.3", "Ce venituri aduce turismul?", "locuri de muncă în hoteluri, restaurante, transport, ghizi", ["niciun venit", "doar poluare", "doar cheltuieli"], "Turismul e un serviciu important.")
    U.a(2, "4.1", "Ce poate face o comunitate pentru a atrage turiști?", "drumuri bune, cazare, trasee marcate, promovare, păstrarea tradițiilor", ["închiderea muzeelor", "poluarea râurilor", "tăierea pădurilor"], "Dezvoltarea turismului.")
    U.a(2, "3.3", "Ce traseu turistic leagă Bucovina de Maramureș prin Pasul Prislop?", "drumul transcarpatic peste Pasul Prislop", ["Autostrada A2", "Canalul Dunăre–Marea Neagră", "Transfăgărășanul"], "Leagă două regiuni cu biserici UNESCO.")
    U.a(2, "3.3", "Ce obiectiv turistic din Hunedoara e un castel gotic celebru?", "Castelul Corvinilor", ["Castelul Peleș", "Castelul Bran", "Palatul Parlamentului"], "Unul dintre cele mai mari castele gotice din Europa.")
    U.a(2, "4.1", "Ce înseamnă turismul responsabil?", "turism care respectă natura, cultura locală și nu lasă deșeuri", ["turism cu orice preț", "turism fără reguli", "turism doar în hoteluri de lux"], "Lasă locul mai frumos decât l-ai găsit.")
    U.a(2, "3.3", "Ce stațiune balneară cu lac heliotermal e în județul Mureș?", "Sovata", ["Herculane", "Felix", "Techirghiol"], "Lacul Ursu.")
    U.a(2, "3.3", "Ce traseu turistic din județul Buzău cuprinde Vulcanii Noroioși, Muzeul Chihlimbarului și Focul Viu?", "„Ținutul Buzăului” (Geoparcul Ținutul Buzăului)", ["Valea Prahovei", "Transalpina", "Drumul Vinului Cotnari"], "Geoparc recunoscut de UNESCO în 2022.", surse=["UNESCO – Global Geoparks: Buzău Land (2022)", "Asociația Ținutul Buzăului (geoparc)"])

    U.a(2, "3.3", "Ce stațiune de pe litoral e cea mai mare și mai cunoscută?", "Mamaia", ["Sulina", "Sfântu Gheorghe", "Tulcea"], "La nord de Constanța.")

    # ================================================================ S33 Expediție
    X = Expeditie(8, "VIII-S33-aplicatii-practice-studii-caz", "Expediție: economia orizontului meu",
                  "Ce se produce, ce se vinde și ce se poate vizita în județul Buzău?",
                  ref=REF.format("Aplicații practice/studii de caz: Activități economice în localitatea/județul natal"))
    X.a(1, "4.1", "Ce activități economice poți întâlni în jurul Râmnicului Sărat?", "agricultură, industrie alimentară, comerț, transport, servicii", ["minerit de aur", "construcție de nave maritime", "pescuit oceanic"], "Economia locală.")
    X.pas("1. Harta economică", "Pe harta județului Buzău, marchează cu simboluri: zone agricole, fabrici, magazine mari, gări, obiective turistice.",
          jurnal="Fotografiază harta și explică legenda.", foto=True)
    X.a(2, "4.1", "Ce surse de energie alternativă se pot folosi în județul Buzău?", "solară și eoliană, biomasă", ["energie geotermală vulcanică activă", "energia mareelor", "energie nucleară în fiecare sat"], "Resurse alternative.")
    X.pas("2. Interviul", "Discută cu un adult care lucrează în economia locală (fermier, comerciant, muncitor, antreprenor). Întreabă-l ce face și ce probleme are.",
          jurnal="Notează 3 informații din interviu.")
    X.a(2, "4.1", "Ce obiectiv din Geoparcul Ținutul Buzăului ai propune unui turist?", "Vulcanii Noroioși de la Berca–Pâclele", ["Castelul Peleș", "Peștera Scărișoara", "Delta Dunării"], "Geoparc UNESCO din 2022.")
    X.pas("3. Pliantul turistic", "Realizează un pliant cu 3 obiective turistice din județul Buzău, cu traseul și ce poate vedea vizitatorul.",
          jurnal="Fotografiază pliantul.", foto=True)
    X.pas("4. Propunerea", "Propune o idee de afacere locală care să folosească o resursă a zonei (produse agricole, turism, energie solară).",
          jurnal="Scrie ideea, resursa folosită și cine ar beneficia.")

    return Unitate(8, "u5-economie.json", "Activitățile economice").add(F, R, V, I, E, M, T, C, U, X)
