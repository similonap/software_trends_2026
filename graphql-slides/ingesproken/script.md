# Spreektekst per slide

Elke slide begint met een regel `## <slide-id> | <titel>`. Alles daaronder tot de volgende `##` is wat er ingesproken wordt.
Pas je de tekst van een slide aan, dan spreekt `python3 maak.py` enkel die slide opnieuw in. De titel na `|` is alleen ter info.

## cover | Software Trends

Welkom bij deze les over GraphQL. Bijna elke applicatie praat met een API. De meeste zijn REST-API's, maar grote spelers zoals GitHub, Shopify, Airbnb en Meta gebruiken GraphQL. We leren wat het is, welke problemen het oplost, hoe de taal werkt, hoe server en client ermee omgaan, en wat er in 2025 en 2026 veranderd is. De titel komt van de officiële website: de API-taal voor mensen en agents. Dat is de rode draad van deze les.

## tagline | The API language for humans and agents

Zo stelt GraphQL zichzelf voor: the API language for humans and agents. Met drie beloftes: sterk getypeerde schema's en veilige requests, teams die onafhankelijk van elkaar kunnen werken, en gebruikersinterfaces die hun eigen data opvragen. Opvallend is het woord agents. GraphQL werd in 2012 voor mensen ontworpen. Is die claim marketing of klopt ze? Dat kan je pas beoordelen als je weet hoe GraphQL werkt. In trend vier komen we erop terug.

## agenda | Agenda

Eerst de vraag waarom GraphQL bestaat, en de vergelijking met REST. Dan de taal zelf: schema, queries, mutations en subscriptions. Dan de server en de client. Het tweede deel bestaat uit vier trends: de standaard die weer beweegt, federatie, security, en agents. We eindigen met wanneer je GraphQL kiest en wanneer REST. Slides met Kernbegrip rechtsboven zijn examenstof.

## kb-graphql | Wat is GraphQL?

GraphQL is twee dingen: een querytaal voor API's, en een runtime op de server die die queries uitvoert, tegen een sterk getypeerd schema. Het kernidee heet declaratieve data fetching: de client beschrijft wat hij nodig heeft, niet hoe het opgehaald wordt. In het voorbeeld vragen we een gebruiker, zijn naam en de titels van zijn posts, en het antwoord heeft exact die vorm. Meestal is er één endpoint. GraphQL zegt niets over opslag of transport. Het ontstond in 2012 bij Facebook en wordt sinds 2018 beheerd door de GraphQL Foundation: een open standaard.

## waarom | Waarom was er nood aan iets nieuws?

Vier redenen. Eén: mobiele apps, met trage verbindingen waar elke overbodige kilobyte telt. Twee: veel verschillende clients, zoals website, iOS en Android. Eén REST-API past niet voor allemaal, dus laat GraphQL de client kiezen. Drie: snellere productiteraties, want de interface verandert elke week en dat mag geen nieuw endpoint vragen. En vier, de nieuwste: AI-agents, die een gestructureerde interface met een schema nodig hebben om een onbekende API te verkennen.

## geschiedenis | Even wat geschiedenis

In 2012 gebruikt Facebook GraphQL intern. In 2015 wordt het open source. In 2016 lanceert GitHub een publieke GraphQL-API. In 2018 komt het onder de GraphQL Foundation. Daarna wordt het stil: vier jaar lang blijft de editie van 2021 de laatste. In september 2025 verschijnt eindelijk een nieuwe, en in 2026 GraphQL.js versie 17. Een misverstand: GraphQL is niet enkel iets voor JavaScript. Er zijn servers en clients in vrijwel elke taal.

## adoptie | Wie gebruikt GraphQL?

Meta, AWS, Airbnb, PayPal, The New York Times, Shopify, GitHub. Meta vertelde in 2026 over honderden miljarden aanroepen per dag. Volgens cijfers uit artikels over het Postman-rapport gebruikt ongeveer een derde van de respondenten GraphQL, tegenover drieënnegentig procent REST. Ik vond die percentages enkel in artikels, niet in het rapport zelf. De conclusie: GraphQL is breed gebruikt, maar vervangt REST niet. Ze bestaan naast elkaar, vaak in hetzelfde bedrijf.

## kb-rest | Wat is REST?

