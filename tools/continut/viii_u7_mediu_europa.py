from autor import Lectie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_ONU = ["Organizația Națiunilor Unite – Member States: Romania (14.12.1955)", "Ministerul Afacerilor Externe – România la ONU"]
S_NATO = ["NATO – Member countries (Romania, 29.03.2004)", "Ministerul Afacerilor Externe – România în NATO"]
S_UE = ["Uniunea Europeană – Țările UE: România (european-union.europa.eu)", "Ministerul Afacerilor Externe – România în UE"]
S_SCH = ["Consiliul UE, decizia din 12.12.2024 – ridicarea controalelor la frontierele terestre cu România și Bulgaria", "Comisia Europeană – Schengen Area"]
S_ODD = ["ONU – Agenda 2030 și cele 17 Obiective de Dezvoltare Durabilă (sdgs.un.org)", "Departamentul pentru Dezvoltare Durabilă (Guvernul României)"]
S_N2000 = ["Agenția Europeană de Mediu (EEA) – Natura 2000 barometer", "Ministerul Mediului – Rețeaua Natura 2000 în România"]
S_UNESCO = ["UNESCO World Heritage Centre – Romania: properties inscribed", "Ministerul Culturii – Monumente UNESCO din România"]
S_RET = ["Parcul Național Retezat (retezat.ro) – istoric: primul parc național (1935)", "Wikipedia (ro) – Parcul Național Retezat"]
S_CARN = ["Comisia Europeană (DG Mediu) – Large Carnivores in the EU: România", "WWF România – Carnivore mari"]
S_PADURI = ["Comisia Europeană – Primary and old-growth forests in the EU", "UNESCO – Ancient and Primeval Beech Forests of the Carpathians and Other Regions of Europe"]


