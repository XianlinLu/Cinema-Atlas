# Complete style specifications 12


<!-- STYLE: whiteboard -->

- **Every stroke sounds**: band-passed felt-on-gloss noise (a hiss band ~2–7.5 kHz + body ~0.5–1.5 kHz) enveloped by the stroke's own speed curve, a tiny nib tick at the start, stick-slip grains, and on some long strokes the **dry-erase squeak** (a 1.5–2.6 kHz sine with 7–13 Hz vibrato). Each colour sounds slightly different. Pan = the stroke's screen x; closer camera = louder.
- **Props**: magnet on steel = click + metal modes + a low board thump; eraser = felt rub modulated by its zig-zag; cap off/on; marker tray bounce.
- **Room**: low room tone; a single diegetic ticker (a wall clock, a fridge hum, a projector fan) can own a silence.
- **Music** options: a solo piano figure; a small jazz trio with brushes; plucked strings and kalimba; a synth arpeggio for tech topics; clockwork minimalism (marimba, pizzicato, woodblock, glockenspiel). Mickey-mouse details: a rising whistle for growth, pings for signals, a harp run for a fall.
- **Techniques to pick from**: adding one instrument per step of a mechanism; a key change when the frame of reference changes; a full stop into silence before a surprise; the previous cue reversed and squeezed for a rewind; two copies of one figure at two tempi (phasing) for anything that diverges, snapping into unison when resolved.
- **Mix**: voice on top (compressed, light room), music well under voice and ducked further under speech, foley ~11 dB under voice; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Writing in stroke order.** The reveal is the explanation: a formula term by term as it is spoken. *Fits content like:* compound interest; the Drake equation; a recipe's ratios.
- **The pen leads the camera.** Transitions are drawn lines the camera rides. *Fits content like:* a nerve signal; a supply chain; the water cycle.
- **Magnets.** The only things allowed to move on a board: give the hero to a magnet; slide, lift, drop, sink it. *Fits content like:* a delivery truck on a route; a cell in a bloodstream; a player on a pitch.
- **The eraser rewinds.** Wiping a trail backwards reads as undoing time. *Fits content like:* an undo in software; reversing a chemical reaction; "what if we hadn't…".
- **Two pens at once.** A live duet comparing two quantities. *Fits content like:* two savings plans; two runners; a population vs its food supply.
- **Ghosts of the old lesson.** A faint previous drawing becomes relevant. *Fits content like:* a theory replaced; last year's forecast; a first draft.
- **The full-board view.** Every region seen at once as one picture. *Fits content like:* a system diagram; a history; a map of a field.

## 9. Pitfalls of the medium

- **One pen, too many jobs** drifts later and later → give each drawing a deadline window and let overlapping jobs go to another pen.
- **Minimum stroke duration × many dashes** makes a dashed line take seconds → dashes need their own floor.
- **A pooled-ink dot bigger than the stroke start** leaves halos on every letter → keep it inside.
- **Punctuation vanishes** (a font period is a 1 px stroke) → render sub-width strokes as dots.
- **Labels half-cut by a push-in** look sloppy.
- **Motion blur with few sub-frames** strobes text.
- **Eraser paths** crossing labels you want to keep.
- **Voice and phoneme set mismatch** (a British voice with US phonemes) mispronounces → match the language code to the voice; ASR-check.

## 10. Engine

`demo/engine/wb.js`: hand-drawn shapes (`line`, `curve`, `poly`, `arc`, `circle`, `rect`, `arrow`, `dashed`, `hatch`), `text()` in writing order from a single-line font (`loadFont`), `Stroke`, floating `Pen`s, `Timeline.draw(pen, shapes, t, {by})` (solves hand speed to a deadline), `Timeline.erase`, `Timeline.cue`, keyed `Camera`, `Board` (ink multiply, dry texture, erasers, sheen, props), prop drawers. API table and a minimal example that draws something new: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the topic's object, the board layout, the colours within the logic, the voice, the music family, the camera route, the opening, the ending and the length.

