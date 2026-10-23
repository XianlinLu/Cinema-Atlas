# Complete style specifications 06


<!-- STYLE: news-package -->

- **Package left behind.** If the strap, source line or tags are drawn once on top of everything, a wipe changes the picture under yesterday's headline and the strap catches up 0.3–0.5 s later. Draw them per picture, inside the wipe's clip.
- **Leftover layout.** Removing subtitles or a crawl without moving the content down leaves a dead band above the strap.
- **Masked type peeking in.** A push-in title clipped by a mask shows its top edge before it moves if the travel distance doesn't clear the mask; start it fully below and don't draw at progress 0.
- **Words stronger than the source.** "Request for information" is not "investigation" or "penalty"; write "no fine, no case opened" or "for the first time" only if a source says so — and check the institution's own pages, which can contradict a report ("first requests" may have gone out months earlier).
- **Thresholds depend on the reference.** "Bear market" = −20 % from *which* high? Name the reference on the axis; from a different peak the claim can be false.
- **Attribute what only a report says.** When the official source does not name the companies, the graphic carries "据… 报道 / reported by …" and so does the voice.
- **A schematic posing as data.** Rolling counters on a close price flash values that never existed; set the close with a mask push instead. Don't label axes the data doesn't support.
- **Source lines under the strap.** Right-aligned mono 13 px: ≤ 36 characters.
- **Stamps over key words.** A stamp hit can mask the voice ("fines"); take the brass off the stamp and low-pass its clack.
- **Gold on paper** has too little contrast: use ink or dark olive.
- **Generated plates** carry stray corner marks: crop them in `prep.py`.
- **Short preview text.** Rundown rows are previews of the stories; `readcheck` flags them as short in the opening — they return in the recap and as straps, so accept the flag or leave them out of `TEXTS`.
- **Names in synthetic speech.** Spell brand names, model numbers and abbreviations the way they should sound in the TTS text (a respelling, a number written as a word, an abbreviation without dots) while the strap and subtitles keep the real spelling; when speech-to-text mishears an unusual name, put the expected transcript in the line's `asr` field instead of rewriting the line.

## 12. Variation space

Decide per film: the channel's name, plate and accent colour; how many items (one lead with a long package, three or four equal items, a five-item round-up); which full-frame graphics each item needs; where the long take goes; the anchor's voice.

- **Three structures:** rundown → items → rundown ticked (round-up); one lead package with a correspondent two-box and a short "also today" grid; a countdown of items (election-night, sports results).
- **Three openings:** sting → rundown; cold open on the biggest graphic, then the sting; sting straight into the first story with the rundown as a recap only.
- **Three endings:** rundown ticked → end card; a "coming up next week" teaser card; the last stamp freezing into the end card.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: satellite-briefing -->

# Satellite Briefing — Style Prompt

> Real satellite imagery of a real place, graded down to an analyst's grey, with thin white measurement lines drawn on the ground: a lock-on reticle, outlines, a range line, one reading. One continuous zoom built from stacked imagery plates carries the viewer from orbit to the ground and back, and time can run inside one locked frame.
> References (grammar only): open-source investigation films that annotate satellite pictures (thin lines on imagery, one claim per screen, measuring as the plot); the Eameses' *Powers of Ten* (one continuous change of scale with a readout); NASA Earth Observatory's *World of Change* (one place, time running). Copy none of their layouts, typefaces, icons or music; never name them in the film.

## 1. Essence, and what it is not

- **The ground is a photograph**: real, licence-clean, georeferenced satellite or aerial imagery of the actual place. Nothing on the ground is drawn, stylised or generated.
- **Two layers, two truths**: the imagery is what the satellite saw; the hairlines are what the analyst measured. Marks are thin, white, sparse, and sit on real coordinates.
- **The grade moves with the story**: orbit in true colour, the analysis layer in grey, colour back only where the story turns.
- **Scale is the camera**: one zoom from orbit to the ground built from nested plates, with an altitude readout and a scale bar from the same camera.
- **One finding per screen**, in the single accent colour.

