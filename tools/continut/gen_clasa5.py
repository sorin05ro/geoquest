import json, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from gen_common import *

V8 = "V-S08-orientarea-spatiul-terestru-elemente"
V9 = "V-S09-aplicatii-practice-masurarea-timpului"
V10 = "V-S10-caracteristici-generale-importanta"
V11 = "V-S11-structura-interna-terrei"
V12 = "V-S12-relieful-continente-bazine-oceanice"
V13 = "V-S13-vulcanii-cutremurele"
V16 = "V-S16-aplicatii-practice-relieful-orizontului"
REF = "Manual Art Klett, clasa a V-a (manuale.edu.ro), lecția „{}”"

# ============================================================ S8 Orientarea
n8 = {
 "id": V8, "tip": "nivel", "titlu": "Orientarea în spațiul terestru",
 "descopera": {"intrebare": "Te-ai rătăcit într-o pădure, fără telefon. E prânz și e senin. Cum afli în ce parte e sudul?", "schema": "busola"},
 "invata": [
  {"titlu": "Punctele cardinale", "schema": "busola",
   "text": "Ne orientăm după patru puncte cardinale: nord (N), sud (S), est (E) și vest (V).\nÎntre ele sunt punctele intermediare: nord-est (NE), sud-est (SE), sud-vest (SV) și nord-vest (NV). Pe hărți, nordul este de obicei sus."},
  {"titlu": "Cum ne orientăm",
   "text": "După Soare: răsare în partea de est și apune în partea de vest. La prânz, în România, Soarele e spre sud, iar umbrele arată spre nord.\nNoaptea, Steaua Polară arată nordul.\nCu instrumente: busola are un ac magnetic care se îndreaptă spre nord. Sistemul GPS din telefon îți află poziția folosind semnale de la sateliți."},
 ],
 "stiaiCa": "Steaua Polară pare să stea pe loc toată noaptea, în timp ce celelalte stele se rotesc în jurul ei. De aceea marinarii o foloseau ca reper.",
 "referintaProfesor": REF.format("Orientarea în spațiul terestru"),
}
c8 = ["V-1.1", "V-2.1", "V-4.3"]
i8 = [
 alegere("V8-01", V8, ["V-1.1"], 1, "Care sunt cele patru puncte cardinale?",
   ["nord, sud, est, vest", "sus, jos, stânga, dreapta", "nord-est, sud-est, sud-vest, nord-vest", "înainte, înapoi, stânga, dreapta"],
   "Nord, sud, est și vest sunt punctele cardinale.", "Punctele cardinale sunt nord, sud, est și vest. Cele cu cratimă (nord-est...) sunt intermediare."),
 etichete("V8-02", V8, ["V-1.1", "V-2.1"], 1, "Pune punctele cardinale pe roza vânturilor.",
   [{"id": "N", "eticheta": "Nord"}, {"id": "E", "eticheta": "Est"}, {"id": "S", "eticheta": "Sud"}, {"id": "V", "eticheta": "Vest"}],
   "Exact: nordul sus, sudul jos, estul la dreapta, vestul la stânga.", "Nordul e sus. Dacă privești spre nord, estul e la dreapta și vestul la stânga.", schema="busola",
   indiciu="Nordul e aproape mereu sus pe hartă."),
 etichete("V8-03", V8, ["V-2.1"], 2, "Pune punctele intermediare pe roza vânturilor.",
   [{"id": "NE", "eticheta": "Nord-est"}, {"id": "SE", "eticheta": "Sud-est"}, {"id": "SV", "eticheta": "Sud-vest"}, {"id": "NV", "eticheta": "Nord-vest"}],
   "Bravo! Punctul intermediar stă între cele două puncte cardinale din numele lui.", "Nord-estul e între nord și est; sud-vestul, între sud și vest.", schema="busola",
   indiciu="Citește numele: „nord-est” înseamnă între nord și est."),
 alegere("V8-04", V8, ["V-1.2"], 1, "Spre ce punct cardinal se îndreaptă acul magnetic al busolei?",
   ["spre nord", "spre sud", "spre est", "spre locul unde stai tu"],
   "Acul busolei e atras spre nordul magnetic.", "Capătul colorat al acului busolei arată spre nord."),
 lacunar("V8-05", V8, ["V-1.1"], 1, "Completează propozițiile.",
   "Soarele răsare în partea de {0} și apune în partea de {1}.", ["est", "vest"], ["nord", "sud"],
   "Corect: răsare la est, apune la vest.", "Soarele răsare în partea de est și apune în partea de vest."),
 alegere("V8-06", V8, ["V-2.1", "V-4.3"], 2, "Este ora prânzului, în România. Spre ce punct cardinal arată umbra unui băț înfipt în pământ?",
   ["spre nord", "spre sud", "spre est", "spre vest"],
   "La prânz Soarele e spre sud, deci umbra cade spre nord.", "La prânz, în România, Soarele e spre sud. Umbra cade în partea opusă: spre nord.", schema=None,
   indiciu="Umbra cade mereu în partea opusă Soarelui."),
 alegere("V8-07", V8, ["V-1.2"], 2, "Noaptea, ce stea te ajută să găsești nordul?",
   ["Steaua Polară", "Soarele", "Luna", "orice stea strălucitoare"],
   "Steaua Polară arată nordul.", "Steaua Polară, din constelația Carul Mic, arată direcția nord."),
 ordoneaza("V8-08", V8, ["V-2.1", "V-4.3"], 2, "Ordonează pașii pentru orientarea cu busola.",
   ["Ții busola orizontal, departe de obiecte de fier", "Aștepți să se oprească acul", "Rotești busola până când capătul colorat al acului ajunge în dreptul literei N", "Citești direcția în care vrei să mergi"],
   "Ordinea pașilor", "Perfect! Așa se folosește busola.", "Întâi ții busola orizontal și aștepți acul, apoi potrivești N cu acul și abia la final citești direcția."),
 asociaza("V8-09", V8, ["V-1.1", "V-2.1"], 2, "Asociază fiecare instrument cu ce face.",
   [["Busola", "arată direcția nord"], ["GPS-ul", "îți află poziția cu ajutorul sateliților"], ["Harta", "reprezintă micșorat un teritoriu"], ["Roza vânturilor", "arată punctele cardinale pe hartă"]],
   "Toate perechile sunt corecte.", "Busola arată nordul; GPS-ul îți află poziția; harta e un desen micșorat al unui teritoriu; roza vânturilor arată direcțiile."),
 alegere("V8-10", V8, ["V-2.1", "V-4.3"], 3, "Mergi spre est. Te întorci la stânga. Spre ce punct cardinal mergi acum?",
   ["nord", "sud", "vest", "sud-est"],
   "Da: cu fața spre est, stânga ta e nordul.", "Cu fața spre est, ai nordul la stânga și sudul la dreapta.",
   indiciu="Desenează o cruce cu N sus și pune-te pe ea cu fața spre E."),
 alegere("V8-11", V8, ["V-2.1"], 1, "Stai cu fața spre nord. Ce punct cardinal ai în dreapta?",
   ["est", "vest", "sud", "nord-vest"],
   "Corect, estul e la dreapta.", "Cu fața spre nord, estul e la dreapta, vestul la stânga și sudul în spate."),
 pin("V8-12", V8, ["V-2.1"], 2, "Atinge pe hartă Polul Nord.", "lume", 89.5, 0, "Polul Nord", 1200,
   "Corect. Polul Nord e punctul cel mai nordic al Pământului, sus pe hartă.", "Polul Nord e în marginea de sus a hărții lumii, în mijlocul Oceanului Arctic.",
   indiciu="Caută marginea de sus a hărții."),
 pin("V8-13", V8, ["V-2.1"], 2, "Atinge pe hartă Polul Sud.", "lume", -89.5, 0, "Polul Sud", 1200,
   "Corect. Polul Sud e în mijlocul Antarcticii.", "Polul Sud e în marginea de jos a hărții, în Antarctica."),
 lacunar("V8-14", V8, ["V-1.1", "V-2.1"], 2, "Completează.",
   "Pe hărți, nordul este de obicei {0}. Direcția dintre nord și vest se numește {1}.", ["sus", "nord-vest"], ["jos", "nord-est"],
   "Exact.", "Nordul e sus pe hartă, iar între nord și vest e nord-vestul."),
 alegere("V8-15", V8, ["V-1.2", "V-2.1"], 2, "Ce folosește GPS-ul din telefon ca să afle unde ești?",
   ["semnale de la sateliți", "acul magnetic", "poziția Soarelui", "Steaua Polară"],
   "Da, GPS-ul primește semnale de la mai mulți sateliți.", "GPS-ul calculează poziția din semnalele trimise de sateliți. Busola, nu GPS-ul, are ac magnetic."),
]

