# Complete style specifications 03


<!-- STYLE: lidar-survey -->

- **Finding data for a new place**: USGS 3DEP (US) as Entwine Point Tiles per project at `https://s3-us-west-2.amazonaws.com/usgs-lidar-public/<project>/ept.json`, projects and footprints in `boundaries/resources.geojson` of github.com/hobuinc/usgs-lidar; bare-earth scouting through the 3DEP elevation ImageServer. OpenTopography (catalogue of many collections, licence per dataset). AHN (Netherlands, CC0). National portals, e.g. England's Environment Agency LiDAR (OGL), France IGN LiDAR HD (Licence Ouverte), Spain PNOA-LiDAR (CC BY 4.0), Finland NLS (CC BY 4.0), New Zealand LINZ (CC BY 4.0); read each portal's terms. Fetch a subset by box and depth, not whole tiles.
- **Licences**: public domain, CC0, CC BY and attribution-only government licences are fine, with credit in `CREDITS`. ODbL, CC BY-SA, "no known restrictions" (not CC0) or non-commercial terms: name them to the user and ask first. Never commercial scans or Google 3D tiles. Ask the user for their own scans (a site survey, a drone or terrestrial scan, their BIM) when the film is about their asset. Never stand in a generated or invented cloud for real evidence.
- **Facts**: keep a FACTS.md in the project folder (claim, source URL, quoted wording, or the measurement method) and deliver it with the film.
- **Coordinates**: EPT copies are often Web Mercator: convert to a local east/north/up frame first; check the vertical datum against known ground.
- **Leaf-off vs leaf-on**: leaf-off lidar reaches the ground but its canopy is sparse; say which season each layer is.
- **Classification is the provider's**: class 1 mixes vegetation, buildings and noise; drop 7 and 18; finish a cut below 0 m or low vegetation stays as stripes.
- **A dense cloud reads as a flat carpet** from afar: go close and low for volume; let the distance fog out.
- **Scan striping** is real texture; don't frame a reveal on it at grazing angles.
- **Traced features are interpretation**: say "traced", keep the tracing in a data file, snap it to the data, leave faint candidates out.
- **Privacy**: crop out houses and yards; keep the survey window on public or uninhabited land.

## 10. Engine

- `demo/film.js`: point shader (front, cutting plane, lift, ghost, window), surface shader (light, AO, contours, feature field, section), photo shader, camera spline (`camAt`), overlay (`reading`, `drawSection`, `subtitles`, readcheck registry).
- `demo/tools/`: `fetch_ept.py` (EPT subset), `terrain.py` (local frame, DTM), `walls.py` (relief model), `trace.py` (snap a tracing, measure), `profile.py` (section from raw returns), `build_data.py` (binaries + facts).
- **Extra packages and packs** (beyond `setup.sh deps voice music`): Python `laspy`, `lazrs` (LAZ decoding), `scikit-image` (relief and ridge tools), `fonttools` + `brotli` (CJK subset). They are not in the library's `.venv`: the agent installs them itself into a private venv in the project folder (the demo uses `demo/assets/raw/.venv`), never into `$LIB/.venv`. Fonts come from github.com/google/fonts (ofl/), fetched by script.
- Minimal example, not in the demo: a building scan. Points coloured by class, a vertical front sweeping the street; behind it a 1 m surface model; one reading (roof height above the street).

## 11. Variation space

The agent decides the place and dataset, which classes to peel or keep, the fronts and their directions, the camera route, the readings, the accent within the colour logic, and whether a photo or a map opens the film.

- **Structures**: a corridor flown end to end with three readings; two surveys of one place (erosion, construction) swapped by a front; one object scanned, cut and dimensioned.
- **Openings**: a black frame the scan paints in line by line; a street-level photograph that dissolves into its own returns; a top-down map that tilts up into the cloud.
- **Endings**: the cloud pulls back to show the whole survey tile; the removed layer returns as a ghost; the last reading holds while the points fade to the instruments.

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: white-model -->

# Projection on White Model — Style Prompt

