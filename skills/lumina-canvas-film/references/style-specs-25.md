# Complete style specifications 25


<!-- STYLE: silent-film -->

In `demo/engine/`: `ink.js` (tonal forms, ink line, wash, hatch; `drawShape()` draws any path in this style), `redraw.js` (`Redraw`: tonal painting or real footage → ink drawing, WebGL2), `film.js` (`FilmPost` print pass + `damage()`, stackable on any 2D canvas, with an optional colour mask), `cards.js` (intertitles, deco borders, iris, theatre), `figure.js` + `heads.js` (2.5D rig). `demo/timeline.js` is a cue sheet that drives both picture and score. API table and a minimal example (a one-colour shape through the whole pipeline): [DEMO.md](DEMO.md) "Engine reference".

## 11. Variation space

You decide the genre (comedy, melodrama, adventure, newsreel), the characters, the gag or the drama, the cards, the tint plan, the opening and the ending. All far from our demo:

- Structures: **a newsreel** (a sequence of "reports" with headline cards and a narrator card between them); **a melodrama in three reels** (each reel a tint: amber, blue, rose; a villain card, a rescue); **a trick film** (Méliès-style: one stage, a magician, objects appearing and transforming by substitution cuts).
- Openings: **mid-chase**, the film already running and scratched, no title yet; **a single intertitle question** before any image; **the projectionist's view**: the beam from the booth, then the screen.
- Endings: **the film breaks** (the print burns through and the lamp shows white); **a final card that addresses the audience** directly; **fade to black on a locked wide** with the piano holding one chord.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: backrooms -->

# Liminal Found Footage — Style Prompt

> Camcorder tapes recovered from empty, endless, fluorescent-lit spaces. Rules instead of monsters.
> Genre reference (grammar only): "the Backrooms" internet folklore and new-weird / rule-horror; 1990s consumer camcorder footage. **Never** use the word "Backrooms", wiki "Level" numbers, community entity names, or any existing organisation or logo inside the film. Everything on screen (rules, forms, company voice, any presence) is original.

Suits short films; the length follows the walk, and the dread thins out once nothing new goes wrong.

## 1. Essence, and what it is not

- **One first-person camcorder recording** (1990s VHS, 4:3), handheld, continuous.
- **An empty, familiar-but-wrong interior** that repeats: an office, a hotel floor, a school, a mall, a parking level, a hospital wing. Humming fluorescent light, no people.
- **Dread from emptiness, repetition, bureaucratic rules, and the camera's own machinery failing at the wrong moment.** Nothing chases anyone. A chill on the back of the neck, not a jump.
- **The medium is the storyteller**: focus, exposure, tape damage and the on-screen display carry the plot.

Not a horror film (no monster close-ups, no gore, no jump scares, no score stings), not an ASCII/CRT terminal piece (the artefacts are tape and lens, not phosphor and scanlines), not a ruin (clean is part of the style).

## 2. Materials & rendering

- **Frame**: 4:3 pillarboxed in 1920×1080. Render 3D at low resolution (e.g. 720×540) and let the VHS pass upscale; low resolution hides CG cleanliness.
- **Space**: axis-aligned partitions on a grid with random gaps and stubs, pillars, a drop ceiling of tiles with recessed light panels at regular intervals. A hand-authored route through procedurally filled space, so every doorway shows more emptiness.
- **Lighting = thousands of lights, no shadows**: store every panel's colour and intensity in a float texture; each fragment sums the nearest panels (emitter cosine × Lambert / (d² + ε)) plus a bounce term. No occlusion: this light is flat. Per-light variation (a few % warm/cool/green), a few % dead, a few % flickering. Ambient occlusion darkens seams.
- **Fog follows local light**: fog colour × (local light / average). Where lights are dead the haze is dark, so a silhouette there reads as a *hole in the light*. Background = fog × ~0.15, so corridors dissolve into darkness, never a bright wall.
- **Restrained decay**: tide-marks at the foot of some walls, a discoloured band under the ceiling, rare peeling seams, a few yellowed or missing tiles, dead insects in diffusers. Percentages in single digits.
- **Printed matter**: office laser-print on yellowed paper, condensed sans headers, form numbers and revisions, numbered rules, a polite closing line from "Management". Pinned or taped.
- **VHS camcorder pass** (not a CRT): small line jitter (≤ 0.25 px low-frequency wobble), a head-switching band, tracking tears on demand, barrel + vignette on the image but **not** the OSD, luma blur + edge ringing, chroma smeared right, light smear, drifting white balance, AGC noise in darks, dropouts, lifted blacks, soft clip. Noise at tape rate (30 fps). No scanlines, no RGB mask.
- **OSD**: a hand-made bitmap font with a black outline: REC dot, battery, time and date. A camcorder title generator uses the same font, larger.

