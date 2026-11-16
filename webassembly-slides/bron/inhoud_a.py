"""Slides 1-30: intro, compilers en JIT, modules bouwen, snelheid."""
from helpers import *

A = []

A.append(cover(
"""Welkom bij deze les over WebAssembly, afgekort Wasm.

We doen dat in twee delen. In het eerste deel bouwen we de basis op: wat WebAssembly is en waarom het bestaat, hoe interpreters, compilers en JIT-compilers werken, hoe je een module bouwt en laadt met C en Rust, en wanneer het sneller is dan JavaScript. In het tweede deel bekijken we vijf trends van 2025 en 2026: de nieuwe standaard Wasm 3.0, het probleem van de lijmcode tussen JavaScript en Wasm, WebAssembly buiten de browser, security en tot slot AI.

Een rode draad vooraf. WebAssembly werd ontworpen als een nieuw soort code voor webbrowsers, en zo wordt het nog vaak voorgesteld. Maar vandaag is de browser nog maar één van de plaatsen waar WebAssembly draait. Daarom de titel: van browsertruc tot universele runtime.

Let tijdens de les op de slides met het woord Kernbegrip rechtsboven. Dat zijn de definities en concepten die je moet kennen en kunnen uitleggen. Achteraan vind je een begrippenlijst.""",
["Twee delen: eerst de basis (wat, compilers en JIT, modules bouwen, snelheid), dan vijf trends van 2025–2026",
 "Trends: Wasm 3.0, glue code, buiten de browser, security, AI",
 "Rode draad: ontworpen voor de browser, maar de browser is nu één van de runtimes",
 "Slides met Kernbegrip rechtsboven = examenstof; begrippenlijst achteraan",
 "→ Het plan van de les"]))

A.append(slide('agenda', 'Agenda',
    ul(['Wat is WebAssembly, en waarom?',
        'Compilers, interpreters en JIT: waarom Wasm anders is',
        'Een module bouwen en laden: C, Rust en andere talen',
        'Snelheid, support en cijfers',
        'Trend 1: Wasm 3.0 en WasmGC',
        'Trend 2: Wasm als eersteklas webtaal',
        'Trend 3: Buiten de browser: WASI en het Component Model',
        'Trend 4: Security',
        'Trend 5: Wasm en AI',
        'Vooruitblik, begrippenlijst en conclusie'], size=39)
    + spacer()
    + '<p style="font-size:34px;line-height:1.4;color:#595959">Slides met <span style="color:#C00000">Kernbegrip</span> rechtsboven bevatten definities die je moet kennen en kunnen uitleggen (examenstof).</p>',
"""Dit is het plan. De eerste vier punten vormen de basis: wat WebAssembly is, hoe compilers en JIT-compilers werken en waarom Wasm anders is, hoe je een module bouwt in C, Rust en andere talen, en wanneer het sneller is dan JavaScript.

Daarna volgen vijf trends, op dezelfde manier opgebouwd als in de les over web frameworks. Elke trend begint met een rode tussenslide.

Er zijn twee soorten slides. Slides met het woord Kernbegrip rechtsboven bevatten een definitie of concept dat je moet kennen en kunnen uitleggen: dat is examenstof. De andere slides zijn trendslides, vaak met een bron onderaan. Die geven context en voorbeelden, en illustreren de kernbegrippen.""",
["Eerste vier punten = de basis; daarna vijf trends, elk met een rode tussenslide",
 "Kernbegrip-slides = examenstof; trend-slides = context met bron",
 "→ Wat is WebAssembly?"]))

# ---------------- Deel 1: wat en waarom ----------------
A.append(slide('kb-wasm', 'Wat is WebAssembly?',
    p('**WebAssembly (Wasm)** is een **binair instructieformaat** voor een virtuele machine: een **compilatiedoel** waar code uit andere talen naartoe vertaald wordt.', 38)
    + row(
        col(ul(['Lang was er in de browser enkel **JavaScript**',
                'Compileer **C, C++, Rust, Go, C#, Kotlin, ...** naar Wasm',
                'Draait tegen (bijna) de **snelheid van native code**',
                'Je hoeft geen nieuwe taal te leren',
                'Je schrijft in principe **nooit zelf** Wasm, maar het kan wel'], size=34)),
        col(card('Stand in 2026', size=32),
            ul(['Officiële **W3C-standaard** sinds 2019; **Wasm 3.0** sinds 17 september 2025',
                'Draait niet enkel in de browser: ook op **servers, edge en kleine toestellen**',
                'De browser is **één van de runtimes**'], size=32)), gap=56),
"""Lange tijd was JavaScript de enige taal die je in een webbrowser kon uitvoeren. Wilde je iets anders gebruiken, dan moest je het omzetten naar JavaScript of een plug-in installeren. WebAssembly, afgekort Wasm, is een derde weg. Het is een binair instructieformaat voor een virtuele machine. Je schrijft het meestal niet zelf: je compileert code uit een andere taal ernaartoe, zoals C, C++, Rust of Go. Een compiler heeft altijd een doel nodig, bijvoorbeeld x86 of ARM. Wasm is een doel dat in elke browser aanwezig is.

Het grote voordeel is dat die code bijna even snel draait als native code. Je hoeft geen nieuwe taal te leren: je gebruikt de taal die je kent, of bestaande code die al jaren werkt. Je zou Wasm zelf kunnen schrijven, dat zien we straks, maar in de praktijk doe je dat nooit.

Rechts de stand van zaken in 2026. Wasm is sinds 2019 een officiële W3C-standaard, naast HTML, CSS en JavaScript. Op 17 september 2025 verscheen versie 3.0, daar komen we op terug in trend 1. En Wasm draait niet meer enkel in de browser, maar ook op servers, op edge-netwerken en op kleine toestellen. De browser is één van de runtimes. Dat is trend 3.""",
["Lang enkel JavaScript in de browser; Wasm = derde weg naast transpileren en plug-ins",
 "Wasm = binair formaat voor een virtuele machine; je compileert ernaartoe (C, C++, Rust, Go, ...)",
 "Bijna native snelheid; geen nieuwe taal leren; zelf schrijven kan maar doe je niet",
 "W3C-standaard sinds 2019, Wasm 3.0 sinds 17/09/2025 (trend 1)",
 "Draait ook buiten de browser: servers, edge, embedded (trend 3)",
 "Examen: Wasm definiëren als compilatiedoel",
 "→ Welke talen kunnen er naar Wasm?"],
kern=True))

A.append(slide('talen', 'Welke talen compileren naar Wasm?',
    row(
        col(h3('🐔 In production', 34), ul(['C', 'C++', 'Rust', 'Go'], size=32)),
        col(h3('🐥 Stable for production usage', 34),
            ul(['.NET, C#, F#', 'Zig, Lua, COBOL, Forth', 'TypeScript (AssemblyScript)', 'Grain, Rego, ...'], size=32)),
        col(h3('🐣 Unstable but usable', 34),
            ul(['Java, Kotlin', 'Dart, Elixir, Ada', 'Crystal, D, ...', 'JavaScript'], size=32)), gap=40)
    + groen('Trend: WasmGC verandert het speelveld', 'Talen **met garbage collector** (Kotlin, Dart, Java, OCaml, Scala, Scheme) worden bruikbaarder en kleiner. Zie trend 1.', size=30, flex='none'),
"""Welke talen kunnen naar WebAssembly? Dit overzicht is gebaseerd op de lijst awesome-wasm-langs op GitHub. De talen zijn ingedeeld in drie niveaus. De kip: in productie. Dat zijn C, C++, Rust en Go. Het kuiken: stabiel genoeg voor productie, zoals C# en .NET, Zig, Lua, en TypeScript via AssemblyScript. En het kuikentje dat uit het ei komt: onstabiel maar bruikbaar, zoals Java, Kotlin en Dart. Je ziet dat bijna elke grote taal een Wasm-route heeft.

Belangrijker dan de lijst is de beweging. Talen met een garbage collector, zoals Kotlin, Dart en Java, vonden Wasm lang lastig, omdat ze hun eigen geheugenbeheer moesten meebrengen. Met WasmGC in Wasm 3.0 is dat opgelost. Daardoor schuiven die talen op richting stabiel. Kotlin/Wasm is bijvoorbeeld al in bèta. Beschouw de lijst dus als een momentopname.""",
["Indeling van awesome-wasm-langs: in production / stable / unstable but usable",
 "Production: C, C++, Rust, Go; bijna elke grote taal heeft een Wasm-route",
 "Trend: WasmGC → talen met GC (Kotlin, Dart, Java, OCaml) schuiven op richting stabiel",
 "Lijst = momentopname; de richting telt",
 "→ Waarom is Wasm ontworpen zoals het is?"],
bron='github.com/appcypher/awesome-wasm-langs'))

