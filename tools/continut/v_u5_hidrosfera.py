from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"
S_APA = ["USGS Water Science School – Where is Earth's Water?", "USGS – How Much Water is There on Earth?"]
S_GHEATA = ["USGS Water Science School – Ice, Snow, and Glaciers and the Water Cycle", "Water Education Foundation – The Earth's Water Supply"]
S_MARIANA = ["NOAA Ocean Exploration – How deep is the Mariana Trench?", "Wikipedia – Challenger Deep"]
S_NIL = ["Encyclopaedia Britannica – Nile River", "Wikipedia – Nile"]
S_DUNARE = ["ICPDR (Comisia Internațională pentru Protecția Dunării) – Danube Basin facts", "Wikipedia – Danube"]
S_BAIKAL = ["UNESCO World Heritage Centre – Lake Baikal", "Encyclopaedia Britannica – Lake Baikal"]
S_CASPIC = ["Encyclopaedia Britannica – Caspian Sea", "Wikipedia – Caspian Sea"]
RS = (45.38, 27.05)


def unitate():
    # ================================================================ S23 Hidrosfera: caracteristici generale
    H = Lectie(5, "V-S23-caracteristici-generale-importanta", "Hidrosfera – caracteristici generale și importanță",
               "Dacă Pământul e acoperit mai ales de apă, de ce spunem că apa potabilă e puțină?",
               [("Ce este hidrosfera", "Hidrosfera este învelișul de apă al Pământului: oceanele și mările, râurile, lacurile, apele subterane, ghețarii și vaporii de apă din atmosferă.\nApa acoperă aproximativ 71 % din suprafața Pământului. De aceea, văzut din spațiu, Pământul e numit „Planeta albastră”."),
                ("Apa sărată și apa dulce", "Aproape toată apa Pământului, aproximativ 96,5 %, e sărată și se află în oceane și mări.\nApa dulce reprezintă doar aproximativ 2,5 % din total, iar cea mai mare parte din ea e înghețată în ghețari sau ascunsă în subteran. Râurile și lacurile conțin o parte foarte mică."),
                ("Circuitul apei în natură", "Apa se mișcă mereu: Soarele o încălzește și ea se evaporă; vaporii urcă, se răcesc și formează nori; din nori cad precipitațiile; apa se scurge prin râuri sau se infiltrează în sol și ajunge înapoi în mări și oceane.\nAșa, aceeași apă circulă de miliarde de ani.")],
               stiaica="Dacă toată apa Pământului ar încăpea într-o sticlă de 1 litru, apa dulce din râuri și lacuri ar fi doar câteva picături.",
               ref=REF.format("Hidrosfera – caracteristici generale și importanță"))
    H.a(1, "1.1", "Ce este hidrosfera?", "învelișul de apă al Pământului", ["învelișul de aer", "stratul de roci", "lumea plantelor"], "Hidro- înseamnă apă.")
    H.a(1, "1.1", "Ce parte din suprafața Pământului e acoperită de apă?", "aproximativ 71 %", ["aproximativ 10 %", "aproximativ 29 %", "aproximativ 99 %"], "Apa acoperă aproximativ 71 %, uscatul aproximativ 29 %.", surse=S_APA)
    H.a(2, "3.1", "Ce procent din apa Pământului se află în oceane și mări?", "aproximativ 96,5 %", ["aproximativ 50 %", "aproximativ 2,5 %", "aproximativ 71 %"], "Oceanele conțin aproximativ 96,5 % din toată apa.", surse=S_APA)
    H.a(2, "3.1", "Ce procent din apa Pământului este apă dulce?", "aproximativ 2,5 %", ["aproximativ 25 %", "aproximativ 50 %", "aproximativ 96,5 %"], "Doar aproximativ 2,5 % din apă e dulce.", surse=S_APA)
    H.a(2, "3.1", "Unde se află cea mai mare parte a apei dulci?", "înghețată în ghețari și calote", ["în râuri", "în lacuri", "în nori"], "Peste două treimi din apa dulce e înghețată.", surse=S_GHEATA)
    H.g(2, "2.3", "Graficul arată împărțirea apei de pe Pământ. Ce fel de apă e cea mai multă?", grafic("structura", "Apa de pe Pământ", [("apă sărată (oceane, mări)", 97.5), ("apă dulce", 2.5)], "%", "USGS Water Science School"), "apa sărată", ["apa dulce", "sunt egale", "apa din râuri"], "Apa sărată e aproximativ 97,5 % (oceane, mări și puțină apă sărată subterană).", surse=S_APA)
    H.s(1, "1.1", "Asociază componenta hidrosferei cu exemplul.", [("ocean", "Oceanul Pacific"), ("mare", "Marea Neagră"), ("râu", "Dunărea"), ("lac", "Lacul Bâlea")], "Toate fac parte din hidrosferă.")
    H.o(2, "1.2", "Ordonează etapele circuitului apei în natură.", ["evaporarea apei din mări", "formarea norilor", "căderea precipitațiilor", "scurgerea apei prin râuri înapoi în mare"], "Ordinea circuitului", "Evaporare, condensare, precipitații, scurgere.")
    H.s(2, "1.1", "Asociază etapa circuitului apei cu explicația.", [("evaporarea", "apa devine vapori"), ("condensarea", "vaporii devin picături, nori"), ("precipitațiile", "apa cade din nori"), ("infiltrarea", "apa pătrunde în sol")], "Fiecare etapă are numele ei.")
    H.a(2, "1.2", "Ce pune în mișcare circuitul apei?", "căldura Soarelui și atracția gravitațională", ["vântul de la poli", "Luna", "vulcanii"], "Soarele evaporă apa; gravitația o aduce înapoi jos.")
    H.adev(1, "1.2", "Apa din oceane e bună de băut.", False, "Fals: e sărată; trebuie desalinizată ca să poată fi băută.")
    H.adev(2, "1.2", "Apa de pe Pământ se mișcă mereu, prin circuitul apei.", True, "Adevărat: evaporare, nori, precipitații, scurgere.")
    H.adev(2, "3.3", "Apa dulce e o resursă care trebuie protejată, pentru că e puțină.", True, "Adevărat: doar o mică parte din apa Pământului e dulce și accesibilă.")
    H.l(1, "1.1", "Completează.", "Pământul e numit „Planeta [albastră]”, pentru că e acoperit mai ales de [apă].", ["roșie", "nisip"], "Din spațiu, oceanele fac Pământul să pară albastru.")
    H.l(2, "1.2", "Completează.", "Apa se transformă în vapori prin [evaporare], iar vaporii devin picături în nori prin [condensare].", ["topire", "înghețare"], "Evaporare și condensare sunt două etape ale circuitului.")
    H.a(2, "3.3", "La ce folosesc oamenii apa?", "la băut, agricultură (irigații), industrie, energie și transport", ["doar la spălat", "doar la înot", "nu o folosesc"], "Apa e esențială pentru viață și economie.")
    H.a(2, "3.3", "Ce activitate consumă cea mai mare parte din apa dulce folosită de oameni?", "agricultura (irigațiile)", ["spălatul pe dinți", "băutul", "piscinele"], "Irigațiile folosesc cea mai multă apă.")
    H.a(2, "1.1", "Cum se numește apa care se află în sol și în roci, sub suprafața pământului?", "apă subterană (freatică)", ["apă de mare", "apă de ploaie", "vapori"], "Fântânile scot apa subterană.")
    H.a(2, "3.3", "De unde vine apa din fântânile de la sat?", "din apa subterană", ["din ocean", "din nori, direct", "din ghețari"], "Fântâna e săpată până la stratul de apă subterană.")
    H.a(2, "4.3", "Cum poți economisi apa acasă?", "închizi robinetul când te speli pe dinți și faci duș scurt", ["lași robinetul deschis", "speli mașina zilnic cu furtunul", "umpli cada de mai multe ori"], "Fiecare litru economisit contează.")
    H.a(3, "1.2", "De ce ploaia e apă dulce, deși vine din apa sărată a oceanului?", "pentru că sarea nu se evaporă; doar apa se transformă în vapori", ["pentru că ploaia vine de pe Lună", "pentru că norii filtrează sarea", "pentru că ploaia vine doar din râuri"], "La evaporare, sarea rămâne în ocean.")
    H.a(3, "4.1", "Cum arăți acasă că sarea nu se evaporă?", "lași o farfurie cu apă sărată la soare; după ce apa dispare, rămâne sarea", ["fierbi apa dulce", "pui apa la congelator", "amesteci apa cu nisip"], "Așa se obține și sarea din saline, la mare.")
    H.a(2, "3.2", "Ce se întâmplă cu apa unei bălți într-o zi foarte caldă?", "se evaporă", ["îngheață", "se transformă în sare", "rămâne neschimbată"], "Căldura grăbește evaporarea.")
    H.a(2, "1.2", "Ce sunt izvoarele?", "locurile unde apa subterană iese la suprafață", ["gurile de vărsare ale râurilor", "valurile mării", "ghețarii"], "Din izvoare se nasc multe râuri.")
    H.a(3, "3.3", "Ce poluează apele?", "deșeurile aruncate, apele uzate netratate și îngrășămintele spălate de pe câmpuri", ["peștii", "plantele de pe mal", "ploaia curată"], "Poluarea apei afectează oamenii și viețuitoarele.")
    H.a(2, "1.1", "Ce stare are apa în ghețari?", "solidă (gheață)", ["lichidă", "gazoasă", "nu are stare"], "Apa există în trei stări: solidă, lichidă, gazoasă.")
    H.s(2, "1.1", "Asociază starea apei cu exemplul.", [("solidă", "gheața de pe lac"), ("lichidă", "apa din râu"), ("gazoasă", "vaporii din aer"), ("solidă, căzută din nori", "zăpada")], "Apa trece mereu dintr-o stare în alta.")
    H.a(3, "3.2", "De ce e important ca pădurile să nu fie tăiate pe versanți?", "rădăcinile țin solul și ajută apa să se infiltreze, reducând inundațiile", ["pădurile cresc nivelul oceanului", "copacii produc ploaie sărată", "nu are legătură cu apa"], "Pădurea reține apa ca un burete.")
    H.a(2, "4.3", "Ce înseamnă „apă potabilă”?", "apă bună de băut, curată, fără microbi și substanțe dăunătoare", ["orice apă din natură", "apă de mare", "apă din bălți"], "Apa potabilă e verificată înainte de a ajunge la robinet.")
    H.a(3, "1.2", "De ce se spune că apa e „aceeași de milioane de ani”?", "pentru că circulă mereu prin circuitul apei, fără să dispară", ["pentru că nu se mișcă niciodată", "pentru că e adusă de comete în fiecare an", "pentru că oamenii o fabrică"], "Cantitatea totală de apă de pe Pământ rămâne aproape aceeași.")

    # ================================================================ S24 Oceanul Planetar
    O = Lectie(5, "V-S24-oceanul-planetar-componente-localizare", "Oceanul Planetar – componente și localizare. Dinamica apelor oceanice",
               "De ce apa mării se ridică și coboară de două ori pe zi?",
               [("Oceanele și mările", "Oceanul Planetar e apa sărată care înconjoară continentele. E împărțit în oceane: Pacific (cel mai mare și cel mai adânc), Atlantic, Indian, Arctic (cel mai mic) și, după mulți geografi, Oceanul de Sud, în jurul Antarcticii.\nMările sunt părți mai mici ale oceanelor, mai apropiate de uscat. Marea Neagră e o mare aproape închisă, legată de Marea Mediterană prin strâmtori."),
                ("Proprietățile apei oceanice", "Apa oceanului e sărată: în medie, aproximativ 35 g de sare la 1 litru. Temperatura apei scade de la Ecuator spre poli și de la suprafață spre adânc.\nCea mai adâncă groapă e Groapa Marianelor, în Oceanul Pacific: aproape 11 000 m."),
                ("Mișcările apei oceanice", "Valurile sunt produse de vânt.\nMareele sunt urcarea și coborârea apei mării de două ori pe zi, din cauza atracției Lunii (și a Soarelui).\nCurenții oceanici sunt „râuri” uriașe în ocean. Curenții calzi (ca Golfstromul) încălzesc țărmurile pe care ajung; curenții reci le răcesc.")],
               stiaica="Golfstromul aduce apă caldă din Golful Mexic până în Europa de Nord-Vest. Datorită lui, porturile din nordul Norvegiei nu îngheață iarna, deși sunt dincolo de Cercul Polar.",
               ref=REF.format("Oceanul Planetar – componente și localizare"))
    O.e(2, "2.1", "Pune pe hartă numele oceanelor.", [("pac", "Oceanul Pacific", 0, -150), ("atl", "Oceanul Atlantic", 10, -30), ("ind", "Oceanul Indian", -20, 75), ("arc", "Oceanul Arctic", 85, 0)], "Pacificul e între Asia, Australia și cele două Americi; Atlanticul între Europa–Africa și Americi; Indianul la sud de Asia; Arcticul în jurul Polului Nord.", harta="lume")
    O.p(1, "2.1", "Atinge pe hartă Oceanul Pacific.", "lume", 0, -150, "Oceanul Pacific", 3500, "Pacificul ocupă aproape o treime din suprafața Pământului.")
    O.p(2, "2.1", "Atinge pe hartă Oceanul Atlantic.", "lume", 15, -40, "Oceanul Atlantic", 2500, "Atlanticul e între Europa și Africa, la est, și cele două Americi, la vest.")
    O.p(2, "2.1", "Atinge pe hartă Oceanul Arctic.", "lume", 85, 0, "Oceanul Arctic", 1500, "Arcticul e în jurul Polului Nord.")
    O.p(2, "2.1", "Atinge pe hartă Marea Neagră.", "lume", 43.2, 34.5, "Marea Neagră", 450, "Marea Neagră e la est de România.")
    O.p(3, "2.1", "Atinge pe hartă Marea Mediterană.", "lume", 35, 18, "Marea Mediterană", 800, "Mediterana e între Europa, Africa și Asia.")
    O.a(1, "1.1", "Care e cel mai mare ocean?", "Oceanul Pacific", ["Oceanul Atlantic", "Oceanul Indian", "Oceanul Arctic"], "Pacificul e cel mai mare și cel mai adânc.")
    O.a(2, "1.1", "Care e cel mai mic ocean?", "Oceanul Arctic", ["Oceanul Indian", "Oceanul Atlantic", "Oceanul Pacific"], "Arcticul e cel mai mic și e acoperit în mare parte de gheață.")
    O.a(2, "4.2", "Unde se află cea mai adâncă groapă oceanică?", "în Oceanul Pacific: Groapa Marianelor, aproape 11 000 m", ["în Marea Neagră: 2 000 m", "în Oceanul Arctic: 500 m", "în Oceanul Atlantic: 30 000 m"], "Groapa Marianelor e aproape de 11 000 m adâncime.", surse=S_MARIANA)
    O.a(2, "1.1", "Ce sunt mările?", "părți mai mici ale oceanelor, apropiate de uscat", ["lacuri mari cu apă dulce", "râuri foarte late", "ghețari topiți"], "Mările țin de oceane.")
    O.a(2, "2.1", "Cu ce mare e legată Marea Neagră prin strâmtorile Bosfor și Dardanele?", "Marea Mediterană", ["Marea Baltică", "Marea Nordului", "Marea Caspică"], "Prin Bosfor, Marea Marmara și Dardanele, Marea Neagră comunică cu Mediterana.")
    O.a(2, "1.2", "Ce produce valurile?", "vântul", ["Luna", "cutremurele mici", "peștii"], "Vântul împinge suprafața apei.")
    O.a(2, "1.2", "Ce produce mareele?", "atracția Lunii și a Soarelui", ["vântul", "râurile", "ploaia"], "Luna atrage apa oceanului; de aceea nivelul urcă și coboară de două ori pe zi.")
    O.a(2, "1.1", "Ce sunt curenții oceanici?", "deplasări mari de apă în ocean, ca niște „râuri” în mare", ["valurile de la țărm", "gheața plutitoare", "furtunile"], "Curenții transportă apă caldă sau rece pe distanțe mari.")
    O.a(3, "3.2", "Ce efect are Golfstromul asupra Europei de Nord-Vest?", "iernile sunt mai blânde decât ar fi normal la acea latitudine", ["iernile sunt mai geroase", "nu are niciun efect", "aduce deșertul"], "Curentul cald încălzește aerul de deasupra.")
    O.s(2, "1.2", "Asociază mișcarea apei cu cauza ei.", [("valurile", "vântul"), ("mareele", "atracția Lunii"), ("curenții oceanici", "vânturile permanente și diferențele de temperatură"), ("tsunami", "un cutremur sub ocean")], "Fiecare mișcare are cauza ei.")
    O.a(3, "4.3", "Ce trebuie să faci dacă, pe o plajă, marea se retrage brusc mult după un cutremur?", "pleci imediat spre un loc înalt, departe de țărm", ["mergi să culegi scoici", "faci fotografii", "intri în apă"], "Retragerea bruscă a mării poate anunța un tsunami.")
    O.adev(2, "1.2", "Temperatura apei oceanice scade de la Ecuator spre poli.", True, "Adevărat: la Ecuator apa e caldă; la poli, aproape înghețată.")
    O.adev(2, "1.2", "Apa e mai caldă în adâncul oceanului decât la suprafață.", False, "Fals: în adânc apa e rece, pentru că lumina și căldura Soarelui nu ajung acolo.")
    O.l(2, "1.1", "Completează.", "Cel mai mare ocean este Oceanul [Pacific], iar cel mai mic este Oceanul [Arctic].", ["Indian", "Atlantic"], "Pacific – cel mai mare; Arctic – cel mai mic.")
    O.l(2, "3.1", "Completează.", "În medie, un litru de apă oceanică conține aproximativ [35] g de sare.", ["3", "350"], "Salinitatea medie e aproximativ 35 la mie.")
    O.o(2, "1.1", "Ordonează oceanele de la cel mai mare la cel mai mic.", ["Pacific", "Atlantic", "Indian", "Arctic"], "Mărime, descrescător", "Pacific, Atlantic, Indian, Arctic (fără Oceanul de Sud).")
    O.g(3, "2.3", "Graficul arată temperatura apei la suprafața oceanului în trei locuri imaginare. Care e, probabil, cel mai aproape de Ecuator?", grafic("bare", "Temperatura apei la suprafață (date imaginare)", [("Punctul A", 4), ("Punctul B", 28), ("Punctul C", 15)], "°C"), "Punctul B", ["Punctul A", "Punctul C", "toate sunt la Ecuator"], "Apa cea mai caldă, 28 °C, e cea mai apropiată de Ecuator.")
    O.a(2, "3.3", "La ce folosesc oamenii oceanele?", "pescuit, transport de mărfuri, sare, turism, petrol", ["la irigat câmpurile direct", "la băut fără tratare", "la nimic"], "Oceanele au resurse și sunt „drumuri” pentru vapoare.")
    O.a(3, "3.3", "Ce problemă mare amenință oceanele astăzi?", "poluarea cu plastic", ["prea mulți pești", "prea multă sare", "lipsa valurilor"], "Plasticul ajunge în ocean și e înghițit de animale.")
    O.a(2, "2.1", "Ce ocean scaldă țărmurile Africii la vest?", "Oceanul Atlantic", ["Oceanul Indian", "Oceanul Pacific", "Oceanul Arctic"], "La est, Africa e scăldată de Oceanul Indian.")
    O.a(2, "2.1", "Ce ocean scaldă țărmurile Africii la est?", "Oceanul Indian", ["Oceanul Atlantic", "Oceanul Pacific", "Oceanul Arctic"], "La vest, Africa e scăldată de Atlantic.")
    O.d(2, "2.1", "Ce mare e marcată pe hartă?", "lume", 43.2, 34.5, "Marea Neagră", ["Marea Mediterană", "Marea Caspică", "Marea Roșie"], "Marea dintre România, Ucraina, Rusia, Georgia, Turcia și Bulgaria e Marea Neagră.")
    O.a(3, "1.2", "De ce se spune că Marea Neagră e o „mare aproape închisă”?", "pentru că e înconjurată de uscat și comunică cu oceanul doar prin strâmtori înguste", ["pentru că e acoperită de gheață", "pentru că nu are pești", "pentru că e lac"], "Strâmtorile Bosfor și Dardanele o leagă de Mediterana.")
    O.a(2, "1.2", "Ce se întâmplă la reflux?", "apa se retrage de la țărm", ["vin valuri mari", "marea îngheață", "apa devine dulce"], "Fluxul – apa urcă; refluxul – apa coboară.")

    # ================================================================ S25 Apele continentale
    C = Lectie(5, "V-S25-apele-continentale", "Apele continentale",
               "De unde vine apa râului Râmnicu Sărat și unde se duce?",
               [("Râurile", "Râul este o apă curgătoare permanentă, care curge pe o vale, de la izvor până la vărsare. Râurile se varsă în alte râuri (ca afluenți), în lacuri, mări sau oceane.\nUn râu mare care se varsă în mare sau ocean se numește fluviu (de exemplu, Dunărea).\nLocul unde un râu se varsă poate fi o deltă (râul se ramifică în brațe) sau un estuar (o gură largă, în formă de pâlnie)."),
                ("Bazinul hidrografic", "Râul principal împreună cu toți afluenții lui formează un sistem hidrografic. Suprafața de pe care își adună apele se numește bazin hidrografic.\nRâul Râmnicu Sărat este un afluent al Siretului, iar Siretul se varsă în Dunăre. Așa, apa care curge prin orașul nostru ajunge, în cele din urmă, în Marea Neagră."),
                ("Lacurile și apele subterane", "Lacurile sunt ape stătătoare, adunate într-o depresiune (o adâncitură). După felul în care s-a format depresiunea, lacurile pot fi glaciare, vulcanice, carstice, de baraj natural, lagune sau limane; există și lacuri făcute de om, numite lacuri de acumulare.\nApele subterane se află în porii și crăpăturile rocilor; ies la suprafață prin izvoare.")],
               stiaica="Lacul Baikal, din Siberia, are 1 642 m adâncime și e cel mai adânc lac de pe Pământ. Conține aproape o cincime din apa dulce de la suprafața uscatului.",
               ref=REF.format("Apele continentale"))
    C.a(1, "1.1", "Ce este un râu?", "o apă curgătoare permanentă, care curge pe o vale", ["o apă stătătoare", "o parte a oceanului", "un ghețar"], "Râul curge mereu, de la izvor la vărsare.")
    C.a(1, "1.1", "Cum se numește locul de unde pornește un râu?", "izvor", ["vărsare", "deltă", "afluent"], "Izvorul e începutul râului.")
    C.a(2, "1.1", "Ce este un afluent?", "un râu care se varsă în alt râu", ["un râu care se varsă direct în ocean", "un lac mic", "locul unde râul se termină"], "Râmnicu Sărat e afluent al Siretului.")
    C.a(2, "1.1", "Ce este un fluviu?", "un râu mare care se varsă într-o mare sau într-un ocean", ["un pârâu de munte", "un lac sărat", "un canal"], "Dunărea e un fluviu.")
    C.s(2, "1.1", "Asociază termenul cu explicația.", [("izvorul", "locul unde începe râul"), ("vărsarea", "locul unde se termină râul"), ("albia", "locul pe unde curge apa"), ("bazinul hidrografic", "suprafața de pe care râul își adună apa")], "Părțile unui râu.")
    C.a(2, "1.1", "Ce este o deltă?", "locul unde un fluviu se ramifică în mai multe brațe înainte de vărsare", ["un lac de munte", "o groapă oceanică", "un vârf de munte"], "Delta Dunării are trei brațe: Chilia, Sulina, Sfântu Gheorghe.")
    C.a(2, "2.1", "În ce râu se varsă râul Râmnicu Sărat?", "în Siret", ["direct în Marea Neagră", "în Olt", "în Mureș"], "Râmnicu Sărat e afluent al Siretului, care se varsă în Dunăre.")
    C.o(3, "2.1", "Ordonează drumul unei picături de apă din orașul nostru până la mare.", ["râul Râmnicu Sărat", "Siretul", "Dunărea", "Marea Neagră"], "De la oraș la mare", "Râmnicu Sărat → Siret → Dunăre → Marea Neagră.")
    C.a(2, "4.2", "Care e cel mai lung fluviu de pe Pământ, după majoritatea măsurătorilor?", "Nilul", ["Dunărea", "Volga", "Rinul"], "Nilul are aproximativ 6 650 km; unii cercetători consideră Amazonul ceva mai lung.", surse=S_NIL)
    C.a(2, "4.2", "Ce fluviu are cea mai mare cantitate de apă de pe Pământ?", "Amazonul", ["Nilul", "Dunărea", "Mississippi"], "Amazonul duce mai multă apă decât oricare alt fluviu.")
    C.a(2, "4.2", "Ce lungime are Dunărea?", "aproximativ 2 860 km", ["aproximativ 286 km", "aproximativ 6 650 km", "aproximativ 28 600 km"], "Dunărea are 2 857 km, după ICPDR; e al doilea fluviu ca lungime din Europa, după Volga.", surse=S_DUNARE)
    C.p(2, "2.1", "Atinge pe hartă Delta Dunării.", "romania", 45.1, 29.3, "Delta Dunării", 50, "Delta Dunării e în estul României, la vărsarea Dunării în Marea Neagră.")
    C.p(3, "2.1", "Atinge pe hartă fluviul Nil, în Egipt.", "lume", 26, 32.5, "Nilul", 600, "Nilul curge prin estul Africii și se varsă în Marea Mediterană.")
    C.p(3, "2.1", "Atinge pe hartă Lacul Baikal.", "lume", 53.5, 108, "Lacul Baikal", 500, "Baikal e în sudul Siberiei, în Rusia.")
    C.a(2, "4.2", "Care e cel mai adânc lac de pe Pământ?", "Lacul Baikal (1 642 m)", ["Marea Caspică", "Lacul Bâlea", "Lacul Victoria"], "Baikal are 1 642 m adâncime.", surse=S_BAIKAL)
    C.a(2, "4.2", "Care e cel mai mare lac de pe Pământ, ca suprafață?", "Marea Caspică", ["Lacul Baikal", "Lacul Snagov", "Lacul Superior"], "Deși se numește „mare”, Caspica e un lac, cu apă ușor sărată.", surse=S_CASPIC)
    C.a(1, "1.1", "Ce este un lac?", "o apă stătătoare, adunată într-o adâncitură a terenului", ["o apă curgătoare", "o parte a oceanului", "un izvor"], "Lacurile nu curg, ca râurile.")
    C.s(3, "1.2", "Asociază tipul de lac cu felul în care s-a format.", [("lac glaciar", "într-o căldare săpată de un ghețar"), ("lac vulcanic", "în craterul unui vulcan stins"), ("lac de acumulare", "în spatele unui baraj construit de om"), ("liman", "la gura unui râu blocată de nisip")], "Lacurile se numesc după originea depresiunii.")
    C.a(2, "2.1", "Ce lac vulcanic din România se află în craterul unui vulcan stins?", "Lacul Sfânta Ana", ["Lacul Bucura", "Lacul Vidraru", "Lacul Razim"], "Sfânta Ana e singurul lac vulcanic din România, în Munții Ciomatu.")
    C.a(2, "2.1", "Ce fel de lac este Vidraru, de pe Argeș?", "lac de acumulare, făcut de om", ["lac glaciar", "lac vulcanic", "lagună"], "Barajul Vidraru reține apa pentru hidrocentrală.")
    C.adev(2, "1.2", "Toate râurile se varsă direct în mare.", False, "Fals: multe se varsă în alte râuri (afluenți) sau în lacuri.")
    C.adev(1, "1.2", "Râurile curg de la locuri înalte spre locuri joase.", True, "Adevărat: apa curge la vale.")
    C.l(2, "1.1", "Completează.", "Locul unde se termină un râu se numește [vărsare]; un râu care se varsă în alt râu se numește [afluent].", ["izvor", "fluviu"], "Vărsare – capătul; afluent – râu care intră în altul.")
    C.l(2, "2.1", "Completează.", "Dunărea se varsă în Marea [Neagră], formând [Delta] Dunării.", ["Roșie", "Lacul"], "Delta Dunării e la vărsarea în Marea Neagră.")
    C.g(3, "2.3", "Graficul arată debitul (cantitatea de apă) unui râu imaginar pe parcursul anului. În ce lună râul are cea mai multă apă?", grafic("profil", "Debitul unui râu imaginar", [("I", 8), ("II", 10), ("III", 22), ("IV", 35), ("V", 30), ("VI", 24), ("VII", 15), ("VIII", 9), ("IX", 7), ("X", 8), ("XI", 10), ("XII", 9)], "m³/s"), "aprilie", ["ianuarie", "septembrie", "decembrie"], "Primăvara se topesc zăpezile și plouă mult: râul crește (viituri de primăvară).")
    C.a(3, "3.2", "De ce râurile din România au cea mai multă apă primăvara?", "pentru că se topește zăpada și plouă mult", ["pentru că e cel mai frig", "pentru că oamenii nu folosesc apa", "pentru că vin mareele"], "Topirea zăpezilor + ploile de primăvară = ape mari.")
    C.a(2, "3.3", "La ce folosesc lacurile de acumulare?", "la producerea energiei electrice, alimentarea cu apă și irigații", ["la extragerea sării", "la oprirea vântului", "la formarea vulcanilor"], "Barajele au mai multe folosințe.")
    C.a(3, "1.2", "Care e diferența dintre o deltă și un estuar?", "în deltă râul se ramifică în brațe; estuarul e o gură largă, ca o pâlnie, spălată de maree", ["nu e nicio diferență", "delta e un lac, estuarul un munte", "estuarul are trei brațe"], "Dunărea are deltă; Tamisa are estuar.")
    C.d(2, "2.1", "Ce lac e marcat pe hartă?", "lume", 53.5, 108, "Lacul Baikal", ["Marea Caspică", "Lacul Victoria", "Lacul Ladoga"], "Lacul alungit din sudul Siberiei e Baikal.")
    C.a(2, "4.3", "Ce poți face ca să protejezi râul din orașul tău?", "nu arunci gunoaie pe mal și participi la acțiuni de ecologizare", ["arunci deșeurile în apă", "speli mașina în râu", "tai sălciile de pe mal"], "Malurile curate înseamnă apă mai curată.")

    # ================================================================ S26 Ghețarii
    G = Lectie(5, "V-S26-ghetarii", "Ghețarii",
               "Pot exista „râuri” de gheață care curg?",
               [("Ce sunt ghețarii", "Ghețarii sunt mase mari de gheață formate din zăpadă care s-a adunat și s-a tasat timp de mulți ani. Se formează unde zăpada care cade iarna nu se topește complet vara: în zonele polare și pe munții foarte înalți.\nGheața ghețarilor e apă dulce. Peste două treimi din apa dulce a Pământului e înghețată în ghețari și calote."),
                ("Tipuri de ghețari", "Calotele glaciare (inlandsisurile) acoperă suprafețe uriașe: Antarctica și Groenlanda.\nGhețarii montani ocupă văile munților înalți (Alpi, Himalaya, Anzi). Ei coboară încet, ca un râu foarte lent, de la câțiva centimetri la câțiva metri pe zi.\nCând un ghețar ajunge la mare, din el se rup bucăți uriașe care plutesc: aisbergurile."),
                ("Urmele ghețarilor", "Ghețarii sapă văi în formă de U și căldări (adâncituri) în care, după topire, apar lacuri glaciare.\nÎn România nu mai există ghețari astăzi, dar în trecut au existat în Carpații cei mai înalți. De la ei au rămas lacurile glaciare din Retezat, Făgăraș și Parâng, de exemplu Lacul Bucura, cel mai mare lac glaciar din țară.")],
               stiaica="Dintr-un aisberg se vede deasupra apei doar o parte mică, aproximativ o zecime. Restul e ascuns sub apă: de aici expresia „doar vârful aisbergului”.",
               ref=REF.format("Ghețarii"))
    G.a(1, "1.1", "Din ce se formează ghețarii?", "din zăpadă adunată și tasată mulți ani", ["din apă de mare înghețată într-o noapte", "din grindină", "din nori"], "Zăpada se transformă încet în gheață sub propria greutate.")
    G.a(2, "1.2", "Unde se formează ghețarii?", "unde zăpada nu se topește complet vara: la poli și pe munții foarte înalți", ["în deșerturi", "în câmpii", "la Ecuator, la nivelul mării"], "Frigul durabil permite adunarea zăpezii de la an la an.")
    G.a(2, "1.1", "Ce fel de apă e în ghețari?", "apă dulce", ["apă sărată", "apă minerală", "apă cu nisip"], "Gheața ghețarilor provine din zăpadă, deci e apă dulce.")
    G.a(2, "3.1", "Ce parte din apa dulce a Pământului e înghețată?", "peste două treimi", ["o sutime", "o zecime", "nimic"], "Ghețarii și calotele sunt cea mai mare rezervă de apă dulce.", surse=S_GHEATA)
    G.s(2, "1.1", "Asociază termenul cu explicația.", [("calotă glaciară", "gheață care acoperă un continent sau o insulă uriașă"), ("ghețar montan", "gheață care coboară pe o vale de munte"), ("aisberg", "bloc de gheață care plutește pe mare"), ("lac glaciar", "lac într-o căldare săpată de ghețar")], "Formele gheții și urmele ei.")
    G.a(2, "2.1", "Ce continent e acoperit de cea mai mare calotă glaciară?", "Antarctica", ["Europa", "Africa", "America de Sud"], "Calota Antarcticii e cea mai mare masă de gheață de pe Pământ.")
    G.a(2, "2.1", "Ce insulă e acoperită în cea mai mare parte de gheață?", "Groenlanda", ["Madagascar", "Marea Britanie", "Sicilia"], "Groenlanda are a doua mare calotă glaciară.")
    G.p(2, "2.1", "Atinge pe hartă Antarctica.", "lume", -80, 30, "Antarctica", 2000, "Antarctica e în jurul Polului Sud.")
    G.p(3, "2.1", "Atinge pe hartă Munții Alpi, unde există ghețari montani.", "lume", 46.5, 9.5, "Alpii", 450, "Alpii sunt în centrul Europei.")
    G.a(2, "1.2", "Ce sunt aisbergurile?", "blocuri mari de gheață rupte din ghețari, care plutesc pe mare", ["insule de nisip", "nori de gheață", "vulcani sub apă"], "Aisbergurile se rup unde ghețarii ajung la mare.")
    G.a(3, "3.1", "Ce parte dintr-un aisberg se vede deasupra apei?", "aproximativ o zecime", ["jumătate", "tot aisbergul", "trei sferturi"], "Gheața e puțin mai ușoară decât apa, așa că doar o mică parte iese afară.")
    G.a(2, "1.2", "Ce formă are o vale săpată de ghețar?", "formă de U", ["formă de V", "formă de stea", "formă de cerc"], "Râurile sapă văi în formă de V; ghețarii, în formă de U.")
    G.a(2, "2.1", "Ce lac glaciar din Munții Retezat e cel mai mare lac glaciar din România?", "Lacul Bucura", ["Lacul Sfânta Ana", "Lacul Vidraru", "Lacul Snagov"], "Bucura, în Retezat, e cel mai întins lac glaciar al țării.")
    G.a(2, "1.2", "Există astăzi ghețari în Carpații României?", "nu, dar au existat în trecut, iar urmele lor sunt căldările și lacurile glaciare", ["da, mulți", "da, pe toți munții", "nu au existat niciodată"], "Clima de azi e prea caldă pentru ghețari în Carpați.")
    G.p(3, "2.1", "Atinge pe harta României Munții Retezat, unde sunt multe lacuri glaciare.", "romania", 45.37, 22.85, "Munții Retezat", 45, "Retezatul e în vestul Carpaților Meridionali, în județul Hunedoara.")
    G.adev(2, "1.2", "Ghețarii stau pe loc și nu se mișcă.", False, "Fals: ghețarii coboară încet, sub propria greutate.")
    G.adev(2, "3.2", "Dacă ghețarii s-ar topi masiv, nivelul oceanului ar crește.", True, "Adevărat: apa din ghețarii de pe uscat ar ajunge în oceane.")
    G.l(2, "1.1", "Completează.", "Masa de gheață care acoperă Antarctica se numește [calotă] glaciară; blocurile de gheață care plutesc pe mare se numesc [aisberguri].", ["ghețar montan", "dune"], "Calotă și aisberg.")
    G.l(2, "1.2", "Completează.", "Văile săpate de râuri au formă de [V], iar cele săpate de ghețari au formă de [U].", ["O", "X"], "V pentru râu, U pentru ghețar.")
    G.o(2, "1.2", "Ordonează cum se formează un ghețar.", ["cade zăpadă multă iarna", "vara nu se topește toată", "straturile de zăpadă se adună an de an", "zăpada se tasează și devine gheață", "gheața începe să curgă încet la vale"], "Formarea ghețarului", "Zăpadă care nu se topește → tasare → gheață → mișcare.")
    G.a(3, "3.2", "De ce se micșorează astăzi mulți ghețari montani?", "pentru că temperaturile medii au crescut", ["pentru că ninge mai mult", "pentru că munții cresc", "pentru că oamenii îi sapă"], "Încălzirea climei topește ghețarii mai repede decât se refac.")
    G.a(3, "3.3", "De ce sunt importanți ghețarii montani pentru oameni?", "alimentează râurile cu apă vara, când se topesc parțial", ["produc petrol", "opresc cutremurele", "încălzesc aerul"], "Multe râuri mari din Asia pornesc din ghețarii Himalayei.")
    G.a(2, "3.2", "Ce se formează într-o căldare glaciară după ce gheața se topește?", "un lac glaciar", ["un vulcan", "o deltă", "o dună"], "Apa se adună în adâncitura săpată de gheață.")
    G.a(2, "1.1", "Ce sunt morenele?", "grămezi de pietre și nisip împinse și lăsate de ghețari", ["valuri de gheață", "lacuri vulcanice", "peșteri"], "Ghețarii cară roci și le depun la margini și la capăt.")
    G.a(3, "4.3", "Ce poate face o familie pentru a încetini topirea ghețarilor?", "economisește energia și folosește mai rar mașina", ["folosește mai multă energie", "taie copaci", "arde frunze"], "Mai puține emisii încetinesc încălzirea climei.")
    G.a(2, "2.1", "În ce munți se află Lacul Bâlea, un lac glaciar?", "Munții Făgăraș", ["Munții Retezat", "Munții Apuseni", "Munții Măcin"], "Bâlea e în Făgăraș, lângă Transfăgărășan.")
    G.g(3, "2.3", "Graficul arată lungimea unui ghețar imaginar măsurată la fiecare 20 de ani. Ce s-a întâmplat cu ghețarul?", grafic("profil", "Lungimea unui ghețar imaginar", [("1960", 12), ("1980", 11.5), ("2000", 10.4), ("2020", 8.9)], "km"), "s-a micșorat tot mai repede", ["a crescut", "a rămas la fel", "a dispărut complet"], "Linia coboară, iar pantele sunt tot mai mari: retragerea se accelerează.")
    G.a(2, "1.1", "Ce viteză are, de obicei, un ghețar montan?", "de la câțiva centimetri la câțiva metri pe zi", ["câțiva kilometri pe oră", "100 km pe zi", "nu se mișcă deloc"], "Ghețarii curg foarte încet.")
    G.d(2, "2.1", "Ce insulă acoperită de gheață e marcată pe hartă?", "lume", 72, -40, "Groenlanda", ["Islanda", "Marea Britanie", "Madagascar"], "Insula uriașă de la nord-est de America de Nord e Groenlanda.")
    G.a(3, "1.2", "Ce pericol reprezentau aisbergurile pentru vapoare?", "vapoarele se puteau lovi de partea ascunsă sub apă", ["aisbergurile atrăgeau fulgere", "făceau apa dulce", "opreau vântul"], "Ca Titanicul, în 1912.")

    # ================================================================ S27 Expediție: apele din orizontul local
    E = Expeditie(5, "V-S27-aplicatii-practice-apele-din", "Expediție: apele din orizontul meu",
                  "De unde vine apa de la robinet și cum o protejăm?",
                  ref=REF.format("Aplicații practice: Apele din orizontul local"))
    E.a(1, "4.1", "Ce râu traversează orașul Râmnicu Sărat?", "râul Râmnicu Sărat", ["Dunărea", "Oltul", "Mureșul"], "Orașul poartă numele râului.")
    E.p(2, "4.1", "Atinge pe harta României orașul Râmnicu Sărat, așezat pe râul cu același nume.", "romania", RS[0], RS[1], "Râmnicu Sărat", 40, "Râmnicu Sărat e în nord-estul județului Buzău.")
    E.pas("1. Râul orașului", "Află, cu ajutorul unei hărți sau al profesorului, de unde izvorăște râul Râmnicu Sărat și în ce râu se varsă.",
          jurnal="Desenează schema: izvorul, orașul, râul în care se varsă, apoi drumul până la mare.")
    E.a(2, "4.3", "Ce înseamnă o avertizare hidrologică de cod roșu pentru un râu?", "risc mare de inundații; trebuie urmate indicațiile autorităților", ["apa e foarte curată", "râul a secat", "e voie la scăldat"], "Avertizările hidrologice sunt emise de Institutul Național de Hidrologie și Gospodărire a Apelor.")
    E.s(2, "4.3", "Asociază situația cu ce faci.", [("inundație", "urci la etaj sau pe un loc înalt, departe de apă"), ("viitură", "nu traversezi râul și nu stai pe mal"), ("pod de gheață", "nu mergi pe gheața râului"), ("apă tulbure la robinet", "anunți furnizorul și nu bei din ea")], "Comportamentul corect te ține în siguranță.")
    E.a(3, "4.3", "Ce NU faci în timpul unei inundații?", "nu traversezi cu mașina sau pe jos un drum acoperit de apă", ["urci pe un loc înalt", "urmărești mesajele RO-ALERT", "oprești curentul electric dacă poți"], "Apa care curge poate lua pe sus o mașină, chiar dacă pare mică.")
    E.pas("2. Fenomene periculoase", "Află dacă în zona ta au fost inundații sau poduri de gheață. Discută cu familia ce ați face într-o astfel de situație.",
          jurnal="Scrie trei reguli de siguranță pentru o inundație.")
    E.a(2, "4.3", "Câtă apă pierzi într-o zi dacă un robinet picură?", "câțiva litri sau chiar zeci de litri", ["deloc", "o picătură", "o mie de litri pe minut"], "Picăturile adunate devin mulți litri.")
    E.pas("3. Detectivul apei", "Pune un pahar sub un robinet care picură (sau imaginează-ți) și măsoară câtă apă se adună într-o oră. Calculează cât ar fi într-o zi.",
          jurnal="Notează câți mililitri s-au adunat într-o oră și înmulțește cu 24. Ce propui ca să economisiți apa acasă?")
    E.pas("4. Afișul apei", "Realizează un afiș: „Cum protejăm apele din orizontul local”. Poți folosi desene sau fotografii făcute de tine pe malul râului (doar cu un adult).",
          jurnal="Fotografiază afișul.", foto=True)

    return Unitate(5, "u5-hidrosfera.json", "Hidrosfera – învelișul de apă al Pământului").add(H, O, C, G, E)
