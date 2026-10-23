# Complete style specifications 22


<!-- STYLE: cel-anime-80s -->

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

| Move | What it expresses | Can serve |
|---|---|---|
| Medium two-shot | the relationship; who reacts how | dialogue; a standoff; a deal |
| Hard cut to a close-up | an interruption, a face breaking | the cut-off line; the realisation; a lie |
| Insert extreme close-up of an object | the absurd detail | a reveal; the problem itself; the wrong result |
| Reaction close-up | the laugh lives on the face | after every absurd image |
| Tight close-up + short shake on one word | panic | the key word; an alarm; a scream |
| Rush zoom into the portal → swirl wipe | leaving a world | any jump between places, times or versions |
| Same framing repeated across worlds | only the world changes | a montage; a comparison; a list |
| Very slow push-in on a still two-shot | a cold silence | the pause after a reversal; a confession |
| Wide with the device and both leads in frame | the whole situation at once | a callback; a trap; a fresh start |
| Over-the-shoulder onto a screen | reading bad news | a message; a readout |
| Whip pan between two faces | overlapping argument | a fight; a bet; a double take |

Rule: every absurd image is followed by a **reaction close-up**. Transitions go through the travel device (swirl wipes) or hard cuts; no dissolves.

## 7. Sound palette

- **Synthesized score, no samples needed.** A **theremin**-like lead (sine + a little 2nd/3rd harmonic, legato portamento ~70 ms, vibrato fading in ~150 ms after each onset, spring reverb) over analog bass, a square-wave arpeggio and a retro drum machine. Minor modes and chromatic lines suit the main theme.
- **Genre cues per world** (options): surf guitar; polka accordion; toy-piano lullaby; elevator bossa (Karplus–Strong nylon guitar); brushed swing with vibes; tuba + slide whistle; warm Rhodes + a vocal "aah"; tremolo strings for panic.
- **Techniques (options)**: a cue's first beat is the cut; a tempo that snaps cuts to a grid; rule of three becoming machine-gun (same stinger, shorter each time).
- **Silence is the punchline**: hard-cut the music, reverb tails included, on a reveal and for a cold pause. Leave only room tone (fluorescent hum, a clock tick, a fridge).
- **Foley (synthesized)**: portal open (sub boom + down-swept noise + rising swirl), hum, close "fwump", swirl whoosh per wipe, pop/boing, wet glorp/squish, slurp, chomp, blink "blip", click-beep, kazoo sting, squeaky toy.
- **Voices**: a two-hander with contrasting voices: low, flat and slow for the deadpan lead (light saturation + a ~180 Hz bump for gravel); higher and faster for the nervous one (presence boost). A tiny creature may say one or two words, pitched up. Compress, RMS-match, add short early reflections so voices sit in the room. Duck music ~−7 dB under dialogue. Master −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Parallel worlds.** Each jump = new palette, new cue, new creature. *Fits content like:* versions of a product; careers you could have had; the same city in five eras.
- **Duo contrast.** Deadpan vs panic: the joke is in the difference between reactions. *Fits content like:* a veteran and a new hire; a parent and a teenager; an AI and its user.
- **Rule of three → machine-gun.** Two slow wrong answers, then one-second worlds cut on the beat with the same rejection word. *Fits content like:* failed prototypes; bad date ideas; tax forms.
- **The suspiciously normal world.** The pattern breaks; the calm is the joke. *Fits content like:* the one boring answer that works; a quiet office after chaos; the real customer.
- **Dead-air reversal.** A long silence after the twist, then one line revealing a character's values. *Fits content like:* a price reveal; a fine print clause; a gift that wasn't wanted.
- **Hardware as junk.** World-bending tech used for a petty chore. *Fits content like:* a quantum computer used for a grocery list; a rocket to deliver a sandwich; a time machine to fix a typo.
- **Callback button.** The last line repeats the first so the story loops. *Fits content like:* a catchphrase of a brand; a morning routine; a running complaint.

## 9. Pitfalls of the medium

- TTS reads hyphen stutters as words: write syllables ("buh, buh-broken"); respell words it mangles; pick names that survive a low voice.
- Whisper mis-hears very short clips unless padded with ~0.6 s of silence.
- A real interruption: generate the interrupted line *longer* than needed and truncate the audio where the other voice cuts in.
- A springy overshoot swallows the actors: gentle back-ease.
- Food and liquids need cues (surface detail, drips, steam) or they read as other objects.
- Square-wave synth cymbals alias into harsh 8–20 kHz fizz: band-passed noise plus a little FM.
- A sustained bass below ~40 Hz is rumble on laptop speakers: end an octave higher.
- A cut music cue without its reverb tail cut is not dead silence.
- `ffmpeg fps=1` contact sheets are offset up to 0.5 s: don't misdiagnose a shot boundary.

