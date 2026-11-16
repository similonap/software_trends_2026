"""Slides 30-57: vier trends van 2025-2026, wanneer GraphQL, begrippenlijst en conclusie."""
from helpers import *

B = []

# ======================= Trend 1 =======================
B.append(divider('div-1', 'Trend 1', 'De standaard beweegt weer',
    'Een nieuwe spec-editie na vier jaar, GraphQL.js v17 en incremental delivery',
"""We beginnen aan de trends. De eerste gaat over de standaard zelf. Tussen oktober 2021 en september 2025 verscheen er geen nieuwe editie van de GraphQL-specificatie, en ook de referentie-implementatie in JavaScript kreeg geen grote nieuwe versie. Sinds 2025 beweegt de standaard weer: een nieuwe spec-editie, GraphQL.js versie 17, en experimentele functies zoals defer en stream die al jaren in de maak waren.""",
["Trend 1: de standaard zelf",
 "Okt. 2021 → sept. 2025: geen nieuwe spec-editie, geen nieuwe major van GraphQL.js",
 "Nu: spec-editie 2025, GraphQL.js v17, defer/stream experimenteel",
 "→ Wat zit er in de nieuwe editie?"]))

B.append(slide('spec-2025', 'De spec-editie van september 2025',
    tabel(['Nieuw', 'Wat het doet'],
          [['**OneOf input objects** (`@oneOf`)', 'Precies één veld van een input moet ingevuld zijn'],
           ['**Schema coordinates**', 'Standaardnotatie voor schema-elementen: `Person`, `Person.name`, `Query.person(by:)`'],
           ['**Descriptions op operaties**', '`"""..."""` boven een query of fragment: documentatie en AI-tooling'],
           ['**Uitgebreide deprecation**', '`@deprecated` op meer plaatsen: evolueren zonder te breken'],
           ['**Volledige Unicode**', 'De taal aanvaardt het volledige Unicode-bereik'],
           ['**Verduidelijkte fout- en uitvoeringsregels**', 'Voorspelbaardere antwoorden voor tools']], [36, 64], size=29)
    + p('De vorige editie dateert van **oktober 2021**. Aangekondigd door Lee Byron, een van de bedenkers van GraphQL, op GraphQLConf 2025.', 30, '#595959'),
"""Op 8 september 2025 verscheen de nieuwe editie van de GraphQL-specificatie, aangekondigd door Lee Byron, een van de oorspronkelijke bedenkers van GraphQL bij Facebook. De vorige editie dateerde van oktober 2021.

Wat is er nieuw? Het belangrijkste is OneOf input objects, de volgende slide. Daarnaast schema coordinates: een standaardnotatie om naar een element van het schema te verwijzen. Person is het type, Person punt name het veld, Query punt person met by tussen haakjes het argument. Dat lijkt klein, maar het maakt foutmeldingen, tools en code reviews eenduidiger.

Descriptions op operaties: je kan nu ook boven een query of fragment documentatie schrijven met drie aanhalingstekens. Dat helpt collega's, en ook AI-tools die moeten begrijpen wat een query doet. Deprecation werkt op meer plaatsen, zoals argumenten en velden van input types. De taal aanvaardt het volledige Unicode-bereik. En de regels rond fouten en uitvoering zijn verduidelijkt.

Geen revolutie dus, maar wel het signaal dat de standaard weer onderhouden en uitgebreid wordt.""",
["8 sept. 2025: nieuwe editie (vorige: okt. 2021), aangekondigd door Lee Byron",
 "@oneOf; schema coordinates (Person, Person.name, Query.person(by:))",
 "Descriptions op operaties (documentatie + AI-tooling); @deprecated op meer plaatsen",
 "Volledige Unicode; verduidelijkte fout- en uitvoeringsregels",
 "Geen revolutie, wel: de standaard leeft weer",
 "→ @oneOf in detail"],
bron='graphql.org/blog (08/09/2025)'))

B.append(slide('kb-oneof', '@oneOf: precies één van de velden',
    row(
        col(code('''input PersonLookup @oneOf {
  id: ID
  name: String
}

type Query {
  person(by: PersonLookup!): Person
}''', 'graphql', 28),
            code('''{ person(by: { id: "1" }) { name } }                    # ✔
{ person(by: { id: "1", name: "Sarah" }) { name } }     # ✘''', 'graphql', 22), gap=16, flex='1.25'),
        col(ul(['Vroeger: twee velden (`personById`, `personByName`) of twee optionele argumenten die je **zelf** controleerde',
                'Met `@oneOf` zegt het schema: **precies één** veld moet ingevuld zijn',
                'De fout wordt al bij **validatie** gevonden'], size=30)
            + card('Getest (GraphQL.js 17)', '*Within OneOf Input Object type "PersonLookup", exactly one field must be specified ...*', size=26), gap=20), gap=40),
"""Het meest gevraagde nieuwe onderdeel: oneOf. Stel dat je een persoon wil opzoeken, ofwel op id, ofwel op naam. Vroeger had je twee opties. Ofwel twee aparte velden, personById en personByName. Ofwel één veld met twee optionele argumenten, en dan moest je in je code zelf controleren dat er precies één ingevuld is. Wie beide invulde of geen enkel, kreeg pas bij het uitvoeren een fout, of erger: een onverwacht resultaat.

Met de richtlijn oneOf op een input type zeg je in het schema zelf: van deze velden moet er precies één ingevuld zijn. Links het input type PersonLookup met id en name, en een veld person dat zo'n lookup als argument krijgt.

De eerste query, met enkel een id, is geldig. De tweede, met een id en een naam, wordt al bij de validatie geweigerd, nog voor er een resolver loopt. Ik heb het getest met GraphQL.js 17: de foutmelding zegt dat er binnen PersonLookup precies één veld opgegeven moet zijn.

In de community heet dit een input union: een van de langst gevraagde uitbreidingen van GraphQL.""",
["Vroeger: twee velden (personById/personByName) of twee optionele args met eigen controle",
 "@oneOf op een input: precies één veld moet ingevuld zijn",
 "{ id } ✔, { id, name } ✘ → al bij validatie geweigerd (getest, GraphQL.js 17)",
 "= 'input union', lang gevraagde uitbreiding",
 "Examen: @oneOf kunnen uitleggen met een voorbeeld",
 "→ GraphQL.js v17"],
kern=True, bron='graphql.org/blog: Safer Multi-option Inputs with @oneOf (04/09/2025)'))

B.append(slide('graphqljs17', 'GraphQL.js v17 (juni 2026)',
    row(
        col(h3('Stabiel', 38),
            ul(['Eerste grote versie sinds **oktober 2021**',
                '**`AbortSignal`**: requests afbreken; resolvers zien het via `info.getAbortSignal()`',
                '**`hideSuggestions`**: geen "Did you mean ...?" meer in foutmeldingen',
                '**`findSchemaChanges()`**: brekende, gevaarlijke en veilige schemawijzigingen in één keer',
                'Resolvers mogen **async iterables** teruggeven voor lijsten'], size=29)),
        col(h3('Experimenteel', 38),
            ul(['**Incremental delivery**: `@defer` en `@stream`',
                '**Foutpropagatie uitschakelen**: enkel het foute veld wordt `null`',
                '**Fragment-argumenten**: variabelen per fragment'], size=29)
            + p('*Experimenteel*: om feedback te verzamelen voordat het in de spec komt.', 27, '#595959'), gap=20), gap=48),
"""GraphQL.js is de referentie-implementatie van GraphQL in JavaScript. Vrijwel elke JavaScript-server, zoals Apollo Server en GraphQL Yoga, gebruikt ze onder de motorkap. Op 15 juni 2026 verscheen versie 17, de eerste grote versie sinds oktober 2021.

Links een paar stabiele nieuwigheden. AbortSignal: een request kan afgebroken worden, bijvoorbeeld als de gebruiker de pagina verlaat, en resolvers zien dat, zodat ze geen werk meer doen voor niemand. hideSuggestions: de foutmelding met Did you mean kan je uitzetten. Dat lijkt een detail, maar in trend 3 zien we dat het een securitymaatregel is. findSchemaChanges: vergelijkt twee versies van een schema en zegt welke wijzigingen brekend, gevaarlijk of veilig zijn. Handig in een CI-pipeline.

Rechts de experimentele functies, die nog niet in de specificatie staan maar wel al gebruikt kunnen worden om feedback te verzamelen. Incremental delivery met defer en stream, de volgende slide. Een manier om foutpropagatie uit te schakelen, zodat bij een fout enkel het foute veld null wordt. En fragment-argumenten: variabelen die per fragment meegegeven worden.""",
["GraphQL.js = referentie-implementatie in JS (onder Apollo Server, GraphQL Yoga, ...)",
 "v17 op 15/06/2026: eerste major sinds okt. 2021",
 "Stabiel: AbortSignal, hideSuggestions (security, trend 3), findSchemaChanges (CI), async iterables",
 "Experimenteel: @defer/@stream, foutpropagatie uitschakelen, fragment-argumenten",
 "→ Incremental delivery"],
bron='graphql.org/blog: Introducing GraphQL.js v17 (15/06/2026)'))

