# Complete style specifications 29


<!-- STYLE: iso-infographic -->

- **Projection**: axes at 30°. `sx = (x − y)·cos30°·k`, `sy = ((x + y)·½ − z)·k`; x runs down-right, y down-left, z up; painter depth = x + y + z. Everything is queued and depth-sorted, then flushed.
- **Three tones per face** chosen from its normal: top light, left (+y) mid, right (+x) dark. Derive tones from one base colour: mix toward warm white ~20 % for the top and toward a cool dark (e.g. `#231A2C`) ~22 % for the dark side, so shadows are slightly cool.
- **Ink lines** (2 px) only for infographic elements: leaders, pins, cut lines, rings, routes, labels.
- **The board**: floats on a pale background with a faint isometric dot lattice and a soft blurred shadow; its front faces show strata (soil, water column, floors, pipes) where the section meets the edge.
- **Composites** (a terraced hill with shrubs, a crane over a ship) are drawn as one ordered item or given a depth bias; generic painter sorting fails on them.
- **People**: minimal billboards (round head, tapered two-tone body, a thick arm stroke, a hat or hair shape for identity, no faces), stepping at 12 fps.
- **Close-ups** of hands or objects: flat faceted shapes in three tones, same logic as the blocks.
- **Level of detail by zoom**: skip small world detail at high zoom, fade tall objects in by zoom so a pull-out never sweeps a giant shape through the frame.

## 3. Colour logic

- **A pale neutral ground** (cream, paper grey or pale blue) and **5–7 flat hues**, each with its three tones; one ink colour.
- **Colour codes meaning**, the way a legend does: one hue per material or role (water is always the same blue, the subject always its hue). Never reuse a hue for two meanings.
- **The subject's hue is reserved**: when the story needs "this one", everything else desaturates toward warm grey and only the subject keeps its colour (focus + context).
- Stations that must be found in a wide shot get a pale plate with a dashed ink outline plus one accent hue.
- Examples: a recycling chain — bottle green, kraft brown, can silver-blue, compost umber, mustard on cream; a hospital — teal, coral, lavender, steel grey on pale grey; a data centre — electric blue, amber, graphite, mint on off-white.

## 4. Type & subtitles

- One geometric sans (e.g. Jost): titles 600 all caps with ~0.12 em tracking, numbers 400 large (~44 px), units at half size. All text has a ~7 px halo in the ground colour so it reads over any block.
- **Label pins**: dot (ink ring, pale fill) → vertical leader → horizontal rule → text. Pins point up or down, left or right, chosen per station so labels never cover the subject.
- **Titles** can be isometric type on a world plane, extruded as blocks.
- **The subtitle is a map label**: a pale card with a small radius and an ink border, a tiny iso cube as legend chip, sans ~42 px, bottom-centre; border draws first, text wipes in. Keep the bottom ~170 px clear for it. Hold ≥ max(1.8 s, speech + 0.6 s); lines never overlap titles or other lines.
- **An end frame can be the legend**: title, totals, the Isotype key, credits, "NOT TO SCALE".

## 5. Motion quality

- **Nothing moves without a line leading it**: a route line is drawn slightly ahead, a leader grows before an inset opens, a cut line draws before a skin slides away.
- **Cutaway**: cut line (~0.3 s) → the near skin slides out along its normal and fades (~0.35 s, ease-out) → hatched section rims fade in over the last part.
- **Isotype fill**: icons pop with a back-ease (overshoot), one per subdivision of the beat; count-up numbers run over the same span.
- **Accumulation = acceleration**: arrivals on quarter notes, then eighths, then waves; the eye feels the system taking over. Solids arrive by motion, never by alpha (semi-transparent blocks look like ghosts).
- **Objects perform**: squash on landing (~18 %) and small bounces; colour changes that show a process (raw → cooked, empty → full).
- **Vehicles** follow polylines with ease-in-out and face their tangent.

## 6. Camera grammar

