# Complete style specifications 19


<!-- STYLE: ukiyoe -->

- **The sheet is the frame**: the print fills the screen at zoom 1, inside a thick + thin ink border, with a paper margin beyond. Sheets can sit on a long mounting scroll (darker tan paper, a roller at one end), so the camera can travel from print to print.
- **Blocks**: draw each colour group into its own offscreen canvas, cached once (key lines; blues; greens / secondary; reds / figures). Composite each with a small fixed registration offset (1.5–2.5 px, a different direction per block).
- **Texture every colour block**: woodgrain (`source-atop`, strongest in sky and water) → baren streaks → goma-zuri specks (both `destination-out`); the key block gets specks only; light paper fibres over the finished sheet so paper shows through the ink. Big dynamic fills get the same textures inside their clip. Woodgrain = iso-lines of a warped noise field; baren = blurred circular arcs + zigzag streaks (recipe and alphas in [DEMO.md](DEMO.md#palette--props)).
- **Bokashi** is generated per pixel: a gradient whose top edge wanders by low-frequency noise per column (±20–30 px). Never strips of `fillRect` (vertical seams).
- **Line**: key lines 2.4–3 px; large contours are variable-width filled strokes, tapered at both ends, with ±20–35 % low-frequency width jitter. Distant things get a grey key line or none.
- **Motifs of the medium**: mist as long rounded flat bands (suyari-gasumi) fading at both ends; pines with flat-topped **needle pads**; fields as high, flat, parallel layers whose cross lines are **parallel and slanted**, never converging; rain as two sets of fine straight lines at slightly different angles under a sumi bokashi sky; water as banded blues with bokashi between bands, foam and spray left as paper.
- **Seal**: characters cut out of red, chipped edges. **Figures** are small in the landscape (roughly 80–130 px at full sheet), flat, with a clear silhouette; faces in a few strokes.

## 3. Colour logic

- **A pigment set, not a colour wheel**: 6–9 flat hues, each printed from its own block, over the paper ground. No gradients except bokashi, no shading on forms.
- **Sumi key line** over everything; **paper is the white** (no white pigment for foam, snow, mist, blank sky).
- **One dominant hue family** carries sky and water (in the 19th-century prints, Prussian blue); **red is rare**: seals, a sun, one garment or tab.
- Far layers pale and low-contrast, near layers saturated with dark key lines.
- Examples, one per film: an indigo-and-beni landscape (Prussian blue, pale blue, beni red, ochre, greens, sumi); a bijin-ga interior (pale pink, mauve, grey-green, lacquer black, a mica-grey ground); an autumn surimono (persimmon, ochre, grey-green, deep brown, one blue).

## 4. Type & subtitles

- **Subtitle = a horizontal cartouche**: a cream slip with a thick + thin ink border and a small red seal at the left; Shippori Mincho (500) in sumi, centred near the bottom. It "prints" in with the reveal mask and fades out. Hold ≥ max(1.8 s, speech + 0.6 s). It covers the bottom ~150 px: keep ground lines and figures above it.
- **View cartouche**: vertical cream slip, thick + thin border, a pale tab with the series title, the view title below in a brush font (e.g. Yuji Syuku), a seal beside: the "full stop" of each view. Titles live on the print as cartouches and seals, never as floating type.

## 5. Motion quality

- Prints are still. **Most of the frame does not move**; each view has one or two small actions (steam, rain, a lantern, a falling leaf).
- **Figures and nature step at 8 fps**; rain and fast water at **12 fps**; **the camera moves on ones (24 fps)**. A stepped camera judders.
- **Printing reveal**: each block appears over ~0.3 s with a diagonal baren sweep with a noisy edge, sliding 5–6 px into registration as it lands (pure noise looks like mould).
- Cartouches drop in (fade + a short slide); a seal *stamps* (scale ~1.35 → 1 in 0.2 s).
- A native move needs a **held beat of about a second** to be read; a peak flashed in under a second reads as noise.

## 6. Camera grammar

The camera moves *over* prints and between them; it never rotates in 3D space inside one. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame on one sheet | Reading a print on a wall | a place; a portrait; a still moment |
| Handscroll slide, right → left through the mounting gap (shorter slides = urgency) | Travel, the next station | a journey; a sequence of steps; a race |
| Very slow push toward a framing device (a window, a fan, a gate) | Attention narrowing | discovery; longing; a detail that matters |
| Tilt past the border into the mount | Something larger than the print | a flood; a rumour; a giant |
| Pull-back from one sheet to many | The series seen whole | a summary; a timeline; a collection |
| Crash-zoom into the texture (grain, specks, fibres) | The medium itself becomes the image | a dream; a breakdown; a memory dissolving |
| Pan across a triptych (three sheets side by side) | One scene too wide for one sheet | a procession; a battle; a festival |
| Hard cut to a blank sheet | Ma (間), a held breath | aftermath; a pause before a decision |

Framing: bold cropping and extreme foreground elements (a branch, a post, a lantern crossing the frame) are native; depth by stacking, never by perspective. Allowed transitions: scroll slides, printing reveals, a wash back to paper, a cut to blank. No cross-dissolves, no 3D flips.

## 7. Sound palette

- **Japanese instruments, not piano and pads**: shamisen (`core/audio/pluck.py shamisen`, with sawari buzz), shakuhachi, koto, taiko and shime-daiko, kotsuzumi / ōtsuzumi calls, hyōshigi (wooden clappers), a small bell.
- **Modes**: miyako-bushi (in scale), yō, ritsu; long breathy tones with a slide into each note and *meri* drops at phrase ends suit the shakuhachi; the shamisen can hold a pulse or an ostinato.
- **Techniques, as options**: absolute silence as *ma* (cut reverb tails too); a single sawari note left ringing; free-rhythm breath phrases against a steady pulse; clappers that accelerate (the kabuki curtain call); a taiko heartbeat that tightens into a roll; a koto glissando for a turn of season; a drum call (*kakegoe*) before an entrance.
- **Foley follows the material**: paper (baren rub = band-passed noise with a slow circular modulation; scroll slide; seal = low thump + tacky peel), wood (block set down, hollow steps), glass (wind chime), water, birds and insects of the season.
- **Voice**: calm, few short lines, like a poem written beside the print. Duck music ~8 dB under voice, ambience ~4 dB. Loudness −14 LUFS; `mux.sh` grain **0** (the paper is the grain).

## 8. Native moves

A menu: use the ones your story needs.

- **A series of views.** One constant subject in different compositions; the story is told by *where it sits in the frame* each time. *Fits content like:* one building through a century; a product in five homes; the same street in four seasons.
- **The handscroll.** Scenes don't cut; the camera slides right to left and the next print arrives. *Fits content like:* a supply chain; the stations of a pilgrimage; the steps of a recipe.
- **Printing, block by block.** Key line first, then each colour lands slightly off and snaps into register. *Fits content like:* a building going up; an idea taking shape; a character being "made" for the story.
- **Paper is the white.** Foam, snow, mist and blank sky are unprinted paper; white can flood the frame and wash the print back to a blank sheet. *Fits content like:* a snowfall that erases a town; forgetting; a clean start.
- **The frame is an object.** Border, cartouche and seal are physical; something big enough breaks out of the border into the mount. *Fits content like:* a festival that can't be contained; a legend; a runaway success.
- **Alternate impressions.** The same key block reprinted with different colour blocks (day → night, spring → winter). *Fits content like:* before and after; a city lit at night; two lives in one house.
- **The triptych.** A scene split across three sheets that join. *Fits content like:* three generations; a panorama of a harbour; a debate between three voices.

## 9. Pitfalls of the medium

- Bokashi from `fillRect` strips leaves vertical seams → build it per pixel.
- Too much speckle or fibre makes dark areas look like sandpaper or scratched film → specks α ≈ 0.3, fibres α ≈ 0.09.
- A perspective grid for fields looks digital → parallel, slanted, flat layering.
- Pine clusters drawn as half-discs look like parasols → flat pads with needle fans.
- Offset curves self-intersect at tight bends → build inner lines from the gentle side of the contour; force control points x-monotonic.
- Breaking out of the print must escape **both** the sheet clip and the frame clip.
- A seal drawn with `multiply` vanishes on dark ground → `source-over` there.

## 10. Engine

In `demo/`: `print.js` (paper, woodgrain, baren, specks, blocks, bokashi, carved lines, reveal masks, cartouche, seals: the reusable core), `nature.js` (mountains, pines, rocks, rain, birds), `wave.js` (banded water, fractal claws, spray), `traveler.js` (flat figure rig), `views.js` (prints as cached blocks + per-frame `paint()`), `main.js` (camera, scroll, reveal, subtitles), `music/score.py`. Instrument recipes and commands: [DEMO.md](DEMO.md#build-notes).

## 11. Variation space

You decide the constant subject (or none), the number of views, the characters, the opening, the ending, the camera path, the pacing and the pigment set. All far from our demo:

- Structures: **alternate impressions** (one key block of a single street, reprinted for dawn, rain, festival night and snow); **a triptych unfolding** (three sheets revealed one at a time, the story only readable when all three join); **a print being made** (the carver's blocks, one per shot, each block's colour telling one chapter).
- Openings: **a close crop** (an extreme foreground detail, a lantern or a sleeve, fills the sheet; the pull-back finds the print); **the bare block** (carved wood inked, the paper laid on, the baren rubs; lifted to reveal the first print); **the mount first** (a closed scroll unrolls to its first sheet).
- Endings: **a seal alone** (the print fades back to paper, only the red seal remains); **the album closes** (sheets stack like pages, the cover lands); **the last print left unfinished** (key line only, colour blocks never land).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: papercut-red -->

# Red Paper-cut — Style Prompt

> Chinese window-flower paper-cuts brought to life: jointed red cut-outs on paper grounds, where the cut *is* the drawing and the holes are where the light gets in.
> References (grammar only): folk window flowers of Shaanxi and Yuxian (sawtooth, crescent, cloud and swirl cuts, fold-symmetric rosettes, *yin* and *yang* cutting); the 1958–59 Shanghai Animation Film Studio cut-paper shorts (jointed figures, profile acting, paper layers in parallax). Copy no studio character, no named artist's work and no real motif sheet: generate every pattern from code, and never name the references in the film.

## 1. Essence, and what it is not

Every visible thing is **a piece of paper that was cut with scissors** and laid flat on another sheet. There is no painting, no gradient shading, no outline stroke: detail, volume and expression come only from **what was cut away**. Red paper is the hero material; grounds are paper too (a light paper by day, a deep dyed paper by night). Characters are **jointed cut-outs** (head, torso, upper and lower limbs pinned at rivets) animated in hard 12 fps steps.

Not shadow puppetry: no light behind a screen, no translucent dyed hide, no rods. Here the paper is **front-lit and opaque**; backlight is a special event you save for the moment that needs it. Not flat vector art (no strokes, no gradients), not a silhouette film (every shape's interior is cut).

## 2. Materials & rendering

- **Paper grain:** a neutral-grey texture in `soft-light` inside each piece (dye mottling, fibres, specks), then the piece's alpha restored with `destination-in`, so holes stay holes.
- **Cut edge:** every silhouette is a polyline with a slight low-frequency wobble (hand-cut), a 1 px light rim upper-left and a dark rim lower-right (the cut face). Architecture and machines use straight segments + wobble, never smoothing.
- **Paper thickness:** each piece casts a tight soft shadow on the layer below; stacked folded paper shows 2–6 offset darker edges.
- **Figures: red block + yin lines.** Every figure piece gets an **inset contour** (a thin slit a few units inside the outline): the classic double outline, which also separates red-on-red overlaps (an arm over a coat).
- **Folk cutting vocabulary** (`demo/motifs.js`): sawtooth rows (fur, grass, tiles, fringe), serrated edges, crescents (scales, quilting), swirls (joints), clouds, rosettes, plum, coin, tapered slits.
- **No floating islands.** A closed ring cut would drop its centre out of real paper. Eyes are two crescents (upper and lower lid) that leave bridges, plus a pupil *hole*.
- Faces never morph: expressions are **swappable face pieces** (smile, surprise, fear, determined, asleep).
- **The rosette (团花)** is designed as one 45° wedge and mirrored 8× (D4); other folds give 2×, 4× or 6×. Alternate rings of *yang* cut (band cut away, red lines left) and *yin* cut (lines cut out of a red field). Fold seams leave faint crease lines: keep them, they are true to the craft.
- **Light:** front-lit scenes use the paper as is. Night: `frame × lightmap` + warm pools, then **emissive** backlit pieces (light × paper transmission via `multiply`; holes at full light), a two-level bloom and optional rays. Keep bloom low enough that the pattern stays legible at the centre.
- **Projected pattern:** a piece's hole mask, squashed onto the ground and added with `lighter`; on a character, masked by its layer alpha over a solid warm spot, so cut features still read as holes.

## 3. Colour logic

- **China red** (around `#d2201f`, range `#c8102e`–`#d7261e`) is the hero material. Depth and role are shown by **paper tones one step apart**, not by shading: near pieces one step brighter, far pieces one step darker, an antagonist or a heavy object one step deeper.
- **Ground and hero must be different paper families.** If background and hero are both red, the silhouettes stop popping. At night, all background layers are one dark dyed family and only the pieces that matter to the story are red; by day, a light paper ground with red and pale-red layers.
- **Gold foil** is an accent kept for one late moment (a sun, a title, a coin); never a second main colour.
- Examples of ground families: indigo night papers (far layers lighter blue, near darker); a warm rice-paper day with pale-red far hills; a jade-green or black paper for a story that isn't festive. Choose from the topic.

## 4. Type & subtitles

- **Subtitles are a paper strip in the world**, e.g. a red banner (横批) darker than the picture's reds so cream text holds, serrated edges, swallow-tail ends; a sturdy OFL serif (e.g. Fraunces SemiBold) around 44 px, low, with a paper shadow. It drops in on two 12 fps steps, like a couplet being pasted. Hold ≥ max(1.8 s, speech + 0.7 s); never overlap.
- **Titles** are cut-out letters (*yang*-cut, counters are real holes) popping in letter by letter on 12 fps steps, with sawtooth border strips and a seal cut by code.
- Small credits may be printed ink on paper.

## 5. Motion quality

- **Characters step at 12 fps** (pose sampled at `floor(t·12)/12`); **camera, light, weather, flames and flying pieces move on ones** at 24 fps.
- Rigs pin pieces at rivets (neck, shoulders, elbows, hips, knees, jaws, tails). Hard poses, tiny eases, 1-frame overshoots ("pop" = 1.15× for one step). Weight comes from **size and camera shake**.
- In profile, a raised near arm crosses the face: keep hands forward of the face or let a prop cover them.
- **Folding:** the flap is split into ~16 strips; each is compressed by cosθ and enlarged along the fold by `1 + 0.28·height` (fake perspective), darkened as it stands up, in a lighter back colour past 90°, with a growing shadow and a crease after. About half a second per fold, each on a hit.
- **Cutting:** the pattern is revealed through a mask of circles along the scissor path; the offcut drops once the outer edge is passed; blades open and close on a subdivision of the beat; scraps flutter out and land.
- **Unfolding:** successive unfolds a fraction of a second apart, each flap swinging from folded to flat with ease-out (the "pa!" snap), then a scale bump and warm flash on the accent.

## 6. Camera grammar

A vocabulary, not a route. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Extreme close-up tracking the scissor tip | making; attention to craft | a beginning of work; a precise act; a signature |
| Flat front view, locked | the cut-out as an emblem | a title; a statement; a family portrait |
| Slow pan across paper layers (parallax) | a world laid out | a village, a route, a timeline |
| Low wide, a shape standing up from the ground layer | scale, threat | a storm; a rival; a deadline arriving |
| Top-down tabletop | the craft as plot | folding, cutting, assembling, sorting |
| Push toward a lit piece, pull back to many | one act spreading | influence; a network lighting up |
| Page turn / sheet peel | time or place changing | day to night; before and after; chapters |
| Pull back to an object in a room | the film was a thing someone made | memory; a gift; a tradition |
| Rotation around a rosette's centre | order, repetition | a cycle; a team |

Framing: layers stay parallel to the screen; depth comes from parallax and paper tones, never from perspective. Transitions are paper actions (fold, page turn, peel, a sheet flying off, a cut through the frame); no dissolves.

## 7. Sound palette

- **Foley follows the material:** scissors = metallic shear sweep (2.5–9 kHz) + a short ring + a fibre crack; folds = swish + crease tap; unfold = sharp snap; heavy steps = *cardboard* thud, not flesh; paper peel; pasting = a palm pat; match strike, puff; firecrackers = dense clicks 20–60 ms apart with low booms.
- **Instruments:** a bright Chinese chamber ensemble, not piano and strings and not the opera percussion of shadow puppetry: pipa (tremolo on long notes), zheng (`dan_tranh`: broken chords, glissandi, tremolo), erhu (glides), dizi (flute), sheng or yangqin colours, woodblock, small and big gong, frame drum. Pentatonic modes.
- Options: one snip = one beat subdivision; a rising zheng run, one note per thing that appears; a frame-drum heartbeat for weight; one big gong saved for one accent; total silence for a held breath.
- **Voice:** warm storyteller, few lines. Duck music ≈ 9 dB and foley ≈ 3 dB under the voice; keep impacts out of voice windows. Folk names may need an `asr` alias in `lines.json`.
- Mix to −14 LUFS, **no film grain** (the paper fibres are the texture).

## 8. Native moves

A menu: use the ones your story needs.


<!-- END STYLE PAGE -->