# ============================================================ S9 Expediție: timpul și orizontul local
n9 = {
 "id": V9, "tip": "expeditie", "titlu": "Expediție: timpul și orizontul local",
 "descopera": {"intrebare": "Cât durează o zi, o lună, un an? Și ce vezi spre fiecare punct cardinal din curtea școlii?"},
 "invata": [{"titlu": "Ce faci în expediție", "text": "Măsori timpul, te orientezi în jurul școlii și desenezi o schiță simplă de hartă. Rezultatele intră în Jurnalul exploratorului."}],
 "pasi": [
  {"titlu": "1. Calendarul", "text": "Ziua vine din mișcarea Pământului în jurul axei sale. Anul vine din mișcarea Pământului în jurul Soarelui.", "itemi": ["V9-01", "V9-02", "V9-03"]},
  {"titlu": "2. Orientarea în curtea școlii", "text": "Ieși în curte cu clasa. Găsește partea în care răsare Soarele: acolo e estul. Întoarce-te cu fața spre nord.",
   "jurnal": {"cerinta": "Scrie ce vezi spre nord, spre sud, spre est și spre vest (clădiri, copaci, dealuri, drumuri)."}},
  {"titlu": "3. Schița drumului spre școală", "text": "Desenează pe o foaie drumul de acasă la școală. Pune săgeata nordului și o legendă cu cel puțin 3 semne (de exemplu: casă, copac, intersecție). Nu scrie adresa ta.",
   "jurnal": {"cerinta": "Spune în 2–3 propoziții ce semne ai pus în legendă și ce ai văzut pe drum.", "foto": True}},
 ],
 "referintaProfesor": REF.format("Aplicații practice: Măsurarea timpului; Orizontul local"),
}
i9 = [
 ordoneaza("V9-01", V9, ["V-4.2"], 1, "Ordonează unitățile de timp de la cea mai scurtă la cea mai lungă.",
   ["ziua", "săptămâna", "luna", "anotimpul", "anul"], "De la scurt la lung",
   "Corect.", "Ordinea e: zi, săptămână, lună, anotimp, an."),
 alegere("V9-02", V9, ["V-3.1"], 1, "Câte zile are un an obișnuit (care nu e bisect)?",
   ["365", "366", "360", "364"], "Corect: 365 de zile.", "Un an obișnuit are 365 de zile; anul bisect are 366, cu 29 februarie."),
 alegere("V9-03", V9, ["V-1.2", "V-3.2"], 2, "Ce mișcare a Pământului dă alternanța zi–noapte?",
   ["mișcarea de rotație, în jurul axei", "mișcarea de revoluție, în jurul Soarelui", "mișcarea Lunii în jurul Pământului", "mișcarea Soarelui în jurul Pământului"],
   "Da, rotația în jurul axei produce ziua și noaptea.", "Ziua și noaptea vin din rotația Pământului în jurul axei. Revoluția în jurul Soarelui dă anul și anotimpurile."),
]

