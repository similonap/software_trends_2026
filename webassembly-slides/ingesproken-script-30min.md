# Ingesproken versie (ongeveer 30 minuten)
Ingekorte spreektekst op basis van `sprekersnotities.md`, ingesproken met ElevenLabs (model eleven_v4, stem Andie). Video: `ingesproken-webassembly-2026.mp4`. Bron: `ingesproken/script.md`; dit bestand wordt gegenereerd door `ingesproken/maak.py`.

## 00:00 – Slide 1: Software Trends

Welkom bij deze les over WebAssembly. Vorig jaar zagen we de basis. Vandaag herhalen we die kort, en kijken we vooral naar wat er het voorbije jaar veranderd is. De rode draad: WebAssembly draait niet meer alleen in de browser. Vandaar de titel: van browsertruc tot universele runtime.

## 00:20 – Slide 2: Agenda

Eerst de basis: wat WebAssembly is, hoe compilers en JIT-compilers werken, en hoe je een module bouwt en laadt. Daarna vijf trends: de nieuwe standaard WebAssembly 3.0, het probleem van de lijmcode, WebAssembly buiten de browser, security en AI. Let op de slides met het woord Kernbegrip rechtsboven: dat is examenstof.

## 00:47 – Slide 3: Wat is WebAssembly?

Lange tijd was JavaScript de enige taal in de browser. WebAssembly is een derde weg: een binair formaat waar je code uit andere talen naartoe compileert, zoals C, C++, Rust of Go. Het draait bijna even snel als native code, en je hoeft geen nieuwe taal te leren. Je schrijft het in de praktijk nooit zelf. Sinds 2019 is het een officiële W3C-standaard, en sinds september 2025 bestaat versie 3.0. En het draait vandaag ook op servers en kleine toestellen. De browser is nog maar één van de plaatsen.

## 01:24 – Slide 4: Welke talen compileren naar Wasm?

Bijna elke grote taal heeft een route naar WebAssembly. In productie: C, C++, Rust en Go. Stabiel genoeg: C#, Zig, Lua en TypeScript via AssemblyScript. Onstabiel maar bruikbaar: Java, Kotlin en Dart. Belangrijker dan de lijst is de beweging. Talen met automatische geheugenopruiming vonden WebAssembly lang lastig. Dat is nu opgelost, en daarom schuiven ze op richting stabiel.

## 01:55 – Slide 5: De vier ontwerpdoelen van WebAssembly

WebAssembly heeft vier doelen. Snel en draagbaar. Leesbaar en debugbaar. Veilig, in een sandbox. En: breek het web niet. Onthoud ze, want ze verklaren veel van wat volgt. Het doel veilig leidt tot het capability-model buiten de browser. Het doel het web niet breken verklaart waarom directe toegang tot de DOM zo traag vooruitgaat.

## 02:22 – Slide 6: Andere pogingen om meer dan JavaScript in de browser te krijgen

WebAssembly is niet de eerste poging. Java-applets, ActiveX, Flash, Silverlight, Google Native Client: bijna alles is verdwenen. Meestal om dezelfde redenen. Ze vroegen een plug-in, ze werkten buiten het beveiligingsmodel van de browser, of ze werden door één bedrijf beheerd. WebAssembly is door alle grote browserfabrikanten samen ontworpen, als open standaard, en vraagt geen plug-in. Een belangrijke tussenstap was asm.js in 2013, een snelle subset van JavaScript.

## 02:57 – Slide 7: Is dat dan allemaal niet hetzelfde als de JVM?

Is dit niet gewoon de Java Virtual Machine opnieuw? Het idee lijkt erop: een virtuele machine met een tussenvorm waar meerdere talen naartoe compileren. Maar WebAssembly ligt dichter bij machinecode, is voorspelbaarder, en een module kan standaard niets: ze krijgt enkel toegang tot wat je meegeeft. Let op met oude artikels: daar staat vaak dat WebAssembly geen garbage collection heeft. Sinds 2025 kan een taal die van de browser gebruiken, maar het is optioneel.

## 03:31 – Slide 8: Use cases

