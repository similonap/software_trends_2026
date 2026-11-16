"""Slides 31-59: de vijf trends van 2025-2026, vooruitblik, begrippenlijst en conclusie."""
from helpers import *

B = []

# ======================= Trend 1: Wasm 3.0 =======================
B.append(divider('div-1', 'Trend 1', 'Wasm 3.0 en WasmGC',
    'De grootste uitbreiding van de standaard sinds de eerste versie',
"""We beginnen aan het tweede deel van de les, met vijf trends. De eerste gaat over de standaard zelf. Op 17 september 2025 is WebAssembly 3.0 officieel de nieuwe live-standaard geworden. Het is de grootste uitbreiding sinds de eerste versie.

Wat opvalt, is dat het geen losse nieuwe trucjes zijn. De meeste functies zaten al jaren in de browsers en zijn nu samen gestandaardiseerd. Het belangrijkste daarvan is WasmGC, garbage collection voor Wasm. Dat is de reden waarom we bij de vergelijking met de JVM zeiden dat garbage collection in Wasm nu optioneel is.""",
["Tweede deel: vijf trends",
 "Trend 1: Wasm 3.0, officieel sinds 17 september 2025",
 "Grootste uitbreiding sinds de eerste versie; veel functies zaten al jaren in browsers",
 "Belangrijkste: WasmGC",
 "→ Wat zit er allemaal in?"]))

B.append(slide('w3-overzicht', 'Wasm 3.0: tien nieuwe functies in gewone taal',
    tabel(['Functie', 'Wat doet het, in één zin?'],
          [['**1. Automatische opruiming** (WasmGC)', 'De browser ruimt het geheugen op, zodat meer programmeertalen kunnen meedoen'],
           ['**2. Duidelijke verwijzingen** (typed references)', 'Wasm weet precies waar een verwijzing naartoe gaat: sneller en veiliger'],
           ['**3. Meer geheugen** (memory64)', 'Programma\'s mogen veel meer dan 4 GB gebruiken'],
           ['**4. Meerdere geheugens**', 'Een programma kan zijn data netjes in aparte blokken bewaren'],
           ['**5. Foutafhandeling** (exceptions)', 'Fouten kunnen rechtstreeks in Wasm opgevangen worden'],
           ['**6. Recursie zonder crash** (tail calls)', 'Functies die zichzelf blijven aanroepen lopen niet vast'],
           ['**7. Veel getallen tegelijk** (relaxed SIMD)', 'Rekenwerk gaat sneller doordat de processor meerdere waarden tegelijk verwerkt'],
           ['**8. Altijd dezelfde uitkomst** (deterministic profile)', 'Op elke computer exact hetzelfde resultaat'],
           ['**9. Extra info in de code** (annotations)', 'Notities voor tools in de leesbare tekstversie'],
           ['**10. Tekst delen met JavaScript** (string builtins)', 'Wasm gebruikt de tekst van JavaScript rechtstreeks']], [44, 56], size=26),
"""Dit zijn de tien nieuwe functies van Wasm 3.0, in gewone taal. Je hoeft de technische namen niet van buiten te kennen. Belangrijker is dat je begrijpt wat het probleem was, wat er nu kan en waarom dat interessant is.

Grofweg zijn er drie groepen. De eerste groep maakt Wasm geschikt voor meer programmeertalen en grotere programma's: automatische opruiming, duidelijke verwijzingen, meer geheugen en meerdere geheugens. De tweede groep maakt programma's sneller en robuuster: foutafhandeling, recursie zonder crash en veel getallen tegelijk. De derde groep gaat over betrouwbaarheid en gebruiksgemak: altijd dezelfde uitkomst, extra info in de code en tekst delen met JavaScript.

We nemen ze één voor één door, telkens op dezelfde manier: wat was het probleem, wat kan er nu, waarom is het interessant en wie gebruikt het. De meeste functies zitten al in de grote browsers.""",
["Tien functies; geen technische namen van buiten leren, wel begrijpen wat ze oplossen",
 "Groep 1: meer talen en grotere programma's (opruiming, verwijzingen, meer geheugen, meerdere geheugens)",
 "Groep 2: sneller en robuuster (fouten, recursie, veel getallen tegelijk)",
 "Groep 3: betrouwbaarheid en gebruiksgemak (altijd dezelfde uitkomst, extra info, tekst delen)",
 "Per functie: probleem, wat kan er nu, waarom interessant, wie gebruikt het",
 "→ Functie 1: automatische opruiming"],
bron='webassembly.org/news/2025-09-17-wasm-3.0'))

B.append(eenvoudig('kb-wasmgc', 'Functie 1: automatische opruiming (WasmGC)',
    'Veel programmeertalen ruimen zelf op wat het programma niet meer nodig heeft. Dat heet **garbage collection**. Wasm laat de **browser** dat doen.',
    'Elke taal (Kotlin, Java, Dart) moest haar **eigen opruimsysteem meebrengen**. Dat maakte programma\'s **groot en traag om te starten**.',
    'De taal gebruikt het opruimsysteem van de **browser**. Programma\'s zijn **kleiner en starten sneller**.',
    'Veel meer talen kunnen **zonder grote omweg** naar het web.',
    'Bedrijven met **bestaande Kotlin-, Java- of Dart-apps**, zoals JetBrains en Google (Flutter).',
    'een gedeelde schoonmaakploeg in een kantoorgebouw, in plaats van dat elk bedrijf zijn eigen poetsploeg meebrengt.',
"""De eerste en belangrijkste nieuwe functie: automatische opruiming, in het Engels WasmGC, garbage collection voor Wasm.

Het probleem eerst. Veel programmeertalen, zoals Java, Kotlin en Dart, ruimen zelf het geheugen op dat het programma niet meer nodig heeft. In C ben je daar zelf verantwoordelijk voor. Om zo'n taal naar Wasm te brengen, moest je vroeger het hele opruimsysteem van die taal meecompileren. Dat maakte de bestanden groot en de opstart traag.

Nu kan Wasm het opruimen overlaten aan de browser, die dat al kan voor JavaScript. Denk aan een kantoorgebouw met één gedeelde schoonmaakploeg, in plaats van dat elk bedrijf zijn eigen poetsploeg meebrengt. Het resultaat: kleinere en snellere programma's.

Waarom is dat interessant? Veel meer programmeertalen kunnen nu zonder grote omweg naar het web. En wie gebruikt het? Bedrijven met bestaande apps in Kotlin, Java of Dart, zoals JetBrains en Google met Flutter, die hun app ook als website willen aanbieden. Talen als C en Rust hebben het niet nodig.""",
["Probleem: talen met automatische opruiming (Kotlin, Java, Dart) moesten hun eigen systeem meebrengen → groot en traag",
 "Nu: de browser doet het opruimen (zoals voor JavaScript) → kleiner en sneller",
 "Interessant: veel meer talen kunnen naar het web",
 "Wie: bedrijven met Kotlin-, Java- of Dart-apps (JetBrains, Google Flutter); C en Rust hebben het niet nodig",
 "Vergelijking: gedeelde schoonmaakploeg i.p.v. elk zijn eigen poetsploeg",
 "Examen: kunnen uitleggen wat garbage collection is en waarom het in de browser beter is",
 "→ Duidelijke verwijzingen"],
kern=True))

B.append(eenvoudig('w3-typed-refs', 'Functie 2: duidelijke verwijzingen (typed references)',
    'Wasm kan nu **precies beschrijven waar een verwijzing naartoe wijst**: naar welk soort functie of gegeven.',
    'De browser moest **tijdens het draaien controleren** of een verwijzing wel klopte. Dat kostte tijd.',
    'Dat is **vooraf al gecontroleerd**. Tijdens het draaien hoeft er **niets meer nagekeken** te worden.',
    '**Sneller en veiliger**. Het is ook de basis waarop functie 1 werkt.',
    'Vooral **mensen die programmeertalen en compilers bouwen**. Gebruikers merken het aan **snellere apps**.',
    'een pakket met een duidelijk label: je hoeft het niet open te maken om te weten wat erin zit.',
"""Functie twee: duidelijke verwijzingen, in het Engels typed references.

Een verwijzing is een soort wegwijzer naar een stuk data of een functie. Vroeger wist Wasm niet precies waar zo'n wegwijzer naartoe wees. De browser moest daarom tijdens het draaien telkens controleren of alles klopte. Dat kost tijd.

Nu kan een verwijzing precies beschrijven waar ze naartoe wijst. De controle gebeurt vooraf, één keer, en daarna is het veilig. Denk aan een pakket met een duidelijk label: je hoeft het niet meer open te maken om te weten wat erin zit.

Waarom is dat interessant? Het maakt programma's sneller en veiliger. En het is de basis waarop de vorige functie, automatische opruiming, werkt. Wie gebruikt het? Vooral de mensen die programmeertalen en compilers bouwen. Als gebruiker merk je het onrechtstreeks: apps in talen als Kotlin en Dart draaien sneller. Je hoeft dit als student niet te kennen tot in de details.""",
["Verwijzing = wegwijzer naar data of een functie",
 "Vroeger: browser moest tijdens het draaien controleren of het klopte",
 "Nu: duidelijk beschreven en vooraf gecontroleerd → sneller en veiliger",
 "Basis voor automatische opruiming (functie 1)",
 "Wie: bouwers van talen en compilers; gebruikers merken snellere apps",
 "Vergelijking: pakket met duidelijk label",
 "→ Wat gebeurt er met talen die dit gebruiken?"]))

