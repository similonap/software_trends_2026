"""Bouwt de ingesproken video opnieuw op uit script.md en slides/.

Gebruik:
  python3 maak.py                 alles bijwerken (enkel gewijzigde slides opnieuw inspreken)
  python3 maak.py --droog         toon wat er zou gebeuren, zonder iets te genereren
  python3 maak.py --opnieuw ID..  spreek deze slides opnieuw in, ook als de tekst niet veranderde
  python3 maak.py --snelheid 1.1  spreeksnelheid voor slides die nu ingesproken worden (0.7 tot 1.2)
"""
import argparse, hashlib, html, json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HIER = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HIER)
VIDEO = os.path.join(PROJECT, 'ingesproken-slides-2026.mp4')
SCRIPT_MD = os.path.join(PROJECT, 'ingesproken-script-40min.md')

VOICE_ID = '8OezxDDjGa2d9W45o5Qs'  # Andie
MODEL = 'eleven_v4'
PAUZE = 0.8  # seconden stilte na elke slide
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

HEAD = ('<!doctype html><html><head><meta charset="utf-8">'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Questrial&family=Source+Code+Pro:wght@400;600&display=swap">'
        '<style>*{margin:0;box-sizing:border-box} body{background:#888;font-family:Arial} '
        'section{position:relative;width:1920px;height:1080px;overflow:hidden;margin:0}\n'
        'ul,ol{padding-left:1.15em} x-shape{display:block} aside{display:none} table{border-collapse:collapse} '
        'td,th{border:1px solid #BFBFBF;padding:.35em .6em;vertical-align:top}\n'
        'x-shape[kind=arrow-right]{clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%)} '
        'x-shape[kind=arrow-down]{clip-path:polygon(30% 0,70% 0,70% 60%,100% 60%,50% 100%,0 60%,30% 60%)}'
        '</style></head><body style="margin:0;overflow:hidden">')


def pad(*delen):
    return os.path.join(HIER, *delen)


def lees_script():
    tekst = open(pad('script.md'), encoding='utf-8').read()
    S = {}
    for blok in re.split(r'^## ', tekst, flags=re.M)[1:]:
        kop, _, rest = blok.partition('\n')
        sid = kop.split('|')[0].strip()
        alineas = [' '.join(a.split()) for a in re.split(r'\n\s*\n', rest) if a.strip()]
        S[sid] = '\n\n'.join(alineas)
    return S


def sleutel(*delen):
    h = hashlib.sha1()
    for d in delen:
        h.update(d if isinstance(d, bytes) else str(d).encode())
    return h.hexdigest()


def titel(sid):
    h = open(pad('slides', f'{sid}.html'), encoding='utf-8').read()
    m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', h, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1).replace('<br>', ' '))).strip() if m else sid


def duur(bestand):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', bestand],
                       capture_output=True, text=True, check=True)
    return float(r.stdout)


def inspreken(sid, S, order, snelheid):
    i = order.index(sid)
    mp3 = pad('audio', f'{sid}.mp3')
    tmp = mp3 + '.tmp.mp3'
    args = ['elevenlabs', 'text-to-speech', 'convert', '--voice-id', VOICE_ID, '--model-id', MODEL,
            '--language-code', 'nl', '--output-format', 'mp3_44100_128', '--text', S[sid], '-o', tmp]
    if i > 0: args += ['--previous-text', S[order[i - 1]]]
    if i < len(order) - 1: args += ['--next-text', S[order[i + 1]]]
    if snelheid != 1.0: args += ['--voice-settings.speed', str(snelheid)]
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(tmp):
        return sid, 'FOUT ' + (r.stderr or r.stdout)[-300:]
    os.replace(tmp, mp3)
    open(pad('audio', f'{sid}.txt'), 'w', encoding='utf-8').write(S[sid])
    return sid, 'ingesproken'


def renderen(sid):
    sectie = open(pad('slides', f'{sid}.html'), encoding='utf-8').read()
    k = sleutel(HEAD, sectie)
    png, kfile = pad('build', 'png', f'{sid}.png'), pad('build', 'png', f'{sid}.key')
    if os.path.exists(png) and os.path.exists(kfile) and open(kfile).read() == k:
        return False
    tmp_html = pad('build', 'png', f'{sid}.html')
    open(tmp_html, 'w', encoding='utf-8').write(HEAD + sectie + '</body></html>')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1920,1080',
                    '--virtual-time-budget=6000', f'--screenshot={png}', f'file://{tmp_html}'],
                   capture_output=True, check=True)
    open(kfile, 'w').write(k)
    return True


