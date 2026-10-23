# Complete style specifications 08


<!-- STYLE: data-physical -->

- **Pieces**: thin boxes or cylinders instanced in the thousands, each with a few-millimetre random offset and yaw, a ±7 % value change and a hairline gap: that is what makes a stack read as stacked, not as a bar.
- **Material per series**, chosen so two series separate in one glance at thumbnail size: brushed metal against tinted acrylic, pale wood against dark stone, copper coins against paper. A third material (e.g. brass) only for the ruler pieces, shared by every series.
- **Base**: a real-texture slab (wood veneer, stone) with inlaid marks: a tick ring, the series' paths, the labels of categories or years, cut into the surface at the base's own scale, lit with the scene.
- **Rendering**: PBR (transmission for acrylic), an HDRI at low intensity for reflections only, a warm key at 20–35° with long soft shadows, one or two cool rims so metal and acrylic separate from wood at distance; GTAO, physical depth of field, 2× supersampling, a light vignette.
- **Screen space only for type**: readings, verdicts, the source line, subtitles, the title card. Every reading is pinned to its object through the same world → screen function as the camera.
- **Post**: grain light (the background is pale), no lens flares, no chromatic aberration.

## 3. Colour logic

- The set is warm and neutral: a seamless greige sweep, the base in a natural material, the series in material colours (silver, pale teal, brass, oak). Material, not paint, separates series.
- **One accent** (e.g. signal orange) for the reading or verdict that matters on this screen; nothing else is accent-coloured.
- Ink is near-black at two strengths (value, then labels at ~60 %).
- No rainbow series palettes, no colour ramps on the objects, no dark mode.

Example (our demo): sweep #C4BEB4, walnut base, aluminium #C8CCD1 (metal), acrylic #9FD3D6 with teal attenuation, brass #D2B07A, ink #1C1D20, accent #D4521C.

## 4. Type & subtitles

- **Roles**: a light grotesk for numbers (e.g. Inter 200–300; the hero reading 130–170 px, a stack reading 46–56 px); a sans for labels and verdicts in the film's language (e.g. Noto Sans SC 500, 24–46 px); a monospace for units, years and source lines (20–24 px); a serif only for the title. OFL, self-hosted, CJK subset.
- **A reading** = a dot on the object, a 1.4 px leader, a small swatch of the series' material, the category line, then the value and unit, on a translucent paper plate (~84 %). Two readings of one pair stack in one column, larger value on top.
- **The source line** (dataset, publisher, year, licence, e.g. "数据：IRENA (2026)，经 Our World in Data 整理 · CC BY 4.0") is in frame with the data, small (20–22 px, ink at ~60 %) in a corner away from the subtitles, at least from the first reading to the summary, and on the title card.
- **A verdict** sits in the upper-left third on its own plate in the accent colour, underlined by a growing rule; it appears only after the readings it judges have been still for ≥ 2.5 s.
- **Subtitles**: bottom-left, a 2 px ink rule and a paper plate fading right; if the film is bilingual, the film's language on top; each line one line only, measured with the real font (`nowrap`), split into two cues rather than wrapped. Hold ≥ max(1.8 s, speech + 0.6 s).
- Labels hold ≥ CJK characters ÷ 4.5 + 1.5 s / letters ÷ 15 + 1.5 s; a counter reports its landing value; nothing below 20 px.

## 5. Motion quality

- On ones, 24 fps; the camera never stops (2–5 % creep on holds).
- **Cascade**: a stack assembles bottom-to-top in 0.5–1.0 s, each piece dropping a few centimetres with an ease-out.
- **Feed**: one period's increase arrives piece by piece from out of frame, quintic ease-out, a yaw that unwinds ("placed", not "dropped"), 8–16 pieces per second, the counter rolling with the pieces landed.
- **A single heavy object** falls with gravity, lands with one small damped bounce, its shadow tightening.
- Readings fade in with a 16 px rise and draw their leader; they leave by fading, never by sliding.
- Never moves: the base, a piece once landed, the ruler pieces.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro dolly along a stack's edge, rack focus | the unit is real and countable | the rule "1 piece = X"; a single record |
| Low lateral track along the series | time passing; growth | a decade; a ranking; a sequence of sites |
| Locked three-quarter frame on two subjects | comparison | before/after; A against B; a crossover |
| Crane with the rising top | accumulation | one year's increase; a target being reached |
| Pull-back to near top view | the whole as an object | a summary; a ratio; an ending |
| Slow orbit around the base | the installation as sculpture | a title; a breath |

