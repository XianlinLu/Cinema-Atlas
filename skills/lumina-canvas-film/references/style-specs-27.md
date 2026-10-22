# Complete style specifications 27


<!-- STYLE: pictogram-motion -->

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

The only camera is the grid scale, plus CRT power states and one possible shot outside the screen.

| Move | What it expresses | Can serve |
|---|---|---|
| Static 80-column terminal | Waiting, procedure, machine time | a countdown; a queue; a log being read |
| Push in (cells grow) | Attention, intimacy | one line of dialogue; a name; a decision typed |
| Pull out (cells shrink) | Context, scale | a title becoming line 1 of a list; one entry among thousands |
| Push into a single glyph | Hidden depth; what a symbol is made of | a letter made of messages; a pixel made of people |
| Scroll (the buffer moves) | Accumulation, time passing | years of records; a changelog; a feed |
| Clear screen / hard redraw | A cut; a new state | a reboot; a new chapter; a crash |
| Text becomes image (grid shrinks as glyphs fall) | Words turning into world | a letter becoming a face; data becoming a map |
| Power on / off, degauss | Birth, death, sleep, shock | a machine waking; an ending; a jolt |
| Pull back off the glass into a drawn room | The screen is an object in a world | who is reading; where the machine is |

Opening and ending come from the topic. Framing: text stays in the safe area inside the curvature; keep the LOG strip clear. Transitions happen on the screen (clear, redraw, scroll, power), never a crossfade between two screens.

## 7. Sound palette


<!-- END STYLE PAGE -->
