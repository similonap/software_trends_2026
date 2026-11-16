---
workflow: faceless-explainer
flow: automation
storyboard: no
message: "Eén PR-titel opende de CI van Nx; de malware liet daarna je eigen AI-assistent je secrets zoeken. CI is aanvalsoppervlak, en een AI-agent zonder vangrails doet ook wat malware vraagt."
destination: lecture
aspect: 1920x1080
language: nl
audience: 3de-jaarsstudenten software engineering (college npm supply chain security)
length: 75s
angle: narrative
voice: "elevenlabs:eleven_v4:Andie (8OezxDDjGa2d9W45o5Qs)"
---

## Intent

"Kan je een filmpje maken over Nx "s1ngularity" en gebruik elevenlabs cli voor de stem. Je mag andie nemen"

Verhaal, chronologisch als een heist: kwetsbare pull_request_target-workflow (PR-titel in bash) →
NPM_TOKEN gestolen → acht kwaadaardige versies in ruim twee uur (26–27 aug 2025) → postinstall
telemetry.js start claude --dangerously-skip-permissions / gemini --yolo / q --trust-all-tools →
secrets drievoudig base64 in publieke repo s1ngularity-repository → 2.349 gelekte secrets, AI-truc
lukte op 95 van 366 systemen, tweede golf maakte private repos publiek → les. Feiten uit
cursustekst.md casestudie 3 en de slide nx.html.

## Customizations

- Stem: Andie via de ElevenLabs CLI (`elevenlabs text-to-speech convert_with_timestamps`), voice `8OezxDDjGa2d9W45o5Qs`, model `eleven_v4`; per frame een host-voicefile.
- Stijl: workflow kiest (gebruiker koos "laat de workflow kiezen").
- Geen muziek.
- Wordt getoond in het college (16:9).
