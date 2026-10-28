import json, sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from gen_common import *

E8 = "VIII-S08-podisul-moldovei-podisul-dobrogei"
E9 = "VIII-S09-campia-vest-dealurile-vest"
E10 = "VIII-S10-campia-romana"
E11 = "VIII-S11-delta-dunarii-platforma-continentala"
E12 = "VIII-S12-aplicatii-practice-studii-caz"
REF = "Manual Art Klett, clasa a VIII-a, ediția 2025 (manuale.edu.ro), lecția „{}”"

GRAF_RELIEF = {"tip": "structura", "titlu": "Treptele de relief ale României (% din suprafață)", "unitate": " %",
               "date": [{"eticheta": "munți", "valoare": 31}, {"eticheta": "dealuri și podișuri", "valoare": 36}, {"eticheta": "câmpii", "valoare": 33}],
               "sursa": "ICPDR – Romania: Facts & Figures"}

# ============================================================ S8 Podișul Moldovei și Podișul Dobrogei
n8 = {
 "id": E8, "tip": "nivel", "titlu": "Podișul Moldovei și Podișul Dobrogei",
 "descopera": {"intrebare": "În Dobrogea sunt cei mai vechi munți din România, dar cel mai înalt vârf al lor are sub 500 m. Cum e posibil?"},
 "invata": [
  {"titlu": "Podișul Moldovei",
   "text": "Se află în estul țării, între Subcarpații Moldovei și râul Prut. E format din roci sedimentare, multe argiloase, de aceea pe versanți sunt frecvente alunecările de teren.\nSubunități: Podișul Sucevei (nord-vest), Câmpia Moldovei (nord-est) și Podișul Bârladului (sud). Orașe: Suceava, Iași, Bârlad, Vaslui."},
  {"titlu": "Podișul Dobrogei",
   "text": "Se află între Dunăre și Marea Neagră. În nord sunt Munții Măcinului, cei mai vechi munți din România: s-au format acum peste 250 de milioane de ani și au fost tociți de eroziune. Vârful Țuțuiatu (Greci) are 467 m.\nTot în nord: Dealurile Tulcei și Podișul Babadag. În sud: Podișul Casimcei (din șisturi verzi) și Podișul Medgidiei, traversat de Canalul Dunăre–Marea Neagră. Clima e secetoasă. Orașe: Constanța, Tulcea, Medgidia."},
 ],
 "stiaiCa": "Munții Măcinului sunt munți hercinici, mult mai vechi decât Carpații. De aceea sunt atât de joși: au avut timp să fie erodați.",
 "referintaProfesor": REF.format("Podișul Moldovei și Podișul Dobrogei"),
}
i8 = [
 pin("E8-01", E8, ["VIII-2.1"], 1, "Atinge pe hartă Podișul Moldovei.", "romania", 46.8, 27.3, "Podișul Moldovei", 120,
   "Corect.", "Podișul Moldovei e în estul țării, între Carpații Orientali (cu Subcarpații) și Prut."),
 pin("E8-02", E8, ["VIII-2.1"], 1, "Atinge pe hartă Podișul Dobrogei.", "romania", 44.6, 28.4, "Podișul Dobrogei", 100,
   "Corect.", "Dobrogea e în sud-est, între Dunăre și Marea Neagră."),
 pin("E8-03", E8, ["VIII-2.1"], 2, "Atinge pe hartă Munții Măcinului.", "romania", 45.21, 28.25, "Munții Măcinului", 45,
   "Corect.", "Munții Măcinului sunt în nord-vestul Dobrogei, chiar lângă Dunăre.", indiciu="Caută în nordul Dobrogei, unde Dunărea face un cot spre est."),
 etichete("E8-04", E8, ["VIII-2.1"], 2, "Pune numele orașelor pe hartă.",
   [{"id": "suceava", "eticheta": "Suceava", "lat": 47.65, "lon": 26.26}, {"id": "iasi", "eticheta": "Iași", "lat": 47.16, "lon": 27.59},
    {"id": "constanta", "eticheta": "Constanța", "lat": 44.17, "lon": 28.63}, {"id": "tulcea", "eticheta": "Tulcea", "lat": 45.18, "lon": 28.80}],
   "Bravo!", "Suceava e cel mai la nord-vest, Iași spre Prut; Constanța e pe țărmul mării, Tulcea lângă Dunăre, la intrarea în Deltă.", harta="romania"),
 asociaza("E8-05", E8, ["VIII-1.1", "VIII-2.1"], 2, "Asociază orașul cu unitatea de relief în care se află.",
   [["Suceava", "Podișul Sucevei"], ["Bârlad", "Podișul Bârladului"], ["Tulcea", "Dobrogea de Nord"], ["Constanța", "Dobrogea de Sud"]],
   "Corect.", "Orașele Suceava și Bârlad dau numele podișurilor lor; Tulcea e în nordul Dobrogei, Constanța în sud."),
 alegere("E8-06", E8, ["VIII-1.1"], 1, "Care sunt cei mai vechi munți din România?", ["Munții Măcinului", "Munții Făgăraș", "Munții Apuseni", "Munții Bucegi"],
   "Corect.", "Munții Măcinului, din Dobrogea, sunt cei mai vechi munți din România.", surse=SURSE["MACIN"]),
 alegere("E8-07", E8, ["VIII-1.1", "VIII-3.1"], 2, "Ce altitudine are Vârful Țuțuiatu (Greci), cel mai înalt din Munții Măcinului?", ["467 m", "2 544 m", "1 467 m", "67 m"],
   "Corect.", "Vârful Țuțuiatu are 467 m.", surse=SURSE["MACIN"]),
 alegere("E8-08", E8, ["VIII-2.2", "VIII-4.2"], 2, "Ce proces modelează des versanții din Podișul Moldovei?", ["alunecările de teren", "erupțiile vulcanice", "ghețarii", "valurile mării"],
   "Corect.", "Rocile argiloase, îmbibate cu apă, alunecă ușor pe versanți."),
 lacunar("E8-09", E8, ["VIII-1.2", "VIII-2.1"], 2, "Completează.",
   "Podișul Dobrogei se află între {0} și Marea Neagră. Canalul Dunăre–Marea Neagră traversează Podișul {1}.",
   ["Dunăre", "Medgidiei"], ["Prut", "Casimcei"], "Corect.", "Dobrogea e între Dunăre și mare; canalul trece prin Podișul Medgidiei."),
 alegere("E8-10", E8, ["VIII-2.1"], 2, "Care subunitate NU aparține Podișului Moldovei?", ["Podișul Babadag", "Podișul Sucevei", "Câmpia Moldovei", "Podișul Bârladului"],
   "Corect: Podișul Babadag e în Dobrogea.", "Podișul Babadag e în nordul Dobrogei. Celelalte trei sunt subunități ale Podișului Moldovei."),
 asociaza("E8-11", E8, ["VIII-1.1", "VIII-1.2"], 2, "Asociază fiecare subunitate cu o caracteristică.",
   [["Munții Măcinului", "munți vechi, din granit, foarte erodați"], ["Podișul Casimcei", "podiș format din șisturi verzi"], ["Podișul Medgidiei", "traversat de Canalul Dunăre–Marea Neagră"], ["Podișul Sucevei", "în nord-vestul Podișului Moldovei"]],
   "Bravo!", "Verifică: șisturile verzi sunt specifice Podișului Casimcei; canalul traversează Podișul Medgidiei."),
 alegere("E8-12", E8, ["VIII-4.3"], 3, "Prin ce se deosebesc Munții Măcinului de Carpați?",
   ["sunt mult mai vechi și mai erodați, deci mult mai joși", "sunt mai tineri și mai înalți", "sunt vulcani activi", "sunt acoperiți de ghețari"],
   "Corect.", "Munții Măcinului sunt mult mai vechi; eroziunea i-a tocit timp îndelungat, de aceea au sub 500 m."),
 grafic("E8-13", E8, ["VIII-2.2"], 2, "Din ce treaptă de relief fac parte Podișul Moldovei și Podișul Dobrogei și ce parte din suprafața țării ocupă treapta lor?",
   GRAF_RELIEF, ["dealuri și podișuri, 36 %", "munți, 31 %", "câmpii, 33 %", "dealuri și podișuri, 33 %"],
   "Corect.", "Podișurile intră în treapta dealurilor și podișurilor, care ocupă 36 % din suprafața țării.", surse=SURSE["RELIEF_RO"]),
 ordoneaza("E8-14", E8, ["VIII-2.1"], 3, "Ordonează unitățile de relief de la nord la sud.",
   ["Podișul Sucevei", "Podișul Bârladului", "Podișul Babadag", "Podișul Medgidiei"], "De la nord la sud",
   "Corect.", "Sucevei (nord), Bârladului (sud Moldova), Babadag (nordul Dobrogei), Medgidiei (sudul Dobrogei).",
   indiciu="Primele două sunt în Moldova, ultimele două în Dobrogea."),
]

