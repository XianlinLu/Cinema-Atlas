# Complete style specifications 17


<!-- STYLE: spy-titles -->

- **1960s spy big band**: stacked staccato trumpets and trombones in octaves with crash (the stab), surf guitar low-string twang through a spring reverb, walking upright bass, brushes or sticks, bongos and shakers, vibraphone, flute, organ stabs, harpsichord. Minor keys, chromatic lines, dotted rhythms. Original motifs only: avoid the famous chromatic crawl of the most famous spy theme and its minor-major-ninth ending chord.
- **Stabs = edit points**: place staccato brass ~8 ms early so the sample's peak hits the frame.
- **Techniques (options)**: a cut interval that shrinks as a chase accelerates; stop-time silence; a big chord for the title followed by a short button; a solo instrument alone for a quiet scene.
- **Foley follows the material**: paper (cut "shh", slides, card slaps for letters landing, blind flips, a tear), metal (keys, chains, locks, clicks), tape (click, hiss). Environments only hinted: a jet pass panned, train wheels in tempo, roulette ticks slowing, wind, a phone ring, footsteps on stairs.
- **Silence**: true zero, reverb tails included; a single tape click or hiss may remain.
- **Mix**: music ducks ~7 dB under voice; a peaky mix needs a few dB into a limiter before loudnorm to reach −14 LUFS.
- **Voice**: a briefing through a tape chain (band-pass ~220–5200 Hz, soft saturation, slow wow, hiss rising under the voice); a few very short lines.

## 8. Native moves

A menu: use the ones your story needs.

- **Type is the set.** Each location is one line of credits and that line is its architecture (letters as pillars, words as carriages, a letter as a lock). *Fits content like:* a conference programme as a city; a menu as a restaurant; team names as a stadium.
- **Credits are rhythm.** Credits land on beats; stabs are cuts. *Fits content like:* a product's features; a festival line-up; an award's nominees.
- **Graphic match cuts.** Shape rhymes, the interval shrinking as tension rises. *Fits content like:* a coin → a planet → a clock; a gear → a wheel → a sun.
- **The diagonal grid.** A diagonal cut multiplies into a grid, and the pieces later fly back along it to assemble something. *Fits content like:* a puzzle solved; a team forming; a logo assembled.
- **Silhouette puppets.** Profile cut-outs whose acting is outline and timing. *Fits content like:* a heist; a courier on a deadline; a detective.
- **Stop-time gag.** Freeze on a stab, silence, resume. *Fits content like:* a near miss; a double take; a price reveal.
- **The object of the chase is the title.** What everyone pursues becomes the last thing assembled. *Fits content like:* a product launch; a book's name; a birthday name.

## 9. Pitfalls of the medium

- Every internal piece outlined with a gap looks like a mannequin diagram → merge pieces in an offscreen layer, cut only joint slits (`destination-out`), outline the whole figure.
- A `clear()` that resets the transform silently kills the camera.
- A figure fully hidden behind a letter reads as "nobody there" → let hat, nose and accent stick out. A stiff streamer reads as a tongue → multi-segment ribbon with a travelling sine.
- A credit only ever seen partially is uncomfortable → always open wide on the full line.
- Black background props read as letters → darker ground colour.
- An object in the same ink as its ground vanishes → black backing.
- Circular props dropped into a word cover neighbouring letters → lay the word out around a gap.
- Match cuts fail if circle centres move across the cut.
- Flat inks + grain make huge files at low CRF → a higher CRF looks the same.

## 10. Engine

In `demo/`: `paper.js` (four inks, cached scissor edges, cut gaps, paper shadow, texture, silhouette layer with joint slits), `glyph.js` (League Gothic → opentype.js outlines → re-cut letters), `chars.js` (silhouette rigs, poses, run/walk cycles), `title.js` (custom cut title glyphs, diagonal split), `story.js` (tempo grid, single source of timing), `film.js` (timeline, acting, cameras, subtitles, sound events). `?sheet=1` renders a model sheet, `?frame=<scene>` a style frame. File list and build steps: [DEMO.md](DEMO.md) "Build notes".

## 11. Variation space

