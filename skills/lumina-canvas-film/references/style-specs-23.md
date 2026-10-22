# Complete style specifications 23


<!-- STYLE: engraving -->

| Move | Expresses | Can serve |
|---|---|---|
| Loupe following the burin tip | One point of attention; making | a first mark; a signature |
| Log-zoom pull-out | The line was part of something larger | scale reveal; context |
| Push to a part, ride with its roundel | Where → what, in one take | an invisible detail; a mechanism |
| Tilt/pan along the sheet at reading zoom | Labels in order | a parts list; a coastline |
| Pull back while something flies | Everything placed in relation | acceleration; summary |
| Locked frame, or a ≤ 2 % breathing push | The plate as document | reading time; colour moving |
| Raking view across the copper | The groove as depth | the cost of craft |
| Cut from mirrored copper to true proof | Reversal | a hidden truth; before/after |

Framing: subject inside the plate mark, labels and roundels in the margins; order details so push-ins never crop a note early. Transitions from printmaking only (proof pulled, tissue guard laid over, region burnished out and re-cut, new sheet on the bed); no dissolves or wipes.

## 7. Sound palette

- **Foley by material**: paper (peel crackle, slip tapped down, tissue rustle, sheet whoosh); press (roller rumble, thump); copper and steel (high band-passed burin hiss with chatter and faint plate ring, swarf pings, a tick on lift, circular scribe, burnishing rub); ink and water (pen scratch, ticks for cut letters, a water plip and wet brush swish). Hatching = micro-scratches denser each pass.
- **Room**: a quiet workroom (faint clock), paper room once the print exists.
- **Instruments** (choose): harpsichord, string quartet, solo cello or viola da gamba, lute, chamber organ, glass harmonica for a cold subject. Plucked and dry while lines are cut; bowed or sustained only when something soft arrives; tiny tings for a scribed ring, a low pluck on landing.
- **Silence** is real: cut room tone too, keep at most one small sound.
- **Mix**: melody an octave above the voice, music ~half under speech, −14 LUFS. Voice: a quiet curator or naturalist.

## 8. Native moves

A menu: use the ones your story needs.

- **The cut.** Burin mid-stroke, swarf rising, nothing else. *Fits:* the first line of a treaty; a watchmaker's scribe; a coast being charted.
- **The three passes.** Form gains volume pass by pass. *Fits:* a building from its plan; a portrait emerging; a skill improving.
- **Magnification roundel.** Ring scribed, burnished, re-cut larger, flown to a margin with a leader, label cut on landing. *Fits:* a gear in a clock; a pollen grain; a harbour inset on a chart.
- **The proof.** Sheet peels off; mirrored copper becomes true paper. *Fits:* a secret out; a draft made final; a coin's die and strike.
- **States of the plate.** A region burnished out and re-cut. *Fits:* a border redrawn; before/after; a design revision.
- **Hand colouring.** Washes bloom after the print. *Fits:* one organ lit; a flag on a historical map; a ripening fruit.
- **Natural size.** A tiny true-scale figure beside the engraving. *Fits:* a seed by its tree; a chip by its circuit; a stamp by its enlargement.
- **The finished plate.** Every label and credit, locked. *Fits:* a museum label; a frontispiece; a certificate.

## 9. Pitfalls of the medium

- Uniform width reads as pen → swell hatches, pinch contours between runs (`hatch({swell})`, `outline({run, pinch})`), keep wMin hair-fine.
- Overlaps without occlusion → pass occluders as `excl` (subtracted ring by ring; even-odd would cancel overlaps).
- Outline-only parts beside a hatched body → hatch along each part's axis, a dark at every joint.
- Burin along the cut hides the groove; big skew looks like poking → ≤ 15°. Regular swarf helix reads as a spring → vary winding, twist, light one edge.
- Reflections over grooves wash them out → copper light first. Roundels authored small freeze sub-pixel → author large, scale in. Leaders hugging the subject read as crossing it → clearance.
- A long early stroke never draws → the ink's early exit must look ahead by the longest stroke.
- A push-in cropping a fresh note breaks the reading rule → put consecutive details on one side.
- Scientific names: TTS may manage, ASR won't → give the checker a plain spelling.

## 10. Engine

`demo/engine/`: `burin.js` (`B.Ink` ordered stroke store + `schedule`, `B.hatch`, `B.engraveTone`, `B.contourHatch`, `B.outline`/`B.stroke`, `B.stipple`, `B.fur`, tone fields), `plate.js` (`drawSheet`, `engraveText`, `writeScript`, `roundelFrame`), `wash.js` (`Wash`), `copper.js` (copper, burin, swarf), `index.js` (`engraveShape(svgPath, {at, light, spacing, style})`: any SVG shape → engraved figure). `demo/example/index.html` engraves and colours a four-pointed spark in ~20 lines; code and function table in DEMO.md "Engine reference".