# ============================================================ S9 Câmpia de Vest și Dealurile de Vest
n9 = {
 "id": E9, "tip": "nivel", "titlu": "Câmpia de Vest și Dealurile de Vest",
 "descopera": {"intrebare": "De ce în vestul țării plouă mai mult decât în Bărăgan, deși ambele sunt câmpii?"},
 "invata": [
  {"titlu": "Dealurile de Vest",
   "text": "Fac trecerea dintre Carpații Occidentali și Câmpia de Vest. Se împart în Dealurile Silvaniei (nord), Dealurile Crișanei (centru) și Dealurile Banatului (sud)."},
  {"titlu": "Câmpia de Vest",
   "text": "Se întinde de-a lungul graniței cu Ungaria și Serbia. E o câmpie de acumulare: s-a format din aluviunile aduse de râurile care coboară din Carpații Occidentali (Someșul, Crișurile, Mureșul, Timișul).\nAre influențe climatice oceanice, deci e mai umedă. Zonele mlăștinoase au fost desecate. Predomină agricultura. Orașe: Timișoara, Arad, Oradea, Satu Mare."},
 ],
 "stiaiCa": "În trecut, mari suprafețe din Banat erau mlaștini. Au fost desecate prin canale, iar azi sunt terenuri agricole.",
 "referintaProfesor": REF.format("Câmpia de Vest și Dealurile de Vest"),
}
i9 = [
 pin("E9-01", E9, ["VIII-2.1"], 1, "Atinge pe hartă Câmpia de Vest.", "romania", 46.3, 21.3, "Câmpia de Vest", 90,
   "Corect.", "Câmpia de Vest e lângă granița cu Ungaria și Serbia."),
 etichete("E9-02", E9, ["VIII-2.1"], 2, "Pune numele orașelor pe hartă.",
   [{"id": "timisoara", "eticheta": "Timișoara", "lat": 45.76, "lon": 21.23}, {"id": "arad", "eticheta": "Arad", "lat": 46.17, "lon": 21.31},
    {"id": "oradea", "eticheta": "Oradea", "lat": 47.05, "lon": 21.93}, {"id": "satumare", "eticheta": "Satu Mare", "lat": 47.79, "lon": 22.89}],
   "Bravo!", "De la nord la sud: Satu Mare, Oradea, Arad, Timișoara.", harta="romania"),
 alegere("E9-03", E9, ["VIII-2.1"], 1, "Unde se află Câmpia de Vest?",
   ["în vestul țării, la granița cu Ungaria și Serbia", "în sudul țării, lângă Dunăre", "în estul țării, lângă Prut", "în centrul Transilvaniei"],
   "Corect.", "Câmpia de Vest e de-a lungul graniței de vest."),
 alegere("E9-04", E9, ["VIII-2.1", "VIII-1.2"], 2, "Între ce unități de relief se află Dealurile de Vest?",
   ["între Carpații Occidentali și Câmpia de Vest", "între Carpații Meridionali și Dunăre", "între Subcarpați și Podișul Moldovei", "între Delta Dunării și mare"],
   "Corect.", "Dealurile de Vest fac trecerea de la Carpații Occidentali la Câmpia de Vest."),
 asociaza("E9-05", E9, ["VIII-2.1"], 2, "Asociază fiecare subunitate cu poziția ei.",
   [["Dealurile Silvaniei", "în nord"], ["Dealurile Crișanei", "în centru"], ["Dealurile Banatului", "în sud"], ["Câmpia de Vest", "la vest de dealuri"]],
   "Corect.", "Silvaniei – nord, Crișanei – centru, Banatului – sud; câmpia e la vest de ele."),
 ordoneaza("E9-06", E9, ["VIII-2.1"], 2, "Ordonează orașele din vest de la nord la sud.", ["Satu Mare", "Oradea", "Arad", "Timișoara"], "De la nord la sud",
   "Corect.", "Satu Mare e cel mai nordic, Timișoara cel mai sudic."),
 lacunar("E9-07", E9, ["VIII-1.1", "VIII-3.1"], 2, "Completează.",
   "Câmpia de Vest s-a format din aluviunile aduse de râuri; este o câmpie de {0}. Râurile care o traversează coboară din Carpații {1}.",
   ["acumulare", "Occidentali"], ["eroziune", "Orientali"], "Corect.", "E o câmpie de acumulare, cu râuri care vin din Carpații Occidentali."),
 alegere("E9-08", E9, ["VIII-2.1"], 2, "Care râu NU traversează Câmpia de Vest?", ["Prutul", "Mureșul", "Someșul", "Timișul"],
   "Corect.", "Prutul e în estul țării. Mureșul, Someșul, Crișurile și Timișul traversează Câmpia de Vest."),
 pin("E9-09", E9, ["VIII-2.1"], 2, "Atinge pe hartă orașul Arad, de pe râul Mureș.", "romania", 46.17, 21.31, "Arad", 35,
   "Corect.", "Aradul e în Câmpia de Vest, pe Mureș."),
 alegere("E9-10", E9, ["VIII-3.3", "VIII-4.3"], 3, "Ce influențe climatice se simt mai mult în Câmpia de Vest?",
   ["influențe oceanice, mai umede", "influențe de ariditate, foarte uscate", "influențe pontice, de la Marea Neagră", "influențe polare"],
   "Corect.", "Vestul țării primește mase de aer umed dinspre ocean; estul e mai uscat."),
 alegere("E9-11", E9, ["VIII-1.1"], 2, "Ce activitate economică predomină în Câmpia de Vest?", ["agricultura", "mineritul de cărbune", "pescuitul la mare", "turismul montan"],
   "Corect.", "Solurile fertile și relieful neted favorizează agricultura."),
 grafic("E9-12", E9, ["VIII-2.2"], 2, "Pe acest profil schematic, ce unitate de relief se află între munți și câmpie?",
   {"tip": "profil", "titlu": "Profil schematic de la est la vest (altitudini orientative, m)", "unitate": "m",
    "date": [{"eticheta": "Carpații Occ.", "valoare": 1400}, {"eticheta": "", "valoare": 700}, {"eticheta": "Dealurile de Vest", "valoare": 350}, {"eticheta": "", "valoare": 180}, {"eticheta": "Câmpia de Vest", "valoare": 100}]},
   ["Dealurile de Vest", "Câmpia Română", "Subcarpații", "Podișul Getic"],
   "Corect.", "Dealurile de Vest fac trecerea de la Carpații Occidentali la Câmpia de Vest."),
 lacunar("E9-13", E9, ["VIII-1.1"], 1, "Completează.", "Dealurile de Vest fac legătura între Carpații {0} și Câmpia de Vest.", ["Occidentali"], ["Orientali", "Meridionali"],
   "Corect.", "Carpații Occidentali sunt chiar la est de Dealurile de Vest."),
 alegere("E9-14", E9, ["VIII-4.2", "VIII-4.4"], 3, "Pe ce fel de terenuri s-au făcut lucrări de desecare în Câmpia de Vest?",
   ["pe terenurile mlăștinoase", "pe vârfurile munților", "pe dunele de nisip", "în orașe"],
   "Corect.", "Desecarea înseamnă scurgerea apei din mlaștini prin canale, ca terenul să poată fi cultivat."),
]