B.append(slide('w3-talen', 'Welke talen profiteren van automatische opruiming?',
    p('Talen die zelf het geheugen opruimen kunnen nu **veel beter** naar Wasm.', 42)
    + ul(['**Kotlin** (Android-wereld): in **bèta**, ook voor webapps met Compose Multiplatform',
          '**Dart** (Flutter): apps voor mobiel én web met één codebase',
          '**Java**, **OCaml**, **Scala** en **Scheme**: ook op weg',
          '**Voorzichtig**: oudere browsers ondersteunen het nog niet; voorzie een **alternatief**'], size=40)
    + spacer()
    + p('Praktisch effect: **één codebase** voor mobiele app, desktop en website.', 36, '#595959'),
"""Welke talen profiteren hiervan? Alle talen die zelf het geheugen opruimen. Het bekendste voorbeeld is Kotlin, de taal van veel Android-apps. Kotlin voor Wasm is nog in bèta, en samen met Compose Multiplatform kan je een app voor mobiel, desktop en web met één codebase maken. Ook Dart, de taal achter Flutter, gebruikt het. Daarnaast zijn Java, OCaml, Scala en Scheme op weg.

Eén waarschuwing: oudere browsers ondersteunen deze functie nog niet. Als je zo'n app publiceert, moet je voor die gebruikers een alternatief voorzien.

Het praktische effect voor bedrijven: één codebase voor de mobiele app, de desktopapp en de website. Dat bespaart veel ontwikkelwerk.""",
["Kotlin (bèta, Compose Multiplatform), Dart (Flutter), ook Java, OCaml, Scala, Scheme",
 "Oudere browsers: voorzie een alternatief",
 "Praktisch effect: één codebase voor mobiel, desktop en web",
 "→ Meer geheugen"],
bron='JetBrains (Kotlin 2.2.20, Compose Multiplatform 1.9.0); webassembly.org'))

B.append(eenvoudig('w3-memory64', 'Functie 3: meer geheugen (memory64)',
    'Een Wasm-programma mag nu **veel meer geheugen** gebruiken dan 4 GB.',
    'Maximaal **4 GB** geheugen per programma. Te weinig voor **grote bestanden en data**.',
    'Veel meer ruimte: in browsers **tot 16 GB**. Oude programma\'s werken gewoon verder.',
    'Grote projecten (video, 3D, grote databanken, AI-modellen) **passen er nu in**.',
    '**Video- en 3D-software**, **databanken in de browser** en **AI-toepassingen**.',
    'een bureau dat groter wordt: grote projecten passen er nu op.',
"""Functie drie: meer geheugen, memory64.

Vroeger mocht een Wasm-programma maximaal vier gigabyte geheugen gebruiken. Voor een gewone website is dat ruim voldoende. Maar voor video bewerken, 3D-modellen, grote databanken of AI-modellen is het te weinig.

Nu kan een programma veel meer geheugen gebruiken. In de browser is de grens 16 gigabyte. Bestaande programma's blijven gewoon werken: het is een keuze. Denk aan een bureau dat groter wordt: grote projecten passen er nu op.

Waarom is dat interessant? Zware toepassingen kunnen nu volledig in de browser draaien, zonder dat je alles in stukjes moet opdelen. Wie gebruikt het? Video- en 3D-software, databanken die in de browser draaien en AI-toepassingen. Een kleine kanttekening voor later, bij security: nieuwe functies brengen soms ook nieuwe fouten mee, en de beveiligingsproblemen in Wasmtime van april 2026 gingen over precies deze functie.""",
["Vroeger: max. 4 GB per programma; nu veel meer (browsers: tot 16 GB)",
 "Oude programma's werken gewoon verder",
 "Interessant: video, 3D, databanken en AI-modellen kunnen volledig in de browser",
 "Wie: video-/3D-software, databanken in de browser, AI",
 "Kanttekening: nieuwe functie = nieuwe fouten (Wasmtime-problemen april 2026 → trend 4)",
 "Vergelijking: een groter bureau",
 "→ Meerdere geheugens"]))

B.append(eenvoudig('w3-multi-memory', 'Functie 4: meerdere geheugens',
    'Een Wasm-programma kan nu **meerdere aparte stukken geheugen** hebben.',
    'Eén groot blok geheugen voor **alles door elkaar**.',
    'Bijvoorbeeld een **privédeel** en een **gedeeld deel**, netjes gescheiden.',
    '**Veiliger en overzichtelijker**. Programma\'s zijn ook **makkelijker samen te voegen**.',
    '**Plug-in-systemen** en bedrijven die **onderdelen van verschillende teams** combineren.',
    'een eigen kluisje én een gedeeld postvak, in plaats van één grote doos voor alles.',
"""Functie vier: meerdere geheugens.

Een Wasm-programma had altijd één groot blok geheugen waar alles door elkaar in stond. Nu kan een programma meerdere aparte blokken hebben, bijvoorbeeld een privédeel dat alleen het programma zelf mag zien, en een gedeeld deel waarmee het met de buitenwereld praat. Denk aan een eigen kluisje en een gedeeld postvak, in plaats van één grote doos voor alles.

Waarom is dat interessant? Het is overzichtelijker en veiliger, en het wordt makkelijker om verschillende Wasm-onderdelen tot één programma samen te voegen. Wie gebruikt het? Vooral systemen met plug-ins, en bedrijven die onderdelen van verschillende teams combineren. Dit is een functie waar vooral de bouwers van tools blij mee zijn. Als gewone ontwikkelaar merk je er weinig van.""",
["Vroeger: één groot blok geheugen voor alles",
 "Nu: meerdere aparte blokken, bv. privé en gedeeld",
 "Interessant: overzichtelijker, veiliger, onderdelen makkelijker samenvoegen",
 "Wie: plug-in-systemen, bedrijven die onderdelen van verschillende teams combineren",
 "Vooral voor bouwers van tools; je merkt het als gewone ontwikkelaar weinig",
 "Vergelijking: kluisje + gedeeld postvak",
 "→ Foutafhandeling"]))

B.append(eenvoudig('w3-exceptions', 'Functie 5: foutafhandeling (exceptions)',
    'Als er iets misgaat, kan een programma een **fout melden** en die **elders netjes opvangen**. Wasm kan dat nu zelf.',
    'Fouten moesten via **JavaScript** nagebootst worden. Dat was **traag** en maakte programma\'s **groter**.',
    'Fouten worden **rechtstreeks in Wasm** afgehandeld: **sneller en compacter**.',
    'Bestaande software (vooral in **C++**) kan **makkelijker naar het web** zonder omwegen.',
    'Bedrijven die **bestaande software naar het web brengen**: **CAD**, **games**, **beeldbewerking**.',
    'een brandalarm dat rechtstreeks naar de brandweer gaat, in plaats van via een omweg.',
"""Functie vijf: foutafhandeling, in het Engels exception handling.

Bijna elke programmeertaal heeft een manier om te zeggen: hier is iets misgegaan, en iemand anders moet dat afhandelen. Zoals een brandalarm dat afgaat en bij de brandweer terechtkomt. In Wasm bestond dat niet. Programma's die het nodig hadden, zoals veel C++-software, moesten het nabootsen via JavaScript. Dat was traag en de programma's werden er groter van.

Nu kan Wasm het zelf, rechtstreeks, zonder omweg. Het resultaat is sneller en compacter.

Waarom is dat interessant? Bestaande software, vooral in C++, kan veel makkelijker naar het web gebracht worden. Wie gebruikt het? Bedrijven die zware, bestaande software naar de browser willen brengen: CAD-programma's, games, beeldbewerking. Voor jou als student is de boodschap: foutafhandeling werkt nu ook in Wasm, zoals je dat van andere talen gewend bent.""",
["Foutafhandeling = fout melden en elders netjes opvangen (zoals try/catch)",
 "Vroeger: nagebootst via JavaScript → traag en groter",
 "Nu: rechtstreeks in Wasm → sneller en compacter",
 "Interessant: bestaande (C++-)software makkelijker naar het web",
 "Wie: CAD, games, beeldbewerking",
 "Vergelijking: brandalarm rechtstreeks naar de brandweer",
 "→ Recursie"]))

B.append(eenvoudig('w3-tail-calls', 'Functie 6: recursie zonder crash (tail calls)',
    'Soms roept een functie **zichzelf opnieuw aan** (recursie). Wasm kan dat nu **heel vaak herhalen** zonder dat het geheugen vol loopt.',
    'Elke herhaling nam extra geheugen in. Na te veel herhalingen: **crash** (stack overflow).',
    'Bij de laatste aanroep wordt **dezelfde plek hergebruikt**. Het kan **eindeloos** doorgaan.',
    '**Geen crashes** en eenvoudiger programma\'s: je hoeft recursie niet meer te vermijden.',
    '**Functionele programmeertalen** (zoals OCaml en Scheme) en tools die **andere talen uitvoeren**.',
    'een lus: je blijft rondjes lopen in plaats van telkens een nieuwe trap te bouwen.',
"""Functie zes: recursie zonder crash, in het Engels tail calls.

Recursie betekent dat een functie zichzelf opnieuw aanroept, bijvoorbeeld om van een getal af te tellen tot nul. Vroeger nam elke aanroep extra geheugen in. Na een paar honderdduizend keer liep het geheugen vol en crashte het programma met een stack overflow.

Met tail calls herkent Wasm dat de laatste aanroep van een functie geen extra geheugen hoeft te kosten. Het hergebruikt gewoon dezelfde plek. Denk aan een lus: je blijft rondjes lopen in plaats van telkens een nieuwe trap te bouwen. Dan kan het in theorie eindeloos doorgaan.

Waarom is dat interessant? Geen crashes en eenvoudigere programma's. Wie gebruikt het? Vooral functionele programmeertalen zoals OCaml en Scheme, waar recursie de normale manier van herhalen is, en tools die andere programmeertalen uitvoeren.""",
["Recursie = functie roept zichzelf aan",
 "Vroeger: elke aanroep extra geheugen → na te veel herhalingen crash (stack overflow)",
 "Nu: laatste aanroep hergebruikt dezelfde plek → kan eindeloos doorgaan",
 "Interessant: geen crashes, eenvoudiger programma's",
 "Wie: functionele talen (OCaml, Scheme), tools die andere talen uitvoeren",
 "Vergelijking: rondjes lopen i.p.v. telkens een nieuwe trap bouwen",
 "→ Veel getallen tegelijk"]))

