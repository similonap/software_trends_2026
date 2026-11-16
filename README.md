# Software Trends 2026–2027

Lesmateriaal voor het vak Software Trends (AP Hogeschool, Toegepaste Informatica).

| Map | Wat |
|---|---|
| [`labo/`](labo/) | De labo's voor studenten, één map per les |
| [`webframeworks-slides/`](webframeworks-slides/) | Trends in JavaScript web frameworks: slides, begeleidende tekst, spreektekst |
| [`webassembly-slides/`](webassembly-slides/README.md) | WebAssembly: cursustekst, slides (bron), spreektekst |
| [`graphql-slides/`](graphql-slides/README.md) | GraphQL: cursustekst, slides (bron), spreektekst |
| [`supply-chain/`](supply-chain/) | Supply chain security: cursustekst, slides, video |

## Labo's

| Labo | Les |
|---|---|
| [`labo/webframeworks/`](labo/webframeworks/README.md) | React Compiler, zoneless Angular en Next.js 16, met agentic coding |

De voorbeeldoplossingen en modelantwoorden staan niet op `main`, maar op de branch `oplossingen`, in `labo-oplossing/`:

```
git switch oplossingen
```

## Gegenereerde bestanden

Wat je uit de bron opnieuw kunt maken, staat niet in git (zie `.gitignore`). Na een verse clone maak je het zo opnieuw. Je hebt enkel Python 3 nodig.

```
# Slides, sprekersnotities en korte notities (GraphQL en WebAssembly)
(cd graphql-slides/bron && python3 bouw.py)
(cd webassembly-slides/bron && python3 bouw.py)

# De presentatie in één bestand (presentatie/presentatie.html)
for d in graphql-slides webassembly-slides webframeworks-slides; do (cd $d/presentatie && python3 maak.py); done
```

## Presentaties als pdf

`python3 tools/maak_pdf.py` maakt van elke presentatie een pdf in `pdf/` (één slide per pagina, zonder notities). Je hebt Google Chrome en internet nodig.

Op GitHub doet de workflow *Presentaties als pdf* dat bij elke wijziging aan de slides op `main`. De nieuwste pdf's staan bij de release [Presentaties (pdf)](https://github.com/similonap/software_trends_2026/releases/tag/presentaties), zonder login te downloaden: [web frameworks](https://github.com/similonap/software_trends_2026/releases/download/presentaties/webframeworks.pdf), [WebAssembly](https://github.com/similonap/software_trends_2026/releases/download/presentaties/webassembly.pdf), [GraphQL](https://github.com/similonap/software_trends_2026/releases/download/presentaties/graphql.pdf) en [supply chain](https://github.com/similonap/software_trends_2026/releases/download/presentaties/supply-chain.pdf).

## Ingesproken video's

De ingesproken video's (`*-slides/ingesproken-*.mp4`) en de opnames in `ingesproken/audio/` staan ook niet in git. `python3 maak.py` in `ingesproken/` maakt ze opnieuw, maar spreekt dan elke slide opnieuw in met ElevenLabs. Dat kost credits en vraagt de `elevenlabs` CLI, `ffmpeg` en Google Chrome.
