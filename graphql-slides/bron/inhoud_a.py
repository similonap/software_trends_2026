"""Slides 1-29: intro, REST, de taal, de server en de client."""
from helpers import *

A = []

A.append(cover(
"""Welkom bij deze les over GraphQL.

Bijna elke applicatie die jullie later bouwen, praat met een API. De meeste van die API's zijn REST-API's, maar een groot deel van de grote spelers, zoals GitHub, Shopify, Airbnb en Meta, gebruikt GraphQL. Vandaag leren we wat GraphQL is, welke problemen het oplost, hoe de taal werkt, hoe een server en een client ermee omgaan, en wat er in 2025 en 2026 veranderd is.

De titel van de les komt van de officiële website van GraphQL zelf. Die opent vandaag met de zin: The API language for humans and agents. GraphQL wil dus niet alleen de taal zijn waarmee ontwikkelaars API's gebruiken, maar ook de taal waarmee AI-agents dat doen. Dat is de rode draad van deze les.

Let tijdens de les op de slides met het woord Kernbegrip rechtsboven. Dat zijn de definities en concepten die je moet kennen en kunnen uitleggen. Achteraan vind je een begrippenlijst.""",
["API's zijn overal; meeste REST, maar GitHub, Shopify, Airbnb, Meta gebruiken GraphQL",
 "Vandaag: wat, waarom, de taal, server en client, trends 2025–2026",
 "Titel komt van graphql.org zelf: 'The API language for humans and agents' → rode draad",
 "Kernbegrip-slides = examenstof; begrippenlijst achteraan",
 "→ Wat bedoelt graphql.org met die slogan?"]))

A.append(slide('tagline', 'Hoe GraphQL zichzelf vandaag voorstelt',
    f'<p style="font-family:{QUEST};font-size:88px;line-height:1.1;color:{ROOD}">"The API language for humans and agents"</p>'
    + row(card('Typesafe schemas, secure requests', size=32), card('Frictionless distributed development', size=32),
          card('Data driven UI at scale', size=32), gap=28)
    + p('Een API-taal die mensen helpt apps te bouwen, en die AI-agents **zelf kunnen verkennen en gebruiken**. Waarom dat werkt, is de rode draad van deze les.', 34, '#595959'),
"""Zo stelt GraphQL zichzelf vandaag voor op graphql.org: the API language for humans and agents. Daaronder drie beloftes. Typesafe schemas, secure requests: een sterk getypeerd schema en veilige requests. Frictionless distributed development: teams kunnen onafhankelijk van elkaar werken. En data driven UI at scale: gebruikersinterfaces die hun eigen data opvragen, ook in heel grote applicaties.

Het opvallende is het woord agents. GraphQL bestaat sinds 2012 en werd ontworpen voor mensen: ontwikkelaars die mobiele apps bouwen. Vandaag zegt de officiële website dat GraphQL ook de taal is waarmee AI-agents API's gebruiken. Op de laatste GraphQLConf, in mei 2026, was AI het dominante thema.

Is dat marketing of klopt het? Om dat te kunnen beoordelen, moet je eerst begrijpen hoe GraphQL werkt: het schema, de introspectie, de validatie. Die begrippen zien we eerst. In trend 4 komen we terug op de agents, en dan kan je zelf oordelen.""",
["graphql.org: 'The API language for humans and agents'",
 "Drie beloftes: typesafe schemas & secure requests; frictionless distributed development; data driven UI at scale",
 "Ontworpen in 2012 voor mensen (mobiele apps); nu ook voor AI-agents; GraphQLConf 2026: AI dominant thema",
 "Marketing of waar? Eerst begrippen (schema, introspectie, validatie), dan oordelen in trend 4",
 "→ Agenda"],
bron='graphql.org (november 2026)'))

A.append(slide('agenda', 'Agenda',
    ul(['Wat is GraphQL, en waarom?',
        'REST en zijn grenzen',
        'De taal: schema, queries, mutations, subscriptions',
        'De server: resolvers en DataLoader',
        'De client: declaratief, fragmenten en codegeneratie',
        'Trend 1: De standaard beweegt weer',
        'Trend 2: Eén graph voor de hele organisatie',
        'Trend 3: Security en performance in productie',
        'Trend 4: De API-taal voor agents',
        'Wanneer GraphQL, begrippenlijst en conclusie'], size=39)
    + spacer()
    + '<p style="font-size:34px;line-height:1.4;color:#595959">Slides met <span style="color:#C00000">Kernbegrip</span> rechtsboven bevatten definities die je moet kennen en kunnen uitleggen (examenstof).</p>',
"""Dit is het plan. We beginnen bij de vraag waarom GraphQL bestaat, en vergelijken het met REST, de manier waarop de meeste API's vandaag werken. Daarna leren we de taal zelf: het schema, queries, mutations en subscriptions. Dan kijken we hoe een server zo'n query beantwoordt en hoe een client in de browser ermee werkt.

Het tweede deel bestaat uit vier trends van 2025 en 2026, elk met een rode tussenslide: de standaard die na vier jaar weer beweegt, federatie, security, en GraphQL als taal voor AI-agents. We eindigen met de vraag wanneer je GraphQL kiest en wanneer REST.

Slides met Kernbegrip rechtsboven zijn examenstof. De andere slides geven context en voorbeelden.""",
["Eerst: waarom, REST, de taal, server, client",
 "Dan vier trends: standaard, federatie, security, agents",
 "Afsluiten met: wanneer GraphQL, wanneer REST",
 "Kernbegrip-slides = examenstof",
 "→ Wat is GraphQL?"]))

# ---------------- Wat en waarom ----------------
A.append(slide('kb-graphql', 'Wat is GraphQL?',
    p('**GraphQL** is een **querytaal voor API\'s** en een **runtime aan de serverkant** die die queries uitvoert tegen een **sterk getypeerd schema**.', 34)
    + row(
        col(ul(['**Declaratieve data fetching**: de client beschrijft *wat* hij nodig heeft, niet *hoe*',
                '**Eén endpoint** (meestal `POST /graphql`) voor alles',
                'Het antwoord heeft **exact de vorm van de query**',
                '**Opslag- en transportonafhankelijk**: elke databank, HTTP of WebSockets'], size=32)),
        col(code('''query {
  user(id: "1") {
    name
    posts { title }
  }
}''', 'graphql', 24),
            code('''{ "data": { "user": {
    "name": "Mary",
    "posts": [{ "title": "Learn GraphQL" }]
} } }''', 'json', 22), gap=12), gap=48)
    + p('Ontstaan bij **Facebook** (2012), open source sinds **2015**, sinds **2018** beheerd door de **GraphQL Foundation** (Linux Foundation).', 30, '#595959'),
"""Wat is GraphQL? Het is twee dingen tegelijk: een querytaal voor API's, en een runtime aan de serverkant die die queries uitvoert. Die runtime werkt tegen een sterk getypeerd schema: een beschrijving van alle data en bewerkingen die de API aanbiedt.

Het belangrijkste idee is declaratieve data fetching. De client beschrijft wat hij nodig heeft, niet hoe het opgehaald moet worden. Rechts zie je een voorbeeld: ik wil de gebruiker met id 1, daarvan enkel de naam, en van zijn posts enkel de titel. En het antwoord eronder heeft exact die vorm. Niet meer, niet minder.

Verder heeft een GraphQL-API meestal één endpoint, typisch POST naar slash graphql, voor alle vragen. En GraphQL zegt niets over hoe je de data opslaat: dat kan een SQL-databank zijn, een NoSQL-databank, een andere API of een bestand. Ook het transport ligt niet vast: meestal HTTP, maar het kan ook over WebSockets.

GraphQL ontstond in 2012 bij Facebook, werd in 2015 open source gemaakt en wordt sinds 2018 beheerd door de GraphQL Foundation, die deel is van de Linux Foundation. Het is dus geen product van één bedrijf meer, maar een open standaard.""",
["GraphQL = querytaal voor API's + runtime die queries uitvoert tegen een sterk getypeerd schema",
 "Declaratief: client beschrijft wat, niet hoe; antwoord heeft exact de vorm van de query",
 "Eén endpoint (POST /graphql); opslag- en transportonafhankelijk",
 "Facebook 2012 → open source 2015 → GraphQL Foundation (Linux Foundation) 2018",
 "Examen: GraphQL kunnen definiëren met de begrippen querytaal, runtime, schema",
 "→ Waarom was dat nodig?"],
kern=True))