# ============================================================ S10 Litosfera: caracteristici
n10 = {
 "id": V10, "tip": "nivel", "titlu": "Litosfera: caracteristici generale și importanță",
 "descopera": {"intrebare": "Pe ce stăm, pe ce construim case și de unde scoatem cărbunele? Toate țin de un singur înveliș al Pământului. Care?"},
 "invata": [
  {"titlu": "Geosferele Terrei",
   "text": "Pământul are mai multe învelișuri, numite geosfere: litosfera (învelișul de roci), atmosfera (aerul), hidrosfera (apa) și biosfera (viețuitoarele).\nLitosfera cuprinde scoarța terestră și partea de sus a mantalei. Numele vine din grecescul „lithos”, care înseamnă piatră."},
  {"titlu": "Rocile și importanța litosferei",
   "text": "Rocile pot fi magmatice (din magmă sau lavă răcită, ca granitul și bazaltul), sedimentare (din materiale depuse în straturi, ca calcarul) și metamorfice (roci transformate de temperatură și presiune, ca marmura).\nLitosfera ne dă locul pe care trăim, solul pentru plante și resurse: cărbune, petrol, gaze naturale, metale, sare, piatră de construcție.\nEa e formată din plăci tectonice, care se mișcă foarte încet."},
 ],
 "stiaiCa": "Marmura albă folosită la statui era la început calcar, transformat în adâncuri de căldură și presiune.",
 "referintaProfesor": REF.format("Litosfera – caracteristici generale și importanță"),
}
i10 = [
 asociaza("V10-01", V10, ["V-1.1"], 1, "Asociază fiecare geosferă cu ce cuprinde.",
   [["Litosfera", "învelișul de roci"], ["Atmosfera", "învelișul de aer"], ["Hidrosfera", "învelișul de apă"], ["Biosfera", "plantele și animalele"]],
   "Toate perechile sunt corecte.", "Lito- = piatră, atmo- = aer, hidro- = apă, bio- = viață."),
 lacunar("V10-02", V10, ["V-1.1"], 1, "Completează.", "Cuvântul „litosferă” vine din grecescul „lithos”, care înseamnă {0}.", ["piatră"], ["apă", "aer"],
   "Corect, litosfera e învelișul de piatră.", "„Lithos” înseamnă piatră."),
 alegere("V10-03", V10, ["V-1.1"], 1, "Care geosferă este formată din roci?", ["litosfera", "atmosfera", "hidrosfera", "biosfera"],
   "Da, litosfera.", "Rocile formează litosfera."),
 alegere("V10-04", V10, ["V-1.2"], 2, "Ce cuprinde litosfera?",
   ["scoarța terestră și partea de sus a mantalei", "doar munții", "nucleul Pământului", "apele și aerul"],
   "Corect.", "Litosfera = scoarța terestră + partea de sus a mantalei."),
 asociaza("V10-05", V10, ["V-1.1", "V-3.3"], 1, "În ce geosferă intră fiecare element?",
   [["granitul", "litosfera"], ["norii", "atmosfera"], ["râul", "hidrosfera"], ["pădurea", "biosfera"]],
   "Bravo!", "Granitul e rocă (litosfera), norii sunt în aer (atmosfera), râul e apă (hidrosfera), pădurea e vie (biosfera)."),
 asociaza("V10-06", V10, ["V-1.1", "V-3.1"], 2, "Asociază fiecare rocă cu tipul ei.",
   [["granitul", "rocă magmatică"], ["calcarul", "rocă sedimentară"], ["marmura", "rocă metamorfică"]],
   "Corect.", "Granitul vine din magmă răcită, calcarul din depuneri, marmura din calcar transformat."),
 alegere("V10-07", V10, ["V-1.2"], 2, "Bazaltul se formează din lava răcită la suprafață. Ce fel de rocă este?",
   ["magmatică", "sedimentară", "metamorfică", "nu e rocă"], "Corect.", "Tot ce vine din magmă sau lavă răcită e rocă magmatică."),
 alegere("V10-08", V10, ["V-3.3", "V-4.1"], 2, "Care dintre acestea NU este o resursă oferită de litosferă?",
   ["oxigenul din aer", "cărbunele", "sarea", "piatra de construcție"],
   "Corect, oxigenul vine din atmosferă.", "Cărbunele, sarea și piatra se scot din litosferă. Oxigenul ține de atmosferă."),
 lacunar("V10-09", V10, ["V-1.1"], 2, "Completează.",
   "Rocile formate din lava răcită sunt roci {0}. Rocile formate din materiale depuse în straturi sunt roci {1}.",
   ["magmatice", "sedimentare"], ["metamorfice"], "Exact.", "Lava răcită → magmatice; depuneri în straturi → sedimentare."),
 ordoneaza("V10-10", V10, ["V-1.2", "V-2.3"], 3, "Ordonează etapele formării unei roci sedimentare.",
   ["Rocile sunt sfărâmate de apă, vânt și variații de temperatură", "Fragmentele sunt transportate de râuri", "Fragmentele se depun în straturi pe fundul lacurilor și mărilor", "Straturile se tasează și se cimentează, formând roca"],
   "Ordinea etapelor", "Perfect!", "Întâi sfărâmare, apoi transport, depunere și, la final, tasare."),
 alegere("V10-11", V10, ["V-3.3"], 1, "Pe ce geosferă construim case și cultivăm plante?", ["litosfera", "atmosfera", "hidrosfera", "nucleul"],
   "Corect.", "Trăim și construim pe litosferă; solul pentru plante se formează tot din roci."),
 alegere("V10-12", V10, ["V-3.3"], 2, "Cărbunele, petrolul și gazele naturale se găsesc...", ["în rocile din litosferă", "în atmosferă", "în nucleul Pământului", "în nori"],
   "Da, în rocile din litosferă.", "Aceste resurse se găsesc în rocile din litosferă."),
 asociaza("V10-13", V10, ["V-3.2", "V-3.3"], 3, "Cum acționează celelalte geosfere asupra litosferei? Asociază.",
   [["Râul roade malul", "hidrosfera"], ["Vântul mută nisipul", "atmosfera"], ["Rădăcinile crapă roca", "biosfera"]],
   "Corect: toate geosferele modelează litosfera.", "Râul = apă (hidrosfera), vântul = aer (atmosfera), rădăcinile = viață (biosfera)."),
 lacunar("V10-14", V10, ["V-1.1"], 3, "Completează.", "Litosfera este împărțită în plăci care se mișcă foarte încet. Ele se numesc plăci {0}.",
   ["tectonice"], ["solare", "abisale"], "Corect.", "Se numesc plăci tectonice."),
]