## 3. Colour logic

- **One dominant sickly hue** from the location's materials (mustard wallpaper, institutional green, hospital blue, beige laminate), with a darker trim and a mottled floor of the same family; ceiling and light panels near-white and slightly warm.
- **Exactly one saturated colour**: a signal such as a red alarm lamp, a green emergency sign, an amber warning light. It is the only thing that blooms (drive its emissive high enough to cross the bloom threshold).
- White balance drifts; colour is never graded clean.
- Example material palettes: wallpaper `#d5bd66`, trim `#4d3d26`, carpet `#8c763c`; pool tile `#9fc7c0`, grout `#e6ece6`, water `#5e8f96`; school corridor `#b9c49a`, lockers `#6f7f66`, linoleum `#a89a7d`.

## 4. Type & subtitles

- **Closed captions (CEA-608 style)**: a monospace (e.g. IBM Plex Mono 600) ~42 px, white on a solid black box per row, ≤ 32 characters, centred inside the 4:3 frame above the OSD. Untouched by tape noise (the TV decodes them). Hold ≥ max(1.8 s, speech + 0.6 s).
- **Speaker marks**: `[PA]` for announcements, italics for the operator, SDH descriptions in brackets (`[LIGHTS FLICKER]`, `[TAPE NOISE]`, `[SILENCE]`).
- **Rules on notices are not captioned**: they are the picture. Readable at 1080p, ≥ 3–4 s uncovered. For close-ups **lower the camera so the lens is parallel to the page**; pitching down at a vertical sheet shears words into fake italics.
- The **title** is camcorder title-generator text over the first shot.

## 5. Motion quality

- **One continuous handheld take.** Cuts happen only where the tape breaks: power-on roll-in, tracking tear, REC off.
- **Handheld** = walking gait (head bob a few cm, sway, small roll) + breathing (~0.27 Hz) + tremor noise at a few frequencies whose amplitude follows a **fear** curve. At a held breath, **freeze all of it**.
- **Looking down** shows only shoe toes and floor, never legs.
- **Autofocus** = focus distance animated with overshoot: blur → lock → slip → lock. Blur comes from pulling focus *near*. Zoom narrows the FOV and opens the aperture.
- **Lights flicker** as short blackouts (~0.1 s); auto-exposure catches up with a lag (~0.45 s) and gain noise pumps.
- Things move by themselves slowly (a door over >1 s, eased), never snap.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Walking POV down a corridor | routine, the endless | establishing the space; time passing |
| Slow pan off a detail to the space | scale; the space goes on | a reveal; a first look |
| Glance down at the feet | obedience, avoidance | obeying a rule; not looking |
| Crouch and hold on printed text | reading; bureaucracy | a rule; a contradiction |
| Zoom + focus hunt into the distance | seeing / not seeing | a presence; a doubt |
| Identical framing after a tear, only the OSD changed | time removed | a jump; a loss |
| Turn a corner, hold still | a threshold | an exit; a choice |
| Slow push-in with no sound | the pull of something | a door; a sign |
| Backing away while filming | retreat, fear | leaving a room; a rule broken |
| Camera set down on a surface, static, recording alone | abandonment | the operator gone; a long wait |
| Whip toward a sound, then nothing | expectation denied | a noise with no source |

Framing: text readable and uncovered; any presence small, far, and in a region of dead lights. Transitions: tape events only.

## 7. Sound palette