Eerst REST, wat er vóór kwam. Roy Fielding beschreef het in 2000. Data wordt aangeboden als resources met een eigen URL, en je bewerkt ze met HTTP-methodes: GET, POST, DELETE. Het is een stijl, geen specificatie, dus elke API pakt paginering, filteren en fouten anders aan. Voordelen: eenvoudig, en je krijgt caching en statuscodes van HTTP gratis. Nadelen: geen standaard voor relaties, en twee problemen die nu volgen: versies, en over- en underfetching.

## rest-versies | REST: het probleem van versies

Het eerste probleem: versies. Endpoints worden vaak rond specifieke schermen gebouwd. Verandert de frontend, dan moet de backend mee. Breekt een wijziging bestaande clients, dan maak je v2, v3. Dat geeft duplicatie, moeilijk onderhoud en trage samenwerking. GraphQL werkt versieloos. Omdat de client zelf kiest welke velden hij vraagt, breekt een nieuw veld niets. Wil je iets weghalen, dan markeer je het eerst als deprecated, meet je of het nog gebruikt wordt, en verwijder je het pas daarna.

## rest-voorbeeld | REST: een voorbeeld

Een blogapp. Het scherm toont de naam van Mary, de titels van haar posts en de namen van haar laatste drie volgers. Met REST doe je drie requests. De gebruiker, met ook adres en geboortedatum. De posts, met volledige inhoud en reacties. De volgers, allemaal, met hun adres. Drie round-trips, en veel meer data dan het scherm toont. Je kan een speciaal endpoint voor dit scherm bouwen, maar dan zit je weer in het versieprobleem.

## gql-voorbeeld | Hetzelfde met GraphQL

Hetzelfde scherm met GraphQL. Eén query: de gebruiker, zijn naam, van de posts enkel de titel, en van de laatste drie volgers enkel de naam. Het antwoord volgt precies de vorm van de query: geen adres, geen geboortedatum, geen inhoud. Eén request in plaats van drie. En wil de frontend morgen ook het aantal reacties tonen, dan voegt ze dat veld toe, zonder dat de backend verandert.

## kb-fetching | Overfetching, underfetching en N+1

Drie begrippen. Overfetching: je krijgt meer data dan je nodig hebt, wat bandbreedte en batterij verspilt. Underfetching: één endpoint geeft te weinig, dus doe je extra requests. In het ergste geval het N+1-probleem: één request voor een lijst en dan één per element. Bij de PokéAPI zijn twintig Pokémon eenentwintig requests. GraphQL lost dit aan de clientkant op. Maar onthoud: het N+1-probleem verdwijnt niet, het verhuist naar de server. Daarover straks meer, bij DataLoader.

## iteraties | Snellere iteraties

Wat betekent dat voor het team? Bij REST wordt elke frontendwijziging backendwerk, en wacht het frontendteam op de backend. Bij GraphQL kiest de client zelf uit het schema. Zolang de data in het schema zit, hoeft de backend niet te veranderen als de interface verandert. Dat was een hoofdreden voor Facebook: honderden ontwikkelaars aan dezelfde app, zonder op elkaar te wachten.

## kb-schema | Het schema

Het hart van GraphQL: het schema, een verzameling types en velden die je kan opvragen. Het werkt als een contract. Omdat het getypeerd is, kan een query gevalideerd worden voor ze uitgevoerd wordt, zelfs al in je editor. En de server geeft garanties: een String met uitroepteken is nooit null. Gevolgen: front- en backend werken onafhankelijk zolang het schema blijft, het schema is bevraagbaar via introspectie, en het is meteen de documentatie.

## kb-sdl | Schema Definition Language

Een schema schrijf je in de SDL. Het voorbeeld heeft Person en Post. ID, String en Int zijn scalars, de basistypes. Een uitroepteken betekent non-null. En de relaties maken het een graph: van persoon naar posts, van post terug naar auteur. Vandaar de naam. Er bestaan ook enums, interfaces, unions en input types. En de tekst tussen drie aanhalingstekens is een description, documentatie in het schema zelf. Onthoud dat, want voor AI-agents wordt dat heel belangrijk.

## queries | Queries

Nu queries. De eenvoudigste: van alle personen de naam. Voeg je age toe aan de query, dan zit age ook in het antwoord. De vorm van de query bepaalt de vorm van het antwoord. Velden kunnen argumenten hebben, zoals last met waarde twee, en het schema bepaalt wat die betekenen. Ik heb deze queries met GraphQL.js 17 uitgevoerd: dit zijn echte antwoorden.

