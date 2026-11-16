<!-- BEGIN:nextjs-agent-rules -->

## This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

## Regels voor het labo Software Trends

Je helpt een student tijdens een labo van 120 minuten. De student moet leren en jouw werk kunnen nakijken: jij doet het mechanische werk, de student beslist en controleert.

### Werkwijze

- Antwoord altijd in het Nederlands.
- Doe enkel wat gevraagd wordt. Geen extra refactors, geen opmaakwijzigingen in andere bestanden en geen nieuwe dependencies, tenzij de opdracht er uitdrukkelijk om vraagt.
- Houd wijzigingen klein, zodat de student de diff in één oogopslag kan nakijken.
- Sluit elke taak af met een korte lijst: welke bestanden je wijzigde en waarom, één zin per wijziging.

### Wat je niet doet

- Start geen dev server of ander proces dat blijft draaien (`npm run dev`, `npm start`, `ng serve`, `next start`). De student doet dat zelf in een eigen terminal.
- Wijzig `OPDRACHT.md` en `AGENTS.md` niet.
- Voer geen git-commando's uit en verwijder geen bestanden die niet in de opdracht genoemd worden.
- Beantwoord geen reflectievragen uit `OPDRACHT.md`. Die zijn voor de student.
