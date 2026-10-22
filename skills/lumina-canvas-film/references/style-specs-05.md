# Complete style specifications 05


<!-- STYLE: visual-investigation -->

- 1920×1080, 60 px margins; content y 60–900, subtitles below it (y ≈ 950–1030). Layouts use the full height; no strip is reserved for a timeline. When a section has no subtitle, centre its content vertically.
- Panels are hard-edged rectangles with 1 px frames; footage panels keep the source's aspect.
- Typical layouts: **map → plan** (left) with a reference photo and a footage panel (right); **one big statement + one quote + one wide schematic**; **five-source board** (three evidence frames on top, sound and report below, schematic right, red links converging); **three-column sync grid** (report / photo / video under one stopwatch, each column lighting up when its source begins); **document strip + two-column verdict**; **claim card + fact-check card + dot matrix**; **evidence map** (plan, broken-axis mini timeline, schematic, thumbnails with links).
- Avoid centred layouts, page headers and slide-like page turns. Transitions are hard cuts on a 0.5 s grid, white flashes and the rewind; no dissolves.

## 7. Sound palette

1. **Bed**: low D held by contrabass and cellos; a filtered room tone about 30 dB under the voice.
2. **Clockwork**: a pendulum tick every 0.5 s in the minute-scale sections, louder in the waiting minutes; in a timed run one tick per **event** second (accent every 5) — the audible stopwatch.
3. **Harmony**: a quiet pizzicato ostinato in eighths (Dm – B♭ – Gm – A) under the slow sections; tremolo minor-second clusters for tension; slow sustained chords for the verdict columns; a resolving D minor add9 with vibraphone for the evidence map.
4. **Foley** (procedural): paper for documents, a shutter for photos, Morse "dits" and keystrokes for telegrams, teletype chatter, a rewind sweep, pencil scratches for plans, one deep thump for the moment of impact — then near-silence.
5. **Original sound** (archival commentary, radio, recorded sound): band-passed 180 Hz–5.5 kHz with sparse crackle, shown as a waveform with a red play-line and word-by-word lighting; music ducks −12 dB under it. Original sound and score alternate; never both loud.
6. **Voice**: calm and flat (ours: Kokoro `am_michael`); music ducks about −9 dB under it; −14 LUFS, true peak ≤ −1.2 dB.

## 8. Native moves (and how to code them)

- **Freeze, circle, magnify.** Freeze a frame with a white flash; draw a 2.5 px red circle clockwise; at 60 % a leader and a bold label appear; a ×2 loupe opens beside it, cropped from the same source pixels (never beyond 1 source px per screen px). *Fits:* a licence plate in CCTV; a crack in a weld.
- **Hard sync point.** Pick one instant every source can recognise (impact, flash, a public clock, a gunshot peak) and align each source to it. A source that starts late just appears late; if the gap matters, say it in the voice or a subtitle. *Fits:* which phone started filming first; when the launch camera lost the vehicle.
- **Three-column sync grid.** Document / photo / video side by side under one big stopwatch; each column cuts in (white flash) at the moment its source begins, so the grid fills left to right as the clock runs; freeze on the sync point with a red dashed line across the pictures. *Fits:* two dashcams and a police log.
- **Readouts change scale.** The time readout changes form at each section cut — card timestamps and a chart playhead (minutes), a `T+` stopwatch (seconds), dates (days) — as the story narrows or widens. *Optional:* a bottom timeline band with tracks per source kind, only for a film that stays on one clock throughout; keep it free of labels and drop it when the clock stops. *Fits:* a market crash from the week to the minute.
- **Rewind cold open.** Start on the decisive frozen frame, slam the other sources into a grid, sweep a sync line, then rewind (footage playing backwards, scan lines) to the start. *Fits:* any reconstruction.
- **Telegrams on the clock.** Typeset radiograms / messages land at their timestamps with Morse and keystrokes; red dashed leaders tie each card to a pin at its time on the data chart's axis. *Fits:* chat logs, ATC calls, emails.
- **Data chart with a playhead.** A chart (wind, speed, temperature) across the lower part of the frame with a time axis, event bands (storm, outage) labelled with one word, the message pins, and a red playhead carrying the clock. *Fits:* power-grid load before a blackout.
- **Map → plan.** A real survey map pushes in to the site, then cuts to a measured plan with the subject's position, a bearing, a distance ring, a camera point and an inferred view cone; the map stays as a locator inset. *Fits:* where each witness stood.
- **Evidence → model links.** Every circle in every source sends a red dashed link to the same zone of one schematic; ✓ badges land 0.12 s apart with small mallet notes. *Fits:* which room a fire started in.
- **Then vs. record.** Play a period claim as original sound, then a fact-check card; strike through the wrong words in the claim. *Fits:* a press release against the filed numbers.
- **Known / unresolved.** Two columns, ticked vs. dashed boxes, every item held whole for ≥ 2.5 s, one source tag for the board. *Fits:* any inquiry's conclusion.
- **Dots for people.** One dot per person; the dead become red open rings one by one; a single large number. *Fits:* passengers, workers, victims of any event.
- **Evidence map.** Plan, broken-axis mini timeline, schematic and thumbnails of every source, all links converging; the poster frame. *Fits:* the end of any investigation.