## 10. Engine

In `demo/`: `toon.js` (vector engine: matrix stack, screen-space boil, constant line width, flat shading), `chars.js` (parametric eyes, mouths, hands, noodle limbs), `worlds.js` (one function per world, creatures, the portal), `voice.py` (per-character processing + lip-sync envelopes), `asr.py` (padded whisper check), `music/score.py` (synthesized score from a cue list), `levels.py` (stem meters), `sheet.sh` / `strip.sh` (contact sheets, consecutive-frame strips). New shapes: build them with `toon.js` in world space; the stroke goes through the screen-space boil at constant weight.

## 11. Variation space

You decide the premise, the cast, the worlds, the jokes, the opening, the ending, the camera path, the pacing and the palettes. All far from our demo:

- Structures: **one world, many clocks** (the duo stays home and a device skips them through times of day, each time worse); **the job interview** (a panel interviews candidates from other worlds, each a different genre cue); **the tech-support call** (split screen between two worlds, one voice guiding the other through a disaster).
- Openings: **mid-disaster** (the portal is already open and something is coming through); **the instruction manual** (a terminal readout explains the device before we see anyone); **the wrong world** (we start in the absurd world and only later see home).
- Endings: **stuck elsewhere** (the device breaks and they settle in, happily); **the audience** (a creature from one world watches the whole film on a screen and rates it); **the cost** (a quiet final shot of what the errand cost someone, no joke).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: midcentury-toon -->

# Mid-century Cartoon — Style Prompt

> 1950s flat colour and limited animation for "follow along" films: colour printed a few pixels off its broken ink line, bodies that hold still while hands do the work, abstract colour-block rooms, a calm classroom narrator, and a cool-jazz combo.
> References (grammar only): UPA's early-1950s shorts (*Gerald McBoing-Boing*, *Rooty Toot Toot*): colour and line on separate cels, geometric people, colour-plane backgrounds, limited animation. 1950s classroom films (Coronet, Encyclopaedia Britannica): direct address, one sentence per picture, numbered cards. Charley Harper and Mary Blair: soft atomic-age complements, geometric figures. 1950s appliance manuals: numbered medallions, curved arrows, round call-outs, sunbursts. Copy none of their characters, drawings, lettering or music, and never name them in a film.

A **scene style**: it performs a real use (a set-up guide, a how-to, a recipe card, a safety card) rather than telling a story. The viewer should come away able to do the thing. See §11 for the jobs.

## 1. Essence, and what it is not

Flat, printed-looking colour with a thin, breathing ink line that never quite closes. **Every fill is a separate "cel" printed a few px off its line**, re-rolled on twos, so the picture shimmers like hand-registered paint while the camera glides. Light dry-brush tooth, paper grain, warm vignette.

People and things are geometric: egg or bean heads with the nose part of the face outline, simple garments in two or three flat colours, four-finger cartoon gloves. **A presenter's body is a held drawing: only arms, hands, eyes and mouth animate.** Rooms are not drawn: a scene is one colour plane, a floor band, a horizon line with gaps, and one or two props.

Not the 1930s rubber-hose cartoon (no black-and-white, no bouncing world, no hot jazz). Not a whiteboard explainer: it shows *how to do*, not *why*. The pictures are printed, not written on.

## 2. Materials & rendering

- **Off-register cels**: fill drawn with a small offset (a few px, down-right) from its line; the offset jitters ±1–2 px on twos. Keep it on everything, text included; switch it off only for a crisp diagram.
- **Line**: 3–5 px ink ribbons with ±40 % width breathing and 12–25 % breaks. Characters ~4 px, props 3–4.5 px, walls in plans thicker and broken. Hands: one outline around the union of palm and fingers, thin finger separations.
- **Shading**: one flat darker plane clipped inside a shape, never a gradient. Drop shadows are a copy of the shape offset down-right in a paper shade at ~50 %.
- **Ornaments**: 4-point atomic sparkles, 8–18-point starbursts, sunburst rays (~30 wedges, semi-transparent), boomerang and kidney shapes, polka dots.
- **Grain**: light; print, not film.

## 3. Colour logic