A.append(slide('doelen', 'De vier ontwerpdoelen van WebAssembly',
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px 40px">'
    + card('Be fast, efficient and portable', 'De code draait snel en op verschillende platformen: desktop, smartphone, IoT.', size=34)
    + card('Be readable and debuggable', 'Het is low-level, maar er is een tekstformaat (.wat) dat een mens kan lezen.', size=34)
    + card('Keep secure', 'Uitvoering in een sandbox; respecteert de beveiligingsregels van de browser.', size=34)
    + card('Don\'t break the web', 'Werkt samen met bestaande webtechnologie en is achterwaarts compatibel.', size=34)
    + '</div>'
    + p('Deze doelen verklaren veel van de trends verderop: *Keep secure* leidt tot WASI-capabilities, *Don\'t break the web* tot het trage tempo van DOM-toegang.', 31, '#595959'),
"""Dit zijn de vier doelen waarmee WebAssembly ontworpen werd.

Eén: snel, efficiënt en draagbaar. De code moet bijna even snel draaien als native code, ongeacht het platform. Twee: leesbaar en debugbaar. Wasm is een low-level taal, maar er bestaat een tekstformaat, dat we straks zien, dat een mens kan lezen. Drie: veilig. Wasm draait in een sandbox en respecteert de beveiligingsregels van de browser. Vier: breek het web niet. Wasm moet goed samenwerken met andere webtechnologie en achterwaarts compatibel blijven.

Onthoud deze doelen, want ze verklaren veel van wat we verderop zien. Het doel veilig leidt tot het capability-model van WASI: een module krijgt enkel toegang tot wat je expliciet meegeeft. Het doel het web niet breken verklaart waarom directe toegang tot de DOM zo traag vooruitgaat: elke wijziging moet veilig en compatibel zijn met dertig jaar bestaande websites.""",
["Vier doelen: fast/efficient/portable, readable/debuggable, secure, don't break the web",
 "Readable: tekstformaat .wat",
 "Secure: sandbox → later WASI-capabilities (trend 3)",
 "Don't break the web → verklaart traag tempo van DOM-toegang (trend 2)",
 "→ Wasm is niet de eerste poging"]))

A.append(slide('pogingen', 'Andere pogingen om meer dan JavaScript in de browser te krijgen',
    '<div style="display:flex;gap:16px;align-items:stretch">'
    + card('1995', 'Java-applets', size=30) + card('1996', 'ActiveX', size=30) + card('1996', 'Flash (einde: dec. 2020)', size=30)
    + card('2007', 'Silverlight', size=30) + card('2011', 'Google NaCl, later PNaCl', size=30)
    + card('2011', 'Dart (Dartium)', size=30) + groen('2013', 'asm.js', size=30)
    + groen('2017', 'WebAssembly', size=30) + '</div>'
    + ul(['De meeste vroegen een **plug-in**: extra aanvalsoppervlak, niet op elk toestel',
          'Vaak **buiten het beveiligingsmodel** van de browser, of door **één bedrijf** beheerd',
          '**asm.js**: een strikte subset van JavaScript die engines sneller konden uitvoeren; Wasm nam dat idee over in een compact binair formaat',
          'Wasm is het eerste dat door **alle browserfabrikanten samen** ontworpen werd'], size=34),
"""WebAssembly is niet de eerste poging om meer dan JavaScript in de browser te krijgen. Op de tijdlijn zie je er een hele reeks. Java-applets in 1995, ActiveX en Flash in 1996, Silverlight van Microsoft in 2007, de Native Client van Google in 2011, en Dart, dat Google eerst rechtstreeks in een aangepaste browser wilde laten draaien. Bijna al deze pogingen zijn verdwenen. Flash is op het einde van 2020 officieel gestopt.

Waarom mislukten ze? Meestal om dezelfde redenen. Ze vroegen een plug-in, wat extra aanvalsoppervlak en onderhoud betekent en wat niet op elk toestel beschikbaar was. Ze werkten vaak buiten het beveiligingsmodel van de browser. En ze werden door één bedrijf beheerd, waardoor de andere browsers geen reden hadden om mee te gaan.

Een belangrijke tussenstap was asm.js in 2013. Dat is een strikte subset van JavaScript waarvan de engines wisten dat ze die snel konden uitvoeren. WebAssembly neemt dat idee over, maar dan in een compact binair formaat dat sneller te laden is. Het verschil met alle vorige pogingen: Wasm is door alle grote browserfabrikanten samen ontworpen, als open standaard, en vraagt geen plug-in. In 2017 zat het in alle grote browsers.""",
["Java-applets (1995), ActiveX en Flash (1996), Silverlight (2007), NaCl (2011), Dart: bijna allemaal verdwenen; Flash gestopt eind 2020",
 "Oorzaken: plug-in nodig, buiten het browser-beveiligingsmodel, één eigenaar",
 "asm.js (2013): snelle subset van JS; Wasm neemt dat over in binair formaat",
 "Wasm: door alle browserfabrikanten samen ontworpen, open standaard, geen plug-in; 2017 in alle grote browsers",
 "→ Is Wasm dan niet gewoon de JVM?"]))

A.append(slide('jvm', 'Is dat dan allemaal niet hetzelfde als de JVM?',
    tabel(['', 'Java Virtual Machine', 'WebAssembly'],
          [['Idee', 'Stack-gebaseerde virtuele machine met tussenvorm (bytecode)', 'Idem: stack-gebaseerd, met een binaire tussenvorm'],
           ['Meerdere talen', 'Java, Kotlin, Scala, ...', 'C, C++, Rust, Go, C#, Kotlin, ...'],
           ['Geheugen', 'Altijd garbage collection', '**Standaard lineair geheugen** dat jij beheert; sinds 3.0 **optioneel WasmGC**'],
           ['Afstand tot hardware', 'Hoger niveau', 'Dichter bij echte machinecode'],
           ['Beveiliging', 'Security manager (afgeschaft)', 'Sandbox: een module kan **standaard niets**'],
           ['JavaScript', 'Aparte bruggen', 'Ingebouwd in de browser']], [18, 38, 44], size=30)
    + p('Let op bij oudere bronnen: *Wasm heeft geen garbage collection* klopt niet meer. Sinds Wasm 3.0 **kan** het er één gebruiken, maar het **moet** niet.', 32, '#C00000'),
"""Een terechte vraag: is dit niet gewoon de Java Virtual Machine opnieuw? De JVM is ook een stack-gebaseerde virtuele machine met een tussenvorm, de bytecode, waar meerdere talen naartoe compileren, zoals Java, Kotlin en Scala. WebAssembly werkt in grote lijnen op dezelfde manier.

Er zijn wel belangrijke verschillen. Wasm ligt dichter bij echte machinecode en de uitvoering is voorspelbaarder. De beveiliging is anders: een Wasm-module kan standaard niets en krijgt alleen toegang tot wat je expliciet meegeeft. De JVM had daarvoor een security manager, maar die is intussen afgeschaft. En Wasm werkt rechtstreeks samen met JavaScript in de browser.

Het geheugen verdient aandacht. Standaard krijgt een Wasm-module een lineair geheugen: één grote rij bytes die het programma zelf beheert, zoals C en Rust dat gewend zijn. Sinds Wasm 3.0 bestaat er ook WasmGC: een taal die een garbage collector wil, kan die van de engine gebruiken. Het verschil met de JVM is dus dat garbage collection optioneel is. Let op als je oudere tutorials of artikels leest: daar staat vaak dat Wasm geen garbage collection heeft. Dat was waar tot 2025, maar nu niet meer.""",
["JVM en Wasm: allebei stack-based VM met tussenvorm waar meerdere talen naartoe compileren",
 "Verschillen: Wasm dichter bij machinecode, voorspelbaarder, sandbox by default, ingebouwd in browser",
 "Geheugen: standaard lineair geheugen; sinds 3.0 optioneel WasmGC",
 "Oudere bronnen zeggen 'geen GC': klopt niet meer sinds Wasm 3.0",
 "→ Waarvoor gebruiken mensen het dan?"]))

A.append(slide('usecases', 'Use cases',
    row(
        col(h3('In de browser', 38),
            ul(['**Beeld en video**: Figma, Photoshop in de browser, ffmpeg.wasm',
                '**CAD en 3D**: AutoCAD Web, Google Earth',
                '**Games en emulatie**: DOSBox, QEMU, MAME, game engines',
                '**Databanken**: SQLite en DuckDB in de browser',
                '**Python in de browser**: Pyodide',
                '**ML en beeldherkenning**; encryptie; compressie',
                '**Zoeken**: docfind (Rust + Wasm) op de VS Code-website'], size=32)),
        col(h3('Buiten de browser', 38),
            ul(['**Serverless en edge**: Cloudflare Workers, Fermyon Spin (Akamai)',
                '**Plug-ins** in een sandbox: Envoy-filters, Shopify Functions, Zed-extensies',
                '**Embedded**: runtimes vanaf 256 KB geheugen',
                '**AI-agents**: sandbox voor tools en gegenereerde code'], size=32)
            + groen('Trend', 'Het accent verschuift van *games en beeldbewerking* naar **infrastructuur en veilige uitvoering** van andermans code.', size=30)), gap=56),
"""Waarvoor wordt WebAssembly gebruikt? Links de toepassingen in de browser die veel rekenwerk vragen. Beeld- en videobewerking, zoals Figma en de webversie van Photoshop, of ffmpeg dat naar Wasm gecompileerd is. CAD en 3D, zoals AutoCAD Web en Google Earth. Games en emulatoren zoals DOSBox, QEMU en MAME. Databanken zoals SQLite en DuckDB die volledig in je browser draaien, Python via Pyodide, en machine learning. En een recent voorbeeld: Microsoft bouwde voor de website van VS Code een zoekfunctie in Rust die naar Wasm gecompileerd is en volledig in je browser draait, zonder server.

Rechts wat de laatste jaren sterk groeit: Wasm buiten de browser. Serverless functies en edge computing, zoals Cloudflare Workers en Spin, dat sinds kort bij Akamai hoort. Plug-in systemen, waarin code van derden veilig in een sandbox draait: filters in de Envoy-proxy, Shopify Functions waarmee winkels eigen logica toevoegen, en extensies voor de code-editor Zed. Embedded toestellen met slechts 256 kilobyte geheugen. En heel recent: een sandbox voor tools en code die door AI-agents gegenereerd is.

De verschuiving is duidelijk: van games en beeldbewerking naar infrastructuur en veilige uitvoering van andermans code. Dat zijn ook de trends die we straks bekijken.""",
["Browser: beeld/video (Figma, Photoshop web, ffmpeg.wasm), CAD/3D (AutoCAD, Google Earth), games/emulatie, SQLite/DuckDB, Pyodide, ML",
 "Recent: docfind (Microsoft): zoeken op de VS Code-website, Rust + Wasm, volledig client-side",
 "Buiten de browser: serverless/edge (Cloudflare Workers, Spin), plug-ins (Envoy, Shopify Functions, Zed), embedded (256 KB), AI-sandbox",
 "Verschuiving: van games/beeldbewerking naar infrastructuur en veilige uitvoering",
 "→ Hoe vaak wordt het echt gebruikt?"],
bron='webassembly.org (21/01/2026); Uno Platform (jan. 2026)'))

