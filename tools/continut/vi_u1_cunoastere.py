from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VI-a (manuale.edu.ro), lecția „{}”"
S_ONU = ["Organizația Națiunilor Unite – Member States (un.org)", "Wikipedia – Member states of the United Nations"]
S_EXPL = ["Encyclopaedia Britannica – European exploration: The Age of Discovery", "Wikipedia – Age of Discovery"]
S_SPATIU = ["NASA History Office – Apollo 11 Mission Overview", "ESA – Yuri Gagarin, first human in space"]
S_RACOVITA = ["Institutul de Speologie „Emil Racoviță” – biografie", "Wikipedia – Belgian Antarctic Expedition"]


def unitate():
    # ================================================================ S2 Repere ale cunoașterii Terrei
    R = Lectie(6, "VI-S02-repere-cunoasterii-terrei-marile", "Repere ale cunoașterii Terrei",
               "Cum au aflat oamenii cum arată lumea, înainte de sateliți și GPS?",
               [("Marile descoperiri geografice", "În secolele XV–XVI, navigatorii europeni au pornit pe oceane, în căutarea unor drumuri noi spre India și China.\nCristofor Columb a ajuns în America în 1492. Vasco da Gama a ocolit Africa și a ajuns în India pe mare, în 1498. Expediția lui Fernando Magellan (1519–1522) a făcut prima călătorie în jurul lumii, dovedind că Pământul e rotund și că oceanele comunică între ele."),
                ("Explorarea regiunilor polare și a înălțimilor", "Roald Amundsen a ajuns primul la Polul Sud, pe 14 decembrie 1911. Edmund Hillary și Tenzing Norgay au urcat primii pe Everest, pe 29 mai 1953.\nRomânul Emil Racoviță a participat la expediția belgiană „Belgica” (1897–1899), prima care a iernat în Antarctica. El a fondat apoi biospeologia, știința vieții din peșteri."),
                ("Explorarea modernă", "Iuri Gagarin a fost primul om în spațiu, pe 12 aprilie 1961. Pe 20 iulie 1969, astronauții misiunii Apollo 11 au pus piciorul pe Lună.\nAstăzi, sateliții fotografiază Pământul zilnic, iar GPS-ul ne arată poziția oriunde ne-am afla. Rămân încă locuri puțin explorate: adâncurile oceanelor și unele peșteri.")],
               stiaica="Dintre cele cinci corăbii ale lui Magellan, doar una, „Victoria”, s-a întors în Spania, cu 18 oameni. Magellan însuși a murit pe drum, în Filipine.",
               ref=REF.format("Repere ale cunoașterii Terrei"))
    R.a(1, "1.1", "Ce înseamnă „mari descoperiri geografice”?", "călătoriile europenilor din secolele XV–XVI, în care au ajuns pe continente și oceane necunoscute lor", ["inventarea hărții", "zborurile în spațiu", "construirea primelor orașe"], "Atunci europenii au cunoscut America și drumul pe mare spre India.")
    R.a(1, "2.2", "În ce an a ajuns Cristofor Columb în America?", "1492", ["1918", "1969", "1066"], "Columb a ajuns în insulele Caraibe în 1492.", surse=S_EXPL)
    R.a(2, "2.2", "Ce a reușit Vasco da Gama în 1498?", "a ajuns în India pe mare, ocolind Africa", ["a descoperit America", "a ajuns la Polul Sud", "a urcat pe Everest"], "Drumul pe mare spre India trecea pe la Capul Bunei Speranțe.", surse=S_EXPL)
    R.a(2, "1.2", "Ce a dovedit expediția lui Magellan (1519–1522)?", "că Pământul e rotund și că poți face înconjurul lumii pe mare", ["că Pământul e plat", "că nu există Oceanul Pacific", "că Africa e o insulă"], "Corabia „Victoria” s-a întors de unde a plecat, navigând mereu spre vest.", surse=S_EXPL)
    R.o(2, "2.2", "Ordonează evenimentele în timp.", ["Columb ajunge în America", "Vasco da Gama ajunge în India", "expediția lui Magellan în jurul lumii", "Amundsen la Polul Sud", "primul om pe Lună"], "Cronologic", "1492, 1498, 1519–1522, 1911, 1969.", surse=S_EXPL)
    R.s(2, "1.1", "Asociază exploratorul cu realizarea.", [("Cristofor Columb", "ajunge în America (1492)"), ("Roald Amundsen", "primul la Polul Sud (1911)"), ("Hillary și Tenzing", "primii pe Everest (1953)"), ("Iuri Gagarin", "primul om în spațiu (1961)")], "Repere ale explorării.")
    R.a(2, "2.2", "Cine a ajuns primul la Polul Sud?", "Roald Amundsen, în 1911", ["Cristofor Columb, în 1492", "Neil Armstrong, în 1969", "Emil Racoviță, în 1897"], "Expediția norvegiană a lui Amundsen a ajuns pe 14 decembrie 1911.")
    R.a(2, "3.4", "În ce expediție a participat românul Emil Racoviță?", "expediția belgiană „Belgica”, în Antarctica (1897–1899)", ["expediția lui Columb", "misiunea Apollo 11", "prima urcare pe Everest"], "„Belgica” a fost prima expediție care a iernat în Antarctica.", surse=S_RACOVITA)
    R.a(2, "1.1", "Ce știință a fondat Emil Racoviță?", "biospeologia – studiul vieții din peșteri", ["astronomia", "vulcanologia", "meteorologia"], "La Cluj a înființat primul institut de speologie din lume.", surse=S_RACOVITA)
    R.a(2, "2.2", "Când au pus oamenii pentru prima dată piciorul pe Lună?", "pe 20 iulie 1969, în misiunea Apollo 11", ["în 1492", "în 1911", "în 2001"], "Neil Armstrong și Buzz Aldrin au coborât pe Lună.", surse=S_SPATIU)
    R.a(2, "2.2", "Cine a fost primul om în spațiu?", "Iuri Gagarin, în 1961", ["Neil Armstrong, în 1969", "Magellan, în 1519", "Amundsen, în 1911"], "Gagarin a făcut o orbită în jurul Pământului pe 12 aprilie 1961.", surse=S_SPATIU)
    R.p(2, "2.1", "Atinge pe hartă Capul Bunei Speranțe, ocolit de Vasco da Gama.", "lume", -34.36, 18.47, "Capul Bunei Speranțe", 600, "Capul e la capătul sudic al Africii.")
    R.p(2, "2.1", "Atinge pe hartă insulele Caraibe, unde a ajuns Columb în 1492.", "lume", 21, -75, "Caraibe", 900, "Columb a ajuns în Bahamas și Cuba, între America de Nord și America de Sud.")
    R.p(3, "2.1", "Atinge pe hartă India, ținta lui Vasco da Gama.", "lume", 20, 78, "India", 900, "India e în sudul Asiei.")
    R.p(3, "2.1", "Atinge pe hartă Strâmtoarea Magellan, din sudul Americii de Sud.", "lume", -53.5, -70.5, "Strâmtoarea Magellan", 700, "Magellan a trecut din Atlantic în Pacific prin această strâmtoare.")
    R.a(2, "3.1", "Ce folosim astăzi ca să aflăm poziția exactă oriunde pe Pământ?", "sistemul GPS, cu sateliți", ["busola singură", "un ceas", "un termometru"], "Receptorul GPS calculează poziția după semnalele mai multor sateliți.")
    R.a(2, "3.1", "La ce folosesc sateliții de observare a Pământului?", "fotografiază suprafața, urmăresc vremea, pădurile, gheața și orașele", ["produc ploaie", "măsoară adâncimea solului", "trimit oameni pe Lună"], "Imaginile satelitare ajută la hărți și prognoze.")
    R.adev(2, "1.2", "Columb credea că a ajuns în India, de aceea locuitorii Americii au fost numiți „indieni”.", True, "Adevărat: Columb voia să ajungă în Asia navigând spre vest.")
    R.adev(2, "1.2", "Astăzi, toată suprafața și toate adâncurile Pământului sunt complet explorate.", False, "Fals: fundul oceanelor și multe peșteri sunt încă puțin cunoscute.")
    R.l(2, "1.1", "Completează.", "Prima călătorie în jurul lumii a fost condusă de [Magellan]; primul om pe Lună a ajuns în anul [1969].", ["Columb", "1492"], "Magellan (1519–1522); Apollo 11 (1969).")
    R.l(2, "3.4", "Completează.", "Exploratorul român [Emil Racoviță] a participat la expediția belgiană în [Antarctica].", ["Africa", "Iuri Gagarin"], "Expediția „Belgica”, 1897–1899.")
    R.a(2, "1.2", "De ce au căutat europenii un drum pe mare spre India, în secolul XV?", "pentru mirodenii, mătase și alte mărfuri scumpe, fără să treacă pe uscat prin multe țări", ["ca să ajungă la Polul Sud", "ca să vadă pinguini", "ca să caute petrol"], "Comerțul cu mirodenii era foarte profitabil.")
    R.a(3, "1.2", "Ce schimbări au adus marile descoperiri geografice?", "hărți noi, schimb de plante și animale între continente, dar și colonizarea și suferința popoarelor locale", ["doar lucruri bune pentru toți", "nicio schimbare", "dispariția oceanelor"], "Istoria are și urmări pozitive, și negative.")
    R.a(2, "3.3", "Ce plante au ajuns în Europa din America după 1492?", "porumbul, cartoful, roșia", ["grâul și orzul", "măslinul și vița-de-vie", "stejarul și fagul"], "Schimbul de plante între continente a schimbat hrana oamenilor.")
    R.a(2, "4.2", "Cum se numesc oamenii care cercetează peșterile?", "speologi", ["astronauți", "meteorologi", "vulcanologi"], "Speologia studiază peșterile.")
    R.a(2, "3.1", "Ce instrument a ajutat navigatorii din secolul XV să știe în ce direcție merg?", "busola", ["GPS-ul", "telefonul", "radarul"], "Busola arată nordul magnetic.")
    R.g(3, "2.3 4.1", "Graficul arată durata unor călătorii celebre (aproximativ). Care a durat cel mai mult?", grafic("bare", "Durata aproximativă a călătoriei", [("Columb, 1492 (dus)", 2), ("Vasco da Gama, 1497–1498 (dus)", 10), ("Magellan, 1519–1522 (în jurul lumii)", 36)], "luni", "Encyclopaedia Britannica"), "expediția lui Magellan", ["călătoria lui Columb", "călătoria lui Vasco da Gama", "au durat la fel"], "Înconjurul lumii a durat aproape trei ani.", surse=S_EXPL)
    R.a(2, "4.3", "Ce au în comun Amundsen, Hillary și Racoviță?", "toți au explorat locuri foarte greu accesibile", ["toți au zburat în spațiu", "toți au descoperit America", "toți au fost meteorologi"], "Polul Sud, Everest, Antarctica.")
    R.d(2, "2.1", "Ce continent, explorat abia în secolele XIX–XX, e marcat pe hartă?", "lume", -80, 30, "Antarctica", ["Australia", "America de Sud", "Africa"], "Antarctica a fost ultimul continent explorat.")
    R.a(3, "4.1", "Vrei să afli traseul lui Magellan. Ce surse sunt de încredere?", "atlasul istoric, enciclopediile și site-urile muzeelor sau universităților", ["un comentariu anonim pe o rețea socială", "o reclamă", "un joc fără autor"], "Verifică informația în cel puțin două surse serioase.")

    # ================================================================ S3 Continente și țări – harta politică
    H = Lectie(6, "VI-S03-continente-tari-reprezentari-cartografice", "Continente și țări. Harta politică a lumii",
               "Câte țări sunt pe lume și cum le deosebești pe hartă?",
               [("Continentele și oceanele", "Pe Pământ sunt șapte continente: Asia, Africa, America de Nord, America de Sud, Antarctica, Europa și Australia (în unele țări, cele două Americi sunt socotite un singur continent). Oceanele le despart: Pacific, Atlantic, Indian, Arctic și Oceanul de Sud.\nEuropa și Asia formează împreună Eurasia; granița lor convențională trece pe Munții Ural, râul Ural, Marea Caspică, Munții Caucaz."),
                ("Statele lumii", "Un stat (o țară) are un teritoriu cu granițe, o populație și o conducere proprie. Capitala e orașul unde se află conducerea.\nOrganizația Națiunilor Unite (ONU) are 193 de state membre. Cea mai mare țară ca suprafață e Rusia; cel mai mic stat e Vaticanul."),
                ("Harta politică", "Harta politică arată statele cu culori diferite, granițele, capitalele și orașele mari. Țările vecine au culori diferite, ca să poată fi deosebite.\nHarta fizică arată relieful și apele; harta politică arată statele. Le folosim împreună.")],
               stiaica="Vaticanul, cel mai mic stat din lume, are o suprafață de mai puțin de jumătate de kilometru pătrat și se află în interiorul orașului Roma.",
               ref=REF.format("Continente și țări – reprezentări cartografice"))
    H.e(2, "2.1", "Pune pe hartă numele continentelor.", [("as", "Asia", 50, 90), ("af", "Africa", 5, 20), ("eu", "Europa", 52, 15), ("an", "America de Nord", 45, -100), ("as2", "America de Sud", -15, -60), ("au", "Australia", -25, 134)], "Asia la est, Africa la sud de Europa, cele două Americi la vest, Australia în sud-est.", harta="lume")
    H.a(1, "1.1", "Ce este un stat?", "un teritoriu cu granițe, populație și conducere proprie", ["un continent", "un munte", "un ocean"], "Statul se mai numește țară.")
    H.a(1, "1.1", "Ce este capitala?", "orașul în care se află conducerea țării", ["cel mai mic oraș", "orașul de lângă mare", "orice oraș"], "București e capitala României.")
    H.a(2, "3.1", "Câte state membre are ONU?", "193", ["50", "27", "1 000"], "Organizația Națiunilor Unite are 193 de state membre.", surse=S_ONU)
    H.a(1, "4.3", "Care e cea mai mare țară din lume ca suprafață?", "Rusia", ["China", "SUA", "Brazilia"], "Rusia se întinde în Europa și Asia.")
    H.a(2, "4.3", "Care e cel mai mic stat din lume?", "Vaticanul", ["Monaco", "Luxemburg", "Malta"], "Vaticanul e în orașul Roma.")
    H.a(2, "2.3", "Ce arată harta politică?", "statele, granițele și capitalele", ["relieful și râurile", "temperaturile", "vegetația"], "Harta fizică arată relieful; cea politică, statele.")
    H.a(2, "2.3", "De ce țările vecine au culori diferite pe harta politică?", "ca să se vadă clar unde se termină o țară și unde începe alta", ["pentru că au climă diferită", "pentru că au munți diferiți", "fără motiv"], "Culorile nu au legătură cu relieful.")
    H.p(1, "2.1", "Atinge pe hartă România.", "lume", 46, 25, "România", 400, "România e în sud-estul Europei centrale, la Marea Neagră.")
    H.p(2, "2.1", "Atinge pe hartă Rusia.", "lume", 60, 90, "Rusia", 2500, "Rusia acoperă estul Europei și nordul Asiei.")
    H.p(2, "2.1", "Atinge pe hartă Brazilia.", "lume", -10, -52, "Brazilia", 1500, "Brazilia ocupă aproape jumătate din America de Sud.")
    H.p(2, "2.1", "Atinge pe hartă Egiptul.", "lume", 26, 30, "Egipt", 700, "Egiptul e în nord-estul Africii, pe Nil.")
    H.p(3, "2.1", "Atinge pe hartă Japonia.", "lume", 36, 138, "Japonia", 700, "Japonia e un arhipelag în estul Asiei.")
    H.p(3, "2.1", "Atinge pe hartă Canada.", "lume", 60, -100, "Canada", 2000, "Canada e în nordul Americii de Nord.")
    H.s(2, "2.1", "Asociază țara cu capitala ei.", [("Franța", "Paris"), ("Italia", "Roma"), ("Germania", "Berlin"), ("Spania", "Madrid")], "Capitale europene importante.")
    H.s(2, "2.1", "Asociază țara cu continentul.", [("China", "Asia"), ("Nigeria", "Africa"), ("Argentina", "America de Sud"), ("Mexic", "America de Nord")], "Fiecare țară e pe un continent (Rusia și Turcia sunt pe două).")
    H.a(2, "2.1", "Ce lanț muntos e considerat granița dintre Europa și Asia?", "Munții Ural", ["Munții Alpi", "Munții Carpați", "Munții Anzi"], "Uralii sunt în Rusia.")
    H.a(2, "1.1", "Ce înseamnă Eurasia?", "Europa și Asia luate împreună, ca o singură masă de uscat", ["o țară din Asia", "un ocean", "o insulă"], "Europa și Asia nu sunt despărțite de ocean.")
    H.a(3, "2.1", "Ce țări se întind pe două continente?", "Rusia și Turcia", ["Franța și Italia", "Brazilia și Chile", "Japonia și Coreea"], "Rusia și Turcia au teritorii și în Europa, și în Asia.")
    H.adev(2, "1.2", "Granițele dintre state se văd mereu în natură, ca niște ziduri.", False, "Fals: majoritatea granițelor sunt linii convenționale; uneori urmează râuri sau munți.")
    H.adev(2, "2.3", "Pe harta politică, culoarea unei țări nu arată relieful ei.", True, "Adevărat: culorile doar deosebesc țările.")
    H.l(2, "1.1", "Completează.", "Cea mai mare țară ca suprafață este [Rusia], iar cel mai mic stat este [Vaticanul].", ["China", "Monaco"], "Rusia – cea mai mare; Vaticanul – cel mai mic.")
    H.l(2, "2.1", "Completează.", "Capitala Franței este [Paris], iar capitala Italiei este [Roma].", ["Berlin", "Madrid"], "Paris și Roma.")
    H.o(2, "4.3", "Ordonează continentele după suprafață, de la cel mai mare la cel mai mic.", ["Asia", "Africa", "America de Nord", "America de Sud", "Antarctica", "Europa", "Australia"], "Suprafață, descrescător", "Asia e cea mai mare; Australia cea mai mică.")
    H.a(2, "2.2", "Ce face o hartă digitală (ca o aplicație de hărți) în plus față de una tipărită?", "poți mări, micșora, căuta locuri și afla trasee", ["arată mereu doar un oraș", "nu are legendă", "nu se poate folosi"], "Hărțile digitale sunt interactive.")
    H.d(2, "2.1", "Ce țară e marcată pe hartă?", "lume", -25, 134, "Australia", ["Noua Zeelandă", "Indonezia", "Madagascar"], "Australia e țara-continent din emisfera sudică.")
    H.d(3, "2.1", "Ce țară e marcată pe hartă?", "lume", 39, -98, "Statele Unite ale Americii", ["Canada", "Mexic", "Brazilia"], "SUA sunt în mijlocul Americii de Nord.")
    H.a(3, "3.2", "De ce granițele unor țări din Africa sunt linii drepte?", "pentru că au fost trasate pe hartă de puterile coloniale, nu după relief sau popoare", ["pentru că acolo nu sunt munți", "pentru că așa au cerut animalele", "pentru că sunt râuri drepte"], "Multe granițe africane au fost trasate în secolul XIX.")
    H.a(2, "1.1", "Ce este o țară fără ieșire la mare?", "o țară care nu are țărm la o mare sau la un ocean", ["o insulă", "o țară cu multe porturi", "o peninsulă"], "Ungaria, Elveția și Austria nu au ieșire la mare.")
    H.a(2, "2.1", "Ce țară vecină cu România nu are ieșire la mare?", "Ungaria", ["Bulgaria", "Ucraina", "nicio țară vecină"], "Ungaria și Serbia nu au ieșire la mare; Bulgaria și Ucraina au țărm la Marea Neagră.")

    # ================================================================ S5 Expediție: distanțe și suprafețe pe hartă
    E = Expeditie(6, "VI-S05-aplicatii-practice-exercitii-apreciere", "Expediție: măsor lumea pe hartă",
                  "Cât de departe e Râmnicu Sărat de București, în linie dreaptă și pe drum?",
                  ref=REF.format("Aplicații practice: Exerciții de apreciere a distanțelor și suprafețelor"))
    E.a(1, "4.1", "Pe o hartă la scara 1:1 000 000, cât înseamnă 1 cm?", "10 km", ["1 km", "100 km", "1 000 km"], "1 000 000 cm = 10 000 m = 10 km.")
    E.a(2, "4.2", "Pe aceeași hartă, două orașe sunt la 13 cm. Ce distanță e în linie dreaptă?", "130 km", ["13 km", "1 300 km", "1,3 km"], "13 × 10 km = 130 km.")
    E.pas("1. Scara hărții", "Folosește harta României din atlas. Citește scara și calculează cât înseamnă 1 cm în realitate.")
    E.a(2, "4.3", "De ce distanța pe drum e mai mare decât cea în linie dreaptă?", "pentru că drumul ocolește dealuri, râuri și trece prin localități", ["pentru că harta e greșită", "pentru că mașinile merg în cerc", "nu e niciodată mai mare"], "Linia dreaptă e cea mai scurtă.")
    E.pas("2. Linie dreaptă și drum", "Măsoară cu rigla distanța Râmnicu Sărat – București pe hartă și transform-o cu scara. Apoi caută distanța pe drum într-o aplicație de hărți (cu un adult).",
          jurnal="Scrie distanța în linie dreaptă, distanța pe drum și diferența dintre ele.")
    E.a(3, "4.2", "Un teren dreptunghiular are pe hartă (1:100 000) 2 cm pe 3 cm. Ce suprafață are în realitate?", "6 km²", ["6 cm²", "60 km²", "600 km²"], "2 cm = 2 km, 3 cm = 3 km; 2 × 3 = 6 km².")
    E.pas("3. Suprafețe cu pătrățele", "Pune o folie cu pătrățele de 1 cm peste harta județului Buzău și numără pătrățelele acoperite (jumătățile se numără împreună). Transformă în km² cu ajutorul scării.",
          jurnal="Notează câte pătrățele ai numărat și cât ai obținut. Compară cu valoarea oficială găsită de profesor.")
    E.pas("4. Harta digitală", "Într-o aplicație de hărți, folosește funcția „Măsoară distanța”. Măsoară drumul de acasă la școală.",
          jurnal="Notează distanța și cât timp îți ia pe jos.")

    return Unitate(6, "u1-cunoastere.json", "Cunoașterea lumii în care trăim").add(R, H, E)
