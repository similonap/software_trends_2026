# Deel 2: zoneless Angular (35 minuten)

**Theorie:** slide 22–23 (signals), 27 (change detection, zone.js, monkey patching), 28 (zoneless en OnPush: vroeger en nu), 29 (Angular 21 en 22), 57–58 en 63 (agents, AGENTS.md, Angular en AI).

## Leerdoelen

- Je kan het verschil tussen **zoneless** (*wanneer* kijkt Angular?) en **OnPush** (*welke* componenten?) aantonen met een experiment.
- Je kan verklaren waarom code die vroeger werkte, in Angular 22 niet meer bijwerkt.
- Je kan een agent de juiste, moderne oplossing laten bouwen met `signal`, `computed` en `resource`, en die oplossing beoordelen.

## Het project

Open de map `deel2-angular-zoneless` als projectmap. Start in een eigen terminal `npm start` en open http://localhost:4200. Start een nieuwe sessie in je agent.

Het dashboard van een bibliotheek heeft vier componenten in `src/app/`:

| Component | Wat doet het? | Hoe? |
|---|---|---|
| `Klok` | toont de tijd, elke seconde bijgewerkt | `setInterval` past een gewoon veld aan |
| `Teller` | telt bezoekers | knop met `(click)`, gewoon veld `aantal++` |
| `Boeken` | haalt boeken op en laat je er een toevoegen | `fetch` in `ngOnInit`, daarna `this.boeken.push(...)` |
| `BoekenLijst` | toont de lijst | krijgt de array binnen via `input()` |

Alles is geschreven zoals je dat jarenlang in Angular deed: met gewone velden, zonder signals.

## 2.0 [Zelf] Rondkijken (2 min)

- Zoek in `package.json`, `angular.json` en `src/app/app.config.ts` naar `zone.js`, en in de componenten naar `changeDetection`. **Noteer** wat dat volgens slide 28 betekent.
- Open `AGENTS.md`. Het bovenste deel werd gemaakt door de Angular CLI (`ng new --ai-config`), onderaan staan de regels voor dit labo. Een coding agent leest dat bestand bij de start van een sessie. **Noteer** welke regels erin over change detection en signals gaan.

## 2.1 [Zelf] Observeren (5 min)

**Voorspel** eerst, test daarna:

| Test | Voorspelling | Resultaat |
|---|---|---|
| Loopt de klok? | | |
| Werkt de teller? | | |
| Verschijnen de boeken na ± 1 s? | | |
| Wat gebeurt er met de klok en de boeken als je op *+1* klikt? | | |
| Voeg twee boeken toe. Wat zeggen de kop *Boeken (…)* en de lijst? | | |

## 2.2 De 2×2-matrix (12 min)

Twee onafhankelijke mechanismen: **wanneer** Angular kijkt (zone.js of zoneless) en **welke** componenten het dan controleert (Eager of OnPush). De agent doet het omschakelen; jij voorspelt en test.

**[Zelf]** Voorspel eerst alle vier de cellen:

| | OnPush (standaard in v22) | Eager (vroeger *Default*) |
|---|---|---|
| **zoneless** (standaard in v21+) | A: dat is 2.1 | B |
| **zone.js** | C | D: zo werkte Angular tot v21 |

**B: zoneless + Eager.**

**[Agent · Uitvoeren]**

```text
Zet in alle componenten in src/app, ook in App, changeDetection op ChangeDetectionStrategy.Eager. Verander verder niets.
```

**[Zelf]** Bekijk de diff en test.

**C: zone.js + OnPush.** Zet eerst de toestand van A terug: dat is de startcode (zie *Nakijken en terugzetten* in de [README](../README.md)). Daarna:

**[Agent · Uitvoeren]**

```text
Zet zone.js terug in dit project zoals in een Angular-project van vóór versie 21: installeer het package zone.js, voeg het toe als polyfill in angular.json en voeg provideZoneChangeDetection() toe in app.config.ts. Verander niets aan de componenten.
```

De agent vraagt toestemming om `npm install` uit te voeren. Lees het commando en keur het goed.

**[Zelf]**
1. Herstart `npm start` en test.
2. Voer `npx ng build` uit en **noteer** de *Initial total* (raw en transfer).

