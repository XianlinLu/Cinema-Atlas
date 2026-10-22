# Complete style specifications 14


<!-- STYLE: archive-lighttable -->

- `demo/film.js`: `IT` (objects: centre, rotation, scale), `toW()` / `toT()` (texture ↔ world), `CAM` keys and `w2s()`, `dive()` (loupe point, land/lift times, lens interior as tracks), `shot(t)`, `int2s()` (photograph → screen for marks), the shader (`lightTable`, `paper`, `negative`, `parallax`, rim and skirt), the overlay (`annot`, `measure`, `compare`, `indexPanel`).
- `demo/tools/prep.py`: emulsion masks from scans, difference matting of a subject against a smooth sky, ground-only cuts, push-pull fill.
- Minimal example, not in the demo: put one 35 mm slide (`IT.slide = {c, r, k, size}`), a loupe landing with `dive(toW(IT.slide, p), t0, t1, keysS, keysC)`, and light one line with `band()`.
- **Extra packages and packs**: none beyond `setup.sh deps voice music` (numpy, scipy, Pillow, soxr are in the core tier). A score in this palette needs sample libraries: `sh tools/fetch.sh instruments salamander` (piano), `vsco2ce` (strings), `vcsl` (glass, bowed vibraphone). Anything else a film needs goes into a private venv or `node_modules` in the project folder, never into `$LIB/.venv`.

## 11. Variation space

The agent decides the objects, their order, the story, which native moves to spend and where, the camera path, the subject of the photograph space, and the signal colour.

- **Three structures**: a company's founding told as five objects in date order, each dive revealing one person; a single photograph explored in three dives (the place, the people, the date on the back); a before/after pair of plans and photographs of one building.
- **Three openings**: the table switching on in the dark; a loupe already on a plate, rising to reveal the table; a hand-written date on an envelope filling the frame.
- **Three endings**: the index of everything on the table; the last photograph held in depth with one line of text; the light table switching off, leaving one object glowing.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: crayon-book -->

# Crayon Picture Book — Style Prompt

> A picture-book page drawn live in wax crayon on toothy paper, with a watercolour wash that reveals what the crayon was hiding.
> References (grammar only): Raymond Briggs' *The Snowman* (1982) (hand-textured frames that breathe, wordless tenderness, a lyrical passage carried by one tune, still backgrounds with living figures). Copy none of its characters, song or imagery, and never name it in the film.

## 1. Essence, and what it is not

A children's picture book page **being drawn while you watch**: wax crayon on warm off-white paper, a limited box of crayons, child-logic perspective, colour that spills past the outline, and every line gently **boiling** because each frame is a fresh drawing. The tone is picture-book storytelling: tender, unhurried, music-led, a few lines of narration that are literally the words printed on the page. Any topic becomes **one page of a picture book that gets finished**: drawing and colouring are the plot.

It is not "cute vector art with a crayon filter": the look comes from **material physics** (wax sticks only to the peaks of the paper tooth, pressure decides how much of the tooth it reaches, watercolour is repelled by wax). Not a whiteboard explainer (no marker, no hand), not a watercolour painting (the wash is a guest, the crayon the host), not a chalkboard.

## 2. Materials & rendering

- **Paper**: warm off-white (around `#f4efe3`). The tooth is **anchored to the page** (it pans with the camera; on zoom two octaves cross-fade so grains stay ~1 px on screen), never screen-fixed: three octaves of value noise plus a horizontal fibre term. A final pass embosses it (lit top-left), less where wax filled the tooth. Low mottling ±2 %, warm vignette.
- **Wax adhesion (the core rule)**: every crayon layer is a canvas where RGB = colour and **A = pressure**; the shader deposits wax where `tooth > 1 − k·pressure` (soft edge). Light pressure = speckled peaks; heavy = almost solid, slightly darker.
- **Strokes**: ribbons with a low-frequency hand wobble (1–2 px), width ±15 %, tapered ends, a denser core and 1–2 thin streaks. Characters and buildings get the heaviest outline; refined "adult" objects about half.
- **Colouring**: back-and-forth zig-zag hatching with a visible gap, each pass at a slightly different pressure; **overshoot the outline by a few px**; a lighter cross-hatch pass on big areas.
- **Watercolour wash**: a separate density canvas multiplied over the page. Pigment pools at edges (density minus blurred density), granulates in the deepest pits, blooms with noise, and is **resisted by wax** (density × (1 − ~0.9·wax coverage)). Brush strokes are wide bands with bristle streaks and a darker wet leading edge while moving.
- **Occlusion**: a front part erases what is behind it inside its outline; characters "keep the paper white" behind them (a knock-out that restores paper and resets wax), the way a child draws the figure first and colours around it.
- **Characters**: a skilled adult imitating a child: round head (≈2.5 heads tall), dot eyes with a white-wax catchlight, pink cheeks, tube limbs, mitten hands, bold hair shapes; objects with faces get big eyes and eyelids. **Child perspective**: gable front + slanted side wall; people bigger than doors.