A.append(slide('waarom', 'Nieuwe technologie in een veranderende wereld',
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px 40px">'
    + card('Meer mobiele applicaties', 'Minder rekenkracht, slechtere netwerken: zo weinig mogelijk dataverkeer en round-trips.', size=34)
    + card('Veel verschillende clients', 'Web, iOS, Android, smartwatch, partners: één API die voor allemaal past, bestaat niet. De client moet zelf kiezen.', size=34)
    + card('Snellere productiteraties', 'De UI verandert elke week; de API moet mee kunnen zonder telkens nieuwe endpoints.', size=34)
    + card('AI-agents', 'Hebben gestructureerde interfaces met duidelijke, verkenbare schema\'s nodig.', size=34)
    + '</div>',
"""Waarom was er nood aan iets nieuws? Vier redenen.

Eén: meer mobiele applicaties. Een telefoon heeft minder rekenkracht dan een laptop en zit vaak op een trage of onbetrouwbare verbinding. Elke extra request en elke kilobyte te veel is merkbaar. Dat was precies het probleem van Facebook in 2012, toen de mobiele app traag werd.

Twee: veel verschillende clients. Een bedrijf heeft een website, een iOS-app, een Android-app, misschien een smartwatch-app en partners die de API gebruiken. Elke client heeft andere data nodig. Eén REST-API die voor allemaal perfect past, bestaat niet. De oplossing van GraphQL: laat de client zelf kiezen.

Drie: snellere productiteraties. De gebruikersinterface verandert elke week. Als elke verandering een nieuw endpoint op de backend vraagt, gaat het traag.

En vier, de nieuwste reden: AI-agents. Een agent die een API moet gebruiken die hij niet kent, heeft nood aan een gestructureerde interface met een duidelijk schema dat hij zelf kan verkennen. Daar komen we in trend 4 op terug.""",
["Mobiel: weinig rekenkracht, slechte netwerken → minimaal dataverkeer en round-trips (Facebook 2012)",
 "Veel clients (web, iOS, Android, partners): één API past niet voor allemaal → client kiest zelf",
 "Snelle productiteraties: UI verandert wekelijks, API moet mee zonder nieuwe endpoints",
 "Nieuw: AI-agents hebben verkenbare, gestructureerde schema's nodig (trend 4)",
 "→ De geschiedenis"]))

A.append(slide('geschiedenis', 'Even wat geschiedenis',
    '<div style="display:flex;flex-direction:column;gap:14px">'
    + ''.join(f'<div style="display:flex;gap:28px;align-items:baseline"><p style="width:150px;flex:none;font-family:{QUEST};font-size:40px;color:#C00000">{j}</p><p style="font-size:34px;line-height:1.3">{inline(t)}</p></div>' for j, t in [
        ('2012', '**Facebook** gebruikt GraphQL intern in zijn mobiele apps'),
        ('2015', 'Voorgesteld op **React.js Conf**; spec en referentie-implementatie **open source**'),
        ('2016', '**GitHub** lanceert een publieke GraphQL-API'),
        ('2018', '**GraphQL Foundation**, gehost door de Linux Foundation'),
        ('2021', 'Spec-editie **oktober 2021**; GraphQL.js v16'),
        ('2025', '**Spec-editie september 2025** (eerste in vier jaar); Apollo MCP Server; GraphQL AI Working Group'),
        ('2026', '**GraphQL.js v17** (juni); GraphQLConf: *"the language of AI"*; GraphiQL 6')]) + '</div>'
    + p('Niet enkel voor React of JavaScript: er zijn servers en clients in **vrijwel elke taal** (Java, C#, Python, Go, Rust, Kotlin, Swift, ...).', 31, '#595959'),
"""De geschiedenis in vogelvlucht. In 2012 begint Facebook GraphQL intern te gebruiken in zijn mobiele apps. In 2015 wordt het voorgesteld op React.js Conf en worden de specificatie en de referentie-implementatie in JavaScript open source gemaakt. In 2016 lanceert GitHub een publieke GraphQL-API, een belangrijk signaal dat het niet enkel iets voor Facebook was. In 2018 komt GraphQL onder de GraphQL Foundation, bij de Linux Foundation.

Dan wordt het een tijd stil rond de standaard: de editie van oktober 2021 blijft vier jaar lang de laatste. In september 2025 verschijnt eindelijk een nieuwe editie. Datzelfde jaar komt er een server waarmee AI-agents GraphQL-API's kunnen gebruiken, en een werkgroep rond AI. In 2026 verschijnt GraphQL.js versie 17, de referentie-implementatie, en heeft de jaarlijkse conferentie als thema GraphQL als de taal van AI.

Een misverstand om meteen uit de weg te ruimen: omdat GraphQL van Facebook komt en vaak met React gebruikt wordt, denken mensen dat het iets voor JavaScript is. Dat klopt niet. Er zijn servers en clients in vrijwel elke programmeertaal.""",
["2012 Facebook intern (mobiel) → 2015 React.js Conf + open source → 2016 GitHub publieke API → 2018 GraphQL Foundation",
 "Spec-editie okt. 2021 blijft 4 jaar de laatste; sept. 2025 nieuwe editie",
 "2025: Apollo MCP Server, AI Working Group; 2026: GraphQL.js v17, GraphQLConf 'the language of AI', GraphiQL 6",
 "Niet enkel React/JS: servers en clients in vrijwel elke taal",
 "→ Wie gebruikt het?"]))

A.append(slide('adoptie', 'Wie gebruikt GraphQL?',
    row(groot_getal('33%', 'van de ontwikkelaars gebruikt **GraphQL** (Postman *State of the API 2025*, via secundaire bronnen)'),
        groot_getal('93%', 'gebruikt **REST**: nog altijd de standaard'),
        groot_getal('100 mld+', 'GraphQL-aanroepen **per dag** bij Meta (GraphQLConf 2026)'), gap=40)
    + p('Op graphql.org: **Meta, AWS, Airbnb, Intuit, IBM, PayPal, The New York Times, Starbucks, Shopify, GitHub**, ...', 33)
    + p('GraphQL is breed gebruikt, maar **vervangt REST niet**. Ze bestaan naast elkaar (zie *Wanneer GraphQL?* achteraan).', 33, '#595959'),
"""Wie gebruikt GraphQL? Op de website staan onder meer Meta, AWS, Airbnb, Intuit, IBM, PayPal, The New York Times, Starbucks, Shopify en GitHub. Meta vertelde op GraphQLConf 2026 dat het om honderden miljarden GraphQL-aanroepen per dag gaat.

Hoe breed is het gebruik? Postman, de bekende tool om API's te testen, publiceert elk jaar een State of the API-rapport. Volgens de cijfers die daaruit geciteerd worden, gebruikt in 2025 ongeveer een derde van de respondenten GraphQL, tegenover 93 procent REST. Een kanttekening: ik heb die percentages gevonden in artikels over het rapport, niet in het rapport zelf.

De conclusie is wel duidelijk. GraphQL is breed gebruikt, maar het vervangt REST niet. De twee bestaan naast elkaar, vaak zelfs in hetzelfde bedrijf. Aan het einde van de les maken we een overzicht van wanneer je welke kiest.""",
["graphql.org: Meta, AWS, Airbnb, Intuit, IBM, PayPal, NYT, Starbucks, Shopify, GitHub",
 "Meta: honderden miljarden GraphQL-aanroepen per dag (GraphQLConf 2026)",
 "Postman State of the API 2025: GraphQL ±33%, REST 93% (via secundaire bronnen)",
 "GraphQL vervangt REST niet: ze bestaan naast elkaar",
 "→ Wat is REST precies?"],
bron='graphql.org; Postman State of the API 2025 (via digitalcxo.com); GraphQLConf 2026 wrap-up'))