**D: zone.js + Eager.**

**[Agent · Uitvoeren]**: gebruik dezelfde prompt als bij B.

**[Zelf]** Test. Haal daarna zelf de regel `changeDetection` weg uit `App` (enkel daar). Wat gebeurt er nu met de klok en de boeken? En als je op *+1* klikt?

**Terug naar A.**
1. Zet de startcode terug. Het package `zone.js` blijft in `node_modules`, maar wordt niet meer gebruikt.
2. Herstart, voer `npx ng build` uit en **noteer** de *Initial total* zonder zone.js.

## 2.3 Zoneless oplossen met signals (9 min)

**[Agent · Plan]**

```text
Maak deze app zoneless-proof met signals, zonder zone.js, zonder ChangeDetectionStrategy.Eager en zonder markForCheck:
- Klok: de tijd als signal, de timer opgeruimd met DestroyRef.
- Teller: als signal.
- Boeken: laden met resource() met een defaultValue, in de template isLoading(), error() en value(); een boek toevoegen met update() en een nieuwe array; het aantal als computed().
Maak eerst een plan per bestand. Wijzig nog niets.
```

**[Zelf]** Beoordeel het plan.
- Voldoet het aan alle punten?
- Gebruikt het nergens `push`, `markForCheck` of `Eager`?

Stuur bij indien nodig en laat de agent het plan daarna uitvoeren. Daarna:

**[Zelf]**
1. Bekijk de diff.
2. Test alle punten uit 2.1.
3. `npx ng build` moet slagen zonder fouten.

## Bonus: Signal Forms

Alleen als je tijd over hebt. Laat de agent het formulier van `Boeken` omzetten naar Signal Forms (`@angular/forms/signals`):
- een titel en een auteur;
- `required` en `maxLength` 80;
- een foutmelding zodra het veld aangeraakt is;
- een knop die uitgeschakeld is zolang het formulier ongeldig is.

Controleer zelf of het formulier na het verzenden leeg is en geen foutmelding toont.

## Reflectievragen (7 min, plus de tijd terwijl de agent werkt)

1. **Wanneer en welke.** Verklaar elk resultaat uit 2.1 met de twee vragen van slide 28: welke melding was er, of net niet (*wanneer*), en welk component was dirty (*welke*)? Doe dat zeker voor:
   - de stilstaande klok;
   - de teller die wel werkt;
   - de boeken die blijven laden;
   - het verschil tussen de kop en de lijst.
2. **Wat deed zone.js eigenlijk?**
   - In situatie C was zone.js terug, en toch werkte bijna niets beter. Waarom niet?
   - Bij een upgrade naar Angular 22 zet `ng update` `Eager` op **alle** bestaande componenten. Verklaar waarom, met je resultaat uit D (enkel `App` zonder Eager).
3. **Hetzelfde probleem, andersom.**
   - In deel 1 zorgde een *nieuwe* referentie voor een *onnodige* render. Hier zorgde dezelfde referentie (`push`) voor een *gemiste* update. Leg uit waarom beide voortkomen uit hetzelfde principe (slide 31).
   - Waarom heeft Angular met signals geen `memo` of een memoïzerende compiler nodig om te weten wat er moet veranderen (slide 23 en 25)?
4. **Magie of expliciet?**
   - Slide 27 noemt zone.js "monkey patching". Leg uit wat dat is.
   - Geef drie nadelen van zone.js, waarvan minstens één die je zelf gemeten hebt.
   - Waarom is `resource()` een betere oplossing dan na de `fetch` zelf `markForCheck()` aanroepen?
5. **De agent en AGENTS.md.**
   - Bekijk de code die de agent in 2.3 schreef. Volgde hij de regels uit `AGENTS.md`? Vind je er stukken uit `AGENTS.md` in terug?
   - Een taalmodel kent het framework van gisteren (slide 57). Welke code zou een agent zonder `AGENTS.md` en zonder jouw prompt waarschijnlijk geschreven hebben voor de klok of de fetch? Waarom had die code in Angular 22 niet gewerkt?
   - Wat zegt dat over het nut van `AGENTS.md` (slide 58 en 63)? En waarom kon jij een goede prompt schrijven: welke kennis uit de theorie zat in die prompt?
