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

Total film duration follows measured speech and approved hard-cut shot boundaries; do not add transition overlaps by default. Show that sum at table review. A model's 30-second maximum is a ceiling per request, not a reason to generate thirty seconds of unrelated shots together.

## Deterministic prompt construction

For each table row, resolve actual assets before writing the final request. Use supported attachment/connection syntax; @labels are only illustrative until bound to a real uploaded asset. Write, in order:

1. True-extension opener only for a validated extension; otherwise no “continue this video” instruction.
2. Selected catalog style grammar, scene/place/time/light, identity/costume/prop anchors and composition.
3. One exact integer total duration supported by the selected task/model.
4. Contiguous local time intervals: framing → one compatible camera path → subject action/expression/gaze/hands → exact dialogue or silence → relevant environment change.
5. Explicit speaker-to-voice/audio mapping, mouth rules, unchanged identity/space/light, ending pose and separate unambiguous prohibitions where needed.

No alternative actions, “approximately” timed beats, random weather, guessed assets, additional dialogue or model-chosen ending. Avoid conflicts such as “static camera” and “continuous tracking” for the same interval. Use the selected style's own vocabulary instead of sample SOP genres or named copyrighted movies/characters. Do not add long lists of unrelated negative terms.

Generate/use scene and prop anchors from the approved script as needed. Create a fresh board when camera position, framing, staging, axis or scene changes. A shared board must depict the starting state, not the action's completed result. Reconnect the correct locked assets on every shot; the previous video/last frame cannot substitute for identity references.

## Scene-aware independent generation and true extension

Classify every row by scene_id and real temporal/action continuity. For consecutive shots in the SAME scene/time with compatible costume/light/action/camera, a ready QC-passed BGM-free predecessor at project ratio and actual native extension support, true extension is eligible. Otherwise generate an independent atomic shot. Different scenes, time jumps or broken action never use extension or the prior scene's last frame as continuation. A shared location or video-reference port is insufficient. Record source ID/version and the mode reason; the table approval authorizes those dependencies. Preserve the current approved identity/voice assets on extensions.

Read the runtime extension schema. The output ratio follows the source; omit ratio if optional, or use the schema's adaptive value if required. Do not send a forced 16:9 ratio with an extension task. Ensure the existing source is already in the intended film ratio. First-frame/last-frame modes may have similar model-specific adaptive-ratio requirements; validate rather than assuming normal reference-generation rules.

If native extension returns source-plus-new footage, measure it and use only the newly generated span on the edit timeline. Do not repeatedly concatenate the source prefix. If continuity or task capabilities fail, revert the affected row to a supported independent shot with the same approved content. Do not mislabel a separate generated shot as a true extension.

## Automatic production and QC

Apply the Video sound planning and output-audio policy failures rules below. Lock each shot’s audio source and real synthesis/lip-sync route in table review before submitting. A terminal policy-blocked shot is isolated from independent jobs, not retried as a transient error.

After native table approval, process all rows automatically with bounded concurrency. Speech/voice/identity assets must exist, be approved, and match current versions. Inspect each generated clip against its row: correct identity and outfit, expected speaker/line, other mouths closed, readable action/camera, ratio, actual length, and no missing or duplicate content. Rework only failed rows and dependencies; a creative change reopens the corresponding native gate.

Keep edit-ready clip trim in/out plus dialogue/narration/effect/ambience cues. Table approval authorizes generation, technical QC and native removal of ONLY model BGM. Follow `audio-postproduction.md`: actual prepared playback must contain all expected voices/effects/ambience before QC_READY and per-shot review. No speaking/effects shot may be silent pending future restoration. Obtain per-shot approval and post-production scope before requested stitching/subtitle editing. Follow production-workflow.md for native Video Editor, automatic final scoring, separate sound-role tracks, optional subtitles, final revision approval and real downloadable export. No extra “continue” request between technical jobs.

---

# Request preflight, observed errors and recovery

## Evidence and scope

User screenshots show the Lumina route `dreamina-seedance-2-5` in r2v returning audio-duration bounds, ratio/task-type constraints, and copyright-related policy failures. These are provider responses, not proof that every Seedance endpoint has the same schema. Query the current tool/model profile; use its supported names, task modes, formats, durations, counts, ratio rules and error details.

Official public reference (verify the active route before applying):
https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh

At this package's update, the public Seedance 2.5 documentation specifies reference audio in [2,30] seconds, at most 10 reference-audio files and ≤30 seconds total. The 2.0 family specifies [2,15], at most 3 and ≤15 seconds total. This is distinct from the user's screenshots' internal 1.8-second minimum and 30.2-second total tolerance. Choose the stricter valid runtime contract, not the tolerance edge. These values apply to reference inputs, not to a story's total running time or the length of archived auditions.

## Before every media request

Default to Seedance 2.5 and project 16:9 unless the user explicitly requested another ratio; bind actual native model/schema and use the eligible scene-aware mode. Verify the real operation/model profile; dependency approvals and versions; accessible, ready asset IDs; correct owners/roles; measured metadata rather than requested metadata; count/size/type constraints; intended duration and output ratio; and a unique job/request fingerprint. Never submit placeholder URLs, a character name as an asset ID, a failed audio node, or an unapproved candidate. Query existing pending jobs before resubmission.

Store role-aware reference inputs explicitly. Sum the actual durations of ALL attached audio files in the request, including music/narration where that route counts them. Count duplicate attachments as the API does. Do not use file names, a requested “25 seconds,” or rounded UI labels as measured duration.

Evidence and documentary styles may require genuine imagery, archive records or measurements. Keep those requirements from the full selected specification; do not synthesize source evidence and label it real. If the available assets cannot support that style, offer an actual supported source or style revision through the native gate before production.

Prefer clean 2.5–6 second identity excerpts from approved auditions where the active limits permit. Keep a margin below the current aggregate limit (for a 30-second route, target ≤29.5 seconds; for a 15-second route, ≤14.5 seconds). Do not attach whole 20–30 second auditions for multiple roles. A silent shot has no reference audio unless an actual planned non-speech use requires it; do not create zero-length dummy audio.

For exact speech conditioning, validate the actual audio's role separately from voice identity. Keep long exact lines split at approved speech/action boundaries. Do not delete words, accelerate delivery, pad false metadata or silently swap owners to satisfy the request. If a measured sample is too short, select a longer clean portion of the approved master or use a genuinely supported audio-driving path.

## Observed errors and bounded repairs

| Response | Meaning indicated by response | Correct action |
|---|---|---|
| Pre-execution/canvas result synchronization failure | Orchestration sync failed; acceptance and actual old/new task state require evidence | Follow runtime-control.md: reuse nodes, inspect real raw result/status, use at most 3 additional non-generating reconciliation attempts; confirmed NOT_ACCEPTED may submit only after sync is healthy, accepted tasks are polled, unknown acceptance is never blindly resubmitted |
| InvalidParameter: audio total duration must be ≤30.2 seconds | Aggregate audio references too long on the pictured route | Measure all inputs; derive shorter clean approved excerpts; remove duplicate/unneeded references; revalidate the stricter runtime sum before retry |
| InvalidParameter: audio duration must be ≥1.8 seconds | A pictured reference file is too short | Identify the indexed content item; use a compliant speech-rich approved excerpt (normally ≥2 seconds on the public 2.5 route), then measure and retry |
| InvalidParameter.TaskTypeConstraint: ratio for video extension | Output ratio is inherited from source | Inspect task kind and source; omit ratio or use required adaptive according to actual schema; keep source ratio aligned with project |
| InputImageSensitiveContentDetected.PolicyViolation / 23010 | Provider rejected an input image, with copyright indicated in the shown message | Stop blind retries; identify the flagged input when reported; native recovery offers provider review or a genuinely different cleared/original asset requiring approval |
| OutputVideoSensitiveContentDetected.PolicyViolation / 23007 | Provider rejected generated video, with copyright indicated | Preserve logs/request IDs; stop retries aimed at evasion; native recovery offers substantive original-content revision/legitimate alternative or provider review |
| OutputAudioSensitiveContentDetected.PolicyViolation from BALLMVideo | Generated video audio rejected, with possible copyright restrictions; not evidence of a TTS input-ID failure | Apply the sound-plan and policy-recovery rules below; preserve successful shots, deduplicate the same task error, use native review for substantive original revisions or provider review, and reapprove affected assets/table rows. No unchanged or mute-and-retry bypass |
| GenInputsFromPipeline: validate audit content 0: content id is empty / code 15000 in this screenshot | An input content identifier was empty during pipeline validation; the input type/root cause is not shown | Apply the Batch speech inputs and empty-content recovery rules below: inspect exposed inputs and readiness, resolve/register actual required handles, remove unintended empty optional references, repair only the failed role, then retry once after repair; persistent internal failure needs platform investigation |
| 429, timeout, temporary 5xx | Capacity/network failure rather than a creative decision | Poll the same accepted task; for confirmed failed/transient submission use bounded backoff and actual idempotency support |

