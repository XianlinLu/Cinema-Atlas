# Complete style specifications 04


<!-- STYLE: city-symphony -->

| Score texture | Cut length | Frames | Use |
|---|---|---|---|
| Opening hit + eighth-note arpeggio | 2 bars → 1 bar | 120 → 60 | the opening still, the first single-camera time-lapse |
| Eighths | 2 beats → 1 beat | 30 → 15 | dawn, match cuts |
| Triplets against eighths (3:2) | 1 beat → ½ beat | 15 → 7/8 alternating | morning, the montage of streets |
| Sixteenths, full ensemble | grid cells light every 1–2 frames; cells re-cut every sixteenth | 1–4 | the grid |
| Arpeggios stop, one long chord | 3–4 s, one or two shots | 90–120 | the brake: the slowed thing, the archive split |
| Sixteenths + triplets + horns | ½ beat → 4 frames → 2 frames | 7 → 4 → 2 | dusk to night, the reverse flashback |
| Dry cut of the whole ensemble, reverb left ringing | hard cut to black on the bar line | — | the hard stop |

Rules:

- **Cuts land on beats.** All cut times come from one function, `bar(n, beat)` in `tools/timeline.py`; shot lengths are never typed in seconds. The music is rendered from the same file.
- **One long single-camera time-lapse is the clock.** It returns three or four times (night → dawn, noon clouds, a one-second nightfall, a day/night flicker), always from the same position, so the viewer knows the time without a caption.
- **Density follows the score.** The editor never cuts faster than the current subdivision, and the slowest picture sits under the place where the arpeggios stop.
- **Shape match cuts** on the beat: clock → clock, arch → arch, grid of streets → grid of cells. A small-to-large punch-in on the same shape is allowed.
- **The grid** is the split screen of this style: 1×2 → 2×2 → 3×3 → 4×4, one stage per half bar or bar, the new cells lighting up in a scattered order over the previous stage within 0.3 s (never back to black), gutters 6 px black; in the last beat the cells re-cut on every sixteenth.
- **Counterpoint split**: two halves, archive left, today right, the same kind of place or shape; the gutter grows from the centre in 8 frames.
- **Day/night flicker**: the same camera, a noon frame and a night frame alternating every 2 frames; a pair of same-position photographs alternating every 2 frames.
- **Reverse flashback**: in the last bar before the hard stop, earlier shots return in reverse order, 4 frames each, then 2 frames each.
- Transitions: hard cuts only, plus the hard cut to black. No dissolves except fades from black for the page and the end card.

## 7. Sound palette

