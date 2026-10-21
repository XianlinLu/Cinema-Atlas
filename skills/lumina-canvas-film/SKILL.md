---
name: lumina-canvas-film
description: Plan and build a short, cinematic visual story on Lumina's canvas agent. Use for storyboard-like canvas narratives, animated-scene concepts, visual explainers, and style-led canvas films; not for editing an existing video file.
---

# Lumina Canvas Film

Turn the user's subject into a clear visual story that can be composed with Lumina's canvas agent. Treat the canvas as the deliverable: make scenes readable, visually coherent, and useful when viewed as a sequence. Do not claim to render or export a video unless an available Lumina tool actually does so.

## Workflow

1. **Understand the brief.** Identify the subject, audience, intended duration or scene count, mood/style, aspect ratio if relevant, and any supplied assets or factual material. Ask one concise, grouped round of questions only for choices that would materially change the result. If the user wants speed or the brief is sufficient, state reasonable assumptions and proceed.
2. **Shape the story.** Write a one-sentence premise and a compact beat sequence. Give each beat one visual action and one purpose in the story. Prefer a beginning, a change or discovery, and a resolved ending. For factual work, distinguish sourced facts from illustrative interpretation and do not invent evidence.
3. **Translate it to canvas.** Use the available canvas tools and their documented element format. Arrange each scene as a distinct panel or clearly separated frame, with consistent reading order, generous spacing, and concise labels. Use native shapes, connectors, text, and available image/media elements; keep the visual hierarchy legible at the canvas's actual zoom. Respect the user's requested style through color, line, texture, typography, and composition rather than long prose pasted onto the canvas.
4. **Build with structure.** Add a title and, when useful, a small style/sequence key. Keep scene labels and narration separate from visual action. Use stable alignment and repeated motifs to make transitions understandable. For complex or data-heavy stories, simplify to the few details needed to support the narrative and attach sources near the relevant scene when available.
5. **Inspect and refine.** Use Lumina's canvas inspection or screenshot tools when available. Check that all frames are present, their order is obvious, text is readable, objects do not overlap unintentionally, connectors point to the right targets, and the ending resolves the opening. Correct concrete issues, then inspect again. Do not report a visual check that was not performed.
6. **Deliver clearly.** Briefly report the canvas result, its scene order, any assumptions, and any limitations of the available canvas tools. If the user asked for a script or timing, include those as notes or labels only when they help the canvas remain readable.

## Lumina-specific operation

- The conversational manager may delegate drawing to a canvas agent. Keep drawing instructions self-contained: state the scene content, layout, style, labels, and constraints in the handoff.
- Prefer the canvas agent's native structured elements (such as Excalidraw elements or SVG, if supported by the current tool) over an image of an entire canvas. This keeps text and shapes editable.
- If the canvas agent supports separate inspect and draw actions, inspect current state before modifying an existing canvas, then inspect the result after drawing. Preserve unrelated existing content.
- Do not assume a particular tool name, element schema, image generator, export path, or animation capability. Check the tools available in the current session and use only documented capabilities.
- When the request is for an actual video file, clarify the available output boundary: this skill produces a storyboard or cinematic canvas composition unless a video-rendering tool is available and the user asks to use it.

## Canvas quality checklist

Before delivery, confirm what is possible with the current tools:

- The story reads in the intended direction and each frame advances it.
- Typography, contrast, spacing, and grouping make the canvas understandable at a glance.
- Repeated visual motifs and palette support one coherent style.
- Factual claims remain faithful to supplied or verified material.
- The final frame provides a clear close, reveal, or next step.
- The user can distinguish finished content from placeholders or unverified assets.
