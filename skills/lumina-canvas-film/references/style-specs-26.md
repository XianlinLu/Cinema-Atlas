# Complete style specifications 26


<!-- STYLE: blueprint -->

- **Camera and draw-on on ones (24 fps).** Continuous moves within a section, hard cuts on downbeats between sections; tiny camera bumps only for physical impacts (paper slap, stamp).
- **Draw-on** truncated by arc length with a glowing nib at the head; items staggered within a layer; each layer starts on a beat.
- **Drafting order**: centre lines → outlines → detail → hatching → dimensions → balloons → labels.
- **Exploded views**: parts leave in sequence on subdivisions of the beat, eased, and return one per beat-group with a click.
- **Mechanisms step on the grid** like an escapement: a gear advances one tooth per subdivision with a short ease-out; meshing phases computed so teeth really interlock; chains move with their sprockets.
- **Machine acting**: angles, droops, volumes and gauge needles are the face. Failure = slowing, sagging, winding down over ~1.5 s; joy = snapping upright, a needle overshooting (back-ease).

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Whole sheet on the table | scale, the document as an object | establishing; a verdict; a series of sheets |
| Medium on a figure, subject ~80 % of height, sky on one side | the design being drawn | drafting; explaining a part |
| Track along a path of force (chain, pipe, wire, beam) | cause and effect | how it works; a sequence of operations |
| 2× close-up cut on a downbeat | the mechanism's heart | gears meshing; a valve; a joint |
| Locked-off, hold a beat | deliberation | a hand revising; a decision |
| Oblique depth factor 0 → 0.5 | the flat drawing "turns" and gains thickness | from plan to object; a reveal of depth |
| Section line sweeping across | inside vs outside | a cutaway; hidden structure |
| Lateral pan across Fig. 1 → Fig. 2 → Fig. 3 | versions, steps, time | revisions; stages of construction |
| Slow push-in, no voice | wonder | the one real thing |

Keep storytelling shots close; full-sheet wides are rare. Keep the main figure at least `960/zoom` from any sheet edge you will frame. Transitions: cuts on downbeats, or fig-number rewrites on the sheet; no dissolves.

## 7. Sound palette

- **Contrapuntal, mechanical music**: harpsichord, bassoon, strings spiccato, harp, celesta, music box, clavichord, a small wind ensemble. Imitative lines (an invention, a canon, a fugato) feel like interlocking parts; a short repeated motive can be the "gear".
- **Foley follows materials**. Paper: roll crackle and slap, T-square wood slide, technical pen scratch (2–6 kHz grain, length = stroke length), lettering bursts, compass squeak, hatching strokes, eraser rub, tracing-paper rustle. Brass and wood: part clicks (resonances ~3–5 kHz), escapement ticks, chain rattle, spring twang, wind-down ticks that slow geometrically. Water: soft damped pats per drop, a light rain bed. Rubber stamp thump, pen cap click.
- **Options for the arc** (in any order, use what the story needs): instruments dropping out with a written-out ritardando into true silence; a single questioning figure alone; a suspended chord held without resolution under the magic; a full cadence on the stamp; the theme in augmentation for a close; adding a section per mechanism that joins.
- **Silence** may contain paper sounds only.
- **Voice**: dry, understated, reading design notes, a few short lines. Leave the most emotional moment voiceless.
- **Mix**: music ducks well under voice (~0.36 ×), foley by half; whooshes low-passed so they don't mask consonants. −14 LUFS. Little added grain (the paper already has it).

## 8. Native moves

A menu: use the ones your story needs.

- **Drafting order.** The object draws itself as an engineer would, a layer per beat. *Fits content like:* a bridge; a violin; a kitchen renovation.
- **Live annotations.** Dimensions measure moving parts and the numbers change; balloons fly with parts; a section line reveals the inside. *Fits content like:* a heart valve; a folding bicycle; a rocket stage separating.
- **Fig. numbers as transitions.** "FIG. 1" struck through and rewritten "FIG. 2 · EXPLODED VIEW". *Fits content like:* versions of a product; phases of a construction; a recipe's stages.
- **Projection as camera.** The oblique factor animates; exploded parts fly along the depth axis. *Fits content like:* a floor plan becoming a building; a circuit board; flat-pack furniture.
- **A symbol made real** (once, if at all). A convention leaves the drawing language: a dimension arrow flies, a hatch becomes rain, a centre line becomes a road, a weld symbol sparks. *Fits content like:* an invention finally working; a city plan becoming a street; a dream becoming a plan.
- **Cyanotype and water.** Drops bloom and soften lines. *Fits content like:* a flood-defence design; grief; a harbour wall.
- **The title block as story.** Status field = the verdict; revision rows = history. *Fits content like:* a rejected permit; REV. 1–5 of a city; an approval after years.