The subject fills at least a third of the frame height at key moments; readings live in empty background, never over the subtitle strip; comparisons keep both subjects completely in frame. Transitions are camera moves inside one set (one continuous take where possible); no cuts to a chart, no wipes, no page turns.

## 7. Sound palette

- **The material's own sound** is the foley: metal plates tick bright and short (inharmonic partials 3–8 kHz), acrylic toks duller (1–3 kHz), wood knocks, coins ring. A cascade is a burst of these at the landing times, scaled down as density rises.
- **The ruler sings**: every ruler piece (each 10th) rings a pitched mallet note, one timbre per series (e.g. glockenspiel for metal, glass harp for acrylic), climbing a pentatonic scale with the count — the chart becomes an arpeggio.
- **Score**: mallets and air — marimba ostinato, bowed and struck vibraphone, harp, glass, a soft synth pad and a pulse bass with audible 2nd/3rd harmonics; horns for a turn. Accelerate by subdivision (8ths → 16ths), not tempo.
- **Impacts**: a turn or a last object lands on punch (60–120 Hz) + bass drum + timpani + a bell; the two or three designed impacts are the loudest moments.
- **Silence**: a 0.3–0.6 s suck-out (music and foley −30 dB) before each designed impact; a thin studio-air bed stays.
- **Mix**: voice ~10 dB over music, ruler notes under the voice, −14 LUFS, true peak ≤ −1.2 dBTP. Voice: calm, precise, short sentences.

## 8. Native moves

- **The unit close-up.** Push into the side of a stack until one piece fills the frame; bracket one piece ("= 10 GW") and one ruler piece ("= 100 GW"). *Fits content like:* tonnes of CO₂ as steel plates; a budget as banknote bricks; a population as wooden discs.
- **The paired climb.** Two series on one base, one material each, built year by year as the camera tracks; the crossover is held still with both readings before the verdict. *Fits content like:* imports vs exports; renewables vs fossil capacity; two companies' revenue.
- **The feed.** One period's increase arrives piece by piece onto last period's level, the counter rolling with the landings. *Fits content like:* this year's new hires on last year's team; a quarter's sales; a record harvest.
- **Chart to installation.** Pull back until the bars are a dial, a skyline or a table piece; the base's inlaid marks become its typography. *Fits content like:* twelve months as a clock; regions as a map-shaped base; product lines as a city.
- **The last object.** One single heavier piece (a brass puck, a coin, a weight) lands on the base carrying the final number engraved. *Fits content like:* a total; a ratio; a target met.

## 9. Pitfalls of the medium

- Two materials too alike (bright aluminium vs clear acrylic) read as one series: give one a tint or a finish change, and check at thumbnail size.
- Long shadows and warm reflections turn metal brown at distance: add a cool rim light and keep the base darker than the pieces.
- Thin pieces moiré at 2–3 px per layer: random per-piece value and offset, 2× supersampling.
- A reading pinned to a moving object can leave the frame: clamp it to a safe box.
- Counters that roll by time instead of by landed pieces lie; tie them to the object count.
- Rounding to whole pieces can invert close values; when two values are within one unit, say so on screen or choose a finer unit.
- Transmission streaks at low angles: acrylic roughness ≥ 0.2, tinted attenuation.

## 10. Engine

- `demo/set.js` — `buildSet(scene)` (HDRI, warm key + cool rims, base with inlay canvas, instanced pieces per material, the last object) and the landing schedule (`SHEETS`, `EVENTS`, `landed(stack, t)`); change `PAIRS`, the unit and the materials for any single or paired series.
- `demo/film.js` — cylindrical camera keys (`track`, `core/lib.js`) with focus on a target point, the reading kit (`pairLabels`, `verdict`, `plate`, `swatch`), counter, subtitles (`SUBCHECK`), `TEXTS`, `EV`. `demo/mix.py` — material foley (`tick_alu`, `tok_acr`), ruler notes, suck-outs, master.
- **Extra packages and packs**: beyond `setup.sh deps` only the studio HDRI, `sh tools/fetch.sh hdri` (Poly Haven, CC0, 12 MB); with narration `setup.sh deps voice`; for a sampled score `sh tools/fetch.sh instruments vsco2ce` / `vcsl` / `freepats`. The walnut veneer is in `core/assets/polyhaven/`. Anything you add (a spreadsheet reader, other textures) goes into a private venv / node_modules in the project folder, never into `$LIB/.venv`.
- Minimal example, not in the demo: one series of twelve monthly values on a 12-position circle, the annual total engraved on the last object.

