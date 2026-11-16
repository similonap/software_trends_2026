# Deel 1: React Compiler (30 minuten)

**Theorie:**
- slide 16–18: virtual DOM, render en commit, reconciliation
- slide 30: waarom rendert een component opnieuw?
- slide 31: React.memo en referentiële gelijkheid
- slide 32: useMemo en useCallback
- slide 33–34: React Compiler en wat hij genereert
- slide 35: Rules of React

## Leerdoelen

- Je kan meten welke componenten opnieuw renderen en verklaren waarom.
- Je begrijpt waarom referentiële gelijkheid cruciaal is voor `memo`, `useMemo` en `useCallback`.
- Je kan de React Compiler aanzetten, controleren dat hij werkt en zijn output lezen.
- Je kan beoordelen of een coding agent een optimalisatie juist uitgevoerd heeft.

## Het project

Open de map `deel1-react-compiler` als projectmap. Voer in een eigen terminal `npm install` uit als je dat bij de voorbereiding nog niet deed. Start daarna `npm run dev`, open http://localhost:5173 en open de console (F12). Start een nieuwe sessie in je agent.

*Takenbord* toont 3000 taken. `App` heeft drie stukken state: een koffieteller, de lijst taken en een filter. `TakenLijst` filtert met `traagFilter`, die bewust 15 ms extra rekenwerk doet.

Rond `TakenLijst` staat een `<Profiler>`. Na elke render toont die in het **meetpaneel** rechtsonder (en in de console) hoe lang het renderen van alles binnen de Profiler duurde:

- `TakenLijst rendert (update): 48.2 ms`: de lijst en zijn kinderen renderden opnieuw.
- `TakenLijst: overgeslagen (0 ms)`: de Profiler deed mee, maar React sloeg de lijst over.
- Komt er geen nieuwe regel bij? Dan deed zelfs de Profiler niet mee aan de render.

> **Let op:** in development mode met `<StrictMode>` rendert React elk component twee keer, en alles is trager dan in productie. Vergelijk de metingen onderling.

## 1.1 [Zelf] Meten zonder optimalisatie (4 min)

1. **Voorspelling:** welke componenten renderen opnieuw als je op *Koffie gedronken* klikt?
2. Klik drie keer op *Koffie gedronken*, kies daarna de filter *open* en vink tot slot een taak aan.

**Noteer** de metingen. Je vult deze tabel verder aan in 1.2 en 1.3:

| Actie | 1.1 Start | 1.2 Handmatig (agent) | 1.2 Zonder useCallback | 1.3 Compiler |
|---|---|---|---|---|
| Koffie gedronken | | | | |
| Filter *open* | | | | |
| Taak aanvinken | | | | |

## 1.2 Handmatig optimaliseren (8 min)

**[Agent · Uitvoeren]** Kopieer deze prompt:

```text
Los de onnodige re-renders van TakenLijst op met React.memo, useMemo en useCallback, zodat een klik op "Koffie gedronken" TakenLijst en TaakItem niet meer laat renderen. Zet de React Compiler NIET aan. Wijzig enkel App.jsx, TakenLijst.jsx en TaakItem.jsx. Leg daarna per gebruikte memo, useMemo en useCallback in één zin uit waarom die nodig is.
```

*Terwijl de agent werkt:* begin aan reflectievraag 1.

**[Zelf]**
1. Kijk de wijzigingen na in de diff. Waar staat `memo`? Wat staat er in de dependency array van `useMemo` en van `useCallback`? Klopt de uitleg van de agent?
2. Meet opnieuw en vul de kolom *1.2 Handmatig* in.
3. Experiment: vervang zelf de `useCallback` rond `wissel` in `App.jsx` door een gewone functie. Laat `memo` en `useMemo` staan. Meet en vul de kolom *Zonder useCallback* in.

## 1.3 [Zelf] De React Compiler (7 min)

