# Complete style specifications 17


<!-- STYLE: silkscreen-poster -->

- **One ink, one beat.** Facts print last, when they are read. *Fits content like:* museum hours; a ferry timetable; tasting notes.
- **Split fountain.** Several inks in one pull fill the frame with colour. *Fits content like:* a festival's night sky; a sunset beach bar; a rainbow of colourways.
- **Palette re-ink.** Same poster, another palette = time passing, a season, a variant. *Fits content like:* summer vs winter hours; three jacket colourways; day and night at a market.
- **Registration slip → snap.** Loose layers clamp into register with one hit, before the key facts. *Fits content like:* the date of a race; a launch price; a ticket sale opening.
- **Paper as a colour.** The unprinted sheet is the brightest element. *Fits content like:* a ski slope; a lighthouse beam; fresh snow on a roof.
- **The route as a printed layer.** A dashed accent line stamped segment by segment. *Fits content like:* a bus line; a marathon course; a delivery path.
- **The series wall.** Every print ends up hung together as the final lockup. *Fits content like:* a city's four districts; a band's tour dates; a product family.

## 9. Pitfalls of the medium

- Stroke edge effects draw internal lines on unioned paths → fills only (fill, then fill shifted inside a clip).
- A full-rectangle screen shadow muddies the print → ring shadow.
- Cool shadow facets next to water read as water → shadows in the near ink.
- Jagged ink beads read as paper edges → a round bead.
- Parallax alone reads as "the mountains are moving" → paper gaps and thickness while loose, snapped to zero with a sound.
- Silhouette wipes hold a dark blank → centre on the switch so full cover lasts ~1 frame.
- Very wide banners are slivers in 16:9 → about 4:1.
- Random coloured dots on the table read as confetti → a real workbench (planks, grain, muted stains, tape).
- Too many items at honest reading times overrun the length → print items side by side in the same pulls, or let secondary ones be read on the final wall.

## 10. Engine

`demo/engine/silk.js` prints **any shape** in this style from a `Path2D`: `makeTextures`, `paperSheet`, `ink(ctx, {path, knock, paint}, {color, reg, clip, sheen, trap})`, `wipeRegion`/`wipeFront` (ragged pull), `squeegee` (blade, beads, split fountain), `screenFrame`, `inkFinish`, `bandSteps` (the gradient substitute), shape helpers. `demo/engine/poster.js` (template, banner, `pickInk` contrast), `demo/engine/scenes.js` (planes you can reorder or extend), `demo/film.js` (timeline and shots). API table and a minimal example that prints a new shape: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the subject, the scenes and their planes, the palettes within the colour logic, the number of posters, the camera path, the opening, the ending, the instrument family and the length. Use cases are **grammar for the order and duration of information**; build your own timeline from the user's facts.

| Use case | Information order (print order) | Hold per layer | Length |
|---|---|---|---|
| **Trail / attraction guide** | place → per item: scene → name → difficulty → distance → time → footer | title ~3 s; name ≥ chars/12 + 1 s; stat row ≥ 2.2–3 s after its last item | 30–40 s, 3 items |
| **Event / festival poster** | scene pulls → headline → date → venue → call to action | headline 2.5 s, date + venue 3 s, final 3 s | 15–20 s |
| **Destination series** | one template, a palette per place: name → one fact → series wall | 2.5 s per poster + 4 s wall | 20–30 s |
| **Product drop** | layers around a flat product silhouette → name → colourway ×3 (re-ink) → price / date | 1.8 s per colourway | 12–18 s |
| **Seasonal / hours notice** | one poster re-inked per season → season + hours | 2 s per swap | 10–15 s |

All far from our demo:

- Structures: **one poster, many runs** (re-inked for each of four nights, the line-up changing in the band); **a street walk** (one multi-plane truck down a street, each shop sign printed as we pass); **a misprint story** (registration drifts until the last pull lands true on the date).
- Openings: **the empty screen** (light through a blank mesh, a stencil being exposed); **the accent first** (a lone product in the bright ink on bare paper); **the finished wall at night**, then back to the table.
- Endings: **the drying rack** (prints clipped in a row, swaying); **the poster in use** (pasted on a bus shelter, rain starting); **the last pull is paper** (the squeegee runs dry, leaving a white silhouette).