> A pure white massing model of a real place stands on a plinth in a dark room, and a projector paints data onto it as light: one layer at a time, falling on the surfaces that face it, spilling a little past the plate. The model never changes; only the light on it does.
> References (grammar only): projection-mapped planning models in city galleries (the dark room, the soft throw, colour only on white surfaces); macro model photography (shallow focus at rooftop height); editorial data graphics (one figure, one label, one source per layer). Copy none of their layouts, typefaces, colours or music, and never name them in the film.

## 1. Essence, and what it is not

- **The model is real geometry of a real place**: building footprints and heights from open data (§2), extruded at a stated scale (1:1000, 1:2000…). Nothing on the model is invented or "representative", and no generated image ever stands in for the place.
- **The model is white; data is light.** Colour is never painted into the material: it is projected, so it brightens surfaces that face the projector, fades on walls turned away, stops at the edge of the throw and reaches a little onto the plinth.
- **Layers arrive one at a time**, each with its own gesture of light (a wash, a pop-on, a rising level, a moving sun), and each answers the question the last one raised.
- **A physical room**: house lights, a projector that strikes and switches, a plinth, darkness around it. Lights out is where the data starts; lights up is where it ends.
- **Every number on screen is computed from the same buildings** that are on the table.

Not Isometric Infographic (no diorama or icons), not Low-poly Island (no invented terrain), not Sci-fi Hologram HUD (no wireframes; light lands on matter), not Satellite Briefing (no imagery), not a laser-scan or point-cloud film (no scan lines; light is projected, not measured).

## 2. Materials & rendering

