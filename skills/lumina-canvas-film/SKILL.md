---
name: lumina-canvas-film
description: Run Lumina's full video production workflow from one idea. Draft the complete script, obtain native Question-card approval, create and approve 16:9 character turnarounds, ask each character's voice preferences, generate and approve 20–30 second auditions, approve a shot production master table, then automatically generate all shots and assemble the finished film. Preserve character/voice identity and preflight media parameters.
---

# Cinema Atlas · Automated Video Director

The user's latest production sequence governs execution. The bundled style documents supply the complete visual grammar; their demo engines and earlier code-only workflows do not override this native image/audio/video pipeline. Produce real media with the host's tools. A script, canvas note, submitted first job, or collection of unassembled clips is not a completed film.

## Start with one idea

Read `references/workflow.md`, `references/selection-ui.md`, and `references/generation-guards.md`. Inspect the current tool schemas for native questions, image generation, speech generation with reusable voice identity, video generation, task status, editing/composition, and automatic continuation. The current Lumina UI displays its native question tool as **Question**; bind to the actual runtime name and schema rather than inventing one.

Infer a coherent story and fitting style from the user's idea without a preliminary questionnaire. Honor a specified library style; otherwise choose a suitable entry from `references/style-index.md` and include the choice in the script review. Read all marked fragments for the selected slug from its listed `references/style-specs-*.md` files, following truncated reads to completion. Use one fixed style except where that style itself specifies multiple media. Do not copy demo plots, characters, or source-document examples.

## Mandatory stage sequence

1. **Full script → 剧本确认.** Write the full story, scenes, exact dialogue/narration, named characters, settings, essential props, and ending. Derive total duration from dramatic rhythm and natural speech, not a fixed 30/45/60-second quota. Explain the proposed duration and style. Present the full artifact, call the native approval card, and wait for its returned decision. No character/audio/video generation before approval.
2. **Character art → 角色三视图确认.** Read `references/characters-voices.md`. For every actual recurring visual character, generate one real 16:9 sheet containing front, side, and back views of the same character. Inspect and present the sheets, then call the native approval card. Lock approved asset IDs and versions. A narrator without an on-screen body does not need a fabricated portrait.
3. **Voice direction → 角色试音要求.** For each speaking character and narrator, ask voice choices through native options, using the confirmed character/personality as context. Supply complete recommended profiles so normal use requires clicks rather than typing. Keep narrator identity separate. Do not infer voice identity from a picture or silently clone a real person.
4. **Real audition audio → 角色试音确认.** Generate an original dry audition of approximately 20–30 seconds for each speaking role using the selected profile. Present playable audio connected to the corresponding character asset. Ask for native approval. Lock the actual voice/asset identifier; an adjective or voice name is not an audio asset. Non-speaking roles remain silent rather than receiving dummy audio.
5. **Shot production master table → 镜头生产总表确认.** Read `references/shots-prompts.md`. Build the complete, versioned table from the approved script and locked images/voices. Prepare exact per-shot speech using those voices and measure it before locking shot durations. Include scene/shot IDs, source-line mapping, framing/action/camera, exact speaker/text, image/voice/audio IDs, mode/dependencies, duration, status and failure reasons. Present the whole table with usable audio previews; obtain native approval before shot-video submission.
6. **Generate every shot automatically.** Resolve real input assets, validate request parameters, submit, poll or register real continuation, inspect output, and repair only failed shots within the retry rules. Use the approved master table as the sole job queue. All on-screen speakers and narration use their approved voice assets; reference auditions are not the spoken script. Preserve completed shots, asset locks, and revision history.
7. **Assemble, inspect, deliver.** Order and trim all approved shots, replace unwanted native audio with the correct approved dialogue/narration, align lip-sync and subtitles, add cleared sound/music as needed, and export one playable film. Verify actual duration, picture ratio, audio, missing/repeated clips, and exports. Only then mark the project complete.

## Automatic continuation and native decisions

At each review, show the actual artifact first, call the native Question tool, record the returned choice for that exact artifact version, and invoke the next stage immediately after approval. Never end with “reply to continue” or a plain-text approval request. Do not substitute a drawn form or Markdown choices for the native interface.

Outside the named gates, continue all authorized work without an extra “continue” card. Persist stage, approvals, asset IDs, queued/running job IDs, and next action before waits. A tool submission acknowledgment is not success; resume or poll the same job until terminal. Do not mark the entire task list complete after submitting shot one. If the host cannot resume background jobs or lacks a required tool, report the concrete blocker through the native recovery choices; never promise unattended completion that the host cannot execute.

Approval is version-specific. Revisions invalidate only dependent artifacts and approvals. No response, ignore, timeout, a preselected option, or successful generation is user approval. Policy rejections require legitimate asset changes or provider review, not evasion. Use the exact runtime model profile for all media limits.

## References

- `references/workflow.md`: durable stage machine, progression and delivery.
- `references/selection-ui.md`: native gate choices and revision behavior.
- `references/characters-voices.md`: 16:9 turnarounds, auditions, voice ownership and shot speech.
- `references/shots-prompts.md`: production table, integer timing, prompts, independent shots and controlled extensions.
- `references/generation-guards.md`: observed errors, parameter preflight and bounded recovery.
- `references/style-index.md`, `references/style-manifest.json`, and the selected `references/style-specs-*.md` fragments: complete style library and exact text provenance.