1. Zet de startcode terug (zie *Nakijken en terugzetten* in de [README](../README.md)). Controleer dat `memo`, `useMemo` en `useCallback` weg zijn.
2. Zet de compiler zelf aan in `vite.config.js`. Dat gaat sneller dan een prompt: haal het commentaar weg bij de twee imports en bij `babel({ presets: [reactCompilerPreset()] })`.
3. Herstart `npm run dev`, meet opnieuw en vul de kolom *1.3 Compiler* in.
4. Open de directe URL van het bestand niet: die toont de originele broncode. Open http://localhost:5173, druk op F12, ga naar het tabblad **Network**, filter op `TakenLijst` en klik op `TakenLijst.jsx`. Bekijk het tabblad **Response**: daar staat de gecompileerde code.
   **Noteer** de `_c(…)`-regel en de `if`-test waarin `traagFilter` wordt aangeroepen: welke waarden worden vergeleken? Vergelijk met slide 34.

## 1.4 De Rules of React (5 min)

**[Agent · Uitvoeren]**

```text
Voer npm run lint uit en los enkel de fouten op die de linter meldt. Verander niets anders.
```

**[Zelf]**
1. Bekijk de diff. **Noteer** de fout en de naam van de lintregel.
2. Open http://localhost:5173, druk op F12, ga naar **Network**, filter op `Statistiek` en klik op `Statistiek.jsx`. Is het component nu gecompileerd (staat er `_c(` in het tabblad **Response**)? Open de directe URL van het bestand niet: die toont altijd de broncode.

Als `_c(` er nog niet in staat:

**[Agent · Plan]**

```text
De React Compiler slaat Statistiek.jsx nog altijd over, ook al is de linter tevreden. Welke Rule of React breekt dit component nog? Wijzig nog niets.
```

**[Zelf]**
1. Klopt de verklaring? Toets ze aan slide 35.
2. Laat de agent het daarna oplossen.
3. Controleer dat `_c(` nu verschijnt.

**Noteer** ook:
- Wat deed de teller *"Dit blok werd al … keer getoond"*? Klopte dat getal?
- Is `open.sort(...)` een overtreding van de Rules of React?

## Bonus: `'use no memo'`

Alleen als je tijd over hebt. Zet zelf `'use no memo'` als eerste regel in de functie `TaakItem`. Meet *Filter* en *Taak aanvinken* opnieuw en verklaar het verschil.

## Reflectievragen (6 min, plus de tijd terwijl de agent werkt)

1. **Referentiële gelijkheid.**
   - Welke van de drie redenen van slide 30 verklaart dat `TakenLijst` in 1.1 bij elke klik op *Koffie* renderde?
   - Waarom renderde de lijst weer in het experiment zonder `useCallback`, terwijl `memo` er nog stond (slide 31)?
   - Waarom was die render toch goedkoper dan in 1.1?
2. **Wat doet de compiler anders?**
   - Met de handmatige versie van de agent gaf de Profiler bij *Koffie* nog `overgeslagen (0 ms)`. Met de compiler kwam er zelfs geen regel meer bij. Verklaar dat: open ook http://localhost:5173/src/App.jsx en zoek waar het `Profiler`-element gecachet wordt.
   - Wie kiest bij de compiler welke waarden vergeleken worden, en welke fout kan je met een handgeschreven dependency array maken die met de compiler niet kan (slide 33–34)?
3. **Puur zijn.**
   - Waarom steeg de teller in `Statistiek` met 2 per render?
   - Wat zou er met dat getal gebeurd zijn als de compiler het component toch gecachet had?
   - Waarom slaat de compiler een component dat de regels breekt over (slide 35)?
   - Wat leer je uit het feit dat de linter tevreden was terwijl de compiler het component nog oversloeg?
4. **Grenzen.** Waarom kost *Taak aanvinken* ook met de compiler nog tientallen milliseconden? Welke hooks vervangt de compiler niet (slide 33)?
5. **De agent en de compiler.**
   - De agent schreef in 1.2 in een paar minuten de handmatige optimalisatie, en in 1.3 maakte de compiler die volledig overbodig. Welke fout in de code van de agent (bijvoorbeeld een ontbrekende `useCallback` of een foute dependency array) had je bij het nakijken kunnen missen, en hoe zou je dat gemerkt hebben?
   - Wat moest je zelf begrijpen om de diff te kunnen goedkeuren?
   - Gebruik je logboek: was de agent in 1.2 sneller dan wanneer je het zelf had gedaan?