## queries-genest | Geneste queries

De echte kracht zit in relaties. Van alle personen de naam, en van hun posts de titel. Het antwoord volgt de nesting. Alice heeft nog geen posts: een lege lijst, geen null, omdat het schema dat zegt. In één request volg je zo de relatie, waar REST het N+1-probleem gaf. Je kan dieper gaan: naar auteur, reacties, auteurs van reacties. Dat is een graph. Het brengt wel een risico mee: wat als iemand tien niveaus diep vraagt? Dat zien we in trend drie.

## kb-variabelen | Operatienaam, variabelen, aliassen, fragmenten

In echte applicaties gebruik je vier dingen. Een operatienaam, handig voor logging en monitoring. Variabelen: de id staat niet in de query maar wordt apart als JSON meegestuurd, zodat de querytekst altijd gelijk blijft, belangrijk voor caching en security. Aliassen, om hetzelfde veld twee keer met andere argumenten te vragen. En fragmenten: herbruikbare selecties van velden, de basis van moderne clients.

## mutations | Mutations

Lezen doe je met queries, wijzigen met mutations: aanmaken, aanpassen, verwijderen. Een mutation geeft ook zelf data terug, in de vorm die de client vraagt. We maken Bob aan en krijgen zijn nieuwe id terug. Vaak vraag je net de velden terug die je scherm moet bijwerken. Een verschil met queries: meerdere mutations in één request worden na elkaar uitgevoerd, queries mogen parallel.

## subscriptions | Subscriptions

Het derde soort: subscriptions. Je abonneert je op een gebeurtenis, en de server pusht data telkens die plaatsvindt: een stroom van resultaten in plaats van request en response. Dat loopt over WebSockets of Server-Sent Events. Typisch voor chat, notificaties en live dashboards. Voor gewone data gebruik je beter queries, want een subscription houdt een verbinding open en kost de server capaciteit.

## kb-root-types | Root types

Queries en mutations werken pas als het schema de ingangen definieert, met drie root types: Query, Mutation en Subscription. Query bevat alles waarmee je kan beginnen lezen. Mutation bevat de wijzigingen, zoals createPerson. Subscription bevat newPerson. De types van de argumenten moeten kloppen met de rest van het schema. Schrijf je bij de leeftijd per vergissing String, dan weigert de server de mutation. Zo'n fout zie je meteen, niet pas wanneer rare data in je databank zit.

## kb-introspectie | Introspectie

Hoe weet de client wat er bestaat? Met introspectie: je bevraagt het schema zelf met een gewone query, via velden die met twee underscores beginnen. Dat maakt tools mogelijk: GraphiQL, een IDE in de browser met autocomplete en documentatie, codegeneratoren, en recent AI-agents die zelf ontdekken wat een API kan. Maar het is ook een risico: interne velden zijn zichtbaar voor iedereen. Veel teams zetten introspectie uit voor publieke clients, maar in trend drie zien we waarom dat niet volstaat.

## kb-antwoord | Het antwoord en foutafhandeling

Een antwoord heeft altijd dezelfde vorm: data, en eventueel errors. GraphQL kan gedeeltelijke resultaten geven. Werkt de dienst met posts niet, dan krijg je toch de naam, posts wordt null, en errors bevat het pad naar het foute veld. De client toont het deel dat werkt. Maar faalt een non-null veld, dan wordt de null doorgegeven naar de ouder, en verder omhoog. Dat heet null bubbling, en het kan veel van het antwoord wissen. Daarover meer in trend één.

## architecturen | Architecturen

Drie typische architecturen. Eén: een GraphQL-server met een eigen databank, vooral bij nieuwe projecten. Twee: GraphQL als laag boven bestaande systemen, oude systemen, microservices en externe API's achter één schema. Drie: een hybride, het meest voorkomend. Voor de client maakt het niet uit waar de data vandaan komt. Hoe de server dat mogelijk maakt: met resolvers.

## kb-resolvers | Resolvers

Elk veld in het schema heeft een resolver: een functie die weet waar de data vandaan komt. De resolver van Query.user haalt de gebruiker uit de databank. De resolver van User.followers krijgt de ouder, de zonet gevonden gebruiker, en de argumenten. De server valideert de query, voert dan voor elk gevraagd veld de resolver uit, van boven naar beneden, en voegt alles samen tot één antwoord. Elke resolver mag een andere bron hebben: SQL, een REST-API, een cache. Zo combineert GraphQL verschillende systemen in één antwoord.

