from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VII-a, ediția 2024 (manuale.edu.ro), lecția „{}”"
S_AF = ["Encyclopaedia Britannica – Africa", "Wikipedia – Africa"]
S_KILI = ["Tanzania National Parks – Kilimanjaro National Park", "Encyclopaedia Britannica – Kilimanjaro"]
S_NIL = ["Encyclopaedia Britannica – Nile River", "Wikipedia – Nile"]
S_POP = ["ONU (UN DESA) – World Population Prospects 2024", "Our World in Data – Population by continent"]
S_SAH = ["Encyclopaedia Britannica – Sahara", "NASA Earth Observatory – Sahara Desert"]
S_ASSAL = ["Encyclopaedia Britannica – Lake Assal (Djibouti)", "Wikipedia – Lake Assal"]
S_TANG = ["Encyclopaedia Britannica – Lake Tanganyika", "Wikipedia – Lake Tanganyika"]
S_VICT = ["Encyclopaedia Britannica – Lake Victoria", "Wikipedia – Lake Victoria"]
S_UA = ["Uniunea Africană – Member States (au.int)", "Wikipedia – Member states of the African Union"]
S_LAGOS = ["ONU (UN DESA) – World Urbanization Prospects 2025", "Encyclopaedia Britannica – Lagos / Cairo / Kinshasa"]


