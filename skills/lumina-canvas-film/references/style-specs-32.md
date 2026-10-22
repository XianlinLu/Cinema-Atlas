# Complete style specifications 32


<!-- STYLE: rubber-hose -->

- Structures: **a singalong** (verse and chorus, the bouncing ball carrying the message while the set acts out each line); **a talent show** (objects take turns on a stage, the smallest wins); **a relay** (a thing passed hand to hand across a town, each hand-off a new instrument on the melody).
- Openings: **out of the inkwell** (a pen draws the hero, who hops onto the set); **a curtain rise** (the band tuning up; a baton starts the film); **an iris on one eye** (it blinks, the iris widens to show whose eye it is).
- Endings: **the card pulled over** (a character drags "The End" in front of itself mid-gag); **the film snaps** (the frame burns, a gloved hand splices it for one last bow); **the band packs up** (instruments leave until one note remains).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: cel-anime-80s -->

# 80s Cel Anime — Style Prompt

> Hand-painted cel animation from the golden age of Japanese OVAs, re-created in code: flat two-tone cels over airbrushed backgrounds, backlit neon, limited-animation timing, played back as a late-80s videotape on a CRT television.
> References (grammar only): 1980s Japanese OVA and TV cel animation in general (painted-background vs flat-cel contrast, backlit light, held drawings, speed grammar, city-pop openings). Borrow the era's craft, never a specific work's characters, mecha, logos, place names or signature shots.

## 1. Essence, and what it is not

Four layers, and the contrast between them is the look:
- **Background painting**: soft airbrushed gradients, glowing windows, wet reflections; painted once at load (colour + emissive pair), then only slid.
- **Cel** (characters, vehicles, props): flat fills, **hard-edged** shadow and highlight shapes, **coloured** outlines, never pure black; stepped at 12 or 8 fps.
- **Light**: backlit cel (透過光): signs, lamps, title letters glowing *through* the frame; flares, halation.
- **Playback**: videotape on a CRT: chroma bleed, scanlines, grille, phosphor glow, darkened corners, faint noise.

If a frame looks like modern digital anime, one layer is missing. Not moe anime (round eyes, giant irises, hatched blush), not vector clip-art (uniform black lines, gradients in shapes), not a film-print pastiche (no gate weave or scratches: this is tape).

## 2. Materials & rendering

**Cel rendering.** Fill, then a **hard** shadow crescent, then a **hard** highlight crescent, then the coloured outline. No gradients inside a cel shape (exception: one "harmony" painted still at a peak). Automatic shading: clip to the shape and fill `shape − shape shifted toward the light` with the shadow colour (even-odd); the same shifted away for the highlight and for a saturated neon **rim light** (2–4 px). Add hand-placed cast shadows. Outlines ~2–3 px at 1080p, scaled down (0.45–0.8×) in extreme close-ups. **Colour models per lighting** (色指定): define each character in daylight, derive other sets by multiplying lit / shadow / line separately, plus a backlit silhouette set with a warm rim.

**People the 80s way.** Construct the head (sphere + jaw): long egg-shaped face, soft-point chin, far eye foreshortened with a cheekbone turn in 3/4. **Almond** eyes near the vertical middle of the head, a thick upper lash line flicking outward, a tall oval layered iris, two highlights, long thin brows. Nose = a shadow plane + one stroke; one faint blush layer, never hatched. Hair in overlapping locks with sharp uneven tips over a wider dark under-layer, a continuous "angel ring" highlight with a zigzag lower edge. Lines: skin thin warm dark brown, hair dark purple; only hard props near-black. Emotion lives in brows, lid height, iris size, mouth corners and shoulders. Build and approve a **model sheet** first; draw every shot from the same head function.

**Backgrounds.** Painted once at load: sky gradients, airbrushed clouds with lit undersides, buildings or landscape with painted light sources, and always a matching **emissive plate** that slides with the colour plate. Wet ground = a flipped, blurred, streaked copy of the plate darkened with ripple bands. Generic sign words only, never brands. Moving plates get a light horizontal smear (~16 px) against strobing.

**Light and lens.** Bloom strongly from the emissive canvas, weakly from the colour canvas above ~0.9; tint the widest bloom red-orange (halation). Flares: star-burst, anamorphic streak, hexagonal ghosts through frame centre. Stamp every cel's silhouette in black onto the emissive canvas so glow never bleeds through it.

