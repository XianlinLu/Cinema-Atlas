# Complete style specifications 18


<!-- STYLE: blueprint -->

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

> A beat-locked flash-card film built from three things only: a **square-grid "core graphic"** of circles, half-discs and tiny patterned cells whose rows slide past each other; **geometric pictograms** made of round-capped bars and a disc head; and **bold bilingual type** that slides up out of masks. Every cut lands on a drum hit.
> References (grammar only): Otl Aicher's 1972 Munich pictograms (geometric athletes); multi-sport-games "look of the games" identity systems (a modular pattern + a colour set used for everything); Swiss sports-broadcast graphics (mono meta text, tick-bar progress). Learn the grammar; never copy any real event's pictograms, emblem, slogan, pattern artwork or colour names, and never name them in the film.

## 1. Essence, and what it is not

A **catalogue film**: N items (products, dishes, steps, species…) shown one card at a time, fast, on the beat. Each card = **one pictogram doing one action + a huge title + a second-language line + a mono index "07 / N"**. Cards group into chapters; each chapter owns one hue, opened by a full-bleed pattern card.

What makes a frame read as this style at a glance:
1. **The grid pattern**: big discs and half-discs spanning square cells, about half the cells carrying a small motif, all in **five tones of one hue**, with **whole rows cut and shifted sideways**: the signature that drives backgrounds and transitions.
2. **The pictogram figure**: flat, faceless, rounded bars and a disc head; far-side limbs mixed toward the background. Props are discs, rings, capsules, lines.
3. **Type as architecture**: a 900-weight grotesk title set very large, a heavy second-language line under it, small mono meta text in the corners like a broadcast HUD.
4. **Beat lock**: every shot starts on a beat, every key action lands on a beat.

Mood: premium broadcast identity; flat colour, light grain, one soft light sweep as the only gradient.

Not an isometric infographic (no depth, no 3D), not Swiss motion graphics (the figure and the pattern carry as much as the type), not a cartoon (figures never emote, have no faces), not a data film (numbers are labels, not charts).

## 2. Materials & rendering

- **Flat Canvas2D**, rendered clean; grain only at mux time. **One square grid** (cell ≈ 1/6 of the frame height) rules bands, transitions and walls.
- **Pattern model**: fill with a mid-dark tone; on grid nodes randomly place cell-radius discs in random tones and discs-with-inner-discs; then a fraction of cells get one motif from a library of generic geometry (quarter-discs, fish-scale waves, dot and triangle scales, concentric arcs, sun wheels, checkers, crescents…), rotated by multiples of 90°; never mascots, landmarks or logos. Draw it wider than the screen so any row can shift one cell.
- **Figure model**: unit = body height, origin at the hip; draw far limbs (mixed ~40 % toward the background), torso, near limbs, head. A second person sits behind, mixed further (~60 %).
- **Stage**: the figure stands on a large **sun disc** in a neighbouring tone, crossed by one faint light sweep.
- **Figure environments** (water, nets, ramps) live in the figure's own buffer, masked to zero before the text column.

## 3. Colour logic

- **A set of five hues + one dark neutral**, each hue in **five tones** (darkest → lightest, the middle one is the base). A chapter = one hue; a multi-hue chapter rotates through the set per card.
- Under type the pattern runs at **low contrast**; on chapter cards at **full contrast**.
- **Light hues take dark type and dark figures**, and their disc uses the lighter tone; dark hues take cream. On the dark neutral, the disc uses a lighter tone or it vanishes; its accent is one warm hue.
- One cream and one ink serve every hue. No outlines, no highlights except the sweep.
- Choose the set from the topic. Examples: warm festival (red, violet, forest green, gold, ochre); coastal (navy, teal, coral, sand, sky); kitchen (tomato, basil, saffron, aubergine, flour cream). Invent names for your hues; never borrow an event's colour names.

## 4. Type & subtitles

