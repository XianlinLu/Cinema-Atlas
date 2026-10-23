# Complete style specifications 11


<!-- STYLE: impasto -->

- **Value first.** Design each set as a flat, value-planned illustration (3 values minimum), then convert it to strokes. If the reference doesn't read at 480 px wide, no brushwork will save it.
- **Stroke sizes by importance and depth.** Coarse to fine: large planes in sky and walls, a few px only at edges and faces (per shape: `maxR`, `detail`, `dir`).
- **Strokes never cross shape groups**, so silhouettes stay crisp. Lost edges are opt-in (put two shapes in the same `group`).
- **Thin underpainting** (the reference itself, blurred ~1.5 px) under the strokes, so the canvas never peeks through as outlines.
- **Knife stroke**: longer than wide (≈ 1.7–3.1 × radius long, 0.95–1.45 × radius wide), slanted ends, small angle and value jitter (≈ ±13°, ±6 %). Solid objects that must read as silhouettes (figures, props) get little or no ragged run-out.
- **Light** rakes over a height field; wet or glossy surfaces get slightly more specular.
- **Reflections** (wet ground, glass, water) are **explicit stacks of short horizontal knife dabs** under each light source, broken and fading; never a painted rectangle.
- Render supersampled (2×). **No film grain**: grain plus compression eats the knife edges.

## 3. Colour logic

- Planes of mixed, slightly broken colour; each stroke may drag a second colour (`c2`) into the first. No gradients made by blending pixels: gradients are made by stroke-to-stroke steps.
- Warm light against cool shadow is the default temperature structure; the brightest, purest chroma is reserved for the story's subject (a prop, a crowd, a light source), not the background.
- **Colour can be an event.** Every stroke can hold a grey and a colour version; a monochrome world with one coloured exception, or a world re-laid from grey to colour, is native to the medium. The grey version is the luminance of the same strokes, slightly cool, with a small colour residue.
- Examples of palettes that fit: an after-rain sunset (cobalt → peach → gold sky, ochre facades, full-chroma props); a harvest field (straw yellow, burnt sienna earth, one viridian tractor); a night kitchen (umber shadows, sodium-lamp orange, one cold blue window). Choose from the topic.

## 4. Type & subtitles

- Titles are **laid in with the knife** (a stroke-by-stroke `appear` sweep of about a second) and can be taken off by the world (washed by rain, scraped, painted over). They move with the world.
- Small text (credits, data, captions) stays crisp DOM text over the painting: knife strokes can't carry small letters.
- A serif display face (e.g. Cormorant, OFL). Subtitles, if there is a voice: plain serif, ≤ 2 lines, in a calm plane; hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- Static paint is static. Only the things the story moves move (weather, figures, props, ribbons, light). Smooth 24 fps, no stepping: clarity is the brief.
- Moving figures are procedural strokes rebuilt each frame from **fixed seeds**, so their paint doesn't boil (walk cycles, IK arms, props that open and close).
- Actions sit on the music grid: a change of direction, a pop, a swell lands on a beat.
- Anticipation → action → follow-through on every gesture (lift before the strike, dip before the snap, swing after the stop).

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow truck + push on a wide | a world observed; patience | a place; a routine; a crowd |
| Push-in through a silence | inner pressure | a doubt; a decision; giving up |
| Tilt-up from the ground or a reflection | discovery from below | a small character entering; a first sight |
| Pull-back from a close-up | reaction; the world answering | consequence; a reveal of who is watching |
| Rotating crane-out, overhead | pattern emerging from many | choreography; traffic; a gathering |
| Same wide, repeated | before/after | change of colour, season or time |
| Locked frame, light moves | time and weather as the actor | a day passing; a storm arriving |
| Macro slide along the paint surface | the matter itself | a texture; a crafted object; a map |
| Whip-pan into a new painted plate | energy, a jump | a list; montage; travel |