**Videotape + CRT, restrained and deterministic:** chroma bleed (sharp luma, horizontally blurred and slightly shifted chroma), fine scanlines anchored to output pixels whose gap shrinks on brights, a faint RGB grille, phosphor glow, darkened corners without curved borders, faint signal noise. Subtitles are composited inside the pass after grading. Two optional accents: a **power-on** (dot → line → picture) and **tracking noise** (a few frames of tearing, rolling band, vertical hop). Check moiré on a 720p downscale. Frame: full 16:9 as a theatrical feature (4:3 pillarbox is valid for an OVA feel).

## 3. Colour logic

- Painted plates carry gradients and atmosphere; cels are flat, few-colour, saturated. Each time of day gets its own colour model, never a filter over the frame.
- The protagonist has **one accent colour** that pops in every lighting set. Line colours are dark versions of their fill.
- Skin gets its own colour in every set; multiplying daylight skin by a tint turns faces pink under neon.
- Examples: night city (indigo, violet, neon magenta, cyan, window gold); seaside noon (cobalt, white cumulus, sand, coral); classroom dusk (amber, chalk green, brown wood, purple shadows).

## 4. Type & subtitles

- Subtitles live on the tape, composited inside the CRT pass: a semi-condensed sans (e.g. Barlow Semi Condensed 600, ~50–56 px), cream-yellow with a thick dark outline and soft shadow, ~96 px above the bottom; a second speaker may take a second colour and a small boxed tag. Hold ≥ max(1.8 s, speech + 0.6 s); a line yields to the next.
- Titles: heavy italic Latin in a **chrome gradient** (sky → white horizon line → violet → pink → gold), dark + neon outlines, optional katakana line (e.g. Dela Gothic One), glowing through the emissive layer, flickering on at 12 fps with a light sweep and a star glint.

## 5. Motion quality

- **Characters on twos (12 fps)**; performance beats (blinks, eye openings, lip flaps, gestures) on threes (8 fps). Camera, light sweeps, flares and rain on ones (24 fps); a stepped camera judders.
- **Cycles**: hair and cloth as ribbons driven by a travelling sine, 4-drawing cycle (6 when calm); bounce = a 12 fps jitter of a few px.
- **Move light, not drawings**: coloured bands sweeping across a held cel (`source-atop`).
- **Impact frames**: 2 frames of an inverted or monochrome silhouette over radial lines, then the result.
- **Hold the peak**: a painted still with a slow pan, only cycles moving.
- Fast blinks (one 8 fps closed drawing); eye openings in three drawings; lip flaps of 3–4 shapes at 8 fps ending on a held expression.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Multiplane crane over a tall plate | a world revealed layer by layer | arriving; descending into a place; rising above it |
| Side tracking, 3–4 parallax layers | steady momentum | a journey; a chase; progress |
| Rear view into a pseudo-3D canyon | speed, pressure ahead | a race; a tunnel; a countdown |
| Held bust with light bands | speed or tension without animation | a drive; waiting; a decision |
| Insert with bokeh and a sliding highlight | this object matters | a letter; a key; a ticket |
| Extreme close-up on eyes | resolve, recognition | a choice; a promise |
| Slow pan across a painted still | awe, a held breath | a peak; a memory; a landscape |
| Radial speed lines + one-beat freeze | the instant before impact | a leap; a collision; a goal |
| Truck-in through a window or screen | entering another world | a flashback; a broadcast; a dream |
| Locked two-shot with lip flaps | conversation | banter; a confession; an argument |
| An earlier composition repainted | what changed | after a storm; years later |

Cut on bars. Framing: cels readable against the painted plate; keep the lower ~120 px clear for subtitles. Transitions: cuts, white flashes, impact frames, tracking noise at a tape-related beat; no digital dissolves or wipes.

## 7. Sound palette

- **Instruments** (city pop, synth funk, anime-opening pop): saxophone or synth-brass lead, FM electric piano with a bell transient, slap bass, chorus-y 16th guitar chanks, gated-reverb snare and big toms, drum machine, arpeggiated analog synth, string pad, FM bell sparkle. Extended jazz-pop harmony (maj7, 9ths).
- **Techniques, as options**: band-pass the score to cassette/AM when a diegetic source plays, then open it; a brass hit on a title; a drum fill left open for an effect; one beat of true silence before a peak; a semitone lift for a last chorus.
- **Foley** (synthesized): engines from an RPM curve, rain, tire hiss, wind, bells, radio squelch, impacts, sparks, cassette clicks, crowd murmur, door buzzers, footsteps on wet pavement; tape accents get their own thunk, whine, hiss.
- **Voice**: an English-dub feel, short lines; a second voice through a phone/radio band-pass (~380–2800 Hz). Verify every line with whisper.
- **Mix**: limit then compress TTS, voices ~10 dB over ducked music (duck ~9 dB), beds ducked ~3 dB, choruses louder than intros, two-pass loudnorm to −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Small flat hero in a huge painted world.** *Fits content like:* a first day in a big company; a child in a museum hall; a lone researcher at an observatory.
- **Stillness as drama** (held close-up or harmony still). *Fits content like:* an exam result; a goodbye at a gate; an unveiling.
- **Backlit light.** *Fits content like:* a lantern festival; a screen full of code; a lighthouse; stage lights.
- **Speed grammar** (speed lines, looping plates, impact frames). *Fits content like:* a sprint final; a data packet crossing the world; a kitchen rush.
- **Light-band sweep on a held cel.** *Fits content like:* a night train; a scanner reading a page; a heartbeat quickening.
- **A song as an object** (tape, radio, jukebox changes the score). *Fits content like:* a band's origin; a family memory; a call-in show.
- **Tape artefacts as punctuation.** *Fits content like:* found home video; a rewind to the past; an interrupted broadcast.
- **Colour-model change** (one place, another hour). *Fits content like:* a day in a shop; a farm's seasons; before/after a renovation.

