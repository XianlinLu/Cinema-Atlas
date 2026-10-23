# Complete style specifications 21


<!-- STYLE: hologram-hud -->

An orbit camera (yaw, pitch, distance, narrow fov) with a screen position for the target, so the subject can sit beside text. A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| High 3/4, slow orbit craning down | Examination; a scan plane reads as an ellipse | a scan-in; a survey |
| Top-down plan view | Layout, order | a parts inventory; an assembly sequence |
| Eye-level profile, locked | The object as it stands in use | a height; a before/after |
| Push-in, then drift, 3/4 | This part matters; internals come towards the lens | the key spec; a flaw |
| Whip following the target box | Attention jumps to the next part | a list of parts |
| Orbit around a part's own axis | Axial structure only reads in rotation | rotors, stacks, hinges, lenses |
| Lateral dolly along a long part | Length, a path | a beam; a cable run |
| Pull back + loupe (frame in frame) | Where (wide) and what (loupe) | small parts; a sensor |
| Crane to eye level or back up | Status change: the object stands up or settles | a transformation; scale |
| Turntable 360° | Every side | a whole object; a symmetry |
| Nearly static, slow dolly | Reading time without a dead frame | a spec sheet; a checklist |

Framing: the subject is ≥ ⅓ of frame height at every key moment. Cards on one side, the chip rail on the other, subtitles bottom centre, a loupe above them: never colliding. Shorten explode vectors rather than fly a piece into text.

## 7. Sound palette

- **Music first**, on a grid (a bar = one information beat); locks land on downbeats, checked against the score.
- **Synth palette**: saw/square arpeggio with ping-pong delay (scooped 1–4 kHz for the voice), square pulse, 8th bass, synth hats and claps, detuned saw pads.
- **Density follows information.** Tools to pick from, in any order (most films need two or three): half-time for reading time; one beat of **true digital silence** (nothing, not even UI blips); a drop (808-style glide + wide saw chord) for the biggest change; a layer added or removed per part; deceleration by longer note values; a key change; a single sustained tone under a long hold.
- **Foley follows the material**: light = sines and FM blips **in the key**; machines = servo slides, pneumatic puffs, hydraulic hiss, metal tinks (J-cuts); a lock = thump + clack + two-tone beep; rolls tick at frame rate. Ambience: projector hum (40/80/120 Hz) and room tone.
- **Voice**: calm, confident. Duck music *and* foley with a **held** envelope (no pumping between words); lock transients escape. −14 LUFS.

## 8. Native moves

Each move serves information, not story. A menu: use the ones your film needs.

- **Scan growth = "this is real data."** *Fits content like:* a coffee machine; a satellite; an architectural model.
- **Target lock = "look here now."** The box is the camera. *Fits content like:* a car's sensors; a laptop's ports; a robot arm's joints.
- **Local explode = "why the number is true."** *Fits content like:* the burr set of a grinder; the layers of a running shoe sole; the elements of a camera lens.
- **Rolling digits = the payoff beat.** *Fits content like:* a brew temperature; a tolerance in microns; a price.
- **Chip accumulation = reading time.** *Fits content like:* 3–5 facts that must all be read.
- **Loupe = two scales at once.** *Fits content like:* a screw inside a watch; a chip on a board; a valve in an engine.
- **Solid hologram + beam = "the whole is ready."** Once, if at all. *Fits content like:* a launch reveal; a finished assembly; a v2 replacing v1.

## 9. Pitfalls of the medium

- Target boxes balloon → rest pose, skip `internal` pieces, long attachments `box:false`.
- Long diagonal leaders point at the wrong part → ring on the part body, flash the part.
- Two parallel boxes moving don't read as an explode → shell slides on its axis, contents stay and glow.
- A part built from generic boxes doesn't read as that part → give it its characteristic silhouette.
- Voice masked by foley, not music → duck foley too, hold the duck through word gaps.
- UI blips inside a silence break it → check cues against silence windows.
- A whip written inside the next segment plays as a hard cut → start it in the previous one.

## 10. Engine

`demo/engine/holo.js` (wireframe engine: projection, scan, explode, Fresnel faces, glow, pad, scan plane, `normalizeModel`, `modelFromPath` to extrude any 2D path), `demo/engine/hud.js` (theme, plate, target box, leader, rolling text, spec card, chip, marker, beam, subtitle, chrome, glitch), `demo/models/mkmodel.mjs` (primitives: tube, ring, disc, box, wheel, cells…). Models are normalised on load, so cameras work for any object. API, model format and an example: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the object, its model, which parts and in what order, the opening, the ending, the camera path, the colours, the pacing and the music. Use cases are **grammar for the order and duration of information**; build your own timeline from the user's facts.