def unitate():
    # ================================================================ S35a Calitatea mediului
    Q = Lectie(8, "VIII-S35-calitatea-mediului-inconjurator-romania", "Calitatea mediului înconjurător în România",
               "Cât de curat e aerul, apa și solul din jurul tău?",
               [("Probleme de mediu", "Poluarea aerului – în marile orașe (trafic, încălzire) și lângă zone industriale. Poluarea apei – din ape uzate netratate, deșeuri pe malurile râurilor. Degradarea solului – eroziune, alunecări, salinizare, poluare cu reziduuri.\nDefrișările ilegale, depozitarea necontrolată a deșeurilor, braconajul și pierderea biodiversității sunt și ele probleme."),
                ("Evoluții recente", "După 1990 și mai ales după aderarea la UE (2007), multe fabrici poluante s-au închis sau s-au modernizat, s-au construit stații de epurare și depozite ecologice, a crescut colectarea selectivă.\nRomânia are aproape un sfert din teritoriu în rețeaua europeană de arii protejate Natura 2000 și păduri virgine printre ultimele din Europa."),
                ("Ce putem face", "Colectare selectivă și reciclare, economie de energie și apă, transport public și bicicletă, plantarea de copaci, participarea la ecologizări, respectarea regulilor în ariile protejate.")],
               stiaica="Pădurile seculare de fag din Carpații României fac parte din patrimoniul mondial UNESCO, alături de păduri din alte 17 țări europene.",
               ref=REF.format("Calitatea mediului înconjurător în România. Evoluții recente"), prefix="VIII35a")
    Q.s(2, "3.2", "Asociază problema de mediu cu o cauză.", [("poluarea aerului în orașe", "traficul și încălzirea"), ("poluarea râurilor", "ape uzate netratate"), ("eroziunea solului", "defrișarea pantelor"), ("pierderea biodiversității", "braconajul și distrugerea habitatelor")], "Probleme și cauze.")
    Q.a(1, "4.3", "Ce înseamnă colectarea selectivă?", "separarea deșeurilor pe categorii: hârtie, plastic și metal, sticlă, resturi organice", ["arderea deșeurilor", "aruncarea tuturor la un loc", "îngroparea lor în curte"], "Permite reciclarea.")
    Q.a(2, "3.2", "Ce parte din teritoriul României e în rețeaua Natura 2000?", "aproape un sfert", ["aproape nimic", "toată țara", "jumătate exact"], "Situri pentru specii și habitate.", surse=S_N2000)
    Q.a(2, "3.4", "Ce păduri din România sunt în patrimoniul mondial UNESCO?", "pădurile seculare (virgine) de fag din Carpați", ["pădurile de molid plantate", "parcurile din orașe", "pădurile tropicale"], "Înscrise în 2017.", surse=S_PADURI)
    Q.a(2, "3.3", "Ce s-a schimbat după aderarea la UE în protecția mediului?", "s-au construit stații de epurare, depozite ecologice și a crescut reciclarea", ["s-au deschis mai multe fabrici poluante", "s-a interzis reciclarea", "nimic"], "Legislația europeană de mediu.")
    Q.a(2, "3.2", "De unde vine poluarea aerului în București?", "mai ales din trafic, încălzire și construcții", ["din vulcani", "din Marea Neagră", "din ghețari"], "Particule fine și noxe.")
    Q.a(2, "4.3", "Ce sunt tăierile ilegale de pădure?", "tăierea copacilor fără autorizație", ["plantarea de copaci", "curățenia pădurii", "vânătoarea autorizată"], "Afectează solul, apele și animalele.")
    Q.a(2, "3.4", "Ce carnivore mari, rare în restul Europei, mai trăiesc în număr mare în Carpații României?", "ursul, lupul și râsul", ["leul și tigrul", "ursul polar", "jaguarul"], "Indicator al pădurilor sănătoase.", surse=S_CARN)
    Q.p(2, "2.2", "Atinge pe harta României Parcul Național Retezat.", "romania", 45.37, 22.85, "Retezat", 40, "Primul parc național (1935).", surse=S_RET)
    Q.p(3, "2.2", "Atinge pe harta României Munții Făgăraș, cu păduri virgine importante.", "romania", 45.6, 24.7, "Făgăraș", 50, "În Carpații Meridionali.")
    Q.adev(2, "3.3", "Calitatea mediului în România nu s-a schimbat deloc după 1990.", False, "Fals: multe surse de poluare au scăzut, dar există încă probleme.")
    Q.adev(2, "4.3", "Reciclarea reduce cantitatea de deșeuri depozitate.", True, "Adevărat.")
    Q.l(2, "4.3", "Completează.", "Separarea deșeurilor se numește colectare [selectivă]; rețeaua europeană de arii protejate se numește Natura [2000].", ["comună", "2007"], "Protecția mediului.", surse=S_N2000)
    Q.l(2, "3.4", "Completează.", "Primul parc național al României este [Retezat], înființat în anul [1935].", ["Bucegi", "1990"], "Arii protejate.", surse=S_RET)
    Q.g(3, "2.2", "Graficul arată rata de reciclare într-un oraș imaginar. Ce tendință observi?", grafic("profil", "Rata de reciclare a deșeurilor (oraș imaginar)", [("2015", 8), ("2018", 13), ("2021", 20), ("2024", 28)], "%"), "reciclarea crește, dar e încă mică", ["reciclarea scade", "toate deșeurile sunt reciclate", "nu se schimbă"], "Mai e mult de făcut.")
    Q.a(3, "4.2", "Compară calitatea aerului dintr-un oraș mare cu cea dintr-un sat de munte.", "în orașul mare aerul e mai poluat din cauza traficului; la munte aerul e mai curat", ["sunt identice", "satul e mai poluat", "orașul nu are poluare"], "Surse diferite de poluare.")
    Q.d(2, "2.2", "Ce rezervație a biosferei, amenințată de poluare și braconaj, e marcată pe hartă?", "romania", 45.1, 29.3, "Delta Dunării", ["Parcul Retezat", "Munții Apuseni", "Bucegi"], "Patrimoniu UNESCO.")
    Q.a(2, "4.3", "Ce poți face ca elev pentru calitatea mediului?", "reciclezi, participi la ecologizări, economisești apă și energie", ["arunci deșeuri pe stradă", "lași apa să curgă", "arzi plasticul"], "Gesturi zilnice.")
    Q.a(2, "3.2", "De ce gropile de gunoi neecologice sunt periculoase?", "poluează solul și apele subterane și emit gaze", ["îmbogățesc solul", "sunt locuri de joacă", "nu au efecte"], "Au fost închise multe după 2007.")
    Q.a(2, "3.3", "Ce sunt stațiile de epurare?", "instalații care curăță apele uzate înainte de a ajunge în râuri", ["fabrici de apă minerală", "hidrocentrale", "fântâni"], "Protejează râurile.")
    Q.a(2, "4.3", "Ce înseamnă „amprentă ecologică”?", "cât consumă o persoană din resursele naturii", ["o urmă de animal", "un tip de hartă", "o rocă"], "Cu cât e mai mică, cu atât mai bine.")
    Q.a(2, "3.2", "Ce problemă a apărut în zonele miniere închise?", "halde de steril și ape acide care poluează solul și râurile", ["mai mulți turiști", "aer mai curat imediat", "nicio problemă"], "Ecologizarea fostelor mine e necesară.")
    Q.a(2, "4.3", "Ce înseamnă un sit Natura 2000?", "un loc protejat pentru specii și habitate importante la nivel european", ["o zonă industrială", "un nou oraș", "o autostradă"], "Activitățile sunt reglementate.")
    Q.a(3, "4.2", "Ce legătură există între defrișări și inundații în Subcarpații Buzăului?", "fără păduri, apa curge repede la vale, produce viituri și alunecări", ["nicio legătură", "defrișările opresc inundațiile", "pădurile produc inundații"], "Pădurea reține apa.")
    Q.a(2, "3.4", "Ce instituție anunță calitatea aerului în timp real în România?", "rețeaua națională de monitorizare a calității aerului (calitateaer.ro)", ["ANM pentru cutremure", "Poliția", "Banca Națională"], "Stații de măsurare în orașe.")
    Q.a(2, "4.3", "Cum ajută bicicleta calitatea mediului?", "nu poluează și reduce traficul", ["poluează mult", "consumă benzină", "nu are niciun efect"], "Piste de biciclete în orașe.")
    Q.a(2, "3.2", "Ce poluant afectează solul din agricultura intensivă?", "pesticidele și îngrășămintele în exces", ["humusul", "râmele", "frunzele căzute"], "Se recomandă folosirea cu măsură.")
    Q.a(2, "3.3", "Ce plantă invazivă, care produce alergii, e răspândită în sudul și vestul României?", "ambrozia", ["floarea de colț", "bujorul de munte", "laleaua pestriță"], "Legea obligă la distrugerea ei.")
    Q.a(3, "4.2", "Ce înseamnă un mediu „de calitate” pentru o comunitate?", "aer și apă curate, deșeuri gestionate, spații verzi, natură protejată", ["multe fabrici fără filtre", "trafic intens", "fără parcuri"], "Mediul influențează sănătatea.")

    Q.a(2, "3.3", "Ce tip de container folosești pentru sticlele de sticlă?", "verde", ["galben", "albastru", "roșu"], "Galben – plastic și metal; albastru – hârtie.")

    # ================================================================ S35b Resurse, populație, dezvoltare sustenabilă
    S = Lectie(8, "VIII-S35-resurse-populatie-elemente-dezvoltarii", "Resurse, populație și elemente ale dezvoltării sustenabile",
               "Cum poate România să se dezvolte fără să-și distrugă resursele?",
               [("Dezvoltare sustenabilă", "Dezvoltarea sustenabilă (durabilă) înseamnă să satisfacem nevoile de azi fără să compromitem posibilitatea generațiilor viitoare de a-și satisface nevoile lor. Are trei piloni: economic, social și de mediu.\nONU a adoptat în 2015 Agenda 2030, cu 17 Obiective de Dezvoltare Durabilă: fără sărăcie, educație de calitate, energie curată, orașe durabile, acțiune climatică etc."),
                ("România: resurse și populație", "Resurse: soluri fertile, păduri, ape, petrol și gaze, energie hidro, eoliană și solară, peisaje pentru turism. Provocări: scăderea și îmbătrânirea populației, emigrarea tinerilor, diferențele dintre regiuni, dependența de unele importuri."),
                ("Soluții", "Educație și inovare, energie regenerabilă, agricultură modernă și ecologică, turism durabil, infrastructură, păstrarea tinerilor în țară, folosirea responsabilă a fondurilor europene.")],
               stiaica="Expresia „dezvoltare durabilă” a fost definită în Raportul Brundtland al ONU, publicat în 1987, cu titlul „Viitorul nostru comun”.",
               ref=REF.format("Resurse, populație și elemente ale dezvoltării sustenabile"), prefix="VIII35b")
    S.a(1, "1.1", "Ce înseamnă dezvoltare sustenabilă?", "dezvoltare care satisface nevoile de azi fără să compromită viitorul", ["dezvoltare cât mai rapidă cu orice preț", "oprirea dezvoltării", "exploatarea totală a resurselor"], "Definiția Brundtland (1987).")
    S.a(2, "3.1", "Câte Obiective de Dezvoltare Durabilă are Agenda 2030 a ONU?", "17", ["3", "27", "100"], "Adoptate în 2015.", surse=S_ODD)
    S.s(2, "3.2", "Asociază pilonul dezvoltării durabile cu un exemplu.", [("economic", "locuri de muncă și firme"), ("social", "educație și sănătate pentru toți"), ("de mediu", "aer și apă curate, natură protejată")], "Cei trei piloni.")
    S.s(2, "3.3", "Asociază resursa României cu o folosire durabilă.", [("pădurea", "tăiere controlată și replantare"), ("vântul din Dobrogea", "parcuri eoliene"), ("solul fertil", "rotația culturilor"), ("peisajele montane", "ecoturism")], "Folosirea durabilă.")
    S.a(2, "3.3", "Ce provocare demografică are România?", "scăderea și îmbătrânirea populației", ["creșterea foarte rapidă a populației", "prea mulți copii", "nicio provocare"], "Spor natural negativ și emigrare.")
    S.a(2, "4.3", "Ce poate face o țară pentru a-și păstra tinerii?", "locuri de muncă bine plătite, educație, locuințe, servicii publice bune", ["închiderea universităților", "salarii mai mici", "nimic"], "Atractivitate.")
    S.a(2, "3.3", "Ce sursă de energie e cea mai durabilă dintre acestea?", "energia solară", ["cărbunele", "petrolul", "lemnul tăiat fără replantare"], "Regenerabilă și curată.")
    S.a(2, "3.4", "În ce an a fost publicat Raportul Brundtland, care a definit dezvoltarea durabilă?", "1987", ["1945", "2007", "2015"], "„Viitorul nostru comun”.")
    S.a(2, "3.3", "Ce obiectiv ODD se referă la clima Pământului?", "„Acțiune climatică” (obiectivul 13)", ["„Viața acvatică” (14)", "„Parteneriate” (17)", "„Fără foamete” (2)"], "Reducerea emisiilor și adaptarea.", surse=S_ODD)
    S.p(2, "2.2", "Atinge pe harta României Dobrogea, unde energia vântului e valorificată durabil.", "romania", 44.5, 28.4, "Dobrogea", 70, "Parcuri eoliene.")
    S.p(3, "2.2", "Atinge pe harta României Regiunea Nord-Est (Iași), cu cea mai tânără populație din țară.", "romania", 47.16, 27.59, "Iași / Nord-Est", 80, "Natalitate ceva mai ridicată decât media.")
    S.adev(2, "3.3", "Dezvoltarea durabilă ține cont doar de economie.", False, "Fals: ține cont de economie, societate și mediu.")
    S.adev(2, "4.3", "Educația e un factor important al dezvoltării durabile.", True, "Adevărat: ODD 4 – educație de calitate.", surse=S_ODD)
    S.l(2, "1.1", "Completează.", "Agenda [2030] a ONU are [17] Obiective de Dezvoltare Durabilă.", ["2007", "27"], "Agenda ONU.", surse=S_ODD)
    S.l(2, "3.2", "Completează.", "Pilonii dezvoltării durabile sunt economic, [social] și de [mediu].", ["militar", "turism"], "Trei piloni.")
    S.g(3, "2.2", "Graficul arată ponderea energiei regenerabile într-o țară imaginară. Ce tendință observi?", grafic("profil", "Energie din surse regenerabile în consumul final (țară imaginară)", [("2005", 17), ("2012", 22), ("2018", 24), ("2024", 28)], "%"), "ponderea crește treptat", ["scade", "rămâne aceeași", "e 100 %"], "Tranziția energetică.")
    S.o(3, "4.2", "Ordonează pașii unui proiect durabil pentru școală.", ["identifici problema (de ex., risipa de energie)", "măsori situația actuală", "propui soluții", "aplici soluțiile", "măsori rezultatele"], "Etapele proiectului", "Planifică, aplică, verifică.")
    S.a(3, "4.2", "Compară o economie bazată pe cărbune cu una bazată pe energie regenerabilă.", "cea pe cărbune poluează și depinde de o resursă care se termină; cea regenerabilă e curată și durabilă", ["sunt identice", "cărbunele e regenerabil", "energia regenerabilă poluează mai mult"], "Sustenabilitate.")
    S.d(2, "2.2", "Ce județ cu orașul nostru, cu resurse variate (agricultură, păduri, turism geologic), e marcat?", "romania", 45.25, 26.75, "Buzău", ["Brăila", "Vrancea", "Prahova"], "Județul Buzău.")
    S.a(2, "4.3", "Ce înseamnă „economie circulară”?", "produsele sunt reparate, refolosite și reciclate, nu aruncate", ["toate produsele se aruncă după o folosire", "comerțul în cerc", "o economie fără bani"], "Deșeurile devin resurse.")
    S.a(2, "3.3", "Ce înseamnă „turism durabil”?", "turism care aduce venituri fără să distrugă natura și cultura locală", ["turism cu orice preț", "turism doar în orașe", "turism cu multe deșeuri"], "Ex.: geoparcul Ținutul Buzăului.")
    S.a(2, "4.3", "De ce e importantă egalitatea de șanse între regiuni?", "toți oamenii să aibă acces la educație, sănătate, locuri de muncă", ["ca toți să locuiască în capitală", "ca regiunile să dispară", "nu e importantă"], "Coeziune.")
    S.a(2, "3.3", "Ce resursă a României e importantă pentru agricultura durabilă?", "solurile fertile (cernoziomurile)", ["petrolul", "aurul", "sarea"], "Trebuie protejate de eroziune.")
    S.a(2, "4.3", "Ce poate face un fermier pentru agricultură durabilă?", "rotația culturilor, irigații eficiente, mai puține chimicale", ["arde miriștile", "ară în pantă", "taie perdelele forestiere"], "Agricultură responsabilă.")
    S.a(2, "3.3", "Ce înseamnă „inovare”?", "idei, tehnologii și metode noi care rezolvă probleme", ["copierea a ceea ce există", "oprirea cercetării", "închiderea școlilor"], "Motor al dezvoltării.")
    S.a(3, "4.2", "De ce o populație îmbătrânită pune presiune pe economie?", "sunt mai puțini oameni care muncesc și mai mulți pensionari", ["sunt mai mulți muncitori", "nu există pensii", "fără motiv"], "Raportul dintre activi și pensionari.")
    S.a(2, "3.3", "Ce înseamnă „mobilitate durabilă”?", "deplasare cu transport public, tren, bicicletă, mers pe jos, mașini electrice", ["mai multe mașini cu benzină", "doar avionul", "nicio deplasare"], "Mai puțină poluare.")
    S.a(2, "4.3", "Ce ODD privește orașele?", "„Orașe și comunități durabile” (obiectivul 11)", ["„Fără sărăcie” (1)", "„Viața terestră” (15)", "„Apă curată” (6)"], "Orașe sigure, verzi, incluzive.", surse=S_ODD)
    S.a(2, "3.3", "Ce înseamnă reciclarea deșeurilor electronice?", "recuperarea metalelor și a altor materiale din aparatele vechi", ["aruncarea lor la gunoi", "arderea lor", "îngroparea lor"], "Se predau la puncte de colectare.")

    S.a(2, "3.3", "Ce înseamnă ODD 7, „Energie curată și la prețuri accesibile”?", "acces pentru toți la energie modernă, sigură și curată", ["interzicerea energiei", "doar energie pe cărbune", "energie doar pentru orașe"], "Unul dintre cele 17 obiective.", surse=S_ODD)

    # ================================================================ S35c Valorile naturale și culturale
    V = Lectie(8, "VIII-S35-valorile-naturale-culturale-romaniei", "Valorile naturale și culturale ale României",
               "Ce comori ale României sunt recunoscute de toată lumea?",
               [("Patrimoniul natural", "Delta Dunării (patrimoniu mondial UNESCO și Rezervație a Biosferei), pădurile seculare de fag din Carpați (UNESCO), parcuri naționale (Retezat, Piatra Craiului, Rodnei, Cheile Bicazului–Hășmaș, Ceahlău, Domogled–Valea Cernei și altele), geoparcurile UNESCO (Hațeg, Ținutul Buzăului).\nPeșteri, chei, lacuri glaciare, vulcani noroioși, fauna de carnivore mari."),
                ("Patrimoniul cultural", "Situri UNESCO: bisericile pictate din nordul Moldovei, bisericile de lemn din Maramureș, satele cu biserici fortificate din Transilvania, centrul istoric al Sighișoarei, Mănăstirea Horezu, cetățile dacice din Munții Orăștiei, peisajul minier de la Roșia Montană, frontierele Imperiului Roman în Dacia.\nPatrimoniu imaterial: Călușul, doina, colindatul în ceată bărbătească, ceramica de Horezu, mărțișorul, tehnicile tradiționale de țesut."),
                ("Personalități", "Mihai Eminescu, Ion Creangă, George Enescu, Constantin Brâncuși, Nicolae Grigorescu, Emil Racoviță, Henri Coandă, Traian Vuia, Aurel Vlaicu, Ana Aslan, Nadia Comăneci.")],
               stiaica="Mărțișorul a fost înscris în patrimoniul imaterial UNESCO în 2017, împreună cu Bulgaria, Republica Moldova și Macedonia de Nord.",
               ref=REF.format("Valorile naturale și culturale ale României"), prefix="VIII35c")
    V.s(2, "3.4", "Asociază situl UNESCO cu regiunea.", [("bisericile pictate", "nordul Moldovei"), ("bisericile de lemn", "Maramureș"), ("cetățile dacice", "Munții Orăștiei"), ("Mănăstirea Horezu", "Oltenia (Vâlcea)")], "Patrimoniu UNESCO.", surse=S_UNESCO)
    V.s(2, "3.4", "Asociază personalitatea cu domeniul.", [("George Enescu", "muzică"), ("Constantin Brâncuși", "sculptură"), ("Henri Coandă", "aviație"), ("Emil Racoviță", "biologie și explorare")], "Personalități românești.")
    V.a(1, "3.4", "Ce rezervație naturală e patrimoniu mondial UNESCO?", "Delta Dunării", ["Lacul Snagov", "Parcul Cișmigiu", "Muntele Tâmpa"], "Din 1991.", surse=S_UNESCO)
    V.a(2, "3.4", "Ce geoparc UNESCO se află în județul Buzău?", "Geoparcul Ținutul Buzăului", ["Geoparcul Hațeg", "Geoparcul Mehedinți", "Delta Dunării"], "Recunoscut în 2022.", surse=["UNESCO – Global Geoparks: Buzău Land (2022)", "Asociația Ținutul Buzăului (geoparc)"])
    V.a(2, "3.4", "Ce geoparc UNESCO e cunoscut pentru dinozaurii pitici?", "Geoparcul Țara Hațegului", ["Ținutul Buzăului", "Delta Dunării", "Munții Apuseni"], "Fosile de dinozauri pitici.")
    V.a(2, "3.4", "Ce tradiție de primăvară a României e în patrimoniul imaterial UNESCO?", "mărțișorul", ["Halloween", "Anul Nou Chinezesc", "Ziua Recunoștinței"], "Înscris în 2017.")
    V.a(2, "3.4", "Ce dans ritual românesc e în patrimoniul imaterial UNESCO?", "Călușul", ["Tango", "Valsul", "Flamenco"], "Înscris în 2005 (inițial ca Capodoperă), apoi în lista reprezentativă.")
    V.a(2, "3.4", "Ce meșteșug din Vâlcea e în patrimoniul imaterial UNESCO?", "ceramica de Horezu", ["sticla de Murano", "porțelanul de Meissen", "dantela de Bruges"], "Înscris în 2012.")
    V.a(2, "3.4", "Ce inventator român a descoperit fenomenul aerodinamic care îi poartă numele?", "Henri Coandă („efectul Coandă”)", ["Traian Vuia", "Aurel Vlaicu", "Hermann Oberth"], "A construit și avionul Coandă-1910.")
    V.a(2, "3.4", "Ce pionier român al aviației a zburat în 1906, lângă Paris, cu un aparat care a decolat doar cu mijloace proprii?", "Traian Vuia", ["Henri Coandă", "Aurel Vlaicu", "Iuri Gagarin"], "Zborul de la Montesson, din 18 martie 1906.")
    V.p(2, "3.4", "Atinge pe harta României Mănăstirea Horezu.", "romania", 45.17, 24.0, "Horezu", 35, "Județul Vâlcea.", surse=S_UNESCO)
    V.p(2, "3.4", "Atinge pe harta României Sarmizegetusa Regia, capitala dacilor.", "romania", 45.62, 23.31, "Sarmizegetusa Regia", 35, "În Munții Orăștiei.", surse=S_UNESCO)
    V.p(3, "3.4", "Atinge pe harta României Roșia Montană.", "romania", 46.31, 23.13, "Roșia Montană", 35, "În Munții Apuseni.", surse=S_UNESCO)
    V.adev(2, "3.4", "Bisericile pictate din nordul Moldovei sunt în patrimoniul mondial UNESCO.", True, "Adevărat, din 1993.", surse=S_UNESCO)
    V.adev(2, "3.4", "România nu are niciun element în patrimoniul imaterial UNESCO.", False, "Fals: Călușul, doina, ceramica de Horezu, mărțișorul și altele.")
    V.l(2, "3.4", "Completează.", "Capitala dacilor, [Sarmizegetusa] Regia, e în Munții [Orăștiei].", ["Apulum", "Apuseni"], "Patrimoniu dacic.", surse=S_UNESCO)
    V.l(2, "3.4", "Completează.", "„Coloana fără sfârșit” e opera lui [Brâncuși]; „Luceafărul” e opera lui [Eminescu].", ["Enescu", "Creangă"], "Valori culturale.")
    V.g(3, "2.2", "Graficul arată numărul de vizitatori pe an la trei obiective imaginare. Care e cel mai vizitat?", grafic("bare", "Vizitatori pe an (obiective imaginare)", [("castelul A", 900), ("mănăstirea B", 400), ("peștera C", 150)], "mii"), "castelul A", ["mănăstirea B", "peștera C", "egal"], "900 de mii de vizitatori.")
    V.o(3, "3.4", "Ordonează în timp aceste valori culturale, de la cea mai veche.", ["cetățile dacice (sec. I î.Hr. – I d.Hr.)", "bisericile pictate din Moldova (sec. XV–XVI)", "Castelul Peleș (sec. XIX)", "Palatul Parlamentului (sec. XX)"], "Cronologic", "Patrimoniu din epoci diferite.")
    V.a(3, "4.2", "Compară patrimoniul natural cu cel cultural.", "patrimoniul natural e creat de natură (Delta, păduri); cel cultural e creat de oameni (biserici, cetăți, tradiții)", ["sunt identice", "cel natural e creat de oameni", "cel cultural e creat de natură"], "Două tipuri de patrimoniu.")
    V.d(2, "3.4", "Ce mănăstire pictată din Bucovina, cu „albastrul” celebru, e marcată pe hartă?", "romania", 47.52, 25.86, "Voroneț", ["Horezu", "Putna", "Curtea de Argeș"], "Patrimoniu UNESCO.", surse=S_UNESCO)
    V.a(2, "3.4", "Ce sportivă română a obținut prima notă 10 din istoria gimnasticii olimpice, în 1976?", "Nadia Comăneci", ["Simona Halep", "Gabriela Szabo", "Ivan Patzaichin"], "La Montréal.")
    V.a(2, "3.4", "Ce medic român a creat primul institut de geriatrie din lume?", "Ana Aslan", ["Victor Babeș", "Carol Davila", "Nicolae Paulescu"], "La București, în 1952.")
    V.a(2, "3.4", "Ce rol are patrimoniul pentru turism?", "atrage vizitatori din țară și din străinătate", ["alungă turiștii", "nu are niciun rol", "înlocuiește hotelurile"], "Turism cultural.")
    V.a(2, "4.3", "Cum protejăm patrimoniul cultural?", "restaurăm monumentele, nu le distrugem, învățăm și transmitem tradițiile", ["scriem pe ziduri", "luăm pietre ca suvenir", "ignorăm tradițiile"], "Responsabilitatea tuturor.")
    V.a(2, "3.4", "Ce sit UNESCO din 2024 cuprinde castre romane din România?", "Frontierele Imperiului Roman – Dacia", ["Pădurile de fag", "Delta Dunării", "Sighișoara"], "Limesul dacic.", surse=S_UNESCO)
    V.a(2, "3.4", "Ce scriitor român a scris „Amintiri din copilărie”?", "Ion Creangă", ["Mihai Eminescu", "Ion Luca Caragiale", "George Coșbuc"], "Despre copilăria de la Humulești.")
    V.a(2, "3.4", "Ce oraș al Moldovei a fost capitala lui Ștefan cel Mare?", "Suceava", ["Iași", "Bacău", "Botoșani"], "Cetatea de Scaun a Sucevei.")
    V.a(2, "3.4", "Ce valoare naturală rară e în județul Buzău, legată de chihlimbar?", "chihlimbarul de Buzău (romanit), expus la Muzeul de la Colți", ["aurul din Apuseni", "sarea din Turda", "marmura din Ruschița"], "O rășină fosilă de milioane de ani.")

    V.a(2, "3.4", "Ce tradiție a colindatului e în patrimoniul imaterial UNESCO?", "colindatul în ceată bărbătească", ["sorcova individuală", "Halloween", "Moș Nicolae"], "Înscris în 2013, împreună cu Republica Moldova.")

    # ================================================================ S35d România în ONU, NATO, UE
    O = Lectie(8, "VIII-S35-romania-ca-membru-onu", "România ca membru ONU, NATO și UE",
               "Ce înseamnă pentru tine că România e membră a Uniunii Europene?",
               [("ONU și NATO", "România e membră a Organizației Națiunilor Unite (ONU) din 14 decembrie 1955. ONU urmărește pacea, drepturile omului și dezvoltarea. România participă la misiuni ONU de menținere a păcii.\nRomânia e membră a Alianței Nord-Atlantice (NATO) din 29 martie 2004: o alianță de apărare colectivă („unul pentru toți, toți pentru unul”)."),
                ("Uniunea Europeană", "România e membră a Uniunii Europene din 1 ianuarie 2007. Cetățenii români pot circula, munci și studia liber în statele UE. România primește fonduri europene pentru drumuri, școli, spitale, agricultură.\nDin 2024 (aerian și maritim) și din 1 ianuarie 2025 (terestru), România face parte complet din spațiul Schengen, fără controale la frontierele interne. România nu a adoptat încă moneda euro."),
                ("Alte organizații", "România face parte și din Consiliul Europei, OSCE, Organizația Mondială a Comerțului, Organizația Internațională a Francofoniei, Organizația Cooperării Economice a Mării Negre (cu sediul la Istanbul) și altele.")],
               stiaica="Românii pot folosi cardul european de sănătate și pot studia cu programul Erasmus+ în orice stat al Uniunii Europene.",
               ref=REF.format("România ca membru ONU, NATO și UE"), prefix="VIII35d")
    O.s(2, "3.4", "Asociază organizația cu anul aderării României.", [("ONU", "1955"), ("NATO", "2004"), ("Uniunea Europeană", "2007"), ("spațiul Schengen (complet)", "2025")], "Aderări.", surse=S_UE)
    O.a(1, "3.4", "De când e România membră a Uniunii Europene?", "1 ianuarie 2007", ["1955", "2004", "2025"], "Împreună cu Bulgaria.", surse=S_UE)
    O.a(2, "3.4", "De când e România membră NATO?", "29 martie 2004", ["2007", "1990", "1955"], "Alianța Nord-Atlantică.", surse=S_NATO)
    O.a(2, "3.4", "De când e România membră ONU?", "14 decembrie 1955", ["1918", "2004", "2007"], "Organizația Națiunilor Unite.", surse=S_ONU)
    O.a(2, "3.4", "De când face România parte complet din spațiul Schengen?", "1 ianuarie 2025", ["2007", "2004", "nu face parte"], "Din martie 2024 pentru frontierele aeriene și maritime.", surse=S_SCH)
    O.a(2, "1.1", "Ce este NATO?", "o alianță de apărare colectivă a unor state din Europa și America de Nord", ["o bancă", "o organizație de turism", "un campionat sportiv"], "Atacul asupra unui membru e considerat atac asupra tuturor.", surse=S_NATO)
    O.a(2, "1.1", "Ce urmărește ONU?", "pacea, drepturile omului, dezvoltarea și cooperarea între state", ["războiul", "comerțul doar cu arme", "turismul spațial"], "Fondată în 1945.", surse=S_ONU)
    O.a(2, "3.3", "Ce drepturi au cetățenii români în Uniunea Europeană?", "pot circula, munci și studia liber în orice stat membru", ["nu pot călători", "au nevoie de viză în fiecare țară UE", "nu au niciun drept nou"], "Libera circulație.")
    O.a(2, "3.3", "Ce moneda folosește România?", "leul", ["euro", "dolarul", "lira"], "România nu a adoptat încă euro.")
    O.a(2, "3.3", "Ce înseamnă spațiul Schengen?", "un grup de state europene fără controale la frontierele dintre ele", ["o monedă", "o armată", "un program TV"], "Circulație liberă a persoanelor.", surse=S_SCH)
    O.p(2, "3.1", "Atinge pe hartă Bruxelles, unde au sediul multe instituții UE și NATO.", "lume", 50.85, 4.35, "Bruxelles", 300, "Bruxelles e capitala Belgiei.")
    O.p(3, "3.1", "Atinge pe hartă New York, unde e sediul ONU.", "lume", 40.75, -73.97, "New York", 400, "Sediul ONU e în Manhattan.")
    O.adev(2, "3.4", "România a aderat la UE înainte de a adera la NATO.", False, "Fals: NATO în 2004, UE în 2007.", surse=S_NATO)
    O.adev(2, "3.3", "Fondurile europene ajută la construirea de drumuri și școli în România.", True, "Adevărat.")
    O.l(2, "3.4", "Completează.", "România e membră NATO din [2004] și a Uniunii Europene din [2007].", ["1955", "2025"], "Aderări.", surse=S_UE)
    O.l(2, "3.3", "Completează.", "Sediul ONU e la [New York], iar multe instituții ale UE sunt la [Bruxelles].", ["Geneva", "Paris"], "Sedii.")
    O.g(3, "2.2", "Graficul arată (schematic) fondurile europene primite de o țară imaginară pe perioade. Ce observi?", grafic("bare", "Fonduri europene alocate (țară imaginară, miliarde euro)", [("2007–2013", 20), ("2014–2020", 31), ("2021–2027", 46)], "miliarde euro"), "fondurile cresc de la o perioadă la alta", ["scad", "rămân la fel", "dispar"], "Perioadele de programare de 7 ani.")
    O.o(3, "3.4", "Ordonează aderările României cronologic.", ["ONU (1955)", "NATO (2004)", "UE (2007)", "Schengen complet (2025)"], "Cronologic", "Integrarea euro-atlantică.", surse=S_UE)
    O.a(3, "4.2", "Compară NATO cu Uniunea Europeană.", "NATO e o alianță militară de apărare; UE e o uniune economică și politică", ["sunt identice", "UE e o alianță militară", "NATO e o piață comună"], "Roluri diferite.")
    O.d(2, "3.1", "Ce oraș, gazda Parlamentului European, e marcat pe hartă?", "lume", 48.58, 7.75, "Strasbourg", ["Bruxelles", "Luxemburg", "Paris"], "Parlamentul European are sesiuni la Strasbourg.")
    O.a(2, "3.3", "Ce program european permite elevilor și studenților să studieze în altă țară?", "Erasmus+", ["Schengen", "Euro", "NATO"], "Și profesorilor.")
    O.a(2, "3.3", "Ce organizație reunește statele de la Marea Neagră pentru cooperare economică?", "Organizația Cooperării Economice a Mării Negre", ["ASEAN", "Mercosur", "Uniunea Africană"], "Sediul la Istanbul.")
    O.a(2, "3.3", "La ce organizație culturală a limbii franceze participă România?", "Organizația Internațională a Francofoniei", ["Commonwealth", "Liga Arabă", "OPEC"], "Franceza a fost mult învățată în România.")
    O.a(2, "3.4", "Ce eveniment din 1989 a deschis drumul României spre NATO și UE?", "Revoluția din decembrie 1989", ["Unirea din 1859", "Marea Unire din 1918", "Războiul de Independență din 1877"], "Trecerea la democrație.")
    O.a(2, "3.3", "Cum poți vota pentru Parlamentul European?", "la alegerile europene, o dată la 5 ani, de la 18 ani", ["nu poți vota", "doar în Belgia", "doar online, de la 10 ani"], "Cetățenii aleg europarlamentarii.")
    O.a(2, "3.3", "Ce baza militară NATO importantă e în România, lângă Constanța?", "Baza Mihail Kogălniceanu", ["Baza Bran", "Baza Sinaia", "Baza Sulina"], "Una dintre cele mai mari din regiune.")
    O.a(3, "4.2", "De ce poziția României la Marea Neagră e importantă pentru NATO și UE?", "e la granița de est a UE și NATO, la o mare cu importanță strategică", ["e în centrul Africii", "nu are importanță", "e la Polul Nord"], "Flancul estic.")
    O.a(2, "3.3", "Ce card îți permite tratament medical în alte state UE?", "cardul european de sănătate", ["cardul de bibliotecă", "carnetul de note", "buletinul de vot"], "Gratuit pentru asigurați.")
    O.a(2, "3.3", "Ce simbol are Uniunea Europeană?", "drapelul albastru cu 12 stele aurii", ["drapelul roșu cu o stea", "un vultur", "o cruce verde"], "Simbolul unității.")
    O.a(2, "3.3", "Ce înseamnă „integrare europeană” pentru economia României?", "acces la piața unică, investiții, fonduri, reguli comune", ["izolare", "taxe vamale mari cu UE", "închiderea fabricilor"], "Beneficii economice.")

    return Unitate(8, "u7-mediu-europa.json", "Caracteristici ale mediului înconjurător. România în Europa și în lume").add(Q, S, V, O)
