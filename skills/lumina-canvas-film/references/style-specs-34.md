# Complete style specifications 34


<!-- STYLE: pixel-rpg -->

> A short film that looks, sounds and *behaves* like a mid-90s console role-playing game: 320×180 pixels, a limited indexed palette, text boxes that type, menus, save files, chip music with echo.
> References (grammar only): mid-90s console RPGs as a system of dialog boxes, menus, battles, overworlds and save points; the palette tricks of indexed hardware (palette swaps, fades by steps, cycling); the colour-depth history of consoles (4 shades → 8-bit → 16-bit). Never use existing game names, characters, UI frames, fonts, logos, melodies or sound effects. Learn the grammar, not the assets.

## 1. Essence, and what it is not

- **320×180 native pixels**, scaled ×6 nearest-neighbour to 1080p; everything, text included, lives in the framebuffer.
- **A limited, indexed palette**; gradients are **ordered dither**, never blends.
- **Sprites** around 20–34 px tall animating in a handful of frames; faces act in **portraits**.
- **Story told the way a game tells it**: dialog boxes with portraits, menus, status bars, battle messages, save files, item fanfares.
- It takes the game's systems seriously as a language for feeling.

Not HD-2D (no depth of field, bloom or real-time light), not CRT nostalgia (no scanlines, no grain), not a parody.

## 2. Materials & rendering

- **Indexed framebuffer** (`Uint8Array` of palette indices) presented through a **lookup table** (index → RGB), so a whole palette can change in one frame. Camera moves are **integer pixels**; each parallax layer rounds its own offset.
- **Master palette** of ~32 colours (a free palette such as ENDESGA-32), plus **protected duplicates** of a few indices that no palette effect touches.
- **Colour-depth tables** computed from the master palette: identity (16-bit), nearest of ~15 NES-like colours (8-bit; it needs a dark green and a dark brown), 4 fixed luminance thresholds (4-colour, drawn natively at 160×90 and doubled), a faded set (`lum^0.8` → ~7 blue-greys), and intermediate subsets for step-by-step collapse. Map by luminance, never by rank.
- **Light is index stepping**: `LIGHT[]` / `DARK[]` tables move each index one step along its ramp; glows are Bayer-thresholded rings. Firelight in a low-colour era uses a warm remap (greens → browns → rust), not generic brightening.
- **Dither**: 4×4 Bayer for gradients and glows; light shafts as a flat 50 % checker with a 25 % edge.
- **Sprites from a rig**: capsule limbs with 3-tone shading from an upper-left light, a per-part inner line in the material's darkest tone, a global 1-px ink outline, plus hand-placed ASCII heads. One rig gives every pose; lower eras drop the highlight tone. Give the hero a **silhouette mark** (a garment tail, a hat, a hairstyle).
- **Portraits** 32×32, 3/4 view, base face + eye/brow and mouth overlays; they carry facial acting (the sprite face has one eye pixel).
- **Props** can be flat-shaded 3D shapes quantised to a few protected indices (e.g. a rotating crystal at 8 frames per 90°).

## 3. Colour logic

- **Palette = feeling.** Colour depth, fades and swaps are story tools; change the whole palette by table, never by alpha.
- **Colour depth can stand for time**: older = fewer colours, lower resolution.
- **Protected indices**: a few colours exempt from every effect become the thread through the film and allow match cuts between eras. Use one or two; more and they stop meaning anything.
- **Warm hues survive reductions**: keep orange, pink and plum in reduced subsets, or the first step turns a scene solid red.
- Example uses of protected colours: a red kite across a childhood; a gold coin in a grey economy; the green of one plant in a faded city.

## 4. Type & subtitles

- **The dialog box is the subtitle**, drawn in the framebuffer at the bottom quarter: a layered rounded border (ink / white / silver), a dithered dark-blue fill, a 32×32 portrait on the left, an **original** variable-width pixel font (cap ~7 px) with a 1-px shadow. It types with the voice (~38–40 chars/s; slower in older eras), ▼ blinks when done.
- **Skins follow the era** (light box for 4-colour, black box with white frame for 8-bit, blue for 16-bit).
- Battle and system messages go in a thin top window. Every box stays ≥ max(1.8 s, speech + 0.6 s); the next box cuts the previous one. Export the `.srt` from the same subtitle array.
- Titles in the pixel font at 2×, 8-neighbour ink outline, row-by-row gradient, Bayer-dissolved in and out.

## 5. Motion quality