# ============================================================ S11 Structura internă
n11 = {
 "id": V11, "tip": "nivel", "titlu": "Structura internă a Terrei",
 "descopera": {"intrebare": "Dacă ai putea săpa o groapă până în centrul Pământului, prin ce straturi ai trece?", "schema": "structura-interna"},
 "invata": [
  {"titlu": "Patru straturi", "schema": "structura-interna",
   "text": "Scoarța terestră e stratul subțire de roci de la suprafață: mai subțire sub oceane, mai groasă sub continente.\nMantaua e cel mai gros strat, din roci foarte fierbinți; ajunge până la aproximativ 2 900 km adâncime.\nNucleul extern e format din metale topite (mai ales fier și nichel). Nucleul intern, din centru, e din metale în stare solidă."},
  {"titlu": "Cum știm?",
   "text": "Nimeni n-a ajuns în mantaua Pământului. Oamenii de știință studiază undele produse de cutremure: ele se propagă diferit prin roci solide și prin materiale topite.\nCentrul Pământului e la aproximativ 6 370 km adâncime. Nucleul intern rămâne solid, deși e foarte fierbinte, pentru că presiunea e uriașă."},
 ],
 "stiaiCa": "Mantaua ocupă cea mai mare parte din volumul Pământului.",
 "referintaProfesor": REF.format("Structura internă a Terrei"),
}
S_INT = SURSE["INTERIOR"]
i11 = [
 etichete("V11-01", V11, ["V-1.2", "V-2.3"], 1, "Pune numele straturilor pe secțiunea prin Pământ.",
   [{"id": "scoarta", "eticheta": "scoarța"}, {"id": "manta", "eticheta": "mantaua"}, {"id": "nucleu-extern", "eticheta": "nucleul extern"}, {"id": "nucleu-intern", "eticheta": "nucleul intern"}],
   "Corect.", "De la suprafață spre centru: scoarța, mantaua, nucleul extern, nucleul intern.", schema="structura-interna"),
 denumeste("V11-02", V11, ["V-1.2"], 1, "Cum se numește stratul evidențiat cu roșu?",
   ["nucleul intern", "nucleul extern", "mantaua", "scoarța"], "Corect.", "Stratul din centru e nucleul intern.", schema="structura-interna", ev="nucleu-intern"),
 denumeste("V11-03", V11, ["V-1.2"], 2, "Cum se numește stratul evidențiat cu roșu?",
   ["mantaua", "scoarța", "nucleul extern", "litosfera"], "Corect.", "Stratul gros dintre scoarță și nucleu e mantaua.", schema="structura-interna", ev="manta"),
 ordoneaza("V11-04", V11, ["V-1.2", "V-4.2"], 1, "Ordonează straturile de la suprafață spre centru.",
   ["scoarța", "mantaua", "nucleul extern", "nucleul intern"], "De la suprafață spre centru", "Corect.", "Ordinea: scoarța, mantaua, nucleul extern, nucleul intern."),
 alegere("V11-05", V11, ["V-1.2", "V-3.1"], 2, "Care este cel mai gros strat al Pământului?", ["mantaua", "scoarța", "nucleul extern", "nucleul intern"],
   "Da, mantaua: aproximativ 2 900 km grosime.", "Mantaua e cel mai gros strat (aproximativ 2 900 km).", surse=S_INT),
 alegere("V11-06", V11, ["V-1.2"], 2, "În ce stare este nucleul extern?", ["lichidă (metale topite)", "solidă", "gazoasă", "e format din gheață"],
   "Corect.", "Nucleul extern e din metale topite; nucleul intern e solid."),
 alegere("V11-07", V11, ["V-1.2", "V-3.3"], 2, "Unde este scoarța terestră mai subțire?", ["sub oceane", "sub munți", "sub continente", "e la fel peste tot"],
   "Corect.", "Scoarța e mai subțire sub oceane și mai groasă sub continente, mai ales sub munți.", surse=S_INT),
 lacunar("V11-08", V11, ["V-3.1"], 2, "Completează cu valorile aproximative.",
   "Mantaua ajunge până la aproximativ {0} km adâncime, iar centrul Pământului se află la aproximativ {1} km.",
   ["2 900", "6 370"], ["290", "63 700"], "Corect.", "Mantaua: aproximativ 2 900 km; centrul: aproximativ 6 370 km.", surse=S_INT),
 grafic("V11-09", V11, ["V-2.3", "V-3.1"], 3, "Graficul arată adâncimea la care se termină fiecare strat. Cât de gros este, aproximativ, nucleul extern?",
   {"tip": "bare", "titlu": "Adâncimea la care se termină stratul (aproximativ)", "unitate": "km",
    "date": [{"eticheta": "Mantaua", "valoare": 2900}, {"eticheta": "Nucleul extern", "valoare": 5150}, {"eticheta": "Nucleul intern (centrul)", "valoare": 6370}],
    "sursa": "University of Alaska Fairbanks, Geophysical Institute"},
   ["aproximativ 2 250 km", "aproximativ 5 150 km", "aproximativ 1 220 km", "aproximativ 2 900 km"],
   "Corect: 5 150 − 2 900 = 2 250 km.", "Nucleul extern începe unde se termină mantaua (2 900 km) și se termină la 5 150 km: 5 150 − 2 900 = 2 250 km.",
   indiciu="Scade adâncimea la care începe din adâncimea la care se termină.", surse=S_INT),
 alegere("V11-10", V11, ["V-3.2", "V-4.1"], 3, "Cum au aflat oamenii de știință cum arată interiorul Pământului?",
   ["studiind undele produse de cutremure", "au forat până în centru", "au coborât cu un submarin", "au fotografiat Pământul din spațiu"],
   "Corect.", "Nimeni n-a forat dincolo de scoarță. Undele cutremurelor trec diferit prin roci solide și topite, iar așa se pot deduce straturile."),
 alegere("V11-11", V11, ["V-1.1"], 1, "Pe ce strat trăim?", ["scoarța terestră", "mantaua", "nucleul extern", "nucleul intern"], "Corect.", "Trăim pe scoarța terestră."),
 asociaza("V11-12", V11, ["V-1.2"], 2, "Asociază fiecare strat cu descrierea lui.",
   [["Scoarța", "strat subțire de roci, la suprafață"], ["Mantaua", "cel mai gros strat, din roci fierbinți"], ["Nucleul extern", "metale topite"], ["Nucleul intern", "metale solide, în centru"]],
   "Bravo!", "Scoarța e subțire, mantaua e cea mai groasă, nucleul extern e topit, nucleul intern e solid."),
 alegere("V11-13", V11, ["V-3.2"], 3, "Nucleul intern e cel mai fierbinte, dar e solid. De ce?",
   ["presiunea acolo e uriașă", "e acoperit de gheață", "e format din piatră obișnuită", "acolo nu ajunge căldura"],
   "Corect: presiunea uriașă ține metalele în stare solidă.", "Presiunea foarte mare din centru împiedică metalele să se topească."),
 lacunar("V11-14", V11, ["V-1.1"], 1, "Completează.", "Nucleul Pământului este format mai ales din {0} și nichel.", ["fier"], ["aur", "cupru"],
   "Corect.", "Nucleul e format mai ales din fier și nichel."),
]