- **Music only.** No narrator, no source sound (the footage soundtracks are other people's music), no sound effects. A narrator would turn watching into listening and would fight the score for the structure; that is why the style has none. If a voice is ever required, one short line at the very start or end, never over the cuts.
- Orchestration (sampled, CC0 — `core/audio/sampler.py`): pipe organ (full and soft stops, pedal), winds staccato (flute, clarinet), strings (spiccato cellos and violins, sustained cellos, violins, double bass), horn pair for the last two bars, concert bass drum on section downbeats, suspended-cymbal crescendos into the hits, glockenspiel only for numbers locking.
- Writing: arpeggios over a one-chord-per-bar progression; additive layering (eighths → triplets over eighths → sixteenths); the *break* is all arpeggios stopping at once into one held chord (maj7 or 9th); the return is a full-organ hit; the hard stop is a dry cut of every instrument in 15 ms with the reverb tail left ringing; the coda is one soft chord that does not resolve, with the opening figure returning in quarter notes under the end card.
- Reverb: `S.room(size .7, mix .28)` for the body, `size .78, mix .36` for the coda. Master to −14 LUFS / −1.2 dBTP with `core/render/mux.sh` (grain 0: the grain is already in the picture).

## 8. Native moves (and how they are built)

| Move | Code |
|---|---|
| **Light river** | `tools/prep.py`: integrate the speed curve to source time; each output frame averages the source frames in its window (cap `blend`). Speed 40× / blend 30 at night, 37.5× / 24 for clouds, 75× / 30 for a one-second nightfall. |
| **Speed ramp** | `speed=[(t, v), …]` keyframes, smoothstep between them, same integrator. |
| **Brake into slow motion** | ramp 2.2× → 0.3× with `interp=3` (ffmpeg `minterpolate` mci, bidir) for soft subjects; `mix=True` (crossfade of the two nearest frames) for thin lines such as cables, where motion compensation tears. |
| **Crowd → tracks** (people as data) | `Trails` in `tools/render.py`: background = per-pixel median of the whole fixed-camera shot; blobs that differ by > 22/255 (scipy `ndimage.label`, area 8–900 px at half size) are people; each centroid joins the nearest one from the previous frame (< 70 px) with a 2 px line; lines fade × 0.9 per frame; the plate is darkened and desaturated as the tracks appear (0.15 → 0.55 s). Fixed cameras only. |
| **Traffic → light** | a static or slowly drifting top-down aerial at 5× with full frame blending. |
| **Grid** | `grid_plate()`: pool clips of 30 frames held in memory at 960×540; stages from `GRID_STAGES`; light-up order scattered; last beat re-cuts cells every sixteenth. |
| **Counterpoint split** | `split_plate()`: archive 4:3 centre 960 px | today centre 960 px, 6 px gutter grown from the centre. |
| **Day/night flicker** | two 15-frame clips from the same camera (noon, night), alternating every 2 frames. |
| **Photo that moves** | a same-position photo pair alternating every 2 frames. |
| **Number lock** | `lock_digits()`: one digit locks per sixteenth, the others roll; `counter()`: ease-out count-up; music adds one glockenspiel note per lock. |
| **Day ring** | a thin 24-hour ring bottom-right with a sodium hand and a 3-hour arc: it runs with the film's day, **freezes and dims during the brake**, and **spins backwards during the reverse flashback**. It is a graphic, not a clock reading. |
| **Reading light on a page** | scanned page, 16:9 window pushed 1.06 → 1.56 page widths, side light (bright top-left), paper tint (1, .93, .80), a Gaussian band (σ 95–140 px) over the quoted line growing to +38 %. |
| **Hard stop** | picture cuts to black on the bar line; the music's dry signal is cut in 15 ms on the same frame; only reverb remains. |

## 9. Pitfalls of the medium

- **Watermarks and slates hidden in CC footage**: corner logos (scale from the centre until they leave frame, within 1.5×), opening thank-you cards, end-card music credits, title text over the first shots. Check a 1-second contact sheet (`tools/secsheet.py`) of every source before choosing in-points.
- **Hidden cuts inside sources.** Hyperlapse reels hide 2–3-frame jump cuts and whip transitions; frame blending across a cut makes ghosts. Scan with `ffmpeg … select='gt(scene,0.25)',showinfo` and keep every clip's source window inside one shot.
- **Too much blending** turns noon clouds into grey mush: about 40 % shutter (24 of 60 frames) looks better than 100 %.
- **Grey-world balance kills night**: it washes sodium light to white. Strength 0 for night shots.
- **Tracking needs a fixed camera.** A drifting drone flags every building as motion. Use a median background only on tripod shots; for moving aerials use blending instead.
- **Motion-compensated slow motion tears thin lines** (cables, rails, text): use the crossfade mode there.
- **Text over bright sky** disappears: put number cards over the dark half of the frame or add the soft darkening; never a box.
- **A slow face is not a free subject.** Do not make an identifiable ordinary person the slowed or close-up hero. Slow a thing; show people as crowds, tracks or ghosts. Public figures and people in news events are a different case.
- **Numbers drift.** Official pages update; quote the page and the year, keep the quote in `FACTS.md`, and recheck before the last render. Prefer one clean figure over a range.
- **CC BY credits are long.** Each one needs author, full title and licence on the end card. Treat them as fine print (16 px, 29 px line pitch, the licence and changes on one header line) and keep the end card short (4–5 s); a 10 s card of text on black loses the audience. The film's last moving shot runs on under the card, darkened.
- **Don't end on dead black.** After the hard stop, the coda is a page (≈1 s), then the quote laid over one last moving city shot (≈4 s, just long enough to pass `readcheck`), then the end card over the same shot.
- Commons rate-limits (HTTP 429): search and download serially with back-off (`tools/s.sh`, `tools/f.sh`); for long 4K files download only the needed excerpt (`tools/seg.py`) or the 1080p transcode.

## 10. Footage: where it comes from

1. **Ask the user first** whether they have their own footage, photographs, documents or data for the place: their own time-lapses, a phone hyperlapse, family photos, a city's open data. Their material comes first.
2. If not, search these sources (all searchable with `demo/tools/footage.py`, which records title, author, licence and page in `SOURCES.jsonl` and writes `SOURCES.md`):
   - **Wikimedia Commons** — modern time-lapse, aerial and slow-motion footage under CC BY / CC0, photographs (for example the Carol M. Highsmith Archive, dedicated to the public domain), scans of old maps and books. Check the licence on each file page. Many videos are YouTube or Vimeo imports: use one only when its page carries a passed review (YouTubeReview / VimeoReview / LicenseReview / Flickrreview with a reviewer and a date) or the author's own source page still shows the licence. A pending review is not enough: a channel can later switch to the standard licence and claim the footage through Content ID.
   - **Library of Congress** (loc.gov, also mirrored on Commons) — archive films published in the US before 1931 are public domain; a rights statement of "no known restrictions" alone is **not** enough: you need the publication date or another public-domain basis.
   - **NASA** (images.nasa.gov, ISS crew photographs) — public domain; the night photos of cities from orbit make a strong opening.
   - **Internet Archive** — scanned books and documents marked NOT_IN_COPYRIGHT with a pre-1931 publication date; take the line you quote from the scan, not from a modern edition.
   - **National archives** (US National Archives, other governments' open archives) — check each country's terms.
   - Licences allowed: public domain, CC0, CC BY. Not allowed: CC BY-SA, "no known restrictions" without a basis, YouTube mirrors, unknown sources, restored or colourised archive copies.
3. **Before downloading, tell the user** what you will download, from where, under which licence, and how it will be credited.

Data for number cards comes from official pages (census, transport department, the place's own statistics); write the claim, URL and quoted wording into `FACTS.md`.

Recipe for another place: one single-camera time-lapse of ≥ 12 hours (the clock); 10–15 ground time-lapses and hyperlapses (streets, stations, bridges); 2–4 aerials, one of them top-down at night; one slow-motion shot of a fragile thing; one fixed-camera crowd shot for tracks; one archive film of the same kind of place; one night photograph from orbit or above; a same-position photo pair; three official numbers; one public-domain sentence written about the place.

## 11. Variation space

- Place: any city, port, airport, market, campus, factory, a river over a year (the clock becomes a season).
- Length: 30–90 s; one brake at least; one hard stop always.
- Score: organ/winds/strings is the default; a choir, a piano ensemble or analogue synth arpeggios also work if the writing stays additive and the break stays a sudden held chord.
- Tempo 96–132 BPM; at 30 fps prefer tempos whose beat is a whole number of frames (120: 15, 100: 18, 112.5: 16).
- Grid sizes and the counterpoint pair change with the material (archive vs today, day vs night, two cities).
- Number cards: 2–4 at most; the day ring may be dropped for non-daily structures.
- Fixed: footage only, the frame-blended light, cuts on the beat, the brake, few words, one quote, the hard stop, the release-print grade.

See [`DEMO.md`](DEMO.md) for the example film.

<!-- STYLE: visual-investigation -->

# Visual Investigation — Style Prompt

> A cold investigation desk: footage, photographs, documents, sound and maps from one real event, laid out on one shared clock so they check each other. The clock lives inside the picture — timestamps on the evidence, a playhead on a data chart, a stopwatch over the decisive seconds; frozen frames are circled and magnified; quotes are highlighted on the page they come from; a plan shows where cameras stood and where they looked; what is known and what is not are kept apart; at the end every piece of evidence is pulled into one map.
> References (grammar only): newspaper visual-investigation videos, forensic-architecture reconstructions, broadcast verification units. Never copy them, quote their names or use their branding.

## 1. Essence, and what it is not

1. **Sources meet at one moment.** The payoff of every section is two or more independent sources (a frame, a photo, a testimony, a report line, a sound) pointing at the same place or the same second. Cut points are sync points.
2. **One clock, read in the picture.** Time is carried by large readouts that belong to the layout: the timestamp on each telegram card, a playhead with its clock on the data chart, a `T+xx.x` stopwatch over the decisive seconds, a frozen "32 s". The scale changes with the story (hours → minutes → seconds → days) at section cuts. A permanent timeline band under every shot is **optional and usually wrong**: it eats the bottom of the frame, adds a layer of small labels and goes empty once the story leaves the clock.
3. **One finding per layout.** Each section says one thing; a heading is part of the layout, never a page header.
4. **Uncertainty is drawn, not apologised for.** `≈`, *inferred*, *schematic*, dashed boxes. Known and unknown are separate columns. A source that does not cover a stretch simply is not on screen yet (it lights up late in its column); never an empty "no footage" box, which reads as a broken render.
5. **Restraint.** Real disasters and real people: no slow motion of the catastrophe, no music that tells you to feel; fire only inside evidence frames; casualties as counted dots and numbers.

Not **Satellite Briefing** (no orbital imagery, no zoom from space). Not **Archive Light Table** (no paper on glass, loupes or hands: documents are flat evidence frames). Not **Halftone Dossier** (no print texture, stamps or collage). Not a newsreel package (no channel bug, ticker or anchor voice). Not a keynote: no centred title slides, no page turns.

## 2. Materials & rendering

- **Three kinds of source at least**: moving image (newsreel, CCTV, phone video, launch camera), documents (testimony, memo, telegram/teletype, report page), photographs. Add sound (original commentary, radio, recordings), data (weather, telemetry, counts) and maps whenever they exist.
- **Documents**: a scanned page is shown as a strip or a page, never re-drawn; only the decisive line is highlighted (red, `multiply`, α ≈ 0.6, wiped left to right). Text that exists only as a transcription (a report, radiograms) is re-typeset by code and labelled as a transcription.
- **Archival picture pipeline** (pre-1950 film, max ≈ 2.5×): deinterlace (`bwdif=0`) → crop borders → deblock (`hqdn3d=2:2:3:3`) → lanczos upscale → light unsharp (`5:5:0.5`) → greyscale; one grain for everything. Modern footage: ≤ 1.5×. Never colourised or "restored" copies.
- **One grade** (canvas `ctx.filter`): footage and photos `grayscale(1) contrast(1.22) brightness(0.94)`; paper `grayscale(1) contrast(1.05) brightness(0.86)` (white pages pressed to light grey); maps greyscale, inverted, `brightness(.62)` so they read as dark line drawings.
- **One grain**: six 256² Gaussian tiles rotated per frame, `overlay`, α 0.22 on footage/photos, 0.10 on paper. Grain only on sources, never on type or lines (`mux.sh … 0`).
- **Drawn evidence** (plan, side schematic, charts, dot matrix) is thin line work on the panel colour, marked *schematic* when it is not measured.
- Remove channel bugs, watermarks and the source's own title cards; never generate an image to stand in for a historical one.

## 3. Colour logic

| Use | Value |
|---|---|
| Ground | `#0B0C0E` |
| Panels | `#141619` |
| Hairlines, frames | `#2E3238` |
| Text | `#ECEAE4` |
| Secondary text | `#8B9097` |
| Ticks, *uncertain* | `#4A4F57` |
| **The one accent: here / now / match** | `#FF4A2E` |
| Paper cards (typeset telegrams) | `#E4E0D4` with ink `#1D1D1B` |

Sources are greyscale; red is the only colour and it only ever points: circles, the chart playhead, sync lines, highlights, ✓ badges (a drawn tick in a red box, no words), the zone everything converges on, the *unresolved* column, a strike-through on a wrong claim.

## 4. Type & subtitles

- Chinese headings and findings: Noto Sans SC 700 (30–124 px). Tags, timecodes and ticks: IBM Plex Mono 400/600. Quotes: Source Serif 4 Italic for the original wording, Noto Serif SC 500 for a translation underneath in the secondary colour (only when the subtitles don't already say it). All OFL, subset to the words on screen.
- **Few words per frame.** Each frame keeps only what this beat needs: the main readout or heading, the quoted original (the highlighted line), and one short source tag per piece of evidence. No eyebrow labels, no English twin under every Chinese label, no archive numbers, dates or "estimate / schematic / not to scale" footnotes unless the beat is about them, nothing the subtitle is saying at the same moment.
- **Source tag**: a 6×12 chip + `type · source` in mono, ≤ about 12 characters (`照片 · Pasquarella`, `FBI 电传 · 1937-05-08`), sitting just above its frame. Full credits go on the end card, not on the panels.
- **Lower third**: a red bar + place name (36 px bold) + one mono line (place code).
- **Subtitles** (bilingual films): at the bottom of the frame (Chinese baseline y ≈ 984, English y ≈ 1022): Chinese 34 px bold over English 23 px, centred, 10 px black shadow; **one line per language**, measured in the page against 1,500 px; a long sentence becomes two cues. Original sound gets subtitles too, marked `【原声】` / `[1937 newsreel]`.
- **Reading time**: every key text stays still and whole for CJK ÷ 4.5 + other ÷ 15 + 1.5 s (`readcheck.mjs`); verdict and comparison frames hold ≥ 2.5 s with every item fully in frame. Counters (timecode readouts, the stopwatch) and tick labels are exempt.

## 5. Motion quality

- 30 fps. Elements **cut in** (≤ 0.1 s opacity) with a 3–4-frame white flash, as if pulled from the evidence locker; nothing flies, bounces or scale-pops.
- Only things that are *drawn* are progressive: circles drawn clockwise in 0.5 s (ease-out cubic), leaders and links 0.4–0.8 s, plans stroke by stroke, highlights wiped, typewriter text for telegrams.
- Inside a frame: a slow push (≤ 1.9× on a map, ≤ 1.06× on a photo) is allowed; the "camera" itself never moves. Layouts change on cuts.
- The event clock (chart playhead, stopwatch) eases between keyframes and moves at constant speed inside a timed run (each tick = one real second).
- Scale changes (minutes → seconds → days) happen on section cuts, carried by the readout changing form (clock → `T+` stopwatch → date), not by a zooming band.
- Something changes at least every second; holds are for verdicts only.

## 6. Shot & layout grammar


<!-- END STYLE PAGE -->
