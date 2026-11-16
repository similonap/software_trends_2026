# Labo: voorbeeldoplossing en modelantwoorden (docent)

> Deze map is **niet** voor studenten. De opgave staat in `labo/webframeworks/`.

**Formule:** 120 minuten, met verplicht gebruik van een coding agent naar keuze voor het mechanische werk. Studenten voorspellen, meten, testen, voeren de aanval uit en reflecteren zelf.

**Wat getest is:** alle code, experimenten en metingen hieronder zijn uitgevoerd op 9 november 2026:
- macOS, Node 24.18, Chrome (headless, via Puppeteer)
- React 19.3.1, Vite 8.3, React Compiler 1.0.0
- Angular 22.2
- Next.js 16.4.5

De voorbeeldoplossingen zijn wat de prompts voor de agent moeten opleveren.

**Wat niet getest is:** de **prompts zelf** zijn niet met een agent uitgevoerd. Het resultaat hangt af van de gekozen agent en het gekozen model. Hieronder staat per taak van de agent wat je mag verwachten en waar je op let. Probeer het labo één keer zelf met een agent en een model die je studenten kunnen gebruiken. Ook het nakijken en terugzetten met git (`git diff .`, `git add .`, `git restore --staged --worktree .`) is niet in een volledig labo doorlopen.

Absolute tijden hangen af van de machine. De verhoudingen zijn wat telt.

| Map | Inhoud |
|---|---|
| `deel1-react-compiler/` | eindoplossing: compiler aan, `Statistiek.jsx` verbeterd; `opdracht-1.2-handmatig/` = het verwachte resultaat van de taak van de agent in 1.2 |
| `deel2-angular-zoneless/` | eindoplossing met signals en `resource()` (= verwacht resultaat van 2.3); `bonus-signal-forms/boeken.ts` = de bonus |
| `deel3-nextjs/` | eindoplossing met Suspense, `'use cache'`, `updateTag`, autorisatie en validatie (= verwacht resultaat van 3.2, 3.3 en 3.4) |

Elk project bevat een `AGENTS.md` met de afspraken voor de agent (*Regels voor het labo Software Trends*). In deel 1 is dat het hele bestand. In deel 2 staan die regels onder de officiële Angular-`AGENTS.md` (gemaakt met `ng new --ai-config=open-ai-codex`), in deel 3 onder het blok van `create-next-app`. `next dev` herschrijft enkel de tekst tussen de markeringen `nextjs-agent-rules`; de labo-regels eronder blijven staan.

## Praktische aandachtspunten voor de docent

- **Voorbereiding:** laat studenten de voorbereiding thuis echt doen: een werkende agent met een model, de startcode in git, en `npm install` in de drie mappen. Een student zonder werkende agent verliest het halve labo.
- **Modelkeuze:** gratis modellen hebben limieten en kunnen trager zijn. Studenten kiezen hun agent zelf. Test vooraf met minstens één agent en model of de prompts betrouwbaar werken, en raad die combinatie aan aan wie nog geen agent heeft.
- **Een map per deel:** studenten moeten elke deel-map **apart** openen als projectmap. Anders leest de agent `AGENTS.md` niet. Niet elke agent leest `AGENTS.md` vanzelf: de testprompt uit de voorbereiding (*"Welke regels uit AGENTS.md volg je daarbij?"*) toont dat. Wie een agent heeft die het bestand niet leest, begint elke sessie met *"Lees eerst AGENTS.md en volg de regels daarin."*
- **Dev servers:** `AGENTS.md` verbiedt de agent om dev servers te starten. Doet een model het toch, dan blijft de taak hangen op een proces dat nooit stopt. Laat de student dan annuleren en zelf de server starten.
- **Next.js:** de cache overleeft een herstart. Wie wil herbeginnen, verwijdert `data/` en `.next/`.

---

## Deel 1: React Compiler

### Metingen

Development mode met StrictMode. Waarden van de tweede klik; de eerste klik is telkens trager door opwarming.

