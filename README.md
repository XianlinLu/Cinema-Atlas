# Code-Cinema-Atlas

**An original Lumina canvas-agent skill for cinematic visual storytelling.**

This repository contains a Lumina-focused directing workflow that turns one idea into topic choices, a selected visual style, and a cinematic canvas or film. It uses native single-choice questions for undecided topics and styles, then follows brief → treatment → look → optional storyboard approval → production → review. The final output depends on the canvas and rendering tools available in the session.

The Lumina skill and its adaptation in this repository are written for this project by its maintainer. A complete project of a separate filmmaking toolkit is kept in `xianlin-lu/`, with its internal directory structure and license notices preserved.

## Skill

- [Lumina Story Director](skills/lumina-canvas-film/SKILL.md) — generate topic candidates, recommend 2–3 of the library's 51 styles, and invoke the host's native choice tool before production.
- The import folder has **43 files**, including the complete specifications of **all 51 styles**, partitioned without losing text. The agent loads the selected style through an index, preserving its look, color, typography, motion, camera, sound, native moves, and pitfalls.
- Every file stays below **19,000 UTF-16 code units**, compatible with both the 20,000-character import warning and the 30,000-character editor shown in Lumina.
- `SKILL.md` contains the operational instructions. `agents/openai.yaml` is optional OpenAI-compatible interface metadata; native question cards require a question tool exposed by Lumina. The skill discovers the available schema at runtime and cannot enable a missing tool.
- No `.skillignore` file is included because the importer accepts only `.md`, `.txt`, `.json`, `.yaml`, and `.yml` files.
- Skill and folder names use lowercase letters and hyphens for import compatibility.

Import only `skills/lumina-canvas-film/`, replacing the previous skill package instead of appending old references. Keep the full `xianlin-lu/` toolkit outside the importer. Rebuild or check the package with `python3 tools/build_lumina_skill.py` or `python3 tools/build_lumina_skill.py --check`; add `--zip <path>` to create a ZIP containing only the import files. The builder verifies exact style reconstruction and hashes, file count, supported extensions, names, and per-file lengths. This validation does not prove that Lumina exposes a native choice tool or a code-rendering environment.

## Source snapshot

The `xianlin-lu/` directory contains the complete tracked file set and original directory layout from the project. Its README files and license notices are retained within that directory. Check those notices before redistributing or reusing its contents.

## 使用说明

这是一个面向 Lumina 的导演工作流：从用户的一句想法中生成选题候选，通过原生单选卡片确定未定的主题和风格，再依次完成需求确认、创作方案、风格验证、按需分镜审批、制作和检查。交付画布还是完整成片，由当前会话实际可用的绘制与渲染工具决定。

本仓库中的 Lumina skill 及其适配内容由本项目维护者撰写。另有一份完整的电影制作工具包项目文件保存在 `xianlin-lu/` 目录中；该目录保留原有内部结构和许可声明。

## Skill 内容

- [Lumina Story Director](skills/lumina-canvas-film/SKILL.md)：根据想法生成主题候选，从固定的 51 种风格中推荐 2–3 种，并在制作前调用宿主原生选择工具。
- 导入包共 **43 个文件**，无损收录 **51 种完整风格规范**。Agent 依据索引按需读取选定风格，保留其材质、色彩、字体、运动、镜头、声音、媒介原生动作和禁忌。
- 所有文件均低于 **19,000 个 UTF-16 代码单元**，同时兼容之前 20,000 字符的导入限制和当前 30,000 字符的编辑器显示。
- 交互规则写在 `SKILL.md` 中；`agents/openai.yaml` 只是兼容 OpenAI 的可选界面元数据。原生选择卡片需要 Lumina 提供实际提问工具，Skill 会运行时识别其参数，不能启用宿主缺失的工具。
- 不包含 `.skillignore`：导入器只接受 `.md`、`.txt`、`.json`、`.yaml` 和 `.yml` 格式。
- Skill 和目录名仅使用小写字母与连字符，以兼容导入器的命名规则。

仅导入 `skills/lumina-canvas-film/`，整包替换旧版本，避免追加已过时的参考文件。完整的 `xianlin-lu/` 工具库保留在仓库中。通过 `python3 tools/build_lumina_skill.py` 重建导入包，或加 `--check` 检查一致性；加 `--zip <路径>` 可生成仅含导入文件的 ZIP。构建器检查完整风格的复原与哈希、文件数、扩展名、命名和单文件长度；这些检查不代表已经在 Lumina 内验证原生弹窗或代码渲染环境。

## 项目文件

`xianlin-lu/` 目录保存全部项目文件，并保留其内部目录结构、README 和许可证文件。重新分发或复用其中内容时，请先遵守对应许可声明。
