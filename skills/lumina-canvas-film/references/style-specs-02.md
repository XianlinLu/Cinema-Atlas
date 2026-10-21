# Complete style specifications 02


<!-- STYLE: briefing-board -->

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

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: lidar-survey -->

# LiDAR Survey — Style Prompt

> Real airborne laser points of a real place, floating in the dark as a measured cloud; a scan line or a cutting plane passes through them and the points condense into a solid, raking-lit surface, which is then measured with hairline instruments. One designed camera move carries the whole film: the cloud is something you fly through, not a picture you look at.
> References (grammar only): survey and archaeology lidar visualisations (colour as height, the canopy removed); architectural section drawings (a cut, dimensioned); museum film cadence (one held reading per screen). Copy none of their layouts, ramps, typefaces or music, and never name them in the film.

## 1. Essence, and what it is not

- **The cloud is the data**: every point is a real return at its measured position; points appear, glow, lift away or give way to a surface, but are never moved into a shape.
- **Points become a surface**: a front (scan line, cutting plane) behind which the cloud condenses into a solid model of the same place.
- **Classification is a lever**: ground, vegetation, buildings, water are layers to peel, isolate and recolour.
- **Measurement in hairlines**: one reading at a time, in the accent, attached to what it measures; numbers from the points or an official source.
- **Dark, quiet, exact**: near-black ground, restrained colour, no glow except at the front.

Not Sci-fi Hologram HUD (no invented interface: the points are real, sparse where the survey was), not Satellite Briefing (photographs from above; here a 3D cloud flown through), not Blueprint, not Low-poly Isometric, not Glass Product Render.

## 2. Materials & rendering

- **Points**: GL points sized in world units (0.12–0.3 m), floor of one output pixel, soft discs, opaque and depth-tested (additive only for a ghost layer); colour from height or class, value from intensity; distance fog.
- **Quantise for the browser**: uint16 positions (2 cm / 1 cm) plus a byte each for height above ground, class, intensity, seed.
- **Height above ground** for every return (minus a ground model triangulated from class-2 returns) drives the colour ramp, the cutting plane and the ruler.
- **The solid surface**: a 0.5–1 m mesh of the ground or surface model, smooth normals, baked short-radius AO, a low raking sun (20–35°), faint contours, crests lightened. Display exaggeration of micro relief (×2–3) only with an on-screen note; measure on undistorted data.
- **The front**: one world-space plane (one uniform) shared by the point and surface shaders; points ahead of it brighten, a thin seam glows behind it and the surface fills in over tens of metres.
- **The cutting plane** (by height above ground): returns above it lift away and fade, a ring glows where it meets the trees, a ruler on the frame edge tracks it.
- **Marks on the surface** (traced features, section lines) are a distance field in the surface shader, kept hairline with `fwidth`; readings, leaders and charts are a 2D overlay through the same world → screen function.
- **A survey window**: outside the measured area the cloud stays as dim points instead of ending in black.
- **Post**: 2× render, high-threshold bloom (only fronts and seams), vignette; no grain (points are already fine detail; encode at a higher CRF).

## 3. Colour logic

- Background near-black with a cold tint; never pure black, never a gradient sky.
- Points: one ramp by height or class, desaturated (deep green-teal → pale; or grey → white); intensity modulates value, not hue. No rainbow elevation ramps.
- The front and seams: one cool near-white; it is light, not a colour.
- The solid surface: warm neutral (stone, clay, plaster), lit; its colour never competes with the accent.
- One accent (amber) reserved for what was found and measured: traced features, the reading, the section line. A second, cooler hue only in a comparison chart.

Example (our demo): background #05080A, canopy #1F3F35 → #5C9A7A → #E2F3DC, ground returns #C8B38C, surface #BDB5A6, front #D4FFF0, accent #FFB347, chart green #83C495.

## 4. Type & subtitles