| Actie | 1.1 Start | Enkel `memo` | 1.2 Handmatig | 1.2 Zonder `useCallback` | 1.3 Compiler | Bonus `'use no memo'` |
|---|---|---|---|---|---|---|
| Koffie gedronken | 50 ms | 51 ms | overgeslagen (0 ms) | 23 ms | geen render (geen regel) | geen render |
| Filter *open* | 105 ms | 115 ms | 78 ms | 118 ms | 43 ms | 98 ms |
| Taak aanvinken | 47 ms | 48 ms | 66 ms | 49 ms | 41 ms | 93 ms |

Gecompileerde componenten: `App` `_c(22)`, `TakenLijst` `_c(13)`, `TaakItem` `_c(10)`, `Statistiek` pas na de volledige oplossing (`_c(8)`).

### Taken van de agent: verwacht resultaat en aandachtspunten

**1.2 (Uitvoeren)**
- **Verwacht resultaat:** zoals in `opdracht-1.2-handmatig/`:
  - `memo` rond `TaakItem` en `TakenLijst`;
  - `useMemo(() => traagFilter(taken, filter), [taken, filter])`;
  - `useCallback` rond `wissel` met een lege dependency array. Dat mag, omdat `wissel` de functionele vorm `setTaken(huidige => …)` gebruikt.
- **Let op bij het nakijken:**
  - Zet het model `taken` in de dependencies van `useCallback`? Dat werkt ook, maar `wissel` wordt dan bij elke wijziging van `taken` opnieuw aangemaakt. Na het aanvinken renderen dan alle 3000 items, en niet één.
  - Vergeet het model `useCallback`, dan toont de meting dat meteen: *Koffie* rendert dan nog.

**1.4 (Act, daarna Plan)**
- **Verwacht resultaat:** de agent haalt `taken.laatsteTelling = …` weg. Dat is de fout `react-hooks/immutability`.
- **Let op:** sterke modellen halen soms meteen ook de globale teller weg, ondanks "verander niets anders". Dan zien studenten niet zelf dat de linter de globale variabele niet vond. Bespreek dat dan klassikaal met dit resultaat: met enkel de globale teller is `npm run lint` tevreden, maar de compiler slaat het component over. Dat is gemeten, `Statistiek.jsx` bevat dan geen `_c(`.
- **De Plan-vraag:** een goed antwoord noemt *puurheid*: geen side effects tijdens het renderen, zoals het aanpassen van een variabele buiten het component (slide 35).

### Antwoorden op de opdrachten

- **1.2, zonder `useCallback`:** `memo` vergelijkt de props met `Object.is`. `wissel` is bij elke render een nieuwe functie, dus `onWissel` is "anders". De render is wel goedkoper (23 ms tegenover 50 ms): `useMemo` hangt af van `[taken, filter]`, en die zijn gelijk, dus `traagFilter` wordt overgeslagen.
- **1.3:** de dev-output van `TakenLijst`:
  ```js
  const $ = _c(13);
  // $[0]: in dev een hash voor Fast Refresh
  const { taken, filter, onWissel } = t0;
  if ($[1] !== filter || $[2] !== onWissel || $[3] !== taken) {
    const zichtbaar = traagFilter(taken, filter);
    // ... <p> en zichtbaar.map(...) ...
  } else { t1 = $[4]; t2 = $[5]; }
  ```
  De compiler zet de filter en het opbouwen van de lijst in **één** blok (`filter`, `onWissel` én `taken`). Een handgeschreven `useMemo` heeft `[taken, filter]`.
- **1.4:**
  - De teller steeg met 2 per render (StrictMode) en telde dus nooit het echte aantal keer dat het blok getoond werd.
  - `open.sort(...)` is geen overtreding: `filter()` maakt een nieuwe, lokale array. `toSorted()` maakt de bedoeling wel duidelijker.