B.append(slide('kb-defer', 'Incremental delivery: @defer en @stream',
    row(
        col(code('''{
  allPersons(last: 1) {
    name
    ... @defer {
      posts { title }
    }
  }
}''', 'graphql', 27),
            ul(['Zonder `@defer` wacht het hele antwoord op het **traagste** veld',
                'Met `@defer`: eerst de snelle velden, **later** de rest',
                '`@stream`: elementen van een lijst komen binnen **zodra ze klaar zijn**'], size=29), gap=18, flex='0.95'),
        col(p('**Eerste antwoord**', 28), code('''{ "data": { "allPersons": [{ "name": "Bob" }] },
  "pending": [{ "id": "0", "path": ["allPersons", 0] }],
  "hasNext": true }''', 'json', 22),
            p('**Later**', 28), code('''{ "incremental": [{ "id": "0", "data": { "posts": [] } }],
  "completed": [{ "id": "0" }],
  "hasNext": false }''', 'json', 22),
            p('Status: **RFC**; experimenteel in GraphQL.js v17; al ondersteund door verschillende servers en clients.', 27, '#595959'), gap=12, flex='1.35'), gap=36),
"""Incremental delivery is een van de oudste voorstellen in GraphQL. Het probleem: sommige velden zijn traag, bijvoorbeeld aanbevelingen of statistieken. Zonder extra hulp wacht het hele antwoord op het traagste veld, en ziet de gebruiker niets tot alles klaar is.

Met de richtlijn defer op een fragment zeg je: dit deel mag later komen. In het voorbeeld vragen we de laatste persoon met de naam meteen, en de posts uitgesteld. Rechts zie je wat de server terugstuurt. Eerst een antwoord met de naam, met een lijst pending: er komt nog iets voor het pad allPersons, nul. En hasNext true: er volgt nog een bericht. Daarna een tweede bericht met incremental: de data voor dat uitgestelde deel, de posts, en completed: dat deel is klaar. hasNext is nu false.

De richtlijn stream doet iets gelijkaardigs voor lijsten: de elementen komen binnen zodra ze klaar zijn, in plaats van allemaal tegelijk.

Ik heb dit uitgevoerd met GraphQL.js 17, met de experimentele functie experimentalExecuteIncrementally: dit is het echte formaat. De status: het is nog een voorstel, een RFC, en experimenteel in GraphQL.js, maar verschillende servers en clients ondersteunen het al. Dit lijkt op het streamen van HTML in de les over web frameworks: eerst de shell, dan de trage delen.""",
["Probleem: antwoord wacht op het traagste veld",
 "@defer op fragment: dit deel later; @stream: lijstelementen zodra klaar",
 "Formaat: eerst data + pending + hasNext true; later incremental + completed + hasNext false (getest, GraphQL.js 17)",
 "Status: RFC, experimenteel in GraphQL.js v17, al in verschillende servers/clients",
 "Vergelijk: streaming HTML bij web frameworks (shell eerst, trage delen later)",
 "Examen: incremental delivery kunnen uitleggen",
 "→ Fouten en nullability"],
kern=True, bron='graphql.org/blog (GraphQL.js v17); eigen test met graphql-js 17.1.0'))

B.append(slide('nullability', 'Fouten en nullability: het null bubbling-probleem',
    row(
        col(ul(['Faalt een **non-null** veld, dan wordt de `null` doorgegeven naar de **ouder**, tot het eerste nullable veld',
                'Eén falend veld kan zo een **groot deel** van het antwoord wissen',
                'Daarom maken veel teams uit voorzorg **alles nullable**: het schema zegt dan weinig nog'], size=31)),
        col(card('Wat er onderweg is', '**Voorstellen** laten de client kiezen wat er bij een fout gebeurt (`onError`), bv. **enkel het foute veld** op `null` zetten. GraphQL.js v17 heeft een experimentele richtlijn `@experimental_disableErrorPropagation`.', size=30),
            code('''type User {
  name: String!
  avatar: String!  # faalt → User wordt null
}''', 'graphql', 24), gap=20), gap=44),
"""Een probleem waar de community al jaren mee worstelt: nullability. Herinner je de regel van daarnet: als een non-null veld faalt, mag het geen null zijn, dus wordt de null doorgegeven naar de ouder, en als die ook non-null is, naar diens ouder, enzovoort tot het eerste veld dat wel null mag zijn.

Rechtsonder een voorbeeld. Een User heeft een naam en een avatar, allebei non-null. Faalt de dienst die avatars levert, dan wordt de hele User null, ook al is de naam perfect beschikbaar. Als die User in een lijst zit die ook non-null is, kan zelfs de hele lijst verdwijnen. Eén falend veld kan zo een groot deel van het antwoord wissen.

Het gevolg in de praktijk: veel teams maken uit voorzorg alle velden nullable, zonder uitroepteken. Dan wist een fout enkel dat ene veld. Maar het schema zegt dan weinig nog: de client moet overal controleren op null, ook voor velden die in de praktijk nooit null zijn.

Wat is er onderweg? Voorstellen om de client te laten kiezen wat er bij een fout gebeurt, met een optie onError, bijvoorbeeld: zet enkel het foute veld op null en geef de fout mee in errors. GraphQL.js 17 heeft daar een experimentele richtlijn voor. Het is nog niet in de specificatie, maar het toont dat de standaard ook aan zijn oude problemen werkt.""",
["Non-null veld faalt → null gaat naar ouder tot eerste nullable veld (null bubbling)",
 "Voorbeeld: avatar faalt → hele User null; in non-null lijst kan alles verdwijnen",
 "Gevolg: teams maken alles nullable → schema zegt weinig, client moet overal op null controleren",
 "Onderweg: client kiest bij fout (onError), bv. enkel foute veld null; GraphQL.js 17: @experimental_disableErrorPropagation",
 "→ Een levende standaard"],
bron='graphql.org/blog: Introducing GraphQL.js v17 (15/06/2026)'))