### Sources, licences, facts

- **Statistics for a new topic**: Our World in Data (each chart's "About this data" names the original source; CC BY 4.0 — credit both), World Bank Open Data (CC BY 4.0), Eurostat (CC BY 4.0), US Census / BLS / EIA (public domain); UN Data, IRENA, IEA free tables and other national statistics offices (e.g. 国家统计局): check each dataset's terms. Search the portal for the indicator, download the CSV, keep the file and its metadata in the project's `data/`.
- **Licences**: CC0, public domain and CC BY are fine with a credit. ODbL, CC BY-SA, "no known restrictions" or "free for non-commercial use" are not CC0: name the terms to the user and ask before using them. Textures and HDRIs: Poly Haven / ambientCG (CC0).
- **The user's own numbers** (annual report, ESG data, sales): ask for them and for the document they come from; never invent or round them into a better story. Never let generated images stand in for real data or material.
- **Keep a FACTS.md in the project folder** — each on-screen number and spoken claim, its source URL, the quoted wording or row, and how any derived value (ratio, difference, units per piece) was computed — and deliver it with the film.

## 11. Variation space

Decided per film: the unit and its materials, the base and its shape, which series share it, the camera route, pacing, the last object, accent hue within the colour logic.

- Structures: a single series rising to a record; two series and their crossover; a ranking of regions laid out as a map-shaped base.
- Openings: the macro of one piece being placed; the finished installation seen from above, then the dive to the first unit; an empty base with its inlay waiting.
- Endings: the last object landing at the centre; a slow orbit of the whole installation; a single piece lifted off to show what one unit is.

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: teardown -->

# Exploded Teardown — Style Prompt

> A real product, built from its own engineering files (CAD, PCB layout, bill of materials), lit like a studio packshot and taken apart in front of the camera: the layers lift on one axis, the camera travels between them, every part is named with the numbers its files contain, and it closes again into one object.
> References (grammar only): hardware-launch exploded films (layer stagger, orbit timing), repair-guide teardowns (opening order, the macro on the part that matters), engineering drawing (leaders, dimension lines). Never copy their products, layouts, typefaces or music, or name them in the film.

## 1. Essence, and what it is not

A frame reads as this style when:

- **the object is real and exact**: geometry, positions and counts come from the product's own files (STEP, KiCad, BOM, assembly guide). Nothing is eyeballed that a file can give;
- **it is shown apart**: layers float on one axis with even, readable gaps, each still oriented as it sits in the product;
- **it is photographed, not drawn**: physically based materials, a studio key light, a cool rim, an HDRI reflection, soft contact shadow on an invisible floor;
- **the numbers live on the object**: thin leader lines from a dot on the part, dimension lines with ticks drawn in the scene's own perspective, never a table beside it;
- **the camera never stops travelling**: one or a few continuous moves, orbit outside, macro inside.

It is not a glass product render (one object, material beauty, no disassembly), not a blueprint (line drawing on a grid, no light), not a keynote (slides, headline type, a stage), not an assembly manual (step numbers, arrows, hands).

## 2. Materials & rendering

- Real-time PBR (three.js `MeshPhysicalMaterial`) at 2× and downsampled, ambient occlusion, a depth of field with one aperture for wide and macro (blur follows 1/focus − 1/z, so it grows as the camera comes close), a high-threshold bloom for emitters only, a vignette.
- Each material keeps its character: plastics with soft sheen (roughness 0.55–0.7), boards with a thin clearcoat and traces as a raised, lighter relief under the mask, metallic pads, tight highlights on machined metal, matte rubber.
- **Boards are painted from their layout files**: copper pours, every trace, via, pad and drill, silkscreen, on both sides, at 14–20 px per millimetre, with roughness, metalness and bump maps from the same drawing. Components stand at their footprint positions with their package sizes.
- Light: a warm key from above front, a cool rectangular rim behind that follows the camera so edges separate from the ground, a soft top light, a low HDRI for reflections; a practical fill only where the camera goes inside.
- Background: a dark graphite seamless sweep (screen-space radial gradient), floor visible only as soft shadow.
- Effects anchored to the world (leaders, dimension lines, glows) are projected from 3D points every frame; only subtitles and title cards live in screen space.

**Where the geometry comes from.** For the user's own product, ask for its STEP / IGES / KiCad / other CAD exports, BOM and spec sheet before anything else. For a public product, look for open hardware (GitHub, GitLab, OSHWA certification list, Hackaday.io, Printables/Thingiverse sources with the original CAD) and component datasheets from the maker. CC0, public domain, CC BY and MIT are fine with credit; CERN-OHL (-P, -W, -S), CC BY-SA, GPL hardware and "no known restrictions" are not the same thing: name the terms to the user and ask before using them. Without files, build only from published dimensions (datasheet, spec page), say on screen or in the voice that it is a model, and show no number you could not source. Never stand in a generated image for the real part.

Keep a FACTS.md in the project folder (claim, source URL, quoted wording, or the measurement method for anything measured from the CAD) and deliver it with the film.

## 3. Colour logic

- The product brings its own colours; the frame around it is neutral and dark, so the product is always the brightest, most saturated thing.
- Interface ink is one warm white at two strengths (names at full, specs at about 60 %), plus **one accent** reserved for measured things: dimension lines, label indices and one matching detail on the product itself.
- Values are ordered: ground darkest, product mid to light, labels lightest. Never put text on a busy, bright part without a dark backing.
- Example (our demo): ground #34363a → #0d0e10, ink #f1efe9, accent #ff6b3d.

## 4. Type & subtitles

- Names: a clean sans at medium weight in the film's script (28–32 px; Noto Sans SC 500 in our demo). Specs and numbers: a monospaced face (15–22 px; JetBrains Mono) so digits line up and read as measurement. A neutral grotesque (Inter) for Latin running text.
- Label structure is fixed: a two-digit index in the accent, the name, one spec line. Units always written (mm, MB, ×n for counts). A label carries at most one fact the voice does not say.
- Dimension text sits on a small dark plate, follows the line's angle and is never upside down.
- Subtitles: a centred strip at the bottom with a soft shadow and no box; if the film is bilingual, the film's language on top. Hold every cue ≥ max(1.8 s, speech + 0.6 s); every label stays fully in frame for CJK ÷ 4.5 + other ÷ 15 + 1.5 s.

## 5. Motion quality

- 24 fps on ones; everything is smooth and deterministic.
- **Separation**: smooth start, fast middle, long settle (ease-in-out cubed); layers leave top first, 0.15–0.2 s apart; repeated parts (keys, screws) fan out in a wave ordered by distance from a corner.
- **Closing**: bottom first, quicker (about 1 s per layer), the last layer lands with a real mechanical response (a key travels its stroke and returns; nothing bounces like rubber unless it is rubber).
- While held apart, layers may float a millimetre or two with offset phases; during macro shots they hold perfectly still.
- Labels draw in (anchor dot, leader growing, text sliding 10 px) and fade out before the parts move again.
- Never moves: the floor, the light rig's relation to the camera, the label column's x position.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Orbit while layers separate | the whole, its order of assembly | a reveal; a structure overview |
| Grazing macro dolly | touch, material, finish | an opening; a texture |
| Dive between layers | being inside | a hidden component; how it works |
| Slow push on one still part | the part that matters | a chip, a sensor, a seal |
| Rise through the stack | one subsystem to the next | a transition between stops |
| Fast pull back | return, synthesis | a closing; a before/after |
| High three-quarter drift | scale and precision | sizes, pitch, thickness |

- At key moments the subject fills at least a third of the frame height. Labels live in a column on the free side (shift the projection with a view offset rather than moving the object), subtitles in the bottom 12 %.
- Transitions are camera moves through the object itself. No cuts to black, no slide transitions, no split screens.
- The camera path is keyed in the product's own coordinates and interpolated without overshoot (monotone cubic), so a held macro really holds.

## 7. Sound palette

- Instruments: tuned mallets (marimba, vibraphone, glockenspiel, glass), a round bass, a short synthetic kick and small dry percussion. Precise and dry outside the object; sustained and airy inside it.
- Foley is the material: hollow plastic clacks for keycaps or housings, a switch click with a low thock, dry taps for boards, inharmonic rings for small machined metal, a soft thud for the enclosure, airy swooshes for layers lifting and for camera dives, a fine pen hiss when a dimension line draws, a tiny tick per label.
- Every separation and every landing has its sound, panned to where the part is.
- Silence: at least two near-silences (room tone only) before the big separations or the turn back; the first sound after each is the most important hit around it.
- Mix: voice clearly on top (music about 10 dB under it while it speaks), music bus ducked, sub-bass kept lean (20–60 Hz well under the full band), loudness −14 LUFS.
- Voice: calm, close, unhurried, short sentences; numbers spoken as words, written as digits.

## 8. Native moves

- **The wave lift.** Repeated parts rise in a wave across the object. *Fits content like:* battery cells; solar tiles; the drawers of a modular shelf.
- **Inside the gap.** The camera enters the space between two lifted layers to see a hidden face. *Fits content like:* the back of a logic board; the inside of a drone arm; the underside of a sensor module.
- **The leader that lands on the part.** A macro label whose line ends on the component. *Fits content like:* a pressure sensor in a shoe; a gasket in a waterproof case; a motor driver.
- **Dimensions drawn on the thing.** After closing, the real outline gets dimension lines in perspective. *Fits content like:* the thickness of a laptop lid; the footprint of a router; the bore of a valve.
- **One real motion.** A part performs its true mechanical motion once (a press, a hinge, a latch). *Fits content like:* a camera shutter; a buckle; a folding hinge.
- **Lights on inside.** Emitters inside the product switch on while it is apart. *Fits content like:* status LEDs; a backlit display; an indicator ring.

## 9. Pitfalls of the medium

- **Invented numbers.** A size that no file gives. Fix: measure it from the CAD and say "measured" in the facts file, or leave it out.
- **Mixed-up revisions.** Plates, cases and boards from different versions of a project. Fix: check hole positions and stack heights across the files (they must coincide), and pin the commit.
- **Panelised boards.** Layout files may hold a panel with breakaway tabs. Fix: take the outline from a plate or case of the same revision, or flood-fill from an interior point.
- **Zero-length edges.** Duplicate outline points give zero normals → NaN → black squares after bloom. Fix: clean outlines, repair zero normals, scan frames for one-frame black tiles.
- **Overshooting camera splines.** Catmull-Rom over unevenly spaced keys flies past a macro stop. Fix: monotone interpolation per component.
- **Labels too short.** Macro stops last about three seconds. Fix: one fact per label, opened before the camera settles; check with `readcheck`.
- **Over-bright light sweeps.** Area lights blow plastics to white. Fix: sweeps at a fraction of the key, bloom threshold above the brightest diffuse surface.
- **Brand marks on parts.** Chip tops and connector shells carry trademarks. Fix: plain package tops; drop logo footprints unless the product is the user's own.
- **Crushed blacks.** Black plastics against a black ground disappear. Fix: lift them to a dark grey and let the rim light separate them.

## 10. Engine

All in `demo/src/` (three.js r170, the library's `core/three/post.js` and `core/lib.js`):

- `parts.js`: `keycapGeometry(w, d, h)` (lofted shell with a spherical dish and a stem), `switchGeometries()`, `loft(rings)`, `shapeFrom(outline, holes, circles)` (KiCad outline to extrusion), `inset`, `hexSpacer`, `screwGeometry`.
- `pcbtex.js`: `paintPCB(data, side, outline, box, ppm)` paints colour, roughness/metalness and bump maps from extracted layout data.
- `comps.js`: `buildBackParts(data, group, y, materials)` places package bodies at footprint positions and returns anchors.
- `overlay.js`: anchored labels (`label`), perspective dimension lines (`dimension`), subtitles, title card, readcheck texts, subtitle width check.
- `main.js`: layers, explode and gap functions, the camera keys (orbit or eye/target, monotone), lights, `window.EV` for the mixer.
- `tools/extract_pcb.py`, `kicad_geom.py`, `sexp.py`: read any `.kicad_pcb` (outlines, tracks, zones, pads, silkscreen, footprints; plain Python). `tools/step2mesh.mjs`: STEP to mesh.

**Extra packages and packs**, beyond `setup.sh deps [voice] [music]`: `occt-import-js` (npm, LGPL-2.1, not in the library's package.json) to triangulate STEP files, and the studio HDRI (`sh tools/fetch.sh hdri`). Install the npm package yourself into a private `node_modules` in the project folder (as `tools/fetch_cad.sh` does in a temp folder), never into `$LIB`.

Minimal example, not in the demo: read a plate file with `extract_pcb.py`, extrude `shapeFrom(outline, cutouts)` 1.5 mm as aluminium (`metalness: 1, roughness: .35`) and orbit it with three `CAM` keys.

## 11. Variation space

Decided per film: which product and revision, which layers to separate and in what order, how many stops inside and which parts deserve them, the camera route, whether to open from the whole or from a detail, the product's palette and the accent, the voice.

- **Three structures**: one orbit with two stops; a "how it works" path following a signal or flow through the layers; two revisions taken apart side by side, each held still before a difference is named.
- **Three openings**: a part performing its real motion in macro; the closed product turning in silence on the seamless; a single component floating alone before the rest of the product assembles around it.
- **Three endings**: closed with its dimensions drawn on it; closing into a top view that becomes a technical drawing; apart one last time, frozen, every part labelled like a printable sheet.

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: microscope -->

# Microscope Story — Style Prompt

> Real, licence-clean microscopy of a real specimen, seen as it is, and one continuous change of scale that carries the viewer from the glass slide in the hand to a single cell. Focus breathes when the magnification changes, a focal plane sweeps when the camera lands, and every scale bar, field of view and reading comes from the image's own metadata.
> References (grammar only): Charles and Ray Eames' *Powers of Ten* (one continuous change of scale with a readout riding along); premium microscope launch films (dark bench, glass catching light, restrained marks, clean instrument sound); digital-pathology viewers' instruments (scale bar, field of view, magnification). Copy none of their layouts, interfaces, typefaces or music; never name them in the film.

## 1. Essence, and what it is not

- **The specimen is a photograph**: a real micrograph or whole-slide scan of the actual sample, CC0, public domain or CC BY. Nothing on the specimen is drawn, retouched or generated. A whole-slide image (WSI) is the ideal source: one sample, one registered pyramid from millimetres to microns, with the pixel size in its metadata.
- **Scale is the camera**: one log-space dive (and, when the story wants it, the climb back) through nested plates of the same sample. The scale bar shortens and jumps in a 1-2-5 sequence, the field-of-view readout rolls, the magnification steps.
- **Focus has a grammar**: a rack-in from soft at the start, a short breath (blur + a hint of field change) each time the magnification changes, a focal-plane sweep across the frame when the camera lands.
- **Readings are measured**: every number is computed from the file (pixel size × pixels) and the screen says how it was measured. Describe what was measured; never diagnose. Keep a `FACTS.md` in the project folder (claim, source URL, quoted wording, or the measurement method) and deliver it with the film.
- **One reading per screen**, in the single accent colour.

Not Satellite Briefing (no grey grade; the stain keeps its colour), not Sci-fi HUD (no glowing wireframes or crosshairs), not Data Storytelling (no chart paper), not a keynote (no slides or header bars).

## 2. Materials & rendering

- **Plates**: the WSI pyramid levels as plates in one world frame (level-0 pixels), the coarse levels whole and alpha-feathered at the scan edge, the fine levels as crops around where the camera lands. Each frame draws the finest plate that is downsampled no more than ~1.45×, and blends the next level in between 2.2× and 1.45×: no seams and no visible upsampling, because every level is the same sample, already registered.
- **The naked-eye plate**: the scanner's own photo of the whole slide (many WSI files carry one), registered through the scan's area-of-interest metadata and checked against the tissue's centroid. Cut the glass out of the scanner tray, remove the line-sensor streaks, and fill any manufacturer's printed logo with the surrounding frosted glass. Below ~30 mm of field the photo would be upsampled: let the cover glass become clean glass (its dust leaves the focal plane).
- **One grade for every plate**: glass normalised to a warm white, a little density and chroma in the stain, nothing else. No false colour, no film emulation.
- **The bench**: graphite under a slow pool of light; a soft shadow under the slide.
- **Focus**: screen-space Gaussian blur on a frame rendered with a margin (so edges never go dark); the focal sweep is a tilted sharp front crossing a softened frame. A light illumination vignette, nothing more.
- **Marks** in screen space but anchored to the specimen through one world → screen function: hairlines 1.5–2.5 px with a dark or light halo, circles drawn on as arcs with cardinal ticks, dimension lines with end ticks, leader lines with one elbow. Counted pixels are shown as a mask revealed behind a scan front, then kept as a faint trace.
- **Frosted panels** (dark translucent glass over a blurred copy of the frame) for readings, instruments, subtitles and the credit: white type reads on glass and stain alike, nothing switches colour mid-shot.

## 3. Colour logic

- Glass: warm paper white. Bench: graphite. The stain is evidence and keeps its true colour (e.g. trichrome red and blue, H&E pink and purple).
- One accent, cool and away from the stain's hues (mint against red and blue; amber against a green or purple stain), only for the measured reading and the counted pixels.
- Ink on glass is near-black; type on stain sits on a frosted panel in warm white.


<!-- END STYLE PAGE -->