All far from our demo:

- Structures: **a proof** (one claim at the top, the board fills downward step by step, each step boxed when proven); **a debate** (two pens, two halves of the board, each drawing its side until the drawings meet in the middle); **a timeline** (one long horizontal line ridden left to right, with events hanging off it).
- Openings: **a question mark** drawn huge in the centre, then shrunk to become a dot in the first diagram; **an erased board** where the ghost of a wrong answer is still visible; **a magnet dropping** onto an empty board with a clack.
- Endings: **the answer circled** twice and the pen capped; **the board wiped** except for one line that survives; **a push into the smallest symbol** on the board, which becomes the title.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: urban-sketch -->

# Urban Sketch · Pen & Wash — Style Prompt

> A sketchbook page drawn on location: fine sepia fineliner lines that wobble, overshoot and never quite close, with loose transparent watercolour dropped on top. The colour sits slightly off the lines, spills over them, and dissolves into cream cold-press paper at the page edge.
> References (grammar only):
> - Urban-sketching sketchbook pages: line first, then wash; colour off-register; handwritten date and place in the corner; the page edge breaking up into dabs.
> - *Paperman* (2012): a monochrome world with one coloured object.
> - *The Red Balloon* (1956): an object as the protagonist, the camera following it across a city.
> - Jazz waltz (the Vince Guaraldi school): 3/4 swing, walking bass, brushes, a woodwind lead.
>
> Nothing is copied from these: no characters, melodies, layouts or type.

## 1. Essence, and what it is not

Reportage drawing, made on location in a few minutes. Two layers that stay visibly separate:

1. **Ink.** One thin, near-constant line (a 0.3–0.5 mm fineliner) in dark sepia. It wobbles slightly, overshoots corners by a few pixels, breaks mid-stroke, and suggests rather than describes: a few window marks instead of a grid, scalloped fragments instead of a whole tree outline.
2. **Wash.** Transparent watercolour glazed on top, **misregistered** by 1–3 px from the line, sometimes spilling past it, leaving paper white for highlights and figures (reserves). Dried edges are darker (pigment pools at the rim), and pigment granulates into the paper tooth.

**The page is part of the image**: warm cream cold-press paper with large-scale mottling and fine tooth. Nothing is painted edge to edge; the painting frays into leaf-sized dabs and white holes, leaving margins for handwriting.

Not Watercolor Brush (no line-free wet-in-wet painting, no painterly edges without ink), not Whiteboard (no marker, no explainer diagrams), not Chinese Ink Wash (no brush calligraphy, no monochrome ink tones). Line and wash, both, always.

## 2. Materials & rendering

- **Paper**: two octaves of fbm mottling (a few %), a tooth tile multiplied over everything, figures included.
- **Ink**: ~96 % coverage; world line width thinner far, thicker near (e.g. 1.3–3.4 px); wobble ~1 px; overshoot 3–8 px; a third to half of long strokes get one small gap. Strokes are baked with their **draw time per pixel**, so the shader plays back stroke order.
- **Wash**: 2–3 rough-edged layers, multiply, alpha ~0.4–0.65, offset from the line by about one line width, a dried edge at 30–40 %; granulation = pigment × (0.82 + 0.36 · fbm).
- **Colour arrival field**: every pixel has a time at which colour reaches it. The wash is revealed through it with a ragged wet front (darkened band just behind the front) and noisy edges. Figures bloom from a point with a noisy circular clip.
- **Foliage**: pale base wash, then light and shadow masses, then small leaf dabs coloured by light direction, holes at the rim, scalloped ink only on the outline.
- **Sky**: a few big soft washes at low alpha, fading upward; clouds are reserves with a tinted belly.
- **Buildings**: local colour; shadow side mixed ~45 % with a cool violet-grey; distant blocks mixed ~50 % with a haze colour.
- **Figures**: a 3D skeleton in orthographic projection; torso from cross-sections; limbs as organic tapered tubes; hair and head as one mass; face left blank (one nose tick in profile); shadow side mixed with violet.
- **Page edge**: a noisy boundary, a white-dab band inside, a coloured-dab spray outside.
- Deterministic: same seed, same marks.