## 9. Pitfalls

- **Inference passed off as fact.** Camera positions, photo times and offsets need `≈ / inferred / unlocated` on screen and in `FACTS.md`.
- **Early reports as facts.** The first-night memo and the period newsreel often disagree with the final report; use them as images or as claims to check, never as the source of a number.
- **Faking a multi-camera event.** With one licensable film, do not borrow clips of unclear origin; cross-check film + photos + documents + sound instead. The structure still holds.
- **Seams in "continuous" shots.** An exposure jump or splice breaks timing; time durations from the official record and state the alignment error.
- **Time zones and clocks.** Old reports may use standard time while the place ran on daylight time; pick one and state it once on screen (`18:25:00 EST` on the first readout).
- **Too much at once.** One layout, one finding; at most five sources on a board, and the subtitle never repeats the heading word for word.
- **Too many words on screen.** Keep only what this beat needs (main readout or heading, the highlighted original, one short tag per source). Eyebrows, English twins of every label, archive numbers, footnotes and translations the subtitle already gives turn the frame into noise.
- **Empty placeholder boxes for missing material.** A grey "no footage" or "waiting for photo" panel looks like a render error. Fill the slot with real material, change the layout, or let the source appear when it starts.
- **A strip reserved at the bottom** (timeline band, caption rail) leaves an empty band when it has nothing to show. Content runs to y ≈ 900; nothing lives in the subtitle area (y ≈ 950–1030).
- **Catastrophe as spectacle.** No slow motion of fire or impact, no full-screen flames, no sound effects on deaths.

## 10. Footage (素材)

1. **Ask the user first.** Before searching: does the user have their own footage, photos, documents, recordings or data (dashcam files, a report PDF, a spreadsheet of readings)? Their own material always comes first.
2. **Where to look, and how to judge the licence.** Use `demo/tools/footage.py` (copy it into the project): `search archive|commons|nasa`, `files`, `fetch` (records licence, author and page into `SOURCES.jsonl`), `used`, `md` (writes `SOURCES.md`).
   - **Internet Archive**: the item's `licenseurl` and collection. The NARA-donated Universal Newsreels (1929–1967) are public domain; other newsreel companies (Hearst, Pathé, Movietone, Paramount) are not, even when uploaders tag them PD. "stock footage" and YouTube-ripped items: skip.
   - **Wikimedia Commons**: read the file page — author, source, licence template. U.S. federal work (Navy, NASA, NARA, NOAA, USGS) = public domain. PD claims resting on "not renewed" agency photos (AP, INS, Wide World): treat as uncertain and skip. Download big files through the API thumbnail URL (3840 px) to avoid 429s.
   - **NASA** (images.nasa.gov): public domain except marked third-party items and logos.
   - **Library of Congress / national archives**: read each item's rights statement; "no known restrictions" is **not** a licence — skip it.
   - **USGS The National Map**: historical topographic maps as PDF (public domain); render the area you need with `pdftoppm -r 300 -x … -y … -W … -H …`.
   - **Government reports and FBI files**: U.S. federal works are public domain; quote them, typeset transcriptions, show scans only as evidence frames.
   - Allowed: public domain, CC0, CC BY (credited in full on the end card). Not allowed: CC BY-SA, "no known restrictions", unclear origin, colourised or restored copies.
3. **Tell the user before downloading**: what (title, length or pages), from where (page URL) and under which licence; keep `raw/` under about 1.5 GB.

## 11. Facts

Keep `FACTS.md` (claim on screen or in the voice → source URL → quoted wording), list every inference separately, and check the final script and subtitles against it before the last render.

## 12. Engine

