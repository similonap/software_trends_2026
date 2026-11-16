# WebAssembly: van browsertruc tot universele runtime

Lesmateriaal voor het vak Software Trends (academiejaar 2026–2027), in dezelfde stijl als de web frameworks-slides. Stand van zaken: november 2026.

| Bestand | Wat |
|---|---|
| `cursustekst.md` | De cursustekst (leerstof): leerdoelen, lesplan, alle onderwerpen, begrippenlijst, bronnen |
| `presentatie/presentatie.html` | De 59 slides met sprekersnotities in één bestand. Open in Chrome; **N** opent het notitievenster (toetsen: zie `presentatie/README.md`) |
| `sprekersnotities.md` | Dezelfde spreektekst per slide als tekstdocument (± 9.600 woorden) |
| `slides/*.html`, `slides/deck.json` | De slides afzonderlijk (1920×1080) |
| `presentatie/kort.md` | Korte bullets voor de "Kort"-modus van de notities (gegenereerd) |
| `bron/` | Generator: pas `inhoud_a.py` (basis) of `inhoud_b.py` (trends) aan, draai `python3 bouw.py` en daarna `python3 maak.py` in `presentatie/`. Afbeeldingen staan in `bron/media/` en worden ingebed. |

Let op: `kort.md`, `sprekersnotities.md` en `slides/` worden door `bouw.py` overschreven. Pas de tekst dus aan in `bron/`.