A.append(slide('cijfers', 'WebAssembly in cijfers (2026)',
    row(groot_getal('97,37%', 'van de gebruikers heeft **browser-support** voor Wasm (caniuse, november 2026)'),
        groot_getal('0,35%', 'van de **desktop-sites** gebruikt Wasm; **0,28%** van de mobiele sites (Web Almanac 2025)'),
        groot_getal('≈ 5,5%', 'van de **paginaladingen in Chrome** gebruikt Wasm; bijna +1 procentpunt op één jaar'), gap=40)
    + tabel(['Browser-support (caniuse)', 'Aandeel gebruikers'],
            [['2024', '94%'], ['2025', '96,02%'], ['2026', '**97,37%**']], [40, 60], size=34)
    + p('Veel support, weinig **zichtbaar** gebruik: Wasm zit vaak **achter de schermen** in bibliotheken. Het grootste gemeten `.wasm`-bestand is 228 MB.', 33, '#595959'),
"""Eerst wat cijfers. Links de browser-support: volgens caniuse ondersteunt 97,37 procent van de gebruikers WebAssembly. Een jaar eerder was dat 96 procent, twee jaar eerder 94. De kern van Wasm is dus zo goed als overal beschikbaar. Per nieuwe functie, zoals garbage collection of 64-bit geheugen, verschilt het wel nog, en Safari loopt soms achter. Dat zien we in trend 1.

Dan het opvallende: hoeveel sites gebruiken Wasm echt? De Web Almanac 2025 van HTTP Archive meet 0,35 procent van de desktop-sites en 0,28 procent van de mobiele sites. Chrome Platform Status komt op ongeveer 5,5 procent van de paginaladingen in Chrome, met een stijging van bijna één procentpunt op een jaar. Die cijfers verschillen omdat ze iets anders meten. Het ene telt sites, het andere paginaladingen, en paginaladingen worden gedomineerd door een paar heel grote sites die veel bezocht worden.

Hoe rijm je grote support met zo'n klein gebruik? Wasm wordt gebruikt voor een paar zware toepassingen die veel mensen bereiken, zoals Figma, en steeds meer achter de schermen, als onderdeel van bibliotheken. Een site die Wasm gebruikt voor zijn zoekfunctie noemt zichzelf geen Wasm-site. DevClass schreef in januari 2026 een artikel met precies die titel: WebAssembly gaining adoption behind the scenes.

Een waarschuwing over bronnen: online vind je cijfers als 41 procent van de bedrijven gebruikt Wasm in productie. Die zijn niet te herleiden naar een echte meting. Zoek altijd de oorspronkelijke bron.""",
["Support (caniuse): 94% (2024) → 96,02% (2025) → 97,37% (nov. 2026)",
 "Gebruik: 0,35% desktop-sites, 0,28% mobiele sites (Web Almanac 2025); ~5,5% van paginaladingen in Chrome, +1 pp op één jaar",
 "Verschil: sites tellen versus paginaladingen (gedomineerd door grote sites)",
 "Veel support, weinig zichtbaar: 'behind the scenes' in bibliotheken (DevClass, jan. 2026)",
 "Examen: kritisch zijn over bronnen; cijfers zonder meting (bv. '41% in productie') niet overnemen",
 "→ Hoe kwamen we hier?"],
bron='caniuse.com/wasm; Web Almanac 2025 (HTTP Archive); Chrome Platform Status via Uno Platform; DevClass (28/01/2026)'))

A.append(slide('geschiedenis', 'Even wat geschiedenis',
    '<div style="display:flex;flex-direction:column;gap:14px">'
    + ''.join(f'<div style="display:flex;gap:28px;align-items:baseline"><p style="width:150px;flex:none;font-family:{QUEST};font-size:40px;color:#C00000">{j}</p><p style="font-size:34px;line-height:1.3">{inline(t)}</p></div>' for j, t in [
        ('1995', '**JavaScript**: volledig geïnterpreteerd, traag'),
        ('2008', '**JIT-compilers**: ongeveer 10× sneller; JS wordt breed bruikbaar (bv. Node.js)'),
        ('2013', '**asm.js**: snelle subset van JavaScript'),
        ('2017', '**WebAssembly** in alle grote browsers (aangekondigd in 2015)'),
        ('2019', '**W3C-standaard**; eerste versie van **WASI**'),
        ('2022', '**Wasm 2.0** (SIMD, bulk memory, reference types)'),
        ('2024', '**WASI 0.2** en het Component Model'),
        ('2025', '**Wasm 3.0** (17 september): WasmGC, 64-bit geheugen, exception handling, ...'),
        ('2026', '**WASI 0.3** (11 juni): native async')]) + '</div>'
    + p('Is Wasm het volgende buigpunt, zoals de JIT in 2008? Ja, maar vooral op de **server** en voor **talen met GC**, niet als nieuwe ×10 in de browser.', 31, '#C00000'),
"""De geschiedenis in vogelvlucht. In 1995 wordt JavaScript geboren: een eenvoudige taal voor kleine scripts, volledig geïnterpreteerd en dus traag. In 2008 verschijnen de JIT-compilers in de browsers. Die zorgden voor ongeveer een factor tien in snelheid, en daardoor kon JavaScript voor veel meer gebruikt worden, bijvoorbeeld voor Node.js op de server. In 2013 komt asm.js, de snelle subset van JavaScript. In 2015 wordt WebAssembly aangekondigd, en in 2017 zit het in alle grote browsers. In 2019 wordt het een W3C-standaard en verschijnt de eerste versie van WASI, de systeeminterface voor Wasm buiten de browser. Wasm 2.0 werd in 2022 in grote lijnen afgerond, met onder andere SIMD: vectorinstructies die één bewerking op meerdere waarden tegelijk uitvoeren.

Dan de recente stappen: in 2024 WASI 0.2 met het Component Model, in september 2025 Wasm 3.0 en in juni 2026 WASI 0.3. Die drie bekijken we in detail in de trends.

De vraag is dan: is WebAssembly het volgende buigpunt, zoals de JIT in 2008? Mijn antwoord: ja, maar niet op dezelfde manier. Het gaat niet om een factor tien sneller in de browser. De verandering zit in waar Wasm nu draait, vooral op de server, en in welke talen er nu mee kunnen werken.""",
["1995 JS (geïnterpreteerd) → 2008 JIT (~10×, Node.js) → 2013 asm.js → 2015 aangekondigd, 2017 in alle browsers",
 "2019 W3C-standaard + eerste WASI; 2022 Wasm 2.0 (SIMD, bulk memory, reference types)",
 "2024 WASI 0.2 + Component Model; sept. 2025 Wasm 3.0; juni 2026 WASI 0.3",
 "Buigpunt? Ja, maar via server en GC-talen, geen nieuwe ×10 in de browser",
 "→ Hoe werken compilers? Eerst interpreter versus compiler"]))

# ---------------- Compilers en JIT ----------------
A.append(slide('kb-compiler-interpreter', 'Compiler versus interpreter',
    p('Tussen programmacode en machinecode is een **vertaling** nodig. Er zijn twee manieren.', 38)
    + row(
        col(h3('Interpreter: regel per regel', 40),
            ul(['Code wordt **tijdens het uitvoeren** vertaald, regel per regel',
                '**Snel gestart**: geen compilatiestap',
                'Eenvoudig op te zetten (bv. Chrome DevTools)',
                '**Inefficiënt bij herhaling**: in een lus wordt dezelfde regel telkens opnieuw vertaald'], size=33)),
        col(h3('Compiler: alles vooraf', 40),
            ul(['Alles wordt **vooraf** vertaald naar machinecode',
                '**Trage start**, maar code in lussen is veel sneller: één keer vertalen',
                'Kent de volledige code en kan dus **optimaliseren**',
                'Een interpreter kan dat niet: dat zou de start te traag maken'], size=33)), gap=56),
"""Tussen de code die jij schrijft en de machinecode die een processor uitvoert, is een vertaling nodig. Daarvoor bestaan twee manieren, en het verschil tussen die twee verklaart waarom WebAssembly bestaat.

Een interpreter vertaalt de code regel per regel, terwijl ze uitgevoerd wordt. Het voordeel is dat je snel kan starten: er is geen aparte compilatiestap. Daarom is het ideaal voor webontwikkeling: je tikt iets in de DevTools van Chrome en je ziet meteen het resultaat. Het nadeel zit in herhaling. Staat een regel in een lus die duizend keer loopt, dan wordt die duizend keer opnieuw vertaald.

Een compiler vertaalt alles vooraf naar machinecode. De start is trager, maar de uitvoering is veel sneller, want de vertaling gebeurt maar één keer. Bovendien kent de compiler de volledige code en kan hij ze herschrijven om efficiënter te zijn. Bijvoorbeeld een berekening die altijd hetzelfde resultaat geeft, buiten de lus halen. Een interpreter kan dat niet doen, want dan zou de start te lang duren.""",
["Vertaling nodig tussen programmacode en machinecode; twee manieren",
 "Interpreter: regel per regel, snel gestart, geen compilatiestap; slecht bij herhaling (lussen)",
 "Compiler: alles vooraf; trage start, snelle uitvoering; kent alle code → optimaliseert",
 "Examen: kunnen uitleggen waarom een interpreter in een lus inefficiënt is",
 "→ Kan je beide combineren? Ja: JIT"],
kern=True))

