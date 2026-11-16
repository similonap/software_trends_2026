# Korte sprekersnotities

Per slide de bullets voor de "Kort"-modus van de presentatie. Pas gerust aan en draai daarna `python3 maak.py`.
Een bullet die begint met "→ " is de overgang naar de volgende slide; "Examen: " wordt geel gemarkeerd.

## cover | 1. Software Trends

- Bijna elke webapp (webshop, dashboard, SaaS) gebouwd met React, Angular, Vue of Svelte, vaak + Next.js of Nuxt
- Frameworks veranderen te snel om te volgen → focus op concepten en grote bewegingen, geen featurelijstjes
- Twee lagen: eerst bouwstenen (rendering, hydration, server components, signals), dan vijf trends
- Rode draad: AI, groot deel van de code wordt door AI-agents geschreven, frameworks passen zich aan
- Slides met Kernbegrip rechtsboven = definities die je moet kennen; begrippenlijst achteraan

## zero-days | 2. Zero days have passed

- dayssincelastjavascriptframework.com: teller staat bijna altijd op nul; overdreven, maar tempo is echt hoog
- Op 12 maanden: Next.js 16, eerste stabiele React Compiler, 2x Angular, Vite 8, RC's van Vue en SvelteKit
- Oktober 2026: twee nieuwe frameworks, Remix 3 en TanStack Start 1.0
- RC = release candidate: functioneel compleet, nog in testfase
- Eén framework uit het hoofd leren heeft weinig zin; concepten blijven (hoe HTML maken, waar draait code, wat verandert er)
- Wie concepten snapt, leert elk nieuw framework snel → daarom focus van de les

## agenda | 3. Agenda

- Start: wat is (meta-)framework + cijfers over landschap 2026
- Belangrijkste theorieblok = bouwstenen: rendering (browser, server, build), hydration, server components, virtual DOM vs signals vs compiler
- Vijf trends: signals/compilers standaard, server vs browser, security, AI-agent als gebruiker, AI verandert het web
- Security: code op de server brengt nieuwe risico's
- Kernbegrip-slides: telkens definitie, werking, voorbeeld, voor- en nadelen; andere slides tonen praktijk

## kb-framework | 4. Library vs framework: wie roept wie aan?

- Definitie: een library roep jij aan, een framework roept jou aan
- Links: date-fns in vanilla JS; jij registreert click-handler, roept format() aan, zet zelf textContent; library = gereedschapskist
- Rechts: React; nergens Klok() in je code, enkel createRoot + render; React beslist wanneer (opstart, bij elke setDatum)
- React past ook zelf de DOM aan: vergelijkt nieuw resultaat met vorig (later: virtual DOM, reconciliation)
- Inversion of control / Hollywood-principe: don't call us, we'll call you
- date-fns blijft rechts gewoon library: format roep je nog zelf aan
- → React doet IoC, gedraagt zich als framework, maar noemt zich library: volgende slide waarom allebei klopt

## kb-spectrum | 5. Geen hokjes maar een spectrum

- Geen ja-neevraag: hoeveel controle geef je af, over welke delen → spectrum
- Library (date-fns, Lodash): beslist niets, jij doet structuur, flow, DOM
- React: neemt enkel UI-rendering over (IoC), routing/data/build/mappen aan jou; kan zelfs in één div van bestaande pagina → noemt zich library
- Angular: ook routing, formulieren, HTTP-client, dependency injection, conventies; Vue en Svelte lichter (officiële router + state)
- Meta-framework (Next.js, Nuxt, SvelteKit): server, file-based routing, data, build, deploy; spaart combineren van tientallen tools, maar je erft hun keuzes
- React-team raadt sinds docs 2023 framework aan (Next.js, React Router); Create React App begin 2025 officieel afgeschaft
- Examen: waarom React soms library, soms framework? IoC voor renderen, maar routing, data en build aan jou

## cijfers | 6. State of JavaScript 2025

- State of JS = jaarlijkse enquête; editie 2025 gepubliceerd feb 2026, ca. 13.000 respondenten
- Onderscheid gebruik (al gebruikt) vs tevredenheid (opnieuw gebruiken); veel gebruik kan met ontevredenheid, bv. omdat je job het oplegt
- React 84% gebruik, maar lagere tevredenheid; Solid 5 jaar op rij hoogste tevredenheid bij ca. 10% gebruik
- Next.js 59%, positief 21% vs negatief 17%: dicht bij elkaar
- TypeScript heeft gewonnen: 40% schrijft enkel TS
- AI stijgt snelst: Claude 22% → 44%, Cursor 11% → 26%, ChatGPT 68% → 60%; van chatten naar AI-tools in je code
- → Dat wordt trend vier

## kb-bundler | 7. Wat doet een build tool?

- Code die jij schrijft (TS, JSX, honderden modules, aparte CSS) ≠ code die browser uitvoert
- Transpileren: TS/JSX → gewone JS, browsers begrijpen geen JSX
- Bundelen: minder bestanden, minder requests; tree shaking: ongebruikte imports weg (dode takken van boom schudden); minificeren: spaties, commentaar, lange namen weg
- Code splitting: elke pagina eigen JS, pas geladen bij bezoek; hash in naam (app-3f9a.js) → nieuwe code = nieuwe naam, browser downloadt opnieuw
- Dev server met HMR: enkel gewijzigde module vervangen, geen herladen
- Rust: native machinecode + makkelijk meerdere CPU-kernen; JS-tools daarin veel trager

## tooling | 8. Build tools: Vite en webpack

- webpack jarenlang standaard: 87% gebruik (vooral oude projecten), tevredenheid gezakt naar 26%
- Vite (Evan You, maker van Vue): 84% gebruik, 98% tevreden; standaard voor nieuwe projecten; React verwijst sinds 2025 naar Vite of meta-framework
- Waarom snel: in dev geen bundling, browser importeert zelf modules → dev server start bijna meteen; bundelen enkel voor productie
- Vroeger esbuild (dev) + Rollup (prod) → kleine verschillen lokaal vs productie; Vite 8 (maart 2026): beide vervangen door Rolldown (Rust)
- Linear: productie-build van 46 naar 6 seconden; Next.js 16 standaard Turbopack, ook Rust
- Belang: AI-agent past aan, bouwt en test in een lus → halve minuut build tientallen keren per taak

## eigenaarschap | 9. Wie zit er achter de frameworks?

- Open source is gratis, maar iemand betaalt de developers → volg het geld
- Model 1, foundation (neutrale non-profit): React feb 2026 naar React Foundation onder Linux Foundation; Meta beslist niet meer alleen
- Model 2, bedrijf verdient elders aan (meestal hosting): Vercel maakt Next.js; Nuxt-team sinds juli 2025 bij Vercel
- Cloudflare kocht Astro (jan 2026); Anthropic kocht Bun want Claude Code draait erop; VoidZero (Vite) lanceert hostingplatform; Remix sinds 2022 van Shopify
- Niet noodzakelijk slecht: alles blijft open source, veel investering; maar vraag bij standaardkeuzes wie er baat bij heeft (meer server = meer hostingomzet)
- Positief: onder druk van community kreeg Next.js in 2026 stabiele Adapter API, makkelijker buiten Vercel deployen

## kb-csr-ssr | 10. Client side rendering vs server side rendering

- Kernvraag: waar wordt de HTML gemaakt? Twee basismodellen
- CSR: bijna lege HTML (lege div + JS-bestand), JS haalt data via API (fetch naar REST) en bouwt DOM; = SPA, navigeren volledig in JS
- CSR voordelen: na laden snel en interactief, statische hosting, server enkel API; nadelen: wit scherm/spinner, zoekmachines en social previews zien soms lege pagina, veel JS
- SSR: per request haalt server data, rendert volledige HTML, gebruiker ziet meteen inhoud; daarna JS interactief maken = hydration
- SSR voordelen: snelle eerste weergave, SEO; nadelen: server werkt bij elk request (kost), hydration kost tijd
- Examen: admin-dashboard achter login (geen SEO, veel interactie) → CSR; webshop die gevonden wil worden → SSR of variant
- → Hydration op volgende slide