B.append(slide('levend', 'Een levende standaard',
    tabel(['Wat', 'Status (november 2026)'],
          [['**GraphQL-specificatie**', 'Editie september 2025'],
           ['**GraphQL over HTTP**', 'Draft: requests, mediatypes (`application/graphql-response+json`), statuscodes'],
           ['**Composite Schemas** (federatie)', 'Draft, al geïmplementeerd door verschillende gateways (trend 2)'],
           ['**GAPs** (*GraphQL Auxiliary Proposals*)', 'Nieuw (juni 2026): community-specificaties **naast** de kernspec'],
           ['**Incremental delivery**, **onError**, fragment-argumenten', 'Voorstellen; experimenteel in GraphQL.js v17'],
           ['**GraphiQL 6**', 'Uitgebracht in november 2026']], [42, 58], size=29)
    + p('De standaard groeit in **lagen**: een kleine kernspec, met specificaties ernaast voor HTTP, federatie en meer.', 32, '#595959'),
"""Om trend 1 af te sluiten, een overzicht van de standaard in november 2026.

De kernspecificatie is de editie van september 2025. Daarnaast bestaat de specificatie GraphQL over HTTP, nog een draft. Die legt vast hoe je een GraphQL-request over HTTP stuurt, welk mediatype je gebruikt, en wat statuscodes betekenen. Composite Schemas, de standaard voor federatie, ook nog een draft, maar al geïmplementeerd: dat is trend 2. In juni 2026 kwam er een nieuw proces bij, GAPs, GraphQL Auxiliary Proposals: een plek voor specificaties die naast de kernspec staan, geschreven door de community. En de voorstellen zoals incremental delivery en onError zijn experimenteel beschikbaar in GraphQL.js 17. GraphiQL, de IDE in de browser, kreeg in november 2026 versie 6.

Het patroon is duidelijk: de kernspec blijft klein en stabiel, en nieuwe dingen komen in lagen ernaast. Dat is dezelfde aanpak als bij het web zelf, met een kern en vele aparte specificaties.""",
["Kernspec: editie sept. 2025",
 "GraphQL over HTTP: draft (mediatype, statuscodes)",
 "Composite Schemas: draft, al geïmplementeerd (trend 2)",
 "GAPs (juni 2026): community-specificaties naast de kernspec",
 "defer/stream, onError, fragment-argumenten: experimenteel in GraphQL.js 17; GraphiQL 6 (nov. 2026)",
 "Standaard groeit in lagen: kleine kern + aparte specs",
 "→ Trend 2: één graph voor de hele organisatie"],
bron='graphql.org/blog (GAPs 01/06/2026, GraphiQL 6 07/11/2026); graphql.github.io'))

# ======================= Trend 2 =======================
B.append(divider('div-2', 'Trend 2', 'Eén graph voor de hele organisatie',
    'Federatie en de Composite Schemas-specificatie',
"""Trend twee gaat over schaal. In een klein project heb je één GraphQL-server. Maar wat doe je in een bedrijf met honderd teams, die elk hun eigen dienst bouwen? Eén server voor iedereen wordt een flessenhals. Het antwoord heet federatie, en in 2025 en 2026 wordt het gestandaardiseerd.""",
["Trend 2: schaal",
 "Klein project: één server; bedrijf met 100 teams: één server = flessenhals",
 "Antwoord: federatie, nu gestandaardiseerd",
 "→ Wat is federatie?"]))

B.append(slide('kb-federatie', 'Federatie: subgraphs, router en supergraph',
    row(
        col(flow(card('Client', size=28),
                 rood('Router / gateway', 'plant de query over de subgraphs', size=28),
                 col(card('Subgraph *accounts*', size=26), card('Subgraph *reviews*', size=26), card('Subgraph *products*', size=26), gap=10, flex='1'), gap=16),
            ul(['Elk team bouwt een **subgraph**: een eigen GraphQL-service met een deel van het schema',
                'De **router** combineert ze tot één **supergraph**',
                'De client ziet **één API**; de router doet aan *query planning*'], size=29), gap=20, flex='1.25'),
        col(code('''# subgraph "accounts"
type User @key(fields: "id") {
  id: ID!
  name: String!
}

# subgraph "reviews"
type User @key(fields: "id") {
  id: ID!
  reviews: [Review!]!
}''', 'graphql', 25),
            p('Twee teams breiden hetzelfde type `User` uit, verbonden via de sleutel `id`.', 27, '#595959'), gap=14), gap=36),
"""Federatie werkt zo. Elk team bouwt een subgraph: een eigen GraphQL-service, met een deel van het totale schema. Het team accounts beheert de gebruikers, het team reviews de beoordelingen, het team products de producten. Bovenop draait een router, of gateway, die alle subgraphs combineert tot één groot schema: de supergraph.

De client ziet enkel die ene API. Stuurt hij een query die gebruikers en hun reviews vraagt, dan zoekt de router uit welke delen naar welke subgraph moeten, in welke volgorde, en voegt hij de antwoorden samen. Dat heet query planning.

Rechts het mooiste deel: entities. Het type User bestaat in twee subgraphs. Accounts weet de naam, reviews weet welke reviews een gebruiker schreef. Beide definiëren User met de richtlijn key op het veld id. Daardoor weet de router dat het om dezelfde gebruiker gaat, en kan hij in één antwoord de naam uit accounts en de reviews uit reviews samenvoegen. Geen team moet de code van het andere team kennen.

Dit is het antwoord op de belofte op de homepage van graphql.org: frictionless distributed development.""",
["Subgraph = eigen GraphQL-service per team met deel van het schema",
 "Router/gateway combineert tot één supergraph; client ziet één API; router doet query planning",
 "Entities: User in accounts (name) en reviews (reviews), verbonden via @key(fields: \"id\")",
 "Geen team moet de code van een ander kennen = 'frictionless distributed development'",
 "Examen: subgraph, router, supergraph kunnen uitleggen",
 "→ Van vendor-specifiek naar standaard"],
kern=True))

B.append(slide('composite', 'Van vendor-specifiek naar standaard',
    row(
        col(h3('Vandaag: elke leverancier een eigen variant', 34),
            ul(['**Apollo Federation** (de bekendste)', '**Hive Gateway** (The Guild, open source)', '**Grafbase**, **WunderGraph Cosmo**',
                '**Fusion** (ChilliCream, .NET)'], size=31)),
        col(h3('Composite Schemas Specification', 34),
            ul(['Gemeenschappelijke spec van de **Composite Schemas Working Group** van de GraphQL Foundation',
                'Richtlijnen zoals `@lookup` en `@key`',
                'Status: **draft**, maar al **geïmplementeerd** door verschillende gateways'], size=31)
            + card('GraphQLConf 2026', 'Federatie is geen experiment meer, maar "a set of well-worn paths" (Uri Goldshtein, The Guild).', size=28), gap=20), gap=48),
"""Federatie werd groot met Apollo Federation. Maar intussen heeft bijna elke leverancier een eigen variant: Hive Gateway van The Guild, open source, Grafbase, WunderGraph Cosmo, en Fusion van ChilliCream in de .NET-wereld. Ze lijken op elkaar, maar de richtlijnen en regels verschillen. Wie voor één leverancier kiest, zit er min of meer aan vast.

Daarom werkt een werkgroep van de GraphQL Foundation, de Composite Schemas Working Group, aan een gemeenschappelijke specificatie: de Composite Schemas Specification. Die definieert onder meer richtlijnen zoals lookup en key, die beschrijven hoe subgraphs samen één schema vormen. De spec is in november 2026 nog een draft, maar wordt al geïmplementeerd door verschillende gateways, onder meer Grafbase.

Op GraphQLConf 2026 zei Uri Goldshtein van The Guild in zijn keynote dat federatie geen experiment meer is, maar een set of well-worn paths: gekende, beproefde paden. Voor jullie betekent dat: als je in een groot bedrijf GraphQL tegenkomt, is de kans groot dat het een gefedereerde graph is.""",
["Vandaag: Apollo Federation, Hive Gateway (The Guild), Grafbase, WunderGraph Cosmo, Fusion (ChilliCream): elk eigen variant",
 "Composite Schemas Spec (GraphQL Foundation WG): gemeenschappelijke regels, bv. @lookup, @key",
 "Status: draft, maar al geïmplementeerd (o.a. Grafbase)",
 "GraphQLConf 2026: federatie = 'a set of well-worn paths' (Uri Goldshtein)",
 "→ Trend 3: security en performance"],
bron='graphql.github.io/composite-schemas-spec; GraphQLConf 2025 en 2026 (graphql.org/blog)'))