A.append(slide('kb-jit', 'JIT-compiler: warm en hot',
    p('Een **Just-in-Time-compiler** combineert beide: de **snelle start** van een interpreter en de **optimalisaties** van een compiler.', 36)
    + flow(card('Interpreter', 'Alle code start hier.', size=30),
           card('Monitor', 'Telt hoe vaak een stuk code uitgevoerd wordt.', size=30),
           card('Warm', 'Meerdere keren uitgevoerd → naar de baseline compiler.', size=30, fill='#FFF2CC', border='#BF9000', tc='#7F6000'),
           rood('Hot 🔥', 'Nog veel vaker → naar de optimizing compiler.', size=30))
    + ul(['Extra onderdeel in de JavaScript-engine: de **monitor** (profiler)',
          'De engines: **V8** (Chrome, Node.js), **SpiderMonkey** (Firefox), **JavaScriptCore** (Safari)'], size=34),
"""De oplossing voor het lusprobleem heet een Just-in-Time-compiler, kortweg JIT. Die combineert de snelle start van een interpreter met de optimalisaties van een compiler. Alle JavaScript-engines werken zo: V8 in Chrome en Node.js, SpiderMonkey in Firefox en JavaScriptCore in Safari.

Hoe werkt het? Alle code start in de interpreter, zodat je snel iets ziet. Naast de interpreter loopt een extra onderdeel mee: de monitor, ook profiler genoemd. Die telt hoe vaak elk stuk code wordt uitgevoerd. Wordt een stuk code meerdere keren uitgevoerd, dan markeert de monitor het als warm. Wordt het nog veel vaker uitgevoerd, dan wordt het hot.

Warme code gaat naar de baseline compiler en hete code gaat naar de optimizing compiler. Op de volgende slide zien we wat elk van die twee doet.""",
["JIT = snelle start van de interpreter + optimalisaties van een compiler",
 "Engines: V8 (Chrome, Node.js), SpiderMonkey (Firefox), JavaScriptCore (Safari)",
 "Alles start in de interpreter; de monitor (profiler) telt uitvoeringen",
 "Meerdere keren → warm; nog veel vaker → hot",
 "Examen: warm versus hot kunnen uitleggen",
 "→ Wat doen de twee compilers?"],
kern=True))

A.append(slide('jit-compilers', 'JIT: de baseline en de optimizing compiler',
    row(
        col(h3('Baseline compiler (warm)', 40),
            ul(['Compileert een stuk code en bewaart het resultaat: een **stub**',
                'Zelfde code, **zelfde types**? Dan wordt de stub hergebruikt',
                'Draait **parallel** aan de interpreter: je hoeft niet te wachten',
                'Doet enkel **snelle**, basisoptimalisaties'], size=32)),
        col(h3('Optimizing compiler (hot)', 40),
            ul(['Doet **diepe optimalisaties**, en dat kost tijd',
                'Maakt **veronderstellingen** over de code, bv. *deze constructor maakt altijd dezelfde soort objecten*',
                'Enkel voor code die vaak genoeg loopt om de moeite te lonen'], size=32)), gap=56)
    + p('Dure optimalisatie loont enkel als de code vaak loopt; daarom zijn er **twee niveaus**.', 34, '#595959'),
"""Warme code gaat naar de baseline compiler. Die compileert het stuk code en slaat het resultaat op, een zogenoemde stub. Komt hetzelfde stuk code opnieuw voorbij, met dezelfde types voor de variabelen, dan wordt de opgeslagen stub gebruikt in plaats van opnieuw te interpreteren. De baseline compiler draait parallel aan de interpreter, dus je moet niet wachten tot hij klaar is. Hij doet enkel snelle, basisoptimalisaties, want hij mag de uitvoering niet vertragen.

Wordt de code hot, dan gaat ze naar de optimizing compiler. Die gaat echt diep in optimaliseren. Dat kost tijd, en dat is de reden dat er twee niveaus zijn: dure optimalisatie loont enkel als de code vaak genoeg uitgevoerd wordt.

Om diep te kunnen optimaliseren, maakt die tweede compiler veronderstellingen over de code. Een voorbeeld: een constructor maakt altijd objecten met dezelfde properties. Als dat klopt, kan hij heel efficiënte code maken. En daar zit het probleem, op de volgende slide.""",
["Baseline compiler: snel, bewaart stub; zelfde code + zelfde types → stub hergebruiken; parallel aan interpreter",
 "Optimizing compiler: diepe optimalisaties, kost tijd; maakt veronderstellingen",
 "Twee niveaus omdat dure optimalisatie enkel loont voor vaak uitgevoerde code",
 "→ Wat als een veronderstelling niet klopt?"]))

A.append(slide('jit-deopt', 'JIT: als de veronderstelling niet klopt',
    p('JavaScript is **dynamisch**. Een aanname kan 99 keer kloppen en de 100ste keer niet.', 38)
    + flow(card('Aanname', 'Constructor maakt altijd objecten met properties x en y.', size=30),
           card('Object 100', 'Mist toevallig property y.', size=30, fill='#FFF2CC', border='#BF9000', tc='#7F6000'),
           rood('Deoptimalisatie', 'Geoptimaliseerde code weggooien en terug naar een trager niveau.', size=30),
           card('Opnieuw', 'Misschien opnieuw optimaliseren, misschien opnieuw falen.', size=30))
    + ul(['Dit heet **deoptimalisatie** (*bailing out*); blijft het zich herhalen, dan spreekt men van *thrashing*',
          'Gevolg: de prestaties van JavaScript zijn **moeilijk te voorspellen**',
          'Een kleine codewijziging kan een optimalisatie breken'], size=35),
"""Hier zit de zwakte van de aanpak. De optimizing compiler gokt dat een constructor altijd objecten met dezelfde properties maakt. Maar dit is JavaScript, en JavaScript is dynamisch. Die aanname kan 99 keer kloppen, en bij object 100 ontbreekt er toevallig een property. De compiler moet dan de geoptimaliseerde versie weggooien en terugvallen op een trager niveau. Dat noemt men deoptimalisatie, in het Engels bailing out. Als het zich blijft herhalen, de engine optimaliseert, faalt, optimaliseert opnieuw en faalt opnieuw, spreekt men van thrashing.

Het gevolg is dat de prestaties van JavaScript moeilijk te voorspellen zijn. Het is snel, maar je weet niet altijd waarom, en een kleine wijziging in je code kan een optimalisatie breken en de snelheid halveren. Onthoud dit probleem: het is een van de redenen waarom WebAssembly bestaat.""",
["Optimizing compiler gokt (aannames); JS is dynamisch → aanname kan falen bij object 100",
 "Deoptimalisatie (bailing out); blijft het zich herhalen: thrashing",
 "Gevolg: prestaties van JS moeilijk te voorspellen; kleine wijziging kan optimalisatie breken",
 "Examen: deoptimalisatie kunnen uitleggen met een voorbeeld",
 "→ Wat levert een JIT in de praktijk op?"],
kern=True))

A.append(slide('jit-grafiek', 'JIT in de praktijk: JavaScript versus C++',
    row(col(h3('Zonder optimalisaties', 34), img('jit-zonder-optimalisatie.jpg', breed=800), gap=12),
        col(h3('Met optimalisaties (TurboFan)', 34), img('jit-met-optimalisatie.jpg', breed=800), gap=12), gap=40)
    + p('De tijd om het n-de priemgetal te berekenen (lager is beter). De JIT verkleint de kloof met C++ sterk, maar **dicht ze niet volledig**; in de inzet zie je de **pieken** vóór de optimalisatie.', 30, '#595959'),
"""Wat levert een JIT in de praktijk op? Deze grafieken komen van Franziska Hinkel, die bij het V8-team van Google werkte. Ze tonen hoe lang het duurt om het n-de priemgetal te berekenen, in JavaScript in het blauw en in C++ in het rood. Lager is beter.

Links zonder optimalisaties. JavaScript wordt dan enkel geïnterpreteerd, en het verschil is enorm: bij het miljoenste priemgetal heeft JavaScript ongeveer 77 seconden nodig, C++ ongeveer 9.

Rechts met de optimaliserende compiler van V8, die toen TurboFan heette. JavaScript zakt naar ongeveer 16 seconden. De kloof met C++ is veel kleiner geworden, maar niet weg: C++ is nog altijd bijna twee keer zo snel.

Kijk ook naar de ingezoomde grafiek. In het begin zie je pieken in de blauwe lijn: de code loopt nog in de interpreter en de baseline compiler. Rond het honderdste priemgetal treedt de optimizing compiler in werking, bij de pijl, en zakt JavaScript bijna tot op het niveau van C++. Dat is de opwarmtijd van een JIT. En dat brengt ons bij de vraag: waar gaat de tijd eigenlijk naartoe?""",
["Grafieken van Franziska Hinkel (V8-team): tijd voor het n-de priemgetal, JS (blauw) vs C++ (rood), lager is beter",
 "Zonder optimalisaties: JS ±77 s, C++ ±9 s bij het miljoenste priemgetal",
 "Met TurboFan: JS ±16 s; kloof veel kleiner, maar C++ nog bijna 2× sneller",
 "Inzet: pieken vóór de optimalisatie; rond priemgetal 100 treedt TurboFan in werking = opwarmtijd",
 "→ Waar gaat de tijd naartoe?"],
bron='Franziska Hinkel (@fhinkel), V8-team, Google'))

def _rij(label, afb):
    return (f'<div style="display:flex;flex-direction:column;gap:6px"><p style="font-size:29px;line-height:1.2;font-weight:700">{label}</p>{afb}</div>')

