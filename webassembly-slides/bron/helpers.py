"""Hulpfuncties om slides in dezelfde stijl als de web frameworks-slides te genereren (1920x1080, inline styles)."""
import base64, html, os, re

MEDIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media")

ROOD = '#C00000'
ARIAL = 'Arial, Helvetica, sans-serif'
QUEST = "Questrial, 'Century Gothic', Arial, sans-serif"
MONO = "'Source Code Pro', 'Courier New', monospace"
BASE = f'background:#FFFFFF;color:#404040;font-family:{ARIAL};padding:104px 128px 144px;display:flex;flex-direction:column;gap:40px'


def esc(t):
    return html.escape(t, quote=False)


def inline(t):
    """**vet**, *cursief* en `code` -> html (na escapen)."""
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'(?<![\w*])\*(.+?)\*(?![\w*])', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', lambda m: f'<span style="font-family:{MONO};font-size:0.92em;background:#F2F2F2;padding:0 6px">{m.group(1)}</span>', t)
    return t


# ---------- code ----------
KW = {
    'js': 'const let var function return await async new import from export if else for while true false null undefined',
    'c': 'int char void return if else for while include define const unsigned',
    'rust': 'use pub fn extern let mut mod impl struct enum match if else for in return',
    'wat': 'module import export func param result local i32 i64 f32 f64 v128 memory table global type tag try_table catch catch_all ref null if then else block loop br br_if return drop data mut struct array sub extern externref',
    'wit': 'package interface world record func export import use resource variant enum flags',
    'bash': 'wasm-pack emcc wat2wasm cargo npm wasmtime rustup',
    'html': '',
    'ts': 'export function return let const i32 f64 if else for',
}
COMM = {'js': r'//[^\n]*', 'c': r'//[^\n]*', 'rust': r'//[^\n]*', 'wat': r';;[^\n]*', 'wit': r'//[^\n]*', 'bash': r'#[^\n]*',
        'html': r'<!--.*?-->', 'ts': r'//[^\n]*'}


def code(src, lang='js', size=28, width=None):
    src = src.strip('\n')
    kws = '|'.join(re.escape(k) for k in KW.get(lang, '').split())
    pat = '(?P<c>' + COMM[lang] + ')|(?P<s>"[^"\n]*"|\'[^\'\n]*\'|`[^`\n]*`)'
    if lang == 'rust':
        pat += r'|(?P<a>#\[[^\]]*\])'
    if lang == 'wat':
        pat += r'|(?P<v>\$[\w.]+)'
    if kws:
        pat += rf'|(?P<k>(?<![\w$.-])(?:{kws})(?![\w$-]))'
    pat += r'|(?P<n>\b\d+(?:\.\d+)?\b)|(?P<f>\b[A-Za-z_][\w.]*(?=\())'
    col = {'c': '#6A9955', 's': '#CE9178', 'a': '#4EC9B0', 'v': '#9CDCFE', 'k': '#569CD6', 'n': '#B5CEA8', 'f': '#DCDCAA'}
    out, pos = [], 0
    for m in re.finditer(pat, src, flags=re.S):
        out.append(esc(src[pos:m.start()]))
        g = m.lastgroup
        out.append(f'<span style="color:{col[g]}">{esc(m.group())}</span>')
        pos = m.end()
    out.append(esc(src[pos:]))
    t = ''.join(out)
    t = re.sub(r'(?m)^( +)', lambda m: '&#160;' * len(m.group(1)), t)
    t = re.sub(r'(?<=>)( {2,})', lambda m: '&#160;' * len(m.group(1)), t)
    t = t.replace('\n', '<br>')
    w = f'width:{width}px;flex:none;' if width else ''
    return (f'<div style="{w}background:#1E1E1E;padding:24px 32px"><p style="font-family:{MONO};font-size:{size}px;'
            f'line-height:1.45;color:#D4D4D4">{t}</p></div>')


# ---------- tekst ----------
def h3(t, size=40):
    return f'<h3 style="font-family:{ARIAL};font-size:{size}px;font-weight:700;line-height:1.25;color:#262626">{inline(t)}</h3>'


def p(t, size=39, color=None, bold=False):
    c = f'color:{color};' if color else ''
    b = 'font-weight:700;' if bold else ''
    return f'<p style="font-size:{size}px;line-height:1.4;{c}{b}">{inline(t)}</p>'


