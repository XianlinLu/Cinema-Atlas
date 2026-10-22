# Complete style specifications 08


<!-- STYLE: news-package -->

- **120 BPM grid**, beat 0 at the end of the sting (1.5 s). Every cut and wipe on a beat or half-beat.
- **Shot lengths**: sting 1.5 s; rundown 4–5 s; story shots 3–7 s; a map long take (6–12 s) as the bulletin's breath; a comparison stays until every item has been fully on screen ≥ 2.5 s.
- **A package action every 0.5–1 s** inside a shot (flip, count, stamp, tick, strap change, map light, line step). No frame flat for more than 1 s; a strong action within 0.5 s of every cut.
- **Date every story**: a weekly bulletin's items happen on different days; the date sits in the rundown row, the eyebrow line, the readout or the document.
- **The order inside an item**: what (the name or the number) → how big (the line, the bars, the price board) → who it hits or who said it (bars, documents, a quote) → the verdict stamp.

## 8. Sound palette

| Layer | What | Level |
|---|---|---|
| Anchor voice | one narrator, one sentence per graphic, starting 0.1 s after the cut; HP 90 Hz, 3:1 compression. Default: the library's Kokoro (`core/tts/tts.py`, free, Apache 2.0) in English or Chinese. The user's own recording, or another TTS they have a key for (for example Doubao, as in the demo), replaces it — never required | music ducked ≈ −7 dB and its 1.2–5 kHz band thinned under speech |
| News theme | 120 BPM, minor key: spiccato violins in root–fifth–octave eighths, pizzicato bass on the beat, horn pads, a low-passed 16th-note saw pulse, kick on 1 and 3, snare on 2 and 4 | full under the rundown and the first story |
| Section moods | markets: violins down an octave, tremolo, four-on-the-floor kick (heartbeat); policy: pizzicato and horns only | |
| Signature hits | sting tutti; glockenspiel notes as the rundown rows land; timpani on hard cuts and story changes; one beat of silence before the biggest break, then the heaviest hit of the film; a held drone after the verdict stamp; a major-key lift for the last story; tutti on the end card | |
| Foley | whoosh on wipes, flap clicks on split-flaps, stamp thump + clack, trading-room ticks under market charts, map clicks per lit country, a sonar ping on a city, paper and typewriter ticks on documents, click + glockenspiel on ticks | |
| Room | server-room hum under a tech plate, soft air under maps | very low |

Master −14 LUFS, true peak −1.2 dB (`core/render/mux.sh`). Samples: VSCO 2 CE and VCSL (CC0); foley synthesised (`core/audio/sfx.py`).

## 9. Native moves

1. **Sting becomes the bug** — the brand plate slams in, then flies to the corner and stays there for the whole bulletin; opening and programme are one object.
2. **Strap tab = category** — the strap's tab changes category (模型 MODELS, 市场 MARKETS, 监管 POLICY …) with a white flash when a new story starts; no separate item cards between stories.
3. **Rundown, then ticked off** — the same list opens and closes the bulletin; at the end each row gets its tick.
4. **Spec card** — a launch reduced to its proportions: the whole and the part on one scale, then what it runs on, joined by a bracket to the total.
5. **Strap that never leaves** — one strap group from the first story to the recap; words flip, the strap itself never exits mid-programme.
6. **Split-flap before/after** — old and new value on one board, each tile flipping from the old to the new.
7. **Breaking the threshold** — a line advances one period per step towards a dashed threshold; the music stops for one beat before the last step and the crossing gets the heaviest hit.
8. **Date in the eyebrow** — every graphic's eyebrow line carries source and date in mono caps, so a weekly round-up never blurs which day each item happened.
9. **City sends the letters** — on a map long take, documents fly out of the sending city to their addressees; one world→screen function keeps labels and documents attached through push and pan.
10. **Quote card + verdict stamp** — the official's own words in type, with name, occasion and date; an underline on the key word as the voice says it; one stamp.

Where each move lives in the demo's code: [DEMO.md](DEMO.md) (build notes).

## 10. Material