# ---------------- REST ----------------
A.append(slide('kb-rest', 'REST: resources en URL\'s',
    p('**REST** (*Representational State Transfer*, Roy Fielding, 2000) is een **architectuurstijl**: data als **resources** met een eigen **URL**, bewerkt met **HTTP-methodes**.', 35)
    + row(
        col(code('''GET    /users       # alle gebruikers
GET    /users/3     # gebruiker 3
POST   /users       # nieuwe gebruiker
DELETE /users/3     # gebruiker 3 verwijderen''', 'http', 27),
            p('Een **stijl**, geen strikte specificatie: elke API pakt relaties, paginering en fouten anders aan.', 29, '#595959')),
        col(tabel(['Voordelen', 'Nadelen'],
                  [['Eenvoudig, snel op te zetten', 'Geen standaard voor relaties'],
                   ['Standaard HTTP: caching, statuscodes', 'Geen standaard voor ordening, paginering'],
                   ['Goed voor stabiele, publieke API\'s', 'Geen notificaties bij nieuwe data'],
                   ['', 'Over- en underfetching, versieproblemen']], [50, 50], size=27)), gap=40),
"""Om GraphQL te begrijpen, moeten we eerst kijken naar wat er vóór kwam: REST. REST staat voor Representational State Transfer en werd in 2000 beschreven door Roy Fielding in zijn doctoraat. Het is een architectuurstijl, geen strikte specificatie. Het idee: data wordt aangeboden als resources, elk met een eigen URL, en je bewerkt die met HTTP-methodes. GET slash users geeft alle gebruikers, GET slash users slash 3 gebruiker 3, POST maakt een nieuwe gebruiker aan, DELETE verwijdert er een.

Omdat REST een stijl is en geen specificatie, pakt elke API de details anders aan: hoe je relaties tussen data aanbiedt, hoe je pagineert of filtert, hoe je fouten teruggeeft. Wie al met een paar REST-API's gewerkt heeft, kent dat.

De voordelen: REST is eenvoudig en snel op te zetten, en je krijgt alles van HTTP gratis, zoals caching en statuscodes. Voor stabiele, publieke API's is het een uitstekende keuze. De nadelen: geen standaard voor relaties, ordening en paginering, geen ingebouwde notificaties bij nieuwe data, en twee problemen die we op de volgende slides bekijken: versies en over- en underfetching.""",
["REST = architectuurstijl (Roy Fielding, 2000), geen strikte specificatie",
 "Resources met eigen URL, bewerkt met HTTP-methodes (GET, POST, DELETE, ...)",
 "Elke API pakt relaties, paginering, fouten anders aan",
 "Voordelen: eenvoudig, HTTP-caching en statuscodes, goed voor stabiele publieke API's",
 "Nadelen: geen standaard voor relaties/paginering, geen notificaties, over-/underfetching, versies",
 "Examen: REST is een architectuurstijl, geen specificatie",
 "→ Het versieprobleem"],
kern=True))

A.append(slide('rest-versies', 'Het versieprobleem van REST',
    row(
        col(ul(['Endpoints worden vaak rond **schermen of clients** gebouwd',
                'Een wijziging in de frontend vraagt een aanpassing van de **backend**',
                'Een brekende wijziging → een **nieuwe versie**: `/api/v1/users`, `/api/v2/users`, ...',
                'Gevolg: **duplicatie**, moeilijk onderhoud, **trage iteratie**'], size=34)),
        col(card('GraphQL is versieloos', 'Je **voegt velden toe** zonder bestaande clients te breken. Oude velden markeer je met `@deprecated` en verwijder je pas als niemand ze nog gebruikt.', size=32),
            code('''type User {
  name: String!
  fullName: String!
    @deprecated(reason: "Gebruik name")
}''', 'graphql', 25), gap=20), gap=48),
"""Het eerste probleem: versies. REST-endpoints worden in de praktijk vaak rond specifieke schermen of clients gebouwd. Verandert de frontend, dan moet de backend mee. En als een wijziging bestaande clients zou breken, bijvoorbeeld een veld dat verdwijnt of van naam verandert, dan maak je een nieuwe versie: v1, v2, v3. Het gevolg: veel duplicatie van logica en code, moeilijk onderhoud omdat je oude versies moet blijven ondersteunen, en een trage samenwerking tussen frontend en backend.

GraphQL werkt versieloos. Omdat de client zelf kiest welke velden hij opvraagt, breekt een nieuw veld nooit een bestaande client: wie het niet vraagt, krijgt het niet. Wil je een veld weghalen, dan markeer je het eerst met de richtlijn deprecated en een reden. Tools tonen dan een waarschuwing, en je kan meten of nog iemand het veld gebruikt. Pas als dat niet meer zo is, verwijder je het.""",
["REST-endpoints rond schermen/clients → frontendwijziging = backendwerk",
 "Brekende wijziging → nieuwe versie (v1, v2, ...) → duplicatie, moeilijk onderhoud, trage iteratie",
 "GraphQL versieloos: nieuwe velden breken niets (wie het niet vraagt, krijgt het niet)",
 "Oude velden: @deprecated(reason: ...), meten, pas later verwijderen",
 "→ Een voorbeeld: een blogapp"]))

def _stap(nr, url, json_):
    return col(p(f'**{nr}.** `{url}`', 29), code(json_, 'json', 20), gap=10)

A.append(slide('rest-voorbeeld', 'Voorbeeld: een blogapp met REST',
    p('Het scherm toont de **naam** van Mary, de **titels van haar posts** en de **namen van haar laatste drie volgers**.', 33)
    + row(_stap(1, 'GET /users/<id>', '''{ "user": {
  "id": "er3tg439frjw",
  "name": "Mary",
  "address": { ... },
  "birthday": "July 30, 1987"
} }'''),
          _stap(2, 'GET /users/<id>/posts', '''{ "posts": [{
  "id": "ncwon3ce89hs",
  "title": "Learn GraphQL today",
  "content": "Lorem ipsum ...",
  "comments": [ ... ]
}, ...] }'''),
          _stap(3, 'GET /users/<id>/followers', '''{ "followers": [{
  "id": "leo83h2dojsu",
  "name": "John",
  "address": { ... },
  "birthday": "July 26, 1982"
}, ...] }'''), gap=28)
    + p('**Drie requests**, en elk antwoord bevat **veel meer** dan het scherm nodig heeft.', 33, '#C00000'),
"""Een concreet voorbeeld: een blogapp. Het scherm toont de naam van Mary, de titels van haar posts en de namen van haar laatste drie volgers. Hoe haal je die data op met een typische REST-API?

Eerste request: GET users met haar id. Je krijgt haar naam, maar ook haar adres, haar geboortedatum en alles wat het endpoint teruggeeft. Tweede request: GET users id posts. Je krijgt al haar posts, met per post niet alleen de titel maar ook de volledige inhoud en de reacties. Derde request: GET users id followers. Je krijgt alle volgers, met per volger hun adres en geboortedatum, terwijl je enkel de naam van de laatste drie nodig hebt.

Dat zijn drie round-trips naar de server, na elkaar of parallel, en in elk antwoord zit veel meer data dan het scherm toont. Op een trage mobiele verbinding merk je dat. Je kan natuurlijk een speciaal endpoint bouwen dat precies dit scherm bedient, maar dan zit je in het versieprobleem van de vorige slide: voor elk nieuw scherm een nieuw endpoint.""",
["Scherm: naam van Mary, titels van haar posts, namen van laatste 3 volgers",
 "REST: 3 requests (users/<id>, /posts, /followers)",
 "Elk antwoord bevat veel meer dan nodig (adres, geboortedatum, volledige posts, alle volgers)",
 "Speciaal endpoint per scherm kan, maar → versieprobleem",
 "→ Hetzelfde met GraphQL"]))

A.append(slide('gql-voorbeeld', 'Hetzelfde scherm met GraphQL',
    row(
        col(h3('Eén query: POST /graphql', 34), code('''query {
  user(id: "er3tg439frjw") {
    name
    posts { title }
    followers(last: 3) { name }
  }
}''', 'graphql', 28)),
        col(h3('Het antwoord', 34), code('''{
  "data": {
    "user": {
      "name": "Mary",
      "posts": [
        { "title": "Learn GraphQL today" }
      ],
      "followers": [
        { "name": "John" }, { "name": "Alice" },
        { "name": "Sarah" }
      ]
    }
  }
}''', 'json', 23)), gap=48)
    + p('**Eén request**, en het antwoord bevat **exact** wat het scherm nodig heeft.', 33, '#375623'),
"""Hetzelfde scherm met GraphQL. Links één query, gestuurd naar het enige endpoint. We vragen de gebruiker met dit id, daarvan de naam, van de posts enkel de titel, en van de laatste drie volgers enkel de naam. Het argument last met waarde drie zit gewoon in de query.

Rechts het antwoord. Kijk naar de vorm: die volgt de query precies. Een object user, met name, een lijst posts met elk een title, en een lijst followers met elk een name. Er zit geen adres in, geen geboortedatum, geen inhoud van de posts.

Eén request in plaats van drie, en exact de data die het scherm nodig heeft. En wil de frontend morgen ook het aantal reacties per post tonen, dan voegt ze dat veld toe aan de query. Zolang het veld in het schema bestaat, moet er aan de backend niets veranderen.""",
["Eén query naar POST /graphql: user(id) { name posts { title } followers(last: 3) { name } }",
 "Antwoord volgt exact de vorm van de query: geen adres, geen geboortedatum, geen inhoud",
 "1 request i.p.v. 3; exact de nodige data",
 "Nieuw veld nodig? Query aanpassen; backend hoeft niet te veranderen (als het in het schema zit)",
 "→ De begrippen: over- en underfetching"]))