Framing: keep the camera **inside the painted plate** (`half = W/2/zoom`), or the canvas shows. The subject gets the hard edges and the smallest strokes; everything else stays in big calm planes. Transitions: paint-over sweeps and scrapes, hard cuts on beats; no dissolves (two layers of knife ridges turn to mud).

## 7. Sound palette

- **Foley follows the paint and the world**: palette-knife scrapes on every repaint or paint-over, wet dabs, the materials of the scene (wet stone, nylon, wood, fabric, glass).
- **Beds** in layers (a hiss, near grains, one distinct detail), filtered when the camera goes under cover.
- **Acoustic instruments with a hand-made grain**: solo strings, accordion, pizzicato, harp arpeggios, glockenspiel or celesta for pops, piano, guitar, woodwinds; a solo instrument for a lonely world, an ensemble for a shared one.
- Options: **one action = one sound = one cut** (music-locked edit); pops pitched as a rising arpeggio so a sequence of events climbs; an unresolved phrase that the film resolves later; a hard silence that cuts music and beds to digital zero, containing at most one sound; a J-cut of the next scene's foley into a silence.
- Mix: music and ambience duck under any voice (~8 dB); −14 LUFS. Music and foley can carry a film without narration.

## 8. Native moves

A menu: use the ones your story needs.

- **Colour re-laid by the knife.** Every stroke keeps a grey and a colour version; a reveal wave re-paints them stroke by stroke (`reveal`, `revC`). *Fits content like:* a town waking up; a patient recovering; a brand relaunch; a season turning.
- **The one coloured thing.** The world drawn with `grey: 1`, one object with `grey: 0`. *Fits content like:* one person in a crowd; the fruit that ripened; a warning light.
- **Motion paints the picture.** Moving objects drip their colour as knife dabs; seen from above, their paths leave a painted pattern. *Fits content like:* a dance; delivery routes across a city; a football play; migration.
- **Raking light.** At the peak, drop the light to a grazing angle so every ridge catches it, then let it settle. *Fits content like:* a sunrise; a moment of recognition; unveiling a sculpture.
- **Paint-over transition.** The next shot's strokes are laid over the previous one in a sweep (`appear`), with a scrape on the soundtrack. *Fits content like:* a renovation; memory replacing the present; a timeline of versions.
- **Sound made visible.** A note or a voice becomes a paint ribbon that carries colour to what it touches. *Fits content like:* a song reaching listeners; a radio broadcast; a rumour spreading.

## 9. Pitfalls of the medium

- Confined strokes shrink near edges and leave canvas-coloured outlines → add the underpainting texture.
- Draw order in the reference matters: painting the ground after the buildings covers their feet.
- Plain rectangles read as posts or blocks → give silhouettes taper, a lit edge, and one or two defining dabs (shoulder, hair, handle).
- Proportions carry the object's identity at this stroke size: a prop drawn too wide reads as a different thing. Check silhouettes at thumbnail size.
- Film grain or heavy compression destroys the knife edges → no grain, supersample, high bitrate.
- Strokes that are re-seeded every frame boil → fixed seeds per stroke.
- Engine-level WebGL traps (reserved words, VAO binding) are listed in DEMO.md build notes.

## 10. Engine

Files: `demo/engine/impasto.js` (renderer), `demo/engine/plate.js` (reference → strokes).

Main calls: `new Impasto(canvas,{W,H,ss})`, `E.begin()` / `E.finish(post)` (raking light + grade), `E.batch()` → `E.draw(batch,o)` for static plates (`cam`, `grey`, `reveal`, `appear`), `E.drawNow()` for moving strokes, `E.under()` for the underpainting, `new Strokes().push({...})` (`KNIFE`, `BRUSH`, `DAB`, `LINE`), `new Ref()` + `paintRef()` (reference illustration → coarse-to-fine strokes confined to shape groups), `strokePath()`. Full parameter table: DEMO.md "Engine reference".