def unitate():
    # ================================================================ S13a Poziție. Simetrie latitudinală
    P = Lectie(7, "VII-S13-caracterizare-geografica-pozitia-geografica", "Africa – poziția geografică. Simetria latitudinală",
               "De ce clima din nordul Africii seamănă cu cea din sudul ei?",
               [("Poziția", "Africa e al doilea continent ca mărime, cu aproximativ 30 de milioane km². E singurul continent străbătut de Ecuator, de ambele tropice și de meridianul de origine (Greenwich).\nE scăldată de Oceanul Atlantic (vest), Oceanul Indian (est), Marea Mediterană (nord) și Marea Roșie (nord-est). Strâmtoarea Gibraltar o desparte de Europa, iar Istmul Suez (cu Canalul Suez) o leagă de Asia."),
                ("Simetria latitudinală", "Ecuatorul trece aproape prin mijlocul Africii. De aceea, la nord și la sud de Ecuator se repetă, ca în oglindă, aceleași zone de climă și vegetație: pădure ecuatorială în centru, apoi savană, apoi deșert (Sahara în nord, Kalahari și Namib în sud), iar la capete climat mediteranean (nordul Africii și extremitatea sudică)."),
                ("Țărmurile", "Țărmurile Africii sunt puțin crestate. Cea mai mare peninsulă e Somalia („Cornul Africii”). Cea mai mare insulă e Madagascar. Golfuri: Golful Guineei, Golful Aden.")],
               stiaica="Africa e singurul continent prin care trec atât Ecuatorul, cât și ambele tropice și meridianul de 0°.",
               ref=REF.format("Caracterizare geografică – Poziția geografică – simetrie latitudinală"), prefix="VII13a")
    P.a(1, "2.1", "Ce loc ocupă Africa între continente, ca suprafață?", "al doilea, după Asia", ["primul", "ultimul", "al cincilea"], "Africa are aproximativ 30 de milioane km².", surse=S_AF)
    P.a(2, "2.1", "Ce linii imaginare importante trec prin Africa?", "Ecuatorul, ambele tropice și meridianul de origine", ["doar Cercul Polar", "niciuna", "doar meridianul de 180°"], "Africa e unică din acest punct de vedere.")
    P.e(2, "2.1", "Pune pe hartă apele care scaldă Africa.", [("atl", "Oceanul Atlantic", 0, -15), ("ind", "Oceanul Indian", -10, 60), ("med", "Marea Mediterană", 35, 18), ("ros", "Marea Roșie", 20, 38.5)], "Atlantic la vest, Indian la est, Mediterana la nord, Marea Roșie la nord-est.", harta="lume")
    P.a(2, "2.1", "Ce strâmtoare desparte Africa de Europa?", "Strâmtoarea Gibraltar", ["Bosforul", "Strâmtoarea Bering", "Strâmtoarea Malacca"], "Gibraltar e între Maroc și Spania.")
    P.a(2, "2.1", "Ce canal leagă Marea Mediterană de Marea Roșie?", "Canalul Suez", ["Canalul Panama", "Canalul Mânecii", "Canalul Kiel"], "Canalul Suez e în Egipt.")
    P.a(2, "2.1", "Care e cea mai mare insulă a Africii?", "Madagascar", ["Sicilia", "Sri Lanka", "Zanzibar"], "Madagascar e în Oceanul Indian.")
    P.a(2, "2.1", "Ce peninsulă e numită „Cornul Africii”?", "Peninsula Somalia", ["Peninsula Arabia", "Peninsula Sinai", "Capul Bunei Speranțe"], "E în estul Africii.")
    P.a(2, "1.1", "Ce înseamnă simetria latitudinală a Africii?", "zonele de climă și vegetație se repetă la nord și la sud de Ecuator, ca în oglindă", ["Africa are formă de cerc", "toată Africa are aceeași climă", "Africa e la fel ca Europa"], "Ecuatorul împarte Africa aproape în două.")
    P.o(3, "2.2 3.1 4.2", "Ordonează zonele naturale de la Ecuator spre nordul Africii.", ["pădurea ecuatorială", "savana", "semideșertul (Sahel)", "deșertul Sahara", "zona mediteraneeană"], "De la Ecuator spre nord", "Aceeași succesiune apare și spre sud.")
    P.o(3, "2.2 3.1 4.2", "Ordonează zonele naturale de la Ecuator spre sudul Africii.", ["pădurea ecuatorială", "savana", "deșertul Kalahari", "zona mediteraneeană (Capul Bunei Speranțe)"], "De la Ecuator spre sud", "Simetria latitudinală.")
    P.s(2, "2.2", "Asociază deșertul cu emisfera.", [("Sahara", "nordică"), ("Kalahari", "sudică"), ("Namib", "sudică, pe țărmul Atlanticului"), ("Deșertul Libian", "nordică, parte a Saharei")], "Deșerturi de o parte și de alta a Ecuatorului.")
    P.p(2, "2.1", "Atinge pe hartă Madagascar.", "lume", -19, 46.7, "Madagascar", 500, "Madagascar e la est de Africa.")
    P.p(2, "2.1", "Atinge pe hartă Peninsula Somalia.", "lume", 8, 48, "Somalia", 500, "„Cornul Africii” e în est.")
    P.p(2, "2.1", "Atinge pe hartă Golful Guineei.", "lume", 2, 3, "Golful Guineei", 700, "Golful Guineei e în vestul Africii.")
    P.p(3, "2.1", "Atinge pe hartă Capul Bunei Speranțe.", "lume", -34.36, 18.47, "Capul Bunei Speranțe", 400, "La sudul Africii.")
    P.p(3, "2.1", "Atinge pe hartă Canalul Suez.", "lume", 30.5, 32.35, "Canalul Suez", 300, "Canalul e în nord-estul Egiptului.")
    P.adev(2, "1.2", "Țărmurile Africii sunt foarte crestate, ca ale Europei.", False, "Fals: țărmurile Africii sunt puțin crestate.")
    P.adev(2, "2.2", "Sahara și Kalahari sunt în emisfere diferite.", True, "Adevărat: Sahara în nord, Kalahari în sud.")
    P.l(2, "2.1", "Completează.", "Cea mai mare insulă a Africii este [Madagascar]; Africa e despărțită de Europa prin Strâmtoarea [Gibraltar].", ["Sicilia", "Bering"], "Madagascar, Gibraltar.")
    P.l(2, "2.2", "Completează.", "La nord de Ecuator e deșertul [Sahara], iar la sud de Ecuator deșertul [Kalahari].", ["Gobi", "Atacama"], "Simetrie.")
    P.d(2, "2.1", "Ce țară, cu Canalul Suez, e marcată pe hartă?", "lume", 26.5, 30, "Egipt", ["Libia", "Sudan", "Algeria"], "Egiptul e în nord-estul Africii.")
    P.d(3, "2.1", "Ce peninsulă, între Africa și Asia, e marcată pe hartă?", "lume", 29.5, 33.8, "Peninsula Sinai", ["Peninsula Somalia", "Peninsula Arabia", "Cap Bon"], "Sinai aparține Egiptului, dar e în Asia.")
    P.a(2, "2.1", "În ce emisfere se află Africa?", "în ambele emisfere: nordică și sudică, estică și vestică", ["doar în emisfera sudică", "doar în emisfera vestică", "doar în emisfera nordică"], "Ecuatorul și meridianul de 0° trec prin Africa.")
    P.a(3, "2.3", "De ce Africa e numită continentul cel mai cald?", "pentru că aproape toată se află între tropice", ["pentru că are vulcani", "pentru că e cea mai mare", "pentru că e lângă pol"], "Razele Soarelui cad aproape perpendicular tot anul.")
    P.g(3, "2.3 4.1", "Graficul arată suprafața a trei continente (milioane km²). Cu cât e mai mare Africa decât Europa?", grafic("bare", "Suprafața (milioane km², rotunjit)", [("Asia", 44), ("Africa", 30), ("Europa", 10)], "milioane km²", "Encyclopaedia Britannica"), "de 3 ori", ["de 10 ori", "la fel", "de 2 ori mai mică"], "30 : 10 = 3.", surse=S_AF)
    P.a(2, "2.1", "Ce golf se află între Peninsula Arabia și Peninsula Somalia?", "Golful Aden", ["Golful Guineei", "Golful Persic", "Golful Biscaya"], "Golful Aden leagă Marea Roșie de Oceanul Indian.")
    P.a(2, "1.2", "Ce înseamnă că Africa are „țărmuri puțin crestate”?", "are puține golfuri și peninsule, deci puține porturi naturale adăpostite", ["are multe fiorduri", "nu are țărm", "are cele mai multe insule"], "Asta a îngreunat accesul în interior.")
    P.a(2, "2.1", "Ce ocean scaldă Africa la est?", "Oceanul Indian", ["Oceanul Atlantic", "Oceanul Pacific", "Oceanul Arctic"], "La vest e Atlanticul.")
    P.a(3, "4.3", "Compară poziția Africii cu a Europei față de Ecuator.", "Africa e străbătută de Ecuator; Europa e toată în emisfera nordică, departe de el", ["ambele sunt pe Ecuator", "Europa e la sud de Africa", "Africa e lângă Polul Nord"], "Poziția explică diferențele de climă.")
    P.a(2, "2.1", "Ce insule africane se află în Atlantic, aproape de Maroc?", "Insulele Canare", ["Madagascar", "Zanzibar", "Seychelles"], "Canarele aparțin Spaniei.")
    P.a(2, "2.1", "Ce oraș de pe Gibraltar, de partea africană, e aproape de Europa?", "Tanger (Maroc)", ["Cairo", "Lagos", "Nairobi"], "Tangerul e la ieșirea din Mediterana.")

    # ================================================================ S13b Relieful. Riftul
    R = Lectie(7, "VII-S13-relieful-africii-caracteristici-generale", "Africa – relieful. Riftul african",
               "Se poate rupe un continent în două?",
               [("Un continent de podișuri", "Relieful Africii e dominat de podișuri vechi și înalte, de aceea Africa e numită „continentul podișurilor”. Altitudinea crește de la nord-vest spre sud-est.\nCâmpiile sunt puține și înguste, de-a lungul țărmurilor. Munți: Atlas (nord-vest, munți tineri), Munții Drakensberg (sud-est), munții vulcanici din est."),
                ("Riftul african", "În estul Africii se află Marele Rift: un șir de fracturi uriașe ale scoarței, lung de mii de kilometri, unde placa africană se rupe încet. Aici sunt văi adânci, lacuri lungi și înguste (Tanganyika, Malawi), vulcani (Kilimanjaro, Kenya) și cutremure.\nÎn milioane de ani, estul Africii s-ar putea desprinde de restul continentului."),
                ("Extreme", "Cel mai înalt vârf: Kilimanjaro (5 895 m), un vulcan, în Tanzania. Cel mai jos punct: Lacul Assal (Djibouti), la aproximativ 155 m sub nivelul mării.")],
               stiaica="Deși e aproape de Ecuator, Kilimanjaro are zăpadă și ghețari pe vârf, care însă se micșorează rapid.",
               ref=REF.format("Relieful Africii – caracteristici generale. Riftul african"), prefix="VII13b")
    R.a(1, "2.1", "Care e cel mai înalt vârf din Africa?", "Kilimanjaro (5 895 m)", ["Everest", "Mont Blanc", "Atlas"], "Kilimanjaro e un vulcan, în Tanzania.", surse=S_KILI)
    R.a(2, "1.2", "De ce Africa e numită „continentul podișurilor”?", "pentru că relieful e dominat de podișuri vechi și înalte", ["pentru că are cei mai mulți munți", "pentru că e plată ca o câmpie", "pentru că are multe fiorduri"], "Câmpiile sunt puține.")
    R.a(2, "1.1", "Ce este Marele Rift african?", "un șir de fracturi uriașe ale scoarței, în estul Africii, unde continentul se rupe încet", ["un râu", "un deșert", "un munte de nisip"], "Riftul are văi adânci, lacuri și vulcani.")
    R.a(2, "2.2", "Ce forme de relief apar de-a lungul riftului?", "văi adânci, lacuri lungi și înguste, vulcani", ["dune de nisip", "fiorduri", "delte"], "Tanganyika și Malawi sunt lacuri de rift.")
    R.a(2, "2.1", "Care e cel mai jos punct al Africii?", "Lacul Assal, la aproximativ 155 m sub nivelul mării", ["Delta Nilului", "Lacul Victoria", "Sahara"], "Lacul Assal e în Djibouti.", surse=S_ASSAL)
    R.s(2, "2.1", "Asociază forma de relief cu regiunea.", [("Munții Atlas", "nord-vest (Maroc, Algeria)"), ("Kilimanjaro", "est (Tanzania)"), ("Munții Drakensberg", "sud-est (Africa de Sud)"), ("Riftul", "est")], "Relieful Africii.")
    R.p(2, "2.1", "Atinge pe hartă Kilimanjaro.", "lume", -3.07, 37.35, "Kilimanjaro", 400, "Kilimanjaro e în nord-estul Tanzaniei.", surse=S_KILI)
    R.p(2, "2.1", "Atinge pe hartă Munții Atlas.", "lume", 31.5, -6, "Munții Atlas", 500, "Atlasul e în Maroc și Algeria.")
    R.p(3, "2.1", "Atinge pe hartă Lacul Tanganyika, un lac de rift.", "lume", -6.5, 29.8, "Lacul Tanganyika", 400, "Tanganyika e între Tanzania și R.D. Congo.", surse=S_TANG)
    R.p(3, "2.1", "Atinge pe hartă Munții Drakensberg.", "lume", -29.5, 29.3, "Drakensberg", 500, "Drakensberg e în sud-estul Africii de Sud.")
    R.a(2, "2.2", "Ce se poate întâmpla, peste milioane de ani, din cauza riftului?", "estul Africii s-ar putea desprinde de restul continentului", ["Africa se va uni cu America", "Sahara va deveni ocean imediat", "nimic"], "Riftul e o graniță între plăci care se depărtează.")
    R.a(2, "2.2", "Ce fenomene naturale sunt frecvente în zona riftului?", "cutremure și erupții vulcanice", ["avalanșe de zăpadă", "taifunuri", "tsunami-uri în deșert"], "Scoarța e activă.")
    R.a(2, "2.2", "De ce Kilimanjaro are zăpadă, deși e lângă Ecuator?", "pentru că altitudinea foarte mare face temperatura scăzută", ["pentru că e la pol", "pentru că ninge în toată Africa", "pentru că zăpada e artificială"], "Temperatura scade cu altitudinea.")
    R.a(2, "2.1", "Ce munți tineri se află în nord-vestul Africii?", "Munții Atlas", ["Munții Drakensberg", "Munții Kenya", "Munții Etiopiei"], "Atlasul s-a format odată cu Alpii.")
    R.a(2, "2.1", "Ce podiș înalt se află în estul Africii, cu munți vulcanici?", "Podișul Etiopiei", ["Podișul Tibet", "Podișul Deccan", "Podișul Mexicului"], "Etiopia e numită „acoperișul Africii”.")
    R.adev(2, "2.2", "Africa are câmpii foarte întinse, ca Asia și Europa.", False, "Fals: câmpiile sunt puține și înguste, pe țărmuri.")
    R.adev(2, "2.2", "Kilimanjaro este un vulcan.", True, "Adevărat: e un vulcan inactiv.")
    R.l(2, "2.1", "Completează.", "Cel mai înalt vârf al Africii este [Kilimanjaro]; în estul Africii scoarța se rupe de-a lungul Marelui [Rift].", ["Atlas", "Canion"], "Kilimanjaro, Rift.")
    R.l(2, "2.2", "Completează.", "Africa e numită continentul [podișurilor]; cel mai jos punct e Lacul [Assal].", ["fiordurilor", "Victoria"], "Podișuri, Assal.")
    R.g(3, "2.3 4.1", "Profilul schematic arată altitudinea de la vest la est prin Africa de Est. Unde e altitudinea cea mai mare?", grafic("profil", "Profil schematic prin Africa de Est (valori aproximative)", [("Bazinul Congo", 400), ("lacul de rift", 800), ("podișul înalt", 1500), ("Kilimanjaro", 5895), ("țărmul Oceanului Indian", 0)], "m"), "la Kilimanjaro", ["în Bazinul Congo", "pe țărm", "la lacul de rift"], "Kilimanjaro e cel mai înalt punct.", surse=S_KILI)
    R.a(3, "4.3", "Compară Kilimanjaro cu Everest.", "Everest e mai înalt (8 848,86 m) și e în munți de încrețire; Kilimanjaro (5 895 m) e un vulcan izolat", ["Kilimanjaro e mai înalt", "sunt identici", "Everest e un vulcan"], "Origini diferite.")
    R.d(2, "2.1", "Ce lac de rift lung și îngust e marcat pe hartă?", "lume", -12, 34.5, "Lacul Malawi", ["Lacul Victoria", "Lacul Ciad", "Lacul Assal"], "Lacul Malawi e în sudul riftului.")
    R.a(2, "2.1", "Ce deșert e cel mai mare de pe uscat, fără regiunile polare?", "Sahara", ["Kalahari", "Namib", "Gobi"], "Sahara are aproximativ 9 milioane km².", surse=S_SAH)
    R.a(2, "2.2", "Ce formă de relief e Bazinul Congo?", "o depresiune largă, înconjurată de podișuri", ["un munte vulcanic", "un fiord", "un rift"], "Bazinul Congo e străbătut de Ecuator.")
    R.a(2, "2.1", "Ce munți vulcanici, al doilea vârf al Africii, se află în Kenya?", "Muntele Kenya", ["Atlas", "Drakensberg", "Ruwenzori"], "Țara poartă numele muntelui.")
    R.a(3, "1.2", "Cum se explică forma lungă și îngustă a lacurilor Tanganyika și Malawi?", "s-au format în văile riftului, care sunt lungi și înguste", ["au fost săpate de oameni", "sunt cratere de vulcan", "sunt lacuri glaciare"], "Lacurile de rift sunt tectonice.")
    R.a(2, "2.1", "Ce munți, cu ghețari, se află la granița Ugandei cu R.D. Congo?", "Munții Ruwenzori", ["Munții Atlas", "Munții Drakensberg", "Munții Kenya"], "Sunt numiți și „Munții Lunii”.")
    R.a(2, "4.4", "De ce se micșorează ghețarii de pe Kilimanjaro?", "din cauza încălzirii climei și a aerului mai uscat", ["pentru că muntele scade", "pentru că sunt topiți de lavă", "pentru că sunt tăiați de oameni"], "Ghețarii tropicali sunt foarte sensibili.")
    R.a(2, "2.2", "Ce dovezi ale primilor oameni s-au găsit în riftul est-african?", "fosile foarte vechi ale strămoșilor omului", ["dinozauri doar", "orașe moderne", "vapoare"], "Riftul e numit „leagănul omenirii”.")
    R.a(2, "2.1", "Ce munți se află la sudul Africii de Sud, lângă Cape Town?", "Munții Capului (cu Muntele Masei)", ["Munții Atlas", "Munții Ural", "Munții Kenya"], "Muntele Masei are vârful plat.")
    R.a(2, "2.2", "Ce înseamnă că altitudinea Africii crește de la nord-vest spre sud-est?", "în nord-vest sunt podișuri mai joase, iar în est și sud podișuri mai înalte", ["Africa e plată", "toată Africa e sub nivelul mării", "munții sunt doar în nord"], "De aceea se vorbește de „Africa joasă” și „Africa înaltă”.")

    # ================================================================ S16 Hidrografia, clima, biogeografia
    H = Lectie(7, "VII-S16-hidrografia-clima-biogeografia-caracteristici", "Africa – ape, climă, vegetație și faună",
               "Cum poate cel mai lung fluviu al lumii să traverseze cel mai mare deșert fierbinte?",
               [("Apele", "Nilul (aproximativ 6 650 km) e cel mai lung fluviu de pe Pământ, după majoritatea măsurătorilor. Se formează din Nilul Alb (din Lacul Victoria) și Nilul Albastru (din Podișul Etiopiei) și traversează Sahara până în Marea Mediterană.\nCongo e fluviul cu cea mai mare cantitate de apă din Africa. Alte fluvii: Niger, Zambezi (cu Cascada Victoria), Orange.\nLacuri: Victoria (cel mai mare lac din Africa), Tanganyika (foarte adânc, de rift), Malawi, Ciad (care se micșorează)."),
                ("Clima", "Africa e cel mai cald continent. Clima e ecuatorială în centru (cald și ploios tot anul), subecuatorială (savană, cu un anotimp ploios și unul secetos), tropical-deșertică (Sahara, Kalahari, Namib), mediteraneeană la extremități.\nÎn Sahara plouă foarte rar, iar între zi și noapte temperatura poate varia cu zeci de grade."),
                ("Vegetația și fauna", "Pădurea ecuatorială (Bazinul Congo): gorile, cimpanzei, okapi. Savana: lei, elefanți, girafe, zebre, antilope, rinoceri – cea mai bogată faună de mamifere mari. Deșertul: dromaderi, fenecul (vulpea deșertului), scorpioni. Madagascar: lemurieni, care trăiesc doar acolo.")],
               stiaica="Cascada Victoria, de pe Zambezi, e numită de localnici „Mosi-oa-Tunya”, adică „fumul care tună”, după norul de stropi care se vede de la zeci de kilometri.",
               ref=REF.format("Hidrografia, clima și biogeografia – caracteristici generale"))
    H.a(1, "2.1", "Care e cel mai lung fluviu de pe Pământ, după majoritatea măsurătorilor?", "Nilul", ["Congo", "Niger", "Zambezi"], "Nilul are aproximativ 6 650 km.", surse=S_NIL)
    H.a(2, "2.1", "Din ce lac pornește Nilul Alb?", "Lacul Victoria", ["Lacul Ciad", "Lacul Tanganyika", "Lacul Assal"], "Nilul Albastru vine din Etiopia.", surse=S_NIL)
    H.a(2, "2.1", "Unde se varsă Nilul?", "în Marea Mediterană", ["în Oceanul Atlantic", "în Marea Roșie", "în Lacul Victoria"], "Nilul formează o deltă în nordul Egiptului.")
    H.a(2, "2.1", "Ce fluviu african are cea mai mare cantitate de apă?", "Congo", ["Nilul", "Orange", "Limpopo"], "Bazinul Congo primește ploi tot anul.")
    H.a(2, "2.1", "Pe ce fluviu se află Cascada Victoria?", "Zambezi", ["Nil", "Congo", "Niger"], "Cascada e la granița Zambiei cu Zimbabwe.")
    H.a(2, "2.1", "Care e cel mai mare lac din Africa?", "Lacul Victoria", ["Lacul Ciad", "Lacul Malawi", "Lacul Assal"], "Victoria e între Uganda, Kenya și Tanzania.", surse=S_VICT)
    H.p(2, "2.1", "Atinge pe hartă Lacul Victoria.", "lume", -1, 33, "Lacul Victoria", 400, "Lacul Victoria e în estul Africii, pe Ecuator.", surse=S_VICT)
    H.p(2, "2.1", "Atinge pe hartă Delta Nilului.", "lume", 31, 31, "Delta Nilului", 300, "Delta Nilului e în nordul Egiptului.")
    H.p(3, "2.1", "Atinge pe hartă Lacul Ciad.", "lume", 13, 14.5, "Lacul Ciad", 500, "Lacul Ciad e la marginea sudică a Saharei.")
    H.s(2, "3.3", "Asociază zona naturală cu animalul tipic.", [("pădurea ecuatorială", "gorila"), ("savana", "girafa"), ("deșertul", "dromaderul"), ("Madagascar", "lemurul")], "Fauna Africii.")
    H.s(2, "3.2", "Asociază climatul cu regiunea.", [("ecuatorial", "Bazinul Congo"), ("subecuatorial", "savanele din est"), ("tropical-deșertic", "Sahara"), ("mediteranean", "nordul Marocului și Algeriei")], "Climatele Africii.")
    H.a(2, "3.2", "Ce caracterizează savana?", "ierburi înalte, copaci rari și un anotimp ploios alternând cu unul secetos", ["păduri dese și ploi zilnice", "gheață tot anul", "fără vegetație"], "Baobabul și acacia sunt tipice.")
    H.a(2, "3.2", "De ce în Sahara nopțile sunt reci?", "aerul uscat și cerul senin lasă căldura să plece repede", ["pentru că bate vânt polar", "pentru că ninge", "pentru că e lângă ocean"], "Amplitudinea zi–noapte e foarte mare.")
    H.a(2, "3.3", "Ce animale trăiesc doar în Madagascar?", "lemurienii", ["leii", "girafele", "zebrele"], "Izolarea insulei a dus la specii unice.")
    H.a(2, "4.4", "De ce s-a micșorat Lacul Ciad?", "din cauza secetelor și a folosirii apei pentru irigații", ["din cauza unui vulcan", "pentru că s-a umplut cu gheață", "pentru că l-a acoperit nisipul într-o zi"], "Milioane de oameni depind de el.")
    H.adev(2, "3.2", "Africa e cel mai cald continent.", True, "Adevărat: cea mai mare parte e între tropice.")
    H.adev(2, "3.3", "Gorilele trăiesc în deșertul Sahara.", False, "Fals: trăiesc în pădurile ecuatoriale.")
    H.l(2, "2.1", "Completează.", "Nilul se formează din Nilul [Alb] și Nilul [Albastru].", ["Roșu", "Verde"], "Se unesc la Khartoum, în Sudan.")
    H.l(2, "3.3", "Completează.", "În savană trăiesc [girafe] și zebre; în pădurea ecuatorială trăiesc [gorile].", ["pinguini", "reni"], "Fauna după zone.")
    H.g(3, "2.3 4.1", "Diagrama arată precipitațiile anuale în trei locuri din Africa (valori aproximative). Care e în Sahara?", grafic("bare", "Precipitații anuale (valori aproximative)", [("Bazinul Congo", 1800), ("savana din Kenya", 800), ("Sahara centrală", 20)], "l/m²"), "Sahara centrală", ["Bazinul Congo", "savana din Kenya", "toate"], "Sub 20 l/m² pe an.", surse=S_SAH)
    H.a(3, "4.3", "De ce Nilul nu seacă traversând Sahara?", "pentru că primește apă din regiunile ploioase (Lacul Victoria, Etiopia), unde izvorăște", ["pentru că plouă mult în Sahara", "pentru că are ghețari", "pentru că e alimentat de mare"], "E un fluviu „alohton” în deșert.")
    H.a(2, "3.3", "Ce copac uriaș, cu trunchi gros, e simbolul savanei?", "baobabul", ["molidul", "palmierul de cocos", "stejarul"], "Baobabul stochează apă.")
    H.a(2, "3.3", "Ce animal din pădurea ecuatorială seamănă cu o girafă mică, cu dungi pe picioare?", "okapi", ["zebra", "lama", "renul"], "Okapi trăiește în R.D. Congo.")
    H.a(2, "3.3", "Ce animal mic, cu urechi mari, trăiește în Sahara?", "fenecul (vulpea deșertului)", ["ursul polar", "lupul", "castorul"], "Urechile mari îl ajută să elimine căldura.")
    H.d(2, "2.1", "Ce fluviu din vestul Africii are cursul în formă de arc și trece prin Mali și Nigeria?", "lume", 13, -2, "Niger", ["Nil", "Congo", "Zambezi"], "Nigerul se varsă în Golful Guineei.")
    H.a(2, "3.2", "Ce vânt fierbinte și uscat bate din Sahara spre Golful Guineei?", "harmattanul", ["musonul", "foehnul", "crivățul"], "Harmattanul aduce praf din deșert.")
    H.a(2, "4.4", "Ce amenință elefanții și rinocerii din savană?", "braconajul pentru fildeș și coarne", ["frigul", "inundațiile de zăpadă", "vulcanii"], "Parcurile naționale îi protejează.")
    H.a(2, "3.3", "Ce parc național din Tanzania e celebru pentru migrația antilopelor gnu?", "Serengeti", ["Yellowstone", "Retezat", "Kruger"], "Milioane de gnu migrează anual între Tanzania și Kenya.")
    H.a(2, "3.2", "Ce climat are Bazinul Congo?", "ecuatorial: cald și ploios tot anul", ["deșertic", "mediteranean", "polar"], "Plouă aproape zilnic.")
    H.a(3, "3.2", "De ce în savană există un anotimp secetos?", "zona ploilor de la Ecuator se mută spre nord și spre sud odată cu Soarele, așa că ploile vin doar o parte din an", ["pentru că bate musonul de iarnă din Siberia", "pentru că e lângă pol", "fără motiv"], "Ploile urmează poziția Soarelui.")
    H.a(2, "3.3", "Ce baraj mare pe Nil formează Lacul Nasser?", "Barajul de la Assuan", ["Trei Defileuri", "Porțile de Fier", "Hoover"], "Barajul de la Assuan e în sudul Egiptului.")

    # ================================================================ S17 Specificul demografic
    D = Lectie(7, "VII-S17-specificul-demografic", "Africa – specificul demografic",
               "De ce Africa are cea mai tânără populație din lume?",
               [("Numărul și creșterea", "În Africa trăiesc aproximativ 1,5 miliarde de oameni, după ONU. E continentul cu cea mai rapidă creștere a populației: natalitatea e foarte mare, iar mortalitatea a scăzut datorită medicinei.\nNigeria e cea mai populată țară a Africii."),
                ("O populație tânără", "Aproape jumătate dintre africani au sub 20 de ani. Piramida vârstelor are baza foarte largă (mulți copii) și vârful îngust.\nSperanța de viață e mai mică decât în Europa, din cauza bolilor (malarie), a sărăciei și a lipsei serviciilor medicale în unele regiuni, dar crește."),
                ("Răspândire și diversitate", "Populația e densă pe Valea Nilului, în jurul Lacului Victoria, pe țărmul Golfului Guineei și în nordul și sudul continentului. Sahara și deșerturile din sud sunt aproape nelocuite.\nÎn Africa trăiesc mii de popoare și se vorbesc peste 2 000 de limbi: araba (în nord), swahili (în est), hausa, yoruba, zulu și altele; se folosesc și engleza, franceza, portugheza.")],
               stiaica="Swahili e vorbită de zeci de milioane de oameni în estul Africii; cuvântul „safari” vine din swahili și înseamnă „călătorie”.",
               ref=REF.format("Specificul demografic"))
    D.a(1, "3.2", "Câți oameni trăiesc în Africa, aproximativ?", "1,5 miliarde", ["150 de milioane", "15 miliarde", "15 milioane"], "După estimările ONU.", surse=S_POP)
    D.a(2, "3.2", "Ce țară africană are cea mai numeroasă populație?", "Nigeria", ["Egipt", "Africa de Sud", "Algeria"], "Nigeria are peste 200 de milioane de locuitori.", surse=S_POP)
    D.a(2, "1.2", "De ce populația Africii crește foarte repede?", "natalitatea e mare, iar mortalitatea a scăzut", ["natalitatea e foarte mică", "vin mulți imigranți din Europa", "nu mor oameni"], "Sporul natural e cel mai mare din lume.")
    D.a(2, "1.2", "Ce formă are piramida vârstelor în multe țări africane?", "bază foarte largă (mulți copii) și vârf îngust", ["vârf larg și bază îngustă", "dreptunghi", "cerc"], "Populație tânără.")
    D.a(2, "1.2", "Ce boală transmisă de țânțari afectează mult Africa?", "malaria", ["gripa aviară", "varicela", "răceala"], "Plasele de țânțari și medicamentele reduc cazurile.")
    D.a(2, "2.2", "Unde e densă populația în Africa?", "pe Valea Nilului, în jurul Lacului Victoria și pe țărmul Golfului Guineei", ["în centrul Saharei", "în deșertul Namib", "pe vârful Kilimanjaro"], "Apa și solurile fertile atrag oamenii.")
    D.a(2, "2.2", "De ce Sahara e aproape nelocuită?", "lipsa apei", ["frigul", "munții înalți", "pădurile dese"], "Oamenii trăiesc doar în oaze.")
    D.s(2, "3.3", "Asociază limba cu regiunea Africii.", [("araba", "nord"), ("swahili", "est"), ("zulu", "sud"), ("yoruba", "vest (Nigeria)")], "Diversitate lingvistică.")
    D.a(2, "3.3", "Câte limbi se vorbesc în Africa, aproximativ?", "peste 2 000", ["10", "100", "50"], "Africa are o diversitate lingvistică uriașă.")
    D.a(2, "3.3", "De ce în multe țări africane limbile oficiale sunt engleza, franceza sau portugheza?", "pentru că au fost colonii ale unor țări europene", ["pentru că sunt în Europa", "pentru că toți locuitorii sunt europeni", "fără motiv"], "Moștenirea colonială.")
    D.p(2, "2.1", "Atinge pe hartă Nigeria.", "lume", 9, 8, "Nigeria", 500, "Nigeria e în vestul Africii, la Golful Guineei.")
    D.p(3, "2.1", "Atinge pe hartă Valea Nilului, în Egipt.", "lume", 26, 32.5, "Valea Nilului", 300, "Aproape toți egiptenii trăiesc pe valea și în delta Nilului.")
    D.adev(2, "1.2", "Africa are cea mai îmbătrânită populație din lume.", False, "Fals: are cea mai tânără populație.")
    D.adev(2, "1.2", "Speranța de viață în Africa crește, dar e încă mai mică decât în Europa.", True, "Adevărat.")
    D.l(2, "3.2", "Completează.", "Cea mai populată țară a Africii este [Nigeria]; în estul Africii se vorbește mult limba [swahili].", ["Egipt", "chineza"], "Nigeria, swahili.")
    D.l(2, "1.2", "Completează.", "În Africa natalitatea e [mare], de aceea populația e foarte [tânără].", ["mică", "îmbătrânită"], "Natalitate mare, populație tânără.")
    D.g(3, "2.3 4.1", "Graficul compară vârsta medie a populației în două regiuni (valori aproximative). Ce observi?", grafic("bare", "Vârsta medie a populației (aproximativ)", [("Africa", 19), ("Europa", 42)], "ani", "ONU – World Population Prospects 2024"), "populația Africii e mult mai tânără", ["Europa are populație mai tânără", "sunt egale", "Africa are populație bătrână"], "Jumătate dintre africani au sub aproximativ 19 ani.", surse=S_POP)
    D.g(3, "2.3 4.1", "Graficul arată evoluția populației Africii (miliarde, aproximativ). Cum a evoluat?", grafic("profil", "Populația Africii (aproximativ)", [("1950", 0.23), ("1980", 0.48), ("2000", 0.82), ("2024", 1.5)], "miliarde", "ONU – World Population Prospects 2024"), "a crescut foarte repede", ["a scăzut", "a rămas la fel", "a crescut doar până în 1950"], "De peste 6 ori din 1950.", surse=S_POP)
    D.a(3, "4.3", "Compară sporul natural din Niger (țară africană) cu cel din România.", "în Niger e foarte mare și pozitiv; în România e negativ", ["în România e mai mare", "sunt egale", "în Niger e negativ"], "Africa are natalitatea cea mai mare.")
    D.a(2, "3.3", "Ce religii sunt majoritare în Africa?", "islamul (mai ales în nord) și creștinismul (mai ales în sud și centru)", ["budismul și hinduismul", "șintoismul", "taoismul"], "Există și religii tradiționale.")
    D.a(2, "1.2", "De ce mulți tineri africani se mută la oraș?", "pentru locuri de muncă și școli", ["pentru că la sat e prea frig", "pentru că orașele sunt mai mici", "pentru că e obligatoriu"], "Urbanizarea Africii e foarte rapidă.")
    D.a(2, "3.3", "Ce popoare trăiesc în Sahara, cu tradiții nomade?", "tuaregii și berberii", ["inuiții", "samii", "maorii"], "Tuaregii sunt numiți „oamenii albaștri” după culoarea veșmintelor.")
    D.a(2, "3.3", "Ce înseamnă „nomad”?", "care se mută des dintr-un loc în altul, cu turmele", ["care stă mereu în același loc", "care locuiește la oraș", "care e marinar"], "Nomazii caută pășuni și apă.")
    D.a(2, "4.4", "Ce ajută la creșterea speranței de viață în Africa?", "vaccinarea, apa potabilă, spitalele și educația", ["mai puține școli", "mai puțină apă", "mai puține medicamente"], "Sănătatea publică salvează vieți.")
    D.d(2, "2.1", "Ce țară africană, cu cea mai mare populație din nordul continentului, e marcată pe hartă?", "lume", 26.5, 30, "Egipt", ["Libia", "Algeria", "Sudan"], "Egiptul are peste 100 de milioane de locuitori.")
    D.a(2, "3.3", "Ce limbă e oficială în Brazilia și în Angola și Mozambic?", "portugheza", ["spaniola", "franceza", "araba"], "Toate au fost colonii portugheze.")
    D.a(3, "1.2", "De ce o populație tânără poate fi o șansă pentru Africa?", "mulți tineri pot munci și inova, dacă au educație și locuri de muncă", ["nu e nicio șansă", "tinerii nu muncesc", "tinerii pleacă toți"], "Se numește „dividend demografic”.")
    D.a(2, "3.3", "Ce limbă se vorbește în nordul Africii (Egipt, Maroc, Algeria)?", "araba", ["swahili", "zulu", "engleza"], "Nordul Africii e o regiune arabă.")
    D.a(2, "2.2", "De ce țărmul Golfului Guineei e dens populat?", "are ploi, soluri bune, porturi și orașe mari", ["e deșert", "e acoperit de gheață", "e foarte muntos"], "Lagos, Accra, Abidjan sunt pe acest țărm.")
    D.a(2, "3.3", "Ce înseamnă cuvântul swahili „safari”?", "călătorie", ["leu", "deșert", "râu"], "Azi înseamnă excursie pentru observarea animalelor.")

    # ================================================================ S19 Harta politică. Orașele
    O = Lectie(7, "VII-S19-harta-politica-marile-orase", "Africa – harta politică și marile orașe",
               "De ce multe granițe din Africa sunt linii drepte?",
               [("Statele Africii", "Africa are 54 de state independente – cele mai multe dintre continente. Cel mai mare ca suprafață e Algeria; cel mai mic, pe continent, e Gambia; Seychelles e cel mai mic stat insular.\nCele mai multe state au devenit independente în anii 1950–1970, după perioada colonială."),
                ("Granițele", "În secolul XIX, puterile europene (Marea Britanie, Franța, Portugalia, Belgia, Germania, Italia) au împărțit Africa în colonii. Multe granițe au fost trasate pe hartă cu rigla, fără să țină seama de popoare sau de relief. De aceea apar granițe drepte, iar unele popoare au fost despărțite."),
                ("Marile orașe", "Cele mai mari orașe: Lagos (Nigeria), Cairo (Egipt), Kinshasa (R.D. Congo), Johannesburg (Africa de Sud), Luanda, Dar es Salaam, Nairobi, Addis Abeba (sediul Uniunii Africane), Casablanca.\nOrașele cresc foarte repede, iar multe au cartiere sărace la margine.")],
               stiaica="Kinshasa și Brazzaville, capitalele a două state diferite, sunt așezate față în față, pe malurile fluviului Congo – cele mai apropiate capitale din lume după Roma și Vatican.",
               ref=REF.format("Harta politică și marile orașe"))
    O.a(1, "1.2", "Câte state independente are Africa?", "54", ["7", "27", "100"], "Africa are cele mai multe state dintre continente.", surse=S_UA)
    O.a(2, "1.2", "Care e cel mai mare stat al Africii ca suprafață?", "Algeria", ["Egipt", "Nigeria", "Kenya"], "Algeria are peste 2,3 milioane km², mare parte din Sahara.")
    O.a(2, "1.2", "De ce multe granițe din Africa sunt drepte?", "au fost trasate pe hartă de puterile coloniale europene", ["urmează râuri drepte", "urmează munți drepți", "au fost alese de animale"], "Împărțirea Africii, secolul XIX.")
    O.a(2, "1.2", "Când au devenit independente cele mai multe state africane?", "în anii 1950–1970", ["în anul 1000", "în 1492", "în 2020"], "Decolonizarea.")
    O.s(2, "2.1", "Asociază statul cu capitala.", [("Egipt", "Cairo"), ("Kenya", "Nairobi"), ("Etiopia", "Addis Abeba"), ("Maroc", "Rabat")], "Capitale africane.")
    O.s(2, "2.1", "Asociază statul cu capitala.", [("Nigeria", "Abuja"), ("R.D. Congo", "Kinshasa"), ("Senegal", "Dakar"), ("Algeria", "Alger")], "Alte capitale africane.")
    O.a(2, "2.1", "Ce oraș e cel mai mare din Nigeria, dar nu e capitala?", "Lagos", ["Abuja", "Cairo", "Nairobi"], "Capitala Nigeriei e Abuja.")
    O.a(2, "2.1", "În ce oraș are sediul Uniunea Africană?", "Addis Abeba (Etiopia)", ["Cairo", "Lagos", "Pretoria"], "Uniunea Africană are 55 de state membre.", surse=S_UA)
    O.p(2, "2.1", "Atinge pe hartă Cairo.", "lume", 30.04, 31.24, "Cairo", 300, "Cairo e la capătul sudic al Deltei Nilului.")
    O.p(2, "2.1", "Atinge pe hartă Lagos.", "lume", 6.52, 3.38, "Lagos", 300, "Lagos e pe țărmul Golfului Guineei.", surse=S_LAGOS)
    O.p(2, "2.1", "Atinge pe hartă Kinshasa.", "lume", -4.32, 15.31, "Kinshasa", 400, "Kinshasa e pe fluviul Congo.")
    O.p(3, "2.1", "Atinge pe hartă Nairobi.", "lume", -1.29, 36.82, "Nairobi", 300, "Nairobi e capitala Kenyei.")
    O.p(3, "2.1", "Atinge pe hartă Johannesburg.", "lume", -26.2, 28.05, "Johannesburg", 400, "Johannesburg e cel mai mare oraș al Africii de Sud.")
    O.a(2, "1.2", "Ce țări europene aveau cele mai multe colonii în Africa?", "Marea Britanie și Franța", ["Elveția și Austria", "Polonia și Cehia", "România și Bulgaria"], "Și Portugalia, Belgia, Germania, Italia.")
    O.a(2, "2.1", "Ce stat african nu a fost niciodată colonizat pe termen lung?", "Etiopia (și Liberia)", ["Nigeria", "Kenya", "Senegal"], "Etiopia a rezistat colonizării.")
    O.adev(2, "1.2", "Toate granițele din Africa urmează râuri și munți.", False, "Fals: multe sunt linii drepte trasate în perioada colonială.")
    O.adev(2, "1.2", "Africa are mai multe state decât orice alt continent.", True, "Adevărat: 54 de state.", surse=S_UA)
    O.l(2, "2.1", "Completează.", "Capitala Egiptului este [Cairo], iar capitala Kenyei este [Nairobi].", ["Alexandria", "Mombasa"], "Cairo, Nairobi.")
    O.l(2, "1.2", "Completează.", "Africa are [54] de state; cel mai mare dintre ele ca suprafață este [Algeria].", ["27", "Nigeria"], "54, Algeria.", surse=S_UA)
    O.o(3, "2.2 3.1 4.2", "Ordonează orașele de la nord la sud.", ["Cairo", "Addis Abeba", "Nairobi", "Kinshasa", "Johannesburg", "Cape Town"], "De la nord la sud", "De la Mediterana la Capul Bunei Speranțe.")
    O.a(2, "3.3", "Ce problemă au multe orașe africane care cresc repede?", "cartiere sărace fără apă curentă și canalizare", ["prea puțini locuitori", "prea multe parcuri", "prea mult spațiu"], "Infrastructura nu ține pasul.")
    O.d(2, "2.1", "Ce stat african, cel mai mare ca suprafață, e marcat pe hartă?", "lume", 28, 2.6, "Algeria", ["Libia", "Mali", "Niger"], "Algeria e în nord-vestul Africii.")
    O.d(3, "2.1", "Ce stat insular din Oceanul Indian e marcat pe hartă?", "lume", -19, 46.7, "Madagascar", ["Mauritius", "Seychelles", "Comore"], "Madagascar e a patra insulă ca mărime din lume.")
    O.a(3, "4.3", "Ce consecințe au avut granițele trasate cu rigla?", "unele popoare au fost despărțite, iar altele, rivale, au fost puse în același stat, ceea ce a produs conflicte", ["nicio consecință", "au oprit toate conflictele", "au făcut toate țările bogate"], "Moștenirea colonială e încă vizibilă.")
    O.a(2, "2.1", "Ce megaoraș african e pe Nil, la capătul sudic al deltei?", "Cairo", ["Lagos", "Kinshasa", "Nairobi"], "Cairo e una dintre cele mai mari aglomerări urbane ale lumii.", surse=S_LAGOS)
    O.a(2, "2.1", "Ce capitală e față în față cu Kinshasa, peste fluviul Congo?", "Brazzaville (Republica Congo)", ["Luanda", "Lagos", "Nairobi"], "Două state cu nume asemănătoare.")
    O.a(2, "2.1", "Ce stat are trei capitale: Pretoria, Cape Town și Bloemfontein?", "Africa de Sud", ["Egipt", "Kenya", "Maroc"], "Fiecare are o funcție diferită.")
    O.a(2, "2.1", "Ce stat african e cel mai nou, independent din 2011?", "Sudanul de Sud", ["Egipt", "Etiopia", "Maroc"], "S-a desprins din Sudan.")
    O.a(2, "3.3", "Ce înseamnă „decolonizare”?", "obținerea independenței de către fostele colonii", ["colonizarea unor noi teritorii", "construirea de orașe", "mutarea capitalei"], "Majoritatea statelor africane s-au decolonizat după 1950.")
    O.a(2, "2.1", "Ce oraș-port mare se află în Maroc, pe Atlantic?", "Casablanca", ["Cairo", "Nairobi", "Kinshasa"], "Casablanca e cel mai mare oraș al Marocului.")

    # ================================================================ S20 Problemele Africii. Sahara
    S = Lectie(7, "VII-S20-studii-caz-problemele-africii", "Problemele Africii în lumea contemporană. Studiu de caz: Sahara",
               "Se poate opri înaintarea deșertului?",
               [("Probleme și progrese", "Africa are resurse bogate (petrol, gaze, aur, diamante, cupru, cobalt, cacao, cafea), dar multe țări au încă venituri mici. Probleme: sărăcia, lipsa apei potabile în unele zone, bolile, conflictele, deșertificarea, braconajul.\nÎn același timp, Africa are economii care cresc repede, o populație tânără, telefonie mobilă și plăți digitale foarte răspândite, energie solară în dezvoltare."),
                ("Sahara", "Sahara e cel mai mare deșert fierbinte de pe Pământ, cu aproximativ 9 milioane km² – aproape cât Statele Unite. Doar o mică parte e acoperită de dune (ergurile); cea mai mare parte e deșert de piatră (hamada) și de pietriș (reg).\nViața se concentrează în oaze, unde apa subterană ajunge la suprafață: aici se cultivă curmali. Sub Sahara există mari rezerve de apă subterană fosilă."),
                ("Deșertificarea și Sahelul", "Sahelul e fâșia semiaridă de la sudul Saharei. Aici, secetele, pășunatul excesiv și tăierea arbuștilor duc la deșertificare – transformarea treptată a terenurilor în deșert.\nProiectul „Marele Zid Verde” urmărește plantarea unei fâșii de vegetație de-a lungul Sahelului, de la Senegal la Djibouti.")],
               stiaica="Acum câteva mii de ani, Sahara era mult mai verde: picturile pe stâncă din munții Tassili n'Ajjer arată girafe, elefanți și oameni care păzeau turme.",
               ref=REF.format("Studii de caz: Problemele Africii în lumea contemporană, Sahara"))
    S.a(1, "2.1", "Ce suprafață are Sahara, aproximativ?", "9 milioane km²", ["900 km²", "90 000 km²", "90 de milioane km²"], "Aproape cât Statele Unite.", surse=S_SAH)
    S.a(2, "1.1", "Ce este deșertificarea?", "transformarea treptată a unor terenuri în deșert", ["plantarea de păduri", "formarea unui lac", "topirea ghețarilor"], "Cauzele sunt seceta și activitățile omului.")
    S.a(2, "1.1", "Ce este Sahelul?", "fâșia semiaridă de la sudul Saharei", ["un munte în Maroc", "un fluviu", "o pădure ecuatorială"], "Sahel înseamnă „țărm” în arabă: „țărmul” deșertului.")
    S.a(2, "1.2", "Ce cauze are deșertificarea în Sahel?", "secetele, pășunatul excesiv și tăierea arbuștilor", ["prea multe ploi", "ninsorile", "vulcanii"], "Solul rămas fără vegetație e luat de vânt.")
    S.a(2, "4.4", "Ce este „Marele Zid Verde”?", "un proiect de plantare a vegetației de-a lungul Sahelului, contra deșertificării", ["un zid de piatră", "un parc de distracții", "o autostradă"], "Se întinde de la Senegal la Djibouti.")
    S.s(2, "1.1", "Asociază tipul de deșert cu descrierea.", [("erg", "deșert de dune de nisip"), ("hamada", "deșert de piatră"), ("reg", "deșert de pietriș"), ("oază", "loc cu apă și vegetație")], "Peisajele Saharei.")
    S.a(2, "1.2", "Ce parte din Sahara e acoperită de dune de nisip?", "o parte mică; cea mai mare parte e piatră și pietriș", ["toată", "jumătate exact", "nimic"], "Imaginea „numai nisip” e greșită.")
    S.a(2, "3.3", "Ce plantă se cultivă în oazele Saharei?", "curmalul", ["molidul", "orezul", "cartoful"], "Curmalele sunt hrană de bază în deșert.")
    S.a(2, "3.3", "Ce resurse are Africa?", "petrol, aur, diamante, cupru, cobalt, cacao, cafea", ["doar nisip", "nicio resursă", "doar zăpadă"], "Africa e foarte bogată în resurse.")
    S.a(2, "3.3", "Ce țară africană e cel mai mare producător de cacao?", "Coasta de Fildeș", ["Egipt", "Algeria", "Libia"], "Și Ghana produce mult.")
    S.a(2, "3.3", "Ce metal important pentru bateriile telefoanelor și mașinilor electrice se extrage mult în R.D. Congo?", "cobaltul", ["aurul", "fierul", "staniul"], "Exploatarea ridică probleme de muncă și mediu.")
    S.p(2, "2.1", "Atinge pe hartă Sahelul, la marginea sudică a Saharei.", "lume", 15, 5, "Sahel", 800, "Sahelul traversează Africa de la vest la est.")
    S.p(3, "2.1", "Atinge pe hartă Munții Ahaggar (Hoggar), în centrul Saharei.", "lume", 23.3, 5.6, "Ahaggar", 500, "Ahaggar e în sudul Algeriei.")
    S.adev(2, "1.2", "Sahara a fost mereu un deșert, de milioane de ani, fără întrerupere.", False, "Fals: acum câteva mii de ani era mult mai verde.")
    S.adev(2, "3.3", "Telefonia mobilă și plățile prin telefon sunt foarte răspândite în multe țări africane.", True, "Adevărat: de exemplu, în Kenya.")
    S.l(2, "1.1", "Completează.", "Deșertul de dune se numește [erg]; locul cu apă din deșert se numește [oază].", ["hamada", "deltă"], "Erg, oază.")
    S.l(2, "4.4", "Completează.", "Transformarea terenurilor în deșert se numește [deșertificare]; ea e puternică în [Sahel].", ["urbanizare", "Congo"], "Deșertificare, Sahel.")
    S.g(3, "2.3 4.1", "Graficul arată suprafața împădurită într-o regiune imaginară din Sahel. Ce s-a întâmplat după începerea plantărilor?", grafic("profil", "Suprafața cu vegetație (regiune imaginară)", [("2000", 30), ("2008", 22), ("2012", 20), ("2018", 27), ("2024", 35)], "mii ha"), "vegetația a scăzut, apoi a crescut din nou", ["a scăzut mereu", "a crescut mereu", "nu s-a schimbat"], "După 2012, plantările au refăcut vegetația.")
    S.a(3, "4.3", "De ce o țară cu multe resurse poate rămâne săracă?", "dacă resursele sunt exportate brute, veniturile nu ajung la populație sau există conflicte", ["resursele fac mereu țara bogată", "pentru că nu are resurse", "fără motiv"], "Economiștii numesc asta „blestemul resurselor”.")
    S.a(2, "4.4", "Ce energie are un mare potențial în Sahara?", "energia solară", ["energia geotermală din gheață", "energia mareelor", "cărbunele"], "Sahara primește foarte mult soare.")
    S.a(2, "3.2", "Ce apă există sub Sahara?", "mari rezerve de apă subterană fosilă, acumulată demult", ["oceane subterane sărate", "ghețari", "nimic"], "Libia o aduce prin conducte uriașe.")
    S.a(2, "3.3", "Ce animal e folosit în Sahara pentru transport?", "dromaderul", ["elefantul", "calul", "renul"], "Dromaderul rezistă mult fără apă.")
    S.a(2, "3.4", "Ce desene vechi pe stâncă arată că Sahara a fost verde?", "picturile rupestre din Tassili n'Ajjer", ["piramidele", "hieroglifele de la Luxor", "statuile din Insula Paștelui"], "Arată girafe și elefanți.")
    S.a(3, "4.4", "Ce soluții ajută țările africane cu lipsă de apă?", "fântâni, colectarea apei de ploaie, irigații prin picurare, desalinizare", ["tăierea pădurilor", "consumul mai mare", "aruncarea deșeurilor în râuri"], "Fiecare picătură contează.")
    S.d(2, "2.1", "Ce țară din Sahel e marcată pe hartă?", "lume", 17, 9, "Niger", ["Nigeria", "Egipt", "Kenya"], "Nigerul e o țară din Sahel, fără ieșire la mare.")
    S.a(2, "3.3", "Ce înseamnă „comerț echitabil” (fair trade) pentru cacao și cafea?", "fermierii primesc un preț corect pentru produsele lor", ["produsele sunt gratuite", "fermierii nu primesc nimic", "produsele sunt interzise"], "Eticheta „fair trade” arată asta.")
    S.a(2, "3.2", "De ce în Sahara plouă foarte rar?", "este o zonă de presiune ridicată, cu aer care coboară și se încălzește, deci nu se formează nori", ["pentru că e prea frig", "pentru că e lângă ocean", "pentru că e muntoasă"], "Aerul descendent e uscat.")
    S.a(2, "4.4", "Ce poate face lumea pentru a ajuta Africa?", "parteneriate pentru educație, sănătate, energie curată și comerț corect", ["să ignore problemele", "să ia resursele fără plată", "să închidă școlile"], "Cooperarea aduce progres.")
    S.a(2, "3.3", "Ce organizație reunește statele africane?", "Uniunea Africană", ["Uniunea Europeană", "ASEAN", "NATO"], "Are sediul la Addis Abeba.", surse=S_UA)
    S.a(3, "4.3", "Compară Sahara cu Gobi.", "Sahara e un deșert fierbinte, tropical; Gobi e un deșert cu ierni geroase, în zona temperată", ["sunt identice", "Gobi e mai cald", "Sahara e în Asia"], "Deșerturile pot fi calde sau reci.")

    # ================================================================ S22 Expediție: un stat african
    E = Expeditie(7, "VII-S22-aplicatii-practice-studii-caz", "Expediție: safari geografic",
                  "Ce stat african ai vrea să cunoști și ce l-ar face unic?",
                  ref=REF.format("Aplicații practice/studii de caz: Caracterizarea geografică a unor state"))
    E.o(1, "4.1 3.1 4.2", "Ordonează pașii caracterizării unui stat.", ["poziția", "relieful", "clima și apele", "vegetația și fauna", "populația și orașele", "economia"], "Algoritmul", "De la natural la uman.")
    E.pas("1. Alege statul", "Alege un stat african: Egipt, Kenya, Africa de Sud, Maroc, Nigeria, Madagascar sau altul.")
    E.s(2, "4.4", "Asociază statul cu o problemă de mediu și o soluție.", [("Kenya", "braconaj → parcuri naționale și rangeri"), ("Niger", "deșertificare → plantări (Marele Zid Verde)"), ("Madagascar", "defrișări → arii protejate"), ("Egipt", "lipsa apei → irigații eficiente")], "Probleme și soluții.")
    E.pas("2. Natură și oameni", "Caracterizează statul după algoritm, cu atlasul și o sursă sigură. Notează sursa fiecărei cifre.",
          jurnal="Completează tabelul: capitală, relief, climă, râu, animal tipic, populație, o resursă.")
    E.a(2, "4.1", "De unde iei date de încredere despre populația unui stat african?", "ONU, Banca Mondială, institutul de statistică al țării", ["din comentarii anonime", "din reclame", "din jocuri"], "Datele trebuie să aibă sursă și an.")
    E.pas("3. Problema și soluția", "Alege o problemă de mediu sau socială a statului și propune o soluție.",
          jurnal="Scrie problema și soluția în 4–5 rânduri.")
    E.pas("4. Afișul", "Realizează un afiș sau o prezentare cu harta statului și 5 informații cheie.",
          jurnal="Fotografiază afișul.", foto=True)

    return Unitate(7, "u2-africa.json", "Africa").add(P, R, H, D, O, S, E)