- One Canvas-2D page (`demo/index.html`), `window.render(t)` deterministic, `window.TEXTS(t)` for `readcheck.mjs` (key texts only; counters exempt), `window.SUBCHECK()` for the one-line subtitle check; all timing in `demo/film.json` (sections, voice starts, original-sound clips, subtitles), shared by the page, the mix (`demo/audio/mix.py`) and the subtitles (`demo/tools/cues.py`).
- Reusable parts in the page: `plate()` (grade + grain + flash), `ring()` (circle + leader label), `cover()` (fill a panel without stretching, returns a source → screen map for circles), `badge()`, `wave()` (waveform with play-line), `playhead()` (event-clock keyframes shared with the mix), `planPanel()`, `schematic()` (16-cell side view with zone/flutter), `push()`.
- Prep: `demo/tools/prep.sh` (ffmpeg + pdftoppm + PIL), `demo/tools/wave.py` (waveform peaks), `demo/tools/fonts.py` (OFL subsets). Checks: `demo/tools/subcheck.mjs`, `demo/tools/final_asr.py` (speech check on the finished film, per line).

## 13. Variation space

The agent decides per film: the event, the sources, the sync point, which time scales the clock passes through, the layouts, the opening and the ending.

- **Three structures:** a cold open on the decisive frame, then rewind and rebuild; one question ("where did it start?") answered source by source; a strict clock (T−10 min → T+1 h) with findings dropping in where they happen.
- **Three sync points:** an impact or flash frame; a sound peak heard in several recordings; a public clock or broadcast time signal.
- **Three endings:** the evidence map; the known/unresolved board left on screen; back to the opening frame, now fully annotated.
- **Other subjects:** a traffic collision (dashcams, CCTV, police report), a protest (phone videos, photos, statements), a disputed call in sport (camera angles, rulebook), a launch failure (tracking cameras, telemetry, accident report).

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: kino-montage -->

# Constructivist Montage — Style Prompt

> Real archive footage, photographs and documents, printed as one ink-and-paper poster with a single red, and cut on a machine beat. Diagonal bands carry the type; windows cut along the axis hold the film; people are scissored out of photographs and stacked into structures; numbers count, documents are marked in red, and two images collide to make a third idea.
> References (grammar only): Soviet montage cinema of the 1920s (city symphonies with split screens, counting and machine rhythm; "intellectual" montage where A + B yields a concept), constructivist posters and photomontage (red / black / paper, steep diagonals, photo cut-outs with geometric blocks, type as structure). Never copy their shots, layouts, slogans or lettering, and never name them in the film.

## 1. Essence, and what it is not

