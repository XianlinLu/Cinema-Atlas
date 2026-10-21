# Code-Cinema-Atlas

**An original Lumina canvas-agent skill for cinematic visual storytelling.**

This repository contains an original, Lumina-focused workflow for turning a brief into a scene-by-scene visual story on a canvas. It guides the agent through story beats, canvas composition, tool-aware drawing, visual inspection, and a clear handoff. The skill treats the canvas as an editable storyboard or visual narrative; it does not claim to render a video unless the active Lumina tools support that.

The skill instructions, Lumina adaptation, and documentation in this repository are written for this project by its maintainer.

## Skill

- [Lumina Canvas Film](skills/lumina-canvas-film/SKILL.md) — plan and compose cinematic storyboards, visual explainers, and scene-based canvas narratives with Lumina.
- The entrypoint is kept concise and below Lumina's 20,000-character per-file limit.
- No `.skillignore` file is included because the importer accepts only `.md`, `.txt`, `.json`, `.yaml`, and `.yml` files.
- Skill and folder names use lowercase letters and hyphens for import compatibility.

## 使用说明

这是一个面向 Lumina 画布 agent 的原创工作流，用于把创意整理为逐场景的画布叙事。Skill 会引导 agent 完成故事节拍规划、画布构图、基于当前工具能力绘制、检查视觉结果并清晰交付。它将画布作为可编辑的分镜或视觉叙事；只有当前 Lumina 工具确实支持视频渲染时，才会声称可以导出视频。

本仓库中的 Skill 说明、Lumina 适配内容与文档由本项目维护者为本项目撰写。

## Skill 内容

- [Lumina Canvas Film](skills/lumina-canvas-film/SKILL.md)：使用 Lumina 规划和编排电影感分镜、视觉解说与逐场景画布叙事。
- 入口文件保持精简，低于 Lumina 单文件 20,000 字符的限制。
- 不包含 `.skillignore`：导入器只接受 `.md`、`.txt`、`.json`、`.yaml` 和 `.yml` 格式。
- Skill 和目录名仅使用小写字母与连字符，以兼容导入器的命名规则。