- **Bonus `'use no memo'`:** *Filter* en *Aanvinken* verdubbelen (±95 ms), omdat alle 3000 items weer renderen. Je gebruikt de directive als tijdelijke uitweg bij een component dat met de compiler fout werkt, of om te debuggen.

### Modelantwoorden reflectievragen deel 1

1. **Referentiële gelijkheid.**
   - **Reden twee van slide 30: de parent rendert.** De state van `App` verandert, en React rendert standaard alle kinderen mee, ook als hun props gelijk zijn. Dus voert `TakenLijst` `traagFilter` uit en renderen 3000 `TaakItem`s, waarna reconciliation vaststelt dat er in de DOM niets verandert (slide 17–18).
   - **Zonder `useCallback`:** `memo` vergelijkt elke prop met `Object.is`. `taken` en `filter` zijn dezelfde referenties, maar de arrow function `wissel` is bij elke render nieuw: `(() => …) !== (() => …)` (slide 31).
   - **Toch goedkoper (23 ms):** `useMemo` had zijn eigen dependencies `[taken, filter]` en die waren gelijk, dus de trage filter werd overgeslagen.

2. **De compiler cachet JSX-elementen.** In `App` staat:
   ```js
   if ($[15] !== filter || $[16] !== taken) {
     t7 = <Profiler id="TakenLijst" onRender={meet}><TakenLijst …/></Profiler>
   }
   ```
   - **Bij *Koffie*:** `App` geeft exact hetzelfde element-object terug, en React slaat de hele deelboom over, inclusief de Profiler.
   - **Met de handmatige `memo`:** `App` maakte wél een nieuw `<Profiler>`-element, en enkel `TakenLijst` werd binnen de Profiler overgeslagen (0 ms).
   - **Wie kiest de dependencies?** De compiler analyseert tijdens de build van welke waarden elke berekening en elk element afhangt, en genereert de vergelijkingen zelf. Met een handgeschreven dependency array kan je een waarde vergeten (je krijgt dan een verouderde waarde, een stale closure) of er een te veel opnemen (dan is er geen cache). Die klasse van fouten bestaat met de compiler niet (slide 33–34).

3. **Puur zijn.**
   - **Waarom 2 per render:** React roept in development elk component twee keer aan om onzuivere componenten te ontmaskeren.
   - **Als de compiler toch cachete:** bij een cache hit wordt de functie niet uitgevoerd, dus zou de teller níet stijgen terwijl het blok wel getoond werd. De optimalisatie zou het gedrag veranderen.
   - **Daarom een bail-out:** de compiler gaat ervan uit dat componenten puur zijn, en slaat een component over als hij dat niet kan garanderen (slide 35).
   - **De linter:** die vangt niet alle overtredingen. Controleer dus met React DevTools (badge *Memo ✨*) of de output, en schrijf code die de regels volgt.

4. **Grenzen.**
   - **Geen snelheid, enkel minder herhaling:** memoization voorkomt **onnodig** herhaald werk. Een berekening die echt moet gebeuren (`taken` veranderde), duurt even lang.
   - **Welke hooks blijven:** de compiler vervangt in de meeste gevallen `memo`, `useMemo` en `useCallback`, maar niet `useState`, `useEffect`, `useRef`, `useContext` … (slide 33).
   - **Trage code** versnel je zelf, bijvoorbeeld met virtualisatie of een snellere filter.

5. **De agent en de compiler.**
   - **Wat je kon missen:** een ontbrekende of foute `useCallback`, of `taken` in de dependency array van `wissel`. Zichtbaar wordt dat alleen door te **meten**: *Koffie* rendert dan nog, of na het aanvinken renderen alle items.
   - **Wat je moest begrijpen om de diff goed te keuren:** referentiële gelijkheid, wat `memo` vergelijkt, en wat een dependency array betekent.
   - **De les:** een agent versnelt het typwerk, maar het nakijken vraagt evenveel kennis als het zelf schrijven. En de compiler maakt die hele klasse van handwerk, en dus ook die foutenbron, overbodig. Een goede automatisering (de compiler) is betrouwbaarder dan snel gegenereerd handwerk (de agent).

