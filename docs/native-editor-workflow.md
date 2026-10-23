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

`剧本确认 → 角色三视图确认 → 角色试音要求 → 角色试音确认 → 镜头生产总表确认 → 每段分镜成片确认 → 后期制作方式 → 剪辑成片确认 ↔ 剪辑修改说明 → 导出下载`

Every required shot has its own approved current output version. A batch may contain one question for each shown clip if the native schema permits it. It never converts approval of one shot into approval of the rest.

The post-production card offers stitching only, subtitles only, both and native Other. Both immediately enables the two operations in the native editor. Subtitles only preserves the existing approved timeline or returns captioned individual clips, with no unrequested concatenation. Other captures the custom request through the card; explicit no-edit delivery is accurately labeled as source clips.

The final review shows the actual current editor preview/version. A request to keep modifying opens native card text for the target shot/time/track, the issue and desired change. The same editor draft is read and patched, with dependent captions/audio checked again. Approval is invalidated by subsequent changes. No main-chat “continue” or drawn imitation card is substituted.

## Generation defaults and source cleanup (v4.1)

Default to Seedance 2.5 and 16:9, with a ratio override only on explicit user instruction. Resolve actual Lumina identifiers rather than inventing an API name. Same-scene consecutive shots may use true extension only when action/time/identity/light/camera and source readiness/ratio are compatible. Different scenes or time jumps never extend the previous scene. Trim repeated source prefixes from extension results.

Before user shot review, remove model-generated background music from each successful clip using native audio operations or Video Editor. Preserve the raw source and record the prepared output. If music and speech are mixed, separate BGM where supported, or mute that original mix and restore exact approved dry speech/necessary sound with real sync. Do not deliver missing dialogue or claim an unavailable stem control. Blocked/rejected outputs remain unavailable under the existing policy rules. This pre-review normalization does not authorize stitching/subtitles early.

All picture boundaries use hard cuts without automatic transition effects/overlaps. Final approved music remains a separate editor track, with beat-aware cutting and optional audio fades. Only BGM-free prepared shot versions can receive shot approval or enter final editing/continuation.

## Music, captions and delivery

Use actual selected music and genuine beat/phrase observations. Cut on narratively valid accents, preserving complete speech, actions and pauses. Do not fabricate BPM, drop words or accelerate dialogue for a beat. A substantive content/music change gets a native decision.

Subtitles derive from actual approved speech and timing, remain editable where supported and follow the final timeline. Merely mixing dry speech does not establish lip-sync. Final exported media must match the user's chosen operations and approved current draft, be playable and offer real download access. A cloud draft, fabricated link or queued export is insufficient.

## Validation boundary

This release verifies package contents, 59 complete style hashes, file counts, reference paths and length constraints. No new unit-test suite or paid media run was performed. Native tool availability, beat analysis, actual editor behavior and full end-to-end output still require verification in Lumina. The Skill cannot add unavailable tool APIs or guarantee platform acceptance.