A.append(slide('kb-fetching', 'Overfetching, underfetching en het N+1-probleem',
    row(
        col(h3('Overfetching', 38),
            ul(['De client krijgt **meer data dan nodig**',
                'Bv. een lijst met namen tonen, maar `/users` geeft ook geboortedatum en adres',
                'Verspilde bandbreedte, zeker op **mobiel**'], size=31)),
        col(h3('Underfetching en N+1', 38),
            ul(['Eén endpoint geeft **niet genoeg**: extra requests nodig',
                '**N+1**: 1 request voor de lijst + **N requests** voor de details van elk element',
                'Bv. de PokéAPI: `/pokemon` geeft namen en URL\'s; per Pokémon nog een request voor de details'], size=31)), gap=56)
    + card('GraphQL lost dit op aan de clientkant', 'De client vraagt exact de velden en relaties die hij nodig heeft, in **één request**. Het N+1-probleem **verhuist naar de server** (zie DataLoader).', size=31, flex='none'),
"""Drie begrippen die je moet kennen. Overfetching: de client krijgt meer data dan hij nodig heeft. Je wil een lijst met namen tonen, maar het endpoint slash users geeft ook de geboortedatum, het adres en de profielfoto van elke gebruiker. Dat is verspilde bandbreedte, en op een mobiele verbinding ook verspilde tijd en batterij.

Underfetching is het omgekeerde: een endpoint geeft niet genoeg informatie, dus de client moet extra requests doen. In het ergste geval krijg je het N+1-probleem: één request voor een lijst, en dan voor elk element in die lijst nog een request voor de details. Een bekend voorbeeld is de PokéAPI: het endpoint slash pokemon geeft een lijst met namen en URL's, en wil je van elke Pokémon de vaardigheden tonen, dan moet je voor elke Pokémon nog een request doen. Twintig Pokémon op een pagina, dan zijn dat eenentwintig requests.

GraphQL lost dit op aan de clientkant: de client vraagt in één request exact de velden en relaties die hij nodig heeft. Maar onthoud: het N+1-probleem verdwijnt niet, het verhuist naar de server. Hoe je het daar oplost, zien we bij DataLoader.""",
["Overfetching: meer data dan nodig (lijst met namen, maar ook geboortedatum, adres) → bandbreedte",
 "Underfetching: te weinig per request → extra requests",
 "N+1: 1 request voor lijst + N voor details (PokéAPI: 20 Pokémon → 21 requests)",
 "GraphQL: exact de nodige velden en relaties in één request",
 "Examen: N+1 verhuist naar de server → DataLoader",
 "→ Wat betekent dat voor ontwikkelsnelheid?"],
kern=True))

A.append(slide('iteraties', 'Snelle productiteraties',
    row(
        col(rood('REST', size=34),
            ul(['Endpoints rond **specifieke schermen**',
                'Nieuwe datacombinatie → vaak een **nieuw endpoint**',
                '**Frontendwijziging = backendwerk**'], size=33)),
        col(groen('GraphQL', size=34),
            ul(['De client kiest zelf **velden en relaties**',
                '**Eén endpoint** volstaat voor alle queries',
                'Backend verandert niet bij nieuwe UI-behoeften, zolang de data in het schema zit',
                '**Veel snellere iteraties**'], size=33)), gap=56),
"""Wat betekent dat voor de snelheid waarmee een team kan werken? Bij REST worden endpoints in de praktijk rond specifieke schermen gebouwd. Wil de frontend een nieuwe combinatie van data tonen, dan heb je vaak een nieuw endpoint nodig, of een aanpassing aan een bestaand endpoint. Elke frontendwijziging wordt zo backendwerk, en het frontendteam moet wachten op het backendteam.

Bij GraphQL kiest de client zelf welke velden en relaties hij nodig heeft, uit het schema. Eén endpoint volstaat voor alle queries. Zolang de data in het schema zit, hoeft de backend niets te veranderen als de gebruikersinterface verandert. Daardoor kunnen teams veel sneller itereren. Dat was een van de hoofdredenen waarom Facebook GraphQL ontwikkelde: honderden ontwikkelaars die tegelijk aan dezelfde app werkten, zonder op elkaar te moeten wachten.""",
["REST: endpoints per scherm; nieuwe combinatie → nieuw endpoint; frontendwijziging = backendwerk",
 "GraphQL: client kiest velden/relaties uit het schema; één endpoint; backend verandert niet zolang data in schema zit",
 "→ veel snellere iteraties; reden voor Facebook (honderden devs, niet op elkaar wachten)",
 "→ Het hart van GraphQL: het schema"]))

# ---------------- De taal ----------------
A.append(slide('kb-schema', 'Het schema: een contract tussen client en server',
    p('Elke GraphQL-server heeft een **schema**: een verzameling **types** en **velden** die je kan opvragen, met hun **type**.', 36)
    + row(
        col(ul(['De client weet precies **wat hij kan vragen**',
                'De server weet precies **wat hij moet teruggeven**',
                'Queries worden **gevalideerd vóór uitvoering**',
                'Zegt het schema `name: String!`, dan is het antwoord **nooit `null`** of een ander type'], size=32)),
        col(ul(['Frontend- en backendteams werken **onafhankelijk** zolang het schema gelijk blijft',
                'Het schema is **zelf bevraagbaar** (introspectie)',
                'Het schema is ook de **documentatie**'], size=32)), gap=48),
"""We komen bij het hart van GraphQL: het schema. Elke GraphQL-server heeft een schema: een verzameling types en velden die je kan opvragen, met voor elk veld het type.

Dat schema werkt als een contract tussen client en server. De client weet precies wat hij kan vragen, en de server weet precies wat hij moet teruggeven. Omdat het schema getypeerd is, kan een query gevalideerd worden voordat ze uitgevoerd wordt. Vraag je een veld dat niet bestaat, of geef je een tekst waar een getal verwacht wordt, dan krijg je meteen een duidelijke fout, en dat kan zelfs al in je editor, nog voor je de query verstuurt. En de server geeft garanties: zegt het schema dat name een String met uitroepteken is, dan is het antwoord nooit null en nooit een getal.

Rechts nog drie gevolgen. Frontend- en backendteams kunnen onafhankelijk werken zolang het schema hetzelfde blijft: de backend kan intern alles herschrijven, de frontend kan nieuwe queries schrijven zonder servercode te wijzigen. Het schema is zelf bevraagbaar, dat heet introspectie en zien we straks. En het schema is meteen ook de documentatie van de API.""",
["Schema = verzameling types en velden met hun type",
 "Contract: client weet wat hij kan vragen, server weet wat hij moet teruggeven",
 "Validatie vóór uitvoering (zelfs in de editor); garanties: String! is nooit null",
 "Teams werken onafhankelijk zolang schema gelijk blijft",
 "Schema is zelf bevraagbaar (introspectie) en is de documentatie",
 "Examen: waarom het schema een contract is",
 "→ Hoe schrijf je een schema?"],
kern=True))

A.append(slide('kb-sdl', 'Schema Definition Language (SDL)',
    row(
        col(code('''"""Een persoon die posts schrijft."""
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
}''', 'graphql', 27)),
        col(ul(['**Scalars**: `ID`, `String`, `Int`, `Float`, `Boolean` (en eigen, bv. `DateTime`)',
                '`!` = **non-null**: dit veld is nooit `null`',
                '`[Post!]!` = een lijst die nooit `null` is, met elementen die nooit `null` zijn',
                '**Relaties**: `Person.posts` en `Post.author` maken er een **graph** van',
                'Ook: `enum`, `interface`, `union`, `input`',
                '`"""..."""` = **description**: documentatie in het schema'], size=30)), gap=44),
"""Een schema schrijf je in de Schema Definition Language, kortweg SDL. Links een voorbeeld met twee types: Person en Post.

Een Person heeft een id, een naam, een leeftijd en een lijst posts. Een Post heeft een id, een titel en een auteur. Kijk naar de types. ID, String en Int zijn scalars: de basistypes. Daarnaast bestaan Float en Boolean, en je kan eigen scalars definiëren, bijvoorbeeld voor een datum.

Het uitroepteken betekent non-null: dit veld is nooit null. Bij posts staat er twee keer een uitroepteken: de lijst zelf is nooit null, en de elementen in de lijst zijn ook nooit null. Je krijgt dus hoogstens een lege lijst.

Het belangrijkste zijn de relaties. Person.posts verwijst naar Post, en Post.author verwijst terug naar Person. Zo ontstaat een graph, een netwerk van verbonden types, en daar komt de naam GraphQL vandaan. Je kan van een persoon naar zijn posts, van een post naar de auteur, van de auteur naar zijn andere posts, enzovoort.

Daarnaast bestaan er enums, interfaces, unions en input types voor argumenten. En de tekst tussen drie aanhalingstekens bovenaan is een description: documentatie die in het schema zelf zit. Onthoud dat, want voor AI-agents wordt dat heel belangrijk.""",
["SDL: types Person (id, name, age, posts) en Post (id, title, author)",
 "Scalars: ID, String, Int, Float, Boolean (+ eigen, bv. DateTime)",
 "! = non-null; [Post!]! = lijst nooit null, elementen nooit null",
 "Relaties Person.posts ↔ Post.author → een graph (naam GraphQL)",
 "Ook enum, interface, union, input; \"\"\"...\"\"\" = description (belangrijk voor agents)",
 "Examen: een SDL-schema lezen en schrijven, betekenis van ! en [ ]",
 "→ Data ophalen met queries"],
kern=True))