## 9. Pitfalls of the medium

- White cels bloom pink → bloom from the emissive canvas; weak, high-threshold bloom on colour.
- Neon bleeds through characters → silhouettes stamped into the emissive canvas.
- Black holes in highlights → clamp before S-curves.
- Thick rim light swallows thin shapes → 2–4 px offsets.
- Hair like tentacles, a face like a paper mask, moe eyes, uniform black lines → the drawing rules in §2.
- Pink faces under coloured light → skin gets its own colour per set; weaker light sweeps on faces.
- Front views are the hardest drawing → hide them behind a visor, a windscreen or backlight when you can.
- Pseudo-3D points behind the camera flip into the sky → clamp z to the near plane.
- Canvas silently falls back to a serif → `document.fonts.load` every weight before painting.
- CRT detail inflates files → noise in the shader, only `noise=c0s=2:allf=t` in ffmpeg, CRF ≈ 23; loudnorm in two passes with `linear=true`; don't let a limiter flatten the dynamics.

## 10. Engine

In `demo/`: `cel.js` (path, cel, ribbon, flutter), `pal.js` (colour models), `head80.js` (80s head, 3 views × expressions), `hands.js`, `bg.js` (painted plates, crane plates, wet reflections), `fx.js` (rain, speed lines, flares, trails), `post.js` (WebGL tape + CRT pass: bloom, grade, subtitles, power-on, tracking noise), `hud.js`, `music/score.py` (numpy FM/slap/brass synthesis), `tools/`. `?test=model|close|side` draws model sheets, `?raw=1` skips the CRT pass. A minimal new use: a harbour sunset plate with its emissive pair, one cel boat shaded with `cel.js`, through `post.js`.

## 11. Variation space

You decide the structure, the characters, the world, the opening, the ending, the camera path, the pacing and the colour models. All far from our demo:

- Structures: **slice of life in four seasons** (one place, four colour models, a small change each time); **two-hander dialogue** (a locked two-shot comedy that breaks into one fantasy sequence); **the mock opening credits** (a character roster introduced one by one, each with a pose and a name card).
- Openings: **in the middle of a conversation** (lip flaps already moving, no establishing shot); **a TV being switched on** to an in-world broadcast; **a close-up of a drawing hand** in a classroom, then cut to the world it draws.
- Endings: **a freeze-frame** on a laugh with a "to be continued" card; **the tape runs out** into blue screen; **a slow pan up to a starry sky** from a quiet rooftop, no dialogue.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: scifi-toon -->

# Sci-Fi Sitcom Toon — Style Prompt

> Adult-animation sci-fi sitcom: thick boiling outlines, flat colour, a duo whose reactions don't match, a glowing portal, and one palette per world.
> References (grammar only): adult-swim-era sci-fi sitcom cartoons (dialogue-driven comedy, reaction close-ups, boiling line, sci-fi hardware as household junk). Borrow the *grammar*, never the characters.

## 1. Essence, and what it is not

Hand-drawn-looking 2D TV animation for adults: **uniform thick dark outlines that boil**, **flat fills with hard-edged shadow shapes (no gradients)**, **big white eyes with tiny pupils**, **elastic mouths**, grotesque-but-cute creatures, and sci-fi hardware treated like household junk. The comedy is **dialogue-driven**: improvised-feeling talk, interruptions, awkward pauses, reaction shots, escalation, and a last-second reversal. The genre's engine is **a tiny, mundane goal pursued with absurdly large sci-fi means**: whoever could solve anything uses it for something petty, and someone else pays the emotional price.

Not a kids' cartoon (dry humour, long pauses), not anime (no sparkly eyes), not a vector explainer (lines boil).