- **A warm paper ground, a warm near-black ink, soft atomic-age complements.** Nothing pure or neon.
- **One ground colour per scene**: a lighter tint for walls, a darker shade for floors. Never place the product on its own colour, never the presenter on their own accent.
- **The product keeps one colour through the whole film**; the accent (a presenter's garment, stars, bullets) is a different hue. Step grounds rotate through the rest.
- Examples: *coral / mustard / turquoise* on cream; *tomato / olive / powder blue* on oatmeal; *plum / lime / sand* on off-white.

## 4. Type & subtitles

- Roles: a 1950s script for a kicker (Oleo Script Bold); a slab serif (Alfa Slab One) for titles, numerals and headers, in ink over an offset colour plate; a geometric sans (Jost 500/600) for body, details, labels and captions.
- **Caption card**: a paper-coloured rounded slab with a thin ink border (its colour cel offset too), small turning stars at the ends, ~40 px sans, bottom-centre. Fades in quickly with a small rise. Hold ≥ max(1.8 s, speech + 0.6 s, chars/12 + 1 s).
- **Step header**: an ink disc with a paper numeral, a small letter-spaced "STEP n OF N", and the step title with a cream plate; it slides in on twos.
- **Detail tags**: a paper card with a star bullet, popping on the action beat next to the call-out. Data lands on the picture, never as a slide.

## 5. Motion quality

- **On twos:** poses, hand shapes and the cel jitter change at 12 fps. The camera, iris wipes, arrows, plan routes and rays move at 24 fps.
- **Held body, moving hands:** switch poses with a single in-between. A hand action has anticipation (pull back or lift), a fast action (0.15–0.25 s, eased out), a follow-through (recoil, settle, lift away) and lands exactly on a beat.
- **Pop-ins:** medallions, tags, labels and titles scale in with a back-ease (~0.25 s, strong overshoot).
- **Reaching the floor**: a kneel pose with 2-bone IK keeps the hands on the object while it moves; never stretch standing arms.
- **Lettering**: a script writes on left→right with a clip; headers slide in on twos.

## 6. Camera grammar

The camera is "the stand": never handheld. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow push (a few %) | Collecting the eye | a product on its stage; a result settling |
| Iris through a medallion | The number *is* the door | a change of step; a change of rule |
| Round call-out with a leader line | Context and detail at once | a hand action; a screen; a small part |
| Tilt with a pointing finger | The finger leads the frame | the one action that matters most |
| Push into a device, pan along signal rings | Person → interface → device | pairing; connecting |
| Iris from a round object into a top view | Circle to circle, function to plan | a button starting a job; a lid opening; a dial |
| Pull-back with counter-rotation from a detail to a plan | One lane becomes a pattern | a route, a schedule, a garden, a floor plan |
| Colour-block wipe (side, bottom-up) | Turning the manual's page | a tip; a summary; a new card |
| Split frame in two colour blocks | Right vs wrong, before vs after | a safety rule; an upgrade |
| Dead still ≥ 3 s | "This is the frame to screenshot" | a summary; a CTA; a QR code |
| Iris-out onto one object | The last circle | a closing on the product, the logo, the result |

Key subjects ≥ 1/3 frame height and clear of the caption band. Transitions are circles, colour-block wipes and cuts on a beat; no dissolves.

## 7. Sound palette

Three layers, always:
- **Music**: an original West-Coast cool-jazz combo: flute or muted trumpet, vibraphone (chords, arpeggios, glissandi, tremolo), pizzicato walking bass, brushes (sticks on the ride for energy), celesta, bongos or finger snaps. Not ragtime, not a spy big band, not piano and strings. Options: give **every step its own vibraphone chord** and bring them back one per summary item; halve or double the feel instead of changing tempo; move up a step for a payoff.
- **Silence as a tool**: cut *everything*, ambience included, for the beat before the most important action, so the first sound after it (the click, the pour) is the step. Room tone alone before a summary.
- **Foley by material**: cardboard creaks and thumps, appliance plastic knocks and clicks, floor scrapes, glass and ceramic clinks, pours, damped rubber stamps for medallions, paper swishes for wipes, slide whistles for dimension arrows, rising pips for "connected", pen scratches for a route, an iris "shhk".
- **Ambience**: warm room tone (low-passed brown noise, very quiet), a mantel-clock tick on the grid; a device's motor hum can take over when it works.
- **Mix**: J/L cuts (lines start before their iris, tails ring on); narration compressed on top, music ducks ~8 dB, foley unducked, −14 LUFS.
- **Voice**: calm classroom authority, one clause per line ("Step one. Set it against a wall."). Whisper-check every line; accents can blur key nouns.

## 8. Native moves

Each move serves information. A menu: use the ones your film needs.

- **Off-register colour** makes an info card hand-made and warm. *Fits content like:* museum rules; a bank app screen; hotel check-in.
- **Limited animation points the eye**: the still body leaves the hand as the only mover, and the hand *is* the step (one hand action per step, on a beat). *Fits content like:* threading a sewing machine; changing a bike tyre; setting a thermostat.
- **The round call-out** is the close-up; the step's data lands inside or on it on the action beat. *Fits content like:* a dosage on a measuring cup; a torque value on a bolt; a PIN on a keypad.
- **The numbered medallion** marks hierarchy and opens the next step; it stamps onto the outgoing subject and the camera goes through it. *Fits content like:* a pool's five rules; a checklist for a flight; stages of a recycling sort.
- **The payoff turns function into ornament**: a real process (a route, a watering schedule, a seating plan) draws itself region by region and, seen whole, reads as an atomic-age textile. *Fits content like:* a sprinkler's coverage; a delivery round; a week of medication.

## 9. Pitfalls of the medium

- A route that ignores obstacles → follow the product's real rules; flow streamlines bend around obstacles and never cross. Lay it one region per beat, not all at once.
- A separate nose wedge looks glued on → one open spline from the bridge round the skull, closed at the nose tip.
- Thin arms read as sticks from the neck → shoulders at the torso corners, sleeves as a thick ink ribbon with a colour ribbon on top.
- Fat-blob fingers turn the hand into a cloud → stroke every part first, fill second (one union outline), slender fingers with separation lines.
- Zooming the world triples the ink → close-ups in call-out circles drawn at native scale.
- Detail text without reading time → move the data into the detail, the context into the title and the voice; chars/12 + 1 s.
- A transition drawing the next scene before its start → clamp local time to just past the start.

## 10. Engine

`demo/engine/toon.js` (the style: `setClock`, `shape` for any shape in the style, `ink` ribbons, `plane`, two-plate `text`, `fit`, the manual `arrow`, ornaments, the global register `REG`), `demo/engine/chars.js` (presenter, glove hands, the demo product), `demo/engine/icons.js` (18 icons). `demo/film.js` has liftable helpers: `callout()`, `medallionAt()`, `tag()`, `stepHeader()`, the flow-route generator `laneY()` + `buildPath()`, and the transition block (medallion iris, button iris, colour-block wipe, iris-out). API table and a minimal example: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the thing, the presenter (or none), which steps and in what order, the opening, the ending, the camera path, the colours, the pacing and the music. Use cases are **grammar for the order and duration of information**; build your own timeline from the user's facts.

| Use case | Information order | Hold per layer | Length |
|---|---|---|---|
| **Product set-up guide** | product name → title → step title → step detail on the action beat → payoff → tip → CTA | title ≥ 4 s; step title the whole step; detail ≥ chars/12 + 1 s; summary ≥ 3 s clean | 30–40 s, 2–5 steps |
| **Safety / rules card** | rule number → rule → one "why"; a held figure, a medallion, a gesture, a pictogram per rule | 3–4 s per rule | 20–40 s, 3–6 rules |
| **Recipe or ritual card** | step → quantity/time → result; side view, call-out on the hands, result as a top-view pattern | 3–5 s per step | 30–45 s |
| **Onboarding for an app or service** | screen action → setting value → confirmation stamp; the screen lives in the call-out | 3–4 s per action | 20–30 s |
| **Store or event notice** | headline → time/place → CTA; colour-block wipes between cards | ≥ 3 s per card | 15–25 s |

All far from our demo:

- Structures: **a rules card with no product**, one held figure and a medallion per rule; **a recipe on a tabletop**, seen from the side, ending in a top view; **a do / don't split**, each rule shown twice in two colour blocks.
- Openings: **the finished result first**, then "here's how"; **the problem in one gesture** (a hand fumbling a cable); **a numbered list** stamped on, then opened item by item.
- Endings: **a checklist ticking itself**; **the hands at rest** beside the finished thing; **a QR code** held dead still in a starburst.

Swapping `demo/content.json` and rebuilding is a technical check that the engine re-flows, not a way to make a film.

---

How our demo was made (story, shots, score, end card, build, content fields): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: pixel-rpg -->

# 16-bit Pixel RPG — Style Prompt


<!-- END STYLE PAGE -->
