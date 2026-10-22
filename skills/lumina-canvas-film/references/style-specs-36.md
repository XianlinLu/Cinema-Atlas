# Complete style specifications 36


<!-- STYLE: game-show -->

- **Ink + paper + candy.** Near-black ink, white, and a warm cream for cards and paper props; around eight saturated candy hues (yellow, orange, red, pink, green, lime, sky, blue) plus two or three deep hues with darker partners for night or finale sets.
- **One set = one hue.** The background, its pattern and the round card share a hue; the card changes colour to match the set it introduces. Neighbouring rounds never share a hue.
- **Characters own colours.** A contestant's body colour is its identity and never changes; keep it distinct from the set it stands on (a character is never the same hue as the background).
- Big words are white or yellow with a thick ink stroke; judgement words may be pink or yellow.
- Set examples: tangerine ground `#FFB870` with `#FFA85A` stripes; teal with mint dots; navy with a gold sunburst.

## 4. Type & subtitles

- **Display**: a heavy rounded sans for Latin and numbers (e.g. Fredoka 700); a black-weight sans for CJK (e.g. Noto Sans SC 900); a hand-lettered face only for handwritten props (e.g. ZCOOL KuaiLe).
- **Telop text**: white or yellow fill with an ink stroke ≈ 14 % of the font size painted *under* the fill (`paint-order: stroke`). Titles are built glyph by glyph so each character can pop in.
- **The telops are the subtitles.** Round cards, corner banners, labels, prop text and judgement words carry the meaning; keep them short (≤ ~20 CJK characters on a banner line, ≤ ~12 on a plate; Latin runs ~1.6× wider). With narration, subtitles are telop plates at the bottom in the same outlined type, never a thin generic caption.
- Hold every text ≥ max(1.8 s, speech + 0.6 s); a judgement word may be shorter because it is read at a glance.

## 5. Motion quality

- **Idle = hop on the beat**: a parabola per beat (8–30 px); neighbours hop on the off-beat so a crowd ripples.
- **Hit = squash**: a damped wobble (~30 rad/s, ~0.35 s) after each hit; a small squash on every downbeat.
- **Entrances drop from the sky** with ease-in and land exactly on their beat, so the sound lands with them. Crowds drop in one per beat or half-beat.
- **Pops use back-ease** for anything appearing (cards, stickers, stamps, words); ease-in for exits. Nothing fades in slowly: things are either on or popping.
- **Shout pose**: arms up + open mouth for about half a beat.
- **Typewriter** reveals on fractions of a beat, with a click every few characters.
- Scene changes are **hard cuts on bar lines**, with a very short white flash. A fade is saved for the very end, if at all.
- Nothing moves off the grid: an event between beats sits on a subdivision.

## 6. Camera grammar

The stage is a frontal, symmetrical proscenium; the frame itself does the moving. A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Beat punch (zoom 0.8–5 % around centre, decays in ~0.16 s) | the hit, felt in the frame | any accent; a slam; a count-in |
| Several punches in one bar | the frame breathing with the music | a chorus; an escalating pattern |
| Locked frontal wide | the whole stage as a game board | a pattern being set up; a crowd; a scoreboard |
| Hard cut on the bar line + flash | a new round, a new set | chapter changes; a before/after |
| Split stage (two halves, two sets) | two sides answering each other | a rivalry; human vs machine; old vs new |
| Shrink to thumbnail (a finished bit scales down into a slot) | memory, accumulation | a recap; "and then all of this happened" |
| Vertical scroll of the set (floor to sky) | rising stakes or scale | a leaderboard; growth; a tower of items |
| Snap zoom onto one prop (hard cut to a 2× framing, back on the next bar) | this detail is the joke | a price tag; a number; a face reacting |

Keep the sum of simultaneous punches below ~0.06 so the frame edge never shows. Characters stand on the floor band; banners top-left, judgement words centre-top. Hard cuts only; no dissolves.

## 7. Sound palette

- **All synthesized** from the picture's events: a sine kick with soft saturation, band-passed noise snare and clap, hats, slap bass, detuned-saw brass stabs with a closing filter, square lead with vibrato, marimba-like pluck, music-box bell, triangle pad, square arp, cowbell.
- **A bright major pop harmony** on a short chord loop, one chord per bar; each round gets its own flavour (funk, quiz, electro, dream, heavy…), not a new song.
- **Event foley is toy-like and pitched**: pops, plop + boing landings, stamps, typewriter clicks, buzzers, dings, servo whirs, splats; pitched pips can spell a melody as a crowd drops in.
- **Shouts, not sentences**: one- to three-word calls ("Hey!", a number, a verdict), placed 20–30 ms before the beat so the consonant lands on it. A crowd shout = several different voices stacked a few ms apart and panned across the stereo field.
- Options to vary intensity (pick what the film needs): a jingle (crash + rising brass + snare roll) into each round; a transposition up for a finale; dropping to drums only for one bar before a big hit; a half-time bar for a reveal; one bar of silence broken by a single shout.
- **Mix**: voices and foley on their own bus; music ducked from that bus's envelope; soft-clip rather than hard limit; −14 LUFS, true peak ≤ −1 dB.

