from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_ANM = ["Administrația Națională de Meteorologie (ANM) – Clima României", "Wikipedia – Climate of Romania"]
S_REC = ["ANM – extreme climatice (44,5 °C la Ion Sion, 1951; −38,5 °C la Bod, 1942)", "Wikipedia – Climate of Romania"]
S_DUN = ["ICPDR – Danube Basin facts", "Administrația Fluvială a Dunării de Jos – Dunărea pe teritoriul României"]
S_PDF = ["Hidroelectrica – Porțile de Fier I (hidroelectrica.ro)", "Encyclopaedia Britannica – Iron Gate"]
S_RAURI = ["INS – Anuarul Statistic al României: principalele râuri (lungime pe teritoriul României)", "Administrația Națională „Apele Române” – bazine hidrografice"]
S_MN = ["Encyclopaedia Britannica – Black Sea (suprafață ~436 400 km², adâncime maximă 2 212 m)", "Wikipedia – Black Sea"]
S_LACURI = ["INS / Administrația Națională „Apele Române” – lacuri", "Wikipedia (ro) – Lista lacurilor din România"]
S_DELTA = ["Administrația Rezervației Biosferei Delta Dunării (ddbra.ro)", "UNESCO World Heritage Centre – Danube Delta"]
S_CARN = ["Comisia Europeană (DG Mediu) – Large Carnivores in the EU: România", "WWF România – Carnivore mari"]
RS = (45.38, 27.05)