A.append(slide('jit-perf', 'Waar gaat de tijd naartoe?',
    row(
        col(_rij('JavaScript, enkel interpreter', img('tijd-js-interpreter.png', breed=640)),
            _rij('JavaScript met JIT', img('tijd-js-jit.png', breed=640)),
            _rij('WebAssembly', img('tijd-wasm.png', hoog=140)), gap=14, flex='none'),
        col(ul(['**Parse**: broncode lezen; **compile + optimize**: baseline en optimizing compiler; **re-optimize**: verloren tijd door foute aannames; **GC**: geheugen opruimen',
          'Bij Wasm: **decode** in plaats van parse, **geen re-optimize**; GC enkel bij talen die WasmGC gebruiken',
          'Schematisch: **geen metingen**, enkel de verhoudingen'], size=30)), gap=56),
"""Deze tekeningen komen uit een bekende reeks van Lin Clark op de Mozilla Hacks-blog. Ze tonen schematisch waar de tijd naartoe gaat. Het zijn geen metingen, enkel de verhoudingen tussen de stappen.

Bovenaan JavaScript met enkel een interpreter. Je hebt tijd om de code te lezen, parse, een heel lange uitvoering, execute, en tijd voor garbage collection: het geheugen opruimen.

In het midden JavaScript met een JIT. De uitvoering is veel korter, maar er komen stappen bij: compileren en optimaliseren, met de baseline en de optimizing compiler, en heroptimaliseren, de tijd die verloren gaat door verkeerde aannames, de deoptimalisatie van daarnet. In werkelijkheid lopen al deze stappen door elkaar.

Onderaan WebAssembly. In plaats van tekst te parsen moet de engine enkel een compact binair formaat decoderen, en dat gaat sneller. Compileren en optimaliseren gaat ook sneller, want de types staan in het bestand en de zware optimalisatie is al vooraf gebeurd. Er is geen heroptimalisatie, want er zijn geen aannames. En er is geen garbage collection: een Wasm-module beheert haar eigen geheugen. Eén nuance sinds 2025: talen die WasmGC gebruiken, hebben wel weer garbage collection, maar dan die van de engine zelf.""",
["Tekeningen van Lin Clark (Mozilla Hacks): schematisch, geen metingen",
 "JS met interpreter: parse + lange execute + GC",
 "JS met JIT: kortere execute, maar compile/optimize en re-optimize erbij; stappen lopen door elkaar",
 "Wasm: decode (binair) i.p.v. parse, sneller compileren, geen re-optimize, geen GC (behalve bij WasmGC-talen)",
 "→ Waarom precies is Wasm anders?"],
bron='Lin Clark, cartoon-reeks over WebAssembly, Mozilla Hacks (2017)'))

A.append(slide('wasm-engine', 'Waarom Wasm in de engine anders werkt',
    tabel(['', 'JavaScript', 'WebAssembly'],
          [['Formaat', 'Tekst: moet geparset worden', 'Compact **binair** formaat, snel te decoderen'],
           ['Types', 'Dynamisch: de engine **raadt** ze', 'Statisch (i32, i64, f32, f64): staan **in het bestand**'],
           ['Optimalisatie', 'Tijdens het draaien, op aannames', '**Vooraf** door de compiler van je broncode (bv. LLVM)'],
           ['Deoptimalisatie', 'Mogelijk', '**Niet nodig**'],
           ['Laden', 'Eerst downloaden, dan parsen', '**Streaming compilation**: compileren tijdens het downloaden'],
           ['Compilatie in de engine', 'Interpreter, baseline, optimizing', 'Ook gelaagd: in V8 een snelle baseline (*Liftoff*) en een optimizing compiler']],
          [22, 36, 42], size=30)
    + p('Het voordeel van Wasm is vooral **voorspelbaarheid** en **piekprestatie bij rekenwerk**, niet dat het *altijd* sneller is.', 34, '#C00000'),
"""Wat doet Wasm nu anders dan JavaScript? Eerst het formaat: Wasm is binair en compact, de engine moet geen tekst parsen. Dan de types: JavaScript is dynamisch, dus de engine moet raden welk type een variabele heeft en dat blijven controleren. In Wasm staan de types, gehele getallen of kommagetallen van 32 of 64 bit, gewoon in het bestand. Daardoor zijn er geen aannames nodig en dus ook geen deoptimalisatie.

De zware optimalisatie gebeurt vooraf, door de compiler van je broncode, vaak LLVM voor C en Rust. Bovendien kan de browser het bestand compileren terwijl het nog binnenkomt. Dat heet streaming compilation, en straks zien we de functie die dat doet.

Een nuance: ook voor Wasm gebruiken engines een gelaagde aanpak. In Chrome heeft V8 voor Wasm een snelle baseline compiler, Liftoff, zodat de module meteen kan starten, en een optimaliserende compiler voor de code die vaak loopt. Het verschil met JavaScript is dat die compilers niet hoeven te raden en nooit hoeven terug te vallen.

Daarom: het voordeel van Wasm is vooral voorspelbaarheid en de piekprestatie bij zwaar rekenwerk. Niet dat het altijd sneller is. Dat nuanceren we nog bij de benchmark.""",
["Binair en compact ↔ tekst parsen",
 "Statische types in het bestand ↔ dynamisch, de engine raadt → geen aannames, geen deoptimalisatie",
 "Optimalisatie vooraf (LLVM) ↔ tijdens het draaien",
 "Streaming compilation: compileren tijdens downloaden",
 "Ook Wasm-engines zijn gelaagd (V8: Liftoff + optimizing compiler), maar zonder gokken",
 "Voordeel = voorspelbaarheid + piekprestatie bij rekenwerk, niet 'altijd sneller'",
 "→ Wat is assembly eigenlijk?"],
kern=True))

A.append(slide('kb-assembly-ir', 'Assembly en intermediate representation',
    row(
        col(h3('Assembly', 40),
            ul(['Low-level taal die **één-op-één** vertaalt naar machinecode',
                'Menselijk leesbaar',
                'Elke processorarchitectuur heeft een **eigen dialect**: x86 is niet ARM'], size=33)),
        col(h3('Intermediate Representation (IR)', 40),
            ul(['Een **tussentaal**, iets hoger dan echte assembly',
                'Talen vertalen naar de IR (**front-end**); de IR wordt vertaald naar elk platform (**back-end**)',
                '**10 talen × 5 platformen = 50 vertalers**; met een IR: **10 + 5 = 15**',
                'Voorbeelden: LLVM IR, JVM-bytecode, **WebAssembly**'], size=33)), gap=56),
"""Om te begrijpen wat WebAssembly precies is, hebben we twee begrippen nodig. Assembly is een low-level programmeertaal die rechtstreeks vertaald kan worden naar machinecode. Ze is menselijk leesbaar, maar elke processorarchitectuur heeft een eigen dialect. Assembly voor een x86-processor, zoals in veel laptops, is anders dan voor een ARM-processor, zoals in telefoons en recente Macs.

Stel nu dat je tien programmeertalen hebt en vijf architecturen. Zou elke taal rechtstreeks naar elke architectuur moeten vertalen, dan heb je vijftig vertalers nodig. Daarom gebruikt men een tussenlaag: de intermediate representation, kortweg IR. Elke taal vertaalt naar de IR, dat is de front-end, en de IR wordt vertaald naar elk platform, de back-end. Dan heb je er nog maar vijftien nodig: tien plus vijf.

Zo werkt LLVM, de compilerinfrastructuur achter Clang en Rust, en zo werkt Java-bytecode. En WebAssembly is ook zo'n tussenvorm, maar met een bijzonder doel, zoals we op de volgende slide zien.""",
["Assembly: low-level, 1-op-1 naar machinecode, leesbaar, dialect per architectuur (x86 ≠ ARM)",
 "IR: tussentaal; talen → IR (front-end), IR → platform (back-end)",
 "10 × 5 = 50 vertalers zonder IR; 10 + 5 = 15 met IR",
 "Voorbeelden: LLVM IR, JVM-bytecode, WebAssembly",
 "Examen: nut van een IR uitleggen met het 50-versus-15-voorbeeld",
 "→ Wasm als virtuele assembly"],
kern=True))

A.append(slide('kb-wasm-isa', 'WebAssembly: een virtuele assembly',
    p('Wasm is een soort **target assembly language**, zoals ARM en x86, maar dan voor een **conceptuele machine**.', 38)
    + ul(['**Geen echte processorarchitectuur**: de instructies heten ook *virtuele instructies*',
          'Veel **dichter bij echte machine-instructies** dan bv. JavaScript',
          'Maar **geen rechtstreekse mapping**: de engine (of runtime) vertaalt Wasm naar de machinecode van jouw toestel',
          'Draait dus op x86, ARM, ... zonder dat jij iets aanpast'], size=36)
    + flow(card('Broncode (C, Rust, ...)', size=30), card('Compiler', 'LLVM en co.', size=30),
           rood('.wasm', 'virtuele instructies', size=30), card('Engine / runtime', 'browser, Wasmtime, ...', size=30),
           card('Machinecode', 'x86, ARM, ...', size=30)),
"""WebAssembly is een soort target assembly language, net zoals ARM en x86. Maar het is geen echte processorarchitectuur. Het is een machinetaal voor een conceptuele machine, een virtuele machine die overal kan draaien. Daarom spreekt men van virtuele instructies.

Die instructies staan veel dichter bij echte machine-instructies dan JavaScript, maar er is geen rechtstreekse mapping met een echte processor. Je compileert dus niet naar x86, maar naar Wasm. Wanneer de module geladen wordt, vertaalt de engine van de browser, of een runtime buiten de browser, de Wasm-instructies naar machinecode voor het toestel waarop ze draait.

De keten onderaan is dus: jouw broncode wordt door een compiler naar een wasm-bestand vertaald, en de engine vertaalt het naar machinecode. Dezelfde wasm-binary draait op een Intel-laptop, een ARM-telefoon en een server. Dat is het portable uit de ontwerpdoelen.""",
["Wasm = target assembly language voor een conceptuele machine; 'virtuele instructies'",
 "Dichter bij machine-instructies dan JS, maar geen directe mapping met x86/ARM",
 "Engine of runtime vertaalt naar machinecode van het toestel → één binary draait overal",
 "Keten: broncode → compiler → .wasm → engine → machinecode",
 "→ Hoe ziet zo'n Wasm-bestand eruit?"],
kern=True))