---

## Deel 2: zoneless Angular

### Resultaten

**2.0:** er staat nergens `zone.js` en er is geen `changeDetection`: zoneless (sinds v21) en OnPush (sinds v22). Relevante regels in `AGENTS.md`:
- "Do NOT set `changeDetection: ChangeDetectionStrategy.OnPush` explicitly. `OnPush` is the default in Angular v22+."
- "Use signals for state management"
- "Use `computed()` for derived state"
- "Do NOT use `mutate` on signals, use `update` or `set` instead"
- "Prefer Signal Forms"

**2.1 (situatie A)**

| Test | Resultaat |
|---|---|
| Klok | staat stil |
| Teller | werkt |
| Boeken na 1 s | blijven op "Laden…" staan |
| Klik op *+1* | klok en boeken blijven ongewijzigd |
| Twee boeken toevoegen | na het eerste verschijnt plots de lijst (4); na het tweede zegt de kop 5, maar toont de lijst er 4 |

**2.2**

| | OnPush | Eager (alle componenten, ook `App`) |
|---|---|---|
| **zoneless** | **A:** klok stil, boeken laden niet, kop ≠ lijst | **B:** klok en boeken springen pas bij een klik ergens naar de juiste waarde; kop = lijst |
| **zone.js** | **C:** exact hetzelfde als A | **D:** alles werkt (= Angular ≤ 21) |

- **D met `App` op OnPush:** klok stil, boeken laden niet. Pas een klik op *+1* (een event in `Teller`, dat `App` als voorouder dirty maakt) werkt alles bij.
- **Bundel:** zonder zone.js 125,33 kB raw (37,94 kB transfer), met zone.js 163,81 kB (50,11 kB): +35,88 kB raw, +11,64 kB transfer. De eindoplossing met `resource()` weegt 136,65 kB (41,01 kB).

### Taken van de agent: verwacht resultaat en aandachtspunten

- **B en D (Eager):** `AGENTS.md` zegt niets over Eager, maar wel "use signals". Een model kan aarzelen of tegenspreken. Dat is een mooi moment: de agent volgt de projectregels, de student moet bewust een experiment opzetten dat ertegen ingaat.
- **C (zone.js):** het model moet toestemming vragen voor `npm install zone.js`. Dat is geen "veilig" commando, dus de agent mag het niet automatisch uitvoeren. Controleer:
  - in `angular.json`: `"polyfills": ["zone.js"]` onder `architect › build › options`;
  - in `app.config.ts`: `provideZoneChangeDetection()`.
- **2.3 (Plan, daarna Uitvoeren):** het verwachte resultaat staat in `src/app/klok.ts`, `teller.ts` en `boeken.ts`. Let op de valkuilen van een plan:
  - `markForCheck` of `ChangeDetectorRef`;
  - `effect()` om state te kopiëren;
  - `push` op de waarde van de resource;
  - een `subscribe` zonder signal.

  `AGENTS.md` bevat ook "Do not assume globals like (`new Date()`) are available". Een model kan daardoor omslachtig doen bij de klok. Bespreek dat: de regel is bedoeld voor templates, niet voor componentcode.

### Modelantwoorden reflectievragen deel 2

1. **Wanneer en welke.**
   - **Klok:** `setInterval` past een gewoon veld aan. Er is geen melding, dus Angular kijkt nooit.
   - **Teller:** een `(click)` in de template is een melding, en maakt `Teller` en zijn voorouders dirty.
   - **Boeken laden:** de fetch zet gewone velden, dus er is geen melding. Een klik op *+1* helpt niet: `Boeken` is OnPush, niet dirty en wordt overgeslagen.
   - **Toevoegen:** de submit is een event in `Boeken`. `Boeken` ververst en ziet nu ook `laden = false`, daarom verschijnt de lijst plots. `BoekenLijst` (OnPush) krijgt dezelfde array-referentie, dus zijn input is volgens `===` niet veranderd. Het component is niet dirty en wordt overgeslagen. De kop telt dus wel mee, de lijst niet.