def segment(sid):
    png, mp3 = pad('build', 'png', f'{sid}.png'), pad('audio', f'{sid}.mp3')
    k = sleutel(open(png, 'rb').read(), open(mp3, 'rb').read(), PAUZE)
    mp4, kfile = pad('build', 'seg', f'{sid}.mp4'), pad('build', 'seg', f'{sid}.key')
    if os.path.exists(mp4) and os.path.exists(kfile) and open(kfile).read() == k:
        return False
    t = round(duur(mp3) + PAUZE, 3)
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-loop', '1', '-framerate', '25', '-i', png, '-i', mp3,
                    '-af', f'apad=pad_dur={PAUZE},aresample=44100', '-t', str(t),
                    '-c:v', 'libx264', '-tune', 'stillimage', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p',
                    '-r', '25', '-c:a', 'aac', '-b:a', '160k', '-ar', '44100', '-ac', '1', mp4], check=True)
    open(kfile, 'w').write(k)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--droog', action='store_true')
    ap.add_argument('--opnieuw', nargs='*', default=[])
    ap.add_argument('--snelheid', type=float, default=1.0)
    a = ap.parse_args()

    order = json.load(open(pad('slides', 'deck.json')))['order']
    S = lees_script()
    ontbreekt = [s for s in order if not S.get(s)]
    extra = [s for s in S if s not in order]
    onbekend = [s for s in a.opnieuw if s not in order]
    if ontbreekt or onbekend:
        sys.exit(f'Geen spreektekst voor: {ontbreekt or onbekend}. Gebruik de slide-id uit slides/deck.json.')
    if extra:
        print('Let op, deze ids staan in script.md maar niet in de deck:', extra)

    def gewijzigd(s):
        txt = pad('audio', f'{s}.txt')
        return not os.path.exists(pad('audio', f'{s}.mp3')) or not os.path.exists(txt) \
            or open(txt, encoding='utf-8').read() != S[s]
    te_doen = [s for s in order if s in a.opnieuw or gewijzigd(s)]
    tekens = sum(len(S[s]) for s in te_doen)
    print(f'In te spreken: {len(te_doen)} slides, {tekens} tekens' + (f': {", ".join(te_doen)}' if te_doen else ''))
    if a.droog:
        return

    # De eerste opname apart: gelijktijdige calls vernieuwen anders allemaal tegelijk het
    # login-token, en dan maakt ElevenLabs de sessie ongeldig.
    def toon(resultaten):
        for sid, status in resultaten:
            print(f'  {sid}: {status}', flush=True)
            if status.startswith('FOUT'):
                sys.exit('Gestopt: inspreken mislukt. Bij een 401: elevenlabs auth login')
    toon([inspreken(s, S, order, a.snelheid) for s in te_doen[:1]])
    with ThreadPoolExecutor(4) as ex:
        toon(ex.map(lambda s: inspreken(s, S, order, a.snelheid), te_doen[1:]))

    os.makedirs(pad('build', 'png'), exist_ok=True)
    os.makedirs(pad('build', 'seg'), exist_ok=True)
    with ThreadPoolExecutor(4) as ex:
        n = sum(ex.map(renderen, order))
    print(f'Slides gerenderd: {n}')
    n = sum(segment(s) for s in order)
    print(f'Videostukken gemaakt: {n}')

    lijst = pad('build', 'lijst.txt')
    open(lijst, 'w').write(''.join(f"file '{pad('build', 'seg', s + '.mp4')}'\n" for s in order))
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lijst,
                    '-c', 'copy', '-movflags', '+faststart', VIDEO], check=True)

    out = ['# Ingesproken versie (ongeveer 40 minuten)\n',
           'Ingekorte spreektekst op basis van `begeleidende-tekst-2026.md`, ingesproken met ElevenLabs '
           '(model eleven_v4, stem Andie). Video: `ingesproken-slides-2026.mp4`. '
           'Bron: `ingesproken/script.md`; dit bestand wordt gegenereerd door `ingesproken/maak.py`.\n']
    t = 0
    for i, s in enumerate(order, 1):
        out.append(f'\n## {int(t // 60):02d}:{int(t % 60):02d} – Slide {i}: {titel(s)}\n\n{S[s]}\n')
        t += duur(pad('audio', f'{s}.mp3')) + PAUZE
    open(SCRIPT_MD, 'w', encoding='utf-8').write(''.join(out))
    print(f'Klaar: {VIDEO} ({int(t // 60)}:{int(t % 60):02d})')


if __name__ == '__main__':
    main()