## 3. Colour logic

- **A box of about a dozen crayons, never more.** Outlines in one dark colour (indigo, dark brown, plum), **never black**. One white crayon reserved for wax resist.
- **At most one watercolour** per film, chosen for what it reveals (ultramarine for night, rose for dawn, sap green for rain). It never paints the characters.
- Saturated crayon on lots of bare paper; value comes from pressure, not extra hues. One accent on a character may echo the story.
- Example boxes: *seaside* — navy line, coral, sand, teal, turquoise, lemon, white; *orchard* — brown line, russet, apple red, mustard, olive, plum, cream, white.

## 4. Type & subtitles

- Subtitles are **the book's printed words**: a handwriting face (Patrick Hand, OFL), 50–56 px, in the outline colour, bottom-centre, each glyph tilted and offset, boiling on twos, written left→right in ~0.35 s, on a ragged knock-out patch of blank paper (never a dark box). Hold ≥ max(1.8 s, speech + 0.6 s); none during wordless music.
- Titles are hand-lettered on the page (Gaegu Bold or similar), written letter by letter. You can't fade crayon: a title leaves by the camera moving off it, a page turn or being coloured over.

## 5. Motion quality

- **Everything drawn steps at 12 fps** (lines, colouring, characters, boil seed); camera, the wash's leading edge and twinkles run at 24 fps.
- **Boil**: each stroke re-jitters offset (<1 px), wobble and hatching rows every 2 frames. Characters full, background lines ~0.6, background colouring still (it also halves the bitrate). Calm the boil to about half when the film goes quiet.
- **Drawing on**: lines reveal along their length in 0.4–0.9 s; colouring row by row; text letter by letter.
- **Acting**: substitution, a new drawing per pose on the beat; two key drawings alternate for a repeated action. Big simple poses; a child's drawing doesn't in-between.
- **Colouring is an action**: being coloured in *is* doing (a coat scribbled on = putting it on; pink scribble = blushing; a wash = night falling).

## 6. Camera grammar

The camera moves over a large page. A vocabulary, not a route; every move needs a reason. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked full page | Paper before drawing; the whole picture | a beginning from nothing; a tableau; a reveal that needs the page |
| Push toward a character | "This one" | a title giving way; a feeling arriving |
| Locked medium close-up | Substitution poses act | comedy; a decision; a small failure |
| Tilt along a gaze | We see what they see | discovery; longing; something huge |
| Tight follow | The world draws itself ahead of the subject | a brave act; a path; building |
| Held wide while the brush moves | The material is the motion | a wash reveal; weather; day or night falling |
| Slow truck across the page | Reading left to right | a list; a sequence; a family |
| Pull out past the page edge | The page is an object | a book on a table; a fridge drawing |
| Page turn | New chapter, time jump | before/after; the next day |

Key figures ≥ 1/4 of frame height in close shots; keep bare paper at the bottom for the printed words. Transitions: drawing on, colouring over, the wash, a pan or a page turn; never a dissolve.

## 7. Sound palette

- **Small wooden and metal-toothed instruments, no strings or grand piano**: ukulele or nylon guitar, clarinet or bassoon (bass, humour), music box (can wind down with a pitch droop), glockenspiel or celesta (a note per uncovered sparkle), toy piano (one note per counted thing), flute or recorder as the singing voice, shaker and woodblock. A simple lilt; one theme can be held back and heard in full once.
- **Silence is a beat**: a full beat of nothing after a failure; a short breath before a wordless passage.
- **Foley follows the material**: crayon = stick-slip band-passed noise whose grain follows stroke speed (colouring = rhythmic swishes); wet brush = soft low-passed noise with bristle grain, panned with the stroke; felt puffs, fabric swishes, a sharpener, a crayon set down, a page turn (lift / whoosh / flap). Ambience: faint crickets or birds, room tone, a distant clock.
- **Mix**: music under narration, rising for wordless passages; metal voices get a gentle high lift. −14 LUFS.
- **Voice**: a soft, warm storyteller, short lines with breaths. Compress before EQ, cut the highs, de-ess, a warm near-field reverb far under the dry voice; a few dB over the bed, never louder. Whisper-check every line, dry and on the final mix. Avoid famous-book phrases.