**Copyright red lines (non-negotiable):**
- Never reproduce any existing show's characters, silhouettes or colour combos (e.g. a spiky-blue-haired old man in a lab coat + a kid in a yellow shirt), names, catchphrases, burp gags, logos, or the look of any existing portal gun.
- Invent your own cast, props and portal device. Never write the source show's name in the film or docs; one line "inspired by adult-swim-era sci-fi sitcom cartoons" is enough.

## 2. Materials & rendering

- **Line**: near-black (a slightly purple black reads best), ~7 px for characters and props, 4–6 px for background detail, round joins. **Line width is constant in screen space**: close-ups are "redrawn" at the same weight, never scaled up (transform points to screen, then stroke with an identity transform).
- **Line boil**: resample every outline in screen space (~7 px steps) and displace along the normal with low-frequency noise, amplitude ~1.7 px; cycle **3 boil drawings at 12 fps**. Everything boils, including held poses and backgrounds: a still frame is never dead.
- **Fill**: flat colours only. Shadows are hard-edged darker shapes clipped inside the fill (one per form, away from the light). Glows are 1–2 flat translucent rings, not gradients. Skies are **flat colour bands**.
- **Faces**: big white eyes (touching in 3/4 view), 4–5 px pupils, heavy lids for deadpan, eye bags. Parametric mouths (open, width, curl, skew) with interior, teeth, tongue. Brows carry the emotion.
- **Cast design**: silhouettes must read in solid black. Give each lead one absurd costume idea. Avoid white lab coat + spiky hair.
- **Creatures**: every world may get one creature that is disgusting *and* adorable; keep it non-verbal (sound effects) so the film stays a dialogue between the leads. Check that anything behind furniture still shows face and upper body.
- **The portal** (or whatever device moves between worlds): the only thing that glows. A lumpy rim with a thick outline, rotating spiral arms, a pale core, orbiting sparks, drips, a flat translucent wash over the scene while it's open. Open with a gentle overshoot (~12 %, back-ease ~0.3 s); a springy overshoot covers the actors.
- **Screen graphics**: a retro-terminal tag (VT323) typed in, coloured per world.

## 3. Colour logic

- **One palette per world**, 3–5 colours, maximally different from the previous world in hue *and* value, so the audience reads "we jumped" from colour alone.
- Line colour and eye white never change between worlds; everything else may.
- Glow colour belongs to the travel device only: nothing else in any world may use it.
- A deliberately bland palette (beige, brown) is itself a joke: use it for the world that is "suspiciously normal".
- Examples of a sequence of worlds: sage lab → magenta and lime jelly → orange and teal; or grey office → ultraviolet and gold → mint and coral → beige. Our demo's values are in DEMO.md.

## 4. Type & subtitles

- **Subtitles**: bottom centre, a rounded heavy sans (Baloo 2 ExtraBold ~50 px), white with a ~11 px black outline, so they look like the cartoon's own captions, with a small **speaker pill** in the character's colour (boiling outline) on the left. Lines over ~1300 px wrap to two lines. Overlapping lines stack; the older one dims to ~70 %.
- **Timing**: hold ≥ max(1.8 s, speech + 0.6 s) for narration; for rapid dialogue, `max(audio + 0.35 s, 0.9 s + chars / 17)`. Clip at world changes and **before a silent beat**, so the silence plays on a clean screen.
- **Title**: chunky display lettering popped in on 12 fps steps on a musical hit. Choose a period look that is not the source genre's logo: **avoid acid green, slime drips and wobbly bubble lettering** together, which reads as a specific show.
- Keep faces out of the subtitle band (bottom ~170 px) and the world tag clear of faces.

## 5. Motion quality

- **Characters on twos (12 fps)**: poses, mouths, blinks, walk cycles and boil step at 12 fps. **Camera moves, portal swirl, flying props and wipes on ones (24 fps)**.
- **Acting over moving**: held poses with small changes (eye twitch, pupils sliding, a gulp, sweat drops). Idle life: breathing (±1 % squash), a nod driven by speech loudness.
- **Anticipation → action** before every gesture.
- **Squash & stretch** on landings (decaying cosine squash ~22 %), stretch while flying out of a portal; "sucked in" = scale toward the portal centre while stretching.
- **Lip-sync from audio**: per line, RMS (open) and spectral centroid (wide vs round) at 24 Hz, sampled at the 12 fps drawing time. Exaggerate for screams (mouth ×1.5–1.9).
- **Nervous jitter**: a 12 fps random offset of 3–6 px plus trembling pupils; amplitude grows with panic.
- What never moves in a cold pause: everything but the boil.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.


<!-- END STYLE PAGE -->