## 11. Variation space

You decide subject, details, order, opening, ending, camera path, colour, pacing and music. Use cases are **grammar for the order and duration of information**; build your own timeline from the user's facts.

| Use case | Information order | Hold per layer | Length |
|---|---|---|---|
| **Museum label / case screen** | title + scientific name → detail + term + note (×N) → where to see it | title ≥ 2.2 s; note ≥ chars/12 + 1 s; final ≥ 4 s | 30–40 s |
| **"One minute on …"** | question → name → 2–3 facts → one number → follow prompt | number ≥ 2.5 s alone | 35–60 s |
| **Textbook figure** | figure → parts labelled one by one → caption | label ≥ chars/12 + 1 s | 20–45 s |
| **Craft heritage** | object → 2–3 craft details → maker / edition | as above | 30–45 s |
| **Map / site plan** | place → insets → legend → visiting info | inset ≥ 3 s; legend ≥ 4 s | 30–45 s |

All far from our demo:

- Structures: **states of one plate** (one view re-cut three times as a place changes); **a book of plates** (four small plates turned like pages, one fact each, no roundels); **a dissection** (parts labelled in teaching order, colour only on the part taught).
- Openings: **the finished proof burnished back** to its first line; **on paper at 1×** (title cut first, figure grows below); **raking light over blank copper** as the design is traced.
- Endings: **plate beside its proof**; **the natural-size figure** held alone; **a blank new sheet** laid on the stack.

Swapping `demo/content.json` and rebuilding is a technical check that the engine re-flows, not a way to make a film.

---

How our demo was made (story, shots, score, end card, build, content fields): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: silkscreen-poster -->

# Silkscreen Travel Poster — Style Prompt

> Opaque, hard-edged flat inks pulled one colour at a time through a screen: 4–6 inks per poster, stepped colour bands instead of gradients, thin paper-white gaps where the registration slips. Information is revealed the way the print is made: one layer, one beat.
> References (grammar only):
> - **1930s–40s WPA national-park screen prints**: 4–6 flat inks, lit and shade faces, stepped-band skies, a dark information band, concentric sun rings.
> - **Fifty-Nine Parks (contemporary)**: restraint, paper as a colour, a series on one template with a new palette per poster.
> - **The physical process**: hinged screen, squeegee pushing an ink bead across mesh, split-fountain pulls, drag streaks, pinholes, off-register slivers.
>
> Never copy a real poster's composition, park name, lettering or logo, and never name a real agency.

A **scene style**: it does a practical job (a guide, an event poster, a destination series) for any place, event or product with a few facts. See §11 for the jobs.

## 1. Essence, and what it is not

A poster being **printed on camera**. Every colour is an opaque ink laid by its own pull; later ink covers earlier ink completely. No halftone, no fluorescent ink, no line work: a shape's edge is where one flat ink stops. **Gradients are forbidden**: skies and haze are **stepped bands** (a flat colour, thinning stripes, the next colour).

What makes it read as silkscreen and not as flat vector art:
- **Registration**: every layer offset 1–3 px at 1080p; a knocked-out shape leaves a crescent of bare paper.
- **Overprint edge**: a faint multiply ghost ~2 u off under each ink, leaving a darker sliver where ink laps over ink.
- **Ink thickness**: a light rim top-left, a dark rim bottom-right, fills only; fresh ink has a wet sheen that fades within a second.
- **Paper**: cream stock with fibres; mottle and pinholes in paper colour, visible only on ink.

Not risograph (translucent fluorescent overprint with halftone grain), not ukiyo-e (key-block line work with bokashi), not woodcut (carved line), not low-poly (3D facets). This style is opaque, line-free, flat and banded.

## 2. Materials & rendering

- **One `Path2D` per ink layer**, filled in the current transform's units; knock-outs are holes in the path. Any shape can be printed.
- **Pull reveal**: a ragged squeegee front as a clip (a ~30 u drag tail); blade, bead and a sliver of handle ride on it.
- **Ink bead**: a round tube with lit half, dark underside, rolling glints and viscous strands; a split fountain puts several colours in one bead.
- **Screen**: a hinged frame with mesh, emulsion and tape; its shadow is a ring (even-odd), never a full rectangle.
- **Shapes**: ridges with a jagged lit facet, pines as one outline of drooping tiers, water as a flat body with glint bars. Hard edges everywhere.
- **Poster template** (1000×1500 u): paper border, art area, a dark **info band** at the foot holding a name, a number, a rule and a row of stats; columns sized by content.
- **Texture budget**: fine paper tile, mottle multiply ~55 %, pinholes ~75 %, light encode grain. More reads as risograph.

## 3. Colour logic