A.append(slide('formaten', 'WebAssembly-formaten: .wat en .wasm',
    row(
        col(h3('.wat: leesbare tekst', 36),
            code('''(module
  (import "math" "callback" (func $callback (param i32)))
  (export "add" (func $add))
  (func $add (param $a i32) (param $b i32) (result i32)
    (local $sum i32)
    local.get $a
    local.get $b
    i32.add
    local.set $sum
    local.get $sum
    call $callback   ;; roept de JS-functie aan
    local.get $sum)) ;; geeft $sum terug''', 'wat', 23), flex='1.25'),
        col(h3('.wasm: binair (74 bytes)', 36),
            code('''00 61 73 6D 01 00 00 00 01 0B
02 60 01 7F 00 60 02 7F 7F 01
7F 02 11 01 04 6D 61 74 68 08
63 61 6C 6C 62 61 63 6B 00 00
03 02 01 01 07 07 01 03 61 64
64 00 01 0A 13 01 11 01 01 7F
20 00 20 01 6A 21 02 20 02 10
00 20 02 0B''', 'bash', 23)
            + code('wat2wasm simple.wat -o simple.wasm', 'bash', 23)
            + p('`00 61 73 6D` = `\\0asm`: het **magic number**', 26, '#595959')), gap=36),
"""Wasm kent twee formaten. Links het wat-bestand, WebAssembly Text, de leesbare variant. Je kan er in principe zelf in schrijven. Wat zie je? Een module met een import: een functie callback die we van buitenaf krijgen, uit JavaScript. Een export: de functie add, die JavaScript kan aanroepen. En de functie zelf: twee parameters van het type i32, een geheel getal van 32 bit, een resultaat en een lokale variabele.

Je ziet ook dat Wasm een stack machine is. local.get zet een waarde op een stapel. i32.add neemt de twee bovenste waarden, telt ze op en zet de som terug. Daarna bewaren we de som in een variabele, roepen we de callback aan met de som, en geven we ze terug.

Rechts het wasm-bestand: de binaire vorm die de engine uitvoert. Dit is exact deze module in binaire vorm: 74 bytes. De eerste vier bytes zijn altijd het magic number, nul, a, s, m: zo herkent een engine een Wasm-bestand. Daarna komt het versienummer, en dan secties: de types, de imports, waarin je de letters van math en callback terugziet, de functies, de exports met add, en de code. Je gaat dit nooit zelf schrijven of lezen, maar het helpt om te begrijpen wat de compilers voor je maken. Met het commando wat2wasm zet je het tekstformaat om naar het binaire.""",
["Twee formaten: .wat (leesbaar, kan je zelf schrijven) en .wasm (binair, wordt uitgevoerd)",
 "Module met import (callback uit JS), export (add) en een functie met twee i32-parameters",
 "Stack machine: local.get zet op de stapel, i32.add neemt er twee en zet de som terug",
 "Rechts: de echte binary van deze module (74 bytes); 00 61 73 6D = magic number '\\0asm'; daarna versie en secties",
 "wat2wasm zet .wat om naar .wasm",
 "→ Hoe laad je dit in de browser?"],
kern=True))

A.append(slide('laden', 'Een module laden en aanroepen',
    row(
        col(code('''const imports = {
  math: { callback: (x) => console.log("resultaat:", x) }
};

const { instance } = await WebAssembly.instantiateStreaming(
  fetch("simple.wasm"),
  imports
);

instance.exports.add(2, 3);   // logt 5 en geeft 5 terug''', 'js', 23), flex='1.45'),
        col(ul(['`fetch()` + `instantiateStreaming()`: **compileren terwijl je downloadt**, de meest efficiënte manier',
                'Het **import-object** geeft JS-functies mee aan de module (bv. een callback)',
                '**Exports** roep je aan als gewone JS-functies',
                'De server moet het bestand serveren als `application/wasm`'], size=31)),
        gap=40)
    + groen('Binnenkort eenvoudiger', 'Met **ESM-integratie** en **source phase imports** laad je een `.wasm` zoals een gewone module (trend 2).', size=30, flex='none'),
"""Hoe laad je een module in de browser? Dit is de moderne manier. Je combineert de fetch API met WebAssembly.instantiateStreaming. De browser begint dan te compileren terwijl de bytes binnenkomen, nog voor het bestand volledig gedownload is. Dat is de meest efficiënte manier, en het is de streaming compilation van daarnet. Een praktisch detail: de webserver moet het bestand serveren met het MIME-type application/wasm, anders weigert de browser deze functie.

Je geeft een import-object mee. Dat zijn de JavaScript-functies die de module mag gebruiken. Hier is dat de callback uit de module van de vorige slide, die we laten loggen naar de console. Wasm kan zo terugroepen naar JavaScript.

Het resultaat is een instance. Op de exports van die instance staan de functies die de module beschikbaar maakt, hier add. Je roept die aan als een gewone JavaScript-functie: add met twee en drie logt vijf via de callback en geeft vijf terug.

Dit stukje code, fetch, imports en instantiate, schrijf je bij elke module opnieuw. Het is boilerplate, en daar komt verandering in. In trend 2 zien we voorstellen om een wasm-bestand te importeren zoals een gewone JavaScript-module.""",
["fetch + WebAssembly.instantiateStreaming = compileren tijdens downloaden (meest efficiënt)",
 "Server moet application/wasm als MIME-type gebruiken",
 "Import-object: JS-functies meegeven aan de module (callback)",
 "Exports: add(2, 3) → logt 5 via de callback en geeft 5 terug",
 "Binnenkort: ESM-integratie en source phase imports vervangen dit boilerplate (trend 2)",
 "→ C naar Wasm met Emscripten"],
kern=True))

# ---------------- Modules bouwen ----------------
A.append(slide('emscripten', 'C naar Wasm: Emscripten',
    p('**Emscripten** is een compiler-toolchain gebaseerd op **LLVM**, een project om compiler-frontends en -backends mee te bouwen.', 36)
    + row(
        col(code('''#include <stdio.h>

int main() {
    printf("Hello World\\n");
    return 0;
}''', 'c', 30), gap=16),
        col(code('emcc hello.c -o hello.html', 'bash', 30),
            p('Resultaat:', 34, bold=True),
            ul(['`hello.wasm`: de binaire module',
                '`hello.js`: de **glue code** die laadt, imports meegeeft en het geheugen regelt',
                '`hello.html`: laadt, compileert en toont de uitvoer'], size=30)), gap=48),
"""Voor C en C++ gebruik je Emscripten. Dat is een compiler-toolchain: een reeks tools die samenwerken om broncode om te zetten naar een uitvoerbaar formaat, hier WebAssembly. Emscripten is gebouwd bovenop LLVM, een project waarmee je compilers kan bouwen, met frontends per taal en backends per platform. Wasm is gewoon één van die backends.

Links een gewoon C-programma dat Hello World afdrukt. Met één commando, emcc hello.c, compileren we het naar WebAssembly. We krijgen drie bestanden. Eén: hello.wasm, de binaire module met de eigenlijke code. Twee: hello.js, de zogenoemde glue code. Dat is JavaScript dat de module laadt, de imports meegeeft, bijvoorbeeld een printf die naar de console schrijft, en het geheugen regelt. Drie: een HTML-bestand dat alles laadt en de uitvoer in de browser toont. Open je dat bestand via een lokale webserver, dan zie je Hello World verschijnen.

Onthoud de term glue code. Die komt terug in trend 2, want ze is een van de grootste hindernissen bij het werken met Wasm.""",
["Emscripten = compiler-toolchain op basis van LLVM (frontends + backends)",
 "emcc hello.c -o hello.html",
 "Output: .wasm (module), .js (glue code), .html (laadt en toont)",
 "Glue code onthouden → trend 2",
 "→ Meestal wil je een eigen functie aanroepen, niet main()"]))

A.append(slide('c-functie', 'C: een eigen functie aanroepen',
    row(
        col(h3('In C', 36), code('''#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
int add(int a, int b) {
    return a + b;
}''', 'c', 28), h3('Compileren', 36),
            code('emcc add.c -o add.js \\\n  -sEXPORTED_RUNTIME_METHODS=ccall,cwrap', 'bash', 26)),
        col(h3('In JavaScript', 36), code('''const add = Module.cwrap(
  "add", "number", ["number", "number"]
);
add(2, 3);   // 5

// of in één keer:
Module.ccall("add", "number",
  ["number", "number"], [2, 3]);''', 'js', 26),
            ul(['`EMSCRIPTEN_KEEPALIVE`: de compiler mag de functie niet als "ongebruikt" weggooien',
                '`cwrap` / `ccall` zetten JS-waarden om naar C-types',
                'Getallen zijn eenvoudig; **strings en structs** vergen geheugen kopiëren'], size=28)), gap=48),
"""Meestal wil je niet gewoon main aanroepen, maar een eigen functie. In C markeer je die dan met EMSCRIPTEN_KEEPALIVE. Dat is nodig omdat de compiler functies die nergens gebruikt worden wegoptimaliseert. Dankzij die markering weet hij dat ze van buitenaf nodig zijn. Bij het compileren vraag je ook om de hulpfuncties ccall en cwrap mee te leveren.

In JavaScript heb je dan twee mogelijkheden. Met cwrap maak je één keer een gewone JavaScript-functie rond de C-functie: je geeft de naam, het type van het resultaat en de types van de parameters. Daarna roep je add met twee en drie aan en krijg je vijf. Met ccall roep je de functie in één keer aan, met de argumenten erbij. In beide gevallen zet Emscripten de JavaScript-waarden om naar C-types.

Voor getallen is dat eenvoudig. Voor tekst of voor structuren wordt het ingewikkelder, want Wasm kent enkel getallen als parameters. Een string moet je in het lineaire geheugen van de module zetten, het adres doorgeven, en daar het resultaat weer uitlezen. Daar zit een groot deel van de glue code, en daar werken de standaarden nu aan.""",
["EMSCRIPTEN_KEEPALIVE: voorkomt dat de compiler de functie weggooit",
 "Compileren met -sEXPORTED_RUNTIME_METHODS=ccall,cwrap",
 "cwrap: één keer een JS-wrapper maken; ccall: in één keer aanroepen → add(2, 3) = 5",
 "Wasm kent enkel getallen als parameters; strings/structs → geheugen kopiëren (glue code)",
 "→ Rust"]))

