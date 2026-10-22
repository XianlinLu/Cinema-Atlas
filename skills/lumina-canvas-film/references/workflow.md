# Autonomous workflow and durable state

## Execution priority

This workflow implements the user's current sequence. It supersedes the previous optional-storyboard and code-rendering-only execution rules. Preserve the selected style's visual, camera, rhythm and sound grammar, while using Lumina's actual image, speech, video and editing capabilities. Read the two supplied SOPs for method, not their sample story. The relevant methods are already adapted in this package; access to those private pages is not required for routine execution.

Required capabilities: native Question cards, real image generation, reusable speech/voice identity, video generation with appropriate audio conditioning or a separate lip-sync path, task status, editing/export, and a way to continue asynchronous work. Inspect actual schemas before starting. Use supported node connections and asset handles, not nonexistent @names or model IDs guessed from examples. If a required capability is absent, use one native recovery card to identify the missing capability and available supported alternatives. If Question itself is absent, state the concrete host limitation and leave the project blocked before paid media calls; a Skill cannot register a missing tool.

## Stage machine

| Stage | Real work | Allowed next stage |
|---|---|---|
| SCRIPT | Infer the concept/style, write full script and natural timing estimate | WAIT_SCRIPT |
| WAIT_SCRIPT | Present the full version; native approval | CHARACTERS only on approval |
| CHARACTERS | Create and inspect each recurring character's 16:9 front/side/back sheet | WAIT_CHARACTERS |
| WAIT_CHARACTERS | Show all sheets with stable role labels; native approval | VOICE_BRIEF only on approval |
| VOICE_BRIEF | Native voice-profile choices for each speaking role and narrator | AUDITIONS after answered profiles |
| AUDITIONS | Generate actual 20–30 second audition files, validate and attach playable previews | WAIT_AUDITIONS |
| WAIT_AUDITIONS | Native approval of actual role/audio versions | MASTER_TABLE only on approval |
| MASTER_TABLE | Build atomic shots, generate exact shot speech, measure audio, lock integer timing | WAIT_TABLE |
| WAIT_TABLE | Present complete table and audio previews; native approval | SHOTS only on approval |
| SHOTS | Automatically render and check every planned shot with correct locked assets | ASSEMBLY when all required shots pass |
| ASSEMBLY | Edit, mix, synchronize, export, and inspect one final video | COMPLETE only after checks pass |
| RECOVERY | Native choices only for a genuine blocker or creative revision | Resume the affected stage |

No text-only “please confirm” between stages. The return of a positive native choice continues execution in the same resumed agent turn. Routine polls, internal checks, splitting a shot for model limits, or repairing technical parameters do not create extra user gates when the approved creative content remains unchanged.

The mandatory gates approve a bundle and its contents: character approval may cover all sheets, audition approval may cover all playable role samples, and table approval includes its exact shot speech. Offer focused native choices to revise only an affected role or row. Large bundles must show every item; do not approve unseen items by omission. A role with no lines has no audition; if there are no visual characters, record CHARACTERS as not applicable and continue to the actual speaking/narration roles. Do not invent assets to fill a stage.

## Script and timing

Generate a complete script from the idea before asking for its approval. Retain the user's full supplied script and dialogue; translation, omission, new characters or a different ending must appear in a newly reviewed script. Never compress a long story into a few 30-second multi-scene generation requests solely to match a model's per-call maximum.

Estimate duration from dialogue at a natural pace, actions, emotional pauses, hooks, and transitions. Present an estimate at script review and the measured sum at table review. Actual speech plus picture handles determines the minimum of dialogue shots. No speaking faster or deleting words to fit. A fixed user target is a creative constraint resolved in script review, not permission to truncate approved lines later.

## Persisted production manifest

Use a project file or persistent canvas note, not conversational memory alone. Use stable IDs and preserve unrelated canvas content. Store at minimum:

```json
{
  "schema_version": 2,
  "project_id": "stable-project-id",
  "stage": "WAIT_SCRIPT",
  "script": {"version": 1, "asset_id": "actual-note-id", "approval": {"status": "pending", "version": 1}},
  "film_ratio": "16:9",
  "characters": {},
  "voices": {},
  "table": {"version": 1, "script_version": 1, "approval": {"status": "pending", "version": 1}},
  "gates": [],
  "shots": [],
  "jobs": [],
  "next_action": "call_native_script_review"
}
```

Replace example handles with real returned IDs; this is a data shape, not an executable host API. Character records store image version/approval and real master/panel IDs. Voice records store owner, version, selected profile, actual audition/voice ID and approval. Shot records store all approved dependencies and job outputs. Gate records store gate ID, artifact/version, returned decision and time. Job records store request fingerprint, model/task kind, attempts, node/task ID, status, output IDs, measured metadata, error/request/log IDs and next poll/resume action. Never record a job as done merely because the node was created.

Write long artifacts with structured file/note arguments or verified chunks; avoid embedding JSON, dialogue, quotes, dollar signs, or newlines into shell command arguments. On partial note-write failure, preserve the full script/table in storage and repair the write; do not shorten approved content to make escaping easier. Re-read written artifacts before asking approval.

## Background continuation and retries

Persist before submitting, after receiving an ID, and after every state change. Reuse a running task on resume. On uncertain submission, query its ID or use actual idempotency support before considering a new call. Register the host's supported completion callback/continuation, or keep polling through its status tool. Keep progress truthful: queued, running, generated, checked and approved are distinct states. A background acknowledgment does not justify a final “done” message.

If the host forces the current turn to end, it must also expose a durable automatic continuation for unattended work. Persist its actual continuation handle. If it does not, mark the limitation explicitly rather than claiming the Skill can continue by itself; present native recovery options once. Do not ask the user to type “继续” after each job. Stay responsive with brief progress updates during long runs.

Limit concurrent work to actual provider quotas. Independent shots can run concurrently; an extension waits for its real predecessor. Follow `generation-guards.md` for retry bounds. Retain successful outputs and rerun only the failing job and genuinely affected dependents.

## Revisions and final acceptance

A revised script invalidates impacted characters, voices, table rows and videos; a new voice invalidates its auditions, speech and affected speaking shots; a changed image invalidates dependent image/video inputs. Unchanged roles and successful unrelated shots stay locked. Reapprove the revised artifact through native Question before paying for affected downstream media.

COMPLETE requires all planned shot IDs exactly once on the edit timeline, actual exported video, intended ratio, measured duration, synchronized approved speech/narration, no unplanned gaps or repeated extension prefixes, and playable output. Inspect image/voice identity, lips, missing/extra lines, source licenses and any required subtitles. If an inspection cannot be performed, report that exact remaining check instead of claiming a pass. Deliver the final video, shot table, asset/voice map, script version, credit/source list, and available editable project/subtitles. Do not finish with a plan in place of a movie.