B.append(eenvoudig('w3-relaxed-simd', 'Functie 7: veel getallen tegelijk (relaxed SIMD)',
    'De processor doet **één bewerking op meerdere getallen tegelijk**. "Relaxed": de **laatste kommacijfers** mogen per computer **een beetje verschillen**.',
    'Getallen werden **één voor één** verwerkt, of er was **extra werk** om overal exact hetzelfde resultaat te krijgen.',
    'De processor gebruikt zijn **snelste manier**. De uitkomst kan **minimaal** verschillen.',
    '**Veel sneller** voor beeld, geluid en AI, waar zulke kleine verschillen niet uitmaken.',
    '**AI in de browser**, **foto- en videobewerking**, **games**.',
    'vier kassa\'s tegelijk open in plaats van één.',
"""Functie zeven: veel getallen tegelijk, in het Engels relaxed SIMD.

Moderne processors kunnen één bewerking op meerdere getallen tegelijk uitvoeren, bijvoorbeeld vier getallen optellen in één stap. Denk aan vier kassa's tegelijk open in plaats van één. Dat is erg handig voor beelden, geluid en AI, waar je met enorme hoeveelheden getallen werkt.

Relaxed betekent dat Wasm iets losser is over de uitkomst. Op verschillende computers mag het resultaat in de allerlaatste kommacijfers een heel klein beetje verschillen. In ruil daarvoor kan elke processor zijn snelste methode gebruiken.

Waarom is dat interessant? Voor een foto of een AI-model maakt zo'n minimaal verschil niet uit, maar de snelheidswinst is groot. Wie gebruikt het? AI in de browser, foto- en videobewerking en games. Voor een boekhoudprogramma zou je dit niet gebruiken, daar moet elk cijfer exact kloppen. Daarvoor is de volgende functie.""",
["Idee: één bewerking op meerdere getallen tegelijk",
 "Relaxed: laatste kommacijfers mogen per computer minimaal verschillen",
 "Interessant: veel sneller voor beeld, geluid en AI",
 "Wie: AI in de browser, foto-/videobewerking, games; niet voor boekhouding",
 "Vergelijking: vier kassa's tegelijk open",
 "→ Het tegenovergestelde: altijd dezelfde uitkomst"]))

B.append(eenvoudig('w3-deterministic', 'Functie 8: altijd dezelfde uitkomst (deterministic profile)',
    'Een **instelling** waarbij een programma op **elke computer exact hetzelfde resultaat** geeft.',
    'Op sommige plaatsen mocht het resultaat **per computer een beetje verschillen**.',
    'In deze modus ligt **alles vast**: dezelfde invoer geeft **overal dezelfde uitkomst**.',
    'Fouten zijn **altijd opnieuw op te roepen**, en je kan **tests betrouwbaar** uitvoeren.',
    '**Blockchains en smart contracts** (alle computers moeten hetzelfde uitrekenen) en **testsystemen**.',
    'een recept met exacte hoeveelheden: je krijgt altijd dezelfde taart.',
"""Functie acht is het tegenovergestelde van de vorige: altijd dezelfde uitkomst, in het Engels het deterministic profile.

Wasm is al bijna voorspelbaar: dezelfde code met dezelfde invoer geeft dezelfde uitkomst. Op een paar plaatsen mag het resultaat per computer een beetje verschillen, zoals we net bij relaxed SIMD zagen. Het deterministic profile is een instelling die dat weghaalt: alles ligt vast, en je krijgt op elke computer exact dezelfde uitkomst. Zoals een recept met exacte hoeveelheden: altijd dezelfde taart.

Waarom is dat interessant? Fouten zijn altijd opnieuw op te roepen, wat debuggen en testen veel makkelijker maakt. En soms is het noodzakelijk: bij blockchains moeten alle computers exact hetzelfde uitrekenen, anders is er geen akkoord. Wie gebruikt het? Blockchain- en smart-contractplatformen en testsystemen. Dat zijn typische voorbeelden. De prijs is dat je een stukje snelheid inlevert.""",
["Instelling: op elke computer exact hetzelfde resultaat",
 "Vroeger: op sommige plaatsen mocht het resultaat per computer verschillen",
 "Interessant: fouten altijd opnieuw op te roepen; betrouwbaar testen",
 "Wie: blockchains/smart contracts (typisch voorbeeld), testsystemen",
 "Prijs: een stukje snelheid",
 "Vergelijking: recept met exacte hoeveelheden",
 "→ Extra info in de code"]))

B.append(eenvoudig('w3-annotations', 'Functie 9: extra info in de code (annotations)',
    'Je kan **extra notities** in de leesbare tekstversie van Wasm zetten, bijvoorbeeld **namen**, die **tools** kunnen gebruiken.',
    'Zulke extra informatie zat enkel in het **binaire bestand**, niet in de leesbare versie.',
    'Ook in de **tekstversie** kan je ze schrijven en lezen. Beide versies blijven **hetzelfde betekenen**.',
    '**Makkelijker te debuggen**: je ziet leesbare namen in plaats van nummers.',
    '**Mensen die tools bouwen** (debuggers, compilers) en bedrijven die Wasm **willen controleren**.',
    'post-its op je code, speciaal voor je tools.',
"""Functie negen: extra informatie in de code, in het Engels custom annotations. Dit is de kleinste functie.

Een Wasm-bestand heeft twee vormen: een binair bestand dat de computer uitvoert en een leesbare tekstversie voor mensen. Het binaire bestand kan extra informatie bevatten die niet voor de computer bedoeld is, maar voor tools. Bijvoorbeeld de namen van functies. In de tekstversie kon je die info niet zetten.

Nu wel. Je kan extra notities in de tekstversie schrijven, als post-its op je code, speciaal voor je tools. Beide versies blijven hetzelfde betekenen.

Waarom is dat interessant? Programma's zijn makkelijker te debuggen, want je ziet leesbare namen in plaats van nummers. Wie gebruikt het? Vooral de mensen die tools bouwen, zoals debuggers en compilers, en bedrijven die Wasm-code willen controleren. Als gewone ontwikkelaar merk je er enkel iets van in betere tools.""",
["Wasm heeft een binaire versie en een leesbare tekstversie",
 "Extra info voor tools (bv. functienamen) kon enkel in het binaire bestand",
 "Nu ook in de tekstversie; beide betekenen hetzelfde",
 "Interessant: makkelijker debuggen (namen i.p.v. nummers)",
 "Wie: bouwers van debuggers/compilers; bedrijven die Wasm willen controleren",
 "Vergelijking: post-its voor je tools",
 "→ Tekst delen met JavaScript"]))

B.append(eenvoudig('w3-string-builtins', 'Functie 10: tekst delen met JavaScript (string builtins)',
    'Wasm kan nu de **tekst van JavaScript rechtstreeks gebruiken**.',
    'Wasm kende **geen tekst**, enkel getallen. Tekst moest **omgezet en gekopieerd** worden met extra **lijmcode**.',
    'Wasm en JavaScript **delen dezelfde tekst**. Geen omzetting of kopie meer nodig.',
    '**Minder lijmcode** en **sneller** bij alles wat met tekst te maken heeft.',
    '**Tekstverwerkers**, **document- en spreadsheetapps** en **zoekfuncties** in de browser.',
    'samen in hetzelfde document werken in plaats van elke keer een kopie op te sturen.',
"""Functie tien, de laatste: tekst delen met JavaScript, in het Engels JS string builtins.

Wasm kent eigenlijk alleen getallen. Tekst doorgeven aan Wasm betekende: de tekst omzetten naar getallen, in het geheugen zetten, en aan de andere kant weer omzetten. Dat vraagt extra code, de lijmcode waar we het in trend twee over hebben, en het kost tijd.

Nu kan Wasm rechtstreeks de tekst van JavaScript gebruiken. Zoals samen in hetzelfde document werken in plaats van elke keer een kopie op te sturen.

Waarom is dat interessant? Minder lijmcode en snellere programma's. Wie gebruikt het? Alles met veel tekst: tekstverwerkers, document- en spreadsheetapps en zoekfuncties in de browser. Het is een mooie kleine stap naar het grotere doel van trend twee: Wasm en JavaScript beter laten samenwerken.""",
["Wasm kent enkel getallen; tekst moest omgezet en gekopieerd worden (lijmcode)",
 "Nu: Wasm gebruikt de tekst van JavaScript rechtstreeks",
 "Interessant: minder lijmcode, sneller",
 "Wie: tekstverwerkers, document-/spreadsheetapps, zoekfuncties",
 "Stap richting beter samenwerken (trend 2)",
 "Vergelijking: samen in hetzelfde document werken",
 "→ Wat ondersteunt welke browser?"]))

B.append(slide('w3-support', 'Browser-support per functie (november 2026)',
    tabel(['Functie', 'Chrome', 'Firefox', 'Safari', 'Wasmtime'],
          [['**WasmGC**', '119', '120', '18.2', '47'],
           ['**Exception handling** (`exnref`)', '137', '131', '18.4', '47'],
           ['**Tail calls**', '112', '121', '18.2', '22'],
           ['**memory64**', '133', '134', '*achter vlag*', '30'],
           ['**Relaxed SIMD**', '114', '145', '*achter vlag*', '15'],
           ['**JS string builtins**', '130', '134', '26.2', 'n.v.t.'],
           ['**JSPI**', '137', '153', '27', 'n.v.t.'],
           ['**Stack switching**', '*achter vlag*', '–', '–', '–']], [34, 16, 16, 18, 16], size=29)
    + p('De kern is overal; **nieuwe functies** komen **per browser** op een ander moment. Gebruik **feature detection** (bv. `wasm-feature-detect`) en een fallback.', 31, '#C00000'),
"""Wasm 3.0 is een standaard, maar elke browser implementeert elke functie op haar eigen tempo. Deze tabel komt van de officiële feature-pagina op webassembly.org, en toont vanaf welke versie een functie standaard aanstaat.

Chrome en Firefox ondersteunen bijna alles. Safari volgt, maar later en niet volledig: WasmGC en tail calls sinds 18.2, exception handling sinds 18.4, de JS string builtins sinds 26.2 en JSPI sinds Safari 27. Memory64 en relaxed SIMD staan in Safari nog achter een vlag, dus voor gewone gebruikers niet beschikbaar. Wasmtime, de belangrijkste runtime buiten de browser, ondersteunt sinds versie 47 ook WasmGC en exception handling. De string builtins en JSPI zijn daar niet van toepassing, want die gaan over de koppeling met JavaScript. Stack switching, voor coroutines en lichtgewicht threads, staat zelfs in Chrome nog achter een vlag.

De conclusie staat onderaan. De kern van Wasm, de 97 procent van daarnet, is overal. Maar nieuwe functies komen per browser op verschillende momenten. Gebruik feature detection, bijvoorbeeld met de bibliotheek wasm-feature-detect van Google, en voorzie een fallback. En weet dat deze tabel snel veroudert.""",
["Bron: officiële feature-tabel webassembly.org/features (versie vanaf wanneer standaard aan)",
 "Chrome en Firefox: bijna alles; Safari later: GC en tail calls 18.2, exceptions 18.4, string builtins 26.2, JSPI 27",
 "Safari: memory64 en relaxed SIMD nog achter vlag; stack switching overal nog experimenteel",
 "Wasmtime 47: ook GC en exceptions; string builtins/JSPI n.v.t. (gaan over JS)",
 "Feature detection (wasm-feature-detect) + fallback; tabel veroudert snel",
 "→ Trend 2: waarom hebben we nog altijd lijmcode?"],
bron='webassembly.org/features (features.json, geraadpleegd 12/11/2026)'))

