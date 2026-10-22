# Complete style specifications 35


<!-- STYLE: hd-2d -->

- **Shadows jump when a light is lit.** A practical turns on next to sprites and their shadows swing across the floor. *Fits content like:* a shop opening at dawn; a server rack powering up; a teacher switching on a projector.
- **The carried light as a meter.** One small light a character carries is key light and gauge at once: its brightness rises and falls with whatever the story is measuring. *Fits content like:* a phone battery on a long trip; a patient's heart monitor; a candle vigil.
- **Tilt-shift preciousness.** An extra-wide with the band on one tiny subject. *Fits content like:* a single delivery van in a city; a newborn's room in a whole hospital; one stall in a night market.
- **Lights popping on one by one.** Windows, lamps or boats light up at a steady cadence across the map. *Fits content like:* users joining a network; a village getting electricity; a festival beginning.
- **RPG grammar.** Chapter card, named character in a dialogue box, biomes, a landmark, a title card. *Fits content like:* onboarding a new employee; a history in eras; a recipe in stages.
- **Weather passes over the diorama.** Rain, snow or lightning sweeps the tabletop with the flash curve. *Fits content like:* a market crash; a harvest threatened; a hard week at work.

## 9. Pitfalls of the medium

- **Checkerboard everywhere** → the dither band is too wide (≈ .22 on sprites, ≈ .45 on textures).
- **A light burns out the sprite that holds it** → move the light ~0.45 m toward the camera; cap sprite lighting in the shader (`min(outgoingLight, diffuse * 1.35 + emissive)`).
- **Lights behind a billboard don't light it** (front normal only) → always the front fill.
- **Cylinder beams facing the camera give NaN** that bloom spreads into black blocks → billboard beam cards that fade toward the lens, glow sprite takes over.
- **Dark scenes unreadable** → lift environment mid-tones ~×2–2.5 outside the one beat that must go dark.
- **Distant glows hidden by fog** → `depthTest = false`, higher `renderOrder`.
- **Tilt-shift with no character to track** → fixed band height per shot. **Tilt as a separate blur pass** breaks occlusion → fold it into the DOF's signed CoC.
- **Node render scripts may not exit** after `done` (server keep-alive) → `process.exit(0)`; the file is complete once `done` prints.

## 10. Engine

