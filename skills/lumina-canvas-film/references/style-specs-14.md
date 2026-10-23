# Complete style specifications 14


<!-- STYLE: paper-lantern -->

- **Text in the picture is paper**: titles, letters, poems and captions are cut strips inside the box, revealed by growing from an anchor edge (scale the texture repeat with the mesh so glyphs aren't squashed), with an optional small seal.
- Chinese: an OFL brush font (e.g. Ma Shan Zheng) for titles, a running script for handwriting, Noto Serif SC for subtitles. Latin: an OFL serif (e.g. Cormorant) at similar weight.
- **Subtitles** are a quiet burned-in line under the box (serif 500, ~40 px CJK / ~38 px Latin, warm off-white, soft shadow, ~74 px from the bottom), fading in just before the line. Split long lines at the comma nearest the middle (~21 CJK / ~42 Latin characters).
- **Words that appear as paper are not subtitled**: never show the same words twice.
- Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **Everything moves like paper on a stick**: layers slide (x/y), rotate about a pivot, scale in from 0 along one axis ("written out"), or light up. No squash and stretch, no morphing, no bending.
- **Jointed figures**: a body sheet + separate limb sheets anchored at the joint; animate rotation only.
- **Light cues are the big motion**: the source, then each layer's translucency in a ~0.4 s stagger, then windows, then flicker (`1 + .06·sin(7.3t)·sin(3.1t)`).
- **Hard action lands on spoken words** (use whisper word timings): an object slams, a character flashes, a light arc grows on its word.
- Hand-held micro-drift on the camera (~0.6 mm) keeps a locked frame alive. Render on ones at 30 fps; never step.

## 6. Camera grammar

A vocabulary, not a route. The lens is small and the box is shallow: moves are short. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow dolly in, nearly frontal | intimacy; being drawn into a place | a memory; a detail that matters; a lit window |
| Slow dolly out | context; loneliness; scale | a figure alone; before/after; the whole place at once |
| Rack focus between layers | attention moving in depth | two people near and far; a clue behind; now and then |
| Lateral travel with depth parallax | journey; time passing | a road trip; a process in stages; a timeline |
| Top-down layer stack | a made thing seen as a craftsman sees it | a recipe; a letter; a map; a product being assembled |
| Pull out of / push into the box | the frame as object; "this is a story told" | a keepsake; a framing device; returning to the present |
| Locked frame with only light changing | waiting; the passage of a day or a night | a vigil; seasons; a city going to sleep |
| Tilt up/down the stack | climbing; falling; sky vs ground | a mountain; a well; hope and weight |
| Near-plane occluder wipe | a curtain between scenes | chapter changes; dreams; a secret revealed |

Framing: the story layer in focus, foreground and far layers soft; box edges fully out of frame inside, clearly in frame outside, never half. Transitions: dissolves (0.5–1.2 s), an iris, light off/on, a near-plane curtain whose halves meet exactly. No whip pans, no digital zooms.

## 7. Sound palette

- **Instruments** that sit like light behind paper: felt piano, music box, celesta, harp or plucked zithers, bamboo flutes, soft strings; a solo instrument of the topic's culture. No drum kit; percussion only as single soft strokes (woodblock, small gong, hand drum).
- **Foley is paper and light**: switch click + rising shimmer when a light turns on; paper rustle and slide; card-stock tap; lid thud; chimes on reveals; soft whoosh for curtains; beds from the scene (river, rails, city hum, crickets, snow wind).
- **Silence**: the lamp switched off — all sound but a room tone drops out, then returns with the light.
- **Mix character**: voice compressed and forward (RMS ~−18 dB), music underneath with ~5–6 dB of ducking under speech, foley low (−24…−34 dB), peak-limited, final at −14 LUFS.
- **Options**: a new instrument entering when the film changes place; one foley sound per light cue; a music hand-over solved backwards so a swell lands on the line that matters.
- **Voice**: warm, a storyteller at a table, not an announcer. Proof every line with whisper; for Chinese polyphonic characters feed TTS a homophone and keep the real text for subtitles.

## 8. Native moves

A menu: use the ones your story needs.

- **The lamp turns on.** Source, then far layers, then windows light up one by one. *Fits content like:* a shop opening at dawn; a startup's first customer; a stadium before a match.
- **Two windows, one light.** Two lit places sharing one light source (a moon, a lighthouse, a satellite). *Fits content like:* a long-distance friendship; two labs working on the same problem; a sister city pair.
- **Depth as distance.** A stack of ranges or streets makes "far away" visible; travel moves layers at speeds proportional to depth. *Fits content like:* a migration route; shipping a parcel; the history of a river.
- **Paper that writes itself.** A strip grows from its edge on the spoken word. *Fits content like:* a recipe; the terms of a treaty; a child's first word.
- **The box as keepsake.** The camera finds the real lamp in a room, real objects lit by its spill. *Fits content like:* a wedding anniversary; a product unboxing; a museum object's story.
- **Light burst from an opened thing.** A lid lifts and analytic glow spills out. *Fits content like:* a gift; a discovery; a new idea.
- **Silhouette in a window.** One jointed figure inside a lit frame. *Fits content like:* someone working late; a portrait of a craftsperson; a patient waiting.

## 9. Pitfalls of the medium

- `destination-out` cut-outs need an **opaque fillStyle** before punching, or the hole is half-cut (`props.js` `cut(x, fn)` does it).
- Soft shadows bleed and halo: layers that must not take part need **both** `shadow: false` and `recv: false`.
- A transparent radial-gradient texture shows a square edge as an additive glow → use an analytic shader falloff (`burst()`).
- A near-plane curtain whose halves don't meet at their **front edges** leaves a slit of the old shot.
- Sheets larger than the cavity poke through the frame in outside shots.
- **Grade state must not carry over** between shots: every grade key a shot omits must fall back to a default each frame, or renders depend on which frame a worker started on (visible pops at worker boundaries).
- Headless Chrome must run with GPU flags; SwiftShader is ~6× slower.

## 10. Engine

In `demo/src/`: `paper.js` (`sheet()` = one lit paper layer; `skyPanel`, `moon`, `text`, `burst`), `stage.js` (scene, top spot, `aim()` camera), `post.js` (DoF, bloom, transitions, grade), `room.js` (the real box and table), `art.js` / `people.js` / `props.js` (motifs, jointed figures, props), `lib.js`. `src/main.js` schedules shots, each `build(E) → { S, update(t), post(t), grade(t) }`. API table and a minimal shot: [DEMO.md](DEMO.md) "Engine reference".

## 11. Variation space

You decide the places, the figures (or none), the ladders, the light source, whether the real world appears, the opening, the ending and the camera path. All far from our demo:

- Structures: **one window, one year** (a locked lamp; the scene inside changes season by season, light the only transition); **a vertical stack** (the film tilts down through sky, city, street, underground, each a chapter); **a relay of objects** (a single object passes hand to hand across five small boxes, each a different ladder).
- Openings: **already lit, mid-scene** (a figure walking through a lit street; we learn it is paper only when the camera racks focus); **darkness and one hole** (a single pinprick of light widens into a moon, a door, an eye); **top-down** (hands' view of a sheet being cut; the cut sheet slides into the stack).
- Endings: **the lights go out one by one**, the last window last; **rack focus to the front layer** until the story blurs into warm light; **a new sheet slides in** at the front, starting the next story.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: risograph -->

# Risograph Print — Style Prompt

> Animation that looks printed, frame by frame, on a stencil duplicator: two or three translucent spot inks overprinted on warm paper, halftone dots, ink grain, and plates that never quite line up.
> References (grammar only): Tom Haugomat's riso illustrations (colour fields and silhouettes, a small figure in a large world, extra colours made by overprinting); Jacques Tati's *Jour de fête* (comedy staged small in a wide frame, everyday sounds as rhythm); real riso prints (translucent inks, misregistration, pinholes, feed streaks). Copy none of their characters, compositions or palettes.

## 1. Essence, and what it is not

A risograph prints **one colour at a time**: each colour is its own stencil ("plate") with its own drum of translucent ink. That one fact makes the look:

- **A tiny palette**: 2–3 spot inks on warm off-white paper.
- **Overprint mixing**: inks multiply, so two inks make a third colour and all three approach black; a tint of one ink over a solid of another gives the brightest mixes.
- **Misregistration**: every plate lands a few pixels off; edges show slivers of paper or a coloured halo.
- **Halftone dots** for mid-tones, each plate on its own screen angle; **imperfect ink**: pinholes in solids, streaks along the feed direction, blotchy density.
- **Flat shapes, no outlines**: forms are colour fields and silhouettes.

Not flat vector art with a noise overlay (every colour comes from the plates), not CMYK pop-art halftone (no process colours, no keyline), not screen-print posters (riso ink is translucent and grainy, not opaque). **Never** show the RISO brand, logo or machine trade dress; ink names are colour references only.

## 2. Materials & rendering

**Pipeline.** Draw each frame into **one RGB canvas where each channel is one plate's density** (R = ink 1, G = ink 2, B = ink 3; 0 = none, 1 = solid). `source-over` gives true **knockouts**; `globalCompositeOperation = 'lighter'` adds ink only to the channels you set: a true **overprint**. A WebGL2 shader "prints" it:

- per plate: offset in px + tiny rotation → misregistration;
- halftone: cosine spot function on a rotated grid, period ~6–8 px at 1080p, anti-aliased threshold; densities ≥ ~0.9 print solid; screen angles ≥ 15° apart;
- grain on the dot threshold, pinholes in solids, density varying with a feed-direction streak and a slow blot noise;
- composite `paper × Π mix(1, ink_i, coverage_i)`, with faint paper fibre;
- dots anchored to the **paper** (screen), not to objects: a pan slides the image under a fixed screen, as if each frame were printed anew;
- a per-plate **gate** and a **roller sweep** (moving edge, slightly heavier ink band) let a plate arrive mid-shot.

**Composition rules.**
- Every area uses **at most two plates, at most one of them as a tint**. Three halftones on top of each other = mud.
- Big flat shapes, lots of solid paper and solid ink; halftone in a few stepped bands (e.g. 20 / 40 / 60 / 100 %) for skies, shadows, distance.
- Characters get a **paper-white knockout halo** (4–5 px): stamp their layer in a ring with `filter: brightness(0)` (zero ink = paper), then draw them. Plates misregister around it, so it picks up coloured fringes like a real trap.
- One horizon, one big flat field or disc, one small figure; the figure's head against the flattest colour in the frame.
- Design for the **one-plate version**: every main colour contains some of the first plate, so a one-ink frame still reads as a complete silhouette. A deliberate exception stays blank paper until its plate arrives: a reveal.

## 3. Colour logic

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


<!-- END STYLE PAGE -->
