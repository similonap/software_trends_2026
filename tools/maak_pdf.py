"""Maakt van elke presentatie een pdf: één slide per pagina (1920×1080), zonder sprekersnotities.

Gebruik:
  python3 tools/maak_pdf.py              alle presentaties, naar pdf/<naam>.pdf
  python3 tools/maak_pdf.py graphql      enkel deze presentatie(s)

Nodig: Python 3 en Google Chrome of Chromium (ander pad: zet de omgevingsvariabele CHROME).
De lettertypes komen van Google Fonts, dus je hebt internet nodig.

Presentaties met een bron/bouw.py (GraphQL, WebAssembly) worden eerst opnieuw gegenereerd.
"""
import json, math, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UIT = ROOT / 'pdf'

# naam van de pdf -> map met één html-bestand per slide
DECKS = {
    'webframeworks': 'webframeworks-slides/ingesproken/slides',
    'webassembly': 'webassembly-slides/slides',
    'graphql': 'graphql-slides/slides',
    'supply-chain': 'supply-chain/slides/slides',
}

CSS = """
@page{size:1920px 1080px;margin:0}
*{margin:0;box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:Arial,Helvetica,sans-serif}
section{position:relative;width:1920px;height:1080px;overflow:hidden;break-after:page;break-inside:avoid}
ul,ol{padding-left:1.15em}
aside{display:none}
table{border-collapse:collapse}
td,th{border:1px solid #BFBFBF;padding:.35em .6em;vertical-align:top}
x-shape{display:block}
x-shape[kind=arrow-right]{clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%)}
x-shape[kind=arrow-down]{clip-path:polygon(30% 0,70% 0,70% 60%,100% 60%,50% 100%,0 60%,30% 60%)}
"""

# De slides van supply-chain komen uit een Slides-artifact en gebruiken <x-icon> en <x-connector>.
# Die elementen bestaan enkel daar, dus hier worden ze omgezet naar svg.
ICONEN = {'Check': '<path d="M20 6 9 17l-5-5"/>'}


def stijl(attrs, eigenschap, standaard):
    m = re.search(r'(?:^|[;"\s])' + eigenschap + r'\s*:\s*([^;"]+)', attrs)
    return m.group(1).strip() if m else standaard


def icoon(m):
    naam = re.search(r'name="([^"]*)"', m.group(1)).group(1)
    if naam not in ICONEN:
        print(f'  Let op: onbekend icoon "{naam}", voeg het toe aan ICONEN')
    s = re.search(r'style="([^"]*)"', m.group(1))
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" style="flex:none;{s.group(1) if s else ""}">{ICONEN.get(naam, "")}</svg>')


def verbinding(m):
    a = m.group(1)
    x1, y1, x2, y2 = (float(re.search(rf'\b{k}="([^"]*)"', a).group(1)) for k in ('x1', 'y1', 'x2', 'y2'))
    kleur = stijl(a, 'color', '#000')
    dikte = float(stijl(a, 'border-width', '2px').replace('px', ''))
    streep = f' stroke-dasharray="{dikte * 3} {dikte * 2}"' if stijl(a, 'border-style', 'solid') == 'dashed' else ''
    kop = ''
    if 'head="none"' not in a:
        lengte = math.hypot(x2 - x1, y2 - y1) or 1
        dx, dy = (x2 - x1) / lengte, (y2 - y1) / lengte
        k = dikte * 4                                 # lengte van de pijlpunt
        bx, by = x2 - dx * k, y2 - dy * k             # basis van de pijlpunt
        kop = (f'<polygon fill="{kleur}" points="{x2},{y2} {bx - dy * k * .55},{by + dx * k * .55} '
               f'{bx + dy * k * .55},{by - dx * k * .55}"/>')
        x2, y2 = bx, by
    return (f'<svg viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0;width:1920px;height:1080px">'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{kleur}" stroke-width="{dikte}"{streep}/>{kop}</svg>')


def slide_html(tekst, media, blobs):
    tekst = re.sub(r'<aside.*?</aside>', '', tekst, flags=re.S)
    tekst = re.sub(r'<x-icon([^>]*)>\s*</x-icon>', icoon, tekst)
    tekst = re.sub(r'<x-connector([^>]*)>\s*</x-connector>', verbinding, tekst)

    def blob(m):
        if m.group(1) not in blobs:
            sys.exit(f'Afbeelding {m.group(1)} staat niet in {media / "blobs.json"}')
        return (media / blobs[m.group(1)]).as_uri()
    return re.sub(r'/_blob/([0-9a-f]+)', blob, tekst)


def chrome():
    kandidaten = [os.environ.get('CHROME'), shutil.which('google-chrome'), shutil.which('google-chrome-stable'),
                  shutil.which('chromium'), shutil.which('chromium-browser'),
                  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
    for k in kandidaten:
        if k and os.path.exists(k):
            return k
    sys.exit('Google Chrome niet gevonden. Zet het pad in de omgevingsvariabele CHROME.')


def maak(naam, tmp):
    slides = ROOT / DECKS[naam]
    bouw = slides.parent / 'bron' / 'bouw.py'
    if bouw.exists():
        subprocess.run([sys.executable, '-B', bouw.name], cwd=bouw.parent, check=True, stdout=subprocess.DEVNULL)

    # deck.json staat naast de slides, of één map hoger (supply-chain)
    deck_json = slides / 'deck.json' if (slides / 'deck.json').exists() else slides.parent / 'deck.json'
    deck = json.loads(deck_json.read_text(encoding='utf-8'))
    media = deck_json.parent / 'media'
    blobs = json.loads((media / 'blobs.json').read_text(encoding='utf-8')) if (media / 'blobs.json').exists() else {}

    fonts = ''.join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck.get('faces', {}).values())
    secties = ''.join(slide_html((slides / f'{s}.html').read_text(encoding='utf-8'), media, blobs) for s in deck['order'])
    pagina = tmp / f'{naam}.html'
    pagina.write_text(f'<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>{deck.get("title", naam)}</title>'
                      f'{fonts}<style>{CSS}</style></head><body>{secties}</body></html>', encoding='utf-8')

    pdf = UIT / f'{naam}.pdf'
    pdf.unlink(missing_ok=True)
    args = [chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-pdf-header-footer',
            '--virtual-time-budget=20000', f'--user-data-dir={tmp / "profiel"}', f'--print-to-pdf={pdf}', pagina.as_uri()]
    if os.environ.get('CI'):
        args.insert(1, '--no-sandbox')  # de sandbox van Chrome werkt niet op de runners van GitHub
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0 or not pdf.exists():
        sys.exit(f'{naam}: Chrome kon geen pdf maken.\n{r.stderr[-2000:]}')

    paginas = len(re.findall(rb'/Type\s*/Page\b', pdf.read_bytes()))
    if paginas != len(deck['order']):
        sys.exit(f'{naam}: {paginas} pagina\'s voor {len(deck["order"])} slides. Loopt er een slide over de rand?')
    print(f'{pdf.relative_to(ROOT)}: {paginas} slides, {pdf.stat().st_size / 1e6:.1f} MB')


def main():
    namen = sys.argv[1:] or list(DECKS)
    onbekend = [n for n in namen if n not in DECKS]
    if onbekend:
        sys.exit(f'Onbekende presentatie: {", ".join(onbekend)}. Kies uit: {", ".join(DECKS)}')
    UIT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for n in namen:
            maak(n, Path(tmp))


if __name__ == '__main__':
    main()
