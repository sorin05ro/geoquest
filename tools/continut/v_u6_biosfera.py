from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"
S_SOL = ["FAO – International Year of Soils 2015, fișa „Soils are a non-renewable resource”", "FAO – Healthy soils are the basis for healthy food production"]


def unitate():
    # ================================================================ S28a Biosfera
    B = Lectie(5, "V-S28-biosfera-caracteristici-generale-importanta", "Biosfera – caracteristici generale și importanță",
               "Unde pe Pământ găsim viață: doar pe uscat, sau și în aer, apă și sol?",
               [("Ce este biosfera", "Biosfera este învelișul viu al Pământului: toate plantele, animalele, ciupercile și microorganismele, împreună cu locurile în care trăiesc.\nViața există în partea de jos a atmosferei, în toată hidrosfera și în partea de sus a litosferei (în sol). De aceea biosfera se întrepătrunde cu celelalte învelișuri."),
                ("De ce depinde viața", "Viețuitoarele au nevoie de lumină, căldură, apă, aer și hrană. Acolo unde acestea sunt din belșug (de exemplu, în pădurile de lângă Ecuator), viața e foarte bogată. Unde sunt puține (deșerturi, zone polare, vârfuri înalte), viața e săracă.\nVarietatea viețuitoarelor dintr-un loc se numește biodiversitate."),
                ("Legăturile dintre viețuitoare", "Plantele își fac singure hrana, cu ajutorul luminii. Animalele ierbivore mănâncă plante, iar carnivorele mănâncă alte animale. Așa se formează lanțurile trofice (lanțuri de hrană).\nCiupercile și microorganismele descompun resturile moarte și le transformă în substanțe care îmbogățesc solul.")],
               stiaica="Pădurea amazoniană, cea mai mare pădure tropicală de pe Pământ, adăpostește un număr uriaș de specii de plante și animale. Multe nu au fost încă descrise de oamenii de știință.",
               ref=REF.format("Biosfera – caracteristici generale și importanță"), prefix="V28a")
    B.a(1, "1.1", "Ce este biosfera?", "învelișul viu al Pământului", ["învelișul de apă", "învelișul de aer", "stratul de roci"], "Bio- înseamnă viață.")
    B.a(2, "1.2", "În ce învelișuri ale Pământului există viață?", "în partea de jos a atmosferei, în hidrosferă și în partea de sus a litosferei", ["doar pe uscat", "doar în ocean", "doar în aer"], "Biosfera pătrunde în toate celelalte învelișuri.")
    B.s(1, "1.1", "Asociază viețuitoarea cu grupul ei.", [("stejarul", "plante"), ("vulpea", "animale"), ("hribul", "ciuperci"), ("bacteriile", "microorganisme")], "Patru mari grupe de viețuitoare.")
    B.a(2, "1.2", "De ce au nevoie plantele ca să-și facă hrana?", "de lumină, apă și dioxid de carbon", ["de întuneric și sare", "doar de sol", "de alte plante"], "Plantele folosesc lumina Soarelui ca să-și producă hrana.")
    B.a(1, "1.1", "Ce înseamnă biodiversitate?", "varietatea viețuitoarelor dintr-un loc", ["numărul de oameni dintr-un oraș", "înălțimea copacilor", "cantitatea de ploaie"], "Cu cât sunt mai multe specii, cu atât biodiversitatea e mai mare.")
    B.a(2, "3.2", "Unde e cea mai mare biodiversitate de pe uscat?", "în pădurile tropicale umede, lângă Ecuator", ["în deșerturi", "în Antarctica", "pe vârfurile munților"], "Căldura și ploile din belșug favorizează viața.")
    B.a(2, "3.2", "De ce în deșerturi viața e săracă?", "pentru că plouă foarte puțin", ["pentru că e prea întuneric", "pentru că nu există aer", "pentru că e prea frig"], "Lipsa apei limitează plantele și animalele.")
    B.o(2, "1.2", "Ordonează lanțul trofic.", ["iarba", "iepurele", "vulpea"], "Cine pe cine mănâncă", "Planta → ierbivorul → carnivorul.")
    B.o(2, "1.2", "Ordonează lanțul trofic din apă.", ["algele", "peștii mici", "știuca", "vulturul pescar"], "Cine pe cine mănâncă", "Algele sunt hrana peștilor mici; aceștia sunt mâncați de pești răpitori și de păsări.")
    B.s(2, "1.1", "Asociază animalul cu felul în care se hrănește.", [("căprioara", "ierbivor"), ("lupul", "carnivor"), ("ursul", "omnivor (plante și animale)"), ("râma", "descompune resturile din sol")], "Ierbivor, carnivor, omnivor, descompunător.")
    B.a(2, "1.2", "Ce rol au ciupercile și microorganismele din sol?", "descompun resturile de plante și animale și îmbogățesc solul", ["produc oxigen în cantitate mare", "fac ploaia", "răcesc aerul"], "Descompunătorii „reciclează” materia în natură.")
    B.adev(2, "3.3", "Plantele produc oxigenul pe care îl respirăm.", True, "Adevărat: plantele eliberează oxigen când își fac hrana.")
    B.adev(1, "1.2", "Viața există doar pe uscat.", False, "Fals: oceanele, râurile, solul și aerul de jos sunt pline de viață.")
    B.adev(2, "3.2", "Cu cât urci mai sus pe munte, cu atât plantele sunt mai puține și mai mici.", True, "Adevărat: sus e frig, vânt și solul e subțire.")
    B.l(2, "1.1", "Completează.", "Varietatea viețuitoarelor se numește [biodiversitate]; lanțul de hrană se numește lanț [trofic].", ["biosferă", "montan"], "Biodiversitate, lanț trofic.")
    B.a(2, "3.3", "Ce le oferă biosfera oamenilor?", "hrană, lemn, medicamente, oxigen, îmbrăcăminte", ["doar distracție", "doar petrol", "nimic"], "Viața din jurul nostru ne asigură multe resurse.")
    B.a(3, "3.2", "Ce se întâmplă dacă dispare un animal dintr-un lanț trofic?", "se strică echilibrul: unele specii se înmulțesc prea mult, altele rămân fără hrană", ["nu se întâmplă nimic", "apar automat alte animale identice", "plantele cresc mai încet"], "Toate viețuitoarele sunt legate între ele.")
    B.a(3, "4.1", "Ce faci ca să observi biodiversitatea din curtea școlii?", "delimitezi un pătrat de 1 m pe 1 m și numeri plantele și insectele diferite din el", ["tai toate plantele", "pulverizezi insecticid", "pui ciment"], "Observația atentă arată câte specii trăiesc într-un loc mic.")
    B.a(2, "3.3", "Ce amenință biodiversitatea?", "tăierea pădurilor, poluarea și vânatul fără control", ["plantarea copacilor", "ariile protejate", "reciclarea"], "Activitățile omului pot duce la dispariția speciilor.")
    B.a(2, "4.3", "Cum se numesc zonele unde natura e protejată prin lege?", "arii protejate (parcuri naționale, rezervații)", ["zone industriale", "cartiere", "porturi"], "Retezat a fost primul parc național al României, în 1935.")
    B.a(2, "2.1", "Ce rezervație din România e un loc foarte important pentru păsări?", "Delta Dunării", ["Bărăganul arat", "Valea Prahovei", "orașul Galați"], "Delta e Rezervație a Biosferei, cu sute de specii de păsări.")
    B.a(3, "1.2", "Ce înseamnă că o specie e „pe cale de dispariție”?", "mai trăiesc foarte puține exemplare și pot dispărea de tot", ["că s-a mutat pe alt continent", "că e foarte numeroasă", "că doarme iarna"], "Speciile amenințate sunt ocrotite prin lege.")
    B.a(2, "1.1", "Cum se numesc animalele care mănâncă și plante, și animale?", "omnivore", ["ierbivore", "carnivore", "descompunători"], "Ursul și mistrețul sunt omnivore.")
    B.a(2, "3.2", "De ce plantele de pe fundul oceanului adânc lipsesc?", "pentru că lumina Soarelui nu ajunge acolo", ["pentru că apa e dulce", "pentru că e prea cald", "pentru că sunt mâncate toate"], "Plantele au nevoie de lumină; ele cresc doar în apa de la suprafață.")
    B.a(2, "1.2", "Ce viețuitoare se află la începutul oricărui lanț trofic de pe uscat?", "o plantă", ["un carnivor", "un om", "o ciupercă"], "Plantele produc hrana pe care o folosesc apoi animalele.")
    B.a(3, "3.3", "De ce albinele sunt importante pentru oameni?", "polenizează florile, iar fără ele multe fructe și legume nu s-ar forma", ["fac doar miere", "mănâncă dăunătorii", "nu sunt importante"], "Polenizarea face posibile recoltele de pomi fructiferi și multe culturi.")
    B.g(3, "2.3", "Graficul arată numărul de specii de păsări observate în trei locuri imaginare. Unde e biodiversitatea cea mai mare?", grafic("bare", "Specii de păsări observate (date imaginare)", [("parcul orașului", 18), ("pădurea", 45), ("parcarea", 3)], "specii"), "în pădure", ["în parcare", "în parcul orașului", "peste tot la fel"], "În pădure sunt 45 de specii: hrană și adăpost din belșug.")
    B.a(2, "1.1", "Cum se numește locul în care trăiește în mod obișnuit o viețuitoare?", "habitat", ["anotimp", "deltă", "climă"], "Habitatul broaștei e balta; al veveriței, pădurea.")
    B.a(3, "4.3", "Ce poți face ca să ajuți păsările iarna?", "pui o căsuță cu semințe, fără sare și fără pâine stricată", ["le alungi din curte", "dai cu pietre", "tai copacii bătrâni"], "Semințele de floarea-soarelui nesărate sunt potrivite.")
    B.a(1, "3.3", "Ce dau pădurile oamenilor?", "lemn, fructe de pădure, aer curat și adăpost pentru animale", ["petrol", "sare", "nisip"], "Pădurile au multe roluri.")

    # ================================================================ S28b Plantele și animalele
    P = Lectie(5, "V-S28-plantele-animalele-repartitia-geografica", "Plantele și animalele – repartiția lor geografică",
               "De ce nu întâlnești urși polari în Africa și girafe în Groenlanda?",
               [("Plantele se schimbă cu clima", "Vegetația unei regiuni depinde mai ales de căldură și de umezeală.\nÎn zona caldă și umedă: pădurea ecuatorială, deasă, cu mai multe etaje. În zona caldă și uscată: savana (ierburi înalte și copaci rari) și deșertul (plante puține, ca cactușii). În zona temperată: pădurile de foioase (stejar, fag), de conifere (molid, brad) și stepa. În zona rece: tundra (mușchi, licheni, arbuști pitici)."),
                ("Animalele urmează plantele", "Fiecare tip de vegetație are animalele lui, adaptate la climă și hrană. În savană: lei, zebre, girafe, elefanți. În deșert: cămile, scorpioni, șopârle. În taiga: urși bruni, lupi, râși. În tundră: reni, vulpi polare. În zonele polare: urși polari, foci, pinguini (doar în emisfera sudică)."),
                ("Etajarea pe munte", "Pe munte, vegetația se schimbă cu altitudinea, ca și cum ai merge spre pol: păduri de foioase jos, apoi conifere, apoi pajiști alpine, iar sus doar stânci, mușchi și licheni.\nÎn Carpați: păduri de fag și stejar, apoi de molid, apoi jneapăn și pajiști alpine.")],
               stiaica="Pinguinii trăiesc aproape toți în emisfera sudică, iar urșii polari doar în nord. Cele două animale nu se întâlnesc în natură.",
               ref=REF.format("Plantele și animalele – repartiția lor geografică"), prefix="V28b")
    P.s(1, "1.1", "Asociază animalul cu locul unde trăiește.", [("ursul polar", "Arctica"), ("cămila", "deșertul"), ("zebra", "savana"), ("maimuța", "pădurea ecuatorială")], "Fiecare animal e adaptat la mediul lui.")
    P.s(2, "1.1", "Asociază vegetația cu zona.", [("pădurea ecuatorială", "zona caldă și umedă"), ("savana", "zona caldă, cu un anotimp ploios și unul secetos"), ("pădurea de foioase", "zona temperată"), ("tundra", "zona rece")], "Vegetația urmează clima.")
    P.a(1, "1.2", "Ce animal trăiește în Antarctica?", "pinguinul", ["ursul polar", "leul", "zebra"], "Pinguinii trăiesc în emisfera sudică.")
    P.a(2, "1.2", "Unde trăiesc urșii polari?", "în Arctica, în jurul Polului Nord", ["în Antarctica", "în Sahara", "în Amazonia"], "Ursul polar trăiește doar în nord.")
    P.a(2, "1.1", "Ce este savana?", "o întindere cu ierburi înalte și copaci rari, în zona caldă", ["o pădure deasă de conifere", "un deșert de gheață", "o mlaștină"], "Savana are un anotimp ploios și unul secetos.")
    P.a(2, "1.1", "Ce este tundra?", "vegetație de mușchi, licheni și arbuști pitici, în zona rece", ["pădure deasă de stejari", "ierburi înalte cu lei", "deșert cu cactuși"], "Solul din tundră e înghețat în adânc.")
    P.a(2, "1.1", "Ce copaci formează mai ales taigaua?", "coniferele (molid, brad, pin)", ["palmierii", "baobabii", "cactușii"], "Taigaua e pădurea de conifere din nordul Europei, Asiei și Americii de Nord.")
    P.a(2, "3.2", "De ce cactușii trăiesc bine în deșert?", "pentru că păstrează apa în tulpinile groase și au țepi în loc de frunze", ["pentru că au nevoie de multă ploaie", "pentru că le place frigul", "pentru că cresc în apă"], "Cactușii sunt adaptați la secetă.")
    P.a(2, "3.2", "De ce mulți copaci din pădurile de foioase își pierd frunzele toamna?", "ca să treacă iarna rece fără să piardă apă și să fie rupți de zăpadă", ["pentru că sunt bolnavi", "pentru că îi taie oamenii", "pentru că e prea cald"], "Lepădarea frunzelor e o adaptare la iarnă.")
    P.a(2, "3.2", "Cum e adaptat ursul polar la frig?", "are blană deasă și un strat gros de grăsime", ["are piele subțire", "nu are blană", "doarme toată vara"], "Blana și grăsimea îl țin cald.")
    P.a(3, "3.2", "Cum e adaptată cămila la deșert?", "poate rezista mult fără apă și are cocoașe cu grăsime", ["are blană foarte groasă", "înoată bine", "trăiește în copaci"], "Cămila e numită „corabia deșertului”.")
    P.o(2, "1.2", "Ordonează vegetația de pe un munte din Carpați, de jos în sus.", ["păduri de stejar", "păduri de fag", "păduri de molid", "jneapăn și pajiști alpine"], "De la poale spre vârf", "Pe munte, vegetația se etajează după altitudine.")
    P.o(3, "1.2", "Ordonează vegetația de la Ecuator spre Polul Nord, prin Africa și Europa.", ["pădurea ecuatorială", "savana", "deșertul", "pădurea de foioase", "taigaua", "tundra"], "De la Ecuator spre nord", "Cu cât te depărtezi de Ecuator, vegetația se schimbă după climă.")
    P.p(2, "2.1", "Atinge pe hartă pădurea amazoniană.", "lume", -4, -62, "Amazonia", 1500, "Amazonia e în nordul Americii de Sud, pe Ecuator.")
    P.p(2, "2.1", "Atinge pe hartă deșertul Sahara.", "lume", 23, 12, "Sahara", 1500, "Sahara ocupă nordul Africii.")
    P.p(3, "2.1", "Atinge pe hartă o zonă de savană: Serengeti (Tanzania).", "lume", -2.3, 34.8, "Serengeti", 800, "Serengeti e în estul Africii, la sud de Ecuator.")
    P.p(3, "2.1", "Atinge pe hartă o zonă de taiga: Siberia.", "lume", 60, 100, "Siberia", 1800, "Siberia e în nordul Asiei, în Rusia.")
    P.adev(2, "1.2", "Pinguinii și urșii polari trăiesc împreună.", False, "Fals: pinguinii sunt în sud, urșii polari în nord.")
    P.adev(2, "3.2", "Vegetația de pe munte se schimbă cu altitudinea, asemănător cu schimbarea de la Ecuator spre pol.", True, "Adevărat: și sus, și spre pol e mai frig.")
    P.l(2, "1.1", "Completează.", "Pădurea de conifere din nordul Europei și al Asiei se numește [taiga], iar vegetația măruntă din zona rece se numește [tundră].", ["savană", "stepă"], "Taiga – conifere; tundra – mușchi și licheni.")
    P.l(2, "1.2", "Completează.", "Zebrele și girafele trăiesc în [savană], iar cămilele în [deșert].", ["tundră", "taiga"], "Animalele trăiesc unde găsesc hrană și clima potrivită.")
    P.a(2, "1.1", "Ce este stepa?", "o întindere cu ierburi scunde, aproape fără copaci, în zona temperată, cu puține ploi", ["o pădure ecuatorială", "un ghețar", "un lac sărat"], "Bărăganul a fost odinioară o stepă.")
    P.a(2, "2.1", "Ce animal carnivor mare, ocrotit, trăiește în pădurile Carpaților?", "ursul brun", ["leul", "ursul polar", "tigrul"], "Carpații adăpostesc una dintre cele mai mari populații de urși bruni din Europa.")
    P.a(2, "3.3", "Ce animal din Carpați e un simbol al munților și e ocrotit?", "capra neagră", ["cangurul", "zebra", "pinguinul"], "Capra neagră trăiește pe stâncăriile înalte.")
    P.a(2, "3.2", "De ce pădurea ecuatorială are mai multe etaje de vegetație?", "pentru că plantele concurează pentru lumină; unele cresc foarte înalt, altele sub ele", ["pentru că e frig", "pentru că nu plouă", "pentru că animalele construiesc etaje"], "Copacii giganți, apoi arbori mai mici, liane, arbuști și ierburi.")
    P.g(3, "2.3", "Graficul arată temperaturile medii anuale în trei peisaje imaginare. Care e, probabil, tundra?", grafic("bare", "Temperatura medie anuală (date imaginare)", [("peisajul A", 27), ("peisajul B", -10), ("peisajul C", 11)], "°C"), "peisajul B", ["peisajul A", "peisajul C", "niciunul"], "Tundra are temperaturi medii negative.")
    P.a(2, "1.2", "Ce animal migrează toamna spre țările calde?", "barza", ["ursul", "vulpea", "veverița"], "Berzele pleacă toamna spre Africa și se întorc primăvara.")
    P.a(3, "3.2", "De ce ursul hibernează iarna?", "pentru că iarna găsește foarte puțină hrană, iar somnul lung îl ajută să economisească energie", ["pentru că e bolnav", "pentru că e prea cald", "pentru că pleacă în Africa"], "Hibernarea e o adaptare la iarnă.")
    P.a(2, "3.3", "Ce plante cultivate provin din alte continente și se cultivă acum la noi?", "porumbul și cartoful, aduse din America", ["stejarul și fagul", "molidul și bradul", "iarba și trifoiul"], "Porumbul și cartoful au fost aduse în Europa după călătoriile spre America.")
    P.a(3, "1.2", "De ce baobabul, din savană, are un trunchi foarte gros?", "pentru că păstrează în el multă apă pentru perioada secetoasă", ["pentru că e foarte bătrân și atât", "pentru că îl udă oamenii", "pentru că acolo e frig"], "Trunchiul baobabului e un rezervor de apă.")

    # ================================================================ S28c Solul
    S = Lectie(5, "V-S28-solul-resursa-vietii", "Solul – resursă a vieții",
               "Câți ani durează să se formeze un strat de sol gros cât degetul tău?",
               [("Ce este solul", "Solul este stratul subțire și afânat de la suprafața uscatului, în care cresc plantele. E format din fragmente de roci, humus (materie organică descompusă), apă și aer.\nHumusul dă culoarea închisă și fertilitatea (capacitatea de a hrăni plantele)."),
                ("Cum se formează", "Solul se formează foarte încet, din roci mărunțite de îngheț, apă și vânt, la care se adaugă resturile de plante și animale descompuse de ciuperci, râme și microorganisme.\nUn strat de 1 cm de sol se poate forma în sute de ani, până la o mie de ani. De aceea solul e o resursă care nu se reface repede."),
                ("Tipuri și protecție", "În locuri cu climă și vegetație diferite se formează soluri diferite. În Câmpia Română, sub vechea stepă, s-a format cernoziomul, foarte fertil, negru. Sub pădurile de foioase se formează soluri brune.\nSolul e amenințat de eroziune (dacă se taie pădurile de pe pante), de poluare și de construcții. Îl protejăm prin perdele de copaci, arătură de-a curmezișul pantei, folosire atentă a îngrășămintelor.")],
               stiaica="Într-o mână de sol fertil trăiesc mai multe microorganisme decât oameni pe Pământ.",
               ref=REF.format("Solul – resursă a vieții"), prefix="V28c")
    S.a(1, "1.1", "Ce este solul?", "stratul afânat de la suprafața uscatului, în care cresc plantele", ["o rocă dură", "apa din pământ", "stratul de aer de jos"], "Solul e stratul fertil.")
    S.s(1, "1.1", "Asociază componenta solului cu ce este.", [("fragmentele de rocă", "partea minerală"), ("humusul", "resturi de plante și animale descompuse"), ("apa", "dizolvă hrana pentru rădăcini"), ("aerul", "umple golurile dintre particule")], "Solul e un amestec.")
    S.a(2, "1.1", "Ce este humusul?", "partea închisă la culoare a solului, din resturi de plante și animale descompuse", ["o rocă vulcanică", "nisipul de mare", "gheața din sol"], "Humusul face solul fertil.")
    S.a(2, "1.1", "Ce înseamnă un sol fertil?", "un sol care hrănește bine plantele", ["un sol foarte dur", "un sol fără apă", "un sol plin de pietre"], "Fertilitatea depinde mai ales de humus.")
    S.a(2, "3.1", "Cât durează formarea unui strat de sol de 1 cm?", "sute de ani, până la o mie de ani", ["o zi", "o lună", "un an"], "De aceea solul e o resursă care se reface foarte greu.", surse=S_SOL)
    S.o(2, "1.2", "Ordonează pașii formării solului.", ["roca dură e crăpată de îngheț și dezgheț", "bucățile se mărunțesc de apă și vânt", "cresc primele plante (mușchi, licheni)", "resturile lor se descompun în humus", "se formează un sol tot mai gros"], "Formarea solului", "De la rocă la sol fertil, în sute de ani.")
    S.a(2, "1.2", "Ce viețuitoare ajută solul, săpând galerii și amestecând humusul?", "râmele", ["vulturii", "peștii", "girafele"], "Râmele afânează solul și îl îmbogățesc.")
    S.a(2, "2.1", "Ce sol foarte fertil s-a format în Câmpia Română?", "cernoziomul", ["solul de tundră", "solul de deșert", "solul vulcanic"], "Cernoziomul e negru și bogat în humus.")
    S.a(2, "3.2", "Ce culoare are de obicei un sol bogat în humus?", "închisă, aproape neagră", ["albă", "galben-deschisă", "roșie-aprinsă"], "Humusul colorează solul în negru.")
    S.a(2, "1.2", "Ce este eroziunea solului?", "îndepărtarea solului de apă sau vânt", ["formarea solului", "udarea grădinii", "creșterea plantelor"], "Eroziunea poate distruge în câțiva ani ce s-a format în sute de ani.")
    S.a(3, "3.2", "De ce tăierea pădurilor de pe pante duce la pierderea solului?", "pentru că nu mai sunt rădăcini care să țină solul, iar ploile îl spală la vale", ["pentru că se răcește aerul", "pentru că vin animalele", "pentru că apare zăpada"], "Rădăcinile sunt ca o plasă care fixează solul.")
    S.s(2, "4.3", "Asociază problema cu soluția.", [("eroziunea pe pante", "plantezi copaci și ari de-a curmezișul pantei"), ("vântul care spulberă solul", "perdele de protecție din copaci"), ("poluarea cu chimicale", "îngrășăminte folosite cu măsură"), ("solul sărăcit", "rotația culturilor și îngrășământ natural")], "Solul se poate proteja.")
    S.adev(2, "3.3", "Solul se reface foarte repede, deci nu trebuie protejat.", False, "Fals: se formează în sute de ani; trebuie protejat.")
    S.adev(1, "3.3", "Cea mai mare parte a hranei noastre crește din sol.", True, "Adevărat: cerealele, legumele, fructele și hrana animalelor depind de sol.")
    S.adev(2, "1.2", "Solul conține aer și apă.", True, "Adevărat: golurile dintre particule sunt pline de aer și apă.")
    S.l(2, "1.1", "Completează.", "Partea solului care îl face fertil se numește [humus]; solul negru din Câmpia Română se numește [cernoziom].", ["nisip", "granit"], "Humus, cernoziom.")
    S.l(2, "1.2", "Completează.", "Îndepărtarea solului de apă sau vânt se numește [eroziune]; ea e mai puternică pe pantele fără [păduri].", ["înghețare", "case"], "Eroziunea e frânată de păduri.")
    S.a(3, "4.1", "Cum poți arăta că solul conține aer?", "pui o bucată de sol uscat într-un pahar cu apă și vezi bulele care ies", ["pui solul la soare", "cântărești solul", "îl amesteci cu sare"], "Apa intră în goluri și scoate aerul afară.")
    S.a(3, "4.1", "Cum poți arăta că solul conține apă?", "încălzești puțin sol într-un borcan acoperit și vezi picături pe capac", ["îl pui în frigider", "îl arunci în aer", "îl cântărești rece"], "Apa se evaporă și condensează pe capacul rece.")
    S.a(2, "3.3", "Ce sol e mai fertil pentru agricultură?", "un sol bogat în humus, afânat", ["un sol plin de pietre", "nisipul de deșert", "solul înghețat al tundrei"], "Humusul și afânarea ajută rădăcinile.")
    S.a(2, "3.2", "De ce în tundră solul e sărac?", "pentru că e frig, plantele sunt puține și resturile se descompun greu", ["pentru că plouă prea mult", "pentru că e prea cald", "pentru că e plin de nisip"], "Frigul încetinește formarea humusului.")
    S.a(2, "3.3", "Ce este compostul?", "îngrășământ natural obținut din resturi vegetale descompuse", ["un tip de rocă", "o plantă de deșert", "un sol înghețat"], "Compostul redă solului humusul.")
    S.a(2, "4.3", "Ce poți composta acasă?", "coji de legume și fructe, frunze uscate, zaț de cafea", ["plastic", "baterii", "sticlă"], "Doar resturile organice se descompun.")
    S.g(3, "2.3", "Graficul arată grosimea solului pe trei terenuri imaginare. Pe care, probabil, s-a tăiat pădurea de pe pantă?", grafic("bare", "Grosimea stratului de sol (date imaginare)", [("terenul A: pădure", 80), ("terenul B: pantă defrișată", 15), ("terenul C: pajiște", 60)], "cm"), "terenul B", ["terenul A", "terenul C", "toate"], "Pe panta defrișată, ploile au spălat solul.")
    S.a(2, "3.2", "Ce fac rădăcinile plantelor pentru sol?", "îl țin pe loc și îl afânează", ["îl transformă în rocă", "îl încălzesc", "îl fac sărat"], "Rădăcinile protejează solul de eroziune.")
    S.a(3, "1.2", "De ce sub pădurile de foioase solul e brun, nu negru ca cernoziomul?", "pentru că vegetația și clima sunt diferite, deci humusul se formează altfel", ["pentru că e mai vechi", "pentru că e mai nisipos din natură peste tot", "pentru că nu are humus deloc"], "Tipul de sol depinde de climă, vegetație și rocă.")
    S.a(2, "3.3", "Ce înseamnă „rotația culturilor”?", "cultivi plante diferite pe același teren, de la un an la altul, ca să nu sărăcești solul", ["cultivi aceeași plantă mereu", "muți terenul în alt loc", "întorci planta cu rădăcinile în sus"], "Rotația culturilor păstrează fertilitatea.")
    S.a(2, "3.3", "Ce se întâmplă cu solul când pe el se construiesc drumuri și parcări?", "e acoperit și nu mai poate hrăni plante", ["devine mai fertil", "se îngroașă", "produce apă"], "Betonarea pierde solul pentru agricultură.")
    S.p(2, "2.1", "Atinge pe harta României Câmpia Bărăganului, unde predomină cernoziomurile.", "romania", 44.6, 27.3, "Bărăganul", 70, "Bărăganul e în estul Câmpiei Române, între Ialomița, Dunăre și Buzău.")
    S.a(1, "1.1", "În ce strat crește rădăcina plantelor?", "în sol", ["în atmosferă", "în manta", "în nucleu"], "Rădăcinile cresc în sol.")

    # ================================================================ S30 Expediție
    E = Expeditie(5, "V-S30-aplicatie-practica-protectia-plantelor", "Expediție: Patrula naturii",
                  "Ce plante și animale trăiesc lângă școala ta și cum le putem proteja?",
                  ref=REF.format("Aplicație practică: Protecția plantelor, a animalelor și conservarea solului"))
    E.a(1, "4.1", "Ce iei cu tine într-o expediție de observare a naturii?", "caiet, creion, lupă, telefon pentru fotografii (cu un adult)", ["insecticid", "foarfecă pentru flori", "plasă pentru prins păsări"], "Observăm fără să deranjăm viețuitoarele.")
    E.pas("1. Echipamentul", "Pregătește-ți Jurnalul exploratorului. În natură privești, fotografiezi și desenezi; nu rupi plante și nu prinzi animale.")
    E.a(2, "4.1", "Cum numeri plantele dintr-un loc fără să le distrugi?", "faci un pătrat de 1 m × 1 m cu sfoară și numeri ce vezi în el", ["smulgi toate plantele", "le tai și le cântărești", "le calci ca să le vezi mai bine"], "Metoda pătratului e folosită și de cercetători.")
    E.pas("2. Pătratul de observație", "În curtea școlii sau într-un parc, fă un pătrat de 1 m × 1 m. Numără câte plante diferite și câte insecte vezi în el în 10 minute.",
          jurnal="Notează câte plante diferite și câte animale mici ai găsit. Desenează sau fotografiază una.", foto=True)
    E.s(2, "4.3", "Asociază fapta cu efectul ei.", [("plantezi un copac", "ții solul și dai adăpost păsărilor"), ("pui o căsuță pentru păsări", "păsările au unde să cuibărească"), ("strângi gunoaiele din parc", "animalele nu se mai rănesc în ele"), ("nu rupi florile ocrotite", "specia nu dispare")], "Fapte mici, efecte mari.")
    E.a(3, "4.3", "Pe o pantă din apropiere, ploaia a spălat solul. Ce propui?", "plantarea de copaci și arbuști pe pantă", ["tăierea tufișurilor rămase", "arătura de sus în jos", "nimic"], "Vegetația oprește eroziunea.")
    E.pas("3. Solul de lângă școală", "Ia, cu o lingură, puțin sol din două locuri: din parc și de lângă un drum. Compară culoarea, mirosul și ce viețuitoare mici găsești.",
          jurnal="Scrie diferențele dintre cele două probe de sol.")
    E.pas("4. Propunerea ta", "Scrie o propunere pentru clasa ta: o faptă concretă pentru protejarea plantelor, animalelor sau solului din jurul școlii (de exemplu, un colț cu plante pentru albine).",
          jurnal="Scrie propunerea în 3–4 rânduri.")

    return Unitate(5, "u6-biosfera.json", "Biosfera și solurile").add(B, P, S, E)