Swapping `demo/content.json` and rebuilding is a technical check that the engine re-flows, not a way to make a film.

---

How our demo was made (story, shots, score, end card, build, content fields): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: swiss-motion -->

# Swiss Motion Graphics — Style Prompt

> International Typographic Style in motion: a modular grid, one typeface, one signal colour, and movement as exact as a printing press.
> References (grammar only): 1950s–70s Zurich posters (Müller-Brockmann, Hofmann, Gerstner, Crouwel) for the grid, flush-left type, scale contrast and "designing programmes"; modern identity systems in motion (Experimental Jetset, Pentagram) for snaps on the beat. Never copy a specific historical poster's composition (no concentric-circle or fan layouts lifted from Müller-Brockmann), never use Helvetica or Akzidenz font files, never name a real institution on a poster.

## 1. Essence, and what it is not

- **Pure 2D graphic design animated on a grid**: flat paper, black type and bars, a very light grey and **one** saturated signal colour.
- **Every element snaps to the grid, every move lands on a beat, nothing bounces.**
- **Rigor with one exception**: the whole frame obeys a system, so the one element that doesn't becomes a character.
- **Extreme scale contrast**: a giant numeral next to tiny technical notes.

Not a keynote (no gradients, no glow, no device renders), not kinetic typography for a lyric video (words don't fly, spin or bounce), not data visualisation (bars have mass as graphic form, not as charted quantities, unless the grid gives them that meaning), not a Bauhaus pastiche of primary shapes.

## 2. Materials & rendering

- **Frame grid**: 1920×1080, 12 columns, ~96 px side margins, 24 px gutters, 24 px baseline. The frame can act as a **spread**: a left page (the programme: numeral, rule text, notes) and a right page (the artifact).
- **Artifact grid** derived from the content (Gerstner): what the columns and rows *mean* is a design decision. **Choose module sizes that give the elements mass**; too many thin columns make a layout look like a chart.
- **Surfaces**: page, paper, ink, signal colour, grid lines in two or three light greys (on page, while building, on paper). No gradients, no shadows, no particles, no grain (mux grain 0).
- **Bars and blocks** are flat rects; consecutive cells of one unit merge into one bar, overdrawn 1 px at seams (antialiasing shows hairlines, especially when rotated or scaled).
- **A secondary voice** can be light-grey elements under the black ones: depth without a second colour.
- **A 2D camera matrix** (centre, scale, rotation) for all moves.

## 3. Colour logic

- **Paper, ink, greys, and one signal colour.** Only one thing carries the signal colour; that makes it the protagonist. It is the only thing allowed to be inexact.
- Overprint is allowed: black type on the signal colour.
- The signal colour can be red, orange, ultramarine or green; choose it for the topic, then never add a second.
- Examples: `#EAE9E5` page, `#FFFFFF` paper, `#111111` ink, signal `#E30613`; or `#F2F0EA` / `#141414` / signal `#FF5A00`; or `#E9ECEF` / `#0B0B0B` / signal `#1F3FFF`.

## 4. Type & subtitles

- **One family for the whole film**, an OFL neo-grotesque (Archivo, Inter, Schibsted Grotesk, Instrument Sans…), several weights. Letter-spacing ~−2 % at ≥ 90 px. Headlines can be lowercase. Load every weight with `document.fonts.load` before drawing.
- **Flush left, ragged right**; everything on a grid line; big white space is part of the layout. Giant numerals are **optically** flush left (subtract the glyph's left bearing).
- **Subtitles are part of the layout**, not a bar at the bottom: each line sits at a column start in the current composition (a small grey lead-in + a large bold statement, or a caption like a museum label), each word clip-revealed on its whisper timestamp. Hold ≥ max(1.8 s, speech + 0.6 s); assert it in code.
- **Caption rows**: small (~19 px) medium-weight notes with a 1 px rule above; technical notes in a corner (module sizes, counts, a bar counter).

## 5. Motion quality

- **Two curves only**: a precise ease `cubic-bezier(.7,0,.2,1)` for snaps; linear for lines being drawn, playheads and the exception. No overshoot, no spring, no bounce.
- **Durations are note values** at the film's tempo. A snap starts one note value early and **lands on the beat**.
- **Entrances are wipes or clip-reveals, never fades**: words rise out of a clip rect from below the baseline and leave upward; lines grow along their length; paper appears by a wipe; big numerals climb in eased steps ("one module at a time").
- **Deletions are knife cuts**: a thin line crosses the element, then the element collapses to its midline.
- **Ripples are ordered by distance** from their cause, a couple of units per subdivision.
- **The exception moves differently**: linear, unsnapped, perhaps pausing mid-flight; a coordinate readout beside it can turn from "on grid" to "off grid".
- Smooth 24 fps, no stepping: digital precision, not hand-made.

## 6. Camera grammar

A vocabulary, not a route. The camera moves only with the precise ease and only on beats. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked spread | cause (left) → effect (right) | a rule applied; a before/after; a comparison |
| Hard pan by one page or column | the next step in a system | a sequence; a catalogue; a timeline |
| Rotate 90° and stop | the same thing read another way | a poster as a score; a chart as a map |
| Pull out to a wall of artifacts | one programme, many outputs | a brand system; a product range; a series |
| Push into one module | detail; the unit of the system | a pixel; a letter; a single data point |
| Grid extends past the page | the system is bigger than the artifact | scale; ambition; a break from constraints |
| Split frame into equal cells | parallel cases | options; variants; team members |
| Vertical scroll through a column | reading; a list | a manifesto; a spec sheet; a timetable |

Framing: everything on the grid; the signal element may sit off-grid only when it is being the exception. Transitions are wipes, knife cuts, camera moves and re-flows; never dissolves.

## 7. Sound palette

- **Music with a grid of its own**: a steady pulse whose subdivisions give snap durations. Options: motorik / krautrock kit and bass, minimal techno, marimba or vibraphone patterns, a mechanical piano ostinato, a drum machine with a glockenspiel; one instrument added per new rule is a clear build.
- **Picture and music can share one data file** (a column → pitch, a row → onset), so a graphic can literally be the score.
- **Techniques (options)**: drop the drums for the one moment of the exception; a near-silent bar before a reveal; thin the band during a reveal so every note is audible.
- **Foley follows the materials of print**, dry and close, no reverb: letterpress clack, ruling pen "tss", guillotine snick, paper slap and slide, numeral thunk, block snap, felt thump for a landing, rubber stamp, typewriter carriage.
- **The exception can be the only element that sings** (a sine glide following its position).
- **Silence**: a hard stop of everything on a downbeat; the next snap reads as an event.
- **Mix**: voice compressed and ≥ 6 dB above music, music ducked ~10 dB under voice, −14 LUFS.
- **Voice**: cool, crisp, rule-like sentences; prefer voices with bright consonants.

## 8. Native moves

A menu: use the ones your story needs.

- **The grid means something.** Columns and rows become a quantity (notes, hours, floors, years). *Fits content like:* a building's floors and rooms; a week's timetable; a city's districts.
- **Snap = beat.** Every arrival is a percussion hit. *Fits content like:* a product's feature list; the steps of a recipe; a countdown.
- **Programme.** Rules applied one by one to one artifact, then the same programme generating many. *Fits content like:* a brand identity; a typeface family; a set of stamps.
- **Extreme scale contrast.** A giant element as chapter card beside tiny notes. *Fits content like:* a record statistic; a year; a price.
- **The exception.** One element breaks the grid, linear and unsnapped. *Fits content like:* an inventor; an outlier in the data; a rebel employee.
- **Knife cut.** An element deleted by a line. *Fits content like:* budget cuts; editing a text; removing a feature.
- **Re-flow.** Everything else rearranges around a change, nearest first. *Fits content like:* a team reorganised; traffic after a road closes; a layout adapting to a phone.

## 9. Pitfalls of the medium

- Too many thin columns look like a chart → fewer, wider modules.
- A "better" composition that isn't obviously better → one strong diagonal with long/short rhythm, a larger signal element, bleeds, type over colour. Merely tilting is not enough.
- Rotating and labelling at once reads as noise → rotate, hold, then add labels.
- Merged bars show seams after rotation → overdraw 1 px.
- Elements that share the camera matrix leak into other shots → draw them only when on screen.
- Canvas `letterSpacing` affects `measureText` → measure after setting the font.
- Onsets that fall between frames flicker → put visual onsets on whole frames.
- Whisper splits or merges words and pads the first word → align by letters, clamp to 0.

## 10. Engine

In `demo/`: `ease.js` (`cubic-bezier(.7,0,.2,1)`, `snap(t, t_arrive, dur)`, `steps()`, `track()`), `film.js` (layout system, clip-reveal text, knife cuts, bars from a score, rotation reveal, wall of artifacts, caption rows), `main.js` (fonts, whisper word times, `?nosub=1`, `?poster=1`), `score.json` (the shared data file for picture and music), `tools/words.py` and `tools/subs.py` (word timings, asserted subtitle intervals). File list and build steps: [DEMO.md](DEMO.md) "Build notes".

## 11. Variation space

You decide the system, what the grid means, the exception (or none), the signal colour, the opening and the ending. All far from our demo:

- Structures: **a timetable** (a 24-row grid of hours fills with the topic's day, one row per beat); **an alphabet** (A to Z, each letter a module of the topic, the grid completing as a specimen sheet); **a comparison** (two systems side by side on a split spread until one element crosses the gutter).
- Openings: **a single dot** placed on the page, then the grid growing from it; **the finished artifact** that is then dismantled into its rules; **a giant numeral** filling the frame, which turns out to be a detail of a small layout.
- Endings: **the empty grid** after every element has been cut away; **a single word** flush left in the corner; **the exception leaves the frame** and the system closes over the space it left.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: spy-titles -->

# 60s Spy Title Sequence — Style Prompt

> A cut-paper, four-ink opening title sequence for a film that never existed: silhouettes move through sets built out of the credits themselves, every brass stab is a cut, and a title is assembled from the pieces.
> References (grammar only): Saul Bass's titles for *North by Northwest*, *Anatomy of a Murder* and *Vertigo* (flat opaque inks, abstraction down to silhouettes, type as structure); the 2002 homage by Kuntzel + Deygas for *Catch Me If You Can* (a cut-paper chase through graphic sets, lateral tracking). Not a gun-barrel opening, not a tiptoeing cartoon panther, not a copy of any real title's logo, lettering, characters or shots.

## 1. Essence, and what it is not

- **Flat, opaque inks on paper**: four colours, no gradients.
- **Hand-cut edges** on every shape; pieces layered with cut gaps and small paper shadows.
- **Abstraction down to silhouettes**: figures in profile, all acting in outline and timing.
- **Typography is the picture's structure**: credits are architecture, props, vehicles.
- **Music cuts the picture**: brass stabs are edit points.
- A title sequence is a story in itself: one goal, a few locations, one reveal.

Not flat vector motion graphics (the edges are cut, the paper is physical), not a halftone print style (no dots), not a Swiss grid (diagonals, jaunty type, playful), not a spy parody with gadgets and gun barrels.

## 2. Materials & rendering

- **Scissor-cut edges**: every polygon resampled every ~9–10 px and displaced along its normal by low-frequency noise (amp ~1.2–2.2 px, larger for bigger shapes) plus a rare 1–2 px notch. **Cut the edge once in the piece's local space and cache it**, so a moving cutout keeps the same edge, exactly like real cutout animation (screen-space edges crawl).
- **Paper layering**: separate pieces are separated by a ~2.4 px cut gap in the ground colour and cast a small paper shadow (offset a few px, blur ~5, alpha ~0.3). Whole figures get the gap as an outline, so a black figure reads in front of a black letter.
- **Paper texture**: one full-frame texture multiplied on top (mottling + faint fibres), a sparse "ink void" speckle on dark ink, faint squeegee streaks; film grain in the mux (~6).
- **Silhouette figures**: tall stylised adults (~7 heads), identity by hat, coat cut, shoes and **one colour accent** that doubles as a motion indicator (a tie or scarf streaming back when running). Pieces **merge into one outline** inside the figure, with only thin slits at shoulder, elbow, hip and knee. Hands are sharp wedges; no faces except an eye slit in close-ups.
- **The object of the chase** sits on a black backing (an ink keyline) so it reads on any ground; it is the brightest thing in frame.
- **Type**: a condensed OFL display face (e.g. League Gothic) for credits, glyph outlines extracted (opentype.js) and **re-cut** per letter (edge noise, ±0.8° rotation, ±1.5 px baseline jitter). A title in custom geometric cut glyphs (straight cuts + arcs, uneven weights, staggered baselines), never a real title's lettering.

## 3. Colour logic


<!-- END STYLE PAGE -->