## kb-dataloader | DataLoader en het N+1-probleem

Hier is het N+1-probleem op de server. De query vraagt posts met de naam van de auteur, maar de resolver van Post.author loopt per post. Duizend posts is duizend en één databankqueries. De oplossing heet DataLoader. Je resolver vraagt niet rechtstreeks de databank, maar roept loader.load aan. DataLoader verzamelt alle aanroepen binnen dezelfde tick, dat heet batching, en voert één query uit met alle id's, ontdubbeld. Ik testte met drie posts: zonder DataLoader drie aanroepen voor de auteurs, met DataLoader één.

## kb-declaratief | Declaratieve data fetching op de client

De clientkant. Je kan GraphQL aanroepen met gewone fetch, maar dan doe je alles zelf, imperatief: request bouwen, antwoord parsen, data bewaren en up-to-date houden. De declaratieve aanpak gebruikt een GraphQL-client. Je beschrijft in een query wat een component nodig heeft, en de bibliotheek haalt de data op, cachet ze en werkt de interface bij. Dat is hetzelfde idee als declaratief versus imperatief in de les over web frameworks. De bekendste clients zijn Apollo Client, Relay van Meta en urql.

## colocation | Fragment colocation

Een patroon in grote applicaties: dingen die samen horen, staan samen. Elk component declareert zijn data-behoefte als een fragment, in hetzelfde bestand. FriendListItem definieert zijn fragment, FriendList gebruikt dat fragment in zijn query, en de client stuurt één query. Wil een kind morgen ook de stad tonen, dan pas je enkel dat fragment aan. Relay en Apollo Client 4 gaan verder met data masking: een component ziet enkel de velden uit zijn eigen fragment. Daarom werkt GraphQL goed in heel grote frontends.

## codegen | Codegeneratie

Het schema en de queries zijn getypeerd, dus schrijf je de TypeScript-types niet met de hand. Dat leidt tot verouderde types en tikfouten. Tools genereren ze: GraphQL Code Generator, gql.tada, en de compiler van Relay. Verandert het schema, bijvoorbeeld omdat age verdwijnt, dan geeft de TypeScript-compiler meteen een fout op elke plaats die het veld gebruikt. Zo vind je de gevolgen van een schemawijziging voordat je gebruikers ze vinden.

## div-1 | Trend 1: de standaard beweegt weer

We beginnen aan de trends. De eerste gaat over de standaard zelf. Tussen oktober 2021 en september 2025 verscheen er geen nieuwe editie en ook geen grote nieuwe versie van de referentie-implementatie. Sinds 2025 beweegt de standaard weer.

## spec-2025 | De nieuwe specificatie (september 2025)

Op 8 september 2025 verscheen de nieuwe editie, aangekondigd door Lee Byron, een van de bedenkers. Het belangrijkste is OneOf input objects, de volgende slide. Verder schema coordinates, een standaardnotatie om naar een element van het schema te verwijzen. Descriptions op operaties, nuttig voor collega's én AI-tools. Deprecation op meer plaatsen, volledig Unicode-bereik en verduidelijkte regels. Geen revolutie, wel het signaal dat de standaard weer onderhouden wordt.

## kb-oneof | OneOf input objects

Het meest gevraagde onderdeel: oneOf. Stel dat je een persoon opzoekt op id óf op naam. Vroeger had je twee velden, of één veld met twee optionele argumenten en zelf controleren dat er precies één was ingevuld. Met oneOf zeg je in het schema: precies één van deze velden. De query met enkel een id is geldig. Die met id én naam wordt al bij de validatie geweigerd, nog voor een resolver loopt. Ik testte het met GraphQL.js 17. In de community heet dit een input union.

## graphqljs17 | GraphQL.js 17

GraphQL.js is de referentie-implementatie. Bijna elke JavaScript-server gebruikt ze. Op 15 juni 2026 verscheen versie 17, de eerste grote versie sinds 2021. Stabiel: afbreekbare requests, zodat resolvers geen werk meer doen voor niemand, en hideSuggestions, wat we in trend drie als securitymaatregel zien. Ook findSchemaChanges, dat brekende wijzigingen detecteert, handig in CI. Experimenteel: incremental delivery met defer en stream, een manier om foutpropagatie uit te schakelen, en fragment-argumenten.

