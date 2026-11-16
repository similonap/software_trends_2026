# Frame packet: 06-ai-accomplice

## Project inputs

- Project: /Users/slimmii/Git/supply-chain/videos/nx-s1ngularity
- Design tokens: /Users/slimmii/Git/supply-chain/videos/nx-s1ngularity/frame.md
- RULES_DIR: /Users/slimmii/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 6 — De AI als handlanger

- scene: a terminal panel; three commands type in one per name: `claude --dangerously-skip-permissions`, `gemini --yolo`, `q --trust-all-tools`, the flags in fire-orange; then a prompt line "You are a file-search agent…" and a "zoek: wallets · secrets" result
- voiceover: "Een postinstall-script zocht naar AI-tools op je machine. Claude. Gemini. Q. Het startte ze met de vangrails uit, en gaf één opdracht: zoek wallets en secrets."
- duration: 12.08s
- transition_in: push-slide LEFT
- status: outline
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

## Selected blueprint: prompt-type-submit-generate

# prompt-type-submit-generate — Prompt, Submit, Generate

**intent**: The AI-era demo shot — a `[prompt / query / command]` types character-by-character into a REAL product input (chat composer, search bar, terminal prompt, URL bar, sidebar assistant) and the machine answers: status theater into a streaming answer / agent action log / diff cards / chart / generated artifact — or the clip cuts at the submit and the ask itself is the show. The keyboard is the actor and the product is the responder. Distinct from `typewriter-reveal` (a line typed as bare typography on an empty field — no product surface, nothing answers) and from `cursor-ui-demo` (a cursor clicking a reconstructed UI through states — there the pointer drives every change; here any cursor work only primes the input or lands the submit, and every state change after that is the machine's own doing).

**roles served**

- Hook (from `app-window-push-in-prompt-typing`): when the opener is "watch me ask" — typed headline beat(s), ONE eased push-in lands tight on the product's input, the prompt types and the clip ends at / just after submission (sub-shape A).
- Hook (from `typed-command-output-scroll`): when the demo loop ITSELF is the hook — command in, output builds and scrolls, and a second command / retype starts before the cut, ending mid-action (sub-shapes B/C with the restart ending).
- Product_Intro (from `prompt-typing-composer`): when the first look at the product IS its composer — a brand beat opens onto the input surface, a long prompt types with hovers / attachments / dropdown picks, and the camera steers gently toward the input or the confirming control (sub-shape A, occasionally running through to an agent-log payoff).
- Product_Intro (from `search-query-walkthrough`): when the product is introduced through its search affordance — a short `[query]` types with a blinking caret, autocomplete / results populate LIVE, and a confirm click settles the result state (sub-shape C, search skin).
- Key_Feature (from `prompt-type-submit-generate`): when the capability is demoed as ONE prompt→response round trip — submit into thinking/status states, then a streaming answer, action-log rows with brand icons, green diff cards, a chart drawing itself, or an instant generated-app reveal (sub-shapes A/B/C — the family's widest role).
- CTA (from `install-command-end-card`): the install-command end card — the closing `[headline]` DEMOTES (shrinks, grays, lifts) to make room for a `[terminal pill]` that springs in and stretches wide, the `[install command]` types out with a blinking cursor, flanking metadata and a `[tool-icon row]` pop in, and the finished card holds long. No submit, no response — the typed command IS the ask (sub-shape A, terminal skin).

**duration**: 5.2–12s (A prompt-as-hook 5.2–12s, incl. the ~7.4s CTA end card; B full generate loop 5.45–11.9s; C instant-result surface 5.7–11.9s — a long-form family: most members run 7–12s because the response needs room to arrive)

**shot structure** (a `[product input]` on/inside a `[product surface — app window, web page, terminal, browser chrome, sidebar]` over `[bg color]`; the input is the gravitational center — the camera makes at most one or two purposeful moves toward or away from it and is otherwise LOCKED; typing is character-by-character behind a visible caret, and response content arrives progressively, never dumped; three folded sub-shapes — **(A) prompt-as-hook**: the clip ends at / just after the submit (or mid-word), the ask is the show; **(B) full generate loop**: submit → status theater → the output builds block by block; **(C) instant-result surface**: the machine answers with a finished surface, often re-queried before the cut)

- **Scene 0 (optional, 0.0–~2s) — lead-in beat.** ONE establishing move before the input owns the shot: a `[headline]` types on centered and clears; a `[title card]` hard-cuts away; a brand beat (`[logo/mascot]` centered, `[serif title]` building in word groups, logo shrinking-and-rising to dock top-center); an `[orb / mark]` forms with a glowing rim; the `[app window]` flies in with motion blur and settles; or a full-frame `[thumbnail grid]` parts at its vertical centerline to clear the stage. Keep it ≤2s — the input is the star.
  - _Variant — Hook_: typed headline beats carry the intro — "[Introducing X]" types on, holds, is replaced by the `[tagline]` typing in the identical style; the typing register is established before the product ever appears.
  - _Variant — Key_Feature_: the capability claim types as a bare title ("[Run a task across multiple models.]") then hard-cuts to the surface — or skip Scene 0 entirely and open on the live surface mid-workflow.
  - _Variant — CTA_: the `[closing line]` types on in two steps ("[Designed.] [Not generated.]") and holds — it will demote in Scene 2.

- **Scene 1 (~1–3s) — the input takes focus.** The `[product input]` arrives or is primed: a `[pill bar]` EXPANDS sideways from the mark/chip; a `[prompt palette / card]` SPRINGS in at center with a soft shadow; ONE smooth eased/accelerating push-in crops tight onto the composer inside the `[app window]` (headline chrome slides out of frame); a `[⌘K search modal]` springs to center while the page blurs behind it; a cursor clicks a `[menu row / Assistant button]` and the prompt block appears; or a `[✕ clear button]` empties the previous query back to `[placeholder]`. Optional composer ritual (pick 1–2, before or during typing): an `[attachment]` drags in and settles in a tray below the input; a `[model / option dropdown]` opens beneath the selector, rows hover-highlight, a checkmark lands and the toolbar label updates.
  - _Variant — Product_Intro_: the ritual is the introduction — a `[chip grid]` fades in and the cursor arcs across 2–3 hover highlights before clicking the one that opens the composer; the affordances are the tour.
  - _Variant — Key_Feature_: the surface already carries an old `[query]` and its previous `[result panel]` — clearing it says "this is a working tool, not a mockup".

- **Scene 2 (~2–6s) — the prompt types (the engine).** The `[prompt text]` types rapidly character-by-character behind a blinking caret; the input card GROWS downward / wraps as text fills, pushing footer controls and attachments down; a typed `[token]` may convert into an inline `[brand pill]` mid-typing (`[@browser]` → a colored `[Browser]` chip, typing continues around it); the camera may run ONE slow continuous push-in toward the input, decelerating to a near-hold on the typed ask. Sub-shape (A) may END here — cut mid-word with the caret blinking, or held on the finished prompt.
  - _Variant — Hook (A)_: the typed ask is the cliffhanger — end on the completed prompt, or on the submit click as the interface DIMS at the cut.
  - _Variant — Product_Intro (A)_: the camera dives toward the bottom input while `[option pills]` cascade in above it; the prompt is still mid-word at the cut — the product is introduced as something you talk to.
  - _Variant — CTA (A, install end card)_: the Scene-0 headline DEMOTES — scales ~50%, desaturates to gray, lifts upward — as a small `[$ chip]` spring-pops below and STRETCHES horizontally into a wide `[terminal pill]`; the `[install command]` types out inside it; a faint `[repo link]` and a "[Works with]" label fade in quietly; a row of `[tool icons]` pops in one after another with soft spring scale; the finished composition holds long, only the caret blinking.

- **Scene 3 (~4–7s) — submit + machine theater.** The `[submit control]` is clicked (cursor glide + press dip; the button may have MORPHED state on first keystroke — waveform → up-arrow — and may flip to a `[stop]` control while streaming) or the retype implies enter. The surface answers instantly with a working state: prior content VANISHES (chip grid gone, panel collapses to its slim header, whole layout swaps); then the theater — `[status phrases]` cross-dissolve with a left-to-right shimmer sweep ("[Thinking]" → "[Modeling…]" → "[Planning…]"), a `[spinner]` rotates over a loading strip, a row of `[loading cards]` lines up, or a `[checklist]` populates and its items flip one by one to green checks with strikethrough while a `[status heading]` flips tense ("[Using X]" → "[Used X]").
  - _Variant — (A) status-flare exit_: end the clip ON the theater — "[Generating…]" / the rotating spinner — the flare is the button; the answer is left to the imagination.

- **Scene 4 (rest) — the answer arrives.** Choose by sub-shape:
  - **Sub-shape B (full generate loop)**: the output BUILDS progressively, each block pushing content down — `[answer text]` streams paragraph by paragraph; `[action-log rows]` pop in sequentially, each with a `[brand icon]`; `[diff cards]` expand with green-highlight added lines; `[chart lines]` draw staggered left-to-right from a shared origin; an `[ASCII / summary table]` draws in; live counters tick; the surface auto-scrolls vertically to follow the newest line (page, terminal, or in-card scroll) — often under ONE slow continuous push-in on the result window.
  - **Sub-shape C (instant-result surface)**: the machine answers with a finished surface — the matching `[result / article]` renders in place; `[autocomplete chips]` stagger-pop below the bar WHILE the query types (the machine answers every keystroke), then a hover fills the `[Search button]` solid and a click confirms; the `[generated page]` rises as a rounded card and SCROLLS continuously beneath the pinned prompt; a blur-whip resolves onto the `[artifact window]` and a tab click FLIPS code → preview; or a zoom-out reveals the prompt pill was inside a full `[workspace]` where the `[content]` rewrites itself live.

- **Scene 5 (final beat) — resolve.** Diverges by role and sub-shape:
  - _Variant — Key_Feature (hold)_: HOLD on the completed output — chart finished, diff cards + `[action buttons]` fully rendered; no fade-out, no blank end frame.
  - _Variant — Product_Intro (confirm)_: the cursor lands the confirming click (`[Create PR]` / `[Generate]` / `[Search]`) as the clip ends, or extras fade and a final push-in leaves the clean end state; one member hard-cuts to a minimal `[end card]` — the submit button alone at dead center with a settle pop.
  - _Variant — Hook (restart — the signature)_: a SECOND `[prompt / command]` starts typing at a fresh prompt line, or the query BACKSPACES-AND-RETYPES and the output swaps wholesale to `[result 2]` — the clip ends MID-ACTION, mid-scroll or mid-word: the loop is endless, and that is the point.
  - _Variant — CTA_: the end card from Scene 2 simply holds to the last frame; the blinking cursor is the only motion.

**motion vocabulary**: character-by-character typing with blinking caret / block cursor; typed-headline beats replacing each other; input pill grows / wraps downward into a multi-line box; prompt palette / card springs in; pill bar expands sideways from a mark or chip; orb formation with glowing rim; typed token → inline brand-pill morph mid-typing; placeholder clear; ✕-click query clear; backspace-and-retype query swap; attachment drag-in and tray settle; dropdown open + row hover-highlight + checkmark select + toolbar label update; chip-grid hover dance; cursor glide / arc with hover highlight fills; click press dip; submit-button state morph (waveform→up-arrow, submit→stop); hover fill-state swap on a Search button; content vanish / panel collapse / layout swap on submit; status-phrase cross-dissolves with left-to-right shimmer sweep; pulsing "Thinking"; spinner rotation; loading strip; animated trailing dots; loading model-card row; status-heading tense flip (Using→Used); checklist squares flipping to green checks with strikethrough; action-log rows popping in sequentially with brand icons; streaming text blocks pushing content down; green-highlight diff cards expanding; staggered left-to-right chart line-draws; ASCII / summary table draw-in; count-up ticker; vertical output scroll (page / terminal / in-card) following the newest line; generated page rising as a rounded card and scrolling beneath a pinned prompt; autocomplete chips rapid stagger-pop; code↔preview instant flip on tab click; blur-whip transition; prompt jumps to a heading on submit; zoom-out reveal from prompt pill to full UI window; single eased / accelerating push-in landing on the input; slow continuous push-in on the result window; window fly-in with motion blur; zoom + pan cropping browser chrome; ⌘K modal spring-in with background blur; full-frame grid parting at the vertical centerline; headline demotion (scale-down + desaturate + lift); chip horizontal-stretch into a wide terminal pill; quiet low-contrast metadata fade-ins; sequential spring pop-ins of an icon row; second prompt typing at the cut; interface dim / fade at the cut; long static end hold with blinking cursor.

**rule mapping**

- character-by-character typing, placeholder clear, backspace-and-retype, second prompt at the cut, typed-headline beats → `discrete-text-sequence` (typing / typos / holds / backspace) backed by `gsap-effects` (typewriter recipe)
- blinking caret / block cursor (persisting through holds) → `context-sensitive-cursor`
- prompt / status / output phrase windows, script-driven beat durations → `dynamic-content-sequencing`
- input card grows downward / wraps as text fills → `anchored-layout-expand` (top-anchored downward growth, stepped at wrap boundaries)
- typed token → inline brand-pill morph mid-typing → composition: `scale-swap-transition` (token→chip swap at the conversion threshold) + `card-morph-anchor` (the reflow around the chip)
- prompt palette / modal / dropdown springs in; loading cards, log rows, diff cards, autocomplete chips, icon rows arriving staggered → `spring-pop-entrance` (single hero or staggered group)
- pill bar expands sideways from a mark; chip stretches into a wide terminal pill → `card-morph-anchor` (container morph)
- cursor glide to a control, press, ripple → `cursor-click-ripple`; the press dip + recovery → `press-release-spring` (or `physics-press-reaction` for cursor+button compressed together)
- hover highlight fills, Search-button instant solid fill, UI keyword accents → `asr-keyword-glow` (static-timeline glow variant) or `press-release-spring` (color-transition variation)
- attachment drag-in with cursor → `context-sensitive-cursor` (pointer↔grab) + `spring-pop-entrance` (tray settle)
- content vanish / layout swap / panel collapse on submit; code↔preview instant flip → `scale-swap-transition` (paired same-center swap) or a hard `tl.set` state swap via `discrete-text-sequence` semantics
- prompt jumps to a heading on submit → FLIP reposition — see `hyperframes-keyframes` (FLIP); the travel itself via `nudge-curve` (slow-fast-slow group slide)
- status-phrase cross-dissolves with shimmer sweep → `discrete-text-sequence` (phrase swaps) + `ambient-glow-bloom` (Shimmer sweep variation — single-pass traveling sheen, clipped to the text)
- spinner rotation, animated trailing dots, pulsing loader glyphs → `svg-icon-enrichment` (rotating / pulsing internal SVG elements); the bounded "Thinking" pulse → `sine-wave-loop` (finite repeats — this pulse PERFORMS status, it is not idle wobble)
- checklist state flips, status-heading tense flip, status-pill swaps → `discrete-text-sequence` (discrete state stepping); the checkmark stamp → `svg-path-draw` or `spring-pop-entrance`
- streaming text blocks / log rows pushing content down → `dynamic-content-sequencing` (per-block windows) + `spring-pop-entrance` (per-row arrival)
- vertical output scroll following the newest line (page / terminal / in-card) → composition: content translateY keyed to the same timeline as the content windows + a matched `viewport-change` counter-pan when the frame itself travels
- generated page as a rounded card whose internal content scrolls → `3d-page-scroll` (flat variant — internal scroll of a page card)
- staggered chart line-draws → `svg-path-draw` (stroke-dashoffset, staggered starts)
- count-up ticker / live counters → `counting-dynamic-scale`; result bars / fills → `stat-bars-and-fills`
- single eased push-in landing on the input; slow continuous push-in on the result → `multi-phase-camera` (push phase) with the destination framed via `coordinate-target-zoom`
- zoom-out reveal from prompt pill to full workspace; zoom + pan cropping chrome → `viewport-change` (composite pan+scale on the `.world` wrapper)
- window fly-in with motion blur; blur-whip transition → `motion-blur-streak`
- ⌘K modal with background blur → `depth-of-field-blur` (blur the page plane, keep the modal sharp) + `spring-pop-entrance`
- full-frame grid parting at the vertical centerline → `center-outward-expansion` (halves glide outward in lockstep)
- orb formation with glowing rim → `ambient-glow-bloom` + `spring-pop-entrance`
- headline demotion (scale-down + desaturate + lift) → `gsap-effects` (plain composite tween; no dedicated rule needed)
- interface dim at the cut, hard cut to a minimal end card, end mid-word / mid-scroll → exit conventions, no rule needed
- long static end hold with only the caret blinking → `context-sensitive-cursor` (the blink is the sanctioned residual motion)

**camera modifier** (the camera always serves the ask or the answer; many members are fully camera-static — typing, submit theater, and streaming carry the shot)

- ONE smooth eased / accelerating push-in that lands tight on the input and LOCKS (Hook, Product_Intro) → `multi-phase-camera` (push) + `coordinate-target-zoom` (target the input) — the defining move of the "watch me ask" opener.
- ONE slow continuous push-in running under the typing or under the output build, decelerating to a near-hold (Product_Intro, Key_Feature) → `multi-phase-camera` — gives the response weight without stealing from it.
- ONE zoom-out reveal — the prompt pill turns out to live inside a full workspace (Key_Feature, sub-shape C) → `viewport-change` (pull-back) — the inverse move; the ask was closer to the product than you thought.
- Entry-only flourishes: window fly-in with motion blur (`motion-blur-streak`), zoom + pan cropping browser chrome (`viewport-change`) — both settle before typing starts.
- Never more than two real viewport moves per shot; the frame is LOCKED during submit theater and streaming (the content scrolls, the camera does not).

## Selected motion rule: css-marker-patterns

# CSS Patterns for Marker Highlighting

## Contents

- [1. Highlight Mode](#1-highlight-mode)
- [2. Circle Mode](#2-circle-mode)
- [3. Burst Mode](#3-burst-mode)
- [4. Scribble Mode](#4-scribble-mode)
- [5. Sketchout Mode](#5-sketchout-mode)
- [Combining Modes in Captions](#combining-modes-in-captions)

Pure CSS + GSAP implementations of all five MarkerHighlight.js drawing modes — no external library dependency, full timeline control. Snippets show mechanism DOM only, inside a standard scene clip (hyperframes-core); assume `tl` exists.

Shared scaffold for every mode: the wrap is `position: relative; display: inline`; the text copy is `position: relative` and z-indexed **above** the accent (below it for sketchout, where the lines cross the text).

## 1. Highlight Mode

Yellow marker sweep behind text — the most common mode.

```html
<span class="mh-highlight-wrap">
  <span class="mh-highlight-bar" id="hl-1"></span>
  <span class="mh-highlight-text">highlighted text</span>
</span>
```

```css
.mh-highlight-bar {
  position: absolute;
  inset: 0 -6px; /* bleed past the text edges */
  background: #fdd835;
  opacity: 0.35;
  transform: scaleX(0);
  transform-origin: left center;
  border-radius: 3px;
  z-index: 0;
}
```

```js
tl.to("#hl-1", { scaleX: 1, duration: 0.5, ease: "power2.out" }, 0.6);
// Optional hand-drawn skew: gsap.set("#hl-1", { skewX: -2 });
// Multi-line: tl.to(".mh-highlight-bar", { scaleX: 1, ..., stagger: 0.3 }, 0.6);
```

## 2. Circle Mode

Hand-drawn ellipse around text — `border-radius: 50%` plus a slight rotation for organic feel.

```html
<span class="mh-circle-wrap">
  <span class="mh-circle-text">IMPORTANT</span>
  <span class="mh-circle-ring" id="circle-1"></span>
</span>
```

```css
.mh-circle-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 130%; /* tight (short words): 150%; rounded-rect: 120% + border-radius: 30% */
  height: 160%;
  transform: translate(-50%, -50%) rotate(-3deg) scale(0);
  border: 3px solid #e53935;
  border-radius: 50%;
  z-index: 0;
}
```

```js
tl.to("#circle-1", { scale: 1, rotation: -3, duration: 0.6, ease: "back.out(1.7)" }, 0.7);
```

## 3. Burst Mode

Radiating lines from text center — each line a positioned span rotated to its angle. Use ~12 lines at 30° steps and **vary `--len` (40–80px)**; equal lengths look mechanical.

```html
<span class="mh-burst-wrap">
  <span class="mh-burst-text">WOW</span>
  <span class="mh-burst-container" id="burst-1">
    <span class="mh-burst-line" style="--angle: 0deg; --len: 70px;"></span>
    <span class="mh-burst-line" style="--angle: 30deg; --len: 55px;"></span>
    <!-- …one line per 30° step through 330deg, --len varied 40-80px -->
  </span>
</span>
```

```css
.mh-burst-container {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  z-index: 1; /* text copy at z-index: 2 */
}
.mh-burst-line {
  position: absolute;
  display: block;
  width: 3px;
  height: var(--len);
  background: #1e88e5;
  left: -1.5px;
  top: calc(-1 * var(--len));
  transform: rotate(var(--angle));
  transform-origin: bottom center;
  opacity: 0;
}
```

```js
tl.fromTo(
  "#burst-1 .mh-burst-line",
  { scaleY: 0, opacity: 0 },
  { scaleY: 1, opacity: 1, duration: 0.4, ease: "power2.out", stagger: 0.03 },
  0.7,
);
```

## 4. Scribble Mode

Wavy SVG underline that draws itself via `stroke-dashoffset`.

```html
<span class="mh-scribble-wrap">
  <span class="mh-scribble-text">underlined text</span>
  <svg class="mh-scribble-svg" viewBox="0 0 500 24" preserveAspectRatio="none">
    <path
      id="scribble-1"
      d="M0,12 Q31,0 62,12 Q93,24 125,12 Q156,0 187,12 Q218,24 250,12 Q281,0 312,12 Q343,24 375,12 Q406,0 437,12 Q468,24 500,12"
      fill="none"
      stroke="#FDD835"
      stroke-width="3"
      stroke-linecap="round"
    />
  </svg>
</span>
```

```css
.mh-scribble-svg {
  position: absolute;
  left: 0;
  bottom: -6px; /* strikethrough variant: top: 50%; transform: translateY(-50%) */
  width: 100%;
  height: 24px;
  z-index: 0;
}
```

```js
const path = document.querySelector("#scribble-1");
const len = path.getTotalLength();
gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
tl.to("#scribble-1", { strokeDashoffset: 0, duration: 0.8, ease: "power1.inOut" }, 0.7);
```

Path tuning: the `Q` control points alternate y between 0 and 24 for a natural wobble. Tighter waves = smaller x-increments (~25px per half-wave); looser = ~50px; subtler amplitude = y range 0–16.

## 5. Sketchout Mode

Cross-hatch over de-emphasized text — two angled lines create a "crossed out" effect.

```html
<span class="mh-sketchout-wrap">
  <span class="mh-sketchout-text">old price</span>
  <span class="mh-sketchout-lines" id="sketchout-1">
    <span class="mh-sketchout-line mh-sketchout-fwd"></span>
    <span class="mh-sketchout-line mh-sketchout-bwd"></span>
  </span>
</span>
```

```css
.mh-sketchout-lines {
  position: absolute;
  inset: 0 -4px;
  overflow: hidden;
  z-index: 1; /* text at z-index: 0 — the lines cross OVER it */
}
.mh-sketchout-line {
  position: absolute;
  display: block;
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  background: #e53935;
  transform-origin: left center;
}
.mh-sketchout-fwd {
  transform: scaleX(0) rotate(-12deg);
}
.mh-sketchout-bwd {
  transform: scaleX(0) rotate(12deg);
}
```

```js
// Forward slash first, backward follows
tl.to("#sketchout-1 .mh-sketchout-fwd", { scaleX: 1, duration: 0.3, ease: "power2.out" }, 1.0);
tl.to("#sketchout-1 .mh-sketchout-bwd", { scaleX: 1, duration: 0.3, ease: "power2.out" }, 1.15);
```

## Combining Modes in Captions

Cycle modes across caption groups for visual variety — every 2-3 groups for high energy, 3-4 for medium, 4-5 for low:

```js
const MODES = ["highlight", "circle", "burst", "scribble"];
GROUPS.forEach((group, gi) => {
  const mode = MODES[gi % MODES.length];
  group.emphasisWords.forEach((word) => applyMode(word.el, mode, tl, word.start));
});
```
