# GraphQL: de API-taal voor mensen en agents

Lesmateriaal voor het vak Software Trends (academiejaar 2026–2027), in dezelfde stijl als de web frameworks- en WebAssembly-slides. Stand van zaken: november 2026.

| Bestand | Wat |
|---|---|
| `cursustekst.md` | De cursustekst (leerstof): leerdoelen, lesplan, alle onderwerpen, begrippenlijst, bronnen |
| `presentatie/presentatie.html` | De 56 slides met sprekersnotities in één bestand. Open in Chrome; **N** opent het notitievenster (toetsen: zie `presentatie/README.md`) |
| `sprekersnotities.md` | Dezelfde spreektekst per slide als tekstdocument (± 8.900 woorden) |
| `slides/*.html`, `slides/deck.json` | De slides afzonderlijk (1920×1080) |
| `presentatie/kort.md` | Korte bullets voor de "Kort"-modus van de notities (gegenereerd) |
| `bron/` | Generator: pas `inhoud_a.py` (basis) of `inhoud_b.py` (trends) aan, draai `python3 bouw.py` en daarna `python3 maak.py` in `presentatie/` |
| `bron/test-voorbeelden.mjs` | Voert alle GraphQL-voorbeelden van de slides uit (schema, queries, mutation, fragmenten, @oneOf, N+1 met/zonder DataLoader, @defer). Gebruik: `npm i graphql@17 dataloader && node test-voorbeelden.mjs` |

Let op: `kort.md`, `sprekersnotities.md` en `slides/` worden door `bouw.py` overschreven. Pas de tekst dus aan in `bron/`.