- **No score.** Only what the tape would have recorded. Music exists only inside the world (hold music, a radio through walls, a tinny PA jingle), filtered and reverberant, possibly slowing with tape wow.
- **Fluorescent bed**: 120 Hz (or 100 Hz) + harmonics, a buzzy band-passed component, a faint ballast whine, bad-tube bursts; gated by the same light curve as the picture; closer in small rooms.
- **PA voice**: calm, corporate, through a ceiling speaker (band-pass ~300–3500 Hz, cone resonance, saturation, room reverb), dry enough to stay intelligible. A short original chime before announcements; after a time jump, chime and voice may drift flat.
- **Operator**: a few short, quiet lines with proximity bass and breath; breathing whose rate follows fear; a held breath and one long exhale.
- **Foley by material**: carpet steps (low thud + wet squelch) or hard-floor squeaks, cloth rustles, camcorder clack and motor, zoom servo, AF ticks, ballast tink on flickers, a stick-slip hinge, a drag overhead, a vending machine, a pipe.
- **Silence**: digital zero for a second or more (tails included), captioned `[SILENCE]`, is the strongest tool. A soft scare at most: everything restriking at once when sound returns.
- **Drone** options: a low brown-noise band with beating sines rising slowly; the room tone itself pitch-shifting; nothing.
- **Mix**: bed and in-world music ≈ −8 dB under voices. −14 LUFS; no added grain (the noise is in the picture).

## 8. Native moves

A menu: use the ones your story needs.

- **Autofocus / auto-exposure hunting.** Something is there only while focus is correct. *Fits content like:* a missing pet on a hotel floor; a figure in an empty stadium; a shape at the end of a hospital corridor.
- **Tape tracking damage.** A tear is a cut the universe made; same framing after, but the clock jumped, the battery drained, a light died. *Fits content like:* a night-watch log; a lost weekend in a mall; a house that ages between tapes.
- **The OSD is plot.** REC, battery, date and time code are evidence. *Fits content like:* an alibi; a countdown; a dated inspection.
- **Rules as text in frame.** Notices and PA announcements start ordinary, drift wrong, contradict each other, and finally address the viewer. *Fits content like:* a pool's safety rules; a school fire drill; a museum after hours.
- **Emptiness and repetition.** The same notice in a different place; the same room with one detail changed; a corridor into fog. *Fits content like:* a moving-day walkthrough; an airport at 4 a.m.; an office after layoffs.
- **The thing that is almost human.** A distant silhouette wrong by 15–40 % (small head, long neck, narrow high shoulders, long arms), drawn as organic curves on a billboard, moving slowly. *Fits content like:* a mannequin that is not; a night guard; a reflection that lags.

## 9. Pitfalls of the medium

- **A fully bright scene reads as a hospital corridor** → partitions with gaps; far areas fall dark.
- **Lights leak through walls** (no occlusion) → a dead zone needs every light within ~±5 m dead, and the space behind it dim.
- **Background shows as a bright rectangle** at a corridor's end → background = fog × ~0.15.
- **Uniform fog lifts silhouettes to grey** → fog follows local light.
- **Line wobble skews text; pitching down italicises it** → ≤ 0.25 px wobble; lower the camera.
- **Primitive-built figures read as toys**, primitive legs as tubes → organic silhouettes; show only shoe toes.
- **Pure red never blooms** at low emissive (low luminance) → drive it far higher.
- **Normalising a filtered signal by its pre-filter peak** blows up a bus → normalise the processed signal.
- **Heavy PA reverb destroys intelligibility** → ASR-check processed lines and the full mix.
- **Billboards stamp dark rectangles** in AO → exclude them.
- **Time-compressing a finished timeline** → keyframes in original time mapped through one warp function, including hard-coded times elsewhere.

## 10. Engine

`demo/world.js` (layout, light DataTexture, custom lighting and fog shaders, props), `demo/tex.js` (procedural wallpaper, carpet, ceiling, panels, notices, signs), `demo/vhs.js` (VHS camcorder ShaderPass), `demo/osd.js` (bitmap font, REC, battery, clock, title generator), `demo/subs.js` (608 captions), `demo/thing2d.js` (organic silhouette), `demo/story.js` (timeline, camera keyframes, focus / fear curves, time warp), `demo/main.js` (renderer, post chain GTAO + DOF + bloom → VHS, handheld rig). File map and build: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the location and its materials, the procedure or reason for filming, the rules, the route, the presence (or none), the signal colour, the opening, the ending and the length.

All far from our demo:

- Structures: **two tapes** (the same route filmed twice, a year apart; the second tape finds what changed); **a real-estate walkthrough** where every room is described cheerfully by the operator while the house keeps adding rooms; **a checklist read aloud** item by item, each item ticked on a clipboard in frame, until an item is not on the list.
- Openings: **mid-sentence** (the tape starts with the operator already talking, tracking still rolling in); **a test pattern** and a date slate before the camera is picked up; **the lens cap on**, sound only, until the cap comes off.
- Endings: **battery dies** (the icon blinks, the frame freezes on the dead cell); **the camera is set down** and keeps recording an empty room; **the tape loops** back to the first shot, now with the operator's shoes visible in it.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: brick-toy -->

