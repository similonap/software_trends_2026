# Ingesproken slides: bron

Alles om `../ingesproken-slides-2026.mp4` opnieuw te maken.

| Map of bestand | Wat |
|---|---|
| `script.md` | Spreektekst per slide. **Dit pas je aan.** |
| `slides/*.html` | Eén bestand per slide (1920×1080, inline styles). `slides/deck.json` bepaalt de volgorde. |
| `audio/` | Ingesproken mp3 per slide, met naast elke mp3 de tekst waarmee hij gemaakt is (`.txt`). |
| `build/` | Tussenresultaten (PNG per slide, videostukjes). Mag je weggooien; wordt opnieuw gemaakt. |
| `maak.py` | Bouwt de video en `../ingesproken-script-40min.md` (met tijdstippen). |

## Nodig

- `elevenlabs` CLI (ingelogd), `ffmpeg`, Google Chrome, Python 3.

## Tekst aanpassen

1. Wijzig de tekst onder de juiste `## slide-id | titel` in `script.md`.
2. `python3 maak.py --droog` toont welke slides opnieuw ingesproken worden en hoeveel tekens dat kost.
3. `python3 maak.py` spreekt enkel die slides opnieuw in en bouwt de video opnieuw (enkele seconden als er niets veranderde, een paar minuten na een volledige render).

Klinkt een slide slecht maar is de tekst goed? `python3 maak.py --opnieuw kb-dom` maakt een nieuwe opname van die slide. Te snel of te traag: voeg `--snelheid 0.95` toe (geldt enkel voor de slides die op dat moment ingesproken worden).

Een woord dat verkeerd uitgesproken wordt, los je meestal het snelst op door het in `script.md` fonetisch te schrijven (bv. "Viet" voor Vite).

## Slide aanpassen

Wijzig `slides/<id>.html`. Bij de volgende `python3 maak.py` wordt enkel die slide opnieuw gerenderd; de audio blijft. Een nieuwe slide: voeg het HTML-bestand toe, zet de id in `order` in `slides/deck.json` en voeg een `## id | titel`-blok toe aan `script.md`.

Let op: deze HTML-bestanden zijn een kopie van het Slides-artifact. Wijzigingen hier komen niet vanzelf in het artifact, en omgekeerd.