## 3. Colour logic

- **Ink is one colour** (dark sepia or warm black); it never changes.
- **Wash is local colour, lightly**: few pigments, mixed on the page; shadows are the local colour mixed toward one shared cool violet; distance mixes toward one haze.
- **Paper white is the brightest value**; it is reserved, never painted.
- **Colour can be withheld**: a page may be ink-only with colour as an event (one tinted object, colour arriving with a cause).
- Example palettes: park in summer (lawn `#c3c96f`, leaves `#7fa04a`, sky `#9fbcd6`, limestone `#d8c6a0`); harbour morning (sea `#7fa6b8`, hulls `#c9573f`, rope `#c8a86b`, sky `#bcd0dc`); winter market (roofs `#8b93a6`, lights `#e2b04a`, awnings `#b8483e`, snow = paper).

## 4. Type & subtitles

- **All text is handwriting on the page**, written on left to right with pen sound, and moves with the camera: a corner note (e.g. Reenie Beanie: day, time, weather, place), titles and colophon in a casual hand (e.g. Caveat 500–600), left-aligned in the blank margin.
- **Subtitles**, if there is a voice: handwritten lines in the page margin or a caption strip written into the lower margin, never a generic overlay box. Hold ≥ max(1.8 s, speech + 0.6 s).
- The style works well without any voice.

## 5. Motion quality

- **Figures boil at 12 fps** (line wobble and wash seeds change every 1/12 s). The static page does not boil (it is a real page); the camera moves every frame, smoothly.
- **Performance**: anticipation, action, follow-through; footsteps on the beat.
- **Invisible forces are drawn**: wind as ink curls that draw on and erase from the tail, trailing dabs; sound as ink lines; heat as wavy strokes.
- **Colour never snaps**: it blooms from a point or arrives through the field.
- Stroke-order draw-on for anything that "appears".

## 6. Camera grammar

A 2D camera over a large page (e.g. 5120 × 2880). Designed moves use cubic easing; follow shots use a critically damped spring on a lead-ahead target, so the camera lags like a hand-held follow. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Push-in | attention; a detail observed | a face; a sign; a small event |
| Lateral follow on a spring | travel, pursuit | an object carried; a walker; a vehicle |
| Crane up | a new level, a view opening | a skyline; a tree; a balcony |
| Whip-tilt with slight roll | sudden change of direction | a fall; a gust; a surprise |
| Punch-in with a short shake | impact | a catch; a collision; a door slam |
| Pull back to the whole page | scale; the sketch as an object | a summary; a place in full |
| Tilt into the margin | from picture to words | notes; a date; a title |
| Slow pan across a line-only area | the world before colour | a quiet start; memory |
| Hold while the pen draws | the act of noticing | a subject being drawn |
| Page turn to a new spread | another time or place | a travel diary; a sequence of days |

Framing: subjects ≥ ⅓ of frame height at story beats; a small key object gets a faint paper halo (reserve) so it reads over busy foliage. Transitions: camera travel on the page, page turns, or colour arriving; no dissolves.

## 7. Sound palette

- **Ambience from the place**: paper room tone first, then the location once it has colour (birds, traffic, harbour gulls, market chatter). J-cut a place's sound a bar before we see it.
- **Pen on cold-press paper**: band-passed noise (~1.6–7.5 kHz) with a fibre texture and grain clicks, one burst per real stroke; thousands overlap into a hiss during a fast sketch; brighter short strokes read like a hi-hat.
- **Water and brush**: a wet brush "shhh" for blooms, a jar rinse, a drip.
- **Foley follows objects** at sketch scale: fabric or paper flapping for things in the wind (rate and level from speed, pan from screen x), steps on the beat, bells, splashes.
- **Music families**: a jazz waltz (walking bass in three, brushes, piano, clarinet or flute); a café accordion trio; solo nylon guitar; a string quartet pizzicato; a brass band for crowds. One colour instrument per area of the page works well.
- **Silence as a tool**: a bar of true silence (ambience included) at the height of suspense; the first sound after it is the next gesture.
- **Mix**: music ducks under key hits; foley high-passed ~90 Hz; −14 LUFS, moderate LRA.

