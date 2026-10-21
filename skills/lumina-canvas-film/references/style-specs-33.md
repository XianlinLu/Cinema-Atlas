# Complete style specifications 33


<!-- STYLE: tilt-shift -->

- **Vantage**: always high. Oblique views at roughly 45–55° pitch from 100–200 m with a moderately long lens (~27–30° vertical FOV); straight top-down for the most "board game" look. Real tilt-shift is never shot from street level, except for a deliberate intimate moment: a true medium close-up at the actors' height, a blurred foreground object framing sharp actors who fill ~1/4–1/3 of the frame height (a long lens from high up keeps them as dots).
- **Blur band** (`demo/post.js`): physical depth of field mixed with a screen-space band. CoC in pixels = `mix(aper·(1/focus − 1/z), sign(dy)·amp·(max(0,|dy|−w)/0.5)^1.2, mix)`, clamped (~30 px). Put the band on the subject; when the subject moves, project it to screen every frame and slide the band there. Narrow the band for intimacy. Gather at output resolution after a 2× supersampled render, with many spiral taps and per-pixel rotation; far samples must not bleed onto nearer sharp ones.
- **Grade**: neutral tone mapping, strong saturation boost, soft added contrast, slightly warm highlights, a vignette. Lower saturation at night.
- **Light**: a hard sun with sharp shadows (a big shadow map fitted to each shot), a low hemisphere fill with warm ground bounce so shadows stay blue but not murky, a sky-gradient environment map for glass and paint. **Cheat the sun azimuth per shot**: each time-lapse clip is its own shot, so front-light the facades you see; one fixed sun leaves half a film backlit and grey.
- **Model-like detail** (what separates "filmed miniature" from "game CG"): facades with several window types, 1.6–3 m bays, dark reveals, world-space grime, sky-reflective glass and walls darkening toward the ground; roof clutter, awnings and signs; worn markings and stains; vehicles with dark glass, a soft contact shadow and brake lights; ambient occlusion over everything.
- **People** are small colour capsules, like model-railway figures. Actors seen up close get organic bodies with a soft sheen material and are made 20–30 % larger than real so they read.

## 3. Colour logic

- Saturated, sunny, "freshly painted model": a pale warm ground of buildings with a few candy accents, very saturated greens, dark ground surfaces so white markings and vehicles pop.
- Shadows stay blue and clean, never grey. Night and dawn are the only low-saturation states; dawn must read as early morning (a warm low fill from the sunrise side, few lit windows), not midnight.
- The subject you want found should be the one saturated thing in the sharp band, or move against the flow.
- Examples: a Mediterranean harbour (whitewash, cobalt shutters, terracotta, turquoise water); a snowy ski village (white, pine green, red gondolas, long blue shadows); a desert market (sand, saffron, indigo awnings, dusty olive).

## 4. Type & subtitles

- Subtitles belong to the world's own signage: a panel in the graphic language of the place's signs (road sign, platform board, harbour notice…), an open sign-revival font (Overpass, OFL, is a Highway-Gothic revival), sitting inside the lower blur band. Hold ≥ max(1.8 s, speech + 0.6 s).
- A **time-lapse clock** with a speed readout (e.g. `×24 TIME-LAPSE` / `×1 REAL TIME`, monospace) is the audience's speedometer for the native trick; use it whenever speed changes carry meaning.
- Titles live in the world: letters on a roof, a sign or a field, placed where nothing blocks them, lit or revealed on the beat.

## 5. Motion quality