Minimal example: a warm-orange four-point sparkle with a short cursor tail, in knife paint.
```js
import { Impasto, Strokes, KNIFE, DAB, hex } from './engine/impasto.js';
const E = new Impasto(canvas), s = new Strokes(), c = hex('#D97757');
for (let k = 0; k < 4; k++) {                                   // four tapered knife points
  const a = k * Math.PI / 2;
  s.push({ x: 960 + Math.cos(a) * 60, y: 540 + Math.sin(a) * 60, ang: a, len: 120, wid: 46, c, c2: hex('#f0a07a'), type: KNIFE, taper: .95, seed: k });
}
s.push({ x: 960, y: 540, len: 40, wid: 40, c: hex('#f6c0a0'), type: DAB, seed: 9 });   // bright core
s.push({ x: 1060, y: 610, ang: .6, len: 90, wid: 16, c, type: KNIFE, alpha: .8, seed: 10 });   // cursor tail
E.begin(); E.drawNow(s.data(), { grey: 0, run: 0 }); E.finish();
```
"Only one colour" (monochrome with one exception): draw the world with `grey: 1, reveal: 1e6`, draw the exception with `grey: 0`.

## 11. Variation space

You decide the structure, the cast (or none), the sets, the opening, the ending, the camera path, the pacing, whether there is a voice, and where colour lives. All far from our demo:

- Structures: **one object, many hands** (a bowl or a boat passes through the people who make and use it, one painted plate per hand); **a still life comes alive** (a locked table whose objects move in turn, the light crossing it hour by hour); **a portrait in layers** (a face painted coarse to fine as a voice tells one life, each layer a decade).
- Openings: **the bare canvas** (underpainting only; the first knife stroke is the first event); **macro on a ridge of paint** that pulls back to become a mountain or a roof; **mid-action** (a figure already running across a finished plate).
- Endings: **scraped back** (the knife takes the painting off to the underpainting, leaving one mark); **the light goes out** (raking light sinks until only the ridges glow, then black); **the frame in a room** (the film was a painting hanging somewhere, seen by someone).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: one-line -->

# One-line Drawing — Style Prompt

> A single ink line that never leaves the paper. Everything on screen is that one line being drawn; scenes don't cut, they morph.
> References (grammar only): Osvaldo Cavandoli's *La Linea* (1971) — one line is both the world and the character, and transformations of the line are the jokes and the transitions; Gjon Mili's 1949 photographs of Picasso drawing with light — the confidence and speed of a single gesture; Norman McLaren's *Begone Dull Care* and *Boogie-Doodle* — lines drawn *to* the music. Do not copy La Linea's character, its gibberish voice, or any specific continuous-line illustration.

## 1. Essence, and what it is not

- **One continuous line** on warm white paper. The pen never lifts: in code the whole film can literally be one point array, from the first touch of the nib to the last frame.
- **Everything is a line**: characters, places, objects, even time. No fills, no shading, no second line weight, no background art.
- **We watch the line being drawn**: the camera follows the nib with a little lag and anticipation.
- Besides ink there is only the paper and a soft **shadow of the pen** (the real world above the paper). One accent colour at most, used once.

Not a whiteboard explainer (no hand, no marker, no erasing, no text-heavy boards), not ink wash (no tones, no brush bloom as a look), not a line-art animation with cuts and many strokes.

## 2. Materials & rendering