## kb-hydration | 11. Hydration

- SSR-HTML ziet er volledig uit, maar is gewoon tekst: knop heeft nog geen click handler, formulier geen validatie
- Hydration: framework voert dezelfde componenten opnieuw uit in browser, bouwt boom, vergelijkt met bestaande HTML, koppelt event handlers en state
- Beeld: gedroogde spons onder water houden
- Drie fases: HTML zichtbaar maar klik doet niets → JS laden en uitvoeren → interactief
- Nadeel: dubbel werk (server én browser) en code van alle componenten naar browser, ook footer of artikeltekst
- Oplossingen: partial/incremental hydration (enkel delen of pas wanneer in beeld; Angular standaard sinds v22), islands (Astro), React Server Components (nooit naar browser)

## kb-ssg-streaming | 12. Static site generation en streaming

- SSG: HTML één keer tijdens build, gewone bestanden op CDN
- CDN = wereldwijd netwerk van servers met kopieën; gebruiker in Japan krijgt bestand uit Tokio, niet uit Brussel
- SSG: zeer snel, goedkoop, geen server-code per request (veilig); nadeel: bij wijziging opnieuw builden, geen personalisatie ('welkom, Jan')
- Streaming, voorbeeld productpagina: productinfo snel, reviews uit trage externe dienst; klassieke SSR wacht tot alles klaar is
- Streaming: meteen eerste HTML met placeholder (spinner), reviews later over dezelfde HTTP-verbinding; HTTP laat response in stukken toe
- React: traag deel in Suspense, fallback = wat ondertussen getoond wordt
- Partial prerendering = statische delen bij build, dynamische gaten bij request gestreamd; Next.js-standaard, zie trend twee

## kb-rsc | 13. React Server Components (RSC)

- RSC = grootste verandering in React van de laatste jaren, basis van Next.js
- Idee: component dat enkel blogposts toont heeft geen interactie nodig → waarom code naar browser sturen en hydrateren?
- Server Component (standaard in Next.js): enkel op server, mag async, leest rechtstreeks database (geen API-endpoint); browser krijgt UI-beschrijving, geen code; dus geen state of klikken
- Client Component: 'use client' bovenaan; klassiek component, voorgerenderd op server + gehydrateerd; useState, effects, events (bv. LikeButton)
- Regel 1: server mag client bevatten, client kan geen server component importeren (browser voert geen server-code uit)
- Regel 2: props server → client serialiseerbaar (getallen, strings, objecten; geen functies); serialisatie komt terug in trend drie
- Voordelen: minder JS, data dicht bij database; nadelen: complexer mentaal model, meer serverwerk

## kb-dom | 14. De DOM (Document Object Model)

- Nodig om virtual DOM te snappen
- Browser parset HTML-tekst tot boom van objecten in geheugen = DOM; elk element en stukje tekst is node met parent, kinderen, siblings
- Scherm = weergave van de boom; boom aanpassen → scherm past aan; JS via document-object
- Rechts: querySelector ul, createElement li, textContent Kaas, appendChild → meteen derde item
- Duur: JS-object aanpassen kost bijna niets, maar DOM-wijziging → reflow (layout herberekenen, lijstitem duwt alles naar beneden) + repaint (pixels)
- Honderd DOM-wijzigingen in lus met tussendoor afmetingen opvragen → mogelijk honderd reflows, traag en schokkerig
- Onthoud: DOM = objectboom uit HTML, aanpassen duur → frameworks doen zo weinig mogelijk DOM-aanpassingen

## kb-imperatief | 15. Imperatief vs declaratief

- Waarom frameworks voor de DOM? Verschil imperatief vs declaratief
- Links imperatief: stap voor stap hoe; teller, knop opzoeken, tekst aanpassen, klasse toevoegen boven 5
- Bug in voorbeeld: zakt teller onder 5, dan wordt klasse niet verwijderd → data en scherm uit sync; typisch bij honderden elementen en tientallen acties
- Rechts declaratief: beschrijf wat, niet hoe; Counter beschrijft UI voor elke toestand tegelijk
- count verandert → React roept functie opnieuw aan en zoekt zelf DOM-aanpassingen; vergeten klasse kan niet
- UI = f(state): kernidee achter React, Vue, Angular, Svelte
- → Vraag: hoe weet React welke DOM-aanpassingen nodig zijn zonder alles opnieuw op te bouwen? Antwoord: virtual DOM

## kb-vdom | 16. De virtual DOM

- Stap 1: JSX lijkt HTML, maar is geen HTML en geen geldige JS; browser begrijpt het niet
- Stap 2: build tool (bv. Vite + React-plugin) maakt er functie-aanroep van: jsx(type, props), vroeger React.createElement; JSX = syntactische suiker
- Stap 3: uitvoeren geeft gewoon object (type, props, children) → boom van objecten = virtual DOM
- Geen kopie van echte DOM met honderden eigenschappen, enkel lichte beschrijving: type, props, kinderen
- Object aanmaken kost nanoseconden, geen layout of tekenen → elke wijziging nieuwe boom, vergelijken, enkel verschillen naar echte DOM
- Misvatting: virtual DOM is niet sneller dan DOM; perfecte imperatieve code is sneller. Voordeel: declaratief én redelijk efficiënt

## kb-render-commit | 17. Van state naar scherm: render en commit

- 1 Trigger: setCount plant update; meerdere updates in één handler gebundeld tot één render = batching
- 2 Render: React roept Counter opnieuw aan → nieuwe virtuele boom; renderen = componentfunctie uitvoeren, niet pixels tekenen
- 3 Reconciliation: nieuwe vs vorige boom → lijst echte wijzigingen (details volgende slide); 4 Commit: enkel die wijzigingen in DOM, browser tekent
- Renderfase (2+3): enkel geheugen, moet puur zijn, geen side effects (data versturen, globale variabelen)
- Fiber (sinds React 16): renderwerk in kleine eenheden, onderbreekbaar voor dringender werk (gebruiker typt); basis voor startTransition, useDeferredValue
- Commitfase niet onderbreekbaar: DOM in één keer, nooit half scherm; daarna effects (useEffect)
- Render met zelfde boom = nul DOM-aanpassingen; niet render zelf duur, wel veel onnodige renders van grote componenten

## kb-reconciliation | 18. Het reconciliation-algoritme

- Reconciliation = vergelijken oude en nieuwe virtuele boom; hart van React, typische examenvraag
- Probleem: tree edit distance, beste algemene algoritmes O(n³); 1.000 elementen = miljard vergelijkingen per klik of toets → onbruikbaar
- Oplossing: heuristiek in O(n), niet altijd minimaal maar bijna altijd goed genoeg
- Twee aannames: verschillend type = verschillende boom; developer duidt stabiele kinderen aan met key
- Regel 1 ander type (div → section, Counter → Timer): hele deelboom weg incl. state, opnieuw opgebouwd
- Regel 2 zelfde type: HTML-tag → enkel gewijzigde attributen (bv. className); component → instantie en state blijven, nieuwe props
- Regel 3 kinderen recursief: zonder keys op positie, met keys op key → volgende slides tonen waarom dat belangrijk is

## kb-reconciliation-vb | 19. Reconciliation: twee voorbeelden

- Boven: className card → card open; type blijft div → regel 2, één DOM-aanpassing (className)
- Kinderen: zelfde positie, zelfde Counter → instantie en state (bv. 7) blijven
- Onder: div wordt section, zelfde className en Counter; voor mens klein, voor React regel 1
- Hele oude div met inhoud verwijderd, nieuwe section + Counter → terug naar 0, state kwijt
- Les: wissel type van wrapper niet op basis van state (div dicht, section open)
- → Tweede valkuil met zelfde oorzaak, veel moeilijker te zien in code: volgende slide

## kb-component-in-component | 20. Valkuil: een component binnen een component