## 9. Pitfalls of the medium

- **Main figure near the sheet edge** → wides show the desk. Keep margins or enlarge the sheet.
- **Upward explosions hit the header** → explode sideways and flatten long parts during the explode.
- **Subtitles on the ink buffer** vanish off-sheet and can't occlude lines → separate overlay, premultiplied alpha.
- **An object darkened by its own shadow** → zero the shadow channel only in its area.
- **Per-lobe shading on a blobby shape reads as grapes** → one gradient across the union; crescents from a union-minus-shifted mask; fill unions as one path (`nonzero`) or overlapping fills make bubbles.
- **A small payoff undersells the return** → the payoff object ~⅓ of frame height, centred, drawn stroke by stroke, subtitles off it.
- **Line weights not scaled with zoom** → sausages in close-ups, vanishing wides.

## 10. Engine

`demo/paper.js` (WebGL2 compositor: procedural cyanotype, ink bleed, wet stains, shadows, stamp, roll), `demo/draw.js` (drafting engine: camera, oblique projection, draw-on polylines, solids with paper fill, hatching, dimensions, balloons, text), `demo/sheet.js` (border, header, title block, parts list, notes, revision cloud, rain, hand shadow, stamp), `demo/film.js` (timeline on a beat grid: cameras, acting, subtitles, sound events). A new machine goes in its own module like `demo/machine.js`. File map and build: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide what is designed, its figures, the flaw or turn (if any), the voice, the one real thing (or none), the camera path, the opening, the ending and the length.

All far from our demo:

- Structures: **a city through revisions** (one site plan, REV. 1 to REV. 6, each revision a decade, the title block filling with dates); **two sheets, one table** (two designs drawn in parallel that turn out to fit together); **a teardown in reverse** (the sheet starts full and parts are erased one by one until only the centre line of the idea remains).
- Openings: **a single centre line** crossing an empty sheet on the first beat; **the stamp first** (REJECTED lands, then we see what was rejected); **tracing paper** lifted off a finished drawing to reveal a blank sheet underneath.
- Endings: **the sheet folds up** along its creases into a pocket-sized square; **a coffee ring** lands on the title block and the tide line becomes the last circle of the design; **the lights go off** and the white lines glow faintly on the dark sheet.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: stained-glass -->

# Stained Glass — Style Prompt