# ======================= Trend 2: glue code =======================
B.append(divider('div-2', 'Trend 2', 'Wasm als eersteklas webtaal',
    'Waarom hebben we nog altijd JavaScript als tussenpersoon nodig?',
"""Trend twee gaat over een probleem dat we al tegenkwamen: de lijmcode tussen WebAssembly en JavaScript. In februari 2026 schreef Mozilla op zijn blog dat WebAssembly nog altijd een tweederangs taal op het web is. We bekijken wat het probleem is en wat eraan gedaan wordt.""",
["Trend 2: Mozilla (feb. 2026): WebAssembly is nog 'second-class' op het web",
 "Wat is het probleem en wat wordt eraan gedaan?",
 "→ Wat is glue code?"]))

B.append(eenvoudig('kb-glue', 'Glue code: de lijm tussen WebAssembly en de browser',
    '**Glue code** is JavaScript die WebAssembly **laadt** en laat **praten met de browser**. Zonder die lijm kan WebAssembly de webpagina niet aanspreken.',
    'WebAssembly kan **enkel getallen** doorgeven. Voor tekst of een melding op het scherm is **extra JavaScript** nodig, per taal anders.',
    'Tools zoals **wasm-bindgen** (Rust) en **Emscripten** (C) **genereren die lijm** voor je. Het blijft wel **extra werk en extra code**.',
    'Het maakt WebAssembly **ingewikkelder** dan nodig en **iets trager**. Veel ontwikkelaars kiezen daarom gewoon JavaScript.',
    'Iedereen die WebAssembly in een website gebruikt, bv. **Figma** of een **zoekfunctie** in de browser.',
    'een tolk tussen twee mensen die een andere taal spreken: het werkt, maar kost tijd.',
"""De glue code, in gewone taal. WebAssembly kan de webpagina niet rechtstreeks aanspreken. Wil het iets tonen of een knop aanpassen, dan moet het langs JavaScript. Die tussenlaag heet glue code, lijmcode.

Het probleem: WebAssembly kent enkel getallen. Voor tekst, of een eenvoudige melding op het scherm, is extra JavaScript nodig. Gelukkig genereren tools als wasm-bindgen voor Rust en Emscripten voor C die lijm automatisch. Maar het blijft extra code, en het kost een beetje snelheid.

Waarom is dat belangrijk? Het maakt WebAssembly ingewikkelder dan nodig. Veel ontwikkelaars kiezen daarom gewoon JavaScript, ook als WebAssembly technisch beter zou passen. Dat is het argument van Mozilla: zolang WebAssembly een tolk nodig heeft, blijft het een gereedschap voor specialisten. Denk aan een tolk tussen twee mensen die een andere taal spreken: het werkt, maar het kost tijd.""",
["Glue code = JavaScript die WebAssembly laadt en laat praten met de browser",
 "Probleem: WebAssembly kent enkel getallen; tekst en schermacties vragen extra JavaScript, per taal anders",
 "Tools (wasm-bindgen, Emscripten) genereren de lijm, maar het blijft extra werk en een beetje trager",
 "Gevolg: veel ontwikkelaars kiezen gewoon JavaScript",
 "Vergelijking: een tolk tussen twee talen",
 "Examen: kunnen uitleggen wat glue code is en waarom ze een probleem is",
 "→ Wat wordt eraan gedaan?"],
kern=True, bron='Mozilla Hacks (02/2026)',
t1='Het probleem', t2='De huidige oplossing', t3='Waarom is dit een probleem?', t4='Wie heeft hier last van?'))

B.append(slide('glue-oplossingen', 'Wat wordt eraan gedaan?',
    p('De lijm wordt **stap voor stap kleiner**. Drie verbeteringen om te kennen:', 40)
    + '<div style="display:flex;gap:32px;align-items:stretch">'
    + card('1. Laden als gewone module', 'Een `.wasm`-bestand importeren zoals gewone JavaScript, zonder het laadwerk zelf te schrijven. **In aantocht.**', size=34)
    + card('2. Tekst delen', 'WebAssembly gebruikt de tekst van JavaScript rechtstreeks (functie 10). **Werkt al.**', size=34, fill='#E2EFDA', border='#70AD47', tc='#375623')
    + card('3. Wachten zonder vast te lopen', 'Een programma kan wachten op iets traags, zoals een netwerkverzoek (**JSPI**, volgende slide). **Werkt al.**', size=34, fill='#E2EFDA', border='#70AD47', tc='#375623')
    + '</div>'
    + spacer()
    + p('Het gaat vooral om **laden, tekst en wachten**: de saaie maar nuttige lijmwerk. Dat is de **realistische winst** op korte termijn.', 34, '#595959'),
"""Er zijn gelukkig verbeteringen onderweg, die de lijm stap voor stap kleiner maken. Drie om te kennen.

Eén: een wasm-bestand laden als een gewone module. Dat is nog in aantocht, maar bundlers en de JavaScript-tool Deno kunnen het al. Twee: tekst delen. WebAssembly gebruikt de tekst van JavaScript rechtstreeks, we zagen dat bij functie tien. Dat werkt al. Drie: wachten zonder vast te lopen, JSPI, dat we op de volgende slide uitleggen. Ook dat werkt al.

Merk op dat het vooral gaat over laden, tekst en wachten. Dat is het saaie maar nuttige lijmwerk, en dat is de realistische winst op korte termijn.""",
["Lijm wordt stap voor stap kleiner",
 "1. Laden als gewone module (in aantocht)",
 "2. Tekst delen met JavaScript (werkt al, functie 10)",
 "3. Wachten zonder vast te lopen: JSPI (werkt al)",
 "Vooral laden, tekst en wachten = realistische winst op korte termijn",
 "→ JSPI uitgelegd"],
bron='Mozilla Hacks (02/2026); Uno Platform (jan. 2026)'))

B.append(eenvoudig('kb-jspi', 'JSPI: wachten zonder vast te lopen',
    'Veel programma\'s **wachten** op een antwoord voor ze verdergaan. De browser werkt **anders**: hij doet intussen iets anders. **JSPI** verzoent die twee.',
    'Een speciale tool (**Asyncify**) schreef de code om zodat ze kon wachten. Het programma werd **groter en trager**.',
    'De browser **pauzeert** het programma tot het antwoord er is. **Geen omschrijving** meer nodig.',
    'Bestaande programma\'s (bv. **in C**) kunnen **zonder aanpassing** op netwerk of bestanden wachten.',
    'Teams die **bestaande software** naar het web brengen. Werkt sinds dit jaar in **alle grote browsers**.',
    'bij een restaurant bestellen en intussen iets anders doen, tot je eten er is.',
"""JSPI, een klein maar handig onderdeel. Veel bestaande programma's werken zo: vraag iets, wacht op het antwoord, ga dan verder. De browser werkt anders: hij vraagt iets en doet intussen iets anders, tot het antwoord er is.

Vroeger loste een tool, Asyncify, dat op door je programma te herschrijven. Dat maakte het groter en trager. Met JSPI pauzeert de browser het programma gewoon tot het antwoord er is, zonder dat je iets moet omschrijven. Denk aan een restaurant: je bestelt, doet intussen iets anders, en gaat verder zodra je eten er is.

Waarom is dat interessant? Bestaande programma's, bijvoorbeeld in C, kunnen zonder aanpassing wachten op netwerk of bestanden. JSPI werkt sinds dit jaar in alle grote browsers. Wil je ook oudere browsers ondersteunen, dan voorzie je nog een alternatief.""",
["Probleem: programma's wachten op antwoorden, de browser doet intussen iets anders",
 "Vroeger: Asyncify herschreef de code → groter en trager",
 "Nu: JSPI pauzeert het programma tot het antwoord er is",
 "Interessant: bestaande (C-)programma's zonder aanpassing; in alle grote browsers sinds dit jaar",
 "Voor oudere browsers: voorzie een alternatief",
 "Vergelijking: bestellen in een restaurant en intussen iets anders doen",
 "→ Wat met de DOM?"],
kern=True, bron='Uno Platform (jan. 2026); caniuse.com',
t1='Vroeger (Asyncify)', t2='Nu (JSPI)'))

B.append(slide('dom', 'En rechtstreeks de webpagina aanpassen (de DOM)?',
    p('**Nog niet.** En misschien nooit zoals je het verwacht.', 44)
    + ul(['De webpagina is **gemaakt voor JavaScript**; WebAssembly kent enkel getallen',
          'Elke koppeling moet **veilig** en **compatibel** blijven met alle bestaande websites',
          'In 2026 schrijf je dus **nog glue code**, maar **minder** dan vroeger',
          'Voor werk dat vooral de webpagina aanpast, blijft **JavaScript** de logische keuze'], size=38)
    + spacer()
    + p('WebAssembly is een **bouwsteen** in een webapp, **geen vervanger** van JavaScript.', 36, '#595959'),
"""Wanneer kan WebAssembly de webpagina rechtstreeks aanpassen, de DOM? Het eerlijke antwoord: nog niet, en misschien nooit zoals je het verwacht. De webpagina is gemaakt voor JavaScript, en WebAssembly kent enkel getallen. Elke koppeling moet bovendien veilig en compatibel blijven met alle bestaande websites.

In 2026 schrijf je dus nog lijmcode, maar minder dan vroeger. Er wordt gewerkt aan een standaard, het Component Model, dat we in trend drie zien, maar voor de browser is die nog niet klaar. Een onderzoeker schreef in 2025 zelfs dat dat misschien niet erg is.

De boodschap: voor werk dat vooral de webpagina aanpast, blijft JavaScript de logische keuze. WebAssembly is een bouwsteen in een webapp, geen vervanger.""",
["DOM-toegang: nog niet, en misschien nooit zoals verwacht",
 "Webpagina gemaakt voor JavaScript; elke koppeling veilig en compatibel",
 "2026: nog glue code, maar minder",
 "Voor DOM-werk: JavaScript; WebAssembly = bouwsteen, geen vervanger",
 "→ Trend 3: buiten de browser"],
bron='Mozilla Hacks (02/2026); ACM Queue (D. Ehrenberg, 2025)'))