# ======================= Trend 3 =======================
B.append(divider('div-3', 'Trend 3', 'Security en performance in productie',
    'De flexibiliteit van GraphQL is ook zijn aanvalsoppervlak',
"""Trend drie: security en performance. De grootste kracht van GraphQL is dat de client zelf bepaalt wat hij vraagt. Dat is ook het grootste risico, want een aanvaller is ook een client. In 2025 en 2026 waren er verschillende kwetsbaarheden die precies daarmee te maken hadden.""",
["Trend 3: kracht = client bepaalt wat hij vraagt = ook risico (aanvaller is ook een client)",
 "2025–2026: kwetsbaarheden die daarmee te maken hebben",
 "→ Het aanvalsoppervlak"]))

B.append(slide('kb-aanval', 'Het aanvalsoppervlak van GraphQL',
    row(
        col(card('Diepe of dure queries (DoS)', 'Geneste relaties, honderden aliassen of recursieve fragmenten leggen de server plat.', size=30),
            code('''{ user(id: "1") { friends { friends { friends {
  friends { friends { name } } } } } } }''', 'graphql', 22),
            card('Batching voor brute force', 'Honderd `login`-mutations in **één request** omzeilen een rate limit per request.', size=30), gap=18),
        col(card('Informatielekken', 'Introspectie en *"Did you mean ...?"*-suggesties verraden het schema, ook interne velden.', size=30),
            code('Cannot query field "nam" on type "Person". Did you mean "name"?', 'bash', 22),
            card('Autorisatie per veld', 'Eén endpoint: je kan niet per URL beveiligen. **Elke resolver** moet controleren of de gebruiker de data mag zien.', size=30), gap=18), gap=40),
"""Wat is er anders aan de beveiliging van een GraphQL-API? Vier risico's.

Eén: diepe of dure queries. Omdat de client relaties kan volgen, kan hij ook een query sturen zoals de code linksboven: de vrienden van de vrienden van de vrienden, vijf niveaus diep. Bij honderd vrienden per persoon is dat tien miljard objecten. Ook honderden aliassen voor hetzelfde dure veld, of fragmenten die naar elkaar verwijzen, kunnen een server platleggen. Dat is een denial-of-service-aanval met één enkele request.

Twee: batching voor brute force. Een rate limit van tien requests per minuut lijkt veilig voor een login. Maar met aliassen kan je honderd login-mutations in één request steken, elk met een ander wachtwoord.

Drie: informatielekken. Introspectie toont het volledige schema, inclusief interne velden. En zelfs als je introspectie uitzet, verraden de suggesties in foutmeldingen veel. Rechts zie je de echte foutmelding van onze testserver voor een tikfout: Did you mean name. Met tools die systematisch woorden proberen, kan een aanvaller zo het schema reconstrueren.

Vier: autorisatie. Bij REST kan je per URL beveiligen: slash admin enkel voor beheerders. Bij GraphQL is er één endpoint, dus moet elke resolver zelf controleren of de gebruiker de gevraagde data mag zien.""",
["DoS: diepe nesting (vrienden van vrienden ... → miljarden objecten), aliassen, recursieve fragmenten",
 "Brute force: 100 login-mutations via aliassen in 1 request omzeilen rate limit per request",
 "Lekken: introspectie + 'Did you mean ...?' (echte melding testserver) → schema reconstrueerbaar",
 "Autorisatie: één endpoint → elke resolver controleert zelf",
 "Examen: de vier risico's kunnen benoemen en uitleggen",
 "→ Echte incidenten"],
kern=True))

B.append(slide('cves', 'Echte incidenten (2025–2026)',
    tabel(['CVE', 'Product', 'Wat', 'Risico'],
          [['**CVE-2025-32032** (april 2025)', 'Apollo Router', 'Diep geneste, hergebruikte fragmenten maakten **query planning** extreem duur', 'DoS'],
           ['**CVE-2025-53364** (juli 2025)', 'Parse Server', 'Het GraphQL-**schema** was opvraagbaar zonder sessie of sleutel', 'Informatielek'],
           ['**CVE-2026-40324** (april 2026)', 'Hot Chocolate (.NET)', 'Parser zonder **recursielimiet**: een document van ±40 KB crasht het hele proces', 'DoS']],
          [24, 18, 44, 14], size=28)
    + p('Telkens hetzelfde patroon: de server vertrouwt **de vorm van de query** te veel. Twee van de drie zijn **DoS via nesting**.', 32, '#C00000'),
"""Drie echte incidenten uit de afgelopen anderhalf jaar.

CVE-2025-32032, april 2025, in de Apollo Router, de gateway voor federatie. Queries met diep geneste en hergebruikte fragmenten maakten de query planning, het uitrekenen van hoe de query over de subgraphs verdeeld wordt, extreem duur. Eén kwaadaardige query kon de router laten vastlopen.

CVE-2025-53364, juli 2025, in Parse Server, een populaire open source backend. Het GraphQL-schema kon opgevraagd worden zonder sessie of sleutel. Dat lekt geen data, maar wel de volledige structuur, en dat maakt het aanvalsoppervlak groter.

CVE-2026-40324, april 2026, in Hot Chocolate, de bekendste GraphQL-server voor .NET. De parser, het stuk dat de tekst van de query leest, had geen limiet op het aantal geneste niveaus. Een document van ongeveer 40 kilobyte, met veel geneste haakjes, veroorzaakte een stack overflow, en die kan je in .NET niet opvangen: het hele serverproces crashte.

Het patroon: telkens vertrouwt de server de vorm van de query te veel. En twee van de drie zijn denial of service via nesting. Dat brengt ons bij de verdediging.""",
["CVE-2025-32032 (Apollo Router): geneste fragmenten → dure query planning → DoS",
 "CVE-2025-53364 (Parse Server): schema opvraagbaar zonder sessie/sleutel → informatielek",
 "CVE-2026-40324 (Hot Chocolate): parser zonder recursielimiet, ±40 KB → proces crasht",
 "Patroon: server vertrouwt de vorm van de query te veel; 2 van 3 = DoS via nesting",
 "→ Hoe verdedig je je?"],
bron='OSV / GitHub Security Advisories (CVE-2025-32032, CVE-2025-53364, CVE-2026-40324)'))

B.append(slide('kb-verdediging', 'Verdediging: limieten, trusted documents en autorisatie',
    row(
        col(ul(['**Diepte- en kostenlimieten**: maximale nesting en een *cost analysis* die elke query een prijs geeft',
                '**Trusted documents** (persisted operations): enkel **vooraf geregistreerde** queries, verstuurd als **hash**',
                '**Introspectie en suggesties uit** voor publieke clients (`hideSuggestions`): helpt, maar is *security through obscurity*',
                '**Autorisatie in de resolvers** (of met richtlijnen zoals `@policy`)',
                '**Rate limiting per operatie**, niet per request; **tijdig updaten**'], size=29)),
        col(p('**Trusted document**: de client stuurt geen vrije query', 29),
            code('''POST /graphql
{
  "documentId": "sha256:7f3a...e91c",
  "variables": { "id": "1" }
}''', 'json', 25),
            p('Ideaal voor **eigen apps**; voor publieke API\'s met externe clients niet mogelijk.', 28, '#595959'), gap=14), gap=40),
"""Hoe verdedig je een GraphQL-API? Vijf maatregelen, die je combineert.

Eén: diepte- en kostenlimieten. Je legt een maximale nestingdiepte vast, bijvoorbeeld tien niveaus. Beter is een cost analysis: elk veld krijgt een kost, lijsten tellen mee met hun lengte, en een query die boven een budget uitkomt, wordt geweigerd voordat ze uitgevoerd wordt.

Twee: trusted documents, ook persisted operations genoemd. Bij het bouwen van je app registreer je alle queries die de app gebruikt op de server. In productie stuurt de client geen vrije query meer, maar enkel de hash van de query en de variabelen, zoals rechts. De server voert enkel queries uit die hij kent. Een aanvaller kan dan geen eigen dure query sturen. Dat werkt voor je eigen apps, maar niet voor een publieke API waar externe ontwikkelaars eigen queries schrijven. Merk op dat dit enkel kan omdat variabelen apart meegestuurd worden: de tekst van de query blijft vast.

Drie: introspectie en suggesties uitschakelen voor publieke clients, met hideSuggestions uit GraphQL.js 17. Dat helpt, maar het is security through obscurity: het schema verbergen maakt een aanval moeilijker, niet onmogelijk.

Vier: autorisatie in de resolvers, of met richtlijnen in het schema zoals policy. En vijf: rate limiting per operatie in plaats van per request, en tijdig updaten van je server, gateway en parser.""",
["Diepte- en kostenlimieten: max nesting, cost analysis (budget per query)",
 "Trusted documents: enkel vooraf geregistreerde queries via hash + variabelen; eigen apps ja, publieke API niet",
 "Introspectie/suggesties uit (hideSuggestions): helpt, maar security through obscurity",
 "Autorisatie in resolvers (of @policy); rate limiting per operatie; updaten",
 "Examen: trusted documents en cost analysis kunnen uitleggen",
 "→ Performance: caching"],
kern=True, bron='graphql.org/learn/security'))