- Klassieke beginnersfout, volgt uit regel 1
- Type van HTML-tag = string 'input'; type van component = het functie-object zelf; React vergelijkt met === (identiteit)
- Fout: Veld binnen Formulier; letter typen → setNaam → Formulier rendert → function Veld opnieuw uitgevoerd → nieuw functie-object
- Oude Veld === nieuwe Veld is false → ander type → input vernietigd en nieuw gemaakt
- Gevolg: focus weg na elke letter; eigen useState in Veld telkens terug naar beginwaarde; zelfde als div → section, maar onzichtbaar
- Oplossing: Veld bovenaan het bestand definiëren, één keer gemaakt, zelfde type → regel 2, enkel value aangepast; data via props (naam, setNaam)
- → Zelfde idee komt terug als referentiële gelijkheid bij React.memo en useCallback

## kb-keys | 21. Lijsten en de key-prop

- Regel 3 apart, want hier loopt veel mis; voorbeeld: [Melk, Brood] → Kaas vooraan erbij
- Zonder key, op positie: 0 Melk→Kaas tekst, 1 Brood→Melk tekst, 2 nieuwe li → 3 operaties voor één invoeging; bij 1.000 items 1.001
- Erger: state (aangevinkt vakje, half ingevuld veld) hangt aan positie → Melk aangevinkt wordt Kaas aangevinkt
- Met key: m en b bestaan al, blijven staan; k nieuw → één invoeging, state bij juiste item
- Key in map-functie: uniek binnen lijst en stabiel over renders; id uit database ideaal
- Niet de index (tenzij lijst nooit verandert): verschuift bij invoegen, verwijderen, sorteren → zelfde probleem; React waarschuwt in console bij vergeten key
- Samengevat: key helpt reconciliation herkennen welk element welk is

## kb-signals | 22. Signals

- Tweede strategie; gebruikt door Angular, Solid, Svelte, Vue, Preact, elk eigen syntax, zelfde principe
- Signal = waarde met lijst abonnees: wie las, wordt verwittigd bij wijziging
- Bouwstenen: signal (schrijfbaar, count = 0), computed (afgeleid, double = count x 2), effect (draait opnieuw: loggen, DOM bijwerken)
- Dependency tracking: computed leest count() → systeem noteert afhankelijkheid; geen handmatige dependency-lijst zoals useMemo in React
- count.set(5) → double herberekend, effect draait, logt 10
- Template: double() in Angular-template → enkel die tekstnode aangepast, geen componentfunctie, geen boom = fine-grained reactivity
- Verschil: VDOM eenheid = component, achteraf zoeken; signals eenheid = waarde, op voorhand weten

## kb-signals-intern | 23. Hoe werkt een signal vanbinnen?

- Basisprincipe past in ca. 15 regels JS; helpt dependency tracking begrijpen
- Globale variabele actief = effect dat nu draait; signal houdt Set met abonnees, geeft functie lees terug
- lees: als er een effect actief is → toevoegen als abonnee; lees.set: waarde aanpassen + alle abonnees opnieuw uitvoeren
- effect: zet fn als actief, voert één keer uit, actief weer null
- Gebruik: effect draait → leest count() → automatisch geregistreerd, niemand zei het expliciet; count.set(5) → één effect, één tekstnode
- Vs VDOM: geen hele componentfunctie, geen boom, geen diff
- Echte implementaties (Angular, Solid, Preact) voegen toe: gecachete computed, batching, oude abonnementen opruimen, dubbele uitvoeringen vermijden

## kb-compiler | 24. Framework-compilers

- Derde strategie: framework-compiler analyseert componenten tijdens build en genereert geoptimaliseerde JS
- Werk dat anders in browser gebeurt, nu vooraf: op machine van developer of in CI-pipeline
- Links Svelte: count met $state + knop; rechts compiler-output: gewone event listener + effect op precies één tekstnode
- Geen virtual DOM, geen diffing: compiler wist bij build welke node van welke variabele afhangt; intern signals → compilers en signals vaak samen
- Andere: Angular compileert templates naar instructies; React Compiler voegt automatisch memoization toe (geen useMemo meer); Vue Vapor Mode → directe DOM-operaties
- Voordelen: kleinere, snellere browsercode, eenvoudigere code schrijven; nadelen: altijd build-stap, onzichtbaar → debuggen van code die je niet zelf schreef
- → Drie strategieën (VDOM, signals, compilers): volgende slide welk framework welke combinatie

## convergentie | 25. Vergelijking van de frameworks

- Framework convergence: frameworks nemen goede ideeën van elkaar over en groeien naar elkaar toe
- Reactiviteit: Angular, Vue (refs), Svelte (runes), Solid allemaal signals; React uitzondering, blijft VDOM met re-render van component
- Compiler: iedereen; React stabiel sinds oktober 2025, Vue werkt aan Vapor, Svelte en Solid altijd al compiler-gebaseerd
- Server: meestal via meta-framework (Next.js, Nuxt, SvelteKit, SolidStart); Angular heeft SSR ingebouwd
- Kiezen op features wordt moeilijk; echte verschillen: standaardinstellingen, ecosysteem, developers op arbeidsmarkt, financiering
- Detail: voorstel signals in JS-taal zelf bij TC39 (beheert JS-standaard), pas stage 1 van 4; frameworks wachten niet

## div-1 | 26. Signals en compilers

- Lange discussie: virtual DOM, incremental DOM, signals of compilers; in 2026 zo goed als beslecht
- Elk groot framework combineert fijnmazige reactiviteit (meestal signals) met compiler die optimaliseert
- → Hoe Angular, React, Vue en Svelte daarnaartoe groeiden; eerst Angular, daarvoor eerst: wat is change detection

## kb-change-detection | 27. Change detection in Angular

- Change detection = hoe Angular bepaalt welke delen van het scherm opnieuw getekend moeten worden na een datawijziging
- zone.js: monkey patching van setTimeout, addEventListener, XMLHttpRequest → Angular weet dát er iets veranderde, niet wát
- Gevolg: hele componentenboom controleren, oude vs nieuwe waarde per binding → traag in grote apps, onleesbare stack traces
- OnPush: enkel controleren bij gewijzigde inputs, event in het component of gewijzigde signal → grote delen van de boom overslaan
- Zoneless: signals weten wie ervan afhangt → vertellen precies welke views bijgewerkt moeten worden
- → Volgende: zoneless en OnPush in detail, met wat vroeger de standaard was en wat nu

## kb-zoneless-onpush | 28. Zoneless en OnPush: vroeger en nu

- Twee vragen die vaak verward worden: zoneless = WANNEER Angular kijkt, OnPush = WELKE componenten
- zone.js: na elke klik, timer of HTTP-antwoord, ook als er niets veranderde
- Zoneless: enkel na een melding: signal in template verandert, template-event, markForCheck() (async pipe), nieuwe input
- Eager (vroeger Default): elk component elke ronde; OnPush: enkel als dirty, anders hele deelboom overgeslagen
- Dirty = nieuwe input-referentie (===, niet de inhoud), event in component of kinderen, gelezen signal, markForCheck()
- Tijdlijn: t/m 17 zone.js + Default (OnPush opt-in sinds Angular 2); 18 (mei 2024) zoneless experiment; 20.2 (aug 2025) stabiel
- 21 (nov 2025): zoneless standaard, geen zone.js in nieuwe projecten; 22 (juni 2026): OnPush standaard, Default heet Eager, ng update zet Eager op bestaande componenten
- Valkuil OnPush: push() op bestaande array = zelfde referentie → scherm blijft staan; nieuwe array of signal
- Valkuil zoneless: setTimeout met teller++ op gewoon veld → niemand meldt het (zone.js deed dat vroeger); signal meldt het zelf
- Examen: verschil zoneless en OnPush? Zoneless bepaalt wanneer, OnPush welke componenten
- → Volgende: wat er verder nog veranderde in Angular 21 en 22

## angular | 29. Angular 21 en 22

- Angular = duidelijkste voorbeeld van trend 1
- Eerste twee bullets = korte terugblik: zoneless standaard sinds 21, OnPush sinds 22 (net gezien)
- Signal Forms: model, waarden en validatie zijn signals; code: required + debounce = pas valideren bij verlaten van het veld
- resource(): async data (bv. HTTP) als signal met waarde, isLoading en error
- @Service(): kortere schrijfwijze; service = klasse met gedeelde logica via dependency injection, hier inject(HttpClient)
- Conclusie: van verborgen magie (zone.js) naar een van de meest expliciete frameworks, ook goed voor AI-agents (trend 4)

