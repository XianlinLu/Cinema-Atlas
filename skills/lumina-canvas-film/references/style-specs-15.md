# Complete style specifications 15


<!-- STYLE: halftone-dossier -->

- **The accusation frame.** A topic becomes "the case of X": list its counts. *Fits content like:* a cognitive bias on trial; a city's traffic problem; a plant that won't stop growing.
- **Numbered exhibits.** Each beat gets a giant halftone numeral behind it. *Fits content like:* five causes of a blackout; three clauses of a contract; the stages of a recall.
- **The stamp.** A verdict is a physical slam. *Fits content like:* APPROVED on a grant; EXPIRED on a policy; VERIFIED on a rumour check.
- **The mugshot.** Frontal subject, height chart, name plate, flash. *Fits content like:* a new species; a product teardown; the "suspect" in a bug report.
- **Evidence board.** Exhibits pinned and linked with string, then shaken. *Fits content like:* a supply chain; a family tree; a heist's timeline.
- **Dot density = emotion.** Dots swell into a halo, crowd the edges for tension, bloom radially for joy. *Fits content like:* a record broken; a deadline closing in; a reunion.
- **Redaction.** Black bars print over words and lift one by one. *Fits content like:* a leaked memo; a surprise party plan; spoilers.

## 9. Pitfalls of the medium

- **Fonts not loaded before layout** → per-character positions computed with a fallback font, glyphs overlap. Preload every family against the whole page source and the built text; runtime strings must use only characters that appear in the file. Use `font-display: block`.
- **Boil on text or dots** turns them to mush → filter only characters and props.
- **Clip-path ids are global** → every clipped numeral needs a unique id.
- **Time-windowed scenes** → an element invisible before its cue needs explicit opacity 0 for `t < t0`.
- **A dot wipe short of full coverage** at the cut shows the hard switch; make the max radius cover the grid cell's diagonal.
- **A 100 % white flash** reads as a dropped frame → cap at ~0.5.
- **Dots too small** (< ~14 px step at 1080p) alias into moiré after encoding.
- **Too many inks** lose the print feel → at most five plus paper.

## 10. Engine

Everything lives in `demo/index.html`: helpers (`el`, `txt`, `tf`, `seg`, easings, `measure`), per-character text (`chars` + `charsPop`), **halftone** (`halftone()` with `radial`/`edge` density fields), `caption()` bar, **stamp** (`stampEl` + `stampAnim`), a mascot rig with a `setFace` interface, `scene(t0, t1, build)`, HUD chips, dot wipe (`WIPES`), paper + grain (`buildPaper`, `drawFx`), `render(t)`. `demo/render.mjs` renders stills and video; `demo/music.py` synthesizes score and SFX. Line ranges and a minimal scene: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide what the file is about, its counts or exhibits, the characters (or none), the inks within the colour logic, the tone (farce or grave), the opening, the ending and the length (it grows with the number of exhibits; each needs time to be read).

All far from our demo:

- Structures: **a declassified report** whose pages are unredacted one by one until the real story shows; **a missing-person file** that works backwards from the last sighting; **an insurance claim** where each exhibit contradicts the claimant's statement.
- Openings: **the evidence bag** (one object on a dark ink ground, the file assembles around it); **a fingerprint** in huge dots that resolves into a face as we pull back; **the phone call** (a caption bar alone on paper, the file drops in after).
- Endings: **the file goes into a drawer** full of identical files; **a redacted final page** (the answer stays blacked out); **the stamp misses** (it lands on the table, the subject walks free out of frame).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: woodcut -->

# Woodcut Print — Style Prompt

> A relief print that carves itself: every frame is a black wood block, and light only exists where a knife has cut it away. One colour at most, and only for the thing that burns.
> References (grammar only): Frans Masereel *Passionate Journey* (1919) and Lynd Ward *Gods' Man* (1929), wordless woodcut novels told as a sequence of self-contained plates; Käthe Kollwitz's woodcuts, where emotion lives in the direction of the gouge; Gustave Doré's engraving, where line spacing and direction build light and volume. Never copy their plates, figures, borders or titles.

