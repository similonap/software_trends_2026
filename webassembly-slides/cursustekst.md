# WebAssembly: van browsertruc tot universele runtime

**Cursustekst bij de les voor het vak Software Trends (AP Hogeschool, Toegepaste Informatica)**
Academiejaar 2026–2027 · stand van zaken: november 2026

---

## Leerdoelen en lesplan

Na deze les kan je:

1. uitleggen wat WebAssembly is, waarom het bestaat en welke problemen het oplost ten opzichte van JavaScript;
2. het verschil beschrijven tussen een interpreter, een compiler en een JIT-compiler, en uitleggen waarom WebAssembly voorspelbaarder presteert dan JavaScript;
3. beschrijven hoe je code uit C of Rust naar WebAssembly compileert en vanuit JavaScript aanroept;
4. beoordelen wanneer WebAssembly sneller is dan JavaScript en wanneer niet;
5. de vijf grote ontwikkelingen van 2025–2026 benoemen en uitleggen: Wasm 3.0 (WasmGC), het probleem van de glue code, WASI en het Component Model, security, en Wasm in AI-toepassingen;
6. kritisch omgaan met claims over WebAssembly (cijfers, benchmarks, "Wasm vervangt JavaScript").

**Voorkennis.** Basis JavaScript en HTML. Je weet ongeveer wat een compiler is; het begrip wordt toch uitgelegd. Voorkennis van C of Rust is niet nodig: de codevoorbeelden worden regel per regel besproken.

**Twee soorten slides.** Net als in de les over web frameworks:

- **Kernbegrip-slides** (met het woord *Kernbegrip* rechtsboven) bevatten een definitie en uitleg. Dit is examenstof.
- **Trend-slides** (met een bron onderaan) tonen wat er in 2025–2026 gebeurt. Ze illustreren de begrippen en geven context.

| Deel | Onderwerp | Richttijd | Kernvraag |
|---|---|---|---|
| 1 | Wat is WebAssembly en waarom? | 10 min | Welk probleem lost het op? |
| 2 | Compilers, JIT en waarom Wasm anders is | 14 min | Waarom is JavaScript soms onvoorspelbaar traag? |
| 3 | Een module bouwen en laden (C, Rust, ...) | 14 min | Hoe krijg ik code uit mijn taal in de browser? |
| 4 | Snelheid en de vraag "vervangt Wasm JavaScript?" | 6 min | Wanneer loont het? |
| 5 | Trend 1: Wasm 3.0 en WasmGC | 8 min | Wat is er aan de standaard zelf veranderd? |
| 6 | Trend 2: Wasm als eersteklas webtaal | 7 min | Waarom hebben we nog JavaScript-lijmcode nodig? |
| 7 | Trend 3: buiten de browser (WASI, Component Model) | 10 min | Is Wasm het nieuwe Docker? |
| 8 | Trend 4: security | 6 min | Hoe veilig is een sandbox? |
| 9 | Trend 5: Wasm en AI | 5 min | Wat doet Wasm in het AI-tijdperk? |
| 10 | Vooruitblik, begrippen en conclusie | 4 min | Wat neem ik mee? |

De volledige spreektekst (zie `sprekersnotities.md`) is langer dan één lesblok. Wie het kort wil houden, behandelt deel 1 tot 4 in een half uur en kiest twee trends; de rest is zelfstudie in deze tekst.

---

## Deel 1: Wat is WebAssembly en waarom?

*Kernvraag: welk probleem lost WebAssembly op?*

### Definitie