B.append(slide('caching', 'Performance: caching zonder URL\'s',
    row(
        col(rood('Het probleem', size=32),
            ul(['REST: elke **URL** is een resource → **HTTP-caching** en CDN\'s werken vanzelf',
                'GraphQL: alles via `POST /graphql` → een CDN kan **niets cachen**'], size=31)),
        col(groen('De oplossingen', size=32),
            ul(['Queries via **GET** met de **hash** van een trusted document: cachebaar per URL',
                '**Caching per veld** of per object op de server',
                '**Genormaliseerde cache** in de client (Apollo, Relay): objecten bewaard op `__typename` + `id`, zodat een mutation alle schermen bijwerkt'], size=31)), gap=48),
"""Een laatste onderwerp van trend 3: performance, en dan vooral caching. Bij REST is caching bijna gratis: elke URL is een resource, en HTTP heeft caching ingebouwd. Een CDN kan het antwoord van GET slash users slash 3 een uur bewaren, zonder dat de server iets moet doen.

Bij GraphQL gaat alles via een POST naar één endpoint. Een CDN cachet geen POST-requests, en zelfs als het dat zou doen, heeft elke query een andere vorm. Dat is een echt nadeel van GraphQL.

De oplossingen. Eén: stuur queries via GET, met de hash van een trusted document en de variabelen in de URL. Dan heeft elke query wel een eigen URL en kan een CDN ze cachen. Twee: caching aan de serverkant, per veld of per object, bijvoorbeeld het resultaat van een dure resolver. En drie: een genormaliseerde cache in de client. Apollo Client en Relay bewaren elk object één keer, op basis van zijn type en id. Wijzig je met een mutation de naam van een persoon, dan wordt die naam automatisch bijgewerkt op elk scherm waar die persoon voorkomt. Daarom is het een goede gewoonte om in mutations het id en de gewijzigde velden terug te vragen.""",
["REST: elke URL = resource → HTTP-caching en CDN gratis",
 "GraphQL: alles POST /graphql → CDN cachet niets (echt nadeel)",
 "Oplossingen: GET met hash van trusted document (cachebaar), caching per veld/object op server",
 "Genormaliseerde client-cache (Apollo, Relay): object op __typename + id → mutation werkt alle schermen bij",
 "Tip: in mutations id + gewijzigde velden terugvragen",
 "→ Trend 4: de API-taal voor agents"]))

# ======================= Trend 4 =======================
B.append(divider('div-4', 'Trend 4', 'De API-taal voor agents',
    '"The API language for humans and agents": wat zit erachter?',
"""We komen bij de slogan van het begin: the API language for humans and agents. In 2025 en 2026 positioneert de GraphQL-community zich nadrukkelijk als de taal waarmee AI-agents API's gebruiken. Er kwam een AI-werkgroep, een server die GraphQL-API's beschikbaar maakt voor agents, en de conferentie van 2026 had als thema de taal van AI. We bekijken waarom dat werkt, hoe het werkt, en waar je kritisch moet blijven.""",
["Terug naar de slogan: 'The API language for humans and agents'",
 "2025–2026: AI-werkgroep, MCP-servers, GraphQLConf 2026 'the language of AI'",
 "Waarom, hoe, en waar kritisch blijven",
 "→ Waarom passen GraphQL en agents bij elkaar?"]))

B.append(slide('kb-agents', 'Waarom GraphQL en agents goed samengaan',
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px 40px">'
    + card('Zelfbeschrijvend', 'Via **introspectie** ontdekt de agent types, velden en relaties, en leest hij de **descriptions** als documentatie.', size=31)
    + card('Gevalideerd', 'Een fout veld geeft geen 200 met rommel, maar een **duidelijke fout** die de agent kan corrigeren.', size=31)
    + card('Precies', 'De agent vraagt **enkel de velden** die hij nodig heeft: dat spaart **context** (tokens).', size=31)
    + card('Samenstelbaar', 'Eén query volgt **relaties** over meerdere types, in plaats van meerdere endpoints te combineren.', size=31)
    + '</div>'
    + code('''"""Een product in de catalogus."""
type Product {
  """Prijs in eurocent."""
  price: Int!
}''', 'graphql', 24),
"""Waarom zou GraphQL goed passen bij AI-agents? Een agent, zoals we zagen in de les over web frameworks, is een taalmodel dat zelf stappen plant en tools gebruikt. Als zo'n agent een API moet gebruiken die hij niet kent, heeft hij vier dingen nodig, en GraphQL biedt ze alle vier.

Eén: zelfbeschrijvend. Via introspectie ontdekt de agent welke types, velden, argumenten en relaties er zijn. En de descriptions in het schema, zoals onderaan, dienen als documentatie. Hier staat dat de prijs in eurocent is: een agent die dat weet, zal geen prijs van 1999 euro tonen voor een product van 19,99. Geen aparte handleiding nodig.

Twee: gevalideerd. Verzint de agent een veld dat niet bestaat, dan krijgt hij geen antwoord met verkeerde data, maar een duidelijke validatiefout, zoals de Did you mean-melding die we zagen. Daarmee kan hij zichzelf corrigeren. Hier zie je het dubbele gezicht van die suggesties: nuttig voor agents, riskant voor security.

Drie: precies. De agent vraagt enkel de velden die hij nodig heeft. Bij een taalmodel telt elk woord in de context: het kost geld, en te veel irrelevante data maakt de antwoorden slechter.

Vier: samenstelbaar. Eén query kan relaties volgen over meerdere types. Bij REST moet een agent meerdere endpoints aanroepen en de resultaten zelf combineren, met meer kans op fouten.""",
["Agent = taalmodel dat zelf plant en tools gebruikt (zie les web frameworks)",
 "Zelfbeschrijvend: introspectie + descriptions als documentatie (prijs in eurocent)",
 "Gevalideerd: verzonnen veld → duidelijke fout (Did you mean ...) → zelfcorrectie (dubbel gezicht met security)",
 "Precies: enkel nodige velden → minder context/tokens",
 "Samenstelbaar: één query volgt relaties i.p.v. endpoints combineren",
 "Examen: vier redenen waarom GraphQL bij agents past",
 "→ Hoe gebruikt een agent zo'n API?"],
kern=True, bron='graphql.org/ai'))