## kb-rerender | 30. Waarom rendert een component opnieuw?

- Eerst begrijpen wanneer React herrendert, om te zien wat de React Compiler oplost
- 3 redenen: eigen state (setCount), parent rendert (ook bij gelijke props!), gebruikte context verandert
- Code: klik → setCount → App rendert → TodoList rendert ook, terwijl todos dezelfde array is → 500 TodoItems mee
- Na reconciliation nul DOM-aanpassingen, maar 501 componentfuncties uitgevoerd en vergeleken, voor niets
- Re-render cascade: update bovenaan stroomt door naar alles eronder; traag bij zware componenten, lange lijsten, typen in invoerveld
- Verschil met signals: daar enkel de tekstnode van de knop aangepast
- → Volgende: React.memo, useMemo en useCallback om onnodige renders over te slaan

## kb-memo | 31. React.memo en referentiële gelijkheid

- Links: component in memo wikkelen → bij parent-render eerst props één voor één vergelijken
- Shallow comparison met Object.is (≈ ===), kijkt niet in objecten; alles gelijk → render van component én kinderen overgeslagen
- Voorbeeld: TodoList in memo + zelfde todos-array → TodoList en 500 items renderen niet mee bij teller
- Vergelijking kost zelf ook iets bij elke parent-render → memo overal is niet gratis
- Rechts: primitieven op waarde vergeleken, objecten/arrays/functies op referentie (geheugenadres): {} !== {}
- Inline arrow onAdd in JSX = elke render nieuwe functie → memo ziet andere props → rendert toch; idem style={{ color: 'red' }}
- → Volgende: useMemo en useCallback om referenties stabiel te houden

## kb-usememo-usecallback | 32. useMemo en useCallback

- useMemo: berekening + dependency array; bij gelijke todos en tab → bewaard resultaat, zelfde referentie
- Twee doelen: dure berekeningen niet herhalen en objecten/arrays stabiele referentie geven voor memo-kinderen
- useCallback: zelfde voor functies, zelfde onAdd zolang tekst gelijk blijft; eigenlijk useMemo(() => fn, deps)
- memo + useMemo + useCallback = klassiek performance-gereedschap in React
- Nadeel 1: dependency vergeten → stale closure, functie onthoudt oude waarde van tekst → subtiele bugs
- Nadeel 2: alles memoïzeren voor de zekerheid (geheugen, minder leesbaar) of net vergeten waar nodig
- Nadeel 3: Rules of Hooks, niet in if of na early return → niet overal memoïzeren
- → Volgende: de React Compiler lost precies deze drie problemen op

## react-compiler | 33. React Compiler 1.0 (oktober 2025)

- React Compiler 1.0: 7 oktober 2025
- Build-tool (Babel-plugin, nu ook Turbopack): analyseert elk component en custom hook, voegt automatisch memoization toe
- Vervangt: React.memo (memoïzeert teruggegeven JSX), useMemo (visible), useCallback (stabiele onAdd)
- Kan meer: genereert code i.p.v. hooks → ook na early return of in if; fijnmaziger (docs-voorbeeld: vergeten inline arrow ondanks useCallback)
- Vervangt niet: useState, useEffect, useRef, useContext; useMemo/useCallback blijven als escape hatch (bv. wanneer effect herdraait)
- Meta Quest Store: laden en navigaties tot 12% sneller, sommige interacties >2,5× sneller
- Werkt met React 17+, ingebouwd in Next.js, Vite-templates en Expo

## kb-compiler-output | 34. Wat genereert de React Compiler?

- Rechts: vereenvoudigde output van het component links
- $ = _c(5): uit react/compiler-runtime, cache-array met 5 vakjes per instantie, bewaard tussen renders (intern useMemoCache)
- zichtbaar: if todos !== $[0] of tab !== $[1] → herberekenen, inputs in 0 en 1, resultaat in 2; anders uit $[2]
- = wat useMemo met [todos, tab] doet, maar de compiler kan geen dependency vergeten
- JSX: nieuw List-element enkel als zichtbaar verandert, anders uit $[4] → zelfde object = React slaat deelboom over (vervangt memo)
- Gewone if-statements, geen hooks → ook na early return of in conditie
- Vergelijking: compiler doet wat signals doen, maar tijdens de build; React houdt volledige re-renders, maar die worden goedkoop

## kb-rules-of-react | 35. De Rules of React

- Compiler memoïzeert enkel veilig als je de Rules of React volgt; die gelden altijd, nu echt belangrijk
- Puur: zelfde props/state → zelfde JSX; geen side effects tijdens render (die horen in event handlers of useEffect)
- Waarom: bij cache-hit draait je componentcode niet → side effect zou plots niet meer gebeuren
- Immutability: todos.push + setTodos(todos) = zelfde referentie → === zegt 'niets veranderd' → item verschijnt niet; wel [...todos, t]
- Rules of Hooks: enkel bovenaan; React herkent hooks aan hun volgorde, die raakt in de war bij if/lus/early return
- Regel gebroken → bail-out: component werkt, maar zonder optimalisatie
- Sinds 1.0 checks in eslint-plugin-react-hooks; uitschakelen per component met 'use no memo'

## vue-svelte | 36. Vue Vapor Mode en Svelte 5

- Ook Vue en Svelte laten de virtual DOM achter zich
- Vue: tot nu virtual DOM met refs; refs zijn in feite signals
- Vapor Mode: template rechtstreeks naar DOM-operaties gekoppeld aan refs → minder geheugen, kleinere bundles, snellere updates
- Per component aan te zetten met één woord in de script-tag → geleidelijk migreren; Vue 3.6 eind sept 2026 nog release candidate
- Svelte altijd al compiler-framework; Svelte 5 runes: $state en $derived = signals met syntax die de compiler herkent
- SvelteKit 3 (RC sinds augustus 2026): remote functions = server-functie aanroepen als lokale functie, SvelteKit doet HTTP, types kloppen
- Principe = RPC (remote procedure call); React heeft hetzelfde met Server Actions, komt terug bij trend 3

## div-2 | 37. Terug naar de server

