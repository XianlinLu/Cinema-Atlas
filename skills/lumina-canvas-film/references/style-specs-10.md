# Complete style specifications 10


<!-- STYLE: lidar-survey -->

- **The cloud is the data**: every point is a real return at its measured position; points appear, glow, lift away or give way to a surface, but are never moved into a shape.
- **Points become a surface**: a front (scan line, cutting plane) behind which the cloud condenses into a solid model of the same place.
- **Classification is a lever**: ground, vegetation, buildings, water are layers to peel, isolate and recolour.
- **Measurement in hairlines**: one reading at a time, in the accent, attached to what it measures; numbers from the points or an official source.
- **Dark, quiet, exact**: near-black ground, restrained colour, no glow except at the front.

Not Sci-fi Hologram HUD (no invented interface: the points are real, sparse where the survey was), not Satellite Briefing (photographs from above; here a 3D cloud flown through), not Blueprint, not Low-poly Isometric, not Glass Product Render.

## 2. Materials & rendering

- **Points**: GL points sized in world units (0.12–0.3 m), floor of one output pixel, soft discs, opaque and depth-tested (additive only for a ghost layer); colour from height or class, value from intensity; distance fog.
- **Quantise for the browser**: uint16 positions (2 cm / 1 cm) plus a byte each for height above ground, class, intensity, seed.
- **Height above ground** for every return (minus a ground model triangulated from class-2 returns) drives the colour ramp, the cutting plane and the ruler.
- **The solid surface**: a 0.5–1 m mesh of the ground or surface model, smooth normals, baked short-radius AO, a low raking sun (20–35°), faint contours, crests lightened. Display exaggeration of micro relief (×2–3) only with an on-screen note; measure on undistorted data.
- **The front**: one world-space plane (one uniform) shared by the point and surface shaders; points ahead of it brighten, a thin seam glows behind it and the surface fills in over tens of metres.
- **The cutting plane** (by height above ground): returns above it lift away and fade, a ring glows where it meets the trees, a ruler on the frame edge tracks it.
- **Marks on the surface** (traced features, section lines) are a distance field in the surface shader, kept hairline with `fwidth`; readings, leaders and charts are a 2D overlay through the same world → screen function.
- **A survey window**: outside the measured area the cloud stays as dim points instead of ending in black.
- **Post**: 2× render, high-threshold bloom (only fronts and seams), vignette; no grain (points are already fine detail; encode at a higher CRF).

## 3. Colour logic

- Background near-black with a cold tint; never pure black, never a gradient sky.
- Points: one ramp by height or class, desaturated (deep green-teal → pale; or grey → white); intensity modulates value, not hue. No rainbow elevation ramps.
- The front and seams: one cool near-white; it is light, not a colour.
- The solid surface: warm neutral (stone, clay, plaster), lit; its colour never competes with the accent.
- One accent (amber) reserved for what was found and measured: traced features, the reading, the section line. A second, cooler hue only in a comparison chart.

Example (our demo): background #05080A, canopy #1F3F35 → #5C9A7A → #E2F3DC, ground returns #C8B38C, surface #BDB5A6, front #D4FFF0, accent #FFB347, chart green #83C495.

## 4. Type & subtitles

- **Roles**: light condensed numerals for readings (110–130 px, e.g. Barlow Condensed 300); a monospace for instruments, coordinates, counts and source lines (19–22 px, e.g. IBM Plex Mono); a sans for labels in the film's language (24–36 px, e.g. Noto Sans SC 500). OFL, self-hosted, CJK subset to the characters used.
- **Instruments** in one corner: place, coordinates, area, data source, point count, any exaggeration; they change only when the medium does.
- **Readings** in the right third beside what they measure: label, number, source/method line; a leader when the feature is in frame; a rolling counter reports its landing value.
- **Subtitles**: a transcript strip bottom-left (2 px rule, plate fading right), one line per language measured with the real font, split rather than wrapped; if bilingual, the film's language on top.
- Nothing below 19 px at 1080p. Hold subtitles ≥ max(1.8 s, speech + 0.6 s); labels ≥ characters ÷ 4.5 + 1.5 s (CJK), letters ÷ 15 + 1.5 s (Latin).