def _qa(q, a, qs=26, as_=22):
    return row(col(code(q, 'graphql', qs), flex='1'), pijl(44), col(code(a, 'json', as_), flex='1.4'), gap=20, align='center')

A.append(slide('queries', 'Data ophalen met queries',
    '<div style="display:flex;flex-direction:column;gap:22px">'
    + _qa('{\n  allPersons { name }\n}', '{ "data": { "allPersons": [\n  { "name": "Johnny" }, { "name": "Sarah" }, { "name": "Alice" } ] } }')
    + _qa('{\n  allPersons { name age }\n}', '{ "data": { "allPersons": [\n  { "name": "Johnny", "age": 23 },\n  { "name": "Sarah", "age": 20 }, { "name": "Alice", "age": 20 } ] } }')
    + _qa('{\n  allPersons(last: 2) {\n    name age\n  }\n}', '{ "data": { "allPersons": [\n  { "name": "Sarah", "age": 20 },\n  { "name": "Alice", "age": 20 } ] } }')
    + '</div>'
    + p('**De vorm van de query bepaalt de vorm van het antwoord.** Argumenten (`last: 2`) sturen het resultaat.', 32, '#595959'),
"""Nu de queries. Bovenaan de eenvoudigste: geef me van alle personen de naam. Het antwoord is een lijst met drie objecten, elk met enkel een name. In het midden voegen we het veld age toe aan de query, en meteen zit age ook in het antwoord. Laat je het weg, dan zit het er niet in. Dat is de kern: de vorm van de query bepaalt de vorm van het antwoord.

Onderaan geven we een argument mee: last met waarde twee. Dan krijgen we enkel de laatste twee personen. Velden kunnen argumenten hebben, en wat die betekenen, bepaalt het schema: hier last, maar het kan ook een filter, een sortering of een id zijn.

Ik heb deze queries met de referentie-implementatie, GraphQL.js versie 17, tegen het schema van de vorige slide uitgevoerd. Dit zijn de echte antwoorden. Merk ook op dat ze telkens in een object data zitten: daar komen we bij foutafhandeling op terug.""",
["{ allPersons { name } } → enkel namen",
 "+ age in de query → age in het antwoord: vorm query = vorm antwoord",
 "Argumenten: allPersons(last: 2) → laatste twee; betekenis bepaalt het schema",
 "Echte antwoorden (GraphQL.js 17); altijd binnen 'data'",
 "→ Relaties opvragen"]))

A.append(slide('queries-genest', 'Relaties opvragen: geneste queries',
    row(
        col(code('''{
  allPersons {
    name
    posts {
      title
    }
  }
}''', 'graphql', 30), flex='0.8'),
        col(code('''{ "data": { "allPersons": [
  { "name": "Johnny",
    "posts": [
      { "title": "GraphQL is awesome" },
      { "title": "Relay is a powerful GraphQL Client" }
    ] },
  { "name": "Sarah",
    "posts": [
      { "title": "How to get started with React & GraphQL" }
    ] },
  { "name": "Alice", "posts": [] }
] } }''', 'json', 25), flex='1.6'), gap=40)
    + p('In **één request** volg je de relatie `Person → Post`. Met REST waren dat 1 + N requests.', 33, '#595959'),
"""De echte kracht zit in relaties. Hier vragen we van alle personen de naam, en van hun posts de titel. Je ziet dat de query genest is: binnen allPersons staat posts, en daarbinnen title.

Het antwoord volgt die nesting. Johnny heeft twee posts, Sarah één, en Alice heeft er nog geen: een lege lijst. Merk op dat het een lege lijst is en geen null, omdat het schema zegt dat posts nooit null is.

In één request volgen we zo de relatie van persoon naar post. Met een klassieke REST-API was dat één request voor de lijst met personen, en dan per persoon een request voor de posts: het N+1-probleem van daarnet. En je kan dieper gaan: van de posts naar de auteur, of naar de reacties, of naar de auteurs van de reacties. Dat is wat een graph betekent. Dat brengt wel een risico mee, waar we in trend 3 op terugkomen: wat als iemand tien niveaus diep vraagt?""",
["Geneste query: allPersons { name posts { title } }",
 "Antwoord volgt nesting; Alice: lege lijst (niet null, want [Post!]!)",
 "Eén request volgt relatie Person → Post; met REST 1 + N requests",
 "Kan dieper (posts → author → ...) = een graph; risico van te diepe queries → trend 3",
 "→ Echte queries: variabelen, aliassen, fragmenten"]))

A.append(slide('kb-variabelen', 'Variabelen, aliassen en fragmenten',
    row(
        col(code('''query PersonCard($id: ID!) {
  eerste: person(by: { id: $id }) {
    ...PersonInfo
  }
  tweede: person(by: { name: "Sarah" }) {
    ...PersonInfo
  }
}

fragment PersonInfo on Person {
  name
  age
}''', 'graphql', 26), p('Variabelen: `{ "id": "1" }`', 27), gap=12),
        col(ul(['**Operatienaam** (`PersonCard`): voor logging, monitoring en caching',
                '**Variabelen** (`$id: ID!`) worden **apart** meegestuurd: de query zelf blijft vast',
                '**Aliassen** (`eerste:`): hetzelfde veld meerdere keren opvragen met andere argumenten',
                '**Fragmenten** (`...PersonInfo`): herbruikbare selectie van velden'], size=30)
            + code('''{ "data": {
  "eerste": { "name": "Johnny", "age": 23 },
  "tweede": { "name": "Sarah", "age": 20 } } }''', 'json', 22), gap=20), gap=40),
"""In echte applicaties schrijf je queries zoals deze. Vier begrippen.

Eén: de operatienaam, hier PersonCard. Die geeft de query een naam, wat handig is voor logging en monitoring: je ziet in je servers welke query traag is.

Twee: variabelen. In plaats van de id in de query te plakken, declareer je een variabele dollar id van het type ID met uitroepteken, en je stuurt de waarde apart mee, als JSON. De tekst van de query blijft daardoor altijd hetzelfde. Dat is belangrijk voor caching, en voor security: in trend 3 zien we dat je zo enkel vooraf goedgekeurde queries kan toelaten.

Drie: aliassen. Hier vragen we twee keer het veld person, met andere argumenten. Dat kan enkel als we ze een andere naam geven in het antwoord: eerste en tweede.

Vier: fragmenten. PersonInfo is een herbruikbare selectie van velden op het type Person: name en age. Met drie puntjes gebruik je het fragment. Fragmenten zijn de basis van hoe moderne clients werken, dat zien we bij de client.

Rechtsonder het echte antwoord: eerste is Johnny, de persoon met id 1, tweede is Sarah.""",
["Operatienaam (PersonCard): logging, monitoring, caching",
 "Variabelen ($id: ID!) apart meegestuurd → query-tekst blijft vast (caching, security: trusted documents)",
 "Aliassen (eerste:, tweede:): zelfde veld meermaals met andere argumenten",
 "Fragmenten (...PersonInfo): herbruikbare selectie; basis van moderne clients",
 "Examen: variabelen, aliassen en fragmenten herkennen en uitleggen",
 "→ Data wijzigen: mutations"],
kern=True))