## 1. Essence, and what it is not

Each shot is **one printed plate**: black ink on laid paper, framed by a paper margin. It follows three rules of real relief printing:

1. **Black is the wood, white is what the knife removed.** Light is *carved*: a bright area is many wide cuts, a dark area untouched wood.
2. **Pictures appear by being carved.** Nothing fades in: cuts grow stroke by stroke along the form, coarse gouges first, fine lines after.
3. **The block is a mirror.** Letters read backwards until the paper is pulled; that reversal is the style's own transition.

Not copperplate engraving (no swelling burin lines on white, no crosshatch built up from white ground), not linocut poster art (no flat colour areas), not a black-and-white photo run through a threshold filter (the cuts must follow the form).

## 2. Materials & rendering

- **Print frame**: the printed image area sits inside a paper margin; the wider bottom margin holds captions. The image edge is the block edge: ragged ink, never a clean rectangle.
- **Knife classes** (widths in 1080p pixels at 1× camera):

| Tool | Width | Use |
|---|---|---|
| Knife `k` | 1.2–2 | contours, the white outline that separates a black figure from a black ground |
| V-gouge `v` | 2–8 | hatching, hair, beard, fine light |
| U-gouge `u` | 10–22 | rays, sky sweeps, the first rough-out |
| Stab `stab` | r 3–8 | snow, sparks, flecks of loam, wood chips |

- **Hatching (Doré grammar in wood)**: line **direction follows form** (a round object is wrapped in arcs, slopes follow the fall line, fire and light radiate, cloth follows its folds). **Width follows tone**: bright = wide cuts almost merging into white, mid-tone = thin cuts, dark = no cuts. Far = dense and fine, near = sparse and coarse. Every line is a separate cut (30–160 px, blunt entry, tapered exit, chipped edge), never a continuous machine line.
- **Figures**: black silhouette + white knife halo + grazing-light hatching on the lit edge only (light z ≈ 0.2, so flat areas stay black). **Skin carved white, features left black** (the wordless-novel rule).
- **Close-ups (hands, objects)**: sculpt a small height field (capsules, blobs, planks, creases), light it and run it through `woodcutFilter` (§10), so cuts follow the isophotes like an engraver's.
- **Printing**: the mask (white = cut) goes through a WebGL2 compositor: knife burr on edges, ±6 % ink unevenness, wood-grain streaks, specks where ink didn't take, a mottled colour plate with a small fixed misregistration. Block mode: glossy inked wood with grain sheen, pale wood in the grooves.

## 3. Colour logic

- Two values carry everything: near-black ink and warm laid-paper white. The raw wood colour appears only in shots that show the block itself.
- **At most one colour plate**, printed only where white has been carved, so it glows out of the cuts and never sits on the black. A colour plate over ink is nearly invisible, so plan it on carved white.
- The colour is reserved for the one thing that matters (a flame, molten metal, a heart, a signal lamp). It can spread at a peak and shrink to a single highlight afterwards; it is never decoration.
- Examples of a plate: a burnt copper-orange for heat; a cold Prussian blue for water or night; a deep oxblood for a wound or a seal. Choose it from the topic.

## 4. Type & subtitles

- **Captions are letterpress in the paper margin**, below the plate, like a plate caption in a woodcut novel. They never cover the image. A letterpress old-style face (IM Fell English, OFL) around 40–44 px, in ink, pushed through the same print shader. The ink comes up in 0.1 s with no slide and fades over 0.15 s. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles are carved, not typed**: cut into the block (IM Fell English SC), mirrored if the block is shown before the print is pulled.
- Any closing text is a fresh print: letterpress in the margin or carved out of a black panel.

## 5. Motion quality