- Output 24 fps. Sprites step at **8 fps** (walk) to **12 fps** (flames, blinks); camera and parallax move on ones at integer pixels.
- **Game-native acting**: hop forward to act, cast pose, knockback recoil, kneel, KO blink (12 fps on/off) and vanish; breath = shoulders up 1 px.
- **UI motion**: windows slide in over ~0.3 s (ease-out, integer px); a hand cursor bobs 1 px at 4 fps and **stops when the character hesitates**.
- **Transitions**: thumbnail expand + mosaic, mosaic cross with a palette switch at the peak, the encounter swirl (polar twist + mosaic + Bayer dissolve to white), screen shake (3–2–1 px over 8 frames), palette step fades (4 levels). Never alpha fades.

## 6. Camera grammar

A vocabulary, not a route. Game cameras are simple and legible. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Side-scroll with parallax layers | journey; loneliness; progress | a commute; a quest; a timeline |
| Locked frame with UI on one third | a choice; a system speaking | a menu decision; a stats reveal |
| Battle side view (enemy / party / windows) | conflict as a system | an exam; a negotiation; an illness |
| Top-down overworld pan | the whole world; where things are | a city; a map of a company; a trip |
| Integer-pixel tilt up something tall | awe; scale | a tower; a door; a mountain |
| Hold while the palette changes | loss or change without motion | grief; a memory fading; nightfall |
| Back view at a threshold | resolve; the unknown ahead | a first day; a launch; a departure |
| Zoom by mosaic into a thumbnail | entering a memory or a file | a flashback; a save slot; a photo |

Framing: characters stay above the dialog box (floor line above its top edge); menus leave the action visible.

## 7. Sound palette

- **Chiptune voices**: pulse waves at 12.5/25/50 % duty, 4-bit triangle bass, LFSR noise drums, wavetable leads, SNES-style echo (a few taps ~180–370 ms, feedback ~0.4, low-pass in the loop). Original melodies only.
- **Fidelity follows colour depth** (option): 4-colour = mono, 4-bit volume steps, low sample rate; 8-bit = NES-like mono; 16-bit = stereo with echo; a faded present = the same music muffled.
- **Techniques (options)**: regional variations of one motif; the arrangement losing one layer per palette step; a key change or the full band returning on a colour flood; a phrase left on the dominant and resolved later; an item-get fanfare as a punctuation.
- **Foley**, synthesised and bit-crushed to the scene's era: cursor and select blips, text blips (pitch per speaker), footsteps with echo, fire crackle, magic shimmer (triangle arpeggio), charge and blast, HP tick-down, KO blink, a bit-drop per palette step, save ticks, door grind, coin and item jingles, menu error buzz.
- **One organic sound** (a breath, a heartbeat) can make a character human at one moment.
- **Silence**: true zero including echo tails.
- **Mix**: music ducks ~7–8 dB under voice (fast attack, slow release); −14 LUFS, grain 0.
- **Voice** (optional): first person, few short lines; or text blips only, for a character who exists only in text.

## 8. Native moves

A menu: use the ones your story needs.

- **Palette collapse / flood.** Colour depth drops one level per beat, or full colour floods back through a dither wave. *Fits content like:* a city blackout and recovery; a company in crisis; burnout and rest.
- **Protected colour match cut.** One exempt colour links two eras in the same screen position. *Fits content like:* a family heirloom; a brand colour across decades; a team jersey.
- **Save files as memory.** A list of files; choosing NEW FILE refuses to overwrite. *Fits content like:* versions of a product; chapters of a career; photo albums.
- **Game UI as narration.** A greyed-out name, an item description, a stat screen. *Fits content like:* a team member leaving; a skill learned; a budget.
- **Level up.** Stats rise with a fanfare. *Fits content like:* a student's year; a startup's funding round; learning a language.
- **Encounter swirl.** A crash into danger. *Fits content like:* a deadline; a diagnosis; a storm.
- **Era shift.** The same characters redrawn in older hardware. *Fits content like:* a town's history; grandparents' youth; the evolution of a device.

## 9. Pitfalls of the medium

- Rank-based palette mapping crushes a scene to black → map by luminance with a gamma.
- Reduced subsets without warm hues turn a sunset solid red → keep warm hues.
- An 8-bit set without dark green or brown turns night grass blue; generic brightening near fire turns grass neon → warm remap.
- Post-quantising a full-colour scene to 4 shades is mud → draw low eras natively with known indices at half resolution.
- Pixel hair as a smooth dome reads as a helmet; single-pixel alternation reads as noise → 2–3 big spikes. Pale clothing reads as skin. Held props cross the face in side view → back hand.
- A dark plank door reads as a jail → panels, bevels, studs.
- Negative modulo indexes `undefined` → `((n % m) + m) % m`.
- The dialog box covers the bottom quarter → keep the floor line above it.
- Match cuts on protected colours need both screen positions computed.