A.append(slide('rust', 'Rust naar Wasm: wasm-bindgen',
    row(
        col(code('''use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}''', 'rust', 27), flex='1.15'),
        col(ul(['**Rust**: sinds ±2010, syntaxis verwant aan C++, **geheugenveilig zonder garbage collector**',
                '`extern "C"`-blok: een **JS-functie aanroepen** vanuit Rust',
                '`#[wasm_bindgen]` op een functie: **beschikbaar voor JS**',
                '**wasm-bindgen** genereert de bindings en zet strings om'], size=31)
            + code('wasm-pack build --target web', 'bash', 28)
            + p('Levert een `pkg/`-map met de `.wasm` en een JS-module.', 29)), gap=44),
"""Rust is een systeemtaal die rond 2010 bij Mozilla ontstond. De syntax is verwant aan die van C++, maar Rust garandeert geheugenveiligheid zonder garbage collector. Dat maakt het bijzonder geschikt voor WebAssembly: de binaries zijn klein, en er hoeft geen runtime of garbage collector mee.

Het voorbeeld toont de brug tussen Rust en JavaScript. Bovenaan importeren we de bibliotheek wasm_bindgen. In het extern-blok geven we aan dat er een JavaScript-functie alert bestaat die we vanuit Rust willen aanroepen. Daaronder de functie greet, met het attribuut wasm_bindgen: dat maakt ze beschikbaar voor JavaScript. Ze roept alert aan met een begroeting.

Wasm-bindgen is de tool die de bindingen tussen Rust en JavaScript genereert. Ze zet bijvoorbeeld een Rust-string om naar een JavaScript-string en omgekeerd: precies het soort glue code waar we het net over hadden, maar dan automatisch. Met wasm-pack build, target web, bouw je het geheel. Je krijgt een pkg-map met de wasm-module en een JavaScript-module om ze te gebruiken. Hoe je dat doet, zie je op de volgende slide.""",
["Rust: sinds ±2010 (Mozilla), C++-achtige syntax, geheugenveilig zonder GC → klein, geen runtime mee",
 "extern \"C\"-blok + wasm_bindgen: JS-functie (alert) aanroepen vanuit Rust",
 "#[wasm_bindgen] op pub fn greet: beschikbaar voor JS",
 "wasm-bindgen genereert bindings (string-omzetting); wasm-pack build --target web → pkg/",
 "→ Hoe gebruik je die pkg-map?"]))

A.append(slide('rust-gebruiken', 'Rust: de module gebruiken in een pagina',
    row(
        col(code('''<!doctype html>
<html lang="nl">
  <head>
    <meta charset="utf-8" />
    <title>hello-wasm</title>
  </head>
  <body>
    <script type="module">
      import init, { greet } from "./pkg/hello_wasm.js";

      await init();         // laadt de .wasm
      greet("WebAssembly"); // alert
    </script>
  </body>
</html>''', 'html', 24), flex='1.3'),
        col(ul(['`hello_wasm.js` is de **gegenereerde glue code**',
                '`init()` doet het **fetch + instantiate**-werk voor jou',
                'Daarna roep je `greet` aan als een **gewone JS-functie**',
                'Serveer via een **lokale webserver**, niet via `file://`'], size=31)), gap=44),
"""Hoe gebruik je die pkg-map nu? In een gewone HTML-pagina, met een script van het type module.

Je importeert twee dingen uit het gegenereerde JavaScript-bestand. De standaardexport init laadt de wasm-module en instantieert ze: dat is het fetch- en instantiate-werk dat we eerder met de hand schreven. En je importeert greet, de Rust-functie. Na het wachten op init roep je greet aan als een gewone JavaScript-functie, en je browser toont Hello, WebAssembly.

Het bestand hello_wasm.js is de glue code die wasm-bindgen voor ons gegenereerd heeft. Kijk er eens in als je dit zelf probeert: je ziet hoe de string WebAssembly in het geheugen van de module geschreven wordt voordat Rust ze kan lezen.

Een praktische tip: open dit niet rechtstreeks als bestand in je browser, maar via een lokale webserver. Modules en fetch werken niet via file-URL's.""",
["HTML met script type=module: import init, { greet } from './pkg/hello_wasm.js'",
 "init() = fetch + instantiate voor jou; daarna greet('WebAssembly') als gewone JS-functie",
 "hello_wasm.js = gegenereerde glue code: kijk erin (string wordt in het geheugen geschreven)",
 "Via een lokale webserver serveren, niet via file://",
 "→ Wat is er in het Rust-ecosysteem veranderd?"]))

A.append(slide('rust-eco', 'Rust en Wasm: het ecosysteem in 2026',
    row(
        col(card('Juli 2025: de rustwasm-organisatie wordt opgeheven', size=30),
            ul(['De oude GitHub-organisatie *rustwasm* had te weinig maintainers',
                '**wasm-bindgen** en **wasm-pack** verhuizen naar een nieuwe organisatie: **github.com/wasm-bindgen**',
                'Andere repo\'s worden **gearchiveerd** of overgedragen',
                'Beide tools worden actief onderhouden (nieuwe versies in oktober 2026)'], size=31)),
        col(h3('Wat betekent dat voor jou?', 38),
            ul(['Tutorials verwijzen vaak nog naar **rustwasm**: zoek de nieuwe locatie op',
                'Volledige webframeworks in Rust bestaan (**Yew**, **Leptos**), maar de meeste teams schrijven **enkel het rekenintensieve deel** in Rust',
                'Rust bereikt ook de server via **WASI** (trend 3)'], size=31)), gap=56),
"""Een wijziging in het Rust-ecosysteem die je moet kennen als je tutorials leest. In juli 2025 kondigde het Rust-project aan dat de GitHub-organisatie rustwasm wordt opgeheven. Die organisatie onderhield jarenlang de belangrijkste tools voor Rust en Wasm, maar had te weinig actieve maintainers.

De twee belangrijkste tools zijn verhuisd naar een nieuwe organisatie, wasm-bindgen, met nieuwe maintainers: wasm-bindgen zelf en wasm-pack, het buildcommando van de vorige slides. Andere repositories werden gearchiveerd of overgedragen aan hun maintainers. Beide tools worden actief onderhouden: er verschenen nog nieuwe versies eind oktober 2026.

Wat betekent dat voor jou? Veel tutorials en antwoorden op Stack Overflow verwijzen nog naar de oude rustwasm-organisatie. De commando's werken nog, maar zoek de nieuwe locatie op voor documentatie en issues.

Er bestaan ook volledige webframeworks in Rust, zoals Yew en Leptos. Maar het gewone gebruik blijft: één deel van de applicatie, het rekenintensieve deel, in Rust schrijven. En Rust is ook een belangrijke taal voor Wasm op de server, dat zien we in trend 3.""",
["Juli 2025: rustwasm-organisatie opgeheven (te weinig maintainers)",
 "wasm-bindgen en wasm-pack verhuisd naar github.com/wasm-bindgen; actief onderhouden (versies okt. 2026)",
 "Andere repo's gearchiveerd of overgedragen",
 "Tutorials verwijzen nog naar rustwasm → nieuwe locatie opzoeken",
 "Yew en Leptos = volledige frameworks in Rust; meestal enkel rekenintensief deel in Rust",
 "→ Twee andere routes: AssemblyScript en Blazor"],
bron='blog.rust-lang.org/inside-rust (21/07/2025); crates.io (wasm-pack 0.15.1, wasm-bindgen 0.2.130)'))

