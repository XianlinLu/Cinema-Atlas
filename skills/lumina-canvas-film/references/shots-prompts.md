# Shot production table and video prompts

Method sources, used for process only:

- https://bytedance.larkoffice.com/docx/Zv1fdJiTdoTcl6xaCBHc8Litn1b
- https://bytedance.larkoffice.com/wiki/MmDTwvNxfi30INkSW2tcEOxDnpc

Do not import their sample characters, stories, dialogue, props or aesthetics. The current user specifies character and voice approval before the final production table, and automatic execution after table approval. Those requirements govern the sequence. The training document's controlled-extension safeguards govern over the older blanket “continue every later shot” template.

## Authoritative master table

Create a full versioned artifact; a short summary cannot replace it. Preserve source script line IDs and exact approved text. Group by scene and assign stable scene, shot and board IDs. Each atomic shot has one main action, one camera setup/path, and one on-screen speaker. Change of scene, time, camera, or speaker normally starts another shot.

The visible compact table follows the training document's six execution columns:

| 镜头与场景 | 分镜板 | 时长与时间轴 | 动作、机位与台词 | 锁定资产、模式与依赖 | 状态、失败原因与验收 |
|---|---|---|---|---|---|
| Stable scene/shot ID and source line mapping | Actual board/start-frame ID, or explicit not-needed status | Measured speech, head/tail handles, integer shot duration, project start/end | Framing/angle/move, action, exact speaker/text, mouth/lighting/state | Approved character/scene/prop/voice/audio IDs and versions; independent or true extension; actual predecessor | Planned, running, generated, checked, user-approved/locked or blocked; reason and output ID |

Keep detailed machine-readable rows alongside the visible table. Required speech mapping is line ID → exact text → speaker ID → voice ID/version → actual shot-audio ID/duration. Store source-line coverage, shot/board relationship, image IDs, reference-audio purpose, local and project timelines, expected output, task kind/model profile and scene-boundary flags. State what is actually approved; “tool succeeded” is not “user approved.” After every revision save the entire table, retaining its version and changed-row history.

For prompt-production/export, provide one section per scene with four source-SOP columns: **输入图/视频 | 提示词 | 生成视频 | 注意事项**. Link these rows to master shot IDs, source line ranges, real asset nodes and resulting clip IDs. Do not mix different scenes in one table. Mark missing inputs visibly as blockers; placeholders and nonexistent @assets must not be sent to generation.

## Timing from measured performance

Before final table approval, synthesize each exact dialogue/narration line with the approved voice and measure it. Reserve at least the intended 0.3-second lead and 0.4-second tail by default. Choose natural action/reading/emotion holds. A dialogue shot must satisfy measured speech plus handles ≤ its actual duration. Split long lines across coherent shots if the model maximum would be exceeded, preserving every word and a traceable line-span mapping. Never shorten text or speed speech just to fit.

The SOP's written prompt timelines use integer seconds and ordinary half-up rounding, not Python's ties-to-even rounding. First organize/merge shots, then allocate integer segment durations, then derive contiguous boundaries from their cumulative sum. Ensure every interval has positive length, begins at the previous end and ends at the shot's total duration. Audio-fit constraints are a floor: if nearest-second rounding would cut speech, increase to the next valid second rather than clipping it. Project shot boundaries are cumulative; do not round independent start/end values into gaps.

For shots at or below four seconds, assess merge eligibility rather than blindly merging. Same scene/time, same identity/costume/light and directly connected action may be merged only if the atomic action, camera, speaker, approved dialogue and all visual requirements remain coherent. Never merge across scenes, conflicting camera instructions, a speaker change, a reveal or a deliberate emotional pause. Record the exact original line/row range. If it cannot merge, use a supported duration with a motivated hold or a user-approved edit; do not generate zero-second rows.

Total film duration is the locked sum after measured speech, intentional transitions and approved edit overlap. Show that sum at table review. A model's 30-second maximum is a ceiling per request, not a reason to generate thirty seconds of unrelated shots together.

## Deterministic prompt construction

For each table row, resolve actual assets before writing the final request. Use supported attachment/connection syntax; @labels are only illustrative until bound to a real uploaded asset. Write, in order:

1. True-extension opener only for a validated extension; otherwise no “continue this video” instruction.
2. Selected catalog style grammar, scene/place/time/light, identity/costume/prop anchors and composition.
3. One exact integer total duration supported by the selected task/model.
4. Contiguous local time intervals: framing → one compatible camera path → subject action/expression/gaze/hands → exact dialogue or silence → relevant environment change.
5. Explicit speaker-to-voice/audio mapping, mouth rules, unchanged identity/space/light, ending pose and separate unambiguous prohibitions where needed.

No alternative actions, “approximately” timed beats, random weather, guessed assets, additional dialogue or model-chosen ending. Avoid conflicts such as “static camera” and “continuous tracking” for the same interval. Use the selected style's own vocabulary instead of sample SOP genres or named copyrighted movies/characters. Do not add long lists of unrelated negative terms.

Generate/use scene and prop anchors from the approved script as needed. Create a fresh board when camera position, framing, staging, axis or scene changes. A shared board must depict the starting state, not the action's completed result. Reconnect the correct locked assets on every shot; the previous video/last frame cannot substitute for identity references.

## Independent generation and true extension

Default to independent atomic shots. The older batch template's “续写这个@视频。” is conditional: use it only when the actual tool truly extends the input timeline, the source clip is usable/approved for this operation, the same scene/time/costume/action continues, and required identity assets can still be connected. A video-reference port alone does not prove true extension. Never carry an extension dependency across a scene boundary.

Read the runtime extension schema. The output ratio follows the source; omit ratio if optional, or use the schema's adaptive value if required. Do not send a forced 16:9 ratio with an extension task. Ensure the existing source is already in the intended film ratio. First-frame/last-frame modes may have similar model-specific adaptive-ratio requirements; validate rather than assuming normal reference-generation rules.

If native extension returns source-plus-new footage, measure it and use only the newly generated span on the edit timeline. Do not repeatedly concatenate the source prefix. If continuity or task capabilities fail, revert the affected row to a supported independent shot with the same approved content. Do not mislabel a separate generated shot as a true extension.

## Automatic production and QC

After native table approval, process all rows automatically with bounded concurrency. Speech/voice/identity assets must exist, be approved, and match current versions. Inspect each generated clip against its row: correct identity and outfit, expected speaker/line, other mouths closed, readable action/camera, ratio, actual length, and no missing or duplicate content. Rework only failed rows and dependencies; a creative change reopens the corresponding native gate.

Keep edit-ready clip trim in/out and dialogue/narration placements. Table approval authorizes routine automated QC and assembly; do not introduce per-shot “please continue” conversations. Assemble every successful required row, remove repeated extension prefixes, use the approved speech tracks, finish sound/subtitles as specified, and verify the exported movie actually exists and plays.
