# Labo: React Compiler, zoneless Angular en Next.js 16, met agentic coding

Software Trends · Trends in JavaScript web frameworks (2026–2027) · **120 minuten**

In de les zag je dat de grote frameworks naar hetzelfde antwoord groeien: fijnmazige reactiviteit, een compiler die het optimalisatiewerk doet, en meer werk op de server. Je zag ook dat een groot deel van de code vandaag geschreven wordt door AI-agents (trend 4). In dit labo combineer je de twee. Je onderzoekt drie frameworks, en je gebruikt daarbij **verplicht een coding agent** voor het mechanische werk. Welke agent je gebruikt, kies je zelf. Zo past alles in 120 minuten, en leer je meteen hoe je een agent aanstuurt en zijn werk controleert.

## Planning

| Tijd | Onderdeel | Theorie (slides) |
|---|---|---|
| 0–5 | Start: je agent controleren, verslag openen | |
| 5–35 | [Deel 1: React Compiler](deel1-react-compiler/OPDRACHT.md) | 16–18, 30–35 |
| 35–70 | [Deel 2: zoneless Angular](deel2-angular-zoneless/OPDRACHT.md) | 22–23, 27–29 |
| 70–110 | [Deel 3: Next.js 16](deel3-nextjs/OPDRACHT.md) | 10–13, 38–41, 47–50 |
| 110–120 | Afsluitende reflectie (onderaan dit document) | 25, 45, 55–69 |

Elke opdracht vermeldt hoeveel tijd je ervoor hebt. Loop je achter op het schema? Sla dan de bonusopdrachten over, niet de reflectievragen.

## Verplicht vooraf (thuis, ± 20 minuten)

Het labo start met alles geïnstalleerd. Installeren tijdens het labo kost te veel tijd.

1. Installeer **Node.js 22.12 of nieuwer** (`node -v`), **git**, een editor (bv. VS Code) en **Google Chrome**.
2. Zorg dat de startcode in git staat: haal het labo binnen met `git clone`. Kreeg je de bestanden als zip? Voer dan in de map van het labo één keer `git init`, `git add -A` en `git commit -m "start"` uit.
3. Kies een **coding agent** en zorg dat hij werkt. Je mag eender welke agent gebruiken, als extensie in je editor of in de terminal, zolang hij:
   - de bestanden in je projectmap kan lezen en wijzigen;
   - terminalcommando's kan uitvoeren, en daarvoor eerst jouw toestemming kan vragen.

   Kies een model dat goed is in code. Gratis modellen zijn vaak trager en hebben limieten, en dat kost in een labo van 120 minuten tijd. **Zet nooit een API-sleutel in je code of in je verslag.**
4. Voer `npm install` uit in elk van de drie projectmappen.
5. Test je agent: open `deel1-react-compiler` als projectmap, zet je agent in zijn plan- of leesmodus en vraag: *"Leg in drie zinnen uit wat dit project doet. Welke regels uit AGENTS.md volg je daarbij?"* Noemt de agent de regels van het labo niet, lees dan hieronder wat je doet als hij `AGENTS.md` niet vanzelf leest.

## Je agent gebruiken in dit labo

Elke agent heeft zijn eigen knoppen en namen. Hieronder staat wat je in dit labo nodig hebt. Zoek vooraf op hoe het in jouw agent heet.

**Open elk deel als aparte projectmap.** Elk project bevat een `AGENTS.md` met afspraken voor de agent: de regels voor dit labo, en in deel 2 en 3 ook de regels die het framework zelf meelevert. De meeste agents lezen dat bestand vanzelf, maar alleen als de projectmap de root van je workspace is, of de map waarin je de agent start. Leest jouw agent `AGENTS.md` niet vanzelf? Begin dan elke sessie met: *"Lees eerst AGENTS.md en volg de regels daarin."* Start voor elk deel een **nieuwe sessie** (een nieuw gesprek of een nieuwe taak).

**Wat mag de agent zonder te vragen?** Stel de permissies van je agent zo in:

| Wat de agent wil doen | Instelling | Waarom |
|---|---|---|
| Projectbestanden lezen | automatisch | lezen is onschuldig en spaart tijd |
| Projectbestanden wijzigen | automatisch | je kijkt elke wijziging achteraf na in de diff |
| Veilige commando's (de build, de linter) | automatisch, als je agent dat onderscheid kent | builds en de linter mogen meteen draaien |
| Alle andere commando's, de browser, MCP-servers | **zelf goedkeuren** | bv. `npm install` keur je zelf goed |
| Een modus die alles automatisch goedkeurt ("YOLO", "auto-run", "bypass permissions") | **uit** | |

