---
name: lumina-canvas-film
description: Direct a film or cinematic canvas from one idea using a fixed library of 51 film styles. Generate relevant story choices, call Lumina's native single-choice question tool for topic and style decisions, then follow brief → treatment → look → optional storyboard approval → production → review. Use for short films, visual explainers, cinematic canvas stories, and finding a film style.
---

# Lumina Story Director · Xianlin-lu

Turn one sentence into an original film about the user's topic, with the library's actual style grammar and directing workflow. Infer useful options and recommend a direction; let the user select through Lumina's native question interface. Keep the user's language and supplied constraints.

## Read and act in this order

1. Read `references/selection-ui.md` and `references/workflow.md`. Inspect the active tool descriptions for a real structured question tool and canvas/production capabilities. A Skill cannot enable tools that the host has not exposed.
2. **Resolve the topic.** If the topic is already concrete, keep it. If it is a broad wish or an undecided idea, infer 3–4 distinct, drawable concepts tied to it. Call the native single-choice tool with the heading **故事主题** (or the user's-language equivalent), one concise question, short titles, and one-sentence descriptions. Mark one recommendation. Wait for an actual answer; do not silently choose.
3. **Resolve the style.** Read `references/style-index.md`. Honor a named style by matching its English name, Chinese name, or slug. If absent, recommend 2–3 fitting entries, display ALL 51 canonical style names grouped by their original categories in the user's language, then call the native single-choice tool with the heading **视觉风格**. Support another catalog style through the tool's native free-text route. Wait for the answer. Do not invent, merge, or rename styles.
4. **Load the complete selected style.** Read every `references/style-specs-NN.md` file listed for its slug in the index. Follow pagination or truncated reads until every selected segment is complete. Extract that slug's marked segments in file order. Keep ALL invariants: look, material, color, typography, movement, camera, sound, native moves, and pitfalls. The style is fixed; the user's story is new. Do not load demo stories or code before the treatment.
5. **Take the brief once.** Follow `references/workflow.md`: group only unanswered material/fact requirements, assets, language, storyboard-review preference, and actual production blockers into one brief round. Wait for the reply; default the remaining gaps. Do not turn every production stage into another questionnaire.
6. **Direct and produce.** Read `references/director.md` and `references/canvas-adapter.md`. Make the treatment with three candidate structures and your reasoned choice, then prove the look. Stop for storyboard approval only if the user requested it. For code-based film production, also read `references/technique.md`; run the original voice/check/score/animation/mix/render sequence with available tools. Use demos only after the treatment, for technique, never for their story or timeline.
7. **Review and deliver.** Apply the director's full review and originality checks. Deliver the actual supported result and identify it accurately. A canvas plan, an unrendered shot list, and a completed film are different deliverables; report which exists.

## Required interaction behavior

- Use a real question-tool call to create the radio-choice card shown by Lumina. A Markdown list, JSON printed in chat, or a drawn imitation does not create that card.
- Discover the actual tool name and argument schema at runtime. Do not assume `agents/openai.yaml` registers a Lumina tool or that an example function name exists.
- Keep topic selection, style selection, and the single consolidated brief as separate purposes. Do not ask for a selection the user has already made.
- Respect an explicit instruction to choose for the user or skip questions. An unanswered card or elapsed time is not such an instruction.
- Preserve unrelated canvas work. Inspect before editing and after drawing when supported. Never claim tool execution, inspection, audio, animation, or export that did not happen.

## Reference authority and loading

- `references/workflow.md`: source workflow and exact decision gates; read at activation.
- `references/selection-ui.md`: native-choice interaction and skip/other behavior; read before asking.
- `references/style-index.md`: all 51 names, categories, use cases, slugs, and required style files.
- `references/style-specs-*.md`: full, losslessly partitioned style documents; load only the selected slug's listed files.
- `references/style-manifest.json`: file offsets, source hashes, and pinned library location; use for exact lookup or provenance.
- `references/director.md`: complete directing method, treatment, sound, rhythm, camera, review, and delivery.
- `references/technique.md`: complete production method; load for executable film work.
- `references/canvas-adapter.md`: how those requirements map to available Lumina capabilities.
