# Complete style specifications 09


<!-- STYLE: microscope -->

Example (our demo): glass #F4F1EC, bench #0B0D0F → #2A3036, ink #181B1F, panel rgba(12,14,17,0.74), accent mint rgb(120,240,205) (on stain) / rgb(0,122,99) (on glass).

## 4. Type & subtitles

- **Roles**: a light condensed grotesk for readings and the scale bar (40–72 px, e.g. Barlow Condensed); a monospace for instruments and pixel counts (20 px, e.g. IBM Plex Mono); a sans in the film's language for labels (20–34 px, e.g. Noto Sans SC); a serif only for the title. OFL, self-hosted, CJK subset.
- **Instruments** live in one frosted panel in a corner: scale bar with its value, field of view, magnification with a small nosepiece glyph that turns a quarter on every change. The source credit in a small panel in the opposite corner.
- **Readings** sit in a frosted panel beside what they measure, joined by a leader: a small label above ("collagen share of tissue area"), the number large in the accent, the method or the raw counts below.
- **Subtitles**: a frosted strip at the bottom; if the film is bilingual, one line per language with the film's language on top, never wrapped. Measure each line with the real font and split long lines into two cues.
- Nothing below 20 px at 1080p. Hold labels ≥ characters ÷ 4.5 + 1.5 s (CJK); a reading that rolls is reported by its landing value.

## 5. Motion quality

- The camera is a similarity transform (zoom, roll, position) interpolated as a log spiral between keys (M^u about the fixed point of the two frames), so every push is a true dive towards one point and the roll is part of it. Ease the moves, creep 2–5 % during holds; never a frozen frame longer than a second.
- Magnification changes happen where the plates actually change, each with a breath of focus, a turret click and the new magnification said once, large.
- Marks arrive by being made: a dimension line grows from its centre, a circle is drawn as an arc, a scan front counts pixels while the reading rolls, the reading lands with a small spring.
- Never moves: the specimen under its marks, the instrument positions.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| The dive (log zoom with roll) | going to look for yourself | an opening; from the slide to the cell |
| Locked frame, slow creep | evidence, a measurement | a reading; a comparison |
| Truck at one magnification | a second sample of the same thing | the counter-example; "meanwhile, nearby" |
| Pull back to frame two marks | comparison | the verdict |
| Focal-plane sweep | arriving; depth | a landing; a reveal inside one frame |
| The climb (reverse dive, scale bar jumping back) | consequence, scale | an ending; a return to the eye's scale |

At key moments the measured structure fills a third of the frame height or more; instruments in a corner, subtitles bottom centre, readings beside their marks. Transitions are scale changes, trucks and focus, never cuts or crossfades between samples.

## 7. Sound palette

- **Instrument foley**: the objective turret (a click, a detent, a small metal ring), a focus servo, pen on glass for each line drawn, a band-passed scan travelling left to right with counter ticks that speed up, a soft filtered sweep for the focal plane.
- **Music**: hard-mallet vibraphone in 8ths and 16ths, marimba ticks, bowed vibraphone and water glasses for pads and the motif, glockenspiel for each reading that lands, a pulse bass with 2nd/3rd harmonics, timpani and bass drum under the landings. Harmony stays open and light; the score is the user's to shape.
- **Beds**: a quiet lab room (fan, a little mains hum).
- **Silence** before the verdict and before the climb; the first sound after it is the reading or the turn.
- **Mix**: voice ~10 dB over music, music ducked under it; −14 LUFS. Voice: a calm, exact narrator; numbers spelled out for the TTS, digits on screen.

## 8. Native moves

- **The dive.** From the slide in the hand to a cell in one camera, the turret clicking at each real change of level. *Fits content like:* a biopsy to its cells; a coated surface to its crystals; a hair or skin section to its layers.
- **Counting the colour.** Draw a circle, let a scan front cross it, light up every counted pixel and roll the share up to its landing value; show the raw counts underneath. *Fits content like:* collagen in tissue; porosity in a ceramic; coverage of a coating; pigment in a sample.
- **Two circles, one verdict.** Measure one place, truck to another at the same scale, then frame both and say what differs. *Fits content like:* treated against untreated; edge against centre; before against after.
- **The focal sweep and the ring.** Land, sweep the focal plane across the frame, ring one structure and give its size. *Fits content like:* a nucleus; a grain; a fibre's diameter.
- **The climb back.** Pull out to the eye's scale with the scale bar jumping backwards; a title card written on the glass.

