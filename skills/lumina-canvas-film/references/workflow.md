# Library workflow adapted to Lumina

Topic/style selection resolves the prerequisites of the library workflow. The topic card is a Lumina adaptation requested by the user; it is not an extra production approval stage. Preserve this sequence once topic and style are fixed:

**Brief → Treatment → Look → Storyboard only when requested → Produce → Self-check and deliver.**

## 1. Brief: one consolidated round

Skip details already supplied. In one message or one native question batch, ask for:

- Facts, names, logos, products, or other topic requirements only the user can decide.
- The user's own assets: recordings or preferred voice, music, photos, logos, fonts; for evidence styles also data, imagery, scans, CAD, or measurements. Supplied material takes priority over style fallback sources.
- Language only if unclear; default voice and subtitles to the user's language.
- Whether the user wants to approve a storyboard first; default no.
- Actual missing production requirements, after inspecting available capabilities. With shell access and the installed library, check the core setup and include reported blockers in this same brief. Add voice/music dependencies only if needed. Without such tools, do not pretend an install check ran.

Wait for the reply, summarize the resolved brief in a few lines, fill other gaps with sensible defaults, then start. Do not return with another generic questionnaire. A later genuine asset/access blocker can require user input.

Defaults from the directing method: 30–60 seconds, 1920×1080 at 24 fps, voice/subtitles in the user's language, final loudness about −14 LUFS. These are intended film settings; on a static canvas they are production notes, not achieved output properties. Honor explicit duration, vertical format, no-voice, or no-subtitle instructions.

## 2. Treatment before demos or drawing

Read `director.md`. Pick 1–2 benchmarks suited to this topic and style: learn their grammar, not their characters, compositions, music, marks, or shots. Write an original treatment before opening demo descriptions or demo code. Use `TREATMENT.md` when files are supported; otherwise create a clearly labeled treatment note in the host.

The treatment must contain all eight source requirements:

1. Three possible story structures and the chosen one with reasons.
2. Logline and setup → turn → ending.
3. Benchmark: what to learn and what not to take.
4. Shot list with framing, angle, camera move, duration, and reason.
5. Second-by-second beat sheet.
6. Cue map: tempo, bar grid, instrumentation, cuts, key actions, subtitles.
7. Sound design table: ambience, main foley, music state by section.
8. Subtitle/title design consistent with the selected style.

Keep one subject, one goal, one turn, an opening hook within three seconds, an ending that echoes, and one medium-native move at the emotional peak. Do not bend the user's topic toward a demo.

## 3. Prove the look

Characters: a model sheet with turnaround, 3–4 expressions, 2–3 key poses, palette, plus two style frames. No characters: three style frames, including the signature shot. Use the real drawing method and inspect against every selected STYLE invariant. A mock-up cannot prove a code renderer's output.

## 4. Storyboard only when requested

If the user requested storyboard review, make 6–9 key shots on one sheet with shot number, framing, duration, and line. Show the logline and uncertainty, then stop and wait for explicit approval. A topic or style selection does not approve this later storyboard. Without that request, proceed after the look check.

## 5. Production

Follow `technique.md`: voice → speech check → score (voice/score may run concurrently) → animation → mix → render. One timeline drives picture, music, foley, and subtitles. Films are made in code; do not replace the pipeline with video generation or stock footage. In canvas-only mode preserve these as planned shot/camera/sound/cue specifications and clearly report the actual deliverable.

Use the full style's sound palette and native transitions. Preserve the directing method's rhythm, silence, readable holds, camera variety, signature shot, character performance, and motion-continuity checks.

## 6. Review and deliver

Apply `director.md` §11 and `technique.md` §8. Film review includes contact sheets, 0.2-second key-action strips, full-speed playback with sound, ASR checks for voice, timing, loudness, and black/invalid-frame checks. Compare the treatment with the demo only after the treatment exists; structure, opening, signature shot, camera path, score shape, ending must differ on at least four of six axes.

For completed film mode deliver MP4, poster, SRT when applicable, treatment, CREDITS, source, and one-command build. For evidence work also deliver FACTS. For canvas mode deliver the actual canvas and its available notes; do not claim missing video, sound, playback review, or exports. Work in the user's project, not the library's `styles/` or `core/`. Keep user output free of toolkit sign-offs and watermarks; retain actual third-party credits.