- **Model**: matte white (≈ #F3F3F1, roughness ≈ 0.9), crisp edges; water a darker satin inlay in the base plate; bridges low white slabs; a thin base plate on a dark satin plinth.
- **Light model**: house light = one soft key + a neutral studio environment + AO on close shots. Projection = a term added to the lit surface in the shader: `colour × (0.42 + 0.58 · max(N·toProjector, 0)) × throw mask`, scaled by albedo, reduced on water. Never a texture on the mesh.
- **Building data is the material.** First look for the place's own open 3D or footprint-with-height data: 3DBAG (Netherlands, CC BY 4.0), PLATEAU (Japan, CC BY 4.0-compatible), city open-data portals (footprints with heights or floors, zoning, plans). Fine: CC0, public domain, CC BY (credited in CREDITS and on screen). OpenStreetMap and Overture (ODbL), CC BY-SA and "no known restrictions" are not CC0: name the terms to the user and ask first. For their own site, ask the user for their data (plan, city model, survey heights).
- **Layers depend on what exists.** Construction years per building are a Dutch luxury (BAG); elsewhere they are often missing. Substitute what the data does hold and the medium can still project: heights or floor counts, footprint area, zoning or plan status, a boundary, sun and shadow (always computable). Never invent a year layer.
- **A layer is state, not a picture**: per-building attributes (year, height, rank, flags) live in vertex data; the shader decides each frame what colour the projector gives them.
- **The sun is a real directional light** with shadow maps, computed from the place's latitude and a real date and time (NOAA/Meeus solar position). The projector can trace what the sun does (a shadow footprint) but never fakes a shadow.
- **Post**: physical depth of field (stronger on close shots), bloom only above the projection highlights, vignette, light grain in ffmpeg. GTAO only on close shots: on wide grazing views it bands.
- **Screen space only for the 2D layer**: readouts, pins, measured lines and subtitles go through the camera's world → screen function so they stay pinned to the model.
- **Keep a FACTS.md in the project folder** (claim, source URL, quoted wording, or the measurement method) and deliver it with the film; every number on screen is computed by a script from the same data as the model.

## 3. Colour logic

- Neutral ground: white model, dark room (near black), dark plinth. Projector black level is a cool near-black on the plate.
- **One hue family per layer**, chosen for the data: a single categorical accent for "the old/the exception" (e.g. warm amber), a sequential ramp for continuous data (blue → cyan → white for time, violet → magenta → peach for height).
- **A colour may return** only with the same meaning (the "before" colour reused later marks the same set of buildings).
- The sun is warm, its shade is a projected deep blue; data colours are put away when the sun arrives.
- Never colour the model in the house light; never use more than two layer palettes on screen at once.

## 4. Type & subtitles

- **Roles**: a light grotesk for the figure (Inter Tight 200, 120–140 px), a sans for labels in the film's language (Noto Sans SC 300/500, 20–36 px), a monospace for instruments, years and coordinates (IBM Plex Mono, 18–22 px). OFL, self-hosted, CJK subset.
- **Readout in the left third**, one per layer: index + layer name, one figure, one label, one source line, a legend bar.
- **Pins**: a hairline from a roof or a ground point up to a tag on a dark plate (title 26 px + one sub line 20 px).
- **Identity label** top-left, quiet: place, scale, data sources.
- **Subtitles** centred at the bottom on a soft dark gradient, no box, measured with the real fonts; if the film is bilingual, the film's language on top, each language on a single line, split into two cues rather than wrap.
- Nothing below 18 px at 1080p. Hold subtitles ≥ max(1.8 s, speech + 0.6 s); labels ≥ characters ÷ 4.5 + 1.5 s (CJK), letters ÷ 15 + 1.5 s (Latin).

## 5. Motion quality

- The camera moves continuously and slowly; it changes speed with the layers, never stops dead.
- **Light is the actor.** Each layer arrives by a soft-edged gesture of light: a wash spreading from the projector axis, buildings switching on one by one with a short flash, a level climbing every facade, the sun's clock running. No hard line sweeping the table.
- House lights cut fast (a relay, 0.25 s) and return slowly (1 s); the projector strikes with a brief flicker.
- Counters roll while the light moves and land when it lands; measured lines grow from A to B with ticks.
- What never moves: the model, the plinth, the pins' anchors on the model.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Macro glide at rooftop height, shallow focus | the model is a real object | an opening; a detail that matters |
| Crane up and back | the whole pattern only seen from above | revealing a hole, a cluster, an edge |
| Slow orbit with a rise | the city as a whole, layers accumulating | growth over time; comparisons across the model |
| Boom down to a low angle against black | height, skyline | tall buildings, heights, a single tower |
| Side-on track along a line | a measured distance on the model | a shadow, a corridor, a route, a view line |
| Pull back as the house lights return | the data stops; the object remains | an ending; a reset between topics |

At key moments the subject fills a third of the frame height; readouts left third, subtitles bottom centre, pins never over the readout. Transitions are light changes on one take (lights out, a layer replacing another, the projector going dark), not cuts, fades or wipes.

## 7. Sound palette

- **The room**: room tone, the projector fan (hum + filtered air) rising when the lamp strikes, relays for the house lights, a lamp strike (zap + thump), the air of a light wash (sliding band-passed noise).
- **Light as sound**: mallets and glass for things switching on, bowed vibraphone for held light, a rising mallet line and air riser for a climbing level, one glass note per highlighted building.
- **Weight**: timpani, gran cassa, gong, low brass for a heavy fact; warm low brass for a turn.
- **Floor**: contrabass and cellos only as a floor under the chords; no generic piano and strings melody.
- **Silence**: the projector goes dark and everything stops but a thin fan hum before the turn; a short suck-out before the heaviest hit. The first sound after the silence is the turn.
- **Mix**: voice about 10 dB over the music; the two designed impacts are the loudest moments; −14 LUFS, true peak ≤ −1.2 dB. Voice: calm, short declarative lines, numbers spoken plainly.

## 8. Native moves

- **Lights out, lamp on.** House light, a relay, darkness, the lamp strikes, the first layer arrives. *Fits content like:* a site before and after; a district before a plan is shown; any "now look closer".
- **The hole.** Light only the set that answers a question (built before a date, owned by one party, inside a zone) and let the absence draw the shape. *Fits content like:* a war-damaged centre; a flood plain with no housing; land a company owns; a protected zone.
- **Layers by time.** Buildings switch on in the decade they were built, each layer faster than the last, a year counter rolling. *Fits content like:* a new town's growth; a campus master plan by phase; a port's expansion; a developer's portfolio by year.
- **The rising level.** A soft level of light climbs every facade at once; low buildings finish first, the tallest last, the reading rides up with it. *Fits content like:* building heights; sea-level or flood depth; floor counts; a height limit being tested.
- **The sun clock.** A real sun at a real date sweeps the shadows; the projector then traces one shadow and measures it. *Fits content like:* a new tower's shadow on a park; winter light in a courtyard; solar panels' best roofs; a street's daylight hours.
- **The pick-out.** One building or set lights alone while the rest stay dark, with a pin. *Fits content like:* a listed building; the plot for sale; the hospital in an evacuation plan.
- **Lights up.** The data stops, the white model comes back. An ending or a reset.

## 9. Pitfalls of the medium

- **Wall normals** wound the wrong way show inside faces (walls look hollow): derive the outward normal from ring orientation. **Shared walls** between parts z-fight: skip the overlap below the lower neighbour.
- **Warm HDRIs turn the white model beige**: use a neutral studio environment.
- **GTAO on wide grazing views** produces wedge-shaped dark bands; keep it on close shots only.
- **A low sun lights facades, not roofs**: shoot from the sunlit side or side-on. **Narrow shadows vanish** among all the others: trace the one that matters (fill + edge) and measure it.
- **Hairline scan lines read as laser scanning**: give every projection front a wide soft edge or switch buildings individually.
- **Floating labels**: anchor pins on the tallest part of a building, not on its footprint centroid.
- **Numbers from mixed sources** (official height vs measured roof): say which on screen ("roof", "measured").

## 10. Engine

- `demo/studio.js` — `makeStudio(W, H, model)`: renderer, post, room, the projection material (`projMaterial(kind)` injects `projLight()` / `roofGlow()` into MeshStandardMaterial), the city mesh (`buildCity`: outward normals, shared walls removed), plate, plinth, house light (index 0) and sun (index 1). Uniforms `U` drive every layer.
- `demo/tools/prep.py` — **3DBAG + BGT only**: it reads 3DBAG fields (`b3_h_70p`, `b3_h_maaiveld`, `oorspronkelijkbouwjaar`) and Dutch RD coordinates (`tools/rd.py`). Another source needs its own adapter that writes the same `model.json`: `{size:[w,d] model metres, b:[[year|0, height_m], …] per building, p:[[building_index, height_model_m, [[[x,z],…] outer ring, …holes]], …] per roof part, decks:[[[x,z],…]]}`, with x east, z south, 1 unit = 1 model metre; plus `water.png` (plate-sized mask) and a `stats.json` with every on-screen number. `tools/sun.py` (solar position, any place and date) and the heightfield shadow are source-independent.
- `demo/overlay.js` — readout, pin, measured range line, subtitle strip, title card; registers texts for readcheck.
- **Extra packages and packs**: none beyond `setup.sh deps` (+ `voice`, `music` for narration and score); downloads are plain `curl` from the data portal. Reprojecting another country's data may need pyproj or shapely: the agent installs them itself into a private venv in the project folder, not into `$LIB/.venv`.
- Minimal example, not in the demo: set `U.uPreC` to a station and `U.uPreR` growing to light everything within walking distance; or put a flood height in `U.uHgtF` with `U.uHgtBand` held at 1 and leave it still.

## 11. Variation space

Decide per film: place and scale, which layers in what order, their colours, the opening, the camera path, the ending, the pace.

- **Structures**: a question answered layer by layer; a plan versus today (the plan's buildings switching on in a second colour); one building's story told by its neighbours.
- **Openings**: a macro glide over white roofs; darkness and a single pick-out; the plinth from across the room as the house lights fall.
- **Endings**: lights up on the white model; one last layer left on alone; the camera rising until the model is an object on a table in a dark room.

---

How our demo was made (story, shots, score, title card, build): [DEMO.md](DEMO.md). Read it after your treatment exists.

<!-- STYLE: data-physical -->

# Data Physicalization — Style Prompt

> Real statistics built as real objects: every unit is a countable piece of material (a plate, a block, a coin, a bar) stacked to exact scale on a crafted base, shot like a product in a studio — soft key, long shadows, shallow depth of field, physically based materials. The camera reads a number at the edge of one plate, follows the data as it grows, and pulls back until the chart is an installation.
> References (grammar only): data-sculpture and physical-visualisation practice (one unit = one object, the object is the axis); product and still-life photography (a warm key at a low angle, a cool rim, a seamless sweep); annual-report editorial design (one reading per screen, a source line, a quiet grotesk). Copy none of them; never name them in the film.

## 1. Essence, and what it is not


<!-- END STYLE PAGE -->