- **Roles**: light condensed numerals for readings (110–130 px, e.g. Barlow Condensed 300); a monospace for instruments, coordinates, counts and source lines (19–22 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–36 px, e.g. Noto Sans SC 500). OFL, self-hosted, CJK subset to the characters used.
- **Instruments** in one corner: place, coordinates, area, data source, point count, any exaggeration; they change only when the medium does.
- **Readings** in the right third beside what they measure: label, number, source/method line; a leader when the feature is in frame; a rolling counter reports its landing value.
- **Subtitles**: a transcript strip bottom-left (2 px rule, plate fading right), one line per language measured with the real font, split rather than wrapped; if bilingual, the film's language on top.
- Nothing below 19 px at 1080p. Hold subtitles ≥ max(1.8 s, speech + 0.6 s); labels ≥ characters ÷ 4.5 + 1.5 s (CJK), letters ÷ 15 + 1.5 s (Latin).

## 5. Motion quality

- On ones, 24 fps; the camera never stops; keys as a C1 spline in target / distance / heading / pitch (no `lookAt` from nadir).
- The front moves on an ease, slowest where the subject is; a cutting plane steps on the beat (eased steps, short holds) so the layers read.
- Points appear behind a front or by height, never by random fade-in across the whole frame.
- Readings land with a small pop; traced features light up along their length in order.
- Never moves: the points relative to each other (no wobble, no noise displacement), the instruments' positions.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Locked nadir with slow push | "this is what a photo shows" | a claim to test; a before; an ending that returns to the map |
| Crane down with tilt to oblique | entering the data; the place has height | the switch from picture to cloud |
| Low oblique close to the cloud (10–20° pitch, 90–150 m) | volume; things standing up | canopy, buildings, a facade, a cliff |
| Slow orbit | studying, the plane doing the work | a peel; a scan; a held reading |
| Rising pull-back | scale reveal of what was found | a network, a site plan, a corridor |
| Lateral track | travelling a feature | a wall, a road, a pipeline, a coast |
| Push to a section | the detail that proves it | a cross-section, a clearance, a height |

Subject ≥ a third of the frame height at key moments; readings right third; instruments in a corner; nothing in the subtitle strip. Transitions are fronts and planes, never crossfades or hard cuts inside the cloud.

## 7. Sound palette

- **Instrument sounds**: FM pings, fine crackle as points arrive, noise sweeps tied to a front, ticks that divide (8ths → 16ths → 32nds) to accelerate, a descending pitched blip per peeled layer, a ratchet while a counter rolls, a ping when a reading lands.
- **Weight and synthesis**: timpani, bass drum, gran cassa for condensations and cuts, a reversed swell into the main impact; low-passed detuned-saw pads; a pulse bass with audible 2nd/3rd harmonics.
- **Dry and wet**: one option is electronics while the subject is still points, and a single organic, wooden or bowed timbre (marimba, bowed vibraphone) for the found features once the surface exists.
- **Beds**: the place's own ambience (wind in leaves, water, traffic) at the start and the end as J- and L-cuts; a thin air bed in between.
- **Silence**: a near silence (air only) before the main reveal; the first sound after it is the impact.
- **Mix**: voice ~10 dB over the music and ducking it; impacts outside the bus compressor; −14 LUFS, true peak ≤ −1.2 dBTP. Voice: a calm, plain narrator, short declarative lines.

## 8. Native moves

- **Photo to points.** A scan line crosses an aerial photo; behind it the place is points. *Fits content like:* a site visit before a design; what the satellite misses; a quarry's real volume.
- **The canopy peel.** A plane descends by height above ground, returns above it lift away layer by layer, a ruler tracks it. *Fits content like:* archaeology under forest; a hidden trail; flood channels; landslide scars.
- **Points condense.** A front turns the remaining points into a solid surface; found features light up in order. *Fits content like:* a building scan to a BIM shell; a cliff to a hazard model; a street to a vehicle clearance model.
- **The section.** A plane crosses one feature; the profile glows and a dimensioned chart of the real returns hangs beside it. *Fits content like:* a levee's height; a bridge's clearance; a road cut.
- **The window.** The measured area is a stage inside the unmeasured cloud. *Fits content like:* a parcel; a corridor; a site boundary.
- **The regrowth.** The removed layer returns as a ghost over what was found. *Fits content like:* an ending; a clearing before/after; a buried pipe under a street.

## 9. Pitfalls of the medium


<!-- END STYLE PAGE -->
