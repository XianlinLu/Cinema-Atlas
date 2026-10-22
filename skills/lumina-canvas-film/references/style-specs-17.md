# Complete style specifications 17


<!-- STYLE: one-line -->

- Structures: **a line that is a graph** (a data series drawn as a horizon; each peak and trough becomes a scene); **two lines** that start in opposite corners and are drawn in alternation until they meet; **a loop** (the line draws a scene and then retraces its way back to the start, which now means something else).
- Openings: **mid-line at speed**, the pen already running across the paper; **a finished drawing** whose line then unravels into the story; **a word written in script** whose last letter becomes the first scene.
- Endings: **the line runs off the edge** of the paper and keeps going; **the ink runs out** and the last stroke fades into dry scratches; **the pen stops in mid-air** over the paper before the last stroke.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: whiteboard -->

# Whiteboard Explainer — Style Prompt

> An explainer drawn live on one glossy dry-erase board: single-line handwriting that is actually *written* stroke by stroke, floating markers with no hand, magnets that can move, an eraser that can rewind, and a camera that travels across the board instead of cutting.
> References (grammar only): RSA Animate / Cognitive Media (one continuous board, the camera travels instead of cutting, a full-board view); minutephysics (one sentence = one drawing, the simplest geometry that carries the idea); Steve Reich's *Piano Phase* (two copies of one figure at two tempi as a structure). Never copy their drawings, characters, hands or music.

Suits explainers, usually science or "how does X work"; the length follows how many ideas the board has to hold.

## 1. Essence, and what it is not

- **One physical whiteboard.** Everything the viewer learns is drawn in dry-erase marker in front of them, in real handwriting order.
- **The board is a map**: each idea lives in its own region; the camera travels between regions, often led by the pen. Distance on the board = distance in the argument.
- **Real marker, not animated text**: ink pools where the nib lands, dry streaks and speckle, strokes overshoot and don't quite close, ghosts of old lessons remain, a glossy sheen drifts slower than the board, and **every stroke makes a sound**.
- **No hands.** Markers float with a real cast shadow that grows when they lift, park outside the frame between phrases and fly back in. Magnets and the eraser move on their own. Never draw a hand, an arm or a cursor.