## kb-defer | Incremental delivery: defer en stream

Het probleem: sommige velden zijn traag, en het hele antwoord wacht op het traagste. Met defer op een fragment zeg je: dit deel mag later komen. De server stuurt eerst het antwoord met de naam, met pending en hasNext true. Daarna volgt een bericht met de uitgestelde data en completed. Stream doet hetzelfde voor lijsten. Ik voerde dit uit met GraphQL.js 17: dit is het echte formaat. Het is nog een voorstel, maar verschillende servers en clients ondersteunen het al. Het lijkt op het streamen van HTML uit de les over web frameworks.

## nullability | Het nullability-probleem

Een oud probleem: nullability. Faalt een non-null veld, dan wordt de null doorgegeven naar de ouder. Faalt de dienst die avatars levert, dan wordt de hele User null, ook al is de naam beschikbaar. Zelfs een hele lijst kan verdwijnen. Daarom maken veel teams alle velden nullable. Dan wist een fout enkel dat veld, maar het schema zegt dan weinig meer. Onderweg zijn voorstellen om de client te laten kiezen wat er bij een fout gebeurt, met een optie onError. GraphQL.js 17 heeft daar een experimentele richtlijn voor.

## levend | Een levende standaard

Een overzicht in november 2026. De kernspecificatie is de editie van september 2025. Daarnaast GraphQL over HTTP, nog een draft, over mediatypes en statuscodes. Composite Schemas voor federatie, ook een draft, maar al geïmplementeerd. In juni 2026 kwam een nieuw proces bij, GAPs, voor specificaties naast de kern, geschreven door de community. Het patroon: de kern blijft klein en stabiel, nieuwe dingen komen in lagen ernaast, net als bij het web zelf.

## div-2 | Trend 2: federatie

Trend twee gaat over schaal. In een klein project is er één server. Maar wat doe je met honderd teams die elk een eigen dienst bouwen? Eén server voor iedereen is een flessenhals. Het antwoord heet federatie, en wordt in 2025 en 2026 gestandaardiseerd.

## kb-federatie | Federatie

Elk team bouwt een subgraph: een eigen GraphQL-service met een deel van het schema. Een router of gateway combineert alle subgraphs tot één schema, de supergraph. De client ziet enkel die ene API. De router zoekt uit welke delen van een query naar welke subgraph moeten, en voegt de antwoorden samen: query planning. Het mooiste zijn entities: het type User bestaat in twee subgraphs, met dezelfde key. Daardoor kan de router naam en reviews samenvoegen, zonder dat teams elkaars code kennen. Dat is de belofte van frictionless distributed development.

## composite | Composite Schemas

Federatie werd groot met Apollo Federation. Intussen heeft bijna elke leverancier een eigen variant: Hive Gateway, Grafbase, WunderGraph Cosmo, Fusion. Wie kiest, zit er min of meer aan vast. Daarom werkt een werkgroep van de GraphQL Foundation aan een gemeenschappelijke specificatie, Composite Schemas. Ze is in november 2026 nog een draft, maar wordt al geïmplementeerd. Op GraphQLConf 2026 zei Uri Goldshtein dat federatie geen experiment meer is, maar een set van beproefde paden. In een groot bedrijf is GraphQL dus vaak een gefedereerde graph.

## div-3 | Trend 3: security en performance

Trend drie: security en performance. De grootste kracht van GraphQL is dat de client bepaalt wat hij vraagt. Dat is ook het grootste risico, want een aanvaller is ook een client. In 2025 en 2026 waren er kwetsbaarheden die precies daarmee te maken hadden.

## kb-aanval | Aanvalsoppervlak van GraphQL

Vier risico's. Eén: diepe of dure queries. De vrienden van de vrienden van de vrienden, vijf niveaus diep, is bij honderd vrienden tien miljard objecten. Honderden aliassen of fragmenten die naar elkaar verwijzen leggen ook een server plat: denial of service met één request. Twee: batching voor brute force. Met aliassen steek je honderd login-pogingen in één request, en een rate limit per request helpt niet. Drie: informatielekken. Introspectie toont het schema, en zelfs zonder introspectie verraden de suggesties in foutmeldingen veel. Vier: autorisatie. Er is één endpoint, dus moet elke resolver zelf controleren wat een gebruiker mag zien.

## cves | Echte incidenten

