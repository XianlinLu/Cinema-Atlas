# Complete style specifications 26


<!-- STYLE: paper-popup -->

- **Real units** (metres): page 0.3–0.5 m wide, actors 3–5 cm, near plane a few mm, so HDRI, shadows and depth of field behave like a real macro shot.
- **Cut-paper finish**: Canvas2D art with a dark ink outline; its silhouette dilated (drawn at many angles on several rings, recoloured `source-in`) into a grey cardboard edge offset slightly down (thickness) and a wide off-white border; a shared paper grain on top (`source-atop`).
- **Drawing**: one dark-brown ink (never black), thick outline + thinner detail line, round joins; shading = one hard **crescent** (fill with shade, refill shifted with base); wobbly shapes (low-harmonic noise), never perfect geometry; simple faces.
- **Pop-up pieces**: planes with art on the front and plain paper on the back (same alpha); `alphaTest` + `alphaToCoverage`; a custom depth material with the alpha map so **the shadow is the cut-out silhouette**. Anything "3D" is several flat cards (front/back layers, triangles hinged on a keel).
- **The book** is modelled: cloth cover with foil title (roughness/metalness map), page block with edge lines, a curling leaf.
- **Real world**: HDRI environment and softly blurred background, real wood or fabric, a few CC0 props. **Neutral tone mapping** (ACES shifts paper colours).
- **Depth of field by hand**: CoC = aperture × (1/focus − 1/z), spiral gather that keeps far samples off a sharp foreground (stock bokeh looks fake at this scale); then light bloom, vignette, warmth.

## 3. Colour logic

- Saturated children's-book colour, **never neon**; the real world stays natural and slightly warm so paper pops against it.
- **One dominant hue family per spread**, so a page turn is also a colour change; a few accents (a red, a yellow, a gold) recur across spreads to stitch the book together.
- Ink dark brown, border off-white, card backs plain paper.
- Unfinished or "outside the story" pages lose colour: graphite on cream. Night is a change of the paper art; the real lamp keeps its warmth.

Examples of spread families: green meadow under sky blue; pink-and-lilac market with mint accents; ochre desert with a turquoise oasis.

## 4. Type & subtitles

- Rounded OFL faces: a rounded sans for subtitles, bubbles, signs (e.g. Fredoka); a chunky display face for cover, banners, action words (e.g. Lilita One); a storybook serif for taglines (e.g. IM Fell English); a playful Chinese face (e.g. ZCOOL KuaiLe) with the Latin face in its stack.
- **Narration subtitles**: bottom centre, ~40 px, cream with a thick dark-brown outline and soft shadow, second language smaller below. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Speech bubbles** live in the paper world: white card, ink outline, tail projected each frame to the speaker; pop in with overshoot, type on with blips.
- **Titles are paper objects**: a cardboard sign dropping on strings and swinging; the cover itself is the film title. Action words (italic display, gradient, double stroke, rays) sparingly, like a game rating.
- Subset Chinese fonts to the characters used; re-subset after every text change.

## 5. Motion quality

- On ones (60 fps suits the smooth macro camera), all a pure function of `t`. Paper moves stiffly; life comes from easing: `back()` overshoot for pop-ups, springs for things on strings, squash and stretch on characters.
- **Pop-ups rise back to front** (delay grows with distance from the reader), far pieces lying back, near ones folding forward face-down; they fold down in the same order.
- Plants and light props sway a few hundredths of a radian around their base.
- **Characters are flat cards redrawn per quantized pose** (walk phase, arms, eyes, mouth, look, blink); walk phase follows distance walked, so feet don't slide.
- **Turning around = a `scale.x` flip** between front and back drawings; never `rotation.y`. Jumps: parabolic arcs, squash at both ends, a paper puff on landing.
- **Page turn**: a many-segment strip whose bend is integrated along its length, so it curls like paper.
- Never moves: the room.

## 6. Camera grammar

One virtual macro camera keyed as position / target / fov / aperture / focus with monotone-cubic interpolation; a new key list = a hard cut. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Eye-level macro track, shallow focus | being inside the story at the actors' size | a walk; a conversation; a chase |
| Pull up to a 3/4 view of the spread | the mechanism, the map | a page turn; a new setting; a plan |
| Descending dolly from human height | entering the book's scale | an arrival; zooming into one part of a system |
| Push-in on a face | feeling | a wish; a fear; a decision |
| Reverse shot from inside the book to the blurred room | the world beyond the page is huge | curiosity; an outside threat; a reader watching |
| Rack focus paper ↔ real object | paper and reality touch | cause and effect; a real product in a paper story |
| Top-down over the open spread | a board game, a diagram | a route; two sides of the gutter compared |
| Locked frame on a pull-tab | the trick is the event | before/after; a count |
| Rising crane leaving the book small | scale, distance | aftermath; a summary; time passing |

Actors in focus, room objects as soft foreground or background; keep near pop-ups out of the lens path. Transitions: page turns, a book closing and reopening, a hard cut on a paper sound; never a video dissolve inside the book.

## 7. Sound palette

