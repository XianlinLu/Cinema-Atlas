# Character assets and stable voices

## 16:9 three-view character sheet

After script approval, enumerate the actual named/recurring visual characters. Create one real landscape **16:9** image per character showing front, side and back as three panels of the same identity, full body, equal scale and neutral pose. Lock face, age presentation, body proportions, hair, costume, colors and defining props to the approved script and selected style. Use clean separation and a neutral background; do not create three different people or add brand/celebrity details not approved by the script. Preserve original/cleared user assets when supplied.

Use the image tool's real ratio parameter and verify returned dimensions/preview; writing “16:9” in prose alone does not set a parameter. The turnaround-sheet ratio remains 16:9 even when a separately approved final film format is vertical. Inspect panel identity, full-body visibility, hands/feet, outfit consistency and missing views. Repair only failed sheets, present actual images, then obtain native approval.

Store CH001-style stable IDs, script version, master node/file ID, image version and approval. Keep the master sheet and derive an approved single-view identity reference when a video tool would mistake a triptych for three on-screen characters. This extraction is for composition/identity; do not crop a policy-rejected image to evade detection. A character portrait is an identity reference, not automatically a frame-composed first-frame image. First frames must have the film's approved composition and ratio.

## Voice direction and audition

For each role with approved lines, use native Question to choose a complete voice profile, informed by its confirmed characterization. Include language/accent, pitch, timbre, age presentation, pace, and emotional range. Use original synthetic voices or cleared recordings; do not infer consent to clone a real voice from a name, photograph, or project license. The narrator gets its own VO_NARRATOR entry and voice decision. A genuinely mute role gets no empty audio job.

Generate a playable **20–30 second** audition, aiming around 24 seconds when no preference specifies otherwise. Use original text with a neutral phrase and an emotional phrase, no background music, no song lyrics or imitation request. Check real duration, intelligibility, clean recording and performance. Use the chosen actual voice engine/profile; keep dry audio at natural pace. If a speech tool cannot produce that length in one request, generate compatible parts with the same voice, assemble and inspect one real audition before presenting it.

Link each audition node to the corresponding approved character image through supported canvas relations or the manifest, and label both with the stable role ID. Pass an image into an audio-generation port only if that tool explicitly accepts it; ordinary TTS does not require an image input. A narrator may have no image. Present the real audio and gather native approval for the actual candidate version. Store the returned reusable voice ID and/or approved audio asset ID. Do not put a human-readable nickname in a field that requires a real asset handle.

## Three different audio purposes

1. **Audition master:** the 20–30 second approved sample heard by the user. Archive it; do not attach every full audition to each video request.
2. **Voice identity excerpt:** a clean measured excerpt from the approved audition, often about 2.5–6 seconds, used only where the runtime video/speech tool accepts voice references. Choose a compliant speech-rich span rather than padding a fake empty sample. Apply current per-file, count and total audio limits across the entire request.
3. **Exact shot speech:** synthesize the approved script line with that locked voice, keep the exact wording, and measure its actual duration. This is what is spoken in the film. Never use the audition's unrelated test sentence as the shot dialogue.

Record audio purpose explicitly so the reference sample cannot be mistaken for a driving soundtrack. A short line can be shorter than a model's reference minimum; use a compliant identity excerpt or the tool's real audio-driving/lip-sync route. Only add legitimate lead/trailing room tone when that route supports it; never repeat/delete words or fabricate duration metadata to pass validation.

## Per-shot speaker ownership

For every dialogue or narration line, maintain: line ID, exact text, speaker ID, approved voice ID/version, synthesized audio ID, measured duration, speech placement and mouth rule. Validate that the voice owner matches the speaker. All visual character references come from the correct approved image versions. Never infer ownership from input-array order or from the model choosing a matching voice by itself.

An on-screen dialogue shot has one primary speaker. Other visible characters remain closed-mouth unless the approved script explicitly assigns another action; split speaker changes into separate atomic shots. Off-screen speech remains off-screen. Narration is a separate track and must not drive a visible character's lips. If narration and dialogue share a frame, preserve separate tracks/timing and validate overlaps against the script.

Generate exact shot speech while preparing the master table. Listen or use supported transcription checks for wording, pronunciation and voice consistency, and make previews available in table review. The accepted table must include these exact lines and audio versions. If a later repair changes a voice, wording or performance materially, reapprove through the native relevant gate; technical re-encoding without content change does not need a new gate.

## Video conditioning and final mix

Use a real voice-reference/audio-conditioning port when the model supports it, and explicitly map each attached asset to the intended role. If the model treats an audio reference as style only, it is not proof of exact lip-sync or exact text. Prefer the approved exact speech as a driving track when supported. Otherwise use the approved voice/reference plus exact prompt dialogue and verify output; route through a real lip-sync step when needed. Never claim synchronization based on prompt wording alone.

At editing, mute unwanted native video speech and place the approved character and narrator tracks at their locked times. Do not double the generated voice and the approved dry voice. Retain/rebuild original or cleared ambience, foley and music on separate tracks. Do not replace a mismatched lip performance with dry speech and claim it is fixed; correct the lip-sync with an actual supported tool or present the capability blocker through native recovery.