A vocabulary, not a route. The camera is a world centre plus a **log-interpolated zoom** k (px per unit); the projection never changes. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow along a route | process; cause → effect | a supply chain; a journey; a signal |
| Hold wide + circular inset | the system and the individual together | one worker in a factory; one cell in an organ |
| Push through nested cutaways | a fall into scale; finding one thing among millions | a needle in a haystack; inside a machine |
| Fast log pull-out | release; the big picture after a detail | scale reveal; a statistic made physical |
| Locked frame while things accumulate | a system filling up; overload | a queue; traffic; data growing |
| Lateral follow over emptiness | a breath; distance | an ocean; a wait; a quiet phase |
| Top-to-bottom tilt through strata | layers; depth; history | geology; a city's underground; a software stack |
| Switch boards (a second diorama) | before/after; here vs there | two cities; two eras; two designs |

Framing: the subject ≥ 1/3 of frame height at key moments; labels never cover it; the subtitle zone stays clear. One continuous take is one option; a cut to a new board or an inset is another.

## 7. Sound palette

- **Music**: acoustic and light: kalimba, marimba, nylon guitar, pizzicato, woodblock and hand percussion (shaker, bongo, cajon), upright or synth bass, glockenspiel, toy piano, or a clean electronic pulse for technical systems. A short motif can mark the subject each time it appears.
- **Techniques (options)**: one sound per icon as numbers fill; instruments dropping out and a low-pass closing as the camera dives; J-cuts (the next station's sound 0.5 s before it appears); one note per station during a final pull-back.
- **Ambience beds per station**, crossfaded (wind and birds, harbour, sea, city hum, machine room, crowd murmur).
- **Foley by material**: fibre snap, fleshy thud, grains pouring, granular rattles, inharmonic steel partials for containers, paper tear, ceramic plink, liquid pour with rising pitch, servo whine, keyboard clicks.
- **Silence**: digital zero or one faint sound; the first sound after it should be one of the most important in the film.
- **Mix**: music ducked ~8 dB under voice, ambience ~7 dB; keep high-band beds (2.5–7 kHz) very low under speech or whisper mishears words. Final −14 LUFS.
- **Voice**: clear, friendly explainer; short lines.

## 8. Native moves

A menu: use the ones your story needs.

- **Cutaway.** Cut line, skin slides away, hatched rims remain. *Fits content like:* a heart's chambers; a server rack; a beehive.
- **Isotype number.** Identical icons in a new arrangement each time (a calendar, a bar, a silhouette formed by the icons themselves). *Fits content like:* votes in an election; litres of water per product; users of an app.
- **Focus + context.** Everything greys except the subject. *Fits content like:* one patient in a hospital; one packet in a network; one tree in a forest.
- **Frame within the frame.** A leader grows into a circular inset with a close-up. *Fits content like:* a chip on a circuit board; a worker's hands; a crack in a bridge.
- **Scale reveal.** Pull back until every label is on screen and the last frame is a finished infographic. *Fits content like:* how a city is powered; a school's day; a festival site.
- **Tracked subject.** One object followed with a "you are here" ring. *Fits content like:* a letter through the post; a drop through a water plant; a vaccine dose.
- **Strata cross-section.** The board's edge becomes the story (layers added or removed). *Fits content like:* a mine; an archaeological dig; a building's floors.

## 9. Pitfalls of the medium

- Newell normals depend on vertex order: faces get culled as back faces → give every face an outward hint and flip the normal to match before culling.
- Painter sorting breaks on composites → draw them as one ordered item; add depth bias for overhangs.
- Semi-transparent moving solids look like ghosts → motion only, no alpha.
- A hull or wheel touching the wrong surface reads as an accident → leave visible clearance.
- World geometry behind a close-up becomes giant discs → skip detail above a zoom threshold, paint a flat backdrop behind hero layers.
- A pull-out through a tall object gives one ugly frame → fade tall objects in by zoom.
- Hidden jumps (a time or place change during a dive) must be drawn in screen space anchored on the tracked subject, so the frame doesn't reveal the jump.
- An object drawn with the wrong silhouette reads as something else (a white box with a red roof is a house) → give machines their tell-tale parts.

## 10. Engine

`demo/engine.js` is dependency-free Canvas 2D: `Iso` (projection, camera, depth-sorted queue: `box`, `prism`, `cyl`, `cone`, `roof`, `sphere`, `flat`, `line3`, `bill`, `text3`, `push/pop` local frames, `desat` + `keep` one-colour hook), `tri()` three-tone generator, `pin`, `inset`, `cutLine`, `hatch`, `ring`, `ICON.*` + `iconGrid`, `person`, and `shape()` which turns any 2D outline into a shaded isometric solid. API table and a minimal example (a shape the demo never uses): [DEMO.md](DEMO.md) "Engine reference".

## 11. Variation space

You decide the system, the board (or several), whether there is a tracked subject, the numbers, the camera path, the opening and the ending. All far from our demo:

- Structures: **one building, floor by floor** (a tilt down through a cutaway tower, each floor a step); **two boards compared** (the same system in two places or eras, alternating, then side by side); **a cycle** (a loop route that returns to its start with one number changed each lap).
- Openings: **the finished infographic**, which then comes apart into its moving parts; **one icon** that multiplies until it becomes the landscape; **a question written as an isometric title** on an empty board.
- Endings: **an unanswered station** (the route stops at an empty plate with a question mark); **the legend alone**, the board faded out; **a close-up of a single icon**, the whole number behind it out of focus.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: dark-keynote -->

# Dark Tech Keynote — Style Prompt

> A software launch film where the interface itself is the star: near-black gradient, hairline grid, soft light, one brand accent, and UI that moves with snap-grid precision. Light reveals, one giant number, and a sound design that is as ordered as the pixels.
> **References (grammar only):** Apple product reveals (black stage, light sweeps, one line per screen, the lone giant number); Linear / Stripe / Vercel launch videos (snap-grid motion, 1 px lines, one accent); Steve Reich's process music (phasing, subtraction); Edgar Wright's insert cuts. Never use their names, interfaces, fonts, system controls, melodies or logos, and never name them in the film.

## 1. Essence, and what it is not

A keynote-grade product film for **software**. There is no physical product and no glass render: the protagonist is the interface (a cursor, windows, notifications, tiles, a number). It lives on a dark stage lit by soft, cool light, with **one brand accent** reserved for the single most important element.

The style is defined by **precision**: every element snaps to a grid, every motion lands on a beat, every sound belongs to one designed family. Drama comes from contrast: disorder shown as generated UI, one decisive action, then empty space.

Not a glass product render (no physical object), not a screencast (no real OS or apps), not a hologram HUD (no scanlines), not a chart film (one number, not a chart).

## 2. Materials & rendering

- **Stage**: a near-black base with a radial lift at the upper centre, one large cool glow at single-digit opacity off-centre, a 50–55 % corner vignette. A hairline grid (white at ~3 %, every 4th line ~6 %) on a 48 px module. No grain.
- **UI kit, all original and drawn in code**: rounded windows (title bar with only a small glyph and title; never traffic-light buttons, menu bars or docks), notification cards, file icons with mono filenames, procedural thumbnails, list rows, tabs, badges, bars, uniform tiles.
- **Surfaces**: three steps of raised dark surface, 1 px border (~8 % white), 1 px inner top highlight, soft shadows.
- **Depth**: a 2.5D camera (`s = 1/(1/zoom − z)`); cards near the lens blur with magnification. Rotations use strip-rendered perspective (rotY ≤ ~24°).
- **Light** is the reveal tool: only pixels the light has passed turn on; unlit areas sit at a few percent.

## 3. Colour logic

- A cool neutral ladder only: near-black stage, three surface steps, text in three greys (primary, secondary, label). Neutrals are slightly blue, never warm brown.
- **One accent**, saturated and luminous, with its own glow. It is reserved for what the product *is* or *does*: the protagonist element, the call to action, confirmations, the key number. If two things are accent-coloured, one is wrong.
- **A problem colour** (typically a red for badges and warnings) may exist only while the problem exists; after the turn it never returns. Problem colour = noise, accent = the product.
- Secondary hues only as **category codes** in motion (a trail per data type), desaturated, and never on static UI.
- Example accents, pick one per film: lime `#B7F34A`, electric violet `#8B7CFF`, signal orange `#FF7A1A`.

## 4. Type & subtitles

- **OFL faces**: Inter (UI, captions, headlines; variable weight), Inter Tight 600 for giant numbers (tracking around −4.5 %), JetBrains Mono for labels, filenames and status text (wide tracking in small-caps labels).
- One line per screen for headlines. The big number gets its own screen and **no caption over it**: the number is the message.
- **Captions are a UI component**: a bottom-centre toast (dark translucent pill, 1 px light border, soft shadow, Inter 500 around 40 px, a small accent "speaking" dot). It enters with a small rise + fade in ~0.16 s and can turn more opaque over busy frames. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Typed text is its own subtitle**: text the cursor types in frame is not burned twice (it goes only into the .srt).
- Lift product content while captions are up so toasts never clip it.

## 5. Motion quality

- 24 fps on ones, no stepping, no boil: this is precision, not craft.
- **Everything lands on the grid and on the beat.** Moves start a beat early and land on it. Easing is fast-out with one small overshoot (`back`, s ≈ 1.3) and an immediate settle. No floaty sine drift.
- **Spawns are short and typed** (drop + bounce, fling, slide-in, pop; 0.2–0.3 s), one motion per element type. Tension can be a tremble of a few px.
- **Flights** follow curved paths with overshoot along the final tangent; same-type elements bend the same way and never cross.
- **A living element can act**: squash, stretch, anticipation (≥ 8 frames of wind-up), a 2-frame contact, spring follow-through. The blink of a cursor makes a natural metronome.
- **Disappearing is designed** (retract one part per beat, CRT-off squash into a point); nothing just fades.
- The stage and grid never move on their own; only the camera moves them.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Locked extreme close-up on a tiny UI element | Intimacy, one thing alive on a screen | a single action; a thought forming; a quiet status |
| Continuous pull-back, keyed per bar in log space | Accumulation, scale growing out of one point | spreading load; a network growing; a team joining |
| Push-in through a frozen frame | Time stopped, focus narrowing | a decision; the instant before a commit; a bug found |
| Whip pull-out in one beat | Cause and effect seen at once | a sync completing; a deploy landing everywhere |
| Dive into a small UI element (log-zoom) + match cut | Going inside the detail | a counter that matters; a log line; a setting |
| Half-second inserts expanding from their source | Overload, too much to read | notification storms; errors; choice overload |
| Near-locked frame while an object turns and light sweeps | Presentation, the product as hero | a reveal; a new version; a feature name |
| Slow lateral track across a UI plane | Order read by the eye | a timeline; a pipeline |
| Top-down plan over the grid | System view, structure | architecture; permissions; a workflow map |
| Return to an earlier framing | Rhyme: what changed | before/after; a loop closed; an echo |

Framing: generous negative space, one focal element, the accent at the focal point. Dutch angle and wobble only for disorder.

**Transitions = UI expand / collapse**: every shot change is an interface element expanding into the frame or the frame collapsing into an element. No fades, no blank frames. An expansion on a beat starts one frame early so the beat frame is already ~80 % open.

## 7. Sound palette

- **Tuned percussion and pads**: marimba, vibraphone (mallet or bowed), glockenspiel, celesta, a synth pad or drone, a low sine pulse, a shaker, plucked synth, felt piano. Clean, dry, minimal; samples e.g. VCSL (CC0).
- **Music as a visible process**: options include phasing (two voices on one pattern, one drifting), additive build (one note per bar), subtractive process (notes removed until one is left), dividing the beat to accelerate instead of changing tempo, or one chord that everything lands on. Picture events can spawn on score notes from a shared note table.
- **Two sound families = story**: disorder sounds *scattered* (detuned by tens of cents, random pans, a different timbre per source); the product's sounds are *one family* (felt ticks, glass taps, all in one mode, centred), so many landings form one in-key shimmer.
- **Foley materials**: cursor tick, low-profile keys, notification glass, file plop, window whoosh, glitch accents, stacking thumps, felt mallet + sine drop for a press, light-sweep shimmer, digit grains, CRT-off.
- **Ambience**: a quiet room, a computer fan, a high coil whine that can grow with pressure. Fan and whine live in the voice band: keep them down until a line ends.
- **Silence is a tool**: digital zero on every track when the screen pauses; near-silence (a −60 dB room) for a breath. The first sound after a silence is the most important one.
- **J / L cuts** carry sound across UI transitions (a chord ringing on, a shimmer arriving before the light).
- **Mix**: music ducks ~8 dB and foley ~4 dB under voice; −14 LUFS; no grain. **Voice**: confident and restrained, short declaratives.

## 8. Native moves

A menu: use the ones your story needs.


<!-- END STYLE PAGE -->