# ============================================================ S10 Câmpia Română
n10 = {
 "id": E10, "tip": "nivel", "titlu": "Câmpia Română",
 "descopera": {"intrebare": "Orașul nostru e la marginea celei mai întinse câmpii a României. Cum se numește și de ce e atât de bună pentru agricultură?"},
 "invata": [
  {"titlu": "Poziție și subunități",
   "text": "Câmpia Română e cea mai întinsă câmpie a țării. E mărginită la sud și la est de Dunăre (în nord-est și de Siret), iar la nord de Podișul Getic și de Subcarpați.\nDe la vest la est: Câmpia Olteniei, Câmpia Burnasului, Câmpia Vlăsiei (cu Bucureștiul) și Bărăganul. Râmnicu Sărat se află la marginea ei nordică, unde câmpia întâlnește Subcarpații de Curbură."},
  {"titlu": "Roci, soluri, climă",
   "text": "O mare parte a câmpiei e acoperită de loess, o rocă afânată, gălbuie. Pe loess s-au format cernoziomuri, soluri foarte fertile.\nÎn Bărăgan sunt crovuri, mici adâncituri rotunjite. Spre est clima devine mai uscată, cu secete frecvente; iarna bate crivățul, un vânt rece și uscat din est. De aceea se fac irigații."},
 ],
 "stiaiCa": "Bărăganul e numit „grânarul țării” pentru culturile mari de cereale.",
 "referintaProfesor": REF.format("Câmpia Română"),
}
i10 = [
 pin("E10-01", E10, ["VIII-2.1"], 1, "Atinge pe hartă Câmpia Română.", "romania", 44.4, 25.8, "Câmpia Română", 150,
   "Corect.", "Câmpia Română e în sudul țării, între Carpați (cu Subcarpații și Podișul Getic) și Dunăre."),
 pin("E10-02", E10, ["VIII-2.1"], 1, "Atinge pe hartă Bucureștiul.", "romania", 44.43, 26.10, "București", 35,
   "Corect.", "Bucureștiul e în Câmpia Vlăsiei, în partea centrală a Câmpiei Române."),
 pin("E10-03", E10, ["VIII-2.1", "VIII-4.2"], 2, "Atinge pe hartă orașul nostru, Râmnicu Sărat.", "romania", 45.38, 27.06, "Râmnicu Sărat", 35,
   "Corect.", "Râmnicu Sărat e în nord-estul Câmpiei Române, la contactul cu Subcarpații de Curbură, între Buzău și Focșani.",
   indiciu="Caută la nord-est de Buzău, aproape de curbura Carpaților."),
 etichete("E10-04", E10, ["VIII-2.1"], 2, "Pune numele orașelor din Câmpia Română pe hartă.",
   [{"id": "craiova", "eticheta": "Craiova", "lat": 44.32, "lon": 23.80}, {"id": "bucuresti", "eticheta": "București", "lat": 44.43, "lon": 26.10},
    {"id": "buzau", "eticheta": "Buzău", "lat": 45.15, "lon": 26.82}, {"id": "slobozia", "eticheta": "Slobozia", "lat": 44.56, "lon": 27.37}],
   "Bravo!", "Craiova e în vest, Bucureștiul în centru, Slobozia în Bărăgan, Buzăul în nord-est.", harta="romania"),
 alegere("E10-05", E10, ["VIII-1.1"], 1, "Care este cea mai întinsă câmpie a României?", ["Câmpia Română", "Câmpia de Vest", "Câmpia Moldovei", "Câmpia Transilvaniei"],
   "Corect.", "Câmpia Română e cea mai întinsă câmpie a țării."),
 alegere("E10-06", E10, ["VIII-1.1", "VIII-3.3"], 2, "Ce rocă afânată, gălbuie, acoperă mare parte din Câmpia Română?", ["loessul", "granitul", "marmura", "bazaltul"],
   "Corect.", "Loessul e o rocă afânată, gălbuie, pe care s-au format soluri fertile."),
 alegere("E10-07", E10, ["VIII-3.3"], 2, "Ce soluri foarte fertile s-au format în Câmpia Română?", ["cernoziomurile", "solurile de tundră", "solurile nisipoase de deșert", "solurile de munte"],
   "Corect.", "Cernoziomurile sunt cele mai fertile soluri ale țării."),
 alegere("E10-08", E10, ["VIII-1.1"], 2, "Cum se numește vântul rece și uscat care bate iarna, dinspre est, în Bărăgan?", ["crivățul", "foehnul", "austrul", "musonul"],
   "Corect.", "Crivățul aduce iarna ger și viscol în estul țării."),
 ordoneaza("E10-09", E10, ["VIII-2.1"], 2, "Ordonează subunitățile Câmpiei Române de la vest la est.",
   ["Câmpia Olteniei", "Câmpia Burnasului", "Câmpia Vlăsiei", "Bărăganul"], "De la vest la est",
   "Corect.", "Olteniei e în vest, Bărăganul în est; Bucureștiul (Vlăsia) e între ele.", indiciu="Bucureștiul e în Câmpia Vlăsiei."),
 lacunar("E10-10", E10, ["VIII-1.2", "VIII-2.1"], 2, "Completează.",
   "Câmpia Română e mărginită la sud de fluviul {0}, iar la nord de Podișul Getic și de {1}.",
   ["Dunărea", "Subcarpați"], ["Prut", "Carpații Meridionali"], "Corect.", "La sud e Dunărea; la nord, Podișul Getic și Subcarpații."),
 alegere("E10-11", E10, ["VIII-3.2", "VIII-4.4"], 3, "De ce se fac irigații în estul Câmpiei Române?",
   ["clima e mai uscată și secetele sunt frecvente", "solul e prea fertil", "plouă prea mult", "câmpia e prea înaltă"],
   "Corect.", "Spre est clima devine mai uscată; fără irigații, secetele distrug recoltele."),
 alegere("E10-12", E10, ["VIII-1.1"], 2, "Ce sunt crovurile, tipice Bărăganului?", ["mici adâncituri rotunjite", "dealuri înalte", "lacuri de munte", "vulcani noroioși"],
   "Corect.", "Crovurile sunt adâncituri mici, rotunjite, formate în loess."),
 asociaza("E10-13", E10, ["VIII-4.3"], 3, "Asociază fiecare câmpie cu o caracteristică.",
   [["Câmpia de Vest", "influențe climatice oceanice"], ["Câmpia Română", "cea mai întinsă câmpie a țării"], ["Bărăganul", "crivăț și crovuri"]],
   "Corect.", "Vestul are influențe oceanice; Câmpia Română e cea mai întinsă; Bărăganul are crivăț și crovuri."),
 pin("E10-14", E10, ["VIII-2.1"], 3, "Atinge pe hartă Bărăganul.", "romania", 44.6, 27.4, "Bărăganul", 70,
   "Corect.", "Bărăganul e în estul Câmpiei Române, la vest de Dunăre, în jurul Sloboziei."),
]