def unitate():
    # ================================================================ S13a Clima – factorii genetici
    F = Lectie(8, "VIII-S13-clima-factorii-genetici", "Clima României – factorii genetici",
               "De ce la Timișoara iernile sunt mai blânde decât la Iași?",
               [("Factori astronomici și geografici", "Poziția la jumătatea distanței dintre Ecuator și Polul Nord (paralela de 45° N) dă României o climă temperată, cu patru anotimpuri.\nPoziția față de Oceanul Atlantic, Marea Mediterană, Marea Neagră și față de uscatul Europei de Est face ca România să primească mase de aer diferite: climă temperat-continentală de tranziție."),
                ("Circulația maselor de aer", "Din vest vin mase de aer umed, oceanic (ploi, ierni blânde). Din est și nord-est vin mase de aer continental, uscat (ierni geroase, veri fierbinți, crivăț). Din sud-vest vin mase de aer cald mediteraneean (Banat, Oltenia). Din nord pot veni mase de aer rece, polar."),
                ("Relieful", "Carpații sunt o barieră: opresc parțial masele de aer, modifică direcția vânturilor și fac ca vestul să fie mai umed, iar estul mai uscat. Altitudinea scade temperatura și crește precipitațiile: apar etaje climatice (de câmpie, de dealuri și podișuri, de munte).")],
               stiaica="Pe vârful Omu (2 505 m), din Bucegi, temperatura medie anuală e sub 0 °C, în timp ce în Câmpia Română depășește 10 °C.",
               ref=REF.format("Clima – Factorii genetici"), prefix="VIII13a")
    F.a(1, "1.1", "Ce climă are România?", "temperat-continentală de tranziție", ["ecuatorială", "polară", "deșertică"], "Între influențele oceanice și cele continentale.", surse=S_ANM)
    F.a(2, "3.1", "Ce factor astronomic determină clima temperată a României?", "poziția la paralela de 45° N", ["apropierea de Ecuator", "apropierea de Polul Nord", "altitudinea Lunii"], "Unghiul de incidență al razelor solare e mediu.")
    F.s(2, "3.1", "Asociază masa de aer cu efectul ei.", [("oceanică, din vest", "ploi și ierni blânde"), ("continentală, din est", "ierni geroase și veri fierbinți"), ("mediteraneeană, din sud-vest", "căldură și ploi de toamnă"), ("polară, din nord", "răciri bruște")], "Masele de aer care influențează clima.")
    F.a(2, "3.2", "Ce rol au Carpații în climă?", "sunt o barieră care oprește parțial masele de aer și creează etaje climatice", ["nu au niciun rol", "încălzesc toată țara", "aduc musonul"], "Vestul e mai umed, estul mai uscat.")
    F.a(2, "2.2", "De ce vestul României e mai umed decât estul?", "primește masele de aer oceanic, iar Carpații le opresc spre est", ["pentru că e mai aproape de Marea Neagră", "pentru că e mai înalt peste tot", "pentru că are deșert"], "Influența Atlanticului scade spre est.")
    F.a(2, "2.2", "De ce Banatul și Oltenia au ierni mai blânde?", "primesc influențe mediteraneene (submediteraneene), din sud-vest", ["primesc aer polar", "sunt la munte", "sunt lângă Marea Neagră"], "Aici cresc și castani comestibili, liliac sălbatic.")
    F.a(2, "3.2", "De unde vine crivățul?", "din nord-est, din aerul rece continental", ["din sud-vest", "din Marea Mediterană", "din Oceanul Atlantic"], "Crivățul aduce ger și viscol în Moldova și Bărăgan.")
    F.a(2, "3.2", "Ce se întâmplă cu temperatura cu cât urci pe munte?", "scade (aproximativ 6 °C la fiecare 1 000 m)", ["crește", "rămâne aceeași", "devine 50 °C"], "De aceea sus e mai frig.")
    F.a(3, "3.2", "Dacă în Câmpia Română, la 100 m, sunt 20 °C, cam câte grade sunt pe un vârf de 2 100 m?", "aproximativ 8 °C", ["aproximativ 20 °C", "aproximativ 30 °C", "aproximativ −20 °C"], "2 000 m × 6 °C/1 000 m = 12 °C mai puțin.", ind="Scade aproximativ 6 °C la fiecare 1 000 m urcați.")
    F.p(2, "2.1", "Atinge pe harta României vârful Omu.", "romania", 45.45, 25.46, "Vârful Omu", 40, "Omu e în Munții Bucegi.")
    F.p(3, "2.1", "Atinge pe harta României Banatul, cu influențe submediteraneene.", "romania", 45.3, 21.8, "Banat", 70, "Banatul e în sud-vestul țării.")
    F.adev(2, "3.2", "Masele de aer oceanic aduc iarna ger puternic și secetă.", False, "Fals: aduc ierni blânde și ploi.")
    F.adev(2, "3.2", "Carpații fac ca vestul țării să fie mai umed decât estul.", True, "Adevărat.")
    F.l(2, "1.1", "Completează.", "Clima României este temperat-[continentală] de [tranziție].", ["oceanică", "deșert"], "Termenul exact.", surse=S_ANM)
    F.l(2, "3.2", "Completează.", "Vântul rece din nord-est se numește [crivăț]; influențele din sud-vest sunt [submediteraneene].", ["austru", "baltice"], "Crivăț, submediteraneene.")
    F.g(3, "2.2", "Graficul arată temperatura medie anuală la diferite altitudini în Carpați (valori aproximative). Ce observi?", grafic("profil", "Temperatura medie anuală după altitudine (aproximativ)", [("100 m", 11), ("500 m", 9), ("1 000 m", 6), ("1 500 m", 3), ("2 000 m", 0), ("2 500 m", -3)], "°C", "ANM – Clima României"), "temperatura scade cu altitudinea", ["temperatura crește", "rămâne constantă", "e mereu negativă"], "Etajarea climatică.", surse=S_ANM)
    F.o(3, "2.2", "Ordonează locurile de la cel mai cald la cel mai rece (medie anuală).", ["Câmpia Română", "Podișul Getic", "Subcarpați", "vârful Omu"], "De la cald la rece", "Altitudinea scade temperatura.")
    F.a(2, "3.1", "Ce influență climatică are Dobrogea, lângă mare?", "pontică (influența Mării Negre)", ["oceanică", "polară", "montană"], "Marea îndulcește temperaturile pe țărm.")
    F.a(2, "3.1", "Ce influență climatică are nordul Moldovei?", "baltică (scandinavo-baltică), cu aer mai umed și rece", ["mediteraneeană", "pontică", "tropicală"], "Influențele din nord.")
    F.d(2, "2.1", "Ce regiune cu cele mai puține precipitații din țară e marcată pe hartă?", "romania", 44.4, 28.4, "Dobrogea", ["Banatul", "Maramureșul", "Bucovina"], "În Dobrogea cad sub 400 l/m² pe an în unele zone.", surse=S_ANM)
    F.a(3, "4.2", "Compară clima de la Timișoara cu cea de la Iași.", "la Timișoara e mai umed și ierni mai blânde; la Iași iernile sunt mai geroase și verile mai uscate", ["sunt identice", "Iașiul are ierni mai blânde", "Timișoara e mai uscată"], "Vest – oceanic; est – continental.")
    F.a(2, "3.2", "Ce este foehnul?", "un vânt cald și uscat care coboară pe versanții munților", ["un vânt rece de la nord", "o ploaie", "o ceață"], "Apare, de exemplu, pe versanții Făgărașului.")
    F.a(2, "3.2", "Ce este austrul?", "un vânt uscat din sud-vest, care aduce secetă vara și ger uscat iarna", ["un vânt umed din vest", "un vânt rece din nord-est", "o briză marină"], "Bate în Oltenia și Muntenia.")
    F.a(2, "3.2", "Ce este briza marină?", "un vânt care bate ziua dinspre mare spre uscat, iar noaptea invers", ["un vânt de munte", "un uragan", "vânt din Siberia"], "Pe litoral vara.")
    F.a(3, "3.2", "De ce în depresiunile intramontane iarna e uneori mai frig decât pe versanți?", "aerul rece, greu, se adună în depresiune (inversiune termică)", ["pentru că sunt mai înalte", "pentru că bate foehnul", "pentru că e lângă mare"], "Ex.: Depresiunea Brașov, Ciuc.")
    F.a(2, "3.2", "Ce vânt local rece bate în Depresiunea Brașov?", "nemira", ["crivățul", "austrul", "briza"], "Nemira aduce viscol în sud-estul Transilvaniei.")
    F.a(2, "2.2", "Ce înseamnă „etaj climatic”?", "zona cu climă asemănătoare, la o anumită altitudine", ["un nor", "un vânt", "o clădire"], "Câmpie, deal, munte.")
    F.a(2, "3.3", "Cum influențează clima agricultura din Dobrogea?", "seceta obligă la irigații, dar soarele favorizează vița-de-vie", ["e prea ploios", "e prea frig pentru orice cultură", "nu o influențează"], "Murfatlar.")
    F.a(2, "1.2", "Unde se află orașul Râmnicu Sărat față de influențele climatice?", "în zona cu influențe continentale (est), cu crivăț iarna", ["în zona oceanică din vest", "în zona mediteraneeană", "în zona polară"], "Nord-estul Munteniei are veri calde și ierni geroase.")

    F.a(2, "3.1", "Ce înseamnă climă „de tranziție”, pentru România?", "între clima oceanică din vestul Europei și cea continentală din est", ["între clima polară și cea ecuatorială", "o climă care se schimbă zilnic", "o climă fără anotimpuri"], "România primește ambele influențe.")

    # ================================================================ S13b Elementele climatice
    E = Lectie(8, "VIII-S13-elementele-climatice", "Elementele climatice ale României",
               "Cât de cald și cât de ploios e, în medie, în România?",
               [("Temperatura", "Temperatura medie anuală scade de la sud la nord și de la câmpie la munte: peste 11 °C în sudul Câmpiei Române și pe litoral, 8–10 °C în dealuri și podișuri, sub 0 °C pe vârfurile cele mai înalte.\nRecorduri: maxima 44,5 °C, la Ion Sion (județul Brăila), pe 10 august 1951; minima −38,5 °C, la Bod (județul Brașov), pe 25 ianuarie 1942."),
                ("Precipitațiile", "Precipitațiile cresc cu altitudinea și de la est spre vest: peste 1 000–1 200 l/m² pe an în munții înalți, 500–700 l/m² în dealuri și în vest, sub 400 l/m² în Dobrogea și Delta Dunării.\nCele mai multe ploi cad la începutul verii (mai–iunie), iar cele mai puține iarna."),
                ("Vânturile", "Vânturile dominante bat din vest și nord-vest. Vânturi locale: crivățul (nord-est, rece, iarna), austrul (sud-vest, uscat), băltărețul (sud, umed, dinspre Dunăre), foehnul (cald, pe versanți), briza (pe litoral), nemira (Depresiunea Brașov).")],
               stiaica="Recordul de căldură al României, 44,5 °C, a fost înregistrat la stația Ion Sion din Bărăgan, în 1951, și nu a fost depășit nici în verile foarte calde de după 2000.",
               ref=REF.format("Elementele climatice"), prefix="VIII13b")
    E.a(1, "2.2", "Cum variază temperatura medie anuală în România?", "scade de la sud la nord și de la câmpie la munte", ["crește spre munte", "e aceeași peste tot", "crește spre nord"], "Latitudinea și altitudinea.", surse=S_ANM)
    E.a(1, "3.1", "Care e temperatura maximă record din România?", "44,5 °C (Ion Sion, 1951)", ["56,7 °C", "38,5 °C", "40 °C"], "Ion Sion, județul Brăila.", surse=S_REC)
    E.a(1, "3.1", "Care e temperatura minimă record din România?", "−38,5 °C (Bod, 1942)", ["−89,2 °C", "−20 °C", "−50 °C"], "Bod, județul Brașov.", surse=S_REC)
    E.a(2, "2.2", "Cum variază precipitațiile în România?", "cresc cu altitudinea și de la est spre vest", ["scad cu altitudinea", "sunt aceleași peste tot", "cresc spre Dobrogea"], "Munții și vestul sunt mai ploioși.", surse=S_ANM)
    E.a(2, "3.1", "Unde cad cele mai puține precipitații?", "în Dobrogea și în Delta Dunării (sub 400 l/m²/an)", ["în Munții Făgăraș", "în Banat", "în Maramureș"], "Cea mai uscată regiune.", surse=S_ANM)
    E.a(2, "3.1", "Unde cad cele mai multe precipitații?", "în munții înalți (peste 1 000–1 200 l/m²/an)", ["în Dobrogea", "în Bărăgan", "în Delta Dunării"], "Aerul urcă pe munți și se răcește.", surse=S_ANM)
    E.a(2, "3.1", "În ce lună cad, de obicei, cele mai multe ploi?", "la începutul verii (mai–iunie)", ["în ianuarie", "în februarie", "în decembrie"], "Ploile de convecție de început de vară.")
    E.s(2, "1.1", "Asociază vântul cu caracteristica lui.", [("crivățul", "rece, din nord-est, iarna"), ("austrul", "uscat, din sud-vest"), ("băltărețul", "umed, dinspre Dunăre"), ("foehnul", "cald, coboară pe versanți")], "Vânturi locale.")
    E.p(2, "2.1", "Atinge pe harta României Ion Sion (Brăila), locul recordului de căldură.", "romania", 45.0, 27.6, "Ion Sion", 45, "În Bărăgan.", surse=S_REC)
    E.p(2, "2.1", "Atinge pe harta României Bod (Brașov), locul recordului de frig.", "romania", 45.76, 25.65, "Bod", 35, "În Depresiunea Brașov.", surse=S_REC)
    E.adev(2, "2.2", "Vânturile dominante în România bat din vest și nord-vest.", True, "Adevărat.")
    E.adev(2, "3.1", "Recordul de frig al României s-a înregistrat în Bărăgan.", False, "Fals: la Bod, în Depresiunea Brașov; în Bărăgan s-a înregistrat recordul de căldură.", surse=S_REC)
    E.l(2, "3.1", "Completează.", "Recordul de căldură al României, [44,5] °C, s-a înregistrat la Ion Sion; recordul de frig, −38,5 °C, la [Bod].", ["56,7", "Omu"], "Recorduri.", surse=S_REC)
    E.l(2, "2.2", "Completează.", "Precipitațiile cresc cu [altitudinea]; cea mai uscată regiune e [Dobrogea].", ["latitudinea", "Banatul"], "Altitudine, Dobrogea.")
    E.g(3, "2.2", "Diagrama arată precipitațiile anuale în trei locuri (valori aproximative). Unde plouă cel mai mult?", grafic("bare", "Precipitații anuale (valori aproximative)", [("Constanța", 400), ("București", 600), ("Timișoara", 630), ("vârful Omu", 1200)], "l/m²", "ANM – Clima României"), "pe vârful Omu", ["la Constanța", "la București", "la Timișoara"], "Munții sunt cei mai ploioși.", surse=S_ANM)
    E.g(3, "2.2 2.3", "Diagrama arată temperatura medie lunară la o stație din Câmpia Română (valori aproximative). Care e amplitudinea anuală?", grafic("profil", "Temperatura medie lunară, Câmpia Română (aproximativ)", [("I", -2), ("II", 0), ("III", 5), ("IV", 11), ("V", 17), ("VI", 21), ("VII", 23), ("VIII", 22), ("IX", 17), ("X", 11), ("XI", 5), ("XII", 0)], "°C", "ANM – normale climatice"), "aproximativ 25 °C", ["aproximativ 23 °C", "aproximativ 2 °C", "aproximativ 40 °C"], "23 − (−2) = 25.", surse=S_ANM)
    E.a(3, "4.2", "Compară clima litoralului cu cea a Bărăganului.", "litoralul are veri mai răcoroase și ierni mai blânde datorită mării; Bărăganul are extreme mai mari", ["Bărăganul e mai blând", "sunt identice", "litoralul are ierni mai geroase"], "Influența pontică.")
    E.d(2, "2.1", "Ce oraș din Bărăgan, foarte afectat de crivăț iarna, e marcat pe hartă?", "romania", 44.56, 27.36, "Slobozia", ["Pitești", "Sibiu", "Bistrița"], "Slobozia e în centrul Bărăganului.")
    E.a(2, "4.4", "Ce fenomene climatice periculoase apar iarna în Bărăgan?", "viscolul și poleiul", ["taifunurile", "tsunami-urile", "musonul"], "Crivățul spulberă zăpada.")
    E.a(2, "4.4", "Ce fenomene climatice periculoase apar vara?", "canicula, seceta, grindina, furtunile", ["viscolul", "poleiul", "avalanșele de zăpadă"], "ANM emite avertizări de cod galben, portocaliu, roșu.")
    E.a(2, "3.1", "Ce temperatură medie anuală are sudul Câmpiei Române?", "peste 11 °C", ["sub 0 °C", "aproximativ 25 °C", "aproximativ −5 °C"], "Cea mai caldă zonă, cu litoralul.", surse=S_ANM)
    E.a(2, "3.1", "Ce temperatură medie anuală au vârfurile cele mai înalte?", "sub 0 °C", ["peste 11 °C", "aproximativ 20 °C", "exact 10 °C"], "Pe Omu, sub 0 °C.", surse=S_ANM)
    E.a(2, "1.1", "Ce este canicula?", "o perioadă cu temperaturi foarte ridicate", ["o perioadă cu ger", "o ploaie torențială", "o ceață"], "Peste 35 °C, de obicei.")
    E.a(2, "1.1", "Ce sunt precipitațiile?", "apa care cade din nori: ploaie, ninsoare, grindină, lapoviță", ["vântul", "temperatura", "presiunea"], "Se măsoară cu pluviometrul.")
    E.a(3, "4.1", "Vrei să compari clima orașului tău cu a altui oraș. Ce date îți trebuie?", "temperaturile și precipitațiile medii lunare pe 30 de ani", ["prognoza pe mâine", "o poză", "numărul de locuitori"], "Normalele climatice.")
    E.a(2, "3.1", "Ce zonă a României are cele mai multe zile cu soare?", "litoralul și Delta Dunării", ["Maramureșul", "Munții Rodnei", "Bucovina"], "Peste 2 300 de ore de soare pe an.")
    E.a(2, "2.2", "De ce iarna, în Moldova, ninsoarea poate fi viscolită puternic?", "crivățul bate tare și spulberă zăpada", ["bate foehnul cald", "vine aer tropical", "nu ninge niciodată"], "Viscolul blochează drumurile.")
    E.a(2, "4.4", "Cum te protejezi pe caniculă?", "stai la umbră între 11 și 17, bei apă, porți haine deschise la culoare", ["alergi la prânz", "stai în mașina închisă", "nu bei apă"], "Regulile de siguranță.")
    E.a(2, "1.2", "Ce aparat folosesc meteorologii pentru a măsura viteza vântului?", "anemometrul", ["higrometrul", "barometrul", "pluviometrul"], "Viteza se exprimă în m/s sau km/h.")

    E.a(2, "1.2", "Ce instrument măsoară cantitatea de precipitații?", "pluviometrul", ["anemometrul", "termometrul", "barometrul"], "Se exprimă în l/m² sau mm.")

    # ================================================================ S16a Particularități climatice regionale
    R = Lectie(8, "VIII-S16-particularitatile-climatice-regionale-etaje", "Particularitățile climatice regionale",
               "De ce în Banat cresc castani comestibili, iar în Bucovina nu?",
               [("Etajele climatice", "Etajul de câmpie: veri calde, ierni reci, precipitații puține (400–600 l/m²).\nEtajul de dealuri și podișuri: temperaturi medii de 8–10 °C, precipitații de 600–800 l/m².\nEtajul de munte: temperaturi scăzute, precipitații multe, zăpadă care stă mult. Pe vârfuri e etajul alpin, cu climă aspră."),
                ("Influențele climatice regionale", "Oceanice – în vest și în Transilvania (umed, ierni blânde). Submediteraneene – în Banat și sud-vestul Olteniei (cald, ploi de toamnă). Continentale/excesive – în est: Moldova, Bărăgan (ierni geroase, secetă). Pontice – în Dobrogea, pe litoral. Baltice – în nordul țării (Maramureș, Bucovina), cu răcoare și umezeală."),
                ("Climatul orizontului local", "Râmnicu Sărat, la contactul Subcarpaților de Curbură cu Câmpia Română, are influențe continentale: veri calde, ierni geroase cu crivăț, ploi moderate. Zona Vrancea–Buzău are și fenomene de foehn pe versanți.")],
               stiaica="În Banat, datorită influențelor submediteraneene, cresc în mod natural liliacul sălbatic, castanul comestibil și chiar ghimpele, plante iubitoare de căldură.",
               ref=REF.format("Particularitățile climatice regionale (etaje și influențe climatice)"), prefix="VIII16a")
    R.s(1, "3.2", "Asociază influența climatică cu regiunea.", [("oceanică", "vestul țării"), ("submediteraneeană", "Banat și sud-vestul Olteniei"), ("continentală", "Moldova și Bărăgan"), ("pontică", "Dobrogea")], "Influențe regionale.")
    R.s(1, "3.2", "Asociază etajul climatic cu caracteristica lui.", [("de câmpie", "veri calde, precipitații puține"), ("de dealuri și podișuri", "8–10 °C, 600–800 l/m²"), ("de munte", "rece, cu precipitații multe"), ("alpin", "climă foarte aspră pe vârfuri")], "Etajele climatice.")
    R.a(1, "3.2", "Ce influență climatică are nordul țării (Maramureș, Bucovina)?", "baltică, cu răcoare și umezeală", ["mediteraneeană", "pontică", "tropicală"], "Masele de aer din nord.")
    R.a(2, "3.2", "Ce plante iubitoare de căldură cresc în Banat?", "castanul comestibil, liliacul sălbatic", ["jneapănul", "lichenii de tundră", "molidul"], "Influențe submediteraneene.")
    R.a(2, "3.2", "Ce influență climatică are orașul Râmnicu Sărat?", "continentală, cu ierni geroase și veri calde", ["oceanică", "submediteraneeană", "baltică"], "La contactul Subcarpați–câmpie, în est.")
    R.p(2, "2.1", "Atinge pe harta României Bucovina, cu influențe baltice.", "romania", 47.6, 25.8, "Bucovina", 60, "Bucovina e în nordul Moldovei.")
    R.p(2, "2.1", "Atinge pe harta României Dobrogea, cu influențe pontice.", "romania", 44.5, 28.4, "Dobrogea", 70, "Între Dunăre și Marea Neagră.")
    R.p(3, "2.1", "Atinge pe harta României orașul Râmnicu Sărat.", "romania", RS[0], RS[1], "Râmnicu Sărat", 35, "Nord-estul județului Buzău.")
    R.adev(2, "3.2", "În Banat influențele climatice sunt baltice.", False, "Fals: sunt submediteraneene.")
    R.adev(2, "3.2", "În Bărăgan, iernile sunt geroase, iar verile secetoase.", True, "Adevărat: influențe continentale.")
    R.l(2, "3.2", "Completează.", "În Dobrogea, influențele sunt [pontice]; în Banat, sunt [submediteraneene].", ["baltice", "oceanice"], "Influențe regionale.")
    R.l(2, "2.2", "Completează.", "Pe munte precipitațiile sunt [mai multe], iar temperatura este [mai scăzută] decât la câmpie.", ["mai puține", "mai ridicată"], "Etajarea.")
    R.g(3, "2.2", "Graficul compară temperatura medie a lunii ianuarie în trei orașe (valori aproximative). Unde e cel mai blând?", grafic("bare", "Temperatura medie în ianuarie (aproximativ)", [("Timișoara", -1), ("Constanța", 1), ("Iași", -3), ("Brașov", -4)], "°C", "ANM – normale climatice"), "la Constanța", ["la Iași", "la Brașov", "la Timișoara"], "Marea îndulcește iarna pe litoral.", surse=S_ANM)
    R.o(3, "2.2", "Ordonează orașele de la cel mai umed la cel mai uscat (precipitații anuale).", ["Cluj-Napoca", "Timișoara", "București", "Constanța"], "De la umed la uscat", "Precipitațiile scad spre est și spre mare.")
    R.a(3, "4.2", "Compară climatul Maramureșului cu cel al Dobrogei.", "Maramureșul e mai rece și mai umed; Dobrogea e mai caldă și mai uscată", ["sunt identice", "Dobrogea e mai rece", "Maramureșul e mai uscat"], "Nord-vest față de sud-est.")
    R.d(2, "2.1", "Ce regiune cu influențe submediteraneene e marcată pe hartă?", "romania", 45.3, 21.8, "Banatul", ["Bucovina", "Dobrogea", "Maramureșul"], "Banatul e în sud-vest.")
    R.a(2, "3.3", "Cum influențează clima agricultura din Banat?", "căldura și ploile permit culturi variate, inclusiv legume și pomi timpurii", ["e prea frig pentru orice", "e deșert", "nu o influențează"], "Câmpia Banatului e fertilă.")
    R.a(2, "3.2", "De ce în Transilvania influențele oceanice sunt mai puternice decât în Moldova?", "Transilvania e mai la vest și e deschisă spre vest prin Munții Apuseni fragmentați", ["pentru că e la mare", "pentru că e mai la est", "fără motiv"], "Aerul oceanic pătrunde mai ușor.")
    R.a(2, "3.2", "Ce fenomen apare în depresiunile montane în nopțile senine de iarnă?", "inversiunea termică (aer mai rece jos, mai cald pe versanți)", ["foehnul de vară", "briza marină", "musonul"], "Ceață și ger în depresiuni.")
    R.a(2, "3.3", "De ce stațiunile montane (Sinaia, Predeal) sunt căutate vara?", "pentru că acolo e mai răcoare decât la câmpie", ["pentru că e mai cald", "pentru că e la mare", "pentru că nu plouă niciodată"], "Climatul montan.")
    R.a(2, "3.3", "De ce litoralul e bun pentru turismul de vară?", "multe zile cu soare, ploi puține, apă caldă", ["ninge vara", "e foarte ploios", "e frig"], "Turism balnear și de plajă.")
    R.a(3, "1.2", "Ce înseamnă climat de tranziție?", "un climat între cel oceanic din vest și cel continental din est", ["un climat care se schimbă zilnic", "un climat polar", "un climat ecuatorial"], "Specific României.")
    R.a(2, "4.4", "Ce fenomen climatic periculos e frecvent în zona Buzău–Vrancea vara?", "ploile torențiale, cu viituri și alunecări de teren", ["avalanșele de nisip", "taifunurile", "tsunami-urile"], "Relieful subcarpatic accentuează efectele.")
    R.a(2, "3.2", "Ce etaj climatic are Delta Dunării?", "de câmpie, cu influențe pontice", ["alpin", "de munte", "subpolar"], "Puține precipitații, multe zile cu soare.")
    R.a(2, "2.2", "Ce culoare au pe harta precipitațiilor zonele foarte ploioase?", "albastru închis", ["galben", "roșu", "alb"], "Cu cât e mai închis albastrul, cu atât plouă mai mult.")
    R.a(2, "3.3", "Ce culturi sunt avantajate de clima caldă a Dobrogei?", "vița-de-vie și cerealele, cu irigații", ["molidul", "orezul de munte", "cartoful de munte"], "Murfatlar, Ostrov.")
    R.a(2, "3.2", "Ce climat are Câmpia de Vest?", "de câmpie, cu influențe oceanice", ["alpin", "pontic", "baltic excesiv"], "Mai umed decât Bărăganul.")
    R.a(3, "4.4", "Cum se adaptează agricultura la secetele tot mai dese din sud-est?", "irigații, soiuri rezistente la secetă, perdele forestiere", ["tăierea perdelelor forestiere", "mai multe culturi care cer multă apă", "nimic"], "Adaptare la schimbările climatice.")
    R.a(2, "1.2", "Ce înseamnă „influențe” climatice?", "efectele maselor de aer venite din anumite direcții asupra climei unei regiuni", ["ploi zilnice", "zăpezi permanente", "vânturi tropicale"], "Influențe oceanice, continentale, mediteraneene etc.")
    R.a(2, "3.2", "De ce în Bucovina e mai răcoare decât în Câmpia Română?", "e mai la nord și mai înaltă, cu influențe baltice", ["e lângă Marea Neagră", "are influențe mediteraneene", "e mai la sud"], "Latitudine și altitudine.")

    # ================================================================ S16b Dunărea
    D = Lectie(8, "VIII-S16-apele-dunarea", "Apele României – Dunărea",
               "Pe unde intră și pe unde iese Dunărea din România?",
               [("Dunărea în România", "Dunărea intră în România la Baziaș și se varsă în Marea Neagră prin Delta Dunării, după aproximativ 1 075 km pe teritoriul sau la granița țării.\nSectoare: Defileul Dunării (Baziaș – Gura Văii), cu Cazanele Dunării; sectorul de luncă, între Gura Văii și Călărași; sectorul bălților (Balta Ialomiței, Balta Brăilei), între Călărași și Brăila; Dunărea maritimă (Brăila – Sulina); Delta Dunării."),
                ("Debit și folosire", "Debitul mediu al Dunării la vărsare e de aproximativ 6 500 m³/s, cel mai mare dintre râurile României. Primește aproape toate râurile țării.\nPe Dunăre s-au construit hidrocentralele Porțile de Fier I (1972) și Porțile de Fier II, împreună cu Serbia. Dunărea e o cale de navigație importantă (Coridorul VII paneuropean); canalul Dunăre–Marea Neagră duce spre portul Constanța."),
                ("Delta", "La Ceatal Chilia, Dunărea se împarte în brațele Chilia și Tulcea; Tulcea se împarte apoi în Sulina și Sfântu Gheorghe.")],
               stiaica="În Cazanele Dunării, pe malul românesc, a fost sculptat în stâncă chipul regelui dac Decebal, înalt de aproximativ 40 m – cea mai mare sculptură în stâncă din Europa.",
               ref=REF.format("Apele – Dunărea"), prefix="VIII16b")
    D.a(1, "2.1", "Pe unde intră Dunărea în România?", "la Baziaș", ["la Sulina", "la Galați", "la Călărași"], "Baziaș e în județul Caraș-Severin.")
    D.a(2, "3.1", "Câți kilometri are Dunărea pe teritoriul sau la granița României?", "aproximativ 1 075 km", ["aproximativ 107 km", "aproximativ 2 857 km", "aproximativ 10 000 km"], "Cea mai lungă porțiune dintre toate țările.", surse=S_DUN)
    D.o(2, "2.1", "Ordonează sectoarele Dunării în sensul curgerii.", ["Defileul Dunării", "sectorul de luncă", "sectorul bălților", "Dunărea maritimă", "Delta Dunării"], "Sensul curgerii", "De la Baziaș spre mare.")
    D.a(2, "2.1", "Ce sunt Cazanele Dunării?", "porțiunea cea mai îngustă și adâncă a Defileului Dunării", ["un lac din Deltă", "o insulă", "un baraj"], "Între Munții Almăj și Munții Miroč (Serbia).")
    D.a(2, "2.1", "Ce bălți mari se află pe Dunăre, între Călărași și Brăila?", "Balta Ialomiței și Balta Brăilei", ["Lacul Razim și Sinoe", "Lacul Bucura", "Lacul Snagov"], "Insula Mare a Brăilei a fost îndiguită.")
    D.a(2, "3.3", "Ce hidrocentrale mari sunt pe Dunăre?", "Porțile de Fier I și II", ["Vidraru și Lotru", "Bicaz și Stejaru", "Mărișelu și Tarnița"], "Construite împreună cu Serbia.", surse=S_PDF)
    D.a(2, "3.3", "În ce an a fost terminată hidrocentrala Porțile de Fier I?", "1972", ["1918", "1990", "2007"], "Cea mai mare hidrocentrală a României.", surse=S_PDF)
    D.a(2, "3.1", "Ce debit mediu are Dunărea la vărsare?", "aproximativ 6 500 m³/s", ["aproximativ 65 m³/s", "aproximativ 650 000 m³/s", "aproximativ 6 m³/s"], "Cel mai mare din țară.", surse=S_DUN)
    D.a(2, "2.1", "Unde se desparte Dunărea în brațele Chilia și Tulcea?", "la Ceatal Chilia (Ceatal Izmail)", ["la Baziaș", "la Călărași", "la Galați"], "Apoi brațul Tulcea se împarte în Sulina și Sfântu Gheorghe.")
    D.p(2, "2.1", "Atinge pe harta României Baziaș, unde Dunărea intră în țară.", "romania", 44.82, 21.38, "Baziaș", 40, "În județul Caraș-Severin.")
    D.p(2, "2.1", "Atinge pe harta României Cazanele Dunării.", "romania", 44.63, 22.3, "Cazanele Dunării", 35, "În Defileul Dunării.")
    D.p(3, "2.1", "Atinge pe harta României Balta Brăilei.", "romania", 45.0, 27.9, "Balta Brăilei", 40, "Între Brațul Măcin și Dunăre.")
    D.p(3, "2.1", "Atinge pe harta României Galați, cel mai mare port dunărean.", "romania", 45.44, 28.05, "Galați", 30, "Pe Dunărea maritimă.")
    D.s(2, "3.3", "Asociază orașul-port de pe Dunăre cu sectorul.", [("Drobeta-Turnu Severin", "la ieșirea din defileu"), ("Giurgiu", "sectorul de luncă"), ("Brăila", "Dunărea maritimă, începutul ei"), ("Tulcea", "la intrarea în Deltă")], "Porturi dunărene.")
    D.adev(2, "3.3", "Dunărea e o cale de navigație internațională.", True, "Adevărat: leagă Marea Nordului de Marea Neagră prin canalul Rin–Main–Dunăre.")
    D.adev(2, "2.1", "Dunărea iese din România prin Defileul Dunării.", False, "Fals: intră prin defileu și se varsă prin Deltă.")
    D.l(2, "2.1", "Completează.", "Dunărea intră în România la [Baziaș] și se varsă prin [Delta Dunării].", ["Sulina", "Porțile de Fier"], "Intrare și vărsare.")
    D.l(2, "3.3", "Completează.", "Cea mai mare hidrocentrală a României e [Porțile de Fier I]; canalul Dunăre–Marea Neagră duce spre portul [Constanța].", ["Vidraru", "Galați"], "Energie și navigație.", surse=S_PDF)
    D.g(3, "2.3", "Graficul arată debitul mediu al Dunării în câteva puncte (m³/s, valori aproximative). Ce observi?", grafic("profil", "Debitul mediu al Dunării (aproximativ)", [("Viena", 1900), ("Budapesta", 2350), ("Baziaș", 5500), ("vărsare", 6500)], "m³/s", "ICPDR"), "debitul crește spre vărsare, pe măsură ce primește afluenți", ["debitul scade spre vărsare", "debitul e constant", "debitul e cel mai mare la Viena"], "Afluenții măresc debitul.", surse=S_DUN)
    D.a(3, "4.2", "Compară sectorul de defileu cu sectorul bălților.", "în defileu albia e îngustă și adâncă între munți; în sectorul bălților Dunărea se desparte în brațe, cu lunci largi", ["sunt identice", "defileul e mai lat", "bălțile sunt la munte"], "Relieful decide forma văii.")
    D.d(2, "2.1", "Ce oraș-port de pe Dunăre, la granița cu Bulgaria, e marcat pe hartă?", "romania", 43.9, 25.97, "Giurgiu", ["Călărași", "Turnu Măgurele", "Calafat"], "Podul Prieteniei leagă Giurgiu de Ruse.")
    D.a(2, "3.4", "Ce sculptură uriașă se află în stâncă, în Cazanele Dunării?", "chipul lui Decebal", ["chipul lui Ștefan cel Mare", "Sfinxul", "Babele"], "Aproximativ 40 m înălțime.")
    D.a(2, "3.3", "Ce poduri leagă România de Bulgaria peste Dunăre?", "Giurgiu–Ruse și Calafat–Vidin", ["Brăila–Galați", "Cernavodă–Fetești", "Tulcea–Sulina"], "Podul Calafat–Vidin a fost deschis în 2013.")
    D.a(2, "3.3", "Ce pod mare peste Dunăre a fost deschis în 2023, lângă Brăila?", "podul suspendat de la Brăila", ["Podul Prieteniei", "Podul Anghel Saligny", "Podul Calafat–Vidin"], "Al treilea cel mai lung pod suspendat din Europa.", surse=["Compania Națională de Investiții Rutiere – Podul suspendat peste Dunăre (Brăila)", "Wikipedia (ro) – Podul suspendat de la Brăila"])
    D.a(2, "3.4", "Ce pod istoric peste Dunăre, construit de Anghel Saligny, e la Cernavodă?", "Podul Regele Carol I (Anghel Saligny)", ["Podul Brăila", "Podul Prieteniei", "Podul Calafat"], "Inaugurat în 1895.")
    D.a(2, "4.4", "De ce sunt importante digurile de pe Dunăre?", "protejează localitățile și terenurile agricole de inundații", ["opresc navigația", "produc energie", "aduc pește"], "Dar au redus luncile naturale.")
    D.a(3, "4.4", "Ce efect au avut îndiguirile din sectorul bălților?", "au crescut terenurile agricole, dar s-au pierdut zone umede și a crescut riscul la viituri mari", ["doar efecte pozitive", "au creat munți", "nu au avut efecte"], "Se discută refacerea unor zone umede.")
    D.a(2, "2.1", "Ce afluenți mari primește Dunărea pe stânga, în România?", "Jiul, Oltul, Argeșul, Ialomița, Siretul, Prutul", ["Mureșul și Someșul", "Tisa și Crișurile direct", "Bega și Timișul direct"], "Mureșul ajunge în Tisa, apoi în Dunăre, în Serbia.")
    D.a(2, "3.3", "Ce animal mare, pe cale de dispariție, migrează din Marea Neagră pe Dunăre ca să depună icre?", "sturionul", ["delfinul", "rechinul", "foca"], "Pescuitul sturionilor e interzis.")

    D.a(2, "2.1", "Ce oraș, cu un port mare, e la ieșirea Dunării din defileu?", "Drobeta-Turnu Severin", ["Giurgiu", "Galați", "Tulcea"], "Aici se văd ruinele podului lui Apolodor din Damasc.")

    # ================================================================ S17 Râurile interioare
    I = Lectie(8, "VIII-S17-raurile-interioare", "Râurile interioare",
               "De ce râurile României par să pornească toate din Carpați?",
               [("Rețeaua hidrografică", "Majoritatea râurilor izvorăsc din Carpați și curg radiar, în toate direcțiile, spre Dunăre (sau spre Tisa, în vest). Aproape toate ajung, în final, în Dunăre.\nGrupe: râurile din vest (Someș, Crișuri, Mureș, Bega, Timiș), râurile din sud (Jiu, Olt, Argeș, Ialomița), râurile din est (Siret, cu afluenții Suceava, Moldova, Bistrița, Trotuș, Buzău, Râmnicu Sărat; Prut), râurile din Dobrogea (Casimcea, Taița), scurte."),
                ("Cele mai lungi", "Mureșul e cel mai lung râu interior (aproximativ 760 km în România). Urmează Prutul (la graniță), Oltul (615 km, cel mai lung râu care curge în întregime prin România, de la izvor la vărsare) și Siretul.\nRâul Buzău și râul Râmnicu Sărat sunt afluenți ai Siretului."),
                ("Regim și folosire", "Râurile au ape mari primăvara (topirea zăpezilor și ploi) și la începutul verii (ploi torențiale – viituri), iar ape mici toamna și iarna.\nSunt folosite pentru alimentare cu apă, hidroenergie (Bistrița, Argeș, Lotru, Olt), irigații, pescuit și turism.")],
               stiaica="Oltul și Mureșul izvorăsc foarte aproape unul de altul, în Munții Hășmaș, dar unul curge spre sud și celălalt spre vest.",
               ref=REF.format("Râurile interioare"))
    I.a(1, "2.1", "De unde izvorăsc cele mai multe râuri ale României?", "din Carpați", ["din Delta Dunării", "din Marea Neagră", "din Bărăgan"], "Rețeaua e radiară.")
    I.a(2, "1.1", "Ce înseamnă rețea hidrografică radiară?", "râurile pornesc din centru (Carpați) și curg în toate direcțiile", ["râurile curg toate spre nord", "râurile sunt paralele", "râurile curg în cerc"], "Ca spițele unei roți.")
    I.a(2, "3.1", "Care e cel mai lung râu interior al României?", "Mureșul", ["Oltul", "Siretul", "Jiul"], "Aproximativ 760 km în România.", surse=S_RAURI)
    I.a(2, "3.1", "Care e cel mai lung râu care curge în întregime prin România?", "Oltul (615 km)", ["Mureșul", "Prutul", "Someșul"], "Mureșul iese în Ungaria.", surse=S_RAURI)
    I.a(2, "2.1", "În ce râu se varsă râul Buzău?", "Siret", ["Ialomița", "Argeș", "direct în Dunăre"], "La fel și Râmnicu Sărat.")
    I.s(2, "2.1", "Asociază râul cu grupa lui.", [("Someșul", "vest"), ("Oltul", "sud"), ("Bistrița", "est (afluent al Siretului)"), ("Casimcea", "Dobrogea")], "Grupe de râuri.")
    I.s(2, "2.1", "Asociază râul cu orașul așezat pe el.", [("Mureș", "Târgu Mureș"), ("Olt", "Râmnicu Vâlcea"), ("Bega", "Timișoara"), ("Buzău", "Buzău")], "Orașe pe râuri.")
    I.a(2, "2.1", "În ce râu se varsă Mureșul?", "Tisa (în Ungaria)", ["Dunărea, în România", "Siret", "Prut"], "Apoi Tisa se varsă în Dunăre, în Serbia.")
    I.a(2, "2.1", "Unde izvorăsc Oltul și Mureșul?", "foarte aproape, în Munții Hășmaș", ["în Munții Făgăraș", "în Delta Dunării", "în Munții Apuseni"], "Apoi curg în direcții diferite.")
    I.a(2, "3.2", "Când au râurile cele mai mari debite?", "primăvara și la începutul verii", ["toamna", "iarna", "niciodată"], "Topirea zăpezii și ploi.")
    I.a(2, "1.1", "Ce este o viitură?", "o creștere bruscă a nivelului unui râu, după ploi torențiale", ["secarea râului", "înghețarea râului", "un lac nou"], "Viiturile pot produce inundații.")
    I.a(2, "3.3", "Ce râu are cele mai multe hidrocentrale în lanț?", "Bistrița (și Oltul)", ["Casimcea", "Bega", "Taița"], "Pe Bistrița e lacul Izvorul Muntelui.")
    I.p(2, "2.1", "Atinge pe harta României vărsarea Oltului în Dunăre.", "romania", 43.72, 24.85, "vărsarea Oltului", 40, "Lângă Turnu Măgurele.")
    I.p(2, "2.1", "Atinge pe harta României vărsarea Siretului în Dunăre.", "romania", 45.42, 28.02, "vărsarea Siretului", 35, "Lângă Galați.")
    I.p(3, "2.1", "Atinge pe harta României municipiul Buzău, așezat pe râul Buzău.", "romania", 45.15, 26.82, "Buzău", 30, "Râul Buzău iese din Subcarpați și traversează câmpia spre Siret.")
    I.p(3, "2.1", "Atinge pe harta României orașul Râmnicu Sărat, pe râul cu același nume.", "romania", RS[0], RS[1], "Râmnicu Sărat", 35, "Râul Râmnicu Sărat e afluent al Siretului.")
    I.adev(2, "2.1", "Toate râurile României se varsă direct în Marea Neagră.", False, "Fals: aproape toate ajung în Dunăre.")
    I.adev(2, "3.2", "Viiturile sunt frecvente vara, după ploi torențiale.", True, "Adevărat.")
    I.l(2, "2.1", "Completează.", "Cel mai lung râu interior este [Mureșul]; cel mai lung râu care curge în întregime prin România este [Oltul].", ["Siretul", "Prutul"], "Mureș și Olt.", surse=S_RAURI)
    I.l(2, "2.1", "Completează.", "Râul Buzău se varsă în [Siret], iar Siretul se varsă în [Dunăre].", ["Ialomița", "Marea Neagră"], "Drumul apei.")
    I.o(3, "2.1", "Ordonează drumul apei de la Munții Buzăului până la mare.", ["râul Buzău", "Siretul", "Dunărea", "Delta Dunării", "Marea Neagră"], "De la munte la mare", "Râu → afluent → fluviu → deltă → mare.")
    I.g(3, "2.3", "Graficul arată lungimea unor râuri pe teritoriul României (km, valori aproximative). Ce râu e al doilea ca lungime, după Mureș?", grafic("bare", "Lungimea râurilor pe teritoriul României (aproximativ)", [("Mureș", 761), ("Prut", 742), ("Olt", 615), ("Siret", 559), ("Buzău", 302)], "km", "INS – Anuarul Statistic"), "Prutul", ["Oltul", "Siretul", "Buzăul"], "Prutul e graniță cu Republica Moldova.", surse=S_RAURI)
    I.a(3, "4.2", "Compară râurile din vest cu cele din est.", "râurile din vest ajung în Tisa; cele din est ajung în Siret și Prut, apoi în Dunăre", ["toate curg spre nord", "nu există diferențe", "cele din est ajung în Tisa"], "Bazine diferite.")
    I.d(2, "2.1", "Ce râu, cu orașul Cluj-Napoca, e marcat pe hartă?", "romania", 46.77, 23.6, "Someșul Mic", ["Mureșul", "Oltul", "Crișul Repede"], "Cluj-Napoca e pe Someșul Mic.")
    I.a(2, "4.4", "Ce faci dacă se anunță viitură pe râul din apropiere?", "te îndepărtezi de albie și urmezi indicațiile autorităților", ["mergi să vezi apa de aproape", "traversezi podul inundat", "intri cu mașina în apă"], "Siguranța înainte de toate.")
    I.a(2, "3.3", "La ce folosesc lacurile de acumulare de pe râuri?", "energie, apă potabilă, irigații, protecție contra inundațiilor", ["doar la înot", "la extragerea petrolului", "la nimic"], "Folosință complexă.")
    I.a(2, "2.1", "Ce râu mare traversează Bucureștiul?", "Dâmbovița", ["Oltul", "Mureșul", "Siretul"], "Dâmbovița e afluent al Argeșului.")
    I.a(2, "4.4", "Ce poluează râurile României?", "apele uzate netratate, deșeurile, îngrășămintele de pe câmpuri", ["peștii", "sălciile de pe mal", "ploaia curată"], "Stațiile de epurare reduc poluarea.")
    I.a(2, "3.2", "De ce râurile din Dobrogea sunt scurte și au puțină apă?", "Dobrogea e uscată și are relief jos, aproape de mare", ["izvorăsc din Carpați", "sunt alimentate de ghețari", "sunt înghețate"], "Casimcea, Taița.")
    I.a(2, "2.1", "Ce râu desparte Moldova de Muntenia, în trecut, ca graniță istorică?", "Milcovul", ["Oltul", "Mureșul", "Jiul"], "Milcovul curge prin Focșani.")

    # ================================================================ S18 Lacurile și apele subterane
    L = Lectie(8, "VIII-S18-lacurile-apele-subterane", "Lacurile și apele subterane",
               "Ce fel de lacuri poți găsi de la munte până la mare?",
               [("Lacurile naturale", "Lacuri glaciare – în căldările din munții înalți: Bucura (cel mai întins lac glaciar) și Zănoaga (cel mai adânc), în Retezat; Bâlea, Capra (Făgăraș); Gâlcescu (Parâng).\nLac vulcanic – Sfânta Ana, în craterul unui vulcan stins (Munții Ciomatu).\nLac de baraj natural – Lacul Roșu, format în 1837 după o alunecare de teren.\nLacuri pe sare – Ursu (Sovata), cu apă caldă în adânc (heliotermal).\nLacuri de câmpie, limane fluviatile (Snagov), lacuri sărate (Amara, Lacul Sărat), lacuri din Deltă, lagune și limane maritime (Razim–Sinoe, cel mai mare complex lagunar; Techirghiol, cu nămol terapeutic)."),
                ("Lacurile artificiale", "Lacuri de acumulare pentru energie și apă: Porțile de Fier (cel mai mare, pe Dunăre), Izvorul Muntelui (Bistrița), Vidraru (Argeș), Vidra (Lotru). Iazuri și heleșteie pentru pește și irigații (în Câmpia Moldovei)."),
                ("Apele subterane", "Apele freatice, aproape de suprafață (fântâni), și apele de adâncime. Apele minerale, cu săruri dizolvate, sunt folosite pentru băut și tratament: Borsec, Bucovina, Slănic Moldova, Băile Herculane, Buziaș, Sângeorz-Băi. Apele termale: Băile Felix, Băile Herculane.")],
               stiaica="Lacul Ursu de la Sovata e heliotermal: Soarele încălzește un strat de apă sărată de sub suprafață, unde temperatura poate ajunge vara la peste 30 °C, deși la suprafață apa e mai rece.",
               ref=REF.format("Lacurile și apele subterane"))
    L.s(1, "1.1", "Asociază lacul cu tipul lui.", [("Bucura", "glaciar"), ("Sfânta Ana", "vulcanic"), ("Lacul Roșu", "de baraj natural"), ("Vidraru", "de acumulare")], "Tipuri de lacuri.")
    L.s(1, "1.1", "Asociază lacul cu tipul lui.", [("Razim", "lagună"), ("Techirghiol", "liman maritim"), ("Ursu", "pe sare, heliotermal"), ("Snagov", "liman fluviatil")], "Alte tipuri.")
    L.a(1, "2.1", "Care e cel mai întins lac glaciar din România?", "Bucura", ["Zănoaga", "Bâlea", "Sfânta Ana"], "În Munții Retezat.", surse=S_LACURI)
    L.a(2, "2.1", "Care e cel mai adânc lac glaciar din România?", "Zănoaga", ["Bucura", "Bâlea", "Capra"], "Tot în Retezat.", surse=S_LACURI)
    L.a(2, "2.1", "Care e singurul lac vulcanic din România?", "Sfânta Ana", ["Lacul Roșu", "Lacul Ursu", "Lacul Bucura"], "În Munții Ciomatu (Harghita).")
    L.a(2, "1.2", "Cum s-a format Lacul Roșu?", "o alunecare de teren a blocat un râu, în 1837", ["într-un crater", "săpat de ghețar", "construit de om"], "Trunchiurile de copaci înecați se văd și azi.")
    L.a(2, "2.1", "Care e cel mai mare lac de acumulare din România?", "Porțile de Fier", ["Vidraru", "Izvorul Muntelui", "Snagov"], "Pe Dunăre.", surse=S_PDF)
    L.a(2, "2.1", "Care e cel mai mare complex lagunar al României?", "Razim–Sinoe", ["Techirghiol", "Bâlea", "Snagov"], "Razim e cel mai mare lac al țării.", surse=S_LACURI)
    L.a(2, "3.3", "Pentru ce e cunoscut Lacul Techirghiol?", "nămolul terapeutic", ["apele glaciare", "vulcanul", "cascada"], "Lacul e foarte sărat.")
    L.a(2, "1.1", "Ce sunt apele minerale?", "ape subterane cu multe săruri dizolvate, bune pentru băut sau tratament", ["ape de ploaie", "ape de mare", "ape poluate"], "Borsec, Buziaș, Slănic Moldova.")
    L.a(2, "1.1", "Ce sunt apele freatice?", "ape subterane aflate aproape de suprafață, din care se alimentează fântânile", ["ape din nori", "ape de mare", "ape termale din adânc"], "Apă de fântână.")
    L.p(2, "2.1", "Atinge pe harta României Lacul Sfânta Ana.", "romania", 46.13, 25.89, "Lacul Sfânta Ana", 35, "În județul Harghita.")
    L.p(2, "2.1", "Atinge pe harta României Lacul Razim.", "romania", 44.9, 28.95, "Lacul Razim", 35, "La sudul Deltei Dunării.", surse=S_LACURI)
    L.p(3, "2.1", "Atinge pe harta României Lacul Roșu.", "romania", 46.79, 25.8, "Lacul Roșu", 35, "Lângă Cheile Bicazului.")
    L.p(3, "2.1", "Atinge pe harta României Lacul Vidraru.", "romania", 45.37, 24.63, "Lacul Vidraru", 35, "Pe Argeș, în Munții Făgăraș.")
    L.adev(2, "1.2", "Lacul Bâlea e un lac vulcanic.", False, "Fals: e un lac glaciar, în Munții Făgăraș.")
    L.adev(2, "3.3", "Apele minerale ale României sunt folosite în stațiuni balneare.", True, "Adevărat: Herculane, Slănic Moldova, Sovata etc.")
    L.l(2, "2.1", "Completează.", "Cel mai întins lac glaciar e [Bucura], iar singurul lac vulcanic e [Sfânta Ana].", ["Zănoaga", "Lacul Roșu"], "Bucura, Sfânta Ana.", surse=S_LACURI)
    L.l(2, "3.3", "Completează.", "Lacul [Techirghiol] e cunoscut pentru nămol, iar Lacul [Ursu] de la Sovata e heliotermal.", ["Snagov", "Bâlea"], "Lacuri balneare.")
    L.g(3, "2.3", "Graficul compară suprafața unor lacuri (km², valori aproximative). Care e cel mai mare?", grafic("bare", "Suprafața unor lacuri din România (aproximativ)", [("Razim", 415), ("Sinoe", 171), ("Izvorul Muntelui", 31), ("Bucura", 0.1)], "km²", "Wikipedia (ro) – Lista lacurilor din România"), "Razim", ["Sinoe", "Izvorul Muntelui", "Bucura"], "Razim e cel mai mare lac al României.", surse=S_LACURI)
    L.o(3, "2.2", "Ordonează lacurile de la cel mai înalt la cel mai jos.", ["Bucura (glaciar)", "Sfânta Ana (vulcanic)", "Lacul Roșu (de baraj natural)", "Snagov (de câmpie)", "Razim (lagună)"], "Altitudine, descrescător", "De la munte la mare.")
    L.d(2, "2.1", "Ce lac de acumulare mare, pe Bistrița, e marcat pe hartă?", "romania", 46.95, 26.05, "Izvorul Muntelui (Bicaz)", ["Vidraru", "Porțile de Fier", "Lacul Roșu"], "Lângă Ceahlău.")
    L.a(3, "4.2", "Compară un lac glaciar cu un lac de acumulare.", "lacul glaciar e natural, mic, în căldări; lacul de acumulare e artificial, în spatele unui baraj, folosit pentru energie", ["sunt identice", "ambele sunt artificiale", "lacul glaciar are baraj de beton"], "Origine și folosință.")
    L.a(2, "3.4", "Ce stațiune cu ape termale și minerale e una dintre cele mai vechi din România, din vremea romanilor?", "Băile Herculane", ["Mamaia", "Poiana Brașov", "Sinaia"], "Numele vine de la Hercule.")
    L.a(2, "3.3", "Ce sunt iazurile?", "lacuri mici artificiale, făcute pe văi, pentru pește sau irigații", ["lacuri glaciare", "lacuri vulcanice", "lagune"], "Frecvente în Câmpia Moldovei.")
    L.a(2, "4.4", "Cum protejăm apele subterane?", "nu aruncăm deșeuri pe sol, folosim îngrășămintele cu măsură, avem canalizare", ["deversăm uleiuri pe sol", "facem gropi de gunoi oriunde", "folosim mult pesticid"], "Poluarea ajunge în fântâni.")
    L.a(2, "2.1", "În ce munți se află Lacul Bâlea?", "Făgăraș", ["Retezat", "Rodnei", "Apuseni"], "Lângă Transfăgărășan.")
    L.a(2, "3.3", "Ce apă minerală cunoscută provine din Depresiunea Borsec, în Carpații Orientali?", "Borsec", ["Techirghiol", "Razim", "Snagov"], "Borsec e numită „regina apelor minerale”.")
    L.a(2, "1.2", "Ce înseamnă lac heliotermal?", "lac în care Soarele încălzește un strat de apă din adânc, mai mult decât la suprafață", ["lac înghețat", "lac vulcanic fierbinte", "lac de acumulare"], "Lacul Ursu de la Sovata.")

    L.a(2, "2.1", "În ce munți se află Lacul Bucura?", "Retezat", ["Făgăraș", "Rodnei", "Apuseni"], "Retezat are peste 80 de lacuri glaciare.")

    # ================================================================ S19 Marea Neagră
    N = Lectie(8, "VIII-S19-marea-neagra", "Marea Neagră",
               "De ce sub o anumită adâncime, în Marea Neagră aproape că nu există viață?",
               [("Caracteristici", "Marea Neagră e o mare aproape închisă, legată de Marea Mediterană prin Bosfor, Marea Marmara și Dardanele. Are aproximativ 436 000 km² și adâncimea maximă de aproximativ 2 212 m, după Britannica.\nPrimește apa multor fluvii mari (Dunăre, Nipru, Nistru, Don), de aceea salinitatea e mică: aproximativ 17–18 ‰ la suprafață (față de 35 ‰ în ocean). Sub aproximativ 150–200 m, apa conține hidrogen sulfurat și aproape nu are oxigen, deci viața lipsește aproape complet."),
                ("Țărmul românesc", "Litoralul românesc are aproximativ 245 km. În nord (Sulina – Capul Midia) țărmul e jos, cu delte, lagune și cordoane de nisip. În sud (Capul Midia – Vama Veche) țărmul e înalt, cu faleze și plaje.\nPlatforma continentală e largă, cu petrol și gaze naturale."),
                ("Viața și folosirea mării", "Trăiesc delfini, calcan, hamsii, stavrid, guvizi, midii. Sturionii migrează pe Dunăre.\nMarea e folosită pentru turism (Mamaia, Eforie, Costinești, Neptun, Mangalia), transport (portul Constanța), pescuit și exploatarea petrolului și gazelor. Există o rezervație marină între Vama Veche și 2 Mai.")],
               stiaica="Apa Mării Negre e de două ori mai puțin sărată decât apa oceanului, pentru că primește multă apă dulce de la fluvii.",
               ref=REF.format("Marea Neagră"))
    N.a(1, "2.1", "Cu ce mare comunică Marea Neagră?", "Marea Mediterană, prin Bosfor, Marea Marmara și Dardanele", ["Marea Baltică", "Marea Nordului", "Marea Caspică"], "O mare aproape închisă.")
    N.a(2, "3.1", "Ce adâncime maximă are Marea Neagră?", "aproximativ 2 212 m", ["aproximativ 22 m", "aproximativ 11 000 m", "aproximativ 200 m"], "După Britannica.", surse=S_MN)
    N.a(2, "3.1", "Ce suprafață are Marea Neagră?", "aproximativ 436 000 km²", ["aproximativ 4 360 km²", "aproximativ 43 milioane km²", "aproximativ 1 milion km²"], "Mai mult decât suprafața României.", surse=S_MN)
    N.a(2, "3.2", "De ce Marea Neagră e puțin sărată?", "primește multă apă dulce de la fluvii mari", ["pentru că e foarte rece", "pentru că e foarte adâncă", "pentru că plouă cu sare"], "Salinitate de aproximativ 17–18 ‰ la suprafață.", surse=S_MN)
    N.a(2, "3.2", "De ce în adâncul Mării Negre aproape că nu există viață?", "sub aproximativ 150–200 m apa are hidrogen sulfurat și aproape deloc oxigen", ["pentru că e prea caldă", "pentru că e înghețată", "pentru că e prea luminoasă"], "Straturile de apă se amestecă foarte puțin.")
    N.a(2, "3.1", "Ce lungime are litoralul românesc?", "aproximativ 245 km", ["aproximativ 24 km", "aproximativ 1 075 km", "aproximativ 2 450 km"], "De la Sulina la Vama Veche.")
    N.s(2, "1.1", "Asociază sectorul de țărm cu caracteristica.", [("nordic (Sulina – Capul Midia)", "țărm jos, cu delte și lagune"), ("sudic (Capul Midia – Vama Veche)", "țărm înalt, cu faleze"), ("platforma continentală", "resurse de petrol și gaze"), ("Vama Veche – 2 Mai", "rezervație marină")], "Țărmul românesc.")
    N.s(2, "3.3", "Asociază viețuitoarea cu Marea Neagră.", [("delfinul", "mamifer marin"), ("calcanul", "pește plat"), ("midia", "moluscă"), ("sturionul", "pește care migrează pe Dunăre")], "Viața din Marea Neagră.")
    N.p(2, "2.1", "Atinge pe harta României portul Constanța.", "romania", 44.17, 28.65, "Constanța", 30, "Cel mai mare port de la Marea Neagră.")
    N.p(2, "2.1", "Atinge pe harta României stațiunea Mamaia.", "romania", 44.25, 28.62, "Mamaia", 30, "La nord de Constanța.")
    N.p(3, "2.1", "Atinge pe harta României Capul Midia, unde se schimbă tipul de țărm.", "romania", 44.34, 28.68, "Capul Midia", 30, "La nord de Mamaia.")
    N.p(3, "2.1", "Atinge pe harta României Mangalia.", "romania", 43.8, 28.58, "Mangalia", 30, "În sudul litoralului.")
    N.a(2, "3.3", "Care e cel mai mare port de la Marea Neagră?", "Constanța", ["Odesa", "Varna", "Mangalia"], "Portul Constanța e unul dintre cele mai mari din Europa.")
    N.a(2, "3.3", "Ce resurse se exploatează din platforma continentală a Mării Negre?", "petrol și gaze naturale", ["aur", "cărbune", "diamante"], "Inclusiv zăcământul Neptun Deep.")
    N.adev(2, "1.2", "Marea Neagră e mai sărată decât oceanul.", False, "Fals: e de aproximativ două ori mai puțin sărată.", surse=S_MN)
    N.adev(2, "3.3", "Pe litoralul sudic românesc există faleze.", True, "Adevărat: între Capul Midia și Vama Veche.")
    N.l(2, "2.1", "Completează.", "Marea Neagră comunică cu Marea Marmara prin strâmtoarea [Bosfor]; cel mai mare port românesc e [Constanța].", ["Gibraltar", "Galați"], "Bosfor, Constanța.")
    N.l(2, "3.2", "Completează.", "Sub aproximativ 200 m, apa Mării Negre conține [hidrogen sulfurat] și aproape deloc [oxigen].", ["sare de bucătărie", "azot"], "Zona fără viață.")
    N.g(3, "2.3", "Graficul compară salinitatea medie la suprafață (‰, valori aproximative). De câte ori e mai sărat oceanul decât Marea Neagră?", grafic("bare", "Salinitatea la suprafață (aproximativ)", [("Oceanul Planetar", 35), ("Marea Mediterană", 38), ("Marea Neagră", 17)], "‰", "Encyclopaedia Britannica"), "de aproximativ 2 ori", ["la fel", "de 10 ori", "de 2 ori mai puțin"], "35 : 17 ≈ 2.", surse=S_MN)
    N.o(3, "2.1", "Ordonează stațiunile de pe litoral de la nord la sud.", ["Mamaia", "Constanța", "Eforie", "Costinești", "Neptun", "Mangalia", "Vama Veche"], "De la nord la sud", "Litoralul românesc.")
    N.a(3, "4.2", "Compară litoralul nordic cu cel sudic.", "nordul e jos, cu lagune și delte, puțin turism; sudul e înalt, cu faleze și stațiuni", ["sunt identice", "nordul are faleze", "sudul are deltă"], "Două sectoare diferite.")
    N.d(2, "2.1", "Ce țară vecină, la sud, are și ea țărm la Marea Neagră?", "lume", 42.7, 25.5, "Bulgaria", ["Ungaria", "Serbia", "Grecia"], "Bulgaria are stațiunile Varna și Burgas.")
    N.a(2, "4.4", "Ce amenință Marea Neagră?", "poluarea adusă de fluvii, deșeurile de plastic și pescuitul excesiv", ["zăpada", "ghețarii", "vulcanii activi"], "Se cer măsuri comune ale statelor riverane.")
    N.a(2, "3.3", "Ce lucrare protejează plajele de eroziunea valurilor?", "diguri și înnisipări artificiale", ["tăierea dunelor", "construcții pe plajă", "extragerea nisipului"], "Plajele de la Mamaia au fost lărgite.")
    N.a(2, "3.3", "Ce state au țărm la Marea Neagră?", "România, Bulgaria, Turcia, Georgia, Rusia, Ucraina", ["România și Ungaria", "Grecia și Italia", "Serbia și Croația"], "Șase state riverane.")
    N.a(2, "3.2", "Ce sunt cordoanele litorale?", "fâșii de nisip care despart lagunele de mare", ["faleze înalte", "insule vulcanice", "recife de corali"], "Ex.: cordonul care închide Lacul Razim.")
    N.a(2, "3.3", "Ce pește mic, hrană pentru delfini, se pescuiește mult în Marea Neagră?", "hamsia", ["somonul", "tonul", "codul"], "Și stavridul.")
    N.a(2, "4.4", "Ce faci dacă vezi un delfin eșuat pe plajă?", "anunți autoritățile sau Muzeul de Științele Naturii din Constanța și nu îl atingi", ["îl împingi în larg singur", "faci poze aproape de el", "îl iei acasă"], "Delfinii sunt protejați prin lege.")
    N.a(2, "3.2", "De ce iarna Marea Neagră nu îngheață pe litoralul românesc, de obicei?", "apa sărată îngheață mai greu, iar marea păstrează căldura", ["e prea adâncă și fierbinte", "nu e niciodată frig", "e acoperită de petrol"], "Doar în ierni foarte geroase apar sloiuri lângă țărm.")

    N.a(2, "2.1", "Ce insulă din Marea Neagră, aproape de Delta Dunării, aparține Ucrainei?", "Insula Șerpilor", ["Insula Mare a Brăilei", "Insula Ada Kaleh", "Insula Sacalin"], "Ada Kaleh a fost acoperită de lacul Porțile de Fier.")

    # ================================================================ S20 Vegetația, fauna, solurile (expediție)
    X = Expeditie(8, "VIII-S20-vegetatia-fauna-solurile-aplicatii", "Expediție: vegetația, fauna și solurile. Siguranța în fața fenomenelor extreme",
                  "Ce plante și animale ocrotite trăiesc în România și cum te protejezi de fenomenele extreme?",
                  ref=REF.format("Vegetația, fauna și solurile. Aplicații practice"))
    X.o(1, "1.1", "Ordonează zonele de vegetație ale României de la câmpie spre vârful muntelui.", ["stepa", "silvostepa", "pădurile de stejar", "pădurile de fag", "pădurile de molid", "jnepenișurile (subalpin)", "pajiștile alpine"], "De jos în sus", "Vegetația urmează altitudinea.")
    X.s(2, "1.2", "Asociază solul cu zona.", [("cernoziomul", "stepa și silvostepa (Bărăgan, Dobrogea)"), ("solurile brune", "pădurile de foioase"), ("podzolurile", "pădurile de conifere, la munte"), ("aluviunile", "luncile râurilor")], "Solurile urmează vegetația și clima.")
    X.a(2, "3.3", "Ce carnivore mari trăiesc în Carpații României?", "ursul brun, lupul, râsul", ["leul, tigrul", "ursul polar", "jaguarul"], "România are cele mai mari populații din UE.", surse=S_CARN)
    X.a(2, "3.3", "Ce animal ocrotit trăiește pe stâncăriile înalte ale Carpaților?", "capra neagră", ["zimbrul", "pelicanul", "delfinul"], "Simbol al munților.")
    X.a(2, "3.3", "Ce animal mare a fost reintrodus în Carpați (Vânători-Neamț, Munții Țarcu)?", "zimbrul", ["ursul polar", "renul", "bizonul american"], "Cel mai mare mamifer terestru din Europa.")
    X.pas("1. Etajele de vegetație", "Pe harta de vegetație din atlas, identifică zonele de vegetație ale României și urmărește cum se schimbă de la câmpie la munte.",
          jurnal="Desenează un munte cu etajele de vegetație și scrie numele fiecăruia.")
    X.a(2, "4.4", "Ce plantă ocrotită crește pe stâncile din munții înalți?", "floarea de colț", ["păpădia", "trandafirul de grădină", "porumbul"], "E interzisă culegerea ei.")
    X.pas("2. Fișa unei specii ocrotite", "Alege o plantă sau un animal ocrotit din România. Află unde trăiește, de ce e amenințat și cum e protejat.",
          jurnal="Scrie fișa speciei: nume, habitat, amenințări, protecție, sursa.")
    X.s(2, "4.4", "Asociază fenomenul cu regula de comportament.", [("viscolul", "nu pleci la drum; ai provizii și lanternă"), ("canicula", "stai la umbră, bei apă"), ("inundația", "urci pe un loc înalt, oprești curentul"), ("furtuna cu fulgere", "te adăpostești într-o clădire, nu sub copaci")], "Reguli de siguranță.")
    X.a(2, "4.4", "Ce înseamnă mesajul RO-ALERT pe telefon?", "o avertizare oficială despre un pericol iminent în zona ta", ["o reclamă", "o glumă", "un mesaj de la prieteni"], "Urmează instrucțiunile.")
    X.a(3, "4.2", "Ce fenomen hidrologic periculos e frecvent iarna pe râurile mari?", "podul de gheață, care poate bloca apa și produce inundații", ["seceta", "canicula", "grindina"], "Nu se merge pe gheața râului.")
    X.pas("3. Planul de siguranță", "Cu familia, alcătuiți un plan pentru o situație de urgență: ce luați în rucsacul de urgență, unde vă întâlniți, ce numere de telefon folosiți (112).",
          jurnal="Scrie lista din rucsacul de urgență și locul de întâlnire stabilit.")
    X.pas("4. Afișul clasei", "Realizați în grup un afiș cu regulile de comportament în caz de fenomen extrem din județul Buzău (inundații, alunecări, viscol, cutremur).",
          jurnal="Fotografiază afișul.", foto=True)

    return Unitate(8, "u3-clima-ape.json", "Clima, apele, vegetația, fauna și solurile").add(F, E, R, D, I, L, N, X)