- **Paper foley is the signature**: page swish, cardboard thump, pop-up snap (short sine sweep + crinkle), fold and crease, pull-tab slide, footsteps as tiny taps with crinkle, slat flaps, string-drop tinks; the book's spine creak and closing thump. All synthesizable from the page's event list.
- **Character voices as typing blips**: one waveform and pitch range per character, a blip every other letter.
- **Narration**: one warm storyteller, picture-book sentences; pronunciations kept apart from displayed text.
- **Music**: whimsical, acoustic or toy-like: music box, pizzicato strings, clarinet, glockenspiel, ukulele, toy piano, brushes. Options: a warmer cue for anything in the real room; a bar-aligned internal edit of a library track so its ending lands on a picture event; a pull-tab's clicks setting a cue's pulse.
- **Ambience**: room tone and a clock for the room; one bed per spread for the paper world.
- **Silence** = the book held still with only room tone; before a turn that matters, or a hesitation.
- **Mix**: voice high-passed, compressed, well above music; music ducked under speech with smooth release; limit SFX per channel; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **The book opens**: creak, the board swings up, the world pops up back to front. *Fits content like:* a project launch; a first school day; a recipe book.
- **Page turn = scene change**: old pieces fold down as new ones spring up. *Fits content like:* stages of a process; a farm's seasons; chapters of a biography.
- **Pull-tab mechanisms**: flipping slats, a sun on a stick, sliding strips, a hinged door, pieces on strings. *Fits content like:* a forecast; old way/new way; a lock opening.
- **Paper as character**: crumpled, smoothed, refolded, torn, taped. *Fits content like:* a mistake becoming a lesson; recycling; a rejected draft becoming the design.
- **The edge of the page**: crossing between paper and the room, either way. *Fits content like:* a character stepping into a phone on the desk; a real object entering the story; a drawing coming true.
- **The real object plays a part**: a lamp as a sun, a mug as a tower. *Fits content like:* a product at home; the reader's presence; real clock time.
- **Typed bubbles and ratings**. *Fits content like:* a tutorial; a quiz; a small victory.

## 9. Pitfalls of the medium

- `rotation.y` shows a card edge-on, then its blank back → `scale.x` flip. Negative scale also swaps front/back materials → draw mirrored props instead.
- A one-plane container hides its contents → back card + front card, contents between.
- Near-lens foreground pop-ups fill the frame with blur → move them or close the aperture.
- Rectangle shadows kill the illusion → alpha-mapped depth material on every card; tight shadow bias and a big shadow map against acne on thin cards.
- A turning page goes black facing away from lights → emissive map = colour map.
- ACES shifts paper colours → Neutral.
- Headless Chrome falls back to software WebGL → GPU ANGLE flags; ES modules need HTTP.
- Redrawing character canvases each frame → redraw only on pose change.
- Chinese subsets miss new characters and Latin glyphs → re-subset; Latin face in the stack.

## 10. Engine

In `demo/` (three.js r170 + Canvas2D): `paper.js` (cut finish, grain, crescent, blobs), `cutmesh.js` (cut mesh with paper back and cut-out shadow, strings, particles), `book.js` (`setOpen(θ)`, `setLeaf(u)` curling page), `art.js` (drawings at a fixed px/m), `actors.js` (posable flat characters, a foldable plane), `sets.js` (spreads, back-to-front pop scheduling), `post.js` (hand DOF → bloom → vignette), `hud.js` (subtitles, bubbles, banners), `lib.js` (easing, `back`, `spring`, `track`), `render.mjs` (stills / events / video). API table and a minimal new-spread example: DEMO.md "Engine reference".

## 11. Variation space

You decide the book, the room, the characters (or none), the spreads and mechanisms, the opening, the ending, the camera path and each spread's palette. All far from our demo:

- Structures: **the almanac** (one spread per month or stage, each pull-tab left running so the book fills with motion); **two books facing each other**, characters trading objects across the gap; **one spread pulled again and again**, each pull a step of how something is made.
- Openings: **mid-turn** (a page already curling, we land in chapter three); **inside the gutter** (low along the fold as the first piece rises over the lens); **a mechanism alone** (a tab slides by itself before any character appears).
- Endings: **the book closes** (pieces fold in reverse, a puff of air, stillness); **one piece stays up** (everything folds but the card that is the point); **the shelf** (the camera finds this book among many).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: tilt-shift -->

# Tilt-Shift Miniature — Style Prompt

> A real-looking place photographed from high above with a tilted lens and a time-lapse camera, so the whole world reads as a tabletop model.
> References (grammar only): Sam O'Hare's *The Sandpit* (2010) and tilt-shift time-lapse photography in general: high vantage points, the blur band, time-lapse rhythm, cloud shadows sweeping over streets. Copy none of its places or music; show no real landmarks, brands or logos.

## 1. Essence, and what it is not

A place seen from high up through a **tilt-shift lens**: only a thin horizontal strip of the frame is sharp, everything above and below melts into blur. The eye reads that as a macro shot of something small, so the world becomes a model. Two more things make the trick work: **saturated, sunny colour** (model-railway paint) and **time-lapse** (vehicles and people move in fast, jittery steps like wind-up toys).

Not a toy or clay render (the world is photoreal, only the lens and the clock make it small), not a game's top-down view (no UI, no clean flat shading), not drone footage (the band, the saturation and the stutter are mandatory).

## 2. Materials & rendering

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


<!-- END STYLE PAGE -->