- Slinger: vroeger alles op de server (PHP), rond 2015 naar client (SPA's: React, Angular, Vue), laatste jaren terug (SSR, Server Components, Next.js)
- Nieuw dit jaar: server-first frameworks erkennen dat server-apps trager kunnen aanvoelen → beste van beide combineren
- Tegelijk tegenbeweging van frameworks die bewust minder op de server inzetten
- → Volgende: twee kernbegrippen, navigatie en caching

## kb-navigatie | 38. Wat gebeurt er bij een klik op een link?

- MPA: volledig nieuwe HTML van de server, scherm even leeg, JS-state weg (bv. half ingevuld formulier); oorspronkelijk web
- SPA: JS-router onderschept klik, URL via History API zonder herladen, meteen nieuwe view (evt. laadindicator), data erna → voelt onmiddellijk
- Server-gedreven (RSC): request → server rendert → browser voegt in zonder herladen; efficiënt, maar bij trage server/verbinding even niets
- Prefetching: code/data ophalen vóór de klik (link in beeld of hover) → alles ligt klaar
- Nadeel prefetching: misschien nooit bekeken → extra netwerkverkeer en serverbelasting
- → Spanningsveld snel aanvoelen vs niet te veel werk komt terug bij Next.js

## kb-caching | 39. Caching

- Caching = resultaat bewaren om het niet opnieuw te berekenen/ophalen; zoals een telefoonnummer onthouden
- Browser (afbeeldingen, CSS, JS lokaal), CDN (kopieën wereldwijd), server (trage query of gerenderde pagina)
- Cache-Control: public = ook gedeelde caches zoals CDN mogen bewaren; max-age 3600 = een uur geldig
- Afweging: sneller en goedkoper vs stale data; bv. productpagina een uur gecachet → klant ziet een uur de oude prijs
- Invalidatie: op tijd (TTL) of op gebeurtenis (product aangepast → cache van die pagina weg); notoir moeilijk
- Quote Phil Karlton: twee moeilijke dingen, cache-invalidatie en dingen een naam geven

## next16 | 40. Next.js 16: Cache Components

- Probleem: vanaf Next.js 13 veel automatische, impliciete caching (requests gecachet, pagina's statisch) → oude data, grote ergernis
- Nieuw principe: alles dynamisch (per request), tenzij je expliciet cachet
- 'use cache' = directive (string bovenaan functie/bestand, zoals 'use client'); cacheLife('hours') = hoe lang; ≈ Cache-Control per component
- Code: getCurrentUser = persoonlijk, elk request; Projects gecachet; Suspense = streaming: welkom meteen, laadindicator tot Projects klaar
- Eén pagina combineert data per request, gecachete data en streaming
- 16.4 (oktober 2026): standaard aan in nieuwe projecten; Next.js 17: standaard voor iedereen
- Verder in 16: Turbopack standaard bundler, middleware.ts heet nu proxy.ts

## instant-nav | 41. Next.js 16.3: Instant Navigations

- Veelzeggend: Next.js-team erkent zelf de 'terechte!' kritiek dat Server Components apps traag laten aanvoelen (uitroepteken staat er echt)
- Probleem: server-app klik → even niets; SPA toont meteen skelet → voelt sneller, ook al duurt het even lang
- 16.3 Instant Navigations: route wacht op data → foutmelding tijdens ontwikkelen dwingt keuze
- Stream (Suspense, meteen laadstatus), Cache ('use cache', eerder gerenderde versie), Block (bewust wachten, bv. blogpost zonder laadscherm)
- Vroeger: prefetch-request per zichtbare link (20 chats in zijbalk = 20 requests, 'belachelijk' volgens het team zelf)
- Partial Prefetching: één herbruikbare shell (layout, laadindicatoren) per route, zoals SPA code per route één keer laadt
- Les: slinger zwaait niet gewoon terug; beste van beide, maar prijs = complexiteit, per stukje UI een bewuste keuze

## react-193 | 42. React 19.2 en 19.3

- Ook React beweegt richting app-gevoel; geen React 20, wel twee kleinere versies
- ViewTransition (stabiel 19.3, sept 2026): laagje op browser View Transition API; momentopname oud/nieuw, verschil geanimeerd zoals native apps
- Activity (19.2): UI verbergen zonder te verwijderen; bv. tabs, half ingevuld formulier staat er nog na terugschakelen
- use(browser()): component enkel in browser renderen (tijdzone, schermgrootte); server toont laadstatus; vervangt typeof window-trucs
- Fragment refs: focus of observer op groep elementen zonder extra div
- Boodschap: server-gerenderde app kan aanvoelen als native app

## kb-islands-pe | 43. Islands en progressive enhancement

- Twee begrippen nodig om de tegenbeweging te begrijpen
- Islands: nieuwssite, artikel/navigatie statisch, enkel carrousel en reactieveld interactief; klassieke SSR hydrateert toch alles
- Bij islands: statische HTML zonder JS, enkel eilandjes krijgen JS en worden apart gehydrateerd
- Astro: Artikel 0 KB JS; client:visible = pas laden en hydrateren als het in beeld komt
- Progressive enhancement: eerst werkend met enkel HTML; form met method post + action werkt ook als JS niet laadt, geblokkeerd is of faalt
- JS erbovenop: validatie tijdens typen, verzenden zonder herladen; Remix en SvelteKit gebouwd rond dit principe
- Klassieke SPA: zonder JS werkt niets; beide principes → minder JS, sneller, robuuster op trage toestellen/netwerken

## tegenbeweging | 44. Niet iedereen wil Server Components

- Duidelijke tegenbeweging tegen de server-first aanpak van Next.js
- Remix 3 (stabiel begin oktober 2026): was React-meta-framework (OpenAI gebruikte het voor ChatGPT), later samengevoegd met React Router 7
- Remix 3 laat React los: eigen runtime uit fork van Preact, nog JSX maar state = gewone variabele; Request/Response + HTML-formulieren
- Eén package, weinig dependencies → ook security-argument
- TanStack Start 1.0 (13 oktober 2026, makers TanStack Query/Router): client-first, SSR als extra, RSC optioneel
- Volledig type-safe: route hernoemen → TypeScript-fout op elke link; blogpost 'We stopped using RSC on tanstack.com': kleinere bundle, complexiteit woog niet op
- Astro (islands): favoriet voor content-sites, hoogste tevredenheid van alle meta-frameworks
- Boodschap: Server Components krachtig, maar geen universele standaard

## wanneer-wat | 45. Welke aanpak voor welke app?

- Tabel = beslissingshulp die alle rendering-begrippen samenbrengt; vereenvoudiging maar goed vertrekpunt
- Examen: vraag van het type 'welke rendering-strategie kies je voor deze applicatie en waarom?'
- Content (blog, docs, portfolio): verandert zelden, moet vindbaar zijn → SSG + evt. islands, Astro ideaal
- Webshop/marketing: snel + SEO, maar persoonlijke delen (winkelmandje, aanbevelingen) → statische shell + streaming, Cache Components
- Dashboard/admin/chat: achter login, SEO irrelevant, interactiviteit alles → SPA vaak eenvoudiger, goedkoper, sneller
- Formulier-zware apps (overheidsformulier, inschrijvingen): SSR + progressive enhancement, werkt ook op trage toestellen of als JS faalt
- Vuistregel: SSR geen doel op zich → meer serverkosten en meer aanvalsoppervlak
- → Volgende: trend 3, security

## div-3 | 46. Security

- Server Components/Actions handig: functie op server aanroepen zonder zelf API te bouwen
- Maar erachter zit een netwerkprotocol: data van browser naar server, daar omgezet naar JS-objecten
- Elke plek waar een server input van buitenaf verwerkt = potentieel doelwit
- December 2025: een van de zwaarste kwetsbaarheden ooit in React
- → Volgende: eerst een aantal security-begrippen

## kb-security | 47. Security-begrippen

- Aanvalsoppervlak (attack surface): alle inputplaatsen (endpoints, formulieren, uploads, headers); meer publieke servercode = groter
- Kwetsbaarheid = misbruikbare fout; exploit = concrete code/request die ze misbruikt
- CVE: uniek nummer per publiek lek, met jaartal + volgnummer
- CVSS: score 0–10 op basis van misbruikgemak (moet je ingelogd zijn?) en impact; vanaf 9 kritiek
- RCE: aanvaller voert eigen code uit op jouw server → data stelen, database leegmaken, malware; het ergste
- DoS: server zo belasten dat hij niet meer antwoordt voor gewone gebruikers
- Patch beschermt pas als je hem installeert; zero-day = al misbruikt voor er een patch is

## kb-server-action | 48. Een Server Action is een publiek endpoint

- Kerninzicht: Server Action (of SvelteKit remote function) = publiek HTTP-endpoint, ook al lijkt het een gewone functie
- 'use server' → framework geeft functie een ID; deletePost(5) = HTTP POST met ID + geserialiseerde argumenten; server deserialiseert en voert uit
- Iedereen kan dat request zelf sturen (curl, script); knop enkel tonen aan admins zonder check → elke bezoeker kan posts verwijderen
- Drie controles: authenticatie (wie ben je?), autorisatie (mag je dit?), validatie (hier zod: geldige UUID)
- Vertrouw nooit client-input, ook niet van je eigen frontend
- Extra risico: deserialisatie gebeurt in het framework vóór jouw code → fout daar = jouw controles helpen niet (React2Shell)
- → Volgende: eerst serialisatie begrijpen

## kb-serialisatie | 49. Serialisatie en deserialisatie

- Serialiseren = object uit geheugen → tekst/bytes om te versturen of op te slaan; deserialiseren = omgekeerd; ook buiten webdev
- JSON.stringify / JSON.parse; JSON bewust beperkt (getallen, strings, booleans, null, arrays, objecten) → relatief veilig, hooguit onverwachte data
- Rijkere formaten: verwijzingen, promises, welke module/klasse → krachtig maar gevaarlijk met aanvallersinput
- Slimme input → parser maakt objecten of roept functies aan die nooit bedoeld waren → in het slechtste geval RCE
- Onveilige deserialisatie staat al jaren in OWASP-lijst; bekende voorbeelden: Java-serialisatie, pickle in Python
- Flight-protocol: React-formaat voor RSC-payload (server → browser) en Server Action-argumenten (browser → server); promises, verwijzingen, streaming
- → Volgende: precies wat er in december 2025 misliep

## react2shell | 50. React2Shell (CVE-2025-55182), december 2025

- 3 december 2025: CVE-2025-55182 in React Server Components, al snel React2Shell genoemd; CVSS 10, het maximum
- Fout in deserialisatie van Flight: één geconstrueerd HTTP-request → RCE, zonder login of gebruikersactie
- Geen eigen Server Action nodig: kwetsbare React-versie met RSC volstond; eigen auth/validatie hielp niet, lek zat vóór jouw code
- Tijdlijn: lek + patch tegelijk; <24 u: Wiz ziet ≥15 aanvalsgroepen (cryptominers, botnets); 5 dec: CISA-lijst actief misbruikt
- Week later: nog twee lekken bij patch-analyse (DoS en lekken van broncode); half december ~helft van publieke kwetsbare servers ongepatcht (Wiz)
- Getroffen: niet enkel Next.js, elk framework met RSC
- Les: RSC niet slecht, maar nieuw protocol op de server heeft tijd nodig om veilig te worden; patch helpt enkel wie installeert

## security-2026 | 51. AI vindt lekken sneller dan ooit

- React2Shell geen eenmalig incident; in 2026 Next.js-security-updates in hoog tempo
- Juli 2026: formeel security-releaseprogramma, ~maandelijks vooraf aangekondigd (zoals Node.js); dringende/misbruikte lekken nog meteen
- Reden volgens het team: aantal gevonden lekken stijgt door LLM-ondersteund onderzoek
- Mozilla: 271 problemen in één Firefox-release, allemaal met AI gevonden; AI werkt in twee richtingen, verdedigers én aanvallers
- Update 14 oktober 2026: RCE in 'use cache'-functies; RCE via kwaadaardige SVG in beeldoptimalisatie (sharp); DoS via Server Actions (CPU volledig bezet)
- Framework kiezen = ook update-ritme kiezen, tijd voorzien; meer op de server = groter aanvalsoppervlak

## kb-supply-chain | 52. Dependencies en de supply chain

- Tweede aanvalsoppervlak: niet je eigen code, maar je dependencies
- Transitieve dependency = dependency van een dependency; nieuw Next.js-project = honderden packages van honderden mensen, je vertrouwt ze allemaal
- Supply chain attack: klein package aanvallen dat duizenden projecten gebruiken i.p.v. jouw beveiligde app
- Semver: major mag breken, minor = features, patch = bugfix; ^ laat elke nieuwere 1.x toe → kwaadaardige 1.4.3 krijg je automatisch
- Lockfile (package-lock.json) legt exacte versie van elk package vast, ook transitieve; npm ci installeert exact dat
- Install-scripts (postinstall) draaien automatisch bij installatie → ideaal voor aanvallers
- Typosquatting: naam bijna gelijk aan bekend package; slopsquatting: aanvallers registreren door AI verzonnen package-namen

## supply-chain | 53. Shai-Hulud: een worm in npm

- Shai-Hulud, naar de zandwormen uit Dune; twee golven: september en eind november 2025
- Phishingmails vermomd als npm-beveiligingswaarschuwing → logins van maintainers van populaire packages gestolen
- Nieuwe versies met malware in postinstall → bij installeren/updaten tokens en secrets (API-sleutels, cloud-credentials) naar aanvallers
- Gevonden npm-token → publiceert zichzelf in packages van het slachtoffer = echte worm; >500 packages getroffen
- npm: besmette packages verwijderd, oude tokens ingetrokken, trusted publishing (publiceren vanuit CI zonder langlevend token)
- Zelf: lockfile committen + npm ci in pipelines, install-scripts beperken, minder dependencies (verkoopargument Remix 3)
- Nieuw in 2026: nakijken wat je AI-agent installeert, soms verzonnen package-namen

## div-4 | 54. AI-agents als gebruiker

- Belangrijkste trend van dit jaar
- Vroeger: gebruiker = developer die docs leest, tutorials volgt, fouten interpreteert
- 2026: veel code geschreven door AI-agent in de codebase, niet door developer zelf
- Next.js-team: 'hoe zou Next.js eruitzien als het ontworpen werd voor agents?'
- Frameworks behandelen agents als volwaardige gebruikers met eigen noden
- → Eerst: wat is een taalmodel en een agent, wat kunnen ze wel en niet

## kb-llm-agent | 55. Van taalmodel naar coding agent

- LLM = neuraal netwerk op tekst en code; voorspelt telkens volgende token (± woorddeel)
- Training cutoff: kent enkel trainingsdata tot een datum → nieuwere frameworkversies onbekend
- Context window: alles wat model op één moment ziet (vraag, bestanden, vorige berichten)
- Chatbot (ChatGPT in browser): ziet enkel wat jij plakt; jij kopieert, test, komt terug met fout
- Coding agent: LLM in lus met tools (bestand lezen/aanpassen, npm test, web zoeken)
- Lus overlopen: doel → plan → tool → resultaat lezen → herhalen tot klaar of vast
- Kerninzicht: agent is zo goed als de info die hij kan zien (training, context, tools)

## ai-cijfers | 56. Stack Overflow Developer Survey 2026

- Survey begin oktober 2026; 73% van AI-gebruikers dagelijks, 31% daarvan >4 uur/dag → normale manier van werken
- Agents (66%) nu meer gebruikt dan chatbots (63%); Claude Code en GitHub Copilot bovenaan
- Verschil: chatbot geeft snippet; agent leest codebase, past aan, draait build en tests, itereert
- Voorzichtig: slechts 20% voor deployen/productie-troubleshooting; 93% wil bronvermelding
- Klopt met State of JS: Claude en Cursor verdubbeld, ChatGPT gedaald
- Codekwaliteit hangt af van hoe goed de agent het framework kent
- → Volgende: het fundamentele probleem daarmee

## training-lag | 57. Een model kent het framework van gisteren

- Training cutoff vs. frameworks die elk kwartaal veranderen; model zag vooral oude tutorials en Stack Overflow
- Next.js: getServerSideProps (Pages Router) al jaren vervangen door App Router + Server Components, toch nog gegenereerd
- middleware.ts in Next.js 16 hernoemd naar proxy.ts
- Angular: modellen geven NgModules + constructor injection i.p.v. standalone, inject(), signals
- Oplossing Next.js: sinds 16.2 volledige docs in npm-package (node_modules) → altijd juiste versie
- Sinds 16.3 schrijft next dev blok in AGENTS.md als agent actief is: 'This is NOT the Next.js you know'
- Verschuiving: docs ook voor agents, versie-specifiek, lokaal in project
- → Volgende: wat AGENTS.md precies is

## kb-agents-md | 58. AGENTS.md en llms.txt

- AGENTS.md: markdown in project-root met stack, commando's (start, test, lint), teamafspraken
- Meeste agents lezen het automatisch bij start; 'README voor nieuwe collega die alles letterlijk neemt'
- Voorbeeld rechts: Stack (App Router → geen Pages Router-code), Commando's (agent kan zelf testen), Conventies (zod, tests draaien)
- Kort en concreet werkt beter dan lang; soms eigen naam, bv. CLAUDE.md voor Claude Code
- llms.txt: vast pad op website, docs-overzicht in platte markdown, zonder menu's/reclame/JS → efficiënt voor LLM
- Next.js: llms.txt + .md achter elke docs-URL voor markdownversie
- Verschil: AGENTS.md = instructies in jouw project; llms.txt = documentatie op website

## kb-mcp | 59. Model Context Protocol (MCP)

- Open standaard van Anthropic (nov. 2024), nu door bijna alle AI-tools ondersteund
- Probleem: vroeger elke AI-tool eigen koppeling per systeem (GitHub, database, Slack); nu één MCP-server per systeem → 'USB-C'
- Architectuur: host met MCP-client (Claude Code, Cursor, VS Code) → MCP-server → systeem (Next.js dev server, database, GitHub)
- Server biedt tools (functies, bv. get_errors), resources (data, bv. databaseschema), prompts (sjablonen)
- Communicatie via JSON-RPC: functies aanroepen met JSON-berichten (voorbeeld rechtsonder)
- Relevantie: agent ziet browser niet ('fix the error' → welke fout?)
- Via next-devtools-mcp of Angular CLI MCP-server: fouten, routes, build-status van draaiende app opvragen

## kb-skills | 60. Skills

- Derde mechanisme naast AGENTS.md en MCP
- Skill = map met SKILL.md: naam, beschrijving wanneer nuttig, stappenplan, evt. scripts/docs → 'receptenkaart'
- Verschil met AGENTS.md: niet altijd geladen; agent ziet eerst enkel naam + beschrijving, leest volledig als taak past
- Reden: context window beperkt; alles meegeven = geen ruimte voor code en model raakt in de war
- Voorbeeld: verify-in-browser; Next.js 16.3 officiële skills (next-dev-loop, migratie naar Cache Components)
- Angular 22: officiële skills met één commando: angular-new-app en angular-developer
- Sterk voor meerstapsworkflows: migraties, vaste manier van testen

## toolbox | 61. Welk mechanisme waarvoor?

- Next.js-team: noden van agent = kennis, zichtbaarheid, verificatie
- Kennis: AGENTS.md (altijd bij start, projectregels + verwijzing naar docs); llms.txt (bij opzoeken)
- Workflow: skills, enkel geladen als taak past
- Zichtbaarheid: MCP; tool-aanroep voor browserfouten, routes, compileert route?
- Verificatie: agent-browser; agent bestuurt echte browser, leest console, netwerk, React-tree → controleren i.p.v. hopen
- Next.js bouwde eigen chat-agent Vector, geschrapt: devs gebruikten al Cursor/Claude Code → maak framework zichtbaar voor bestaande agents
- Next.js en Angular maakten MCP-server kleiner in 2026: kennis via docs/skills, MCP voor live info

## actionable-errors | 62. Foutmeldingen geschreven voor agents

- Links: Next.js 16.3-terminaloutput bij ongecachete data zonder Suspense: beschrijving, 3 gelabelde oplossingen (stream/cache/block), docs-link
- Waarom terminal? Agent leest terminal, niet browser; ook next build en CI-logs zelfde structuur
- Browser-overlay: 'Copy prompt' → prompt voor agent: lees docs, pas canoniek patroon toe, verifieer in echte browser
- Foutpagina's bewust voor agents: patronen, trade-offs, valkuilen die agent bij eerste poging mist
- Next.js 16.4 (begin okt. 2026): next upgrade --agent = migratiegidsen, codemods, verificatie; herinnering bij security-upgrade
- Agent feedback: agent stelt bugrapporten op over onduidelijke docs/fouten; niets verstuurd zonder jouw review
- Ook beter voor mensen: duidelijke fouten met concrete oplossingen

## angular-ai | 63. Angular 22 en AI-agents

- Niet enkel Next.js: Angular volgt exact dezelfde strategie
- Skills (Angular 22): angular-new-app (projecten opzetten) en angular-developer (code, architectuur) = 'dé bron van Angular-kennis'
- Gevolg: agent genereert signal-gebaseerde, zoneless code i.p.v. NgModules en constructor injection
- CLI MCP-server sinds 20.1; in v22 tools verwijderd (voorbeelden zoeken, moderniseren) omdat skills dat beter doen
- Zelfde beweging als Next.js: kennis via docs/skills, live info via MCP
- In dev: signal-graph en DI-graph als tools in Chrome DevTools; via Chrome DevTools MCP kan agent die opvragen i.p.v. gokken
- → Angular 22 heeft ook experimentele WebMCP, komt bij trend vijf

## kb-prompt-injection | 64. Prompt injection

- Belangrijkste securityrisico van zelfstandige AI-agents
- Aanvaller verstopt instructies in data (issue, webpagina, e-mail, README); model voert uit alsof van gebruiker
- Voorbeeld: instructie in HTML-commentaar in issue, onzichtbaar op GitHub; agent met schrijfrechten kan die uitvoeren
- Vergelijk SQL-injectie: daar scheiden prepared statements data en commando's; bij LLM kan dat niet, alles is tekst in één context
- Dus schade beperken: least privilege (bv. read-only), sandbox zonder echte systemen of geheimen
- Human in the loop voor mergen, deployen, verwijderen; dubbele controle door tweede onafhankelijke agent
- → Volgende: hoe het Next.js-team die principes toepaste

## maintainer-agent | 65. Case: agents in de Next.js-repository

- Agents helpen frameworks ook onderhouden; toont verdedigingsprincipes in de praktijk
- Gemiddeld 36 nieuwe issues/week; 10 aug. 2026: 2.244 open; auto-close na 18 maanden inactiviteit sloot soms echte bugs
- Onderzoeksagent: per issue verse sandbox (Next.js-code, Node.js, browser); leest discussie, zoekt PR's en commits
- Reproduceert op gemelde en nieuwste versies, zoekt actief bewijs tegen eigen conclusie; ±30 min, tot 200 sessies tegelijk
- Veiligheid: read-only (niet sluiten/pushen/commenten), negeert instructies in issuetekst, maintainer leest elk advies
- Resultaat: 1.462 gesloten in ±3 weken, backlog onder 1.000; >1/3 was al opgelost
- Nu: agent sluit zelf duidelijkste gevallen, max 25/week, enkel als tweede agent hetzelfde besluit; code altijd via mens

## design-for-agents | 66. Wat maakt een framework agent-vriendelijk?

- Samenvatting trend: zes principes
- Expliciet boven magie: impliciete caching (oud Next.js) en zone.js vervangen door 'use cache' en signals
- Types overal: compiler als vangnet voor agentfouten; TanStack Start: type-safe routes en server-functies
- Sterke conventies (file-based routing): minder vrijheid → minder fouten, sneller project begrijpen
- Webstandaarden (Request, Response, FormData, fetch) veranderen niet, correct in trainingsdata; argument van Remix-team
- Fouten met oplossing in de terminal; snelle feedbacklus: agent bouwt tientallen keren per taak → Rust-tooling
- Developer experience en agent experience versterken elkaar

## div-5 | 67. Het AI-native web

- Vijfde en laatste trend: AI niet enkel hulpmiddel om code te schrijven
- AI kiest technologie, bouwt apps voor niet-programmeurs, chatbots tonen web-UI, agents bezoeken websites (nieuwe standaarden), AI in de browser

## default-stack | 68. Wie kiest het framework? Het model

- Wie kiest het framework? Steeds vaker het taalmodel
- Zonder context 'bouw een todo-app' → React (Next.js of Vite), Tailwind, shadcn/ui; bij v0, Lovable, Claude
- Benadrukken: observaties uit blogposts en praktijk, geen wetenschappelijke studie
- Tailwind: utility-klassen in HTML (p-4, text-center), styling naast markup; shadcn/ui: broncode gekopieerd in project, agent kan die lezen
- Vliegwiel: populair → trainingsdata → gegenereerd → online → nieuwe trainingsdata
- Voordeel React (verklaart dominantie ondanks lagere tevredenheid); drempel voor Vue, Svelte, Angular, nieuwe frameworks → investeren in AGENTS.md, skills, llms.txt
- Bijsturen: expliciete instructies, AGENTS.md met stack, voorbeeldcomponenten, lint-regels

## vibe-coding | 69. Vibe coding

- Term van Andrej Karpathy, begin 2025: beschrijven, laten genereren, accepteren zonder code te lezen, bijsturen op wat je ziet
- v0, Lovable, Bolt: niet-programmeurs krijgen webapp, typisch React + Tailwind + Supabase
- Lovable: ±10% van 1.645 apps volledig open database; Row-Level Security stond uit
- Supabase: browser praat rechtstreeks met database → zonder RLS kan iedereen met publieke sleutel alles lezen/aanpassen
- Veracode, >100 modellen: 45% van code bevatte OWASP Top 10-lek (injectie, ontbrekende toegangscontrole, zwakke authenticatie)
- Veel verschillende cijfers, zelfde richting; probleem: niemand kijkt na, gevaarlijkste fouten in configuratie
- Prima voor prototype; productie vraagt engineering: code review, tests, wie mag wat

## mcp-apps | 70. MCP Apps: je webapp draait in de chat

- Generative UI: AI antwoordt met interactieve interface (tabel, kaart, formulier, boekingsscherm)
- MCP Apps gelanceerd 26 jan. 2026: eerste officiële MCP-uitbreiding; samensmelting MCP-UI (community) + OpenAI Apps SDK
- Schema: vraag vluchten Lissabon → tool op MCP-server (bv. reisbureau) geeft data + UI-resource (HTML+JS) → host toont in sandboxed iframe
- Sandboxed iframe: geen toegang tot cookies, DOM, data van host; enkel postMessage → UI kan gesprekken niet lezen
- Clients zonder UI-ondersteuning krijgen altijd tekstversie
- Die UI is gewone webapp (React, Vue, web components) → je webapp krijgt nieuwe plek: de chat
- Frameworks voor AI-UI: Vercel AI SDK 6, TanStack AI 1.0 (23 okt. 2026)

## webmcp | 71. WebMCP: websites met een API voor agents

- Browser-agents (Gemini in Chrome, agent-modi) lezen pagina/screenshots en klikken als mens → traag, foutgevoelig, breekt bij redesign
- WebMCP: pagina biedt tools aan met naam, beschrijving, JSON-schema; agent roept functie aan ('zoek producten', 'voeg toe aan winkelmandje')
- Verschil met MCP: MCP = apart programma buiten browser; WebMCP in pagina, binnen sessie en login → zelfde rechten als gebruiker
- W3C Community Group, Google en Microsoft drijvend; Chrome preview feb. 2026, origin trial sinds Chrome 149
- Origin trial = sites registreren om experimentele feature bij echte gebruikers te testen; nog geen standaard, Safari/Firefox niet
- Rechts: Angular 22 experimenteel; naam, beschrijving, inputSchema, execute met gewone dependency injection
- Vergelijk SEO: binnenkort site ook optimaliseren voor agents

## builtin-ai | 72. Een taalmodel in de browser

- Chrome levert Gemini Nano mee, draait lokaal op toestel, niet in cloud; bruikbaar via JS-API's
- Prompt API (vrije opdrachten) stabiel in Chrome 148 volgens release-berichten; ook samenvatten, vertalen, taaldetectie; schrijven/herschrijven nog origin trial
- Code: feature detection = eerst checken of browser het ondersteunt; dan sessie + prompt (tags voor productreview)
- Else-tak essentieel: fallback naar server-API of feature weglaten → progressive enhancement
- Voordelen: data blijft op toestel (privacy, GDPR), geen kosten per aanroep, werkt offline
- Nadelen: enkel Chromium (Chrome, Edge), model enkele GB te downloaden (kritiek: zonder expliciete toestemming), minder slim dan cloud

## platform | 73. De browser neemt framework-taken over

- Stille trend: browser neemt taken over waarvoor je vroeger framework/library nodig had
- Interop: jaarlijks project Apple, Google, Microsoft, Mozilla, Igalia; features overal gelijk, gemeten met duizenden tests; 2026: 20 focusgebieden
- Baseline: label dat feature in alle grote browsers werkt
- View Transitions (React <ViewTransition> is laagje erboven); Navigation API vervangt History API, één centrale plek voor navigaties
- Temporal vervangt beruchte Date: Firefox, Chrome, Node 26, Safari nog niet; anchor positioning zonder JS-library; dialog/popover enkel HTML
- Scoped custom element registries: namen niet meer globaal → twee versies van zelfde component op één pagina
- Les: meer platform = minder framework; webstandaarden staan ook correct in trainingsdata

## studenten | 74. Wat betekent dit voor jullie?

- In één zin: de agent kent de API, jij moet het systeem kennen
- Fundamenten: agent zoekt syntax (Signal Forms, 'use cache') op, maar server vs. browser, traagheid, security beslissen = HTTP, DOM, rendering, hydration, reactiviteit, caching
- Lees de diff (overzicht van wijzigingen): AI-code als code van nieuwe collega; vaak goed, soms subtiel fout, jouw verantwoordelijkheid bij merge
- Ken de servergrens: na React2Shell geen detail; wat draait op server, wat gaat naar browser, wat is publiek bereikbaar
- Stuur je agent: AGENTS.md, actuele docs, tests = beste specificatie want agent kan ze zelf uitvoeren
- Blijf kritisch, volg het geld: niet wat model standaard kiest of hostingbedrijf promoot, wel wat je app nodig heeft

## kernbegrippen-1 | 75. Begrippenlijst (1/3): rendering en reactiviteit

- Studiehulp voor examen; in de les snel overlopen of overslaan
- Deze slide: begrippen rendering en reactiviteit
- Examen: geef per begrip definitie + voordeel + nadeel + framework-voorbeeld
- Voorbeeld hydration: voordeel server-pagina wordt interactief; nadeel werk dubbel; oplossingen islands (Astro), incremental hydration (Angular), Server Components (React)

## kernbegrippen-react | 76. Begrippenlijst (2/3): DOM, virtual DOM en React

- Alles over DOM, virtual DOM en React optimaliseren
- Examen: begrippen in logische volgorde aan elkaar koppelen
- Ketting: DOM duur door reflow/repaint → declaratief model met virtual DOM
- Renderfase: componenten uitvoeren, reconciliation (ander type = vervangen, keys voor lijsten); commitfase: enkel verschillen
- Nadeel re-render cascade → React.memo; faalt door referentiële gelijkheid bij nieuwe objecten/functies → useMemo/useCallback
- React Compiler doet dat automatisch, mits Rules of React gevolgd

## kernbegrippen-2 | 77. Begrippenlijst (3/3): server, security en AI

- Begrippen uit trend 2 tot 5: navigatie en caching, security, AI
- Examen: let op de verbanden tussen begrippen
- Server Action = publiek HTTP-endpoint, argumenten geserialiseerd → fout in deserialisatie → RCE (React2Shell, CVSS 10)
- Coding agent: AGENTS.md voor kennis, skills voor workflows, MCP voor live info
- Kwetsbaar voor prompt injection → least privilege, sandbox, mens die controleert
- Wie verbanden kan uitleggen, plaatst ook de trends van 2027 snel

## conclusie | 78. Conclusie

- 1. Signals en compilers gewonnen: Angular signal-first en zoneless, React stabiele compiler, Vue/Svelte laten virtual DOM achter
- 2. Server-slinger: Cache Components, streaming, Instant Navigations; tegenbeweging Remix 3, TanStack Start, Astro; kies per stukje UI: streamen, cachen, blokkeren
- 3. Security: Server Actions publiek, React2Shell = deserialisatiefout → RCE; AI versnelt lekken vinden aan beide kanten; supply chain; framework = update-ritme
- 4. Agent als gebruiker: AGENTS.md, MCP, skills, oplosbare foutmeldingen; bescherming tegen prompt injection; goed voor agents = goed voor mensen
- 5. AI-native web: modellen sturen stackkeuze, app builders met risico's, MCP Apps en WebMCP
- Boodschap: blijf kritisch, tegenover bedrijven achter frameworks én tegenover code van je AI-agent

## vragen | 79. Vragen?

- Vragen? Anders discussie: kies je framework op basis van wat je agent het best kent?
- Bv. React omdat modellen het kennen, ook als Svelte/Angular beter past? Geen juist antwoord, teams vragen het echt
- Extra vraag: mag een framework automatisch AGENTS.md in je project schrijven?
- Extra vraag: bijna elk groot framework eigendom van of gefinancierd door cloud-/AI-bedrijf, wat vind je daarvan?
- Extra vraag: als agent 1.500 issues triëert, wat betekent dat voor de rol van open source maintainer?
- Rechts: bronnen; alle cijfers komen daaruit, secundaire bronnen en praktijkobservaties vermeld
- Bedanken voor de aandacht