## 8. Native moves

A menu: use the ones your story needs.

- **Rounds with a card.** A 1-bar card (round number + name + a tag such as a year or a step) flies in on a jingle, then play. *Fits content like:* the steps of a recipe; the stages of a startup; the chapters of a museum tour.
- **Report card.** A typewritten recap with a grade stamp. *Fits content like:* a quarterly review; a trip summary; a final score.
- **Call-and-response.** Anything with a turn becomes a rhythm pattern; speeding up the pattern (quarters → eighths) *is* the plot. *Fits content like:* a teacher's question and the class answer; a customer order and the barista's reply; ping-pong between two negotiators.
- **Next-level tease.** Something hatches or unlocks. *Fits content like:* a next version; next season; a next grade.
- **Judgement word.** A big outlined word pops at an angle on the round's last hit. *Fits content like:* "Delivered!" on a logistics step; "Approved!" on a permit; "Personal best!" on a training plan.
- **Remix board.** One set with a timeline ribbon; each item gets a few bars centre stage, then shrinks into a slot along the bottom; at a climax all slots bounce together. *Fits content like:* a year in review; a team's release list; a festival line-up.
- **Stats as game UI.** Numbers become podium scores, counters racing to a target, price tags getting hammered, bar charts that grow per beat. *Fits content like:* fundraising progress; calories per dish; downloads of an app.
- **Crowd drop.** Many contestants drop in one per beat, each with a pitched pip. *Fits content like:* every member of a club; the planets; the ingredients of a dish.

## 9. Pitfalls of the medium

- **Stateful updates break parallel renders**: a worker starting cold shows the initial state. Recompute every pose from `t`; compare single stills with a sequential render.
- **Cue lists drift** when cut flashes, jingles and arrangement are separate hand lists: derive them from one table.
- **Fixed-length audio buffers** cut the tail: size them from the duration.
- **Text measured before fonts load** overflows plates: load fonts, then build.
- **TTS misreads digits and symbols** in shouts: spell them out.
- **Real products as characters**: names on tags, original mascots, no logos or UI; real people only as generic stand-ins.

## 10. Engine