Not Blueprint (no blue sheet, no drafting conventions), not Crayon Picture Book (no wax texture, no children's story), not a kinetic-type explainer (text is handwritten stroke by stroke, never animated as blocks).

## 2. Materials & rendering

- **Board**: a warm white gradient, a faint scuff and micro-scratch tile, a few dozen **ghost marks** (old words, circles, arrows) at 5–10 % in grey or pale blue, and a soft diagonal **window sheen** (white, 10–16 %) moving at ~0.35× the camera: this one detail sells "glossy".
- **Ink**: alpha ~0.94, composited with **multiply** so overlaps darken like real marker. Width 6–11 px for drawing, ~13 % of cap height for lettering.
- **Stroke character**: resampled every ~0.6 × width; low-frequency hand wobble along the normal (a few px, long wavelength) plus a finer tremor; chisel-tip width modulated by direction; a pressure ramp at the start and a small taper at the end; circles start at an angle and **overlap past closure**; rectangles are four strokes with small corner overshoot; a darker pooled dot *inside* the start of long strokes.
- **Dry-marker texture**: a speckle-and-streak tile subtracted from the ink layer (destination-out), locked to board space, faded out when the camera is wide.
- **Lettering**: a single-line (single-stroke) font written in stroke order, each glyph with small rotation, baseline and scale jitter. Missing symbols (μ ≈ → × − ✓ ² ° ±) are hand-defined.
- **Props**: dry-erase markers (white barrel, colour band and cap in the ink colour, felt nib), a felt eraser, magnets (glossy, with specular highlight and soft cast shadow). Frame, tray and wall appear only if the camera ever goes past the board edge.

## 3. Colour logic

- **Three marker colours at most**, each with a meaning held for the whole film: one dark ink for things and structure, one for signals / measurement / process, one accent for the thing that matters (one accent per region).
- **Monochrome variant**: everything in the dark ink, one element in the accent (the "only colour").
- Ghost marks and board stay neutral; the accent never appears on props except its own marker cap and the hero magnet.
- Example sets: black `#23262c` / blue `#2a5cb3` / orange `#d97757`; black / green `#2e8b57` / red `#c8363a`; navy `#1f2a44` / teal `#1f8a8a` / purple `#7a4fb3`.

## 4. Type & subtitles

- **Handwriting only**: a single-line hand (e.g. EMS Tech, OFL) for all board text; titles large (~120–200 px cap height), labels 30–70 px.
- **Title and end card are written on the board** in the same hand.
- **Burned subtitles**: an off-white rounded label (~90 %), a handwriting-like face (e.g. Architects Daughter ~44 px), dark text, a short accent-colour marker dash. Split at clauses, ≤ 44 characters per line, bottom ~12 % of the frame kept free for them in every shot. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Writing finishes on the word**: a term appears exactly when the narrator says it.
- A label is fully in or fully out of every shot it appears in.

## 5. Motion quality

- **Hand speed**: every stroke follows a slow-fast-slow curve (`u − sin(2πu)/2π × 0.8`). Strokes are scheduled into a **time window** and the engine solves the speed, so writing always finishes on time.
- **Pen hops** between strokes lift in proportion to distance (shadow slides and blurs); long gaps send the pen off-frame to park and back shortly before its next stroke.
- **Magnet**: drop with a shrinking shadow; slide with a small lift; lift-off and sink possible.
- **Eraser**: constant speed along a path, a wide band at ~90 % strength (a ghost always remains).
- **Speed**: faster than real hands (a sped-up lesson) but never so fast the stroke order is lost: a label ~0.3–0.8 s, a title ~3 s.
- Camera on ones with real motion blur when it moves fast.

## 6. Camera grammar

A 2D camera over a large board (e.g. 8000 × 4500): position, zoom interpolated in 1/z so pushes feel like dollies, a little roll. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Pull back from a tiny drawing | scale | a surprising size; context |
| Ride the line the pen is drawing | one idea leads to the next | a transition; a process; a path |
| Hold still | read now | an equation; a definition; a list |
| Whip to a new region | a new idea after a pause | a twist; a "but" |
| Return to an earlier region | a callback, for free | reusing a result; a comparison |
| Split view of two regions (zoomed out enough for both) | two things at once | a duet; before/after |
| Slow push into one symbol | this term is the point | a unit; a variable; a name |
| Track along a long diagram | sequence, time | a timeline; a pipeline; a journey |
| Pull back past the board edge to the wall | the whole lesson as one picture | a summary; a scale jump |

Motion blur: when the camera moves more than ~14 px per frame, render and average sub-frames (≤ 4 px apart). No cuts on the board; if a cut is needed, it is a whip.

## 7. Sound palette

- **Every stroke sounds**: band-passed felt-on-gloss noise (a hiss band ~2–7.5 kHz + body ~0.5–1.5 kHz) enveloped by the stroke's own speed curve, a tiny nib tick at the start, stick-slip grains, and on some long strokes the **dry-erase squeak** (a 1.5–2.6 kHz sine with 7–13 Hz vibrato). Each colour sounds slightly different. Pan = the stroke's screen x; closer camera = louder.
- **Props**: magnet on steel = click + metal modes + a low board thump; eraser = felt rub modulated by its zig-zag; cap off/on; marker tray bounce.
- **Room**: low room tone; a single diegetic ticker (a wall clock, a fridge hum, a projector fan) can own a silence.
- **Music** options: a solo piano figure; a small jazz trio with brushes; plucked strings and kalimba; a synth arpeggio for tech topics; clockwork minimalism (marimba, pizzicato, woodblock, glockenspiel). Mickey-mouse details: a rising whistle for growth, pings for signals, a harp run for a fall.
- **Techniques to pick from**: adding one instrument per step of a mechanism; a key change when the frame of reference changes; a full stop into silence before a surprise; the previous cue reversed and squeezed for a rewind; two copies of one figure at two tempi (phasing) for anything that diverges, snapping into unison when resolved.
- **Mix**: voice on top (compressed, light room), music well under voice and ducked further under speech, foley ~11 dB under voice; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Writing in stroke order.** The reveal is the explanation: a formula term by term as it is spoken. *Fits content like:* compound interest; the Drake equation; a recipe's ratios.
- **The pen leads the camera.** Transitions are drawn lines the camera rides. *Fits content like:* a nerve signal; a supply chain; the water cycle.
- **Magnets.** The only things allowed to move on a board: give the hero to a magnet; slide, lift, drop, sink it. *Fits content like:* a delivery truck on a route; a cell in a bloodstream; a player on a pitch.
- **The eraser rewinds.** Wiping a trail backwards reads as undoing time. *Fits content like:* an undo in software; reversing a chemical reaction; "what if we hadn't…".
- **Two pens at once.** A live duet comparing two quantities. *Fits content like:* two savings plans; two runners; a population vs its food supply.
- **Ghosts of the old lesson.** A faint previous drawing becomes relevant. *Fits content like:* a theory replaced; last year's forecast; a first draft.
- **The full-board view.** Every region seen at once as one picture. *Fits content like:* a system diagram; a history; a map of a field.

## 9. Pitfalls of the medium

- **One pen, too many jobs** drifts later and later → give each drawing a deadline window and let overlapping jobs go to another pen.
- **Minimum stroke duration × many dashes** makes a dashed line take seconds → dashes need their own floor.
- **A pooled-ink dot bigger than the stroke start** leaves halos on every letter → keep it inside.
- **Punctuation vanishes** (a font period is a 1 px stroke) → render sub-width strokes as dots.
- **Labels half-cut by a push-in** look sloppy.
- **Motion blur with few sub-frames** strobes text.
- **Eraser paths** crossing labels you want to keep.
- **Voice and phoneme set mismatch** (a British voice with US phonemes) mispronounces → match the language code to the voice; ASR-check.

## 10. Engine

`demo/engine/wb.js`: hand-drawn shapes (`line`, `curve`, `poly`, `arc`, `circle`, `rect`, `arrow`, `dashed`, `hatch`), `text()` in writing order from a single-line font (`loadFont`), `Stroke`, floating `Pen`s, `Timeline.draw(pen, shapes, t, {by})` (solves hand speed to a deadline), `Timeline.erase`, `Timeline.cue`, keyed `Camera`, `Board` (ink multiply, dry texture, erasers, sheen, props), prop drawers. API table and a minimal example that draws something new: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the topic's object, the board layout, the colours within the logic, the voice, the music family, the camera route, the opening, the ending and the length.

All far from our demo:

- Structures: **a proof** (one claim at the top, the board fills downward step by step, each step boxed when proven); **a debate** (two pens, two halves of the board, each drawing its side until the drawings meet in the middle); **a timeline** (one long horizontal line ridden left to right, with events hanging off it).
- Openings: **a question mark** drawn huge in the centre, then shrunk to become a dot in the first diagram; **an erased board** where the ghost of a wrong answer is still visible; **a magnet dropping** onto an empty board with a clack.
- Endings: **the answer circled** twice and the pen capped; **the board wiped** except for one line that survives; **a push into the smallest symbol** on the board, which becomes the title.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: urban-sketch -->

# Urban Sketch · Pen & Wash — Style Prompt

> A sketchbook page drawn on location: fine sepia fineliner lines that wobble, overshoot and never quite close, with loose transparent watercolour dropped on top. The colour sits slightly off the lines, spills over them, and dissolves into cream cold-press paper at the page edge.
> References (grammar only):
> - Urban-sketching sketchbook pages: line first, then wash; colour off-register; handwritten date and place in the corner; the page edge breaking up into dabs.
> - *Paperman* (2012): a monochrome world with one coloured object.
> - *The Red Balloon* (1956): an object as the protagonist, the camera following it across a city.
> - Jazz waltz (the Vince Guaraldi school): 3/4 swing, walking bass, brushes, a woodwind lead.
>
> Nothing is copied from these: no characters, melodies, layouts or type.

## 1. Essence, and what it is not

Reportage drawing, made on location in a few minutes. Two layers that stay visibly separate:

1. **Ink.** One thin, near-constant line (a 0.3–0.5 mm fineliner) in dark sepia. It wobbles slightly, overshoots corners by a few pixels, breaks mid-stroke, and suggests rather than describes: a few window marks instead of a grid, scalloped fragments instead of a whole tree outline.
2. **Wash.** Transparent watercolour glazed on top, **misregistered** by 1–3 px from the line, sometimes spilling past it, leaving paper white for highlights and figures (reserves). Dried edges are darker (pigment pools at the rim), and pigment granulates into the paper tooth.

**The page is part of the image**: warm cream cold-press paper with large-scale mottling and fine tooth. Nothing is painted edge to edge; the painting frays into leaf-sized dabs and white holes, leaving margins for handwriting.

Not Watercolor Brush (no line-free wet-in-wet painting, no painterly edges without ink), not Whiteboard (no marker, no explainer diagrams), not Chinese Ink Wash (no brush calligraphy, no monochrome ink tones). Line and wash, both, always.

## 2. Materials & rendering

- **Paper**: two octaves of fbm mottling (a few %), a tooth tile multiplied over everything, figures included.
- **Ink**: ~96 % coverage; world line width thinner far, thicker near (e.g. 1.3–3.4 px); wobble ~1 px; overshoot 3–8 px; a third to half of long strokes get one small gap. Strokes are baked with their **draw time per pixel**, so the shader plays back stroke order.
- **Wash**: 2–3 rough-edged layers, multiply, alpha ~0.4–0.65, offset from the line by about one line width, a dried edge at 30–40 %; granulation = pigment × (0.82 + 0.36 · fbm).
- **Colour arrival field**: every pixel has a time at which colour reaches it. The wash is revealed through it with a ragged wet front (darkened band just behind the front) and noisy edges. Figures bloom from a point with a noisy circular clip.
- **Foliage**: pale base wash, then light and shadow masses, then small leaf dabs coloured by light direction, holes at the rim, scalloped ink only on the outline.
- **Sky**: a few big soft washes at low alpha, fading upward; clouds are reserves with a tinted belly.
- **Buildings**: local colour; shadow side mixed ~45 % with a cool violet-grey; distant blocks mixed ~50 % with a haze colour.
- **Figures**: a 3D skeleton in orthographic projection; torso from cross-sections; limbs as organic tapered tubes; hair and head as one mass; face left blank (one nose tick in profile); shadow side mixed with violet.
- **Page edge**: a noisy boundary, a white-dab band inside, a coloured-dab spray outside.
- Deterministic: same seed, same marks.

## 3. Colour logic

- **Ink is one colour** (dark sepia or warm black); it never changes.
- **Wash is local colour, lightly**: few pigments, mixed on the page; shadows are the local colour mixed toward one shared cool violet; distance mixes toward one haze.
- **Paper white is the brightest value**; it is reserved, never painted.
- **Colour can be withheld**: a page may be ink-only with colour as an event (one tinted object, colour arriving with a cause).
- Example palettes: park in summer (lawn `#c3c96f`, leaves `#7fa04a`, sky `#9fbcd6`, limestone `#d8c6a0`); harbour morning (sea `#7fa6b8`, hulls `#c9573f`, rope `#c8a86b`, sky `#bcd0dc`); winter market (roofs `#8b93a6`, lights `#e2b04a`, awnings `#b8483e`, snow = paper).

## 4. Type & subtitles

- **All text is handwriting on the page**, written on left to right with pen sound, and moves with the camera: a corner note (e.g. Reenie Beanie: day, time, weather, place), titles and colophon in a casual hand (e.g. Caveat 500–600), left-aligned in the blank margin.
- **Subtitles**, if there is a voice: handwritten lines in the page margin or a caption strip written into the lower margin, never a generic overlay box. Hold ≥ max(1.8 s, speech + 0.6 s).
- The style works well without any voice.

## 5. Motion quality

- **Figures boil at 12 fps** (line wobble and wash seeds change every 1/12 s). The static page does not boil (it is a real page); the camera moves every frame, smoothly.
- **Performance**: anticipation, action, follow-through; footsteps on the beat.
- **Invisible forces are drawn**: wind as ink curls that draw on and erase from the tail, trailing dabs; sound as ink lines; heat as wavy strokes.
- **Colour never snaps**: it blooms from a point or arrives through the field.
- Stroke-order draw-on for anything that "appears".

## 6. Camera grammar

A 2D camera over a large page (e.g. 5120 × 2880). Designed moves use cubic easing; follow shots use a critically damped spring on a lead-ahead target, so the camera lags like a hand-held follow. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Push-in | attention; a detail observed | a face; a sign; a small event |
| Lateral follow on a spring | travel, pursuit | an object carried; a walker; a vehicle |
| Crane up | a new level, a view opening | a skyline; a tree; a balcony |
| Whip-tilt with slight roll | sudden change of direction | a fall; a gust; a surprise |
| Punch-in with a short shake | impact | a catch; a collision; a door slam |
| Pull back to the whole page | scale; the sketch as an object | a summary; a place in full |
| Tilt into the margin | from picture to words | notes; a date; a title |
| Slow pan across a line-only area | the world before colour | a quiet start; memory |
| Hold while the pen draws | the act of noticing | a subject being drawn |
| Page turn to a new spread | another time or place | a travel diary; a sequence of days |

Framing: subjects ≥ ⅓ of frame height at story beats; a small key object gets a faint paper halo (reserve) so it reads over busy foliage. Transitions: camera travel on the page, page turns, or colour arriving; no dissolves.

## 7. Sound palette


<!-- END STYLE PAGE -->