# Brick Toy — Style Prompt

> Stop-motion toy-brick films shot like macro photography on a real desk: a world built from interlocking plastic bricks with round studs, animated a pose at a time.
> References (grammar only): brick-film stop-motion on a tabletop and the "brick movie" approach of stepping characters while the camera moves smoothly; macro toy photography (softboxes on glossy plastic, shallow focus, real objects as landscape). Copy none of their characters, sets or music, and never use a brand name.

## 1. Essence, and what it is not

A brick world on a **real surface** (a wooden desk, a kitchen table, a windowsill), shot with a **macro lens** and animated **in stop-motion**. The charm is the tension between the toy world and the real room.

One-glance traits: glossy ABS with clean rectangular highlights; studs on every top face; seams darkened by contact shadow; real objects out of focus behind; characters that move in held poses on twos.

**Never** use the LEGO name, logo or minifigure silhouette (trademarks). Characters are *built from bricks* (e.g. 1×1 columns for legs, a 2×2 brick for a torso, round bricks for arms, a round 2×2 helmet). Studs carry no lettering.

Not a low-poly isometric island (no flat-shaded facets, no floating diorama), not a clay or felt stop-motion (no deformation: bricks are rigid), not a clean product render of a toy (this world is played with, handled, knocked over).

## 2. Materials & rendering

- **Plastic**: ABS with strong clearcoat (~0.85, clearcoat roughness ~0.07); a roughness map with faint fingerprints and scratches (base ~0.17, scratches up to ~0.65); a bevel so edges catch a highlight.
- **Geometry**: rounded box bodies (bevel ~0.045 stud), studs with a thin lip. Unit = 1 stud pitch (8 mm); brick height 1.2, plate 0.4. Large baseplates are **matte** (lower clearcoat than bricks), or they reflect softboxes as a coloured wash.
- **Set**: a real surface with a real texture and real props at true scale (1 m = 125 studs). Household objects become landscape. Light it with a **neutral daylight studio HDRI**, never a tungsten interior (white bricks turn orange).
- **Light**: a toy-photography setup. A directional key from one upper side, warm-white, casting shadows (fit its shadow frustum to each shot so shadows stay crisp); two or three **RectAreaLight softboxes** (key front, cool rim behind, one over any big set) so glossy plastic shows clean rectangular highlights; environment kept low (~0.45) for contrast. Add a soft contact-shadow blob where the key's shadow falls behind a hero object.
- **Ambient occlusion is mandatory**: GTAO (radius a few studs) darkens seams between stacked bricks, stud bases and contact points. Without it bricks look pasted on.
- **Supersample 2×** (render 3840×2160, deliver 1080p): thin stud edges and bevel highlights shimmer without it.
- **Lens**: physical depth of field (CoC ∝ |1/focus − 1/z|). Scale aperture with shot size: widest for close-ups, less for mediums, least for a wide (too much blurs the hero at mid distance). Focus is always on a character's head or the brick being placed.
- **Effects are bricks**: fire, smoke, water, light, weather, celestial bodies are all built from plates, round bricks and translucent pieces, jittered or rebuilt per drawing. Nothing is a particle system or a soft gradient.

## 3. Colour logic

- A **toy palette**: a handful of saturated brick primaries plus white, black, greys, tan. Each built object has one dominant colour and at most one or two trim colours; characters and hero objects take the most saturated ones.
- The **real world stays natural and muted**: wood, paper, ceramic, daylight. The saturated colour belongs to the toys, which makes them pop against the room.
- **Whites must read white**: grade slightly cool so white bricks don't go cream from the room bounce; soft contrast, saturation lifted ~10 %.
- Translucent pieces (orange, yellow, clear, blue) are reserved for effects: fire, light, water, glass.
- Example palette (the classic brick primaries): red `#c91a09`, blue `#0055bf`, yellow `#f2cd37`, green `#237841`, white `#f2f2ee`, black `#1b2a34`. Others: pastels and tan; greys with one accent.

## 4. Type & subtitles

