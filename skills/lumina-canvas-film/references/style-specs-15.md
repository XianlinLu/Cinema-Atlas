# Complete style specifications 15


<!-- STYLE: watercolor -->

Framing: generous paper margins; one hero subject per view with its note; labels never cover the subject. Transitions: brush-edge wipes, mist, a page turn, or a continuous camera move; no hard video cuts, no dissolves between unrelated pictures.

## 7. Sound palette

- **Music**: acoustic and gentle: felt piano, fingerpicked guitar, woodwinds, light strings, glockenspiel, kalimba, soft pads. A licensed track can be edited with beat-aligned jumps; the picture can then take its beat grid.
- **Foley made from the scene's matter**: a paper brush rustle for each painting-in (band-passed noise, light tremolo, a panned sweep); pencil scratch for notes; a soft thump for a stamp; page flips; nature beds and creatures of the subject (birds, wind, rain plinks, water, insects, fire crackle).
- **Silence**: the brush lifted: music out, only paper and room; it frames a single painted moment.
- **Mix character**: voice forward (RMS a few dB over the music), music ducked ~4 dB under voice with a smoothed envelope, a short soft reverb, final −14 LUFS. Kokoro voices are peaky (~17 dB peak-to-RMS): limit before level-matching.
- **Voice**: warm, unhurried documentary read, one line per idea.

## 8. Native moves

A menu: use the ones your story needs.

- **Painting-in as reveal.** A new thing appears stroke by stroke as it enters. *Fits content like:* the stages of a building; the ingredients of a dish; the organs of a body.
- **Burst.** A whole group paints in at once (≤ 1 s) for a peak. *Fits content like:* a festival crowd; a field in bloom; a city lighting up.
- **Palette as data.** Sky, ground and background blend by a measured value. *Fits content like:* pollution along a river; temperature by altitude; noise across a city.
- **Specimen + note.** One hero object with a hand-written label and leader line. *Fits content like:* a tool kit; a wine region's grapes; parts of a bicycle.
- **Mist erase.** The world washes back to paper. *Fits content like:* forgetting; a dream ending; a site demolished.
- **Map in time.** A painted map whose fills change continuously through years. *Fits content like:* a language spreading; a coastline eroding; a railway network growing.
- **Painted transformation.** Objects cross-fade to a burnt, wet or aged sprite and regrow. *Fits content like:* a wildfire and recovery; a flood; a restoration.

## 9. Pitfalls of the medium

- Offscreen wash strips too short flatten tall shapes into flat tops and expose seams on tilts → size strips well beyond the frame.
- A translucent wash that ends at its canvas edge shows a hard seam under other layers → extend below the frame and fade to paper with a gradient.
- Classic scripts share one global scope: touching a `const` before its declaration in async init leaves `READY` false and every screenshot times out → build everything inside the init; read `[pageerror]` lines.
- The stroke builder consumes the global RNG: any stroke created in `render(t)` must be wrapped in `withSeed` or parallel workers disagree.
- Thousands of strokes per frame are too slow → sprite cache.
- Beat-locked animation must be re-derived when the music edit changes.
- New CJK subtitle characters fall back to another font until the subset is rebuilt.

## 10. Engine

In `demo/`: `engine.js` (RNG, easing, noise, monotone keyframe tracks; the stroke engine `mk`, `drawS`, `drawList`, `sprite`, `clump`, `edgeOf`, `withSeed`), `plants.js` (plant and prop generators, local coordinates, root at 0,0), `scene.js` (layers, wash strips `washPoly`, world placement `add`, annotations `hand` / `leader` / `note`), `main.js` (map, mist, HUD, subtitles, `render(t)`, async init → `READY`), `paper.py`, `fetch_fonts.mjs`, `mix.py`, `render.mjs`. API table and a minimal example: [DEMO.md](DEMO.md) "Engine reference".

## 11. Variation space

You decide the subject, the structure, what gets painted, the palette logic, whether anything is measured, the opening, the ending and the camera. All far from our demo:

- Structures: **a journal kept over one year** (locked page per month, each painted over the last); **anatomy of one object** (a single specimen dissected into labelled parts, each part a painted close-up); **a recipe or process** (steps painted top to bottom on one tall sheet, tilting down).
- Openings: **a finished painting** that we then watch being painted backwards to its first stroke, and forwards again; **a close-up of wet pigment** spreading, pulled back to show what it became; **a hand-written question** on blank paper, answered by painting.
- Endings: **the page left unfinished**, brush lifted mid-stroke; **a close-up of one detail** as the rest fades to paper; **the sheet dries and is filed** into a stack of other pages.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: ink-wash -->