B.append(slide('agent-flow', 'Hoe een agent een GraphQL-API gebruikt',
    flow(card('1. Taak', '"Toon de omzet per regio voor de top 5 categorieën in Q4."', size=28),
         card('2. Introspectie', 'Ontdekt `Product`, `Order`, `RevenueMetrics`, `Region`.', size=28),
         card('3. Query samenstellen', 'Het model zet de vraag om in **één** precieze query.', size=28),
         card('4. Gestructureerde JSON', 'In de vorm van de query; fouten in `errors` met een `path`.', size=28))
    + code('''query RevenueQ4 {
  orders(from: "2026-10-01", to: "2026-12-31") {
    product { category { name } }
    revenue { region { name } amount }
  }
}''', 'graphql', 26),
"""Hoe gaat dat concreet? graphql.org beschrijft het in vier stappen.

Eén: de agent krijgt een taak, bijvoorbeeld van een gebruiker: toon de omzet per regio voor de top vijf categorieën in het vierde kwartaal.

Twee: de agent doet introspectie op de API en ontdekt welke types er zijn: Product, Order, RevenueMetrics, Region. Hij leest de descriptions om te begrijpen wat de velden betekenen.

Drie: het taalmodel zet de vraag om in één precieze query, zoals onderaan: alle orders van het vierde kwartaal, met de categorie van het product en de omzet per regio. Is de query ongeldig, dan krijgt hij een validatiefout en probeert hij opnieuw.

Vier: de agent krijgt gestructureerde JSON terug, in exact de vorm van zijn query. Faalt een deel, dan staat in errors welk veld, met het path, en kan de agent met de gedeeltelijke resultaten verder.

Merk op dat de agent in deze aanpak zelf queries schrijft. Dat is flexibel, maar ook riskant: hij kan een dure query schrijven, of data opvragen die hij niet nodig heeft. Daarom bestaat er ook een andere aanpak, op de volgende slide.""",
["1. Taak (omzet per regio, top 5 categorieën, Q4)",
 "2. Introspectie: Product, Order, RevenueMetrics, Region + descriptions",
 "3. Model stelt één query samen; ongeldig → validatiefout → opnieuw",
 "4. JSON in vorm van de query; fouten met path; verder met gedeeltelijke resultaten",
 "Agent schrijft zelf queries: flexibel maar riskant (dure queries)",
 "→ MCP"],
bron='graphql.org/ai'))

B.append(slide('mcp', 'GraphQL en MCP',
    row(
        col(p('Het **Model Context Protocol** (MCP) is de standaard waarmee agents **tools** aanroepen (zie les web frameworks).', 31),
            ul(['**Apollo MCP Server** (1.0, oktober 2025, open source): GraphQL-operaties worden **MCP-tools**, zonder extra code',
                'Optioneel: de agent kan zelf het schema **introspecteren en doorzoeken**',
                'Ondersteunt **OAuth 2.1** (MCP-autorisatie) en OpenTelemetry'], size=30), gap=16),
        col(tabel(['Strategie', 'Voor', 'Tegen'],
                  [['**Volledig schema**: agent schrijft zelf queries', 'Flexibel', 'Grote context, dure of riskante queries'],
                   ['**Gecureerde operaties** als tools', 'Veilig, zuinig, voorspelbaar', 'Minder flexibel']], [36, 28, 36], size=27)
            + p('Apollo meldt voor gecureerde operaties ±40% minder schemacontext en 40–75% minder tool-aanroepen: **cijfers van de leverancier zelf**.', 27, '#595959'), gap=16), gap=40),
"""Agents roepen tools aan via het Model Context Protocol, MCP, dat we in de les over web frameworks zagen. Hoe koppel je een GraphQL-API daaraan?

De bekendste oplossing is de Apollo MCP Server, die in oktober 2025 versie 1.0 bereikte en open source is. Hij maakt van GraphQL-operaties MCP-tools, zonder dat je extra code moet schrijven. Elke operatie wordt een tool, met de variabelen van de query als parameters en de description als uitleg. Optioneel kan de agent ook zelf het schema introspecteren en doorzoeken. En er is ondersteuning voor OAuth 2.1, zodat de agent enkel kan wat de gebruiker mag.

Er zijn dus twee strategieën. Je geeft de agent het volledige schema en laat hem zelf queries schrijven. Dat is flexibel, maar een groot schema neemt veel context in, en de agent kan dure of riskante queries schrijven. Of je geeft hem een gecureerde set operaties als tools: een beperkte lijst van vooraf geschreven queries. Dat is veilig, zuinig en voorspelbaar, maar minder flexibel. Merk op dat dit hetzelfde idee is als trusted documents uit trend 3.

Apollo meldt dat de gecureerde aanpak ongeveer 40 procent minder schemacontext en 40 tot 75 procent minder tool-aanroepen geeft. Maar dat zijn cijfers van de leverancier zelf, geen onafhankelijke meting. graphql.org zegt dat ook expliciet.""",
["MCP = standaard waarmee agents tools aanroepen (les web frameworks)",
 "Apollo MCP Server 1.0 (okt. 2025, open source): operaties → MCP-tools; optioneel introspectie/zoeken; OAuth 2.1",
 "Strategie 1: volledig schema, agent schrijft queries (flexibel, grote context, riskant)",
 "Strategie 2: gecureerde operaties als tools (veilig, zuinig) = idee van trusted documents",
 "Apollo: ±40% minder context, 40–75% minder tool-calls: cijfers van de leverancier",
 "→ Wat doet de community?"],
bron='apollographql.com (Apollo MCP Server 1.0, 07/10/2025); graphql.org/ai'))

B.append(slide('ai-community', 'De community gaat mee',
    row(
        col(card('GraphQL AI Working Group (sinds oktober 2025)', size=30),
            ul(['**Semantic introspection**: betekenis en verbanden in het schema, zodat een agent de **relevante delen** van een groot schema vindt',
                '**`@mock`**-richtlijn: voorgedefinieerde antwoorden voor prototypes en tests',
                '**Embeddings** van schema\'s, ook met kleine lokale modellen'], size=29), gap=14),
        col(card('GraphQLConf 2026 (mei, Fremont)', size=30),
            ul(['Dominant thema: AI. Afsluiter Matt DeBergalis (Apollo): GraphQL *"can and must be the language of AI"*',
                'Talks van **Meta**, **Netflix**, **IBM**, **Starbucks**, **Wayfair**, ... over agents en MCP',
                'De spec-editie 2025 voegde **descriptions op operaties** toe, mee voor AI-tooling'], size=29), gap=14), gap=44),
"""De GraphQL-community gaat hier volop in mee. In oktober 2025 startte de GraphQL AI Working Group. Die werkt aan drie dingen. Semantic introspection: een uitbreiding van introspectie die niet alleen zegt welke velden er zijn, maar ook wat ze betekenen en hoe ze samenhangen, zodat een agent in een schema met tienduizenden velden de relevante delen vindt. Een mock-richtlijn: een standaard manier om voorgedefinieerde antwoorden te geven, handig voor prototypes en tests, ook voor agents die code schrijven. En embeddings van schema's: wiskundige representaties van types en velden, waarmee een agent snel het juiste veld vindt. Een prototype werkte met een klein lokaal model op acht gigabyte geheugen.

Op GraphQLConf 2026, in mei in Fremont in Californië, was AI het dominante thema. Matt DeBergalis, de CEO van Apollo, sloot af met de uitspraak dat GraphQL de taal van AI kan en moet zijn. Er waren talks van onder meer Meta, Netflix, IBM, Starbucks en Wayfair over agents en MCP.

En ook de spec-editie van 2025 voegde descriptions op operaties toe, mee met het oog op AI-tooling.""",
["AI Working Group (okt. 2025): semantic introspection (relevante delen van groot schema), @mock, embeddings van schema's (klein lokaal model, 8 GB)",
 "GraphQLConf 2026 (mei, Fremont): AI dominant; Matt DeBergalis: 'can and must be the language of AI'",
 "Talks van Meta, Netflix, IBM, Starbucks, Wayfair over agents en MCP",
 "Spec 2025: descriptions op operaties, mee voor AI-tooling",
 "→ Maar: blijf kritisch"],
bron='graphql.org/blog: AI WG (14/10/2025, 22/01/2026); GraphQLConf 2026 wrap-up (14/07/2026)'))