Not Data Storytelling (a chart on paper), not Sci-fi Hologram HUD (no glowing wireframes or invented chrome), not Blueprint, not Isometric Infographic (real nadir or oblique views, no diorama), not a keynote (no slides, header bars or chapter numbers).

## 2. Materials & rendering

- **Plates**: georeferenced rasters with a lon/lat box, sampled in a shader where the camera ray hits the ground, nested by resolution (world → region → detail) with feathered edges so finer plates dissolve in as the camera descends.
- **Globe**: ray–sphere from a perspective camera, a thin atmosphere rim, limb shading at orbit only; compute |C|² − R² in double precision (float32 fails below a few tens of km).
- **Time**: dated plates share one grid. A soft scan front (a satellite pass, never a hairline) swaps them: north → south forward, south → north for a rewind. Growth can run outward from the old edge, ordered by a distance map.
- **The analyst's grade** (one uniform from colour to grey): luminance with local contrast and clarity, a shoulder so salt, snow and cloud stay below white, toned blue-black → cool silver up to ~65 % grey, a fifth of the chroma. White belongs to the marks.
- **Marks**: a 2D overlay through the same world → screen function: hairlines 1.2–2.6 px with a dark halo, dashes for history and claims, brackets, ticks, leader lines. Lines draw on; outlines print behind the scan.
- **Screen space only for instruments** (altitude, scale bar, imagery credit) and the transcript strip. Everything else is anchored to the ground.
- **The claim layer** is a printed map drawn in the shader from a distance field of the old outline: paper grain a few pixels wide at any zoom, halftone ink, coast and waterlines, graticule, the serif name.
- **Post**: light grain in ffmpeg, a vignette, directional blur only on whip pans.

## 3. Colour logic

- Neutral ground: grey, roughly 3–65 % in value. White means *measured*.
- One accent (warm, e.g. amber) for the single reading on screen, never decoration.
- A second hue may mark the **claim** the imagery tests (a map, a plan, a promise): flat, cartographic, never used for anything measured.
- True colour is evidence: at orbit, and again only where the story turns (the field that greened, the water that returned).
- No false-colour ramps over the imagery.

Example (our demo): ground #070B0E → #A1A7A9, marks #F2F5F6, reading #FFBE55, map blue rgb(46, 112, 206).

## 4. Type & subtitles

- **Roles**: a light condensed grotesk for the reading (96–130 px, e.g. Barlow Condensed); a monospace for instruments and dates (20–34 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–42 px); a serif only for the claim layer and the title. OFL, self-hosted, CJK subset to the characters used.
- **Labels attach to the ground** with a leader line. The reading sits in the right third beside what it measures, label above, source note below ("Landsat, measured").
- **Subtitles are a transcript strip** at the bottom left: a 2 px white rule, a dark plate fading right, left-aligned, each line on one line (measure with the real font, `nowrap`; split a long sentence into two cues). If the film is bilingual, the film's language on top.
- Nothing below 20 px at 1080p, the imagery credit included.
- Hold subtitles ≥ max(1.8 s, speech + 0.6 s); a rolling counter reports its landing value; labels stay ≥ characters ÷ 4.5 + 1.5 s (CJK).

## 5. Motion quality

- The camera never stops: distance interpolates in log space, segments ease, holds keep a 2–5 % creep or a slow rotation. No frozen frame longer than a second.
- Marks arrive by being made: a line grows, an outline prints behind the scan, a counter rolls and lands with a small pop, a reticle snaps with overshoot.
- Time changes are scans, never dissolves; their spacing tells the speed, and the camera moves with them (accelerating as the steps shorten, braking on the last).
- Never moves: the ground under its annotations, the instrument positions.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Oblique orbit, limb in frame | scale, context, distance | an opening; a return; a title card |
| Dive (log zoom, tilt to nadir) | going to look for yourself | a reveal; checking a claim |
| Locked nadir frame, slow creep | evidence, comparison | time running in one place; a measurement |
| Push-in on a point | singling out | one town, one dam, one field |
| Track along a line | travelling a distance | measuring; a river, a road, a border |
| Whip pan with blur | a new subject at the same altitude | the counter-example; "meanwhile" |
| Climb back to orbit | consequence, perspective | an ending; a summary |

