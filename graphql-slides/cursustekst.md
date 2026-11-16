# GraphQL: de API-taal voor mensen en agents

**Cursustekst bij de les voor het vak Software Trends (AP Hogeschool, Toegepaste Informatica)**
Academiejaar 2026–2027 · stand van zaken: november 2026

---

## Leerdoelen en lesplan

Na deze les kan je:

1. uitleggen wat GraphQL is en welke problemen van REST het oplost (over- en underfetching, versiebeheer, trage productiteraties);
2. een GraphQL-schema lezen en schrijven in de Schema Definition Language (SDL), met types, relaties en de root types `Query`, `Mutation` en `Subscription`;
3. queries, mutations en subscriptions schrijven, met argumenten, variabelen, aliassen en fragmenten;
4. uitleggen hoe een GraphQL-server werkt met resolvers, en hoe je het N+1-probleem oplost met DataLoader;
5. de ontwikkelingen van 2025–2026 beschrijven: de nieuwe spec-editie, GraphQL.js v17, federatie en composite schemas, security in productie en GraphQL als API-taal voor AI-agents;
6. beargumenteren wanneer je GraphQL kiest en wanneer REST.

**Voorkennis.** HTTP, JSON en een REST-API aanroepen met `fetch`. Basis JavaScript. Voor trend 4 helpt de les over web frameworks (agents, MCP, prompt injection).

**Twee soorten slides.** Net als in de andere lessen:

- **Kernbegrip-slides** (met *Kernbegrip* rechtsboven) bevatten een definitie en uitleg. Dit is examenstof.
- **Trend-slides** (met een bron onderaan) tonen wat er in 2025–2026 gebeurt.

| Deel | Onderwerp | Richttijd | Kernvraag |
|---|---|---|---|
| 1 | Wat is GraphQL en waarom? | 8 min | Waarom bestaat GraphQL? |
| 2 | REST en zijn grenzen | 10 min | Welke problemen lost GraphQL op? |
| 3 | De taal: schema, queries, mutations, subscriptions | 16 min | Hoe beschrijf en vraag ik data? |
| 4 | De server: resolvers en DataLoader | 8 min | Hoe beantwoordt een server een query? |
| 5 | De client: declaratief, fragmenten, codegen | 6 min | Hoe gebruik ik GraphQL in een frontend? |
| 6 | Trend 1: de standaard beweegt weer | 8 min | Wat is er nieuw in de spec? |
| 7 | Trend 2: één graph voor de hele organisatie | 5 min | Hoe combineer je vele services? |
| 8 | Trend 3: security en performance | 8 min | Wat gaat er mis in productie? |
| 9 | Trend 4: de API-taal voor agents | 9 min | Waarom past GraphQL bij AI-agents? |
| 10 | Wanneer GraphQL, begrippen en conclusie | 4 min | Wat neem ik mee? |

---

## Deel 1: Wat is GraphQL en waarom?

*Kernvraag: waarom bestaat GraphQL?*

### "The API language for humans and agents"

De officiële website graphql.org opent vandaag met de slogan **"The API language for humans and agents"**. Daaronder: *typesafe schemas, secure requests*, *frictionless distributed development* en *data driven UI at scale*. GraphQL is ontworpen voor mensen die apps bouwen, maar wordt nu nadrukkelijk gepositioneerd als de taal waarmee AI-agents API's gebruiken. Waarom dat zo is, is de rode draad van deze les.

### Definitie

**GraphQL** is een **querytaal voor API's** en een **runtime aan de serverkant** die die queries uitvoert. De server beschrijft in een sterk getypeerd **schema** welke data en bewerkingen er zijn; de client stuurt een query die **exact beschrijft welke velden** hij nodig heeft, en krijgt een antwoord in **precies die vorm**.

Kenmerken:

- **Declaratieve data fetching**: de client beschrijft *wat* hij nodig heeft, niet *hoe* het opgehaald moet worden.
- **Eén endpoint** (meestal `POST /graphql`) voor alle queries en mutations.
- **Sterk getypeerd schema** dat tegelijk contract en documentatie is.
- **Opslag- en transportonafhankelijk**: GraphQL zegt niets over de databank erachter, en kan over HTTP, WebSockets of andere protocollen.
- **Open standaard**: ontstaan bij Facebook, sinds 2018 beheerd door de **GraphQL Foundation** bij de Linux Foundation.

### Waarom: een veranderende wereld

- **Mobiele apps**: minder rekenkracht en slechtere netwerken. Zo weinig mogelijk dataverkeer en zo weinig mogelijk round-trips.
- **Veel verschillende clients**: web, iOS, Android, smartwatch, partners. Eén REST-API die voor allemaal perfect past, bestaat niet. De client moet zelf kunnen kiezen welke data hij nodig heeft.
- **Snelle productiteraties**: de UI verandert wekelijks; de API moet mee kunnen zonder telkens nieuwe endpoints.
- **AI-agents**: hebben gestructureerde interfaces met duidelijke schema's nodig die ze zelf kunnen verkennen (deel 9).

### Geschiedenis