Drie incidenten. April 2025, CVE-2025-32032 in de Apollo Router: diep geneste fragmenten maakten de query planning extreem duur, en één query kon de router laten vastlopen. Juli 2025 in Parse Server: het schema was op te vragen zonder sessie of sleutel. April 2026 in Hot Chocolate, de bekendste GraphQL-server voor .NET: de parser had geen limiet op nesting, en een document van veertig kilobyte veroorzaakte een stack overflow die het hele proces liet crashen. Het patroon: de server vertrouwt de vorm van de query te veel, en twee van de drie zijn denial of service via nesting.

## kb-verdediging | Verdediging

Vijf maatregelen, te combineren. Eén: diepte- en kostenlimieten, bij voorkeur met cost analysis. Twee: trusted documents, ook persisted operations: de app registreert vooraf zijn queries, en in productie stuurt de client enkel de hash en de variabelen. Dat werkt voor je eigen apps, niet voor een publieke API. Drie: introspectie en suggesties uitschakelen, maar dat is security through obscurity. Vier: autorisatie in de resolvers. Vijf: rate limiting per operatie en tijdig updaten van server, gateway en parser.

## caching | Caching en performance

Bij REST is caching bijna gratis, want elke URL is een resource en een CDN kan het antwoord bewaren. Bij GraphQL is alles een POST naar één endpoint, en een CDN cachet dat niet. Dat is een echt nadeel. Oplossingen: stuur queries via GET met de hash van een trusted document, zodat elke query een eigen URL heeft. Cache aan de serverkant per veld of object. En gebruik een genormaliseerde cache in de client: elk object wordt één keer bewaard, en een mutation werkt het automatisch bij op elk scherm. Vraag in mutations dus het id en de gewijzigde velden terug.

## div-4 | Trend 4: GraphQL voor humans and agents

We komen bij de slogan van het begin. In 2025 en 2026 positioneert de GraphQL-community zich nadrukkelijk als de taal waarmee AI-agents API's gebruiken: er kwam een AI-werkgroep, een server voor agents, en de conferentie van 2026 draaide erom. We bekijken waarom het werkt, hoe, en waar je kritisch moet blijven.

## kb-agents | Waarom past GraphQL bij AI-agents?

Een agent die een onbekende API moet gebruiken, heeft vier dingen nodig, en GraphQL biedt ze alle vier. Zelfbeschrijvend: via introspectie ontdekt hij types, velden en relaties, en de descriptions zijn de documentatie. Staat daar dat de prijs in eurocent is, dan toont hij geen prijs van 1999 euro voor een product van 19,99. Gevalideerd: verzint hij een veld, dan krijgt hij een duidelijke fout en kan hij zichzelf corrigeren. Precies: hij vraagt enkel wat hij nodig heeft, en bij een taalmodel telt elk woord in de context. En samenstelbaar: één query volgt relaties over meerdere types, waar REST meerdere endpoints vraagt.

## agent-flow | Hoe gaat dat concreet?

graphql.org beschrijft vier stappen. Eén: de agent krijgt een taak, bijvoorbeeld de omzet per regio voor de top vijf categorieën. Twee: hij doet introspectie en leest de descriptions. Drie: het taalmodel zet de vraag om in één precieze query. Is die ongeldig, dan krijgt hij een validatiefout en probeert hij opnieuw. Vier: hij krijgt gestructureerde JSON terug, en bij een fout staat in errors welk veld, zodat hij met gedeeltelijke resultaten verder kan. Hier schrijft de agent zelf queries. Dat is flexibel maar riskant: hij kan een dure query schrijven. Daarom bestaat er een andere aanpak.

## mcp | MCP en de Apollo MCP Server

Agents roepen tools aan via het Model Context Protocol. De bekendste oplossing voor GraphQL is de Apollo MCP Server, versie 1.0 in oktober 2025, open source. Hij maakt van GraphQL-operaties MCP-tools, met de variabelen als parameters en de description als uitleg, plus OAuth 2.1. Er zijn twee strategieën. Geef de agent het volledig schema en laat hem queries schrijven: flexibel, maar duur in context en risicovol. Of geef hem een gecureerde set operaties: veilig en voorspelbaar, maar minder flexibel. Dat is hetzelfde idee als trusted documents. De cijfers van Apollo over besparingen komen van de leverancier zelf, geen onafhankelijke meting.

## ai-community | De community en AI