2. **zone.js beantwoordt alleen *wanneer*.** zone.js start na elke async gebeurtenis een ronde. Maar met OnPush slaat die ronde elk component over dat niet dirty is, en een timer of fetch maakt niets dirty. Vroeger werkte "alles vanzelf" door de **combinatie** van zone.js en Default/Eager. **Migratie:** OnPush slaat een niet-dirty component **met al zijn kinderen** over, ook Eager-kinderen (zie D met `App` op OnPush). Enkel de "probleemcomponenten" op Eager zetten zou dus niet volstaan. Bovendien kan geen tool betrouwbaar bepalen welke componenten van impliciete change detection afhangen. Alles op Eager zetten is de enige migratie die gegarandeerd hetzelfde gedrag behoudt.

3. **Hetzelfde principe.**
   - **De gedeelde vergelijking:** zowel `memo` als OnPush vergelijken met `===`.
   - **React:** een nieuwe functie is een nieuwe referentie, dus "gewijzigd", met een onnodige render als gevolg.
   - **Angular:** `push` op dezelfde array is dezelfde referentie, dus "niet gewijzigd", met een gemiste update als gevolg.
   - **Oplossing in beide gevallen:** immutability (slide 31).

   **Signals** houden bij welke consumers ze lezen (templates, `computed`, effects). Bij `set` of `update` worden precies die consumers dirty, en worden enkel die views ververst (slide 23). Er wordt niets "voor niets" uitgevoerd, dus er is ook niets te memoïzeren. React voert de componentfunctie opnieuw uit en beperkt daarna met memoization. Hetzelfde doel, een andere weg: de build bij React, de runtime bij Angular (slide 25).

4. **Magie of expliciet?**
   - **Monkey patching:** tijdens het draaien bestaande functies (`setTimeout`, `addEventListener`, `Promise`, `XMLHttpRequest` …) vervangen door een versie met extra code die Angular verwittigt (slide 27).
   - **Nadelen van zone.js:**
     - +36 kB JavaScript (gemeten);
     - change detection na elke gebeurtenis, ook als er niets veranderde;
     - moeilijke stack traces;
     - een verborgen afhankelijkheid: of het scherm bijwerkt, hangt af van *hoe* de code asynchroon werkt.
   - **`resource()` tegenover `markForCheck()`:** met `markForCheck()` moet je na elke asynchrone stap zelf onthouden om Angular te verwittigen, ook in elk foutpad, en zelf laadstatus en fouten bijhouden. `resource()` levert `value`, `isLoading` en `error` als signals, en verwittigt Angular automatisch. De verantwoordelijkheid ligt bij het framework.

5. **De agent en AGENTS.md.**
   - **Verwacht:** de code van de agent volgt de regels uit `AGENTS.md`: signals, `computed`, `update` in plaats van mutatie, geen expliciete OnPush, en `inject()`.
   - **Zonder `AGENTS.md` en zonder sturing:** een model dat vooral oudere Angular-code kent, schrijft waarschijnlijk `this.nu = new Date()` in een `setInterval`, of `this.boeken = data` na een `subscribe` of `await`. Dat is precies de code uit de startversie. Ze werkte met zone.js en Default, maar werkt in Angular 22 niet meer (slide 57).
   - **Nut van `AGENTS.md`:** het geeft het model actuele, versiegebonden regels mee, en het Angular-team levert het zelf mee via `ng new --ai-config` (slide 58 en 63).
   - **Wat de student nodig had:** de prompt kon alleen goed zijn omdat de student wist wat de oplossing moest bevatten: signals, `resource`, een nieuwe array, en geen `markForCheck` of Eager. Dat is precies de theorie van slide 28 en 29.

---

## Deel 3: Next.js 16

### Resultaten