**WebAssembly** (afgekort **Wasm**) is een binair instructieformaat voor een virtuele machine. Je schrijft het meestal niet zelf: je compileert code uit een andere taal (C, C++, Rust, Go, C#, Kotlin, ...) ernaartoe. De browser of een andere runtime voert het uit met een snelheid die dicht bij die van native code komt. Sinds 2019 is het een officiële W3C-standaard, naast HTML, CSS en JavaScript.

Lange tijd kon je in de browser maar één taal uitvoeren: JavaScript. Wilde je een andere taal gebruiken, dan moest je ofwel naar JavaScript omzetten (transpileren), ofwel een plug-in installeren. Wasm is een derde weg: een **compilatiedoel**. Een compiler heeft altijd een doel nodig (x86, ARM, ...). Wasm is een doel dat in elke browser beschikbaar is.

### Stand van zaken in 2026

| Onderwerp | Stand in november 2026 |
|---|---|
| Standaard | **Wasm 3.0**, officieel sinds 17 september 2025 (WasmGC, 64-bit geheugen, exception handling, tail calls, ...) |
| Geheugenbeheer | Standaard een lineair geheugen; sinds 3.0 **optioneel garbage collection** (WasmGC) |
| Browser-support | **97,37%** van de gebruikers (caniuse) |
| Buiten de browser | **WASI 0.3** (11 juni 2026) met native async; Wasm op servers, edge en kleine toestellen |
| Laden in de browser | Nog via `fetch` + `instantiateStreaming`; laden als ES-module is onderweg |

De belangrijkste vaststelling: WebAssembly werd ontworpen als een nieuw soort code voor webbrowsers, maar vandaag is de browser één van de runtimes, niet de enige.

### De vier ontwerpdoelen

1. **Fast, efficient and portable**: de code draait bijna even snel als native code, op elk platform.
2. **Readable and debuggable**: het is een low-level taal, maar er bestaat een tekstformaat (`.wat`) dat een mens kan lezen.
3. **Keep secure**: Wasm draait in een sandbox en respecteert de beveiligingsregels van de browser (same-origin policy, Content Security Policy).
4. **Don't break the web**: het werkt samen met bestaande webtechnologie en blijft achterwaarts compatibel.

Deze doelen verklaren veel van de trends verderop. *Keep secure* leidt tot het capability-model van WASI (deel 7). *Don't break the web* verklaart waarom directe toegang tot de DOM zo traag vooruitgaat (deel 6).

### Andere pogingen

Wasm is niet de eerste poging om meer dan JavaScript in de browser te krijgen:

| Jaar | Technologie | Lot |
|---|---|---|
| 1995 | Java-applets | Verdwenen |
| 1996 | ActiveX (Microsoft) | Verdwenen |
| 1996 | Flash | Gestopt eind december 2020 |
| 2007 | Silverlight (Microsoft) | Verdwenen |
| 2011 | Google Native Client (NaCl), later PNaCl | Verdwenen, vervangen door Wasm |
| 2011 | Dart in een aangepaste browser (Dartium) | Dart compileert nu naar JS en Wasm |
| 2013 | asm.js | Voorloper van Wasm |
| 2017 | WebAssembly | In alle grote browsers |

De meeste mislukten om dezelfde redenen: ze vroegen een **plug-in** (extra aanvalsoppervlak, niet op elk toestel), werkten **buiten het beveiligingsmodel** van de browser, of werden door **één bedrijf** beheerd. Wasm is het eerste dat door **alle browserfabrikanten samen** ontworpen werd, als open standaard, en dat geen plug-in vraagt.

**asm.js** (2013) was een belangrijke tussenstap: een strikte subset van JavaScript waarvan engines wisten dat ze die snel konden uitvoeren. Wasm nam dat idee over, maar in een compact binair formaat dat sneller te laden is.

### Is dat niet gewoon de JVM?

De Java Virtual Machine is ook een stack-gebaseerde virtuele machine met een tussenvorm (bytecode) waar meerdere talen naartoe compileren (Java, Kotlin, Scala). De verschillen:

| | JVM | WebAssembly |
|---|---|---|
| Geheugen | Altijd garbage collection | Standaard een **lineair geheugen** dat het programma zelf beheert; sinds 3.0 **optioneel** WasmGC |
| Beveiliging | Security manager (intussen afgeschaft) | Een module kan standaard **niets**; alles wat ze mag, krijgt ze expliciet mee |
| Afstand tot hardware | Hoger niveau | Dichter bij machinecode |
| Samenwerking met JavaScript | Via aparte bruggen | Ingebouwd in de browser |

> **Let op bij oudere bronnen.** In tutorials en artikels van vóór 2025 lees je vaak dat Wasm geen garbage collection heeft. Sinds Wasm 3.0 klopt dat niet meer: Wasm *kan* de GC van de engine gebruiken, maar dwingt het niet af.

### Use cases

Wasm loont wanneer je **veel rekenwerk** hebt, **bestaande code** uit een andere taal wilt hergebruiken, of **code van derden veilig** wilt uitvoeren.

**In de browser:**

- **Beeld- en videobewerking**: Figma, Photoshop in de browser, ffmpeg.wasm
- **CAD en 3D**: AutoCAD Web, Google Earth
- **Games en emulatie**: game engines, DOSBox, QEMU, MAME
- **Databanken in de browser**: SQLite en DuckDB als Wasm-module
- **Scripttalen**: Python in de browser via Pyodide
- **Machine learning en beeldherkenning**, vaak samen met WebGPU (zie deel 9)
- **Encryptie en compressie**
- **Zoeken aan de clientkant**: Microsoft bouwde `docfind` (Rust + Wasm) voor de zoekfunctie van de VS Code-website (januari 2026)

**Buiten de browser:**

- **Serverless en edge**: Cloudflare Workers, Fermyon Spin (sinds december 2025 onderdeel van Akamai)
- **Plug-ins** die code van derden in een sandbox draaien: filters voor de Envoy-proxy, Shopify Functions, extensies voor de Zed-editor
- **Embedded**: runtimes voor toestellen met maar 256 KB geheugen
- **AI-agents**: sandbox voor tools en gegenereerde code (zie deel 9)

Het accent verschuift van games en beeldbewerking naar **infrastructuur en veilige uitvoering van andermans code**.

> **Voor de docent.** Vraag de zaal welke van deze applicaties ze zelf gebruiken. Bijna iedereen gebruikt Figma of Google Earth zonder te weten dat er Wasm onder zit. Dat is precies het punt van de cijfers hieronder: Wasm wordt veel gebruikt, maar zelden zichtbaar.

### Wasm in cijfers

Een paradox die je moet kunnen uitleggen:

- **Support**: volgens caniuse ondersteunt **97,37%** van de gebruikers WebAssembly (november 2026; in 2025 was dat 96,02%, in 2024 94%).
- **Gebruik**: de **Web Almanac 2025** (HTTP Archive) vindt Wasm op slechts **0,35% van de desktop-sites** en **0,28% van de mobiele sites**. Chrome Platform Status telt Wasm bij ongeveer **5,5% van de paginaladingen** in Chrome, bijna 1 procentpunt meer dan een jaar eerder. Het grootste gemeten `.wasm`-bestand is 228 MB.

De cijfers verschillen omdat ze iets anders meten: het ene telt **sites**, het andere **paginaladingen**, en die worden gedomineerd door een paar heel grote sites. Wasm wordt gebruikt in een paar zware toepassingen die veel mensen bereiken, en steeds vaker **achter de schermen** als onderdeel van bibliotheken. DevClass vatte het in januari 2026 samen als *WebAssembly gaining adoption "behind the scenes"*.

> **Let op bij bronnen.** Over Wasm circuleren cijfers met een vage oorsprong, zoals "41% van de bedrijven gebruikt Wasm in productie". Zoek altijd de oorspronkelijke meting. Een cijfer zonder meting is marketing.

### Even wat geschiedenis

| Jaar | Gebeurtenis |
|---|---|
| 1995 | JavaScript: volledig geïnterpreteerd, traag |
| 2008 | JIT-compilers in de browser: ongeveer 10× sneller; JavaScript wordt breed bruikbaar (bv. Node.js) |
| 2013 | asm.js |
| 2015 | WebAssembly aangekondigd |
| 2017 | WebAssembly in alle grote browsers |
| 2019 | W3C-standaard; eerste versie van WASI |
| 2022 | Wasm 2.0 in grote lijnen af (SIMD, bulk memory, reference types) |
| 2024 | WASI 0.2 en het Component Model |
| 2025 | **Wasm 3.0** (17 september) |
| 2026 | **WASI 0.3** (11 juni) |

Is Wasm een buigpunt zoals de JIT in 2008? Ja, maar op een andere manier: niet als een nieuwe factor tien in de browser, wel doordat Wasm nu op de server draait en talen met een garbage collector kan bedienen.

**Kernpunt.** WebAssembly is een compilatiedoel: een veilig, snel en draagbaar binair formaat voor een virtuele machine, dat in elke browser en in steeds meer andere omgevingen draait.

---

## Deel 2: Compilers, JIT en waarom Wasm anders is

*Kernvraag: waarom is JavaScript soms onvoorspelbaar traag?*

### Interpreter

Een **interpreter** vertaalt code regel per regel terwijl ze uitgevoerd wordt. Voordelen: snel opgestart, geen aparte compilatiestap, ideaal voor webontwikkeling (je tikt code in de DevTools en ziet meteen het resultaat). Nadeel: bij herhaalde code (een lus) wordt dezelfde regel telkens opnieuw vertaald.

### Compiler

Een **compiler** vertaalt alles vooraf naar machinecode. De start is trager, maar de uitvoering is veel sneller: de vertaling gebeurt maar één keer, en de compiler kent de volledige code. Daardoor kan hij **optimaliseren**, bijvoorbeeld een berekening die altijd hetzelfde oplevert buiten een lus halen. Een interpreter kan dat niet: de start zou te lang duren.

### JIT-compiler: het beste van twee werelden

Een **Just-in-Time-compiler** combineert beide. Alle JavaScript-engines werken zo: V8 (Chrome, Node.js), SpiderMonkey (Firefox) en JavaScriptCore (Safari).

1. Alles start in de **interpreter**: snel opgestart.
2. Een **monitor** (profiler) telt hoe vaak een stuk code uitgevoerd wordt. Meerdere keren: **warm**. Heel vaak: **hot**.
3. **Warme** code gaat naar de **baseline compiler**. Die vertaalt snel naar machinecode en bewaart het resultaat (een *stub*). Komt dezelfde code terug met dezelfde types, dan wordt de stub hergebruikt. De baseline compiler draait parallel aan de interpreter en doet enkel snelle optimalisaties.
4. **Hete** code gaat naar de **optimizing compiler**. Die optimaliseert diep, op basis van **veronderstellingen**: "deze constructor maakt altijd objecten met dezelfde properties."
5. **Deoptimalisatie** (*bailing out*): JavaScript is dynamisch. Klopt de aanname 99 keer en de 100ste keer niet, dan moet de engine de geoptimaliseerde code weggooien en terugvallen op een trager niveau. Herhaalt zich dat, dan spreekt men van *thrashing*.

Het resultaat: JavaScript is dankzij JIT veel sneller dan vroeger, maar **de prestaties zijn minder voorspelbaar**. Een kleine codewijziging kan een optimalisatie breken.

### Wat levert een JIT op?

Franziska Hinkel (V8-team, Google) mat hoe lang het duurt om het n-de priemgetal te berekenen in JavaScript en in C++:

- **Zonder optimalisaties** (enkel de interpreter): bij het miljoenste priemgetal ongeveer **77 seconden** voor JavaScript tegenover **9 seconden** voor C++.
- **Met de optimizing compiler** (toen TurboFan): JavaScript zakt naar ongeveer **16 seconden**. De kloof is veel kleiner, maar C++ blijft bijna twee keer zo snel.
- In het begin van de meting zie je **pieken**: de code loopt nog in de interpreter. Rond het honderdste priemgetal treedt de optimizing compiler in werking. Dat is de **opwarmtijd** van een JIT.

### Waar gaat de tijd naartoe?

Lin Clark tekende in haar reeks over WebAssembly (Mozilla Hacks, 2017) schematisch waar de tijd naartoe gaat:

- **JavaScript met enkel een interpreter**: *parse* (code lezen), een lange *execute* en *garbage collection*.
- **JavaScript met JIT**: kortere *execute*, maar er komen *compile + optimize* en *re-optimize* (verloren tijd door foute aannames) bij. In werkelijkheid lopen die stappen door elkaar.
- **WebAssembly**: *decode* in plaats van parse (binair formaat), snellere *compile + optimize*, geen *re-optimize* en geen garbage collection. Uitzondering: talen die WasmGC gebruiken, hebben wel garbage collection, maar dan die van de engine.

### Waarom Wasm anders werkt

| | JavaScript | WebAssembly |
|---|---|---|
| Formaat | Tekst, moet geparset worden | Compact binair formaat, snel te decoderen |
| Types | Dynamisch: de engine raadt ze | Statisch (`i32`, `i64`, `f32`, `f64`): staan in het bestand |
| Optimalisatie | Tijdens het draaien, op aannames | Vooraf, door de compiler van je broncode (bv. LLVM) |
| Deoptimalisatie | Mogelijk | Niet nodig |
| Laden | Downloaden, dan parsen | **Streaming compilation**: compileren tijdens het downloaden |
| Compilatie in de engine | Interpreter, baseline, optimizing | Ook gelaagd (in V8: snelle baseline *Liftoff* + optimizing compiler), maar zonder te gokken |

Het voordeel van Wasm is vooral **voorspelbaarheid** en **piekprestatie bij rekenwerk**, niet dat het altijd sneller is (zie deel 4).

### Assembly en intermediate representation

**Assembly** is een menselijk leesbare taal die één-op-één vertaalt naar machinecode. Elke processorarchitectuur heeft een eigen dialect: x86 is niet ARM.

Wil je 10 talen naar 5 architecturen vertalen, dan heb je 50 vertalers nodig. Met een **Intermediate Representation (IR)** zijn dat er 15: elke taal vertaalt naar de IR (*front-end*), elke architectuur vertaalt vanuit de IR (*back-end*). Zo werken LLVM en Java-bytecode.

**WebAssembly is zo'n tussenvorm**, met een bijzonder doel: een **virtuele** instructieset voor een *conceptuele machine*. Het is geen echte processor, maar staat er veel dichter bij dan JavaScript. Er is **geen één-op-één mapping** met x86 of ARM: de engine van de browser of de runtime vertaalt de Wasm-instructies naar machinecode van jouw toestel. Daardoor draait één `.wasm`-bestand op x86 en ARM.

### De formaten: .wat en .wasm

- **`.wat`** (*WebAssembly Text*): de leesbare variant, waarin je zelf kan schrijven.
- **`.wasm`**: het binaire formaat dat de engine uitvoert. `wat2wasm` zet het ene om naar het andere.

```wat
(module
  (import "math" "callback" (func $callback (param i32)))
  (export "add" (func $add))
  (func $add (param $a i32) (param $b i32) (result i32)
    (local $sum i32)
    local.get $a
    local.get $b
    i32.add
    local.set $sum
    local.get $sum
    call $callback   ;; roept de JavaScript-functie aan met $sum
    local.get $sum)) ;; geeft $sum terug
```

Je ziet een **stack machine**: `local.get` zet waarden op een stapel, `i32.add` neemt er twee en zet de som terug. Gecompileerd is deze module **74 bytes** groot. De eerste vier bytes zijn altijd `00 61 73 6D` (`\0asm`), het *magic number* waaraan een engine een Wasm-bestand herkent; daarna volgen het versienummer en de secties (types, imports, functies, exports, code).

**Kernpunt.** JavaScript wordt snel via een JIT die aannames maakt; Wasm hoeft niets te raden omdat de types en de zware optimalisatie vooraf vastliggen. Wasm is een virtuele assembly: een IR die de engine naar echte machinecode vertaalt.

---

## Deel 3: Een module bouwen en laden

*Kernvraag: hoe krijg ik code uit mijn taal in de browser?*

### Een module laden

```js
const imports = { math: { callback: (x) => console.log("resultaat:", x) } };

const { instance } = await WebAssembly.instantiateStreaming(
  fetch("simple.wasm"),
  imports
);

instance.exports.add(2, 3);   // logt 5 en geeft 5 terug
```

- `fetch` + `instantiateStreaming`: de browser **compileert terwijl hij downloadt**. Dat is de efficiëntste manier. De server moet het bestand serveren met het MIME-type `application/wasm`.
- Het **import-object** geeft JavaScript-functies mee aan de module, zodat Wasm kan terugroepen naar JavaScript.
- De **exports** roep je aan als gewone JavaScript-functies.

Dit patroon herhaal je bij elke module. Deel 6 bespreekt hoe *ESM-integratie* en *source phase imports* dat vereenvoudigen.

### C met Emscripten

**Emscripten** is een compiler-toolchain gebaseerd op **LLVM** die C en C++ naar Wasm compileert.

```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```

```bash
emcc hello.c -o hello.html
```

Je krijgt drie bestanden: `hello.wasm` (de module), `hello.js` (de **glue code**: laadt de module, geeft imports mee zoals een `printf` die naar de console schrijft, en regelt het geheugen) en `hello.html` (laadt alles en toont de uitvoer).

Wil je een eigen functie aanroepen in plaats van `main()`:

```c
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
int add(int a, int b) {
    return a + b;
}
```

```bash
emcc add.c -o add.js -sEXPORTED_RUNTIME_METHODS=ccall,cwrap
```

```js
const add = Module.cwrap("add", "number", ["number", "number"]);
add(2, 3);   // 5
Module.ccall("add", "number", ["number", "number"], [2, 3]);   // in één keer
```

`EMSCRIPTEN_KEEPALIVE` voorkomt dat de compiler de functie als ongebruikt weggooit. `cwrap` en `ccall` zetten JavaScript-waarden om naar C-types. Voor getallen is dat eenvoudig. Strings en structs moet je in het lineaire geheugen van de module kopiëren: Wasm kent als parameters enkel getallen.

### Rust met wasm-bindgen

**Rust** (ontstaan rond 2010 bij Mozilla) is een systeemtaal met een syntax verwant aan C++, die geheugenveiligheid garandeert zonder garbage collector. Voor Wasm is het een van de populairste talen: de binaries zijn klein en er hoeft geen runtime mee.

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);              // een JavaScript-functie aanroepen vanuit Rust
}