Waarvoor gebruikt men het? In de browser voor zwaar rekenwerk: Figma, Photoshop op het web, AutoCAD, Google Earth, games en emulatoren, SQLite en DuckDB, en Python via Pyodide. Maar vooral groeit het buiten de browser: serverless functies, plug-in systemen zoals Shopify Functions, embedded toestellen, en een sandbox voor AI-agents. De verschuiving is duidelijk: van games en beeldbewerking naar infrastructuur en veilige uitvoering van andermans code.

## 04:05 – Slide 9: WebAssembly in cijfers (2026)

Eerst cijfers. Zevenennegentig procent van de gebruikers heeft browser-support. Maar de Web Almanac meet WebAssembly op nog geen half procent van de websites. Hoe rijm je dat? WebAssembly zit in een paar zware toepassingen die veel mensen bereiken, en steeds meer achter de schermen in bibliotheken. Een waarschuwing: cijfers zoals eenenveertig procent van de bedrijven gebruikt het in productie, zijn niet te herleiden naar een echte meting. Zoek altijd de bron.

## 04:37 – Slide 10: Even wat geschiedenis

In 1995 komt JavaScript, volledig geïnterpreteerd en traag. In 2008 komen de JIT-compilers: ongeveer tien keer sneller. In 2015 wordt WebAssembly aangekondigd, in 2017 zit het in alle grote browsers, in 2019 wordt het een standaard. Dan WASI in 2024 met het Component Model, WebAssembly 3.0 in september 2025 en WASI 0.3 in juni 2026. Is dit het volgende buigpunt? Ja, maar anders: niet tien keer sneller in de browser, maar op nieuwe plaatsen en met nieuwe talen.

## 05:20 – Slide 11: Compiler versus interpreter

Tussen jouw code en de processor is een vertaling nodig, en er zijn twee manieren. Een interpreter vertaalt regel per regel terwijl de code draait. Snel gestart, maar in een lus wordt dezelfde regel duizend keer opnieuw vertaald. Een compiler vertaalt alles vooraf. Trager gestart, maar veel sneller uitgevoerd, en omdat hij alle code kent, kan hij ze ook optimaliseren.

## 05:46 – Slide 12: JIT-compiler: warm en hot

Een JIT-compiler combineert beide. Alle code start in de interpreter. Een monitor telt hoe vaak elk stuk code uitgevoerd wordt. Meerdere keren: warm. Heel vaak: hot. Warme code gaat naar de baseline compiler, hete code naar de optimizing compiler. Zo werken V8 in Chrome, SpiderMonkey in Firefox en JavaScriptCore in Safari.

## 06:13 – Slide 13: JIT: de baseline en de optimizing compiler

De baseline compiler vertaalt snel en bewaart het resultaat. Komt dezelfde code terug met dezelfde types, dan wordt dat hergebruikt. De optimizing compiler gaat veel dieper, maar dat kost tijd, daarom enkel voor hete code. En om diep te kunnen optimaliseren, doet hij aannames over de code. Bijvoorbeeld: deze constructor maakt altijd dezelfde soort objecten.

## 06:39 – Slide 14: JIT: als de veronderstelling niet klopt

Maar JavaScript is dynamisch. Een aanname kan negenennegentig keer kloppen en de honderdste keer niet. Dan moet de engine de geoptimaliseerde code weggooien en terugvallen op een trager niveau. Dat heet deoptimalisatie. Het gevolg: de prestaties van JavaScript zijn moeilijk te voorspellen. Een kleine codewijziging kan een optimalisatie breken. Onthoud dit probleem: het is een van de redenen waarom WebAssembly bestaat.

## 07:08 – Slide 15: JIT in de praktijk: JavaScript versus C++

Deze grafieken tonen de tijd om een priemgetal te berekenen, JavaScript in het blauw, C++ in het rood. Zonder optimalisaties is JavaScript ongeveer acht keer trager. Met de optimaliserende compiler zakt het naar ongeveer twee keer trager dan C++. En in de ingezoomde grafiek zie je de opwarmtijd van een JIT: eerst pieken, en dan, bij de pijl, schakelt de optimizing compiler in.

## 07:36 – Slide 16: Waar gaat de tijd naartoe?