At key moments the subject fills a third of the frame height; reading right, subtitles bottom left, instruments in the corners. Transitions: scan-line swaps, a map layer switched off, zooming through plates, whip pans, the reticle opening into a title card. No crossfades between unrelated places, no hard cuts inside a zoom.

## 7. Sound palette

- **Telemetry**: FM pings (a lock-on ping worth bringing back), dry ticks on the grid that divide to accelerate, noise scans (rising for a rewind, falling forward), servo whines, a ratchet for a range line.
- **Weight**: timpani, bass drum, gran cassa, bowed cymbal, a tam-tam reversed when time runs backwards. Measurements land on a pitched hit.
- **Synthesis**: a pulse bass with audible 2nd and 3rd harmonics, detuned-saw pads under a low-pass, risers for dives.
- **Beds**: orbit hum, radio hiss, data chatter; the place's own ambience (wind, water, a far horn), sparingly, often as J- or L-cuts.
- **One option for the shape**: keep the palette dry (electronics, skins, metal) and let one wet timbre (glass, water, bowed metal) mark the turn.
- **Silence**: music and foley stop, a thin bed stays, impacts may decay into it; the first sound after it is the turn. A short suck-out (0.2–0.45 s, music and foley down ~25 dB) before the heaviest impacts makes them land.
- **Mix**: voice ~10 dB over music; the two or three designed impacts are the loudest moments (out of the bus compressor, with mid-range body, e.g. a low-brass stab); 20–60 Hz about 15 dB under the full band (high-pass ~40 Hz, impact weight at 60–120 Hz); −14 LUFS, true peak ≤ −1.2 dB. Voice: a calm analyst, short declarative lines.

## 8. Native moves

- **The map against the photograph.** The camera falls into the printed map of the claim; a scanner bar tears it away and the ground is underneath; the name outlives the page. *Fits content like:* a lake still on maps but gone; a cleared concession forest; a planned city never built.
- **Time rings in a locked frame.** Dated plates scan in one by one; each leaves its outline, the band lost between two rings flashes. *Fits content like:* a glacier's retreat; a city's sprawl; a fire scar season after season.
- **The range line.** Mark the destination, grow a ticked line from A to B, chase the tip while the reading counts up, land on the number, pull back to show the whole distance. *Fits content like:* how far a shore moved; a village to its well; a camp to the border.
- **The dive and the climb.** One zoom from orbit to the ground, or back. *Fits content like:* locating anything; a scale reveal; an ending that returns one place to the planet.
- **Colour returns where the story turns.** Only the subject regains true colour inside the grey. *Fits content like:* an irrigated field; a refilled reservoir; a regrown forest.
- **The reticle becomes the frame**: the lock-on brackets open out to frame a title card or the last reading.

## 9. Pitfalls of the medium