You decide what is pursued, by whom, the locations (as credits), the inks, the opening and the ending. All far from our demo:

- Structures: **no chase: a countdown** (ten credits, ten locations, a bomb-clock number built from type in each); **a heist in reverse** (the object is returned, location by location, to where it belongs); **two agents, one frame** (split diagonally, each side a different ground colour, until they meet).
- Openings: **a full-frame title** that shatters into the sequence (the reveal moved to the start); **a telephone rings** in a single cut-out room; **the hero already falling** through a column of type.
- Endings: **the title never assembles**, one piece missing, the hero walking off with it; **a slow pull-out** showing every location was one giant credit page; **a stop-time freeze** on the final stab, held.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: art-deco -->

# Art Deco — Style Prompt

> Black lacquer, engraved gold line and airbrushed geometry: a 1930s poster that moves. Every composition has a centre axis, transitions open or close along it, and light arrives as bulbs switching on one by one.
> References (grammar only): **A. M. Cassandre** posters (giant geometry, steep perspective, airbrush inside hard edges); **Chrysler Building / Rockefeller Center ornament** (setbacks, sunbursts, chevrons); **Busby Berkeley** overhead numbers overheads (human kaleidoscopes); **The Great Gatsby (2013) title sequence** (gold line drawing itself on black); **Gershwin-era symphonic jazz** (clarinet, piano, muted trumpet). Never copy a poster layout, a real building, a character, a typeface design or a melody.

## 1. Essence, and what it is not

A world built from **gold keylines on warm black**, filled with **airbrushed hard-edged volumes** (Cassandre, Lempicka), organised around **one vertical axis**. Ornament *is* the picture: sunbursts are backgrounds, stepped arches are frames, a dial is a progress bar, a bulb marquee is a reveal. Motion is **mechanical and symmetrical**: things unfold from the centre, doors split along the seam, lights switch on in counted order. Native register: glamour with a clock ticking (an event, a deadline, a launch).

Not a gold-foil slideshow (things move and have volume), not Art Nouveau (no whiplash curves, no flowers), not a flat vector poster (volumes are airbrushed and rimmed), not a 60s spy title (no silhouettes on flat colour).

## 2. Materials & rendering

- **Ground**: warm lacquer black, never neutral grey-black; a night sky may drift toward a deep emerald near the horizon.
- **Gold is a banded metal gradient** (dark – light – hot – light – dark); animate its `sheen` offset for a light sweep.
- **The signature stroke** (`gline`): a dark engraved underline ~1.6 px wider than the line, the gold gradient line, and a hairline highlight on top. Optional glow and a parallel twin (`double`). Nothing gets a black cartoon outline.
- **Volumes**: hard edge + airbrush (`airbrush`): a directional gradient from shade to light inside the shape, one consistent light direction (upper left by default), a thin gold rim on the lit side.
- **Motifs** (sunburst, stepped arch / ziggurat, fish-scale, chevrons, fan, four-point sparkle, speed lines, clock face, dial) are structural (a background, a frame, a transition), not stickers.
- **Perspective is real**: true one-point (mode-7 floors) and two-point perspective through a pinhole camera, so dolly, tilt and pan change perspective instead of scaling flats.
- **Characters are deco too**: about 7 heads tall, tapered streamline bodies, faceted lacquer planes (Lempicka), almond or arc eyes, a one-stroke nose, airbrush + gold rim. Give each lead one or two silhouette marks readable at a quarter of frame height.

## 3. Colour logic

- Three constants: **warm black ground, gold line and metal, ivory** for paper, gloves, light and type.
- **One saturated accent reserved for the protagonist** (or the one object the story follows). It is the only large saturated area, so the eye finds it in any wide shot. A cooler jewel tone may carry secondary surfaces, never competing in area.
- **The one-colour exception**: any single element can be drawn in its own colour through the same fill + keyline + glow (`color` option) while everything else stays gold.
- Always expand hex to six digits in code (three-digit hex breaks colour mixing).
- Examples of the triad (accent / jewel / metal): burgundy / emerald / gold; coral / sapphire / pale gold; jade / plum / rose gold. Our demo's actual values are in DEMO.md.