#[wasm_bindgen]
pub fn greet(name: &str) {          // een Rust-functie beschikbaar maken voor JS
    alert(&format!("Hello, {}!", name));
}
```

```bash
wasm-pack build --target web
```

**`wasm-bindgen`** genereert de bindingen tussen Rust en JavaScript, bijvoorbeeld het omzetten van een Rust-`&str` naar een JavaScript-string. `wasm-pack` levert een `pkg/`-map met de module en een JavaScript-bestand. Dat gebruik je zo:

```html
<script type="module">
  import init, { greet } from "./pkg/hello_wasm.js";
  await init();          // laadt en instantieert de .wasm
  greet("WebAssembly");  // toont "Hello, WebAssembly!"
</script>
```

Serveer dit via een lokale webserver; modules en `fetch` werken niet via `file://`.

**Het ecosysteem in 2026.** In juli 2025 kondigde het Rust-project aan dat de GitHub-organisatie *rustwasm* wordt opgeheven, omdat er te weinig maintainers waren. **wasm-bindgen** en **wasm-pack** verhuisden naar een nieuwe organisatie, **github.com/wasm-bindgen**, en worden actief onderhouden (nieuwe versies in oktober 2026). Andere repo's werden gearchiveerd of overgedragen. Veel tutorials verwijzen nog naar de oude locatie.