## 8. Native moves

A menu: use the ones your story needs.

- **Wax resist.** White crayon is invisible until a wash passes; hide the payoff in plain sight from the first frame. *Fits content like:* a farewell message; a product's hidden feature; roots under a garden.
- **Drawn live.** The world draws itself just ahead of the hero. *Fits content like:* a bridge plank by plank; a journey map; a company timeline.
- **Colouring is an action.** *Fits content like:* a town lighting up window by window; a team putting on kit; fruit ripening.
- **Boil.** A held frame is alive; calming it quiets the film. *Fits content like:* a pause for thought; grief; rest.
- **Child logic.** Wrong perspective, faces on objects, numbers in the sky. *Fits content like:* a launch countdown; a talking house on insulation; a sun that clocks out.
- **It is a book.** Pull back to the object; turn the page. *Fits content like:* a year in review; a "chapter two"; a thank-you card.

## 9. Pitfalls of the medium

- Gaps between wash bands leave white stripes → overlap bands and cover all intended paper.
- Wavy band edges and wide light streaks read as hills → small high-frequency waviness, thin faint streaks (α ≤ 0.12).
- Light-pressure colouring goes muddy under a wash → pressure ≥ 0.8 or cross-hatch wherever the wash crosses.
- Text where the wash passes survives it (wax resists) → place it elsewhere or accept it.
- Characters vanish under a wash → composite them *after* the wash.
- Outlines over hair read as a headband → outline hair masses on their outer edge only.
- Knock-out drawn into a plain layer shows as grey crayon → use a dummy canvas.
- Page turn from rectangle strips shows a staircase → an affine transform per strip.
- Double vignette/emboss at a page-to-object transition → page with vignette 0, ramp the outer scene's in.
- Screen-fixed tooth bloats the file → anchor it, don't boil background fills, no ffmpeg grain.
- Reverb IR from unit-variance noise is hugely loud → scale wet to ~18 dB under dry.

## 10. Engine

In `demo/`: `gl.js` (WebGL2 compositor: paper, wax adhesion, knock-out, watercolour + resist, emboss/vignette/lamp), `crayon.js` (`line` ribbons with taper, streaks, boil; `fill` hatching with overshoot; `text`; shapes), `rig.js` (occlusion + knock-out parts, limb tubes), `sheet.js` (model sheets, `?test=model&page=…`), `end.js` (page on a desk, page turn). Draw your own character's model sheet with them before any shot. File map and commands: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the structure, the characters (or none), the page, the opening, the ending, the camera path, the pacing, the crayon box and whether there is a wash. All far from our demo:

- Structures: **a colouring-book page** (all outlines there from frame one; each idea colours one area); **a flip through several pages** (one stage per page, joined by turns); **two children, one page** (two crayon colours argue, then combine).
- Openings: **a finished page rubbed out** to begin again; **a crayon tip in extreme close-up** mid-stroke, pulling back; **a crumpled page being flattened**.
- Endings: **the page taped to a fridge** among others; **a last scribble** filling the frame with one colour; **a stray splash of water** finding the white-wax message.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: watercolor -->

# Watercolor Brush — Style Prompt

> A hand-painted journal page that paints itself: translucent brush strokes with dry-brush flying white on warm cotton paper, hand-written notes beside what is painted, nothing drawn with a vector line.
> References (grammar only): naturalist field-journal and botanical-plate watercolours (specimen + note); long horizontal handscroll panoramas (one continuous painted world); the textbook "transect" diagram (a gradient read across space). Borrow the grammar, never a specific artwork, character or layout.

## 1. Essence, and what it is not

- **One sheet of warm, fibrous paper** under everything; it is also the eraser (paper-coloured mist washes things away).
- **Everything is individual brush strokes**: a variable-width ribbon at partial opacity plus a few thin **bristle tracks** that break into dashes (flying white). Strokes overlap and darken where they cross, like transparent pigment. No vector outlines; a darker edge stroke along a form is the only "line".
- **Things paint themselves in**, stroke by stroke, structure before detail (trunk → branches → leaves; outline wash → shadow → accent).
- **An annotation layer** in a hand the painter would write with: labels with pen leader lines, a small measured value, a quiet title.
- Tone: calm, curious, precise. Numbers are real; the palette can carry data.

Not ink wash (colour, not ink tones; no calligraphic brush-as-gesture), not impasto (no thick paint, no knife), not a children's picture book (no crayon, no cute outlines), not vector illustration with a watercolour texture laid on top.

