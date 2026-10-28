from autor import Lectie, Unitate, grafic

REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"


def unitate():
    Z = Lectie(5, "V-S31-diversitatea-peisajelor-terestre-naturale", "Diversitatea peisajelor terestre naturale",
               "Dacă ai face înconjurul lumii, prin ce peisaje ai trece?",
               [("Ce este un peisaj natural", "Un peisaj natural este o porțiune de pe suprafața Pământului unde relieful, clima, apele, plantele, animalele și solurile se potrivesc între ele și formează un întreg.\nPeisajele naturale se repetă după zonele de climă și se numesc zone naturale."),
                ("Zonele naturale ale zonei calde", "Pădurea ecuatorială: cald și ploios tot anul, vegetație deasă, cu multe etaje.\nSavana: un anotimp ploios și unul secetos; ierburi înalte, copaci rari (baobab, acacia), mari ierbivore.\nDeșertul tropical: foarte puține ploi, zile fierbinți și nopți reci; dune de nisip, oaze."),
                ("Zonele naturale temperate și reci", "Zona mediteraneeană: veri calde și uscate, ierni blânde și ploioase; măslin, viță-de-vie.\nPădurile de foioase și stepa, în zona temperată. Taigaua: păduri întinse de conifere, ierni lungi.\nTundra: ierni foarte lungi, mușchi și licheni. Deșerturile reci: gheață tot anul (Antarctica, Groenlanda).")],
               stiaica="Unele deșerturi nu sunt fierbinți: Antarctica e considerată cel mai mare deșert de pe Pământ, pentru că primește foarte puține precipitații.",
               ref=REF.format("Diversitatea peisajelor terestre naturale"))
    Z.a(1, "1.2", "Ce este un peisaj natural?", "o porțiune de teren unde relieful, clima, apele, plantele, animalele și solul formează un întreg", ["o fotografie frumoasă", "un oraș mare", "un parc cu bănci"], "Toate componentele se influențează între ele.")
    Z.s(2, "1.2", "Asociază zona naturală cu clima ei.", [("pădurea ecuatorială", "cald și ploios tot anul"), ("savana", "un anotimp ploios și unul secetos"), ("deșertul tropical", "foarte cald și foarte uscat"), ("tundra", "ierni foarte lungi și reci")], "Clima decide zona naturală.")
    Z.s(2, "1.2", "Asociază zona naturală cu planta tipică.", [("pădurea ecuatorială", "liane și copaci uriași"), ("savana", "baobabul"), ("zona mediteraneeană", "măslinul"), ("taigaua", "molidul")], "Plantele spun ce zonă naturală e.")
    Z.s(2, "1.2", "Asociază zona naturală cu animalul tipic.", [("savana", "girafa"), ("deșertul", "cămila"), ("taigaua", "râsul"), ("tundra", "renul")], "Animalele sunt adaptate zonei lor.")
    Z.o(3, "2.2", "Ordonează zonele naturale de la Ecuator spre Polul Nord, prin Africa și Europa.", ["pădurea ecuatorială", "savana", "deșertul tropical", "zona mediteraneeană", "pădurea de foioase", "taigaua", "tundra"], "De la Ecuator spre nord", "Zonele naturale se succed după latitudine.")
    Z.a(2, "1.2", "Ce zonă naturală are veri calde și uscate și ierni blânde și ploioase?", "zona mediteraneeană", ["tundra", "taigaua", "pădurea ecuatorială"], "E clima țărmurilor Mării Mediterane: Italia, Grecia, Spania.")
    Z.a(2, "1.2", "În ce zonă naturală plouă aproape în fiecare zi?", "pădurea ecuatorială", ["deșertul", "savana, în anotimpul secetos", "tundra"], "Lângă Ecuator, ploile de după-amiază sunt aproape zilnice.")
    Z.a(2, "1.1", "Ce este o oază?", "un loc din deșert cu apă și vegetație", ["o dună de nisip", "un vulcan", "un ghețar"], "Oazele apar unde apa subterană ajunge la suprafață.")
    Z.a(2, "1.2", "Ce zonă naturală acoperă cea mai mare parte a României?", "zona pădurilor de foioase și a stepei (zona temperată)", ["tundra", "savana", "pădurea ecuatorială"], "România e în zona temperată.")
    Z.p(2, "2.2", "Atinge pe hartă o zonă de pădure ecuatorială: Bazinul Congo.", "lume", -1, 22, "Bazinul Congo", 1200, "Bazinul Congo e pe Ecuator, în Africa.")
    Z.p(2, "2.2", "Atinge pe hartă o zonă de deșert: Sahara.", "lume", 23, 12, "Sahara", 1500, "Sahara e cel mai mare deșert fierbinte.")
    Z.p(3, "2.2", "Atinge pe hartă o zonă de tundră: nordul Canadei.", "lume", 68, -100, "Nordul Canadei", 1500, "Tundra se întinde pe țărmurile Oceanului Arctic.")
    Z.p(3, "2.2", "Atinge pe hartă o zonă mediteraneeană: Grecia.", "lume", 39, 22, "Grecia", 500, "Grecia e pe țărmul Mediteranei.")
    Z.e(3, "2.2", "Pune pe hartă etichetele zonelor naturale.", [("ec", "pădure ecuatorială", -3, -60), ("sv", "savană", -5, 30), ("ds", "deșert", 23, 12), ("tg", "taiga", 60, 100)], "Amazonia – pădure ecuatorială; estul Africii – savană; Sahara – deșert; Siberia – taiga.", harta="lume")
    Z.adev(2, "1.2", "Toate deșerturile sunt fierbinți.", False, "Fals: Antarctica e un deșert rece, cu foarte puține precipitații.")
    Z.adev(2, "1.2", "Zonele naturale se repetă în emisfera nordică și în emisfera sudică.", True, "Adevărat: de o parte și de alta a Ecuatorului apar zone asemănătoare.")
    Z.adev(2, "2.2", "Pe munții înalți, zonele naturale se înlocuiesc cu altitudinea, ca niște etaje.", True, "Adevărat: de la păduri jos la pajiști alpine și stânci sus.")
    Z.l(2, "1.2", "Completează.", "Zona cu ierburi înalte și copaci rari se numește [savană], iar zona cu păduri de conifere se numește [taiga].", ["tundră", "oază"], "Savană și taiga.")
    Z.l(2, "1.2", "Completează.", "Locul cu apă și palmieri din mijlocul deșertului se numește [oază]; dealurile de nisip formate de vânt se numesc [dune].", ["deltă", "morene"], "Oaza și dunele sunt tipice deșertului.")
    Z.a(3, "3.3", "Ce activitate economică e tipică zonei mediteraneene?", "cultivarea măslinului și a viței-de-vie și turismul pe litoral", ["creșterea renilor", "exploatarea pădurilor de conifere", "pescuitul la copcă"], "Clima caldă și însorită atrage turiști.")
    Z.a(3, "3.3", "Cu ce se ocupă tradițional oamenii din tundră?", "cu creșterea renilor, vânatul și pescuitul", ["cu cultivarea bananelor", "cu cultivarea măslinului", "cu culesul cacaoei"], "Frigul nu permite agricultura obișnuită.")
    Z.a(2, "3.3", "Ce problemă amenință pădurea ecuatorială?", "tăierea copacilor pentru lemn și terenuri agricole", ["prea multă zăpadă", "înghețul", "lipsa ploii"], "Defrișările reduc biodiversitatea.")
    Z.g(3, "2.3", "Graficul arată precipitațiile anuale în trei zone naturale imaginare. Care e deșertul?", grafic("bare", "Precipitații anuale (date imaginare)", [("zona A", 2500), ("zona B", 60), ("zona C", 700)], "l/m²"), "zona B", ["zona A", "zona C", "niciuna"], "Doar 60 l/m² pe an: e un deșert.")
    Z.g(3, "2.3", "În același grafic imaginar, care zonă e, probabil, pădurea ecuatorială?", grafic("bare", "Precipitații anuale (date imaginare)", [("zona A", 2500), ("zona B", 60), ("zona C", 700)], "l/m²"), "zona A", ["zona B", "zona C", "niciuna"], "2 500 l/m² pe an: ploi abundente, ca lângă Ecuator.")
    Z.a(2, "2.2", "În ce zonă naturală e Siberia, în cea mai mare parte?", "taiga", ["savana", "deșertul tropical", "zona mediteraneeană"], "Siberia are întinse păduri de conifere.")
    Z.a(2, "2.2", "Ce zonă naturală domină estul Africii, cu Serengeti?", "savana", ["tundra", "taigaua", "pădurea de foioase"], "Serengeti e una dintre cele mai cunoscute savane.")
    Z.a(3, "1.2", "De ce în deșert nopțile sunt reci, deși zilele sunt fierbinți?", "pentru că aerul uscat și cerul senin lasă căldura să plece repede noaptea", ["pentru că bate vânt polar", "pentru că Soarele e mai mic noaptea", "pentru că nisipul se topește"], "Fără nori și umezeală, căldura nu e păstrată.")
    Z.a(3, "4.2", "Organizezi o „expoziție a zonelor naturale”. Ce pui la standul tundrei?", "fotografii cu reni, mușchi, licheni și zăpadă", ["fotografii cu cămile și dune", "fotografii cu lei și baobabi", "fotografii cu măslini"], "Fiecare stand arată elementele tipice.")
    Z.a(2, "4.3", "Cum ajuți la protejarea peisajelor naturale când mergi în excursie?", "rămâi pe poteci, iei gunoiul cu tine și nu faci zgomot", ["faci foc oriunde", "rupi flori", "hrănești animalele sălbatice"], "Natura rămâne frumoasă și pentru alții.")
    Z.a(3, "1.2", "Ce leagă clima de soluri, plante și animale într-o zonă naturală?", "clima decide ce plante cresc, plantele decid ce animale trăiesc și ce sol se formează", ["nimic, sunt independente", "doar relieful decide totul", "animalele decid clima"], "Componentele peisajului sunt legate între ele.")

    return Unitate(5, "u7-zone-naturale.json", "Zonele naturale ale Terrei").add(Z)
