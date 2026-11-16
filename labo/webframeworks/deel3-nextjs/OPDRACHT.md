# Deel 3: Next.js 16 (40 minuten)

**Theorie:**
- slide 10–13: CSR en SSR, hydration, SSG en streaming, React Server Components
- slide 38–41: navigatie, caching, Cache Components, Instant Navigations
- slide 47–50: security-begrippen, de Server Action als publiek endpoint, serialisatie, React2Shell
- slide 58 en 64: AGENTS.md, prompt injection

## Leerdoelen

- Je kan aantonen welke code op de server draait en welke in de browser.
- Je kan bij uncached data bewust kiezen tussen *stream*, *cache* en *block*, en een cache gericht ongeldig maken.
- Je kan aantonen dat een Server Action een publiek endpoint is, en controleren of ze correct beveiligd is.
- Je kan inschatten welke risico's een coding agent met zich meebrengt, en hoe je die beperkt.

## Het project

Open de map `deel3-nextjs` als projectmap en start een nieuwe sessie in je agent. Het project is gemaakt met `create-next-app` (Next.js 16.4, met Cache Components en de React Compiler aan, zie `next.config.ts`).

| Bestand | Wat |
|---|---|
| `app/boeken/page.tsx` | de lijst met boeken |
| `app/boeken/boeken-zoeker.tsx` | zoekveld en lijst, met een knop *Verwijder* voor beheerders |
| `app/boeken/nieuw-boek.tsx` | formulier om een boek toe te voegen |
| `app/beheer/page.tsx` | *Aanmelden*: wissel tussen de rol *lezer* en *beheerder* |
| `app/acties.ts` | de Server Actions |
| `lib/db.ts` | nep-database: een JSON-bestand in `data/`, met een trage query (1,5 s) |
| `lib/sessie.ts` | leest je rol uit een cookie |
| `AGENTS.md` | instructies voor coding agents: bovenaan het blok van `create-next-app`, onderaan de regels voor dit labo |

> **Afspraak:** *Aanmelden* is een simulatie. Doe alsof je daar met een wachtwoord inlogt.
>
> **Opnieuw beginnen?** Stop de server en verwijder de mappen `data` en `.next`.

## 3.1 Server of client? (7 min)

**[Agent · Plan]**

```text
Teken de componentenboom van de route /boeken als tekstboom. Duid bij elk component aan of het een Server Component of een Client Component is, en waaraan je dat ziet. Wijzig niets.
```

**[Zelf]**
1. Controleer het antwoord van de agent door zelf te zoeken naar `'use client'` en `'use server'`. Klopt het?
2. Start `npm run dev` en open http://localhost:3000/boeken.
   - **Noteer** waar `[db] boeken opgehaald om …` verschijnt: in de terminal, in de browserconsole, of allebei?
   - Staan de titels al in de paginabron (Ctrl+U)?
   - Zoek in DevTools › *Sources* naar `boeken opgehaald`: zit die code in het JavaScript van de browser?
3. **Experiment.** Voeg in `boeken-zoeker.tsx` bovenaan `import { haalBoekenOp } from '@/lib/db'` toe, en in de functie `console.log(haalBoekenOp)`.
   - Voer `npm run build` uit en **noteer** de foutmelding.
   - Zet daarna `import 'server-only'` als eerste regel in `lib/db.ts`, bouw opnieuw en **noteer** de nieuwe foutmelding.
   - Haal de import en de `console.log` weer weg. Laat `server-only` staan.

## 3.2 Stream en cache (9 min)

**[Zelf]** Voer `npm run build` uit. De build faalt. **Noteer** de drie oplossingen die Next.js voorstelt, en de **twee** dingen in `app/boeken/page.tsx` die het probleem veroorzaken.

**[Agent · Uitvoeren]**

```text
npm run build faalt op de route /boeken. Los dit op met stream én cache, volgens de documentatie van deze Next.js-versie (zie AGENTS.md):
- Verplaats het ophalen van de boeken en de rol naar een async component Boekenlijst in app/boeken/page.tsx, binnen een <Suspense> met als fallback <p className="kaart">Boeken laden…</p>. De titel en het formulier blijven erbuiten.
- Cache haalBoekenOp in lib/db.ts met 'use cache', cacheLife('hours') en cacheTag('boeken').
Voer daarna npm run build uit en toon de routetabel.
```

*Terwijl de agent werkt:* begin aan reflectievraag 1.

**[Zelf]**
1. Bekijk de diff. Heeft de agent de documentatie in `node_modules/next/dist/docs` gelezen, zoals `AGENTS.md` vraagt? Je ziet in het verloop van de sessie welke bestanden hij las.
2. **Noteer** de routetabel: welk symbool krijgen `/` en `/boeken`, en wat betekenen ze?
3. Stop de dev server en start de productieversie met `npm start`. Open `/boeken` twee keer met het tabblad *Network* open.
   - **Noteer** hoe snel je de lijst ziet, en hoeveel `[db]`-regels er in de terminal staan.
   - Waarom stond er al een `[db]`-regel in de uitvoer van de build?