De community gaat er volop in mee. In oktober 2025 startte de AI Working Group. Ze werkt aan semantic introspection, die ook zegt wat velden betekenen, zodat een agent in een schema met tienduizenden velden de relevante delen vindt. Aan een mock-richtlijn voor voorgedefinieerde antwoorden. En aan embeddings van schema's. Op GraphQLConf 2026 was AI het dominante thema, en de CEO van Apollo zei dat GraphQL de taal van AI kan en moet zijn. Er waren talks van onder meer Meta, Netflix en IBM.

## kritisch | Blijf kritisch

Zes kanttekeningen. Eén: grote schema's passen niet in een context window. Twee: agents schrijven dure queries, dus kostenlimieten en trusted documents zijn nog belangrijker. Drie: prompt injection blijft een risico, want data uit de API kan als instructie gelezen worden, en GraphQL lost dat niet op. Vier: REST is soms eenvoudiger, zegt graphql.org zelf. Vijf: veel cijfers komen van leveranciers. En zes: de slogan komt van de GraphQL-community zelf, die belang heeft bij populariteit. Dat maakt hem niet onwaar, maar het is een reden om zelf te oordelen. Dat kan je nu.

## wanneer | Wanneer kies je GraphQL, wanneer REST?

GraphQL is een goede keuze bij veel verschillende clients met verschillende databehoeften, een snel veranderende interface, veel backends en teams achter één API met federatie, of een API die agents moeten kunnen verkennen. REST is beter voor een eenvoudige CRUD-API met weinig clients, voor een publieke API waar CDN-caching cruciaal is, voor bestanden en media, en voor snelle interne communicatie kies je vaak gRPC. Het is geen religie: veel bedrijven gebruiken beide.

## studenten | Wat kan je er zelf mee?

Vijf tips. Eén: speel met een publieke API in GraphiQL, zoals de Star Wars-API of die van GitHub. Twee: bouw een kleine server en meet het N+1-probleem met en zonder DataLoader. Drie: genereer je TypeScript-types in plaats van ze met de hand te schrijven. Vier: denk in productie aan diepte- en kostenlimieten, trusted documents en autorisatie per veld. Vijf: schrijf descriptions in je schema, voor je collega's en voor de agents die je API misschien gaan gebruiken. Het schema is het hart van GraphQL.

## begrippen-1 | Begrippenlijst (1/2): basis

De eerste helft van de begrippenlijst: de basis. Je moet de begrippen kunnen definiëren en met een voorbeeld uitleggen. Let op wat samenhangt: over- en underfetching en het N+1-probleem, dat op de server terugkomt bij resolvers en DataLoader; het schema, de SDL en de root types; en variabelen, aliassen en fragmenten.

## begrippen-2 | Begrippenlijst (2/2): client en trends

De tweede helft gaat over de client en de trends. Declaratieve data fetching, fragment colocation en codegeneratie bij de client. OneOf, defer en stream en null bubbling bij de standaard. Federatie bij trend twee. Cost analysis, trusted documents en de genormaliseerde cache bij trend drie. En MCP en semantic introspection bij de agents. Kan je een begrip niet uitleggen, ga dan terug naar de slide met het label Kernbegrip.

## conclusie | Conclusie

Zeven punten. Eén: GraphQL laat de client kiezen, in één request. Twee: het schema is het hart, contract, documentatie en basis voor tooling. Drie: de server werkt met resolvers, en zonder DataLoader verhuist het N+1-probleem naar de server. Vier: de standaard beweegt weer. Vijf: federatie maakt één graph voor een hele organisatie. Zes: de flexibiliteit is ook het aanvalsoppervlak, dus limieten, trusted documents en autorisatie per veld. Zeven: voor AI-agents zijn introspectie, typering en precieze queries sterk, maar REST blijft juist voor eenvoudige API's. Ontwerp je schema goed, voor mensen én voor agents. Bedankt voor jullie aandacht.

## vragen | Vragen?

Dan zijn er nu vragen. Een discussievraag: zou jij een AI-agent vrij queries laten schrijven op je GraphQL-API, of enkel gecureerde operaties aanbieden? Denk aan de flexibiliteit en de introspectie, maar ook aan dure queries, informatielekken, de kost van context en prompt injection. Alle codevoorbeelden in deze les heb ik uitgevoerd met GraphQL.js 17.1 en DataLoader: de antwoorden die je zag, zijn echte antwoorden.
