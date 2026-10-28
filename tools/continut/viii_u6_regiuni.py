from autor import Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_REG = ["Ministerul Dezvoltării – Regiunile de dezvoltare (Legea nr. 315/2004)", "Eurostat – Regional GDP per capita (NUTS 2)"]
RS = (45.38, 27.05)


def unitate():
    # ================================================================ S34a Diferențieri regionale
    D = Expeditie(8, "VIII-S34-diferentieri-regionale", "Expediție: diferențieri regionale",
                  "De ce unele regiuni ale României sunt mai dezvoltate decât altele?",
                  ref=REF.format("Diferențieri regionale"), prefix="VIII34a")
    D.a(1, "1.1", "Ce înseamnă „diferențieri regionale”?", "deosebirile dintre regiuni în ce privește natura, populația și economia", ["regiunile sunt identice", "granițele dintre state", "doar diferențe de climă"], "Natural, uman, economic.")
    D.s(2, "2.1", "Asociază regiunea de dezvoltare cu un oraș important.", [("Nord-Est", "Iași"), ("Sud-Est", "Constanța"), ("Vest", "Timișoara"), ("Nord-Vest", "Cluj-Napoca")], "Regiunile de dezvoltare.", surse=S_REG)
    D.a(2, "4.3", "Ce regiune de dezvoltare are cel mai mare PIB pe locuitor?", "București-Ilfov", ["Nord-Est", "Sud-Vest Oltenia", "Sud-Muntenia"], "Capitala concentrează servicii și investiții.", surse=S_REG)
    D.a(2, "4.3", "Ce regiune de dezvoltare are de obicei cel mai mic PIB pe locuitor?", "Nord-Est", ["București-Ilfov", "Vest", "Centru"], "Multe zone rurale, infrastructură mai slabă.", surse=S_REG)
    D.pas("1. Hărțile regiunilor", "Compară, în atlas, harta regiunilor de dezvoltare cu hărțile de relief, populație și economie.",
          jurnal="Scrie 2 diferențe între Regiunea Vest și Regiunea Nord-Est.")
    D.g(3, "2.3", "Graficul compară (schematic) PIB-ul pe locuitor în trei regiuni (indice, media națională = 100). Ce observi?", grafic("bare", "PIB pe locuitor, indice (schematic, media țării = 100)", [("București-Ilfov", 220), ("Vest", 100), ("Nord-Est", 60)], "indice", "Eurostat – Regional GDP (NUTS 2), prelucrare schematică"), "diferențe mari între capitală și celelalte regiuni", ["toate regiunile sunt egale", "Nord-Est e cea mai bogată", "Vest e cea mai săracă"], "Bucureștiul are de aproximativ trei ori PIB-ul pe locuitor al Regiunii Nord-Est.", surse=S_REG)
    D.a(3, "4.4", "Ce poate reduce diferențele dintre regiuni?", "autostrăzi, investiții, educație, fonduri europene pentru zonele mai puțin dezvoltate", ["închiderea școlilor", "mutarea tuturor în capitală", "nimic"], "Politica de coeziune a UE.")
    D.pas("2. Cauzele", "Discută în grup: ce factori (poziție, relief, drumuri, orașe mari, istorie) fac o regiune mai dezvoltată?",
          jurnal="Notează 3 factori și un exemplu pentru fiecare.")
    D.a(2, "4.2", "În ce regiune de dezvoltare se află Râmnicu Sărat?", "Sud-Est", ["Nord-Est", "Centru", "Sud-Muntenia"], "Județul Buzău e în Regiunea Sud-Est.", surse=S_REG)
    D.pas("3. Regiunea noastră", "Caracterizează pe scurt Regiunea Sud-Est: județe, relief, orașe mari, activități economice.",
          jurnal="Scrie 5 rânduri despre Regiunea Sud-Est.")

    # ================================================================ S34b Regiunile geografice pe baze naturale
    R = Expeditie(8, "VIII-S34-regiunile-geografice-baze-naturale", "Expediție: regiunile geografice ale României",
                  "Cum ai împărți România după natură, nu după județe?",
                  ref=REF.format("Regiunile geografice pe baze naturale"), prefix="VIII34b")
    R.s(1, "1.2", "Asociază regiunea geografică cu trăsătura ei principală.", [("Carpații", "munți, păduri, pășuni"), ("Depresiunea Transilvaniei", "dealuri și podișuri, gaze și sare"), ("Câmpia Română", "cereale, cernoziom"), ("Delta Dunării", "ape, stuf, păsări")], "Regiuni naturale.")
    R.a(2, "1.2", "Ce criterii se folosesc pentru regiunile pe baze naturale?", "relieful, clima, apele, vegetația și solurile", ["numărul de magazine", "partidele politice", "culoarea caselor"], "Caracteristicile naturale.")
    R.e(2, "2.1", "Pune pe hartă regiunile geografice.", [("ca", "Carpații", 45.6, 24.7), ("tr", "Depresiunea Transilvaniei", 46.6, 24.4), ("cr", "Câmpia Română", 44.4, 26), ("dd", "Delta Dunării", 45.1, 29.3), ("pm", "Podișul Moldovei", 47, 27.3)], "Unitățile majore.", harta="romania")
    R.pas("1. Harta regiunilor", "Pe harta fizică a României, delimitează cu creionul regiunile geografice mari și dă-le un nume.",
          jurnal="Fotografiază harta.", foto=True)
    R.a(2, "2.2", "Ce regiune naturală are cele mai puține precipitații?", "Dobrogea", ["Carpații Meridionali", "Maramureșul", "Bucovina"], "Sub 400 l/m² pe an în unele zone.")
    R.a(3, "4.3", "Compară regiunea Subcarpaților cu Câmpia Română.", "Subcarpații au dealuri, livezi, vii și alunecări; câmpia are cereale, cernoziom și secetă", ["sunt identice", "câmpia are alunecări mai multe", "Subcarpații au deltă"], "Diferențe naturale și economice.")
    R.pas("2. Comparația", "Alege două regiuni naturale și compară-le după relief, climă, ape, vegetație și ocupațiile oamenilor.",
          jurnal="Completează un tabel comparativ.")
    R.a(2, "4.2", "În ce regiuni naturale se întinde județul Buzău?", "Carpații de Curbură, Subcarpații de Curbură și Câmpia Română", ["doar Delta Dunării", "doar Podișul Moldovei", "Munții Apuseni"], "Județul are toate cele trei trepte.")
    R.pas("3. Județul în regiuni", "Arată pe hartă cum se împarte județul Buzău între munte, deal și câmpie.",
          jurnal="Scrie ce ocupații au oamenii în fiecare treaptă.")

    # ================================================================ S34c Caracterizarea unei regiuni
    C = Expeditie(8, "VIII-S34-aplicatii-practice-studii-caz", "Expediție: caracterizarea unei regiuni la alegere",
                  "Ce regiune a României ai prezenta colegilor și de ce?",
                  ref=REF.format("Aplicații practice/studii de caz: Caracterizarea geografică a unei regiuni"), prefix="VIII34c")
    C.o(1, "4.1", "Ordonează pașii caracterizării unei regiuni.", ["poziția și limitele", "relieful", "clima și apele", "vegetația, fauna, solurile", "populația și așezările", "economia", "probleme și perspective"], "Algoritmul", "De la natural la uman.")
    C.pas("1. Alege regiunea", "Alege o regiune: Maramureș, Bucovina, Țara Bârsei, Delta Dunării, Banat, Oltenia, Dobrogea sau Ținutul Buzăului.")
    C.a(2, "4.1", "Ce surse folosești pentru caracterizare?", "atlasul, manualul, INS, site-urile oficiale ale județelor și parcurilor", ["comentarii anonime", "reclame", "jocuri video"], "Notează sursa fiecărei cifre.")
    C.pas("2. Datele", "Adună informațiile pentru fiecare pas al algoritmului. Pentru cifre, notează sursa și anul.",
          jurnal="Scrie tabelul cu datele și sursele.")
    C.a(2, "4.4", "Ce problemă de mediu are Delta Dunării?", "poluarea apelor și braconajul", ["deșertificarea totală", "avalanșele", "vulcanii"], "Măsuri: zone strict protejate.")
    C.pas("3. Probleme și soluții", "Identifică o problemă a regiunii și propune o soluție.",
          jurnal="Scrie problema și soluția.")
    C.pas("4. Prezentarea", "Prezintă regiunea în 3 minute, cu o hartă și 3 imagini (făcute de tine sau cu licență liberă).",
          jurnal="Fotografiază un diapozitiv al prezentării.", foto=True)

    return Unitate(8, "u6-regiuni.json", "Regiuni geografice și dezvoltarea regională").add(D, R, C)