## 3.3 Wijzigen en de cache ongeldig maken (5 min)

**[Zelf]** Voeg in de productieversie een boek toe. Verschijnt het? En na herladen? **Noteer** wat je ziet.

**[Agent · Uitvoeren]**

```text
Een toegevoegd of verwijderd boek moet meteen zichtbaar zijn voor de gebruiker die de wijziging deed. Gebruik daarvoor de juiste functie uit next/cache in app/acties.ts.
```

**[Zelf]**
1. Bekijk de diff. **Noteer** welke functie de agent koos (`updateTag`, `revalidateTag` of `revalidatePath`) en hoe hij die keuze verantwoordde.
2. `npm run build`, `npm start` en test opnieuw.

## 3.4 Een Server Action is een publiek endpoint (11 min)

**[Zelf] De aanval.**
1. Ga naar *Aanmelden* en word **beheerder**. Open `/boeken` met het tabblad *Network* open en verwijder één boek.
   **Noteer** voor het request: de methode, de URL, de header `Next-Action` en de body.
2. Rechtsklik op het request › *Copy* › *Copy as fetch*.
3. Word **lezer**: de knoppen *Verwijder* zijn weg. Plak de `fetch` in de console, vervang in de `body` het id door dat van een ander boek, voer hem uit en herlaad.
   **Noteer** het resultaat.

**[Agent · Uitvoeren] De verdediging.**

```text
Beveilig de Server Actions in app/acties.ts. Elke action moet zelf controleren wie de gebruiker is, of die de actie mag uitvoeren, en of de input geldig is:
- verwijderBoek: enkel voor beheerders; het id moet een geheel getal zijn.
- voegBoekToe: titel en auteur verplicht en maximaal 80 tekens. Toon de foutmelding in het formulier met useActionState.
```

**[Zelf] De controle.**
1. Bekijk de diff. Staat de controle op de rol **in de action zelf**, of enkel in de UI?
2. Bouw en start opnieuw (`npm run build`, `npm start`) en herhaal de aanval.
   **Noteer** de HTTP-status, wat er in het antwoord staat en waar de foutmelding zelf staat.
3. Haal in DevTools › *Elements* `required` weg bij de inputs, verstuur enkel spaties en **noteer** wat er gebeurt.

## Reflectievragen (8 min, plus de tijd terwijl de agent werkt)

1. **Wat draait waar?**
   - Na 3.2 krijgt `/boeken` het symbool ◐ (*Partial Prerender*). Welk deel van de pagina wordt gemaakt tijdens de build, welk deel per request op de server, en welk deel draait in de browser? Koppel aan SSG, SSR met streaming en CSR met hydration (slide 10–12).
   - Welke code kwam in de browser terecht en welke niet? Hoe toonde je dat aan in 3.1 (slide 13)?
2. **De grens tussen server en client.**
   - Vergelijk de twee foutmeldingen uit 3.1, zonder en met `server-only`. Waarom is een expliciete grens beter?
   - Een array met boeken mag als prop naar een Client Component, een functie niet. Een Server Action mag dan weer wel doorgegeven worden. Leg uit met serialisatie (slide 49).
3. **Cache en invalidatie.**
   - Waarom staat de rol (uit de cookie) in een `<Suspense>` en niet in de cache? Tip: probeer `'use cache'` in `huidigeRol()` als je tijd hebt. Wat zou er misgaan als de lijst mét verwijderknoppen één keer gecachet werd voor iedereen?
   - Hoe illustreert 3.3 het citaat van Phil Karlton (slide 39)?
   - Koos de agent in 3.3 de beste functie? Wanneer gebruik je `updateTag` en wanneer `revalidateTag(…, 'max')` (slide 40)?
4. **Publiek endpoint.**
   - Leg met 3.4 uit wat er echt gebeurt als de client een Server Action aanroept, en welke drie controles elke action zelf moet doen (slide 48).
   - Waarom stuurt Next.js in productie enkel een `digest` naar de browser?
   - Welk probleem heeft `wisselRol` nog?
   - Was je app met perfecte controles in je eigen actions veilig tegen React2Shell (slide 50)?
5. **De agent als risico.**
   - Een agent volgt instructies uit `AGENTS.md`, maar ook tekst die hij onderweg leest. Wat kan er gebeuren als een dependency of een issue verborgen instructies bevat (prompt injection, slide 64)?
   - Welke afspraken uit dit labo (wat de agent automatisch mag, geen modus die alles goedkeurt, `npm install` zelf goedkeuren, de startcode kunnen terugzetten, elke diff nakijken) passen *least privilege* en *human in the loop* toe?
   - Waarom zou je een agent in een echt project nooit alle commando's zonder goedkeuring laten uitvoeren op een machine met toegang tot productie?