# ======================= Trend 3: buiten de browser =======================
B.append(divider('div-3', 'Trend 3', 'Buiten de browser',
    'WASI, het Component Model, Wasmtime en WebAssembly op de server',
"""Trend drie is de belangrijkste verschuiving van de laatste jaren: WebAssembly verlaat de browser. In 2019 schreef Solomon Hykes, medeoprichter van Docker, dat Docker niet nodig geweest zou zijn als WebAssembly en WASI in 2008 bestaan hadden. We bekijken hoe WebAssembly buiten de browser met de computer praat, hoe onderdelen samenwerken, welke runtime erachter zit, en of het Docker echt kan vervangen.""",
["Trend 3: WebAssembly verlaat de browser",
 "2019: Solomon Hykes (Docker): met WASM en WASI hadden we Docker niet nodig gehad",
 "WASI, Component Model, Wasmtime, en: het nieuwe Docker?",
 "→ Eerst: WASI"]))

B.append(eenvoudig('kb-wasi', 'WASI: hoe WebAssembly met de computer praat',
    'Een WebAssembly-programma kan alleen **rekenen**. **WASI** is de **afspraak** waarmee het buiten de browser **bestanden, netwerk en de klok** kan gebruiken.',
    'Een gewoon programma kan **standaard alles** wat jij als gebruiker kan. Beperken moet je er **achteraf** bij doen.',
    'Een WebAssembly-programma kan **standaard niets**. Je geeft per keer **toestemming**: deze map, dit netwerkadres.',
    '**Veilig vanaf de start**: ook onbetrouwbare code kan weinig kwaad.',
    '**Servers**, **plug-in systemen** en **edge-platformen** die code van derden draaien.',
    'een gast in je huis die enkel de kamers mag betreden die jij openzet.',
"""WASI, de WebAssembly System Interface. Een WebAssembly-programma kan van zichzelf enkel rekenen. Zodra het een bestand wil lezen, het netwerk gebruiken of de klok vragen, heeft het een afspraak met het besturingssysteem nodig. Die afspraak heet WASI.

Het bijzondere is dat WebAssembly het omgekeerde doet van een gewoon programma. Een gewoon programma kan standaard alles wat jij als gebruiker kan, en beperken moet je er achteraf bij doen. Een WebAssembly-programma kan standaard niets. Je geeft per keer toestemming: deze ene map, dit ene netwerkadres. Denk aan een gast in je huis die enkel de kamers mag betreden die jij openzet.

Waarom is dat interessant? Het is veilig vanaf de start, dus ook onbetrouwbare code kan weinig kwaad. Servers, plug-in systemen en edge-platformen die code van derden draaien, gebruiken het daarom graag. Onderweg: WASI 0.1 in 2019, 0.2 in 2024, en 0.3 in juni 2026.""",
["WASI = afspraak waarmee WebAssembly buiten de browser bestanden, netwerk, klok gebruikt",
 "Gewoon programma: standaard alles; WebAssembly: standaard niets, toestemming per map/adres (capability)",
 "Interessant: veilig vanaf de start; wie: servers, plug-ins, edge",
 "Versies: 0.1 (2019), 0.2 (2024), 0.3 (juni 2026)",
 "Vergelijking: gast die enkel de kamers mag betreden die jij openzet",
 "Examen: WASI en het idee 'standaard niets toegestaan' (capability) kunnen uitleggen",
 "→ Onderdelen samenbrengen"],
kern=True, bron='wasi.dev/releases',
t1='Gewoon programma', t2='WebAssembly met WASI'))

B.append(eenvoudig('kb-component', 'Het Component Model: bouwstenen die in elkaar passen',
    'Het **Component Model** laat onderdelen in **verschillende programmeertalen** samenwerken, als **bouwstenen** met een gedeelde beschrijving.',
    'Onderdelen deelden **enkel getallen**. Tekst of lijsten moest je **zelf omzetten**, per taal anders (glue code).',
    'Een **gedeelde beschrijving** (WIT) zegt wat een onderdeel doet. Een onderdeel in **Rust** kan er een in **Python** aanroepen.',
    'Teams kiezen **per onderdeel de beste taal** en **hergebruiken** andermans onderdelen.',
    '**Serverplatformen** en **plug-in systemen**. Voor de browser nog **in ontwerp**.',
    'LEGO-blokjes met dezelfde noppen: elk blokje past op elk ander.',
"""Het Component Model, de standaard om onderdelen te laten samenwerken. Vroeger konden WebAssembly-onderdelen enkel getallen uitwisselen. Tekst of lijsten moest je zelf omzetten, en elke taal deed dat anders. Dat is dezelfde lijmcode als daarnet.

Nu kan je de interface van een onderdeel beschrijven in een gedeelde taal, WIT. Een onderdeel in Rust kan dan een onderdeel in Python aanroepen, met gewone tekst en lijsten. Denk aan LEGO-blokjes met dezelfde noppen: elk blokje past op elk ander.

Waarom is dat interessant? Teams kiezen per onderdeel de beste taal en hergebruiken onderdelen van anderen. Platformen en plug-in systemen op de server gebruiken het al. Voor de browser is het nog in ontwerp.""",
["Probleem: onderdelen delen enkel getallen; tekst/lijsten per taal anders omzetten",
 "Component Model: gedeelde beschrijving (WIT) van wat een onderdeel doet",
 "Rust-onderdeel kan Python-onderdeel aanroepen",
 "Interessant: beste taal per onderdeel, hergebruik; nu bruikbaar op de server, in de browser nog in ontwerp",
 "Vergelijking: LEGO-blokjes met dezelfde noppen",
 "Examen: Component Model en WIT kunnen uitleggen",
 "→ WASI 0.3"],
kern=True, bron='wasi.dev; Mozilla Hacks (02/2026)',
t1='Vroeger', t2='Nu'))

B.append(eenvoudig('wasi03', 'WASI 0.3 (juni 2026): wachten zonder te blokkeren',
    '**WASI 0.3** voegt **asynchroon werk** toe: een programma kan op iets traags **wachten** zonder de rest te **blokkeren**.',
    'Wachten op een netwerkverzoek ging via een **omslachtige** constructie die niet paste bij talen met **async en await**.',
    'Dat is nu **ingebouwd** in het Component Model. De runtime regelt het **plannen** voor je.',
    '**Natuurlijkere code** en servers die **veel verzoeken tegelijk** aankunnen.',
    '**Serverplatformen** en **edge-aanbieders**. **Wasmtime** ondersteunt het sinds versie 46.',
    'bij een restaurant bestellen en intussen iets anders doen, tot je eten er is.',
"""WASI 0.3 is op 11 juni 2026 verschenen. Het grote probleem van de vorige versie was wachten op iets traags, zoals een netwerkverzoek, zonder de rest te blokkeren. Dat kon wel, maar via een omslachtige constructie die slecht paste bij talen met async en await.

Nu is dat ingebouwd, en regelt de runtime het plannen voor je. Het resultaat: natuurlijkere code en servers die veel verzoeken tegelijk aankunnen. Wasmtime, de runtime die we zo meteen zien, ondersteunt het sinds versie 46.

Maar het is nog niet af. Sommige onderdelen, zoals threads, ontbreken nog, en over WASI 1.0 bestaat geen officiële datum. Het is dus nog volop in beweging.""",
["WASI 0.3: 11 juni 2026, asynchroon werk",
 "Vroeger: omslachtige constructie, past slecht bij async/await",
 "Nu: ingebouwd; runtime regelt het plannen",
 "Interessant: natuurlijkere code, servers met veel gelijktijdige verzoeken; Wasmtime sinds versie 46",
 "Nog niet af (threads); geen officiële datum voor WASI 1.0",
 "→ Wasmtime"],
bron='wasi.dev/releases/wasi-p3'))

B.append(eenvoudig('wasmtime', 'Wasmtime: de motor onder veel WebAssembly-servers',
    '**Wasmtime** is een programma dat **WebAssembly uitvoert buiten de browser**, zoals Chrome dat doet voor websites.',
    'Gemaakt door de **Bytecode Alliance** (open source) en geschreven in **Rust**.',
    'De **referentie voor WASI**: nieuwe functies komen er het **eerst**. WASI 0.3 standaard sinds versie 46.',
    'Een **belangrijke bouwsteen** onder veel serverplatformen: wie WebAssembly op de server draait, komt er **vaak** langs.',
    '**Spin**, **SpinKube** en Microsoft **Wassette** (AI-tools). Het **bewaakt de sandbox**: zijn beveiliging is cruciaal (trend 4).',
    'Chrome voor websites, maar voor WebAssembly op servers.',
"""Wasmtime is een naam die je vaak tegenkomt bij WebAssembly op de server, dus even apart. Wasmtime is een programma dat WebAssembly uitvoert buiten de browser, zoals Chrome dat doet voor websites. Het wordt gemaakt door de Bytecode Alliance, een open-sourceorganisatie, en is geschreven in Rust.

Waarom is het belangrijk? Het is de referentie voor WASI: nieuwe functies verschijnen er als eerste. Sinds versie 46 draait WASI 0.3 standaard, en sinds versie 47 ondersteunt het ook garbage collection en foutafhandeling. Wie WebAssembly op de server draait, komt er vaak langs. Spin en SpinKube gebruiken het, en ook Microsofts Wassette voor tools van AI-agents.

En nog iets interessants: omdat Wasmtime de sandbox bewaakt, is zijn beveiliging cruciaal. Dat zien we in trend vier, waar Wasmtime dit jaar meerdere beveiligingsproblemen had. Denk aan Chrome voor websites, maar dan voor WebAssembly-programma's op servers.""",
["Wasmtime = programma dat WebAssembly uitvoert buiten de browser (zoals Chrome voor websites)",
 "Gemaakt door de Bytecode Alliance (open source), geschreven in Rust",
 "Referentie voor WASI: nieuwe functies eerst; WASI 0.3 standaard sinds v46, GC en foutafhandeling sinds v47",
 "Gebruikt door Spin/SpinKube en Microsoft Wassette (AI-tools)",
 "Bewaakt de sandbox → beveiliging cruciaal (trend 4)",
 "Vergelijking: Chrome voor WebAssembly op servers",
 "→ Wie gebruikt WebAssembly nog meer op de server?"],
bron='wasi.dev/releases; github.com/bytecodealliance/wasmtime',
t1='Wat is het?', t2='Waarom belangrijk?', t3='Waarom interessant?', t4='Wie gebruikt het?'))