| Jaar | Gebeurtenis |
|---|---|
| 2012 | Facebook gebruikt GraphQL intern in zijn mobiele apps |
| 2015 | Voorgesteld op React.js Conf; spec en referentie-implementatie open source |
| 2016 | GitHub lanceert een publieke GraphQL-API |
| 2018 | GraphQL Foundation, gehost door de Linux Foundation |
| 2021 | Spec-editie oktober 2021; GraphQL.js v16 |
| 2025 | **Spec-editie september 2025** (eerste in vier jaar); nieuwe website: *"The API language for humans and agents"*; Apollo MCP Server 1.0; GraphQL AI Working Group |
| 2026 | **GraphQL.js v17** (juni); GraphQLConf 2026 (mei) met als thema *"the language of AI"*; GraphiQL 6 (november) |

GraphQL is **niet enkel voor React of JavaScript**: er zijn servers en clients in zo goed als elke taal (Java, Kotlin, C#, Python, Go, Rust, Swift, ...).

### Wie gebruikt het?

Op graphql.org staan onder meer Meta, AWS, Airbnb, Intuit, IBM, PayPal, The New York Times, Starbucks, Shopify en GitHub. Meta meldde op GraphQLConf 2026 dat het om *honderden miljarden* API-aanroepen per dag gaat.

In Postmans *State of the API 2025* (± 5.700 respondenten) gebruikt volgens secundaire bronnen **33%** GraphQL, tegenover **93%** REST. GraphQL is dus breed gebruikt, maar REST blijft de standaard. Dat is ook de juiste conclusie: GraphQL vervangt REST niet overal (deel 10).

**Kernpunt.** GraphQL is een querytaal en runtime waarmee de client met één request exact de data opvraagt die hij nodig heeft, op basis van een sterk getypeerd schema.

---

## Deel 2: REST en zijn grenzen

*Kernvraag: welke problemen lost GraphQL op?*

### Kernbegrip: REST

**REST** (*Representational State Transfer*, Roy Fielding, 2000) is een **architectuurstijl**, geen strikte specificatie. Data wordt aangeboden als **resources** met een eigen **URL**, die je bewerkt met **HTTP-methodes**:

```http
GET    /users          # alle gebruikers
GET    /users/3        # gebruiker 3
POST   /users          # nieuwe gebruiker
DELETE /users/3        # gebruiker 3 verwijderen
```

Omdat REST een stijl is, gaat elke API er anders mee om: hoe je relaties, paginering, filters of fouten aanbiedt, verschilt van API tot API.

| Voordelen | Nadelen |
|---|---|
| Eenvoudig, snel op te zetten | Geen standaard voor relaties tussen data |
| Standaard HTTP: caching, statuscodes, tools | Geen standaard voor ordening, paginering, filters |
| Goed voor stabiele, publieke API's | Geen ingebouwde notificaties bij nieuwe data |
| | Over- en underfetching; versieproblemen bij snel veranderende clients |

### Het versieprobleem

REST-endpoints worden vaak rond specifieke schermen gebouwd. Verandert de frontend, dan moet de backend mee, en bij een brekende wijziging komt er een nieuwe versie: `/api/v1/users`, `/api/v2/users`, ... Gevolg: duplicatie van logica, moeilijk onderhoud en trage iteratie tussen frontend en backend. GraphQL werkt **versieloos**: je voegt velden toe zonder bestaande clients te breken, en markeert oude velden met `@deprecated`.

### Voorbeeld: een blogapp

Een scherm toont de naam van Mary, de titels van haar posts en de namen van haar laatste drie volgers.

**Met REST** zijn dat drie requests:

1. `GET /users/<id>` → naam, maar ook adres, geboortedatum, ...
2. `GET /users/<id>/posts` → alle velden van alle posts
3. `GET /users/<id>/followers` → alle velden van alle volgers

**Met GraphQL** is het één request:

```graphql
query {
  user(id: "er3tg439frjw") {
    name
    posts { title }
    followers(last: 3) { name }
  }
}
```

```json
{
  "data": {
    "user": {
      "name": "Mary",
      "posts": [{ "title": "Learn GraphQL today" }],
      "followers": [{ "name": "John" }, { "name": "Alice" }, { "name": "Sarah" }]
    }
  }
}
```

### Kernbegrip: over- en underfetching

- **Overfetching**: de client krijgt meer data dan hij nodig heeft. Je wilt een lijst met namen, maar `/users` geeft ook geboortedatum en adres. Verspilde bandbreedte, zeker op mobiel.
- **Underfetching**: één endpoint geeft niet genoeg; de client moet extra requests doen.
- **N+1-probleem (aan de clientkant)**: een lijst-endpoint geeft enkel ID's of URL's terug, en voor elk element moet de client nog een request doen: 1 request voor de lijst + N requests voor de details. De PokéAPI is een bekend voorbeeld: `/pokemon` geeft namen en URL's, en voor de details van elke Pokémon is een extra request nodig.

GraphQL lost dit op aan de clientkant: de client vraagt exact de velden en relaties die hij nodig heeft, in één request. Het N+1-probleem verhuist dan naar de **server** (deel 4).

### Snelle productiteraties

- **REST**: endpoints worden rond schermen gebouwd. Een nieuwe datacombinatie betekent vaak een nieuw endpoint. Frontendwijziging = backendwerk.
- **GraphQL**: de client kiest zelf velden en relaties uit het schema. Zolang de data in het schema zit, hoeft de backend niets te veranderen.

**Kernpunt.** REST is een architectuurstijl met vaste resources per URL; dat leidt bij veel verschillende clients tot over- en underfetching, extra requests en versies. GraphQL laat de client de vorm van het antwoord kiezen.

---

## Deel 3: De taal

*Kernvraag: hoe beschrijf en vraag ik data?*

### Kernbegrip: het schema als contract

Elke GraphQL-server heeft een **schema**: een verzameling **types** en **velden** die je kan opvragen, met hun type. Het schema is een **contract** tussen client en server:

- De client weet precies wat hij kan vragen; de server weet precies wat hij moet teruggeven.
- Tools kunnen een query **valideren vóór uitvoering**: een onbestaand veld of verkeerd type wordt meteen geweigerd.
- Zegt het schema dat `name` een `String!` is, dan is het antwoord nooit `null` of een ander type.
- Frontend- en backendteams kunnen **onafhankelijk** werken zolang het schema hetzelfde blijft.
- Het schema is **zelf bevraagbaar** (introspectie, zie verder).

### Kernbegrip: Schema Definition Language (SDL)

```graphql
type Person {
  id: ID!
  name: String!
  age: Int!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  author: Person!
}
```

- **Scalars**: `ID`, `String`, `Int`, `Float`, `Boolean` (en eigen scalars zoals `DateTime`).
- **`!`** betekent *non-null*: dit veld is nooit `null`.
- **`[Post!]!`**: een lijst die zelf nooit `null` is, met elementen die nooit `null` zijn.
- **Relaties**: `Person.posts` en `Post.author` verbinden de types; zo ontstaat een *graph*.
- Daarnaast bestaan `enum`, `interface`, `union` en `input` (types voor argumenten).
- **Descriptions** met `"""..."""` documenteren types en velden in het schema zelf.

### Queries

```graphql
{ allPersons { name } }
```

```json
{ "data": { "allPersons": [{ "name": "Johnny" }, { "name": "Sarah" }, { "name": "Alice" }] } }
```

- Voeg je `age` toe, dan krijg je ook `age`. Laat je het weg, dan niet. **De vorm van de query bepaalt de vorm van het antwoord.**
- **Argumenten**: `allPersons(last: 2) { name age }` geeft enkel de laatste twee.
- **Geneste relaties**: `allPersons { name posts { title } }` geeft personen met hun posts, in één request.

### Kernbegrip: variabelen, aliassen en fragmenten

In echte applicaties schrijf je queries met een **naam** en **variabelen**, in plaats van waarden in de query te plakken:

```graphql
query PersonCard($id: ID!) {
  eerste: person(by: { id: $id }) { ...PersonInfo }
  tweede: person(by: { name: "Sarah" }) { ...PersonInfo }
}

fragment PersonInfo on Person {
  name
  age
}
```

- **Operatienaam** (`PersonCard`): handig voor logging, monitoring en caching.
- **Variabelen** (`$id: ID!`): worden apart meegestuurd (`{"id": "1"}`). De query zelf blijft vast, wat belangrijk is voor caching en security (trusted documents, deel 8).
- **Aliassen** (`eerste:`, `tweede:`): hetzelfde veld twee keer opvragen met andere argumenten.
- **Fragmenten** (`...PersonInfo`): herbruikbare selecties van velden.

### Mutations

Wijzigingen gebeuren met **mutations**: aanmaken, aanpassen en verwijderen (CRUD zonder de R).

```graphql
mutation {
  createPerson(name: "Bob", age: 36) {
    id
    name
  }
}
```

Een mutation geeft zelf ook data terug, in de vorm die de client vraagt. Vaak vraag je enkel het nieuwe `id` op.

### Subscriptions

**Subscriptions** geven een **realtime verbinding**: de server **pusht** data naar de client bij een gebeurtenis. Het is een **stroom** van resultaten, geen request-response. In de praktijk loopt dat over **WebSockets** (protocol `graphql-ws`) of **Server-Sent Events**.

```graphql
subscription {
  newPerson { name age }
}
```

### Kernbegrip: de root types

De queries hierboven werken pas als het schema de **ingangspunten** definieert. Daarvoor zijn er drie speciale **root types**:

```graphql
type Query {
  allPersons(last: Int): [Person!]!
  allPosts(last: Int): [Post!]!
}

type Mutation {
  createPerson(name: String!, age: Int!): Person!
  updatePerson(id: ID!, name: String, age: Int): Person!
  deletePerson(id: ID!): Person!
}

type Subscription {
  newPerson: Person!
}
```

Let op het type van `age`: `Int!`, zoals in `Person`. Zou je in de mutation `age: String!` schrijven, dan weigert de server `createPerson(name: "Bob", age: 36)` met de fout *String cannot represent a non string value*. Het schema maakt zulke fouten meteen zichtbaar.

### Kernbegrip: introspectie

De server kent het schema, de client niet. Via **introspectie** vraag je het schema op met een gewone query:

```graphql
{
  __type(name: "Person") {
    fields { name type { name kind } }
  }
}
```

Introspectie maakt tools mogelijk zoals **GraphiQL** (een IDE in de browser met autocomplete; versie 6 verscheen in november 2026), codegeneratoren en, recent, **AI-agents** die zelf ontdekken wat een API kan. Het is ook een securityrisico als het schema dingen verraadt die niet publiek mogen zijn (deel 8).

### Kernbegrip: de vorm van een antwoord

Een GraphQL-antwoord heeft altijd dezelfde vorm: een object met **`data`** en eventueel **`errors`**.

```json
{
  "data": { "user": { "name": "Mary", "posts": null } },
  "errors": [{ "message": "Posts service unavailable", "path": ["user", "posts"] }]
}
```

- GraphQL kan **gedeeltelijke resultaten** teruggeven: één veld faalt, de rest komt toch.
- Het `path` toont welk veld faalde.
- Faalt een veld dat non-null is (`!`), dan **propageert** de `null` naar boven tot het eerste nullable veld. Dat heet *null bubbling* (zie trend 1).
- Over HTTP gaf een GraphQL-server traditioneel altijd status **200**, ook bij fouten. De **GraphQL over HTTP**-spec (nog een draft) introduceert het mediatype `application/graphql-response+json`, waarmee de statuscode wel betekenis krijgt.

**Kernpunt.** Het schema (SDL) beschrijft types, relaties en de root types `Query`, `Mutation` en `Subscription`. De client stelt met queries, variabelen en fragmenten exact het antwoord samen dat hij nodig heeft, en krijgt `data` en eventueel `errors` terug.

---

## Deel 4: De server

*Kernvraag: hoe beantwoordt een server een query?*

### Drie architecturen

1. **GraphQL-server met eigen databank**: typisch bij nieuwe projecten (*greenfield*). De server leest en schrijft rechtstreeks in de databank.
2. **GraphQL als laag boven bestaande systemen**: een GraphQL-server die legacy systemen, microservices en externe API's verenigt achter één schema. De client ziet één API, de complexiteit zit achter de server.
3. **Hybride**: een combinatie van een eigen databank en bestaande systemen.

### Kernbegrip: resolvers

Een query bestaat uit velden, en **elk veld heeft een resolver**: een functie die weet waar en hoe de data voor dat veld gehaald wordt.

```js
const resolvers = {
  Query: {
    user: (_, { id }) => db.users.findById(id),
  },
  User: {
    followers: (user, { first }) => db.followers.forUser(user.id, first),
  },
};
```

Voor de query `user(id: "...") { name followers(first: 5) { name age } }`:

1. De server valideert de query tegen het schema.
2. De resolver van `Query.user` haalt de gebruiker op.
3. Voor elk gevraagd veld van `User` loopt de bijhorende resolver. Velden zonder eigen resolver (`name`) lezen gewoon de property.
4. `User.followers` krijgt de gebruiker als eerste argument (`parent`) en de argumenten van het veld.
5. Alles wordt samengevoegd tot één antwoord in de vorm van de query.

Omdat elke resolver zijn eigen bron mag hebben (databank, REST-API, cache, ...), kan GraphQL data uit verschillende systemen in één antwoord combineren.

### Kernbegrip: het N+1-probleem aan de serverkant en DataLoader

Vraag je `allPosts { title author { name } }`, dan loopt de resolver van `Post.author` **één keer per post**. Met 3 posts zijn dat 1 query voor de lijst + 3 queries voor de auteurs; met 1.000 posts 1.001 queries. Het N+1-probleem is van de client naar de server verhuisd.

De standaardoplossing is **DataLoader**: een kleine bibliotheek (oorspronkelijk van Facebook) die alle `load(id)`-aanroepen binnen één tick van de event loop **verzamelt (batching)** en in één databank-query uitvoert, en dubbele ID's **ontdubbelt (caching per request)**.

```js
const userLoader = new DataLoader(async (ids) => {
  const users = await db.users.findByIds(ids);   // één query
  return ids.map((id) => users.find((u) => u.id === id));
});

const resolvers = {
  Post: { author: (post) => userLoader.load(post.authorId) },
};
```

Getest met graphql-js 17: drie posts gaven zonder DataLoader **3** databank-aanroepen voor de auteurs, met DataLoader **1**.

**Kernpunt.** Een GraphQL-server voert per veld een resolver uit. Dat maakt het flexibel, maar zonder batching (DataLoader) krijg je snel het N+1-probleem op de server.

---

## Deel 5: De client

*Kernvraag: hoe gebruik ik GraphQL in een frontend?*

### Imperatief versus declaratief

- **Imperatief** (klassiek met `fetch`): je bouwt het request, wacht, parset, bewaart de data lokaal en houdt die zelf up-to-date.
- **Declaratief** (met een GraphQL-client): je schrijft een query die beschrijft welke data een component nodig heeft; de bibliotheek doet de rest: ophalen, caching, updaten van de UI.

Bekende clients: **Apollo Client** (versie 4 in 2025, met onder meer data masking en betere suspense-ondersteuning), **Relay** (van Meta, compiler-gebaseerd) en **urql**.

### Fragment colocation

Een component declareert zijn eigen data-behoefte als fragment, naast de code van het component. De ouder stelt de fragmenten samen tot één query:

```graphql
fragment FriendListItem on User {
  id
  name
  profilePic
}

query FriendList {
  me {
    friends { ...FriendListItem }
  }
}
```

Voegt `FriendListItem` een veld toe, dan pas je enkel dat fragment aan. graphql.org noemt dit *data colocation*; het is het hart van Relay en wordt ook door Apollo Client ondersteund (*data masking*: een component ziet enkel de velden uit zijn eigen fragment).

### Codegeneratie

Het schema is getypeerd; het zou zonde zijn om de TypeScript-types met de hand bij te houden (verouderde types, tikfouten, onvolledige typing). Tools genereren ze uit het schema en je queries:

- **GraphQL Code Generator** (The Guild)
- **gql.tada** (types afgeleid in TypeScript zelf, zonder build-stap)
- **Relay compiler**

**Kernpunt.** GraphQL-clients maken data fetching declaratief: componenten beschrijven met fragmenten welke data ze nodig hebben, en types worden gegenereerd uit het schema.

---

## Deel 6: Trend 1 — De standaard beweegt weer

*Kernvraag: wat is er nieuw in de spec?*

Tussen oktober 2021 en september 2025 verscheen er geen nieuwe editie van de GraphQL-specificatie. Sinds 2025 beweegt de standaard weer.

### De spec-editie van september 2025

| Nieuw | Wat het doet |
|---|---|
| **OneOf input objects** (`@oneOf`) | Precies één veld van een input moet ingevuld zijn |
| **Schema coordinates** | Standaardnotatie om naar schema-elementen te verwijzen: `Person`, `Person.name`, `Query.person(by:)` |
| **Descriptions op operaties** | `"""..."""` boven een query of fragment, voor documentatie en AI-tooling |
| **Uitgebreide deprecation** | `@deprecated` op meer plaatsen, zodat API's kunnen evolueren zonder te breken |
| **Volledige Unicode** | De taal aanvaardt het volledige Unicode-bereik |
| **Verduidelijkte fout- en uitvoeringsregels** | Voorspelbaardere antwoorden voor tools |

### Kernbegrip: @oneOf

Vroeger moest je voor "zoek een persoon op ID óf op naam" twee aparte velden maken (`personById`, `personByName`) of twee optionele argumenten die je zelf controleerde. Met `@oneOf` zegt het schema dat **precies één** van de velden ingevuld moet zijn:

```graphql
input PersonLookup @oneOf {
  id: ID
  name: String
}

type Query {
  person(by: PersonLookup!): Person
}
```

`person(by: { id: "1" })` is geldig. `person(by: { id: "1", name: "Sarah" })` wordt al bij de validatie geweigerd. Dit is een vorm van *input union*: een van de langst gevraagde uitbreidingen van GraphQL.

### GraphQL.js v17 (juni 2026)

**GraphQL.js** is de referentie-implementatie in JavaScript, gebruikt door vrijwel elke JS-server. Versie 17 is de eerste grote versie sinds oktober 2021:

- **`AbortSignal`**: een request kan afgebroken worden; resolvers zien dat via `info.getAbortSignal()`.
- **`hideSuggestions`**: verbergt "Did you mean ...?" in foutmeldingen (minder schema-lekken, zie deel 8).
- **`findSchemaChanges()`**: geeft brekende, gevaarlijke en veilige schemawijzigingen in één keer.
- **Experimenteel**: incremental delivery (`@defer` en `@stream`), uitschakelen van foutpropagatie en fragment-argumenten.

### Kernbegrip: incremental delivery (@defer en @stream)

Sommige velden zijn traag (aanbevelingen, statistieken). Zonder `@defer` wacht het hele antwoord op het traagste veld. Met `@defer` krijg je eerst de snelle velden en later de rest:

```graphql
{
  allPersons(last: 1) {
    name
    ... @defer { posts { title } }
  }
}
```

Eerste antwoord:

```json
{ "data": { "allPersons": [{ "name": "Bob" }] }, "pending": [{ "id": "0", "path": ["allPersons", 0] }], "hasNext": true }
```

Later:

```json
{ "incremental": [{ "id": "0", "data": { "posts": [] } }], "completed": [{ "id": "0" }], "hasNext": false }
```

`@stream` doet hetzelfde voor lijsten: elementen komen binnen zodra ze klaar zijn. Status: nog een voorstel (RFC), experimenteel in GraphQL.js v17 (`experimentalExecuteIncrementally`), en al ondersteund door verschillende servers en clients. Het formaat met `pending`, `incremental` en `completed` is op deze manier getest met graphql-js 17.1.

### Foutafhandeling en nullability

Faalt een non-null veld, dan wordt de `null` naar boven doorgegeven tot het eerste nullable veld (*null bubbling*). Eén falend veld kan zo een groot deel van het antwoord wissen. Daarom maken veel teams uit voorzorg alles nullable, wat het schema minder informatief maakt. Voorstellen in behandeling laten de client kiezen wat er bij een fout gebeurt (`onError`), bijvoorbeeld enkel het foute veld op `null` zetten. GraphQL.js v17 heeft daar een experimentele richtlijn voor (`@experimental_disableErrorPropagation`).

### Een levende standaard

- **GAPs** (*GraphQL Auxiliary Proposals*, juni 2026): een nieuwe plek voor community-specificaties naast de kernspec.
- **GraphQL over HTTP**: draft-spec voor requests, mediatypes en statuscodes.
- **Composite Schemas**: draft-spec voor federatie (trend 2).

**Kernpunt.** Na vier jaar stilte beweegt de standaard weer: de spec-editie van 2025 (met `@oneOf`), GraphQL.js v17 en experimentele functies als `@defer` en `@stream`.

---

## Deel 7: Trend 2 — Eén graph voor de hele organisatie

*Kernvraag: hoe combineer je vele services?*

### Kernbegrip: federatie

In een grote organisatie is één GraphQL-server voor alles onwerkbaar: tientallen teams, elk met hun eigen service. **Federatie** lost dat op:

- Elk team bouwt een **subgraph**: een eigen GraphQL-service met een deel van het schema.
- Een **gateway** of **router** combineert alle subgraphs tot één **supergraph**.
- De client ziet één API; de router plant hoe een query over de subgraphs verdeeld wordt (*query planning*).
- Entities zoals `User` kunnen door meerdere subgraphs uitgebreid worden, verbonden via een sleutel.

```graphql
# subgraph "accounts"
type User @key(fields: "id") {
  id: ID!
  name: String!
}

# subgraph "reviews"
type User @key(fields: "id") {
  id: ID!
  reviews: [Review!]!
}
```

### Van vendor-specifiek naar standaard

Federatie werd groot met **Apollo Federation**, maar elke leverancier had zijn eigen variant (Apollo, The Guild Hive Gateway, Grafbase, WunderGraph Cosmo, ChilliCream Fusion). De **GraphQL Composite Schemas Working Group** schrijft daarom een gemeenschappelijke specificatie (met richtlijnen als `@lookup` en `@key`). Die spec is in november 2026 nog een **draft**, maar wordt al geïmplementeerd. Op GraphQLConf 2026 beschreef Uri Goldshtein (The Guild) federatie als "a set of well-worn paths": geen experiment meer, maar een gekende aanpak.

**Kernpunt.** Federatie combineert subgraphs van verschillende teams tot één supergraph achter een router. De Composite Schemas-spec moet de vendor-varianten standaardiseren.

---

## Deel 8: Trend 3 — Security en performance in productie

*Kernvraag: wat gaat er mis in productie?*

### Kernbegrip: het aanvalsoppervlak van GraphQL

GraphQL geeft de client veel vrijheid. Dat is de kracht, maar ook het risico:

- **Diepe of dure queries (DoS)**: `user { friends { friends { friends { ... } } } }` kan een server platleggen. Ook aliassen (hetzelfde veld honderd keer) en fragmenten kunnen dat.
- **Batching voor brute force**: honderd `login`-mutations in één request omzeilen een rate limit per request.
- **Informatielekken**: introspectie en "Did you mean ...?"-suggesties verraden het schema, ook interne velden.
- **Autorisatie per veld**: één endpoint betekent dat je niet per URL kan beveiligen; elke resolver moet zelf controleren of de gebruiker de data mag zien.

### Echte incidenten

| CVE | Product | Wat |
|---|---|---|
| CVE-2025-32032 (april 2025) | Apollo Router | Diep geneste, hergebruikte fragmenten maakten query planning extreem duur: DoS |
| CVE-2025-53364 (juli 2025) | Parse Server | Het GraphQL-schema was opvraagbaar zonder sessie of sleutel |
| CVE-2026-40324 (april 2026) | Hot Chocolate (.NET) | Parser zonder recursielimiet: een document van ±40 KB crasht het hele proces |

### Kernbegrip: verdediging

- **Diepte- en kostenlimieten**: een maximale nestingdiepte en een *cost analysis* die elke query een prijs geeft en te dure queries weigert.
- **Trusted documents (persisted operations)**: de client stuurt geen vrije query, maar de **hash** van een vooraf geregistreerde query. De server voert enkel bekende queries uit. Ideaal voor je eigen apps; voor publieke API's met externe clients niet mogelijk.
- **Introspectie en suggesties** uitschakelen voor publieke clients (`hideSuggestions` in GraphQL.js v17). Let op: dat is *security through obscurity* en volstaat op zich niet.
- **Autorisatie in de resolvers** (of met richtlijnen zoals `@policy`), niet enkel aan de rand.
- **Rate limiting op operaties**, niet enkel op requests.
- **Tijdig updaten** van server, router en parser.

### Caching

REST profiteert van HTTP-caching: elke URL is een resource. GraphQL stuurt alles via `POST /graphql`, dus een CDN kan niets cachen. Oplossingen: queries via **GET** met een persisted-query-hash (cachebaar), caching per veld op de server, en een **genormaliseerde cache** in de client (Apollo, Relay) die objecten op `id` bewaart.

**Kernpunt.** De flexibiliteit van GraphQL is ook zijn aanvalsoppervlak. Beperk diepte en kost, gebruik trusted documents voor eigen clients, autoriseer per veld en update je server.

---

## Deel 9: Trend 4 — De API-taal voor agents

*Kernvraag: waarom past GraphQL bij AI-agents?*

### Waarom GraphQL en agents goed samengaan

Een AI-agent (zie de les over web frameworks) moet een API gebruiken die hij niet kent. GraphQL biedt wat hij nodig heeft:

- **Zelfbeschrijvend**: via introspectie ontdekt de agent types, velden, argumenten en relaties, en leest hij de **descriptions** (`"""..."""`) als documentatie. Geen aparte handleiding nodig.
- **Sterk getypeerd en gevalideerd**: een fout veld geeft geen 200 met rommel, maar een duidelijke validatiefout die de agent kan corrigeren, bijvoorbeeld *Cannot query field "nam" on type "Person". Did you mean "name"?*
- **Precies**: de agent vraagt enkel de velden die hij nodig heeft. Dat bespaart **context** (tokens), wat bij LLM's geld en kwaliteit kost.
- **Samenstelbaar**: één query volgt relaties over meerdere types, waar een agent bij REST meerdere endpoints moet combineren.

### Hoe een agent een GraphQL-API gebruikt

1. **Taak**: "Toon de omzet per regio voor de top 5 categorieën in Q4."
2. **Introspectie**: de agent ontdekt `Product`, `Order`, `RevenueMetrics`, `Region`.
3. **Query samenstellen**: het model zet de vraag om in één precieze query.
4. **Gestructureerde JSON** terug, in de vorm van de query; bij een gedeeltelijke fout ziet de agent in `errors` wat er misliep.

### GraphQL en MCP

Het **Model Context Protocol** (MCP) is de standaard waarmee agents tools aanroepen. Een GraphQL-API leent zich goed als bron van zulke tools:

- **Apollo MCP Server** (1.0 sinds oktober 2025, open source): GraphQL-operaties worden MCP-tools, zonder extra wrappercode. Optioneel kan de agent zelf het schema introspecteren en doorzoeken.
- Twee strategieën: de agent krijgt **het volledige schema** en schrijft zelf queries (flexibel, maar groot en riskant), of een **gecureerde set operaties** als tools (veilig en zuinig). Apollo meldt voor de tweede aanpak ongeveer 40% minder schemacontext en 40–75% minder tool-aanroepen; dat zijn cijfers van de leverancier zelf.

### De community gaat mee

- **GraphQL AI Working Group** (sinds oktober 2025): werkt aan *semantic introspection* (betekenis en verbanden in het schema, zodat een agent de relevante delen van een groot schema vindt), een `@mock`-richtlijn en embeddings van schema's.
- **GraphQLConf 2026** had AI als dominant thema; de afsluiter (Matt DeBergalis, Apollo): GraphQL *"can and must be the language of AI"*. Er waren talks van onder meer Meta, Netflix, IBM, Starbucks en Wayfair.
- De spec-editie van 2025 voegde **descriptions op operaties** toe, mee met het oog op AI-tooling.

### Kritische noot

- **Grote schema's passen niet in een context window**: een schema met tienduizenden velden moet je filteren of doorzoekbaar maken.
- **Agents schrijven dure queries**: kostenlimieten en trusted documents (deel 8) zijn hier nog belangrijker.
- **Prompt injection** blijft een risico: data uit de API kan instructies bevatten (zie de les over web frameworks).
- **REST is soms eenvoudiger**: graphql.org zelf geeft toe dat een taak die op één endpoint past, met REST simpeler is.
- **Cijfers van leveranciers** zijn geen onafhankelijke benchmarks; de AI Working Group vraagt zelf om reproduceerbare metingen.

**Kernpunt.** Introspectie, sterke typering en precieze queries maken GraphQL geschikt als API-taal voor agents, onder meer via MCP. Dezelfde vrijheid vraagt wel extra aandacht voor kosten en security.

---

## Deel 10: Wanneer GraphQL, begrippen en conclusie

### Wanneer GraphQL, wanneer REST?

| Situatie | Keuze |
|---|---|
| Veel verschillende clients (web, mobiel) met andere databehoeften | **GraphQL** |
| Snel veranderende UI, product-gedreven ontwikkeling | **GraphQL** |
| Veel backends samenbrengen achter één API | **GraphQL** (met federatie) |
| API voor AI-agents die zelf moeten verkennen | **GraphQL** (of gecureerde MCP-tools) |
| Eenvoudige CRUD-API, weinig clients | **REST** |
| Publieke API waar HTTP-caching cruciaal is | **REST** |
| Bestanden uploaden en downloaden, streaming media | **REST** |
| Interne communicatie tussen services met hoge performance | **gRPC** |

### Wat kan je er zelf mee?

- Speel met een publieke API in **GraphiQL** (bv. de Star Wars-API op graphql.org of de GitHub GraphQL-API).
- Bouw een kleine server met **GraphQL.js**, Apollo Server of GraphQL Yoga, en meet het N+1-probleem met en zonder **DataLoader**.
- Genereer je TypeScript-types met **GraphQL Code Generator** of gql.tada.
- Zet in productie **diepte- en kostenlimieten**, **trusted documents** en **autorisatie per veld**.
- Schrijf **descriptions** in je schema: voor je collega's én voor agents.

### Begrippenlijst

| Begrip | Betekenis |
|---|---|
| **GraphQL** | Querytaal voor API's en runtime die queries tegen een getypeerd schema uitvoert |
| **REST** | Architectuurstijl met resources per URL en HTTP-methodes |
| **Overfetching** | Meer data ontvangen dan nodig |
| **Underfetching** | Te weinig data per request, waardoor extra requests nodig zijn |
| **N+1-probleem** | 1 request/query voor een lijst + N extra voor de details van elk element |
| **Schema** | Verzameling types en velden: het contract tussen client en server |
| **SDL** | Schema Definition Language: de notatie voor een schema |
| **Non-null (`!`)** | Veld dat nooit `null` is |
| **Query / Mutation / Subscription** | Data lezen / data wijzigen / realtime stroom van gebeurtenissen |
| **Root types** | `Query`, `Mutation`, `Subscription`: de ingangspunten van het schema |
| **Variabele** | Apart meegestuurde waarde in een query (`$id`) |
| **Alias** | Andere naam voor een veld in het antwoord |
| **Fragment** | Herbruikbare selectie van velden |
| **Introspectie** | Het schema opvragen met een query (`__schema`, `__type`) |
| **Resolver** | Functie die de data voor één veld ophaalt |
| **DataLoader** | Bibliotheek die resolver-aanroepen bundelt (batching) tegen het N+1-probleem |
| **Fragment colocation** | Elk component declareert zijn data-behoefte als fragment naast zijn code |
| **Codegeneratie** | Types genereren uit schema en queries |
| **@oneOf** | Input waarvan precies één veld ingevuld moet zijn |
| **@defer / @stream** | Incremental delivery: delen van het antwoord later sturen |
| **Null bubbling** | Een fout in een non-null veld maakt de ouder `null` |
| **Federatie** | Subgraphs van verschillende teams samengevoegd tot één supergraph achter een router |
| **Trusted documents** | Enkel vooraf geregistreerde queries (via hash) worden uitgevoerd |
| **Cost analysis** | Elke query krijgt een kost; te dure queries worden geweigerd |
| **MCP** | Model Context Protocol: standaard waarmee AI-agents tools aanroepen |

### Conclusie

1. **GraphQL laat de client kiezen**: exact de data die hij nodig heeft, in één request, volgens een getypeerd schema.
2. **Het schema is het hart**: contract, documentatie en basis voor validatie, tooling en codegeneratie.
3. **De server werkt met resolvers**; zonder DataLoader verhuist het N+1-probleem naar de server.
4. **De standaard beweegt weer**: spec-editie 2025 (`@oneOf`), GraphQL.js v17, `@defer`/`@stream` onderweg.
5. **Federatie** maakt één graph voor een hele organisatie; de Composite Schemas-spec moet het standaardiseren.
6. **Flexibiliteit is aanvalsoppervlak**: beperk kosten, gebruik trusted documents, autoriseer per veld.
7. **"The API language for humans and agents"**: introspectie en typering maken GraphQL geschikt voor AI-agents, maar REST blijft de juiste keuze voor eenvoudige API's.

---

## Bronnen

- graphql.org (homepage, *GraphQL for AI*: graphql.org/ai, *Security*: graphql.org/learn/security), geraadpleegd november 2026
- GraphQL-blog: *Announcing the September 2025 Edition of the GraphQL Specification* (08/09/2025); *Safer Multi-option Inputs with @oneOf* (04/09/2025); *Introducing the New GraphQL.org* (08/09/2025); *Announcing the GraphQL AI Working Group* (14/10/2025); *GraphQL AI Working Group Recap: January 2026* (22/01/2026); *Introducing GAPs* (01/06/2026); *Introducing GraphQL.js v17* (15/06/2026); *GraphQLConf 2026 wrap-up: "the language of AI"* (14/07/2026); *Introducing GraphiQL 6* (07/11/2026)
- GraphQL over HTTP (draft): graphql.github.io/graphql-over-http
- Composite Schemas Spec (draft): graphql.github.io/composite-schemas-spec
- Apollo: *Apollo MCP Server 1.0 is generally available* (07/10/2025); Apollo Client 4
- OSV/GitHub Advisories: CVE-2025-32032 (Apollo Router), CVE-2025-53364 (Parse Server), CVE-2026-40324 (Hot Chocolate)
- Postman, *State of the API 2025* (via secundaire bronnen)
- DataLoader: github.com/graphql/dataloader
- Eigen tests van de codevoorbeelden met graphql-js 17.1.0 en dataloader (november 2026)