# Chinese Ink Wash — Style Prompt

> Xieyi ink painting on rice paper, animated: blank paper is space, one brushstroke is a mountain, a wave, a gesture or a cut.
> References (grammar only): Shanghai Animation Film Studio's *Feelings of Mountains and Water* (1988) (blank-paper space, ink bloom, guqin pacing, figures in a few strokes); the bamboo-forest fight of *Crouching Tiger, Hidden Dragon* (weightlessness, stillness before action). Copy none of their characters, compositions or music.

## 1. Essence, and what it is not

An ink painting (水墨) painted and unrolled before you: black ink on warm rice paper in five tones, plus **one** red, the vermilion seal. No Western outlines: forms are made by **loaded brushstrokes** whose dark edge *is* the contour (没骨, "boneless" painting), by **wet washes** that bleed into the paper, and by **dry, fast strokes** where the paper shows through the bristle tracks (飞白, "flying white").

Most of the frame is **empty paper** (留白): water, sky, mist, silence. Things are *painted into existence*, not cut to.

Not watercolour (no colour washes), not vector art with a brush texture (no flat fills or closed outlines), not a calligraphy title sequence.

## 2. Materials & rendering

- **Paper** is procedural, in the compositor, never a texture file: warm rice paper (around `#F2ECDE`), cloud mottling, long fibres, pulp flecks, grain that fades when zoomed out (or it shimmers), a light vignette; anchored to the world.
- **Ink** is stroke opacity multiplied onto paper (never an overlay), in five tones (墨分五色):

| Tone | Opacity | Use |
|---|---|---|
| 焦 jiao (burnt) | ~.96 | calligraphy, the sharpest lines, moss dots |
| 浓 nong (thick) | ~.82 | contours, dark edge of loaded strokes |
| 重 zhong (heavy) | ~.60 | secondary lines, folds |
| 淡 dan (light) | ~.34 | mountain bodies, robe and body washes |
| 清 qing (clear) | ~.16 | far mountains, faces, mist |

- **Brushstroke model**: centreline × pressure profile × width noise, plus 4–60 **bristles** whose ink load drops along the stroke and breaks on long-scale noise. `dry` runs from a solid wet stroke to flying white (dry strokes are bristle tracks only).
- **Loaded stroke**: bristles darker on one side, so the stroke carries its own contour: this makes bodies, rocks and waves read as ink, not vectors.
- **Two layers**: the wet one bleeds in the compositor (noisy blur, **edge pigment accumulation**, granulation); the dry one only gets fibre jitter and paper tooth.
- **Masses**: soft polygons, jittered edges, a gradient; never flat fills.
- **Landscape**: mountains dissolve downward into mist bands, with 披麻皴 texture and 苔点 moss dots on near ranges only; rocks are outline → axe-cut texture → shadow wash → dots.
- **Water is blank paper**, moved by faint dry streaks and open ink rings. Solid water: Song-dynasty **parallel wave lines** (dense near the edge) or a pale body with a few huge loaded strokes along its face.
- **Figures are xieyi**: one pale body mass plus two loaded strokes, burnt-ink lines for limbs; features, if ever shown, in 3–5 strokes.
- **Calligraphy**: an OFL brush font is only a **skeleton**: trace centrelines in stroke order, pressure from glyph thickness, hidden-tip entry (藏锋), tapered exits.

## 3. Colour logic

- Ink only, from cool grey at low density to warm black at full density. No other hue in the world.
- **One vermilion** (around `#B02E22`), for the seal and at most one tiny accent in the story (an object the protagonist carries). The accent finds the protagonist in wide shots and can rhyme with the seal. Never a red wash, never red type.
- Values carry depth: far = pale and soft, near = dark and textured. If a frame gets busy, remove ink rather than add tone.

## 4. Type & subtitles

- Subtitles are **inscriptions (题跋)**: a classical italic serif (Cormorant Garamond italic), ink-coloured, no box, ≤ 2 lines, placed in each shot's empty paper. A small vermilion square marks the start of each line. They appear wet and dry in a fraction of a second. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles are written on the painting itself, in vertical columns in its empty space, with a vermilion 白文 seal drawn by code (lines knocked out of a slightly irregular red square, with ink-paste speckles). They move with the world.
- Screen-space overlays reset the camera transform.

