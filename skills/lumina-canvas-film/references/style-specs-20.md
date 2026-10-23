# Complete style specifications 20


<!-- STYLE: iso-infographic -->

- Structures: **one building, floor by floor** (a tilt down through a cutaway tower, each floor a step); **two boards compared** (the same system in two places or eras, alternating, then side by side); **a cycle** (a loop route that returns to its start with one number changed each lap).
- Openings: **the finished infographic**, which then comes apart into its moving parts; **one icon** that multiplies until it becomes the landscape; **a question written as an isometric title** on an empty board.
- Endings: **an unanswered station** (the route stops at an empty plate with a question mark); **the legend alone**, the board faded out; **a close-up of a single icon**, the whole number behind it out of focus.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: dark-keynote -->

# Dark Tech Keynote — Style Prompt

> A software launch film where the interface itself is the star: near-black gradient, hairline grid, soft light, one brand accent, and UI that moves with snap-grid precision. Light reveals, one giant number, and a sound design that is as ordered as the pixels.
> **References (grammar only):** Apple product reveals (black stage, light sweeps, one line per screen, the lone giant number); Linear / Stripe / Vercel launch videos (snap-grid motion, 1 px lines, one accent); Steve Reich's process music (phasing, subtraction); Edgar Wright's insert cuts. Never use their names, interfaces, fonts, system controls, melodies or logos, and never name them in the film.

## 1. Essence, and what it is not

A keynote-grade product film for **software**. There is no physical product and no glass render: the protagonist is the interface (a cursor, windows, notifications, tiles, a number). It lives on a dark stage lit by soft, cool light, with **one brand accent** reserved for the single most important element.

The style is defined by **precision**: every element snaps to a grid, every motion lands on a beat, every sound belongs to one designed family. Drama comes from contrast: disorder shown as generated UI, one decisive action, then empty space.

Not a glass product render (no physical object), not a screencast (no real OS or apps), not a hologram HUD (no scanlines), not a chart film (one number, not a chart).

## 2. Materials & rendering

- **Stage**: a near-black base with a radial lift at the upper centre, one large cool glow at single-digit opacity off-centre, a 50–55 % corner vignette. A hairline grid (white at ~3 %, every 4th line ~6 %) on a 48 px module. No grain.
- **UI kit, all original and drawn in code**: rounded windows (title bar with only a small glyph and title; never traffic-light buttons, menu bars or docks), notification cards, file icons with mono filenames, procedural thumbnails, list rows, tabs, badges, bars, uniform tiles.
- **Surfaces**: three steps of raised dark surface, 1 px border (~8 % white), 1 px inner top highlight, soft shadows.
- **Depth**: a 2.5D camera (`s = 1/(1/zoom − z)`); cards near the lens blur with magnification. Rotations use strip-rendered perspective (rotY ≤ ~24°).
- **Light** is the reveal tool: only pixels the light has passed turn on; unlit areas sit at a few percent.

## 3. Colour logic

- A cool neutral ladder only: near-black stage, three surface steps, text in three greys (primary, secondary, label). Neutrals are slightly blue, never warm brown.
- **One accent**, saturated and luminous, with its own glow. It is reserved for what the product *is* or *does*: the protagonist element, the call to action, confirmations, the key number. If two things are accent-coloured, one is wrong.
- **A problem colour** (typically a red for badges and warnings) may exist only while the problem exists; after the turn it never returns. Problem colour = noise, accent = the product.
- Secondary hues only as **category codes** in motion (a trail per data type), desaturated, and never on static UI.
- Example accents, pick one per film: lime `#B7F34A`, electric violet `#8B7CFF`, signal orange `#FF7A1A`.

## 4. Type & subtitles

- **OFL faces**: Inter (UI, captions, headlines; variable weight), Inter Tight 600 for giant numbers (tracking around −4.5 %), JetBrains Mono for labels, filenames and status text (wide tracking in small-caps labels).
- One line per screen for headlines. The big number gets its own screen and **no caption over it**: the number is the message.
- **Captions are a UI component**: a bottom-centre toast (dark translucent pill, 1 px light border, soft shadow, Inter 500 around 40 px, a small accent "speaking" dot). It enters with a small rise + fade in ~0.16 s and can turn more opaque over busy frames. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Typed text is its own subtitle**: text the cursor types in frame is not burned twice (it goes only into the .srt).
- Lift product content while captions are up so toasts never clip it.