# ============================================================ S12 Relieful
n12 = {
 "id": V12, "tip": "nivel", "titlu": "Relieful: continente și bazine oceanice",
 "descopera": {"intrebare": "Dacă ai goli oceanele, ce ai vedea pe fundul lor: o câmpie netedă sau munți și prăpăstii?", "schema": "fund-oceanic"},
 "invata": [
  {"titlu": "Continente și oceane",
   "text": "Uscatul formează continentele: Europa, Asia, Africa, America de Nord, America de Sud, Australia și Antarctica.\nApa sărată formează Oceanul Planetar, împărțit în Oceanul Pacific (cel mai mare), Atlanticul, Oceanul Indian și Oceanul Arctic (Înghețat de Nord). Oceanele acoperă cea mai mare parte a Terrei."},
  {"titlu": "Formele majore de relief", "schema": "fund-oceanic",
   "text": "Pe continente: munți (cele mai înalte), dealuri și podișuri (înălțimi mijlocii) și câmpii (joase și netede).\nPe fundul oceanelor: platforma continentală (uscatul continuă sub apă la adâncimi mici), abruptul continental, câmpiile abisale, dorsalele oceanice (lanțuri de munți submarini) și gropile abisale, cele mai adânci locuri.\nCel mai înalt vârf e Everest (8 848,86 m), în Munții Himalaya. Cel mai adânc loc cunoscut e în Groapa Marianelor, în Oceanul Pacific."},
 ],
 "stiaiCa": "Cel mai lung lanț muntos al Pământului e sub apă: dorsalele oceanice înconjoară planeta.",
 "referintaProfesor": REF.format("Relieful: bazine oceanice și continente; forme majore de relief"),
}
CONT = [{"id": "europa", "eticheta": "Europa", "lat": 52, "lon": 15}, {"id": "asia", "eticheta": "Asia", "lat": 45, "lon": 90},
        {"id": "africa", "eticheta": "Africa", "lat": 5, "lon": 20}, {"id": "amn", "eticheta": "America de Nord", "lat": 45, "lon": -100},
        {"id": "ams", "eticheta": "America de Sud", "lat": -15, "lon": -60}, {"id": "australia", "eticheta": "Australia", "lat": -25, "lon": 134},
        {"id": "antarctica", "eticheta": "Antarctica", "lat": -80, "lon": 30}]
