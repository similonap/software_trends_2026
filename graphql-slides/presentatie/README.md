# Presentatie met sprekersnotities

Open `presentatie.html` in Chrome: dubbelklik volstaat, je hebt geen server of internet nodig.

## Presenteren

1. Open `presentatie.html` en sleep het venster naar de beamer.
2. Druk op **N**. Het notitievenster opent apart; zet het op je laptopscherm.
3. Druk in het presentatievenster op **F** voor volledig scherm.

Je kunt in beide vensters navigeren, ook met een presenter-clicker (PageUp en PageDown).

| Toets | Werkt in | Wat |
|---|---|---|
| → ↓ PageDown spatie | beide | volgende slide |
| ← ↑ PageUp | beide | vorige slide |
| cijfer + Enter | beide | naar die slide (bv. `19` Enter) |
| Home / End | beide | eerste / laatste slide |
| B of . | beide | zwart scherm aan/uit (het notitievenster toont dat in het geel) |
| N | presentatie | notitievenster openen |
| F | presentatie | volledig scherm |
| ? | presentatie | hulp tonen |
| K | notities | wisselen tussen **Kort** (bullets) en **Volledig** (de volledige tekst) |
| + / − | notities | grotere / kleinere letters |

In het notitievenster zie je:
- het slidenummer
- een timer, met knoppen voor pauze en reset
- de klok
- de huidige en de volgende slide

In de korte notities herken je twee soorten bullets:
- Een cursieve bullet die met **→** begint, is de overgang naar de volgende slide.
- Een gele **Examen:**-bullet is een examentip.

Je kunt beide vensters herladen of sluiten zonder dat ze uit sync raken. Ze zoeken elkaar vanzelf terug.

## Aanpassen

De slides, de volledige notities en de korte notities worden gegenereerd vanuit `../bron/` (`inhoud_a.py` en `inhoud_b.py`). Pas de tekst daar aan en draai:

```bash
cd ../bron && python3 bouw.py      # slides/*.html, kort.md, sprekersnotities.md
cd ../presentatie && python3 maak.py   # presentatie.html
```

`sjabloon.html` is de speler zelf (opmaak en toetsen); `fonts/` bevat Questrial en Source Code Pro, ingebed zodat de presentatie ook offline werkt.