- Title: a 900-weight grotesk (e.g. Inter Tight), 150–330 px at 1080p, tight tracking, auto-fitted. Second language: a heavy face under it. Meta: a mono (e.g. DM Mono) ~22 px, wide tracking; tags as mono chips.
- **HUD** on every card: mono corner text and a **progress bar of N ticks** (current tall, done dimmed, rest faint), N derived from the item list.
- **Bilingual rule**: one language is always the big title; the second language is chosen per version by a switch, never by hand-editing cards.
- The card type *is* the text layer. With narration, captions are a mono line on a solid band in the chapter hue, bottom, never over the title; hold ≥ max(1.8 s, speech + 0.6 s). A card that must be read (a spec, a number) holds ≥ 1.6 s.
- Deliver an `.srt` of the title cards, generated from the edit list.

## 5. Motion quality

- **A grid of time**: pick one tempo for the film; every shot starts on a beat and every key action in a pose (release, contact, landing) lands on an integer beat.
- **Pace ladder**: normal cards last one bar; related sub-items become half-length rapid-fire runs. A second tempo comes from dividing the beat, never from changing tempo.
- Easing: exponential ease-out for entrances, exponential in-out for whips and wipes; a back ease once at most.
- **Type enters by mask slide-up**: title first, second line ~0.08 s later, tag after; meta lines type on without a caret. Short cards compress all timings.
- **Figure assembly**: the figure arrives as horizontal bands sliding into register from alternating sides.
- **Backgrounds breathe**: rows drift in alternating directions; on chapter cards they jump a quarter-cell on beats.
- **Transitions** snap to the grid: sliding rows, dropping columns, a push, quarter-discs from cell corners, an iris from the last figure, a tile flip. Rotate them; each lasts a few frames around the cut.
- **Motion blur only where things move**: sub-frame averaging inside transition and whip windows; static frames render once.

## 6. Camera grammar

Mostly a locked flat frame; energy comes from row shifts, transitions and figure actions. When the camera moves, it moves along the grid. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked flat frame | clarity, the card as a poster | any item; a spec that must be read |
| Lateral track with a one-screen whip per beat | one continuous family, momentum | a line of stations; a production line; a route |
| Slow drift along a row | calm, browsing | a gallery; a menu; a slower chapter |
| Vertical scroll by grid rows | ranking, depth, descent | a top-ten; floors of a building; ocean depths |
| Push into one motif cell until it becomes the next frame | zooming into a part | an ingredient inside a dish; a city inside a map |
| Pull back to a tiled wall of items | the whole set at once | a summary; "all of them"; a comparison |
| Tiles collapsing to one point | many become one | a merger; a shared goal; a count reaching zero |
| Split screen along a grid line | two items side by side | versus; before/after; two versions |

Framing: text and figure never overlap (one text column, one stage); horizontal poses move the stage outward. The HUD stays in the corners. Allowed transitions are the grid ones in §5; never dissolves, 3D camera moves, handheld shake or depth of field.

## 7. Sound palette

- **Type and music can carry the film alone**; a voice is optional, calm, one line per chapter at most.
- **Percussion is the spine**: choose a drum family that suits the topic (frame drums, taiko, marching snares, steel pans, body percussion, an electronic kit) plus rim clicks, claps, shakers and crashes.
- Colour instruments on top: Karplus-Strong plucks (any lute, koto or harp-like voice, with pitch bends), mallets (marimba, glockenspiel), detuned-saw chord stabs, a synth bass, pads, risers and a drone.
- **Per-family accents**: every shot onset gets a hit chosen by chapter (a splash, a pok, a clank, a crack, a whoosh, a sizzle): foley reads the chapter's matter.
- **Picture-locked by data**: the score reads the edit list's shot times and places accents there; check every onset to ±15 ms.
- **Silence as a tool**: half a beat of drums-and-bass-muted before a big hit, or one whole bar stripped to a single ticking sound under a count.
- Mix: glue compressor and limiter, −14 LUFS, ≤ −1 dBTP.

## 8. Native moves

A menu: use the ones your film needs.