i12 = [
 etichete("V12-01", V12, ["V-2.1", "V-2.2"], 2, "Pune numele continentelor pe hartă.", CONT,
   "Toate continentele sunt la locul lor!", "Verifică: Europa și Asia sunt lipite, Africa e la sud de Europa, cele două Americi sunt în vest.", harta="lume",
   indiciu="Începe cu Antarctica: e jos, la Polul Sud."),
 etichete("V12-02", V12, ["V-2.1"], 2, "Pune numele oceanelor pe hartă.",
   [{"id": "pacific", "eticheta": "Oceanul Pacific", "lat": 0, "lon": -140}, {"id": "atlantic", "eticheta": "Oceanul Atlantic", "lat": 15, "lon": -40},
    {"id": "indian", "eticheta": "Oceanul Indian", "lat": -20, "lon": 75}, {"id": "arctic", "eticheta": "Oceanul Arctic", "lat": 80, "lon": -10}],
   "Corect.", "Pacificul e între Asia–Australia și cele două Americi; Atlanticul între Americi și Europa–Africa; Indianul la sud de Asia; Arcticul în nord.", harta="lume"),
 pin("V12-03", V12, ["V-2.1"], 1, "Atinge pe hartă Oceanul Pacific.", "lume", 0, -150, "Oceanul Pacific", 4500,
   "Corect, cel mai mare ocean.", "Pacificul e oceanul uriaș dintre Asia–Australia și cele două Americi."),
 alegere("V12-04", V12, ["V-4.2"], 1, "Care este cel mai mare ocean?", ["Oceanul Pacific", "Oceanul Atlantic", "Oceanul Indian", "Oceanul Arctic"],
   "Corect.", "Pacificul e cel mai mare ocean."),
 etichete("V12-05", V12, ["V-1.1", "V-2.3"], 2, "Pune denumirile pe profilul fundului oceanic.",
   [{"id": "platforma", "eticheta": "platforma continentală"}, {"id": "abrupt", "eticheta": "abruptul continental"}, {"id": "campie-abisala", "eticheta": "câmpia abisală"},
    {"id": "dorsala", "eticheta": "dorsala oceanică"}, {"id": "groapa", "eticheta": "groapa abisală"}],
   "Excelent!", "De la țărm spre larg: platforma continentală, abruptul, câmpia abisală; dorsala e un munte submarin, groapa e cea mai adâncă.", schema="fund-oceanic"),
 denumeste("V12-06", V12, ["V-1.1", "V-2.3"], 2, "Ce formă de relief oceanic e evidențiată?",
   ["groapa abisală", "dorsala oceanică", "platforma continentală", "câmpia abisală"], "Corect.", "Partea cea mai adâncă, îngustă, e groapa abisală.", schema="fund-oceanic", ev="groapa"),
 alegere("V12-07", V12, ["V-1.1", "V-4.2"], 2, "Care este cel mai înalt vârf de pe Terra?",
   ["Everest, 8 848,86 m (Himalaya)", "Mont Blanc (Alpi)", "Moldoveanu (Carpați)", "Kilimanjaro (Africa)"],
   "Corect.", "Everest, în Munții Himalaya, are 8 848,86 m (măsurătoarea Nepal–China din 2020).", surse=SURSE["EVEREST"]),
 pin("V12-08", V12, ["V-2.1"], 2, "Atinge pe hartă vârful Everest, în Munții Himalaya.", "lume", 27.99, 86.93, "Vârful Everest", 800,
   "Corect.", "Everest e în Asia, la granița dintre Nepal și China, la nord de India.", indiciu="Caută la nord de India."),
 pin("V12-09", V12, ["V-2.1"], 3, "Atinge pe hartă Groapa Marianelor, cel mai adânc loc cunoscut din ocean.", "lume", 11.35, 142.2, "Groapa Marianelor", 1000,
   "Corect.", "Groapa Marianelor e în vestul Oceanului Pacific, la est de Filipine.", indiciu="E în Pacific, la est de Filipine."),
 asociaza("V12-10", V12, ["V-1.1", "V-1.2"], 1, "Asociază forma de relief cu descrierea ei.",
   [["Munții", "cele mai înalte forme, cu vârfuri și văi adânci"], ["Dealurile", "înălțimi mai mici, cu pante domoale"], ["Podișurile", "suprafețe înalte, aproape netede, tăiate de văi"], ["Câmpiile", "suprafețe joase și netede"]],
   "Bravo!", "Munții sunt cei mai înalți, câmpiile cele mai joase și netede; podișurile sunt înalte, dar netede."),
 ordoneaza("V12-11", V12, ["V-4.2"], 1, "Ordonează formele de relief de la cea mai joasă la cea mai înaltă.", ["câmpia", "dealul", "muntele"], "De la jos la sus",
   "Corect.", "Câmpia e cea mai joasă, apoi dealul, apoi muntele."),
 grafic("V12-12", V12, ["V-2.3", "V-3.1"], 3, "Profilul arată altitudinile într-un ținut imaginar. Între care două puncte urci cel mai mult?",
   {"tip": "profil", "titlu": "Profil printr-un ținut imaginar (altitudini în metri)", "unitate": "m",
    "date": [{"eticheta": "A", "valoare": 120}, {"eticheta": "B", "valoare": 450}, {"eticheta": "C", "valoare": 1800}, {"eticheta": "D", "valoare": 2300}, {"eticheta": "E", "valoare": 900}, {"eticheta": "F", "valoare": 150}]},
   ["între B și C", "între C și D", "între A și B", "între E și F"],
   "Corect: de la 450 la 1 800 m urci 1 350 m.", "Calculează diferențele: A–B = 330 m, B–C = 1 350 m, C–D = 500 m. Cel mai mult urci între B și C.",
   indiciu="Scade altitudinile vecine două câte două."),
 lacunar("V12-13", V12, ["V-1.1"], 2, "Completează.",
   "Partea de uscat care continuă sub apă, la adâncimi mici, se numește {0}. Lanțurile de munți de pe fundul oceanelor se numesc {1}.",
   ["platformă continentală", "dorsale oceanice"], ["câmpie abisală", "gropi abisale"], "Corect.", "Platforma continentală e la adâncimi mici; dorsalele sunt munți submarini."),
 alegere("V12-14", V12, ["V-3.3"], 2, "Ce ocupă cea mai mare parte din suprafața Pământului?", ["oceanele", "continentele", "munții", "deșerturile"],
   "Da, oceanele.", "Oceanul Planetar acoperă mai mult de jumătate din suprafața Pământului, adică mai mult decât uscatul."),
]