## 8. Native moves

A menu: use the ones your story needs.

- **Line before colour.** The pen draws a subject in real stroke order, then the wash drops in; the drawing is the spectacle. *Fits content like:* a cathedral façade; a chef plating a dish; a street musician.
- **Colour as arrival.** Wash spreads from a source with a wet front, so an event paints the page; figures stay frozen line drawings until colour touches them. *Fits content like:* a sunrise over a harbour; a parade moving down a street; the lights of a market switching on.
- **The one coloured thing.** A colourless sketch with a single tinted object that becomes the protagonist. *Fits content like:* a red umbrella in the rain; a yellow taxi; a child's kite.
- **The page as frame.** Pull back until the whole page shows, edges dissolving, handwritten notes in the margin. *Fits content like:* a travel diary entry; a neighbourhood portrait; a day in a place.
- **Carrot people.** Distant crowds as one wash blob, two leg lines and a head dot. *Fits content like:* a station at rush hour; a stadium; a beach.

## 9. Pitfalls of the medium

- **Straight edges in the colour field** from clipping by a bounding box → clip by the actual noisy distance.
- **Rectangular masks around complex silhouettes** leave notches → mask with the real stepped silhouette.
- **Characters losing colour** when they move into unpainted areas → sample arrival once (or tie it to the event), never at the current position.
- **Static ink can't be occluded by later washes** → erase far ink inside nearer shapes before drawing; use carrot people for far crowds.
- **IK feet pinned while blending poses** splay the legs → blend foot targets toward under-hip.
- **Front-facing heads go bald** → draw the hair mass, then knock the face out of it.
- **Big canvases in headless Chrome**: pack ink and time into RGBA byte textures yourself and upload the arrival field as a filterable float texture (`R16F`).
- **Painting edge to edge** kills the sketchbook feel → leave margins and fray the edge.

## 10. Engine

`demo/engine.js` (deterministic): `penStroke` + `drawPen` (fineliner with wobble, overshoot, gaps, draw-on), `rasterPen` (bakes stroke order into an ink + time layer), `wash`, `reserve`, `dab` / `foliage`, `arrivalField` (colour arrival per cell from sources), `compositor` (WebGL page: paper × wash revealed by arrival × ink revealed by stroke time), `figure` + `drawPrims` (sketched people), `sketchShape` (any shape in this style in one call), `handwrite`. `demo/poses.js` holds a pose library. API table and a minimal example that draws something new: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the place, the subjects, what colour does (always there, withheld, arriving), the voice (or none), the music family, the camera path, the opening, the ending and the length.

All far from our demo:

- Structures: **a travel diary** of five pages, one per day, each page turned by the wind or a hand; **a single street corner** drawn at four times of day, the wash changing while the ink stays; **a recipe** where each ingredient is drawn from life at the market and the final dish is painted last.
- Openings: **the blank page** with only the handwritten date, then the first line of the horizon; **a close-up of a coffee cup** on the page's edge, pulling back to find the city drawn behind it; **rain dots** landing on the paper and blooming into the first washes.
- Endings: **the sketchbook closes** on the page; **the last figure walks off the page** into the blank margin; **the colour drains** back to ink as the evening comes, leaving one lit window.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: shadow-puppet -->

# Shadow Puppetry — Style Prompt

> Chinese shadow theatre: translucent dyed-hide puppets, carved like lace, pressed against a cotton screen and lit from behind by oil lamps.
> References (grammar only): Lotte Reiniger's *The Adventures of Prince Achmed* (1926) for profile acting and lace-like scenery; Shaanxi / Huayin shadow theatre for carving, colour and gong-and-drum rhythm. Never reproduce a specific historical puppet, melody or recording, and never name them in the film.