For a deterministic parameter error, make one diagnosed correction and revalidate; if it still fails, inspect the new error and allow at most one further distinct technical correction. Do not rerun unchanged invalid payloads. For confirmed transient GENERATION-SUBMISSION failures, use at most two resubmission attempts after resolving every prior attempt's acceptance. A missing ID, timeout or one empty listing is not proof of non-acceptance. Canvas/read synchronization has its separate bounded, non-generating recovery in runtime-control.md; never spend that read budget on execute calls or use it to increase billable retry limits. Respect Retry-After and actual host scheduling. Polling a healthy accepted job is not resubmission. Persistent faults require saved recovery, not a fabricated promise to wake later.

Policy failures have **no automatic evasion retries**. Do not crop/blur/remove watermarks, rename the same protected character, hide semantic terms, disguise voice identity, or switch endpoints as a way to get the same blocked content through. A rights statement may support provider review but does not override the provider's technical rejection. A genuinely original redesigned asset is a creative revision: describe it honestly in a native choice, obtain approval, regenerate it, and update only affected dependencies. Do not promise that original assets or these checks eliminate all false positives.

## Ratio and task type

Use an explicit ratio in ordinary reference/text generation only when that task schema permits. For real extension the source ratio controls the result; omit the field if allowed, otherwise choose the required adaptive value. Do not assume an omitted field will work if it is required. On the public 2.5 API, edit, extension and first/last-frame tasks have adaptive-ratio restrictions; internal Lumina aliases may express them differently. Build first-frame boards at the intended output ratio; a cropped portrait is not a 16:9 scene frame.

Do not change a 9:16 source into a 16:9 extension by forcing a parameter. Use a supported independent shot at the approved ratio or a legitimate composition/edit route. Avoid extension mode entirely when it is not actually needed. Preserve task intent rather than adding a video reference that unexpectedly turns an independent job into an extension.

## Failure ownership and finish criteria

Write the failed stage, shot/character/voice ID, node/task/request/log IDs, exact error code, measured request properties, attempts and next action into the manifest. Repair at that stage. Never discard approved unrelated assets or mark a blocked shot successful to finish a progress list. Native recovery choices are for actual user decisions; routine metadata fixes continue automatically.

At completion, verify current per-shot user approvals, post-production scope, final native editor revision approval and actual downloadable export under production-workflow.md. Preserve approved shot/line coverage, correct ratio/duration, speech/narration and lip-sync; no required background job remains. If a host tool or runtime continuation is missing, state the concrete limitation; a text Skill cannot supply missing infrastructure.

## Optional executable checks

The repository has `tools/lumina_preflight.py` outside this import folder. Where the repository and execution tools are actually available, normalize the real request plus current endpoint limits and run its request check; normalize the versioned production manifest and run its project check before downstream jobs. Its checks supplement, and do not implement or replace, v4 per-shot/post-production/final-approval requirements; follow production-workflow.md and runtime-control.md for completion. This is validation only and submits no media. Do not assume that file exists in a Lumina session, or paste its example schema directly into a provider request.

The normalized request uses `model_id`, `operation`, `duration_seconds`, submitted `ratio`, intended `target_ratio`, measured `audio_refs`, and `source_video` for extension. Each reference stores the actual asset ID, ready state, format and duration. The profile records current audio per-file/count/aggregate limits, video bounds and task-specific ratio rules. Project validation records approved versioned script/table, approved character `sheet` records, approved `voices` with owners, exact `script.lines`, shot start/end/duration, current image/voice version references, dialogue audio metadata and mouth rules. The source of each field is the real host state; no inferred approval or metadata is acceptable.

---

## Batch speech inputs and empty-content recovery

Keep one immutable job record per role/line: owner, chosen profile/version, exact nonblank text, real operation, required ready inputs and fingerprint. Never share a mutable role input list. Run the first REAL requested audition end to end, without an extra paid diagnostic clip; default remaining ready roles to a serial automatic queue. Increase concurrency only with explicit service support and healthy resolved jobs. No user continue action is needed between roles.