**3.1**
- **Componentenboom:**
  - Server Components: `RootLayout`, `BoekenPagina` (na 3.2 ook `Boekenlijst`) en `NieuwBoek` (enkel in de startcode).
  - Client Components: `BoekenZoeker` (`'use client'`) en, na 3.4, `NieuwBoek` (voor `useActionState`).
  - `app/acties.ts` is `'use server'`: dat zijn Server Functions, geen componenten.
- **De `[db]`-log** staat in de terminal, en in development ook in de browserconsole met het label *Server*. In productie staat hij enkel in de terminal (gecontroleerd).
- **Paginabron en JavaScript:** de titels staan in de HTML. De tekst `boeken opgehaald` staat in geen enkel JS-bestand van de browser.
- **Zonder `server-only`:** de build crasht met een interne Turbopack-fout: "the chunking context (unknown) does not support external modules (request: node:fs/promises)".
- **Met `server-only`:** "'server-only' cannot be imported from a Client Component module", met een import trace.

**3.2**
- **De build van de startcode faalt:** *Route "/boeken": Next.js encountered uncached or runtime data during prerendering.* De opties: `[stream]` Suspense, `[cache]` `"use cache"`, `[block]` `export const instant = false`.
- **Oorzaken:** de trage query (uncached) en `cookies()` in `huidigeRol()` (runtime data).
- **Na de oplossing:** `/` ○ (statisch), `/boeken` ◐ (Partial Prerender) met *Revalidate 1h, Expire 1d*.

| Productie | Lijst zichtbaar | `[db]`-regels tijdens het draaien |
|---|---|---|
| Enkel stream (ter vergelijking) | fallback meteen, lijst na ± 1,5 s, bij elk bezoek | 1 per bezoek |
| Stream + `'use cache'` | ± 130 ms, daarna ± 30 ms | 0: de cache werd gevuld tijdens de build, vandaar de `[db]`-regel in de build-uitvoer |

**3.3**

| Situatie | Direct na toevoegen | Na herladen | Enkele seconden later |
|---|---|---|---|
| Cache, geen invalidatie | oud | **oud** (tot 1 uur) | oud |
| `updateTag('boeken')` | **nieuw** | nieuw | nieuw |
| `revalidateTag('boeken', 'max')` | oud | oud | **nieuw** (na ± 2,5 s) |

**3.4**
- **Het request:**
  - `POST /boeken`
  - headers `Next-Action` (het id van de functie), `Next-Router-State-Tree`, `Accept` en `Content-Type`
  - body `[1]`
- **Vóór de beveiliging:** als lezer met body `[2]` geeft het request **HTTP 200**, en het boek is weg.
- **Na de beveiliging:**
  - het request geeft **HTTP 500**, met in het antwoord enkel `E{"digest":"…"}`;
  - de foutmelding staat enkel in de serverlog;
  - het boek blijft bestaan.
- **Spaties als titel:** in de startcode wordt een leeg boek opgeslagen. Na de beveiliging verschijnt "Titel en auteur zijn verplicht.".

### Taken van de agent: verwacht resultaat en aandachtspunten

- **3.1 (Plan):** controleer of het model `BoekenZoeker` correct als Client Component herkent (`'use client'`), en `app/acties.ts` niet als component benoemt.
- **3.2 (Uitvoeren):** `AGENTS.md` vraagt om de documentatie in `node_modules/next/dist/docs/` te lezen. Een goed model doet dat zichtbaar in het verloop van de sessie, door bestanden uit die map te lezen. Het verwachte resultaat staat in `app/boeken/page.tsx` en `lib/db.ts`. Let op: zet het model ook `huidigeRol()` in de cache, dan faalt de build met "`cookies()` can't be read inside `"use cache"`".
- **3.3 (Uitvoeren):** de prompt noemt bewust geen functie. Wat het model kiest:
  - **`updateTag('boeken')`:** de beste keuze, want *read-your-own-writes* en enkel in Server Actions.
  - **`revalidateTag('boeken', 'max')`:** de gebruiker ziet zijn eigen wijziging niet meteen.
  - **`revalidatePath('/boeken')`:** werkt, maar is grover.

  Dat verschil is stof voor reflectievraag 3.