Waarom die keuzes? Dat zijn *least privilege* en *human in the loop* (slide 64), en je komt erop terug in de reflectievragen.

**Werkwijze.** Bij elke stap staat wie het werk doet:
- **[Zelf]**: je voert het zelf uit: voorspellen, meten, testen, aanvallen en nadenken. Dat besteed je niet uit.
- **[Agent · Plan]**: de agent mag enkel lezen en een plan of antwoord geven. Jij beoordeelt dat plan. Gebruik de plan- of leesmodus van je agent. Heeft hij die niet, dan volstaat de prompt: elke Plan-prompt vraagt uitdrukkelijk om niets te wijzigen.
- **[Agent · Uitvoeren]**: de agent wijzigt code. Kopieer de prompt letterlijk. Daarna kijk je de wijziging **altijd** na in de **diff**, vóór je verder gaat.

**Nakijken en terugzetten.** Je hebt drie handelingen nodig. Met git werken ze bij elke agent. Voer de commando's zelf uit in de projectmap, in een eigen terminal:

| Handeling | Met git | Of met je agent |
|---|---|---|
| De **diff** van de laatste wijziging bekijken | `git diff .` of het paneel *Source Control* van je editor | de diffweergave van de agent |
| Een nagekeken wijziging goedkeuren | `git add .` Daarna toont `git diff .` enkel wat er nadien nog wijzigt. | |
| De **startcode** van het deel terugzetten | `git restore --staged --worktree .` | een herstelpunt (checkpoint, rewind, undo) van vóór de eerste wijziging |

Bestanden die de agent nieuw aanmaakte, staan niet in `git diff .`: die zie je met `git status`. Het commando om terug te zetten raakt enkel de projectmap waarin je staat. Je verslag en de andere delen blijven dus zoals ze zijn.

Terwijl de agent werkt, werk jij aan je verslag: begin dan al aan de reflectievraag die bij de opdracht staat.

**Agent-logboek.** Houd in je verslag voor elke taak van de agent bij:
- hoe lang ze duurde;
- wat ze kostte, als je agent dat toont (tokens of kost);
- of het resultaat meteen klopte;
- wat je moest corrigeren.

Je hebt dat logboek nodig voor de reflectievragen.

## Voorspel, test, verklaar

Bij elke opdracht werk je in drie stappen:

1. **Voorspel** wat er gaat gebeuren, vóór je iets uitvoert.
2. **Test** het en noteer wat je ziet.
3. **Verklaar** het verschil met de begrippen uit de theorie.

Alles wat je moet opschrijven, staat aangeduid met **Noteer**. Elk deel eindigt met **reflectievragen**: daar koppel je je resultaten aan de theorie, en dat is het belangrijkste deel van je verslag. Een goed antwoord gebruikt de juiste begrippen en verwijst naar iets wat je zelf gemeten of gezien hebt. De agent mag code schrijven, maar je reflecties schrijf je zelf.

Gebruik [`verslag-sjabloon.md`](verslag-sjabloon.md) als start voor je verslag.

## Indienen

Dien je verslag in (PDF of Markdown, met je agent-logboek), samen met de bronbestanden van je eindoplossing per deel, zonder `node_modules`, `.next`, `.angular` en `dist`.

## Afsluitende reflectie (10 minuten)

Beantwoord elke vraag in maximaal tien regels, met voorbeelden uit de drie delen.

**A. Drie frameworks, één richting.**
- In deel 1 deed een **compiler** het werk tijdens de build, in deel 2 deden **signals** het tijdens het draaien in de browser, en in deel 3 deed de **server** een groot deel van het werk. Leg voor elk deel uit *wanneer* en *waar* beslist wordt wat er op het scherm moet veranderen.
- Waarom zeggen we dat de frameworks naar elkaar toe groeien (slide 25)?
- Wat zou jij kiezen voor een intern dashboard, en wat voor een webshop (slide 45)?

**B. Wat deed de agent, en wat deed jij?**
- Waar won je met de agent echt tijd, en waar niet? Gebruik je logboek.
- Welke kennis uit de theorie had je nodig om de agent de juiste opdracht te geven en om zijn werk goed te keuren? Geef minstens één voorbeeld waarin je een fout of een slechte keuze van de agent zelf opmerkte, of had kunnen opmerken.
- Wat is het risico als een developer die kennis niet heeft (*vibe coding*, slide 69)?