Er bestaan ook volledige webframeworks in Rust (**Yew**, **Leptos**), maar het gewone gebruik blijft: het rekenintensieve deel van een webapplicatie in Rust schrijven.

### AssemblyScript

**AssemblyScript** is een taal met TypeScript-syntax die naar Wasm compileert, met echte types (`i32`, `f64`) en zonder de dynamische delen van JavaScript:

```ts
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
}
```

Een laagdrempelige manier om Wasm uit te proberen zonder een nieuwe taal te leren.

### Blazor WebAssembly (.NET)

**Blazor WebAssembly** laat je single-page applicaties in C# bouwen. De browser downloadt de .NET-runtime als Wasm en voert je code daarbovenop uit. Aantrekkelijk voor .NET-teams die één taal voor front- en back-end willen, maar **in de praktijk niet sneller dan bijvoorbeeld React**: het meeste werk in een gewone web-app is DOM-werk, en dat loopt via JavaScript. De runtime-download vertraagt bovendien de start.

.NET 10 (november 2025) verbetert de opstart met fingerprinting en preloading van assets. Volgens Uno Platform volgt de overstap van de Mono-runtime naar **CoreCLR** op Wasm: een preview in .NET 11, een volledige release in .NET 12. Dat is een verwachting, geen zekerheid.

### Welke talen compileren naar Wasm?