- **Time-lapse stutter is the soul of the style.** In fast-forward the whole world (vehicles, people, lights, sun) updates at a low rate and holds each position for several frames (8 Hz = 3 frames at 24 fps); choose the rate so every jump lands on the musical grid. **The camera stays smooth on every frame.** Step at a middle rate while the speed is moderate; below about ×2 the stutter disappears and motion becomes silky, which makes a drop to real time hit hard.
- Systems run on simple simulations pre-computed per clip (car-following, signal cycles, crowds gathering and surging), with cycle offsets chosen so changes land on bar lines.
- Hero actors get art-directed timing (scripted paths fitted through beat times), never a hope that the sim hits a beat.
- Close-up acting: anticipation squash → stretch → land squash → settle; a failed attempt before success is the comedy engine.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| High oblique wide, very slow slide | a whole system at a glance | setting a place; routine; many small actors |
| Band follows one subject across a wide | "this one" | a single commuter; a delivery; a lost child |
| Rack of the band from one subject to another | attention changing hands | cause and effect; a handover; a comparison |
| Slow push on an intersection, station or yard | a system heating up | rush hour; a festival setting up; a queue |
| Straight top-down, slowly rotating | the world as a board or machine | patterns; logistics; choreography |
| Continuous dive from high to actor height with a speed ramp | the one small thing that matters | a twist; a joke; a meeting |
| Band narrowing to a sliver | intimacy | a confession; a reunion; one decision |
| Vertical rise with logarithmic height | scale, letting go | aftermath; a summary; a system becoming a pattern |
| Lateral track along a line (rail, river, road) | a process in order | a supply chain; a parade; a race |
| Locked frame across hours | time as the actor | a construction; a market day; tide |

Framing: stay high; the sharp band carries the subject; vehicles and people stay tiny except in a close-up. Transitions: cuts on the beat, speed ramps, dives and rises; avoid dissolves that reveal the fake lens.

## 7. Sound palette

- **Ensemble**: tuned percussion carries the style (marimba, glockenspiel, vibraphone, woodblocks, kalimba, celesta), pulse-based and minimalist (Reich grammar: phasing, voices added one at a time, pulsing chords), plus plucked strings or a small reed section. Not generic piano and strings.
- **Techniques, as options**: world events gate the notes of a fixed phrase skeleton (vehicles crossing a line, lights changing, crowds moving each trigger an instrument), with a base fill rate so the phrase stays audible; tuned horns or bells voiced as chords; a tape-stop (varispeed down, voices dropping out) into silence when time slows; single notes for single events in a rest; phasing two identical lines apart; a music-box version of the theme for the smallest scale.
- **Sound follows speed**: in time-lapse, music first with a faint granular "sped-up world" hiss, clacks and relay clicks. At real speed the world turns suddenly real: idling engines, distant traffic, birds, small voices, footsteps. On release, engines rev and wind rises.
- **Silence** is the moment real time arrives: cut the music, keep one or two real sounds.
- **Voice**: relaxed, few short lines, music ducked ~8 dB. Verify every line with whisper; write numbers as words and put digits in the `asr` field. Master to −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **The speed drop (×40 → ×1).** Time crashes to real speed on one detail. *Fits content like:* one worker finishing a shift; a child dropping an ice cream; a proposal on a crowded pier.
- **The band as pointer.** Slide or narrow the sharp strip to steer the eye. *Fits content like:* a courier through a market; a single wrong-way skier; one boat leaving port.
- **God's-eye system.** The place as a sequencer or machine. *Fits content like:* a port unloading ships; an airport's turnaround; a farm harvest.
- **Long-exposure light.** At dusk, lights leave trails that draw on the world. *Fits content like:* ferries crossing a bay; runners with headlamps; lanterns along a river.
- **The scale reveal.** Rise until the place becomes a pattern. *Fits content like:* a festival from setup to crowd; a school at recess; a city grid at night.
- **Cloud shadows sweeping.** Weather crossing the model. *Fits content like:* a season turning; a mood change; a news cycle.

## 9. Pitfalls of the medium

- Tall buildings plus shallow pitch hide the ground → low to mid-rise buildings, pitch 45°+.
- The subject hides in a canyon or behind a facade → route it on the camera side and let the band follow it.
- Instance caps silently drop actors → cull by distance from the camera (≈ 4× camera height) and raise the cap.
- Simulated vehicles stop short of lines (the jam gap) → subtract it where the story needs contact.
- Focus lags a frame → update actors before the camera.
- A top-down → oblique dive twists → rotate the top-down so its screen-up matches the target shot.
- A close-up from high up is too far → go low and close, small near plane for foreground objects.
- Clouds wash out a rise → unlit white, low opacity, nothing below the camera. Light pools read as bubbles → denser, larger, fainter pools.
- Scene backlit and grey → cheat the sun per shot. Dawn reads as midnight → warm low fill, fewer lit windows.