## 5. Motion quality

- 24 fps on ones, no stepping, no boil: this is precision, not craft.
- **Everything lands on the grid and on the beat.** Moves start a beat early and land on it. Easing is fast-out with one small overshoot (`back`, s ≈ 1.3) and an immediate settle. No floaty sine drift.
- **Spawns are short and typed** (drop + bounce, fling, slide-in, pop; 0.2–0.3 s), one motion per element type. Tension can be a tremble of a few px.
- **Flights** follow curved paths with overshoot along the final tangent; same-type elements bend the same way and never cross.
- **A living element can act**: squash, stretch, anticipation (≥ 8 frames of wind-up), a 2-frame contact, spring follow-through. The blink of a cursor makes a natural metronome.
- **Disappearing is designed** (retract one part per beat, CRT-off squash into a point); nothing just fades.
- The stage and grid never move on their own; only the camera moves them.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | Expresses | Can serve |
|---|---|---|
| Locked extreme close-up on a tiny UI element | Intimacy, one thing alive on a screen | a single action; a thought forming; a quiet status |
| Continuous pull-back, keyed per bar in log space | Accumulation, scale growing out of one point | spreading load; a network growing; a team joining |
| Push-in through a frozen frame | Time stopped, focus narrowing | a decision; the instant before a commit; a bug found |
| Whip pull-out in one beat | Cause and effect seen at once | a sync completing; a deploy landing everywhere |
| Dive into a small UI element (log-zoom) + match cut | Going inside the detail | a counter that matters; a log line; a setting |
| Half-second inserts expanding from their source | Overload, too much to read | notification storms; errors; choice overload |
| Near-locked frame while an object turns and light sweeps | Presentation, the product as hero | a reveal; a new version; a feature name |
| Slow lateral track across a UI plane | Order read by the eye | a timeline; a pipeline |
| Top-down plan over the grid | System view, structure | architecture; permissions; a workflow map |
| Return to an earlier framing | Rhyme: what changed | before/after; a loop closed; an echo |

Framing: generous negative space, one focal element, the accent at the focal point. Dutch angle and wobble only for disorder.

**Transitions = UI expand / collapse**: every shot change is an interface element expanding into the frame or the frame collapsing into an element. No fades, no blank frames. An expansion on a beat starts one frame early so the beat frame is already ~80 % open.

## 7. Sound palette

- **Tuned percussion and pads**: marimba, vibraphone (mallet or bowed), glockenspiel, celesta, a synth pad or drone, a low sine pulse, a shaker, plucked synth, felt piano. Clean, dry, minimal; samples e.g. VCSL (CC0).
- **Music as a visible process**: options include phasing (two voices on one pattern, one drifting), additive build (one note per bar), subtractive process (notes removed until one is left), dividing the beat to accelerate instead of changing tempo, or one chord that everything lands on. Picture events can spawn on score notes from a shared note table.
- **Two sound families = story**: disorder sounds *scattered* (detuned by tens of cents, random pans, a different timbre per source); the product's sounds are *one family* (felt ticks, glass taps, all in one mode, centred), so many landings form one in-key shimmer.
- **Foley materials**: cursor tick, low-profile keys, notification glass, file plop, window whoosh, glitch accents, stacking thumps, felt mallet + sine drop for a press, light-sweep shimmer, digit grains, CRT-off.
- **Ambience**: a quiet room, a computer fan, a high coil whine that can grow with pressure. Fan and whine live in the voice band: keep them down until a line ends.
- **Silence is a tool**: digital zero on every track when the screen pauses; near-silence (a −60 dB room) for a breath. The first sound after a silence is the most important one.
- **J / L cuts** carry sound across UI transitions (a chord ringing on, a shimmer arriving before the light).
- **Mix**: music ducks ~8 dB and foley ~4 dB under voice; −14 LUFS; no grain. **Voice**: confident and restrained, short declaratives.

## 8. Native moves

A menu: use the ones your story needs.