## 1. Essence, and what it is not

A white cloth screen; behind it, flat puppets cut from **translucent dyed hide**, lit by an **oil lamp**. Colour arrives *by transmitted light*: dyes glow like stained glass, carved holes shine brightest, overlaps go darker. Puppets are jointed with **visible thread rivets** and moved by **thin rods** (neck and hands) that show as soft grey lines just off the screen. It is live theatre, not stop-motion: the screen **flickers with the lamp**, puppets **tremble in the hand**, loose parts **swing on their rivets**.

Not a black silhouette film (colour is the second protagonist), not paper-cut (the light comes *through*), not stained glass (no lead lines; pieces move and overlap), not flat vector cut-out animation.

## 2. Materials & rendering

**Rendering model.** Per pixel: `image = tonemap( lampLight × hideTransmission × clothTexture )`.
- `hideTransmission`: a 2D canvas that starts **white**; every piece is drawn with `multiply`. Holes stay white, overlaps darken by themselves.
- `lampLight`: per lamp a broad lobe plus a tight hotspot (~6 : 1), each flickering independently (a few % of ~7 Hz value noise plus a faster sine). Warm light, never white.
- `tonemap = 1 − exp(−hdr)`, exposure ∝ `1/√(lamps lit)`: more lamps bleach the frame but keep it readable. Lamp count is a dial the story can turn.
- **Cloth**: procedural weave (sin × sin, noise-warped), fibre speckle, low-frequency density blotches, darker edges at the frame. **Post**: warm-tinted bloom, a **warm vignette** (toward brown, never grey), slight saturation, soft S-curve, light grain; heat haze only when the story burns.

**Hide and carving.** Multiply a tileable hide texture (mottling, fibres, specks) into each piece and restore its alpha with `destination-in` so holes survive. **Carving is density**: leave thin strips, cut out most of the area. Cut vocabulary: crescent rows (scales, tiles), diamond lattice, coin holes (round hole, square of hide inside), cloud collars and scrolls, tapered slits (cracks, rain, fur), strata along a ridge, leaf holes in a canopy. A dark carved outline (1.5–2.4 px) on every region. With `destination-out`, set `fillStyle = '#000'` first: fill alpha decides how much is cut.

**Figures are jointed puppets**: 8–12 pieces, head ~1.2× natural with large headwear, sleeves in a different dye from the torso, round joint lobes with a rivet (dark ring + pale knot), arms by 2-bone IK from hand targets, held objects as separate pieces on the hand line. Sympathetic figures have *open-cut faces* (features as thin strips around a hole); antagonists solid faces.

**Scenery** is carved set pieces on mostly empty lit cloth: one lace piece per element, a narrow carved ground strip, separate liftable strips for water or sky. Fire, smoke and moving water are carved pieces on rods, swapped and shaken, never particles.

**Stage and backstage.** A lacquered frame (lintel, pillars, warm spill on its inner edges), optional blurred audience heads. Backstage = the same transmission canvas with the camera mirrored (`x → −x`), dark wood around, hanging lamps (additive flame glow; snuffed ones trailing dark smoke), hands and sleeves as **silhouettes with a warm rim** (mask minus mask shifted away from the light), rods sharp.

## 3. Colour logic

- All colour is **transmitted**: a dye filters warm lamplight, so nothing is brighter than the lamp and every hue leans warm.
- 3–5 saturated dyes + **raw hide** (the neutral) + **ink** (outlines, hair, boots). Holes are the brightest value.
- Overlap is darkness: plan which pieces cross.
- Brightness comes from the number of lamps, not grading. Night is fewer lamps, never added blue.
- Thin things that must read (strings, shafts, text) are dark: pale pieces vanish on a bright cloth.
- Example sets: *court* (vermilion, ochre, malachite); *river* (indigo, jade, one ochre); *harvest* (flame orange, gold, one green).