# ============================================================ S13 Vulcanii și cutremurele
n13 = {
 "id": V13, "tip": "nivel", "titlu": "Vulcanii și cutremurele",
 "descopera": {"intrebare": "Ce au în comun un vulcan din Italia și un cutremur din Vrancea?", "schema": "vulcan"},
 "invata": [
  {"titlu": "Vulcanii", "schema": "vulcan",
   "text": "Sub vulcan, magma se adună în camera magmatică. Când presiunea gazelor crește, magma urcă prin coșul vulcanic și iese prin crater.\nMagma ajunsă la suprafață se numește lavă. Lava răcită, cenușa și bucățile de rocă formează conul vulcanului.\nExemple: Etna și Vezuviul (Italia), Fuji (Japonia)."},
  {"titlu": "Cutremurele",
   "text": "Cutremurul e o mișcare bruscă a scoarței. Locul din adânc unde se produce se numește hipocentru (focar); punctul de la suprafață, chiar deasupra lui, se numește epicentru.\nCutremurele se înregistrează cu seismograful. Vulcanii și cutremurele apar mai ales la marginile plăcilor tectonice.\nÎn România, cele mai multe cutremure puternice se produc în zona Vrancea, aproape de Râmnicu Sărat.\nLa cutremur: te adăpostești sub bancă și te ții de ea, stai departe de geamuri, nu folosești liftul, ieși calm abia după ce se oprește mișcarea."},
 ],
 "stiaiCa": "Cutremurele de sub ocean pot produce valuri uriașe, numite tsunami.",
 "referintaProfesor": REF.format("Vulcanii și cutremurele"),
}
i13 = [
 etichete("V13-01", V13, ["V-1.1", "V-1.2"], 1, "Pune denumirile pe secțiunea prin vulcan.",
   [{"id": "camera", "eticheta": "camera magmatică"}, {"id": "cos", "eticheta": "coșul vulcanic"}, {"id": "crater", "eticheta": "craterul"}, {"id": "con", "eticheta": "conul vulcanic"}, {"id": "nor", "eticheta": "norul de cenușă"}],
   "Excelent!", "De jos în sus: camera magmatică, coșul, craterul. Conul e muntele format din lavă și cenușă.", schema="vulcan"),
 ordoneaza("V13-02", V13, ["V-1.2", "V-2.3"], 2, "Ordonează etapele unei erupții vulcanice.",
   ["Magma se adună în camera magmatică", "Presiunea gazelor crește", "Magma urcă prin coșul vulcanic", "Lava, gazele și cenușa ies prin crater", "Lava se răcește și înalță conul"],
   "Etapele erupției", "Perfect!", "Totul pornește din camera magmatică; lava se răcește abia la final."),
 lacunar("V13-03", V13, ["V-1.1"], 1, "Completează.", "Magma ajunsă la suprafață se numește {0}.", ["lavă"], ["cenușă", "rocă"], "Corect.", "Magma care iese la suprafață se numește lavă."),
 pin("V13-04", V13, ["V-2.1"], 2, "Atinge pe hartă vulcanul Etna, din insula Sicilia (Italia).", "lume", 37.75, 14.99, "Etna", 500,
   "Corect.", "Etna e în Sicilia, insula din sudul Italiei.", indiciu="Italia seamănă cu o cizmă; Sicilia e mingea din fața ei."),
 pin("V13-05", V13, ["V-2.1"], 3, "Atinge pe hartă vulcanul Fuji, din Japonia.", "lume", 35.36, 138.73, "Fuji", 600,
   "Corect.", "Fuji e în Japonia, în estul Asiei."),
 alegere("V13-06", V13, ["V-1.1"], 1, "Cum se numește locul din adânc unde se produce cutremurul?", ["hipocentru (focar)", "epicentru", "crater", "seismograf"],
   "Corect.", "Locul din adânc e hipocentrul; deasupra lui, la suprafață, e epicentrul."),
 alegere("V13-07", V13, ["V-1.1"], 2, "Cum se numește punctul de la suprafață aflat chiar deasupra hipocentrului?", ["epicentru", "crater", "camera magmatică", "dorsală"],
   "Corect.", "Epicentrul e la suprafață, deasupra hipocentrului."),
 alegere("V13-08", V13, ["V-3.1"], 1, "Cu ce aparat se înregistrează cutremurele?", ["seismograful", "busola", "termometrul", "barometrul"],
   "Corect.", "Seismograful înregistrează vibrațiile scoarței."),
 ordoneaza("V13-09", V13, ["V-4.3"], 2, "Ești în clasă și începe un cutremur. Ordonează ce faci.",
   ["Te adăpostești sub bancă și te ții de ea", "Stai departe de geamuri și dulapuri", "Aștepți să se oprească mișcarea", "Ieși calm, cu profesorul, pe traseul de evacuare"],
   "Ordinea acțiunilor", "Corect. Așa te protejezi.", "Întâi te protejezi pe loc; ieși abia după ce se oprește mișcarea."),
 alegere("V13-10", V13, ["V-4.3"], 2, "În timpul cutremurului ești pe hol, lângă lift. Ce faci?",
   ["nu folosești liftul; te adăpostești lângă un perete interior, departe de geamuri", "iei liftul ca să ieși repede", "fugi pe scări în timp ce clădirea se mișcă", "te așezi lângă geam ca să vezi ce se întâmplă"],
   "Corect.", "Liftul se poate bloca. Rămâi pe loc, protejat, departe de geamuri, până se oprește mișcarea."),
 alegere("V13-11", V13, ["V-3.3", "V-4.3"], 2, "În ce zonă din România se produc cele mai multe cutremure puternice?", ["zona Vrancea", "Delta Dunării", "Câmpia de Vest", "Munții Apuseni"],
   "Corect, zona Vrancea, aproape de orașul nostru.", "Cele mai multe cutremure puternice din România se produc în zona Vrancea."),
 asociaza("V13-12", V13, ["V-1.1"], 3, "Asociază termenul cu definiția.",
   [["magma", "rocă topită, aflată în adânc"], ["lava", "magmă ajunsă la suprafață"], ["craterul", "deschiderea din vârful vulcanului"], ["coșul vulcanic", "canalul prin care urcă magma"]],
   "Bravo!", "Magma e în adânc, lava la suprafață; coșul e canalul, craterul e deschiderea de sus."),
 alegere("V13-13", V13, ["V-3.2"], 3, "De ce apar vulcanii și cutremurele mai ales la marginile plăcilor tectonice?",
   ["acolo plăcile se ciocnesc, se depărtează sau alunecă una pe lângă alta", "acolo e mai cald la suprafață", "acolo sunt mai multe orașe", "acolo plouă mai mult"],
   "Corect.", "Mișcarea plăcilor la margini produce cutremure și deschide drum magmei."),
 lacunar("V13-14", V13, ["V-1.1", "V-3.2"], 3, "Completează.", "Valurile uriașe produse de cutremurele de sub ocean se numesc {0}.", ["tsunami"], ["uragan", "maree"],
   "Corect.", "Se numesc tsunami."),
]