Schematisch, geen metingen. JavaScript met enkel een interpreter: lang uitvoeren, plus parsen en geheugen opruimen. Met een JIT is de uitvoering korter, maar er komt compileren en heroptimaliseren bij. Onderaan WebAssembly: een compact binair formaat dat sneller te decoderen is, de types staan in het bestand, de zware optimalisatie is vooraf gebeurd, en er zijn geen aannames, dus geen heroptimalisatie.

## 08:07 – Slide 17: Waarom Wasm in de engine anders werkt

Samengevat: WebAssembly is binair in plaats van tekst, heeft vaste types in plaats van gokwerk, wordt vooraf geoptimaliseerd, en kan al compileren terwijl het nog gedownload wordt. Ook WebAssembly-engines zijn gelaagd, maar ze hoeven nooit terug te vallen. Het voordeel is dus vooral voorspelbaarheid en piekprestatie bij zwaar rekenwerk. Niet dat het altijd sneller is.

## 08:33 – Slide 18: Assembly en intermediate representation

Assembly is een leesbare taal die één-op-één naar machinecode vertaalt, met een eigen dialect per processor. Tien talen naar vijf processors zijn vijftig vertalers. Met een tussenlaag, de intermediate representation, zijn het er maar vijftien: elke taal vertaalt naar de tussenlaag, en de tussenlaag naar elke processor. Zo werken LLVM en Java-bytecode. En ook WebAssembly.

## 09:00 – Slide 19: WebAssembly: een virtuele assembly

WebAssembly is een assemblytaal voor een denkbeeldige machine. De instructies staan dicht bij echte machine-instructies, maar er is geen rechtstreekse koppeling met een processor. De engine vertaalt ze naar machinecode van het toestel waarop ze draait. Daardoor draait dezelfde binary op een Intel-laptop, een ARM-telefoon en een server.

## 09:23 – Slide 20: WebAssembly-formaten: .wat en .wasm

Er zijn twee formaten. Links het leesbare tekstformaat. We zien een import, een export en een functie die twee getallen optelt, met instructies die op een stapel werken. Rechts de binaire vorm, die de engine uitvoert: slechts vierenzeventig bytes voor dezelfde module. De eerste vier bytes zijn altijd hetzelfde magic number. Je schrijft of leest dit nooit zelf, maar het helpt om te begrijpen wat compilers maken.

## 09:52 – Slide 21: Een module laden en aanroepen

Zo laad je een module: fetch gecombineerd met instantiateStreaming, zodat de browser compileert terwijl hij downloadt. Je geeft een import-object mee met JavaScript-functies, en daarna roep je de exports aan als gewone functies. Dit stukje code schrijf je bij elke module opnieuw. Dat is boilerplate, en daar komt verandering in, in trend twee.

## 10:16 – Slide 22: C naar Wasm: Emscripten

Voor C en C++ gebruik je Emscripten, gebouwd op LLVM. Met één commando, emcc, compileer je een C-programma. Je krijgt drie bestanden: de wasm-module, een JavaScript-bestand met glue code, en een HTML-pagina. Onthoud de term glue code: dat is JavaScript die de module laadt en met de browser laat praten. Ze komt terug in trend twee.

## 10:43 – Slide 23: C: een eigen functie aanroepen

Meestal wil je een eigen functie aanroepen in plaats van main. Je markeert ze met EMSCRIPTEN_KEEPALIVE, zodat de compiler ze niet wegoptimaliseert, en roept ze in JavaScript aan met cwrap of ccall. Voor getallen is dat eenvoudig. Voor tekst wordt het ingewikkeld, want WebAssembly kent enkel getallen. Daar zit veel van de glue code.

## 11:08 – Slide 24: Rust naar Wasm: wasm-bindgen

Rust is geheugenveilig zonder garbage collector, en dus ideaal voor WebAssembly: kleine bestanden, geen runtime. In het voorbeeld roept Rust een JavaScript-functie aan, en maakt de functie greet beschikbaar voor JavaScript. De tool wasm-bindgen genereert de glue code die tekst omzet tussen beide werelden. Met wasm-pack bouw je het geheel.