Bijna alle grote talen hebben een Wasm-route. [awesome-wasm-langs](https://github.com/appcypher/awesome-wasm-langs) deelt ze in:

- 🐔 **In production**: C, C++, Rust, Go
- 🐥 **Stable for production usage**: .NET/C#, F#, COBOL, Forth, Grain, Lua, TypeScript (via AssemblyScript), Zig, ...
- 🐣 **Unstable but usable**: Ada, Crystal, D, Elixir, Java, JavaScript, Kotlin, ...

Talen met een garbage collector schuiven op richting stabiel dankzij WasmGC (deel 5).

**Kernpunt.** Je schrijft Wasm niet; je compileert ernaartoe. Je hebt een toolchain nodig (Emscripten, wasm-bindgen, ...) en meestal glue code om JavaScript en Wasm te laten samenwerken.

---

## Deel 4: Snelheid, en vervangt Wasm JavaScript?

*Kernvraag: wanneer loont het?*

### Benchmark

Op de publieke testpagina van takahirox (*JavaScript vs WebAssembly easy benchmark*) berekenen dezelfde recursieve Fibonacci-functie in JavaScript en in C (gecompileerd met `emcc -Os`) een Fibonacci-getal:

```js
function jsFib(n) { if (n === 1) return 1; if (n === 2) return 1; return jsFib(n-1) + jsFib(n-2); }
```

```c
int fib(int n) { if (n == 1) return 1; if (n == 2) return 1; return fib(n-1) + fib(n-2); }
```

Gemeten op 12 november 2026 in Chrome 157 op een MacBook, drie runs: JavaScript **432–484 ms**, WebAssembly **153–158 ms**, dus Wasm is **2,8 à 3,1× sneller**.

**Met een korrel zout.** Een microbenchmark meet één ding, op één machine, in één browserversie, en het resultaat verschilt van run tot run. De JavaScript-engines worden elk jaar sneller. En een recursieve rekenfunctie is het sterkste geval voor Wasm: het zegt niets over een gewone website. Meet altijd je eigen toepassing.

### Is WebAssembly altijd sneller?

| Scenario | Aanbeveling |
|---|---|
| Rekenintensief algoritme (beeld, video, compressie, simulatie) | **WebAssembly** |
| Vooral DOM-werk | **JavaScript** |
| Games | Wasm voor de CPU-intensieve delen |
| WebGL / WebGPU | Hangt af van hoeveel API-aanroepen je doet |
| AI-modellen in de browser | Wasm (met SIMD) als fallback voor **WebGPU** |
| Websites, blogs, formulieren | **JavaScript is your friend** |

Elke oversteek tussen JavaScript en Wasm kost iets: gegevens omzetten en kopiëren. Een Wasm-functie die duizend keer per seconde met kleine objecten aangeroepen wordt, kan trager zijn dan de JS-versie. De vuistregel: **weinig oversteken, veel rekenwerk binnen de module**.

### Zal Wasm JavaScript vervangen?

Nee. Ze zijn **complementair**:

- Wasm is goed in zware berekeningen; JavaScript in lijmcode, UI en DOM.
- Wasm heeft **geen directe toegang tot de DOM** en andere web-API's; alles gaat via JavaScript (deel 6).
- Het JavaScript-ecosysteem is enorm. Zelfs de grootste Wasm-toepassingen hebben JavaScript nodig om te laden en voor de UI.

**Kernpunt.** Wasm is sneller en voorspelbaarder bij rekenwerk, niet bij DOM-werk. Je gebruikt het voor specifieke onderdelen, niet als vervanging van JavaScript.

---

## Deel 5: Trend 1 — Wasm 3.0 en WasmGC

*Kernvraag: wat is er aan de standaard zelf veranderd?*

Op **17 september 2025** werd **WebAssembly 3.0** de nieuwe "live" standaard: de grootste uitbreiding sinds de eerste versie. De meeste functies zaten al jaren in de browsers en zijn nu samen gestandaardiseerd.

### De nieuwe functies

| Functie | Wat het doet | Waarom het ertoe doet |
|---|---|---|
| **WasmGC** + typed references | Garbage-collected structs en arrays in de engine; precieze types voor verwijzingen | Talen met GC worden bruikbaar en kleiner |
| **memory64** | 64-bit adressen voor geheugen en tabellen | Meer dan 4 GB (browsers beperken tot 16 GB) |
| **Multiple memories** | Meerdere geheugens per module | Veilig data kopiëren; modules samenvoegen (`wasm-merge`) |
| **Exception handling** | Native `throw`/`catch` met *tags* | Geen omweg meer via JavaScript voor C++ en andere talen |
| **Tail calls** | Een aanroep op het einde van een functie hergebruikt de stack | Functionele talen en diepe recursie |
| **Relaxed SIMD** | Vectorinstructies die in randgevallen mogen verschillen | Sneller op verschillende hardware |
| **Deterministic profile** | Vast gedrag voor niet-deterministische gevallen | Reproduceerbare uitvoering |
| **Custom annotations** | Annotaties in het tekstformaat | Betere tooling |
| **JS string builtins** | Wasm gebruikt JavaScript-strings rechtstreeks | Minder glue code |

### Kernbegrip: WasmGC

Vóór WasmGC had Wasm één soort geheugen: het **lineaire geheugen**, één grote rij bytes. Een taal met garbage collector (Kotlin, Java, Dart) moest dan haar **eigen GC en runtime meebrengen**, gecompileerd naar Wasm, en alle objecten zelf in dat geheugen beheren. Gevolg: grote bestanden, trage opstart, en twee garbage collectors in dezelfde browser die niets van elkaar weten.

Met **WasmGC** definieert Wasm zelf **struct- en array-types** die in een door de engine beheerde heap leven. De compiler vertaalt de objecten van de taal naar die types, en de **GC van de browser** (dezelfde als voor JavaScript) ruimt ze op.

- **Voordelen**: kleinere binaries, snellere opstart, betere interactie met JavaScript-objecten, geen dubbele GC.
- **Nadelen**: de taal moet haar objectmodel kunnen afbeelden op de WasmGC-types; minder controle over de geheugenindeling.
- **C, C++ en Rust** gebruiken WasmGC niet; zij houden hun lineaire geheugen. WasmGC is een extra optie, geen vervanging.

### Wie gebruikt WasmGC?

- **Kotlin/Wasm**: *Beta* sinds Kotlin 2.2.20 (september 2025). Kotlin 2.4 (juli 2026) voegt experimentele ondersteuning voor het Component Model toe.
- **Compose Multiplatform for web**: *Beta* sinds 1.9.0: dezelfde Kotlin-UI-code voor Android, iOS, desktop en web.
- **Flutter** (Dart) kan zijn webversie naar WasmGC compileren.
- **Java** via J2CL, **OCaml**, **Scala** (Scala.js), **Scheme** (Hoot).

Risico: een browser zonder WasmGC (bijvoorbeeld Safari ouder dan 18.2) kan zulke apps niet draaien. Voorzie een fallback.

### De tien functies in gewone taal

Je hoeft de technische namen niet van buiten te kennen. Belangrijker is dat je begrijpt wat het probleem was, wat er nu kan en waarom dat interessant is. Elke functie heeft in het slide-deck een eigen slide met dezelfde opbouw: wat doet het, vroeger en nu, waarom interessant, wie gebruikt het.

Ze vallen in drie groepen: **(1)** Wasm geschikt maken voor meer talen en grotere programma's (functies 1 tot 4), **(2)** programma's sneller en robuuster maken (functies 5 tot 7), en **(3)** betrouwbaarheid en gebruiksgemak (functies 8 tot 10).

| # | Functie | Wat doet het? | Vroeger | Waarom interessant? | Wie gebruikt het? |
|---|---|---|---|---|---|
| 1 | **Automatische opruiming** (WasmGC) | De browser ruimt het geheugen op dat een programma niet meer nodig heeft | Elke taal moest haar eigen opruimsysteem meebrengen: grote, trage programma's | Veel meer talen kunnen zonder omweg naar het web; kleinere, snellere apps | Bedrijven met Kotlin-, Java- of Dart-apps (JetBrains, Google Flutter) |
| 2 | **Duidelijke verwijzingen** (typed references) | Een verwijzing beschrijft precies waar ze naartoe wijst | De browser moest tijdens het draaien controleren of het klopte | Sneller en veiliger; basis van functie 1 | Bouwers van talen en compilers; gebruikers merken snellere apps |
| 3 | **Meer geheugen** (memory64) | Programma's mogen veel meer dan 4 GB gebruiken (in browsers tot 16 GB) | Maximaal 4 GB | Grote projecten (video, 3D, databanken, AI-modellen) passen erin | Video- en 3D-software, databanken in de browser, AI |
| 4 | **Meerdere geheugens** | Een programma kan meerdere aparte blokken geheugen hebben, bv. privé en gedeeld | Eén groot blok voor alles | Overzichtelijker en veiliger; onderdelen zijn makkelijker samen te voegen | Plug-in-systemen, bedrijven die onderdelen van verschillende teams combineren |
| 5 | **Foutafhandeling** (exceptions) | Een fout kan gemeld en elders netjes opgevangen worden, rechtstreeks in Wasm | Nagebootst via JavaScript: traag en groter | Bestaande (C++-)software kan makkelijker naar het web | CAD, games, beeldbewerking |
| 6 | **Recursie zonder crash** (tail calls) | Een functie kan zichzelf heel vaak aanroepen zonder dat het geheugen volloopt | Na te veel herhalingen: crash (stack overflow) | Geen crashes, eenvoudiger programma's | Functionele talen (OCaml, Scheme), tools die andere talen uitvoeren |
| 7 | **Veel getallen tegelijk** (relaxed SIMD) | Eén bewerking op meerdere getallen tegelijk; de laatste kommacijfers mogen per computer minimaal verschillen | Getallen één voor één, of extra werk voor exact gelijke resultaten | Veel sneller voor beeld, geluid en AI | AI in de browser, foto- en videobewerking, games |
| 8 | **Altijd dezelfde uitkomst** (deterministic profile) | Een instelling waarbij elke computer exact hetzelfde resultaat geeft | Op sommige plaatsen kon het resultaat per computer verschillen | Fouten zijn altijd opnieuw op te roepen; betrouwbaar testen | Blockchains en smart contracts, testsystemen (typische voorbeelden) |
| 9 | **Extra info in de code** (custom annotations) | Notities voor tools (bv. functienamen) in de leesbare tekstversie | Zat enkel in het binaire bestand | Makkelijker te debuggen | Bouwers van debuggers en compilers, bedrijven die Wasm controleren |
| 10 | **Tekst delen met JavaScript** (string builtins) | Wasm gebruikt de tekst van JavaScript rechtstreeks | Tekst moest omgezet en gekopieerd worden met lijmcode | Minder lijmcode, sneller | Tekstverwerkers, document- en spreadsheetapps, zoekfuncties |

**Alledaagse vergelijkingen.** (1) Een gedeelde schoonmaakploeg in plaats van een eigen poetsploeg per bedrijf. (2) Een pakket met een duidelijk label. (3) Een groter bureau. (4) Een eigen kluisje en een gedeeld postvak. (5) Een brandalarm dat rechtstreeks naar de brandweer gaat. (6) Rondjes lopen in plaats van telkens een nieuwe trap bouwen. (7) Vier kassa's tegelijk open. (8) Een recept met exacte hoeveelheden. (9) Post-its voor je tools. (10) Samen in hetzelfde document werken in plaats van kopieën te sturen.

Kanttekeningen: nieuwe functies brengen soms nieuwe fouten mee (de Wasmtime-problemen van april 2026 gingen over functie 3, zie trend 4). Welke bedrijven welke functie gebruiken is een inschatting op basis van waarvoor de functie bedoeld is; het zijn voorbeelden, geen officiële lijst.

### Support per browser (november 2026)

Versie vanaf wanneer een functie standaard aanstaat, volgens de officiële feature-tabel op webassembly.org:

| Functie | Chrome | Firefox | Safari | Wasmtime |
|---|---|---|---|---|
| WasmGC | 119 | 120 | 18.2 | 47 |
| Exception handling (`exnref`) | 137 | 131 | 18.4 | 47 |
| Tail calls | 112 | 121 | 18.2 | 22 |
| memory64 | 133 | 134 | achter vlag | 30 |
| Relaxed SIMD | 114 | 145 | achter vlag | 15 |
| JS string builtins | 130 | 134 | 26.2 | n.v.t. |
| JSPI | 137 | 153 | 27 | n.v.t. |
| Stack switching | achter vlag | – | – | – |

De kern van Wasm is overal; nieuwe functies komen per browser op een ander moment. Gebruik **feature detection** (bijvoorbeeld de bibliotheek `wasm-feature-detect`) en een fallback.

**Kernpunt.** Wasm 3.0 maakt Wasm geschikt voor talen met een garbage collector en voor grote applicaties. Bestaande modules blijven werken.

---

## Deel 6: Trend 2 — Wasm als eersteklas webtaal

*Kernvraag: waarom hebben we nog altijd JavaScript als tussenpersoon nodig?*

In februari 2026 schreef Mozilla dat WebAssembly nog altijd een *tweederangs taal op het web* is. De reden is eenvoudig: WebAssembly kan de webpagina niet rechtstreeks aanspreken. Alles loopt via JavaScript.

### Kernbegrip: glue code

**Glue code** (lijmcode) is JavaScript die een WebAssembly-module **laadt** en laat **praten met de browser**. WebAssembly kent enkel getallen. Voor tekst of een melding op het scherm is dus extra JavaScript nodig, en dat is per programmeertaal anders. Tools zoals **wasm-bindgen** (Rust) en **Emscripten** (C) genereren die lijm, maar het blijft extra code en een beetje trager.

Het gevolg: veel ontwikkelaars kiezen gewoon JavaScript, ook als WebAssembly technisch beter zou passen. *Vergelijking: een tolk tussen twee mensen die een andere taal spreken.*

### Wat wordt eraan gedaan?

De lijm wordt stap voor stap kleiner:

1. **Laden als gewone module**: een `.wasm`-bestand importeren zoals gewone JavaScript (in aantocht; bundlers en Deno kunnen het al).
2. **Tekst delen**: WebAssembly gebruikt de tekst van JavaScript rechtstreeks (functie 10 van Wasm 3.0). Werkt al.
3. **Wachten zonder vast te lopen (JSPI)**: zie hieronder. Werkt al.

Het gaat vooral om laden, tekst en wachten: het saaie maar nuttige lijmwerk. Dat is de realistische winst op korte termijn.

### Kernbegrip: JSPI

Veel bestaande programma's (bv. in C) **wachten** op een antwoord voor ze verdergaan. De browser werkt anders: hij doet intussen iets anders. Vroeger loste de tool **Asyncify** dit op door je code om te schrijven, wat haar groter en trager maakte. **JSPI** (JavaScript Promise Integration) laat de browser het programma gewoon **pauzeren** tot het antwoord er is. Het werkt sinds dit jaar in alle grote browsers. Wil je ook oudere browsers ondersteunen, voorzie dan een alternatief. *Vergelijking: in een restaurant bestellen en intussen iets anders doen.*

### En de webpagina (DOM) rechtstreeks aanpassen?

**Nog niet**, en misschien nooit zoals je het verwacht. De webpagina is gemaakt voor JavaScript, en elke koppeling moet veilig en compatibel blijven met alle bestaande websites. In 2026 schrijf je dus nog lijmcode, maar minder dan vroeger. Voor werk dat vooral de webpagina aanpast, blijft JavaScript de logische keuze.

**Kernpunt.** WebAssembly heeft JavaScript nodig als tussenpersoon. Die lijm wordt kleiner, maar verdwijnt niet.

---

## Deel 7: Trend 3 — Wasm buiten de browser

*Kernvraag: is WebAssembly het nieuwe Docker?*

In 2019 schreef Solomon Hykes, medeoprichter van Docker, dat Docker niet nodig geweest zou zijn als WebAssembly met WASI in 2008 bestaan had. Zeven jaar later zien we waarom die uitspraak serieus genomen wordt, én waarom ze nog niet uitgekomen is.

### Kernbegrip: WASI

Een WebAssembly-programma kan van zichzelf enkel **rekenen**. **WASI** (*WebAssembly System Interface*) is de afspraak waarmee het buiten de browser **bestanden, netwerk en de klok** kan gebruiken.

Het bijzondere is het **capability-model**: een gewoon programma kan standaard alles wat de gebruiker kan, een WebAssembly-programma kan **standaard niets**. Je geeft per keer toestemming: deze map, dit netwerkadres. Daardoor is het veilig vanaf de start. *Vergelijking: een gast in je huis die enkel de kamers mag betreden die jij openzet.* Versies: 0.1 (2019), 0.2 (januari 2024), 0.3 (11 juni 2026).

### Kernbegrip: Component Model

Onderdelen die in verschillende talen geschreven zijn, konden enkel getallen uitwisselen. Het **Component Model** lost dat op met een **gedeelde beschrijving** (WIT) van wat een onderdeel doet. Een onderdeel in Rust kan zo een onderdeel in Python aanroepen, met gewone tekst en lijsten. *Vergelijking: LEGO-blokjes met dezelfde noppen.* Op de server is het bruikbaar, in de browser nog in ontwerp.

### WASI 0.3 (11 juni 2026)

WASI 0.3 voegt **asynchroon werk** toe: een programma kan op iets traags wachten zonder de rest te blokkeren, zonder omslachtige constructie en passend bij `async`/`await`. Het is nog niet af (bv. threads ontbreken), en over WASI 1.0 bestaat geen officiële datum.

### Wasmtime

**Wasmtime** is een programma dat **WebAssembly uitvoert buiten de browser**, zoals Chrome dat doet voor websites. Het wordt gemaakt door de **Bytecode Alliance** (open source) en is geschreven in **Rust**. Het is de **referentie voor WASI**: nieuwe functies komen er het eerst. Sinds versie 46 draait WASI 0.3 standaard, sinds versie 47 ondersteunt het ook garbage collection en foutafhandeling. Het wordt gebruikt door **Spin** en **SpinKube** en door Microsofts **Wassette** (tools voor AI-agents). Omdat Wasmtime de sandbox bewaakt, is zijn beveiliging cruciaal (trend 4).

### Wie gebruikt het nog op de server?

- **Platformen**: Spin en SpinKube, wasmCloud, Cloudflare Workers. In december 2025 kondigde **Akamai** de overname van **Fermyon** (het bedrijf achter Spin) aan.
- **Plug-in systemen**: code van derden veilig draaien, bv. **Shopify Functions**, filters voor de **Envoy**-proxy en extensies voor de editor **Zed**.
- **Kleine toestellen**: een runtime die draait op toestellen met maar 256 kilobyte geheugen.

Waarom? Een WebAssembly-programma is klein, start in milliseconden, draait op elke processor en is veilig afgeschermd.

### Is het dan het nieuwe Docker?

Nee, ze vullen elkaar aan. Een container is ideaal voor **volledige applicaties** met veel onderdelen; WebAssembly is sterk voor **kleine, snelle functies en plug-ins**. Een container start in seconden en is tientallen tot honderden MB groot, een WebAssembly-programma start in milliseconden en is KB tot enkele MB groot (typische ordes van grootte, geen metingen). Het ecosysteem van containers is veel groter en volwassener. WebAssembly draait zelfs *in* Kubernetes, via SpinKube.

**Kernpunt.** WASI geeft WebAssembly een veilige manier om met de computer te praten, het Component Model laat onderdelen samenwerken, en runtimes zoals Wasmtime voeren het uit op servers.

---

## Deel 8: Trend 4 — Security

*Kernvraag: hoe veilig is een sandbox?*

### Kernbegrip: sandbox

Een **sandbox** is een afgesloten ruimte waarin code **enkel kan wat jij toestaat**. Voor WebAssembly betekent dat: het programma kan enkel in zijn **eigen stukje geheugen** werken, het kan **niet naar willekeurige plaatsen springen**, en het heeft **geen toegang** tot bestanden, netwerk of klok zonder toestemming. In de browser gelden dezelfde regels als voor JavaScript. Zo kan je **code van derden draaien zonder erop te vertrouwen**: plug-ins, extensies, AI-code. *Vergelijking: een speelkamer met hekjes.*

### Een sandbox is maar zo sterk als haar runtime

In 2026 had **Wasmtime** meerdere kritieke beveiligingsproblemen waarbij een kwaadaardig programma uit zijn sandbox kon ontsnappen. In **april** twee, enkel bij het grote 64-bit geheugen (functie 3 van Wasm 3.0) of een niet-standaardinstelling. In **oktober** twee ernstigere, in de standaardinstelling, met de hoogste score (9,9 op 10). Het gaat om één runtime, niet om de browsers.

De les: **nieuwe functies zijn nieuw aanvalsoppervlak**, en een sandbox is zo sterk als de compiler van de runtime. Wie niet-vertrouwde code draait (plug-ins, AI-code) moet de runtime **tijdig updaten**.

### Wat de sandbox niet oplost

- **Fouten binnenin de module**: de sandbox beschermt de computer tegen de module, niet de module tegen zichzelf. Een C-programma met een buffer overflow heeft die ook in WebAssembly. Reden om voor nieuwe code Rust te verkiezen.
- **Een `.wasm` is een dependency**: een binair bestand, moeilijk te controleren, vaak in npm-packages. Neem het mee in je supply-chainbeleid (vaste versie, integriteitscontrole, wachttijd voor nieuwe versies).

**Kernpunt.** Een sandbox is een extra laag, geen vrijbrief.

---

## Deel 9: Trend 5 — Wasm en AI

*Kernvraag: wat doet WebAssembly in het AI-tijdperk?*

### 1. AI in je browser

Kleine AI-modellen kunnen **volledig in je browser** draaien, zonder dat je gegevens naar een server gaan: **privacy**, **geen serverkosten** en **offline** bruikbaar. Bibliotheken zoals **Transformers.js** voeren het model uit met **WebGPU** (snel, op de grafische kaart) of **WebAssembly** (werkt overal, op de processor). WebAssembly is het **reservewiel**: je probeert eerst WebGPU en valt terug op WebAssembly. Cijfers als "WebGPU is 10 tot 15 keer sneller" komen van blogs en leveranciers; er is geen betrouwbare, onafhankelijke meting. Meet zelf.

### 2. Een sandbox voor AI-agents

Een AI-agent voert **code uit** en gebruikt **tools**: onbetrouwbare code die in een afgesloten ruimte moet draaien. Met WebAssembly krijgt elke tool een **eigen sandbox** (start in milliseconden) en **enkel de toegang die nodig is**. Microsoft maakte hiervoor **Wassette** (augustus 2025), dat tools voor AI-agents als WebAssembly-onderdelen draait, bovenop Wasmtime.

Maar een sandbox beschermt **niet tegen prompt injection** (een tool die het model misleidt). Het is een beveiligingslaag, geen volledige oplossing.

**Kernpunt.** WebAssembly is in AI het reservewiel voor modellen in de browser en een sandbox voor niet-vertrouwde code.

---

## Deel 10: Vooruitblik, begrippen en conclusie

### Wat om in de gaten te houden

- **WASI 1.0** en de verdere rijping van het **Component Model**.
- **Source phase imports** en **ESM-integratie** in de browsers.
- **Safari**: memory64 en relaxed SIMD staan nog achter een vlag.
- **Stack switching** in de browser, **threads** in WASI.
- **.NET** op CoreCLR (volgens Uno Platform: preview in .NET 11, volledig in .NET 12).
- **Kotlin/Wasm** en Compose for web van *beta* naar *stable*.
- Beveiligingsadviezen van de runtimes.

Dit zijn roadmaps, geen zekerheden: WASI 0.3 werd eerst begin 2026 verwacht en verscheen in juni.

### Wat kan je er zelf mee?

- **Gebruik Wasm zonder het te schrijven**: SQLite, DuckDB, ffmpeg en Pyodide bieden een Wasm-versie.
- **Probeer Rust + wasm-bindgen** voor een rekenintensief stuk van een project, en **meet** voor en na.
- **Gebruik feature detection en een fallback** voor nieuwe functies (WasmGC, JSPI, WebGPU).
- **Behandel `.wasm` als een dependency**: versie vastzetten, integriteit controleren.
- Voer **niet-vertrouwde code** uit in een Wasm-sandbox, en **update** de runtime.
- **Wees kritisch** over cijfers en benchmarks.

### Begrippenlijst

| Begrip | Betekenis |
|---|---|
| **WebAssembly (Wasm)** | Binair instructieformaat voor een virtuele machine; compilatiedoel voor vele talen |
| **Compilatiedoel (target)** | Formaat waar een compiler naar vertaalt (x86, ARM, Wasm) |
| **Interpreter** | Vertaalt en voert code regel per regel uit |
| **Compiler** | Vertaalt alles vooraf naar machinecode en kan optimaliseren |
| **JIT-compiler** | Interpreteert, en compileert warme en hete code tijdens het draaien |
| **Deoptimalisatie** | Een JIT gooit geoptimaliseerde code weg omdat een aanname niet meer klopt |
| **Assembly** | Leesbare low-level taal, één-op-één met machinecode, per architectuur |
| **Intermediate Representation (IR)** | Tussenvorm tussen taal en machinecode (LLVM IR, JVM-bytecode, Wasm) |
| **`.wasm` / `.wat`** | Binair formaat / leesbaar tekstformaat |
| **Streaming compilation** | Compileren terwijl de module nog gedownload wordt |
| **Emscripten** | LLVM-gebaseerde toolchain die C/C++ naar Wasm compileert |
| **Glue code** | JavaScript die een Wasm-module laadt, data omzet en web-API's bereikbaar maakt |
| **wasm-bindgen** | Genereert bindingen tussen Rust en JavaScript |
| **Lineair geheugen** | Het eigen geheugenblok van een Wasm-module (een rij bytes) |
| **WasmGC** | Door de engine beheerde heap met structs en arrays; garbage collection voor Wasm |
| **memory64** | Wasm-geheugen met 64-bit adressen (meer dan 4 GB) |
| **Tail call** | Aanroep op het einde van een functie die de stack hergebruikt |
| **Exception handling** | Native `throw`/`catch` in Wasm |
| **SIMD** | Eén instructie op meerdere gegevens tegelijk |
| **ESM-integratie / source phase imports** | Een `.wasm`-bestand importeren als module |
| **JSPI** | Laat synchrone Wasm-code wachten op een JavaScript-Promise |
| **Asyncify** | Oudere, tragere techniek die Wasm-code herschrijft om te kunnen pauzeren |
| **WASI** | Gestandaardiseerde systeeminterface voor Wasm buiten de browser |
| **Capability** | Expliciet meegegeven recht (een map, een socket); zonder capability geen toegang |
| **Component Model** | Standaard voor samenwerking tussen Wasm-modules met rijke types, over talen heen |
| **WIT** | Taalonafhankelijke notatie voor de interfaces van een component |
| **Wasmtime** | Programma dat WebAssembly uitvoert buiten de browser (Bytecode Alliance, in Rust); referentie voor WASI |
| **Sandbox** | Afgeschermde omgeving waarin code enkel kan wat expliciet is toegestaan |
| **Runtime** | Programma dat Wasm uitvoert (Wasmtime, WasmEdge, browser-engines) |

### Conclusie

1. **WebAssembly is een compilatiedoel**, geen taal: veilig, snel en draagbaar.
2. **Het vervangt JavaScript niet**: gebruik het voor rekenwerk en hergebruik van bestaande code.
3. **Wasm 3.0 (2025)** maakt het geschikt voor talen met garbage collection en grote applicaties.
4. **Wasm blijft een tweederangs burger op het web**: de glue code wordt kleiner, maar verdwijnt niet.
5. **Buiten de browser** groeit het snel (WASI 0.3, Component Model), als plug-in-, edge- en serverruntime.
6. **Veilig by design**, maar een sandbox is zo sterk als haar runtime, en binnenin blijft code code.
7. **In AI** is Wasm het vangnet voor modellen in de browser en een sandbox voor niet-vertrouwde code.

---

## Bronnen

- WebAssembly 3.0 (17/09/2025): webassembly.org/news/2025-09-17-wasm-3.0
- The States of WebAssembly (21/01/2026): webassembly.org/news/2026-01-21-states-of-webassembly
- Feature-tabel: webassembly.org/features (features.json, geraadpleegd 12/11/2026)
- Uno Platform, *The State of WebAssembly – 2025 and 2026* (Gerard Gallant, januari 2026)
- Web Almanac 2025, hoofdstuk WebAssembly (HTTP Archive)
- caniuse.com/wasm en caniuse.com/mdn-webassembly_jspi (november 2026)
- WASI 0.3: wasi.dev/releases/wasi-p3
- Mozilla Hacks, *Making WebAssembly a first-class language on the Web* (februari 2026)
- D. Ehrenberg, *When Is WebAssembly Going to Get DOM Support?*, ACM Queue (juli 2025)
- DevClass, *WebAssembly gaining adoption "behind the scenes"* (28/01/2026)
- Wasmtime security advisories: github.com/bytecodealliance/wasmtime/security/advisories (CVE-2026-34971, -34987, -115889, -115893)
- Akamai, overname van Fermyon (01/12/2025); CNCF, wasmCloud als incubating project (12/11/2024)
- Microsoft Open Source Blog, *Introducing Wassette* (06/08/2025)
- Rust Blog, *Sunsetting the rustwasm GitHub org* (21/07/2025); crates.io (wasm-pack, wasm-bindgen)
- JetBrains/Kotlin: Kotlin 2.2.20, Kotlin 2.4.0 (whatsnew24), Compose Multiplatform 1.9.0
- Franziska Hinkel (V8-team): grafieken JavaScript versus C++ (priemgetallen)
- Lin Clark, cartoon-reeks over WebAssembly, Mozilla Hacks (2017)
- takahirox, *JavaScript vs WebAssembly easy benchmark* (eigen meting 12/11/2026)
- awesome-wasm-langs (GitHub)