## 4. Type & subtitles

- **Type (OFL)**: Limelight (titles), Poiret One (numbers, sign skeletons, plaques), Josefin Sans (subtitles, labels), Italiana (numerals).
- **Titles are architecture**: a stepped gold title bar over an arch or sunburst, optional badge and wings; drawn on in gold, then a sheen sweep.
- **Subtitle card** (`subtitleCard`): a lacquer bar (~88 % black) with stepped ends like the title bar, double gold keyline, Josefin Sans SemiBold ~40–42 px ivory, an optional small speaker icon per voice. It **unfolds from the centre** like every other title, so titles, subtitles and transitions are one system. Hold ≥ max(1.8 s, speech + 0.6 s).
- Numbers carry plot without narration: dials, clock faces, floor medallions, badges.

## 5. Motion quality

- **Characters step on twos (12 fps)**; camera, light, bulbs, gold draw-on and sheen run on ones (24 fps). A stepped camera reads as stutter.
- **Everything unfolds from the centre**: a point → a hairline → bars open symmetrically → text rises → wings and sparkle.
- **Draw-on follows the music**: a gold line grows at the speed of the phrase under it and lands on the hit.
- **Bulbs have an ignition overshoot** (~1.6× flash settling in ~0.18 s) and a relay "chunk"; once a sign is lit, a fast chase may run across it.
- **Mechanical easing**: doors, dials and hands move with firm ease-in-out and a small settle, like machinery; nothing floats.
- **Performance beats get anticipation** and escalation in threes (once, twice, mash).
- What never moves: the centre axis of a composition. Symmetry may rotate or open, but it never drifts off-centre.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Symmetric split (two door leaves hinged at the edges; or a revolving-door wipe) | a threshold crossed | a new place; a new chapter; a reveal behind a façade |
| Leaves sliding shut over the live shot | a door closing on a moment | leaving; a decision made; the end of an era |
| Extreme low-angle Cassandre tilt | scale and aspiration | a goal far above; a tower, a rocket, a monument |
| Architectural section (pull out to a cutaway of the whole building) | progress through a structure | climbing, descending, a process in stages; a company's floors |
| Busby Berkeley overhead, mirrored and rotating | people become pattern | a team, a release, a celebration, a system of parts |
| Push-in on a dial, medallion or clock | the number is the plot | a deadline; a count; a milestone |
| Match-cut on shape (circle → circle, ray → ray) | two places, one rhyme | jumping between departments, cities, eras |
| Low oblique along a sign or marquee | light travelling letter by letter | a name revealed; a launch; a score being counted |
| Pull back from detail to skyline | where the moment sits in the world | aftermath; a city-wide effect; scale |

Framing: the centre axis is sacred; an asymmetric frame must resolve to it within the shot. At an emotional peak the protagonist fills ≥ ~1/3 of frame height (smaller, the face reads as a prop in the ornament). Transitions: splits, revolves, arch openings, shape matches; never a generic dissolve or slide.

## 7. Sound palette

- **Symphonic jazz of the 1920s–30s, not a 60s big band.** Options: stride or concert piano, clarinet (trill; a glissando by time-varying resampling of a long note), strings (tremolo, rushes, pizzicato), muted trumpet commentary, trombone and sax section, walking pizz bass, brushes or sticks, tubular bells, harp glissandi, banjo, xylophone runs, celesta.
- Rhythm families to choose from: foxtrot, Charleston, tango, a slow torch-song ballad, a fanfare in the manner of a newsreel.
- **Techniques (options)**: one hit per unit of counted light; accelerate by dividing the beat; plant a theme in fragments so its full statement is a payoff; low-pass a band that is physically far away and open it as we approach; move a period narrator through acoustic spaces (horn, radio, PA, live mic) to make distance audible.
- **Foley by material**: brass clicks, bronze clang + chain, iron treads, marble heels, silver trays, wooden doors + spring twang, paper flutter, knife-switch "chunk" + filament hum, relay ticks, elevator ding, champagne cork.
- **Silence as a tool**: before the most important sound, drop to one small diegetic sound (a clock tick, wind) and cut back in with that sound alone.
- **J/L-cuts** carry architecture: the next room's sound enters a bar before its door opens.
- Mix: duck music ~−9 dB under voice (less under a period announcer who is part of the texture), beds −6 dB, −14 LUFS, light film grain.