- **Generated accumulation.** UI spawned by rule, faster and faster, hundreds of items; you don't draw the mess, you generate it. *Fits content like:* unread tickets piling up; cloud costs creeping; a dependency tree exploding.
- **The snap grid.** A whole promise in one motion: everything flies into a grid in one beat; the grid stays invisible until then. *Fits content like:* a CMS publishing to every channel; a scheduler filling a week; an audit turning green.
- **The living element.** The cursor (or the product's smallest live element) is the protagonist and the brand mark. *Fits content like:* a search box that grows ambitious; a progress ring that refuses to finish; a status dot.
- **Freeze.** Everything stops mid-air and the sound drops to digital zero; only a screen can stop time like this. *Fits content like:* a security breach caught; a failed deploy; the second before "send".
- **Light reveal.** A soft band sweeps across and only lit pixels turn on (soft front, glint ≤ 20 %, ≤ ~1.3 s so nothing stays dark). *Fits content like:* a redesign; a new pricing page; an API console.
- **Number from glyph noise.** Digits scramble and lock one per sixteenth note with a small bounce. *Fits content like:* latency cut; a count of users; a price.
- **Type streams.** Elements fly to their own rows along coloured curved trails, so categories read as streams. *Fits content like:* an inbox triaged; logs routed by severity; files synced by device.
- **Put-away.** The UI dismantles itself one part per beat until one element is left. *Fits content like:* "less is more" features; offboarding; focus mode.

## 9. Pitfalls of the medium

- Strip perspective of a semi-transparent canvas shows vertical seams (overlapping slices double alpha) → project the *opaque* surface, then light it in screen space.
- A hard white glint reads as a sticker reflection → soft front, glint ≤ 20 %.
- Nearest-slot snapping looks like a flicker, not a collapse → typed destinations, curved paths, trails.
- Too few elements leave holes in a grid that read as a mistake → generate by rule, then trim or pad to exactly the slot count per group.
- A flat tinted rectangle for "closing" looks like a placeholder → squash the real surface.

## 10. Engine

`demo/engine.js` (Canvas 2D ES module): `setAccent`, `bg`, `grid`, `panel`, `litShape` (any shape in this style), `trail`, `caret`, the UI kit, `flyPose`, `lightReveal`, `perspective`, `scramble`, `toast`, `camera` (2.5D). Function table and a minimal example: [DEMO.md](DEMO.md#engine-reference); `?scene=engineDemo` renders it.

## 11. Variation space

You decide the product's verb, the protagonist element (or none), the problem image, the accent, the structure, the opening, the ending, the camera path and the score process. All far from our demo:

- Structures: **a countdown** (a release checklist ticking through its items, each a UI moment, ending on "shipped"); **side by side** (two versions of a workflow run in split screen, the old one drowning, the new one finishing early); **a zoom ladder** (one pixel → a component → a screen → a fleet of devices, each level a new fact).
- Openings: **the number first** (a huge stat on black, its meaning revealed backwards); **a plan view of an empty grid** that fills slot by slot; **a hard insert storm** from frame one, calm arriving only later.
- Endings: **one tile left** lit in the accent on an empty grid; **the product running quietly** in a wide shot, no text; **a shipped state** (a single confirmation toast, then darkness).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: living-screencast -->

# Living Screencast — Style Prompt

> A product walkthrough that looks like a real screen recording, where a low-resolution mascot lives inside a high-resolution interface and acts out what the software is doing.
> References (grammar only):
> - **Screen Studio-style product recordings:** auto-zoom to the cursor, cursor smoothing, click push-ins, and a window floating on wallpaper.
> - **Apple "Guided Tour" videos:** real interface, calm narration, one feature per sentence.
> - **Duolingo and Headspace mascot motion:** squash and stretch, anticipation, a character that performs inside the UI.
> - **The Browser Company (Arc) launch films:** playful tone and fast cutting.
>
> Never copy their characters, UI, music or footage.

A walkthrough of a piece of software, typically 45–75 s. The user gives the product and the features; you decide the story, shots, choreography, sound and music.

## 1. Essence, and what it is not

The film looks like a **screen recording of the real product**, but it is not a recording. Every window, menu, diff line and button is **redrawn in 2D (HTML/CSS/SVG)**, so the camera can go anywhere, every pixel is controllable and text stays sharp at any zoom.

A **mascot made of big square pixels** lives in that high-resolution world. The clash of two resolutions, a hard-edged low-res sprite against anti-aliased UI, is the look.

The mascot is the software's agency made visible: when the software reads, it runs along the rows it reads; when it plans, it holds a pixel pencil; when it tests, it stomps the button.

**Two actors, never a hand:** the **cursor** is the user; the **mascot** is the software.

Not a dark tech keynote (no black stage, no invented abstract UI: this is the real product), not a pixel-art game (the world is hi-res vector UI; only the mascot and its props are pixels), not a real capture (nothing is a screenshot).

## 2. Materials & rendering

- **Real UI, redrawn**: every label, mode name and shortcut matches the real product; no screenshots, no lorem ipsum. Demo content (code, data, test output) is coherent, and the app under test really changes.
- **Pixel grid is sacred**: the mascot, its props (pencil, "!", sparkles, heart, dust) and trails share one square-pixel grid with crisp edges. It scales with the camera; its position snaps to half-pixels, so its motion feels stepped.
- **Gravity = top edges of UI**: the mascot only stands on the top edge of a real element (input box, menu, list row, code line, button, status bar, the letters of a heading). Its position comes from **measuring the live DOM** every frame, never hand-placed coordinates.
- **Window on wallpaper**: the app floats on a desktop with a soft shadow; zoom never shows beyond the monitor.
- **Depth** only where it serves attention: rack focus (blur the pane that doesn't matter), a vignette spotlight. Never blur text the viewer must read.
- **Motion blur** is derived from camera speed and applied as an anisotropic blur on an **untransformed wrapper**, only on whips. Slow moves stay sharp.

## 3. Colour logic

- The product's own interface colours rule: follow its real light and dark themes exactly.
- The mascot keeps the product's or brand's mascot colour, or one saturated hue that no UI element uses, so it finds the eye in any frame.
- Overlays (chapter pill, key HUD, captions) are neutral frosted glass; one accent at most, taken from the product.
- A theme switch can be a story event: the whole film may change state with it.

## 4. Type & subtitles

- UI type follows the product (or licence-free look-alikes such as Inter, JetBrains Mono, a serif for editorial UIs).
- **Information layers only**: a chapter pill (01–04), a KeyCastr-style keystroke HUD, frosted-glass caption pills, an optional "▶▶ 4×" time-lapse tag. Nothing else overlays the screen.
- Captions sit in a pill at the bottom, never over the element being discussed and never under the mascot; hold ≥ max(1.8 s, speech + 0.6 s).
- A title, if any, is diegetic: it appears as part of the UI (an empty-state heading, a window title, a notification).

## 5. Motion quality

- 30 fps; UI on ones; mascot position stepped to its pixel grid.
- **Mascot acting**: jumps with anticipation crouch, stretch on take-off, tucked legs, landing squash with a damped bounce and dust. Idle breathes (a tiny squash) on the score's beat and blinks irregularly. Walks by leg alternation, flipping the sprite for direction.
- **Eyes carry the acting** (neutral / left / right / up / down / wide / happy / shut / blink): they look at what matters. Arms: down / up (cheer) / wave.
- **Cursor**: smoothed, spring-eased paths, small push on click, never teleports.
- **Cause and effect**: every mascot action triggers a real UI state change; every user action is a cursor move, click or keystroke shown on the HUD.
- UI animates like the real product (its own menus, popovers, diff reveals); don't invent flourishes the product doesn't have.

## 6. Camera grammar

A recording-software camera: one continuous take inside the screen, zoom ≥ 1, cuts only under chapter transitions. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Push-in to the cursor or caret | "this is where it happens" | typing a prompt; choosing a menu item; a setting |
| Slow drift at rest | the app is alive while we listen | a line of narration; waiting for a result |
| Whip-pan between panes (with blur) | cause here, effect there | sending a message → a result appearing; code → preview |
| Push-in + vignette freeze | the one promise to remember | a safety guarantee; a price; an undo |
| Rack focus between panes | attention moves, nothing else does | reading files; logs scrolling while chat waits |
| Pull back to the full window | the whole workflow in view | a summary; parallel tasks; before/after |
| Follow the mascot along a list | the software working through items | scanning results; a checklist; a migration |
| Split-window reframe | two things at once | parallel sessions; compare two versions |

Framing: the thing being discussed and its caption never overlap; the mascot never covers text to be read. Transitions: chapter pill wipes, pixel wipes, a theme reveal circle; never dissolves or screenshots.

## 7. Sound palette

- **Two resolutions in the music**: a hi-fi layer (piano, upright or electric bass, brushed or tight kit, glockenspiel, real samples) is the world; a chiptune square or pulse voice is the mascot. They can trade, duet or merge.
- Options: a low-passed "night" version of the band for a dark theme; a tom fill and crash at chapter seams; dropping the drums to build tension; the mascot's notes on words it lands on; a stereo split for split screens; a single held pad under a freeze.
- **Foley**: keyboard (a thock plus a click, human timing jitter), trackpad clicks, pane swishes, popup pops, notification chimes, CI ticks, a shutter for screenshots. Mascot steps, jumps and landings are 8-bit.
- **Silence**: a short drop to room tone before the key promise makes it land.
- **Voice**: calm, one feature per line; product names verified with whisper. Keep effects off word onsets. Duck music under voice; −14 LUFS.

## 8. Native moves

A menu: use the ones your walkthrough needs.

- **Match-cut origin.** The mascot is born from something already in the UI (a logo's block characters, an icon, a loading spinner) and climbs out, leaving an outline. *Fits content like:* a chat bubble turning into a guide; an icon becoming an assistant; a spinner becoming a helper.
- **Diegetic title.** The name appears as a real UI element; the mascot lands on it on a downbeat. *Fits content like:* an empty state; a new-project dialog; a welcome email.
- **Moving floor.** The mascot rides a caret, a popup, a sent message, a progress bar. *Fits content like:* a message flying into a thread; an upload bar; a drag-and-drop.
- **Time-lapse with a tag.** Long work runs at N× with a flashing tag and rack focus. *Fits content like:* indexing a library; a data import; a build.
- **Spotlight freeze.** Push in and vignette the one badge that holds the promise. *Fits content like:* "Saved"; "Encrypted"; "No charges until…".
- **The film changes state.** A toggle's effect escapes the preview and takes over the whole film, and returns later. *Fits content like:* dark mode; a language switch; offline mode.
- **Cell division.** A new session or window splits the screen and the mascot splits with a pixel burst. *Fits content like:* parallel tasks; multiple accounts; team members.
- **Cursor and mascot as characters.** The cursor pets, pokes or drags the mascot, and it reacts. *Fits content like:* approving a suggestion; undoing; onboarding delight.
- **Karaoke-ball words.** The mascot hops from word to word as they are spoken. *Fits content like:* a slogan; a shortcut list; step names.

## 9. Pitfalls of the medium

- Invented features or renamed modes → check every button, mode and shortcut against the product's documentation; if it isn't in the docs, it isn't in the film.
- The mascot floats or drifts off its element → measure the DOM every frame, stand only on top edges.
- The mascot covers text or sits under a caption → reserve a text-free lane for it.
- Blur-filter "fake depth" on text you want read, or zooming out past the screen → rack focus only on panes not being read; zoom ≥ 1.
- A hand, arm or finger on screen → the cursor is the user.
- Motion blur applied to a transformed layer smears the pixel sprite wrong → blur an untransformed wrapper, and only on whips.
- A keypress or pop landing on a product name masks it → shift foley off word onsets; re-check with whisper on the final mix.
- TTS mispronounces the product name → try voices and spellings, verify with whisper.

## 10. Engine

In `demo/`: `film.js` (timeline: VO at fixed times, every visual beat hung on a spoken word with `W(id, word)`, camera moves, `Actor` mascot segments, `Cursor`, sound events), `ui.js` (state → HTML for each interface), `clawd.js` (sprite grid, poses, pixel props: replace the sprite with your own mascot), `main.js` (light/dark layers, DOM anchor measurement, motion blur, HUD: captions, keys, pixel wipes, spotlight), `sound.py` (score, foley and VO from `events.json`, with ducking). Build notes: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the features and their order, the mascot (the product's own, or an original pixel character), the story, the opening, the ending, the camera path, the chapters and the music. All far from our demo:

- Structures: **a bug hunt** (the mascot chases one error through logs, code and a fix, a single chapter); **a day of one user** (morning to evening in one app, the theme and music shifting with the hour); **a race** (two windows side by side, old way vs. new way, the mascot winning on the right).
- Openings: **mid-task** (a half-written document; the mascot is already pushing the cursor's selection); **the notification** (a system toast lands; the mascot is inside it); **empty state** (a blank app, a caret blinking; the mascot drops from the menu bar).
- Endings: **the mascot goes to sleep** on the finished item as the window dims; **the app closes** and the mascot is left standing on the dock; **a real share** (the result is sent and the mascot rides it out of frame).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: hologram-hud -->

# Sci-fi Hologram HUD — Style Prompt

> An object is scanned into a glowing wireframe. Target boxes lock onto its parts; each opens in a local exploded view, a leader pulls out, and its number rolls from garbage glyphs into the real value. It may light up, once, into a solid hologram.
> References (grammar only): the *Iron Man* / *Avengers* HUDs (target boxes, callouts, rolling numbers, layered depth); the *Oblivion* interfaces (one colour, hairlines, space); CAD exploded views. Copy none of their layouts, icons, fonts or colours.

A **scene style**: it does a practical job (a spec walkthrough, a teardown, a loop screen) for any object with parts. See §11 for the jobs.

## 1. Essence, and what it is not

The subject is always a **line wireframe made of light** above a round projector pad on a near-black stage, never a rendered object. Everything reads as *scanned data*: a scan plane grows the model, parts pull apart along their assembly axes, numbers are *computed* on screen.

Three depth layers are always present: a **background dot grid** (slow parallax), the **subject** with its pad and floor, and the **foreground HUD** (corner brackets, rulers that parallax faster, status text).

Not a type-driven keynote (dark-keynote), not a drafting sheet (blueprint), not a product render (glass-product). The subject stays a wireframe; it may gain translucent faces once, and even then the lines stay on top.

## 2. Materials & rendering

- **Stage**: near-black tinted by the hue, a radial lift behind the subject, a fading dot grid, a strong vignette.
- **Projector pad** in true perspective: concentric rings (one bright, one dashed), ticks, faint rays; it rotates slowly and spins with any turntable move.
- **Wireframe**: additive ~1.3 px strokes in a few alpha levels set by **depth fog** (near bright, far ~25 %), plus two low-res glow passes.
- **Hot edges** (near-white of the hue) only for what matters now: the scan front, inner pieces flagged `hot` when opened, a light wave, a part being pinged.
- **Real CAD topology**: tubes are rings plus longitudinal lines. **Every part is physically connected**: a floating piece is noticed first.
- **Solid hologram**: faces filled with a screen-space **Fresnel** × a scrolling **interlace**; lines thicken as it ignites; a light wave climbs the model. A **beam** (one path, nonzero winding) with faint rays and dust.
- **HUD furniture**: corner brackets, parallaxing rulers, subject // mode top left, a live status line top right, telemetry at the bottom.
- **Text never sits on the wireframe**: every text block has its own **dark plate** (translucent near-black, 1 px border, corner ticks); the camera still keeps the subject clear of text.

## 3. Colour logic

- **One cold hue plus one warm accent**, both parameters (e.g. mint/orange, violet/lime, ice-blue/red; choose from the subject).
- The hue carries lines, HUD and fills. The **accent is spent on locked values only**: a number turns accent-coloured at the frame it becomes true. Nothing else ever uses it.
- White is heat: near-white edges and one-frame flashes mark what is active. Everything at rest sits in the hue's alpha levels.
- One object may keep its own colour (the single-colour exception, `keep`), for a brand mark, never for decoration.

## 4. Type & subtitles

- Rajdhani, all caps: Light for big numbers and the product name (wide tracking), Medium/SemiBold for labels. Share Tech Mono for micro data (coordinates, counters, zoom).
- Numbers are **monospaced** so rolls never jitter; the decimal point is a small square (a glowing "." reads as a comma).
- Subtitles are HUD: a dark plate with corner brackets and "voiceprint" bars moving with the speech, near-white Rajdhani Medium, bottom centre; in just before the voice, hold ≥ max(1.8 s, speech + 0.6 s).
- The title is part of the scene (no title card): the name rolls in like a value, then code, category and tagline.

## 5. Motion quality

- **Everything on ones at 24 fps.** Only glyph scrambling steps, every frame.
- **Target lock**: oversized, rotated 45°, faint; snaps to fit in ~0.2 s (cubic ease-out), flashes white 3 frames on the downbeat.
- **Explode** along each piece's assembly axis: the shell slides *along its own axis*, the contents stay in place and glow. Open over a beat or two, close fast.
- **Leader**: anchor ring → diagonal → horizontal to the card in ~0.5 s. **Rolling value**: characters lock right-to-left and turn accent on the downbeat with a one-frame flash.
- **Chip dock**: a finished value slides into a side rail and stays until the end.
- **The camera follows the box**: cubic ease, starting *before* the next lock, **real motion blur** only inside the whip (sub-frames, 180° shutter); HUD stays sharp.
- **No cuts or fades inside the scene**: only the scan plane (scanning in or erasing) and a loupe iris. A **glitch** of three frames at most once, on the biggest change.

## 6. Camera grammar


<!-- END STYLE PAGE -->