- A rounded, friendly OFL face (e.g. Fredoka, in `core/fonts`) for titles and subtitles.
- Subtitles live on a **toy element**: a dark rounded pill low in the frame with a small brick icon beside the text, or a printed tile, or a sign built into the set. White on dark, ≤ 2 lines. A second speaker type (radio, device, narrator) gets its own icon colour or tag. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles pop in on 12 fps steps, like a piece being placed; a short sub-line in a brick colour.

## 5. Motion quality

- **Characters and bricks step at 12 fps** (on twos); **camera, focus, fire and flying vehicles move on ones** at 24 fps. Stepping the camera too reads as judder, not charm.
- Bricks **fly in on arcs** and **snap** with a tiny overshoot (a fraction of a stud → 0 in ~4 frames). Every snap is a click on the soundtrack.
- Characters act with **big readable poses** held for several drawings: a V of arms for pride, arms flung up for alarm, a bowed head for sadness, a hop for joy. Walk cycles swing legs about ±0.55 rad with a small bob. Arms and legs rotate at their joints; nothing bends.
- Collapses and falls use **real rigid-body physics**: tip about the base edge, then independent bodies with gravity (a lower-than-true value reads better at this scale), bounces (restitution ~0.3), friction, settling flat. Pre-simulate so every render is identical.
- Tiny imperfections are allowed. Bricks never stretch, squash or morph.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Extreme macro on one brick or stud, real room blurred behind | The toy scale is the world | a beginning; a detail that matters; a single part |
| Low angle at minifig eye level | A tiny character made heroic | ambition; pride; standing up to something big |
| High wide over the whole surface | The scale reveal: it was a toy all along | a summing-up; irony; a finished build |
| Low, wide, lonely frame, character small in a corner | Smallness, failure | a setback; waiting; loss |
| Frontal close-up, hands and brick in focus | Intimacy, decision | a choice; a repair; a gift |
| Handheld shake on impact | Physical shock | a collapse; an arrival; a collision |
| Tracking alongside a moving object, destination ahead | Momentum toward a goal | a journey; a race; a launch |
| Top-down plan view | Order, layout, a map | a plan; sorting parts; a city from above |
| Rack focus from a real object to a brick (or back) | Two scales in one frame | "big world, small maker"; a comparison |
| Orbit around a finished build | Pride, inspection | a product; a monument; a result |

Framing: keep foreground clutter out of the frame edges (piles of parts love to block the lens); check headroom in every shot; check every real prop against every camera, because an object placed on one shot's axis sneaks into the background of another. Cut on beats or bars; a snap can be a cut point. No generic dissolves; transitions can be a hand-placed brick covering the lens, a whip along the desk, or a pull out of one set into the next.

## 7. Sound palette

- **Instruments**: small, acoustic, playful (glockenspiel, toy piano, pizzicato, ukulele, whistling, claps, melodica); a brass or orchestral swell for scale; a heartbeat drum for suspense. Licensed or original, edited to the picture (cut on bars, bar-aligned jumps, chroma similarity at joins) rather than looped under it.
- **Foley** (synthesizable): plastic creak before a failure, tiny plastic footsteps, a crash of many clacks, a brick click (short transient + resonances near 2.9 kHz and 4.6 kHz), clack on wood, rattle of a parts pile being stirred, whoosh on throws, a bell "ding" for discovery, bricks sliding over paper, motors and engines built from filtered noise.
- **Silence is a tool**: cut music dead at a failure or a surprise; leave only room tone and one small real-world sound (a ticking clock, a fridge hum, a distant bird). Music can also drop out before a big moment, leaving a pulse or a countdown.
- **Voice**: a warm storyteller, few short lines with room to breathe; secondary voices through a device filter (band-pass ~380–2800 Hz + soft saturation), optionally with beeps. Verify every line with whisper.
- Mix: voice compressed, music ducked ~40 % under voice, loudness −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Snap-together building.** The plot is an act of building; pieces fly in on arcs and click home. *Fits content like:* a company assembling its first product; a neighbourhood rising street by street; a recipe put together ingredient by ingredient.
- **Break without harm.** Things fall apart and the parts become something new; failure yields spare parts. *Fits content like:* a pivot after a failed plan; recycling; a team reshuffled into a better shape.
- **Toy on a real desk.** Real objects become landscape at toy scale. *Fits content like:* a laptop keyboard as a city grid; a houseplant as a jungle; a coffee spill as a flood.
- **Hand-made stop-motion.** 12 fps poses, tiny imperfections, even fire and water made of bricks. *Fits content like:* a weather report; a kitchen explained with brick flames; a science demo of a volcano.
- **Rebuild into something else.** The same pieces, rearranged on screen, become a different object. *Fits content like:* one career turning into another; a before/after renovation; a word re-spelled.
- **The scale reveal.** Pull back until the whole world is a toy on a table. *Fits content like:* a big ambition that is still small; a year in review; a child's imagination.

