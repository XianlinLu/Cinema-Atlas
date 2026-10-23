# Native Video Editor workflow / 原生后期流程

## Method and runtime

The requested reference was read at OpenFilm revision `cf6cd6fa9b3d4ee50dd963853ee6ca4f8354ecf4`:

- [Skill entry](https://github.com/openfilm/openfilm/blob/cf6cd6fa9b3d4ee50dd963853ee6ca4f8354ecf4/skills/openfilm/SKILL.md)
- [Full editing manual](https://github.com/openfilm/openfilm/blob/cf6cd6fa9b3d4ee50dd963853ee6ca4f8354ecf4/packages/openfilm/MANUAL.md)

Its core editing method is mapped to Lumina's native tools. HTML page rendering and OpenFilm-specific command syntax are not interpreted as Lumina capabilities. Music beat selection, per-shot approval and native modification cards implement the user's added requirements; the reference manual does not supply an automatic beat-detection algorithm.

| Editing method | Lumina execution requirement |
|---|---|
| Open the editable project before changing it | Open/reuse actual native Video Editor and store its returned project/draft IDs |
| Read the current project before each edit | Read actual latest draft; retain user locks, overrides and unrelated changes |
| Distinct visual, text and sound tracks | Native editable picture/caption/audio tracks and actual layering rules |
| Non-destructive source ranges and clip placement | Native source in/out and timeline positions; preserve original assets |
| Move shot sound with the picture | Preserve linked speech/foley placement and real lip-sync during ripple edits |
| Source-timed subtitles follow edits | Native timed captions or supported SRT/VTT import; recompute final placement after trim/rate changes |
| Inspect frames, sequence and sound before export | Native preview and actual playback/QC; document unavailable checks |
| Export when requested | User's final native confirmation authorizes exporting that exact revision and returning an accessible download |

## Required native decisions

`剧本确认 → 角色／重要道具配图确认（适用的合并卡片） → 角色试音要求 → 角色试音确认 → 镜头生产总表确认 → 每段分镜成片确认 → 后期制作方式 → 剪辑成片确认 ↔ 剪辑修改说明 → 导出下载`

The visual phase automatically extracts important close-up/recurring objects, including background props/decorations, alongside the cast. Generate real prop references and bind approved versions/states to their boards/shots under `skills/lumina-canvas-film/references/props-assets.md`. Initial props share the existing applicable visual review; newly discovered important objects receive targeted incremental review before dependent production, without restarting unrelated approved roles/voices.

Every required shot has its own approved current output version. A batch may contain one question for each shown clip if the native schema permits it. It never converts approval of one shot into approval of the rest.

The post-production card offers stitching only, subtitles only, both and native Other. Both immediately enables the two operations in the native editor. Subtitles only preserves the existing approved timeline or returns captioned individual clips, with no unrequested concatenation. Other captures the custom request through the card; explicit no-edit delivery is accurately labeled as source clips.

The final review shows the actual current editor preview/version. A request to keep modifying opens native card text for the target shot/time/track, the issue and desired change. The same editor draft is read and patched, with dependent captions/audio checked again. Approval is invalidated by subsequent changes. No main-chat “continue” or drawn imitation card is substituted.

## Generation defaults and source cleanup (v4.1)

Default to Seedance 2.5 and 16:9, with a ratio override only on explicit user instruction. Resolve actual Lumina identifiers rather than inventing an API name. Same-scene consecutive shots may use true extension only when action/time/identity/light/camera and source readiness/ratio are compatible. Different scenes or time jumps never extend the previous scene. Trim repeated source prefixes from extension results.

Before user shot review, remove ONLY model-generated background music using native audio operations or Video Editor. Preserve all intended dialogue, off-screen speech, narration, effects and ambience. Infer that sound plan from the approved script/action, not merely the presence of a visible speaker. Keep a no-music source audible. If a mixed source requires whole-mix muting, that remains intermediate until ALL intended sound is actually restored and synchronized in the playable prepared shot. Missing sound cannot be deferred to final editing or passed by a waveform/stream-presence check. Blocked outputs remain unavailable; missing native separation/composition is an honest blocker. This preparation does not authorize early stitching/subtitles.

All picture boundaries use hard cuts without automatic transition effects/overlaps. Final approved music remains a separate editor track, with beat-aware cutting and optional audio fades. Only BGM-free prepared shot versions can receive shot approval or enter final editing/continuation.

## Music, captions and delivery

Automatically fit original/cleared final music to actual content, mood, style and rhythm through native tools unless excluded or already specified. Do not add a routine questionnaire; show the real score in final review. Keep real separate picture, background-music, selected subtitle and effects tracks, with correct source/dedicated speech and no doubling. Native extraction of a mixed soundtrack does not prove isolated stems; required separation must be real. Use genuine beat/phrase observations and duck music under speech/effects. Preserve complete words, actions and pauses; do not invent BPM or force speech speed. Respect stitching/subtitle scope and explicit no-music choices.

The full runtime sound contract is bundled in `skills/lumina-canvas-film/references/audio-postproduction.md`. It requires audible shot QC before per-shot cards and audible final-mix/export checks. Only the user's approval of the current native preview/timeline/mix revision authorizes final whole-film export; changes require renewed review. Technical shot renders and review previews do not count as final delivery exports.

Subtitles derive from actual approved speech and timing, remain editable where supported and follow the final timeline. Merely mixing dry speech does not establish lip-sync. Final exported media must match the user's chosen operations and approved current draft, be playable and offer real download access. A cloud draft, fabricated link or queued export is insufficient.

## Validation boundary

This release verifies package contents, 59 complete style hashes, file counts, reference paths and length constraints. No new unit-test suite or paid media run was performed. Native tool availability, beat analysis, actual editor behavior and full end-to-end output still require verification in Lumina. The Skill cannot add unavailable tool APIs or guarantee platform acceptance.