## 10. Engine

In `demo/`: `post.js` (tilt-shift DOF: band + physical, grade; `band.follow`), `city.js` (procedural town, facade shader, sign), `geo.js` (merged geometry), `sky.js` (clock → sun, sky, fog, env map), `traffic.js` (lanes, lights, IDM sim, fleet, trails, walkers), `train.js`, `ducks.js` (lathe-turned characters + hop choreography), `main.js` (cameras, stepping, crowds, HUD), `music/score.py` (sampled marimba, skeleton + event gating). A minimal new use: build a harbour from `geo.js` boxes, run boats as a one-lane `traffic.js` fleet on water, and point `band.follow` at one of them.

## 11. Variation space

You decide the place, the system, the tiny actor, the structure, the opening, the ending, the camera path, the speed curve and the palette within the colour logic. All far from our demo:

- Structures: **one day, dawn to night** (a single locked vantage, the sun and the shadows sweep, one shop's light the last to go out); **the relay** (the band hands attention from actor to actor across a whole place, each one passing something to the next); **before/after** (a construction site time-lapsed from empty lot to opening day, with one real-time moment per stage).
- Openings: **mid-bustle at full density** with the band already on one oddity; **a top-down pattern** that only slowly tilts into a place; **real time first**: one person at actor height, then the lens lifts and time speeds up.
- Endings: **a drop to real time that stays there** (no pull-back); **lights going out one by one** at night from high above; **the lens un-tilts**: the band widens to full sharpness and the model becomes a real place.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: lowpoly-island -->

# Low-poly Isometric Island — Style Prompt

> A tiny faceted world seen through an orthographic isometric lens: everything is a geometric block, and everything that appears arrives with a bounce and a note.
> References (grammar only): *Townscaper* (building is the performance; every piece lands with a springy bounce and a sound; pieces sprout small details by themselves); *Monument Valley* (isometric geometry, soft pastel palettes, gradient skies, calm pacing, lots of empty space). Never copy their grids, buildings, characters, UI or typography, and never name them on screen.

## 1. Essence, and what it is not

A miniature world built from **flat-shaded low-poly geometry** (hexagonal tile columns, box buildings with prism roofs, cone and icosahedron trees) floating in a faceted sea or void, watched by an **orthographic camera** at an isometric angle. No perspective and no horizon: distance dissolves into a **screen-space sky gradient**, so the world looks like a model suspended in colour. **Light, not texture, tells time**: every facet changes colour as the sun moves; in the dark only emissive blocks keep their colour.

Not a voxel game (no cubes-of-cubes, no pixel texture), not a tilt-shift photograph of a real place (no perspective, no photo detail), not a smooth-shaded 3D cartoon (no rounded normals, no subsurface).

## 2. Materials & rendering

- **Geometry** (world unit = one hex tile's circumradius): pointy-top hexagonal columns (`CylinderGeometry(r, r, h, 6)`), axial → world `x = √3(q + r/2)`, `z = 1.5 r`. Terrain height encodes material (sand low, grass, hills, rock highest). A thin separate top cap sits over a darker side colour; **sink the side column's top below the cap** or it z-fights. Leave a small gap between tiles so AO draws the seams.
- **Props** are primitive assemblies: boxes, prisms, low-segment cylinders and cones, icosahedra at detail 0, pinched boxes. Emissive parts (windows, lamps) get their own material per object so they can light individually.
- **Materials**: `MeshStandardMaterial({ flatShading: true, roughness ≈ .9 })`, **no textures**. Jitter each tile's lightness a few percent so the ground isn't a spreadsheet.
- **Water** (if any): a dense non-indexed plane displaced by summed sines in the shader, flat-shaded so each triangle glints on its own (not too low a roughness or facets flash white); a coarse plane below for zoom-outs; a **shallow map** redrawn per frame where land exists, mixing deep → shallow colour with a faint foam rim; a thin transparent ring at each tile's water line for surf.
- **Sky without a horizon**: in post, linearise the orthographic depth and blend distant pixels into a vertical screen gradient; set haze start/end as fractions of frustum height × cot(elevation) so the horizon band stays in the top third at any zoom. Stars (hash grid, twinkle) only where haze is thick.
- **Post**: MSAA + depth → **GTAO** (mandatory: it draws the seams between tiles and under roofs) → sky/haze composite → a very light tilt-shift at the frame edges → bloom (stronger at night) → pastel grade → Neutral tone mapping. Supersample 2×.
- **Light beams** (searchlight, projector, torch): a camera-facing ribbon with a Gaussian profile, bright at the root and fading with distance, plus a wider faint halo copy; light the surface under it in its own shader.

## 3. Colour logic

- **Pastel, low contrast, a handful of hues**: one ground family (sand/grass/earth or its equivalent), one neutral rock, and a small set of wall and roof colours repeated across buildings.
- **Time of day is a keyframed set of colours** (zenith, horizon, deep, shallow, sun colour, intensity, elevation, azimuth), interpolated. Day is airy and cool; dusk warms the horizon; night desaturates everything toward blue-violet.
- **At night, warm emissives are the only bright things** (windows, lamps, a beam). Keep the sun sideways to the camera in key shots (low sun behind the target turns faceted water into glare); water receives no shadows.
- No outlines, no black; shadows and AO are the only darks.

Examples of world palettes: sand, grass and coral roofs under a pale-blue day; snow tiles, pine greens and red cabins under a lilac sky; terracotta mesas, sage scrub and turquoise pools under an apricot dusk.

## 4. Type & subtitles

- Geometric OFL sans faces: a rounded one for subtitles (e.g. Quicksand 600), a geometric caps face with wide tracking for titles (e.g. Josefin Sans).
- **Subtitles**: no box; warm white with a soft dark-blue drop shadow, centred low; a small flat-shaded tile icon beside them whose top colour follows the time of day. Hold ≥ max(1.8 s, speech + 0.6 s), never overlapping the next line or a title.
- **Titles behave like tiles**: letters rise one by one from under a water line, overshoot and settle.
- A text card over the world leaves a gap where the world stays visible.

## 5. Motion quality

- On ones (24 fps), smooth. The charm is in the **arrival curves**, not stepping.
- **Rise from below**: a short cubic ease up, then a damped-sine overshoot; a splash ring and spray the moment it breaks the surface. The event time is when it settles.
- **Drop and stack** (floors, roofs, rings): a fast ease-in fall, a damped bounce, and volume-preserving squash-and-stretch on landing.
- **Pop** (trees, lamps, details): scale `1 − e^(−k s)·cos(ω s)`, about 25 % overshoot.
- **Life**: mills turn, smoke puffs, birds circle, boats bob with the same wave function as the water (evaluated on the CPU).
- **Schedule growth on the music grid**: at most one piece per smallest slot, so every event keeps its own note; accelerate by density (halves → quarters → eighths), not by tempo.
- Never moves: the projection (no perspective, no fov change).

## 6. Camera grammar

`THREE.OrthographicCamera`. **Frustum height is the zoom** (a few units for a close-up, the whole world at a dozen or more, hundreds for a scale reveal); place the camera ≥ 3 × frustum height away or the bottom of the frame looks under the sea. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Turntable (azimuth sweep) | the thing seen from every side | building; inspecting; a product assembled |
| Pure orthographic zoom (frustum change) | scale without perspective | a detail in context; smallness; a world among worlds |
| Elevation change | low (≈20–25°) widens the sky band; high (≈50°) reads as a map | night and stars; a sweep across the whole world; a plan |
| Locked 3/4 wide | the world lives on its own | lights coming on; time-lapse; waiting |
| Tight close-up on one arrival | the bounce and the splash | a key piece; a milestone; a gag |
| Side angle trailing a mover | travel across the frame, never at the lens | a delivery; a departure; a route |
| Lateral truck along a row of tiles | a list, a sequence | steps of a process; a timeline |
| Time-lapse sun sweep, camera still | light is the time machine | a day; a season; history |

Intercut wide and close on beats: wide shows the shape growing, close sells the bounce. Transitions: hard cuts on the beat, a time-of-day change, a zoom through the sky; no dissolves, no perspective whip-pans.

## 7. Sound palette


<!-- END STYLE PAGE -->