## 10. Engine

In `demo/`: `px.js` (indexed framebuffer, palettes and LUTs for every colour depth, Bayer dither, mosaic), `font.js` (variable-width pixel font), `ui.js` (windows, dialog, menus, file list, status bars), `sprites.js` (rig + ASCII heads), `portraits.js` (32×32 portraits + expressions), `props.js`, `scenes.js` (parallax, index lighting, tilt), `main.js` (shots, transitions, palette timing, sound events, subtitles). `?sheet=1` renders a model sheet; `?frame=<scene>&lut=<table>` renders an environment through any colour-depth table. File list and build steps: [DEMO.md](DEMO.md) "Build notes".

## 11. Variation space

You decide which game system the topic hides, the characters, the eras, the palette plan, the opening and the ending. All far from our demo:

- Structures: **an overworld tour** (a top-down map; each town a chapter entered by a door transition); **a shop and an inventory** (the story told entirely through items bought, used and sold); **a turn-based duel** (two sides take turns; each move is a scene of the topic).
- Openings: **PRESS START**, a title screen with an attract-mode demo; **a battle already in progress** with HP low; **a boot screen** that fails to load and must be retried.
- Endings: **GAME OVER** answered by a choice (retry / give up) left open; **credits scrolling over the overworld** as characters walk home; **the save screen** where the last slot is written and the menu closes.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: hd-2d -->

# HD-2D — Style Prompt

> Hand-made pixel sprites standing like paper cut-outs inside a lit, fogged, fully 3D diorama, shot from a high three-quarter angle through a tilt-shift lens: a toy world where every lamp throws a real shadow.
> References (grammar only): *Octopath Traveler* (Square Enix × Acquire, 2018) and its sequel (2023), the games that defined the HD-2D look. Learn the grammar: sprite-in-diorama, high 3/4 camera, tilt-shift focus band, point lights with shadows, heavy bloom and vignette, framed dialogue box. Never use their characters, places, logos, UI ornaments or music, and never name them in the film.
> Name: "HD-2D" is Square Enix's term (and trademark) for that look. The library borrows it only to describe the style; this style and its demo have no connection to Square Enix and are not endorsed by it. Don't use "HD-2D" as a title or brand in a film.

## 1. Essence, and what it is not

A **3D miniature set** of boxes and cylinders wrapped in **pixel-art textures**, populated by **flat 2D pixel sprites that receive light and cast shadows**, seen from a **high, far camera** through a **tilt-shift band** so the world reads as a tabletop model. **Light is the subject**: practicals throw sprite shadows across the floor; shafts, fog, dust or rain hang in the air; strong bloom, heavy vignette. On top, a small **RPG UI**: chapter card, framed dialogue box with typewriter text, serif subtitles.

The key contrast: characters stay **flat, low-res and stepped** while camera, light, particles and focus move smoothly every frame.

Not a voxel game (no cubic characters), not a flat 2D pixel RPG (the set is real 3D with real light), not a tilt-shift photo of a real miniature (textures are pixels, not materials).

## 2. Materials & rendering

- **Constant texel density**: surfaces drawn per pixel on small canvases, `NearestFilter`, world-space UVs at one density (e.g. 24 px/m); sprites on a similar scale (a character ~30–60 px tall).
- **Colour from ramps**: 3–6 swatches picked by brightness through a narrow 4×4 Bayer dither. Sprites get a 1 px *selout* outline (neighbour colour darkened toward the ink).
- **Boxes and cylinders** for buildings, floors, rock; **billboards** (instanced) for foliage, distant props, ridges. Windows are emissive pixel panes; fire is a pixel atlas stepping at ~10 fps; water a shader with quantized ripples and light columns toward the camera.
- **Light rig per set**: one dim shadow-casting key, a hemisphere fill, **practical point lights** with shadows (lamps, fires, windows, screens), and a **front fill** ~2 m before the hero (a billboard lit from behind stays black). An additive glow sprite on every source gives bloom something to grab.
- **Post chain, at render time**: supersampled render → physical DOF with tilt-shift in the same signed circle of confusion (above the band = far, below = near; far never bleeds over a sharp foreground) → bloom → vignette/grade → filmic tone map. No film grain.

## 3. Colour logic