## 11:31 – Slide 25: Rust: de module gebruiken in een pagina

Het resultaat gebruik je in een gewone pagina met een script van het type module. Je importeert init, dat de module laadt, en greet, de Rust-functie. Daarna roep je greet aan als gewone JavaScript. Let op: open dit via een lokale webserver, niet rechtstreeks als bestand.

## 11:51 – Slide 26: Rust en Wasm: het ecosysteem in 2026

Een wijziging om te kennen als je tutorials leest. In juli 2025 werd de GitHub-organisatie rustwasm opgeheven. De twee belangrijkste tools, wasm-bindgen en wasm-pack, verhuisden naar een nieuwe organisatie en worden actief onderhouden. Veel tutorials verwijzen nog naar de oude plek. De commando's werken nog, maar zoek de nieuwe documentatie op.

## 12:16 – Slide 27: AssemblyScript en Blazor WebAssembly

Twee andere routes. AssemblyScript heeft de syntax van TypeScript, maar is strenger, en is een laagdrempelige manier om WebAssembly uit te proberen. Blazor laat je webapps in C# bouwen. Het is in de praktijk niet sneller dan React, want het meeste werk is DOM-werk, en de runtime moet eerst gedownload worden. .NET 10 verbetert de opstart, en een volgende stap wordt verwacht in .NET 11 en 12.

## 12:45 – Slide 28: Benchmark: JavaScript versus WebAssembly

Een benchmark: hetzelfde Fibonacci-algoritme in JavaScript en in C. Ik voerde het uit in Chrome op een MacBook, drie keer. JavaScript had ongeveer vierhonderdvijftig milliseconden nodig, WebAssembly ongeveer honderdvijftig. Dus ongeveer drie keer sneller. Maar een microbenchmark meet één ding op één machine. Doe het zelf, en onthoud dat dit een rekenfunctie is: het sterkste geval voor WebAssembly.

## 13:14 – Slide 29: Is WebAssembly altijd sneller?

Nee. Voor zwaar rekenwerk, zoals beeld, compressie en simulatie, is het een goede keuze. Voor werk dat vooral de DOM aanpast, gebruik je JavaScript. Voor gewone websites, blogs en formulieren: JavaScript is your friend. De belangrijkste reden: elke oversteek tussen JavaScript en WebAssembly kost iets. Vuistregel: weinig oversteken, veel rekenwerk binnen de module.

## 13:41 – Slide 30: Zal WebAssembly JavaScript vervangen?

Waarschijnlijk niet. Ze zijn complementair: zware berekeningen in WebAssembly, lijmcode, interface en DOM in JavaScript. WebAssembly heeft geen directe toegang tot de DOM, en het JavaScript-ecosysteem is enorm. Zelfs Figma heeft JavaScript nodig. Dat sluit de basis af. Nu de vijf trends.

## 14:04 – Slide 31: Wasm 3.0 en WasmGC

Trend één: WebAssembly 3.0. Sinds september 2025 is dit de nieuwe standaard, de grootste uitbreiding sinds het begin. Het zijn geen losse trucjes: de meeste functies zaten al jaren in de browsers en zijn nu samen gestandaardiseerd.

## 14:22 – Slide 32: Wasm 3.0: tien nieuwe functies in gewone taal

Tien nieuwe functies, in gewone taal. Je hoeft de technische namen niet te kennen, wel wat ze oplossen. Eerst functies die WebAssembly geschikt maken voor meer talen en grotere programma's. Dan functies voor snelheid en robuustheid. En tot slot functies voor betrouwbaarheid en gebruiksgemak. We nemen ze één voor één door.

## 14:45 – Slide 33: Functie 1: automatische opruiming (WasmGC)

Functie één: automatische opruiming. Talen zoals Java, Kotlin en Dart ruimen zelf geheugen op. Vroeger moest elke taal haar eigen opruimsysteem meecompileren naar WebAssembly: grote, trage programma's. Nu doet de browser het opruimen, zoals een gedeelde schoonmaakploeg in een kantoorgebouw. Het resultaat: kleinere, snellere programma's, en veel meer talen op het web. Gebruikers zijn bedrijven met Kotlin-, Java- of Dart-apps, zoals JetBrains en Google met Flutter.

