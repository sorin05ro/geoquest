from autor import Lectie, Unitate, existent, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
F = "u2-relief.json"
S_MOLD = ["Encyclopaedia Britannica – Carpathian Mountains: Southern Carpathians (Moldoveanu 2 544 m)", "Wikipedia (ro) – Vârful Moldoveanu"]
S_PIETROS = ["Parcul Național Munții Rodnei – prezentare (Pietrosul Rodnei 2 303 m)", "Wikipedia (ro) – Vârful Pietrosul Rodnei"]
S_CURC = ["Parcul Natural Apuseni – prezentare", "Wikipedia (ro) – Vârful Curcubăta Mare"]
S_SCAR = ["Parcul Natural Apuseni – Peștera Ghețarul Scărișoara", "Wikipedia (ro) – Peștera Scărișoara"]
S_RET = ["Parcul Național Retezat (retezat.ro) – istoric: primul parc național (1935)", "Wikipedia (ro) – Parcul Național Retezat"]
S_BERCA = ["Euronews România – Buzău, județul vulcanilor noroioși", "Adevărul (ediția Buzău) – Vulcanii Noroioși"]
S_DELTA = ["Administrația Rezervației Biosferei Delta Dunării (ddbra.ro)", "UNESCO World Heritage Centre – Danube Delta"]
BZ = (45.15, 26.82)