A.append(slide('mutations', 'Data wijzigen: mutations',
    row(
        col(code('''mutation {
  createPerson(name: "Bob", age: 36) {
    id
    name
    age
  }
}''', 'graphql', 30),
            code('''{ "data": { "createPerson": {
  "id": "4", "name": "Bob", "age": 36
} } }''', 'json', 25), gap=20),
        col(ul(['Drie soorten: **aanmaken** (create), **aanpassen** (update), **verwijderen** (delete)',
                'Een mutation geeft **zelf ook data terug**, in de vorm die de client vraagt',
                'Vaak vraag je enkel het nieuwe `id` op, of de velden die je scherm moet bijwerken',
                'Mutations in één request worden **na elkaar** uitgevoerd (queries mogen parallel)'], size=31)), gap=48),
"""Lezen doe je met queries, wijzigen met mutations. Er zijn drie soorten: data aanmaken, aanpassen en verwijderen. De R van CRUD, read, zijn de queries.

Links maken we een nieuwe persoon aan: Bob, 36 jaar. Het bijzondere is dat een mutation ook zelf data teruggeeft, in de vorm die de client vraagt. Hier vragen we het nieuwe id, de naam en de leeftijd terug, en dat krijgen we in het antwoord eronder: Bob heeft id 4 gekregen. Vaak vraag je enkel het nieuwe id op, of net de velden die je scherm moet bijwerken, zodat je geen tweede request nodig hebt.

Een technisch verschil met queries: als je in één request meerdere mutations stuurt, voert de server ze na elkaar uit, in de volgorde van de request. Velden van een query mogen parallel uitgevoerd worden, want lezen heeft geen bijwerkingen.""",
["Mutations: aanmaken, aanpassen, verwijderen (CRUD zonder R)",
 "createPerson(name: \"Bob\", age: 36) { id name age } → id 4 terug",
 "Mutation geeft zelf data terug in de gevraagde vorm (vaak enkel id of velden voor het scherm)",
 "Meerdere mutations in één request: na elkaar; queryvelden mogen parallel",
 "→ Realtime: subscriptions"]))

A.append(slide('subscriptions', 'Realtime: subscriptions',
    row(
        col(code('''subscription {
  newPerson {
    name
    age
  }
}''', 'graphql', 30)),
        col(ul(['Een **realtime verbinding** met de server',
                'De server **pusht** data naar de client bij een gebeurtenis',
                'Een **stroom** van resultaten, geen request-response',
                'In de praktijk via **WebSockets** (protocol `graphql-ws`) of **Server-Sent Events**',
                'Bv. chat, notificaties, live scores, dashboards'], size=32)), gap=48),
"""Het derde soort operatie: subscriptions. Een subscription is een realtime verbinding met de server. In plaats van te vragen en een antwoord te krijgen, abonneer je je op een gebeurtenis, en de server pusht data naar de client telkens die gebeurtenis plaatsvindt. Hier: telkens er een nieuwe persoon bijkomt, krijg ik zijn naam en leeftijd. Het is dus een stroom van resultaten, geen request-response.

In de praktijk loopt dat over WebSockets, met het protocol graphql-ws, of over Server-Sent Events, een eenvoudigere techniek waarbij de server over een open HTTP-verbinding berichten stuurt.

Typische toepassingen zijn chatberichten, notificaties, live scores en dashboards. Voor gewone data, die niet elke seconde verandert, gebruik je beter gewone queries: een subscription houdt een verbinding open, en dat kost aan de serverkant geheugen en capaciteit.""",
["Subscription = realtime verbinding; server pusht data bij een gebeurtenis",
 "Stroom van resultaten, geen request-response",
 "Transport: WebSockets (graphql-ws) of Server-Sent Events",
 "Toepassingen: chat, notificaties, live scores, dashboards; anders gewone queries (open verbinding kost capaciteit)",
 "→ Hoe staan deze ingangspunten in het schema?"]))

A.append(slide('kb-root-types', 'De root types: Query, Mutation en Subscription',
    row(
        col(code('''type Query {
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
}''', 'graphql', 25), flex='1.35'),
        col(ul(['Drie speciale **root types** zijn de **ingangspunten** van de API',
                'Elk veld op een root type is een **operatie** met argumenten en een returntype',
                'De types van de argumenten moeten **kloppen** met de rest van het schema'], size=30)
            + card('Het schema vangt fouten', 'Met `age: String!` in `createPerson` zou `createPerson(name: "Bob", age: 36)` geweigerd worden: *String cannot represent a non string value*.', size=27), gap=20), gap=40),
"""De queries en mutations van daarnet werken pas als het schema de ingangspunten definieert. Daarvoor zijn er drie speciale types, de root types: Query, Mutation en Subscription.

Het type Query bevat alle velden waarmee je kan beginnen te lezen: allPersons en allPosts, elk met een optioneel argument last. Het type Mutation bevat alle wijzigingen: createPerson met een verplichte naam en leeftijd, updatePerson met een verplicht id en optionele naam en leeftijd, en deletePerson. Elk geeft de betrokken persoon terug. En Subscription bevat newPerson.

Let op de types van de argumenten: die moeten kloppen met de rest van het schema. Leeftijd is in Person een Int, dus ook in createPerson. Zou je daar per vergissing String schrijven, dan weigert de server de mutation createPerson met leeftijd 36, met de fout String cannot represent a non string value. Dat is het voordeel van een getypeerd schema: zo'n fout zie je meteen, en niet pas als er rare data in je databank zit.""",
["Root types Query, Mutation, Subscription = ingangspunten van de API",
 "Elk veld = operatie met argumenten en returntype (allPersons(last: Int), createPerson(name: String!, age: Int!), ...)",
 "Argumenttypes moeten kloppen met de rest van het schema (age: Int!)",
 "Fout type (age: String!) → mutation met 36 geweigerd: getypeerd schema vangt fouten meteen",
 "Examen: een volledig schema met root types kunnen lezen en schrijven",
 "→ Hoe kent een client het schema? Introspectie"],
kern=True))

A.append(slide('kb-introspectie', 'Introspectie: het schema opvragen',
    row(
        col(code('''{
  __type(name: "Person") {
    name
    fields {
      name
      type { name kind }
    }
  }
}''', 'graphql', 28),
            p('Velden van `Person`: `id`, `name`, `age`, `posts`, `followers`', 27, '#595959'), gap=14),
        col(ul(['De server kent het schema, de client niet: met **introspectie** vraag je het schema op **met een gewone query** (`__schema`, `__type`)',
                'Maakt tools mogelijk: **GraphiQL** (IDE in de browser, versie 6 in november 2026), autocomplete, **codegeneratie**',
                'Recent: **AI-agents** ontdekken zelf wat een API kan (trend 4)',
                'Maar ook een **securityrisico** als het schema te veel verraadt (trend 3)'], size=30)), gap=44),
"""De server kent het schema, maar hoe weet de client wat er bestaat? Met introspectie. Je vraagt het schema op met een gewone GraphQL-query, via speciale velden die met twee underscores beginnen: double underscore schema voor het volledige schema, double underscore type voor één type.

Links vragen we het type Person op, met de naam en het type van elk veld. Het antwoord van onze testserver: id, name, age, posts en followers.

Introspectie maakt een hele reeks tools mogelijk. GraphiQL is een IDE in de browser waarin je queries schrijft met autocomplete en documentatie, allemaal op basis van introspectie. In november 2026 verscheen versie 6. Codegeneratoren maken er TypeScript-types van. En recent: AI-agents gebruiken introspectie om zelf te ontdekken wat een API kan. Dat is de kern van trend 4.

Maar introspectie is ook een risico. Als je schema interne velden bevat die niet voor het publiek bedoeld zijn, toont introspectie die aan iedereen. Daarom schakelen veel teams introspectie uit voor publieke clients. In trend 3 zien we waarom dat op zich niet volstaat.""",
["Introspectie = schema opvragen met een gewone query (__schema, __type)",
 "Voorbeeld: __type(name: \"Person\") → id, name, age, posts, followers",
 "Maakt tools mogelijk: GraphiQL (v6, nov. 2026), autocomplete, codegeneratie",
 "AI-agents ontdekken zo zelf wat een API kan (trend 4)",
 "Risico: verraadt interne velden → vaak uit voor publieke clients (trend 3)",
 "Examen: wat introspectie is en waarvoor het gebruikt wordt",
 "→ Hoe ziet een antwoord met een fout eruit?"],
kern=True))