In `demo/`: `px.js` (pixel canvas, Bayer ramps, surfaces, lit billboards, glow), `kit.js` (world UVs, materials, houses, props, pixel fire), `fx.js` (sky, pixel sea, particles, rain, beam cards, `flick`), `chars.js` (pose-table pixel characters, `makeChar`), `post_ts.js` (`makePost`: DOF + tilt-shift + bloom + grade), `ui.js` (chapter card, dialogue box, subtitles, title), `main.js` (page contract, `?tilt=1`). Module table, parameters and a minimal new set (a lantern-lit alley): [DEMO.md § Engine reference](DEMO.md#engine-reference).

## 11. Variation space

You decide the places, the characters, the light the story turns on, the chapters, the opening, the ending, the camera path, the key temperature and the music. All far from our demo:

- Structures: **a day-cycle map** (one set, dawn to night, each hour lit by different practicals as the town's routine unfolds); **a party of three** (three short chapters, each character's biome and light, converging in one room); **a menu of places** (a top-down overworld; the camera dives into one location per topic point and pulls back to the map between).
- Openings: **in the middle of the room** (a dialogue box already typing over a close 3/4 shot); **overhead map** (straight top-down, the band as a strip, then tilt down into the 3/4 view); **daylight** (a bright noon wide with no practicals at all, so the first lamp later is an event).
- Endings: **a save point** (the hero rests at a small glowing object, the UI shows a save line, fade); **the band narrows** (the sharp strip thins onto one sprite until everything else is blur); **the party leaves frame** (a locked wide holds after the characters walk out; only ambience and flicker remain).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: microgame -->

# Microgame Frenzy — Style Prompt

> A rapid-fire party-game film: one command word, a few seconds, one action. Every microgame is drawn in a completely different art style, and the film keeps getting faster.
> Genre reference (grammar only): the WarioWare series. Never use its name, characters, UI, microgames or music.

The format suits short films; once the frenzy stops building, end it.

## 1. Essence, and what it is not

- **A microgame = a shouted command word + 2.5–4 s + one action + one result** (success, or a funny failure).
- **Each microgame uses a different visual medium** (crayon, ink wash, terminal, risograph, pixel, blueprint, Swiss type, clay, cut paper, woodcut…). The jolt of each switch is both the joke and the beat.
- **One fixed home look** holds the film together: a show stage with a host, a lives counter and a stage number, which the film returns to between games.
- **It keeps accelerating**: every few games tempo, game length, dwell, command hold and animation frame rate step up together.
- **The hero survives every medium** by keeping two or three silhouette marks.

Not Game Show Flat (one art style, rounds of bars, call-and-response), not a style sampler reel (every game has stakes; lives connect them), not a montage (each game has a rule grasped in under a second).

## 2. Materials & rendering

- **Home stage**: flat toon, thick near-black outline (~7 px), flat fills, **one hard-edged shadow** (fill in the shade colour, clip to the shape, refill shifted up-left). Fixed furniture: a frame-within-the-frame where games play (a TV, an arcade cabinet, a phone, a window), the lives board, a stage badge, a trigger prop (button, lever, bell).
- **Each medium is a simplified re-drawing, 100–200 lines of code**, built around one channel trick that makes it read at a glance:
  - drawn media store **pressure or wetness in a channel** (crayon: alpha = pressure against paper tooth; ink: wet and dry ink channels);
  - print media store **plate densities** (riso: a channel per plate, additive overprint, halftone, misregistration);
  - screen media are **low-res buffers** scaled up (pixel: indexed buffer, auto outline, dither; terminal: hand-authored glyph art, phosphor shader);
  - technical media are **line systems** (blueprint: line weights and dimensions; Swiss: a strict grid, one sans, one signal colour).
- **Hero translation**: the hero is redrawn from scratch in each medium, but the same marks always survive (e.g. a hat shape, one coloured dot, a number on the chest). Make a model sheet of the hero in every medium before animating.
- **Mixed-media frames**: alpha-coverage media over a base, paper media multiplied, screen media flat and clipped to a panel. WebGL2 material shaders turn the channel buffers into each look.

## 3. Colour logic

- **The home stage owns a saturated party palette**: a deep ground behind a rotating sunburst, two or three loud accents, plus a fixed success colour and a fixed fail colour used by stamps and the lives board only.
- **Each medium brings its own palette** from its tradition (wax colours, one-ink-plus-vermilion, amber phosphor, three riso plates, a limited pixel palette, white-on-blue, black-white-red). Never tint a medium with the home palette.
- **One accent follows the hero across media** where the medium allows (a single vermilion dot in ink, an inverse glyph in a terminal, a signal-red circle in Swiss type): it is how the eye finds the hero after a switch.
- Example home palettes: violet `#2a0f5c` with magenta `#ff2e88`, gold `#ffc928`, cyan `#1fd1d1`; teal ground with coral and lemon; black stage with hot orange and electric blue.

## 4. Type & subtitles

- **The command word is the subtitle**: a heavy display face (e.g. Titan One), white with a thick ink outline, a coloured drop and a burst behind it, skewed a few degrees. It slams in over ~3 frames (overshoot → settle), holds, then **shrinks into a corner tag before the first action**, so the result is never covered. One-off banners fly out instead of tagging, so tags never pile up.
- **Other lines**: a rounded card in the home palette with the home outline and hard shadow, a friendly rounded face (e.g. Lilita One ~50 px), a small speaker icon; placed above the timer in games. Hold ≥ max(1.8 s, speech + 0.6 s), never under a big banner.
- Inside a game, any text (replay captions, labels) uses **that medium's own typography**.
- The command word appears in the .srt only, never burned twice.

## 5. Motion quality

- **The frame rate is part of the ladder**: characters step on twos or at 8 fps early, faster later, on ones at the climax. Camera moves, transitions and the timer spark always run on ones.
- **Five things accelerate together** at each speed-up: tempo, game length, stage dwell, command hold, character frame rate.
- **The timer is visible and on the beat**: e.g. a fuse with one knot per beat, the spark passing each knot exactly on it. It freezes in a replay.
- **Unified transition through the frame-within-the-frame**: push into the screen to start a game (~0.25 s), shrink the game back into it to return (~0.33 s) with a ✓ / ✗ stamp. No fades, no blank frames.
- **Failure is performed**: the action overshoots, splats, bonks or rolls off; the medium's own physics makes the joke.
- **Instant replay** for a failure that must be understood: freeze, half speed, push-in, letterbox, a caption in the medium's type.
- The home host has a tick on every beat; stopping it dead is the strongest emotional tool.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Start inside a game, command already slamming | the rules explain themselves | throwing the viewer in |
| Pull back out of the game screen | scale: this was one screen on a show | the first return to the stage |
| Locked frontal home frame | the constant; only the scoreboard changes | stage beats; the host's reaction |
| Slot reels (the stage splits into spinning strips of earlier frames, stopping one per beat) | acceleration, a summary | a speed-up; a change of round |
| Extreme insert on the trigger prop | the start, felt | a game starting on the downbeat |
| Lights cut to one top spot, frame unchanged | stakes; the last chance | the last life; a decision |
| Tile flip (last frames of past games flip into pieces of a new frame) | the past becomes the material of the present | a boss or finale; a recap |
| Push into a detail, hold | the viewer notices before the hero does | a clue; a silence |
| Snap back to wide on one beat | release | a solution blooming; a save |
| Split screen, two media side by side | comparison, rivalry | two players; before/after; two approaches |

Framing: the game screen is a fixed fraction of the frame (around 40 % of the width); in a mixed-media frame keep **one focal chain** (A leads to B leads to C) and push info panels into a corner.

## 7. Sound palette

- **Music first**: a tempo grid and a cue table before any animation; every picture hit lands on a listed cue.
- **A constant groove + one colour instrument per medium.** The groove (kit with ghost notes, slap or synth bass, brass stabs, keys) runs throughout; each medium adds its own timbre: toy piano for crayon, shakuhachi or guqin for ink, square beeps for terminals, vibes for print, pulse arpeggios for pixel, a typewriter for drafting, claves for Swiss, kalimba for clay, koto for woodcut.
- **Foley follows the medium**: wax squeaks, wet splats, teletype relays, paper crunch, bit-crushed noise, ratchets and stamps, hollow bonks. Home stage: a spring trigger click, glass crack for a lost life, card flips, a reel whirr, sparse claps.
- **Acceleration options** (use what fits): a rising brass run into each speed-up; the key rising a step per round; halving note values instead of changing tempo; dropping the groove to a heartbeat on the last life.
- **Real silences**: at least one before the biggest hit (a heartbeat or one pitched note may remain). The loudest moment comes right after the longest silence.
- **Voices**: a host who shouts every command a hair *after* the stab so brass doesn't mask it; a hero with very few words (reactions work best). Duck music ~11 dB and foley ~6 dB under voice. −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Style switch per game.** Each task is drawn in the medium that suits it. *Fits content like:* the steps of baking bread (flour in crayon, oven dial in blueprint, crust in woodcut); a day of a nurse; a heist's roles.
- **Command word.** One verb is script, subtitle and downbeat. *Fits content like:* SCAN! at a checkout; BREATHE! in a yoga class; SIGN! at a contract signing.
- **Lives as UI.** The counter carries emotion without narration; 3 → 2 → 1 (blinking) builds tension alone. *Fits content like:* a phone battery; retries on a driving test; chances left on a quiz.
- **SPEED UP.** Everything steps up together. *Fits content like:* rush hour; the last week before a deadline; a kitchen during dinner service.
- **Failure becomes the solution.** The material of an earlier failure returns in the final game as the answer. *Fits content like:* a spilled coffee that later stains the winning map; a bug that becomes a feature; a missed train that leads to the right meeting.
- **Boss mixes the rules.** The final game is built from pieces of earlier media. *Fits content like:* a final exam; launch day; a festival's closing night.
- **Instant replay.** The joke explained in slow motion. *Fits content like:* a goal-line decision; a typo that shipped; a cat's leap that missed.

## 9. Pitfalls of the medium

- **A luminance-ramp ASCII figure is mush** → hand-authored glyph art with structural glyphs, an inverse glyph for the accent.
- **Ink shapes read as smoke** unless their silhouette is designed (a short round blot phase, then a clear structure with seams and light edges).
- **A failure at high tempo goes unread** → make the action overshoot and hit something, or give it an instant replay.
- **Alpha-coverage media show the background through gaps** → a full-pressure base where it must be solid.
- **Drawing helpers with a global context** draw on the wrong canvas when scenes render into offscreen buffers (game screen, reels, tiles) → set and restore the context.
- **Command tags pile up** → secondary commands fly out.
- **A 100 % white flash** reads as a blank frame → cap at ~60 %.
- **TTS single-word commands** gain a vowel tail ("Pump!" → "Pompey") → generate a two-word phrase and cut after the first word using ASR timestamps; verify each clip, since ASR mishears 0.2 s words in a dense mix.

## 10. Engine

`demo/timeline.js` (tempo grid and segments, the single source of truth), `demo/toon.js` + `demo/stage.js` + `demo/hud.js` (home look, stage, timer, command word, stamps, lives, subtitle cards; call `setCtx` when drawing offscreen), `demo/chars.js` (host and hero rigs), `demo/glpass.js` (WebGL2 material shaders: riso, crayon, CRT, ink, blueprint paper), one `demo/g_<medium>.js` per medium (`sceneX(g, lt)` + the hero translation), `demo/film.js` (transitions through the TV, slot reels, tiles, events). Module map and build: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the tasks, which medium draws each, the home stage and its frame-within-the-frame, the host and hero, the number of rounds, where failures fall, the finale, the opening and the ending. The command → action → result unit, the medium switch and the acceleration stay.

All far from our demo:

- Structures: **two players, alternating** (each game is played by one of two rivals; the lives board is a tug-of-war); **one day, hour by hour** (each game is an hour, the speed-ups are the morning rush and the evening rush, the finale is midnight); **a relay** (the result of each game is the object handed into the next one, so the chain is the story).
- Openings: **the home stage asleep** (lights off, the host wakes on the first beat); **a game-over screen** we rewind from; **the lives board alone**, a counter clicking down before we know what it counts.
- Endings: **a high-score table** where the hero types their name letter by letter in each medium; **the credits as one more microgame** (CATCH THE NAMES!); **the home stage packs away** into the frame-within-the-frame and the screen switches off.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: game-show -->

# Game Show Flat — Style Prompt

> A rhythm-game variety show in flat vector: toy-like mascots with thick ink outlines on candy-coloured stripes and sunbursts, every hit landing on a fixed tempo grid, call-and-response patterns, and a judgement word when each round is won.
> References (grammar only): rhythm-action party games in the Rhythm Heaven mould (cue → answer, round cards, judgement words), Japanese variety-show telops (thick outlined captions, stripe and sunburst sets), WarioWare-style stage cards. Never use their names, characters, UI, levels or music.

The length follows the number of rounds: each round is a title card plus its bars of play. Narration is optional: the style can carry a film on short shouts and telops alone.

## 1. Essence, and what it is not

- **Everything is on the grid.** One fixed, fast tempo. Every pop, drop, stamp, typed character and camera punch sits at a (bar, beat) and is also a sound event; the score is generated from the picture's own timeline, so they can't drift.
- **One drawing kit, many sets.** Flat fills, one heavy ink outline, round caps, hard offset shadows; each round gets a new saturated background colour and pattern.
- **Characters are toys.** One body construction for the whole cast, told apart by colour, a belly patch, one head accessory and a name tag. They hop on the beat, squash on hits, throw arms up on a shout.
- **A round = a repeatable verb + a win.** The topic is split into rounds; each round has one action that can repeat on a beat, and ends on a judgement the audience reads in one glance.

Not a microgame frenzy (no timer or one-verb command per 3 s game, no change of art style per round), not a mid-century cartoon (no textured painted backgrounds, no character acting), not a keynote (no slow reveals, no gradients).

## 2. Materials & rendering

- **Vector only**, SVG or canvas paths at 1920×1080: flat fills, one outline colour (near-black), 8 px outlines on characters and props, 5–7 px on small parts, round joins and caps.
- **No gradients, no blur, no texture, no soft shadow.** Depth is a **hard offset shadow**: the same shape in outline colour shifted ~10 px (stickers, banners) to ~14 px (cards), then the coloured shape on top.
- **Sets** = one saturated background + a same-hue pattern one step lighter: diagonal stripes (often scrolling slowly), offset polka dots (~20 % white), or a rotating sunburst. A darker floor band with an ink line on top grounds the characters.
- **Characters**: a rounded bean body, stubby arms with mitten hands, oval eyes with a catch-light, a mouth that swaps to an open one. Humans share the construction; older machines or eras read through a boxier silhouette.
- **UI kit**: round card, corner sticker banner, judgement word, burst (star + ring + speed lines), scoreboards.
- `render(t)` is a pure function of `t`: every element's state is recomputed from `t`, never carried over from the previous frame.

## 3. Colour logic


<!-- END STYLE PAGE -->
