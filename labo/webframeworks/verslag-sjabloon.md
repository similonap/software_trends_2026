# Verslag labo: React Compiler, zoneless Angular en Next.js 16

Naam:
Klas:
Datum:
Coding agent en model (de naam van de agent en van het model):

## Agent-logboek

Eén regel per taak van de agent. De kost (of het aantal tokens) vul je in als je agent die toont.

| Opdracht | Plan of Uitvoeren | Duur | Kost / tokens | Meteen correct? | Wat moest je corrigeren of bijsturen? |
|---|---|---|---|---|---|
| 1.2 | Uitvoeren | | | | |
| 1.4 | Uitvoeren | | | | |
| 1.4 | Plan | | | | |
| 2.2 B | Uitvoeren | | | | |
| 2.2 C | Uitvoeren | | | | |
| 2.2 D | Uitvoeren | | | | |
| 2.3 | Plan + Uitvoeren | | | | |
| 3.1 | Plan | | | | |
| 3.2 | Uitvoeren | | | | |
| 3.3 | Uitvoeren | | | | |
| 3.4 | Uitvoeren | | | | |

---

## Deel 1: React Compiler

Voorspelling bij 1.1:

| Actie | 1.1 Start | 1.2 Handmatig (agent) | 1.2 Zonder useCallback | 1.3 Compiler |
|---|---|---|---|---|
| Koffie gedronken | | | | |
| Filter *open* | | | | |
| Taak aanvinken | | | | |

- 1.2: wat de agent wijzigde, en of de uitleg klopte:
- 1.3: de `_c(…)`-regel en de `if`-test rond `traagFilter`:
- 1.4: de lintfout en de regel; gecompileerd na de lint-oplossing? na de volledige oplossing?; de teller "keer getoond"; `open.sort(...)`:

### Reflectievragen deel 1

1.
2.
3.
4.
5.

---

## Deel 2: zoneless Angular

- 2.0: zone.js en `changeDetection` in het project; regels in `AGENTS.md` over change detection en signals:

### 2.1 Observeren

| Test | Voorspelling | Resultaat |
|---|---|---|
| Loopt de klok? | | |
| Werkt de teller? | | |
| Verschijnen de boeken na ± 1 s? | | |
| Klok en boeken na een klik op *+1*? | | |
| Twee boeken toegevoegd: kop en lijst? | | |

### 2.2 De 2×2-matrix

| | OnPush: voorspelling / resultaat | Eager: voorspelling / resultaat |
|---|---|---|
| zoneless | A: | B: |
| zone.js | C: | D: |

- D met enkel `App` zonder Eager:
- Initial total met zone.js: ... · zonder: ...

### 2.3 Zoneless met signals

- Wat je in het plan van de agent beoordeelde of bijstuurde:

### Reflectievragen deel 2

1.
2.
3.
4.
5.

---

## Deel 3: Next.js 16

- 3.1: klopte de componentenboom van de agent?; waar staat de `[db]`-log?; paginabron en JavaScript; foutmelding zonder en met `server-only`:
- 3.2: de drie opties en de twee oorzaken; las de agent de documentatie?; de routetabel; metingen in productie:
- 3.3: zonder invalidatie; de functie die de agent koos, en waarom:
- 3.4: het request (methode, URL, `Next-Action`, body); de aanval vóór en na de beveiliging; spaties als titel:

### Reflectievragen deel 3

1.
2.
3.
4.
5.

---

## Afsluitende reflectie

A.

B.