## 15:21 – Slide 34: Functie 2: duidelijke verwijzingen (typed references)

Functie twee: duidelijke verwijzingen. Een verwijzing is een wegwijzer naar data of een functie. Vroeger moest de browser tijdens het draaien controleren of die klopte. Nu beschrijft ze precies waar ze naartoe wijst, en wordt dat vooraf gecontroleerd. Dat is sneller en veiliger, en het is de basis voor functie één. Vooral bouwers van talen en compilers gebruiken het; jij merkt het aan snellere apps.

## 15:48 – Slide 35: Welke talen profiteren van automatische opruiming?

Wie profiteert? Kotlin, met Compose Multiplatform voor één codebase op mobiel, desktop en web, nog in bèta. Dart met Flutter. Ook Java, OCaml, Scala en Scheme komen eraan. Eén waarschuwing: oudere browsers ondersteunen het nog niet, dus voorzie een alternatief.

## 16:10 – Slide 36: Functie 3: meer geheugen (memory64)

Functie drie: meer geheugen. Een WebAssembly-programma mocht maximaal vier gigabyte gebruiken. Nu veel meer, in browsers tot zestien gigabyte. Denk aan een groter bureau: grote projecten passen er nu op. Interessant voor video, 3D, databanken en AI-modellen die volledig in de browser draaien. Een kanttekening voor later: nieuwe functies brengen soms nieuwe fouten mee.

## 16:38 – Slide 37: Functie 4: meerdere geheugens

Functie vier: meerdere geheugens. Vroeger één groot blok voor alles. Nu kan een programma meerdere aparte blokken hebben, bijvoorbeeld een privédeel en een gedeeld deel, zoals een eigen kluisje en een gedeeld postvak. Dat is overzichtelijker en veiliger, en onderdelen zijn makkelijker samen te voegen. Vooral interessant voor plug-in systemen en bouwers van tools.

## 17:06 – Slide 38: Functie 5: foutafhandeling (exceptions)

Functie vijf: foutafhandeling. Een programma kan een fout melden en ergens anders netjes opvangen, zoals een brandalarm dat rechtstreeks naar de brandweer gaat. Vroeger moest dat via JavaScript worden nagebootst: traag en groter. Nu gebeurt het rechtstreeks in WebAssembly. Dat maakt het makkelijker om bestaande C++-software, zoals CAD, games en beeldbewerking, naar het web te brengen.

## 17:33 – Slide 39: Functie 6: recursie zonder crash (tail calls)

Functie zes: recursie zonder crash. Soms roept een functie zichzelf opnieuw aan. Vroeger nam elke aanroep extra geheugen in, en na te veel herhalingen crashte het programma. Nu hergebruikt de laatste aanroep dezelfde plek, zoals rondjes lopen in plaats van telkens een nieuwe trap te bouwen. Interessant voor functionele programmeertalen en tools die andere talen uitvoeren.

## 18:01 – Slide 40: Functie 7: veel getallen tegelijk (relaxed SIMD)

Functie zeven: veel getallen tegelijk. De processor voert één bewerking op meerdere getallen tegelijk uit, zoals vier kassa's tegelijk open. Relaxed betekent dat de laatste kommacijfers per computer een beetje mogen verschillen, in ruil voor snelheid. Voor foto's, geluid en AI maakt dat niets uit, en het gaat veel sneller. Voor een boekhoudprogramma zou je het niet gebruiken.

## 18:28 – Slide 41: Functie 8: altijd dezelfde uitkomst (deterministic profile)

Functie acht, het tegenovergestelde: altijd dezelfde uitkomst. Een instelling waarbij elke computer exact hetzelfde resultaat geeft, zoals een recept met exacte hoeveelheden. Fouten zijn altijd opnieuw op te roepen, en testen wordt betrouwbaar. Nodig bij blockchains, waar alle computers hetzelfde moeten uitrekenen. De prijs is een stukje snelheid.

## 18:54 – Slide 42: Functie 9: extra info in de code (annotations)