- **3.4 (Uitvoeren):** het verwachte resultaat staat in `app/acties.ts` en `app/boeken/nieuw-boek.tsx`. Controleer dat de rol **in de action** gecontroleerd wordt, niet enkel in de UI. Een model kan ook enkel `throw` gebruiken bij validatiefouten in `voegBoekToe`: dat werkt, maar geeft geen nette foutmelding in het formulier. Een return-waarde met `useActionState` doet dat wel.

### Modelantwoorden reflectievragen deel 3

1. **Wat draait waar?**
   - **Tijdens de build:** de layout, de titel, het formulier en de fallback (de statische shell, vergelijkbaar met SSG).
   - **Per request op de server:** de lijst met de rol uit de cookie, gestreamd in de open HTML-response (SSR met streaming, slide 12). De boeken zelf komen uit de server-cache.
   - **In de browser:** het zoekveld en de knoppen, geïnteractiveerd door hydration (slide 11).
   - **Code in de browser:** enkel het JavaScript van Client Components gaat naar de browser. Van Server Components komt alleen het resultaat mee. Aangetoond: `boeken opgehaald` staat in geen enkel JS-bestand.
   - **Voordeel:** minder JavaScript, en databasecode en geheimen verlaten de server niet (slide 13).
2. **De grens.**
   - **Zonder `server-only`:** de bundler crasht diep in het proces, met een interne fout die niets over je eigen code zegt.
   - **Met `server-only`:** een duidelijke fout met de importketen. Het beschermt ook modules zonder Node-API's, maar met geheime logica of sleutels, die anders stilletjes in de browserbundel zouden belanden.
   - **Serialisatie:** props van server naar client reizen als tekst in de RSC-payload (Flight). Data kan geserialiseerd worden, maar een functie (code plus closure) niet (slide 49).
   - **Een Server Action** wordt niet zelf verstuurd: er gaat enkel een verwijzing mee (het action-id), en een aanroep wordt een HTTP POST naar de server. Daardoor is ze ook een publiek endpoint.
3. **Cache en invalidatie.**
   - **De rol:** persoonlijke data, bij elk request vers. Een gedeelde cache hergebruikt een resultaat voor iedereen. Next.js verbiedt `cookies()` in `'use cache'`.
   - **Als de lijst met knoppen één keer gecachet werd:** werd ze gecachet nadat een beheerder de pagina opvroeg, dan zag elke lezer de verwijderknoppen. Dat is een klassiek datalek door caching.
   - **3.3:** het boek bleef onzichtbaar tot de cache verliep. Cachen is eenvoudig, weten **wanneer** het resultaat niet meer klopt (invalidatie) is het moeilijke deel (slide 39). Next.js 16 maakt dat expliciet met `cacheTag` en `updateTag`/`revalidateTag`, waar Next.js 13–15 veel impliciet cachete (slide 40).
   - **`updateTag`:** meteen ongeldig, enkel in Server Actions. Voor *read-your-own-writes*, bijvoorbeeld een reactie plaatsen of een profiel aanpassen.
   - **`revalidateTag(…, 'max')`:** stale-while-revalidate (gemeten: ± 2,5 s oude data). Voor content waarbij snelheid voor iedereen belangrijker is dan meteen actueel zijn, zoals een productcatalogus of een blog, bijvoorbeeld via een CMS-webhook.