- **Characters on twos (12 fps)**; camera, particles, fire and light on ones (24 fps). Hatching lives in each body part's local space, so cuts move with the limb and don't boil; only fire and liquids re-cut every 2 frames, as deliberate boil.
- **Anticipation / action / follow-through** on every key action: a few frames back → a 2-frame strike → settle + a short shake.
- **Carve reveal**: each stroke has its own start time and speed (0.08–0.35 s). Reveal keys: `light` (bright areas first, coarse to fine), `radial` (from a point: rays, a pour), `down`, or any function.
- **Hard cut = a new impression**: two frames of misregistration (a few pixels, then back).
- **Paper transition** (the one transition grammar): brayer rolls ink (a wet highlight sweeps) → paper lays down → baren spirals, the image soaks through → the sheet peels on a cylinder toward camera, heavy then fast, its back showing the mirrored show-through.
- What never moves: the paper margin.

## 6. Camera grammar

The camera moves over the paper; the margin stays fixed. The knife tip, or the brightest cut, is the focus.

| Move | What it expresses | Can serve |
|---|---|---|
| Track with the knife tip | Making; the line is the story | a first mark; a route drawn on a map; a signature |
| Continuous pull-back as cuts spread | A line becomes a world; scale | a city from one street; a family tree; a reach of sound or news |
| Locked plate | A page of a wordless novel; reading time | a decision; a portrait; the aftermath |
| Slow macro push on a sculpted close-up | Patience, touch, labour | hands at work; a tool; a letter being read |
| Snap zoom and hold | Shock; the detail that breaks | a crack; a wrong number; a face turning |
| Frame in a frame (door, window, arch) | Distance, exclusion, waiting | a crowd outside; a sickroom; a border |
| Hard cuts on the beat, each a new impression | Accumulation, a series of prints | offerings; days passing; a list of names |
| Crane up from a detail to the whole | Consequence | a flood reaching a village; a light reaching faces |
| Rack between two plates via the peel | One state printed over another | before/after; a promise kept; generations |

Opening and ending come from the topic. Framing: black masses on carved white or white on uncut black, never grey on grey; text only in the margin. Transitions: hard cut (new impression) or the peel; never a dissolve.

## 7. Sound palette

- **Instruments**: low strings (contrabass, cellos; spiccato, pizzicato), wood and skin (log drum, woodblock, frame drum), gran cassa, timpani, one tam-tam, synthesised struck metal (modal: 3–5 inharmonic partials + hammer transient); a bowed saw or hurdy-gurdy drone for a folk colour.
- **Options**: withhold the timbre of the story's object until it appears; a metric modulation instead of a tempo jump; a modal shift inside a long decay; one drone under a locked plate.
- **Foley follows the material**, all synthesisable: knife into wood (transient + band-passed fibre tearing tied to knife speed), chips, brayer tack, paper air, baren rasp, the wet peel; metals by size (large = low, small = high and pure); resonant objects as modal models plus echoes for distance.
- **Silence is a tool**: near-silence with one faint ambience, or true digital silence before the loudest moment; the first sound after it is chosen.
- **J/L cuts** carry sound across plates and peels.
- **Mix**: music ducks ~8 dB under voice and a little under key foley; **foley ducks too** under voice. Pan hard transients off centre. −14 LUFS.
- **Voice**: few lines, low and plain, like captions spoken; the plates tell the rest.

## 8. Native moves

A menu: use the ones your story needs.

- **Light is carved.** A burst of radial cuts from a point. *Fits content like:* a power grid switched on; a scientific insight; a lighthouse restored.
- **Carving = time.** Patient work on screen, cut by cut. *Fits content like:* a year of training; a building rising; a craft apprenticeship.
- **Mirrored block → true print.** A backwards word reads true when the sheet is pulled. *Fits content like:* a vote result; a name cleared; a misunderstanding put right.
- **Stab cuts as texture.** White dots can freeze mid-air or be inked back in until the black is clean. *Fits content like:* stars going out over a city; rain stopping; a disease receding on a map.
- **The one colour plate spreads and withdraws.** *Fits content like:* a blood donation; a sunrise over a harvest; a single lit window in a blackout.
- **Filter a sculpt or a frame** into form-following cuts. *Fits content like:* a portrait of a real person drawn from a photo; a machine part; an archive image re-cut.
- **Wordless-novel sequencing.** Self-contained plates, few or no lines; a gap can be silent. *Fits content like:* a migration; a strike; a life in seven plates.