Functie negen, de kleinste: extra info in de code. Je kan notities, zoals functienamen, in de leesbare tekstversie zetten, als post-its voor je tools. Vroeger kon dat alleen in het binaire bestand. Het maakt debuggen makkelijker, omdat je namen ziet in plaats van nummers. Vooral nuttig voor wie tools bouwt.

## 19:16 – Slide 43: Functie 10: tekst delen met JavaScript (string builtins)

Functie tien: tekst delen met JavaScript. WebAssembly kent enkel getallen, dus tekst moest omgezet en gekopieerd worden, met lijmcode. Nu gebruikt WebAssembly rechtstreeks de tekst van JavaScript, zoals samen in hetzelfde document werken in plaats van kopieën te sturen. Minder lijmcode, sneller bij alles met tekst, zoals editors en spreadsheetapps.

## 19:41 – Slide 44: Browser-support per functie (november 2026)

Elke browser implementeert elke functie op haar eigen tempo. Chrome en Firefox ondersteunen bijna alles. Safari volgt later, en twee functies, het grote geheugen en relaxed SIMD, staan er nog achter een vlag. De conclusie: de kern is overal, nieuwe functies niet. Gebruik feature detection, voorzie een alternatief, en weet dat deze tabel snel veroudert.

## 20:08 – Slide 45: Wasm als eersteklas webtaal

Trend twee: de glue code. In februari 2026 schreef Mozilla een stuk met een duidelijke titel: waarom is WebAssembly een tweederangs taal op het web?

## 20:21 – Slide 46: Glue code: de lijm tussen WebAssembly en de browser

WebAssembly kan de webpagina niet rechtstreeks aanspreken. Het kent enkel getallen, dus voor tekst of een melding op het scherm is extra JavaScript nodig: de glue code. Tools zoals wasm-bindgen en Emscripten genereren die lijm, maar het blijft extra werk en een beetje trager. Daarom kiezen veel ontwikkelaars gewoon JavaScript. Denk aan een tolk tussen twee mensen die een andere taal spreken: het werkt, maar het kost tijd.

## 20:52 – Slide 47: Wat wordt eraan gedaan?

De lijm wordt stap voor stap kleiner. Eén: een wasm-bestand laden als een gewone module, in aantocht. Twee: tekst delen met JavaScript, dat zagen we bij functie tien en dat werkt al. Drie: wachten zonder vast te lopen, JSPI, dat werkt ook al. Het gaat vooral om laden, tekst en wachten: saai maar nuttig.

## 21:17 – Slide 48: JSPI: wachten zonder vast te lopen

Veel programma's wachten op een antwoord, de browser doet intussen iets anders. Vroeger herschreef een tool, Asyncify, je code, waardoor ze groter en trager werd. Met JSPI pauzeert de browser het programma gewoon tot het antwoord er is, zoals je in een restaurant bestelt en intussen iets anders doet. Het werkt sinds dit jaar in alle grote browsers.

## 21:42 – Slide 49: En rechtstreeks de webpagina aanpassen (de DOM)?

Kan WebAssembly de webpagina rechtstreeks aanpassen? Nog niet, en misschien nooit zoals je verwacht. De webpagina is gemaakt voor JavaScript, en elke koppeling moet veilig en compatibel blijven. Je schrijft dus nog lijmcode, maar minder. Voor werk dat vooral de webpagina aanpast, blijft JavaScript de logische keuze.

## 22:04 – Slide 50: Buiten de browser

Trend drie: buiten de browser. In 2019 schreef Solomon Hykes, medeoprichter van Docker, dat Docker niet nodig geweest zou zijn als WebAssembly met WASI in 2008 had bestaan. We bekijken hoe WebAssembly met de computer praat, hoe onderdelen samenwerken, welke runtime erachter zit, en of het Docker kan vervangen.

## 22:29 – Slide 51: WASI: hoe WebAssembly met de computer praat

Een WebAssembly-programma kan enkel rekenen. WASI is de afspraak waarmee het buiten de browser bestanden, netwerk en de klok kan gebruiken. Het bijzondere: een gewoon programma kan standaard alles, een WebAssembly-programma standaard niets. Je geeft per keer toestemming, deze map, dit netwerkadres. Denk aan een gast in je huis die enkel de kamers mag betreden die jij openzet. De versies: nul punt één in 2019, nul punt twee in 2024, en nul punt drie in juni 2026.