B.append(slide('kritisch', 'Blijf kritisch',
    ul(['**Grote schema\'s passen niet in een context window**: tienduizenden velden moet je filteren of doorzoekbaar maken',
        '**Agents schrijven dure queries**: kostenlimieten en trusted documents (trend 3) zijn nog belangrijker',
        '**Prompt injection** blijft een risico: data uit de API kan instructies bevatten (les web frameworks)',
        '**REST is soms eenvoudiger**: volgens graphql.org zelf is een taak die op één endpoint past, met REST simpeler',
        '**Cijfers van leveranciers** zijn geen onafhankelijke benchmarks; de AI Working Group vraagt zelf om reproduceerbare metingen',
        'De slogan komt van de **GraphQL-community zelf**: ze heeft er belang bij'], size=35),
"""Tot slot van deze trend: blijf kritisch. Zes kanttekeningen.

Eén: grote schema's passen niet in een context window. Het schema van een groot bedrijf heeft tienduizenden velden. Dat kan je niet zomaar aan een taalmodel geven; je moet filteren, zoeken of gecureerde operaties gebruiken. Daar werkt de AI-werkgroep net aan.

Twee: agents schrijven dure queries. Een agent die vrij queries mag schrijven, kan per ongeluk precies de diepe query van trend 3 schrijven. Kostenlimieten en trusted documents zijn bij agents nog belangrijker.

Drie: prompt injection blijft een risico. Data die uit de API komt, zoals een productbeschrijving, kan tekst bevatten die het model als instructie leest. GraphQL lost dat niet op.

Vier: REST is soms eenvoudiger. graphql.org zegt zelf dat een taak die op één goed ontworpen endpoint past, met REST simpeler is.

Vijf: veel cijfers komen van leveranciers. De AI-werkgroep vraagt zelf om reproduceerbare metingen.

En zes: de slogan the API language for humans and agents komt van de GraphQL-community zelf, en die heeft er belang bij dat GraphQL populair blijft. Dat maakt het niet onwaar, maar het is een reden om zelf te oordelen. Dat kan je nu: je kent de begrippen.""",
["Grote schema's passen niet in context window → filteren/zoeken/gecureerde operaties",
 "Agents schrijven dure queries → kostenlimieten en trusted documents nog belangrijker",
 "Prompt injection: API-data kan instructies bevatten (les web frameworks)",
 "REST soms eenvoudiger (graphql.org geeft dat zelf toe)",
 "Leverancierscijfers ≠ onafhankelijke benchmark; slogan komt van de community zelf",
 "→ Wanneer kies je GraphQL?"],
bron='graphql.org/ai'))

# ======================= Afsluiting =======================
B.append(slide('wanneer', 'Wanneer GraphQL, wanneer REST?',
    tabel(['Situatie', 'Keuze'],
          [['Veel verschillende clients (web, mobiel) met andere databehoeften', '**GraphQL**'],
           ['Snel veranderende UI, productgedreven ontwikkeling', '**GraphQL**'],
           ['Veel backends samenbrengen achter één API, veel teams', '**GraphQL** (met federatie)'],
           ['API voor AI-agents die zelf moeten verkennen', '**GraphQL** (of gecureerde MCP-tools)'],
           ['Eenvoudige CRUD-API, weinig clients', '**REST**'],
           ['Publieke API waar HTTP-caching cruciaal is', '**REST**'],
           ['Bestanden uploaden en downloaden, streaming media', '**REST**'],
           ['Snelle interne communicatie tussen services', '**gRPC**']], [66, 34], size=30)
    + p('Geen religie: veel bedrijven gebruiken **beide**.', 33, '#595959'),
"""Wanneer kies je nu GraphQL, en wanneer REST? Een vuistregeloverzicht.

GraphQL is een goede keuze als je veel verschillende clients hebt met verschillende databehoeften, zoals een website en mobiele apps. Als je gebruikersinterface snel verandert. Als je veel backends en teams achter één API wil samenbrengen, met federatie. En als je een API bouwt die AI-agents zelf moeten kunnen verkennen, of je biedt ze gecureerde operaties via MCP.

REST is de betere keuze voor een eenvoudige CRUD-API met weinig clients: dan is GraphQL extra complexiteit zonder veel winst. Voor een publieke API waar HTTP-caching via CDN's cruciaal is. En voor het uploaden en downloaden van bestanden of het streamen van media: GraphQL is gemaakt voor gestructureerde data, niet voor grote binaire bestanden.

En voor snelle interne communicatie tussen services kies je vaak gRPC, een binair protocol van Google.

Het belangrijkste staat onderaan: het is geen religie. Veel bedrijven gebruiken beide, bijvoorbeeld GraphQL voor hun apps en REST voor publieke integraties en webhooks.""",
["GraphQL: veel clients, snel veranderende UI, veel backends/teams (federatie), API voor agents",
 "REST: eenvoudige CRUD, HTTP-caching cruciaal, bestanden/media",
 "gRPC: snelle interne communicatie tussen services",
 "Geen religie: veel bedrijven gebruiken beide",
 "Examen: een keuze tussen GraphQL en REST kunnen beargumenteren",
 "→ Wat kan je er zelf mee?"],
kern=True))

B.append(slide('studenten', 'Wat kan je er zelf mee?',
    ul(['Speel met een publieke API in **GraphiQL**: de Star Wars-API op graphql.org of de **GitHub GraphQL-API**',
        'Bouw een kleine server met **GraphQL.js**, Apollo Server of GraphQL Yoga, en **meet** het N+1-probleem met en zonder **DataLoader**',
        'Genereer je TypeScript-types met **GraphQL Code Generator** of gql.tada',
        'Zet in productie **diepte- en kostenlimieten**, **trusted documents** en **autorisatie per veld**',
        'Schrijf **descriptions** in je schema: voor je collega\'s én voor agents'], size=38)
    + spacer()
    + p('Het schema is het hart: wie het goed ontwerpt, krijgt validatie, documentatie, tooling en agent-ondersteuning **gratis**.', 34, '#595959'),
"""Wat kan je er zelf mee? Vijf tips.

Eén: speel met een publieke API in GraphiQL. Op graphql.org staat een Star Wars-API, en GitHub heeft een publieke GraphQL-API waarmee je je eigen repositories kan bevragen. Gebruik de autocomplete en de documentatie die uit introspectie komt.

Twee: bouw een kleine server met GraphQL.js, Apollo Server of GraphQL Yoga, en meet het N+1-probleem met en zonder DataLoader. Tel het aantal databank-aanroepen. Zo zie je met eigen ogen waarom DataLoader bestaat.

Drie: genereer je TypeScript-types met GraphQL Code Generator of gql.tada, in plaats van ze met de hand te schrijven.

Vier: als je ooit een GraphQL-API in productie zet, denk dan aan diepte- en kostenlimieten, trusted documents voor je eigen apps en autorisatie per veld.

En vijf: schrijf descriptions in je schema. Voor je collega's, en voor de agents die je API misschien ooit gaan gebruiken.

De rode draad: het schema is het hart van GraphQL. Wie het goed ontwerpt, krijgt validatie, documentatie, tooling en ondersteuning voor agents er gratis bij.""",
["GraphiQL: Star Wars-API op graphql.org, GitHub GraphQL-API",
 "Kleine server (GraphQL.js, Apollo Server, Yoga) + N+1 meten met/zonder DataLoader",
 "Types genereren (GraphQL Code Generator, gql.tada)",
 "Productie: diepte/kostenlimieten, trusted documents, autorisatie per veld",
 "Descriptions schrijven: voor collega's én agents",
 "Schema = hart: validatie, documentatie, tooling, agents gratis",
 "→ Begrippenlijst"]))

