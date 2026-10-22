# Complete style specifications 07


<!-- STYLE: telestrator -->

- **Freeze entry**: white flash 0.1 s (0.55) + punch 1.035 → 1.0 in 0.35 s (ease-out) + desaturate 42 % + a cool cast + heavier vignette; then a slow 1.2 % creep. Overlays use the same transform as the picture, or they slide off the players.
- **Spotlight**: everything outside a focus ellipse darkens to 0.42 (even-odd hole), 0.3 s fade.
- **Marker line**: dark outline (w + 6, black 0.55) + coloured core with glow 18 + thin white highlight (w × 0.28); drawn along its length; an arrowhead pops in over the last 10 %; deterministic small wobble at the vertices so it feels hand-drawn. Dashed for intended or future paths (a cross, a run), solid for what happened.
- **Ring**: perspective ellipse (ry = 0.36 r) under the feet, drawn clockwise, outer dashed ring rotating at 60 px/s; a vertical light beam while the player moves.
- **Draw order inside a freeze**: ring (who) → area or link (what happened) → label (the one-line finding), 0.3–0.6 s apart.
- **Slow motion**: source frames at 0.6–0.85×, neighbours cross-blended (no stutter).
- **Rewind**: the clip reversed in 0.6 s (ease-in-out), ±13 px horizontal jitter, four white tracking bars, a big ◀◀ and the word REWIND.
- **Trails**: in screen space keep only the last ~0.6 s (ball 0.24 s) — the camera pans, so long trails land in the wrong place.
- **Stamp** (e.g. a VAR decision): a framed card that drops from 1.7× to 1× with overshoot, slightly rotated, with a small flash — once per film.
- **Perspective flatten**: see Native moves 7.

## 7. Grade and image quality

- Footage: `hqdn3d=1.2:1.2:2.5:2.5` → lanczos to 1920×1080 (modern footage at most 1.5×) → `unsharp=5:5:0.55` → `eq=saturation=0.9:contrast=1.04:gamma=0.97` + slightly cool shadows; one grade for every clip; film grain 2 added once at the master (`mux.sh`).
- Broadcaster logos and URLs are covered by the packaging (bug and score bar placed exactly over them, present from frame 1), or kept outside split-screen windows — never by cropping past 1.5×.
- Prefer a broadcaster's native resolution over an "AI-upscaled" stream.

## 8. Sound palette

- **Layers**: English voice-over (one line per freeze, ≈2.5–3 s) → match sound (commentary + crowd at full level in live play; under freezes only a low-passed crowd bed, looped; the goal roar on the goal frame) → score → foley. Voice ducks everything else to 0.55.
- **Score**: sampled band (drum kit, electric bass, staccato trumpet and trombone, timpani, horn, cellos, glockenspiel), about 120 BPM. The groove restarts at the head of each played segment, so cuts don't need a global bar grid. **On a freeze the drums stop**: one brass stab + timpani + low thump + camera shutter, then only closed hi-hat — the music freezes with the picture. Goals: a big brass chord with crash and glockenspiel on the score-bar flip.
- **Foley**: marker squeak (2–5 kHz band-passed noise with flutter) for each line, pops for rings, a tick per landed label, whoosh on every wipe, tape-motor whine on a rewind, a stopwatch tick every 0.2 s, a thump for the stamp, a long whoosh and a timpani roll under the flatten.
- Mix limited before `mux.sh` normalises to −14 LUFS.

## 9. Native moves (and how the code does them)

1. **Freeze and draw** — a freeze segment = one source frame + flash + punch + desaturate + spotlight; overlays drawn by progress (`overlayAnalysis()`, `overlayG1()` in `demo/index.html`).
2. **Tracked ring** — hand keyframes of the feet point in source pixels every ~3–6 frames, linearly interpolated (`TRK`, `at()`); check them with `?dbg=1`, which paints every tracked point in magenta.
3. **Frame-counting stopwatch** — starts at the receiving frame and counts source frames ÷ fps; stops and turns yellow on the strike (`stopwatch()`).
4. **Score-bar flip on the goal frame**, one entry per goal (`GOALS`, `scoreAt()`, `bugScore()`).
5. **Packaging over watermarks** — corner bug and score bar positioned from the logo and URL coordinates, drawn from frame 1 (`bugTop()`, `bugScore()`).
6. **Dual-angle freeze** — two windows, each its own clip and frame range, both reaching their freeze frame on the same beat; overlays drawn in each window's source coordinates (`splitView()`, `overlayG2()`).
7. **Perspective flatten into a shot map** — for each shot, mark 6–8 known pitch points in its own frame (box and six-yard corners, where the penalty arc meets the box line; FIFA dimensions) and fit a ground-plane homography by least squares (`demo/tools/homography.py` reads `tools/pitch.json`, writes `assets/pitch.json`; residuals ≤ 6 px are fine). The strike frame is then drawn as a mesh of triangles in pitch coordinates (1.5 m cells), each vertex moving from its image position to its board position, each triangle affine-mapped (`drawTri()`); the picture fades out as the chalk board takes over, and the other shots' feet points, converted with their own frames' matrices, drop onto the same board (`shotMap()`). The broadcaster's URL is painted out of the source frame first, because the flatten drags it into the middle of the screen.
8. **Data card** — the counted numbers re-stated on a board page: label left, big yellow number right, red marker circle on the key one (`notes()`).
9. **Commentary transcript** — original-language words with timecodes and a translation, in a small box during live play; inaudible words become an ellipsis, never a guess (`transcript()`).