| Use case | Information order | Hold per layer | Length |
|---|---|---|---|
| **Spec walkthrough** | Name + tagline → one spec per part (label, value, unit, detail) → weight / price → CTA | Title ≥ 5 s; value ≥ 2.5 s, then docked; final sheet ≥ 3 s | 30–40 s, 2–5 parts |
| **Loop screen** | Name → 3–5 specs → CTA, no voice; last frame = first | 3 s per spec, 5 s final | 20–30 s loop |
| **Teardown** | Part → what it does → one number; internals only when opened | 4–6 s per part | 40–60 s |
| **Upgrade** | Part → old value (dim) → new value (accent); old part scan-erased, new one scanned in | 3 s per upgrade | 20–30 s |
| **Assembly order** | Step number → part name; parts snap home one by one | one bar per part | 20–40 s |

All far from our demo:

- Structures: **a loop screen** that never names a product and cycles five sensors; **a teardown** one layer deeper per shot until the core is a single hot piece; **an upgrade** where two versions share the pad and every number rolls from old to new.
- Openings: **a part first** (one component locked in close-up; the rest scans out from it); **a flat outline** (a 2D silhouette extrudes into the wireframe, `modelFromPath`); **plan view** (top-down, the pad as a dial, the object arriving as its footprint).
- Endings: **one value at eye level** (the wireframe dims around the single number that matters); **knolling** (parts fly into a labelled top-down layout); **power-down** (edges cool, HUD panels switch off until only the pad glows).

Swapping `demo/content.json` and rebuilding is a technical check that the engine re-flows, not a way to make a film.

---

How our demo was made (story, shots, score, end card, build, content fields): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: rubber-hose -->

# 1930s Rubber Hose Cartoon — Style Prompt

> Black-and-white hand-inked cartoons where every object is alive and swings to a hot jazz band.
> References (grammar only): early Fleischer Studios shorts (c. 1930–33) for "the whole world dances", surreal transformation, the bouncing-ball singalong and ink-and-pen framing devices; *Cuphead* for how a modern team finishes the look and scores it with a big band. Never use an existing cartoon character, name or silhouette, and never copy designs, melodies or logos. **Avoid the "cup-head on a human body with a straw" design**: if your hero is an object, the *whole object is the body*.

## 1. Essence, and what it is not

Hand-inked black-and-white animation from the early sound era: characters with **rubber-hose limbs** (equal-width tubes, no elbows, no knees), **white four-finger gloves**, **pie eyes** (black oval pupils with a wedge cut out), huge round shoes, and bodies that squash and stretch like balloons. The backgrounds are soft grey watercolour paintings; the characters are flat white, grey and ink. Everything (furniture, machines, plants, the walls) **breathes in time with the music**. The film looks like a worn 35 mm print projected in a 4:3 gate: flicker, scratches, dust, gate weave, vignette.

Not a 1950s flat cartoon (no limited animation, no colour, no graphic backgrounds), not a silent film (the synchronised music is the engine), not a "retro filter" over modern animation (no joints, no rendered shading).

## 2. Materials & rendering