# ============================================================ S11 Delta Dunării și platforma continentală
n11 = {
 "id": E11, "tip": "nivel", "titlu": "Delta Dunării și platforma continentală",
 "descopera": {"intrebare": "Cea mai nouă unitate de relief a României crește în fiecare an. Ce este și de ce crește?"},
 "invata": [
  {"titlu": "Delta Dunării",
   "text": "Delta e cea mai nouă unitate de relief: s-a format din aluviunile depuse de Dunăre la vărsarea în Marea Neagră, și încă se formează.\nDunărea se desparte în trei brațe: Chilia (în nord, la granița cu Ucraina, cu cel mai mare debit), Sulina (în centru, rectificat pentru nave) și Sfântu Gheorghe (în sud).\nUscatul e format din grinduri, fâșii mai înalte de nisip și aluviuni, ca Letea și Caraorman. În sud se află Lacul Razim. Poarta deltei e orașul Tulcea."},
  {"titlu": "Rezervație și platformă",
   "text": "În 1990, Delta a devenit Rezervație a Biosferei, iar în 1991 a intrat pe Lista Patrimoniului Mondial UNESCO.\nÎn fața Deltei și a Dobrogei, sub mare, se întinde platforma continentală a Mării Negre, cu adâncimi mici. Din ea se extrag petrol și gaze naturale."},
 ],
 "stiaiCa": "În Delta Dunării trăiesc peste 300 de specii de păsări, printre ele pelicanii.",
 "referintaProfesor": REF.format("Delta Dunării și platforma continentală a Mării Negre"),
}
i11 = [
 etichete("E11-01", E11, ["VIII-2.1"], 2, "Pune numele brațelor Dunării pe hartă.",
   [{"id": "chilia", "eticheta": "Brațul Chilia", "lat": 45.326, "lon": 28.982}, {"id": "sulina", "eticheta": "Brațul Sulina", "lat": 45.182, "lon": 29.511},
    {"id": "sfg", "eticheta": "Brațul Sfântu Gheorghe", "lat": 45.026, "lon": 29.281}],
   "Corect.", "Chilia e în nord, Sulina la mijloc, Sfântu Gheorghe în sud.", harta="romania", indiciu="Brațele, de la nord la sud: Chilia, Sulina, Sfântu Gheorghe."),
 pin("E11-02", E11, ["VIII-2.1"], 1, "Atinge pe hartă Delta Dunării.", "romania", 45.15, 29.3, "Delta Dunării", 55,
   "Corect.", "Delta e în extremitatea de est a țării, unde Dunărea se varsă în Marea Neagră."),
 pin("E11-03", E11, ["VIII-2.1"], 2, "Atinge pe hartă orașul Tulcea, poarta Deltei.", "romania", 45.18, 28.80, "Tulcea", 30,
   "Corect.", "Tulcea e pe Dunăre, chiar înainte ca fluviul să se despartă în brațe."),
 alegere("E11-04", E11, ["VIII-1.1"], 1, "Care este cea mai nouă unitate de relief a României?", ["Delta Dunării", "Munții Măcinului", "Câmpia Română", "Podișul Moldovei"],
   "Corect.", "Delta e cea mai nouă unitate de relief și încă se formează."),
 alegere("E11-05", E11, ["VIII-1.1", "VIII-2.2"], 2, "Care braț al Dunării duce cea mai mare cantitate de apă?", ["Chilia", "Sulina", "Sfântu Gheorghe", "Borcea"],
   "Corect: aproximativ jumătate din debitul Dunării trece pe Chilia.", "Brațul Chilia, din nord, duce cam jumătate din apa Dunării.", surse=SURSE["CHILIA"]),
 alegere("E11-06", E11, ["VIII-1.1"], 2, "Ce braț a fost rectificat (îndreptat) pentru navele maritime?", ["Sulina", "Chilia", "Sfântu Gheorghe", "niciunul"],
   "Corect.", "Brațul Sulina a fost îndreptat și adâncit pentru navigație."),
 ordoneaza("E11-07", E11, ["VIII-2.1"], 1, "Ordonează brațele Dunării de la nord la sud.", ["Chilia", "Sulina", "Sfântu Gheorghe"], "De la nord la sud",
   "Corect.", "Chilia (nord), Sulina (centru), Sfântu Gheorghe (sud)."),
 alegere("E11-08", E11, ["VIII-1.1"], 2, "Ce sunt grindurile din Deltă?",
   ["fâșii de uscat mai înalte, din nisip și aluviuni", "lacuri adânci", "canale săpate de om", "insule vulcanice"],
   "Corect.", "Grindurile sunt fâșii mai înalte de uscat, ca Letea și Caraorman."),
 asociaza("E11-09", E11, ["VIII-1.2"], 2, "Asociază fiecare element cu o caracteristică.",
   [["Brațul Chilia", "la granița cu Ucraina"], ["Brațul Sulina", "rectificat pentru navigație"], ["Brațul Sfântu Gheorghe", "brațul din sud"], ["Grindul Letea", "pădure pe nisipuri"]],
   "Bravo!", "Chilia e la graniță, Sulina e pentru nave, Sfântu Gheorghe e la sud; pe grindul Letea crește o pădure."),
 lacunar("E11-10", E11, ["VIII-3.4"], 2, "Completează.",
   "Delta Dunării a devenit Rezervație a Biosferei în anul {0} și a intrat pe Lista Patrimoniului Mondial UNESCO în anul {1}.",
   ["1990", "1991"], ["1989", "2007"], "Corect.", "Rezervație a Biosferei: 1990; patrimoniu UNESCO: 1991.", surse=SURSE["DELTA_ANI"]),
 alegere("E11-11", E11, ["VIII-3.1"], 3, "De ce Delta Dunării înaintează treptat spre mare?",
   ["Dunărea depune aluviuni la vărsare", "nivelul mării scade mult în fiecare an", "vântul aduce nisip din deșert", "o ridică mișcările vulcanice"],
   "Corect.", "Aluviunile aduse de Dunăre se depun la vărsare și formează uscat nou."),
 alegere("E11-12", E11, ["VIII-1.1", "VIII-3.1"], 2, "Ce se exploatează pe platforma continentală a Mării Negre?", ["petrol și gaze naturale", "cărbune", "aur", "sare gemă"],
   "Corect.", "Pe platforma continentală se extrag petrol și gaze naturale."),
 alegere("E11-13", E11, ["VIII-2.1"], 2, "Cum se numește lacul mare din sudul Deltei, desprins din mare?", ["Lacul Razim", "Lacul Sfânta Ana", "Lacul Bâlea", "Lacul Snagov"],
   "Corect.", "Razim e un lac lagunar mare din sudul Deltei."),
 alegere("E11-14", E11, ["VIII-4.4"], 3, "Care măsură protejează Delta Dunării?",
   ["interzicerea pescuitului în perioada de reproducere a peștilor", "desecarea lacurilor pentru agricultură", "construirea de hoteluri pe grinduri", "aducerea de specii străine de pești"],
   "Corect.", "Desecările, construcțiile și speciile străine strică ecosistemul. Pauza de pescuit lasă peștii să se înmulțească."),
]