1. **Facts first.** Every on-screen number and every sentence of the voice comes from an official source (the company's own page, the exchange's data, the institution's press release or speech), recorded in `demo/FACTS.md` with claim, URL, quoted wording and any arithmetic. When a fact exists only in a news report, attribute it on screen and in the voice ("据…报道 / … reports") and keep to the plain claim; never put a single report's allegations about a real company or person on screen.
2. **Data.** Draw charts from real series only; when you have just a few reported numbers, draw a *schematic* line, tag it `SCHEMATIC`, and label only what you know. Exchange closes: the exchange itself, the central bank's statistics portal, or a market-data file whose source you log.
3. **Pictures: ask in this order.**
   a. **The user's own images** — photos, b-roll stills, their logo and colours (the package is rebuilt around their brand). Use these first.
   b. **Generated illustrative plates**, if the user wants them. Before generating, tell the user how many images and what each shows (one line per plate). With the Codex CLI installed and able to generate images, `demo/tools/gen_image.py` (driven by `demo/tools/gen_plates.sh`) makes them and saves JPEGs to `demo/assets/plates/`. With any other image tool (an API or a web app), give the user the prompts and the target file names; they generate the images and drop them into `demo/assets/plates/`. Prompts ask for no text, letters, logos, flags or people.
   c. **No generated images**: public-domain, CC0 or CC BY photographs (licences below), or abstract backgrounds drawn in code (gradients, grids, light fins — the package already carries the frame).
   Whatever the source: every word on screen is typeset in code, never baked into an image; a generated plate is only ever an illustration behind a graphic, tagged `ILLUSTRATION / 示意` for as long as it is visible, and never stands in for the event, a place in the news, or a person. No generated anchor.
4. **Photo and footage licences** (judge each file on its own page, not the search result):
   - **Wikimedia Commons**: CC0, public domain or CC BY (credit author, title, licence on the end card and in `CREDITS`). Not used: CC BY-SA, "no known restrictions", unclear licences, YouTube re-uploads, colourised or "restored" versions.
   - **U.S. federal agencies** (NASA, NOAA, NARA, USGS…): public domain; check the page does not credit a contractor or third party.
   - **Internet Archive**: only items whose page states public domain, CC0 or CC BY; U.S. works published before 1931 are public domain.
   - **Library of Congress / national archives**: read each rights statement; "no known restrictions" is not enough.
   - **Institutions' audiovisual services** (for example the European Commission's): read their reuse terms per item; many require attribution and forbid implying endorsement.
   - **Maps**: Natural Earth (public domain), via `world-atlas` TopoJSON.
5. **Before downloading, tell the user** what you will fetch, from where and under which licence. The finder copied into this style, `demo/tools/footage.py` (`search commons|archive|nasa`, `fetch`, `used`, `md`), logs licence, author, page and the seconds used into `SOURCES.jsonl` and writes `SOURCES.md`. Keep `raw/` under ~1.5 GB.
6. **Logos**: never use a company's logo for a company in the news; set its name in type.
7. **People**: public figures in the news can be named on a profile strap; no close-up or slow motion of private individuals.
8. **Voice and music**: ask whether the user has a recorded anchor, a preferred voice or a theme of their own before synthesising one.

## 11. Pitfalls

- **Package left behind.** If the strap, source line or tags are drawn once on top of everything, a wipe changes the picture under yesterday's headline and the strap catches up 0.3–0.5 s later. Draw them per picture, inside the wipe's clip.
- **Leftover layout.** Removing subtitles or a crawl without moving the content down leaves a dead band above the strap.
- **Masked type peeking in.** A push-in title clipped by a mask shows its top edge before it moves if the travel distance doesn't clear the mask; start it fully below and don't draw at progress 0.
- **Words stronger than the source.** "Request for information" is not "investigation" or "penalty"; write "no fine, no case opened" or "for the first time" only if a source says so — and check the institution's own pages, which can contradict a report ("first requests" may have gone out months earlier).
- **Thresholds depend on the reference.** "Bear market" = −20 % from *which* high? Name the reference on the axis; from a different peak the claim can be false.
- **Attribute what only a report says.** When the official source does not name the companies, the graphic carries "据… 报道 / reported by …" and so does the voice.
- **A schematic posing as data.** Rolling counters on a close price flash values that never existed; set the close with a mask push instead. Don't label axes the data doesn't support.
- **Source lines under the strap.** Right-aligned mono 13 px: ≤ 36 characters.
- **Stamps over key words.** A stamp hit can mask the voice ("fines"); take the brass off the stamp and low-pass its clack.
- **Gold on paper** has too little contrast: use ink or dark olive.
- **Generated plates** carry stray corner marks: crop them in `prep.py`.
- **Short preview text.** Rundown rows are previews of the stories; `readcheck` flags them as short in the opening — they return in the recap and as straps, so accept the flag or leave them out of `TEXTS`.
- **Names in synthetic speech.** Spell brand names, model numbers and abbreviations the way they should sound in the TTS text (a respelling, a number written as a word, an abbreviation without dots) while the strap and subtitles keep the real spelling; when speech-to-text mishears an unusual name, put the expected transcript in the line's `asr` field instead of rewriting the line.

