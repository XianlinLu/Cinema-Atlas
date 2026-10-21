# Native topic and style selection

The required experience is a real host question card: a short heading, a single question, radio options with a label and a description, and the host's submit/other/skip controls. The host renders it from a tool call. Neither this file nor `agents/openai.yaml` can register that host tool.

## Bind to the runtime tool

Read the active tools' names, descriptions, and schemas. Look for a tool that asks the user structured questions and accepts choices (a host might call it AskUserQuestion, request_user_input, or something else). These names are examples, not an API contract. Use only a tool that is actually exposed and allowed in this session.

Map the following semantic fields onto its real schema:

| Meaning | Topic selection | Style selection |
|---|---|---|
| Short heading | 故事主题 | 视觉风格 |
| Question | Which direction should this idea take? Tailor it to the actual request and language. | Which of these library styles should the selected topic use? |
| Selection mode | Single choice, not multiple | Single choice, not multiple |
| Choices | 3–4 distinct concepts, subject to schema limits | 2–3 catalog styles matched to the topic |
| Label | Short original title; one recommendation | Exact catalog name; one recommendation annotation |
| Description | Protagonist/subject + action + turn, in one sentence | Why it fits, using that style's real grammar |

Use the schema's actual question/option limits. If it allows only three topics, supply three strong topics. Use the built-in free-text/Other route if provided; do not duplicate it with an extra fake option. Do not create a local form or draw radio circles on the canvas.

If the drawing subagent cannot access the question tool but a parent agent can, send the parent the heading, question, labels, descriptions, and pending decision, and have the parent ask the user. Wait for the answer to be passed back before drawing. If neither agent can call a native choice tool, state that limitation once, present numbered text alternatives, and wait for an answer. Do not claim the native card appeared.

## Topic options from one sentence

Keep the user's stated subject, language, audience, mood, and exclusions. Derive genuinely different angles: a personal journey, a reveal, a contrast, or a consequence when those fit. Each choice must be visually stageable and have one subject, one goal, and one turn. Recommend the one most faithful to the prompt. Infer details needed for a useful concept; do not fabricate facts about real people or events.

The sample labels visible in a user's screenshot are UI examples, not fixed content. Generate fresh choices for each idea. If the user already chose a concrete topic, skip this card and retain that topic.

## Style choices from the fixed library

Before asking, show the full catalog grouped by its 10 original categories, in the user's language only, then recommend 2–3 entries. Do not limit the catalog to the recommendations. Keep exact names and slugs, even where a canonical name contains another language. Let a native free-text answer select any other catalog entry.

Resolve English names, Chinese names, or slugs. For an ambiguous match, show the closest 2–3 and ask. For an unlisted style, explain that strict-library mode has no such entry and offer actual neighboring entries; adopt a custom style only if the user explicitly changes the requirement. Never quietly blend two catalog entries into a new style.

## Advance only on a real outcome

Persist the returned topic/style decision so it is not asked again after a tool boundary or delegation. A recommendation is not a selection. Do not proceed because a card has been open for a while.

If the user explicitly submits Other, use that content and resolve it. If the tool explicitly returns skip/ignore, use the recommended option as a declared assumption and continue, unless the skipped item needs a real fact or supplied asset. If the user says “you choose” or asks for fully automatic execution, use the recommendation and do not force a card. Ordinary topic/style answers are followed by the one consolidated brief, not approval prompts at every stage.