## 23:06 – Slide 52: Het Component Model: bouwstenen die in elkaar passen

Onderdelen in verschillende talen konden enkel getallen uitwisselen. Het Component Model lost dat op met een gedeelde beschrijving van wat een onderdeel doet. Een onderdeel in Rust kan zo een onderdeel in Python aanroepen, met gewone tekst en lijsten. Denk aan LEGO-blokjes met dezelfde noppen. Het is bruikbaar op de server, in de browser nog in ontwerp.

## 23:30 – Slide 53: WASI 0.3 (juni 2026): wachten zonder te blokkeren

WASI nul punt drie, van juni 2026, voegt asynchroon werk toe: een programma kan op iets traags wachten zonder de rest te blokkeren, op een manier die past bij async en await. Het is nog niet af, bijvoorbeeld threads ontbreken, en over WASI één punt nul bestaat geen officiële datum.

## 23:51 – Slide 54: Wasmtime: de motor onder veel WebAssembly-servers

Een naam die je vaak tegenkomt: Wasmtime. Het is een programma dat WebAssembly uitvoert buiten de browser, zoals Chrome dat voor websites doet. Het wordt gemaakt door de Bytecode Alliance, is open source en geschreven in Rust. Het is de referentie voor WASI: nieuwe functies komen er eerst. Spin en Microsofts Wassette gebruiken het. En omdat het de sandbox bewaakt, is zijn beveiliging cruciaal. Dat zien we in trend vier.

## 24:20 – Slide 55: Wie gebruikt WebAssembly op de server?

Drie soorten gebruikers. Platformen zoals Spin, wasmCloud en Cloudflare Workers. In december 2025 kocht Akamai het bedrijf achter Spin. Plug-in systemen waar code van derden veilig draait: Shopify Functions, filters voor de Envoy-proxy en extensies voor de editor Zed. En kleine toestellen, met maar tweehonderdzesenvijftig kilobyte geheugen. Waarom? Klein, milliseconden opstarttijd, elke processor en veilig afgeschermd.

## 24:53 – Slide 56: Is WebAssembly het nieuwe Docker?

Is WebAssembly het nieuwe Docker? Nee, ze vullen elkaar aan. Een container is ideaal voor volledige applicaties, WebAssembly voor kleine, snelle functies en plug-ins. Een container start in seconden, WebAssembly in milliseconden, en is veel kleiner. Maar het ecosysteem van containers is veel volwassener. WebAssembly draait zelfs in Kubernetes. Het is geen vervanging, maar een extra gereedschap.

## 25:22 – Slide 57: Security

Trend vier: security. WebAssembly is veilig ontworpen, maar een sandbox is maar zo sterk als de runtime die ze bewaakt. Dit jaar zagen we daar voorbeelden van.

## 25:35 – Slide 58: De sandbox: een afgesloten speelruimte

Een sandbox is een afgesloten ruimte waarin code enkel kan wat jij toestaat. Een WebAssembly-programma werkt enkel in zijn eigen stukje geheugen, kan niet naar willekeurige plaatsen springen, en heeft geen toegang tot bestanden, netwerk of klok zonder toestemming. Zo kan je code van derden draaien zonder erop te vertrouwen. Denk aan een speelkamer met hekjes.

## 25:59 – Slide 59: Een sandbox is maar zo sterk als haar runtime

Hoe sterk is zo'n sandbox? Wasmtime had in 2026 meerdere kritieke beveiligingsproblemen, waarbij een kwaadaardig programma kon ontsnappen. In april twee, enkel bij het grote geheugen of een niet-standaardinstelling. In oktober twee ernstigere, in de standaardinstelling, met score negen komma negen op tien. De les: nieuwe functies zijn nieuw aanvalsoppervlak, en wie niet-vertrouwde code draait, moet de runtime tijdig updaten. Het gaat om één runtime, niet om de browsers.

## 26:34 – Slide 60: Wat de sandbox niet oplost