B.append(slide('server', 'Wie gebruikt WebAssembly op de server?',
    '<div style="display:flex;gap:32px;align-items:stretch">'
    + card('Platformen', 'Spin en SpinKube, wasmCloud, Cloudflare Workers. In december 2025 kocht **Akamai** het bedrijf achter Spin (**Fermyon**).', size=34)
    + card('Plug-in systemen', 'Code van derden veilig draaien: **Shopify Functions** (eigen logica in een webwinkel), filters voor de **Envoy**-proxy, extensies voor de editor **Zed**.', size=34)
    + card('Kleine toestellen', 'Een runtime die draait op toestellen met maar **256 kilobyte** geheugen.', size=34)
    + '</div>'
    + spacer()
    + p('Waarom? Een WebAssembly-programma is **klein**, **start in milliseconden**, draait op **elke processor** en is **veilig afgeschermd**.', 36, '#595959'),
"""Wie gebruikt WebAssembly nog meer op de server? Drie soorten. Platformen: Spin, wasmCloud en Cloudflare Workers. In december 2025 kondigde Akamai, een groot CDN-bedrijf, de overname aan van Fermyon, het bedrijf achter Spin. Dat is een signaal dat grote spelers WebAssembly zien als infrastructuur aan de rand van het netwerk.

Plug-in systemen: daar draait code van derden veilig in een sandbox. Shopify Functions laat webwinkels eigen logica toevoegen, de Envoy-proxy heeft WebAssembly-filters, en de editor Zed gebruikt het voor extensies. En kleine toestellen: er bestaat een runtime die draait op een toestel met maar 256 kilobyte geheugen.

Waarom kiezen mensen voor WebAssembly? Een programma is klein, start in milliseconden, draait op elke processor en is veilig afgeschermd.""",
["Platformen: Spin/SpinKube, wasmCloud, Cloudflare Workers; Akamai koopt Fermyon (dec. 2025)",
 "Plug-in systemen: Shopify Functions, Envoy-filters, Zed-extensies",
 "Kleine toestellen: runtime vanaf 256 KB",
 "Waarom: klein, milliseconden opstart, elke processor, veilig afgeschermd",
 "→ Is het dan het nieuwe Docker?"],
bron='akamai.com (01/12/2025); cncf.io; Uno Platform (jan. 2026)'))

B.append(slide('docker', 'Is WebAssembly het nieuwe Docker?',
    '<div style="display:flex;gap:32px;align-items:stretch">'
    + card('Container (Docker)', '**Volledige applicaties** met veel onderdelen', size=34)
    + card('WebAssembly', '**Kleine, snelle** functies en plug-ins', size=34, fill='#E2EFDA', border='#70AD47', tc='#375623')
    + '</div>'
    + tabel(['', 'Container', 'WebAssembly'],
            [['Start', 'seconden', '**milliseconden**'], ['Grootte', 'tientallen tot honderden MB', '**KB tot enkele MB**'],
             ['Ecosysteem', '**groot en volwassen**', 'jong, nog in beweging']], [26, 37, 37], size=34)
    + spacer()
    + p('**Conclusie:** ze vullen elkaar aan. WebAssembly draait zelfs **in** Kubernetes (via SpinKube). Het is **geen vervanging**, wel een extra gereedschap.', 34),
"""Is WebAssembly dan het nieuwe Docker? Kort: nee, ze vullen elkaar aan. Een container is ideaal voor volledige applicaties met veel onderdelen. WebAssembly is sterk voor kleine, snelle functies en plug-ins.

De tabel toont het verschil in orde van grootte. Een container start in seconden, een WebAssembly-programma in milliseconden. Een container is tientallen tot honderden megabytes groot, WebAssembly kilobytes tot enkele megabytes. Maar het ecosysteem van containers is veel groter en volwassener, dat is waar WebAssembly nog moet groeien. De cijfers zijn typische ordes van grootte, geen metingen.

WebAssembly draait zelfs in Kubernetes, via SpinKube. De uitspraak van Hykes uit 2019 is dus nog niet uitgekomen, maar ze wordt wel serieus genomen.""",
["Container: volledige applicaties; WebAssembly: kleine snelle functies en plug-ins",
 "Start: seconden vs. milliseconden; grootte: tientallen-honderden MB vs. KB-enkele MB; ecosysteem: groot vs. jong",
 "Tabel = ordes van grootte, geen metingen",
 "Conclusie: complementair; WebAssembly draait zelfs in Kubernetes (SpinKube)",
 "→ Trend 4: security"]))

# ======================= Trend 4: security =======================
B.append(divider('div-4', 'Trend 4', 'Security',
    'Veilig ontworpen, maar geen magie',
"""Trend vier gaat over beveiliging. WebAssembly is ontworpen met veiligheid als vertrekpunt, en dat is een groot deel van de reden waarom het zo aantrekkelijk is voor plug-ins en servers. Maar een sandbox is maar zo sterk als de runtime die ze bewaakt. Dit jaar zagen we daar voorbeelden van.""",
["Trend 4: WebAssembly is veilig ontworpen, maar...",
 "Een sandbox is zo sterk als de runtime die ze bewaakt",
 "→ Wat is een sandbox?"]))

B.append(eenvoudig('kb-sandbox', 'De sandbox: een afgesloten speelruimte',
    'Een **sandbox** is een **afgesloten ruimte** waarin code **enkel kan wat jij toestaat**.',
    'Een WebAssembly-programma kan **enkel in zijn eigen stukje geheugen** werken en **niet naar willekeurige plaatsen springen**.',
    'Zonder toestemming heeft het **geen toegang** tot bestanden, netwerk of de klok. In de browser gelden **dezelfde regels als voor JavaScript**.',
    'Je kan **code van derden draaien zonder erop te vertrouwen**: plug-ins, extensies, AI-code.',
    '**Browsers**, **plug-in systemen**, **edge-platformen** en **AI-toepassingen**.',
    'een speelkamer met hekjes: kinderen mogen vrij spelen, maar niet de straat op.',
"""Wat maakt WebAssembly veilig? Een sandbox is een afgesloten ruimte waarin code enkel kan wat jij toestaat. Voor WebAssembly betekent dat drie dingen. Het programma kan enkel in zijn eigen stukje geheugen werken. Het kan niet naar willekeurige plaatsen springen. En het heeft geen toegang tot bestanden, netwerk of klok, tenzij jij dat toestaat. In de browser gelden bovendien dezelfde regels als voor JavaScript.

Waarom is dat interessant? Je kan code van derden draaien zonder erop te vertrouwen, zoals plug-ins, extensies of door AI geschreven code. Denk aan een speelkamer met hekjes: kinderen mogen vrij spelen, maar niet de straat op.""",
["Sandbox = afgesloten ruimte; code kan enkel wat jij toestaat",
 "Enkel eigen geheugen; geen willekeurige sprongen; geen toegang zonder toestemming; in de browser dezelfde regels als JavaScript",
 "Interessant: code van derden draaien zonder erop te vertrouwen (plug-ins, extensies, AI-code)",
 "Vergelijking: speelkamer met hekjes",
 "Examen: sandbox kunnen uitleggen",
 "→ Maar de sandbox kan lekken"],
kern=True,
t1='Wat WebAssembly afdwingt', t2='Wat ze niet kan'))

B.append(eenvoudig('cve', 'Een sandbox is maar zo sterk als haar runtime',
    'In 2026 had **Wasmtime** meerdere **kritieke beveiligingsproblemen**: een kwaadaardig programma kon uit zijn sandbox **ontsnappen**.',
    '**April**: twee sandbox-escapes, enkel bij het **grote geheugen** (functie 3) of een niet-standaardinstelling. **Oktober**: twee **ernstigere**, in de **standaardinstelling**, score **9,9 op 10**.',
    '**Nieuwe functies** zijn **nieuwe aanvalsoppervlakken**, en een sandbox is zo sterk als de **compiler** van de runtime.',
    'Wie **niet-vertrouwde code** draait (plug-ins, AI-code) moet de runtime **tijdig updaten**.',
    'Enkel wie die **runtime** gebruikt, niet de **browsers**.',
    'een hek rond de speelkamer: sterk, maar een gat in het hek maakt het nutteloos.',
"""Hoe sterk is zo'n sandbox in de praktijk? Wasmtime, de runtime die we net zagen, publiceerde dit jaar meerdere beveiligingsadviezen. In april twee sandbox escapes, waarbij een kwaadaardig programma uit zijn sandbox kon ontsnappen. Die speelden enkel bij het grote geheugen, functie drie, of een niet-standaardinstelling. In oktober kwamen er twee ernstigere bij, met de hoogste score, negen komma negen op tien, en die gelden in de standaardinstelling.

Wat leren we? Nieuwe functies zijn nieuwe aanvalsoppervlakken. En een sandbox is zo sterk als de compiler van de runtime. Wie niet-vertrouwde code draait, zoals plug-ins of door AI geschreven code, moet de runtime tijdig updaten. Dit gaat over één runtime, niet over de browsers. Denk aan een hek rond de speelkamer: sterk, maar een gat in het hek maakt het nutteloos.""",
["2026: Wasmtime had meerdere kritieke beveiligingsproblemen: sandbox-escapes",
 "April: twee, enkel bij 64-bit geheugen (functie 3) of niet-standaardinstelling",
 "Oktober: twee ernstigere in de standaardinstelling, score 9,9 op 10",
 "Les: nieuwe functie = nieuw aanvalsoppervlak; sandbox is zo sterk als de runtime; updaten",
 "Gaat over één runtime, niet over de browsers",
 "→ Wat een sandbox niet oplost"],
bron='Wasmtime security advisories (CVE-2026-34971, CVE-2026-34987 en oktober 2026)',
t1='Wat gebeurde er?', t2='Wat leren we?', t3='Waarom is dit belangrijk?', t4='Wie is getroffen?', voet='Vergelijking: '))

