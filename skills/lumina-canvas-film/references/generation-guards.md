# Request preflight, observed errors and recovery

## Evidence and scope

User screenshots show the Lumina route `dreamina-seedance-2-5` in r2v returning audio-duration bounds, ratio/task-type constraints, and copyright-related policy failures. These are provider responses, not proof that every Seedance endpoint has the same schema. Query the current tool/model profile; use its supported names, task modes, formats, durations, counts, ratio rules and error details.

Official public reference (verify the active route before applying):
https://docs.volcengine.com/docs/ark/create-video-generation-task-api?lang=zh

At this package's update, the public Seedance 2.5 documentation specifies reference audio in [2,30] seconds, at most 10 reference-audio files and ≤30 seconds total. The 2.0 family specifies [2,15], at most 3 and ≤15 seconds total. This is distinct from the user's screenshots' internal 1.8-second minimum and 30.2-second total tolerance. Choose the stricter valid runtime contract, not the tolerance edge. These values apply to reference inputs, not to a story's total running time or the length of archived auditions.

## Before every media request

Verify the real operation/model profile; dependency approvals and versions; accessible, ready asset IDs; correct owners/roles; measured metadata rather than requested metadata; count/size/type constraints; intended duration and output ratio; and a unique job/request fingerprint. Never submit placeholder URLs, a character name as an asset ID, a failed audio node, or an unapproved candidate. Query existing pending jobs before resubmission.

Store role-aware reference inputs explicitly. Sum the actual durations of ALL attached audio files in the request, including music/narration where that route counts them. Count duplicate attachments as the API does. Do not use file names, a requested “25 seconds,” or rounded UI labels as measured duration.

Evidence and documentary styles may require genuine imagery, archive records or measurements. Keep those requirements from the full selected specification; do not synthesize source evidence and label it real. If the available assets cannot support that style, offer an actual supported source or style revision through the native gate before production.

Prefer clean 2.5–6 second identity excerpts from approved auditions where the active limits permit. Keep a margin below the current aggregate limit (for a 30-second route, target ≤29.5 seconds; for a 15-second route, ≤14.5 seconds). Do not attach whole 20–30 second auditions for multiple roles. A silent shot has no reference audio unless an actual planned non-speech use requires it; do not create zero-length dummy audio.

For exact speech conditioning, validate the actual audio's role separately from voice identity. Keep long exact lines split at approved speech/action boundaries. Do not delete words, accelerate delivery, pad false metadata or silently swap owners to satisfy the request. If a measured sample is too short, select a longer clean portion of the approved master or use a genuinely supported audio-driving path.

## Observed errors and bounded repairs

| Response | Meaning indicated by response | Correct action |
|---|---|---|
| InvalidParameter: audio total duration must be ≤30.2 seconds | Aggregate audio references too long on the pictured route | Measure all inputs; derive shorter clean approved excerpts; remove duplicate/unneeded references; revalidate the stricter runtime sum before retry |
| InvalidParameter: audio duration must be ≥1.8 seconds | A pictured reference file is too short | Identify the indexed content item; use a compliant speech-rich approved excerpt (normally ≥2 seconds on the public 2.5 route), then measure and retry |
| InvalidParameter.TaskTypeConstraint: ratio for video extension | Output ratio is inherited from source | Inspect task kind and source; omit ratio or use required adaptive according to actual schema; keep source ratio aligned with project |
| InputImageSensitiveContentDetected.PolicyViolation / 23010 | Provider rejected an input image, with copyright indicated in the shown message | Stop blind retries; identify the flagged input when reported; native recovery offers provider review or a genuinely different cleared/original asset requiring approval |
| OutputVideoSensitiveContentDetected.PolicyViolation / 23007 | Provider rejected generated video, with copyright indicated | Preserve logs/request IDs; stop retries aimed at evasion; native recovery offers substantive original-content revision/legitimate alternative or provider review |
| OutputAudioSensitiveContentDetected.PolicyViolation | Provider rejected generated audio, with copyright indicated | Native recovery for provider review or a genuinely new original voice/music choice; reapprove changed audio and invalidate its dependent shots |
| 429, timeout, temporary 5xx | Capacity/network failure rather than a creative decision | Poll the same accepted task; for confirmed failed/transient submission use bounded backoff and actual idempotency support |

For a deterministic parameter error, make one diagnosed correction and revalidate; if it still fails, inspect the new error and allow at most one further distinct technical correction. Do not rerun unchanged invalid payloads. For transient errors, use at most two resubmission attempts after checking for an existing accepted job. Respect Retry-After and host scheduling. Polling a running job is not a resubmission.

Policy failures have **no automatic evasion retries**. Do not crop/blur/remove watermarks, rename the same protected character, hide semantic terms, disguise voice identity, or switch endpoints as a way to get the same blocked content through. A rights statement may support provider review but does not override the provider's technical rejection. A genuinely original redesigned asset is a creative revision: describe it honestly in a native choice, obtain approval, regenerate it, and update only affected dependencies. Do not promise that original assets or these checks eliminate all false positives.

## Ratio and task type

Use an explicit ratio in ordinary reference/text generation only when that task schema permits. For real extension the source ratio controls the result; omit the field if allowed, otherwise choose the required adaptive value. Do not assume an omitted field will work if it is required. On the public 2.5 API, edit, extension and first/last-frame tasks have adaptive-ratio restrictions; internal Lumina aliases may express them differently. Build first-frame boards at the intended output ratio; a cropped portrait is not a 16:9 scene frame.

Do not change a 9:16 source into a 16:9 extension by forcing a parameter. Use a supported independent shot at the approved ratio or a legitimate composition/edit route. Avoid extension mode entirely when it is not actually needed. Preserve task intent rather than adding a video reference that unexpectedly turns an independent job into an extension.

## Failure ownership and finish criteria

Write the failed stage, shot/character/voice ID, node/task/request/log IDs, exact error code, measured request properties, attempts and next action into the manifest. Repair at that stage. Never discard approved unrelated assets or mark a blocked shot successful to finish a progress list. Native recovery choices are for actual user decisions; routine metadata fixes continue automatically.

At completion, verify all shot IDs have usable real outputs, the final edit includes each required shot once, output ratio/actual duration are correct, exact approved dialogue and narrator audio are present, lips match, and no background task remains necessary for the film. If a host tool or runtime continuation is missing, state the concrete limitation; a text Skill cannot supply missing infrastructure.

## Optional executable checks

The repository has `tools/lumina_preflight.py` outside this import folder. Where the repository and execution tools are actually available, normalize the real request plus current endpoint limits and run its request check; normalize the versioned production manifest and run its project check before downstream jobs. Run its completion check against actual exported metadata and observation results before declaring the film complete. This is validation only and submits no media. Do not assume that file exists in a Lumina session, or paste its example schema directly into a provider request.

The normalized request uses `model_id`, `operation`, `duration_seconds`, submitted `ratio`, intended `target_ratio`, measured `audio_refs`, and `source_video` for extension. Each reference stores the actual asset ID, ready state, format and duration. The profile records current audio per-file/count/aggregate limits, video bounds and task-specific ratio rules. Project validation records approved versioned script/table, approved character `sheet` records, approved `voices` with owners, exact `script.lines`, shot start/end/duration, current image/voice version references, dialogue audio metadata and mouth rules. The source of each field is the real host state; no inferred approval or metadata is acceptable.
