# Complete style specifications 21


<!-- STYLE: risograph -->

- **2–3 spot inks, never more**, plus paper; every other colour is an overprint or a tint. No gradients except stepped halftone.
- Pick inks whose pairs mix into useful colours; at least one must carry a silhouette alone.
- Paper is warm off-white (around `#F4EEE2`), never pure white; paper white is a colour too (knockouts, highlights, subtitles).
- Light neutral surfaces (skin): a light tint of the palest ink. Dots of a saturated ink on skin look like a rash.
- Save the full overprint (every plate, densest mixes) for the moment that earns it.
- Example ink sets: Blue `#0078BF` + Yellow `#FFE800` + Fluorescent Pink `#FF48B0`; Teal `#00838A` + Fluorescent Orange `#FF7477`; Federal Blue `#3D5588` + Red `#FF665E` + Sunflower `#FFB511`.

## 4. Type & subtitles

- **Type is printed**: titles and subtitles live on one plate, so they misregister and grain with it. A title can be printed on two plates with a visible offset: the riso double-hit.
- Fonts (OFL): heavy grotesque for titles (e.g. Bricolage Grotesque 800), geometric sans for captions (e.g. Jost 500–700). Preload every weight before `READY`.
- Subtitles: a **paper-white knockout strip** (zero ink, small radius) with text on one plate, ~40–46 px; its edges catch misregistration fringes. Hold ≥ max(1.8 s, speech + 0.6 s).
- Prints don't fade: titles arrive with a roller wipe or on a beat and leave on a cut.

## 5. Motion quality

- **Characters act on twos** (12 fps); **camera moves on ones** (24 fps): a stepped camera reads as judder.
- **Registration is not jittered every frame.** One fixed set of offsets per shot (±1–3 px). A **kick** (≈ 8–14 px, decaying in ~0.25 s with slight ringing) on an accent; a **drift** up to ~25 px through a held moment, snapping back on the downbeat.
- Grain boils partly (about a third re-rolls per print); sheet streaks and blots change only at cuts.
- Simple cycles on few drawings; secondary motion (scarf, flag, tail) as a travelling sine wave.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Wide lateral tracking, small figure, empty sky | Travel, routine, room | a commute; a process line; a title |
| Static wide, the subject crosses the frame | Comedy of scale | a gag; an arrival; a crowd |
| Locked composition: horizon, disc, figure | Stillness, awe | a decision; a reveal; the film's one pause |
| Ground-level low angle, big foreground shapes | Energy, abundance | a burst; a harvest; a launch |
| Medium two-shot held for a look | Reaction | a joke landing; a deal; a disagreement |
| Straight top-down, long shadows | Pattern, a map | a schedule; a floor plan; a game board |
| Push into a halftone field until dots are shapes | Entering the print | a close look at data; a memory; a cell |
| Pull back to reveal the paper | It was one sheet | a series; an archive; a summing-up |
| Match cut on a flat shape | Continuity through form | a time jump; cause and effect; before/after |

Framing: lots of paper and solid ink, text on empty sky or a knockout strip. Transitions: overprint growths, roller sweeps, shape match cuts, hard cuts on beats. Never a cross-dissolve, never a soft digital wipe.

## 7. Sound palette

- **Instruments**, as options: warm, dry, handmade, slightly lo-fi: upright or electric bass, vibraphone or marimba, nylon guitar, whistled or hummed melody, Rhodes, toy piano, brushed kit, shaker and rim clave, a small drum machine through tape saturation.
- **Layering like plates** (an option): each new plate brings one instrument, and they can leave one by one.
- **The machine is the signature foley**: feed "shhk", drum "ka-chunk" at a plate arrival, motor hum, a sheet landing on a stack, a guillotine cut. Other foley dry, close and papery, following the story's materials.
- **Silence**: a held bar with reverb tails cut, at most ambience or one distant sound; it pairs with a registration drift, and the snap brings everything back.
- **Mix**: dry and close; music ducks ~8 dB under voice; −14 LUFS. Voice relaxed and conversational, short lines, verified with whisper. No grain added at mux: it is in the print.

## 8. Native moves

A menu: use the ones your story needs.

