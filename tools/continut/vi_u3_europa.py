from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VI-a (manuale.edu.ro), lecția „{}”"
S_ELBRUS = ["Encyclopaedia Britannica – Mount Elbrus", "Wikipedia – Mount Elbrus"]
S_MB = ["Encyclopaedia Britannica – Mont Blanc", "Le Monde / AFP, 2021 – Mont Blanc măsurat la 4 805,59 m"]
S_VOLGA = ["Encyclopaedia Britannica – Volga River", "Wikipedia – Volga"]
S_DUNARE = ["ICPDR – Danube Basin facts", "Wikipedia – Danube"]
S_UE = ["Uniunea Europeană – Țările UE (european-union.europa.eu)", "Consiliul UE – statele membre"]
S_EUPOP = ["ONU (UN DESA) – World Population Prospects 2024", "Eurostat / Encyclopaedia Britannica – Europe"]
S_UNESCO = ["UNESCO World Heritage Centre – lista patrimoniului mondial (whc.unesco.org)", "Ministerul Culturii – Monumente UNESCO din România"]


def unitate():
    # ================================================================ S13 Mediul natural ca suport al locuirii
    M = Lectie(6, "VI-S13-mediul-natural-ca-suport", "Mediul natural ca suport al locuirii umane",
               "De ce oamenii au construit orașe pe malul râurilor și al mărilor?",
               [("Mediul și oamenii", "Mediul natural (relieful, clima, apele, solurile, vegetația) a decis de-a lungul timpului unde se stabilesc oamenii și cu ce se ocupă.\nCâmpiile cu soluri fertile au atras agricultorii. Râurile au dat apă, hrană și drumuri. Țărmurile au permis pescuitul și comerțul pe mare. Munții au oferit pășuni, lemn și adăpost."),
                ("Avantaje și limite", "Unele medii sunt favorabile locuirii: climă temperată, apă, relief jos. Altele sunt restrictive: frigul polar, deșertul, munții foarte înalți, mlaștinile.\nOamenii s-au adaptat: case pe piloni în zone inundabile, terase pe pante, irigații în zone secetoase, diguri în Țările de Jos."),
                ("Riscuri naturale", "Mediul aduce și riscuri: cutremure, inundații, alunecări de teren, secete, avalanșe. Oamenii trebuie să construiască și să se poarte ținând cont de ele.")],
               stiaica="În Țările de Jos, o mare parte din teritoriu se află sub nivelul mării și e protejată de diguri și stăvilare.",
               ref=REF.format("Mediul natural ca suport al locuirii umane"))
    M.a(1, "1.1", "Ce înseamnă mediu natural?", "relieful, clima, apele, solurile, plantele și animalele dintr-un loc", ["doar orașele", "doar fabricile", "doar drumurile"], "Mediul natural e ce nu a fost construit de om.")
    M.a(1, "1.2", "De ce au atras câmpiile oamenii?", "pentru solurile fertile și terenul plan, bune pentru agricultură", ["pentru vulcani", "pentru gheață", "pentru frig"], "Agricultura a fixat oamenii în câmpii.")
    M.a(2, "1.2", "Ce le-au oferit râurile primelor așezări?", "apă, pește și drumuri de transport", ["minereu de fier", "zăpadă tot anul", "petrol"], "Multe orașe mari sunt pe râuri: Paris pe Sena, Londra pe Tamisa, Viena pe Dunăre.")
    M.s(2, "1.2", "Asociază mediul cu avantajul lui pentru oameni.", [("câmpia", "agricultură"), ("muntele", "pășuni și lemn"), ("țărmul mării", "pescuit și comerț"), ("valea râului", "apă și cale de transport")], "Fiecare mediu are resursele lui.")
    M.s(2, "1.2", "Asociază mediul restrictiv cu problema lui.", [("deșertul", "lipsa apei"), ("zona polară", "frigul"), ("muntele foarte înalt", "aer rarefiat, pante mari"), ("mlaștina", "teren moale, inundat")], "Unele medii sunt greu de locuit.")
    M.a(2, "1.2", "Cum s-au adaptat oamenii la pantele dealurilor pentru agricultură?", "au construit terase", ["au mutat dealurile", "au acoperit pantele cu ciment", "nu cultivă deloc"], "Terasele reduc eroziunea și permit culturi.")
    M.a(2, "1.2", "Cum s-au protejat locuitorii Țărilor de Jos de mare?", "au construit diguri", ["au mutat țara", "au plantat cactuși", "au săpat munți"], "Digurile țin marea departe.")
    M.p(2, "1.2", "Atinge pe hartă Țările de Jos.", "lume", 52.2, 5.3, "Țările de Jos", 300, "Țările de Jos sunt la Marea Nordului, între Belgia și Germania.")
    M.a(2, "1.2", "Ce risc natural e frecvent în zona Vrancei?", "cutremurele", ["tsunami-urile", "erupțiile vulcanice", "avalanșele de nisip"], "Zona seismică Vrancea produce cutremure puternice, resimțite și la Râmnicu Sărat.")
    M.a(2, "1.2", "De ce casele din zonele inundabile sunt uneori ridicate pe piloni?", "ca apa să treacă pe sub ele la inundații", ["ca să fie mai răcoroase iarna", "ca să se vadă marea", "pentru frumusețe"], "E o adaptare la risc.")
    M.a(2, "1.1", "Ce este o alunecare de teren?", "deplasarea la vale a unei porțiuni de teren de pe o pantă", ["o erupție", "o furtună", "o inundație pe mare"], "Alunecările sunt frecvente în Subcarpați după ploi.")
    M.adev(2, "1.2", "Oamenii pot locui doar în medii fără niciun risc natural.", False, "Fals: oamenii trăiesc și în zone cu riscuri, dar se adaptează și se protejează.")
    M.adev(1, "1.2", "Multe capitale europene sunt construite pe malul unui râu.", True, "Adevărat: Viena, Budapesta, Belgrad pe Dunăre; Paris pe Sena; Londra pe Tamisa.")
    M.l(2, "1.1", "Completează.", "Zonele cu climă temperată, apă și relief jos sunt [favorabile] locuirii; deșerturile și zonele polare sunt [restrictive].", ["interzise", "artificiale"], "Medii favorabile și restrictive.")
    M.l(2, "1.2", "Completează.", "Parisul e pe râul [Sena], iar Londra pe râul [Tamisa].", ["Rin", "Volga"], "Capitale pe râuri.")
    M.a(2, "1.2", "Ce capitale sunt așezate pe Dunăre?", "Viena, Bratislava, Budapesta, Belgrad", ["Paris, Londra, Roma", "Madrid, Lisabona", "Oslo, Stockholm"], "Dunărea trece prin patru capitale.", surse=S_DUNARE)
    M.a(3, "1.2", "De ce în nordul Scandinaviei populația e rară?", "pentru că iernile sunt foarte lungi și reci, iar solul e sărac", ["pentru că e prea cald", "pentru că sunt prea multe orașe", "pentru că e deșert de nisip"], "Frigul limitează agricultura și locuirea.")
    M.a(2, "1.2", "Ce aduce muntele oamenilor?", "pășuni, lemn, ape minerale, turism", ["deșerturi", "petrol din abundență", "plaje"], "Muntele are resurse specifice.")
    M.a(2, "1.1", "Ce înseamnă că un loc e „favorabil locuirii”?", "are condiții bune pentru viață: apă, climă blândă, hrană", ["e foarte frig", "e foarte uscat", "e foarte înalt"], "Condițiile naturale bune atrag oamenii.")
    M.a(3, "1.2", "De ce au apărut orașe vechi la confluența a două râuri?", "pentru apă, transport pe două direcții și apărare", ["pentru că acolo e deșert", "pentru că acolo e gheață", "fără motiv"], "Confluența e un loc strategic.")
    M.a(2, "1.2", "Cum se adaptează casele din zonele cu multă zăpadă?", "au acoperișuri înclinate, pe care zăpada alunecă", ["au acoperișuri plate", "nu au acoperiș", "sunt făcute din hârtie"], "Zăpada grea poate rupe acoperișurile plate.")
    M.a(2, "1.2", "Ce îi ajută pe oameni să cultive în zone secetoase?", "irigațiile", ["digurile marine", "pârtiile de schi", "tunelurile"], "Apa e adusă prin canale.")
    M.a(3, "1.2", "Ce relație există între relief și drumuri?", "drumurile urmează de obicei văile și trec munții prin pasuri", ["drumurile urcă direct pe vârfuri", "relieful nu contează", "drumurile ocolesc câmpiile"], "Pasurile sunt locuri mai joase între munți.")
    M.a(2, "1.1", "Ce este un pas montan?", "un loc mai jos între munți, pe unde trec drumurile", ["un vârf", "un lac", "o peșteră"], "Pasul Predeal, pasul Oituz sunt exemple din Carpați.")
    M.a(2, "1.2", "De ce în deltele mari agricultura e grea?", "pentru că terenul e mlăștinos și se inundă des", ["pentru că e prea uscat", "pentru că e munte", "pentru că e gheață"], "Delta Dunării e potrivită mai ales pentru pescuit și natură.")
    M.a(3, "1.2", "Ce schimbă tehnologia în relația om–mediu?", "permite locuirea și în medii grele (aer condiționat, irigații, încălzire)", ["face mediul complet inutil", "nu schimbă nimic", "oprește riscurile naturale"], "Tehnologia reduce limitele mediului, dar nu le elimină.")
    M.a(2, "1.2", "De ce porturile s-au dezvoltat în golfuri adăpostite?", "pentru că acolo apa e mai liniștită, ferită de valuri mari", ["pentru că apa e dulce", "pentru că acolo sunt munți", "pentru că acolo nu e vânt niciodată"], "Golfurile protejează corăbiile.")
    M.a(2, "1.1", "Ce este o confluență?", "locul unde se unesc două râuri", ["izvorul unui râu", "un lac de munte", "o insulă"], "Confluența e întâlnirea a două râuri.")
    M.a(2, "1.2", "Ce face o pădure pentru așezările de la poalele muntelui?", "reduce alunecările de teren și viiturile", ["produce cutremure", "aduce secetă", "provoacă avalanșe de nisip"], "Pădurea protejează versanții.")
    M.a(3, "1.2", "De ce Râmnicu Sărat s-a dezvoltat în locul în care se află?", "e la contactul dintre deal și câmpie, pe un râu și pe un drum comercial vechi", ["e pe un vârf de munte", "e pe malul mării", "e în mijlocul unui deșert"], "Zonele de contact deal–câmpie au favorizat târgurile.")

    # ================================================================ S16 Poziția geografică. Țărmurile
    P = Lectie(6, "VI-S16-pozitia-geografica-tarmurile-golfuri", "Europa – poziție geografică. Țărmurile",
               "De ce se spune că Europa e o „peninsulă a Asiei”?",
               [("Poziția Europei", "Europa se află în emisfera nordică și în cea mai mare parte în emisfera estică. E înconjurată de Oceanul Arctic la nord, Oceanul Atlantic la vest, Marea Mediterană și Marea Neagră la sud.\nLa est, Europa nu e despărțită de Asia prin apă; granița convențională urmează Munții Ural, râul Ural, Marea Caspică și Munții Caucaz.\nEuropa are aproximativ 10 milioane km² și e unul dintre cele mai mici continente."),
                ("Țărmurile", "Țărmurile Europei sunt foarte crestate: au multe golfuri, peninsule, insule și strâmtori.\nPeninsulele mari: Scandinavă (cea mai mare), Iberică, Italică, Balcanică, Crimeea, Iutlanda.\nInsulele mari: Marea Britanie (cea mai mare), Islanda, Irlanda, Sicilia, Sardinia, Corsica, Creta.\nGolfuri: Golful Biscaya, Golful Botnic, Golful Finic. Strâmtori: Gibraltar, Bosfor, Dardanele, Pas de Calais (Canalul Mânecii)."),
                ("Termeni", "Peninsula e uscatul înconjurat de apă din trei părți. Insula e uscatul înconjurat de apă din toate părțile. Golful e apa care pătrunde în uscat. Strâmtoarea e o apă îngustă între două uscaturi, care leagă două mări.")],
               stiaica="Strâmtoarea Gibraltar, dintre Europa și Africa, are în punctul cel mai îngust aproximativ 14 km. În zilele senine, din Spania se vede Marocul.",
               ref=REF.format("Poziția geografică. Țărmurile"))
    P.s(1, "2.2", "Asociază termenul cu definiția.", [("peninsulă", "uscat înconjurat de apă din trei părți"), ("insulă", "uscat înconjurat de apă din toate părțile"), ("golf", "apă care pătrunde în uscat"), ("strâmtoare", "apă îngustă între două uscaturi")], "Formele țărmului.")
    P.a(1, "2.1", "Ce ocean scaldă Europa la vest?", "Oceanul Atlantic", ["Oceanul Pacific", "Oceanul Indian", "Oceanul Arctic"], "Atlanticul e la vest; Arcticul la nord.")
    P.a(1, "2.1", "Ce ocean scaldă Europa la nord?", "Oceanul Arctic", ["Oceanul Indian", "Oceanul Atlantic", "Oceanul Pacific"], "Marea Barents și Marea Albă țin de Oceanul Arctic.")
    P.a(2, "2.1", "Pe unde trece granița convențională dintre Europa și Asia?", "Munții Ural, râul Ural, Marea Caspică, Munții Caucaz", ["Munții Alpi și Dunărea", "Marea Mediterană", "Munții Pirinei"], "Granița de est nu e marcată de un ocean.")
    P.a(2, "2.1", "Care e cea mai mare peninsulă a Europei?", "Peninsula Scandinavă", ["Peninsula Italică", "Peninsula Iberică", "Peninsula Balcanică"], "Pe ea se află Norvegia și Suedia.")
    P.a(2, "2.1", "Care e cea mai mare insulă a Europei?", "Marea Britanie", ["Sicilia", "Creta", "Corsica"], "Marea Britanie e cea mai mare insulă europeană (fără Groenlanda, care ține de America de Nord).")
    P.e(2, "2.1", "Pune pe hartă numele peninsulelor.", [("sc", "Peninsula Scandinavă", 64, 15), ("ib", "Peninsula Iberică", 40, -4), ("it", "Peninsula Italică", 42.5, 13), ("bal", "Peninsula Balcanică", 42, 22)], "Scandinavă la nord, Iberică la sud-vest, Italică în centrul sudului, Balcanică la sud-est.", harta="lume")
    P.p(2, "2.1", "Atinge pe hartă Peninsula Iberică.", "lume", 40, -4, "Peninsula Iberică", 500, "Pe ea se află Spania și Portugalia.")
    P.p(2, "2.1", "Atinge pe hartă Peninsula Italică.", "lume", 42.5, 13, "Peninsula Italică", 400, "Peninsula Italică are forma unei cizme.")
    P.p(2, "2.1", "Atinge pe hartă Islanda.", "lume", 64.9, -18.6, "Islanda", 400, "Islanda e în nordul Atlanticului.")
    P.p(3, "2.1", "Atinge pe hartă Strâmtoarea Gibraltar.", "lume", 36, -5.5, "Strâmtoarea Gibraltar", 300, "Gibraltar e între Spania și Maroc.")
    P.p(3, "2.1", "Atinge pe hartă Golful Biscaya.", "lume", 45, -4, "Golful Biscaya", 400, "Golful Biscaya e între Franța și Spania.")
    P.a(2, "2.1", "Ce leagă Strâmtoarea Gibraltar?", "Marea Mediterană de Oceanul Atlantic", ["Marea Neagră de Marea Mediterană", "Marea Nordului de Marea Baltică", "Oceanul Arctic de Pacific"], "Gibraltar e „poarta” Mediteranei spre ocean.")
    P.a(2, "2.1", "Ce strâmtoare leagă Marea Neagră de Marea Marmara?", "Bosforul", ["Gibraltar", "Pas de Calais", "Dardanele"], "Istanbulul e pe ambele maluri ale Bosforului.")
    P.a(2, "2.1", "Ce strâmtoare desparte Marea Britanie de Franța?", "Pas de Calais (Canalul Mânecii)", ["Bosfor", "Gibraltar", "Dardanele"], "Pe sub Canalul Mânecii trece un tunel feroviar.")
    P.a(2, "2.1", "În ce emisfere se află Europa?", "în emisfera nordică și în cea mai mare parte în emisfera estică", ["în emisfera sudică", "doar în emisfera vestică", "pe Ecuator"], "Meridianul de 0° trece prin vestul Europei.")
    P.a(2, "3.1", "Ce suprafață are Europa, aproximativ?", "10 milioane km²", ["1 milion km²", "45 de milioane km²", "100 000 km²"], "Europa are aproximativ 10 milioane km²; doar Australia e mai mică.", surse=["Encyclopaedia Britannica – Europe", "Wikipedia – Europe"])
    P.adev(2, "2.2", "Europa e despărțită de Asia printr-un ocean.", False, "Fals: Europa și Asia sunt legate pe uscat (Eurasia).")
    P.adev(2, "2.2", "Țărmurile Europei sunt foarte crestate, cu multe peninsule și golfuri.", True, "Adevărat: de aceea multe țări europene au ieșire la mare.")
    P.l(2, "2.1", "Completează.", "Spania și Portugalia se află în Peninsula [Iberică], iar Norvegia și Suedia în Peninsula [Scandinavă].", ["Balcanică", "Italică"], "Iberică și Scandinavă.")
    P.l(2, "2.2", "Completează.", "O apă îngustă care leagă două mări se numește [strâmtoare]; uscatul înconjurat de apă din toate părțile se numește [insulă].", ["golf", "peninsulă"], "Strâmtoare și insulă.")
    P.d(2, "2.1", "Ce insulă e marcată pe hartă?", "lume", 37.5, 14.2, "Sicilia", ["Sardinia", "Corsica", "Creta"], "Sicilia e la sudul Peninsulei Italice.")
    P.d(3, "2.1", "Ce peninsulă e marcată pe hartă?", "lume", 56, 9.2, "Iutlanda", ["Crimeea", "Peninsula Iberică", "Peninsula Kola"], "Iutlanda e peninsula pe care se află Danemarca.")
    P.o(3, "2.2", "Ordonează aceste țări de la vest la est.", ["Portugalia", "Spania", "Franța", "Germania", "Polonia", "Ucraina"], "De la vest la est", "Pe paralela Europei centrale, de la Atlantic spre est.")
    P.a(3, "3.2", "De ce țărmurile crestate au favorizat comerțul pe mare în Europa?", "pentru că golfurile adăpostite au permis porturi, iar marea e aproape de multe regiuni", ["pentru că apa e dulce", "pentru că nu sunt valuri", "pentru că nu există vânt"], "Multe orașe-port mari: Rotterdam, Hamburg, Marsilia, Genova.")
    P.a(2, "2.1", "Ce mare internă scaldă țărmul României?", "Marea Neagră", ["Marea Nordului", "Marea Baltică", "Marea Adriatică"], "Litoralul românesc are aproximativ 245 km.")
    P.a(2, "2.1", "Ce mare se află între Peninsula Italică și Peninsula Balcanică?", "Marea Adriatică", ["Marea Baltică", "Marea Nordului", "Marea Neagră"], "Adriatica e un braț al Mediteranei.")
    P.a(2, "2.1", "Ce mare e înconjurată de Suedia, Finlanda, Polonia, Germania și Țările Baltice?", "Marea Baltică", ["Marea Neagră", "Marea Egee", "Marea Tireniană"], "Marea Baltică e în nordul Europei.")
    P.a(3, "2.1", "Ce fiorduri sunt cunoscute în Europa?", "golfurile lungi și înguste de pe țărmul Norvegiei, săpate de ghețari", ["deltele din Spania", "dunele din Olanda", "lagunele din Italia"], "Fiordurile sunt văi glaciare inundate de mare.")
    P.a(2, "3.1", "Ce înseamnă „țară fără ieșire la mare” în Europa?", "o țară precum Ungaria, Austria sau Elveția, fără țărm", ["o insulă", "o peninsulă", "o țară cu fiorduri"], "Aceste țări folosesc porturile vecinilor.")

    # ================================================================ S17 Relieful Europei
    R = Lectie(6, "VI-S17-caracteristici-generale-reliefului-unitati", "Relieful Europei – unități majore",
               "Unde sunt cei mai înalți munți ai Europei și unde sunt cele mai întinse câmpii?",
               [("Caracteristici generale", "Europa are o altitudine medie mică, de aproximativ 300 m: predomină câmpiile și podișurile.\nCea mai întinsă e Câmpia Europei de Est (Câmpia Rusă). Câmpia Europei Centrale se întinde din Franța până în Polonia."),
                ("Munții", "Munții tineri, înalți, cu vârfuri ascuțite: Alpii, Pirineii, Apeninii, Carpații, Balcanii, Caucazul.\nCel mai înalt vârf din Alpi e Mont Blanc (aproximativ 4 805 m). Cel mai înalt vârf din Europa e Elbrus (5 642 m), în Munții Caucaz.\nMunții vechi, mai joși, rotunjiți: Uralii, Munții Scandinaviei, Masivul Central Francez."),
                ("Relief vulcanic și glaciar", "Vulcani activi: Etna și Vezuviul (Italia), vulcanii din Islanda.\nGhețarii au modelat munții Scandinaviei și Alpii: văi în formă de U, fiorduri, lacuri glaciare.")],
               stiaica="Etna, din Sicilia, e unul dintre cei mai activi vulcani de pe Pământ și cel mai înalt vulcan activ din Europa.",
               ref=REF.format("Caracteristici generale ale reliefului. Unități majore"))
    R.a(1, "2.1", "Care e cel mai înalt vârf din Europa?", "Elbrus (5 642 m)", ["Mont Blanc", "Moldoveanu", "Olimp"], "Elbrus e în Munții Caucaz.", surse=S_ELBRUS)
    R.a(2, "2.1", "Care e cel mai înalt vârf din Munții Alpi?", "Mont Blanc", ["Elbrus", "Moldoveanu", "Etna"], "Mont Blanc are aproximativ 4 805 m; înălțimea variază puțin cu stratul de gheață.", surse=S_MB)
    R.a(2, "2.1", "Care e cea mai întinsă câmpie din Europa?", "Câmpia Europei de Est", ["Câmpia Padului", "Câmpia Română", "Câmpia Panonică"], "Câmpia Europei de Est ocupă mare parte din Rusia europeană, Ucraina și Belarus.")
    R.a(2, "4.3", "Ce predomină în relieful Europei?", "câmpiile și podișurile", ["munții foarte înalți", "deșerturile", "ghețarii"], "Altitudinea medie a Europei e mică.")
    R.e(2, "2.1", "Pune pe hartă munții Europei.", [("alp", "Alpii", 46.5, 10), ("pir", "Pirineii", 42.7, 0.5), ("car", "Carpații", 47.5, 24), ("ura", "Uralii", 60, 59)], "Alpii în centru, Pirineii între Franța și Spania, Carpații în centrul și estul Europei, Uralii la granița cu Asia.", harta="lume")
    R.p(2, "2.1", "Atinge pe hartă Munții Alpi.", "lume", 46.5, 10, "Alpii", 400, "Alpii sunt în Franța, Elveția, Italia, Austria.")
    R.p(2, "2.1", "Atinge pe hartă Munții Pirinei.", "lume", 42.7, 0.5, "Pirineii", 300, "Pirineii sunt granița dintre Franța și Spania.")
    R.p(3, "2.1", "Atinge pe hartă Munții Caucaz, unde e vârful Elbrus.", "lume", 43.3, 42.5, "Munții Caucaz", 400, "Caucazul e între Marea Neagră și Marea Caspică.", surse=S_ELBRUS)
    R.p(3, "2.1", "Atinge pe hartă Munții Ural.", "lume", 60, 59, "Uralii", 800, "Uralii sunt în Rusia, la granița cu Asia.")
    R.s(2, "4.3", "Asociază munții cu tipul lor.", [("Alpii", "munți tineri, înalți"), ("Uralii", "munți vechi, joși"), ("Carpații", "munți tineri"), ("Munții Scandinaviei", "munți vechi, modelați de ghețari")], "Munții tineri sunt înalți și ascuțiți; cei vechi, tociți de eroziune.")
    R.a(2, "4.3", "Prin ce se deosebesc munții tineri de munții vechi?", "munții tineri sunt mai înalți, cu vârfuri ascuțite; cei vechi sunt mai joși și rotunjiți", ["munții vechi sunt mai înalți", "nu e nicio diferență", "munții tineri sunt sub mare"], "Eroziunea a tocit munții vechi în milioane de ani.")
    R.a(2, "2.1", "Ce munți sunt granița dintre Franța și Spania?", "Pirineii", ["Alpii", "Apeninii", "Balcanii"], "Pirineii despart Peninsula Iberică de restul Europei.")
    R.a(2, "2.1", "Ce munți străbat Peninsula Italică de la nord la sud?", "Apeninii", ["Alpii", "Uralii", "Pirineii"], "Apeninii sunt „coloana vertebrală” a Italiei.")
    R.a(2, "2.1", "Ce vulcan activ se află în Sicilia?", "Etna", ["Vezuviul", "Elbrus", "Olimp"], "Etna e cel mai înalt vulcan activ din Europa.")
    R.d(2, "2.1", "Ce vulcan, lângă Napoli, a distrus orașul Pompei în anul 79?", "lume", 40.82, 14.43, "Vezuviul", ["Etna", "Stromboli", "Hekla"], "Vezuviul a acoperit Pompeiul cu cenușă.")
    R.a(2, "2.1", "În ce țară sunt numeroși vulcani activi, pe dorsala medio-atlantică?", "Islanda", ["Polonia", "Ungaria", "Belgia"], "Islanda e o insulă vulcanică.")
    R.a(2, "2.1", "Ce câmpie e străbătută de râul Pad, în nordul Italiei?", "Câmpia Padului", ["Câmpia Panonică", "Câmpia Română", "Câmpia Europei de Est"], "Câmpia Padului e foarte fertilă și populată.")
    R.a(2, "2.1", "Ce câmpie se află în Ungaria, în bazinul mijlociu al Dunării?", "Câmpia Panonică", ["Câmpia Padului", "Câmpia Română", "Câmpia Andaluziei"], "Câmpia Panonică e înconjurată de Alpi, Carpați și Dinarici.")
    R.adev(2, "4.3", "Carpații sunt munți tineri, ca Alpii.", True, "Adevărat: s-au format în aceeași perioadă cu Alpii.")
    R.adev(2, "4.3", "Uralii sunt cei mai înalți munți din Europa.", False, "Fals: Uralii sunt munți vechi și relativ joși; cei mai înalți sunt Caucazul și Alpii.")
    R.l(2, "2.1", "Completează.", "Cel mai înalt vârf din Europa este [Elbrus], în Munții [Caucaz].", ["Mont Blanc", "Alpi"], "Elbrus, Caucaz.")
    R.l(2, "4.3", "Completează.", "Fiordurile din Norvegia sunt văi săpate de [ghețari] și apoi inundate de [mare].", ["vânt", "lavă"], "Relief glaciar.")
    R.o(2, "4.3", "Ordonează vârfurile de la cel mai înalt la cel mai jos.", ["Elbrus (5 642 m)", "Mont Blanc (aproximativ 4 805 m)", "Olimp (2 918 m)", "Moldoveanu (2 544 m)"], "Altitudine, descrescător", "Elbrus, Mont Blanc, Olimp, Moldoveanu.", surse=S_ELBRUS)
    R.g(3, "2.3 4.1", "Graficul arată altitudinea unor vârfuri din Europa. Cu cât e mai înalt Elbrus decât Moldoveanu?", grafic("bare", "Altitudinea unor vârfuri din Europa", [("Elbrus", 5642), ("Mont Blanc", 4805), ("Olimp", 2918), ("Moldoveanu", 2544)], "m", "Encyclopaedia Britannica"), "cu 3 098 m", ["cu 2 544 m", "cu 837 m", "cu 5 642 m"], "5 642 − 2 544 = 3 098 m.", surse=S_ELBRUS)
    R.a(3, "3.2", "De ce Europa are o altitudine medie mică?", "pentru că predomină câmpiile și podișurile, iar munții înalți ocupă suprafețe mici", ["pentru că nu are munți", "pentru că e sub nivelul mării", "pentru că e acoperită de gheață"], "Câmpiile mari scad media.")
    R.a(2, "2.1", "Ce munți separă Europa de Asia?", "Uralii", ["Alpii", "Pirineii", "Carpații"], "Uralii sunt o graniță convențională.")
    R.a(3, "3.2", "Unde e cel mai jos punct al Europei?", "țărmul Mării Caspice, sub nivelul oceanului", ["vârful Elbrus", "Delta Dunării, la 500 m", "Câmpia Padului, la 2 000 m"], "Nivelul Mării Caspice e la aproximativ 28 m sub nivelul oceanului.")
    R.a(2, "2.1", "Ce munți se află în centrul Peninsulei Balcanice, în Bulgaria?", "Munții Balcani", ["Munții Ural", "Munții Alpi", "Munții Pirinei"], "Balcanii au dat numele peninsulei.")
    R.d(2, "2.1", "Ce peninsulă muntoasă, cu Apeninii, e marcată pe hartă?", "lume", 42.5, 13, "Peninsula Italică", ["Peninsula Iberică", "Peninsula Balcanică", "Peninsula Scandinavă"], "Peninsula Italică e străbătută de Apenini.")
    R.a(3, "3.2", "De ce Alpii au mulți ghețari, iar Carpații nu?", "pentru că Alpii sunt mult mai înalți, deci mai reci la vârf", ["pentru că Alpii sunt mai la sud", "pentru că în Carpați plouă mai mult", "pentru că Alpii sunt vulcani"], "Altitudinea decide dacă zăpada rezistă vara.")

    # ================================================================ S18 Hidrografia Europei
    H = Lectie(6, "VI-S18-hidrografia", "Hidrografia Europei",
               "Care e cel mai lung fluviu al Europei: Dunărea sau Volga?",
               [("Fluviile", "Cel mai lung fluviu din Europa e Volga (aproximativ 3 530 km), care se varsă în Marea Caspică. Al doilea e Dunărea (2 857 km), care izvorăște din Munții Pădurea Neagră (Germania) și se varsă în Marea Neagră, prin Delta Dunării.\nAlte fluvii: Rinul (Alpi → Marea Nordului), Sena, Loara, Elba, Vistula, Nipru, Tamisa."),
                ("Lacurile", "Lacuri glaciare: Ladoga și Onega (Rusia, cele mai mari lacuri din Europa), lacurile din Finlanda (numită „țara celor o mie de lacuri”), lacurile din Alpi (Geneva, Constanța, Garda).\nLacuri tectonice: Balaton (Ungaria). Lacuri de acumulare: Porțile de Fier (pe Dunăre)."),
                ("Mările și oceanele", "Mări ale Oceanului Atlantic: Marea Nordului, Marea Baltică, Marea Mediterană (cu Marea Adriatică, Marea Egee), Marea Neagră. Mări ale Oceanului Arctic: Marea Barents, Marea Albă.")],
               stiaica="Dunărea trece prin zece țări și prin patru capitale: Viena, Bratislava, Budapesta și Belgrad. Niciun alt fluviu din lume nu trece prin atâtea țări.",
               ref=REF.format("Hidrografia"))
    H.a(1, "2.1", "Care e cel mai lung fluviu din Europa?", "Volga", ["Dunărea", "Rinul", "Sena"], "Volga are aproximativ 3 530 km.", surse=S_VOLGA)
    H.a(2, "2.1", "Unde se varsă Volga?", "în Marea Caspică", ["în Marea Neagră", "în Marea Baltică", "în Oceanul Atlantic"], "Volga e cel mai lung fluviu din lume care se varsă într-un lac.", surse=S_VOLGA)
    H.a(1, "2.1", "Unde se varsă Dunărea?", "în Marea Neagră", ["în Marea Nordului", "în Marea Caspică", "în Marea Mediterană"], "Dunărea formează Delta Dunării.")
    H.a(2, "2.1", "Unde izvorăște Dunărea?", "în Munții Pădurea Neagră, din Germania", ["în Carpați", "în Alpi, în Elveția", "în Munții Ural"], "Izvoarele Dunării sunt în sud-vestul Germaniei.", surse=S_DUNARE)
    H.a(2, "3.1", "Prin câte țări trece Dunărea?", "zece", ["două", "patru", "douăzeci"], "Germania, Austria, Slovacia, Ungaria, Croația, Serbia, România, Bulgaria, Republica Moldova, Ucraina.", surse=S_DUNARE)
    H.o(3, "2.2", "Ordonează țările prin care trece Dunărea, de la izvor spre vărsare.", ["Germania", "Austria", "Slovacia", "Ungaria", "Serbia", "România"], "De la izvor spre vărsare", "Dunărea curge de la vest spre est.", surse=S_DUNARE)
    H.o(3, "2.2", "Ordonează capitalele de pe Dunăre, de la izvor spre vărsare.", ["Viena", "Bratislava", "Budapesta", "Belgrad"], "În sensul curgerii", "Viena, Bratislava, Budapesta, Belgrad.", surse=S_DUNARE)
    H.a(2, "2.1", "Unde se varsă Rinul?", "în Marea Nordului", ["în Marea Neagră", "în Marea Mediterană", "în Marea Caspică"], "Rinul izvorăște din Alpi și se varsă prin Țările de Jos.")
    H.s(2, "2.1", "Asociază râul cu orașul așezat pe el.", [("Sena", "Paris"), ("Tamisa", "Londra"), ("Tibru", "Roma"), ("Vistula", "Varșovia")], "Capitale pe râuri.")
    H.p(2, "2.1", "Atinge pe hartă vărsarea Volgăi în Marea Caspică.", "lume", 46, 48, "Delta Volgăi", 500, "Delta Volgăi e la nordul Mării Caspice.")
    H.p(2, "2.1", "Atinge pe hartă vărsarea Rinului.", "lume", 51.9, 4.1, "vărsarea Rinului", 300, "Rinul se varsă în Marea Nordului lângă Rotterdam.")
    H.p(3, "2.1", "Atinge pe hartă Lacul Ladoga.", "lume", 61, 31.5, "Lacul Ladoga", 300, "Ladoga e în nord-vestul Rusiei, lângă Sankt Petersburg.")
    H.a(2, "2.1", "Care e cel mai mare lac din Europa?", "Lacul Ladoga", ["Lacul Balaton", "Lacul Geneva", "Lacul Garda"], "Ladoga e în Rusia (Marea Caspică e considerată separat).")
    H.a(2, "2.1", "Ce țară e numită „țara celor o mie de lacuri”?", "Finlanda", ["Spania", "Grecia", "Portugalia"], "Finlanda are zeci de mii de lacuri glaciare.")
    H.a(2, "2.1", "Ce lac mare se află în Ungaria?", "Balaton", ["Ladoga", "Onega", "Garda"], "Balatonul e cel mai mare lac din Europa Centrală.")
    H.a(2, "3.2", "De ce Finlanda are atât de multe lacuri?", "pentru că ghețarii au săpat multe adâncituri care s-au umplut cu apă", ["pentru că plouă tot anul", "pentru că are vulcani", "pentru că e deșert"], "Lacurile finlandeze sunt glaciare.")
    H.a(2, "2.1", "Ce mare desparte Peninsula Scandinavă de restul Europei la sud-est?", "Marea Baltică", ["Marea Neagră", "Marea Adriatică", "Marea Caspică"], "Marea Baltică e aproape închisă, cu apă puțin sărată.")
    H.adev(2, "2.2", "Dunărea e cel mai lung fluviu din Europa.", False, "Fals: e al doilea, după Volga.")
    H.adev(2, "3.2", "Fluviile Europei sunt folosite pentru transport, energie și irigații.", True, "Adevărat: Rinul și Dunărea sunt mari căi navigabile.")
    H.l(2, "2.1", "Completează.", "Volga se varsă în Marea [Caspică], iar Dunărea în Marea [Neagră].", ["Baltică", "Nordului"], "Volga – Caspică; Dunărea – Neagră.")
    H.l(2, "2.1", "Completează.", "Pe Sena se află orașul [Paris], iar pe Tamisa orașul [Londra].", ["Roma", "Viena"], "Paris pe Sena, Londra pe Tamisa.")
    H.g(3, "2.3 4.1", "Graficul arată lungimea unor fluvii europene. Care e al doilea ca lungime?", grafic("bare", "Lungimea unor fluvii europene", [("Volga", 3530), ("Dunărea", 2857), ("Rinul", 1230), ("Sena", 777)], "km", "Encyclopaedia Britannica; ICPDR"), "Dunărea", ["Volga", "Rinul", "Sena"], "Volga e prima, Dunărea a doua.", surse=S_VOLGA)
    H.a(2, "3.2", "Ce face Canalul Dunăre–Marea Neagră pentru vapoare?", "scurtează drumul spre portul Constanța", ["oprește apa Dunării", "duce apa în Carpați", "nu are niciun rol"], "Canalul leagă Dunărea de Constanța.")
    H.a(2, "3.4", "Ce rezervație a biosferei se află la vărsarea Dunării?", "Delta Dunării", ["Lacul Balaton", "Câmpia Padului", "Munții Alpi"], "Delta Dunării e în patrimoniul mondial UNESCO.", surse=S_UNESCO)
    H.d(2, "2.1", "Ce mare e marcată pe hartă?", "lume", 56, 3, "Marea Nordului", ["Marea Baltică", "Marea Neagră", "Marea Mediterană"], "Marea Nordului e între Marea Britanie și Scandinavia.")
    H.a(3, "3.2", "De ce râurile din vestul Europei au apă destul de constantă tot anul?", "pentru că acolo plouă des, tot anul, sub influența oceanului", ["pentru că se topesc ghețari uriași mereu", "pentru că nu plouă deloc", "pentru că sunt îndiguite complet"], "Clima oceanică dă ploi regulate.")
    H.a(3, "3.2", "De ce multe râuri din Rusia îngheață iarna?", "pentru că iernile sunt foarte reci, în clima continentală", ["pentru că sunt prea adânci", "pentru că sunt sărate", "pentru că vin din deșert"], "Clima continentală are ierni geroase.")
    H.a(2, "2.1", "Ce lac se află la granița Elveției cu Franța?", "Lacul Geneva (Leman)", ["Lacul Ladoga", "Lacul Balaton", "Lacul Onega"], "Pe malul lui e orașul Geneva.")
    H.a(2, "2.1", "Ce hidrocentrală mare e construită pe Dunăre, la granița României cu Serbia?", "Porțile de Fier", ["Vidraru", "Bicaz", "Lotru"], "Porțile de Fier e cea mai mare hidrocentrală de pe Dunăre.")
    H.a(2, "2.1", "Ce mare se află între Grecia și Turcia?", "Marea Egee", ["Marea Baltică", "Marea Nordului", "Marea Albă"], "Marea Egee are multe insule.")

    # ================================================================ S19 Clima și vegetația Europei
    C = Lectie(6, "VI-S19-diferentieri-climatice-biogeografice", "Europa – diferențieri climatice și biogeografice",
               "De ce la Londra iernile sunt blânde, iar la Moscova geroase, deși sunt la latitudini apropiate?",
               [("Climatul temperat", "Cea mai mare parte a Europei are climă temperată.\nClimatul temperat oceanic (vestul Europei): ierni blânde, veri răcoroase, ploi tot anul, datorită Oceanului Atlantic și curentului cald Golfstrom.\nClimatul temperat continental (estul Europei): ierni geroase, veri calde, ploi puține.\nClimatul de tranziție (centrul Europei, inclusiv România): între oceanic și continental."),
                ("Alte climate", "Climatul mediteranean (sudul Europei): veri calde și uscate, ierni blânde și ploioase.\nClimatul subpolar și polar (nordul Scandinaviei, Islanda, nordul Rusiei): ierni lungi și foarte reci.\nClimatul montan: pe munții înalți, mai rece și mai umed cu altitudinea."),
                ("Vegetația și fauna", "De la nord la sud: tundra (mușchi, licheni; reni), taigaua (molid, pin; urs brun, lup, râs), pădurile de amestec și de foioase (stejar, fag; căprioară, mistreț), stepa (ierburi; rozătoare), vegetația mediteraneeană (măslin, stejar de plută, chiparos).\nPe munți, vegetația se etajează cu altitudinea.")],
               stiaica="Datorită Golfstromului, în sud-vestul Irlandei și al Marii Britanii cresc chiar și palmieri, deși latitudinea e mai nordică decât a României.",
               ref=REF.format("Diferențieri climatice și biogeografice"))
    C.s(1, "3.2", "Asociază climatul cu regiunea.", [("temperat oceanic", "vestul Europei"), ("temperat continental", "estul Europei"), ("mediteranean", "sudul Europei"), ("subpolar", "nordul Scandinaviei")], "Climatele Europei.")
    C.s(1, "3.2", "Asociază climatul cu caracteristica.", [("oceanic", "ierni blânde, ploi tot anul"), ("continental", "ierni geroase, veri calde, ploi puține"), ("mediteranean", "veri uscate, ierni ploioase"), ("polar", "frig aproape tot anul")], "Fiecare climat are tiparul lui.")
    C.a(1, "3.2", "De ce vestul Europei are ierni blânde?", "datorită Oceanului Atlantic și curentului cald Golfstrom", ["pentru că e mai aproape de Ecuator decât Africa", "pentru că are vulcani", "pentru că nu are munți"], "Oceanul și curentul cald îndulcesc iernile.")
    C.a(2, "3.2", "Ce climat are România?", "temperat de tranziție, cu influențe continentale în est", ["mediteranean", "polar", "ecuatorial"], "România e între influențele oceanice și continentale.")
    C.a(2, "3.2", "Ce climat are sudul Italiei și Grecia?", "mediteranean", ["polar", "continental excesiv", "oceanic rece"], "Veri calde și uscate, ierni blânde.")
    C.a(2, "3.2", "Unde sunt iernile mai geroase?", "la Moscova", ["la Londra", "la Lisabona", "la Roma"], "Moscova are climat continental.")
    C.o(2, "2.2", "Ordonează vegetația Europei de la nord la sud.", ["tundra", "taigaua", "pădurile de foioase", "vegetația mediteraneeană"], "De la nord la sud", "Cu cât mergi spre sud, e mai cald.")
    C.a(2, "3.3", "Ce animal trăiește în tundra din nordul Europei?", "renul", ["cămila", "leul", "flamingoul"], "Renii sunt crescuți de populația sami.")
    C.a(2, "3.3", "Ce copaci domină taigaua?", "coniferele (molid, pin)", ["măslinii", "palmierii", "baobabii"], "Taigaua e pădurea de conifere a nordului.")
    C.a(2, "3.3", "Ce plantă e tipică vegetației mediteraneene?", "măslinul", ["molidul", "mesteacănul pitic", "lichenul de tundră"], "Măslinul suportă verile uscate.")
    C.p(2, "2.1", "Atinge pe hartă o regiune cu tundră: nordul Scandinaviei (Laponia).", "lume", 69, 25, "Laponia", 500, "Laponia e în nordul Norvegiei, Suediei și Finlandei.")
    C.p(3, "2.1", "Atinge pe hartă o regiune cu climat mediteranean: Grecia.", "lume", 39, 22, "Grecia", 400, "Grecia e în sudul Peninsulei Balcanice.")
    C.g(3, "2.3 4.1", "Graficul arată temperatura medie din ianuarie în trei orașe. Ce observi?", grafic("bare", "Temperatura medie în ianuarie (valori aproximative)", [("Londra", 5), ("Berlin", 0), ("Moscova", -7)], "°C", "Meteo – medii climatice 1991–2020 (valori rotunjite)"), "iernile sunt tot mai reci de la vest spre est", ["iernile sunt tot mai calde spre est", "toate au aceeași temperatură", "Londra e cea mai rece"], "Influența oceanului scade spre est.", surse=["Met Office – UK climate averages (Londra)", "Wikipedia – Climate of Moscow / Climate of Berlin"])
    C.adev(2, "3.2", "În climatul mediteranean cele mai multe ploi cad vara.", False, "Fals: vara e uscată; ploile cad mai ales iarna.")
    C.adev(2, "3.2", "Spre est, în Europa, iernile devin mai reci și ploile mai puține.", True, "Adevărat: scade influența Oceanului Atlantic.")
    C.l(2, "3.2", "Completează.", "Curentul cald care îndulcește clima Europei de Vest se numește [Golfstrom]; în est, clima e temperat [continentală].", ["Labrador", "oceanică"], "Golfstrom, continental.")
    C.l(2, "3.3", "Completează.", "Pădurea de conifere din nordul Europei se numește [taiga], iar vegetația de mușchi și licheni se numește [tundră].", ["stepă", "savană"], "Taiga și tundră.")
    C.a(2, "3.3", "Ce vegetație naturală era tipică pentru Ucraina și sudul Rusiei?", "stepa", ["tundra", "taigaua", "pădurea ecuatorială"], "Azi stepa e în mare parte cultivată cu cereale.")
    C.a(3, "3.2", "De ce Alpii au climat montan, deși sunt în centrul Europei?", "pentru că altitudinea mare scade temperatura", ["pentru că sunt la pol", "pentru că sunt lângă Ecuator", "pentru că nu primesc lumină"], "Climatul montan depinde de altitudine.")
    C.a(2, "3.3", "Ce animal mare trăiește în taiga și în Carpați?", "ursul brun", ["ursul polar", "girafa", "cămila"], "Ursul brun trăiește în pădurile de conifere și de amestec.")
    C.a(3, "3.2", "De ce plouă mult pe țărmul vestic al Norvegiei?", "pentru că vânturile umede de pe ocean se lovesc de munți și se răcesc", ["pentru că e deșert", "pentru că e în climat continental", "pentru că nu bate vântul"], "Munții obligă aerul să urce și să se descarce.")
    C.a(2, "4.3", "Compară vara la Atena cu vara la Oslo.", "la Atena e mai caldă și mai uscată", ["la Oslo e mai caldă", "sunt identice", "la Atena ninge vara"], "Atena e mai la sud, în climat mediteranean.")
    C.a(2, "3.3", "Ce culturi agricole sunt tipice zonei mediteraneene?", "măslinul, vița-de-vie, citricele", ["secara și cartoful în tundră", "orezul de munte", "cafeaua"], "Clima caldă și însorită favorizează aceste culturi.")
    C.d(2, "2.1", "Ce oraș cu climat temperat continental e marcat pe hartă?", "lume", 55.75, 37.6, "Moscova", ["Londra", "Paris", "Lisabona"], "Moscova are ierni geroase.")
    C.a(3, "3.3", "De ce în nordul Europei sunt mai puține specii de plante decât în sud?", "pentru că e frig, sezonul de creștere e scurt și solul e sărac", ["pentru că plouă prea puțin", "pentru că e prea cald", "pentru că oamenii le-au tăiat pe toate"], "Biodiversitatea crește spre zonele mai calde.")
    C.a(2, "3.2", "Ce fenomen meteorologic e frecvent iarna în estul Europei?", "viscolul și gerul", ["musonul", "taifunul", "ploaia caldă tropicală"], "Masele de aer rece vin din Siberia.")
    C.a(2, "3.3", "Ce este stejarul de plută?", "un copac mediteraneean din scoarța căruia se face pluta", ["un conifer din taiga", "un mușchi de tundră", "o plantă acvatică"], "Portugalia e cel mai mare producător de plută.")
    C.a(2, "3.2", "Ce climat au Islanda și nordul Rusiei?", "subpolar și polar", ["mediteranean", "tropical", "deșertic cald"], "Iernile sunt foarte lungi și reci.")
    C.a(2, "3.2", "Ce climat are Lisabona, la Atlantic, în sud-vestul Europei?", "mediteranean, cu influențe oceanice", ["polar", "continental excesiv", "subpolar"], "Lisabona are ierni blânde și veri calde, uscate.")
    C.a(3, "4.3", "Ce au în comun climatul montan din Alpi și climatul din nordul Scandinaviei?", "temperaturi scăzute și vegetație de tip alpin sau tundră", ["veri foarte calde", "ploi doar iarna", "lipsa zăpezii"], "Altitudinea și latitudinea au efecte asemănătoare.")

    # ================================================================ S21 Harta politică a Europei
    S = Lectie(6, "VI-S21-oameni-locuri-harta-politica", "Europa – harta politică. State și regiuni",
               "Câte state are Europa și cum le grupăm?",
               [("Statele Europei", "Europa are aproximativ 45 de state independente, de la Rusia (cel mai mare stat din lume, întins și în Asia) până la Vatican (cel mai mic). Există și state mici, numite microstate: Vatican, Monaco, San Marino, Liechtenstein, Andorra, Malta."),
                ("Regiunile Europei", "Pentru studiu, statele se grupează în regiuni geografice: Europa de Nord (Norvegia, Suedia, Finlanda, Danemarca, Islanda, Țările Baltice), Europa de Vest (Franța, Marea Britanie, Irlanda, Belgia, Țările de Jos, Luxemburg), Europa Centrală (Germania, Polonia, Cehia, Slovacia, Ungaria, Austria, Elveția), Europa de Sud (Spania, Portugalia, Italia, Grecia, Malta), Europa de Sud-Est (Balcanii: Bulgaria, Serbia, Croația etc.) și Europa de Est (Rusia, Ucraina, Belarus, Republica Moldova). România e uneori inclusă în Europa Centrală, alteori în Europa de Sud-Est."),
                ("Uniunea Europeană", "Uniunea Europeană (UE) are 27 de state membre, care colaborează economic și politic. Multe folosesc moneda comună euro. România este membră a UE din 2007.")],
               stiaica="Monaco are o suprafață de aproximativ 2 km², dar e unul dintre cele mai dens populate state din lume.",
               ref=REF.format("Oameni și locuri – Harta politică – state și regiuni"))
    S.a(1, "1.1", "Care e cel mai mic stat din Europa (și din lume)?", "Vaticanul", ["Monaco", "Malta", "Luxemburg"], "Vaticanul e în interiorul Romei.")
    S.a(2, "1.1", "Câte state membre are Uniunea Europeană?", "27", ["12", "45", "50"], "UE are 27 de state membre.", surse=S_UE)
    S.a(2, "1.2", "De când este România membră a Uniunii Europene?", "din 2007", ["din 1918", "din 1990", "din 2020"], "România și Bulgaria au aderat la 1 ianuarie 2007.", surse=S_UE)
    S.a(2, "1.1", "Ce este euro?", "moneda comună folosită de multe state ale UE", ["un munte", "o limbă", "un râu"], "România încă folosește leul.")
    S.a(2, "1.1", "Ce sunt microstatele?", "state foarte mici ca suprafață, precum Monaco sau San Marino", ["state cu mulți munți", "state fără capitală", "state insulare mari"], "Microstatele Europei: Vatican, Monaco, San Marino, Liechtenstein, Andorra, Malta.")
    S.s(2, "1.1", "Asociază statul cu regiunea Europei.", [("Norvegia", "Europa de Nord"), ("Franța", "Europa de Vest"), ("Italia", "Europa de Sud"), ("Ucraina", "Europa de Est")], "Regiunile geografice ale Europei.")
    S.s(2, "1.1", "Asociază statul cu capitala.", [("Polonia", "Varșovia"), ("Ungaria", "Budapesta"), ("Bulgaria", "Sofia"), ("Grecia", "Atena")], "Capitale europene.")
    S.s(2, "1.1", "Asociază statul cu capitala.", [("Portugalia", "Lisabona"), ("Austria", "Viena"), ("Suedia", "Stockholm"), ("Republica Moldova", "Chișinău")], "Alte capitale europene.")
    S.a(2, "1.2", "Ce țări sunt vecine cu România?", "Ucraina, Republica Moldova, Bulgaria, Serbia, Ungaria", ["Franța, Italia, Spania", "Polonia, Cehia, Austria", "Grecia, Turcia, Albania"], "România are 5 vecini.")
    S.a(2, "1.2", "Ce microstat e înconjurat complet de Italia, în afară de Vatican?", "San Marino", ["Monaco", "Andorra", "Liechtenstein"], "San Marino e una dintre cele mai vechi republici.")
    S.a(2, "1.2", "Ce microstat se află între Franța și Spania, în Pirinei?", "Andorra", ["Monaco", "Malta", "Liechtenstein"], "Andorra e un stat montan.")
    S.a(1, "1.1", "Care e capitala Germaniei?", "Berlin", ["München", "Viena", "Hamburg"], "Berlin e cel mai mare oraș al Germaniei.")
    S.a(2, "1.1", "Care e capitala Spaniei?", "Madrid", ["Barcelona", "Lisabona", "Sevilla"], "Madrid e în centrul Peninsulei Iberice.")
    S.a(2, "1.2", "Ce stat european are teritorii și în Asia?", "Rusia (și Turcia)", ["Franța", "Spania", "Austria"], "Rusia e cel mai mare stat al lumii.")
    S.adev(2, "1.2", "Toate statele Europei sunt membre ale Uniunii Europene.", False, "Fals: de exemplu, Norvegia, Elveția, Marea Britanie și Ucraina nu sunt membre.")
    S.adev(2, "1.2", "România folosește moneda euro.", False, "Fals: România folosește leul.")
    S.l(2, "1.1", "Completează.", "Uniunea Europeană are [27] de state membre; România a aderat în anul [2007].", ["45", "1990"], "27 de state; 2007.", surse=S_UE)
    S.l(2, "1.1", "Completează.", "Capitala Franței este [Paris], iar capitala Marii Britanii este [Londra].", ["Berlin", "Dublin"], "Paris și Londra.")
    S.a(2, "1.2", "Ce țară a ieșit din Uniunea Europeană în 2020?", "Regatul Unit (Marea Britanie)", ["Franța", "Germania", "Italia"], "Ieșirea Regatului Unit din UE e cunoscută ca Brexit.")
    S.a(2, "1.1", "Care e capitala Țărilor de Jos?", "Amsterdam", ["Bruxelles", "Rotterdam", "Copenhaga"], "Guvernul are sediul la Haga, dar capitala oficială e Amsterdam.")
    S.a(2, "1.1", "În ce oraș se află multe instituții ale Uniunii Europene?", "Bruxelles (Belgia)", ["Madrid", "Varșovia", "București"], "Comisia Europeană are sediul la Bruxelles.")
    S.a(3, "1.2", "De ce statele UE folosesc o monedă comună?", "pentru a ușura comerțul și călătoriile între ele", ["pentru că au aceeași limbă", "pentru că au aceeași climă", "pentru că sunt pe același munte"], "Fără schimb valutar, comerțul e mai simplu.")
    S.a(2, "1.1", "Care e capitala Italiei?", "Roma", ["Milano", "Napoli", "Veneția"], "Roma e pe râul Tibru.")
    S.a(2, "1.2", "Ce stat insular din Mediterana e membru al UE?", "Malta", ["Islanda", "Norvegia", "Elveția"], "Malta și Cipru sunt state insulare membre.")
    S.a(2, "1.1", "Care e capitala Norvegiei?", "Oslo", ["Stockholm", "Helsinki", "Copenhaga"], "Oslo e la capătul unui fiord.")
    S.a(2, "1.2", "Ce țări formează Țările Baltice?", "Estonia, Letonia, Lituania", ["Suedia, Norvegia, Danemarca", "Polonia, Cehia, Slovacia", "Spania, Portugalia, Andorra"], "Sunt pe țărmul estic al Mării Baltice.")
    S.a(2, "1.1", "Care e capitala Ucrainei?", "Kiev", ["Odesa", "Harkov", "Lvov"], "Kievul e pe Nipru.")
    S.a(3, "1.2", "De ce granițele din Europa s-au schimbat de multe ori?", "din cauza războaielor, a unirilor și a destrămării unor state", ["din cauza vulcanilor", "din cauza mareelor", "nu s-au schimbat niciodată"], "De exemplu, în secolul XX s-au destrămat URSS, Iugoslavia și Cehoslovacia.")
    S.a(2, "1.1", "Care e capitala Elveției?", "Berna", ["Zürich", "Geneva", "Basel"], "Berna e capitala federală.")
    S.a(2, "1.1", "Care e capitala Cehiei?", "Praga", ["Brno", "Bratislava", "Budapesta"], "Praga e pe râul Vltava.")

    # ================================================================ S22 Populația Europei
    Q = Lectie(6, "VI-S22-raspandirea-geografica-populatiei-elemente", "Populația Europei – răspândire și diversitate",
               "Câte limbi se vorbesc în Europa?",
               [("Numărul și răspândirea", "În Europa trăiesc peste 740 de milioane de oameni, după estimările ONU. Populația e mai densă în vestul și centrul continentului (Țările de Jos, Belgia, Marea Britanie, Germania, nordul Italiei) și mai rară în nord (Scandinavia, nordul Rusiei).\nÎn multe țări europene se nasc puțini copii, iar populația îmbătrânește."),
                ("Diversitatea etnică și lingvistică", "Europa are multe popoare și limbi. Cele mai mari familii de limbi sunt: limbile romanice (română, italiană, franceză, spaniolă, portugheză), germanice (germană, engleză, olandeză, suedeză, norvegiană, daneză) și slave (rusă, ucraineană, poloneză, cehă, bulgară, sârbă). Mai există: maghiara, finlandeza, estona, greaca, albaneza, limbile baltice, limbile celtice."),
                ("Diversitatea religioasă și culturală", "Cea mai mare parte a europenilor sunt creștini: ortodocși (mai ales în est și sud-est), catolici (mai ales în sud și centru), protestanți (mai ales în nord). Există și comunități de musulmani, evrei și alte religii, precum și persoane fără religie.\nFiecare popor are tradiții, sărbători, muzică și bucătărie proprii.")],
               stiaica="Româna e o limbă romanică, înrudită cu italiana, franceza, spaniola și portugheza, toate provenite din latină.",
               ref=REF.format("Răspândirea geografică a populației. Elemente de diversitate umană"))
    Q.a(2, "2.3", "Câți locuitori are Europa, aproximativ?", "peste 740 de milioane", ["7,4 milioane", "7,4 miliarde", "74 de milioane"], "Europa are peste 740 de milioane de locuitori, după ONU.", surse=S_EUPOP)
    Q.a(2, "2.2", "Unde e mai densă populația Europei?", "în vest și centru", ["în nordul Scandinaviei", "în nordul Rusiei", "pe vârfurile Alpilor"], "Țările de Jos și Belgia sunt foarte dens populate.")
    Q.a(2, "2.2", "De ce nordul Scandinaviei e slab populat?", "din cauza climei reci și a solurilor sărace", ["pentru că e deșert cald", "pentru că e prea plat", "pentru că e lângă Ecuator"], "Frigul limitează locuirea.")
    Q.s(2, "2.2", "Asociază limba cu familia ei.", [("româna", "romanică"), ("germana", "germanică"), ("poloneza", "slavă"), ("maghiara", "fino-ugrică")], "Familiile de limbi ale Europei.")
    Q.s(2, "2.2", "Asociază limba cu familia ei.", [("spaniola", "romanică"), ("suedeza", "germanică"), ("bulgara", "slavă"), ("finlandeza", "fino-ugrică")], "Altă serie de limbi.")
    Q.a(1, "2.2", "Din ce limbă provine limba română?", "din latină", ["din greacă", "din germană", "din rusă"], "Româna e o limbă romanică.")
    Q.a(2, "2.2", "Ce limbă e înrudită cu româna?", "italiana", ["maghiara", "rusa", "finlandeza"], "Ambele sunt limbi romanice.")
    Q.a(2, "2.2", "Ce religie e majoritară în România?", "creștinismul ortodox", ["islamul", "budismul", "hinduismul"], "Majoritatea românilor sunt ortodocși.")
    Q.s(2, "2.2", "Asociază confesiunea creștină cu regiunea în care e majoritară.", [("ortodoxă", "estul și sud-estul Europei"), ("catolică", "sudul și centrul Europei"), ("protestantă", "nordul Europei")], "Repartiția confesiunilor creștine.")
    Q.a(2, "2.2", "Ce înseamnă că populația unei țări „îmbătrânește”?", "crește proporția persoanelor vârstnice, pentru că se nasc puțini copii", ["oamenii se nasc bătrâni", "dispar școlile", "crește natalitatea"], "E o problemă comună multor țări europene.")
    Q.p(2, "2.1", "Atinge pe hartă Țările de Jos, una dintre cele mai dens populate țări europene.", "lume", 52.2, 5.3, "Țările de Jos", 300, "Țările de Jos au o densitate foarte mare.")
    Q.p(3, "2.1", "Atinge pe hartă Finlanda, unde se vorbește o limbă fino-ugrică.", "lume", 63, 26, "Finlanda", 500, "Finlanda e în nordul Europei.")
    Q.adev(2, "2.2", "Toți europenii vorbesc aceeași limbă.", False, "Fals: în Europa se vorbesc zeci de limbi.")
    Q.adev(2, "2.2", "Maghiara nu e o limbă slavă și nici romanică.", True, "Adevărat: maghiara e o limbă fino-ugrică.")
    Q.l(2, "2.2", "Completează.", "Româna, italiana și franceza sunt limbi [romanice]; rusa și poloneza sunt limbi [slave].", ["germanice", "celtice"], "Romanice și slave.")
    Q.l(2, "2.3", "Completează.", "Europa are peste 740 de [milioane] de locuitori; populația e mai densă în [vest] și centru.", ["miliarde", "nord"], "Peste 740 de milioane.", surse=S_EUPOP)
    Q.g(3, "2.3 4.1", "Graficul arată densitatea populației în trei țări (valori rotunjite). Care e cea mai dens populată?", grafic("bare", "Densitatea populației (valori rotunjite)", [("Țările de Jos", 520), ("România", 80), ("Norvegia", 15)], "loc./km²", "Eurostat / Banca Mondială"), "Țările de Jos", ["România", "Norvegia", "sunt egale"], "Țările de Jos au peste 500 loc./km²; Norvegia doar aproximativ 15.", surse=["Banca Mondială – Population density (people per sq. km)", "Eurostat – Population density"])
    Q.a(2, "2.2", "Ce sărbătoare e comună multor popoare creștine din Europa?", "Crăciunul", ["Diwali", "Anul Nou Chinezesc", "Ramadanul"], "Crăciunul se sărbătorește în toată Europa creștină.")
    Q.a(3, "2.2", "De ce în multe orașe europene trăiesc oameni din țări foarte diferite?", "din cauza migrației pentru muncă, studii sau siguranță", ["pentru că nu există granițe deloc", "pentru că toți vorbesc româna", "pentru că așa e obligatoriu"], "Migrația crește diversitatea orașelor.")
    Q.a(2, "2.2", "Ce limbă e oficială în mai multe țări europene: Germania, Austria, Elveția, Liechtenstein?", "germana", ["franceza", "italiana", "olandeza"], "Germana e cea mai vorbită limbă maternă din UE.")
    Q.a(2, "2.2", "Ce limbă se vorbește în Republica Moldova, ca limbă oficială?", "româna", ["rusa", "ucraineana", "bulgara"], "Limba oficială a Republicii Moldova este limba română.")
    Q.a(2, "2.2", "Ce stat european are patru limbi oficiale?", "Elveția (germană, franceză, italiană, romanșă)", ["Portugalia", "Polonia", "Grecia"], "Elveția e un exemplu de diversitate lingvistică.")
    Q.a(3, "2.3", "Ce este o piramidă a vârstelor?", "un grafic care arată câți bărbați și câte femei sunt pe grupe de vârstă", ["o clădire veche", "o formă de relief", "o hartă a orașelor"], "Piramida arată îmbătrânirea populației.")
    Q.a(2, "2.2", "Ce minorități naționale trăiesc în România?", "maghiari, romi, ucraineni, germani, turci, tătari, lipoveni și altele", ["doar germani", "nicio minoritate", "doar francezi"], "România e o țară cu diversitate etnică.")
    Q.a(2, "2.2", "Ce limbă e cel mai des învățată ca limbă străină în Europa?", "engleza", ["latina", "greaca veche", "islandeza"], "Engleza e folosită larg în comunicarea internațională.")
    Q.d(2, "2.1", "Ce țară dens populată, cu capitala la Londra, e marcată pe hartă?", "lume", 52.5, -1.5, "Regatul Unit", ["Irlanda", "Islanda", "Norvegia"], "Regatul Unit e pe insula Marea Britanie și în nordul Irlandei.")
    Q.a(3, "2.2", "De ce diversitatea culturală e o bogăție?", "pentru că oamenii învață unii de la alții tradiții, idei, limbi și artă", ["pentru că produce conflicte obligatoriu", "pentru că face toți oamenii la fel", "nu e o bogăție"], "Respectul pentru diversitate ne face mai bogați.")
    Q.a(2, "2.2", "Ce alfabet folosesc bulgarii, rușii și sârbii?", "alfabetul chirilic", ["alfabetul latin doar", "alfabetul arab", "hieroglife"], "Alfabetul chirilic e folosit de mai multe popoare slave.")
    Q.a(2, "2.2", "Ce limbă romanică se vorbește în Portugalia și în Brazilia?", "portugheza", ["spaniola", "italiana", "franceza"], "Portugheza a ajuns în Brazilia prin colonizare.")
    Q.a(2, "2.2", "Ce alfabet folosește limba greacă?", "alfabetul grecesc", ["alfabetul chirilic", "alfabetul arab", "alfabetul chinezesc"], "Alfabetul grecesc e unul dintre cele mai vechi.")

    # ================================================================ S23 Mari orașe europene
    O = Lectie(6, "VI-S23-mari-orase-europene", "Mari orașe europene",
               "Ce oraș european ai vrea să vizitezi și de ce?",
               [("Orașele Europei", "Europa are multe orașe mari și foarte vechi. Printre cele mai populate sunt Moscova, Londra, Paris, Madrid, Berlin, Roma. Istanbulul, întins pe două continente, e cel mai mare oraș de la granița Europei cu Asia.\nMulte orașe s-au dezvoltat pe râuri sau pe țărmuri: Londra pe Tamisa, Paris pe Sena, Lisabona la vărsarea Tejo."),
                ("Funcțiile orașelor", "Capitalele au funcție politică și administrativă. Unele orașe sunt mari porturi (Rotterdam, Hamburg, Marsilia), altele centre financiare (Londra, Frankfurt, Zürich), universitare (Oxford, Cambridge, Bologna), culturale și turistice (Paris, Roma, Veneția, Florența, Praga)."),
                ("Patrimoniul orașelor", "Multe orașe au centre istorice înscrise în patrimoniul mondial UNESCO: Roma, Florența, Veneția, Praga, Viena, Budapesta, Sighișoara.\nAcropole din Atena, Colosseumul din Roma, catedrala Notre-Dame din Paris, Sagrada Família din Barcelona sunt simboluri ale Europei.")],
               stiaica="Veneția e construită pe aproximativ 118 insule mici, legate prin poduri; în loc de străzi, are canale.",
               ref=REF.format("Mari orașe europene"))
    O.s(2, "3.4", "Asociază orașul cu simbolul lui.", [("Paris", "Turnul Eiffel"), ("Roma", "Colosseumul"), ("Atena", "Acropole"), ("Londra", "Big Ben")], "Simboluri ale orașelor europene.")
    O.s(2, "3.2", "Asociază orașul cu funcția lui principală.", [("Rotterdam", "mare port maritim"), ("Frankfurt", "centru financiar"), ("Oxford", "oraș universitar"), ("Veneția", "oraș turistic")], "Orașele au funcții diferite.")
    O.a(2, "3.2", "Pe ce râu se află Londra?", "Tamisa", ["Sena", "Rin", "Dunărea"], "Londra e pe Tamisa.")
    O.a(2, "3.2", "Ce oraș e construit pe insule și are canale în loc de străzi?", "Veneția", ["Viena", "Madrid", "Varșovia"], "Veneția e în nord-estul Italiei.")
    O.a(2, "3.2", "Ce oraș se întinde pe două continente, Europa și Asia?", "Istanbul", ["Atena", "Moscova", "Sofia"], "Istanbulul e pe ambele maluri ale Bosforului.")
    O.a(2, "3.4", "În ce oraș se află Sagrada Família, biserica proiectată de Antoni Gaudí?", "Barcelona", ["Madrid", "Lisabona", "Roma"], "Lucrările lui Gaudí sunt în patrimoniul UNESCO.", surse=S_UNESCO)
    O.a(2, "3.2", "Care e cel mai mare port al Europei?", "Rotterdam", ["Constanța", "Veneția", "Praga"], "Rotterdam e la vărsarea Rinului.")
    O.a(2, "3.4", "Ce oraș din România are centrul istoric în patrimoniul UNESCO?", "Sighișoara", ["Ploiești", "Galați", "Râmnicu Sărat"], "Centrul istoric al Sighișoarei e înscris în patrimoniul UNESCO.", surse=S_UNESCO)
    O.p(1, "3.1", "Atinge pe hartă Paris.", "lume", 48.86, 2.35, "Paris", 250, "Parisul e în nordul Franței, pe Sena.")
    O.p(2, "3.1", "Atinge pe hartă Londra.", "lume", 51.5, -0.12, "Londra", 250, "Londra e în sud-estul Angliei.")
    O.p(2, "3.1", "Atinge pe hartă Roma.", "lume", 41.9, 12.5, "Roma", 250, "Roma e în centrul Italiei.")
    O.p(2, "3.1", "Atinge pe hartă Madrid.", "lume", 40.4, -3.7, "Madrid", 250, "Madrid e în centrul Spaniei.")
    O.p(3, "3.1", "Atinge pe hartă Moscova.", "lume", 55.75, 37.6, "Moscova", 300, "Moscova e în vestul Rusiei.")
    O.p(3, "3.1", "Atinge pe hartă Viena.", "lume", 48.2, 16.37, "Viena", 200, "Viena e capitala Austriei, pe Dunăre.")
    O.a(2, "3.3", "Ce probleme au marile orașe europene?", "trafic aglomerat, poluare, locuințe scumpe", ["lipsa totală de transport", "prea puțini oameni", "lipsa apei potabile peste tot"], "Orașele mari caută soluții: metrou, biciclete, parcuri.")
    O.a(2, "4.3", "Ce soluții au orașe precum Amsterdam sau Copenhaga pentru trafic?", "piste de biciclete și transport public bun", ["mai multe autostrăzi prin centru", "interzicerea bicicletelor", "închiderea metroului"], "Bicicleta e un mijloc de transport important acolo.")
    O.adev(2, "3.2", "Toate capitalele europene sunt orașe-port la mare.", False, "Fals: Madrid, Viena, Berlin, Praga nu sunt la mare.")
    O.adev(2, "3.4", "Centrul istoric al Romei e în patrimoniul mondial UNESCO.", True, "Adevărat: Roma are monumente de peste 2 000 de ani.", surse=S_UNESCO)
    O.l(2, "3.2", "Completează.", "Orașul cu Turnul Eiffel este [Paris], iar orașul cu Colosseumul este [Roma].", ["Londra", "Atena"], "Paris și Roma.")
    O.l(2, "3.2", "Completează.", "Cel mai mare port al Europei este [Rotterdam], la vărsarea râului [Rin].", ["Hamburg", "Sena"], "Rotterdam, Rin.")
    O.d(2, "3.1", "Ce capitală, pe Dunăre, e marcată pe hartă?", "lume", 47.5, 19.04, "Budapesta", ["Viena", "Belgrad", "Praga"], "Budapesta e capitala Ungariei, pe ambele maluri ale Dunării.")
    O.d(3, "3.1", "Ce capitală e marcată pe hartă?", "lume", 52.52, 13.4, "Berlin", ["Varșovia", "Praga", "Amsterdam"], "Berlinul e în nord-estul Germaniei.")
    O.a(3, "4.2", "Caracterizează pe scurt Parisul.", "capitala Franței, pe Sena, mare centru cultural, turistic și economic", ["port la Marea Neagră", "oraș minier din Alpi", "sat pescăresc"], "Parisul e unul dintre cele mai vizitate orașe din lume.")
    O.a(2, "3.4", "Ce monument antic se află pe un deal din Atena?", "Acropole (cu Partenonul)", ["Colosseumul", "Big Ben", "Turnul Eiffel"], "Acropole e în patrimoniul UNESCO.", surse=S_UNESCO)
    O.a(2, "3.2", "Ce oraș e capitala Uniunii Europene, în sensul că găzduiește multe instituții?", "Bruxelles", ["Paris", "Berlin", "Roma"], "Comisia Europeană e la Bruxelles.")
    O.o(3, "4.3", "Ordonează orașele de la vest la est.", ["Lisabona", "Madrid", "Paris", "Berlin", "Varșovia", "Moscova"], "De la vest la est", "De la Atlantic spre Rusia.")
    O.a(2, "3.2", "Ce oraș e un mare centru financiar al Europei, pe Tamisa?", "Londra", ["Lisabona", "Atena", "Sofia"], "Londra e unul dintre cele mai importante centre financiare ale lumii.")
    O.a(2, "3.4", "În ce oraș se află Muzeul Luvru, unde e expusă „Mona Lisa”?", "Paris", ["Roma", "Madrid", "Viena"], "Luvrul e cel mai vizitat muzeu de artă din lume.")
    O.a(3, "3.3", "De ce orașele vechi europene au străzi înguste în centru?", "pentru că au fost construite înainte de apariția mașinilor", ["pentru că așa e legea azi", "pentru că nu au bani", "pentru că sunt sate"], "Centrele istorice au fost gândite pentru pietoni și căruțe.")
    O.a(2, "3.2", "Care e cel mai mare oraș al României?", "București", ["Cluj-Napoca", "Timișoara", "Iași"], "București e capitala și cel mai populat oraș.")

    # ================================================================ S24 Resursele naturale ale Europei
    N = Lectie(6, "VI-S24-economia-resursele-naturale-valorificarea", "Europa – resursele naturale",
               "De unde vin gazele naturale cu care se încălzesc casele din Europa?",
               [("Resurse energetice", "Petrol și gaze naturale: în Marea Nordului (Norvegia, Marea Britanie), în Rusia, în România.\nCărbune: în Germania, Polonia, Ucraina, Rusia, România (Valea Jiului).\nEnergie din surse regenerabile: hidroenergie (Norvegia, Alpii, Dunărea), vânt (Danemarca, Germania, Marea Nordului), Soare (Spania, Italia, Grecia), geotermie (Islanda)."),
                ("Resurse minerale", "Minereu de fier: Suedia (Kiruna), Rusia, Ucraina. Bauxită (pentru aluminiu): Grecia, Ungaria. Sare: Polonia, Germania, România.\nRoci de construcție și marmură: Italia (Carrara), Grecia."),
                ("Resursele solului, pădurilor și apelor", "Soluri fertile (cernoziom) în Ucraina, Rusia, Câmpia Română, Câmpia Panonică – mari zone agricole.\nPădurile din Scandinavia, Finlanda, Rusia dau lemn și hârtie.\nMările dau pește (Norvegia, Islanda) și sunt căi de transport.")],
               stiaica="În Islanda, cea mai mare parte a caselor se încălzește cu apă caldă din adâncul pământului, adică cu energie geotermală.",
               ref=REF.format("Economia – Resursele naturale și valorificarea lor"))
    N.s(1, "3.2", "Asociază resursa cu țara în care e importantă.", [("petrolul din Marea Nordului", "Norvegia"), ("minereul de fier de la Kiruna", "Suedia"), ("energia geotermală", "Islanda"), ("marmura de Carrara", "Italia")], "Resurse ale Europei.")
    N.a(1, "3.2", "Unde se exploatează petrol și gaze în nordul Europei?", "în Marea Nordului", ["în Alpi", "în Marea Mediterană, lângă Malta", "în Câmpia Padului"], "Norvegia și Marea Britanie extrag petrol din Marea Nordului.")
    N.a(1, "3.2", "Ce țară produce cea mai mare parte a electricității din hidrocentrale?", "Norvegia", ["Țările de Jos", "Malta", "Danemarca"], "Norvegia are munți și multă apă.")
    N.a(2, "3.2", "Ce țară e cunoscută pentru energia eoliană și turbinele de vânt?", "Danemarca", ["Elveția", "Austria", "Ungaria"], "Danemarca are vânt puternic de pe mare.")
    N.a(2, "3.2", "Ce tip de energie folosește Islanda pentru încălzire?", "energia geotermală", ["energia solară din deșert", "cărbunele", "energia mareelor doar"], "Islanda e o insulă vulcanică.")
    N.a(2, "3.2", "Ce țări din sudul Europei au condiții bune pentru energia solară?", "Spania, Italia, Grecia", ["Norvegia, Finlanda, Islanda", "Irlanda, Scoția", "Țările Baltice"], "În sud sunt multe zile însorite.")
    N.a(2, "3.2", "Ce resursă importantă pentru agricultură au Ucraina și sudul Rusiei?", "solurile de cernoziom, foarte fertile", ["petrolul din Marea Nordului", "ghețarii", "vulcanii"], "Ucraina e un mare producător de cereale.")
    N.a(2, "3.2", "Ce resursă dau pădurile din Finlanda și Suedia?", "lemn și hârtie", ["petrol", "aur", "cafea"], "Industria lemnului e importantă în Scandinavia.")
    N.a(2, "3.4", "Ce resurse are România?", "petrol, gaze naturale, cărbune, sare, păduri, soluri fertile, ape", ["doar aur", "doar cafea", "nicio resursă"], "România are resurse variate.")
    N.p(2, "3.1", "Atinge pe hartă Marea Nordului, unde se extrage petrol.", "lume", 56.5, 3, "Marea Nordului", 400, "Marea Nordului e între Marea Britanie și Norvegia.")
    N.p(3, "3.1", "Atinge pe hartă Islanda, unde se folosește energia geotermală.", "lume", 64.9, -18.6, "Islanda", 400, "Islanda e în nordul Atlanticului.")
    N.adev(2, "3.2", "Europa își produce singură tot petrolul și gazele de care are nevoie.", False, "Fals: multe țări europene importă petrol și gaze.")
    N.adev(2, "3.3", "Energia vântului și a Soarelui crește tot mai mult în Europa.", True, "Adevărat: țările europene investesc în energie regenerabilă.")
    N.l(2, "3.2", "Completează.", "Energia din căldura interioară a Pământului se numește [geotermală]; cea produsă de vânt se numește [eoliană].", ["solară", "nucleară"], "Geotermală și eoliană.")
    N.l(2, "3.2", "Completează.", "Petrolul din nordul Europei se extrage din Marea [Nordului]; minereul de fier se extrage la Kiruna, în [Suedia].", ["Neagră", "Italia"], "Marea Nordului și Suedia.")
    N.g(3, "2.3 4.1", "Graficul arată ponderea energiei regenerabile în electricitatea a trei țări imaginare. Care folosește cel mai mult surse regenerabile?", grafic("bare", "Electricitate din surse regenerabile (țări imaginare)", [("țara A", 90), ("țara B", 25), ("țara C", 50)], "%"), "țara A", ["țara B", "țara C", "sunt egale"], "Țara A produce 90 % din electricitate din surse regenerabile.")
    N.a(3, "3.3", "De ce Europa vrea să folosească mai puțin cărbune?", "pentru că arderea lui poluează aerul și produce mult dioxid de carbon", ["pentru că s-a terminat peste tot", "pentru că e prea ieftin", "pentru că e regenerabil"], "Cărbunele e cel mai poluant combustibil fosil.")
    N.a(2, "3.2", "Ce țări europene au mari bazine de cărbune?", "Germania și Polonia", ["Islanda și Malta", "Portugalia și Grecia", "Danemarca și Irlanda"], "Polonia produce o mare parte din electricitate din cărbune.")
    N.a(2, "3.2", "Ce resursă se exploatează în salinele din Polonia (Wieliczka) și România (Turda, Slănic)?", "sarea", ["aurul", "petrolul", "bauxita"], "Salinele vechi sunt și atracții turistice.")
    N.a(2, "3.2", "Ce țară e cunoscută pentru pescuitul în Atlantic și Marea Nordului?", "Norvegia", ["Austria", "Ungaria", "Elveția"], "Norvegia are coaste lungi și o industrie mare a peștelui.")
    N.a(3, "3.3", "Ce înseamnă „dependența energetică” a unei țări?", "țara importă o mare parte din energia de care are nevoie", ["țara produce prea multă energie", "țara nu folosește energie", "țara exportă tot"], "Dependența de import face țara vulnerabilă la crize.")
    N.d(2, "3.1", "Ce țară, cu multe hidrocentrale și fiorduri, e marcată pe hartă?", "lume", 62, 9, "Norvegia", ["Suedia", "Finlanda", "Danemarca"], "Norvegia e pe coasta de vest a Peninsulei Scandinave.")
    N.a(2, "3.2", "Ce sursă de energie e folosită în Franța pentru cea mai mare parte a electricității?", "energia nucleară", ["cărbunele", "petrolul", "energia geotermală"], "Franța are multe centrale nucleare.")
    N.a(2, "4.3", "Compară Norvegia și Polonia după sursele de energie.", "Norvegia folosește mai ales hidroenergie; Polonia mai ales cărbune", ["ambele folosesc doar Soarele", "Norvegia folosește cărbune, Polonia apă", "sunt identice"], "Resursele naturale decid sursele de energie.")
    N.a(2, "3.2", "Ce resursă a Alpilor e folosită pentru energie?", "apa râurilor de munte, în hidrocentrale", ["petrolul", "cărbunele", "gazele"], "Alpii au multe lacuri de acumulare.")
    N.a(3, "3.2", "De ce Ucraina e numită „grânarul Europei”?", "pentru solurile negre foarte fertile, bune pentru cereale", ["pentru că are multe mori de vânt", "pentru că are multe mine", "pentru că nu are câmpii"], "Cernoziomul face posibile recolte mari.")
    N.a(2, "3.2", "Ce produs se obține din bauxită?", "aluminiul", ["fierul", "sarea", "lemnul"], "Grecia și Ungaria au bauxită.")
    N.a(2, "4.2", "Ce este o centrală eoliană offshore?", "o centrală cu turbine de vânt construită în mare", ["o hidrocentrală pe munte", "o mină de cărbune", "o centrală solară în deșert"], "Marea Nordului are multe parcuri eoliene offshore.")
    N.a(2, "3.4", "Ce lac de acumulare important pe Bistrița e folosit pentru energie în România?", "Lacul Izvorul Muntelui (Bicaz)", ["Lacul Balaton", "Lacul Ladoga", "Lacul Geneva"], "Barajul Bicaz a fost construit în anii '50–'60.")
    N.a(3, "3.3", "Ce poate face Europa ca să depindă mai puțin de importurile de gaze?", "mai multă energie regenerabilă, izolarea clădirilor și economie de energie", ["mai multe centrale pe cărbune fără filtre", "oprirea transportului public", "tăierea pădurilor"], "Eficiența energetică reduce consumul.")

    # ================================================================ S25 Activitățile economice ale Europei
    T = Lectie(6, "VI-S25-activitatile-economice-agricultura-industria", "Europa – agricultura, industria, serviciile",
               "Ce produse fabricate în Europa folosești în fiecare zi?",
               [("Agricultura", "Europa are agricultură modernă, cu randamente mari. Se cultivă cereale (grâu, porumb, orz) în câmpiile mari, cartof și sfeclă de zahăr în centru și nord, viță-de-vie, măslini și citrice în sud.\nSe cresc bovine (Țările de Jos, Franța, Irlanda), porcine (Germania, Spania, Danemarca), ovine (Marea Britanie, România, Spania)."),
                ("Industria", "Industria europeană e foarte dezvoltată: construcții de mașini și automobile (Germania, Franța, Italia, Cehia, România), avioane (Airbus, cu fabrici în Franța și Germania), industrie chimică și farmaceutică (Germania, Elveția), electronică, industrie alimentară, textilă și de mobilă."),
                ("Serviciile", "Serviciile ocupă cea mai mare parte a populației active din Europa: comerț, transporturi, bănci, educație, sănătate, IT.\nEuropa e unul dintre cele mai vizitate continente de turiști. Franța, Spania și Italia sunt printre cele mai vizitate țări din lume. Transportul are rețele dense de autostrăzi, căi ferate de mare viteză (TGV în Franța), porturi și aeroporturi.")],
               stiaica="Primul tren de mare viteză din Europa, TGV-ul francez, a fost pus în circulație în 1981. Azi, astfel de trenuri depășesc 300 km/h.",
               ref=REF.format("Activitățile economice: agricultura, industria, serviciile"))
    T.s(1, "3.2", "Asociază cultura agricolă cu zona Europei.", [("măslinul", "sudul (zona mediteraneeană)"), ("cartoful", "centrul și nordul"), ("grâul", "câmpiile mari"), ("citricele", "sudul (Spania, Italia)")], "Clima decide culturile.")
    T.s(1, "3.2", "Asociază țara cu produsul industrial cunoscut.", [("Germania", "automobile"), ("Elveția", "ceasuri și medicamente"), ("Italia", "modă și mașini sport"), ("Franța", "avioane și parfumuri")], "Fiecare țară are industriile ei.")
    T.a(1, "3.2", "Ce țări europene sunt mari producătoare de vin?", "Franța, Italia, Spania", ["Norvegia, Finlanda, Islanda", "Țările Baltice", "Irlanda și Scoția"], "Vița-de-vie are nevoie de căldură și soare.")
    T.a(2, "3.2", "Ce țară europeană e cel mai mare producător de automobile?", "Germania", ["Malta", "Islanda", "Luxemburg"], "Volkswagen, BMW, Mercedes-Benz sunt mărci germane.")
    T.a(2, "3.2", "În ce domeniu lucrează majoritatea europenilor?", "în servicii", ["în agricultură", "în minerit", "în pescuit"], "Țările dezvoltate au o economie bazată pe servicii.")
    T.a(2, "3.2", "Ce țări europene sunt printre cele mai vizitate de turiști din lume?", "Franța, Spania, Italia", ["Belarus și Moldova", "Islanda și Malta", "Letonia și Estonia"], "Clima, patrimoniul și plajele atrag turiști.")
    T.a(2, "3.2", "Ce este TGV-ul?", "trenul francez de mare viteză", ["un avion", "un vapor", "o autostradă"], "TGV înseamnă tren de mare viteză.")
    T.a(2, "3.2", "Ce companie europeană construiește avioane de pasageri, cu fabrici în Franța și Germania?", "Airbus", ["Dacia", "Nokia", "IKEA"], "Airbus e un proiect european comun.")
    T.a(2, "3.4", "Ce produse agricole sunt importante în România?", "porumb, grâu, floarea-soarelui", ["cafea, cacao, ceai", "banane și ananas", "orez de munte"], "Câmpia Română și Câmpia de Vest sunt mari zone agricole.")
    T.a(2, "3.2", "Ce țară e cunoscută pentru produsele lactate și florile (lalelele)?", "Țările de Jos", ["Grecia", "Portugalia", "Bulgaria"], "Agricultura olandeză e foarte modernă.")
    T.a(2, "3.2", "Ce înseamnă industria farmaceutică?", "producerea medicamentelor", ["producerea mașinilor", "producerea mobilei", "extragerea petrolului"], "Elveția și Germania au mari companii farmaceutice.")
    T.p(2, "3.1", "Atinge pe hartă Germania, principalul producător de automobile din Europa.", "lume", 51, 10.5, "Germania", 400, "Germania e în centrul Europei.")
    T.p(3, "3.1", "Atinge pe hartă Elveția.", "lume", 46.8, 8.2, "Elveția", 200, "Elveția e în Alpi, între Germania, Franța, Italia și Austria.")
    T.adev(2, "3.2", "Agricultura europeană folosește puțini oameni, dar multe mașini.", True, "Adevărat: mecanizarea face agricultura eficientă.")
    T.adev(2, "3.2", "Turismul nu are importanță în economia Europei.", False, "Fals: turismul aduce venituri mari în multe țări.")
    T.l(2, "3.2", "Completează.", "Germania e cunoscută pentru industria de [automobile], iar Elveția pentru [ceasuri].", ["cafea", "petrol"], "Automobile și ceasuri.")
    T.l(2, "3.2", "Completează.", "Cultivarea viței-de-vie se numește [viticultură], iar cultivarea pomilor fructiferi se numește [pomicultură].", ["silvicultură", "piscicultură"], "Viticultură, pomicultură.")
    T.g(3, "2.3 4.1", "Graficul arată structura populației ocupate într-o țară vest-europeană imaginară. Ce domeniu domină?", grafic("structura", "Populația ocupată (țară imaginară)", [("agricultură", 3), ("industrie", 22), ("servicii", 75)], "%"), "serviciile", ["agricultura", "industria", "egal"], "75 % din oameni lucrează în servicii.")
    T.a(3, "3.3", "De ce în Europa de Est agricultura ocupă mai mulți oameni decât în vest?", "pentru că acolo agricultura e mai puțin mecanizată și sunt multe ferme mici", ["pentru că în est nu există orașe", "pentru că în vest nu există câmpii", "pentru că în est e mai cald"], "Mecanizarea diferă între regiuni.")
    T.a(2, "3.2", "Ce țară scandinavă e cunoscută pentru mobilă și design?", "Suedia", ["Grecia", "Spania", "Bulgaria"], "IKEA a fost fondată în Suedia.")
    T.a(2, "3.4", "Ce stațiune românească e cunoscută pentru sporturi de iarnă?", "Poiana Brașov", ["Mamaia", "Eforie", "Sulina"], "Poiana Brașov e în Munții Postăvaru.")
    T.a(2, "3.4", "Ce fabrică românească produce automobile Ford?", "uzina de la Craiova", ["uzina de la Mioveni", "uzina de la Sibiu", "uzina de la Iași"], "Ford produce la Craiova, Dacia la Mioveni.")
    T.a(2, "3.2", "Ce tunel feroviar leagă Marea Britanie de Franța?", "Tunelul de sub Canalul Mânecii", ["Tunelul Gotthard", "Tunelul Mont Blanc", "Tunelul Bosfor"], "Tunelul a fost deschis în 1994.")
    T.a(3, "4.3", "Compară agricultura din Spania cu cea din Finlanda.", "Spania cultivă măslini și citrice; Finlanda are puține culturi, pentru că e frig", ["Finlanda cultivă citrice", "sunt identice", "Spania nu are agricultură"], "Clima face diferența.")
    T.a(2, "3.2", "Ce mijloc de transport e cel mai folosit pentru mărfuri pe distanțe mari între continente?", "transportul maritim, cu vapoare", ["bicicleta", "telefericul", "tramvaiul"], "Vapoarele cu containere transportă cele mai multe mărfuri.")
    T.a(2, "3.2", "Ce înseamnă „servicii financiare”?", "activitatea băncilor, a asigurărilor și a bursei", ["agricultura", "mineritul", "construcția de drumuri"], "Londra și Frankfurt sunt centre financiare.")
    T.d(2, "3.1", "Ce țară, unul dintre cei mai mari producători de măsline, e marcată pe hartă?", "lume", 40, -4, "Spania", ["Portugalia", "Franța", "Italia"], "Spania ocupă cea mai mare parte a Peninsulei Iberice.")
    T.a(3, "3.3", "De ce IT-ul se dezvoltă repede în România?", "pentru că există mulți specialiști bine pregătiți și internet rapid", ["pentru că e cald", "pentru că sunt multe mine", "pentru că sunt mulți munți"], "Cluj-Napoca, București, Iași, Timișoara sunt centre IT.")
    T.a(2, "3.2", "Ce industrie e importantă în Italia, la Milano?", "industria modei și a designului", ["mineritul cărbunelui", "pescuitul de balene", "creșterea renilor"], "Milano e o capitală a modei.")
    T.a(2, "3.2", "Ce animale se cresc mult în Irlanda și Țările de Jos?", "bovinele, pentru lapte și carne", ["cămilele", "renii", "lamele"], "Pajiștile verzi sunt potrivite pentru vaci.")

    # ================================================================ S27 Expediție: state din regiuni diferite
    E = Expeditie(6, "VI-S27-aplicatii-practice-studii-caz", "Expediție: ghidul turistic al Europei",
                  "Dacă ai fi ghid, ce ai arăta despre o țară europeană?",
                  ref=REF.format("Aplicații practice/studii de caz: Caracterizarea unor state din regiuni diferite ale Europei"))
    E.o(1, "4.2", "Ordonează pașii unei caracterizări geografice a unui stat.", ["poziția geografică", "relieful", "clima și apele", "populația și orașele", "economia", "obiective turistice"], "Algoritmul de caracterizare", "De la natural la uman.")
    E.pas("1. Alege țara", "Alege câte un stat din două regiuni diferite ale Europei (de exemplu, Norvegia și Italia). Caracterizarea urmează pașii de mai sus.")
    E.a(2, "4.1", "Ce surse folosești pentru date despre o țară?", "atlasul, manualul, site-uri oficiale (Eurostat, guvernul țării), enciclopedii", ["un comentariu anonim", "o reclamă", "un joc"], "Datele trebuie să aibă sursă și an.")
    E.pas("2. Adună datele", "Folosește atlasul și o sursă de încredere. Pentru fiecare cifră, notează sursa și anul.",
          jurnal="Fă un tabel cu cele două țări: capitală, relief, climă, râuri, populație, ocupații, un obiectiv turistic.")
    E.s(2, "4.2", "Asociază țara cu un element caracteristic.", [("Norvegia", "fiorduri"), ("Italia", "Peninsula Italică și vulcani"), ("Țările de Jos", "diguri și teren sub nivelul mării"), ("Elveția", "Alpi și lacuri")], "Fiecare țară are ceva care o deosebește.")
    E.pas("3. Compară", "Scrie 3 asemănări și 3 deosebiri între cele două țări.",
          jurnal="Notează asemănările și deosebirile.")
    E.pas("4. Broșura", "Realizează o broșură turistică sau o prezentare de 4 diapozitive pentru una dintre țări.",
          jurnal="Fotografiază broșura sau o captură a prezentării.", foto=True)

    # ================================================================ S28 Caracterizarea unor state (I)
    K = Lectie(6, "VI-S28-caracterizarea-geografica-state-cel", "Caracterizarea geografică a unor state (I)",
               "Prin ce se deosebesc Franța, Germania și Norvegia?",
               [("Franța (Europa de Vest)", "Capitala: Paris. Relief: câmpii în nord și vest, Masivul Central în centru, Alpii (Mont Blanc) și Pirineii la granițe. Râuri: Sena, Loara, Rhône. Climă: oceanică în vest, mediteraneeană în sud.\nEconomie: agricultură dezvoltată (grâu, vin), industrie (avioane, automobile, energie nucleară), turism foarte dezvoltat."),
                ("Germania (Europa Centrală)", "Capitala: Berlin. Relief: câmpie în nord, podișuri și munți mijlocii în centru, Alpii în sud. Râuri: Rin, Elba, Dunărea (izvorăște aici).\nEconomie: cea mai mare economie din Europa; automobile, mașini industriale, industrie chimică; porturi mari (Hamburg)."),
                ("Norvegia (Europa de Nord)", "Capitala: Oslo. Relief: munți vechi, modelați de ghețari; țărm cu fiorduri. Climă: oceanică pe țărm, subpolară în nord.\nEconomie: petrol și gaze din Marea Nordului, hidroenergie, pescuit, construcții navale. Norvegia nu e membră a UE.")],
               stiaica="Fiordul Sogne (Sognefjord) din Norvegia pătrunde în uscat peste 200 km.",
               ref=REF.format("Caracterizarea geografică a unor state"))
    K.s(1, "2.1", "Asociază țara cu capitala.", [("Franța", "Paris"), ("Germania", "Berlin"), ("Norvegia", "Oslo")], "Capitalele celor trei state.")
    K.s(1, "2.3", "Asociază țara cu elementul de relief.", [("Franța", "Masivul Central"), ("Germania", "Câmpia Germano-Polonă în nord"), ("Norvegia", "fiordurile")], "Relieful fiecărei țări.")
    K.s(1, "2.3", "Asociază țara cu un râu important.", [("Franța", "Loara"), ("Germania", "Elba"), ("Norvegia", "râuri scurte de munte, cu hidrocentrale")], "Hidrografia.")
    K.s(2, "2.3", "Asociază țara cu o activitate economică importantă.", [("Franța", "energie nucleară și turism"), ("Germania", "automobile"), ("Norvegia", "petrol și pescuit")], "Economia celor trei state.")
    K.p(2, "2.1", "Atinge pe hartă Franța.", "lume", 46.5, 2.5, "Franța", 400, "Franța e în vestul Europei.")
    K.p(2, "2.1", "Atinge pe hartă Germania.", "lume", 51, 10.5, "Germania", 350, "Germania e în centrul Europei.")
    K.p(2, "2.1", "Atinge pe hartă Norvegia.", "lume", 62, 9, "Norvegia", 500, "Norvegia e pe coasta de vest a Peninsulei Scandinave.")
    K.a(2, "2.3", "Ce climat are sudul Franței (Coasta de Azur)?", "mediteranean", ["polar", "continental excesiv", "subpolar"], "Veri calde și uscate.")
    K.a(2, "2.3", "Ce munți se află la granița Franței cu Spania?", "Pirineii", ["Alpii", "Carpații", "Uralii"], "Pirineii sunt la sud-vestul Franței.")
    K.a(2, "2.3", "Ce mare fluviu european izvorăște din Germania?", "Dunărea", ["Volga", "Sena", "Tamisa"], "Dunărea izvorăște din Pădurea Neagră.")
    K.a(2, "2.3", "Ce mare port german e pe Elba?", "Hamburg", ["Rotterdam", "Marsilia", "Constanța"], "Hamburg e unul dintre cele mai mari porturi ale Europei.")
    K.a(2, "2.3", "Ce formă de relief, săpată de ghețari, e tipică Norvegiei?", "fiordul", ["delta", "duna", "vulcanul"], "Fiordurile sunt văi glaciare inundate de mare.")
    K.a(2, "2.3", "Este Norvegia membră a Uniunii Europene?", "nu", ["da, din 1957", "da, din 2007", "da, a fondat-o"], "Norvegia a respins aderarea prin referendum.")
    K.a(2, "2.3", "Ce sursă dă cea mai mare parte a electricității în Norvegia?", "hidrocentralele", ["cărbunele", "centralele nucleare", "petrolul ars în centrale"], "Râurile de munte sunt folosite pentru energie.")
    K.a(2, "2.3", "Ce sursă dă cea mai mare parte a electricității în Franța?", "centralele nucleare", ["cărbunele", "vântul", "geotermia"], "Franța are multe reactoare nucleare.")
    K.a(2, "2.3", "Ce economie e cea mai mare din Europa?", "a Germaniei", ["a Norvegiei", "a Islandei", "a Maltei"], "Germania are cea mai mare economie europeană.")
    K.adev(2, "2.3", "Norvegia are un țărm foarte crestat, cu fiorduri.", True, "Adevărat: fiordurile sunt simbolul Norvegiei.")
    K.adev(2, "2.3", "Germania nu are ieșire la mare.", False, "Fals: Germania are țărm la Marea Nordului și la Marea Baltică.")
    K.l(2, "2.1", "Completează.", "Capitala Franței, [Paris], e pe Sena; capitala Germaniei, [Berlin], e pe Spree.", ["Lyon", "Hamburg"], "Paris, Berlin.")
    K.l(2, "2.3", "Completează.", "Norvegia extrage [petrol] din Marea Nordului și are o flotă mare de [pescuit].", ["aur", "minerit"], "Petrol și pescuit.")
    K.o(3, "2.3", "Ordonează statele de la sud la nord.", ["Franța", "Germania", "Norvegia"], "De la sud la nord", "Franța e cea mai sudică dintre ele, Norvegia cea mai nordică.")
    K.g(3, "2.3 4.1", "Graficul arată populația celor trei state (milioane, valori rotunjite). Care are cea mai mare populație?", grafic("bare", "Populația (milioane, valori rotunjite)", [("Germania", 84), ("Franța", 68), ("Norvegia", 5.5)], "milioane", "Eurostat / Statistics Norway"), "Germania", ["Franța", "Norvegia", "sunt egale"], "Germania are cea mai mare populație din UE.", surse=["Eurostat – Population on 1 January", "Statistics Norway (SSB) – Population"])
    K.a(3, "2.3", "De ce Norvegia are puțini locuitori față de suprafață?", "pentru că are mult relief muntos și climă rece în nord", ["pentru că e deșert", "pentru că e foarte cald", "pentru că e o insulă mică"], "Populația stă mai ales pe țărm și în sud.")
    K.a(2, "2.1", "Ce munte, cel mai înalt din Alpi, e la granița Franței cu Italia?", "Mont Blanc", ["Elbrus", "Olimp", "Moldoveanu"], "Mont Blanc are aproximativ 4 805 m.", surse=S_MB)
    K.a(2, "2.3", "Ce obiectiv turistic din Paris e simbolul Franței?", "Turnul Eiffel", ["Colosseumul", "Big Ben", "Acropole"], "Turnul Eiffel a fost construit pentru Expoziția Universală din 1889.")
    K.a(3, "2.3", "Ce au în comun Franța și Germania?", "sunt state fondatoare ale Uniunii Europene, cu economii puternice", ["nu au ieșire la mare", "au climă polară", "au fiorduri"], "Au semnat Tratatul de la Roma în 1957.")
    K.d(2, "2.1", "Ce stat e marcat pe hartă?", "lume", 46.5, 2.5, "Franța", ["Spania", "Germania", "Italia"], "Franța are forma unui hexagon.")
    K.a(2, "2.3", "Ce climat are cea mai mare parte a Germaniei?", "temperat de tranziție (între oceanic și continental)", ["mediteranean", "polar", "ecuatorial"], "Germania e în centrul Europei.")
    K.a(2, "2.3", "Ce animale cresc populațiile sami în nordul Norvegiei?", "reni", ["cămile", "zebre", "lame"], "Creșterea renilor e o ocupație tradițională.")
    K.a(3, "2.3", "Ce regiune a Franței e cunoscută pentru vinuri?", "Bordeaux (și Champagne, Burgundia)", ["Laponia", "Siberia", "Bavaria"], "Franța e unul dintre cei mai mari producători de vin.")

    # ================================================================ S30 Caracterizarea unor state (II)
    L = Lectie(6, "VI-S30-caracterizarea-geografica-state-continuare", "Caracterizarea geografică a unor state (II)",
               "Ce au în comun Italia, Polonia și Ucraina cu România?",
               [("Italia (Europa de Sud)", "Capitala: Roma. Relief: Alpii în nord, Câmpia Padului, Apeninii pe toată peninsula, vulcani (Vezuviu, Etna). Climă mediteraneeană în cea mai mare parte.\nEconomie: industrie în nord (Milano, Torino: automobile, modă), agricultură (măslini, viță, citrice), turism foarte dezvoltat (Roma, Veneția, Florența). Italia are cele mai multe situri UNESCO din lume."),
                ("Polonia (Europa Centrală)", "Capitala: Varșovia. Relief: în cea mai mare parte câmpie (Câmpia Germano-Polonă), Carpații în sud. Râuri: Vistula, Oder. Climă temperată de tranziție.\nEconomie: cărbune, industrie, agricultură (cartof, secară), servicii în creștere rapidă."),
                ("Ucraina (Europa de Est)", "Capitala: Kiev. Relief: câmpie și podiș, Carpații în vest, Crimeea în sud. Râuri: Nipru, Nistru; ieșire la Marea Neagră.\nEconomie: soluri de cernoziom, mari producții de cereale și floarea-soarelui, minereu de fier, cărbune. Ucraina e vecină cu România.")],
               stiaica="Italia are cele mai multe situri înscrise în patrimoniul mondial UNESCO dintre toate țările lumii.",
               ref=REF.format("Caracterizarea geografică a unor state (continuare)"))
    L.s(1, "3.2", "Asociază țara cu capitala.", [("Italia", "Roma"), ("Polonia", "Varșovia"), ("Ucraina", "Kiev")], "Capitalele celor trei state.")
    L.s(1, "3.2", "Asociază țara cu un râu.", [("Italia", "Pad"), ("Polonia", "Vistula"), ("Ucraina", "Nipru")], "Râurile principale.")
    L.s(1, "3.3", "Asociază țara cu o cultură agricolă importantă.", [("Italia", "măslinul"), ("Polonia", "cartoful"), ("Ucraina", "floarea-soarelui")], "Culturi după climă și sol.")
    L.a(2, "3.2", "Ce munți străbat Italia de la nord la sud?", "Apeninii", ["Pirineii", "Uralii", "Balcanii"], "Apeninii sunt „coloana vertebrală” a Italiei.")
    L.a(2, "3.2", "Ce vulcani activi are Italia?", "Vezuviul și Etna", ["Elbrus și Olimp", "Hekla și Katla", "Fuji și Kilimanjaro"], "Vezuviul lângă Napoli, Etna în Sicilia.")
    L.a(2, "3.4", "Ce țară are cele mai multe situri UNESCO din lume?", "Italia", ["Polonia", "Ucraina", "Norvegia"], "Italia are un patrimoniu cultural foarte bogat.", surse=S_UNESCO)
    L.a(2, "3.2", "Ce formă de relief ocupă cea mai mare parte a Poloniei?", "câmpia", ["muntele înalt", "deșertul", "fiordurile"], "Numele „Polonia” vine de la „pole” – câmp.")
    L.a(2, "3.3", "De ce Ucraina e un mare producător de cereale?", "pentru solurile de cernoziom foarte fertile", ["pentru că are multe fiorduri", "pentru că are climă polară", "pentru că are vulcani"], "Cernoziomul e unul dintre cele mai fertile soluri.")
    L.a(2, "3.2", "La ce mare are ieșire Ucraina?", "Marea Neagră (și Marea Azov)", ["Marea Nordului", "Marea Mediterană", "Marea Baltică"], "Odesa e un port important.")
    L.a(2, "3.2", "La ce mare are ieșire Polonia?", "Marea Baltică", ["Marea Neagră", "Marea Mediterană", "Marea Nordului"], "Gdańsk e un port polonez.")
    L.a(2, "3.3", "Ce orașe din nordul Italiei sunt centre industriale?", "Milano și Torino", ["Napoli și Palermo", "Bari și Catania", "Roma și Florența"], "Nordul e cea mai industrializată regiune a Italiei.")
    L.p(2, "3.2", "Atinge pe hartă Italia.", "lume", 42.5, 12.5, "Italia", 450, "Italia are forma unei cizme.")
    L.p(2, "3.2", "Atinge pe hartă Polonia.", "lume", 52, 19, "Polonia", 350, "Polonia e în centrul Europei, la Marea Baltică.")
    L.p(2, "3.2", "Atinge pe hartă Ucraina.", "lume", 49, 32, "Ucraina", 500, "Ucraina e la nord de Marea Neagră.")
    L.adev(2, "3.2", "Ucraina este vecină cu România.", True, "Adevărat: România se învecinează cu Ucraina la nord și la est.")
    L.adev(2, "3.2", "Polonia are relief predominant muntos.", False, "Fals: predomină câmpia; munții sunt doar în sud.")
    L.l(2, "3.2", "Completează.", "Capitala Italiei este [Roma], iar capitala Poloniei este [Varșovia].", ["Milano", "Cracovia"], "Roma și Varșovia.")
    L.l(2, "3.3", "Completează.", "Solul foarte fertil din Ucraina se numește [cernoziom]; pe el se cultivă mult [grâu] și floarea-soarelui.", ["podzol", "cafea"], "Cernoziom și grâu.")
    L.o(3, "4.2", "Ordonează statele de la vest la est.", ["Italia", "Polonia", "Ucraina"], "De la vest la est", "Italia e cea mai vestică dintre ele, Ucraina cea mai estică.")
    L.a(3, "3.3", "Ce asemănări are Ucraina cu sudul României?", "câmpii întinse cu cernoziom, climat cu nuanțe continentale, ieșire la Marea Neagră", ["fiorduri și ghețari", "vulcani activi", "climat mediteranean"], "Câmpia Română și stepa ucraineană seamănă.")
    L.a(3, "3.4", "Ce oraș italian e construit pe insule și e în patrimoniul UNESCO?", "Veneția", ["Milano", "Torino", "Bologna"], "Veneția și laguna ei sunt patrimoniu mondial.", surse=S_UNESCO)
    L.a(2, "3.4", "Ce salină veche din Polonia e în patrimoniul UNESCO?", "Wieliczka", ["Slănic", "Turda", "Praid"], "Salina Wieliczka, lângă Cracovia, e patrimoniu mondial.", surse=S_UNESCO)
    L.a(2, "3.2", "Ce munți se află și în sudul Poloniei, și în vestul Ucrainei, și în România?", "Carpații", ["Alpii", "Apeninii", "Pirineii"], "Carpații sunt un lanț comun mai multor țări.")
    L.g(3, "2.3 4.1", "Graficul arată suprafața celor trei state (mii km², rotunjit). Care e cel mai mare?", grafic("bare", "Suprafața (mii km², valori rotunjite)", [("Ucraina", 604), ("Italia", 302), ("Polonia", 313)], "mii km²", "Encyclopaedia Britannica"), "Ucraina", ["Italia", "Polonia", "sunt egale"], "Ucraina e cel mai mare stat aflat în întregime în Europa.", surse=["Encyclopaedia Britannica – Ukraine / Italy / Poland", "Wikipedia – List of European countries by area"])
    L.a(2, "3.3", "Ce climat are cea mai mare parte a Italiei?", "mediteranean", ["polar", "subpolar", "continental excesiv"], "Veri calde și uscate.")
    L.d(2, "3.2", "Ce stat e marcat pe hartă?", "lume", 52, 19, "Polonia", ["Germania", "Ucraina", "Cehia"], "Polonia e la est de Germania.")
    L.a(2, "3.4", "Ce monument din Roma era o arenă pentru gladiatori?", "Colosseumul", ["Partenonul", "Turnul Eiffel", "Big Ben"], "Colosseumul are aproape 2 000 de ani.")
    L.a(3, "4.2", "Compară economia nordului cu cea a sudului Italiei.", "nordul e mai industrializat și mai bogat; sudul e mai agricol", ["sudul e mai industrializat", "sunt identice", "nordul nu are industrie"], "Diferențele regionale sunt mari în Italia.")
    L.a(2, "3.2", "Pe ce râu se află capitala Poloniei?", "Vistula", ["Oder", "Nipru", "Dunărea"], "Varșovia e pe Vistula.")
    L.a(2, "3.2", "Pe ce râu se află capitala Ucrainei?", "Nipru", ["Nistru", "Vistula", "Volga"], "Kievul e pe Nipru.")

    return Unitate(6, "u3-europa.json", "Europa – identitate geografică").add(M, P, R, H, C, S, Q, O, N, T, E, K, L)