def ul(items, size=37, ordered=False):
    tag = 'ol' if ordered else 'ul'
    return f'<{tag} style="font-size:{size}px;line-height:1.4">' + ''.join(f'<li>{inline(i)}</li>' for i in items) + f'</{tag}>'


def col(*parts, flex='1', gap=20):
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px;flex:{flex}">' + ''.join(parts) + '</div>'


def row(*parts, gap=48, align='start'):
    return f'<div style="display:flex;gap:{gap}px;align-items:{align}">' + ''.join(parts) + '</div>'


def card(title, body=None, size=27, fill='#DAE3F3', border='#8FAADC', tc='#1F3864', flex='1'):
    b = f'<p style="font-size:{size - 3}px;line-height:1.3;color:{tc}">{inline(body)}</p>' if body else ''
    return (f'<div style="background:{fill};border:1px solid {border};padding:20px 24px;display:flex;flex-direction:column;'
            f'gap:8px;flex:{flex}"><p style="font-size:{size}px;line-height:1.25;color:{tc};font-weight:700">{inline(title)}</p>{b}</div>')


def rood(title, body=None, size=27, flex='1'):
    return card(title, body, size, fill='#F4CCCC', border='#C00000', tc='#7F0000', flex=flex)


def groen(title, body=None, size=27, flex='1'):
    return card(title, body, size, fill='#E2EFDA', border='#70AD47', tc='#375623', flex=flex)


def pijl(size=56):
    return f'<div style="font-size:{size}px;line-height:1;color:{ROOD};flex:none;align-self:center;font-family:{ARIAL}">&#8594;</div>'


def flow(*boxes, gap=20):
    parts = []
    for i, b in enumerate(boxes):
        if i:
            parts.append(pijl(44))
        parts.append(b)
    return f'<div style="display:flex;gap:{gap}px;align-items:stretch">' + ''.join(parts) + '</div>'


def tabel(head, rows, widths, size=33):
    th = ''.join(f'<th style="width:{w}%;text-align:left;color:#FFFFFF;font-weight:700">{inline(h)}</th>' for h, w in zip(head, widths))
    out = f'<table style="font-size:{size}px;color:#404040;font-family:{ARIAL}"><tr style="background:{ROOD}">{th}</tr>'
    for i, r in enumerate(rows):
        bg = '#F2F2F2' if i % 2 == 0 else '#FFFFFF'
        tds = ''.join((f'<td><b>{inline(c)}</b></td>' if j == 0 else f'<td>{inline(c)}</td>') for j, c in enumerate(r))
        out += f'<tr style="background:{bg}">{tds}</tr>'
    return out + '</table>'


def spacer():
    return '<div style="flex:1"></div>'


def grid2(items, size=27):
    return ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 56px">'
            + ''.join(f'<p style="font-size:{size}px;line-height:1.35">{inline(i)}</p>' for i in items) + '</div>')


def groot_getal(getal, label, kleur=ROOD, size=120):
    return (f'<div style="display:flex;flex-direction:column;gap:8px;flex:1;align-items:flex-start">'
            f'<p style="font-family:{QUEST};font-size:{size}px;line-height:1;color:{kleur}">{getal}</p>'
            f'<p style="font-size:30px;line-height:1.3;color:#595959">{inline(label)}</p></div>')


def balk(label, pct, tekst, kleur=ROOD, breed=1000):
    return (f'<div style="display:flex;align-items:center;gap:28px"><p style="width:300px;flex:none;font-size:32px;font-weight:700">{inline(label)}</p>'
            f'<div style="width:{breed}px;background:#F2F2F2"><div style="width:{pct}%;background:{kleur};padding:14px 20px"><p style="font-size:30px;color:#FFFFFF;font-weight:700;white-space:nowrap">{inline(tekst)}</p></div></div></div>')


def img(naam, breed=None, hoog=None, rand=False):
    """Afbeelding uit bron/media, ingebed als data-URI zodat presentatie.html één bestand blijft."""
    pad = os.path.join(MEDIA, naam)
    mime = 'image/jpeg' if naam.lower().endswith(('.jpg', '.jpeg')) else 'image/png'
    data = base64.b64encode(open(pad, 'rb').read()).decode()
    st = ''
    if breed: st += f'width:{breed}px;'
    if hoog: st += f'height:{hoog}px;'
    st += 'object-fit:contain;display:block;' + ('border:1px solid #D9D9D9;' if rand else '')
    return f'<img src="data:{mime};base64,{data}" alt="" style="{st}">'