## 9. Pitfalls of the medium

- Tungsten HDRI → orange whites. Use a neutral studio HDRI and a slightly cool grade.
- Clearcoat on a large flat baseplate reflects softboxes as a coloured wash. Make it matte.
- Flat, slightly jagged first renders: even light, no AO, single-sample rendering, stepped camera. Fix: softboxes + low environment, GTAO, 2× supersampling, cool grade, camera on ones.
- Too much aperture blurs the hero at mid distance. Scale aperture with shot size.
- A fast-rising or fast-moving object becomes a dot on a blank wall. Track it and keep its destination in frame.
- Curved transparent parts made from a sphere segment vanish inside a cylindrical part. Use an open-cylinder panel.
- Real props on a later shot's camera axis sneak into the background. Check props against every camera.
- Random jitter used as a material or colour index can go negative → undefined material crash. Clamp.

## 10. Engine

In `demo/`: `bricks.js` (rounded brick/plate/round-brick geometry, studs, plastic materials with clearcoat and fingerprint roughness), `actors.js` (a brick-built character rig with pose objects and `walkPose`), `set.js` (desk, HDRI, real props at true scale, softboxes), `rockets.js` (props, pre-simulated rigid-body physics, brick fire and smoke), `main.js` (acting, cameras, DOF, subtitles, sound events), `mix.py` (synthesized foley + voice + music), `music/edit.py` (bar-aligned score edit). Minimal start: a brick lighthouse from `bricks.js` on a stack of books, lit by the `set.js` softboxes, one still via `core/render/still.mjs`.

## 11. Variation space

You decide the structure, the characters (or none), the surface and its props, the opening, the ending, the camera path, the pacing, the palette within the colour logic and the music. All far from our demo:

- Structures: **a catalogue** (one build per beat, each a different object answering the same question, lined up at the end); **two builders** on opposite sides of the table whose builds grow toward each other; **a disassembly** (a finished thing is taken apart piece by piece to explain what's inside).
- Openings: **a hand pours a bin of bricks** onto the table and the pile settles into the first shape; **a real object first** (a mug, a phone), then rack focus to the tiny world at its base; **plan view** of an empty baseplate filling in like a map.
- Endings: **one piece left over** held in close-up, the question it raises unanswered; **the lights go out** in the room and only a lit brick window glows; **a real hand** reaches in and picks the character up.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: paper-popup -->

# Paper Pop-up Book — Style Prompt

> A pop-up book on a real desk becomes a stage: flat cut-paper actors with white borders perform in front of paper sets that spring up from the page, under real lamp light and a real macro lens.
> References (grammar only): the *Paper Mario* series (flat cut-paper actors with a white border in a 3D diorama, bubbles that type on with blips, action ratings); Robert Sabuda / Matthew Reinhart pop-up books (layered V-folds, pieces rising back to front, pull-tabs); macro "tiny world on a real desk" photography. Never copy their characters, logos, UI or music, and never name them in the film.

## 1. Essence, and what it is not

Two worlds in one frame. **The real world** at human scale: a photoreal surface lit by an HDRI room, a few real objects, a macro lens (shallow focus, warm practical light, soft contact shadows). **The paper world**: a hardcover book in that room; when it opens, one board stands up as the **backdrop** and the lower page is the ground. Every set piece is a **flat cut-paper card** that lies on the page and **pops up** around its bottom edge. Characters are cut paper too: a few centimetres tall, flat, with a thick off-white border, a grey cardboard edge and grain.

What sells it is the **mismatch of scale and material**: flat, saturated, outlined paper cartoons under real light, casting cut-out-shaped shadows and going soft in real lens blur. Keep the paper graphic; let light and lens make it real.

Not a papercut silhouette film (no one-colour lace, no backlight), not a 3D cartoon (nothing modelled round), not claymation (paper hinges, folds, curls and slides; it never squishes).

## 2. Materials & rendering


<!-- END STYLE PAGE -->