## 5. Motion quality

- **Figures step at 12 fps** (on twos); their position, the camera, blooms, ripples and splatter move on ones at 24 fps.
- **Stable strokes on twos**: seed every stroke by its index and compute bristle breaks along *normalized* arc length × a fixed reference length, so flying-white gaps don't crawl every drawing. Allow only a small "boil" on the width noise.
- **Painted into existence**: strokes appear in drawing order.
- **Stillness before action** (when a decisive stroke is the event): hold, with at most a slow push-in, then let the stroke cross the frame in a few frames. Consequences start only after the stroke has finished.
- Nothing is tweened like a vector shape: things are painted, bloom or dissolve into mist.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Locked frame on the paper | The page is the stage; things are painted in | a thing forming; a line being read; a still decision |
| Right-to-left pan (handscroll) | Time and distance as one painting | a journey; a history; a process |
| Vertical tilt (hanging scroll) | Height, stages stacked | seasons; a climb; generations |
| Lateral tracking, lead room, slow far parallax | Motion through a world | travel; a chase; a commute |
| High wide, a tiny figure in blank paper | Smallness, solitude | loneliness; nature's scale; one life among many |
| Low angle, dark mass towering, slow push-in with shake | Weight, threat | an obstacle; a storm; pressure |
| Hard cut to an extreme close-up | A break in the flow (the style's only hard cuts) | a decision; a shock; a memory |
| Push into an ink bloom or mist | Passing between states | memory; dream; a season turning |
| Pull back until a mark joins the whole | The part was inside something larger | a summing-up; irony of scale |
| Return to an earlier framing | The rhyme shows what changed | aftermath; growth; before/after |

Framing: 60–80 % empty paper; dark foreground may pass along the frame bottom. Transitions are ink blooms, pans along the scroll or mist; never a generic dissolve or a wipe.

## 7. Sound palette

- **Guqin-led, not piano and strings**: guqin (`core/audio/pluck.py` `guqin`: open and stopped strings, slides, vibrato, glassy harmonics, sweeps), a low breathy xiao, big drum and timpani for mass, frame drum for steps, a small gong for a seal. Chinese pentatonic modes.
- **Cue to the picture, never loop**: unmetred plucks suit emptiness, a pulse suits movement, rolls suit mass; painted strokes can each land on a pluck.
- **Silence is literal**: zero the whole bus (music, ambience, reverb tails) with short fades. At most one sound inside it (a drip, one ring). Place it where the story holds its breath.
- **Foley follows the material**: ink drop (short "tink" + soft wet thud), brush air (band-passed noise with bristle grains, never a metal whoosh), steps on water (small splash), splatter (wet ticks), seal (wooden thump + paper crackle).
- **Voice**: calm, few lines, like colophons that don't explain the picture. Duck music ~8 dB and ambience too; verify each line with whisper on the final mix.

## 8. Native moves

A menu: use the ones your story needs.

- **One stroke is everything.** *Fits content like:* a product born from one line; a city growing from a single street; a day beginning with one bird.
- **Emptiness is matter.** Removing ink reveals paper white. *Fits content like:* a door opening in a wall; a crowd parting; an absence in a family portrait.
- **Brush = gesture = action.** Stroke order becomes choreography. *Fits content like:* a dancer's phrase that spells a word; a signature; a chef's knife work.
- **Flying white (飞白).** One fast dry stroke across the frame, strongest out of a silence. *Fits content like:* a sprint finish; a decision; a comet.
- **Ink bloom transition.** The next scene grows inside a spreading drop with a dark tide-line (noisy radial mask; world-anchored for elements, in the compositor for scenes). *Fits content like:* memories; seasons; one era giving way to the next.
- **The handscroll.** One long painting panned right to left, seen whole at last. *Fits content like:* a history; a supply chain from field to hand; a day in a street.
- **Splitting a mass.** Halves clipped either side of the cut; one rises and fades, one slumps; splatter stays. *Fits content like:* breaking a record; a barrier falling; an idea splitting in two.

## 9. Pitfalls of the medium

- Dry brush looks like dashed lines → breaks from long-scale noise and an ink load that drops along the stroke.
- Parallel semi-transparent strokes make bodies look like organ pipes → one base mass + two loaded strokes.
- Big side-brush strokes look like a hairbrush → a gradient mass + a few low-dryness strokes. Gradients in vertical bands leave seams → a cached per-pixel layer.
- A stroke body split between wet and dry layers loses density → full body in the dry layer plus a wet halo.
- Clipping calligraphy with the font outline notches the junctions → font as skeleton only.
- Uniform hatching inside a wave turns it into a wire mesh → loaded strokes along the face.

## 10. Engine

In `demo/`: `ink.js` (brush engine: strokes, bristles, loaded strokes, masses, blots), `comp.js` (WebGL rice-paper compositor: bleed, edge pigment, paper, bloom), `land.js` (mountains, cun, cliffs, pine, reeds, ripples), `wave.js` (gestural wave), `glyph.js` (skeleton-traced calligraphy), `seal.js` (vermilion seal), `hero.js` (xieyi figure rig), `subs.js` (inscription subtitles), `music/score.py` (guqin writing with `core/audio/pluck.py`); `?test=sheet|pose|frame` pages draw model sheets from the real engine.

## 11. Variation space

You decide the structure, the characters (or none), the landscape, the opening, the ending, the camera path, the pacing and where the red goes. All far from our demo:

- Structures: **one character, stroke by stroke** (no figure; each stroke of one large character opens into a vignette of the topic); **a hanging scroll** (a tilt from sky to ground through four stages, tone deepening); **two brushes in dialogue** (alternating strokes answer each other until they meet in one bloom).
- Openings: **in motion** (a figure already painted and moving; the world washes in around it); **ink first** (a fully inked frame; ink is lifted where light or a road appears); **the bristles** (a wet stroke fills the frame; only when it lifts do we see what it drew).
- Endings: **one small mark** (close on a footprint or a leaf while the ink around it dries; no pull-back); **evaporation** (the painting un-paints in reverse stroke order); **mid-gesture** (the brush stops before the last stroke lands).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: impasto -->

# Impasto · Palette Knife — Style Prompt

> Thick oil paint laid with a palette knife: big, flat, sharp-edged planes of colour, raked by light so every ridge of paint shows. Clarity first: value structure before texture, hard edges at the focus, calm planes everywhere else.
> References (grammar only): the opening titles of *The Umbrellas of Cherbourg* (1964) (overhead choreography read as moving colour); palette-knife street paintings (Leonid Afremov and the genre around him) (knife mosaic, vertical wet reflections, warm lights against cool shadow); Sorolla / Sargent (few, decisive strokes and strong light); Edgar Wright's music-locked editing (one action, one sound, one cut). Never copy their images, compositions, melodies or characters, and never name them in the film.

## 1. Essence, and what it is not

A moving oil painting made of knife strokes. Each stroke is a real object: a slanted plane of paint with a ridge where the blade pressed, a lip where it lifted off, broken streaks where the paint ran out, two colours dragged into each other. The world is **repainted from its strokes every frame**, but static paint never moves: only things that move in the story move. Light rakes across a height field, so the paint has body.

The look is clear and graphic (readable like a children's book at thumbnail size) but has the tactile surface of impasto at 100 % crop.

Not a Van Gogh swirl filter (strokes boiling everywhere), not a brush texture over flat vector art, not watercolour (paint is opaque), not a "painterly" photo filter (strokes are designed, not sampled from noise).

## 2. Materials & rendering

- **Value first.** Design each set as a flat, value-planned illustration (3 values minimum), then convert it to strokes. If the reference doesn't read at 480 px wide, no brushwork will save it.
- **Stroke sizes by importance and depth.** Coarse to fine: large planes in sky and walls, a few px only at edges and faces (per shape: `maxR`, `detail`, `dir`).
- **Strokes never cross shape groups**, so silhouettes stay crisp. Lost edges are opt-in (put two shapes in the same `group`).
- **Thin underpainting** (the reference itself, blurred ~1.5 px) under the strokes, so the canvas never peeks through as outlines.
- **Knife stroke**: longer than wide (≈ 1.7–3.1 × radius long, 0.95–1.45 × radius wide), slanted ends, small angle and value jitter (≈ ±13°, ±6 %). Solid objects that must read as silhouettes (figures, props) get little or no ragged run-out.
- **Light** rakes over a height field; wet or glossy surfaces get slightly more specular.
- **Reflections** (wet ground, glass, water) are **explicit stacks of short horizontal knife dabs** under each light source, broken and fading; never a painted rectangle.
- Render supersampled (2×). **No film grain**: grain plus compression eats the knife edges.

## 3. Colour logic


<!-- END STYLE PAGE -->