## 10. Material

1. **Ask the user first** whether they have their own footage (club or academy video, their own camera, a licensed broadcast clip), line-ups, event data or photos, and the rights to use them. Their material comes first.
2. **Where to look** (judge every file on its own page):
   - **Wikimedia Commons** (search "goal", the match, the player): many clips are cut from broadcasters' own YouTube uploads under CC BY. Fine: CC0, public domain, CC BY. Not used: CC BY-SA, "no known restrictions", unclear licences.
   - **A broadcaster's or club's own YouTube channel** when its video page says *Creative Commons Attribution license (reuse allowed)*: check that the channel is the rights holder's official, verified channel (not a re-upload or a fan mirror), save the evidence (channel id, verification, licence field, date checked), and download the native resolution, not an AI-upscaled stream. Third-party re-uploads, fan mirrors, colourised or "restored" versions are never used.
   - **Facts** (scores, minutes, how a goal was scored): the league's or broadcaster's own match page or video description, then established newspapers; quote them in `FACTS.md`. When sources disagree, use the official list and leave the disputed detail out.
   - Photos of players: Commons (CC BY / CC0); state the year when the photo isn't from the match.
3. **Before downloading, tell the user** what you will fetch, from where and under which licence. The finder copied into this style, `demo/tools/footage.py` (`search commons|archive|nasa`, `fetch`, `used`, `md`), logs licence, author, page and the seconds used into `SOURCES.jsonl` and writes `SOURCES.md`; `demo/tools/fetch_sources.sh` shows how a verified YouTube CC BY source is fetched with `uvx yt-dlp`. Wikimedia rate-limits bursts (HTTP 429): one request at a time.
4. **People on screen**: players, referees and staff in the event are fine; never slow down or freeze on an identifiable spectator.

## 11. Engine

Canvas 2D, one page: `window.render(t)` is async and deterministic, frames load on demand from JPEG sequences (one folder per clip, 90-frame cache). `timeline.json` (segments with clip and source frame range, voice lines) drives the page, `tools/mix.py` and `tools/cues.py`. `window.TEXTS(t)` reports the text that must be read, for `readcheck.mjs`. `core/render/video.mjs` renders at 30 fps.

## 12. Pitfalls

- **Wrong tracking points** are the biggest risk: reading coordinates off a scaled contact sheet is easily 20–50 px off. Read them on full-resolution crops with a pixel ruler, then check with `?dbg=1`.
- **Overlays not under the punch transform** slide off the players during a freeze.
- **Balls vanish**: long shots are a few pixels with motion blur; colour tracking loses them; frames where the ball is invisible are interpolated and the number says "≈".
- **Numbers the footage can't support** (ball speed, distance run) are not written. Distances only from a homography fitted to visible markings, each shot in its own frame (the camera zooms and pans between shots).
- **Packaging late by one frame** shows the logo: bugs never fade in over footage.
- **Split-screen windows sliding in** reveal what's outside them (a logo, a URL): clip each window to its slice in source coordinates, not only to the screen half.
- **Score state must match the moment**: before the 67th-minute goal it is 3–2, not 3–3.
- **Names in TTS**: spell them phonetically for the voice ("Zayits", "Saduk") and keep the real spelling in subtitles; record the ASR result for proper names in `lines.json` (`asr`).
- **Freeze labels echo the subtitle** and live only ~1 s; anything the viewer must read (scores, board rows, the data card) gets ≥ 2.5 s and goes into `TEXTS`.

## 13. Variation space

The agent decides per film: the sport (football, basketball pick-and-roll with screens drawn as bars, tennis rallies with landing zones, F1 overtakes with racing lines — anything with a wide camera that shows the whole play), the moments, the show's fictional name and colours (keeping the three roles), how many freezes.