B.append(slide('binnen-sandbox', 'Wat de sandbox niet oplost',
    '<div style="display:flex;gap:32px;align-items:stretch">'
    + card('Fouten binnenin de module', 'De sandbox beschermt de **computer** tegen de module, niet de module **tegen zichzelf**. Een C-programma met een **buffer overflow** heeft die ook in WebAssembly. Reden om voor **nieuwe code Rust** te verkiezen.', size=32)
    + card('Een .wasm is een dependency', 'Het is een **binair bestand**, moeilijk te controleren, en het zit vaak **in npm-packages**. Neem het mee in je **supply-chainbeleid**: vaste versie, integriteitscontrole, wachttijd voor nieuwe versies.', size=32)
    + '</div>'
    + spacer()
    + p('Een sandbox is een **extra laag**, geen vrijbrief.', 36, '#595959'),
"""Twee dingen die de sandbox niet oplost. Eén: fouten binnenin de module zelf. De sandbox beschermt de computer tegen de module, niet de module tegen zichzelf. Een C-programma met een buffer overflow heeft die ook in WebAssembly, binnen zijn eigen geheugen. Het is een extra reden om voor nieuwe code Rust te verkiezen.

Twee: een wasm-bestand is een dependency. Het is een binair bestand, moeilijk te controleren, en het zit vaak in npm-packages. Neem het daarom mee in je supply-chainbeleid, zoals we in de les over supply chain security zagen: een vaste versie, integriteitscontrole en een wachttijd voor nieuwe versies. Een sandbox is een extra laag, geen vrijbrief.""",
["Sandbox beschermt de computer tegen de module, niet de module tegen zichzelf",
 "C met buffer overflow → blijft bestaan in WebAssembly; reden voor Rust bij nieuwe code",
 "Een .wasm is een dependency: binair, moeilijk te controleren, vaak in npm-packages",
 "Neem mee in supply-chainbeleid (zie les supply chain)",
 "Sandbox = extra laag, geen vrijbrief",
 "→ Trend 5: AI"]))

# ======================= Trend 5: AI =======================
B.append(divider('div-5', 'Trend 5', 'Wasm en AI',
    'Modellen in de browser en een sandbox voor AI-agents',
"""De vijfde trend sluit aan bij de rode draad van dit vak: AI. WebAssembly komt op twee manieren in AI terecht. Ten eerste om kleine AI-modellen rechtstreeks in de browser uit te voeren. En ten tweede als sandbox voor code en tools van AI-agents.""",
["Trend 5: rode draad AI",
 "Twee rollen: modellen in de browser; sandbox voor AI-agents",
 "→ Eerst: modellen in de browser"]))

B.append(eenvoudig('ai-browser', 'AI in je browser: WebGPU en WebAssembly',
    'Kleine AI-modellen kunnen **volledig in je browser** draaien, zonder dat je gegevens naar een server gaan.',
    'Elke vraag ging naar een **server** van het AI-bedrijf.',
    'Het model draait op **jouw toestel**: met **WebGPU** (snel, op de grafische kaart) of **WebAssembly** (werkt overal, op de processor).',
    '**Privacy** (je data blijft bij jou), **geen serverkosten** en het werkt **offline**.',
    'Apps met **foto-, spraak- of tekstverwerking** op je toestel, via bibliotheken zoals **Transformers.js**.',
    'WebAssembly is het reservewiel: het werkt altijd, ook als WebGPU ontbreekt.',
"""De eerste rol van WebAssembly in AI: modellen in de browser. Kleine AI-modellen kunnen volledig in je browser draaien, zonder dat je gegevens naar een server gaan. Dat heeft drie voordelen: privacy, geen serverkosten en het werkt offline.

Hoe werkt dat? Een bibliotheek zoals Transformers.js voert het model uit met één van twee methodes. WebGPU is de snelle weg, op de grafische kaart. WebAssembly is de weg die overal werkt, op de processor, ook als WebGPU niet beschikbaar is. WebAssembly is dus het reservewiel. Je probeert eerst WebGPU, en valt terug op WebAssembly.

Een waarschuwing: online lees je dat WebGPU tien tot vijftien keer sneller zou zijn. Dat komt van blogs en leveranciers. Ik vond geen betrouwbare, onafhankelijke meting. Meet zelf.""",
["Kleine modellen volledig in de browser; data verlaat je toestel niet",
 "WebGPU = snel (grafische kaart); WebAssembly = overal (processor), reservewiel",
 "Interessant: privacy, geen serverkosten, offline; bv. Transformers.js",
 "Cijfers '10-15× sneller' = blogs/leveranciers; geen onafhankelijke meting → meet zelf",
 "→ Tweede rol: sandbox"],
bron='openreplay.com, sitepoint.com (2026); geen onafhankelijke benchmark',
t1='Vroeger', t2='Nu'))

B.append(eenvoudig('ai-sandbox', 'WebAssembly als sandbox voor AI-agents',
    'Een AI-agent **voert code uit** en gebruikt **tools**. Dat is **onbetrouwbare code**: ze moet in een **afgesloten ruimte** draaien.',
    'Door AI geschreven code of tools liepen met **te veel rechten** op de computer.',
    'Elke tool krijgt een **eigen sandbox** (start in milliseconden) en **enkel de toegang die nodig is**.',
    'Als de AI iets verkeerd doet, blijft de **schade beperkt**.',
    'Bedrijven met **AI-agents en tools**, bv. Microsofts **Wassette** (draait op Wasmtime).',
    'Let op: dit beschermt niet tegen **prompt injection** (een tool die de AI misleidt). Het is een laag, geen volledige oplossing.',
"""De tweede rol: een sandbox voor AI-agents. Een AI-agent voert code uit en gebruikt tools. Dat is onbetrouwbare code, want het model kan fouten maken of misleid worden. Die code hoort in een afgesloten ruimte.

WebAssembly past daar goed bij. Elke tool krijgt een eigen sandbox die in milliseconden start, en enkel de toegang die nodig is. Gaat de AI iets verkeerd doen, dan blijft de schade beperkt. Microsoft maakte in augustus 2025 Wassette, dat tools voor AI-agents als WebAssembly-onderdelen draait, bovenop Wasmtime.

Maar let op. Een sandbox beschermt tegen code die schade aanricht, niet tegen prompt injection, waarbij een tool het model misleidt. Dat probleem bespraken we in de les over web frameworks. Een sandbox is een beveiligingslaag, geen volledige oplossing.""",
["AI-agent voert code uit en gebruikt tools = onbetrouwbare code → afgesloten ruimte",
 "Vroeger: te veel rechten; nu: eigen sandbox per tool (ms-opstart), enkel nodige toegang",
 "Interessant: schade beperkt; wie: bedrijven met AI-agents, Microsoft Wassette (op Wasmtime)",
 "Let op: beschermt niet tegen prompt injection; beveiligingslaag, geen volledige oplossing",
 "→ Vooruitblik"],
bron='opensource.microsoft.com (Wassette, 06/08/2025); glama.ai (06/2026)',
t1='Vroeger', t2='Nu', voet=''))

# ======================= Afsluiting =======================
B.append(slide('roadmap', 'Vooruitblik: wat houden we in de gaten?',
    ul(['**WASI 1.0** en het **Component Model**: een stabiele basis voor WebAssembly op de server',
        '**WebAssembly laden als gewone module**: het einde van veel lijmcode',
        '**Safari** moet de laatste functies van Wasm 3.0 nog toevoegen',
        '**Kotlin** en **.NET** op WebAssembly: van bèta naar stabiel',
        '**Beveiligingsadviezen** van runtimes blijven opvolgen'], size=40)
    + spacer()
    + p('Dit zijn **verwachtingen**, geen zekerheden. WebAssembly gaat in **kleine stappen** vooruit.', 36, '#595959'),
"""Waar moet je op letten in het volgende jaar? Vijf dingen. WASI 1.0 en het Component Model, voor een stabiele basis op de server. WebAssembly laden als gewone module, het einde van veel lijmcode. Safari, dat de laatste functies van WebAssembly 3.0 nog moet toevoegen. Kotlin en .NET op WebAssembly, van bèta naar stabiel. En de beveiligingsadviezen van runtimes.

Dit zijn verwachtingen, geen zekerheden. WASI 0.3 verscheen bijvoorbeeld later dan eerst gepland. WebAssembly gaat in kleine stappen vooruit, niet in grote sprongen.""",
["WASI 1.0 en Component Model",
 "WebAssembly laden als gewone module → minder lijmcode",
 "Safari: laatste functies Wasm 3.0",
 "Kotlin en .NET: bèta → stabiel",
 "Beveiligingsadviezen opvolgen",
 "Verwachtingen, geen zekerheden; kleine stappen",
 "→ Wat kan je er zelf mee?"],
bron='wasi.dev; Uno Platform (jan. 2026); kotlinlang.org'))

B.append(slide('studenten', 'Wat kan je er zelf mee?',
    ul(['**Gebruik Wasm zonder het te schrijven**: SQLite, DuckDB, ffmpeg en Pyodide bieden een Wasm-versie',
        '**Probeer Rust + wasm-bindgen** voor een rekenintensief stuk van een bestaand project, en **meet** het resultaat',
        '**Feature detection en een fallback** voor nieuwe functies (WasmGC, JSPI, WebGPU)',
        '**Behandel `.wasm` als een dependency**: versie vastzetten, integriteit controleren',
        'Voer **niet-vertrouwde code** (plug-ins, AI-code) uit in een **Wasm-sandbox**, en **update** de runtime',
        '**Wees kritisch** over cijfers en benchmarks, ook die in deze les'], size=38)
    + spacer()
    + p('Wasm is geen doel op zich: het is een gereedschap voor **rekenwerk**, **hergebruik van bestaande code** en **veilige uitvoering**.', 36, '#595959'),
"""Wat kan je er zelf mee? Zes praktische tips.

Eén: gebruik Wasm zonder het zelf te schrijven. SQLite, DuckDB, ffmpeg en Pyodide bieden een Wasm-versie, en je kan ze gebruiken als een gewone bibliotheek. Twee: probeer Rust met wasm-bindgen voor een rekenintensief stuk van een bestaand project, en meet het resultaat. Meet voor en na, want je hebt gezien dat een overgang tussen JavaScript en Wasm niet gratis is. Drie: gebruik feature detection en een fallback voor nieuwe functies zoals WasmGC, JSPI en WebGPU. Vier: behandel een wasm-bestand als een dependency, met een vaste versie en integriteitscontrole. Vijf: voer niet-vertrouwde code, zoals plug-ins of door AI geschreven code, uit in een Wasm-sandbox en update de runtime. En zes: wees kritisch over cijfers en benchmarks, ook die in deze les.

De rode draad: Wasm is geen doel op zich. Het is een gereedschap voor rekenwerk, voor hergebruik van bestaande code en voor veilige uitvoering. Wie het zo bekijkt, kiest het op het juiste moment.""",
["Gebruik Wasm zonder het te schrijven (SQLite, DuckDB, ffmpeg, Pyodide)",
 "Rust + wasm-bindgen voor een rekenintensief deel; meet voor en na",
 "Feature detection + fallback; .wasm = dependency (versie, integriteit)",
 "Niet-vertrouwde code in een Wasm-sandbox; runtime updaten",
 "Kritisch zijn over cijfers en benchmarks",
 "Wasm = gereedschap voor rekenwerk, hergebruik, veilige uitvoering",
 "→ Begrippenlijst"]))