## 4. Type & subtitles

- Subtitles belong to the theatre: a **storyteller's placard** (narrow dark-lacquer board, thin gold line, small carved seal), a label on a rod, or letters carved into hide. Classical OFL serif (e.g. Cormorant Garamond 600), 40–50 px, cream on dark, short slide in. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles are puppets**: dark hide plaques with letters cut out (`fillText` + `destination-out`, so words glow), a carved border, carried on rods, pressed on to enter, lifted off to exit.

## 5. Motion quality

- **24 fps continuous** for puppets and camera; only swapped effect pieces (fire, water) step at 12 fps.
- **Hand tremor** on every puppet (a few px, ~0.02 rad, low-frequency), stronger under tension.
- Body glides with the main rod; **legs, plumes, tassels are simulated** (damped pendulums / spring chains driven by body acceleration, pre-simulated at a fixed rate for determinism).
- Operatic phrasing: shuffling run → hop → crouch → **freeze pose on a percussion accent** (~1 s, only loose parts quiver) → head turn.
- Faces never change; attitude = head angle + body tilt (up = resolve, down = sorrow).
- **Press on / lift off**: arrivals come large and blurred onto the cloth and snap sharp (~0.5 s); exits grow, blur and fade (~1 s).
- A new lamp flares with overshoot; a snuffed lamp gutters with fast flicker.
- Never moves: the cloth, the frame. Nothing morphs: pieces rotate on rivets, slide on rods, or are swapped.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Audience seat (whole stage, heads below) | "This is a show" | a legend; a lesson; a framed memory |
| Push through the frame onto the cloth | Entering the tale | a story within a story; focus |
| Lateral pan across a wide cloth | Extent, a place laid out | a journey; a disaster's reach; a procession |
| Follow a puppet, slight zoom | Being with one figure | a pursuit; a working day |
| **Crash zoom** of a few frames on a percussion hit | The drum becomes the camera | an entrance; a pose; a reveal |
| Whip pan along a moving piece | Cause to effect | a message sent; a strike |
| **Locked wide** | Every step of a change is seen | counting; repetition; stages |
| Medium-close, empty cloth between two pieces | Distance, hesitation | a choice; a parting |
| Close on a carved detail | Craft as meaning | a vow; a tool; a clue |
| Tilt from ground strip to top of cloth | Height, hierarchy | a tower; heaven and earth |
| Truck round to the back (mirror view) | The trick revealed | behind the scenes; who pulls the strings |
| Pull back from cloth into the dark room | The tale becomes an object | aftermath; a story ending for the night |

Puppets in profile; most of the cloth stays empty. When zoomed in, clamp the camera to the screen rectangle (no black bars); push on frame centre unless diving into a lamp. Transitions: lamps dimming, a blurred foreground pillar wipe, a piece lifting off in light, a flash to warm white; never a generic crossfade or digital wipe.

## 7. Sound palette

- **Percussion first, not piano and strings** (gong-and-drum pattern thinking, 锣鼓经): low barrel drum, hard high clapper drum (woodblock), cymbals, small gong with rising pitch ("tai"), big gong with falling pitch ("kuang"); also a bamboo clapper board, pellet drum, sanxian pluck, a bamboo flute for quiet.
- **Bowed and reed voices**: a bright nasal fiddle (erhu-like: pitched up, nasal formant, pitch-curve resampling for slides and vibrato), plain pentatonic (**huan-yin**) or sorrowful microtonal (**ku-yin**: raised 4th, lowered 7th); a shrill suona-like reed (oboe + 1.2–3 kHz formant + saturation) at most once.
- **Techniques, as options**: a single tap inside a silence; one big gong per decisive hit; a heartbeat drum under dread; accelerating rolls into an entrance; one hit per visual step; a gong scrape to change space; a hard stop (≤ 30 ms, tails included).
- **Silence**: hard-cut the whole bed; at most one sound inside (a breath, a tap, a sizzle).
- **Foley follows the materials**: wooden clapper (醒木), match strike, lamp "fwoomp" and "pfft" + sizzle, rod taps on cloth, dry leather flaps on lift-off, leather steps, creaks of hide and wood props, leather thwacks, cloth rustle, backstage room tone.
- **Voice**: a storyteller, few short lines, small-theatre reverb; music ducked ~12 dB, foley ~4 dB, voice ≥ 12 dB above the bed; −14 LUFS; check each line with whisper alone and on the final mix.