- **Three structures:** chronological build-up to the deep breakdown (secondary moments get light treatments, the decisive one the full rewind-and-freeze); one moment taken apart from three angles; a "what went wrong" defensive breakdown ending on the space map.
- **Three openings:** the show sting into a match-record card; the goal frame frozen in the first second, then rewind; the stopwatch running over live play.
- **Three endings:** the top-down board that sums up the moments; the data card with one number circled; the hero shot slowed with the minute and name.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: news-package -->

# Broadcast News Package — Style Prompt

> A television newsroom's on-air package, built entirely in code: a sting that becomes the channel bug, a rundown of today's stories that opens and closes the bulletin, a lower-third strap that never leaves the bottom of the frame, and full-frame graphics (split-flap price boards, a line breaking a threshold, explainer maps, documents flying out of a city, quote cards, spec cards with proportion bars, stamps) that carry the facts. The style is the **package system plus its cutting rules**, not a drawing style. 16:9, a clean frame: no burned-in subtitles, no news crawl.
> References (grammar only): evening network news headline menus, financial-channel market graphics, European news channels' explainer maps, tech-desk spec cards. Never copy a broadcaster's logo, set, fonts, colours, music or idents, and never name them in the film.

## 1. Essence, and what it is not

1. **One package system, used consistently.** Every graphic is built from the same few parts: a brand plate (parallelogram), a tab in the accent colour, a paper strap, ink cards with an accent top edge, mono datelines, stamps. Viewers read the system before they read the words.
2. **The bulletin's order.** Sting → rundown ("today we have four stories") → item → item → … → back to the rundown, ticked off → sign-off. Each item opens with its category on the strap's tab and its date on the first graphic.
3. **One fact per screen.** A full-frame graphic states one thing: the price, the break, the two stocks, the place, the two letters, the quote, the verdict.
4. **The strap holds the headline.** One lower-third strap is on screen from the first story to the recap and changes its words with a vertical flip; the picture above it is free for the graphic.
5. **Clean panel.** No crawl, no burned-in subtitles; subtitles ship as a separate `.srt`. The frame is the graphic, the strap, the bug and a source line.

Not **Caption News** (that is captions-first social video: huge slammed captions are the lead, no rundown, no strap; here type is small and orderly and the graphics lead). Not **Data Storytelling** (one chart per beat, never a dashboard; the chart is an insert in a bulletin). Not a keynote: no centred title-and-bullets, no page turns. Not a studio show: no virtual set, no anchor, no fly-throughs — the package is flat graphics over ink.

## 2. Frame and layout (1920×1080)

| Zone | Position | Content |
|---|---|---|
| Content | x 96–1824, y 56–840 | the full-frame graphic; when a strap is up, nothing important below y 840 |
| Lower-third strap | tab x 96 y 856, 48 high; strap x 96 y 904, 1250×104, + 120 px ink end block | category tab (accent, ink text, Chinese + English), headline in Chinese 50 px + one English line 27 px |
| Source line | right-aligned at x 1836, y 950 / 978 | `SOURCE: …` mono 13 px + Chinese 16 px, 75 % opacity; English ≤ 36 characters or it slides under the strap's end block |
| Channel bug | top right, plate centre (1739, 86), 0.327 of the sting plate | the plate plus `AI NEWS` |
| Corner tag | top left x 96 y 56, 330×64 | `ILLUSTRATION / 示意 · AI 生成画面` on generated plates, `SCHEMATIC / 示意图` on schematic charts; flips in and out 0.2 s |

Content layers sit lower than a subtitled layout would put them (a 60–110 px downward shift) so the bottom strap does not leave an empty band above it. When you remove subtitles and the crawl, re-lay the page; never leave the space they used.

## 3. Package parts (specs)