B.append(slide('begrippen-1', 'Begrippenlijst (1/2): basis',
    grid2(['**WebAssembly (Wasm)**: binair instructieformaat voor een virtuele machine; compilatiedoel voor vele talen',
           '**Compilatiedoel**: formaat waar een compiler naar vertaalt (x86, ARM, Wasm)',
           '**Interpreter**: vertaalt en voert code regel per regel uit',
           '**Compiler**: vertaalt alles vooraf naar machinecode en kan optimaliseren',
           '**JIT-compiler**: interpreteert, en compileert warme en hete code tijdens het draaien',
           '**Deoptimalisatie**: een JIT gooit geoptimaliseerde code weg omdat een aanname niet meer klopt',
           '**Assembly**: leesbare low-level taal, één-op-één met machinecode, per architectuur',
           '**Intermediate Representation (IR)**: tussenvorm tussen taal en machinecode (LLVM IR, JVM-bytecode, Wasm)',
           '**.wasm / .wat**: binair formaat / leesbaar tekstformaat',
           '**Emscripten**: LLVM-gebaseerde toolchain die C/C++ naar Wasm compileert',
           '**Glue code**: JavaScript die een Wasm-module laadt, data omzet en web-API\'s bereikbaar maakt',
           '**wasm-bindgen**: genereert bindings tussen Rust en JavaScript',
           '**Lineair geheugen**: het eigen geheugenblok van een Wasm-module (een rij bytes)',
           '**Streaming compilation**: compileren terwijl de module nog gedownload wordt'], size=27),
"""Dit is de eerste helft van de begrippenlijst, de basis uit het eerste deel. Je moet deze begrippen kunnen definiëren en met een voorbeeld kunnen uitleggen. Ik loop niet alles langs, want je hebt ze in de les gezien. Let vooral op de begrippen die bij elkaar horen: interpreter, compiler en JIT; assembly en IR; en glue code samen met wasm-bindgen en Emscripten. Het lineaire geheugen is het begrip dat in trend 4, over security, terugkomt.""",
["Basisbegrippen uit deel 1: Wasm, compilatiedoel, interpreter, compiler, JIT, deoptimalisatie, assembly, IR",
 ".wasm/.wat, Emscripten, glue code, wasm-bindgen, lineair geheugen, streaming compilation",
 "Examen: definitie + voorbeeld kunnen geven"]))

B.append(slide('begrippen-2', 'Begrippenlijst (2/2): de trends',
    grid2(['**WasmGC**: door de engine beheerde heap met structs en arrays; garbage collection voor Wasm',
           '**memory64**: Wasm-geheugen met 64-bit adressen (meer dan 4 GB)',
           '**Tail call**: aanroep op het einde van een functie die de stack hergebruikt',
           '**Exception handling**: native `throw` en `catch` in Wasm',
           '**SIMD**: één instructie op meerdere gegevens tegelijk',
           '**ESM-integratie / source phase imports**: een `.wasm` importeren als module',
           '**JSPI**: laat synchrone Wasm-code wachten op een JS-Promise',
           '**Asyncify**: oudere, tragere techniek die Wasm-code herschrijft om te kunnen pauzeren',
           '**WASI**: gestandaardiseerde systeeminterface voor Wasm buiten de browser',
           '**Capability**: expliciet meegegeven recht (een map, een socket); zonder capability geen toegang',
           '**Component Model**: standaard voor samenwerking tussen Wasm-modules met rijke types, over talen heen',
           '**WIT**: taalonafhankelijke notatie voor de interfaces van een component',
           '**Sandbox**: afgeschermde omgeving waarin code enkel kan wat is toegestaan',
           '**Runtime**: programma dat Wasm uitvoert (Wasmtime, WasmEdge, browser-engines)'], size=27),
"""De tweede helft van de begrippenlijst gaat over de trends. WasmGC, memory64, tail calls, exception handling en SIMD zijn de functies van Wasm 3.0. ESM-integratie, source phase imports, JSPI en Asyncify gaan over het verbinden met JavaScript. WASI, capability, het Component Model en WIT horen bij de server. En sandbox en runtime komen terug bij security.

Als je een begrip niet kan uitleggen, ga dan terug naar de slide met het label Kernbegrip. Alle begrippen met label staan in de cursustekst met een voorbeeld.""",
["Wasm 3.0: WasmGC, memory64, tail call, exception handling, SIMD",
 "Verbinden met JS: ESM-integratie/source phase imports, JSPI, Asyncify",
 "Server: WASI, capability, Component Model, WIT; security: sandbox, runtime",
 "Examen: definitie + voorbeeld kunnen geven"]))

B.append(slide('conclusie', 'Conclusie',
    ul(['**WebAssembly is een compilatiedoel**: veilig, snel en draagbaar, geen taal',
        '**Het vervangt JavaScript niet**: rekenwerk en hergebruik van bestaande code',
        '**Wasm 3.0**: WasmGC en meer; talen met garbage collector kunnen mee',
        '**Nog een tweederangs burger op het web**: de glue code wordt kleiner, maar verdwijnt niet',
        '**Buiten de browser** groeit het snel: WASI 0.3, Component Model, edge en plug-ins',
        '**Veilig by design**, maar de sandbox is zo sterk als de runtime',
        '**In AI**: vangnet voor modellen in de browser en sandbox voor niet-vertrouwde code'], size=38, ordered=True)
    + spacer()
    + p('Blijf kritisch: een snelle standaard is nog geen snelle toepassing.', 42, '#595959'),
"""Tot slot de conclusie. Zeven punten.

Eén: WebAssembly is een compilatiedoel, geen taal: veilig, snel en draagbaar. Twee: het vervangt JavaScript niet. Je gebruikt het voor rekenwerk en om bestaande code te hergebruiken. Drie: Wasm 3.0 in september 2025 bracht onder andere WasmGC, waardoor talen met een garbage collector, zoals Kotlin en Dart, kunnen meedoen. Vier: het is nog altijd een tweederangs burger op het web. De glue code wordt kleiner, maar verdwijnt niet, en directe DOM-toegang bestaat niet. Vijf: buiten de browser groeit het snel, met WASI 0.3, het Component Model, edge en plug-ins. Zes: het is veilig by design, maar de sandbox is zo sterk als de runtime: Wasmtime had dit jaar zelfs kritieke lekken in de standaardinstelling. Zeven: in AI is Wasm het vangnet voor modellen in de browser en een sandbox voor niet-vertrouwde code, zonder prompt injection op te lossen.

En onthoud de les van de benchmark: een snelle standaard is nog geen snelle toepassing. Meet altijd zelf. Bedankt voor jullie aandacht.""",
["1. Compilatiedoel, geen taal: veilig, snel, draagbaar",
 "2. Vervangt JS niet: rekenwerk en hergebruik",
 "3. Wasm 3.0: WasmGC → talen met GC kunnen mee",
 "4. Nog tweederangs op het web: glue code kleiner, geen DOM",
 "5. Buiten de browser: WASI 0.3, Component Model, edge, plug-ins",
 "6. Veilig by design; sandbox = zo sterk als runtime (Wasmtime: kritieke lekken in 2026)",
 "7. AI: vangnet voor modellen in de browser; sandbox voor niet-vertrouwde code",
 "Blijf kritisch: een snelle standaard is geen snelle toepassing"]))

B.append(slide('vragen', 'Vragen?',
    p('Discussie: zou jij Wasm gebruiken om **plug-ins van derden** in je applicatie te laten draaien, in plaats van een container of gewoon JavaScript?', 42)
    + p('Belangrijkste bronnen', 38, bold=True)
    + ul(['webassembly.org: *WebAssembly 3.0* (17/09/2025), *The States of WebAssembly* (21/01/2026), feature-tabel',
          'Uno Platform: *The State of WebAssembly, 2025 and 2026*; Web Almanac 2025 (WebAssembly); caniuse.com',
          'wasi.dev: WASI 0.3; Mozilla Hacks: *Making WebAssembly a first-class language on the Web* (02/2026)',
          'DevClass (28/01/2026); Akamai en Fermyon (01/12/2025); CNCF wasmCloud (12/11/2024)',
          'Wasmtime security advisories (2026); Microsoft Wassette (08/2025)',
          'Rust Blog: rustwasm sunset (07/2025); JetBrains: Kotlin 2.4, Compose Multiplatform 1.9.0'], size=30),
"""Dan zijn er nu vragen. Een discussievraag om mee te beginnen: zou je Wasm gebruiken om plug-ins van derden in je applicatie te laten draaien, in plaats van een container of gewoon JavaScript? Denk aan wat je vandaag hebt gezien: de sandbox, de capabilities, de opstarttijd, maar ook de jonge tooling, de beveiligingsadviezen en het feit dat een deel van de standaard nog in beweging is.

Onderaan de belangrijkste bronnen. De volledige lijst staat in de cursustekst. Ik raad vooral de blogpost van Mozilla over Wasm als eersteklas webtaal aan: die geeft het beste beeld van waarom het web voor Wasm nog altijd lastig is. En het artikel over WebAssembly 3.0 op webassembly.org, voor wie de details van de standaard wil lezen.""",
["Discussie: Wasm voor plug-ins van derden i.p.v. container of gewoon JS?",
 "Denk aan: sandbox, capabilities, opstarttijd versus jonge tooling, beveiligingsadviezen, standaard nog in beweging",
 "Bronnen: webassembly.org (3.0, States of WebAssembly, features), Uno Platform, Web Almanac, wasi.dev, Mozilla Hacks"]))