- **Plates as narrative.** The world gains a plate at each turning point. *Fits content like:* a product arriving as a new ink; a city history, one ink per era; colour returning during a recovery.
- **Two inks, a third where they meet.** *Fits content like:* a merger; a duet; two data sets whose overlap is the finding.
- **Overprint transition.** A shape of one ink grows over the frame, turning everything beneath into the mix, then shrinks into the next scene's key shape. *Fits content like:* a pill dissolving; a spotlight becoming a moon; a stamp becoming a map pin.
- **Registration as rhythm and feeling.** Kicks on accents, drift in a held moment, snap on the downbeat. *Fits content like:* nerves before a speech; dizziness; a memory coming into focus.
- **Reflections as separated plates.** Each plate wobbles on its own phase. *Fits content like:* a shop window; heat over a road; a coffee surface.
- **Knockout reveal.** A shape made only of missing ink; its plate arrives later. *Fits content like:* a missing piece; a secret; a logo hidden in plain sight.
- **Halftone scale.** Dots grow into shapes as the camera pushes in. *Fits content like:* population; rainfall; a crowd that turns out to be people.
- **It is a sheet of paper.** The print can be stacked, folded, cut or pinned; grain boils like a flipbook of prints. *Fits content like:* a zine; a poster series; a flyer passed hand to hand.

## 9. Pitfalls of the medium

- Three halftoned plates in one area = mud → two plates, one tint.
- `fract(p*vec2(233.34,851.73))` draws vertical stripes across solids at 1080p → a well-mixed hash (`fract(vec3(p.xyx)*.1031)` family).
- Per-frame registration jitter and sheet streaks flicker and blow up file size → fixed offsets per shot, kicks on accents, sheet noise at cuts, partial boil.
- JPEG screenshots (4:2:0) smear saturated dots → PNG frames into a lossless yuv444 intermediate, encoded once with `-tune grain`; check at 100 % and 50 % for moiré.
- The halo layer must copy the canvas transform, or zoomed shots draw the subject at the wrong scale.
- Additive `over()` inside a transparent layer loses its meaning → overprint on the plate canvas.
- A main colour without the first plate floats loose in one-ink frames → build palette recipes up from the one-ink silhouette.
- `evenodd` fills of arches fill solid → trace the inner edge in the opposite direction.

## 10. Engine

In `demo/`: `riso.js` (print shader: plates, halftone, grain, registration, kicks and drift, gates, roller sweeps, reflection wobble), `draw.js` (`ink(b,y,p)` densities, `over()` overprint, `layer()` paper halo, 2-bone IK, limbs), `sheet.js` (model sheet with a "plates = story" row via `S.mask`), `tools/video_png.mjs` (PNG frames → lossless intermediate), `tools/mux.sh`. Minimal new frame: two plates (R = teal, G = orange); a solid teal hill, an orange disc drawn with `lighter` so it darkens where it crosses the hill, a 40 % teal sky band, a figure knocked out with `layer()`.

## 11. Variation space

You decide the inks and what each plate means, the structure, characters (or none), opening, ending, camera path and pacing. All far from our demo:

- Structures: **two inks in dialogue** (two subjects alternate shots and only overlap at the end, making the third colour); **subtraction** (start at full overprint, lose a plate at each loss, end in one ink); **a zine** (each shot a page turned, each page a different two-plate pairing).
- Openings: **a knockout** (a blank shape in a full-colour field, filled by its plate seconds later); **dots first** (extreme close-up of halftone that pulls back into an image); **ghosts converge** (three colour ghosts drift together and snap into a readable frame on the first beat).
- Endings: **one ink left** (plates lift away until the last line stands in one colour); **the print on a wall** (the last frame becomes a poster pasted up inside the world it showed); **a folded sheet** (the print folds into something the story needs: a boat, an envelope, a ticket).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: halftone-dossier -->

# Halftone Dossier — Style Prompt

> A retro print case file: cream archive paper, overprinted halftone dots in a few flat inks, huge heavy headlines with misregistered shadows, rubber stamps that slam, and thick-outlined characters. The film is a file that is read out one exhibit at a time.
> References (grammar only, never copy): Ben-Day-dot pop-art printing (Roy Lichtenstein era comics) for dot density as shading; riso/offset overprint zines for multiply layers and misregistration; police mugshot height charts and case-file folders for the framing device; Japanese variety-show telop captions for the keyword-highlight caption bar.

## 1. Essence, and what it is not

- **The whole film is paper.** A warm cream sheet with low-frequency mottling, fine grain, a vignette and a fold; dark scenes are printed on it too, never glowing.
- **Shading is never a gradient**: it is halftone dots whose size follows a density field. Two or three dot layers at different screen angles overprint (multiply); that is the "printed" feel.
- **Bureaucratic apparatus**: case numbers, file chips, numbered exhibits, height charts, name plates, stamps. Their seriousness is the frame; the subject can be grave or trivial.
- **Loud but readable**: one idea per 2–4 s card, one big headline, one visual gag or exhibit, one caption line.

Not Risograph (no grainy two-ink riso texture as the whole look, no zine collage), not Swiss motion (no grid-driven kinetic type on white), not Game Show Flat (no candy sets, no rhythm-game rounds). Dots, paper and stamps must be visible in every frame.

## 2. Materials & rendering