- **One card = one item.** The count is the hook ("ALL N"). *Fits content like:* every tool in a workshop; every station of a subway line; every dish of a regional cuisine.
- **Chapter = colour.** Families become hues so the viewer always knows where they are. *Fits content like:* instrument sections of an orchestra; food groups; departments of a company.
- **One verb per item.** One body action readable in a bar, or a prop action (a gear turns, a cup pours). *Fits content like:* yoga poses; kitchen techniques; jobs on a construction site.
- **Pace ladder run.** A sub-family at double speed. *Fits content like:* four knife cuts; the bones of a hand; weekday routines.
- **Long take down a track.** Stations one screen apart, the camera whipping on each cut. *Fits content like:* the steps of a recipe; checkpoints of a marathon; stages of a rocket launch.
- **Count-up slam.** A big number rolls to its value on a bar. *Fits content like:* tonnes recycled; members of a club; years of a company.
- **Icon wall.** All pictograms return as a grid and turn one colour. *Fits content like:* a summary of a year; a periodic table of habits; a team roster.

## 9. Pitfalls of the medium

- Figure environments spread into the text column → render the figure layer into its own buffer and fade it out with a gradient mask before the text.
- Cream on light hues fails contrast → dark type and dark figures on light hues; their disc is the lighter tone.
- The sun disc vanishes on the dark neutral → use a lighter tone for it.
- Pattern canvases are large and seeded per card → cache with a bounded LRU; an unbounded cache runs out of memory with parallel renderers.
- Horizontal poses (swimming, lying, crawling) cross the title → move the stage outward and narrow the text column.
- Imitating a real identity too closely → your own palette, mark and slogan from the grid motifs.

## 10. Engine

In `demo/`: `engine.js` (`G.pattern`, `G.motif`, `G.joints` / `G.drawFigure`, `G.keyPose`, `G.maskText`, easings), `poses/base.js` (pose contract, props `G.P`), `edl.js` (edit list in beats), `scenes.js` (layouts, transitions, HUD, motion blur), `lab.mjs` (pose sheets), `music/music.py` (picture-locked score with onset report). API table, pose convention and a minimal example: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the items, grouping, verbs, palette, chapter order, any long take, the pace ladder, opening, ending, music and voice. All far from our demo:

- Structures: **a countdown** (items ranked from N to 1, the camera scrolling down rows, the pace speeding up as the list shortens); **a day in pictograms** (one figure, one card per hour, the palette moving from dawn to night hues); **an assembly** (each card adds one part to a single growing pictogram machine seen in the corner).
- Openings: **a single motif cell** (one cell fills the frame and splits into the grid); **mid-action** (the first pictogram is already running when the type slams in); **a blank grid** (hairlines draw the grid on the beat before any colour appears).
- Endings: **one card held long** (the last item stays while the pattern rows stop, one by one); **the figure walks off** (the last pictogram exits the frame and the HUD ticks out); **reverse assembly** (the grid disassembles into rows that slide off-screen, leaving cream).

---

How our demo was made (story, shots, score, end card, build, engine reference): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: ascii-crt -->

# ASCII / CRT Terminal: Style Prompt

> Everything on screen is a real character on a monospace grid, lit by the phosphor of an old monochrome CRT.
> References (grammar only): 1970s–80s monochrome terminals and teletype logs (typed output, cursor, status lines); ASCII art and demoscene text-mode pictures (images from glyph density); analog-synth film scores of the early 1980s (cold pulse, patient drones). Copy no film's interface text, fonts or logos, and use no real agency names.

## 1. Essence, and what it is not

A single monochrome terminal screen: **P3 amber** (or P1 green) phosphor glowing on dark glass, curved at the edges, with scanlines. Every image, including title, landscape, face, room and subtitles, is made of **real glyphs placed on a character grid** and chosen by ink density. The film has one camera, the screen itself. It moves only by changing the **font size of the grid**: bigger characters push in, smaller characters pull out.

The mood is cold, patient and machine-calm: typed text, a blinking cursor as suspense, and one warm surprise.