Twee dingen die de sandbox niet oplost. Fouten binnenin de module: een C-programma met een buffer overflow heeft die ook in WebAssembly, een reden om voor nieuwe code Rust te kiezen. En een wasm-bestand is een dependency: binair, moeilijk te controleren en vaak meegeleverd in npm-packages. Neem het mee in je supply-chainbeleid. Een sandbox is een extra laag, geen vrijbrief.

## 27:01 – Slide 61: Wasm en AI

Trend vijf: AI. WebAssembly komt op twee manieren in AI terecht: om modellen in de browser uit te voeren, en als sandbox voor door AI geschreven code en tools.

## 27:14 – Slide 62: AI in je browser: WebGPU en WebAssembly

Kleine AI-modellen kunnen volledig in je browser draaien, zonder dat je gegevens naar een server gaan: privacy, geen serverkosten en offline gebruik. De bibliotheek gebruikt WebGPU, snel op de grafische kaart, of WebAssembly, dat overal werkt. WebAssembly is het reservewiel. Cijfers over hoeveel sneller WebGPU is, komen van leveranciers: meet zelf.

## 27:41 – Slide 63: WebAssembly als sandbox voor AI-agents

Een AI-agent voert code uit en gebruikt tools: onbetrouwbare code. WebAssembly geeft elke tool een eigen sandbox die in milliseconden start, met enkel de toegang die nodig is. Microsoft maakte daarvoor Wassette. Maar het beschermt niet tegen prompt injection. Het is een beveiligingslaag, geen volledige oplossing.

## 28:02 – Slide 64: Vooruitblik: wat houden we in de gaten?

Wat volgt? WASI één punt nul en het Component Model. WebAssembly laden als gewone module, minder lijmcode. Safari dat de laatste functies nog moet toevoegen. Kotlin en .NET van bèta naar stabiel. En beveiligingsadviezen van runtimes. Dit zijn verwachtingen, geen zekerheden: WebAssembly gaat in kleine stappen vooruit.

## 28:26 – Slide 65: Wat kan je er zelf mee?

Wat kan je zelf doen? Gebruik WebAssembly zonder het te schrijven, via bibliotheken zoals SQLite, DuckDB en ffmpeg. Probeer Rust voor een rekenintensief stuk, en meet voor en na. Gebruik feature detection. Behandel een wasm-bestand als een dependency. Draai niet-vertrouwde code in een sandbox en update de runtime. En wees kritisch over cijfers, ook die van mij.

## 28:55 – Slide 66: Begrippenlijst (1/2): basis

Dit is de eerste helft van de begrippenlijst, de basis. Je moet de begrippen kunnen definiëren en met een voorbeeld uitleggen. Let op de groepen die bij elkaar horen: interpreter, compiler en JIT, assembly en intermediate representation, en glue code samen met Emscripten en wasm-bindgen.

## 29:16 – Slide 67: Begrippenlijst (2/2): de trends

De tweede helft gaat over de trends: de functies van WebAssembly 3.0, het verbinden met JavaScript, WASI, capabilities en het Component Model, en sandbox en runtime. Kan je een begrip niet uitleggen, ga dan terug naar de slide met het label Kernbegrip.

## 29:35 – Slide 68: Conclusie

Zeven punten. Eén: WebAssembly is een compilatiedoel, geen taal. Twee: het vervangt JavaScript niet. Drie: versie 3.0 brengt onder andere automatische opruiming, waardoor meer talen kunnen meedoen. Vier: op het web blijft het een tweederangs burger, de glue code wordt kleiner maar verdwijnt niet. Vijf: buiten de browser groeit het snel. Zes: veilig by design, maar de sandbox is zo sterk als de runtime. Zeven: in AI is het vangnet en sandbox. En onthoud: een snelle standaard is nog geen snelle toepassing. Meet altijd zelf. Bedankt voor jullie aandacht.

## 30:20 – Slide 69: Vragen?

Dan zijn er nu vragen. Een discussievraag om mee te beginnen: zou je WebAssembly gebruiken om plug-ins van derden te laten draaien, in plaats van een container of gewoon JavaScript? Denk aan de sandbox en de opstarttijd, maar ook aan de jonge tooling en de beveiligingsadviezen van dit jaar.