- **Paper**: warm white (around `#F4EFE4`), procedural mottling (soft-light, large tile), long fibres that fade out when zoomed out (or they shimmer), a sparse paper-tooth speckle over the ink at close zoom, light vignette. All textures anchored to the paper; they move with the camera.
- **Ink** is a filled polygon around the path (not `ctx.stroke`), mixed with paper colour to an opaque tone per point.
  - Width = base width of the current "voice" of the line × pen pressure × fine noise (±8 %); pressure from speed: `0.66 + 0.8·exp(−v/300)` (fast = thin, slow = fat).
  - The line's character can change along the path (base width, alpha, tremble, dryness); blend over a short stretch at boundaries.
  - Ink bleed: the same polygon slightly wider, blurred on an offscreen layer, composited at ~20 %.
  - Pooling: extra round dots where speed drops low.
  - Tremble (perpendicular noise) and dry-brush gaps (long-scale noise + thin bristle strands) for age, fear or fatigue.
  - A stop leaves a teardrop-shaped blot: tip at the nib, belly sagging downward as it spreads, a dark tide line at the rim.
  - **A screen-space minimum width**: widths scale with zoom like a line under a macro lens, but clamp the zoom used for width during pull-backs so a wide view keeps its weight.
- **The pen is never drawn**: a soft blurred wedge of shadow from the nib and a tiny contact dot. Hands, if any, appear only as shadows, each hand composited as one flat layer.
- **Path design**: chapters written as SVG path strings, sampled by arc length, joined by tangent-continuous connectors; time assigned per point weighted by curvature.

## 3. Colour logic

- **Ink on paper.** A warm black (around `#1D1A17`) on warm white; nothing else fills the frame.
- **One accent at most, used once**, on a stretch of the line that means something; it returns to ink afterwards and stays visible in the final picture if the picture is revealed.
- Examples of an accent's job: red for love or danger; blue for water or cold; gold for money or a prize. Never a second accent.

## 4. Type & subtitles

- **Text is written, like the line**: a handwriting face (e.g. Caveat) for subtitles, ink at ~84 %, no box, centred near the bottom, **written on** left to right (~0.2 s + ~17 ms per character) behind a soft paper-coloured halo so passing lines never cross the letters; fade out ~0.45 s. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles in a monoline connected script (e.g. Sacramento: itself a one-line drawing), written on in empty paper away from the drawing, gone before the camera moves into them.

## 5. Motion quality

- **Everything on ones** (24 fps): the appeal is the continuous act of drawing; stepping breaks it.
- **Timing = chapter windows + curvature**: within a window, time per point is weighted by `1 + K·turn` (sharp turns get more time, smoothed so speed never jumps). Pin musical beats with marks: by arc-length fraction or by position ("the second time the pen passes here"). A stop is two marks at the same place.
- Corners (speed minima at high turn) can be exported to the soundtrack as candidate note onsets.
- Speeds: ~300–700 units/s for travelling lines, ~50–150 for small details. The most important stroke is usually the slowest.
- **Retracing** over an existing line is legal and invisible (it only thickens slightly).

## 6. Camera grammar

A vocabulary, not a route. The camera is one continuous move: composition centre, zoom, a few degrees of roll, and a follow weight (0 = composed, 1 = locked to the nib); the follow point averages the nib over roughly −0.55…+0.4 s (lag and anticipation), with a soft clamp keeping the nib inside the central ~70 % of the frame. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow the nib (high follow weight) | travel; momentum; a thread of time | a journey; a process; a timeline |
| Composed frame, low follow weight | a scene that must read as a whole | a vignette; a joke; a diagram |
| Macro on the nib | intimacy; the act of making | a first touch; a signature; a detail |
| Hold with a slow push-in | weight; a stop | a loss; a doubt; a decision |
| Mirrored framing | rhyme across time | parent and child; before/after |
| Continuous pull-back | everything was one picture | a reveal; a map; a word |
| Lateral scroll with the line running ahead | a horizon; a graph; a race | a stock chart; a heartbeat; a road |
| Roll with the line | vertigo; play | a loop-the-loop; a fall; a dance |

No cuts. Transitions are morphs: the last stroke of one image is the first stroke of the next.

## 7. Sound palette

