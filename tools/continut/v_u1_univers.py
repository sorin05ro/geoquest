from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"
NASA = "NASA – Earth Fact Sheet (nssdc.gsfc.nasa.gov)"
S_RAZA = [NASA, "Wikipedia – Earth radius"]
S_LUMINA = ["BBC Sky at Night Magazine – How long does it take for light from the Sun to reach Earth?", "Universe Today – How Long Does It Take Sunlight to Reach the Earth?"]
S_DIST = [NASA + ": semiaxa mare 149,598 milioane km", "Universe Today – How Long Does It Take Sunlight to Reach the Earth?"]


def unitate():
    # ================================================================ S2
    L = Lectie(5, "V-S02-universul-sistemul-solar-aspecte", "Universul și Sistemul Solar",
               "Noaptea, pe cer vezi mii de puncte luminoase. Sunt toate stele? Ce e Pământul printre ele?",
               [("Universul", "Universul cuprinde tot ce există: galaxii, stele, planete, praf și gaze. Galaxiile sunt grupări uriașe de stele. Galaxia noastră se numește Calea Lactee.\nO stea, ca Soarele, produce lumină și căldură. Planetele și sateliții nu au lumină proprie: reflectă lumina Soarelui."),
                ("Sistemul Solar", "Sistemul Solar e format din Soare și din corpurile care se rotesc în jurul lui: 8 planete, sateliții lor, planete pitice, asteroizi și comete.\nPlanetele, de la Soare spre exterior: Mercur, Venus, Pământ, Marte (planete telurice, mici și stâncoase), Jupiter, Saturn, Uranus, Neptun (planete gigantice, mari, formate mai ales din gaze).\nÎntre Marte și Jupiter se află centura de asteroizi. Pluto este, din 2006, planetă pitică.")],
               stiaica="Lumina Soarelui ajunge la noi în aproximativ 8 minute și 20 de secunde. Când privești Soarele, îl vezi așa cum era acum 8 minute.",
               ref=REF.format("Universul și Sistemul Solar"))
    L.a(1, "1.1", "Cum se numește galaxia noastră?", "Calea Lactee", ["Andromeda", "Sistemul Solar", "Carul Mare"], "Galaxia în care se află Sistemul Solar se numește Calea Lactee.")
    L.a(1, "1.1", "Ce este Soarele?", "o stea", ["o planetă", "un satelit", "o cometă"], "Soarele e o stea: produce lumină și căldură.")
    L.o(1, "4.2", "Ordonează planetele de la cea mai apropiată de Soare la cea mai îndepărtată.", ["Mercur", "Venus", "Pământ", "Marte", "Jupiter", "Saturn", "Uranus", "Neptun"], "De la Soare spre exterior", "Ordinea: Mercur, Venus, Pământ, Marte, Jupiter, Saturn, Uranus, Neptun.", ind="Pământul e a treia planetă.")
    L.a(1, "1.1", "Câte planete are Sistemul Solar?", "8", ["9", "7", "10"], "Sunt 8 planete. Pluto a fost reclasificat ca planetă pitică în 2006.")
    L.a(2, "4.2", "Care este cea mai mare planetă din Sistemul Solar?", "Jupiter", ["Saturn", "Pământul", "Neptun"], "Jupiter e cea mai mare planetă; în el ar încăpea peste o mie de Pământuri.")
    L.a(2, "4.2", "Care planetă este cea mai apropiată de Soare?", "Mercur", ["Venus", "Marte", "Pământul"], "Mercur e prima planetă de la Soare.")
    L.a(1, "1.1", "Ce este Luna?", "satelitul natural al Pământului", ["o stea", "o planetă pitică", "o cometă"], "Luna se rotește în jurul Pământului: e satelitul lui natural.")
    L.s(1, "1.1", "Asociază corpul ceresc cu ce este.", [("Soarele", "stea"), ("Pământul", "planetă"), ("Luna", "satelit natural"), ("Calea Lactee", "galaxie")], "Soarele e stea, Pământul planetă, Luna satelit, Calea Lactee galaxie.")
    L.l(1, "1.1", "Completează.", "Pământul este a [treia] planetă de la Soare.", ["doua", "patra"], "Ordinea: Mercur, Venus, Pământ. Pământul e a treia.")
    L.a(2, "1.2 3.3", "Care grup cuprinde doar planete telurice (mici și stâncoase)?", "Mercur, Venus, Pământ, Marte", ["Jupiter, Saturn, Uranus, Neptun", "Mercur, Jupiter, Marte, Neptun", "Venus, Saturn, Pământ, Uranus"], "Primele patru planete de la Soare sunt telurice; ultimele patru sunt gigantice, gazoase.")
    L.a(2, "1.1", "Ce este o cometă?", "un corp din gheață și praf care capătă o coadă luminoasă când se apropie de Soare", ["o stea căzătoare", "o planetă mică", "un satelit al lui Jupiter"], "Cometele sunt din gheață și praf; lângă Soare, gheața se evaporă și apare coada.")
    L.a(2, "1.1", "Ce numim meteorit?", "o bucată de rocă din spațiu care ajunge la suprafața Pământului", ["o stea nouă", "un nor de gaze", "un satelit artificial"], "Meteoritul e un fragment din spațiu care cade pe Pământ.")
    L.a(2, "2.1", "Între ce planete se află centura principală de asteroizi?", "Marte și Jupiter", ["Pământ și Marte", "Jupiter și Saturn", "Venus și Pământ"], "Centura de asteroizi e între Marte și Jupiter.")
    L.a(2, "3.1", "Cât timp îi ia, în medie, luminii Soarelui să ajungă pe Pământ?", "aproximativ 8 minute și 20 de secunde", ["o secundă", "o zi", "un an"], "Lumina parcurge distanța Soare–Pământ în aproximativ 8 minute și 20 de secunde.", surse=S_LUMINA)
    L.a(3, "3.1", "Care este, aproximativ, distanța medie dintre Pământ și Soare?", "150 de milioane de km", ["150 de mii de km", "15 milioane de km", "1,5 miliarde de km"], "Distanța medie e de aproximativ 150 de milioane de kilometri (149,6 milioane).", surse=S_DIST)
    L.a(2, "3.2 3.3", "De ce există viață pe Pământ?", "are apă lichidă, aer cu oxigen și e la o distanță potrivită de Soare", ["e cea mai mare planetă", "e cea mai apropiată de Soare", "nu are atmosferă"], "Apa lichidă, atmosfera și temperatura potrivită (datorată distanței față de Soare) permit viața.")
    L.l(2, "1.1", "Completează.", "Sistemul Solar este format din [Soare] și din corpurile care se rotesc în jurul lui: [planete], sateliți, asteroizi și comete.", ["Luna", "galaxii"], "În centrul Sistemului Solar e Soarele; în jurul lui se rotesc planetele și celelalte corpuri.")
    L.a(1, "3.1", "Cu ce instrument observăm corpurile cerești îndepărtate?", "telescopul", ["microscopul", "busola", "termometrul"], "Telescopul mărește imaginea corpurilor cerești îndepărtate.")
    L.a(2, "1.1", "Ce sunt constelațiile?", "grupuri de stele care, văzute de pe Pământ, par să formeze figuri", ["planete apropiate între ele", "nori de gaze", "sateliți artificiali"], "Constelațiile sunt grupuri de stele, ca Ursa Mare (Carul Mare).")
    L.a(1, "1.2", "De ce strălucește Luna noaptea?", "reflectă lumina Soarelui", ["produce lumină proprie", "arde", "e o stea"], "Luna nu are lumină proprie: reflectă lumina Soarelui.")
    L.o(2, "4.2", "Ordonează corpurile cerești de la cel mai mic la cel mai mare.", ["Luna", "Pământul", "Jupiter", "Soarele"], "De la mic la mare", "Luna e mai mică decât Pământul, Pământul decât Jupiter, iar Soarele e cel mai mare.")
    L.adev(1, "1.2", "Soarele se rotește în jurul Pământului.", False, "Fals: Pământul se rotește în jurul Soarelui.")
    L.adev(2, "1.2", "Planetele nu au lumină proprie; ele reflectă lumina Soarelui.", True, "Adevărat: doar stelele produc lumină.")
    L.a(1, "1.1", "Care planetă este numită „planeta roșie”?", "Marte", ["Venus", "Jupiter", "Mercur"], "Marte are culoarea roșiatică datorită rocilor bogate în fier.")
    L.a(2, "1.1", "Care planetă are cele mai spectaculoase inele?", "Saturn", ["Marte", "Venus", "Mercur"], "Inelele lui Saturn, din gheață și roci, se văd chiar și cu un telescop mic.")
    L.a(2, "1.2", "Cum se numește mișcarea unei planete în jurul Soarelui?", "mișcarea de revoluție", ["mișcarea de rotație", "eclipsa", "maree"], "Revoluția e mișcarea în jurul Soarelui; rotația e mișcarea în jurul axei proprii.")
    L.s(3, "1.1 3.3", "Asociază planeta cu caracteristica ei.", [("Mercur", "cea mai apropiată de Soare"), ("Jupiter", "cea mai mare planetă"), ("Saturn", "inele foarte vizibile"), ("Neptun", "cea mai îndepărtată de Soare")], "Mercur e primul, Neptun ultimul; Jupiter e cel mai mare; Saturn are inelele cele mai vizibile.")
    L.a(3, "1.2", "De ce a devenit Pluto „planetă pitică” în 2006?", "e mic și orbita lui are multe alte corpuri, pe care nu le-a „curățat”", ["a fost distrus", "s-a apropiat de Soare", "a devenit satelit al lui Neptun"], "Uniunea Astronomică Internațională a stabilit că o planetă trebuie să-și fi „curățat” orbita; Pluto nu a făcut asta.")
    L.a(1, "1.1", "Cum se numește știința care studiază corpurile cerești?", "astronomia", ["geologia", "biologia", "meteorologia"], "Astronomia studiază stelele, planetele și galaxiile.")
    L.l(3, "1.1 1.2", "Completează.", "Planetele [telurice] sunt mici și stâncoase, iar planetele [gigantice] sunt mari și formate mai ales din gaze.", ["pitice", "înghețate"], "Telurice: Mercur, Venus, Pământ, Marte. Gigantice: Jupiter, Saturn, Uranus, Neptun.")

    # ================================================================ S3
    T = Lectie(5, "V-S03-terra-planeta-sistemului-solar", "Terra – o planetă a Sistemului Solar (formă și dimensiuni)",
               "Dacă Pământul ar fi plat, ce ar trebui să vezi când o corabie pleacă spre orizont?",
               [("Forma Pământului", "Pământul are formă aproape sferică, ușor turtită la poli. Forma lui reală se numește geoid.\nDovezi: fotografiile din spațiu; umbra rotundă a Pământului pe Lună, în timpul eclipsei de Lună; corabia care dispare treptat la orizont (întâi carena, apoi catargul); călătoriile în jurul lumii."),
                ("Dimensiuni și consecințe", "Raza Pământului e de aproximativ 6 378 km la Ecuator și 6 357 km la poli; în medie, 6 371 km. Lungimea Ecuatorului e de aproximativ 40 000 km.\nPentru că Pământul e rotund, razele Soarelui cad diferit: aproape vertical la Ecuator (cald) și foarte înclinat la poli (rece). De aici apar zonele de climă.")],
               stiaica="Diferența dintre raza de la Ecuator și cea de la poli e de doar circa 21 km. Pe un glob de clasă, turtirea nici nu s-ar vedea.",
               ref=REF.format("Terra – o planetă a Sistemului Solar"))
    T.a(1, "1.1", "Ce formă are Pământul?", "aproape sferică, ușor turtită la poli", ["plată", "de cub", "de con"], "Pământul e aproape sferic, ușor turtit la poli.")
    T.a(2, "1.1", "Cum se numește forma reală a Pământului?", "geoid", ["cerc", "elipsă", "piramidă"], "Forma proprie a Pământului se numește geoid.")
    T.a(2, "1.2 4.1", "Care este o dovadă că Pământul e rotund?", "umbra rotundă a Pământului pe Lună, în timpul eclipsei", ["Soarele răsare dimineața", "plouă primăvara", "munții sunt înalți"], "În eclipsa de Lună, umbra Pământului pe Lună e mereu rotundă.")
    T.o(2, "1.2 2.3", "O corabie se îndepărtează spre orizont. În ce ordine dispare din vedere?", ["carena (partea de jos)", "puntea", "vârful catargului"], "Ce dispare primul", "Pentru că suprafața mării e curbă, întâi dispare partea de jos, la final vârful catargului.")
    T.a(2, "3.1", "Care este, aproximativ, raza medie a Pământului?", "6 371 km", ["637 km", "63 710 km", "1 000 km"], "Raza medie e de aproximativ 6 371 km.", surse=S_RAZA)
    T.a(2, "3.1", "Unde e mai mare raza Pământului?", "la Ecuator", ["la poli", "e la fel peste tot", "la Tropice"], "La Ecuator raza e de aproximativ 6 378 km, la poli de 6 357 km: Pământul e turtit la poli.", surse=S_RAZA)
    T.a(2, "3.1", "Cât măsoară, aproximativ, Ecuatorul?", "40 000 km", ["4 000 km", "400 000 km", "12 000 km"], "Ecuatorul are aproximativ 40 000 km (calculat din raza ecuatorială: 2 × 3,14 × 6 378 km ≈ 40 075 km).", surse=[NASA + " (raza ecuatorială; lungimea rezultă prin calcul)"])
    T.a(1, "1.1", "Ce este Ecuatorul?", "cercul imaginar care împarte Pământul în emisfera nordică și emisfera sudică", ["o linie de la un pol la altul", "un fluviu", "un munte"], "Ecuatorul e la egală distanță de cei doi poli.")
    T.l(1, "1.1", "Completează.", "Ecuatorul împarte Pământul în emisfera [nordică] și emisfera [sudică].", ["estică", "vestică"], "Ecuatorul separă nordul de sud.")
    T.a(1, "1.1", "Ce este axa terestră?", "linia imaginară care trece prin centrul Pământului, de la Polul Nord la Polul Sud", ["Ecuatorul", "un meridian", "orbita Pământului"], "Pământul se rotește în jurul axei terestre, care unește cei doi poli.")
    T.a(2, "3.2", "De ce e mai cald la Ecuator decât la poli?", "razele Soarelui cad aproape vertical la Ecuator și foarte înclinat la poli", ["la Ecuator sunt mai mulți munți", "Ecuatorul e mai aproape de Lună", "la poli e mai mult vânt"], "Razele verticale încălzesc mai mult; cele înclinate se împrăștie pe o suprafață mare și încălzesc puțin.")
    T.a(1, "1.1", "Cum se numește modelul micșorat al Pământului?", "globul geografic", ["harta", "busola", "telescopul"], "Globul geografic e o reprezentare micșorată a Pământului, cu formă sferică.")
    T.p(1, "2.1", "Atinge pe hartă un punct de pe Ecuator, în Africa.", "lume", 0, 20, "Ecuatorul, în Africa", 900, "Ecuatorul traversează Africa prin centru (Gabon, Congo, Kenya).", ind="Ecuatorul e linia orizontală din mijlocul hărții.")
    T.p(2, "2.1", "Atinge pe hartă Polul Nord.", "lume", 89.5, 0, "Polul Nord", 1200, "Polul Nord e marginea de sus a hărții, în Oceanul Arctic.")
    T.adev(1, "1.2", "Pământul este perfect sferic.", False, "Fals: e ușor turtit la poli (geoid).")
    T.adev(2, "1.2", "Călătoriile în jurul lumii, pornind spre vest și revenind din est, arată că Pământul e rotund.", True, "Adevărat: mergând mereu în aceeași direcție, revii la punctul de plecare.")
    T.s(2, "1.1", "Asociază termenul cu explicația.", [("Ecuatorul", "împarte Pământul în nord și sud"), ("axa terestră", "unește cei doi poli"), ("polii", "capetele axei terestre"), ("emisfera", "jumătate de Pământ")], "Ecuatorul împarte Pământul în emisfere; axa unește polii.")
    T.a(2, "1.2", "Ce vede un astronaut din spațiu?", "Pământul ca o sferă albastră, cu nori albi", ["Pământul plat, ca o masă", "doar Luna", "Pământul ca un cub"], "Fotografiile din spațiu arată clar forma sferică.")
    T.a(3, "3.1", "Cu câți kilometri e mai mare raza de la Ecuator decât cea de la poli?", "cu aproximativ 21 km", ["cu aproximativ 2 100 km", "cu aproximativ 210 km", "sunt egale"], "6 378 km − 6 357 km ≈ 21 km. Diferența e foarte mică față de mărimea Pământului.", surse=S_RAZA)
    T.l(2, "1.1", "Completează.", "Pământul este turtit la [poli] și ușor bombat la [Ecuator].", ["Tropice", "munți"], "Turtirea e la poli, bombarea la Ecuator.")
    T.a(2, "3.3", "Unde găsim cele mai reci regiuni ale Pământului?", "în jurul polilor", ["la Ecuator", "la Tropice", "în mijlocul oceanelor"], "La poli razele Soarelui cad foarte înclinat și încălzesc puțin.")
    T.o(3, "3.2", "Ordonează locurile de la cel mai cald la cel mai rece, după unghiul razelor Soarelui.", ["Ecuatorul", "România", "Polul Nord"], "De la cald la rece", "La Ecuator razele cad aproape vertical; în România, înclinat; la pol, foarte înclinat.")
    T.a(1, "1.1", "Cum se numesc cele două capete ale axei terestre?", "Polul Nord și Polul Sud", ["Estul și Vestul", "Tropicele", "Ecuatorul și Greenwich"], "Axa terestră iese la suprafață în cei doi poli.")
    T.a(2, "4.1", "Ce experiment simplu arată de ce dispare corabia treptat?", "o furnică plimbată pe o minge pare că „coboară” după curbura ei", ["aprinzi o lanternă într-o cameră întunecată", "pui apă la înghețat", "arunci o piatră în apă"], "Pe o suprafață curbă, obiectele care se îndepărtează dispar de jos în sus.")
    T.a(2, "1.1", "Care dintre acestea NU este o dovadă a formei Pământului?", "existența anotimpurilor în România", ["fotografiile din spațiu", "umbra rotundă pe Lună", "dispariția treptată a corăbiilor"], "Anotimpurile se datorează înclinării axei și revoluției, nu formei.")
    T.a(1, "1.1", "Pe ce planetă trăim?", "Terra (Pământul)", ["Marte", "Venus", "Luna"], "Terra este numele latin al Pământului.")
    T.l(3, "3.1", "Completează cu valorile aproximative.", "Raza Pământului la Ecuator este de aproximativ [6 378] km, iar la poli de aproximativ [6 357] km.", ["3 780", "63 570"], "La Ecuator: 6 378 km; la poli: 6 357 km.", surse=S_RAZA)
    T.adev(2, "3.2", "La Polul Nord, Soarele nu urcă niciodată sus pe cer, de aceea e frig.", True, "Adevărat: la poli razele cad foarte înclinat tot anul.")
    T.a(3, "3.2 3.3", "Ce consecință are forma sferică a Pământului?", "regiunile se încălzesc diferit, de la Ecuator spre poli", ["toate regiunile au aceeași temperatură", "există cutremure", "există maree"], "Forma sferică face ca unghiul razelor să scadă de la Ecuator spre poli, deci și căldura.")
    T.a(1, "2.1", "Ce emisferă locuim noi, în România?", "emisfera nordică", ["emisfera sudică", "pe Ecuator", "la Polul Sud"], "România e la nord de Ecuator, în emisfera nordică.")
    T.s(3, "1.2 4.1", "Asociază dovada cu ce observăm.", [("eclipsa de Lună", "umbră rotundă pe Lună"), ("corabia la orizont", "dispare de jos în sus"), ("fotografia din spațiu", "o sferă albastră"), ("călătoria în jurul lumii", "revii de unde ai plecat")], "Toate arată că Pământul e rotund.")

    # ================================================================ S4 Expediție
    E = Expeditie(5, "V-S04-aplicatie-practica-calatorie-virtuala", "Expediție: călătorie virtuală în Univers",
                  "Dacă ai putea zbura de la Soare până la Neptun, pe lângă ce ai trece?", ref=REF.format("Aplicație practică: Călătorie virtuală în Univers"))
    E.o(1, "4.2", "Planifică traseul navei: ordonează opririle de la Soare spre exterior.", ["Mercur", "Venus", "Pământ", "Marte", "centura de asteroizi", "Jupiter"], "De la Soare spre exterior", "După Marte urmează centura de asteroizi, apoi Jupiter.")
    E.a(2, "4.3", "Nava trebuie să ocolească o zonă cu multe corpuri mici de rocă. Între ce planete se află?", "Marte și Jupiter", ["Venus și Pământ", "Saturn și Uranus", "Mercur și Venus"], "Centura de asteroizi e între Marte și Jupiter.")
    E.pas("1. Traseul navei", "Pregătește drumul prin Sistemul Solar.")
    E.a(2, "4.1", "Ce planetă vezi cu ochiul liber, dimineața sau seara, ca pe un punct foarte strălucitor?", "Venus", ["Neptun", "Uranus", "Pluto"], "Venus e cel mai strălucitor punct de pe cer după Lună; e numită și Luceafărul.")
    E.pas("2. Observă cerul", "Într-o seară senină, ieși cu un adult și privește cerul timp de 10 minute. Caută Luna și cele mai strălucitoare puncte.",
          jurnal="Notează data, ora, cum arăta Luna (ce formă avea) și câte stele strălucitoare ai văzut.")
    E.pas("3. Machetă sau desen", "Desenează sau construiește o machetă a Sistemului Solar, cu planetele în ordine. Folosește mărimi diferite: Jupiter cel mai mare, Mercur cel mai mic.",
          jurnal="Fotografiază lucrarea și scrie ce materiale ai folosit.", foto=True)
    E.pas("4. Prezintă o planetă", "Alege o planetă și află 3 lucruri despre ea din manual sau dintr-o sursă sigură (de exemplu, site-ul NASA).",
          jurnal="Scrie numele planetei, 3 informații și sursa.")

    return Unitate(5, "u1-univers.json", "Terra – o planetă a Universului").add(L, T, E)