- **Two temperatures**: one large ambient key (cold, or pale, or dusty) against small warm or saturated practicals. The practicals carry the story; the ambient carries the mood.
- The darkest value is a warm ink, never pure black; the brightest is the light source itself, bloomed.
- Each set owns one fog colour and one light key, so a cut to a new place reads instantly.
- The hero wears the one saturated costume colour that no set uses, so the tiny sprite is findable in a wide.
- UI is one metal (gold, silver, copper) plus one paper white over a dark translucent plate.
- Examples: night canal town (blue fog, amber windows); autumn market at dusk (violet sky, pink paper lanterns); snowy mine at noon (grey-white daylight, green mineral glow).

## 4. Type & subtitles

- An inscriptional capital serif (Cinzel, wide tracking) for chapter labels and titles; an old-style serif (Cormorant, Cormorant Garamond italic) for subtitles, dialogue, taglines. All OFL.
- **Narration subtitles**: italic serif ~46–54 px, centred low on a soft dark gradient band, one line per voice clip, in ~0.35 s before the voice.
- **On-screen speech gets a dialogue box**, not a subtitle: dark plate, thin metal border, corner ornaments, name plate on its top edge, text **typed over ~90 % of the voice**, blinking caret, soft chime on entry.
- Chapter cards and a title card belong to the grammar. Hold ≥ max(1.8 s, speech + 0.6 s). Export the `.srt` from the data that drives the overlay.

## 5. Motion quality

- **Sprites step, everything else glides.** Walk cycles 4 frames at 6–10 fps, idles alternate two frames at ~1–2 Hz, blinks every few seconds, pose changes are instant cuts between drawings. Camera, lights, particles, beams and focus update every output frame (60 fps).
- **Poses are data**: a parameter object per drawing; a new pose is a new table entry.
- **Lights breathe**: every flame flickers (a few summed sines, about ±20 %). A light's level is one value that drives the sprite drawing, the point light (intensity ∝ level^~1.3), the glow opacity and its scale together.
- **Weather is procedural**: slanted rain streaks; lightning as a scripted flash curve (strike, dip, re-strike, decay) lifting sky, fill and exposure together.
- The world never shakes except for impact; the set never moves, only the camera and what lives in it.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic. Always look **down** on the world (never at eye level); every path is a monotone spline of a few keys, no overshoot; focus is recomputed every frame from camera to the subject.

| Move | Expresses | Can serve |
|---|---|---|
| Very high, very far, slow push; band on one tiny subject | Preciousness, a whole place as a map | where we are; scale; a landmark |
| Medium-high 3/4, near-static drift | Two figures on one stage | a conversation; a handover; a choice |
| Lateral tracking, camera leading slightly, foreground passing blurred | A path through a world | travel; a process with steps; a commute |
| Dive low and close while a figure kneels or stops | The toy world suddenly personal | exhaustion; care; a secret |
| Rising pull-back, focus handed from figure to object | The act spreads outward | consequence; a system switching on |
| Orbit half-way round a building or prop | An object seen from all sides | a workshop; a machine; a monument |
| Top-down, straight overhead, tilt band as a strip | A board game, a plan | routes; a schedule; a queue |
| Rack focus between two depths in a locked frame | Attention changing hands | a memory; someone watching; before/after |
| Return to an earlier framing, changed | The rhyme shows what changed | aftermath; growth; a season later |

Framing: characters ~1/12–1/8 of frame height; the sharp band follows the subject's projected height (clamped ~.2–.8 of screen); with no character, use a fixed band height per shot. Transitions: short fades to black or cuts between sets; no wipes, no 3D spins.

## 7. Sound palette

- **Music**: chamber-fantasy or cinematic colours (harp, celesta, strings, horns, low choir, timpani) or small folk instruments (lute, recorder, hand drum). Either one piece whose own arc matches the story, **cut inside it** at downbeats, or an original score; a downbeat can land on the frame of a visual event.
- **Silence as a tool**: a hard stop into a reverb tail, a pad alone, or one heartbeat when the light nearly dies; a short breath (< 1 s) when something fails.
- **Foley follows the diorama's matter**: footsteps per surface (wood, dirt, stone, snow), fire crackle, cloth, a UI chime for dialogue boxes and menus, small bells for things switching on, thunder after each flash, a deep boom with shimmer for a big ignition; ambience beds per set, crossfaded.
- **Voice**: storybook narrator, slow (speed ~.82–.90); on-screen characters low-passed (~7 kHz) so they sit "in the world". Put invented names in the TTS `asr` field.
- **Mix**: lines compressed and RMS-matched; per-line auto-duck ~10 dB (down only); −14 LUFS via `core/render/mux.sh`, grain 0.

## 8. Native moves

A menu: use the ones your story needs.


<!-- END STYLE PAGE -->
