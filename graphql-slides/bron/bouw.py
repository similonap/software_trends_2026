"""Genereert slides/*.html, slides/deck.json, presentatie/kort.md en sprekersnotities.md uit inhoud_a.py en inhoud_b.py.

Gebruik:  python3 bouw.py        (daarna: cd ../presentatie && python3 maak.py)
"""
import html, json, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from inhoud_a import A
from inhoud_b import B

ROOT = os.path.join(HIER, '..')
SL = os.path.join(ROOT, 'slides')
os.makedirs(SL, exist_ok=True)
os.makedirs(os.path.join(ROOT, 'presentatie'), exist_ok=True)

ALLE = A + B
ids = [s['id'] for s in ALLE]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]

NR = '<p style="position:absolute;right:128px;bottom:48px;width:80px;text-align:right;font-size:24px;color:#7F7F7F">{}</p>'
NRR = '<p style="position:absolute;right:128px;bottom:48px;width:80px;text-align:right;font-size:24px;color:#F4CCCC">{}</p>'

for i, s in enumerate(ALLE, 1):
    h = s['html'].replace('@@NR@@', NR.format(i)).replace('@@NRR@@', NRR.format(i))
    open(os.path.join(SL, s['id'] + '.html'), 'w', encoding='utf-8').write(h + '\n')

secties = {
    's0': ('Intro: wat is GraphQL en waarom, geschiedenis en adoptie', 'cover'),
    's1': ('REST en zijn grenzen: versies, over- en underfetching, N+1', 'kb-rest'),
    's2': ('De taal: schema, SDL, queries, variabelen, fragmenten, mutations, subscriptions, introspectie', 'kb-schema'),
    's3': ('De server en de client: resolvers, DataLoader, declaratief, colocation, codegen', 'architecturen'),
    's4': ('Trend 1: de standaard beweegt weer', 'div-1'),
    's5': ('Trend 2: één graph voor de hele organisatie (federatie)', 'div-2'),
    's6': ('Trend 3: security en performance in productie', 'div-3'),
    's7': ('Trend 4: de API-taal voor agents', 'div-4'),
    's8': ('Wanneer GraphQL, begrippenlijst en conclusie', 'wanneer'),
}
deck = {'v': 4, 'title': 'GraphQL: de API-taal voor mensen en agents', 'order': ids,
        'sections': {k: {'description': d, 'start': st} for k, (d, st) in secties.items()},
        'faces': {'questrial': {'family': 'Questrial', 'href': 'https://fonts.googleapis.com/css2?family=Questrial&display=swap'},
                  'source-code-pro': {'family': 'Source Code Pro', 'href': 'https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;600&display=swap'}},
        'designSystems': []}
json.dump(deck, open(os.path.join(SL, 'deck.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# korte notities
k = ['# Korte sprekersnotities', '',
     'Per slide de bullets voor de "Kort"-modus van de presentatie. Pas gerust aan en draai daarna `python3 maak.py`.',
     'Een bullet die begint met "→ " is de overgang naar de volgende slide; "Examen: " wordt geel gemarkeerd.', '']
for i, s in enumerate(ALLE, 1):
    k.append(f'## {s["id"]} | {i}. {s["titel"]}')
    k.append('')
    k += [f'- {b}' for b in s['kort']]
    k.append('')
open(os.path.join(ROOT, 'presentatie', 'kort.md'), 'w', encoding='utf-8').write('\n'.join(k))

# volledige begeleidende tekst (sprekersnotities) als markdown
woorden = 0
m = ['# Begeleidende tekst bij de slides: GraphQL', '',
     '**Software Trends (AP Hogeschool, Toegepaste Informatica)** · stand van zaken: november 2026', '',
     'Deze tekst staat per slide uitgeschreven als spreektekst. Dezelfde tekst staat in de sprekersnotities van het slide-deck (`presentatie/presentatie.html`, druk op N).', '',
     'Per slide staan eerst de slidetitel en daaronder de spreektekst. Slides met *Kernbegrip* zijn examenstof; de andere slides zijn trendslides met context.', '', '---', '']
delen = {'cover': 'Intro', 'kb-rest': 'REST en zijn grenzen', 'kb-schema': 'De taal', 'architecturen': 'De server en de client',
         'div-1': 'Trend 1: De standaard beweegt weer', 'div-2': 'Trend 2: Eén graph voor de hele organisatie',
         'div-3': 'Trend 3: Security en performance', 'div-4': 'Trend 4: De API-taal voor agents', 'wanneer': 'Afsluiting'}
for i, s in enumerate(ALLE, 1):
    if s['id'] in delen:
        m += [f'## {delen[s["id"]]}', '']
    t = html.unescape(re.search(r'<aside>(.*?)</aside>', s['html'], flags=re.S).group(1)).strip()
    woorden += len(t.split())
    kern = ' *(Kernbegrip)*' if 'Kernbegrip</p>' in s['html'] else ''
    m += [f'### Slide {i}: {s["titel"]}{kern}', '', t, '']
open(os.path.join(ROOT, 'sprekersnotities.md'), 'w', encoding='utf-8').write('\n'.join(m))
print(f'{len(ALLE)} slides, {woorden} woorden spreektekst')