- **Frame**: 1920×1080 output with a **4:3 gate** (1440×1080 centred, black pillarbox), gate corners rounded (r ≈ 28 px), soft inner shadow on the gate edge.
- **Characters**: flat fills, one hard-edged form-shadow band (light grey) on the side away from an upper-left light, ink outline **constant in screen space** at any zoom (transform points first, then stroke; ~6 px at 1080p), light **line boil** (±1.2 px, 3 drawings cycling at 12 fps).
- **Anatomy kit**:
  - Limbs: noodle tubes of constant width (about 1/20 of the character's height), one smooth bend, round caps.
  - Gloves: palm + 3 fat fingers + thumb, flared cuff with a fold line, 3 stitch lines on the back. Outline the union only (stroke all parts thick first, then fill all).
  - Pie eyes: white oval, big black pupil (≈ 64 % × 74 % of the eye) with a wedge cut toward the upper right; blink with an eyelid in body colour and a lid line.
  - Mouths: smile with cheek ticks, open grin, "O", wavy (scared), pucker, tongue-out. Shoes: big black ovals with a white toe glint.
- **Object characters**: the face sits on the body; a **secondary feature carries the mood** (steam, a flame, a lampshade tilt, a spring). A box-shaped object is a real projected 3D shape seen slightly from above, the face mapped onto its front.
- **Backgrounds**: painted once into a cached canvas at 1.25–1.5× (push-ins stay crisp): flat wash + soft blotches (±5 %) + inner edge darkening + a thin dark-grey outline + paper grain. They never boil. Period motifs: patterned wallpaper, panelled furniture, checker floors, brick, clapboard.
- **Film damage** (composite pass, not the scene): low-frequency gate weave (±1.2 px) with a rare jump; flicker ±4 %; 0–3 drifting vertical scratches; 3–8 dust specks per frame; an occasional hair; strong vignette; a small jump on every cut; slight blur. Grain in ffmpeg (`mux.sh` grain **3**), not in the page.

## 3. Colour logic

- **Strictly greyscale**: about 6 grey steps plus a separate character white. No hue anywhere, not even in the film damage.
- **Characters own the extremes**: character whites and ink blacks are brighter and darker than anything in the background. Backgrounds live in the middle greys (walls around mid grey, furniture one or two steps darker). Add a mild contrast boost (≈ 1.1–1.15) in the final composite: 1930s prints are rich black and bright white, never flat grey.
- Form shadow is one light-grey band, never a gradient.
- Examples of the grey ramp's temperature: warm paper greys (our demo); cool silver-nitrate greys; a faint sepia print. Pick one and keep it for the whole film.

## 4. Type & subtitles

- **Subtitles are a period title card**: a small near-black plate with a white double-rule border and dot-and-ring corner ornaments; text in **IM Fell English SC** (~36 px), paper white. Drawn in the scene layer so it weaves and flickers with the film; pops on and off with no fades. Bottom by default, top when the action is low. One card may span two short voice clips; hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: **Shrikhand** fat retro script, white face, heavy ink outline (~14 % of the cap height), ink drop shadow down-right; letters can hop in a travelling wave on the beat. Sub-lines in **Limelight** caps.

## 5. Motion quality

- **Characters on twos** (12 fps); camera moves on ones (24 fps). A stepped camera reads as judder.
- **Tempo grid**: choose a tempo where one beat is an **even whole number of frames** at 24 fps (8, 10, 12, 16 or 20 frames), so every beat lands on a drawing of the twos.
- **Breathing**: every idle object squashes and stretches with `cos(2π·beats)`: an extreme on every beat (stretch on the beat, squash on the off-beat), sampled on twos, amplitude ~5–7 %, all props in phase. A peak of joy can raise the amplitude ×3 and squash the whole background painting around the floor line (~2.5 %).
- **Walk**: one step per beat with a body bob (sad = smaller steps, limp arms). **Run**: legs as a windmill (feet orbit a circle), lean forward, speed lines.
- **Anticipation–hold–action**: before every big move, crouch (squash to ~0.8), hold (let the band stop), then snap. Impacts get a squash with an exponential spring-back.
- **Held frames are acting**: a chain of holds, each glance on an eighth note with a woodblock tick, reads as thinking.
- **Freeze on a band stop**: when the music stops, freeze everything, background breathing included.

## 6. Camera grammar

A theatre camera: mostly locked, moving only to follow a runner or to land a gag. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Stage-wide, locked, eye level | A proscenium: the set is a stage and everyone on it performs | introducing a place; a group number; a routine |
| Hard cut to a face close-up | The reaction is the joke | a surprise; a taste; a realisation |
| Trucking pan beside a runner, eased start and stop | Pursuit, momentum | a chase; a race; a delivery |
| Medium follow shot (character ≈ 1/4–1/3 of the frame height) | Every step is a note | Mickey-moused climbing, dancing, working |
| Tilt with a fall or a rise | Gravity as rhythm | a tumble; a rocket; a lift |
| Slightly high angle, one unbroken shot | The hazard and the answer in one frame | a danger; a stretch; a rescue |
| Tabletop pan (flat characters in front of a model set turning in depth) | The world is a real place | a street; a carousel; a factory floor |
| Pull-back from a close-up to a packed medium-full | One feeling spreads to everyone | a celebration; a crowd joining in |
| Iris in / iris out (grabbable by a character) | The film is an object | a beginning; an ending; a scene change with a gag |

Framing: faces must read, so no far-wide shot for a gag or a musical moment. The destination prop enters frame before the gag lands. Arcs and leaps stay inside the gate at the current zoom. Transitions: iris, a hard cut on a beat, a title card rolling up like a window shade; no dissolves.

## 7. Sound palette

- **1930s hot dance band / ragtime**: stride piano, clarinet, trumpet (open + plunger-mute "wah-wah"), trombone (smears), tuba oom-pah, banjo on 2 & 4, snare with brushes and rolls, xylophone, woodblocks, slide whistle, cymbal, kazoo, washboard, a pit organ. **No string pads, no modern synths.** One short original syncopated theme can be restated in different arrangements.
- **Mickey-mouse the score, as options**: a band member "answering" a character (trombone raspberry, trumpet laugh); a stop (hard silence, reverb tails too) before a gag or on a stare; a stinger per gag; slide whistle for every stretch or fall; a prop that *is* an instrument; a solo for tenderness; a key change for a lift.
- **Foley by material** (synthesised): porcelain and glass = hard inharmonic partials + a tiny transient; wood = woodblock; metal = bells and clanks; springs = "boing"; water = filtered noise + rising blips and bubbles; rubber = sawtooth creak through a band-pass.
- **Voice**: a period character (a radio announcer calling the action, a vaudeville MC, a crooner), few short lines. Radio chain: HP ~260 Hz / LP ~4.6 kHz, tanh saturation, a short room, compression. Duck the music ~8 dB.
- **Optical soundtrack pass** over music + foley: band-limit ~110 Hz–6.2 kHz, slight wow (~0.6 Hz) and flutter (~7 Hz), soft saturation; then a bed of hiss, crackle and a 24 Hz projector gate clatter, the *only* sound allowed inside a silence.
- Loudness −14 LUFS (two-pass loudnorm in `core/render/mux.sh`).

## 8. Native moves

A menu: use the ones your story needs.

- **Everything breathes on the beat.** The setting is a character; at the peak the *whole world* can dance in sync, walls included. *Fits content like:* a factory at shift change; a garden after rain; a city waking up.
- **Mickey-mousing.** Every step is a note; a prop becomes an instrument. *Fits content like:* stairs as a piano; a typewriter as a drum kit; fence posts as a xylophone.
- **Rubber-hose stretch.** Limbs reach any length in one unbroken shot. *Fits content like:* reaching a top shelf; a long-distance handshake; catching a falling baby bird.
- **Transformation.** Anything becomes something else mid-motion (a tail into a question mark, a hose into a saxophone). *Fits content like:* an idea turning into a product; a problem into a tool; a word into an object.
- **The bouncing-ball singalong.** Lyrics on a title card, a ball hopping from word to word on the beat. *Fits content like:* a jingle; a safety rhyme; a slogan to remember.
- **The film is a physical object.** Title cards roll up like window shades; the iris is grabbed and pulled shut; intertitles get bumped; the frame line slips. *Fits content like:* a brand reveal; a "the end?" twist; a character escaping the cartoon.
- **The ink bottle.** An artist's pen draws the hero, who then argues with it. *Fits content like:* a making-of; a mascot introduction; a lesson about drawing.

## 9. Pitfalls of the medium

- **Flat grey frames.** Push backgrounds to mid grey, keep pure white and ink for characters, add a contrast boost.
- **Wide shots kill gags**: a far shot makes characters tiny and Mickey-mousing unreadable. Use medium shots, and a packed medium-full for crowds.
- "Sad" brows drawn as "angry": define brows by inner / outer end (inner = near the nose), not by left / right.
- A limb drawn behind a body gets hidden by the silhouette (a handle, a tail): kick and reach outward past it.
- Painted characters collide with background props at some camera positions: check every shot's last frame.
- Smoke puffs in a row read as thought bubbles: scatter and grow them.
- Short voice clips make subtitles flash: merge consecutive lines into one card.

## 10. Engine

In `demo/`: `toon.js` (constant-width ink, line boil, affine stack), `film.js` (gate and film damage, reusable as is), `chars.js` (rigs, pie eyes, gloves, shoes), `cast.js` (breathing props), `bg.js` (cached watercolour backgrounds), `ui.js` (title lettering, title-card subtitles), `mix.py` (foley, radio chain, optical ageing), `music/score.py` (big band via `core/audio/sampler.py`). File map and commands: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the location (or several), the cast, the structure, the opening, the ending, the camera path, the tempo and the band's line-up. All far from our demo:

- Structures: **a singalong** (verse and chorus, the bouncing ball carrying the message while the set acts out each line); **a talent show** (objects take turns on a stage, the smallest wins); **a relay** (a thing passed hand to hand across a town, each hand-off a new instrument on the melody).
- Openings: **out of the inkwell** (a pen draws the hero, who hops onto the set); **a curtain rise** (the band tuning up; a baton starts the film); **an iris on one eye** (it blinks, the iris widens to show whose eye it is).
- Endings: **the card pulled over** (a character drags "The End" in front of itself mid-gag); **the film snaps** (the frame burns, a gloved hand splices it for one last bow); **the band packs up** (instruments leave until one note remains).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: cel-anime-80s -->

# 80s Cel Anime — Style Prompt

> Hand-painted cel animation from the golden age of Japanese OVAs, re-created in code: flat two-tone cels over airbrushed backgrounds, backlit neon, limited-animation timing, played back as a late-80s videotape on a CRT television.
> References (grammar only): 1980s Japanese OVA and TV cel animation in general (painted-background vs flat-cel contrast, backlit light, held drawings, speed grammar, city-pop openings). Borrow the era's craft, never a specific work's characters, mecha, logos, place names or signature shots.

## 1. Essence, and what it is not

Four layers, and the contrast between them is the look:
- **Background painting**: soft airbrushed gradients, glowing windows, wet reflections; painted once at load (colour + emissive pair), then only slid.
- **Cel** (characters, vehicles, props): flat fills, **hard-edged** shadow and highlight shapes, **coloured** outlines, never pure black; stepped at 12 or 8 fps.
- **Light**: backlit cel (透過光): signs, lamps, title letters glowing *through* the frame; flares, halation.
- **Playback**: videotape on a CRT: chroma bleed, scanlines, grille, phosphor glow, darkened corners, faint noise.

If a frame looks like modern digital anime, one layer is missing. Not moe anime (round eyes, giant irises, hatched blush), not vector clip-art (uniform black lines, gradients in shapes), not a film-print pastiche (no gate weave or scratches: this is tape).

## 2. Materials & rendering

**Cel rendering.** Fill, then a **hard** shadow crescent, then a **hard** highlight crescent, then the coloured outline. No gradients inside a cel shape (exception: one "harmony" painted still at a peak). Automatic shading: clip to the shape and fill `shape − shape shifted toward the light` with the shadow colour (even-odd); the same shifted away for the highlight and for a saturated neon **rim light** (2–4 px). Add hand-placed cast shadows. Outlines ~2–3 px at 1080p, scaled down (0.45–0.8×) in extreme close-ups. **Colour models per lighting** (色指定): define each character in daylight, derive other sets by multiplying lit / shadow / line separately, plus a backlit silhouette set with a warm rim.

**People the 80s way.** Construct the head (sphere + jaw): long egg-shaped face, soft-point chin, far eye foreshortened with a cheekbone turn in 3/4. **Almond** eyes near the vertical middle of the head, a thick upper lash line flicking outward, a tall oval layered iris, two highlights, long thin brows. Nose = a shadow plane + one stroke; one faint blush layer, never hatched. Hair in overlapping locks with sharp uneven tips over a wider dark under-layer, a continuous "angel ring" highlight with a zigzag lower edge. Lines: skin thin warm dark brown, hair dark purple; only hard props near-black. Emotion lives in brows, lid height, iris size, mouth corners and shoulders. Build and approve a **model sheet** first; draw every shot from the same head function.

**Backgrounds.** Painted once at load: sky gradients, airbrushed clouds with lit undersides, buildings or landscape with painted light sources, and always a matching **emissive plate** that slides with the colour plate. Wet ground = a flipped, blurred, streaked copy of the plate darkened with ripple bands. Generic sign words only, never brands. Moving plates get a light horizontal smear (~16 px) against strobing.

**Light and lens.** Bloom strongly from the emissive canvas, weakly from the colour canvas above ~0.9; tint the widest bloom red-orange (halation). Flares: star-burst, anamorphic streak, hexagonal ghosts through frame centre. Stamp every cel's silhouette in black onto the emissive canvas so glow never bleeds through it.

**Videotape + CRT, restrained and deterministic:** chroma bleed (sharp luma, horizontally blurred and slightly shifted chroma), fine scanlines anchored to output pixels whose gap shrinks on brights, a faint RGB grille, phosphor glow, darkened corners without curved borders, faint signal noise. Subtitles are composited inside the pass after grading. Two optional accents: a **power-on** (dot → line → picture) and **tracking noise** (a few frames of tearing, rolling band, vertical hop). Check moiré on a 720p downscale. Frame: full 16:9 as a theatrical feature (4:3 pillarbox is valid for an OVA feel).

## 3. Colour logic

- Painted plates carry gradients and atmosphere; cels are flat, few-colour, saturated. Each time of day gets its own colour model, never a filter over the frame.
- The protagonist has **one accent colour** that pops in every lighting set. Line colours are dark versions of their fill.
- Skin gets its own colour in every set; multiplying daylight skin by a tint turns faces pink under neon.
- Examples: night city (indigo, violet, neon magenta, cyan, window gold); seaside noon (cobalt, white cumulus, sand, coral); classroom dusk (amber, chalk green, brown wood, purple shadows).

## 4. Type & subtitles

- Subtitles live on the tape, composited inside the CRT pass: a semi-condensed sans (e.g. Barlow Semi Condensed 600, ~50–56 px), cream-yellow with a thick dark outline and soft shadow, ~96 px above the bottom; a second speaker may take a second colour and a small boxed tag. Hold ≥ max(1.8 s, speech + 0.6 s); a line yields to the next.
- Titles: heavy italic Latin in a **chrome gradient** (sky → white horizon line → violet → pink → gold), dark + neon outlines, optional katakana line (e.g. Dela Gothic One), glowing through the emissive layer, flickering on at 12 fps with a light sweep and a star glint.

## 5. Motion quality

- **Characters on twos (12 fps)**; performance beats (blinks, eye openings, lip flaps, gestures) on threes (8 fps). Camera, light sweeps, flares and rain on ones (24 fps); a stepped camera judders.
- **Cycles**: hair and cloth as ribbons driven by a travelling sine, 4-drawing cycle (6 when calm); bounce = a 12 fps jitter of a few px.
- **Move light, not drawings**: coloured bands sweeping across a held cel (`source-atop`).
- **Impact frames**: 2 frames of an inverted or monochrome silhouette over radial lines, then the result.
- **Hold the peak**: a painted still with a slow pan, only cycles moving.
- Fast blinks (one 8 fps closed drawing); eye openings in three drawings; lip flaps of 3–4 shapes at 8 fps ending on a held expression.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Multiplane crane over a tall plate | a world revealed layer by layer | arriving; descending into a place; rising above it |
| Side tracking, 3–4 parallax layers | steady momentum | a journey; a chase; progress |
| Rear view into a pseudo-3D canyon | speed, pressure ahead | a race; a tunnel; a countdown |
| Held bust with light bands | speed or tension without animation | a drive; waiting; a decision |
| Insert with bokeh and a sliding highlight | this object matters | a letter; a key; a ticket |
| Extreme close-up on eyes | resolve, recognition | a choice; a promise |
| Slow pan across a painted still | awe, a held breath | a peak; a memory; a landscape |
| Radial speed lines + one-beat freeze | the instant before impact | a leap; a collision; a goal |
| Truck-in through a window or screen | entering another world | a flashback; a broadcast; a dream |
| Locked two-shot with lip flaps | conversation | banter; a confession; an argument |
| An earlier composition repainted | what changed | after a storm; years later |

Cut on bars. Framing: cels readable against the painted plate; keep the lower ~120 px clear for subtitles. Transitions: cuts, white flashes, impact frames, tracking noise at a tape-related beat; no digital dissolves or wipes.

## 7. Sound palette

- **Instruments** (city pop, synth funk, anime-opening pop): saxophone or synth-brass lead, FM electric piano with a bell transient, slap bass, chorus-y 16th guitar chanks, gated-reverb snare and big toms, drum machine, arpeggiated analog synth, string pad, FM bell sparkle. Extended jazz-pop harmony (maj7, 9ths).
- **Techniques, as options**: band-pass the score to cassette/AM when a diegetic source plays, then open it; a brass hit on a title; a drum fill left open for an effect; one beat of true silence before a peak; a semitone lift for a last chorus.
- **Foley** (synthesized): engines from an RPM curve, rain, tire hiss, wind, bells, radio squelch, impacts, sparks, cassette clicks, crowd murmur, door buzzers, footsteps on wet pavement; tape accents get their own thunk, whine, hiss.
- **Voice**: an English-dub feel, short lines; a second voice through a phone/radio band-pass (~380–2800 Hz). Verify every line with whisper.
- **Mix**: limit then compress TTS, voices ~10 dB over ducked music (duck ~9 dB), beds ducked ~3 dB, choruses louder than intros, two-pass loudnorm to −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.


<!-- END STYLE PAGE -->