- **Licences**: not usable: Google Earth/Maps, Bing, Esri World Imagery, Mapbox Satellite, Planet, Maxar, news photos, AI-generated imagery. EOX Sentinel-2 cloudless is CC BY 4.0 only for 2016 (2018 onward is NC). Raw Copernicus Sentinel data need "Contains modified Copernicus Sentinel data [year]"; check the user's rules. Public domain or free with credit: USGS Landsat (1972 on, worldwide), USGS NAIP (US, ~1 m), NASA Blue Marble, MODIS, VIIRS. Burn a readable credit into the picture and list every asset in `CREDITS`.
- **Finding imagery for a new place**: search by bounding box and date in the Planetary Computer STAC (Landsat C2, Sentinel-2 L2A; no account) or USGS EarthExplorer; MODIS/VIIRS and Blue Marble from NASA GIBS; outlines from Natural Earth. Log every request. OSM (ODbL), CC BY-SA and "no known restrictions" are not CC0: name the terms and ask the user first. Ask for the user's own surveys or GIS layers when the place is theirs. Never fill a gap with generated imagery presented as evidence.
- **Seams**: paths imaged on other days disagree. One date per path, each scene gain-matched on stable land, feathered overlaps, holes filled from the same year only.
- **Old sensors**: Landsat MSS (to 1992) has no blue or SWIR and drops scan lines: nearest-neighbour resampling, near-zero rows as nodata filled from same-year scenes, scan-angle streaks cleaned on land only. Inspect every year at full contrast.
- **Plumes and haze** cross water as bright diagonal bands: swap the scene for another date of the same year rather than painting it out.
- **Edges**: resampling against nodata darkens scene rims (erode the mask); drop contour pieces along a plate border. Real straight edges (dikes, polders) can read as seams: frame them out or label them.
- **Grey mush at close range**: raise local contrast for that altitude only and dim outside the measured corridor.
- **Water and cloud**: MNDWI where shortwave infrared exists, only the basin you measure; clouds read as features in grey, so use the dry season.
- **Facts**: keep a FACTS.md in the project folder (claim, source URL, quoted wording, or the measurement method with scene IDs and dates) and deliver it with the film. Measure on the date you show.

## 10. Engine

- `demo/engine.js`: `makeCamera({lat, lon, d, tilt, heading, sx, sy})`, `project()` / `unproject()`, the WebGL2 plate shader (nested plates, time scans, growth map, analyst grade, printed-map layer, whip blur).
- `demo/overlay.js`: hairlines, brackets, `readout`, the measured single-line `subtitle` strip, `text` with a registry for `window.TEXTS`.
- `demo/tools/`: `fetch_landsat.py` (STAC, one date per path, same-year gap fill), `plates.py` (normalisation, streak cleaning, water masks, areas), `vectors.py` (shorelines, distances), `mapfield.py` (the printed map), `growth.py`.
- **Extra packages and packs**: none beyond `setup.sh deps voice` and the sample packs the score uses (`sh tools/fetch.sh instruments <lib>` for vsco2ce, vcsl, freepats in the demo). Imagery uses only the standard library, numpy, SciPy, Pillow (no GDAL); allow 3–4 GB for cached scenes. Anything more (rasterio, pyproj) goes in a private venv in the project folder, not `$LIB/.venv`.

## 11. Variation space

The agent decides the place or places, whether there is a claim layer, which dates, the structure, the camera path, the accent hue and where colour comes back.

- **Structures**: a locked time-lapse of one place ending in a push-in; a river followed from source to mouth with a reading at each stop; two places compared at one scale with whip pans.
- **Openings**: a ground-level detail that climbs to reveal its scale; a black frame a scan line paints in; an oblique orbit with a searching reticle.
- **Endings**: the climb back to orbit; a last measurement that lands and holds in silence; the claim layer redrawn to match the ground.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: briefing-board -->

# Engineering Briefing Board — Style Prompt

> One real whiteboard wall, filmed: window light on enamel, ghosts of erased marker, frame and tray. Cut-out photographs of real things land on it with weight; tags, magnets, a ruler and stamps are pinned to it; marker ink draws itself in three colours with fixed meanings. The camera rides the lines from fact to fact and only at the end pulls back to show the whole briefing.
> References (grammar only): explainers filmed on a map wall; the long pull-back over a wall covered in work; drafting conventions (plan above elevation, dimension lines, hatching). Never copy them or name them in the film.

## 1. Essence, and what it is not

