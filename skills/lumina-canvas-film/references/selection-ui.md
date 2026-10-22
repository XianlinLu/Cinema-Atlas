# Lumina native Question gates

The current Lumina interface shows a tool labeled **Question**. It renders the radio-option card with a short heading, question, labels/descriptions, and submit/other/ignore controls. Use the actual exposed tool schema; the UI label does not establish the function name or its arguments. `agents/openai.yaml` is display metadata and does not wire the tool.

Every required decision must be a real native call. Do not use Markdown checkboxes, a drawn imitation, printed JSON, or a request to type into the main chat. If the canvas subagent cannot access Question, return the artifact/version, heading, question and option descriptions to the parent that can, and resume after its actual returned decision.

## Review card sequence

Present and verify the real artifact before the card. Fit the options to actual schema limits; use concise labels with full informative descriptions. Standard review choices should normally be enough without typing:

| Gate heading | Choices and next action |
|---|---|
| 剧本确认 | 通过并生成角色图（推荐）; 调整剧本（opens targeted choices for plot, pacing, ending or dialogue）; 调整风格（catalog choices, then revised script review） |
| 角色三视图确认 | 全部通过，继续试音; 调整指定角色（choose role then image dimensions such as face/outfit/proportion）; 重新查看（show actual images, remain at gate） |
| 角色试音要求 | For the named role, offer 2–3 complete voice profiles matched to personality; descriptions cover pitch/timbre, language/accent, natural pace and performance. Mark one recommendation. |
| 角色试音确认 | 全部通过，生成镜头总表; 调整指定声音（choose role and sound/performance change）; 再听一次（play the real samples, remain at gate） |
| 镜头生产总表确认 | 通过并自动完成全部分镜与成片（推荐）; 调整指定镜头（select scene/shot and a concrete edit）; 重新查看表格与对白 |
| 异常处理 | Only on a real unresolved blocker: supported technical alternative, genuine replacement asset/voice, provider review, or save/pause as appropriate |

For every speaking character and narrator, show its actual role label and confirmed character image if available. Ask voice preferences before producing its audition, even if all other roles have a selected voice. Group several voice-profile questions into one native batch when supported, then fill remaining roles in schema-sized batches. Each profile should be a useful complete choice rather than an ambiguous “male/female” label. Honor voice requirements already supplied instead of repeating them.

Other/free text is optional advanced control, not the expected route. Use native built-in Other if provided; do not add a duplicate fake option. To revise a role or shot, derive targeted menus from current artifacts. Let users select multiple targets only if the real schema supports it. Never select a creative change merely because a card default was preselected.

## Returned decisions and approval scope

Persist gate ID, artifact ID, version and actual response. Only a returned affirmative choice approves that exact version. Submit intent, successful generation, default recommendation, an empty response, timeout and ignore/skip do not approve review gates. Ignore leaves the gate pending; explain through one native reminder that the stage needs an explicit decision. Do not loop repeated cards indefinitely or run downstream work without approval. A user explicitly asking to pause stops work with durable state.

After approval, close only that gate and immediately call the next production action without another “shall I continue?” question. A positive script review approves the script, not unseen character sheets or future voice audio. A positive table review authorizes automatic shot generation, technical repairs consistent with the approved content, assembly and export. It does not approve new dialogue, different identity or a new voice.

## Native recovery without a chat interview

Explain a blocker briefly inside the native recovery question, with real choices that change the situation. Parameter and transient failures should normally be repaired automatically before involving the user. Policy rejections use legitimate asset replacement or provider review; never offer “bypass detection.” A rights assertion does not make a rejected asset technically accepted.

The Skill cannot force a card if the host omits Question, cannot resume a background agent without host support, and cannot accept an approval on the user's behalf. These are capability blockers, not permission to fall back to ordinary multi-turn typing while claiming the requested native workflow is working.