# ============================================================ S16 Expediție: relieful orizontului local
n16 = {
 "id": V16, "tip": "expeditie", "titlu": "Expediție: relieful orizontului local",
 "descopera": {"intrebare": "Ce forme de relief sunt în jurul orașului nostru și ce pericole ascund?"},
 "invata": [{"titlu": "Ce faci în expediție", "text": "Observi relieful din jurul școlii, înveți semnele unei alunecări de teren și faci un plan pentru cutremur, acasă."}],
 "pasi": [
  {"titlu": "1. Relieful din jurul școlii",
   "text": "Orașul Râmnicu Sărat se află în zona în care Câmpia Română se întâlnește cu dealurile Subcarpaților de Curbură.\nDin curtea școlii sau de la geam, uită-te spre nord-vest și spre sud-est.",
   "jurnal": {"cerinta": "În ce direcție vezi teren mai înalt? Cum arată terenul în direcția opusă? Desenează și fotografiază o schiță.", "foto": True}},
  {"titlu": "2. Alunecările de teren", "text": "Pe versanții cu roci argiloase, după ploi multe, pământul poate aluneca la vale.", "itemi": ["V16-01", "V16-02"]},
  {"titlu": "3. Planul familiei pentru cutremur", "text": "Discută acasă: unde vă adăpostiți, unde vă întâlniți afară, ce puneți în rucsacul de urgență.", "itemi": ["V16-03"],
   "jurnal": {"cerinta": "Scrie 3 reguli ale familiei tale pentru cutremur și 5 lucruri din rucsacul de urgență."}},
 ],
 "referintaProfesor": REF.format("Aplicații practice: Relieful orizontului local; reguli de comportare"),
}
i16 = [
 alegere("V16-01", V16, ["V-4.3"], 2, "Care este un semn că un versant ar putea aluneca?",
   ["crăpături noi în pământ și copaci înclinați", "iarba verde", "un drum asfaltat", "păsări pe cer"],
   "Corect.", "Crăpăturile din sol, copacii și gardurile înclinate arată că terenul se mișcă."),
 ordoneaza("V16-02", V16, ["V-4.3"], 2, "Vezi că terenul începe să alunece lângă casă. Ordonează ce faci.",
   ["Te îndepărtezi de zona care alunecă", "Anunți un adult", "Se sună la 112", "Nu te întorci până nu spun autoritățile că e sigur"],
   "Ordinea acțiunilor", "Corect.", "Întâi te pui în siguranță, apoi anunți; nu te întorci până nu e sigur."),
 alegere("V16-03", V16, ["V-4.3"], 1, "Ce NU pui în rucsacul de urgență?", ["jocuri video", "apă de băut", "lanternă", "trusă de prim ajutor"],
   "Corect.", "În rucsac pui lucruri care te ajută să rămâi în siguranță: apă, lanternă, trusă medicală, fluier, haine."),
]

boss5 = [{"id": "V-T2", "test": "T2", "titlu": "Boss T₂: Paznicul Litosferei", "saptamana": 13, "niveluri": [V10, V11, V12, V13]}]

idx = {"clasa": 5, "fisiere": [
  scrie(5, "u2-miscare.json", "Terra – o planetă în mișcare", [n8, n9], i8 + i9),
  scrie(5, "u3-litosfera.json", "Terra – o planetă în transformare. Litosfera", [n10, n11, n12, n13, n16], i10 + i11 + i12 + i13 + i16),
]}
json.dump(idx, open(f"{ROOT}/clasa-5/index.json", "w"), ensure_ascii=False, indent=1)
print("clasa 5:", sum(len(x) for x in [i8, i9, i10, i11, i12, i13, i16]), "itemi")