- **Music: one solo instrument, one unbroken melodic line**, the sound equivalent of the drawing: a bowed or plucked string (cello, violin, viola, harp), a solo woodwind (clarinet, flute, bassoon), a hummed voice, a single guitar. A second colour only as a rare accent (a chime, a pizzicato stretch). No pads.
- **Write the score to the drawing**: key notes on marks and corners; fast line = short notes; a stopped line = one long note fading into silence; the highest note on the most important touch.
- **The pen on paper is the most important sound**, synthesised from the pen speed: band-passed noise (brighter when fast, duller when slow), random paper-fibre ticks with density ∝ speed, amplitude ∝ √speed, panned with the nib's screen position; broken up by dry gaps; lighter and jerkier for a young hand. Plus: a wooden tap on the first touch, a faint wet swell for a blot, a tiny rub for a handoff, a page lift.
- **Silence is literal**: zero the music bus including reverb tails; drop room tone.
- **Mix**: music ducks ~5 dB and the pen ~4 dB under voice; −14 LUFS; grain 0 (the paper is in the render).
- **Voice**: warm, few short lines that leave space for the line; place key words on picture beats with whisper word timestamps.

## 8. Native moves

A menu: use the ones your story needs.

- **The pen never lifts.** Anything that is one continuous thing. *Fits content like:* a river from source to sea; a relay race; a production line.
- **The line is time.** The stroke's character changes with age, mood or strain. *Fits content like:* a building aging; a runner tiring; a machine wearing out.
- **Transformation.** One image morphs into the next. *Fits content like:* a seed becoming a tree becoming a table; a sketch becoming a product; a word becoming its object.
- **Stopping is an event.** The nib stops, ink pools, music cuts to silence (1.5–3 s). *Fits content like:* a power cut; a pause for a minute's silence; a hesitation before a signature.
- **Reverse-designed scale reveal.** Every vignette is secretly part of one big picture seen at the end. *Fits content like:* a city's landmarks forming its skyline; a company's milestones forming its logo; a recipe's steps forming the dish.
- **Handoff.** The pen passes to another hand (as a shadow) and a new line begins. *Fits content like:* a teacher and a student; a founder and a successor; one generation to the next.
- **Line as graph.** The line becomes a chart while staying a drawing. *Fits content like:* a heartbeat; a temperature record; a football match's momentum.

## 9. Pitfalls of the medium

- **Stray connectors ruin a reveal**: every extra line reads as a wrinkle, beard or mask. Fix the topology (where each chapter enters and leaves), not the drawing. Plan it like an Euler path: a closed motif is a circuit (you leave where you came in); retrace or reorder chapters.
- Each region of a final picture is drawn exactly once; connectors must fall on natural lines of that picture.
- **Test the reveal early and often**: render the whole path at once at final scale after every change.
- Lines drawn too close braid together once width is applied; keep a gap.
- A round blot reads as a mole → a sagging teardrop.
- Thin lines at wide zoom → clamp the width zoom.
- Translucent hand shadows double-darken where they overlap → one layer per hand.
- Titles collide with the drawing as the camera moves → check every frame of the title's window.
- Whisper mishears short lines → rephrase rather than fight it.

## 10. Engine

In `demo/`: `geom.js` (samples SVG paths by arc length in the browser, adds tangent-continuous connectors, assigns time by curvature, marks and holds), `ink.js` (the line renderer: pressure, bleed, pooling, tremble, dry brush, accent stretch, blot, minimum screen width), `paper.js` (paper, fibres, tooth, vignette), `cam.js` (composition keys + nib follow + soft clamp), `hands.js` (pen and hand shadows), `subs.js` (written-on subtitles and titles). The drawing itself lives in one file of SVG path strings and a chapter table (`face.js`); replace it with your own path. Debug views (`?all=1`, `?cams=`) render the whole path or many camera views in one session: see [DEMO.md](DEMO.md) "Build notes".

## 11. Variation space

You decide what the line draws, whether it reveals one final picture, where it stops, the accent (or none), the opening and the ending. All far from our demo:

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


<!-- END STYLE PAGE -->