4. **Publiek endpoint.**
   - **Wat er echt gebeurt:** de client stuurt een POST met het action-id in `Next-Action` en de geserialiseerde argumenten in de body. De server deserialiseert de argumenten en voert de functie uit. Iedereen kan dat request sturen, met andere argumenten en zonder je UI (3.4: een lezer verwijderde een boek).
   - **Elke action controleert dus zelf:** authenticatie, autorisatie en validatie (slide 48).
   - **De `digest`:** foutmeldingen kunnen interne details verraden. In productie stuurt Next.js daarom enkel een `digest`, waarmee je de volledige fout in de serverlog terugvindt. Nette meldingen geef je terug als return-waarde.
   - **`wisselRol`** is zelf een publiek endpoint: iedereen kan zich beheerder maken. In een echte app bepaalt een login op de server de rol, met een ondertekende sessie.
   - **React2Shell:** het lek zat in de **deserialisatie** in React zelf, vóór je eigen code liep. Je eigen checks werden nooit bereikt. Bescherming: snel updaten, dependencies opvolgen (`npm audit`, Dependabot, Renovate) en lockfiles (slide 50).
5. **De agent als risico.**
   - **Prompt injection:** een LLM kan instructies en data in zijn context niet fundamenteel uit elkaar houden (slide 64). Een `AGENTS.md`, een README in `node_modules`, een issue of een webpagina met verborgen instructies kan de agent laten doen wat een aanvaller wil:
     - code toevoegen;
     - een sleutel lekken;
     - een kwaadaardige dependency installeren.

     `AGENTS.md` is zelf het bewijs dat agents zulke bestanden volgen.
   - **Least privilege in dit labo:** enkel lezen, bewerken en "veilige" commando's automatisch; alle andere commando's, de browser en MCP-servers enkel na goedkeuring, en geen modus die alles automatisch goedkeurt.
   - **Human in the loop:** `npm install` zelf goedkeuren, een plan beoordelen vóór de agent iets wijzigt, elke wijziging nakijken in de diff, en de startcode kunnen terugzetten.
   - **Productie:** met een agent die alle commando's zonder goedkeuring uitvoert op een machine met toegang tot productie kan één geïnjecteerde instructie data verwijderen, geheimen versturen of code deployen. Zonder dat een mens het ziet. Daarom: een sandbox, beperkte rechten, en menselijke goedkeuring voor alles wat niet terug te draaien is.

---

## Afsluitende reflectie: kern van een goed antwoord

**A.**
- **React met de compiler:** de beslissing *wat* hergebruikt wordt, valt **tijdens de build**. In de browser slaat React gecachete elementen over.
- **Angular met signals:** de beslissing valt **tijdens het draaien in de browser**. Signals kennen hun afhankelijken en verversen enkel die views.
- **Next.js:** veel werk verhuist naar de **server** en de **build**: de shell prerenderen, de server-cache, en Server Components die de browser niet bereiken.
- **Convergentie (slide 25):** alle drie doen ze alleen werk waar er echt iets veranderde, en zo weinig mogelijk in de browser. Ze gebruiken dezelfde bouwstenen in een andere verhouding.
- **Keuze (slide 45):**
  - **Intern dashboard:** geen SEO nodig, veel interactie. Een client-side app volstaat.
  - **Webshop:** SEO en snelheid zijn cruciaal. Een meta-framework met serverrendering en caching, met aandacht voor de security van Server Actions.

**B.** Een goed antwoord gebruikt het logboek.
- **Tijdwinst met de agent:** omschakelen en refactoren, dus het mechanische werk (2.2, 2.3, 3.2).
- **Weinig of geen tijdwinst:** kleine wijzigingen (1.3 zelf sneller), en wachten op het model.
- **Benodigde kennis:**
  - referentiële gelijkheid, om de memoization na te kijken;
  - het verschil tussen zoneless en OnPush, om de juiste prompt in 2.3 te schrijven;
  - het verschil tussen `updateTag` en `revalidateTag`, om de keuze in 3.3 te beoordelen;
  - het principe "publiek endpoint", om te zien dat een UI-check niet volstaat.
- **Het risico van vibe coding (slide 69):** wie die kennis niet heeft, aanvaardt code die werkt in de demo, maar fout, traag of onveilig is. Het bekendste voorbeeld uit de les: een verborgen knop als "beveiliging".