## 8. Native moves

A menu: use the ones your story needs.

- **Counted light.** A bulb sign lights one letter per beat or per event, so the audience can count. *Fits content like:* the countdown to a product launch; the letters of a city name lighting as a train arrives; votes tallied into a winner.
- **Threshold doors.** Every scene change is a door split along the seam. *Fits content like:* the departments of a company; the rooms of a museum; stages of a career.
- **Machine kaleidoscope.** People or objects become a mirrored, rotating pattern that locks into a symbol. *Fits content like:* a team becoming a logo; gears of a supply chain; a choir becoming a clock.
- **Dials carry the plot.** A floor indicator, a clock or a gauge moves instead of narration. *Fits content like:* a funding thermometer; the altitude of a climb; a stock ticker at the opening bell.
- **The architectural cutaway.** Pull out until a building is a section and the protagonist a coloured dot with speed lines. *Fits content like:* data moving through a server stack; a letter through a post office; a skier down a resort.
- **Sheen sweep / draw-on.** Light crosses a gold object on a hit; a gold line engraves itself at the speed of a glissando. *Fits content like:* unveiling a trophy; a map route; a signature on a treaty.
- **The one colour.** One element keeps its own colour in a gold world. *Fits content like:* the one product among competitors; the patient among doctors; the new idea in an old firm.

## 9. Pitfalls of the medium

- Bulb signs from glyph skeletons break on curves (G, S, R): Zhang–Suen staircase pixels fool a neighbour-count junction test → use the **crossing number** and weld chain ends within ~14 px.
- A generic cartoon character looks pasted in → characters are deco (§2).
- Fish-scale reads as brickwork → lower half-circles row by row, each overlapping the previous row, plus an inner arc.
- Door leaves over a flat "interior" read as a blank frame → draw only the leaves, closing over the live shot.
- A gold point on pure black trips `blackdetect` → lift the background wedges and glow slightly.
- Period loudspeaker distortion is unintelligible under music → gentle drive; whisper-check every line on the final mix.

## 10. Engine

Canvas2D, deterministic in `t`, in `demo/engine/`: `deco.js` (gold gradient, `gline`, `airbrush`, motifs, `drawShape` for any path in the deco manner, `color` for the one-colour exception), `type.js` (title bar, digits, badges, dial, clock, `subtitleCard`), `bulbs.js` (any text → bulb sign, `litSequence`), `cam.js` (pinhole camera, `cardTransform`). `demo/frames.js` renders model sheets and style frames from the real engine. Signatures and a minimal example that draws something not in the demo: DEMO.md "Engine reference".

## 11. Variation space

You decide the structure, the characters (or none), the settings, the opening, the ending, the camera path, the pacing, the accent colour and what gets counted. All far from our demo:

- Structures: **the exhibition** (five pavilions of a world's fair, one idea of the topic behind each door); **the ocean liner** (three decks from engine room to ballroom, a horn per stage); **the trophy night** (nominees as sunburst panels, the winner revealed in light).
- Openings: **the machine room** (gold gears and pistons building to the first beat); **the engraved map** (a gold route crosses a continent before anyone appears); **the telegram** (ticker tape types the premise).
- Endings: **the lights go out** (letters switch off in reverse until one bulb remains); **the dawn** (lacquer black warms to a pale sky); **the poster** (the last shot flattens into a printed poster with a date).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: blueprint -->

# Blueprint — Style Prompt

> Engineering drawings that come alive on a sheet of cyanotype paper: white technical line work on Prussian blue, drawn in drafting order, with annotations that move.
> References (grammar only, never copy): the moving technical drawings in Prologue Films' *Iron Man* (2008) end credits, Leonardo's *Codex Atlanticus* pages, 19th-century US patent drawings (Fig. 1 / Fig. 2, part balloons, fine-line shading), the automaton drawings in *Hugo* (2011). No Marvel elements, no real patents, no real inventor's machine or signature.

Suits films of 30–60 s.

## 1. Essence, and what it is not

- **The whole film happens on one sheet of blueprint paper** lying on a dark drafting table. The camera moves over it like an eye reading a drawing.
- **White line work on uneven Prussian blue**: centre lines, outlines, hatching, dimension lines, leader lines with numbered balloons, a title block, a notes column.
- **A 2D line-drawing language**: orthographic and oblique/isometric projection are allowed, **3D rendering never**.
- **Rigorous convention carries the tone**: the drawing is dry and exact; the notes can carry wit, warmth or gravity.
- **The designed thing is the character.** A machine, object, building or plan acts through its parts; people appear only as a hand shadow with a pen, or a signature.

Not Hologram HUD (no glowing wireframe, no 3D orbit), not Whiteboard (no marker on white), not Copperplate Engraving (no burin tonal hatching as the whole look).

## 2. Materials & rendering

- **Sheet**: procedural cyanotype in a shader in *sheet coordinates*, crisp at any zoom: fbm between two Prussian blues, coating streaks, fibres, fold creases (bright edge, dark edge, whitening), bleached edges, specks. Around it: dark drafting cloth with a drop shadow.
- **Lines**: pale blue-white, slightly soft (mipmap bleed), a faint ink breakup driven by paper grain. Four weights (outline, detail, thin, hair; e.g. 3.2 / 2.0 / 1.25 / 0.9 sheet units). **Screen width = sheet width × zoom^0.65**, so close-ups don't turn into sausages and wides don't vanish.
- **Dash conventions**: centre line (long-short), hidden (short dashes), phantom / cutting plane (long-short-short), scaled with zoom so the pattern stays on the paper.
- **Occlusion by painter's order**: every solid is filled with "paper" before its outline is stroked. Oblique extrusion: stroke the outline at N depth steps at 2× width, then fill the same steps with paper; a clean silhouette survives.
- **Composite in buffers**: ink (white = exposed line); fx (shadow, wetness, stamp ink as channels); a subtitle overlay last. Shadows darken lines too: that is how a lifted object proves it has left the paper.
- **Hatching** (fine-line shading) for sections, soil, weights, at 45°, spacing 8–14 units.
- **Cyanotype and water**: a drop blooms deeper blue with a pale tide line; white lines inside the stain go soft; ink signatures bleed.
- **The one real thing** (optional, at most once): a drawing symbol that leaves the drawing language gets soft volume, one gradient across its whole shape, glow, and a shadow falling across the lines. It leaves a pale unexposed imprint where it was drawn.

## 3. Colour logic

- **Blue and white only.** The blue varies in value (coating, stains, folds); the white varies in weight and softness, never in hue.
- **One non-blue colour, used exactly once**: a rubber-stamp ink (red is classic; a green APPROVED or black VOID work too). It carries the verdict.
- The "real" object at the climax may carry light (white glow, soft value), not a new hue.
- Example blues: `#18336B` → `#2A58A6` with lines `#E7F0F9` and table `#0D1116`; a faded sun-bleached sheet `#3A6DA8` → `#5B8CC4`; a deep over-exposed sheet `#0F2350` → `#1D3F80`.

## 4. Type & subtitles

- **Hand lettering** for header, labels, notes and subtitles (e.g. Architects Daughter); a technical sans for title-block fields (e.g. B612); a script only for the signature (e.g. Allura). All OFL.
- **Text is written on left to right** with a glowing nib, like everything else.
- **Subtitles are drawing notes**: a light translucent box with double white rules, a "NOTE / n" cell, the text lettered on in ~0.35 s, a small leader tick. **Placed per shot in empty sky**, never fixed to the bottom (the bottom of a drawing is ground line, base and title block). Wrap at ~880 px. Hold ≥ max(1.8 s, speech + 0.6 s).
- Every subtitle is also lettered into the sheet's **GENERAL NOTES** column, so the final wide shows the whole voiceover as drawing notes.
- The **title is the sheet header**; the **title block** holds status and verdict fields.

## 5. Motion quality

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


<!-- END STYLE PAGE -->