## 9. Pitfalls of the medium

- **Licences**: most microscopy on the web is CC BY-NC or all rights reserved. Usable: CC0 whole-slide scans (e.g. the OpenSlide test data: check each file's licence line), public-domain government micrographs (NIH, CDC PHIL, NASA, USGS), CC BY collections (Cell Image Library, Wellcome Collection), with every file listed in `CREDITS`. Not usable: CC BY-SA without agreement, NC images, journal figures, AI images.
- **Finding material for a new topic**: search by organ, stain or material plus "whole slide" in the OpenSlide test data, NCI Imaging Data Commons (TCGA/CPTAC slides, licence per collection), the Cell Image Library, Wellcome Collection, Wikimedia Commons (filter by licence) and NIH/CDC galleries; prefer a file whose metadata carries its pixel size. CC BY-SA, ODbL or "no known restrictions" are not CC0: name the terms to the user and ask before using them. For a product, a lab or a brand, ask the user for their own scans (SVS/NDPI/MRXS, SEM TIFFs with a scale) first. Never stand in a generated image for a real specimen.
- **Different samples never zoom into each other**: two micrographs of "the same thing" at two scales are two specimens. Use one pyramid; if you must join sources, cut on a focus breath and say so.
- **Pixel size**: read it from the file (XMP `ScanRes`, TIFF resolution, OME `PhysicalSizeX`); a slide-photo's resolution tag can be trusted only after checking against the scan.
- **Upsampling** shows as mush beyond ~1.6×: end the dive at the scan's real resolution.
- **Tile seams**: some scanners overlap tiles; check the joint info, frame out visible seams.
- **Labels and logos** on the slide: barcodes and IDs are part of the object; manufacturer logos are not — fill or crop them.
- **Claims**: a stain's colour means what the stain protocol says, nothing more; measured shares are of the drawn region and the stated threshold, never a clinical score.

## 10. Engine

- `demo/film.js`: log-spiral camera (`camAt`), plate selection by downsampling ratio and coverage, objective events from real level changes, focus, frosted `panel()`, marks, readings, `TEXTS` / `SUBCHECK` / `EV`.
- `demo/tools/plates.py`: slide-photo registration and cleaning, graded plates, collagen mask and the scan's cumulative curve, the tissue axis. `nucleus.py`: membrane edge on 72 rays, least-squares circle.
- **Extra packages and packs** (beyond `setup.sh deps voice`): `tifffile` + `imagecodecs` read TIFF-based slides (Ventana BIF, Aperio SVS, Hamamatsu NDPI, generic pyramidal TIFF; `demo/tools/plates.py` is written for BIF: its label page, XMP and AOI); MRXS, SCN, VMS and others need `openslide-python` with the OpenSlide library (`brew install openslide`), or an adapter of your own. Install them yourself into a private venv in the project folder, not into `$LIB/.venv`.
- Minimal example, not in the demo: a coated steel sample: one SEM pyramid, a dive to one crack, a circle counting coverage, a ring around one grain.

## 11. Variation space

The agent decides the specimen, the stain or modality, what is counted, the camera path, the accent, the ending.

- **Structures**: a single dive ending in one measurement; a comparison of two regions or two samples at one scale; a climb that starts on a cell and reveals the object.
- **Openings**: the slide on the bench under moving light; a cell already in focus, the climb revealing what it belongs to; a blurred field racking into focus.
- **Endings**: the title written on the glass; a last reading held in silence; the slide lifted out of frame.

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: archive-lighttable -->

# Archive Light Table — Style Prompt

> Real archive objects (glass negatives, slides, letters, telegrams, clippings, drawings) lie on a cool, backlit light table. A loupe comes down on one of them, and inside the glass the object comes alive: a negative turns positive, a line of type lights up, a number lifts off the page, a photograph opens into depth. Precise catalogue numbers, dates and readings are pinned to the objects. Clean, modern and quiet, with no vintage filter.
> References (grammar only): archive documentaries that push into still photographs; visual investigations that annotate real imagery (one line, one reading, one source per screen); product macro films (glass edges, transmitted light). Copy none of their layouts, typefaces, shots or music, and never name them in the film.

## 1. Essence, and what it is not

- **The objects are real**: scans of public-domain or licensed archive items, at their true proportions, with their real damage (broken corners, emulsion edges, folds, pencil marks). Nothing in them is drawn or generated.
- **Light comes from below**: the table glows a near-white cool grey; film and glass transmit it, paper glows warm at its edges, opaque things read darker than the table.
- **The loupe is the camera's door**: every dive into an object goes through a loupe that lands on it. The inside of the lens is where the object changes state.
- **Catalogue truth**: every object carries its real identifier, date and title from its holder; numbers on screen come from the record.
- **One signal colour** for marks, readings and anchors; everything else is the archive's own greys and paper tones.

**Sources and licences.** Open collections with masters and catalogue records: the Library of Congress (files on `tile.loc.gov`; records from its SRU server `lx2.loc.gov:210/lcdb` when loc.gov pages are blocked), Smithsonian Open Access (CC0), the Rijksmuseum (CC0), NARA, Europeana (check each item's rights statement). CC0, public domain and CC BY (credited) are fine. "No known restrictions", CC BY-SA and other terms are not CC0: name the terms to the user and ask. For brand history, ask the user for their scans, archive numbers and right to use them. Never stand a generated image in for an archive object. Keep a `FACTS.md` in the project folder (claim, source URL, quoted wording, or how a figure was derived) and deliver it with the film.

Not Halftone Dossier (no newsprint dots, no aged-paper grade), not Satellite Briefing (objects on a table, not the ground from orbit), not Data Storytelling (no charts; the numbers live on the objects), not a keynote (no slides or header bars).

## 2. Materials & rendering

- **One world, one camera**: every object is a textured quad on the table with a centre, rotation and scale (texture px → world units at true size). The camera is a 2D centre, zoom and roll; the table and every mark go through the same world → screen function.
- **The light table**: an emissive surface (≈ 0.97 white, slightly cool), soft falloff, diffuser noise, an aluminium frame and a dark desk beyond. It can be switched off (ambient ≈ 0.04) and flicker on.
- **Glass negatives**: transmission from the scan's positive, `T = 0.035 + 0.9 · (1 − pos)^1.25`, with a warm silver-gelatin tint; the emulsion mask comes from the scan (white margin touching the border = no glass), so broken corners show the table. Dust and scratches are procedural, anchored to the table.
- **Paper**: backlit, its colour is transmission (paper tone × light); lit lines get darker ink and brighter paper; unlit text can dim to bring one line forward.
- **The loupe**: inside the lens each pixel maps back to the table through the magnification (≈ 2.5×) with a pincushion term (k ≈ 0.16 at the rim), slightly different per RGB channel for colour fringes. Around it: a black ring with a bevel highlight and a clear acrylic skirt that refracts the table and glows at its foot. Landing and lifting, it scales by about 1.35× and casts a soft shadow.
- **The photograph space**: after the push the lens stops being a lens. A photo gains depth from a ground-plane nearness map (zero at the horizon, linear in the row below it), cut-out layers for upright subjects and a filled background; a dolly and a lateral shift drive parallax, and a subject layer may drift. Things left on the ground plane lean: centre the dolly between them.
- **Sampling**: all texture reads inside the branching lens code use explicit gradients (`textureGrad`), otherwise quads that cross a branch pick a wrong mip level and leave dashed seams.
- **Marks** live on a 2D canvas above the picture: hairlines 1.5–3 px, rings, crop corners, underlines, leaders. Table marks are clipped out under the loupe; marks inside a photograph use its forward mapping, parallax included.
- **Post**: a light vignette and fine moving grain (heavier inside photographs). No film damage, no sepia, no halftone.

## 3. Colour logic

- Neutral ground: the light table (near-white, cool) and the archive's own tones (silver greys, paper tans). Do not regrade the archive into a colour scheme.
- **One signal colour** (e.g. a signal orange) for marks, readings, anchors and the verdict; never as a fill behind pictures, never for decoration.
- Text is ink (near-black) on light areas and paper-white on dark caption plates; choose the contrast by the ground, never colour on colour.
- Positives inside the lens may be gently levelled (black and white points) so a weak scan reads; negatives stay as the glass gives them.

Example (our demo): table #F7F9FB, ink #15171A, signal #FF5A1F, caption plates rgba(14,15,17,0.74).

## 4. Type & subtitles

- **Roles**: a monospace for identifiers, dates and readings (e.g. IBM Plex Mono, 17–34 px; readings 74–120 px); a sans for labels in the film's language (e.g. Noto Sans SC or Inter, 21–36 px); a serif only for titles and the one name a photograph carries (60–76 px). OFL, self-hosted, CJK subset when needed.
- **Labels attach to objects**: an anchor dot and ring, a vertical leader, then the text. A reading sits in a dark caption plate with a small label above and the source (the catalogue number or the original wording) below.
- **Subtitles** are a caption strip at the bottom centre, on a dark plate with a 3 px signal-coloured edge. If the film is bilingual, the film's language goes on top. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Quote the source when you can**: a crop of the actual line, or the record's wording in quotation marks, beats a paraphrase.

## 5. Motion quality

- 24 fps on ones; every camera parameter on smooth monotone curves through keys (no overshoot, no stepping).
- The camera glides across the table, slows to let the loupe land, then pushes. Speed lives in the glides and pushes; holds are for reading.
- The loupe lands with a fast ease-out (≈ 0.4 s), lifts the same way. Lines draw on in 0.3–0.6 s; text wipes in from its leader side; numbers count up and land with the voice.
- What never moves: the archive's own content outside a photograph space, and the table itself.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| table glide (pan and roll) | surveying; moving to the next piece of evidence | a timeline of documents; a product family; an album |
| loupe landing + push into the lens | choosing one object; "look closer" | the claim; the key photograph; a signature |
| inside the lens: tracking along a line | reading | a letter, a ledger line, a caption, a spec |
| photograph space: dolly + parallax | being there | the event itself; the founding moment; the place |
| rise out of the lens | stepping back, the evidence noted | a transition; a summary |
| pull back to the whole table | scale; everything at once | an index, a timeline, a closing |

Framing: at a reading moment the subject fills at least a third of the frame height; readings and labels stay clear of the subtitle strip (bottom 140 px). Transitions are made by the loupe (land, push, rise, lift) and the glide; no cuts, fades to black or page turns between objects.

## 7. Sound palette

- **Ambience**: the light table's ballast hum (100 Hz and harmonics), starter clicks, room tone. Inside a photograph the hum gives way to that place's air.
- **Foley**: the loupe on glass (a clack with a high ring), paper sweeps for glides and lit lines, ticks for scales and counters, a pen stroke for a verdict, soft clicks as labels land.
- **Music**: restrained and small: a felt piano, a few strings, glass or bowed metal for the moments of seeing. Build by subdivision and register, not by drums. Leave real silences before a reveal or a verdict; the first sound after them should be the loupe, the place or the verdict.
- **Voice**: a calm narrator, short sentences that state what the object says. Music about 10 dB under the voice, ducked while it speaks; −14 LUFS.

## 8. Native moves

- **Negative to positive under the loupe.** A develop front spreads from the lens centre with a thin warm edge, turning the glass negative into its positive only inside the lens. *Fits content like:* a founder's portrait plate; a factory on a lantern slide; an X-ray film becoming the product inside.
- **The line lights up.** On paper inside the lens one line of type brightens while the rest dims, an underline draws under it, and one word or number lifts out into a reading card. *Fits content like:* a ledger entry; a patent claim; the first order on an invoice.
- **Into the photograph.** The lens rim grows past the frame while the view inside widens; the photograph gains layered depth and a subject drifts. *Fits content like:* the first shop front; a launch day crowd; an expedition camp.
- **Measuring on the photograph.** A ruler laid on the ground plane in perspective, with ticks that crowd toward the horizon and a counter that lands on the recorded figure, marked as a schematic when it is one. *Fits content like:* a race distance; a bridge span; a building's height.
- **Two records, held side by side.** Two caption cards, each with a crop of its source, held still until both are read before one is struck. *Fits content like:* a misprinted date; two versions of a founding story; specification against delivery.
- **The table becomes the index.** Pull back to the whole table; each object's tag flies into one list with its identifier and its reading. *Fits content like:* a company timeline; a collection catalogue; a product family.

## 9. Pitfalls of the medium

- **Over-magnifying a weak scan**: keep the lens interior under about 1.5 screen px per scan px; choose items by scan size.
- **The loupe sweeping over empty table**: lay objects close together, land the loupe straight onto the object (drop in, don't slide in), and glide the camera over objects, not gaps.
- **Shear in the photograph space**: one depth map for a photo with people or machines in it tears them apart. Cut upright subjects into layers, fill behind them, and keep 2.5D moves small enough that the fill is barely seen.
- **Labels that scroll away**: a label on a moving table leaves the frame before it is read; hold the camera, or fix the caption on screen.
- **Vintage creep**: no sepia, no halftone, no paper-ageing overlay. The age is in the objects, not the grade.

## 10. Engine

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


<!-- END STYLE PAGE -->