1. **A physical board in a room**: enamel, window falloff, a sliding reflection, ghosts of earlier work, frame and tray.
2. **Real things on it**: cut-out photographs of the real objects, a few millimetres off the board, shadowed by one window, parallaxing. They are evidence: never a generated image presented as a real object.
3. **Ink that means something**: graphite for names and rules, blue for water and measurement, red only for the decision; rejected ideas erased to ghosts.
4. **One continuous wall**: no pages; the camera travels along lines, projections and leaders.
5. **The whole wall, once**: every shot is a crop of the final briefing, seen whole only in the last pull-back, as a poster.

Not **Whiteboard Explainer** (a hand drawing line art on a flat page): the board is a filmed object, subjects are photographs. Not **Data Storytelling**: comparisons are dimension lines in real units beside real objects. Not a keynote: no headers, centred bullets, page turns.

## 2. Materials & rendering

- **Board (z 0)**: procedural enamel, wiped ghost strokes, smudges, a window falloff, a sliding diagonal reflection; the frame shadows a warm grey wall.
- **Ink (multiply)**: flat colour at about 90 %, lighter core, round caps, a wet-tip glint on the stroke being drawn. Lettering: a marker font revealed glyph by glyph with seeded tilt and baseline jitter. Erasing leaves a blurred ghost (about 7 %).
- **Prints (z ≈ 6–14)**: photographs cut out at full resolution (a matting model, or a hand polygon / mask), clean edges, one shared grade (lower saturation, a touch warmer, lifted blacks). Thin structure (cables, wires, masts, railings) is measured in the photo and redrawn as clean lines in one colour. Shadow = blurred silhouette along one light vector, softer the higher the object. **No frame upsamples a photo**: ≥ 1 source px per screen px at its largest, measured; cap the zoom or find a bigger source.
- **Secondary layer** (only where the camera never goes before the end): the photos as pinned prints, a source card, sums on sticky notes, a small sketch. Texture and proof for the final wall, lighter than the main line.
- **Props (z ≈ 8–26)**: magnetic tags, magnets, a steel ruler, printed cards, a pitted stamp impression; the tray (z 70) nearest the lens.
- **Camera**: parallax by height, sub-frame motion blur (180° shutter), light grain. Only subtitles are screen-space.

## 3. Colour logic

- Ground: the enamel and its light falloff; the wall around is neutral warm grey.
- Ink: graphite = names, rules, facts; blue = water and measurement (dimensions, projection lines, measured numbers); red = the decision (a rejection, the key word of a verdict, the one mark to notice); grey for drafting only (extension lines, hatching).
- Red is rare: two or three red marks per frame at most, never on a red object. Full colour belongs to the photographs; props stay neutral; a red magnet is a verdict.

## 4. Type & subtitles

- **Marker lettering**: a single-weight marker face covering every script the film uses (ours: LXGW Marker Gothic, OFL, subset — re-run when words change). Content 100–160 board px; a verdict 230–400.
- **Printed labels** (tags, cards, stamps): a sturdy sans; credit lines in a monospace. A tag holds one to three words.
- **Subtitles**: a frosted acrylic strip at the bottom centre with a blue marker tick. If the film is bilingual, the film's language sits on top. **One line per language**: `nowrap`, measured in the page against a 1,500 px safe width; a long line becomes two cues. Key content stays above the strip (bottom 15 %).
- **Reading time**: subtitles ≥ max(1.8 s, speech + 0.6 s); board text stays fully in frame for CJK ÷ 4.5 + other ÷ 15 + 1.5 s from when it appears. In the final wall, text meant to be read is ≥ 20 px on screen.

## 5. Motion quality