## 9. Pitfalls of the medium

- **White marks on white areas are invisible** → stab cuts need dark masses behind them.
- **Hatching every surface looks like fur or rain** → grazing light; 3–6 cuts on the lit edge only.
- **Black faces with white cuts don't read small** → skin white, features black, a black keep-line around white parts.
- **Hand-drawn close-up props look like mittens and blobs** → height field + `woodcutFilter`.
- **Short hatch segments with a tonal wobble turn into zig-zag chevrons** → long cuts (14–50 × spacing), one broad highlight band, a thin rim light, a stronger halo.
- **Steam or smoke on top of the subject reads as flames** → draw it behind, so only wisps escape.
- **Lazily cached strokes shared between shots** make frames depend on the render worker → every cache builds itself on first use.
- **Fine hatching + ink noise + grain inflate the file** → a higher CRF with `-tune grain`; check a 1:1 crop. `woodcutFilter` NaN in flat areas → clamp before `sqrt`.

## 10. Engine

`demo/engine/index.js` (imports only `/core/lib.js`) carves and prints **any path or shape**, on two canvases: a **mask** (black = uncut, white = cut) and an optional **colour plate**. Main functions: `shape` (carved solid with halo and form-following hatching), `cutAlong` (a path as hand-cut strokes), `hatch` (streamline hatching of a region), `flecks` (stab cuts), `rays` (carved light), `drawStrokes`, `plate`, `woodcutFilter` (image or frame → cuts), `makePrinter(W,H).render` (print / block compositor). Reusable demo pieces: `demo/trans.js` (paper peel), `demo/hands.js` (height-field sculpts). Option table, a minimal example and the filter recipe: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the story, characters (or none), plates, opening, ending, camera path, pacing and what the one colour is for. All far from our demo:

- Structures: **a book of hours** (seven locked plates, one per hour, no moves inside a plate); **the same block recut** (carved deeper each scene, the image changing as wood goes); **two blocks printed in turn** (two places alternate impressions until one sheet carries both).
- Openings: **the finished print on a wall** (then back into the block to see it cut); **white paper** (an inked block pressed onto it: the first image arrives whole); **wood grain** that becomes water or a field as the first cuts follow it.
- Endings: **the block cleaned** (ink washed off, pale carved wood remains); **a stack of prints** (rising over many sheets of one plate); **an uncarved corner** (holding on black wood the knife never reached).

---

How our demo was made (story, shots, score, end card, build, engine reference): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: engraving -->

# Copperplate Engraving — Style Prompt

> An intaglio plate that engraves itself: a burin cuts swelling lines into copper, a proof is pulled, and the figure builds up — outline, hatching, cross-hatching — until engraved lettering, magnified details and a hand-laid wash make a finished plate.
> References (grammar only): 19th-century natural-history plates — Haeckel, Audubon, Westwood, the *Britannica* copperplates (centred subject, numbered roundels, roman title over an italic name, "del." / "sculp." credits, the plate mark); Hogarth and Doré for the burin line (hatching that follows the form, crossing only in half-tones); hand-coloured plates for washes laid after printing. Never copy a plate, pose, border or title.

## 1. Essence, and what it is not

An **intaglio print**: the line is ink held in a groove a burin cut into copper. Three rules:

1. **Tone is made of lines, never of fills.** Light is bare paper; half-tone is one family of parallel lines; shadow a second family crossing it; the deepest dark a third, lozenge-making family. No grey fill anywhere in the ink.
2. **Every line swells and tapers.** The burin enters fine, bites deeper mid-run and lifts out to a point. Lines thicken where the form turns from the light and vanish where it faces it; contours are cut in several runs and thin where runs hand over. A uniform-width line reads as a pen or vector drawing — never.
3. **Colour comes afterwards, by hand**: transparent watercolour laid flat region by region over the finished black print, spilling past the lines, pooling at its edges, ink always on top. A film may stay monochrome long; colour arriving is an event.

Not a woodcut (black block, white gouges — `woodcut`), not a pen sketch (loose broken lines — `urban-sketch`), not an engineering drawing (`blueprint`), not a sepia filter.

## 2. Materials & rendering

- **The sheet is the world**: 1920×1080 world units of laid paper (cream, ~`#f1e8d2`) with world-space texture (fibres, laid lines, sparse foxing) that zooms with the camera; a pressed, bevelled **plate mark** and a ruled border (rule + hairline) frame it.
- **Ink** is one warm near-black (~`#1c1510`). Width ratios: outlines heaviest (swelling ×0.45–1.35), first hatching from a hair (~0.18 px) to ~2 px, crossing ~0.8×, third family ~0.6×, hair and stipple finest. Spacing is **relative to the figure** (~1/180 of its height, a little wider per later family) so small figures never go grey.
- **Swell law** for every hatch line: width × (0.2 + 0.8·sin(πu)^0.7), tapered over its first and last ~22 %. Families switch on by tone thresholds (~0.14, ~0.5, ~0.75 on a 0–1 tone).
- **One light direction** for the whole film (upper left by convention); heavier outlines away from it; tone fields come from the shape (pillow lighting, analytic spheres and cylinders), never from texture. **Occlusion** is geometric: lines stop at the shapes in front.
- **Roundels**: double-ruled circle, ruled-machine ground with a white halo round the subject, content authored at a large radius and scaled in. **Leaders**: hairlines from a dot on the part to the rim, routed with clearance, a small italic figure number at the root.
- **Hand colouring** multiplies over paper and under ink: a few px of spill, slight misregister, tide-line at the wet edge, low-frequency density lift, occasional backruns, granulation; each region blooms from where the brush touched.
- **Copper** (when shown): polished warm metal, polishing hairlines, a soft reflected window; grooves = dark trough + bright burr toward the light. The **burin** (lozenge steel shaft, bevelled face, mushroom handle) is held low and turned ≤ 15° off the line so the fresh groove shows; **swarf** is a narrowing ribbon curling ahead of the point, one edge lit.

## 3. Colour logic

- The print is two values, paper and ink; all tone is line density.
- Colour is **transparent wash only**, in muted earth and mineral pigments, one stronger pigment at most. Never opaque, never on lettering, rules or paper outside the figure.
- Reserve it: the whole subject at one moment, or only the part that matters — or none.
- Example wash sets: an amber insect with blue-grey wings; a map with a sea-green coastal band on buff land; one madder-rose organ on an otherwise black anatomy plate.

## 4. Type & subtitles

- Lettering belongs to the plate: **roman capitals** (Bodoni Moda; title ~44–56 px, wide tracking; labels ~15–19 px), **italics** for scientific names (~20–24 px), **script** (Pinyon Script) for notes, fixed size, balanced over two lines, never shrunk.
- Roman letters are **cut glyph by glyph**; script is **written** in one left-to-right stroke. Nothing fades in.
- Subtitles: script on a deckled paper slip, bottom centre, ≤ 2 lines, never over a label. Hold ≥ max(1.8 s, speech + 0.6 s). An engraved note stays in frame chars ÷ 12 + 1 s from when it starts writing.

## 5. Motion quality