1. **Evidence, recut.** Every picture is real material (archive film, photographs, documents) about the actual subject. The film's argument comes from how they are cut and set, not from illustration.
2. **One printed sheet.** All material is converted to the same two-tone print (warm ink → paper); red is the only colour and is laid on top as a printed element.
3. **The beat is the editor.** Cuts, slams, wipes and counts sit on a 120 BPM grid (or the score's tempo); sections accelerate by halving shot length.
4. **Type is structure.** Words and numbers are beams: on a −18° band, as solid blocks, stacked vertically. Never floating captions.
5. **The collective over the individual.** Crowds, hands, machines and many small figures; a single face is never the protagonist.

Not **Data Storytelling** or a keynote: no centred headline with bullets, no slide transitions, no header bars; data appears as marked documents, counters and measured bars inside the composition. Not **Swiss Motion Graphics**: asymmetric, diagonal, no grid of white space, no thin rules as decoration. Not **Art Deco** or **60s Spy Titles**: no gold, no fine lines, no jazz. Not a museum slideshow: archive material is never shown "as is" in a neutral frame; it is cut, windowed, stacked and counted.

## 2. Materials & rendering

- **Four kinds of element only**: **bands** (red or ink, along the axis), **windows** (rectangles or parallelograms holding film or photographs), **cut-outs** (people scissored from photographs with a paper-white border), **type blocks**. Plus one paper-fibre texture over everything.
- **The print grade** (one function for film, photos and documents): luminance → percentile stretch (film: one pair of percentiles per clip, so it never pumps; 0.7 / 99.5; photos 0.8 / 99.4) → S-curve `x + s·(x−0.5)·(1−|2x−1|)·2`, s = 0.32 (documents 0.18, they keep their paper) → map to ink→paper: `rgb = INK + (PAPER − INK)·g`. Archive film keeps a ±2.5 % per-frame flicker inside its window (`hash(frame)`), photographs and documents do not.
- **Cut-outs**: a person-segmentation model (u2net_human_seg via onnxruntime) → threshold 0.5 → median filter → largest component → 7 px paper border dilated outside the mask. The border is the medium's own look and hides the model's edge errors. Group photos rarely segment cleanly: use them whole in windows.
- **Documents**: scans at full resolution, never retyped. They are marked: a red highlighter bar in `multiply` over the exact sentence, a hand-drawn red ellipse round a heading, a red circle on a map. Drawings on a document (a chart, a map) may be lifted off the page and reused, keyed from their paper (`alpha = (205 − luminance) / 90`).
- **Resolution ceiling**: archive film ≤ 2.5× its source pixels on screen, modern footage ≤ 1.5×, photos ≥ 1 source px per screen px where possible. Prepare clips with `hqdn3d → lanczos → light unsharp` before grading; add grain only in the mux. A 720-line film transfer can fill a 1,700 px window, not a full 1080p frame: frame it (a window, a split strip, an iris) instead of stretching it.
- **Paper fibre**: a fixed seeded noise canvas multiplied over the frame at α 0.5; film grain 4 added by `mux.sh`.

## 3. Colour logic

| Role | Value | Use |
|---|---|---|
| Red | `#D52B1E` | bands, wedges, blocks, the key number, marker bars, circles and leaders, the one winner in a comparison |
| Ink | `#141210` | type, beams under each floor, window borders, dark grounds |
| Paper | `#EDE4D0` | ground, reversed type, cut-out borders |

- Everything photographic is ink-on-paper; nothing else has colour. Red is never laid on red: a red block on a red ground becomes ink.
- Alternate grounds to make cuts land: paper scene → ink scene → paper. In an acceleration the background itself alternates red / ink per cut.

## 4. Type & subtitles

| Use | Face | Size (1080p) |
|---|---|---|
| Chinese display, slogans | Noto Sans SC 900 (subset) | 110–210 px; stacked vertically 170 px per character |
| Numbers, English display | Oswald 600–700 | numbers 230–440 px; English lines 30–62 px, letter-spacing 2–10 px, capitals |
| Source and footage tags | Space Mono Bold (CJK falls back to Noto) | 17–18 px on an ink or red tab, padding 6 |
| Subtitles | Noto Sans SC 700 40 px over Oswald 500 28 px | bottom left, ink bar at 90 %, a 10 px red tick |

- **Bilingual pairs**: Chinese block, then one English line in Oswald directly under it (or on the neighbouring band). Each language one line, measured.
- **Placement**: along the −18° axis on a band, or as an ink / red block; never centred on the frame, never a header. Numbers can be bigger than the words that explain them.
- **Tags**: every archive window carries its footage tag (`FILM · <TITLE> · <PLACE> <YEAR>`, `PHOTO · <AUTHOR> <YEAR>`), every fact a source tag (`来源 · <PUBLISHER> <YEAR>`). If the footage is not of the subject itself, the tag says what it really is.
- **Subtitles** stay bottom-left in a 960–1056 px strip; key type keeps above y 930 while narration runs. Subtitles hold ≥ max(1.8 s, speech + 0.6 s). On-screen text follows `readcheck.mjs` (CJK ÷ 4.5 + other ÷ 15 + 1.5 s, fully in frame); a comparison holds every item ≥ 2.5 s before its verdict.

## 5. Edit grammar

- **Grid**: one tempo for picture and score (120 BPM: beat 0.5 s, bar 2 s). Every cut, slam, wipe and count lands on a beat, half-beat or sixteenth. The page exports these times as `window.EV`; the mix reads the same list.
- **Shot length**: 0.5–2 s for footage; one idea per shot. A section may accelerate by halving: 0.5 → 0.25 → 0.125 s (never shorter than 3 frames). Holds are reserved for reading: a text block, a freeze, a comparison.
- **Cut rule**: adjacent shots conflict in at least one of direction (left slam / right slam), value (paper / ink ground), or geometry (diagonal band / upright window). Never two paper documents in a row.
- **Nothing static for more than a second**: inside a hold something moves (film in its window, a counter, a slow push, a frame-within-the-frame). Planned exceptions only: the comparison hold, one silence beat, the end card.
- **Transitions inside the medium** (pick per cut, don't fade):
  - *red wipe*: a 260 px red band at 72° (perpendicular to the axis) sweeps the frame in 0.25 s, the next scene revealed behind it; it lands on the downbeat;
  - *iris*: a red marker circle drawn on a map or photo becomes an aperture and opens onto footage;
  - *slam*: the next element arrives from outside along the axis in 0.08–0.2 s, ease-out, hard stop, frame shake (amplitude 3–18 px, `exp(−14·Δt)`);
  - *flash cut*: one frame of 50–80 % paper over a window at a cut or freeze;
  - *hard cut on the beat* between grounds of opposite value;
  - *jump-in*: inside a freeze, a cut to a 1.2× crop of the same frame, the annotation scaling with it.
- **Two silences**: one where the orchestra stops and only an original recording remains, and one true half-bar of nothing (ink frame, one red dot) before the heaviest hit.

## 6. Formats (each is a function in `demo/index.html`)


<!-- END STYLE PAGE -->