## 5. Motion quality

- On ones, 24 fps; the camera never stops; keys as a C1 spline in target / distance / heading / pitch (no `lookAt` from nadir).
- The front moves on an ease, slowest where the subject is; a cutting plane steps on the beat (eased steps, short holds) so the layers read.
- Points appear behind a front or by height, never by random fade-in across the whole frame.
- Readings land with a small pop; traced features light up along their length in order.
- Never moves: the points relative to each other (no wobble, no noise displacement), the instruments' positions.

## 6. Camera grammar

| Move | What it expresses | Can serve |
|---|---|---|
| Locked nadir with slow push | "this is what a photo shows" | a claim to test; a before; an ending that returns to the map |
| Crane down with tilt to oblique | entering the data; the place has height | the switch from picture to cloud |
| Low oblique close to the cloud (10–20° pitch, 90–150 m) | volume; things standing up | canopy, buildings, a facade, a cliff |
| Slow orbit | studying, the plane doing the work | a peel; a scan; a held reading |
| Rising pull-back | scale reveal of what was found | a network, a site plan, a corridor |
| Lateral track | travelling a feature | a wall, a road, a pipeline, a coast |
| Push to a section | the detail that proves it | a cross-section, a clearance, a height |

Subject ≥ a third of the frame height at key moments; readings right third; instruments in a corner; nothing in the subtitle strip. Transitions are fronts and planes, never crossfades or hard cuts inside the cloud.

## 7. Sound palette

- **Instrument sounds**: FM pings, fine crackle as points arrive, noise sweeps tied to a front, ticks that divide (8ths → 16ths → 32nds) to accelerate, a descending pitched blip per peeled layer, a ratchet while a counter rolls, a ping when a reading lands.
- **Weight and synthesis**: timpani, bass drum, gran cassa for condensations and cuts, a reversed swell into the main impact; low-passed detuned-saw pads; a pulse bass with audible 2nd/3rd harmonics.
- **Dry and wet**: one option is electronics while the subject is still points, and a single organic, wooden or bowed timbre (marimba, bowed vibraphone) for the found features once the surface exists.
- **Beds**: the place's own ambience (wind in leaves, water, traffic) at the start and the end as J- and L-cuts; a thin air bed in between.
- **Silence**: a near silence (air only) before the main reveal; the first sound after it is the impact.
- **Mix**: voice ~10 dB over the music and ducking it; impacts outside the bus compressor; −14 LUFS, true peak ≤ −1.2 dBTP. Voice: a calm, plain narrator, short declarative lines.

## 8. Native moves

- **Photo to points.** A scan line crosses an aerial photo; behind it the place is points. *Fits content like:* a site visit before a design; what the satellite misses; a quarry's real volume.
- **The canopy peel.** A plane descends by height above ground, returns above it lift away layer by layer, a ruler tracks it. *Fits content like:* archaeology under forest; a hidden trail; flood channels; landslide scars.
- **Points condense.** A front turns the remaining points into a solid surface; found features light up in order. *Fits content like:* a building scan to a BIM shell; a cliff to a hazard model; a street to a vehicle clearance model.
- **The section.** A plane crosses one feature; the profile glows and a dimensioned chart of the real returns hangs beside it. *Fits content like:* a levee's height; a bridge's clearance; a road cut.
- **The window.** The measured area is a stage inside the unmeasured cloud. *Fits content like:* a parcel; a corridor; a site boundary.
- **The regrowth.** The removed layer returns as a ghost over what was found. *Fits content like:* an ending; a clearing before/after; a buried pipe under a street.

## 9. Pitfalls of the medium

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


<!-- END STYLE PAGE -->