| Part | Spec | Rules |
|---|---|---|
| Sting | 0–1.5 s | two accent slashes (0.04, 0.10 s) → the plate slams in with an overshoot, an impact ring and shake (0.16–0.42) → letters drop in one by one → wordmark and dateline open from the centre → a glint → the plate flies to the top right and **becomes the bug** while a vertical band wipes into the first shot. A hit within 0.4 s |
| Brand plate | parallelogram 520×180, accent gradient, ink and gold bars at the left, name in condensed 800 | the same object is the sting, the bug, the desk front and the end card |
| Rundown | left: date block (big numerals, month, week); right: three rows, 1024×140, number block in accent | rows flip in vertically on the beat (back ease) with a glint; at the close the same object returns and each row is ticked |
| Lower-third strap | see §2 | enters with the first story, flips (new words up from below, old up and out, 0.32 s; the tab flashes white when the category changes), leaves with a slide when the recap starts. A **profile** version (tab `人物 PROFILE`) names a speaker |
| Split-flap board | tiles 220×130, top and bottom halves clipped separately | old value and new value on the same board, so the change reads in one look; ×2 / +x % called out to the right |
| Threshold chart | line from the peak, the threshold as a dashed gold line | the line head advances one trading day per step; the last step crosses the threshold in accent with a shake and a ring; the readout panel slides in after; axes show only what the data supports |
| Bars | grow from a zero line downward for losses, values roll | a reference line at the shared threshold plus a badge |
| Explainer map | the same projection, one long take | members light in order of distance from the city; the city label, the institution label with leader, a stamp; the camera pushes, then pans to make room |
| Documents | 380×490 paper, ink header | fly out of the city dot on an arc (0.5 s, scale 0.08 → 1, rotation settles); check boxes tick on the voice's key words |
| Quote card | ink background with the package's light streaks, a large accent quotation mark lands first, lines push up one by one (0.18 s apart), then the Chinese gist, a gold rule, name, occasion and date | the official wording, in the language it was said; never paraphrase inside quotation marks; an underline sweeps the key word as the voice says it |
| Spec card | eyebrow (source · date), the product name pushed up from a mask, a category stamp, proportion bars on one scale (the whole vs the part, values rolling), a percentage badge, a context chip; a second group on the right for the hardware or the place, filling cell by cell, joined by a bracket to its total | one scale for every bar, so the proportion is true; every number from the source page |
| Stamps | accent fill or ink with a double accent frame, −6° to −10° | land from 1.9× in 0.16 s with an expanding ellipse; one per story at most |
| Transitions | vertical band wipe (accent 84 px + ink 5 px + gold 14 px edge, 0.3 s) between stories and programme parts; hard cut + timpani inside a story; slanted wipe into the end card | nothing else: no dissolves, no 3D flips, no page turns, no fly-throughs. **The package layer travels with its picture**: under a wipe each side draws its own strap words, tab, source line and corner tag (old state on the old side, new state on the new side), so the band brushes the headline over; on a hard cut they change on the same frame. Strap words never flip or overlap. The incoming picture's entry animation starts under the band, so its first revealed frame already has content |

## 4. Colour

| Role | Value | Use |
|---|---|---|
| ink | `#121417` | backgrounds, panels, strap end block |
| ink2 / ink3 | `#1B1E23` / `#22262C` | cards, land on maps |
| accent (lemon) | `#F2CF1D` (light `#F8DE4A`, dark `#D8B30C`) | plate, tabs, band wipe, bars, stamps, the line that breaks |
| gold | `#D4B064` | thresholds, datelines, source lines, light fins, badges |
| paper | `#F4F1E8` | strap, documents, the chart line |
| breaking | `#FE6B3D` | only for BREAKING and LIVE. A weekly round-up has neither, so it never appears |

Structure to keep when you change the brand: one accent + one gold-like secondary + paper + ink, and a reserved alarm colour. Ink text on the accent; on paper, English secondary lines in a dark olive (`#6E5A1E`) because gold is too weak there.

## 5. Type

- Chinese: Noto Sans SC 900 (headlines, strap) / 700 (labels).
- Latin: Barlow Condensed 800 (numbers, names, the plate), 600 (secondary lines, quotes), 600 italic (the end-card English title).
- Mono: IBM Plex Mono 500 for datelines, sources, axis labels, all caps with 1–4 px tracking.
- All OFL, subset from Google Fonts by `demo/tools/fonts.sh` (the character list is read from `main.js`; delete `fonts/*.woff2` after a text change). No handwriting faces in this style.
- Every label is bilingual on one line each (Chinese first, English smaller); never wrap.

## 6. Picture layer and grade

- When there is no footage, the picture layer is data graphics drawn in code plus, at most, a few **illustrative plates** (generated or stock), each tagged `ILLUSTRATION` for as long as it is on screen. They set a mood (a server room behind a model launch, a wafer behind chip stocks); they never stand in for the event, the place or the people.
- One grade for every plate: greyscale → auto black/white points (0.5 / 99.6 percentile) → γ 1.05 → 35 % S-curve → black 8, white 232 → duotone `#0E1013` → `#ECE7D8` (`tools/prep.py: grade()`), plus a left-dark ink gradient for type, a 50–55 % vignette and 7 % overlay grain cycling through six tiles. Graphics and the package are never grained.
- Real footage, if you have it, takes the same grade path; modern footage ≤ 1.5× scale, archive ≤ 2.5× after deblocking; crop out station logos.

## 7. Editing grammar


<!-- END STYLE PAGE -->