- **One palette per poster, ≤ 6 inks**, assigned by role: light sky, deep sky / bands, far, mid, near (darkest; also the info band), and **one bright accent** (sun, route, highlights, key number). An optional lit-face ink.
- **Values step from far (light) to near (dark)**; depth is value, never blur.
- **The accent is rare**: the sun or light source, the one route or product, the most important number.
- **Paper is a colour**: an unprinted area is the brightest thing on the sheet (water, snow, a beam of light).
- **A series = one template, a new palette per item** (time of day, season, colourway, neighbourhood). Re-inking the same geometry in another palette is a statement.
- **Text inks are chosen by contrast** against the ink underneath (WCAG), never by a fixed key; a night palette must not swallow a header.
- Examples (sky1 → near, accent): dawn `#F6CD98 #EE9A73 #9A7FA8 #3E7079 #1E3B3F #FBE6B4`; harbour noon `#E8F0F2 #7FB3C8 #D9C7A3 #2F6E8E #173247 #E8553D`; winter `#EEF1F4 #B8C9D9 #8B9BB0 #4A5D78 #1F2A3C #F2B134`.

## 4. Type & subtitles

- **Condensed display** for names and values (e.g. Big Shoulders Display, League Gothic), auto-fit; a geometric sans for letter-spaced labels (e.g. Outfit 600).
- Headers are **printed into the sky**, tracked out; the info band is printed last.
- **The poster text is the subtitle.** No narration is needed; if there is a voice, subtitles are a printed strip (a band pull), never a floating caption.
- **Reading rule**: each text stays ≥ chars/12 + 1 s (min 1.5 s) after its **last** item lands, and ≥ max(1.8 s, speech + 0.6 s) with a voice. Compute it from the content, round up to the beat.
- On a wall shot, labels stay ≥ ~18 px and values ≥ ~30 px at 1080p; close-ups on a band keep the whole band in frame with ≥ 5 % side margins.

## 5. Motion quality

- **Pulls are linear and steady** (a squeegee does not ease). Accent inks start half a beat after the main ink of their layer.
- **Info items** print left to right on subdivisions of the beat. **There is no fade anywhere.**
- **Screen lift**: the frame hinges up (vertical squash + growing shadow) in ~0.4 s.
- **Palette re-ink**: a wide squeegee travels diagonally over the sheet in ~0.35 s; geometry identical on both sides of the blade, only the inks change. Show only the blade, bead and a sliver of handle.
- **Loose layers**: in a multi-plane move, planes parallax by depth with paper gaps and thickness shadows, then **snap into register** on one hit.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Truck with the squeegee, slight roll, frame edge in view | the act of printing; colour arriving | a hook; a split-fountain sky |
| Locked top-down full sheet | layers stacking into a picture | watching a poster build; a comparison |
| Fast pull-back as the screen lifts | the reveal of a finished layer | a scene complete; a title |
| Push + tilt to the info band | reading | facts; a date; a price |
| Truck through a foreground silhouette (tree, lamp post, sail) in screen space | passing into the next poster | poster-to-poster transitions |
| Crane through loose planes (multi-plane parallax) | depth, a journey inside the print | a route; a climb; a street |
| Slow lateral dolly along a row of prints | a set, a range | a series wall; colourways |
| Push into the mesh until the weave shows | the craft, the grain of the medium | an intimate beat; a detail |
| Log-zoom pull-back to the wall or window | the poster in the world | a final lockup (hold ≥ 3 s) |

Close-ups on a sheet keep its edge in frame; a squeegee across a close-up is tilted with the handle hidden, so it doesn't split the frame. Layers change by squeegee, posters through foreground silhouettes or a table move. No dissolves, no bare cuts.

## 7. Sound palette

- **Acoustic, hand-played instruments**: strummed guitar, slide guitar, harmonica, upright bass, cajon or brushes, banjo, fiddle, accordion, harmonium, ukulele. Choose the family from the place: folk, surf, bossa or brass band all fit.
- **One pull, one hit**: each ink lands on a musical event (a strum, a hit, a chord change); accelerate by subdividing, not by changing tempo. A registration snap is a loud downbeat.
- **Foley by material**: squeegee on mesh (band-passed noise with a ~220–280 Hz mesh grain; faster = brighter), wet ink squelch, screen clack and hinge creak, paper stamps, ticks for dashed routes, paper hiss, a wood-and-metal clamp, drying-rack clips.
- **Ambience from inside the print**: a finished scene may "wake up" (surf, street, crowd), J-cut in and L-cut out. Room tone under the table.
- **Silence as a tool**: the music drops out for a beat before the key facts; what remains is one ambience, and the first sound after is a decisive gesture (a clamp, a long slide up).
- Music ducks a few dB under foley. −14 LUFS.

## 8. Native moves

Each serves information order. A menu: use the ones your film needs.

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


<!-- END STYLE PAGE -->