## 2. Materials & rendering

- **Paper**: a pre-generated image (warm base, three octaves of smooth noise ±3.5 %, a few thousand short curved fibres, fine grain, light vignette), drawn first every frame.
- **Stroke** (`engine.js` `mk`/`drawS`): a ribbon whose width follows a profile (`brush`, `leaf`, `even`, `tip`, `trunk`) with ~±22 % value-noise roughness, filled as a thin wash (≈ 0.55–0.6 body opacity when bristles are present), plus 3–9 bristle tracks at 30–85 % opacity, each with a random dash pattern and a random early end: that is the flying white. A stroke can be painted up to any fraction of its length (a moving brush tip).
- **Wash**: the same polygon painted in 3 passes with jittered vertices at a third of the opacity each, so edges darken where passes disagree (a pooled watercolour edge).
- **Depth by layers**: several parallax layers of washes and painted objects; farther = smaller, lighter, less saturated; paper-coloured mist bands between layers.
- **Cache finished objects as sprites**; draw stroke by stroke only what is being painted or transformed.
- **Everything is a pure function of `t`**; any stroke made inside `render(t)` is built under a fixed seed.

## 3. Colour logic

- **Paper is the white.** Never paint pure white; light is unpainted paper.
- **Transparent layering**: darker = more passes, not a darker pigment on top. Keep 3–5 hues per scene plus ink.
- **Ink** (a warm near-black and a lighter brown) for lines, text, edges and stems only.
- **Colour may carry the data or the mood**: blend sky, ground and background by position or time so the palette itself changes with the subject. Map ramps quantised into 4–6 bands read as paint, continuous ramps read as software.
- **One accent** (a vermilion, a rain blue) reserved for one element that recurs: a stamp, a marker, a key object.
- Examples: arid-to-wet — red ochre → sage → straw → blue-grey → deep green; a harbour at dawn — `#f3e2c8` sky, `#9fb4c4` water, `#5f7486` hulls, accent `#c8442a` buoys; a vegetable garden — `#e8e0c0` soil light, `#8ea860` leaves, `#4e6e3c` shade, accent `#d9632e` pumpkins.

## 4. Type & subtitles

- An elegant serif (e.g. Cormorant Garamond) for titles and subtitles, a handwriting face (e.g. Caveat) for notes, a small mono (e.g. IBM Plex Mono, wide tracking) for measured labels, Noto Serif SC for Chinese (subset to the characters used).
- Hand notes are drawn twice over a paper-coloured halo, revealed left to right like writing, with a pen leader line that grows to its specimen.
- **Subtitles** sit on the paper, not in a box: centred at the bottom, serif italic ~36 px (2 balanced lines max), a second-language line beneath at ~2/3 size, ink at ~78 % over a paper-coloured halo. Hold ≥ max(1.8 s, speech + 0.6 s).
- Numbers are spelled out in the TTS text and written as digits on screen.

## 5. Motion quality

- **Painting-in is the main motion**: an object's progress is a function of where it sits on screen or of a cue; strokes in a list each take a slice of that progress, so structure appears first.
- **Sway** only after an object is finished: a small horizontal skew (`sin(1.15t+φ) + .4 sin(2.7t+2φ)`), ~0.006 for trees, 0.01–0.03 for grass.
- **Brush-edge wipes**: a wavy vertical clip reveals a whole scene; lines grow by stroke progress; labels open with a left-to-right clip.
- **Mist** erases: paper-coloured layers with a wavy rising edge.
- Animated creatures and events may be phased to the music's beat grid so landings hit the beat.
- Smooth easing (`ss`, `eio`, `eo`, `ei`); 60 fps suits the slow, fluid brush; nothing jitters.

## 6. Camera grammar

A vocabulary, not a route. The picture is one painted sheet; cutting is rare. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Long lateral dolly over a continuous world | a gradient; a journey; cause and consequence | a transect; a route; a timeline |
| Vertical tilt along one object | scale; measurement | a tall tree; a building; a depth |
| Locked sheet, things painted in | study; attention | a specimen plate; a recipe; a diagram |
| Slow push into a detail | the observer leaning in | a seed; an insect; a hand-written note |
| Pull-back to a map or diagram | the whole re-framed | where it all happened; a system |
| Mist wash to blank paper | chapter end; time passing | a season; forgetting; a new place |
| Page turn / new sheet slides over | a new entry in the journal | a new day; a new species; a new case |
| Change in time on a locked view | growth; decay; history | a season cycle; before/after; deep time |


<!-- END STYLE PAGE -->