- **Cutting order is the animation**: outline → first hatching sweeping across each form → crossing → darks, hair, stipple. Strokes run at constant burin speed, many at once (a few for outlines, dozens for hatching).
- A long single stroke may be followed by the camera; start it partly cut so no frame is empty. Keep a full build to a few seconds.
- Roundels fly on an eased arc with a small lift, growing log-linearly to size. Colour blooms from one point with a ragged front and a wet rim that dries; regions staggered.
- Nothing fades or slides like UI: lines are cut, text cut or written, colour blooms, sheets are pressed, peeled or laid down.

## 6. Camera grammar

The camera is a **loupe over a sheet**. A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Loupe following the burin tip | One point of attention; making | a first mark; a signature |
| Log-zoom pull-out | The line was part of something larger | scale reveal; context |
| Push to a part, ride with its roundel | Where → what, in one take | an invisible detail; a mechanism |
| Tilt/pan along the sheet at reading zoom | Labels in order | a parts list; a coastline |
| Pull back while something flies | Everything placed in relation | acceleration; summary |
| Locked frame, or a ≤ 2 % breathing push | The plate as document | reading time; colour moving |
| Raking view across the copper | The groove as depth | the cost of craft |
| Cut from mirrored copper to true proof | Reversal | a hidden truth; before/after |

Framing: subject inside the plate mark, labels and roundels in the margins; order details so push-ins never crop a note early. Transitions from printmaking only (proof pulled, tissue guard laid over, region burnished out and re-cut, new sheet on the bed); no dissolves or wipes.

## 7. Sound palette

- **Foley by material**: paper (peel crackle, slip tapped down, tissue rustle, sheet whoosh); press (roller rumble, thump); copper and steel (high band-passed burin hiss with chatter and faint plate ring, swarf pings, a tick on lift, circular scribe, burnishing rub); ink and water (pen scratch, ticks for cut letters, a water plip and wet brush swish). Hatching = micro-scratches denser each pass.
- **Room**: a quiet workroom (faint clock), paper room once the print exists.
- **Instruments** (choose): harpsichord, string quartet, solo cello or viola da gamba, lute, chamber organ, glass harmonica for a cold subject. Plucked and dry while lines are cut; bowed or sustained only when something soft arrives; tiny tings for a scribed ring, a low pluck on landing.
- **Silence** is real: cut room tone too, keep at most one small sound.
- **Mix**: melody an octave above the voice, music ~half under speech, −14 LUFS. Voice: a quiet curator or naturalist.

## 8. Native moves

A menu: use the ones your story needs.

- **The cut.** Burin mid-stroke, swarf rising, nothing else. *Fits:* the first line of a treaty; a watchmaker's scribe; a coast being charted.
- **The three passes.** Form gains volume pass by pass. *Fits:* a building from its plan; a portrait emerging; a skill improving.
- **Magnification roundel.** Ring scribed, burnished, re-cut larger, flown to a margin with a leader, label cut on landing. *Fits:* a gear in a clock; a pollen grain; a harbour inset on a chart.
- **The proof.** Sheet peels off; mirrored copper becomes true paper. *Fits:* a secret out; a draft made final; a coin's die and strike.
- **States of the plate.** A region burnished out and re-cut. *Fits:* a border redrawn; before/after; a design revision.
- **Hand colouring.** Washes bloom after the print. *Fits:* one organ lit; a flag on a historical map; a ripening fruit.
- **Natural size.** A tiny true-scale figure beside the engraving. *Fits:* a seed by its tree; a chip by its circuit; a stamp by its enlargement.
- **The finished plate.** Every label and credit, locked. *Fits:* a museum label; a frontispiece; a certificate.

## 9. Pitfalls of the medium