B.append(slide('begrippen-1', 'Begrippenlijst (1/2): de basis',
    grid2(['**GraphQL**: querytaal voor API\'s en runtime die queries uitvoert tegen een getypeerd schema',
           '**REST**: architectuurstijl met resources per URL en HTTP-methodes',
           '**Overfetching**: meer data ontvangen dan nodig',
           '**Underfetching**: te weinig per request, waardoor extra requests nodig zijn',
           '**N+1-probleem**: 1 request/query voor een lijst + N extra voor de details',
           '**Schema**: verzameling types en velden, het contract tussen client en server',
           '**SDL**: Schema Definition Language, de notatie voor een schema',
           '**Non-null (`!`)**: veld dat nooit `null` is',
           '**Query / Mutation / Subscription**: lezen / wijzigen / realtime stroom',
           '**Root types**: `Query`, `Mutation`, `Subscription`, de ingangspunten',
           '**Variabele, alias, fragment**: apart meegestuurde waarde / andere naam / herbruikbare selectie',
           '**Introspectie**: het schema opvragen met een query (`__schema`, `__type`)',
           '**Resolver**: functie die de data voor één veld ophaalt',
           '**DataLoader**: bundelt resolver-aanroepen (batching) tegen het N+1-probleem'], size=26),
"""De eerste helft van de begrippenlijst: de basis. Je moet deze begrippen kunnen definiëren en met een voorbeeld uitleggen. Let vooral op de begrippen die samenhangen: over- en underfetching en het N+1-probleem, dat op de server terugkomt bij resolvers en DataLoader; het schema, de SDL en de root types; en variabelen, aliassen en fragmenten.""",
["Basis: GraphQL, REST, over-/underfetching, N+1, schema, SDL, non-null",
 "Query/Mutation/Subscription, root types, variabele/alias/fragment, introspectie",
 "Resolver, DataLoader",
 "Examen: definitie + voorbeeld kunnen geven"]))

B.append(slide('begrippen-2', 'Begrippenlijst (2/2): client en trends',
    grid2(['**Declaratieve data fetching**: beschrijven welke data je nodig hebt, de client-bibliotheek doet de rest',
           '**Fragment colocation**: elk component declareert zijn data-behoefte als fragment naast zijn code',
           '**Codegeneratie**: types genereren uit schema en queries',
           '**@oneOf**: input waarvan precies één veld ingevuld moet zijn',
           '**@defer / @stream**: incremental delivery, delen van het antwoord later sturen',
           '**Null bubbling**: een fout in een non-null veld maakt de ouder `null`',
           '**Federatie**: subgraphs van teams samengevoegd tot één supergraph achter een router',
           '**Cost analysis**: elke query krijgt een kost; te dure queries worden geweigerd',
           '**Trusted documents**: enkel vooraf geregistreerde queries (via hash) worden uitgevoerd',
           '**Genormaliseerde cache**: client bewaart elk object één keer op type + `id`',
           '**MCP**: Model Context Protocol, standaard waarmee AI-agents tools aanroepen',
           '**Semantic introspection**: voorstel om betekenis en verbanden aan introspectie toe te voegen'], size=26),
"""De tweede helft gaat over de client en de trends. Declaratieve data fetching, fragment colocation en codegeneratie horen bij de client. OneOf, defer en stream en null bubbling bij de standaard. Federatie bij trend 2. Cost analysis, trusted documents en de genormaliseerde cache bij trend 3. En MCP en semantic introspection bij de agents.

Kan je een begrip niet uitleggen, ga dan terug naar de slide met het label Kernbegrip, of naar de cursustekst.""",
["Client: declaratief, fragment colocation, codegeneratie",
 "Standaard: @oneOf, @defer/@stream, null bubbling",
 "Federatie; security: cost analysis, trusted documents; genormaliseerde cache",
 "Agents: MCP, semantic introspection",
 "Examen: definitie + voorbeeld kunnen geven"]))

B.append(slide('conclusie', 'Conclusie',
    ul(['**GraphQL laat de client kiezen**: exact de data die hij nodig heeft, in één request',
        '**Het schema is het hart**: contract, documentatie, validatie en tooling',
        '**De server werkt met resolvers**; zonder DataLoader krijg je N+1 op de server',
        '**De standaard beweegt weer**: spec-editie 2025, GraphQL.js v17, `@defer`/`@stream` onderweg',
        '**Federatie** maakt één graph voor een hele organisatie',
        '**Flexibiliteit is aanvalsoppervlak**: limieten, trusted documents, autorisatie per veld',
        '**"The API language for humans and agents"**: sterk voor agents, maar REST blijft juist voor eenvoudige API\'s'], size=36, ordered=True)
    + spacer()
    + p('Ontwerp je schema goed: voor mensen én voor agents.', 42, '#595959'),
"""Tot slot de conclusie. Zeven punten.

Eén: GraphQL laat de client kiezen. Hij vraagt exact de data die hij nodig heeft, in één request. Twee: het schema is het hart: het is het contract, de documentatie en de basis voor validatie en tooling. Drie: de server werkt met resolvers, één functie per veld, en zonder DataLoader verhuist het N+1-probleem naar de server.

Vier: de standaard beweegt weer, met de spec-editie van 2025, GraphQL.js versie 17 en incremental delivery onderweg. Vijf: federatie maakt één graph voor een hele organisatie, en wordt gestandaardiseerd. Zes: de flexibiliteit van GraphQL is ook zijn aanvalsoppervlak: zet limieten, gebruik trusted documents en autoriseer per veld.

En zeven: the API language for humans and agents. Introspectie, typering en precieze queries maken GraphQL sterk voor AI-agents. Maar REST blijft de juiste keuze voor eenvoudige API's.

De kern: ontwerp je schema goed, voor mensen én voor agents. Bedankt voor jullie aandacht.""",
["1. Client kiest exact de data, in één request",
 "2. Schema = hart: contract, documentatie, validatie, tooling",
 "3. Resolvers per veld; zonder DataLoader N+1 op de server",
 "4. Standaard beweegt: spec 2025, GraphQL.js v17, defer/stream",
 "5. Federatie: één graph voor een organisatie",
 "6. Flexibiliteit = aanvalsoppervlak: limieten, trusted documents, autorisatie per veld",
 "7. Sterk voor agents, maar REST voor eenvoudige API's",
 "Ontwerp je schema goed: voor mensen én agents"]))

B.append(slide('vragen', 'Vragen?',
    p('Discussie: zou jij een agent **vrij queries laten schrijven** op je GraphQL-API, of enkel **gecureerde operaties** aanbieden? Waarom?', 42)
    + p('Belangrijkste bronnen', 38, bold=True)
    + ul(['graphql.org: homepage, *GraphQL for AI* (graphql.org/ai), *Security* (graphql.org/learn/security)',
          'graphql.org/blog: spec-editie september 2025, @oneOf, GraphQL.js v17, AI Working Group, GraphQLConf 2026, GAPs, GraphiQL 6',
          'GraphQL over HTTP en Composite Schemas (drafts, graphql.github.io)',
          'Apollo MCP Server 1.0 (07/10/2025); Apollo Client 4',
          'OSV/GitHub Advisories: CVE-2025-32032, CVE-2025-53364, CVE-2026-40324',
          'Eigen tests van alle codevoorbeelden met graphql-js 17.1.0 en DataLoader'], size=30),
"""Dan zijn er nu vragen. Een discussievraag om mee te beginnen: zou jij een AI-agent vrij queries laten schrijven op je GraphQL-API, of enkel gecureerde operaties aanbieden? Denk aan wat je vandaag zag: de flexibiliteit en de introspectie, maar ook de dure queries, de informatielekken, de kosten van context en prompt injection.

Onderaan de belangrijkste bronnen. De volledige lijst staat in de cursustekst. Alle codevoorbeelden in deze les heb ik uitgevoerd met GraphQL.js 17.1 en DataLoader: de antwoorden die je zag, zijn echte antwoorden.""",
["Discussie: agent vrij queries laten schrijven of enkel gecureerde operaties? Waarom?",
 "Denk aan: flexibiliteit, introspectie vs. dure queries, lekken, context-kost, prompt injection",
 "Bronnen: graphql.org (+ /ai, /learn/security), blog, drafts, Apollo MCP Server, OSV",
 "Codevoorbeelden getest met graphql-js 17.1.0 + DataLoader"]))