## 12. Variation space

Decide per film: the channel's name, plate and accent colour; how many items (one lead with a long package, three or four equal items, a five-item round-up); which full-frame graphics each item needs; where the long take goes; the anchor's voice.

- **Three structures:** rundown → items → rundown ticked (round-up); one lead package with a correspondent two-box and a short "also today" grid; a countdown of items (election-night, sports results).
- **Three openings:** sting → rundown; cold open on the biggest graphic, then the sting; sting straight into the first story with the rundown as a recap only.
- **Three endings:** rundown ticked → end card; a "coming up next week" teaser card; the last stamp freezing into the end card.

---

How our demo was made (story, shots, score, end card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: satellite-briefing -->

# Satellite Briefing — Style Prompt

> Real satellite imagery of a real place, graded down to an analyst's grey, with thin white measurement lines drawn on the ground: a lock-on reticle, outlines, a range line, one reading. One continuous zoom built from stacked imagery plates carries the viewer from orbit to the ground and back, and time can run inside one locked frame.
> References (grammar only): open-source investigation films that annotate satellite pictures (thin lines on imagery, one claim per screen, measuring as the plot); the Eameses' *Powers of Ten* (one continuous change of scale with a readout); NASA Earth Observatory's *World of Change* (one place, time running). Copy none of their layouts, typefaces, icons or music; never name them in the film.

## 1. Essence, and what it is not

- **The ground is a photograph**: real, licence-clean, georeferenced satellite or aerial imagery of the actual place. Nothing on the ground is drawn, stylised or generated.
- **Two layers, two truths**: the imagery is what the satellite saw; the hairlines are what the analyst measured. Marks are thin, white, sparse, and sit on real coordinates.
- **The grade moves with the story**: orbit in true colour, the analysis layer in grey, colour back only where the story turns.
- **Scale is the camera**: one zoom from orbit to the ground built from nested plates, with an altitude readout and a scale bar from the same camera.
- **One finding per screen**, in the single accent colour.

Not Data Storytelling (a chart on paper), not Sci-fi Hologram HUD (no glowing wireframes or invented chrome), not Blueprint, not Isometric Infographic (real nadir or oblique views, no diorama), not a keynote (no slides, header bars or chapter numbers).

## 2. Materials & rendering

- **Plates**: georeferenced rasters with a lon/lat box, sampled in a shader where the camera ray hits the ground, nested by resolution (world → region → detail) with feathered edges so finer plates dissolve in as the camera descends.
- **Globe**: ray–sphere from a perspective camera, a thin atmosphere rim, limb shading at orbit only; compute |C|² − R² in double precision (float32 fails below a few tens of km).
- **Time**: dated plates share one grid. A soft scan front (a satellite pass, never a hairline) swaps them: north → south forward, south → north for a rewind. Growth can run outward from the old edge, ordered by a distance map.
- **The analyst's grade** (one uniform from colour to grey): luminance with local contrast and clarity, a shoulder so salt, snow and cloud stay below white, toned blue-black → cool silver up to ~65 % grey, a fifth of the chroma. White belongs to the marks.
- **Marks**: a 2D overlay through the same world → screen function: hairlines 1.2–2.6 px with a dark halo, dashes for history and claims, brackets, ticks, leader lines. Lines draw on; outlines print behind the scan.
- **Screen space only for instruments** (altitude, scale bar, imagery credit) and the transcript strip. Everything else is anchored to the ground.
- **The claim layer** is a printed map drawn in the shader from a distance field of the old outline: paper grain a few pixels wide at any zoom, halftone ink, coast and waterlines, graticule, the serif name.
- **Post**: light grain in ffmpeg, a vignette, directional blur only on whip pans.

## 3. Colour logic

- Neutral ground: grey, roughly 3–65 % in value. White means *measured*.
- One accent (warm, e.g. amber) for the single reading on screen, never decoration.
- A second hue may mark the **claim** the imagery tests (a map, a plan, a promise): flat, cartographic, never used for anything measured.
- True colour is evidence: at orbit, and again only where the story turns (the field that greened, the water that returned).
- No false-colour ramps over the imagery.

Example (our demo): ground #070B0E → #A1A7A9, marks #F2F5F6, reading #FFBE55, map blue rgb(46, 112, 206).

## 4. Type & subtitles

- **Roles**: a light condensed grotesk for the reading (96–130 px, e.g. Barlow Condensed); a monospace for instruments and dates (20–34 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–42 px); a serif only for the claim layer and the title. OFL, self-hosted, CJK subset to the characters used.
- **Labels attach to the ground** with a leader line. The reading sits in the right third beside what it measures, label above, source note below ("Landsat, measured").
- **Subtitles are a transcript strip** at the bottom left: a 2 px white rule, a dark plate fading right, left-aligned, each line on one line (measure with the real font, `nowrap`; split a long sentence into two cues). If the film is bilingual, the film's language on top.
- Nothing below 20 px at 1080p, the imagery credit included.
- Hold subtitles ≥ max(1.8 s, speech + 0.6 s); a rolling counter reports its landing value; labels stay ≥ characters ÷ 4.5 + 1.5 s (CJK).

## 5. Motion quality

- The camera never stops: distance interpolates in log space, segments ease, holds keep a 2–5 % creep or a slow rotation. No frozen frame longer than a second.
- Marks arrive by being made: a line grows, an outline prints behind the scan, a counter rolls and lands with a small pop, a reticle snaps with overshoot.
- Time changes are scans, never dissolves; their spacing tells the speed, and the camera moves with them (accelerating as the steps shorten, braking on the last).
- Never moves: the ground under its annotations, the instrument positions.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Oblique orbit, limb in frame | scale, context, distance | an opening; a return; a title card |
| Dive (log zoom, tilt to nadir) | going to look for yourself | a reveal; checking a claim |
| Locked nadir frame, slow creep | evidence, comparison | time running in one place; a measurement |
| Push-in on a point | singling out | one town, one dam, one field |
| Track along a line | travelling a distance | measuring; a river, a road, a border |
| Whip pan with blur | a new subject at the same altitude | the counter-example; "meanwhile" |
| Climb back to orbit | consequence, perspective | an ending; a summary |

At key moments the subject fills a third of the frame height; reading right, subtitles bottom left, instruments in the corners. Transitions: scan-line swaps, a map layer switched off, zooming through plates, whip pans, the reticle opening into a title card. No crossfades between unrelated places, no hard cuts inside a zoom.

## 7. Sound palette

- **Telemetry**: FM pings (a lock-on ping worth bringing back), dry ticks on the grid that divide to accelerate, noise scans (rising for a rewind, falling forward), servo whines, a ratchet for a range line.
- **Weight**: timpani, bass drum, gran cassa, bowed cymbal, a tam-tam reversed when time runs backwards. Measurements land on a pitched hit.
- **Synthesis**: a pulse bass with audible 2nd and 3rd harmonics, detuned-saw pads under a low-pass, risers for dives.
- **Beds**: orbit hum, radio hiss, data chatter; the place's own ambience (wind, water, a far horn), sparingly, often as J- or L-cuts.
- **One option for the shape**: keep the palette dry (electronics, skins, metal) and let one wet timbre (glass, water, bowed metal) mark the turn.
- **Silence**: music and foley stop, a thin bed stays, impacts may decay into it; the first sound after it is the turn. A short suck-out (0.2–0.45 s, music and foley down ~25 dB) before the heaviest impacts makes them land.
- **Mix**: voice ~10 dB over music; the two or three designed impacts are the loudest moments (out of the bus compressor, with mid-range body, e.g. a low-brass stab); 20–60 Hz about 15 dB under the full band (high-pass ~40 Hz, impact weight at 60–120 Hz); −14 LUFS, true peak ≤ −1.2 dB. Voice: a calm analyst, short declarative lines.

## 8. Native moves


<!-- END STYLE PAGE -->