# ---------- slides ----------
def notitie(t):
    return '<aside>' + esc(t.strip()) + '</aside>'


def slide(sid, titel, body, notes, kort, kern=False, bron=None):
    """Standaard inhoudsslide. kort = lijst bullets voor de korte notities."""
    s = [f'<section id="{sid}" data-transition="fade" style="{BASE}">',
         f'<h2 style="font-family:{QUEST};font-size:64px;font-weight:400;line-height:1.15;color:{ROOD}">{inline(titel)}</h2>',
         body]
    if kern:
        s.append(f'<p style="position:absolute;right:128px;top:48px;width:360px;text-align:right;font-size:24px;color:{ROOD}">Kernbegrip</p>')
    if bron:
        s.append(f'<p style="position:absolute;left:128px;bottom:48px;width:1480px;font-size:24px;color:#7F7F7F">Bron: {esc(bron)}</p>')
    s.append('@@NR@@')
    s.append(notitie(notes))
    s.append('</section>')
    return {'id': sid, 'titel': re.sub(r'<[^>]+>', '', inline(titel)), 'html': '\n'.join(s), 'kort': kort, 'light': True}


def divider(sid, label, titel, sub, notes, kort):
    s = (f'<section id="{sid}" data-transition="fade" style="background:{ROOD};color:#FFFFFF;font-family:{ARIAL};padding:128px;'
         f'display:flex;flex-direction:column;justify-content:center;gap:28px">'
         f'<p style="font-size:44px;line-height:1.2;color:#FFFFFF">{esc(label)}</p>'
         f'<h1 style="font-family:{QUEST};font-size:104px;font-weight:400;line-height:1.1;color:#FFFFFF">{esc(titel)}</h1>'
         f'<p style="font-size:36px;line-height:1.4;color:#F4CCCC">{esc(sub)}</p>'
         f'@@NRR@@{notitie(notes)}</section>')
    return {'id': sid, 'titel': titel, 'html': s, 'kort': kort}


def cover(notes, kort):
    s = (f'<section id="cover" data-transition="fade" style="background:{ROOD};color:#FFFFFF;font-family:{ARIAL};padding:128px;'
         f'display:flex;flex-direction:column;justify-content:center;gap:32px">'
         f'<h1 style="font-family:{QUEST};font-size:128px;font-weight:400;line-height:1.05;color:#FFFFFF">Software Trends</h1>'
         f'<p style="font-family:{QUEST};font-size:60px;line-height:1.2;color:#FFFFFF">WebAssembly: van browsertruc tot universele runtime</p>'
         f'<p style="font-size:34px;line-height:1.4;color:#F4CCCC">Academiejaar 2026–2027</p>'
         f'{notitie(notes)}</section>')
    return {'id': 'cover', 'titel': 'Software Trends', 'html': s, 'kort': kort}


def waarom_wie(waarom, wie, size=26, stack=False):
    """Vast kader onderaan een functie-slide: waarom handig + welke bedrijven/software dit gebruiken."""
    if stack:
        size = 23
        return ('<div style="display:flex;flex-direction:column;gap:14px">'
                + card('Waarom is dit handig?', waarom, size=size + 2, fill='#E2EFDA', border='#70AD47', tc='#375623')
                + card('Wie gebruikt dit?', wie, size=size + 2)
                + '</div>')
    return ('<div style="display:flex;gap:28px;align-items:stretch">'
            + card('Waarom is dit handig?', waarom, size=size + 2, fill='#E2EFDA', border='#70AD47', tc='#375623')
            + card('Wie gebruikt dit?', wie, size=size + 2)
            + '</div>')


def eenvoudig(sid, titel, wat, vroeger, nu, waarom, wie, denkaan, notes, kort, kern=False, bron='webassembly.org/news/2025-09-17-wasm-3.0',
              t1='Vroeger', t2='Nu', t3='Waarom is dit interessant?', t4='Wie gebruikt dit?', voet='Denk aan: '):
    """Eenvoudige slide voor studenten: één zin uitleg, twee kaders (vroeger/nu), waarom interessant, wie gebruikt het."""
    body = (p(wat, 40)
            + row(rood(t1, vroeger, size=36), groen(t2, nu, size=36), gap=32)
            + row(card(t3, waarom, size=36), card(t4, wie, size=36), gap=32)
            + spacer()
            + p(voet + denkaan, 30, '#595959'))
    return slide(sid, titel, body, notes, kort, kern=kern, bron=bron)