A.append(slide('kb-antwoord', 'De vorm van een antwoord: data en errors',
    row(
        col(code('''{
  "data": {
    "user": { "name": "Mary", "posts": null }
  },
  "errors": [{
    "message": "Posts service unavailable",
    "path": ["user", "posts"]
  }]
}''', 'json', 26)),
        col(ul(['Altijd een object met **`data`** en eventueel **`errors`**',
                '**Gedeeltelijke resultaten**: één veld faalt, de rest komt toch',
                '`path` toont **welk veld** faalde',
                'Faalt een **non-null** veld (`!`), dan wordt de ouder `null`: *null bubbling* (trend 1)',
                'Over HTTP vaak altijd status **200**; de *GraphQL over HTTP*-spec (draft) geeft statuscodes betekenis met `application/graphql-response+json`'], size=29)), gap=44),
"""Hoe ziet een antwoord eruit als er iets misgaat? Een GraphQL-antwoord heeft altijd dezelfde vorm: een object met data, en eventueel errors.

Het bijzondere is dat GraphQL gedeeltelijke resultaten kan teruggeven. In het voorbeeld werkt de naam van Mary, maar de dienst die de posts levert is onbereikbaar. Je krijgt dan toch de naam, posts wordt null, en in errors staat de foutmelding met een path: het pad naar het veld dat faalde, hier user, posts. De client kan dus het deel van het scherm tonen dat wel werkt.

Een belangrijke regel: als een veld faalt dat non-null is, met een uitroepteken, dan mag het geen null zijn. De null wordt dan doorgegeven naar het ouderobject, en als dat ook non-null is, naar diens ouder, enzovoort. Dat heet null bubbling, en het kan een groot deel van het antwoord wissen. In trend 1 zien we hoe de standaard dat probeert op te lossen.

Over HTTP gaf een GraphQL-server traditioneel altijd status 200, ook bij fouten, wat monitoring lastig maakt. De specificatie GraphQL over HTTP, nog een draft, introduceert daarom het mediatype application graphql-response plus json, waarbij de statuscode wel iets betekent.""",
["Antwoord = { data, errors? }",
 "Gedeeltelijke resultaten: posts faalt → null + fout in errors met path [user, posts]",
 "Non-null veld faalt → null gaat naar de ouder: null bubbling (trend 1)",
 "HTTP traditioneel altijd 200; GraphQL over HTTP (draft): application/graphql-response+json met betekenisvolle statuscodes",
 "Examen: de vorm van een antwoord met gedeeltelijke fout kunnen uitleggen",
 "→ Hoe beantwoordt de server dit? Eerst de architectuur"],
kern=True))

# ---------------- Server ----------------
def _srv(label):
    return card(label, size=26, flex='none')

A.append(slide('architecturen', 'Drie architecturen voor een GraphQL-server',
    row(
        col(card('1. Met eigen databank', 'Typisch voor nieuwe projecten (*greenfield*). De server leest en schrijft rechtstreeks in de databank.', size=30),
            p('Client → **GraphQL-server** → databank', 29, '#7F0000'), gap=16),
        col(card('2. Laag boven bestaande systemen', 'Verenigt legacy systemen, microservices en externe API\'s achter **één schema**. De complexiteit zit achter de server.', size=30),
            p('Client → **GraphQL** → legacy, microservices, externe API\'s', 29, '#7F0000'), gap=16),
        col(card('3. Hybride', 'Een eigen databank **én** bestaande systemen. In de praktijk het meest voorkomend.', size=30),
            p('Client → **GraphQL + databank** → legacy, externe API\'s', 29, '#7F0000'), gap=16), gap=32)
    + p('Voor de client maakt het **niet uit** waar de data vandaan komt: hij ziet één schema.', 33, '#595959'),
"""Hoe ziet een GraphQL-server eruit? Er zijn drie typische architecturen.

Eén: een GraphQL-server met een eigen databank. Dat zie je vooral bij nieuwe projecten, greenfield. De server ontvangt de query, haalt de data uit de databank en bouwt het antwoord.

Twee: GraphQL als laag boven bestaande systemen. Veel bedrijven hebben een oud systeem, een paar microservices en externe API's van leveranciers. Een GraphQL-server kan die allemaal achter één schema verenigen. De client ziet één nette API; alle complexiteit, zoals verschillende protocollen en dataformaten, zit verborgen achter de server.

Drie: een hybride, met een eigen databank én bestaande systemen. In de praktijk is dat het meest voorkomend.

Het belangrijkste punt staat onderaan: voor de client maakt het niet uit waar de data vandaan komt. Hij ziet één schema. Hoe de server dat mogelijk maakt, zien we op de volgende slide: met resolvers.""",
["1. Eigen databank: greenfield, server leest/schrijft rechtstreeks",
 "2. Laag boven bestaande systemen: legacy, microservices, externe API's achter één schema",
 "3. Hybride: databank + bestaande systemen (meest voorkomend)",
 "Client ziet één schema, ongeacht de bron",
 "→ Hoe? Resolvers"]))

A.append(slide('kb-resolvers', 'Resolvers: één functie per veld',
    row(
        col(code('''query {
  user(id: "er3tg4sa9frj") {
    name
    followers(first: 5) {
      name
      age
    }
  }
}''', 'graphql', 23),
            code('''const resolvers = {
  Query: {
    user: (_, { id }) => db.users.findById(id),
  },
  User: {
    followers: (user, { first }) =>
      db.followers.forUser(user.id, first),
  },
};''', 'js', 22), gap=12, flex='1.2'),
        col(ul(['**Elk veld** heeft een **resolver**: een functie die weet waar en hoe de data gehaald wordt',
                'De server **valideert** de query en voert per gevraagd veld de resolver uit',
                'Een resolver krijgt de **ouder** (`user`) en de **argumenten** (`first`)',
                'Velden zonder eigen resolver (`name`, `age`) lezen gewoon de property',
                'Elke resolver mag een **andere bron** hebben: databank, REST-API, cache, ...'], size=29)), gap=40),
"""Hoe beantwoordt een server een query? Met resolvers. Elk veld in het schema heeft een resolver: een functie die weet waar en hoe de data voor dat veld gehaald wordt.

Links bovenaan een query: de gebruiker met dit id, zijn naam, en van zijn eerste vijf volgers de naam en leeftijd. Daaronder de resolvers in JavaScript. De resolver van Query.user krijgt de argumenten, hier id, en haalt de gebruiker uit de databank. De resolver van User.followers krijgt als eerste argument de ouder, het object user dat de vorige resolver teruggaf, en als tweede argument de argumenten van het veld, hier first.

Wat gebeurt er als de query binnenkomt? De server valideert eerst de query tegen het schema. Daarna voert hij voor elk gevraagd veld de bijhorende resolver uit, van boven naar beneden: eerst user, dan voor die user de followers, dan voor elke follower name en age. Velden zonder eigen resolver, zoals name en age, lezen gewoon de gelijknamige property van het object. Alle resultaten worden samengevoegd tot één antwoord in de vorm van de query.

Het krachtige is dat elke resolver een andere bron mag hebben. User kan uit een SQL-databank komen, followers uit een REST-API van een andere dienst, en een veld met de koers van een aandeel uit een cache. Zo combineert GraphQL data uit verschillende systemen in één antwoord.""",
["Elk veld heeft een resolver: functie die weet waar/hoe de data gehaald wordt",
 "Server valideert, voert dan per gevraagd veld de resolver uit (boven naar beneden)",
 "Resolver krijgt ouder (user) en argumenten (first); velden zonder resolver lezen de property",
 "Elke resolver mag andere bron hebben (DB, REST, cache) → data combineren in één antwoord",
 "Examen: werking van resolvers kunnen uitleggen met een voorbeeld",
 "→ Het N+1-probleem op de server"],
kern=True))

A.append(slide('kb-dataloader', 'Het N+1-probleem op de server: DataLoader',
    row(
        col(code('{\n  allPosts {\n    title\n    author { name }\n  }\n}', 'graphql', 26),
            p('`Post.author` loopt **één keer per post**: 1 query voor de lijst + **N** voor de auteurs.', 29), gap=14, flex='0.85'),
        col(code('''const userLoader = new DataLoader(async (ids) => {
  const users = await db.users.findByIds(ids); // één query
  return ids.map((id) => users.find((u) => u.id === id));
});

const resolvers = {
  Post: { author: (post) => userLoader.load(post.authorId) },
};''', 'js', 23),
            tabel(['3 posts, auteurs ophalen', 'Databank-aanroepen'],
                  [['Zonder DataLoader', '**3**'], ['Met DataLoader', '**1**']], [60, 40], size=27), gap=16, flex='1.6'), gap=36)
    + p('**DataLoader** verzamelt alle `load(id)`-aanroepen binnen één tick (**batching**) en ontdubbelt ze (**cache per request**).', 30, '#595959'),
"""Daarnet zei ik dat het N+1-probleem naar de server verhuist. Hier is het. Links een onschuldige query: alle posts, met de titel en de naam van de auteur. Maar de resolver van Post.author loopt één keer per post. Met drie posts zijn dat één query voor de lijst en drie queries voor de auteurs. Met duizend posts: duizend en één queries naar de databank, voor één request van de client.

De standaardoplossing heet DataLoader, een kleine bibliotheek die oorspronkelijk van Facebook komt. Rechts zie je hoe het werkt. Je maakt een loader met een functie die een lijst id's krijgt en in één query alle gebruikers ophaalt. In de resolver roep je niet meer rechtstreeks de databank aan, maar userLoader.load met het id van de auteur.

Wat gebeurt er dan? DataLoader verzamelt alle load-aanroepen die binnen dezelfde tick van de event loop gebeuren, dat heet batching, en voert dan één keer de functie uit met alle id's samen. Dubbele id's worden ontdubbeld: twee posts van dezelfde auteur geven één opzoeking.

Ik heb dit getest met GraphQL.js 17 en drie posts: zonder DataLoader drie databank-aanroepen voor de auteurs, met DataLoader één. Elke serieuze GraphQL-server gebruikt dit patroon of iets gelijkaardigs.""",
["allPosts { title author { name } }: Post.author loopt per post → 1 + N queries (1.000 posts → 1.001)",
 "DataLoader (oorspronkelijk Facebook): batch-functie met lijst id's → één query",
 "Resolver: userLoader.load(post.authorId) i.p.v. rechtstreeks de DB",
 "Batching binnen één tick + ontdubbelen (cache per request)",
 "Getest (GraphQL.js 17, 3 posts): 3 aanroepen → 1",
 "Examen: N+1 op de server en DataLoader kunnen uitleggen",
 "→ De client"],
kern=True))