A.append(slide('as-blazor', 'AssemblyScript en Blazor WebAssembly',
    row(
        col(h3('AssemblyScript', 42),
            code('''/** Het n-de Fibonacci-getal. */
export function fib(n: i32): i32 {
  let a = 0, b = 1;
  if (n > 0) {
    while (--n) {
      const t = a + b;
      a = b;
      b = t;
    }
    return b;
  }
  return a;
}''', 'ts', 22),
            ul(['**TypeScript-syntax**, maar met echte types (`i32`, `f64`) en zonder de dynamische delen van JS',
                'Handig om **Wasm te proberen** zonder een nieuwe taal te leren'], size=28)),
        col(h3('Blazor WebAssembly (.NET)', 42),
            ul(['Bouw **single-page applicaties in C#**; de .NET-runtime wordt als Wasm gedownload',
                '**In de praktijk niet sneller dan bv. React**: de meeste tijd gaat naar DOM-werk, en dat loopt via JS',
                'Download van de runtime vertraagt de start'], size=30)
            + groen('Recent: .NET 10 (november 2025)', '**Fingerprinting** en **preloading** van assets. Volgende stap volgens Uno Platform: **CoreCLR** op Wasm (preview in .NET 11, volledig in .NET 12).', size=28)), gap=56),
"""Twee andere routes. Links AssemblyScript: een taal met TypeScript-syntax die naar Wasm compileert. Het ziet eruit als TypeScript, maar het is strenger: je gebruikt echte types zoals i32 en f64, en de dynamische delen van JavaScript bestaan er niet. Het voorbeeld berekent het n-de Fibonacci-getal met een lus. Voor webontwikkelaars is AssemblyScript een laagdrempelige manier om Wasm uit te proberen, zonder een nieuwe taal te leren.

Rechts Blazor WebAssembly van Microsoft. Daarmee bouw je single-page applicaties in C#. De browser downloadt de .NET-runtime als Wasm en voert je code daarbovenop uit. Dat is aantrekkelijk voor .NET-teams die één taal voor front-end en back-end willen. Maar het is in de praktijk niet sneller dan bijvoorbeeld React. Het meeste werk in een gewone webapplicatie is DOM-werk, en dat loopt via JavaScript. En de runtime die gedownload moet worden, vertraagt de start.

.NET 10, uitgekomen in november 2025, verbetert de opstart met fingerprinting en preloading van de bestanden. Volgens Uno Platform komt de volgende grote stap met de overstap van de Mono-runtime naar CoreCLR, de runtime die .NET ook op de server gebruikt: een preview in .NET 11 en een volledige release in .NET 12. Dat is een verwachting, geen zekerheid.""",
["AssemblyScript: TypeScript-syntax, echte types (i32, f64); voorbeeld: Fibonacci met een lus",
 "Laagdrempelig om Wasm te proberen",
 "Blazor WASM: SPA's in C#; .NET-runtime als Wasm",
 "Niet sneller dan React: DOM-werk loopt via JS; runtime-download vertraagt start",
 ".NET 10 (nov. 2025): fingerprinting, preloading; volgens Uno: CoreCLR op Wasm (preview .NET 11, volledig .NET 12)",
 "→ Hoe snel is het nu echt?"],
bron='assemblyscript.org; learn.microsoft.com (ASP.NET Core 10); Uno Platform (jan. 2026)'))

# ---------------- Snelheid ----------------
A.append(slide('benchmark', 'Benchmark: JavaScript versus WebAssembly',
    row(
        col(h3('JavaScript', 34), code('''function jsFib(n) {
  if (n === 1) return 1;
  if (n === 2) return 1;
  return jsFib(n-1) + jsFib(n-2);
}''', 'js', 25)),
        col(h3('C, gecompileerd met emcc -Os', 34), code('''int fib(int n) {
  if (n == 1) return 1;
  if (n == 2) return 1;
  return fib(n-1) + fib(n-2);
}''', 'c', 25)), gap=40)
    + tabel(['Gemiddelde per run, 3 runs (Chrome 157, MacBook, november 2026)', 'Tijd'],
            [['JavaScript', '432–484 ms'], ['WebAssembly', '153–158 ms'], ['Verhouding JS / Wasm', '**2,8 à 3,1×**']], [66, 34], size=32)
    + p('Meet zelf op je eigen laptop: het resultaat verschilt per machine, browser en run.', 31, '#C00000'),
"""Een benchmark om het te illustreren. We berekenen een Fibonacci-getal recursief, links in JavaScript, rechts in C, gecompileerd met Emscripten. Het is dezelfde functie. De benchmark komt van een publieke testpagina van takahirox.

Ik heb de test in november 2026 drie keer uitgevoerd in Chrome 157 op een MacBook. JavaScript had gemiddeld tussen 432 en 484 milliseconden nodig, WebAssembly tussen 153 en 158. WebAssembly was dus ongeveer drie keer sneller, tussen 2,8 en 3,1 keer. Je ziet ook meteen dat het resultaat van run tot run verschilt, vooral bij JavaScript.

Een belangrijke kanttekening: zo'n microbenchmark meet één ding, op één machine, in één browserversie. Op een andere laptop of in een andere browser kan de verhouding anders zijn, en de JavaScript-engines worden elk jaar sneller. Doe het daarom zelf: open de pagina, druk op run en kijk wat jouw laptop doet. En onthoud dat dit een recursieve rekenfunctie is, het soort taak waar Wasm sterk in is. Het zegt niets over een gewone website.""",
["Fibonacci recursief: JS versus C (emcc -Os), takahirox-benchmark",
 "Gemeten nov. 2026, Chrome 157, MacBook, 3 runs: JS 432–484 ms, Wasm 153–158 ms → 2,8 à 3,1× sneller",
 "Resultaat verschilt van run tot run, vooral bij JS",
 "Kanttekening: microbenchmark, één machine/browser; JS-engines worden sneller → meet zelf, live",
 "Rekenfunctie = sterkste geval voor Wasm; zegt niets over gewone websites",
 "→ Is Wasm dan altijd sneller?"],
bron='takahirox.github.io/WebAssembly-benchmark (eigen meting, 12/11/2026)'))

A.append(slide('sneller', 'Is WebAssembly altijd sneller?',
    tabel(['Scenario', 'Aanbeveling'],
          [['Compute-heavy algoritme (beeld, video, compressie, simulatie)', '**Gebruik WebAssembly**'],
           ['Vooral DOM-werk', 'Gebruik voornamelijk **JavaScript**'],
           ['Games', 'Wasm voor de **CPU-intensieve** delen'],
           ['WebGL / WebGPU', 'Hangt af van **hoeveel API-aanroepen** je doet'],
           ['AI-modellen in de browser', 'Wasm met SIMD als **fallback** voor WebGPU (trend 5)'],
           ['Websites, blogs, formulieren', '**JavaScript is your friend**']], [56, 44], size=34)
    + ul(['Elke oversteek tussen JS en Wasm **kost iets** (data omzetten en kopiëren)',
          'Vuistregel: **weinig oversteken, veel rekenwerk binnen de module**'], size=34),
"""Is WebAssembly dan altijd sneller? Nee. Voor rekenintensieve algoritmes, zoals beeldverwerking, compressie of simulatie, is Wasm een goede keuze. Voor werk dat vooral de DOM aanpast, gebruik je JavaScript. Bij games gebruik je Wasm voor de CPU-intensieve delen, zoals physics. Voor WebGL en WebGPU hangt het af van hoeveel API-aanroepen je doet, want die lopen allemaal via JavaScript. Voor AI-modellen in de browser zien we in trend 5 dat Wasm vaak de fallback is wanneer WebGPU niet beschikbaar is. En voor gewone websites, blogs en formulieren: JavaScript is your friend.

Onderaan de belangrijkste reden waarom Wasm niet altijd wint: elke keer dat je heen en weer gaat tussen JavaScript en Wasm betaal je een prijs, want gegevens moeten omgezet en gekopieerd worden. Een Wasm-functie die duizend keer per seconde met kleine objecten wordt aangeroepen, kan trager zijn dan de JavaScript-versie. De vuistregel: weinig oversteken en veel rekenwerk binnen de module.""",
["Compute-heavy → Wasm; DOM-werk → JS; games → Wasm voor CPU-delen; WebGL/WebGPU → hangt af van aantal API-aanroepen",
 "AI-modellen in de browser → Wasm (SIMD) als fallback voor WebGPU (trend 5)",
 "Websites/blogs/formulieren → JS",
 "Elke JS↔Wasm-oversteek kost iets (omzetten, kopiëren)",
 "Examen: vuistregel 'weinig oversteken, veel rekenwerk binnen de module'",
 "→ Gaat Wasm JS dan vervangen?"]))

A.append(slide('vervangen', 'Zal WebAssembly JavaScript vervangen?',
    p('**Waarschijnlijk niet.** Ze zijn eerder **complementair**.', 44)
    + ul(['**Zware berekeningen**: Wasm; **lijmcode, UI en DOM**: JavaScript',
          'Wasm heeft **geen directe toegang tot de DOM** en andere web-API\'s; alles loopt via JavaScript',
          'Het **JavaScript-ecosysteem** is enorm en niet zomaar te vervangen',
          'Zelfs de grootste Wasm-toepassingen hebben JS nodig voor **laden en UI**'], size=37)
    + card('Ook in 2026 nog zo', 'Mozilla noemt Wasm in februari 2026 nog een *second-class language on the web*. Zie trend 2.', size=31, flex='none'),
"""De klassieke vraag: gaat WebAssembly JavaScript vervangen? Het antwoord: waarschijnlijk niet. De twee zijn complementair. Zware berekeningen kunnen door WebAssembly uitgevoerd worden, terwijl JavaScript de lijmcode, de gebruikersinterface en de DOM blijft doen.

De belangrijkste reden: WebAssembly heeft geen directe toegang tot de DOM en andere web-API's. Wil Wasm iets op de pagina veranderen, dan moet het JavaScript aanroepen. Verder is het JavaScript-ecosysteem enorm, met miljoenen packages, frameworks en ontwikkelaars. Dat vervang je niet zomaar. Zelfs de grootste Wasm-toepassingen, zoals Figma, hebben JavaScript nodig om te laden en voor de interface.

En dat is in 2026 nog altijd zo. In februari 2026 schreef Mozilla op de Hacks-blog dat Wasm nog altijd een tweederangs taal is op het web. Wat dat betekent, en wat eraan gedaan wordt, zien we in trend 2. Daarmee sluiten we de basis af.""",
["Antwoord: waarschijnlijk niet; complementair",
 "Zware berekeningen → Wasm; lijmcode, UI, DOM → JS",
 "Wasm heeft geen directe DOM-toegang; alles via JS",
 "JS-ecosysteem te groot om te vervangen; ook Figma e.d. gebruiken JS voor laden en UI",
 "2026: Mozilla noemt Wasm nog 'second-class language on the web' → trend 2",
 "→ Einde van de basis; nu de vijf trends. Trend 1: Wasm 3.0"],
bron='Mozilla Hacks (02/2026)'))