> A medieval stained-glass window seen from inside a dark stone hall, alive only where the sun touches it: light is the clock, the camera and the story.
> References (grammar only): the window prologue of *Beauty and the Beast* (1991) (chapters pane by pane, a storyteller's pace); the glass knight of *Young Sherlock Holmes* (1985) (glass that cracks and recombines piece by piece); 12th–13th-century Chartres glass (colour logic, grisaille, leading). Copy none of their characters, compositions, subjects or music.

## 1. Essence, and what it is not

- **Cut pieces of coloured glass in dark lead cames**, faces and folds **painted in brown grisaille**.
- Glass has no light of its own: it **glows only when the sun is behind it** and throws a soft coloured copy onto the stone floor; unlit, it is dark and milky.
- Figures move **piece by piece**, rigid and stepped.
- The room is always there: stone, a splayed embrasure, iron saddle bars, a floor that catches light.
- **Secular**: no crosses, saints, halos or other religious imagery; borrow the craft, not the subjects.

Not vector art with black outlines, not a kaleidoscope or Voronoi filter, not Tiffany Art Nouveau, not mosaic (mosaic reflects; glass transmits).

## 2. Materials & rendering

One formula for everything (a WebGL compositor), so every element sits in the same light:

```
glass   = tonemap( backlight(x,y,time) × transmittance × glass texture ) + weathering haze × room light
surface = albedo × (room ambient + glow spilled from lit panes + point lights)          // stone, lead, iron
floor   = flagstones × (ambient + projected colour-patch map, blurred + halo)            // perspective or top-down
+ additive light shafts with dust · bloom (bright glass eats into the lead: the "irradiation" effect)
```

- **Hue-preserving tone mapping**: per-channel `1-exp(-x)` turns cobalt pastel; blend to per-channel only at the very top so a sun disc burns white while blue stays jewel blue.
- **Unlit panes**: weak sky light + room-lit weathering haze, figures ghostly but readable. **Lit panes**: backlight ~2–3×, a soft, slightly skewed moving band edge.
- **Pieces**: smooth Catmull-Rom cuts (no deep concave corners). **Every piece is textured** (`multiply` in its clip): streaks at a per-piece angle, hue drift (±10 %), darker aged edges by the lead, ±9 % thickness variation. The shader adds seed bubbles, scratches and thickness clouds in world space; fade small features below ~0.6× zoom or they sparkle.
- **Lead**: near-black, one planar network, thinner on small pieces, round joins, faint grey flange, solder blobs; only where colours meet (one colour = one piece).
- **Grisaille**: tapered trace lines in translucent dark brown; **matting** (stippled wash, graded shade, soft band inside the lead); **scraped highlights** (a thin stroke beside each fold in the piece's own colour: the only highlight transmitted light allows). Patterns (mail, scales, plates) are grisaille arcs and bands.
- **Faces**: almond eyes, heavy upper lid, big pupils, brow flowing into the nose. **Expression lives in brows and mouth**; change it by swapping the face piece, never morphing.
- **Backgrounds**: hand-cut **lozenge quarries** (jittered lattice, shared vertices, a painted motif each); borders of a coloured band with pearls and a white fillet with a running vine.
- **Room**: warm grey ashlar, a lighter embrasure, mullions; floor of **large irregular flagstones**, never the wall's running bond.
- **Floor projection**: blurred, ~20 % desaturated, modulated by the stone, haloed, mirrored (the window's top lands farthest into the room). **Shafts**: additive with dust, near 0 at the window, peaking ~40 % down.

## 3. Colour logic

- Two hues **carry the picture** (one deep, one hot); three or four more only as **small touches**. Example (Chartres logic): cobalt ground, ruby, touches of gold, green, murrey.
- Greenish white glass sparingly (faces, fillets, sky). **Flesh darker than you think**, or backlit faces burn white.
- A story light (candle, lamp, screen) may take a colour no glass uses, so it reads as a source.
- **The sun's colour is the clock**: blue-white dawn, near-white brightest noon, gold afternoon, deep orange dusk (raise intensity rather than redness), weak blue moonlight. Patch length follows sun height.
- Stone and lead take colour only from spilled or projected light.

## 4. Type & subtitles

- **Subtitles**: a parchment **banderole** near the bottom (curled ends, gentle sag, thin rule), IM Fell English ~44 px in dark ink. It unfurls from the centre; text fades in only once it is ≥ 75 % open; pad the ribbon well past the text. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: incised Roman capitals (Cinzel 600) in the stone, dark cut, light lower lip, gilding, revealed by a moving band of light; small lines ≥ 30 px on screen. In the glass, text only as grisaille on a white-glass scroll.

## 5. Motion quality

- **Figures step at 8 fps**; light, camera, shafts and dust move on ones (24 fps): stepped light reads as flicker.
- Rigid pieces on 2D FK (`setTransform(base · T(part))`, free draw order); long bodies are spine chains of banded pieces.
- **Freeze rule**: a pane's figures use `min(t, t_lightLeft)`. Actions land on the beat.
- **Crack**: jagged lines race from the impact in ~¼ s, bright with light, a short white flash and a 2-frame shake.
- **Re-leading**: piece groups slide one beat each with a small outward bump along the lead, each ending in a weld spark; cracks become mending leads.
- Glass never bends or morphs; things appear by being lit, not faded in.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Truck sideways with the band of light | Time passing, the story moving on | a sequence of steps; a day; chapters |
| Locked close-up on one pane | This panel is "now" | a line being read; a character's decision; a detail |
| Pull back to the whole window | The rule, or the whole story at once | learning the system; a summary; aftermath |
| Tilt down the shafts to the floor, then top-down | The picture leaves the glass and becomes light | an event too big for its frame; a dream; a memory |
| Hold through a crack, no cut | The event is the medium breaking | a turning point; a loss; a revelation |
| Slow push toward a small light | Attention narrowing to one source | a discovery; a secret; hope |
| Tilt up to a rose or tracery | Something above the panels governs them | a clock; a cycle; an overview |
| Rack between two panes, one lit, one dark | Past and present side by side | before/after; two lives; cause and effect |
| Low angle along the embrasure, glass raking | The window as architecture, scale | awe; an institution; a long history |
| Return to an earlier framing under new light | The rhyme shows what changed | growth; nightfall; repair |

Framing: subjects big (close-ups ~1.3–2.3× a lancet width); in a narrow lancet stack figures diagonally; a revealed thing near centre, ≥ ~1/8 frame width with glow. Transitions: moving light, shafts, a crack, darkness; never a dissolve, wipe or flip.

## 7. Sound palette

- **Instruments**: organ (pedal drone, soft stops, full), harp, hand chimes, tubular bells, recorder or a chant-like voice, water-glass notes, timpani; also hurdy-gurdy drone, psaltery, portative organ. No generic piano or strings.
- **Mode families**: church modes (Dorian, Mixolydian, Aeolian, Lydian), open fifths, drones, parallel organum.
- **Options**: free unmetred chant for darkness; one note meaning "the light" each time a pane wakes; an organ pedal that holds and then cuts out; a rising scale, one step per lit piece.
- **Foley, material first** (synthesizable): struck glass = inharmonic partials ~1 : 2.32 : 4.25 : 6.63 : 9.38; crack = snap + pane thump + rain of tinkles; lead = stick-slip creak; glass sliding in a came = gritty band noise + faint squeal; solder = hiss + tick; air on light moves; stone-hall ambience; birds in the vault; iron ticking as it cools.
- **Silence**: a hard stop, reverb tails included, only the glass's own ring or creak inside; a single long-reverb bell can close it.
- **Mix**: big and reverberant; heavy hits avoid word onsets; music ducked ~9 dB under voice; −14 LUFS. **Voice**: a gentle, even storyteller, few short lines.

## 8. Native moves

A menu: use the ones your story needs.

- **Light is time, and the camera.** Only the lit pane is alive; figures freeze when the light leaves. *Fits content like:* the steps of a recipe; a factory's shifts; four seasons of one farm.
- **Glass projects onto stone.** A key scene plays in the floor patch, which stretches as the sun sinks. *Fits content like:* a memory seen larger than life; a sports play replayed as shadows; a data trend drawn by lengthening light.
- **Glass cracks, lead mends.** Pieces slide along the leads into a new picture, leaving scars. *Fits content like:* a company's reinvention; an injury and recovery; an old building restored.
- **A window holds its own light.** At night one pane glows from a source inside the story. *Fits content like:* a lighthouse keeper; a night-shift nurse; a server that never sleeps.
- **The window as a diagram.** Lancets as columns, a rose as a wheel or dial, the border as a timeline. *Fits content like:* a product lineup; the parts of a cycle; a family tree.

## 9. Pitfalls of the medium

- Hidden leads show through front pieces → erase the surface under each piece before stroking its lead.
- Pastel glass → hue-preserving tone mapping; darker flesh. Red dusk × blue glass = mud → keep blue alive, raise intensity.
- Voronoi reads as a filter; flat fills read as clip-art → hand-cut lozenges, texture on every piece, heavy grisaille.
- A sharp floor patch looks like a decal → blur, desaturate, stone-modulate, halo. Shafts at full strength at the window wash out the pane.
- Top-down projection is flipped → put the wall at the frame bottom so figures stand upright (mirrored, correct).
- Patch-map canvas size mismatched with the code draws into a corner of the texture → one constant size.
- Carved text in a dark wide is unreadable → push in, park a light on it.

## 10. Engine

In `demo/`: `glass.js` (pieces, textures, lead, grisaille, lozenges), `comp.js` (WebGL2 compositor), `window.js` (lancets, rose, borders, wall, carving), `scene.js` (camera, floor projection, shafts, dust), `subs.js` (banderole), `test.js` / `frames.js` (model sheets and style frames from the real engine), `music/score.py`, `mix.py` (glass/lead foley). `knight.js` / `dragon.js` show the rigid-piece FK rig pattern; build your own subjects with it.

## 11. Variation space

You decide the window (lancets, a rose, a medallion, a clerestory), the subjects, the order of light, opening, ending, camera path and pacing. All far from our demo:

- Structures: **a rose window as a dial** (petals lit in turn like hours, the centre the answer); **one tall lancet read bottom to top** (a tilt up a life or a process, medallion by medallion); **two windows facing each other** (the sun lights one side in the morning, the other in the evening; the floor between them holds their meeting).
- Openings: **the floor first** (only a coloured patch on stone; tilt up to find its source); **a lit window from outside at night** (a figure passes a glowing pane, then we are inside); **the glazier's bench** (a single piece cut and leaded, becoming the first piece of the picture).
- Endings: **clouds cover the sun** (every pane fades to grey at once; one line lingers); **a new pane leaded in** (an empty lancet filled with the last scene); **the camera leaves through the door** (the window small behind, its patch still on the floor).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: pictogram-motion -->

# Pictogram Motion — Style Prompt


<!-- END STYLE PAGE -->