- **Paper layer** (canvas, multiply over everything, built once): an upscaled random tile for mottling, per-pixel noise with a slight warm bias, a radial vignette, a faint centre fold.
- **Grain layer** (per frame): a few hundred paper-coloured specks and fewer ink specks, reseeded every 2 frames: dust on the print, not film grain.
- **Halftone**: a rotated grid of circles drawn as one path; step 20–26 px; screen angle different per layer; radius = density × step × k with k 0.6–0.72 (around 0.7 dots merge into solid ink). Density fields: radial (halos, blooms, corner glows), edge (dots crowding the frame border), linear ramps ("lit from above"). The second layer is multiplied so inks overprint.
- **Halftone-filled numerals and shapes**: a flat fill overprinted with a darker halftone clipped to the glyph; giant numerals may bleed off the frame.
- **Line boil**: turbulence displacement (small, ~5 px) reseeded ~10×/s plus a fine ink-grain mask that eats a little of every fill. Characters and hand-drawn props only; **never** on text, halftone, HUD or captions.
- **Characters**: chunky shapes with a heavy ink outline (~7 px), flat fills, a lighter belly or face area, glossy eyes (ink ellipse + two highlights) that can squint, blink or close into a happy arc. One head rig shared by all body poses.
- **Stamps**: a double rounded rectangle and bold text through a coarse ink-grain + displacement filter so edges are rough and the ink mottled; ~93 % opacity, tilted ±10°.
- **Props**: starbursts, speech bubbles, confetti, radial rays, sticky notes, folders, clocks: all flat fill + ink outline.

## 3. Colour logic

- **A paper ground, one dark ink, and four or five flat spot inks.** The dark ink (navy, black-brown or deep green) carries every outline, body text and the caption bar, and is the fade-out colour.
- One ink is the **overprint shadow** colour (misregistration offsets, caption shadows); one is the **highlight** for keywords and numerals; one warm red is reserved for stamps and alarms.
- Flat inks only. No gradients, no transparency ramps; tone comes from dot size and overprint.
- **Night or "secret" scenes** switch to a dark ink ground with a lighter dot layer of the same family, still multiplied by the paper.
- Characters may own one or two local colours (fur, clothing) that appear nowhere else.
- Example palettes: cream / navy / cobalt / hot pink / yellow / red; manila / sepia-black / teal / mustard / vermilion; off-white / forest green / tomato / sky / ochre.

## 4. Type & subtitles

- **Headlines**: a black-weight serif (e.g. Noto Serif SC 900 for CJK; a black slab for Latin), 100–230 px, left-aligned near the margin, with a **misregistration shadow** (+8/+8 px in the overprint ink, multiplied).
- **Display / numerals**: a fat rounded display face (e.g. Bagel Fat One) for names, big numbers, times.
- **Interjections**: a playful hand face (e.g. ZCOOL KuaiLe), paper fill with a thick ink stroke and an offset shadow.
- **Data / HUD**: a heavy monospace (e.g. JetBrains Mono 800) for case numbers, dates, rulers, file names.
- **Captions and stamps**: a black-weight sans.
- **Cards are the subtitles.** A headline per beat, plus a **caption bar**: a dark-ink rounded pill with an overprint-ink offset shadow, paper-coloured text, the **keyword in the highlight ink**. It pops in after the headline and holds ≥ max(1.8 s, speech + 0.6 s). With narration, the caption bar carries the spoken line.
- **HUD**: case number and a chapter chip top-left, a status (REC dot, date) top-right; colours invert on dark scenes.
- Latin runs 2–3× longer than CJK: smaller headlines, 1–2-word stamps (GUILTY, CLOSED), a tighter per-character stagger.

## 5. Motion quality

- 30 fps transforms; **line boil at ~10 fps** on characters, so the drawing breathes while positions stay smooth.
- **Everything enters with overshoot** (back ease, 0.3–0.45 s): rising from below the frame or scaling from 0. Nothing fades in.
- **Per-character pop** for headlines: each glyph drops 30–100 px and squashes in, stagger 0.05–0.08 s (0.02 s for small text).
- **Stamp slam**: ~0.09 s from ~2.6× to 1× (ease-in), then a small damped bounce; camera shake, flash and stamp sound on the same frame.
- **Squash landings** preserve volume (`scale(1/sq, sq)` with a damped cosine).
- **Idle life**: breathing, tail or hair sway, blinks at scripted times, twinkles, a blinking REC dot or clock colon.
- **Dot wipe transitions**: a coarse grid of circles grows to full cover and shrinks back (~0.44 s) with a diagonal delay; the scene switches while covered. Each cut may take its own wipe colour. A hard cut is the contrast tool, on a big hit.

## 6. Camera grammar