## 8. Native moves

A menu: use the ones your story needs; put the strongest at the peak.

- **The light is the world.** Lamp count drives heat and colour. *Fits content like:* city lights spreading at night; a fever rising and falling; servers switching on one by one.
- **Off the screen = big and blurry.** A piece pulled toward the lamp grows and blurs. *Fits content like:* a rumour growing; a memory fading; a deadline pressing onto the cloth and snapping sharp.
- **Go behind the screen.** Lamp, hands, rods. *Fits content like:* how a product is really made; who controls a market; a teacher revealing the method.
- **Carved and translucent.** Holes glow, overlaps darken, open faces vs solid. *Fits content like:* an x-ray of a system; good and bad actors in a fable; layers of a city.
- **Hand-held.** Tremor and swinging parts. *Fits content like:* a nervous interview; a tightrope; a toddler's first steps.
- **Piece swap.** One carved piece on a rod replaced by another. *Fits content like:* seasons; a machine's states; weather over a harvest.
- **Strip lift-off.** A band of scenery lifted to reveal another. *Fits content like:* geological layers; before/after a flood; an old town under a new one.

## 9. Pitfalls of the medium

- Flat clip-art look → hide texture, denser openwork, deeper dyes, carved outlines everywhere.
- Figures unreadable in profile → bigger head, fuller lower body, collar piece, contrasting sleeves.
- Radiating shapes read as saw blades or petals → flame tongues with a fat base, belly and hooked tip, alternating curl.
- Grey corners when overexposed → warm vignette.
- Thin pale pieces vanish → make them dark.
- Mirror view flips pieces when rotation uses the x scale for both axes → x scale for x, y scale for y.
- Smoke with `lighter` is invisible on bright cloth → dark wisps, warm additive only near a lamp.
- Push-in centred on an edge lamp shoves figures out → push on frame centre.
- Beds leaking into a silence → hard-cut them.
- Headless screenshots time out under GPU load → retry.

## 10. Engine

In `demo/`: `carve.js` (piece sprites, `cut` / `cutLine` / `cutTaper`, pattern library, hide texture, rivets), `gl.js` (WebGL2 compositor: lamp field × transmission × cloth, mirror, bloom, haze, warm fade), `stage.js` (frame, audience, pillar wipe, cut-letter plaques), `backstage.js` (rim-lit silhouettes, flame, smoke), `hud.js` (placard), `scenery.js` (landscape pieces, ground strip, fire), plus the jointed rig with IK and pendulum parts; `?test=model|frame|hands` draws sheets from the real engine. A first test unlike the demo: carve a lantern-seller with a lattice basket, press it onto one lamp, light three more and watch the frame bleach.

## 11. Variation space

You decide the story, the figures (or none), what the lamp means, what leaves the screen, the opening, the ending, the camera path, the dyes and the pacing. All far from our demo:

- Structures: **a procession** (one long pan; each figure adds a dye until the cloth is a full street); **two puppeteers** (rival hands argue through their puppets; backstage shows who is winning); **a workshop** (a puppet is carved, dyed and riveted on the cloth, then performs its own making).
- Openings: **backstage first** (rim-lit hands and rods before the front); **one hole of light** (the screen all dark hide; one carved hole glows and widens); **mid-show** (the camera finds a performance already in full percussion).
- Endings: **the lamp is carried away** (the cloth darkens from one side); **the puppets rest** (lifted off one by one, laid flat on a dim table); **the audience leaves** (the heads stand and go, the cloth still glowing).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- END STYLE PAGE -->