def unitate():
    # ================================================================ S3 Relieful – caracteristici generale
    G = Lectie(8, "VIII-S03-relieful-caracteristici-generale", "Relieful României – caracteristici generale",
               "De ce se spune că relieful României e „armonios”?",
               [("Proporție și dispunere", "Relieful României e variat și proporționat: aproximativ o treime munți, o treime dealuri și podișuri, o treime câmpii.\nE dispus concentric, în trepte: în centru Depresiunea Colinară a Transilvaniei, apoi arcul Carpaților, apoi Subcarpații, dealurile și podișurile, iar la exterior câmpiile și Delta Dunării. Treptele coboară de la peste 2 500 m (vârful Moldoveanu, 2 544 m) până la nivelul mării, în Deltă."),
                ("Roci și vârste", "Cele mai vechi roci sunt în Munții Măcinului (Dobrogea de Nord), din munți foarte vechi, erodați. Carpații s-au format în aceeași perioadă cu Alpii, deci sunt munți tineri. Cea mai nouă unitate e Delta Dunării, care se formează și acum.\nTipuri de relief după rocă: vulcanic (Călimani, Harghita), carstic, pe calcare (Apuseni, Mehedinți), glaciar (Retezat, Făgăraș, Parâng, Rodnei), pe sare (Slănic), pe gresii și conglomerate (Ceahlău, Bucegi)."),
                ("Agenți modelatori", "Relieful e modelat de ape (văi, alunecări de teren), vânt (în Dobrogea și Câmpia Română, dune la Hanu Conachi și Carei), îngheț-dezgheț (pe vârfuri), ghețari (în trecut) și de om (cariere, terase, baraje).")],
               stiaica="La Berca–Pâclele, în județul Buzău, gazele din adânc împing la suprafață noroi și formează conuri mici, numite vulcani noroioși – un fenomen rar în Europa.",
               ref=REF.format("Relieful – caracteristici generale"))
    G.a(1, "3.1", "Care e cel mai înalt vârf din România?", "Moldoveanu (2 544 m)", ["Negoiu", "Omu", "Pietrosul Rodnei"], "Moldoveanu e în Munții Făgăraș.", surse=S_MOLD)
    G.a(2, "3.2", "Ce proporție au treptele de relief ale României?", "aproximativ o treime munți, o treime dealuri și podișuri, o treime câmpii", ["90 % munți", "doar câmpii", "jumătate deșert"], "Relief proporționat și armonios.")
    G.a(2, "2.2", "Cum e dispus relieful României?", "concentric, în trepte, în jurul Depresiunii Transilvaniei", ["haotic", "doar în linie dreaptă de la nord la sud", "totul la aceeași altitudine"], "Ca un amfiteatru.")
    G.o(2, "2.2", "Ordonează treptele de relief de la centru spre exterior.", ["Depresiunea Colinară a Transilvaniei", "Carpații", "Subcarpații, dealurile și podișurile", "câmpiile", "Delta Dunării"], "Dispunere concentrică", "De la centru spre margini.")
    G.a(2, "3.1", "Unde se află cele mai vechi roci din România?", "în Munții Măcinului", ["în Delta Dunării", "în Câmpia Română", "în Munții Bucegi"], "Munții Măcinului sunt resturile unor munți foarte vechi.")
    G.a(2, "3.1", "Care e cea mai nouă unitate de relief a României?", "Delta Dunării", ["Munții Măcinului", "Carpații", "Podișul Moldovei"], "Delta se formează și acum.")
    G.s(2, "3.1", "Asociază tipul de relief cu un exemplu.", [("vulcanic", "Munții Călimani"), ("carstic", "Munții Apuseni"), ("glaciar", "Munții Retezat"), ("pe conglomerate", "Ceahlău, Bucegi")], "Relieful după rocă și agent.")
    G.s(2, "3.2", "Asociază agentul modelator cu forma de relief.", [("râul", "vale"), ("ghețarul", "căldare glaciară"), ("vântul", "dună"), ("apa care dizolvă calcarul", "peșteră")], "Agenți și forme.")
    G.a(2, "3.2", "Ce fenomen natural rar se întâlnește la Berca–Pâclele, în județul Buzău?", "vulcanii noroioși", ["gheizerele", "ghețarii activi", "dunele de nisip"], "Gazele din adânc împing noroi la suprafață.", surse=S_BERCA)
    G.p(2, "2.1", "Atinge pe harta României vârful Moldoveanu.", "romania", 45.6, 24.74, "Vârful Moldoveanu", 40, "Moldoveanu e în Munții Făgăraș.", surse=S_MOLD)
    G.p(2, "2.1", "Atinge pe harta României Vulcanii Noroioși de la Berca–Pâclele.", "romania", 45.35, 26.7, "Vulcanii Noroioși", 35, "Sunt în Subcarpații Buzăului.", surse=S_BERCA)
    G.p(3, "2.1", "Atinge pe harta României Munții Măcinului.", "romania", 45.2, 28.3, "Munții Măcinului", 45, "Sunt în nord-vestul Dobrogei.")
    G.p(3, "2.1", "Atinge pe harta României Depresiunea Colinară a Transilvaniei.", "romania", 46.6, 24.4, "Depresiunea Transilvaniei", 70, "În centrul țării, înconjurată de Carpați.")
    G.a(2, "3.2", "Ce proces afectează des versanții din Subcarpați după ploi mari?", "alunecările de teren", ["erupțiile vulcanice", "avalanșele de nisip", "tsunami-urile"], "Rocile argiloase alunecă ușor.")
    G.a(2, "3.2", "Unde se află dune de nisip în România?", "la Hanu Conachi (Galați) și în zona Carei (Satu Mare)", ["în Munții Făgăraș", "în Delta, pe vârfuri de munte", "nu există"], "Formate de vânt.")
    G.a(3, "3.4", "Ce înseamnă relief antropic?", "relief creat sau modificat de om: cariere, haldele de steril, terase, diguri", ["relief vulcanic", "relief glaciar", "relief marin"], "Antropic = făcut de om.")
    G.adev(2, "3.1", "Carpații sunt munți tineri, de aceeași vârstă cu Alpii.", True, "Adevărat.")
    G.adev(2, "3.2", "Relieful României e dominat de munți foarte înalți, de peste 4 000 m.", False, "Fals: vârful maxim e 2 544 m, iar relieful e proporționat.")
    G.l(2, "3.1", "Completează.", "Cel mai înalt vârf din România este [Moldoveanu], în Munții [Făgăraș].", ["Omu", "Bucegi"], "Moldoveanu, Făgăraș.", surse=S_MOLD)
    G.l(2, "3.1", "Completează.", "Cele mai vechi roci sunt în Munții [Măcinului], iar cea mai nouă unitate de relief este [Delta Dunării].", ["Apuseni", "Câmpia Română"], "Vechi și nou.")
    G.g(3, "2.3", "Profilul schematic arată relieful de la Munții Făgăraș până la Dunăre (valori aproximative). Ordonează treptele.", grafic("profil", "Profil schematic Făgăraș – Dunăre", [("Făgăraș", 2500), ("Subcarpați", 700), ("Podișul Getic", 400), ("Câmpia Română", 100), ("Dunărea", 20)], "m"), "munți – Subcarpați – podiș – câmpie – Dunăre", ["câmpie – munți – podiș", "Dunăre – munți – câmpie", "podiș – câmpie – munți"], "Treptele coboară spre Dunăre.")
    G.a(2, "3.3", "De ce relieful variat e un avantaj pentru România?", "oferă resurse diverse: păduri și pășuni la munte, livezi și vii pe dealuri, cereale la câmpie", ["nu e un avantaj", "împiedică orice agricultură", "face țara mai frigului"], "Varietatea reliefului = varietatea economiei.")
    G.d(2, "2.1", "Ce munți vulcanici din Carpații Orientali sunt marcați pe hartă?", "romania", 47.1, 25.3, "Munții Călimani", ["Munții Bucegi", "Munții Retezat", "Munții Apuseni"], "Călimani fac parte din lanțul vulcanic Oaș–Harghita.")
    G.a(2, "3.4", "Ce parc național e primul din România (1935)?", "Parcul Național Retezat", ["Parcul Natural Apuseni", "Delta Dunării", "Parcul Bucegi"], "Retezat are peste 80 de lacuri glaciare.", surse=S_RET)
    G.a(2, "3.1", "Ce rocă formează Ceahlăul și Bucegii, cu forme spectaculoase (Babele, Sfinxul)?", "conglomeratele", ["sarea", "lava", "nisipul"], "Babele și Sfinxul au fost sculptate de vânt și îngheț.")
    G.a(2, "3.2", "Ce forme de relief s-au format pe sare?", "masive de sare, lacuri sărate, „munți de sare” (Slănic)", ["vulcani", "fiorduri", "atoli"], "Sarea se dizolvă ușor.")
    G.a(3, "4.2", "De ce Delta Dunării crește spre mare?", "Dunărea depune aluviuni la vărsare", ["valurile aduc nisip din Turcia", "se ridică scoarța rapid", "o construiesc oamenii"], "Aluviunile formează uscat nou.")
    G.a(2, "4.4", "Cum reduc oamenii eroziunea pe versanți?", "plantează păduri, fac terase, construiesc drenaje", ["taie pădurile", "ară de sus în jos", "nu fac nimic"], "Protejarea solului.")
    G.a(2, "2.2", "Ce culoare au pe harta fizică a României Carpații?", "maro", ["verde", "albastru", "galben deschis"], "Maroul arată altitudinile mari.")
    G.a(2, "3.2", "Ce sunt depresiunile intramontane?", "zone mai joase înconjurate de munți, locuite din vechime", ["vârfuri foarte înalte", "lacuri sărate", "dune"], "Exemple: Țara Bârsei, Depresiunea Petroșani, Depresiunea Maramureșului.")

    # ================================================================ S4 Carpații și Depresiunea Transilvaniei
    C = Lectie(8, "VIII-S04-unitatile-majore-relief-carpatii", "Carpații și Depresiunea Colinară a Transilvaniei",
               "Prin ce se deosebesc Carpații Orientali de cei Meridionali?",
               [("Carpații Orientali", "Se întind de la granița de nord până la Valea Prahovei. Au trei grupe: nordică (Maramureș, Rodnei – vârful Pietrosul Rodnei, 2 303 m), centrală (Ceahlău, Hășmaș, Ciuc) și sudică – Carpații de Curbură (Siriu, Penteleu, Podu Calului, Munții Buzăului, Vrancei, Ciucaș).\nAu un lanț vulcanic la vest (Oaș, Gutâi, Țibleș, Călimani, Gurghiu, Harghita) și multe depresiuni (Maramureș, Dornelor, Ciuc, Brașov)."),
                ("Carpații Meridionali și Occidentali", "Carpații Meridionali, între Valea Prahovei și Culoarul Timiș–Cerna, sunt cei mai înalți și masivi: Bucegi, Făgăraș (Moldoveanu 2 544 m, Negoiu), Parâng, Retezat (Peleaga, 2 509 m). Au relief glaciar.\nCarpații Occidentali, între Dunăre și Someș, sunt mai joși și fragmentați: Munții Banatului, Poiana Ruscă și Munții Apuseni (vârful Curcubăta Mare, 1 849 m), cu relief carstic spectaculos (Peștera Scărișoara, cu un ghețar subteran)."),
                ("Depresiunea Colinară a Transilvaniei", "În interiorul arcului carpatic se află o depresiune largă, cu dealuri și podișuri: Podișul Someșan, Câmpia Transilvaniei (de fapt, dealuri joase), Podișul Târnavelor. Are zăcăminte de gaze naturale și sare.")],
               stiaica="Peștera Ghețarul de la Scărișoara, din Munții Apuseni, adăpostește unul dintre cei mai mari ghețari subterani din Europa.",
               ref=REF.format("Unitățile majore de relief: Carpații și Depresiunea Colinară a Transilvaniei"))
    C.s(2, "2.1", "Asociază grupa Carpaților cu vârful cel mai înalt.", [("Carpații Orientali", "Pietrosul Rodnei (2 303 m)"), ("Carpații Meridionali", "Moldoveanu (2 544 m)"), ("Carpații Occidentali", "Curcubăta Mare (1 849 m)")], "Vârfurile maxime.", surse=S_PIETROS)
    C.a(1, "2.1", "Care grupă a Carpaților e cea mai înaltă?", "Carpații Meridionali", ["Carpații Orientali", "Carpații Occidentali", "Munții Măcinului"], "Au cele mai multe vârfuri de peste 2 500 m.")
    C.a(2, "2.1", "Ce vale desparte Carpații Orientali de Carpații Meridionali?", "Valea Prahovei", ["Valea Oltului", "Valea Mureșului", "Valea Jiului"], "Pe Valea Prahovei sunt Sinaia, Bușteni, Azuga.")
    C.a(2, "2.1", "Ce culoar desparte Carpații Meridionali de Carpații Occidentali?", "Culoarul Timiș–Cerna", ["Valea Prahovei", "Valea Bistriței", "Valea Someșului"], "Culoarul face legătura Banat–Oltenia.")
    C.a(2, "2.1", "Din ce grupă a Carpaților fac parte Munții Buzăului?", "Carpații de Curbură (grupa sudică a Carpaților Orientali)", ["Carpații Meridionali", "Carpații Occidentali", "Munții Apuseni"], "Munții Buzăului, Siriu, Penteleu, Podu Calului sunt în Curbură.")
    C.a(2, "3.1", "Ce munți vulcanici se află în Carpații Orientali?", "Oaș, Gutâi, Țibleș, Călimani, Gurghiu, Harghita", ["Bucegi, Piatra Craiului", "Retezat, Parâng", "Măcin, Babadag"], "Cel mai lung lanț vulcanic din Europa.")
    C.a(2, "3.1", "Ce relief e tipic Munților Apuseni?", "carstic, cu peșteri și chei", ["vulcanic activ", "glaciar cu ghețari actuali", "de dune"], "Calcarele sunt dizolvate de apă.")
    C.a(2, "3.4", "Ce peșteră din Apuseni are un ghețar subteran?", "Scărișoara", ["Peștera Urșilor", "Peștera Muierii", "Peștera Polovragi"], "Ghețarul are mii de ani.", surse=S_SCAR)
    C.a(2, "3.1", "Ce relief e tipic în Retezat, Făgăraș, Parâng și Rodnei?", "glaciar: căldări, lacuri glaciare, văi în U", ["vulcanic", "de dune", "carstic marin"], "Ghețarii au existat aici în trecut.")
    C.a(2, "3.4", "Care e cel mai înalt vârf al Munților Retezat?", "Peleaga (2 509 m)", ["Moldoveanu", "Omu", "Ceahlău"], "Retezat are peste 80 de lacuri glaciare.", surse=S_RET)
    C.p(2, "2.1", "Atinge pe harta României Munții Apuseni.", "romania", 46.5, 22.8, "Munții Apuseni", 60, "Apusenii sunt în vestul Transilvaniei.")
    C.p(2, "2.1", "Atinge pe harta României Munții Retezat.", "romania", 45.37, 22.85, "Munții Retezat", 40, "Retezatul e în județul Hunedoara.", surse=S_RET)
    C.p(2, "2.1", "Atinge pe harta României Munții Rodnei.", "romania", 47.55, 24.7, "Munții Rodnei", 45, "Munții Rodnei sunt în nordul Carpaților Orientali.", surse=S_PIETROS)
    C.p(3, "2.1", "Atinge pe harta României Munții Buzăului.", "romania", 45.5, 26.35, "Munții Buzăului", 45, "În Carpații de Curbură, la nord-vest de Buzău.")
    C.p(3, "2.1", "Atinge pe harta României Ceahlăul.", "romania", 46.98, 25.95, "Ceahlău", 35, "Ceahlăul e în județul Neamț.")
    C.a(2, "3.3", "Ce resurse are Depresiunea Colinară a Transilvaniei?", "gaze naturale și sare", ["petrol din abundență și aur", "cărbune și uraniu", "nimic"], "Gazul metan din Transilvania e foarte curat.")
    C.a(2, "2.1", "Ce subunități are Depresiunea Colinară a Transilvaniei?", "Podișul Someșan, Câmpia Transilvaniei, Podișul Târnavelor", ["Bărăganul, Burnasul", "Podișul Bârladului, Câmpia Moldovei", "Podișul Mehedinți, Podișul Getic"], "Câmpia Transilvaniei e de fapt un relief deluros.")
    C.adev(2, "3.1", "Carpații Occidentali sunt mai înalți decât Carpații Meridionali.", False, "Fals: sunt mai joși și mai fragmentați.")
    C.adev(2, "3.1", "„Câmpia Transilvaniei” e, de fapt, o regiune de dealuri joase.", True, "Adevărat: numele e tradițional.")
    C.l(2, "2.1", "Completează.", "Carpații Orientali se termină la Valea [Prahovei]; cel mai înalt vârf al lor e [Pietrosul Rodnei].", ["Oltului", "Moldoveanu"], "Prahova și Pietrosul.", surse=S_PIETROS)
    C.l(2, "3.1", "Completează.", "Munții Apuseni au relief [carstic]; Munții Călimani au relief [vulcanic].", ["glaciar", "dunar"], "Carstic și vulcanic.")
    C.o(3, "2.1", "Ordonează grupele Carpaților după altitudinea vârfului maxim, descrescător.", ["Carpații Meridionali", "Carpații Orientali", "Carpații Occidentali"], "Altitudine, descrescător", "2 544 m, 2 303 m, 1 849 m.", surse=S_MOLD)
    C.g(3, "2.3", "Graficul compară vârfurile maxime ale grupelor carpatice. Cu cât e mai înalt Moldoveanu decât Curcubăta Mare?", grafic("bare", "Vârfuri maxime ale Carpaților românești", [("Moldoveanu", 2544), ("Pietrosul Rodnei", 2303), ("Curcubăta Mare", 1849)], "m"), "cu 695 m", ["cu 241 m", "cu 454 m", "cu 1 849 m"], "2 544 − 1 849 = 695.", surse=S_CURC)
    C.d(2, "2.1", "Ce depresiune intramontană mare, cu orașul Brașov, e marcată pe hartă?", "romania", 45.75, 25.7, "Depresiunea Brașov (Țara Bârsei)", ["Depresiunea Petroșani", "Depresiunea Maramureșului", "Depresiunea Ciuc"], "Cea mai mare depresiune intramontană.")
    C.a(3, "4.2", "Compară Carpații Meridionali cu Carpații Occidentali.", "Meridionalii sunt mai înalți, masivi, cu relief glaciar; Occidentalii sunt mai joși, fragmentați, cu relief carstic", ["sunt identici", "Occidentalii sunt mai înalți", "Meridionalii sunt vulcanici"], "Diferențe de altitudine și roci.")
    C.a(2, "3.3", "Ce pas leagă Transilvania de Muntenia pe Valea Prahovei?", "Pasul Predeal", ["Pasul Prislop", "Pasul Tihuța", "Pasul Vâlcan"], "Pe aici trec calea ferată și DN1.")
    C.a(2, "3.3", "Ce drum spectaculos traversează Munții Făgăraș?", "Transfăgărășanul", ["Transalpina", "DN1", "Autostrada A1"], "Leagă Argeșul de Sibiu, pe lângă Lacul Bâlea.")
    C.a(2, "3.3", "Ce drum urcă cel mai sus în România, prin Munții Parâng?", "Transalpina", ["Transfăgărășanul", "DN1", "Valea Oltului"], "Ajunge la peste 2 100 m.")
    C.a(2, "2.1", "Prin ce defileu traversează Oltul Carpații Meridionali?", "Defileul Oltului (Turnu Roșu – Cozia)", ["Cheile Bicazului", "Defileul Dunării", "Cheile Turzii"], "Râul a tăiat munții.")
    C.a(2, "3.4", "Ce chei celebre se află în Carpații Orientali, lângă Lacul Roșu?", "Cheile Bicazului", ["Cheile Turzii", "Cheile Nerei", "Cheile Râșnoavei"], "Pereți de calcar de sute de metri.")

    # ================================================================ S6 Subcarpații, Podișul Getic, Podișul Mehedinți
    S = Lectie(8, "VIII-S06-subcarpatii-podisul-getic-podisul", "Subcarpații, Podișul Getic și Podișul Mehedinți",
               "Ce fel de relief se află între Munții Buzăului și Câmpia Română?",
               [("Subcarpații", "Subcarpații sunt dealuri înalte situate la exteriorul Carpaților Orientali și Meridionali, de la Valea Moldovei până la Valea Motrului. Au roci moi (argile, marne, nisipuri, sare), deci alunecări de teren frecvente.\nSe împart în: Subcarpații Moldovei, Subcarpații de Curbură (între Trotuș și Dâmbovița – aici e județul Buzău, cu Vulcanii Noroioși) și Subcarpații Getici. Au depresiuni largi, dens populate, cu livezi și vii (Dealu Mare)."),
                ("Podișul Getic", "Podișul Getic se află la sudul Subcarpaților Getici, între Dâmbovița și Dunăre. E format din piemonturi (depozite de pietrișuri și nisipuri cărate de râuri din munți): Piemontul Cândești, Argeșului, Cotmeana, Olteț, Bălăciței.\nResurse: petrol și gaze, cărbune (lignit, în Oltenia)."),
                ("Podișul Mehedinți", "Mic, situat între Carpații Meridionali și Subcarpații Getici, în vestul Olteniei. E alcătuit din roci cristaline și calcare: are relief carstic (Podul Natural de la Ponoarele, Peștera Topolnița).")],
               stiaica="La Ponoarele, în Podișul Mehedinți, apa a săpat în calcar un pod natural de piatră pe care trece un drum.",
               ref=REF.format("Subcarpații, Podișul Getic și Podișul Mehedinți"))
    S.a(1, "2.1", "Ce sunt Subcarpații?", "dealuri înalte situate la exteriorul Carpaților", ["munți vulcanici", "câmpii joase", "podișuri de calcar"], "„Sub” Carpați, la poalele lor.")
    S.s(2, "2.1", "Asociază ramura Subcarpaților cu poziția ei.", [("Subcarpații Moldovei", "nord-est"), ("Subcarpații de Curbură", "la cotul Carpaților, inclusiv în Buzău"), ("Subcarpații Getici", "sud, între Dâmbovița și Motru")], "Cele trei ramuri.")
    S.a(2, "2.1", "În ce ramură a Subcarpaților se află Vulcanii Noroioși?", "Subcarpații de Curbură", ["Subcarpații Getici", "Subcarpații Moldovei", "Podișul Mehedinți"], "La Berca–Pâclele, județul Buzău.", surse=S_BERCA)
    S.a(2, "3.2", "De ce în Subcarpați sunt frecvente alunecările de teren?", "rocile sunt moi (argile, marne), iar pantele sunt mari", ["sunt vulcani activi", "e deșert", "sunt ghețari"], "După ploi mari, terenul alunecă.")
    S.a(2, "3.3", "Ce podgorie cunoscută se află în Subcarpații de Curbură?", "Dealu Mare", ["Murfatlar", "Cotnari", "Recaș"], "Între Prahova și Buzău.")
    S.a(2, "1.1", "Ce este un piemont?", "o întindere formată din pietrișuri și nisipuri cărate de râuri din munți și depuse la poalele lor", ["un vârf de munte", "un lac glaciar", "un vulcan"], "Podișul Getic e format din piemonturi.")
    S.a(2, "2.1", "Între ce râuri se află Podișul Getic?", "între Dâmbovița și Dunăre (Motru)", ["între Prut și Siret", "între Mureș și Someș", "între Ialomița și Buzău"], "În sudul Subcarpaților Getici.")
    S.a(2, "3.3", "Ce resurse are Podișul Getic?", "petrol, gaze și lignit", ["aur și argint", "sare din abundență", "diamante"], "Lignitul e exploatat în Oltenia.")
    S.a(2, "3.1", "Ce relief are Podișul Mehedinți?", "carstic, pe calcare", ["vulcanic", "de dune", "glaciar"], "Podul Natural de la Ponoarele, Peștera Topolnița.")
    S.p(2, "2.1", "Atinge pe harta României Subcarpații de Curbură, lângă Buzău.", "romania", 45.3, 26.6, "Subcarpații de Curbură", 45, "Între Trotuș și Dâmbovița.")
    S.p(2, "2.1", "Atinge pe harta României Podișul Getic.", "romania", 44.7, 24, "Podișul Getic", 70, "Podișul Getic e în nordul Olteniei și Munteniei.")
    S.p(3, "2.1", "Atinge pe harta României Podișul Mehedinți.", "romania", 44.85, 22.65, "Podișul Mehedinți", 40, "În vestul Olteniei.")
    S.p(3, "2.1", "Atinge pe harta României municipiul Buzău.", "romania", BZ[0], BZ[1], "Buzău", 30, "Buzău e la ieșirea râului din Subcarpați în câmpie.")
    S.a(2, "3.3", "De ce depresiunile subcarpatice sunt dens populate?", "au climă blândă, soluri bune, ape și sunt adăpostite", ["sunt foarte reci", "sunt deșerturi", "nu au apă"], "Livezi, vii, sate mari.")
    S.a(2, "3.4", "Ce mină de sare veche, transformată în atracție turistică, e în Subcarpații de Curbură?", "Salina Slănic (Prahova)", ["Salina Turda", "Salina Praid", "Salina Ocnele Mari"], "Slănic e în județul Prahova.")
    S.adev(2, "3.2", "Subcarpații sunt alcătuiți mai ales din roci dure, ca granitul.", False, "Fals: din roci moi (argile, marne, nisipuri, sare).")
    S.adev(2, "3.3", "Podișul Getic are zăcăminte de petrol și gaze.", True, "Adevărat.")
    S.l(2, "2.1", "Completează.", "Județul Buzău se află în Subcarpații de [Curbură]; fenomenul natural rar de la Berca e reprezentat de vulcanii [noroioși].", ["Getici", "stinși"], "Curbură, noroioși.", surse=S_BERCA)
    S.l(2, "1.1", "Completează.", "Podișul Getic e format din [piemonturi]; Podișul Mehedinți are relief [carstic].", ["dune", "vulcanic"], "Piemonturi și carst.")
    S.o(3, "2.2", "Ordonează unitățile de relief de la nord la sud prin județul Buzău.", ["Munții Buzăului", "Subcarpații de Curbură", "Câmpia Română"], "De la nord-vest la sud-est", "Munte, deal, câmpie.")
    S.g(3, "2.3", "Profilul schematic arată relieful pe Valea Buzăului (valori aproximative). Ce unitate e între munți și câmpie?", grafic("profil", "Profil schematic pe Valea Buzăului", [("Munții Buzăului", 1500), ("Subcarpații de Curbură", 600), ("municipiul Buzău", 100), ("Câmpia Română", 60)], "m"), "Subcarpații de Curbură", ["Podișul Getic", "Delta Dunării", "Podișul Moldovei"], "Subcarpații sunt treapta de tranziție.")
    S.d(2, "2.1", "Ce podiș e marcat pe hartă, la sudul Subcarpaților Getici?", "romania", 44.7, 24, "Podișul Getic", ["Podișul Moldovei", "Podișul Dobrogei", "Podișul Târnavelor"], "Format din piemonturi.")
    S.a(3, "4.2", "Compară Subcarpații cu Carpații.", "Subcarpații sunt mai joși, din roci moi, cu alunecări; Carpații sunt mai înalți, din roci mai dure", ["Subcarpații sunt mai înalți", "sunt identici", "Carpații au roci mai moi"], "Treapta de tranziție.")
    S.a(2, "3.3", "Ce culturi sunt tipice pe dealurile subcarpatice?", "pomii fructiferi și vița-de-vie", ["orezul", "bumbacul", "ceaiul"], "Livezile de prun și podgoriile.")
    S.a(2, "3.4", "Ce fenomen natural, flăcări care ies din pământ, e la Lopătari (Buzău)?", "Focul Viu", ["Vulcanii Noroioși", "Gheizerul", "Izvorul Mucului"], "Gazele naturale ard la suprafață.")
    S.a(2, "3.4", "Ce muzeu unic se află la Colți, în Munții Buzăului?", "Muzeul Chihlimbarului", ["Muzeul Satului", "Muzeul Aurului", "Muzeul Sării"], "Chihlimbarul de Buzău (romanit) e o rășină fosilă.")
    S.a(2, "2.1", "Ce oraș important e în Subcarpații Getici?", "Râmnicu Vâlcea (și Târgu Jiu)", ["Constanța", "Iași", "Timișoara"], "Așezate în depresiuni subcarpatice.")
    S.a(2, "4.4", "Cum se pot proteja satele subcarpatice de alunecări?", "împădurirea versanților, drenarea apei, evitarea construcțiilor pe pante instabile", ["construcții pe pante instabile", "tăierea pădurii", "irigații abundente pe pante"], "Prevenție.")
    S.a(2, "3.2", "Ce sunt cutele diapire din Subcarpați?", "cute ale straturilor în care sarea a străpuns rocile de deasupra", ["vulcani activi", "ghețari", "dune"], "Sarea urcă spre suprafață.")

    S.a(2, "2.1", "Ce râu desparte Subcarpații Getici de Podișul Mehedinți la vest?", "Motrul", ["Oltul", "Argeșul", "Buzăul"], "Subcarpații Getici se întind până la Motru.")

    # ================================================================ S8–S11 extinse
    M8 = existent(8, F, "VIII-S08-podisul-moldovei-podisul-dobrogei", "E8")
    M8.p(2, "2.1", "Atinge pe harta României orașul Iași.", "romania", 47.16, 27.59, "Iași", 30, "Iașiul e în Câmpia Moldovei (Podișul Moldovei).")
    M8.p(2, "2.1", "Atinge pe harta României orașul Constanța.", "romania", 44.18, 28.63, "Constanța", 30, "Constanța e pe țărmul Mării Negre, în Podișul Dobrogei.")
    M8.a(2, "3.1", "Ce subunitate a Podișului Moldovei e de fapt un relief deluros jos, numit „câmpie”?", "Câmpia Moldovei (Jijiei)", ["Podișul Sucevei", "Podișul Bârladului", "Podișul Covurlui"], "Ca și Câmpia Transilvaniei.")
    M8.a(2, "3.2", "Ce sunt cuestele din Podișul Moldovei?", "dealuri asimetrice, cu o pantă abruptă și una lină, formate pe straturi înclinate", ["vulcani", "dune", "fiorduri"], "Ex.: Coasta Iașilor.")
    M8.a(2, "3.3", "Ce podgorie celebră e în Podișul Moldovei?", "Cotnari", ["Dealu Mare", "Murfatlar", "Recaș"], "Grasa de Cotnari.")
    M8.a(2, "3.3", "Ce podgorie celebră e în Podișul Dobrogei?", "Murfatlar", ["Cotnari", "Dealu Mare", "Odobești"], "Dobrogea are multe zile însorite.")
    M8.a(2, "2.1", "Ce râuri mărginesc Podișul Moldovei?", "Siretul (vest) și Prutul (est)", ["Oltul și Jiul", "Mureșul și Someșul", "Argeșul și Ialomița"], "Siretul și Prutul curg de la nord la sud.")
    M8.a(2, "3.1", "Ce relief de calcare apare în Dobrogea de Sud?", "podiș jos, cu văi seci și peșteri (carst)", ["vulcani activi", "ghețari", "dune de nisip înalte"], "Ex.: Peștera Limanu.")
    M8.a(2, "2.2", "De ce Dobrogea are puține râuri?", "e cea mai uscată regiune a țării", ["e cea mai ploioasă", "e acoperită de gheață", "e muntoasă"], "Sub 400 l/m² pe an în unele zone.")
    M8.adev(2, "3.1", "Munții Măcinului sunt cei mai vechi munți din România.", True, "Adevărat: resturi ale unui lanț hercinic erodat.")
    M8.adev(2, "3.1", "Podișul Dobrogei e mai înalt decât Carpații.", False, "Fals: e un podiș jos.")
    M8.d(2, "2.1", "Ce subunitate a Podișului Moldovei e marcată pe hartă, în sud?", "romania", 46.3, 27.6, "Podișul Bârladului", ["Podișul Sucevei", "Câmpia Moldovei", "Podișul Covurlui"], "Cea mai întinsă subunitate.")
    M8.a(3, "4.2", "Compară Podișul Moldovei cu Podișul Dobrogei.", "Moldova are roci sedimentare tinere și cueste; Dobrogea are roci foarte vechi (Măcin) și climă mai uscată", ["sunt identice", "Moldova e mai uscată", "Dobrogea are roci mai tinere peste tot"], "Diferențe de roci și climă.")
    M8.a(2, "3.4", "Ce oraș antic grecesc se află pe țărmul Dobrogei, lângă Constanța?", "Tomis (Constanța de azi)", ["Sarmizegetusa", "Apulum", "Napoca"], "Și Histria, Callatis.")
    M8.a(2, "3.2", "Ce vânt rece bate iarna în Moldova și Dobrogea, dinspre nord-est?", "crivățul", ["foehnul", "austrul", "musonul"], "Crivățul aduce ger și viscol.")
    M8.a(2, "4.4", "Ce problemă de mediu are Podișul Moldovei?", "eroziunea solului și alunecările de teren", ["erupțiile vulcanice", "avalanșele", "tsunami-urile"], "Pădurile au fost defrișate în trecut.")

    M9 = existent(8, F, "VIII-S09-campia-vest-dealurile-vest", "E9")
    M9.p(2, "2.1", "Atinge pe harta României Timișoara.", "romania", 45.75, 21.23, "Timișoara", 30, "Timișoara e în Câmpia de Vest, pe Bega.")
    M9.p(2, "2.1", "Atinge pe harta României Oradea.", "romania", 47.06, 21.93, "Oradea", 30, "Oradea e pe Crișul Repede.")
    M9.a(2, "2.1", "Ce subunități are Câmpia de Vest?", "Câmpia Someșului, Crișurilor, Mureșului, Timișului", ["Bărăganul, Burnasul", "Câmpia Jijiei", "Câmpia Transilvaniei"], "După râurile care o traversează.")
    M9.a(2, "3.2", "Ce fel de câmpie e Câmpia de Vest?", "câmpie de subsidență (care s-a lăsat) și de glacis, cu zone mlăștinoase desecate", ["câmpie vulcanică", "câmpie glaciară", "câmpie deltaică"], "Râurile au divagat mult.")
    M9.a(2, "3.3", "Ce resursă specială are Câmpia de Vest, folosită în stațiuni?", "ape termale (Băile Felix, Băile 1 Mai)", ["sare gemă", "aur", "cărbune"], "Lângă Oradea.")
    M9.a(2, "3.3", "Ce canal navigabil traversează Timișoara?", "Canalul Bega", ["Canalul Dunăre–Marea Neagră", "Canalul Sulina", "Canalul Suez"], "Construit în secolul XVIII.")
    M9.a(2, "2.1", "Ce dealuri se află între Câmpia de Vest și Munții Apuseni?", "Dealurile de Vest", ["Subcarpații", "Podișul Getic", "Dealurile Moldovei"], "Dealurile Crișanei, Banatului.")
    M9.adev(2, "3.2", "Câmpia de Vest are influențe climatice oceanice mai puternice decât Câmpia Română.", True, "Adevărat: e mai aproape de Atlantic și mai umedă.")
    M9.adev(2, "3.1", "Dealurile de Vest sunt mai înalte decât Carpații Meridionali.", False, "Fals: sunt dealuri joase.")
    M9.d(2, "2.1", "Ce oraș din Câmpia de Vest, pe Mureș, e marcat pe hartă?", "romania", 46.18, 21.32, "Arad", ["Timișoara", "Oradea", "Satu Mare"], "Arad e pe Mureș.")
    M9.a(3, "4.2", "Compară Câmpia de Vest cu Câmpia Română.", "Câmpia de Vest e mai umedă, mai mică, cu influențe oceanice; Câmpia Română e mai mare și mai uscată în est", ["sunt identice", "Câmpia de Vest e mai uscată", "Câmpia Română e mai mică"], "Influențe climatice diferite.")
    M9.a(2, "3.3", "Ce dune de nisip se află în nord-vestul Câmpiei de Vest?", "dunele de la Carei", ["dunele de la Hanu Conachi", "Babele", "Sfinxul"], "Rezervația Dunele de nisip de la Foieni.")
    M9.a(2, "3.4", "Ce stațiune balneară, cu ape termale, se află lângă Oradea?", "Băile Felix", ["Băile Herculane", "Sovata", "Techirghiol"], "Apă termală din adânc.")
    M9.a(2, "3.3", "Ce culturi sunt importante în Câmpia de Vest?", "cereale, legume, sfeclă de zahăr", ["orez de munte", "ceai", "banane"], "Soluri fertile și climă umedă.")
    M9.a(2, "2.2", "De ce râurile din Câmpia de Vest au albii instabile?", "panta e foarte mică, iar râurile își schimbă cursul (divagă)", ["sunt înghețate tot anul", "sunt subterane", "curg pe munte"], "S-au făcut îndiguiri și canale.")
    M9.a(2, "2.1", "Ce râu traversează Oradea?", "Crișul Repede", ["Mureșul", "Bega", "Someșul"], "Oradea e în Câmpia Crișurilor.")

    M10 = existent(8, F, "VIII-S10-campia-romana", "E10")
    M10.a(2, "2.1", "Ce subunitate a Câmpiei Române e cea mai uscată, în est?", "Bărăganul", ["Câmpia Olteniei", "Câmpia Pitești", "Câmpia Târgoviștei"], "Bărăganul are cele mai puține ploi din câmpie.")
    M10.a(2, "2.1", "Ce subunitate a Câmpiei Române se află în jurul orașului nostru?", "Câmpia Râmnicului, în nord-estul Câmpiei Române", ["Câmpia Olteniei", "Câmpia Burnasului", "Câmpia Găvanu-Burdea"], "Câmpiile Buzăului și Râmnicului sunt în nord-estul Câmpiei Române.")
    M10.a(2, "3.2", "Ce sunt câmpiile de subsidență?", "câmpii joase care se lasă lent, cu râuri care divagă și zone mlăștinoase", ["câmpii foarte înalte", "câmpii din nisip vulcanic", "câmpii glaciare"], "Ex.: Câmpia Siretului Inferior, Câmpia Buzăului.")
    M10.a(2, "3.2", "Ce sunt câmpiile piemontane (de glacis)?", "câmpii înalte, la contactul cu dealurile, formate din materiale aduse de râuri", ["câmpii sub nivelul mării", "câmpii de deltă", "câmpii de gheață"], "Ex.: Câmpia Pitești, Câmpia Târgoviștei.")
    M10.a(2, "3.3", "Ce culturi agricole predomină în Câmpia Română?", "grâu, porumb, floarea-soarelui", ["orez și ceai", "cafea", "măslini"], "E cel mai important grânar al țării.")
    M10.a(2, "3.4", "Ce lac sărat cu nămol terapeutic e în Bărăgan?", "Lacul Amara (și Lacul Sărat de lângă Brăila)", ["Lacul Bucura", "Lacul Sfânta Ana", "Lacul Vidraru"], "Lacurile sărate din Bărăgan sunt balneare.")
    M10.adev(2, "3.2", "Câmpia Română e cea mai întinsă câmpie a României.", True, "Adevărat.")
    M10.adev(2, "3.2", "În estul Câmpiei Române plouă mai mult decât în vest.", False, "Fals: estul (Bărăganul) e mai uscat.")
    M10.d(2, "2.1", "Ce subunitate a Câmpiei Române, în vest, e marcată pe hartă?", "romania", 44.1, 23.7, "Câmpia Olteniei", ["Bărăganul", "Câmpia Burnasului", "Câmpia Vlăsiei"], "Câmpia Olteniei are dune de nisip la Dăbuleni.")
    M10.a(3, "4.2", "Compară vestul cu estul Câmpiei Române.", "vestul e mai umed, cu păduri de stejar în trecut; estul e mai uscat, cu stepă și irigații", ["sunt identice", "estul e mai umed", "vestul e deșert"], "Influențe climatice diferite.")
    M10.a(2, "3.3", "Ce zonă cu nisipuri din sudul Olteniei e cunoscută pentru pepeni?", "Dăbuleni", ["Bărăgan", "Vlăsia", "Burnas"], "Nisipurile de la Dăbuleni sunt cultivate.")
    M10.a(2, "3.2", "Ce pădure veche a acoperit câmpia din jurul Bucureștiului?", "Codrii Vlăsiei", ["Codrii Cosminului", "Pădurea Letea", "Pădurea Hoia"], "Azi au rămas doar resturi (Snagov, Băneasa).")
    M10.a(2, "2.1", "Ce râuri traversează Câmpia Română de la nord la sud?", "Jiul, Oltul, Argeșul, Ialomița, Buzăul, Siretul", ["Mureșul și Crișurile", "Someșul și Tisa", "Bega și Timișul"], "Toate se varsă în Dunăre (direct sau prin afluenți).")
    M10.a(2, "4.4", "Ce problemă climatică amenință agricultura din Bărăgan?", "seceta", ["avalanșele", "ghețarii", "taifunurile"], "Irigațiile sunt esențiale.")
    M10.a(2, "3.4", "Ce oraș-port de pe Dunăre e în estul Câmpiei Române?", "Brăila", ["Pitești", "Târgoviște", "Ploiești"], "Brăila e pe Dunărea maritimă.")
    M10.a(2, "2.1", "Ce câmpie se află între Ialomița și Dunăre, în est?", "Bărăganul (Bărăganul Ialomiței)", ["Câmpia Olteniei", "Câmpia Pitești", "Câmpia Găvanu-Burdea"], "Bărăganul are crovuri și lacuri sărate.")

    M11 = existent(8, F, "VIII-S11-delta-dunarii-platforma-continentala", "E11")
    M11.a(2, "3.4", "Din ce an e Delta Dunării Rezervație a Biosferei?", "1990", ["1935", "2007", "1880"], "Și patrimoniu mondial UNESCO din 1991.", surse=S_DELTA)
    M11.a(2, "3.3", "Ce pasăre e simbolul Deltei Dunării?", "pelicanul", ["barza", "vulturul pleșuv", "pinguinul"], "Delta are cea mai mare colonie de pelicani din Europa.")
    M11.a(2, "1.1", "Ce sunt plaurii?", "insule plutitoare de stuf și rădăcini", ["dune de nisip", "brațe ale Dunării", "păduri pe grinduri"], "Plaurii se mișcă pe lacuri.")
    M11.a(2, "3.3", "Ce pădure veche, cu liane, se află pe grindul Letea?", "Pădurea Letea", ["Codrii Vlăsiei", "Pădurea Băneasa", "Pădurea Hoia"], "Cea mai nordică pădure cu liane din Europa.")
    M11.a(2, "3.3", "Ce ocupații tradiționale au locuitorii Deltei?", "pescuitul, recoltarea stufului, turismul", ["mineritul", "creșterea renilor", "industria oțelului"], "Lipovenii sunt pescari pricepuți.")
    M11.a(2, "3.3", "Ce plantă acoperă cea mai mare parte a Deltei?", "stuful", ["molidul", "cactusul", "bambusul"], "Delta are una dintre cele mai mari suprafețe de stuf din lume.")
    M11.p(3, "2.1", "Atinge pe harta României orașul Sulina, la vărsarea brațului Sulina.", "romania", 45.16, 29.66, "Sulina", 30, "Sulina e cel mai estic oraș al României.")
    M11.adev(2, "3.4", "Delta Dunării e în patrimoniul mondial UNESCO.", True, "Adevărat, din 1991.", surse=S_DELTA)
    M11.adev(2, "3.2", "Delta Dunării e o unitate de relief foarte veche.", False, "Fals: e cea mai nouă și se formează și acum.")
    M11.d(2, "2.1", "Ce oraș, „poarta Deltei”, e marcat pe hartă?", "romania", 45.18, 28.8, "Tulcea", ["Sulina", "Galați", "Brăila"], "Tulcea e la începutul Deltei.")
    M11.a(3, "4.2", "Compară cele trei brațe ale Dunării.", "Chilia e cel mai mare debit, Sulina e rectificat pentru nave, Sfântu Gheorghe e cel mai vechi și sinuos", ["sunt identice", "Sulina are cel mai mare debit", "Chilia e rectificat"], "Fiecare braț are particularitatea lui.")
    M11.a(2, "3.1", "Ce e platforma continentală a Mării Negre?", "continuarea sub apă a uscatului, până la aproximativ 200 m adâncime", ["groapa cea mai adâncă", "o insulă", "un vulcan submarin"], "E foarte largă în dreptul Dobrogei.")
    M11.a(2, "3.3", "Ce resursă se exploatează din platforma continentală românească?", "petrol și gaze naturale", ["aur", "cărbune", "sare gemă"], "Inclusiv zăcământul Neptun Deep.")
    M11.a(2, "4.4", "Ce măsură protejează păsările din Delta?", "zonele strict protejate, unde accesul e interzis", ["vânătoarea liberă", "desecarea lacurilor", "zgomotul bărcilor cu motor puternic oriunde"], "Regulile Rezervației.")
    M11.a(2, "2.1", "Ce complex lagunar se află la sudul Deltei?", "Razim–Sinoe", ["Bâlea", "Techirghiol", "Snagov"], "Razim e cel mai mare lac al României.")
    M11.a(2, "3.3", "Ce minoritate etnică, cu tradiții de pescari, trăiește în Delta?", "lipovenii", ["secuii", "sașii", "moții"], "Lipovenii sunt de origine rusă, de rit vechi.")

    S12 = existent(8, F, "VIII-S12-aplicatii-practice-studii-caz", "E12")
    return Unitate(8, F, "Relieful României").add(G, C, S, M8, M9, M10, M11, S12)
