from autor import Lectie, Expeditie, Unitate, grafic

REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"
S_RPL = ["INS – Recensământul Populației și Locuințelor 2021: rezultate definitive (recensamantromania.ro)", "Wikipedia (ro) – Recensământul populației din 2021 (România)"]
S_EVOL = ["INS – recensămintele din 1930, 1956, 1966, 1977, 1992, 2002, 2011, 2021", "Wikipedia (ro) – Demografia României"]
S_ADM = ["INS – Anuarul Statistic al României: organizarea administrativă a teritoriului", "Legea nr. 2/1968 privind organizarea administrativă a teritoriului (cu modificările ulterioare)"]
S_REG = ["Ministerul Dezvoltării – Regiunile de dezvoltare (Legea nr. 315/2004)", "Eurostat – NUTS: Romania"]
S_ORASE = ["INS – RPL 2021: populația rezidentă pe municipii și orașe", "Fanatik.ro – cele mai populate 10 orașe din România (date RPL 2021)"]
RS = (45.38, 27.05)
BZ = (45.15, 26.82)


def unitate():
    # ================================================================ S21 Populația
    P = Lectie(8, "VIII-S21-populatia-elemente-structuri-demografice", "Populația României – elemente și structuri demografice",
               "De ce scade populația României?",
               [("Numărul populației", "La recensământul din 2021, România avea 19 053 815 locuitori, după INS. Populația a crescut până în jurul anului 1990 (peste 23 de milioane), apoi a scăzut, din cauza natalității mici și a emigrării.\nSporul natural e negativ din 1992: mor mai mulți oameni decât se nasc. Mulți români au emigrat pentru muncă, mai ales în Italia, Spania, Germania, Marea Britanie."),
                ("Densitatea și repartiția", "Densitatea medie e de aproximativ 80 loc./km². Populația e densă în București și în jurul marilor orașe, în Subcarpați, pe Valea Prahovei, în Câmpia Moldovei, și rară în Delta Dunării și în munții înalți."),
                ("Structuri demografice", "Structura pe sexe: puțin mai multe femei decât bărbați. Structura pe vârste: populația îmbătrânește – crește ponderea vârstnicilor.\nStructura etnică (din cei care au declarat etnia, RPL 2021): români aproximativ 89 %, maghiari aproximativ 6 %, romi aproximativ 3 %, apoi ucraineni, germani, turci, ruși-lipoveni, tătari și alții.\nStructura religioasă: majoritatea sunt ortodocși; urmează romano-catolicii, reformații, penticostalii, greco-catolicii și alții.")],
               stiaica="La recensământul din 2021 s-a putut răspunde, pentru prima dată, și online, de pe telefon sau calculator.",
               ref=REF.format("Populația – elemente și structuri demografice"))
    P.a(1, "2.3", "Câți locuitori avea România la recensământul din 2021?", "19 053 815 (aproximativ 19 milioane)", ["aproximativ 9 milioane", "aproximativ 23 de milioane", "aproximativ 190 de milioane"], "După INS.", surse=S_RPL)
    P.a(2, "1.2", "De ce scade populația României?", "natalitatea e mică și mulți oameni au emigrat", ["pentru că se nasc prea mulți copii", "pentru că vin mulți imigranți", "nu scade"], "Spor natural negativ și emigrare.")
    P.a(2, "1.2", "Din ce an e sporul natural negativ în România?", "din 1992", ["din 1950", "din 2020", "nu a fost niciodată negativ"], "Mor mai mulți decât se nasc.", surse=S_EVOL)
    P.a(2, "2.3", "Ce densitate medie are România?", "aproximativ 80 loc./km²", ["aproximativ 8 loc./km²", "aproximativ 800 loc./km²", "aproximativ 1 loc./km²"], "19 milioane : 238 de mii km².", surse=S_RPL)
    P.a(3, "2.3", "Calculează: 19 milioane de locuitori pe 238 de mii km². Ce densitate rezultă?", "aproximativ 80 loc./km²", ["aproximativ 8 loc./km²", "aproximativ 800 loc./km²", "aproximativ 12 loc./km²"], "19 000 000 : 238 000 ≈ 80.", ind="Împarte populația la suprafață.")
    P.a(2, "2.2", "Unde e cea mai mică densitate a populației?", "în Delta Dunării și în munții înalți", ["în București", "pe Valea Prahovei", "în Câmpia Moldovei"], "Condiții naturale restrictive.")
    P.a(2, "2.2", "Unde e cea mai mare densitate a populației?", "în București și în jurul marilor orașe", ["în Delta Dunării", "în Munții Retezat", "în Bărăgan"], "Concentrare urbană.")
    P.a(2, "1.1", "Ce înseamnă emigrare?", "plecarea oamenilor din țară pentru a trăi în altă țară", ["venirea străinilor în țară", "nașterea copiilor", "mutarea în alt cartier"], "Mulți români au emigrat după 1990.")
    P.a(2, "1.2", "În ce țări au emigrat cei mai mulți români?", "Italia, Spania, Germania, Marea Britanie", ["China, Japonia", "Brazilia, Argentina", "Australia, Noua Zeelandă"], "Țări ale Uniunii Europene, mai ales.")
    P.s(2, "1.1", "Asociază structura demografică cu ce arată.", [("pe sexe", "câți bărbați și câte femei"), ("pe vârste", "câți tineri, adulți, vârstnici"), ("etnică", "ce etnii declară oamenii"), ("religioasă", "ce religii declară oamenii")], "Structuri demografice.")
    P.a(2, "2.3", "Ce etnie e majoritară în România, după RPL 2021?", "română (aproximativ 89 % din cei care au declarat etnia)", ["maghiară", "germană", "turcă"], "Urmează maghiarii (≈6 %) și romii (≈3 %).", surse=S_RPL)
    P.a(2, "2.2", "Unde trăiesc mai ales maghiarii din România?", "în județele Harghita și Covasna și în alte zone din Transilvania", ["în Dobrogea", "în Oltenia", "în Bărăgan"], "Secuii sunt o comunitate de limbă maghiară.")
    P.a(2, "2.2", "Ce minorități trăiesc mai ales în Dobrogea?", "turcii, tătarii și lipovenii", ["secuii și sașii", "moții", "ceangăii"], "Dobrogea e o regiune multietnică.")
    P.a(2, "1.2", "Ce înseamnă că populația României „îmbătrânește”?", "crește ponderea vârstnicilor și scade ponderea copiilor", ["oamenii trăiesc mai puțin", "se nasc mai mulți copii", "toți sunt tineri"], "Efect al natalității mici.")
    P.adev(2, "1.2", "Populația României crește rapid în ultimii ani.", False, "Fals: scade, din 1990 încoace.", surse=S_EVOL)
    P.adev(2, "2.3", "În România trăiesc puțin mai multe femei decât bărbați.", True, "Adevărat: femeile au speranța de viață mai mare.", surse=S_RPL)
    P.l(2, "2.3", "Completează.", "La RPL 2021, România avea aproximativ [19] milioane de locuitori; sporul natural e [negativ].", ["23", "pozitiv"], "19 milioane, spor negativ.", surse=S_RPL)
    P.l(2, "1.1", "Completează.", "Plecarea din țară se numește [emigrare]; venirea în țară se numește [imigrare].", ["navetă", "urbanizare"], "Migrație externă.")
    P.g(3, "2.3", "Graficul arată populația României la recensăminte (milioane, valori rotunjite). Când a fost populația cea mai mare?", grafic("profil", "Populația României la recensăminte", [("1956", 17.5), ("1966", 19.1), ("1977", 21.6), ("1992", 22.8), ("2002", 21.7), ("2011", 20.1), ("2021", 19.1)], "milioane", "INS"), "în 1992 (dintre recensămintele din grafic)", ["în 1956", "în 2021", "în 2002"], "Apoi a scăzut.", surse=S_EVOL)
    P.g(3, "2.3 4.1", "Folosind graficul, cu cât a scăzut populația între 1992 și 2021?", grafic("profil", "Populația României la recensăminte", [("1956", 17.5), ("1966", 19.1), ("1977", 21.6), ("1992", 22.8), ("2002", 21.7), ("2011", 20.1), ("2021", 19.1)], "milioane", "INS"), "cu aproximativ 3,7 milioane", ["cu 1 milion", "cu 10 milioane", "a crescut"], "22,8 − 19,1 = 3,7.", surse=S_EVOL)
    P.a(3, "4.1", "Ce formă are piramida vârstelor în România azi?", "bază îngustă (puțini copii) și mijloc larg (mulți adulți)", ["bază foarte largă, ca în Africa", "triunghi perfect", "cerc"], "Populație îmbătrânită.")
    P.p(2, "2.1", "Atinge pe harta României județul Harghita, cu populație majoritar maghiară.", "romania", 46.5, 25.6, "Harghita", 50, "În estul Transilvaniei.")
    P.p(3, "2.1", "Atinge pe harta României Delta Dunării, cea mai slab populată regiune.", "romania", 45.1, 29.3, "Delta Dunării", 50, "Sub 10 loc./km².")
    P.d(2, "2.1", "Ce oraș, cu populația cea mai mare din țară, e marcat pe hartă?", "romania", 44.43, 26.1, "București", ["Ploiești", "Pitești", "Giurgiu"], "Capitala.")
    P.a(2, "1.2", "Ce instituție face recensămintele în România?", "Institutul Național de Statistică (INS)", ["Poliția", "Banca Națională", "Primăria"], "Recensământul se face o dată la 10 ani.")
    P.a(2, "1.2", "Ce înseamnă natalitate scăzută?", "se nasc puțini copii la 1 000 de locuitori", ["se nasc foarte mulți copii", "mor puțini oameni", "vin mulți imigranți"], "Natalitatea României e printre cele mai mici din UE.")
    P.a(3, "2.2", "Ce consecințe are emigrarea tinerilor?", "lipsa forței de muncă, îmbătrânirea populației, sate depopulate", ["creșterea natalității", "mai mulți copii la școală", "nicio consecință"], "Dar și bani trimiși acasă.")
    P.a(2, "1.2", "Ce religie e majoritară în România?", "creștin-ortodoxă", ["islamul", "budismul", "iudaismul"], "Urmată de romano-catolici și reformați.", surse=S_RPL)
    P.a(2, "2.2", "Ce comunitate germană istorică trăiește în sudul Transilvaniei?", "sașii", ["secuii", "lipovenii", "tătarii"], "Satele cu biserici fortificate sunt ale sașilor.")

    P.a(2, "1.1", "Ce este un recensământ?", "numărarea oficială a tuturor locuitorilor și locuințelor dintr-o țară", ["un sondaj de opinie", "o hartă", "un concurs"], "Se face o dată la 10 ani.")

    # ================================================================ S22 Așezările rurale
    R = Lectie(8, "VIII-S22-asezarile-rurale-evolutie-diferentieri", "Așezările rurale – evoluție și diferențieri",
               "Prin ce se deosebește un sat din Bărăgan de unul din Munții Apuseni?",
               [("Satele României", "În România sunt aproape 13 000 de sate, organizate în peste 2 800 de comune. Aproape jumătate din populație trăiește la sat.\nSatele sunt foarte vechi: multe sunt menționate în documente din Evul Mediu. În Transilvania se păstrează sate săsești cu biserici fortificate (Viscri, Biertan)."),
                ("Forme și mărimi", "După formă: sate adunate (case strânse, în câmpie – Bărăgan), răsfirate (case în grupuri, pe dealuri), risipite (case împrăștiate, la munte – Apuseni, Bran), liniare (de-a lungul unui drum sau al unei văi).\nSatele de câmpie sunt mari (mii de locuitori), cele de munte, mici."),
                ("Funcții", "Agricole (cereale, legume), pastorale (creșterea oilor – Mărginimea Sibiului), viticole și pomicole (pe dealuri), pescărești (în Deltă), forestiere (la munte), turistice (Bran, Sirnea, Botiza, Viscri – agroturism).\nProbleme: îmbătrânirea, plecarea tinerilor, lipsa unor servicii (medici, școli, transport). Avantaje: aer curat, tradiții, natură.")],
               stiaica="Sirnea, din Țara Bârsei, a fost primul sat turistic din România, declarat așa încă din 1968.",
               ref=REF.format("Așezările rurale – evoluție și diferențieri teritoriale"))
    R.a(1, "3.1", "Câte comune are România, aproximativ?", "peste 2 800", ["aproximativ 41", "aproximativ 300", "aproximativ 28 000"], "Cu aproape 13 000 de sate.", surse=S_ADM)
    R.s(2, "3.2", "Asociază forma satului cu relieful.", [("sat adunat", "câmpie (Bărăgan)"), ("sat risipit", "munte (Apuseni)"), ("sat răsfirat", "deal"), ("sat liniar", "vale sau drum")], "Relieful decide forma.")
    R.s(2, "3.3", "Asociază funcția satului cu un exemplu.", [("pescărească", "satele din Delta Dunării"), ("pastorală", "Mărginimea Sibiului"), ("turistică", "Bran, Sirnea"), ("viticolă", "satele de pe Dealu Mare")], "Funcțiile satelor.")
    R.a(2, "3.2", "Ce formă au de obicei satele din Bărăgan?", "adunată, cu case strânse și străzi drepte", ["risipită", "răsfirată pe dealuri", "pe stânci"], "Terenul plan permite asta.")
    R.a(2, "3.2", "Ce formă au de obicei satele din Munții Apuseni?", "risipită, cu case împrăștiate pe versanți", ["adunată", "liniară pe autostradă", "în blocuri"], "Fiecare gospodărie lângă terenul ei.")
    R.a(2, "3.4", "Ce sate din Transilvania au biserici fortificate în patrimoniul UNESCO?", "sate săsești, ca Viscri și Biertan", ["satele din Deltă", "satele din Bărăgan", "satele din Dobrogea"], "Construite de sași în Evul Mediu.", surse=["UNESCO World Heritage Centre – Villages with Fortified Churches in Transylvania", "Fundația Mihai Eminescu Trust – Viscri"])
    R.a(2, "3.4", "Care a fost primul sat turistic din România?", "Sirnea", ["Viscri", "Bran", "Botiza"], "Declarat în 1968.")
    R.a(2, "3.3", "Ce înseamnă agroturism?", "turism în gospodării rurale, cu cazare și mâncare tradițională", ["turism în orașe mari", "turism pe vapoare", "turism la fabrici"], "Bran, Moieciu, Maramureș, Bucovina.")
    R.a(2, "3.3", "Ce probleme au multe sate din România?", "îmbătrânirea, plecarea tinerilor, lipsa unor servicii", ["prea mulți copii", "trafic aglomerat", "prea multe fabrici"], "Depopulare rurală.")
    R.a(2, "3.3", "Ce avantaje are viața la sat?", "aer curat, liniște, natură, tradiții", ["trafic intens", "poluare industrială", "zgomot"], "Calitatea mediului.")
    R.p(2, "3.1", "Atinge pe harta României Viscri.", "romania", 46.05, 25.09, "Viscri", 35, "Viscri e în județul Brașov.")
    R.p(2, "3.1", "Atinge pe harta României Branul.", "romania", 45.52, 25.37, "Bran", 35, "Bran e între Bucegi și Piatra Craiului.")
    R.p(3, "3.1", "Atinge pe harta României Mărginimea Sibiului.", "romania", 45.7, 23.9, "Mărginimea Sibiului", 40, "La sud-vest de Sibiu.")
    R.adev(2, "3.2", "Satele de munte sunt de obicei mai mari decât satele de câmpie.", False, "Fals: satele de câmpie sunt mai mari.")
    R.adev(2, "3.3", "Aproape jumătate din populația României trăiește la sat.", True, "Adevărat, după RPL 2021.", surse=S_RPL)
    R.l(2, "3.2", "Completează.", "La câmpie satele sunt [adunate], iar la munte sunt [risipite].", ["liniare", "răsfirate"], "Formele satelor.")
    R.l(2, "3.4", "Completează.", "Satele cu biserici fortificate sunt tipice [sașilor], iar bisericile de lemn sunt tipice [Maramureșului].", ["secuilor", "Dobrogei"], "Patrimoniu rural.")
    R.g(3, "3.1", "Graficul arată populația a trei sate imaginare la două recensăminte. Ce sat s-a depopulat cel mai mult?", grafic("bare", "Populația satelor imaginare (2011 / 2021)", [("satul A 2011", 1200), ("satul A 2021", 1150), ("satul B 2011", 800), ("satul B 2021", 450), ("satul C 2011", 2500), ("satul C 2021", 2600)], "locuitori"), "satul B", ["satul A", "satul C", "niciunul"], "Satul B a pierdut aproape jumătate din locuitori.")
    R.a(3, "3.2", "De ce satele din jurul marilor orașe cresc, iar cele izolate scad?", "lângă orașe sunt locuri de muncă și servicii; satele izolate pierd tineri", ["satele izolate au mai multe școli", "orașele se mută la sat", "fără motiv"], "Suburbanizare.")
    R.d(2, "3.1", "Ce regiune cu biserici de lemn din patrimoniul UNESCO e marcată pe hartă?", "romania", 47.7, 24, "Maramureș", ["Bucovina", "Oltenia", "Dobrogea"], "Biserici de lemn cu turle înalte.")
    R.a(2, "3.3", "Ce ocupație au locuitorii satelor din Delta Dunării?", "pescuitul", ["mineritul", "creșterea renilor", "industria oțelului"], "Și recoltarea stufului, turismul.")
    R.a(2, "3.4", "Ce înseamnă transhumanță?", "mutarea turmelor de oi de la munte (vara) la câmpie sau în bălți (iarna)", ["mutarea satelor", "migrația păsărilor", "plecarea în străinătate"], "Tradiție pastorală veche.")
    R.a(3, "3.3", "Ce poate ajuta satele să-și păstreze tinerii?", "internet, drumuri bune, locuri de muncă, școli și dispensare", ["închiderea școlilor", "desființarea transportului", "nimic"], "Dezvoltare rurală.")
    R.a(2, "3.1", "Ce unitate administrativă cuprinde unul sau mai multe sate?", "comuna", ["județul", "municipiul", "regiunea"], "Comuna are primar și consiliu local.")
    R.a(2, "3.3", "Ce sat din Maramureș e cunoscut pentru „Cimitirul Vesel”?", "Săpânța", ["Viscri", "Sirnea", "Biertan"], "Crucile pictate în albastru cu versuri.")
    R.a(2, "3.3", "Ce funcție au satele de pe dealurile subcarpatice ale Buzăului?", "pomicole și viticole", ["pescărești", "miniere de aur", "portuare"], "Livezi și podgorii.")
    R.a(2, "3.2", "De ce satele vechi s-au format lângă izvoare și râuri?", "pentru apă de băut și pentru animale", ["pentru apărare de vulcani", "pentru că era obligatoriu", "fără motiv"], "Apa e esențială.")
    R.a(2, "3.4", "Ce muzeu din București prezintă case tradiționale din toată țara?", "Muzeul Național al Satului „Dimitrie Gusti”", ["Muzeul Țăranului Român doar cu picturi", "Muzeul de Istorie", "Muzeul Antipa"], "În Parcul Herăstrău.")
    R.a(2, "3.3", "Ce înseamnă depopulare?", "scăderea numărului de locuitori dintr-o localitate", ["creșterea populației", "construirea de case", "mutarea unui oraș"], "Frecventă în satele izolate.")

    R.a(2, "3.2", "Ce formă au satele de-a lungul unei văi înguste de munte?", "liniară", ["adunată", "circulară", "risipită pe câmpie"], "Casele urmează drumul și râul.")

    # ================================================================ S23 Așezările urbane
    U = Lectie(8, "VIII-S23-asezarile-urbane-evolutie-caracteristici", "Așezările urbane – evoluție și caracteristici",
               "Care e cel mai vechi oraș al României?",
               [("Evoluție", "Cele mai vechi orașe sunt cetățile grecești de pe țărmul Mării Negre (secolele VII–VI î.Hr.): Histria, Tomis (Constanța), Callatis (Mangalia). Romanii au întemeiat orașe ca Apulum (Alba Iulia), Napoca (Cluj), Drobeta.\nÎn Evul Mediu au apărut orașe-târguri și cetăți: Brașov, Sibiu, Sighișoara, Suceava, Iași, Târgoviște, București. Industrializarea din secolul XX a creat orașe noi și a mărit mult pe cele vechi."),
                ("Rețeaua urbană azi", "România are aproximativ 320 de orașe, dintre care 103 municipii. Puțin peste jumătate din populație trăiește la oraș.\nDupă București, cele mai mari orașe sunt (RPL 2021): Cluj-Napoca, Iași, Constanța, Timișoara, Brașov, Craiova, Galați – fiecare cu peste 200 000 de locuitori.\nRâmnicu Sărat și Buzău sunt municipii în județul Buzău."),
                ("Funcții și probleme", "Funcții: administrative (reședințe de județ), industriale (Pitești, Brașov), portuare (Constanța, Galați), universitare (Cluj, Iași), turistice (Sinaia, Mamaia), balneare (Băile Herculane, Sovata).\nProbleme: trafic, poluare, lipsa spațiilor verzi, extinderea necontrolată. Soluții: transport public, piste de biciclete, parcuri, zone metropolitane.")],
               stiaica="Histria, întemeiată de coloniști greci în secolul al VII-lea î.Hr., e considerată cel mai vechi oraș atestat de pe teritoriul României.",
               ref=REF.format("Așezările urbane – evoluție și caracteristici actuale"))
    U.a(1, "3.4", "Care e considerat cel mai vechi oraș atestat de pe teritoriul României?", "Histria", ["București", "Cluj-Napoca", "Râmnicu Sărat"], "Colonie grecească din secolul VII î.Hr.")
    U.s(2, "3.4", "Asociază numele antic cu orașul de azi.", [("Tomis", "Constanța"), ("Callatis", "Mangalia"), ("Napoca", "Cluj-Napoca"), ("Apulum", "Alba Iulia")], "Orașe antice.")
    U.a(2, "3.1", "Câte municipii are România?", "103", ["41", "320", "2 862"], "După INS.", surse=S_ADM)
    U.a(2, "3.1", "Care e cel mai mare oraș al României după București (RPL 2021)?", "Cluj-Napoca", ["Iași", "Constanța", "Timișoara"], "Aproximativ 287 000 de locuitori.", surse=S_ORASE)
    U.s(2, "3.3", "Asociază orașul cu funcția lui principală.", [("Constanța", "port maritim"), ("Pitești", "industrie de automobile"), ("Sinaia", "turism montan"), ("Băile Herculane", "balneară")], "Funcțiile orașelor.")
    U.p(2, "2.1", "Atinge pe harta României Cluj-Napoca.", "romania", 46.77, 23.6, "Cluj-Napoca", 30, "În nord-vestul Transilvaniei.")
    U.p(2, "2.1", "Atinge pe harta României Iași.", "romania", 47.16, 27.59, "Iași", 30, "În nord-estul țării.")
    U.p(2, "2.1", "Atinge pe harta României Brașov.", "romania", 45.66, 25.61, "Brașov", 30, "La curbura Carpaților.")
    U.p(3, "2.1", "Atinge pe harta României Craiova.", "romania", 44.32, 23.8, "Craiova", 30, "În Oltenia, pe Jiu.")
    U.p(3, "2.1", "Atinge pe harta României Histria.", "romania", 44.55, 28.77, "Histria", 35, "Pe malul Lacului Sinoe.")
    U.a(2, "3.2", "De ce multe orașe au crescut mult în secolul XX?", "industrializarea a atras oameni de la sate", ["s-au mutat orașele", "s-au născut mai mulți copii doar la oraș", "fără motiv"], "Urbanizare rapidă.")
    U.a(2, "3.3", "Ce orașe sunt mari centre universitare?", "Cluj-Napoca, Iași, București, Timișoara", ["Sulina, Vama Veche", "Bran, Sirnea", "Săpânța, Viscri"], "Universități vechi și mari.")
    U.a(2, "3.1", "Ce rang administrativ are Râmnicu Sărat?", "municipiu", ["comună", "sat", "capitală de județ"], "Reședința județului e municipiul Buzău.")
    U.adev(2, "3.1", "Puțin peste jumătate din populația României trăiește la oraș.", True, "Adevărat, după RPL 2021.", surse=S_RPL)
    U.adev(2, "3.4", "Bucureștiul e cel mai vechi oraș al României.", False, "Fals: e atestat documentar din 1459; Histria e mult mai veche.")
    U.l(2, "3.4", "Completează.", "Constanța de azi se numea în Antichitate [Tomis], iar Mangalia se numea [Callatis].", ["Napoca", "Apulum"], "Cetăți grecești.")
    U.l(2, "3.1", "Completează.", "România are [103] municipii; cel mai mare oraș după București este [Cluj-Napoca].", ["41", "Iași"], "Rețeaua urbană.", surse=S_ADM)
    U.g(3, "2.3", "Graficul arată populația marilor orașe (RPL 2021, mii locuitori, rotunjit). Ce oraș e pe locul al doilea în grafic?", grafic("bare", "Populația orașelor mari (RPL 2021, rotunjit)", [("Cluj-Napoca", 287), ("Iași", 272), ("Constanța", 264), ("Timișoara", 251), ("Brașov", 238), ("Craiova", 234)], "mii", "INS – RPL 2021"), "Iași", ["Timișoara", "Constanța", "Craiova"], "Cluj, Iași, Constanța, Timișoara, Brașov, Craiova.", surse=S_ORASE)
    U.o(3, "2.2", "Ordonează orașele după vechimea atestării, de la cel mai vechi.", ["Histria (sec. VII î.Hr.)", "Apulum (sec. II d.Hr.)", "Brașov (sec. XIII)", "București (1459)"], "Cronologic", "Greci, romani, Ev Mediu.")
    U.a(3, "4.2", "Compară un oraș industrial cu un oraș turistic.", "orașul industrial are fabrici și cartiere de muncitori; orașul turistic are hoteluri și obiective de vizitat", ["sunt identice", "orașul turistic are mai multe fabrici", "orașul industrial nu are locuitori"], "Funcții diferite.")
    U.d(2, "2.1", "Ce oraș-port de pe Dunăre e marcat pe hartă?", "romania", 45.44, 28.05, "Galați", ["Brăila", "Tulcea", "Giurgiu"], "Galați are cel mai mare șantier naval.")
    U.a(2, "4.4", "Ce soluții are un oraș pentru traficul aglomerat?", "transport public, piste de biciclete, parcări la marginea orașului", ["mai multe mașini în centru", "închiderea autobuzelor", "tăierea copacilor"], "Mobilitate urbană.")
    U.a(2, "3.3", "Ce este o zonă metropolitană?", "un oraș mare și localitățile din jur, legate prin navetă și servicii", ["un sat izolat", "un parc", "o insulă"], "Ex.: zona metropolitană Cluj, Iași.")
    U.a(2, "3.4", "Ce oraș medieval transilvănean a fost Capitală Culturală Europeană în 2007?", "Sibiu", ["Buzău", "Constanța", "Galați"], "Timișoara a fost în 2023.")
    U.a(2, "3.4", "Ce oraș românesc a fost Capitală Europeană a Culturii în 2023?", "Timișoara", ["Iași", "Cluj-Napoca", "Craiova"], "Al doilea oraș românesc, după Sibiu.")
    U.a(2, "3.3", "Ce funcție are municipiul Buzău?", "reședință de județ, centru administrativ, industrial și comercial", ["stațiune montană", "port maritim", "sat pescăresc"], "Buzău e reședința județului Buzău.")
    U.a(2, "3.2", "De ce Brașov s-a dezvoltat ca centru comercial medieval?", "era la intersecția drumurilor comerciale prin trecătorile Carpaților", ["era la mare", "era în deltă", "era pe un vulcan"], "Poziție strategică.")
    U.a(2, "3.3", "Ce înseamnă „spații verzi” în oraș?", "parcuri, grădini, scuaruri cu vegetație", ["parcări", "fabrici", "autostrăzi"], "Îmbunătățesc calitatea vieții.")
    U.a(3, "3.2", "De ce unele orașe mici, foste centre miniere, au pierdut populație?", "minele s-au închis și oamenii au plecat să caute muncă", ["s-au născut prea mulți copii", "au devenit capitale", "s-a mutat marea"], "Ex.: orașele din Valea Jiului.")

    U.a(2, "3.1", "Ce oraș, al treilea după populație (RPL 2021), e cel mai mare port?", "Constanța", ["Galați", "Brăila", "Tulcea"], "Aproximativ 264 000 de locuitori.", surse=S_ORASE)

    # ================================================================ S24 București
    B = Lectie(8, "VIII-S24-caracterizarea-geografica-orasului-bucuresti", "Caracterizarea geografică a orașului București",
               "Cum a devenit Bucureștiul capitala României?",
               [("Poziție și cadru natural", "Bucureștiul e în sud-estul țării, în Câmpia Română (Câmpia Vlăsiei), pe râurile Dâmbovița și Colentina. Altitudinea e mică (aproximativ 60–90 m). Climă de câmpie, cu veri calde și ierni geroase.\nÎn trecut era înconjurat de Codrii Vlăsiei; azi are lacuri (salba de lacuri pe Colentina: Herăstrău, Floreasca, Tei) și parcuri (Cișmigiu, Herăstrău – Parcul Regele Mihai I)."),
                ("Istorie și populație", "E atestat documentar din 1459, într-un act al lui Vlad Țepeș. A devenit capitala Țării Românești, apoi a Principatelor Unite (1862) și a României.\nLa RPL 2021 avea aproximativ 1,7 milioane de locuitori, de aproape șase ori mai mult decât următorul oraș. E împărțit în 6 sectoare."),
                ("Funcții", "Centru politic și administrativ (Parlamentul, Guvernul, Președinția), economic (bănci, companii, IT), universitar, cultural (Ateneul Român, muzee, teatre), nod de transport (Gara de Nord, aeroportul Henri Coandă, autostrăzi, metrou).\nProbleme: trafic, poluare, lipsa spațiilor verzi pe cap de locuitor, risc seismic ridicat.")],
               stiaica="Palatul Parlamentului din București e una dintre cele mai mari clădiri administrative din lume.",
               ref=REF.format("Caracterizarea geografică a orașului București"))
    B.a(1, "2.1", "Pe ce râu e așezat Bucureștiul?", "Dâmbovița (și Colentina)", ["Oltul", "Mureșul", "Siretul"], "Dâmbovița traversează centrul.")
    B.a(2, "2.1", "În ce unitate de relief se află Bucureștiul?", "Câmpia Română (Câmpia Vlăsiei)", ["Podișul Getic", "Subcarpați", "Carpați"], "Altitudine de aproximativ 60–90 m.")
    B.a(2, "3.4", "În ce an e atestat documentar Bucureștiul?", "1459", ["1918", "1862", "1600"], "Într-un act al lui Vlad Țepeș.")
    B.a(2, "3.4", "Din ce an e Bucureștiul capitala Principatelor Unite?", "1862", ["1459", "1918", "2007"], "După Unirea din 1859.")
    B.a(2, "3.1", "Câți locuitori avea Bucureștiul la RPL 2021?", "aproximativ 1,7 milioane", ["aproximativ 170 000", "aproximativ 17 milioane", "aproximativ 700 000"], "Aproape 1,72 milioane, după INS.", surse=S_ORASE)
    B.a(2, "3.1", "În câte sectoare e împărțit Bucureștiul?", "6", ["2", "10", "41"], "Fiecare are primărie de sector.")
    B.s(2, "3.3", "Asociază funcția Bucureștiului cu un exemplu.", [("politică", "Parlamentul și Guvernul"), ("culturală", "Ateneul Român"), ("de transport", "Gara de Nord și aeroportul Henri Coandă"), ("universitară", "Universitatea din București")], "Funcțiile capitalei.")
    B.a(2, "3.3", "Ce lacuri formează o salbă pe râul Colentina?", "Herăstrău, Floreasca, Tei și altele", ["Bucura, Zănoaga", "Razim, Sinoe", "Vidraru, Bicaz"], "Lacuri amenajate.")
    B.a(2, "3.4", "Ce clădire din București e una dintre cele mai mari clădiri administrative din lume?", "Palatul Parlamentului", ["Ateneul Român", "Gara de Nord", "Arcul de Triumf"], "Construit în anii 1980.")
    B.a(2, "3.4", "Ce sală de concerte e simbolul culturii Bucureștiului?", "Ateneul Român", ["Palatul Parlamentului", "Arena Națională", "Casa Presei"], "Inaugurat în 1888.")
    B.p(2, "2.1", "Atinge pe harta României Bucureștiul.", "romania", 44.43, 26.1, "București", 30, "În sud-estul țării.")
    B.p(3, "2.1", "Atinge pe harta României aeroportul Henri Coandă (Otopeni).", "romania", 44.57, 26.08, "Otopeni", 25, "La nord de București.")
    B.a(2, "3.3", "Ce risc natural e important pentru București?", "cutremurele (din zona Vrancea)", ["erupțiile vulcanice", "tsunami-urile", "avalanșele"], "Cutremurul din 4 martie 1977 a produs pagube mari.")
    B.a(2, "4.4", "Ce problemă de mediu are Bucureștiul?", "poluarea aerului și traficul", ["avalanșele de zăpadă", "lipsa totală de apă", "vulcanii"], "Transportul public și spațiile verzi ajută.")
    B.adev(2, "3.1", "Bucureștiul are de câteva ori mai mulți locuitori decât oricare alt oraș al României.", True, "Adevărat: de aproape șase ori mai mult decât Clujul.", surse=S_ORASE)
    B.adev(2, "2.1", "Bucureștiul e situat în Subcarpați.", False, "Fals: e în Câmpia Română.")
    B.l(2, "3.4", "Completează.", "Bucureștiul e atestat documentar în anul [1459]; e împărțit în [6] sectoare.", ["1862", "41"], "Istorie și organizare.")
    B.l(2, "3.3", "Completează.", "Cel mai mare aeroport al țării se numește [Henri Coandă]; cea mai mare gară e [Gara de Nord].", ["Traian Vuia", "Gara Basarab"], "Noduri de transport.")
    B.g(3, "2.3", "Graficul compară populația Bucureștiului cu a altor orașe (RPL 2021, mii, rotunjit). De câte ori e mai mare Bucureștiul decât Clujul?", grafic("bare", "Populația (RPL 2021, mii, rotunjit)", [("București", 1717), ("Cluj-Napoca", 287), ("Iași", 272), ("Oradea", 183)], "mii", "INS – RPL 2021"), "de aproximativ 6 ori", ["de 2 ori", "de 20 de ori", "la fel"], "1 717 : 287 ≈ 6.", surse=S_ORASE)
    B.a(3, "4.2", "Compară Bucureștiul cu Clujul.", "Bucureștiul e capitala, mult mai mare, în câmpie; Clujul e în Transilvania, între dealuri, mare centru universitar și IT", ["sunt identice", "Clujul e capitala", "Bucureștiul e la munte"], "Poziții și funcții.")
    B.d(2, "2.1", "Ce județ înconjoară Bucureștiul?", "romania", 44.5, 26.05, "Ilfov", ["Giurgiu", "Prahova", "Ialomița"], "Bucureștiul și Ilfov formează o regiune de dezvoltare.")
    B.a(2, "3.3", "Ce mijloc de transport public subteran are Bucureștiul?", "metroul", ["telefericul", "vaporașul", "tramvaiul subteran pe apă"], "Primul tronson s-a deschis în 1979.")
    B.a(2, "3.4", "Ce muzeu de științele naturii poartă numele unui mare naturalist român?", "Muzeul „Grigore Antipa”", ["Muzeul Satului", "Muzeul Țăranului", "Muzeul Enescu"], "Diorame cu animale din toată lumea.")
    B.a(2, "3.3", "De ce Bucureștiul e cel mai important nod de transport al țării?", "aici se întâlnesc autostrăzi, căi ferate, aeroportul cel mai mare", ["are port maritim", "e la munte", "e în deltă"], "Toate drumurile principale pornesc din capitală.")
    B.a(2, "3.3", "Ce autostradă leagă Bucureștiul de Constanța?", "A2 (Autostrada Soarelui)", ["A1", "A3", "A10"], "A1 merge spre Pitești.")
    B.a(2, "3.4", "Ce monument din București amintește de Marea Unire și de victoria din Primul Război Mondial?", "Arcul de Triumf", ["Ateneul Român", "Palatul Parlamentului", "Turnul Chindiei"], "Refăcut în piatră în 1936.")
    B.a(2, "3.3", "Ce parc mare din București are un lac și Muzeul Satului?", "Parcul Regele Mihai I (Herăstrău)", ["Cișmigiu", "Parcul Tineretului", "Grădina Botanică"], "Pe malul lacului Herăstrău.")
    B.a(3, "4.4", "De ce clădirile vechi din București trebuie consolidate?", "orașul e expus cutremurelor puternice din Vrancea", ["din cauza inundațiilor din mare", "din cauza vulcanilor", "din cauza ghețarilor"], "Clădirile cu bulină roșie sunt cu risc seismic.")
    B.a(2, "3.3", "Ce domeniu economic modern s-a dezvoltat mult în București?", "IT-ul și serviciile financiare", ["mineritul cărbunelui", "pescuitul", "creșterea oilor"], "Multe companii au sedii în capitală.")

    B.a(2, "2.1", "Ce râu formează o salbă de lacuri în nordul Bucureștiului?", "Colentina", ["Dâmbovița", "Argeș", "Ialomița"], "Lacurile Herăstrău, Floreasca, Tei.")

    # ================================================================ S25 Organizarea administrativ-teritorială
    A = Lectie(8, "VIII-S25-organizarea-administrativ-teritoriala", "Organizarea administrativ-teritorială",
               "Ce e un județ și ce e o regiune de dezvoltare?",
               [("Unitățile administrative", "Teritoriul României e împărțit în 41 de județe și municipiul București. Județele sunt formate din municipii, orașe și comune; comunele sunt formate din sate.\nFiecare județ are o reședință (de exemplu, municipiul Buzău pentru județul Buzău), un Consiliu Județean și un prefect. Fiecare localitate are primar și consiliu local."),
                ("Regiunile de dezvoltare", "Pentru dezvoltare și fonduri europene, județele sunt grupate în 8 regiuni de dezvoltare: Nord-Est, Sud-Est, Sud-Muntenia, Sud-Vest Oltenia, Vest, Nord-Vest, Centru și București-Ilfov. Ele nu sunt unități administrative.\nJudețul Buzău face parte din Regiunea Sud-Est, alături de Brăila, Constanța, Galați, Tulcea și Vrancea."),
                ("Regiunile istorice", "Tradițional, România are regiuni istorice: Muntenia, Oltenia, Moldova, Transilvania, Banat, Crișana, Maramureș, Dobrogea, Bucovina.\nJudețul Buzău e în nord-estul Munteniei, la granița istorică cu Moldova.")],
               stiaica="Județul Buzău e singurul județ cu un muzeu al chihlimbarului (la Colți) și cu vulcani noroioși care sunt rezervație naturală (Berca–Pâclele).",
               ref=REF.format("Organizarea administrativ-teritorială"))
    A.a(1, "1.1", "Câte județe are România?", "41 (plus municipiul București)", ["27", "8", "100"], "București are statut special.", surse=S_ADM)
    A.a(2, "1.1", "Ce unități administrative formează un județ?", "municipii, orașe și comune", ["doar sate", "regiuni de dezvoltare", "state"], "Comunele sunt formate din sate.", surse=S_ADM)
    A.a(2, "1.1", "Câte regiuni de dezvoltare are România?", "8", ["41", "6", "12"], "Pentru planificare și fonduri europene.", surse=S_REG)
    A.a(2, "2.1", "Din ce regiune de dezvoltare face parte județul Buzău?", "Sud-Est", ["Nord-Est", "Centru", "Vest"], "Alături de Brăila, Constanța, Galați, Tulcea, Vrancea.", surse=S_REG)
    A.a(2, "2.1", "Care e reședința județului Buzău?", "municipiul Buzău", ["Râmnicu Sărat", "Nehoiu", "Pogoanele"], "Râmnicu Sărat e al doilea municipiu al județului.")
    A.s(2, "2.1", "Asociază județul cu reședința lui.", [("Prahova", "Ploiești"), ("Vrancea", "Focșani"), ("Brăila", "Brăila"), ("Ialomița", "Slobozia")], "Județele din jurul Buzăului.")
    A.s(2, "2.1", "Asociază județul cu reședința lui.", [("Argeș", "Pitești"), ("Dolj", "Craiova"), ("Mureș", "Târgu Mureș"), ("Suceava", "Suceava")], "Alte reședințe.")
    A.s(2, "1.2", "Asociază instituția cu nivelul ei.", [("primarul", "localitate"), ("Consiliul Județean", "județ"), ("prefectul", "reprezentantul Guvernului în județ"), ("Guvernul", "țară")], "Administrația publică.")
    A.a(2, "1.2", "Ce sunt regiunile de dezvoltare?", "grupări de județe pentru planificare și fonduri europene, fără să fie unități administrative", ["unități administrative cu primar", "noi state", "zone militare"], "Corespund nivelului NUTS 2 din UE.", surse=S_REG)
    A.e(2, "2.1", "Pune pe hartă regiunile istorice.", [("tr", "Transilvania", 46.5, 24.5), ("mo", "Moldova", 47, 27), ("mu", "Muntenia", 44.6, 26), ("ol", "Oltenia", 44.4, 23.5), ("do", "Dobrogea", 44.4, 28.4), ("ba", "Banat", 45.4, 21.5)], "Regiunile istorice ale României.", harta="romania")
    A.p(2, "2.1", "Atinge pe harta României județul Buzău.", "romania", 45.25, 26.75, "județul Buzău", 50, "În nord-estul Munteniei.")
    A.p(3, "2.1", "Atinge pe harta României Focșani, reședința Vrancei.", "romania", 45.7, 27.18, "Focșani", 30, "Vecin la nord cu Râmnicu Sărat.")
    A.adev(2, "1.2", "Regiunile de dezvoltare au primari și consilii proprii, ca județele.", False, "Fals: nu sunt unități administrative.", surse=S_REG)
    A.adev(2, "2.1", "Râmnicu Sărat e un municipiu din județul Buzău.", True, "Adevărat.")
    A.l(2, "1.1", "Completează.", "România are [41] de județe și municipiul București; ele sunt grupate în [8] regiuni de dezvoltare.", ["27", "6"], "Organizarea teritoriului.", surse=S_ADM)
    A.l(2, "2.1", "Completează.", "Județul Buzău e în regiunea istorică [Muntenia] și în regiunea de dezvoltare [Sud-Est].", ["Moldova", "Centru"], "Buzău.", surse=S_REG)
    A.g(3, "2.3", "Graficul arată numărul de unități administrative (INS). Ce fel de unitate e cea mai numeroasă?", grafic("bare", "Unități administrativ-teritoriale (INS)", [("județe", 41), ("municipii", 103), ("orașe", 216), ("comune", 2862)], "număr", "INS – Anuarul Statistic"), "comuna", ["județul", "municipiul", "orașul"], "Peste 2 800 de comune.", surse=S_ADM)
    A.o(3, "1.2", "Ordonează unitățile de la cea mai mică la cea mai mare.", ["satul", "comuna", "județul", "regiunea de dezvoltare", "țara"], "De la mic la mare", "Ierarhia teritorială.")
    A.a(3, "4.2", "Compară județul cu regiunea de dezvoltare.", "județul e unitate administrativă, cu instituții proprii; regiunea grupează județe pentru dezvoltare, fără administrație proprie", ["sunt identice", "regiunea e mai mică", "județul nu are instituții"], "Diferențe de rol.")
    A.d(2, "2.1", "Ce reședință de județ, vecină la sud-est cu Buzău, e marcată pe hartă?", "romania", 45.27, 27.96, "Brăila", ["Galați", "Slobozia", "Focșani"], "Brăila e pe Dunăre.")
    A.a(2, "2.1", "Ce județe se învecinează cu județul Buzău?", "Prahova, Brașov, Covasna, Vrancea, Brăila, Ialomița", ["Cluj, Bihor", "Dolj, Olt", "Suceava, Botoșani"], "Buzău are șase vecini.")
    A.a(2, "1.2", "Ce înseamnă reședință de județ?", "orașul (municipiul) în care se află conducerea județului", ["cel mai mic sat", "orice comună", "capitala țării"], "Ex.: Buzău pentru județul Buzău.")
    A.a(2, "2.1", "Ce regiune istorică se află între Dunăre și Marea Neagră?", "Dobrogea", ["Banatul", "Oltenia", "Crișana"], "Județele Constanța și Tulcea.")
    A.a(2, "2.1", "Ce regiune istorică se află la vest de Olt, în sud?", "Oltenia", ["Muntenia", "Moldova", "Dobrogea"], "Oltul desparte Oltenia de Muntenia.")
    A.a(2, "2.1", "Ce regiune de dezvoltare e cea mai mică ca suprafață?", "București-Ilfov", ["Nord-Est", "Sud-Est", "Centru"], "Doar capitala și județul Ilfov.", surse=S_REG)
    A.a(2, "1.2", "La ce servesc fondurile europene pentru regiuni?", "la construirea de drumuri, spitale, școli, rețele de apă", ["la cumpărarea de arme", "la nimic", "doar la turism"], "Reduc diferențele dintre regiuni.")
    A.a(3, "2.2", "De ce Regiunea Nord-Est e considerată mai puțin dezvoltată?", "are venituri mai mici, populație rurală numeroasă și infrastructură mai slabă", ["are prea multe fabrici", "e la mare", "e capitala"], "Diferențe regionale.")
    A.a(2, "2.1", "Ce râu desparte istoric Muntenia de Moldova, aproape de Buzău?", "Milcovul", ["Oltul", "Dâmbovița", "Ialomița"], "Focșaniul e pe Milcov.")
    A.a(2, "1.2", "Ce înseamnă „prefect”?", "reprezentantul Guvernului într-un județ", ["primarul unui sat", "un profesor", "un deputat european"], "Prefectura veghează legalitatea.")

    A.a(2, "2.1", "Ce oraș e reședința județului Ilfov?", "Buftea", ["București", "Otopeni", "Voluntari"], "Ilfov înconjoară Bucureștiul.")

    # ================================================================ S27 Expediție: populația județului
    X = Expeditie(8, "VIII-S27-aplicatii-practice-studii-caz", "Expediție: populația județului meu",
                  "Cum s-a schimbat populația județului Buzău și a orașului Râmnicu Sărat?",
                  ref=REF.format("Aplicații practice/studii de caz: grafice și hărți despre populația României"))
    X.a(1, "4.1", "De unde iei date oficiale despre populația județului Buzău?", "de la INS (recensămintele și baza de date TEMPO)", ["de pe rețele sociale", "din reclame", "din jocuri"], "Datele trebuie să aibă sursă și an.")
    X.pas("1. Datele", "Cu profesorul, caută pe site-ul INS populația județului Buzău și a orașului Râmnicu Sărat la recensămintele din 2002, 2011 și 2021.",
          jurnal="Notează valorile în tabel: anul, populația județului, populația orașului.")
    X.a(2, "4.2", "Ce grafic e potrivit pentru evoluția populației în timp?", "graficul liniar", ["harta politică", "diagrama de structură", "profilul de relief"], "Linia arată creșterea sau scăderea.")
    X.pas("2. Graficul", "Desenează un grafic liniar cu evoluția populației orașului Râmnicu Sărat.",
          jurnal="Fotografiază graficul.", foto=True)
    X.a(2, "4.2", "Ce grafic e potrivit pentru structura pe vârste?", "piramida vârstelor", ["graficul liniar al temperaturii", "harta fizică", "profilul geologic"], "Arată câți oameni sunt în fiecare grupă de vârstă, pe sexe.")
    X.a(3, "4.2", "O piramidă a vârstelor are baza îngustă și vârful lat. Ce înseamnă?", "se nasc puțini copii și sunt mulți vârstnici", ["se nasc mulți copii", "populația e foarte tânără", "nu sunt vârstnici"], "Populație îmbătrânită.")
    X.pas("3. Interpretarea", "Scrie 3 concluzii: populația a crescut sau a scăzut? De ce crezi? Ce consecințe are pentru oraș?",
          jurnal="Scrie concluziile.")
    X.pas("4. Harta densității", "Pe harta județului Buzău, colorează comunele după densitatea populației (date de la profesor), cu o legendă de 3 culori.",
          jurnal="Fotografiază harta și explică legenda.", foto=True)

    return Unitate(8, "u4-populatie.json", "Populația, așezările omenești și organizarea administrativ-teritorială").add(P, R, U, B, A, X)