A 2D camera group over a flat, frontal page. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal with a small beat pulse (~0.6 %) | the page as a poster, grooving | a title; a list; an accusation |
| Slow push-in (1 → 1.05–1.08) | scrutiny, rising tension | a profile; a summary before a verdict |
| Shake with quadratic decay (5–26 px) | impact | a stamp; a crash; a landing |
| Flash frames (white overlay ≤ 0.95 → 0, capped at 0.5 for big hits) | being photographed, a revelation | a mugshot; a verdict; evidence found |
| Pan across a pinned board | connection between exhibits | a timeline; suspects; a chain of events |
| Snap zoom into a halftone detail until dots are huge | "look closer" | a fingerprint; a signature; a number |
| Page turn / folder slide | next file, next chapter | a second case; a flashback |
| Pull back to reveal the whole desk | the file is one among many | scale; "this happens every day" |

Compose like a printed page: headline top-left, subject right-centre, caption bar bottom-centre, HUD in the corners. Transitions: dot wipe or hard cut; no dissolves.

## 7. Sound palette

- **Synth pop-print toolkit**: synth kick, snare, clap, hat; a square-ish 8th-note bass; triangle pad; a **marimba-like pluck** (fundamental + ~4× partial) for melody; pizzicato and finger snaps for sneaking; music-box bell for tenderness.
- **Foley follows the print and the gag**: stamp = pitch-dropping boom + click (a crackle for big ones), camera shutter, paper slides and folder flaps, typewriter or keyboard clicks, whooshes into wipes, pops on every glyph, boings and plops for characters, glass or ceramic for breakables, synthesized animal or creature voices (formant sweeps).
- **Silence before the stamp**: empty the music just before a verdict so the stamp lands alone. Other options: a snare roll + rising sweep into a reveal; stripping to bass and snaps for a secret scene; a bell arpeggio as a tag; a single sustained pad under a sad exhibit.
- **Voice** is optional; cards carry the film. If narrated: a dry, deadpan report voice, never breathless.
- **Mix**: SFX ahead of the music on impacts, soft-clip master, −14 LUFS, true peak ≤ −1 dB.

## 8. Native moves

A menu: use the ones your story needs.

- **The accusation frame.** A topic becomes "the case of X": list its counts. *Fits content like:* a cognitive bias on trial; a city's traffic problem; a plant that won't stop growing.
- **Numbered exhibits.** Each beat gets a giant halftone numeral behind it. *Fits content like:* five causes of a blackout; three clauses of a contract; the stages of a recall.
- **The stamp.** A verdict is a physical slam. *Fits content like:* APPROVED on a grant; EXPIRED on a policy; VERIFIED on a rumour check.
- **The mugshot.** Frontal subject, height chart, name plate, flash. *Fits content like:* a new species; a product teardown; the "suspect" in a bug report.
- **Evidence board.** Exhibits pinned and linked with string, then shaken. *Fits content like:* a supply chain; a family tree; a heist's timeline.
- **Dot density = emotion.** Dots swell into a halo, crowd the edges for tension, bloom radially for joy. *Fits content like:* a record broken; a deadline closing in; a reunion.
- **Redaction.** Black bars print over words and lift one by one. *Fits content like:* a leaked memo; a surprise party plan; spoilers.

## 9. Pitfalls of the medium

- **Fonts not loaded before layout** → per-character positions computed with a fallback font, glyphs overlap. Preload every family against the whole page source and the built text; runtime strings must use only characters that appear in the file. Use `font-display: block`.
- **Boil on text or dots** turns them to mush → filter only characters and props.
- **Clip-path ids are global** → every clipped numeral needs a unique id.
- **Time-windowed scenes** → an element invisible before its cue needs explicit opacity 0 for `t < t0`.
- **A dot wipe short of full coverage** at the cut shows the hard switch; make the max radius cover the grid cell's diagonal.
- **A 100 % white flash** reads as a dropped frame → cap at ~0.5.
- **Dots too small** (< ~14 px step at 1080p) alias into moiré after encoding.
- **Too many inks** lose the print feel → at most five plus paper.

## 10. Engine

Everything lives in `demo/index.html`: helpers (`el`, `txt`, `tf`, `seg`, easings, `measure`), per-character text (`chars` + `charsPop`), **halftone** (`halftone()` with `radial`/`edge` density fields), `caption()` bar, **stamp** (`stampEl` + `stampAnim`), a mascot rig with a `setFace` interface, `scene(t0, t1, build)`, HUD chips, dot wipe (`WIPES`), paper + grain (`buildPaper`, `drawFx`), `render(t)`. `demo/render.mjs` renders stills and video; `demo/music.py` synthesizes score and SFX. Line ranges and a minimal scene: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space


<!-- END STYLE PAGE -->