**Never** fake it with an image plus an "ASCII filter". Characters must be drawn as characters on a grid. Not a hacker-movie green rain, not a pixel-art game (no sprites, no free pixels), not a sci-fi HUD (no vector lines, no free-floating panels).

## 2. Materials & rendering

- **Font**: one monospace bitmap-style font (VT323, OFL); cell 0.4 em × 0.8 em (1:2). A large prerendered glyph atlas with a stroke for beam spread, scaled with `drawImage`, keeps zooms continuous and sharp.
- **Grids**: column count per shot (title ~20, terminal 80, picture 200+); a push-in can go until one cell holds a sub-grid of its own.
- **Density ramp**: each glyph's measured ink coverage × dim / normal / bold → about 20 levels, near-duplicates dropped; a small ordered-plus-hash dither per cell; cells below a threshold stay blank. **Negative space makes ASCII art readable.**
- **Picture pipeline**: paint grayscale into an offscreen "negative" aligned exactly to the grid (several samples per cell; channels for phosphor, second colour, a flag), average per cell, pick a glyph. Interiors get local contrast (`m + 0.9·(m − mean)`) to keep outlines.
- **Recognisable subjects**: silhouettes, not noise (real coastline polygons, a face from a few planes); dark = sparse dim glyphs, bright = dense bold, shadow sides sparse `.` only; an angle with a clear silhouette.
- **Depth on a grid**: far = darker and sparser, near = brighter and denser; a thin bright rim separates planes.
- **CRT post** (WebGL, adapted from `core/post/crt.js`):
  - **Phosphor colour**: luminance maps along the phosphor's ramp (dim deep orange → amber → overexposed near-white for P3).
  - **Glow**: multi-level bloom plus a faint halo.
  - **Glass**: fine scanlines (narrower on bright areas), slight barrel curvature, rounded mask, warm near-black unlit glass, faint reflection, ~1 % flicker, fine noise. **No RGB grille: monochrome tubes have none.**
- **Afterglow**: text that disappears decays with τ ≈ 0.1 s, computed analytically so every frame is deterministic. Moving glyphs get one faint trail sample.

## 3. Colour logic

- **One phosphor** carries everything: amber, green or white, in its own brightness ramp. No second hue for decoration.
- **At most one soft second colour**, used for one thing only (the emotional object), switched on at a single moment, on a downbeat, and never taken back casually.
- Examples: amber screen with an ice blue-white for something far away; green screen with a warm pink for a living thing; white P4 screen with a pale gold for a memory.
- Brightness is the only other tool: dim / normal / bold and inverse video.

## 4. Type & subtitles

- **Subtitles are terminal output.** A reserved **LOG strip** at the bottom: a dim separator, an inverse-video tag, then a prompt and the line in uppercase at ~45 px. It is **typed word by word in sync with the voice** (whisper word timestamps) and holds ≥ max(1.8 s, speech + 0.6 s). It lives outside the zooming grid, like a status line, with the same scanlines and glow. When nobody speaks it can show system state (a progress bar, a waiting message).
- **On-screen text that the story shows** is picture, not subtitle; in the `.srt` it appears as `[SCREEN] …`.
- **Titles** are typed with key clicks, as a filename, a command or a header.

## 5. Motion quality

- **Characters never move off-grid, except in a declared transformation moment.** Typing, scrolling and counters jump from cell to cell. A roller flips digits discretely, fast then slowing.
- **Only three things move continuously**: grid scale (the camera), CRT physics, and particles in a transformation.
- **Typing speed is performance**: machine output is even and fast (~10–40 ms/char); dramatic lines slow to note values of the score; human typing is hand-timed, uneven, with pauses and bursts.
- **Particles** spawn from random points inside source glyphs, start small, fade in, ease to their cell, and flash briefly on landing, so they never stack into bright bars.
- **Push to a character**: hold where the whole glyph reads, then push until its inner text reads; inner text full brightness, outside text a few percent, neighbours dimmed, so the shape reads before the text.

## 6. Camera grammar


<!-- END STYLE PAGE -->