`demo/frame_head.html` (SVG helpers: `el`, `txt`, `tf`, `op`, easing `E`, per-glyph `chars`/`charsPop`, `measure`), `demo/main_v1.js` (tempo grid `at(bar, beat)`, `ev()` sound events, `punch()`, `hopY`/`hitSq`, `gtext` telops, `stripes`/`dots`/`raysEl` sets, `burst`, `judge`, `banner`), `demo/main_b.js` (`bean()` characters + `pose()`, `human()`, `scene(t0, t1, build)`, `card()`, `dropY`, `heyAt`), `demo/music.py` + `demo/synth_lib.py` (event-driven score and SFX). The contract: `scene()` builds nodes once and returns `update(t)`, which only sets attributes. Module table and a minimal new round: [DEMO.md](DEMO.md#engine-reference).

## 11. Variation space

You decide the rounds and their verbs, the cast, the sets and colours, whether there is narration, the tempo, the opening, the ending and the length. The grid, the drawing kit and the telop language stay.

All far from our demo:

- Structures: **a tournament bracket** (two contestants per round, the winner advances, the final is a split stage); **one long round** that keeps escalating its single pattern from quarters to sixteenths as the story's pressure rises; **a quiz show** with three contestants where each question is a fact of the topic and the scoreboard is the argument.
- Openings: **the judgement first** (a "Perfect!" pops on an empty stage, then we rewind to how it was earned); **a single contestant alone** hopping on a bare floor until the crowd drops in; **the scoreboard** showing a final number, then counting back to zero.
- Endings: **a group photo** (everyone freezes mid-hop, a flash, the frame becomes a polaroid on a card); **a level-select map** where every finished round is a lit node; **a curtain** falling bar by bar with the last shout under it.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: silent-film -->

# 1920s Silent Film — Style Prompt

> An engraved-illustration silent film projected in a picture house: ink line and silver wash, a 4:3 print that flickers and weaves between velvet curtains, intertitles instead of voices, and a cinema pianist who plays every beat.
> References (grammar only): **Buster Keaton**, *The General* (1926) and *Sherlock Jr.* (1924) — the whole gag in one locked-off wide shot, a deadpan face, a body that does the acting; **Harold Lloyd**, *Safety Last!* (1923) — the near-miss; **Georges Méliès** — the iris and the trick shot; **The Artist** (2011) — how few intertitles a modern audience needs; **1920s photoplay piano cue sheets** — music by mood section, the piano doing the sound effects. Never use the Tramp look (bowler, toothbrush moustache, cane), any real film's gags, or any published melody.

## 1. Essence, and what it is not

A one-reel film as it would look *projected*:
- **A 4:3 print in a gate between theatre curtains**; the sides of the 16:9 frame are the picture house.
- **An ink drawing with washed greys and hatching**, printed on silver stock that flickers, weaves, scratches and burns at the edges.
- **Nobody speaks.** Beats are told by **action in wide shots** and by **intertitle cards**.
- **The only sound is a cinema instrument** (piano, organ) and the projector in the booth.

Not a noir (no hard shadows as mood, no voice-over), not a sepia photo filter on modern animation (the drawing itself is engraved and inked), not a Chaplin pastiche.

## 2. Materials & rendering

- **Tonal painting + Redraw.** Scenes are painted in grey values only (print densities roughly: ink 0.07, dark cloth 0.15–0.3, mid wood 0.45–0.6, skin 0.8, white linen 0.9–0.95), with soft light gradients and a thin separation line. A **Redraw** pass (WebGL2) inks the whole frame: difference-of-Gaussians contours on the dark side of every edge, luminance posterised into ~5 soft wash steps, and 45° hatching (then crossed) in the darks, re-drawn every two frames like hand-redrawn animation. Real video frames can go through the same pass so footage and drawing share one hand.
- **Print pass**: silver tone with a sepia amount between ~0.1 and ~0.36, print black ~0.055 and white ~0.93, S-curve, halation on highlights, uneven density, flicker, gate weave with occasional perforation jumps, broken vertical scratches (white = scraped emulsion, dark = dirt on the negative), brown burn creeping from the edges, vignette, two-octave silver grain; then dust, a hair in the gate, a rare blotch.
- **Frame**: 1440×1080 in the centre of 1920×1080, a rounded aperture with a soft dark rim; velvet drapes at the sides lit by the screen's spill and by footlights. Curtains can part and close.
- **Figures**: realistic proportions (7.5-head adults, ~5-head children) on a 2.5D rig (joints solved in 3D, projected with a yaw), silent-era make-up (pale skin, dark lids and lips); identity by silhouette marks (a hat, a garment, a tool).

## 3. Colour logic

- **Monochrome silver**, tinted only by the print: colder and harsher (more damage, less sepia) when things go wrong, warmer and cleaner when the film turns tender. Tint and damage are mood controls, set per section.
- Values carry everything: dark clothes against pale walls, pale faces against dark interiors; check every shot as a thumbnail.
- **One colour, at most**: an element drawn into a separate colour mask keeps its hue through the print (still getting grain, flicker, vignette). Use it for the single thing the film is about, or not at all.
- Period tinting of whole scenes (amber for day interiors, blue for night, rose for romance) is a valid alternative to sepia; one tint per section.

## 4. Type & subtitles

- **The intertitles are the subtitles**; the `.srt` lists their text. A card holds 2.5–3.75 s (≥ max(1.8 s, reading time + 0.6 s)).
- A black painted card with a deco border whose ornament follows the emotion: one heavy rule for a shout (the text shakes), a double rule with stepped corners and fans for narration, vines and small flowers for tenderness.
- Period faces (OFL): a small-caps display serif (e.g. Playfair Display SC) for titles and shouts, an italic old-style serif (e.g. Old Standard TT Italic) for narration and dialogue.
- A few words per card; three to five cards in a short film. A card never explains what the picture already shows.

## 5. Motion quality

- **Hand-cranked sampling**: character and camera motion sampled at 16 fps (18 or more to undercrank a fast scene); flicker, weave, grain and scratches change every output frame (24 fps). That mix makes it look projected rather than merely low-frame-rate.
- **Speed is an emotion**: undercrank chases and panic (faster motion, faster flicker); return to 16 fps and a calmer print for tender scenes.
- **Deadpan performance**: the face barely changes; the body acts (crouch before effort, held poses, the two-frame snap of a double take, hands on knees). Objects act too (a wobble before a fall, a ritardando to rest).
- **Keyframed, eased poses**; only deliberate gags snap.

## 6. Camera grammar

A vocabulary, not a route. The period camera is heavy: most shots are locked. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked-off extreme wide | cause and effect seen whole; the wait is the joke | a mechanical gag; a crowd; an elaborate process |
| Locked full shot | the premise in one frame | a character's routine; a confrontation |
| Tracking shot with foreground passing | pursuit; momentum | a chase; a race; a delivery against the clock |
| Iris in / out | attention on one thing; a beginning or end of a thought | an object; a face; a memory |
| Half-open iris, held | a character sharing a look with the audience | a wink; a secret; complicity |
| Slow motivated push-in | tenderness; realisation | a kneel; a letter read; a decision |
| Masked shot (keyhole, binoculars) | point of view; spying | a detective; curiosity; romance |
| Split screen / double exposure | trickery; dream; two places at once | a phone call; a ghost; a daydream |

Framing: wide and medium shots; big close-ups of rigged faces look like mannequins, so keep any close-up small or inside an iris. Transitions: iris, fade to black, straight cuts, the curtain. No dissolves between shots of the same scene, no modern whip pans.

## 7. Sound palette

- **The instrument is the sound design**, as in a picture house: an upright piano (optionally a reed organ, theatre organ, violin or small ensemble) plays every event. Mickey-mousing vocabulary (options): chromatic creep in the bass (sneaking), grace note (a wink), forearm cluster (a crash), swelling diminished tremolo (a wait), low rumbling tremolo (a storm, a machine), "plink … plonk" (emptiness), diminished sforzando (a shock), rolled chord (a door, a reveal), descending glissando (a fall), low "boing" (a bounce), nervous trill (hesitation), minor second (something breaking).
- **Photoplay idiom**: stride left hand, music by mood section in the manner of cue sheets (Hurry, Misterioso, Agitato, Tenderly, Maestoso), a theme that returns changed. Original music only.
- **No foley, no voice.** **The projector is the ambience**: lamp click, motor spin-up, claw-and-motor purr, film flapping on the take-up reel.
- **Silence**: the music stops and the projector alone remains; it frames a held moment.
- **Mix**: tame piano hammer transients with light compression before loudness normalisation (−14 LUFS). Grain goes in the picture (mux grain 1).

## 8. Native moves

A menu: use the ones your story needs.

- **The chain in one take.** A triggers B, B leaves the frame, the audience waits, B returns and hits C. *Fits content like:* a supply chain gone wrong; how a rumour spreads; a Rube Goldberg invention.
- **The near-miss.** A hand closes exactly where the object was a frame ago. *Fits content like:* catching a bus; a startup missing a deal; a goalkeeper.
- **The intertitle twist.** A card reframes the next shot in a few words. *Fits content like:* "Meanwhile, in the lab…"; "The machine had other ideas."; a statistic as a punchline.
- **Undercranked chaos.** Speed and damage rise together. *Fits content like:* rush hour; a kitchen at dinner service; a stock crash.
- **Iris on the look.** An iris stops half-way so a character can glance at the audience. *Fits content like:* a product winking; a cat that knows; a scientist's secret.
- **Redrawn footage.** Real video pushed through the ink pass becomes a period drawing. *Fits content like:* a company's archive; a family film; a sports clip.
- **The echo gesture.** A gesture from the start repeated by someone else with a new meaning. *Fits content like:* a teacher and a pupil; a handover; a tradition.

## 9. Pitfalls of the medium

- **Too much content kills a silent film**: a many-step chain at small figure scale is noise in a thumbnail. One legible chain with a pause in the middle beats three busy ones.
- **Puppet arms**: apply abduction before flexion, let the shoulder rise and swing forward as the arm goes up, slim the torso's shoulder corner on the raised side, hide the arm's contour where it lies over the torso. Raise arms sideways (or turn the figure) so they don't cross the face.
- **Pose pops**: drive every figure by eased keyframe lists, never by `if` branches.
- **Floating props**: hold a prop between the palms at the depth between the arms; tie a rolling object's rotation to distance (angle = distance / radius).
- Brow angles flip with facing direction: check expressions in a crop at final size.
- An iris must track its target in film coordinates after any camera zoom.
- A grab must put the hand exactly where the object is at the beat, or it doesn't read.
- Closed curtains lit only by a dark screen go pure black: add footlights.
- Heavy grain makes huge files → re-encode with `-tune grain` at a higher CRF.

## 10. Engine


<!-- END STYLE PAGE -->