Resolve only the active route's required inputs. Existing-voice TTS needs actual compatible voice settings and text; supported original voice design may use profile fields without a prior voice ID. Never make an audition depend on its own future output. Character/audio association is logical unless the audio operation explicitly needs an image. Do not attach the whole canvas, unnecessary images, failed nodes, empty strings/null reference items or placeholder handles. Omit absent optional inputs; unresolved required inputs block that role. Use real upload/registration/resolution results and readiness/access where exposed. Node/task/voice/asset/internal content IDs are distinct; never substitute or fabricate them. Use supported inline text paths when available; do not invent internal registration fields.

`GenInputsFromPipeline ... validate audit content 0: content id is empty` / code 15000 in the screenshot is input-resolution validation. It does not identify the missing input type/root cause, prove empty speech or excessive concurrency, or mean copyright rejection. The numeric code alone is not a universal definition; a global success toast is not that node's success.

Record the affected role/node and exact error; query any accepted task. Inspect actual exposed inputs/producer states if possible, without fabricating unavailable inspection. Poll supported pending registration, repair missing/stale bindings using supported registration/reattachment/refresh, omit unintended optional empties and revalidate. Do not poll a terminal invalid input forever. Recreate only that audio node if supported and necessary; preserve source images and correct outputs. Retry once AFTER an observed repair, within the overall two technical-correction maximum. No unchanged retry loop or regeneration of approved artwork solely to obtain an ID. If valid external inputs still produce an internally empty ID, preserve logs for platform investigation and block that role. Continue independent ready jobs; unresolved roles get native recovery and cannot advance to approval/downstream shots. Mark audio generated only when its actual output resolves and plays; verify measured duration/text/owner.

## Video sound planning and output-audio policy failures

Before initial shot submission/table approval, lock each shot's exact dialogue/narration IDs and owners/versions, planned music/ambience sources, whether native sound synthesis is needed, and actual lip-sync/edit route. Use original scripts/auditions and original synthetic profiles or supplied cleared sources. Do not request exact celebrity impressions, known songs/movie scores/lyrics or demo audio. Preserve catalog names and concrete media grammar; they do not authorize copying sample content. Do not silently rewrite approved text or invent source clearance.

Default to preserving intended voices, scene effects and ambience while avoiding model background score. A global audio-off switch removes all native sound; it is NOT a music-only switch. Only plan picture-only generation when actual native speech/effect production, lip-sync and composition are resolved from the start, with ALL intended sound restored into audible prepared playback BEFORE shot review/continuation reuse. Never use silent picture as the default cleanup result or defer restoration until final editing. Public Seedance documents `generate_audio=false`; do not assume Lumina exposes it or copy it into an unsupported schema. Prefer actual integrated sound with approved voices/exact lines and no background score when supported. Keep speech/effect cues in the authoritative table; bind only real required inputs. A style reference proves neither exact speech nor lip-sync. Apply `audio-postproduction.md` for BGM-only separation/reconstruction and audible checks. Final automatic/selected score belongs on the native editor's separate music track, never in source shots. Do not silently change an approved route or declare missing voices/effects complete.

`OutputAudioSensitiveContentDetected.PolicyViolation` from BALLMVideo means the generated video's audio was rejected, with possible copyright restrictions in the shown message. It does not identify a song, prove infringement or reject the prior audition by implication. Deduplicate repeated notifications for the same task/log; the two supplied screenshots were one failure. Treat policy errors separately from technical/transient retries.

Mark POLICY_BLOCKED, save exact prompt/task/node/log/request IDs and sound map, and retain successful independent jobs. No unchanged resubmission, random-seed/model/endpoint switching, disguised names, pitch/speed tricks, blocked-result extraction or automatic mute-and-retry to get rejected content through. Do not use an existing separate-track plan as permission to extract a blocked video. Use only outputs actually released as successful. Follow the detailed no-evasion rules in production-requests.md.

At the dependency barrier use a native recovery card: provider review, a substantively new original voice/music/content proposal for approval, or save/pause. Supply the user a support summary; do not contact support without authorization. A separate-production alternative must be permitted, supported and genuinely resolve the issue, not bypass moderation. Changed voice/script/table/shot approvals are invalidated only where dependent; regenerate and reapprove real revisions before proceeding. Rights statements do not override provider rejection. No skipped shot, fictitious pass or incomplete export to finish a checklist. Original material and these checks cannot guarantee zero false positives; persistent internal/provider issues need platform investigation.

