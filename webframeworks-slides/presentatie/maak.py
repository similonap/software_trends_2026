"""Bouwt presentatie.html: alle slides, sprekersnotities en korte notities in één bestand.

Gebruik:  python3 maak.py      (daarna presentatie.html openen in Chrome)

Bronnen:
  ../ingesproken/slides/*.html + deck.json   de slides (met de volledige notities in <aside>)
  kort.md                                    de korte notities (bullets) per slide
  sjabloon.html                              de speler (navigatie, notitievenster)
  fonts/                                     Questrial en Source Code Pro, ingebed voor offline gebruik
"""
import base64, html, json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HIER, '..', 'ingesproken', 'slides')


def lees(*p):
    return open(os.path.join(HIER, *p), encoding='utf-8').read()


def kort():
    K = {}
    for blok in re.split(r'^## ', lees('kort.md'), flags=re.M)[1:]:
        kop, _, rest = blok.partition('\n')
        K[kop.split('|')[0].strip()] = [re.sub(r'\s+', ' ', b).strip()
                                        for b in re.findall(r'^- (.*(?:\n(?!- |\n).*)*)', rest, flags=re.M)]
    return K


def fonts():
    css = lees('fonts', 'fonts.css')
    def inline(m):
        data = base64.b64encode(open(os.path.join(HIER, m.group(1)), 'rb').read()).decode()
        return f'url(data:font/woff2;base64,{data})'
    return re.sub(r'url\((fonts/[^)]+)\)', inline, css)


def main():
    order = json.load(open(os.path.join(SLIDES, 'deck.json')))['order']
    K = kort()
    data = []
    for s in order:
        h = open(os.path.join(SLIDES, f'{s}.html'), encoding='utf-8').read()
        m = re.search(r'<aside[^>]*>(.*?)</aside>', h, flags=re.S)
        notities = html.unescape(m.group(1)).strip() if m else ''
        sectie = re.sub(r'<aside.*?</aside>', '', h, flags=re.S).strip()
        t = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sectie, flags=re.S)
        titel = html.unescape(re.sub(r'<[^>]+>', '', t.group(1).replace('<br>', ' '))).strip() if t else s
        data.append({'id': s, 'titel': titel, 'html': sectie, 'notities': notities, 'kort': K.get(s, [])})

    zonder = [s for s in order if not K.get(s)]
    extra = [s for s in K if s not in order]
    if zonder: print('Let op, geen korte notities voor:', ', '.join(zonder))
    if extra: print('Let op, in kort.md maar niet in de deck:', ', '.join(extra))

    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    uit = lees('sjabloon.html').replace('/*FONTS*/', fonts()).replace('/*DATA*/', js)
    open(os.path.join(HIER, 'presentatie.html'), 'w', encoding='utf-8').write(uit)
    print(f'Klaar: presentatie.html ({len(order)} slides, {len(uit) // 1024} kB)')


if __name__ == '__main__':
    sys.exit(main())