- 24 fps on ones; nothing is stepped.
- Camera: overlapping eased moves, velocity ∝ u^a (1−u)^b (a, b ≈ 1.5–4), so speed and acceleration never jump; b > a gives inertia. A hand-held breath (≤ 3 px) underneath; shake only on an impact.
- Weight: prints are lowered from the camera side, land, bounce and settle as the shadow tightens; magnets clack on to pin them; tags swing; removed magnets pop toward the lens; struck things jolt and spring back. The camera may meet a landing close, briefly, on the object's most telling detail, then pulls out.
- Blurred in motion, sharp where words are read. Every 1–2 beats something lands, draws or swings; only silences and judgement holds go still.
- Ink draws at the speed of a hand; dimension lines land with an arrowhead tap.
- Never: dissolves, scale-pops on text, bouncy UI easing, text fading in by itself.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Ride a line (with the pen or a dimension) | measuring; "how far does it go?" | lengths compared; a route; a timeline |
| Tilt along projection lines | the same quantity in another view | plan → elevation; a total → its parts |
| Slow push-in, slight Dutch tilt | tension, an approaching problem | a collision; a deadline; an overrun |
| Pull back and sideways | stepping back to state a rule | a constraint; a turn in the argument |
| Whip with the line, overshoot, settle | a result that exceeds | a record; an outlier |
| Rise along a leader line | from evidence to verdict | a conclusion; a recommendation |
| Staircase framing (each new item with the previous result) | comparison in sequence | rankings; tests; options |
| Judgement frame: the whole item, the limit and the verdict, held ≥ 2.5 s | a test the viewer can check | pass / fail against a threshold; a budget against a cap |
| Long pull-back to the whole wall | scale; everything at once | the end of an argument; a summary |

Framing: off-centre, cropped, close. The first frame holds a readable subject; the first strong action hits within 0.5 s. Items tested against a limit each get a judgement frame (wider each time if they grow); the verdict lands after the camera settles. Before the reveal: ≤ about 60 % of the board's width, never both side edges, never the reveal's zone. Transitions are moves; no cuts, fades or zoom-to-fit.

## 7. Sound palette

- Room: an air-conditioning bed and traffic through the window, about 20 dB under the voice — audible, not a hiss; silences keep only this.
- Foley: felt-tip squeaks scaled to stroke length, nib taps, magnet clacks (a pitch per magnet in a row), suction pops, print landings (board thump, paper slap), a ruler's ring, eraser felt, a stamp's thud.
- The subject's own sound arrives early as a J-cut; the first sound after a silence is an impact or the subject's sound.
- Music: a small rhythmic ensemble, walking to brisk — bass, a light kit, wooden percussion, low brass stabs for verdicts (or mallets); no piano-and-strings pad. Landings, stamps and arrows sit on the beat. Voice calm, briefing-room confident, about 8–10 dB over the music; −14 LUFS.

## 8. Native moves

- **The whole-wall reveal.** Design the wall as a poster first (hierarchy, reading path, filling the frame), then plan every shot as a crop of it; keep one zone (secondary layer, verdict, title card) for the reveal alone. *Fits:* a product roadmap; a household budget.
- **The subject passes through the answer.** The real thing moves through the chosen solution, its sound first. *Fits:* a parcel along the chosen route; a train over the new viaduct.
- **Ride the dimension line.** A quantity drawn as a real length to one scale; the camera rides the tip. *Fits:* battery ranges of four cars.
- **Projection lines.** Dashed lines carry an edge from one view to another so two drawings share a scale. *Fits:* a trail map above its elevation profile.
- **Magnets as countable things.** Units clack on in rhythm, pop off when a rule removes them. *Fits:* seats in a vote.
- **Erase to a ghost.** A rejected idea wiped but faintly visible. *Fits:* last year's plan under this year's.
- **The stamp.** A verdict lands with a thud and a jolt. *Fits:* passed / failed tests.
- **The physical answer.** A real prop laid down as the solution. *Fits:* one cable instead of five.
- **Leader to the verdict.** An arrow from the deciding number to the conclusion. *Fits:* the bottleneck in a process.

## 9. Pitfalls of the medium