- Uniform width reads as pen → swell hatches, pinch contours between runs (`hatch({swell})`, `outline({run, pinch})`), keep wMin hair-fine.
- Overlaps without occlusion → pass occluders as `excl` (subtracted ring by ring; even-odd would cancel overlaps).
- Outline-only parts beside a hatched body → hatch along each part's axis, a dark at every joint.
- Burin along the cut hides the groove; big skew looks like poking → ≤ 15°. Regular swarf helix reads as a spring → vary winding, twist, light one edge.
- Reflections over grooves wash them out → copper light first. Roundels authored small freeze sub-pixel → author large, scale in. Leaders hugging the subject read as crossing it → clearance.
- A long early stroke never draws → the ink's early exit must look ahead by the longest stroke.
- A push-in cropping a fresh note breaks the reading rule → put consecutive details on one side.
- Scientific names: TTS may manage, ASR won't → give the checker a plain spelling.

## 10. Engine

`demo/engine/`: `burin.js` (`B.Ink` ordered stroke store + `schedule`, `B.hatch`, `B.engraveTone`, `B.contourHatch`, `B.outline`/`B.stroke`, `B.stipple`, `B.fur`, tone fields), `plate.js` (`drawSheet`, `engraveText`, `writeScript`, `roundelFrame`), `wash.js` (`Wash`), `copper.js` (copper, burin, swarf), `index.js` (`engraveShape(svgPath, {at, light, spacing, style})`: any SVG shape → engraved figure). `demo/example/index.html` engraves and colours a four-pointed spark in ~20 lines; code and function table in DEMO.md "Engine reference".

## 11. Variation space

You decide subject, details, order, opening, ending, camera path, colour, pacing and music. Use cases are **grammar for the order and duration of information**; build your own timeline from the user's facts.

| Use case | Information order | Hold per layer | Length |
|---|---|---|---|
| **Museum label / case screen** | title + scientific name → detail + term + note (×N) → where to see it | title ≥ 2.2 s; note ≥ chars/12 + 1 s; final ≥ 4 s | 30–40 s |
| **"One minute on …"** | question → name → 2–3 facts → one number → follow prompt | number ≥ 2.5 s alone | 35–60 s |
| **Textbook figure** | figure → parts labelled one by one → caption | label ≥ chars/12 + 1 s | 20–45 s |
| **Craft heritage** | object → 2–3 craft details → maker / edition | as above | 30–45 s |
| **Map / site plan** | place → insets → legend → visiting info | inset ≥ 3 s; legend ≥ 4 s | 30–45 s |

All far from our demo:

- Structures: **states of one plate** (one view re-cut three times as a place changes); **a book of plates** (four small plates turned like pages, one fact each, no roundels); **a dissection** (parts labelled in teaching order, colour only on the part taught).
- Openings: **the finished proof burnished back** to its first line; **on paper at 1×** (title cut first, figure grows below); **raking light over blank copper** as the design is traced.
- Endings: **plate beside its proof**; **the natural-size figure** held alone; **a blank new sheet** laid on the stack.

Swapping `demo/content.json` and rebuilding is a technical check that the engine re-flows, not a way to make a film.

---

How our demo was made (story, shots, score, end card, build, content fields): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: silkscreen-poster -->

# Silkscreen Travel Poster — Style Prompt

> Opaque, hard-edged flat inks pulled one colour at a time through a screen: 4–6 inks per poster, stepped colour bands instead of gradients, thin paper-white gaps where the registration slips. Information is revealed the way the print is made: one layer, one beat.
> References (grammar only):
> - **1930s–40s WPA national-park screen prints**: 4–6 flat inks, lit and shade faces, stepped-band skies, a dark information band, concentric sun rings.
> - **Fifty-Nine Parks (contemporary)**: restraint, paper as a colour, a series on one template with a new palette per poster.
> - **The physical process**: hinged screen, squeegee pushing an ink bead across mesh, split-fountain pulls, drag streaks, pinholes, off-register slivers.
>
> Never copy a real poster's composition, park name, lettering or logo, and never name a real agency.

A **scene style**: it does a practical job (a guide, an event poster, a destination series) for any place, event or product with a few facts. See §11 for the jobs.

## 1. Essence, and what it is not


<!-- END STYLE PAGE -->