# ============================================================ S12 Expediție
n12 = {
 "id": E12, "tip": "expeditie", "titlu": "Expediție: relieful și riscurile județului Buzău",
 "descopera": {"intrebare": "În același județ ai munți, dealuri și câmpie. Ce riscuri aduce fiecare?"},
 "invata": [{"titlu": "Ce faci în expediție", "text": "Citești un profil de relief, cunoști riscurile din orizontul local, recapitulezi regulile pentru cutremur și explici rolul reliefului în dezvoltarea orașului nostru."}],
 "pasi": [
  {"titlu": "1. Treptele de relief ale județului", "text": "Județul Buzău coboară de la munte, prin Subcarpații de Curbură, până în Câmpia Română.", "itemi": ["E12-01", "E12-02"]},
  {"titlu": "2. Riscurile din orizontul local", "text": "În zona noastră se întâmplă cutremure (zona Vrancea), alunecări de teren pe dealuri, inundații și secete.", "itemi": ["E12-03", "E12-04"],
   "jurnal": {"cerinta": "Descrie un loc din localitatea ta unde ai văzut urme de alunecare, de inundație sau de secetă (fără adrese exacte). Ce măsură ai propune?", "foto": True}},
  {"titlu": "3. Cutremurele în România", "text": "Cele mai multe cutremure puternice din România se produc în zona Vrancea, la adâncimi mari.", "itemi": ["E12-05"]},
  {"titlu": "4. Rolul reliefului", "text": "Gândește-te de ce s-au dezvoltat așezări la contactul dintre deal și câmpie.",
   "jurnal": {"cerinta": "Explică în 4–5 propoziții cum influențează relieful drumurile, agricultura și construcțiile din județul nostru."}},
 ],
 "referintaProfesor": REF.format("Aplicații practice: profile geografice; relieful județului natal; riscuri"),
}
i12 = [
 ordoneaza("E12-01", E12, ["VIII-2.2", "VIII-4.2"], 2, "Ordonează unitățile de relief pe care le traversezi prin județul Buzău, de la nord-vest la sud-est.",
   ["Carpații de Curbură", "Subcarpații de Curbură", "Câmpia Română"], "De la nord-vest la sud-est",
   "Corect: de la munte spre câmpie.", "Coborând de la nord-vest: munții, apoi Subcarpații, apoi câmpia."),
 alegere("E12-02", E12, ["VIII-3.4"], 2, "Ce fenomen natural rar poți vedea în județul Buzău, la Berca–Pâclele?", ["vulcanii noroioși", "ghețarii", "gheizerele fierbinți", "dunele de nisip"],
   "Corect.", "Vulcanii noroioși sunt un fenomen rar; zona e arie protejată.", surse=["Euronews România – Buzău, județul vulcanilor noroioși", "Adevărul (ediția Buzău) – Vulcanii Noroioși"]),
 alegere("E12-03", E12, ["VIII-4.4"], 2, "Ce măsură reduce riscul de alunecare pe un versant?", ["plantarea de arbori pe versant", "tăierea pădurii", "arătura din deal spre vale", "construirea de case grele pe margine"],
   "Corect.", "Rădăcinile copacilor țin solul. Tăierea pădurii și arătura pe direcția pantei cresc riscul."),
 alegere("E12-04", E12, ["VIII-4.4"], 2, "Ce faci dacă se anunță cod roșu de inundații în zona ta?",
   ["urmezi indicațiile autorităților și te muți pe un loc mai înalt", "mergi să filmezi râul de aproape", "traversezi podul ca să vezi apa", "rămâi la subsol"],
   "Corect.", "La cod roșu urmezi indicațiile autorităților și stai departe de râu, pe un loc mai înalt."),
 alegere("E12-05", E12, ["VIII-3.2", "VIII-4.4"], 2, "Unde se produc cele mai multe cutremure puternice din România?", ["în zona Vrancea, la curbura Carpaților", "în Delta Dunării", "în Câmpia de Vest", "în Munții Măcinului"],
   "Corect, chiar lângă județul nostru.", "Zona seismică Vrancea e la curbura Carpaților, aproape de Râmnicu Sărat."),
]

boss8 = [{"id": "VIII-T2", "test": "T2", "titlu": "Boss T₂: Câmpii, podișuri și Delta", "saptamana": 11, "niveluri": [E8, E9, E10, E11]}]
idx = {"clasa": 8, "fisiere": [scrie(8, "u2-relief.json", "Relieful României", [n8, n9, n10, n11, n12], i8 + i9 + i10 + i11 + i12)]}
json.dump(idx, open(f"{ROOT}/clasa-8/index.json", "w"), ensure_ascii=False, indent=1)
print("clasa 8:", sum(len(x) for x in [i8, i9, i10, i11, i12]), "itemi")