- **Text glimpsed in passing** fails the reading time. Fix: words where the camera rests; frame each new item with the last result.
- **Only close-ups.** The viewer never sees the whole object against the limit. Fix: detail → judgement frame → hold → verdict → move on.
- **Photos that don't belong together.** Fix: one grade, one light vector, one viewpoint family.
- **Thin parts lost or stair-stepped** by the matte. Fix: key them against the clean background, redraw clean lines at the measured positions.
- **Upsampled photos** go soft in close-ups. Fix: full-resolution cuts, large sources, a per-frame check.
- **Lettering in photos** (signs, names, logos). Fix: paint out, cut, or choose another photo.
- **The wall seen too early** spends the ending; **a sparse or tiny final wall** wastes it. Fix: measure every frame's visible share; size the hierarchy for the poster; a quiet secondary layer, no empty middle.

## 10. Sources, facts, engine

- **Photos**: Wikimedia Commons (read each file page's licence and author), national libraries and archives (e.g. the Library of Congress: check each item's rights statement), agency media pages, Flickr Commons. Fine: CC0, public domain, CC BY (credit it). CC BY-SA, "no known restrictions" (≠ CC0) or other terms: name them to the user and ask first. For the user's own product, site or people, ask for their photos. No licensable photo of a real thing → draw it in marker as a sketch; never a generated image presented as the real object.
- **Facts**: keep a `FACTS.md` in the project folder (each claim on screen or in the voice, its source URL, the quoted wording, or the measurement method) and deliver it with the film. List every photo in `CREDITS` with source, author and licence.
- **Extra packages and packs** (beyond `setup.sh deps voice music`): `onnxruntime` and the BiRefNet-general matting model (MIT, ~970 MB: https://github.com/danielgatis/rembg/releases/download/v0.0.0/BiRefNet-general-epoch_244.onnx, path in `$BIREFNET_ONNX`) for cut-outs; `fonttools` only to subset CJK fonts offline. The agent installs them itself into a private venv in the project folder (`demo/kit/tools/kit_env.sh` does venv and model), never into `$LIB/.venv`. Without the model: cut with `prep_object.py --poly` (hand polygon) or `--mask` (a mask image).
- **Engine** (copy into the project): `demo/kit/board.js` (camera, prints, tags, magnets, ruler, cards, stamp, ink, erasing, `sceneTexts(t)`, `subCheck()`; fields in `demo/kit/README.md`), `demo/kit/batch.mjs` (stills), `demo/kit/tools/` (cut-outs, line redraws, lettering wipe, prints, fonts), checks in `demo/tools/` (`camcheck.mjs` visible share and judgement frames, `rescheck.mjs`, `subcheck.mjs`).

A minimal world (`node demo/kit/batch.mjs park.json`; `fetch_fonts.py park.json` first for new characters):

```json
{ "dur": 6, "t": 5.5, "board": { "w": 4000, "h": 2400 }, "hand": 0, "cam": { "x": 1500, "y": 1000, "z": 0.8, "moves": [] },
  "elements": [
    { "type": "tag", "text": "地下车库", "xy": [560, 800], "size": 60, "arrive": { "t": 0.2, "kind": "swing" } },
    { "type": "ink", "kind": "dim", "from": [700, 900], "to": [1300, 900], "color": "blue", "t": 0.6, "d": 0.6 },
    { "type": "ink", "kind": "write", "text": "120 米", "xy": [1360, 940], "size": 100, "color": "blue", "t": 1.2 },
    { "type": "stamp", "text": "首选", "xy": [1500, 700], "size": 110, "rot": -8, "t": 4.2 } ] }
```

## 11. Variation space

The agent decides per film: structure, which objects are photographed, plan vs elevation, the wall's reading path, opening, ending, camera path, pacing.

- **Three structures:** one measurement that keeps growing until it breaks a limit; a before/after where the erased first plan stays as a ghost under the second; a checklist stamped item by item as the camera moves down the wall.
- **Three openings:** a stamp on a finished drawing, then back to see why; one number written large, then the line that measures it; a photo dropped onto an empty corner.
- **Three endings:** the wall revealed with the answer circled; back to the opening mark, now corrected; the last tag flipped from a question to an answer, then the pull-back.


<!-- END STYLE PAGE -->