# ---------------- Client ----------------
A.append(slide('kb-declaratief', 'De client: declaratieve data fetching',
    row(
        col(rood('Imperatief (klassiek, bv. met fetch)', size=32),
            ul(['Bouw een HTTP-request', 'Wacht op het antwoord', 'Parse de data', 'Bewaar ze lokaal en houd ze **zelf** up-to-date',
                'Kan ook met GraphQL, maar dan doe **jij** alles'], size=30)),
        col(groen('Declaratief (met een GraphQL-client)', size=32),
            ul(['Beschrijf in een query **welke data** een component nodig heeft',
                'De bibliotheek doet de rest: ophalen, **caching**, de UI bijwerken',
                'Minder boilerplate, minder fouten, meer focus op de UI'], size=30)
            + p('Bekende clients: **Apollo Client** (v4, 2025), **Relay** (Meta), **urql**', 29, '#595959')), gap=48),
"""Dan de clientkant. Je kan een GraphQL-API perfect aanroepen met een gewone fetch: een POST-request met de query als JSON. Maar dan doe je alles zelf, op een imperatieve manier: je bouwt het request, wacht op het antwoord, parset de data, bewaart ze lokaal, en houdt ze zelf up-to-date als er iets verandert.

De declaratieve aanpak gebruikt een GraphQL-client. Je beschrijft in een query welke data een component nodig heeft, en de bibliotheek doet de rest: de data ophalen, ze cachen, en de gebruikersinterface bijwerken als de data verandert, bijvoorbeeld na een mutation. Dat betekent minder boilerplate, minder fouten en meer focus op de interface.

Dit is hetzelfde idee als declaratief versus imperatief in de les over web frameworks: je beschrijft wat je wil, niet hoe. De bekendste clients zijn Apollo Client, waarvan in 2025 versie 4 verscheen, Relay van Meta, dat met een compiler werkt, en urql, een lichtere variant.""",
["Imperatief (fetch): request bouwen, wachten, parsen, lokaal bewaren, zelf up-to-date houden",
 "Declaratief (GraphQL-client): query beschrijft data per component; bibliotheek haalt op, cachet, werkt UI bij",
 "Zelfde idee als declaratief vs. imperatief bij web frameworks",
 "Clients: Apollo Client (v4, 2025), Relay (Meta, compiler), urql",
 "Examen: imperatief vs. declaratief data fetching",
 "→ Hoe weet een component welke data het nodig heeft? Fragmenten"],
kern=True))

A.append(slide('colocation', 'Fragment colocation: elk component vraagt zijn eigen data',
    row(
        col(code('''# FriendListItem.tsx
fragment FriendListItem on User {
  id
  name
  profilePic
}

# FriendList.tsx
query FriendList {
  me {
    friends { ...FriendListItem }
  }
}''', 'graphql', 26)),
        col(ul(['Elk component declareert zijn **data-behoefte als fragment**, naast zijn code',
                'De ouder stelt de fragmenten samen tot **één query**',
                'Voegt `FriendListItem` een veld toe, dan pas je **enkel dat fragment** aan',
                '**Data masking** (Relay, Apollo Client 4): een component ziet enkel de velden uit zijn eigen fragment'], size=31)), gap=48),
"""Een patroon dat je in grote applicaties overal ziet: fragment colocation. Colocation betekent dat dingen die samen horen, ook samen staan.

Elk component declareert zijn eigen data-behoefte als een fragment, in hetzelfde bestand als de code van het component. Het component FriendListItem toont een vriend met naam en profielfoto, dus het definieert een fragment op User met id, name en profilePic. Het component FriendList toont een lijst van vrienden, en stelt zijn query samen door het fragment van FriendListItem te gebruiken. De client stuurt uiteindelijk één query naar de server.

Het voordeel: wil FriendListItem morgen ook de stad tonen, dan pas je enkel dat fragment aan. De ouder hoeft niet te weten welke velden zijn kinderen nodig hebben.

Relay en Apollo Client 4 gaan nog een stap verder met data masking: een component krijgt enkel de velden uit zijn eigen fragment te zien, ook al zitten er meer in het antwoord. Zo kan een component niet per ongeluk afhankelijk worden van data die een ander component opvraagt. graphql.org noemt dit data colocation, en het is een van de redenen waarom GraphQL goed werkt in heel grote frontends.""",
["Colocation: data-behoefte als fragment naast de code van het component",
 "Ouder stelt fragmenten samen tot één query (FriendList gebruikt ...FriendListItem)",
 "Veld toevoegen → enkel het fragment aanpassen; ouder hoeft het niet te weten",
 "Data masking (Relay, Apollo Client 4): component ziet enkel zijn eigen velden",
 "→ Types genereren uit het schema"],
bron='graphql.org (data colocation); Apollo Client 4'))

A.append(slide('codegen', 'Codegeneratie: types uit het schema',
    row(
        col(ul(['Het schema is getypeerd: types **met de hand** bijhouden is zonde',
                'Problemen bij handwerk: **verouderde** types, **tikfouten**, **onvolledige** typing',
                'Tools genereren **TypeScript-types** uit schema en queries:',
                '**GraphQL Code Generator** (The Guild)',
                '**gql.tada**: types afgeleid in TypeScript zelf, zonder build-stap',
                '**Relay compiler**'], size=31)),
        col(code('''// gegenereerd (vereenvoudigd)
export type PersonCardQuery = {
  eerste: { name: string; age: number } | null;
  tweede: { name: string; age: number } | null;
};''', 'ts', 25),
            p('Verandert het schema, dan geeft de **compiler** meteen fouten in de frontend.', 30, '#595959'), gap=16), gap=44),
"""Een laatste stuk van de client: codegeneratie. Het schema is sterk getypeerd, en de queries ook. Het zou zonde zijn om in je frontend de TypeScript-types nog eens met de hand te schrijven. Dat leidt tot verouderde types als het schema verandert, tikfouten en onvolledige typing.

Daarom genereren tools de types uit het schema en je queries. De bekendste is GraphQL Code Generator van The Guild. Een nieuwere aanpak is gql.tada, dat de types rechtstreeks in TypeScript afleidt, zonder aparte build-stap. En Relay heeft een eigen compiler die dit doet.

Rechts een voorbeeld van wat er gegenereerd wordt voor de query PersonCard van daarnet: eerste en tweede, elk met een name als string en een age als number, of null als de persoon niet gevonden wordt. Verandert het schema, bijvoorbeeld omdat age verdwijnt, dan geeft de TypeScript-compiler meteen een fout op elke plaats in de frontend die dat veld gebruikt. Zo vind je de gevolgen van een schemawijziging voordat je gebruikers ze vinden.""",
["Schema en queries zijn getypeerd → TS-types met de hand = verouderd, tikfouten, onvolledig",
 "Tools: GraphQL Code Generator (The Guild), gql.tada (zonder build-stap), Relay compiler",
 "Voorbeeld: gegenereerd type voor PersonCard (name: string, age: number, of null)",
 "Schemawijziging → compilerfout in de frontend: gevolgen vinden vóór de gebruiker",
 "→ Einde van de basis; nu de trends. Trend 1: de standaard"],
bron='the-guild.dev/graphql/codegen; gql-tada.0no.co'))
