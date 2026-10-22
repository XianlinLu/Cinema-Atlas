# Cinema-Atlas

**Cinema Atlas Video Director — a Lumina workflow by Xianlin-lu.**

Turn one idea into a finished video while keeping creative approvals in Lumina's native **Question** cards. The agent drafts the full script, locks character and voice assets, prepares a shot production master table, generates every shot, and assembles one playable film. It continues automatically after each returned approval; ordinary use does not require typing “continue” between stages.

The required sequence is:

1. Full script and rhythm-based duration → native script approval.
2. One **16:9 front/side/back sheet** per visual character → native character approval.
3. Native voice-profile choices per speaking character and narrator → actual **20–30 second auditions** → native audio approval.
4. Full shot production master table, exact dialogue/voice bindings and measured timing → native table approval.
5. Automatic shot generation, bounded technical recovery, editing, audio synchronization, export and final inspection.

All **59 film styles** are available through their complete specifications. Read the selected style by index, preserving its visual grammar; the current native production workflow governs execution over legacy engine examples. Documentary/evidence requirements remain in force where a style requires real source material.

## Import into Lumina

Import only [`skills/lumina-canvas-film/`](skills/lumina-canvas-film/). Replace the previous package as a whole; do not append it to old reference files or upload the entire repository.

- **49 files**, all in supported Markdown/YAML/JSON formats.
- Every file is below **19,800 UTF-16 code units**, retaining margin below the earlier 20,000-character import limit.
- The full 59-style specification texts are partitioned without loss, indexed, reconstructed and hash-checked during packaging.
- `SKILL.md` defines the workflow. Five focused references cover state/continuation, native gates, characters/voices, shot tables/prompts and generation safeguards. Style index, manifest and specification fragments supply the library.
- `agents/openai.yaml` is optional OpenAI-compatible UI metadata. It does not install a Lumina tool.

Native cards require the host's actual Question tool. Full unattended production additionally requires generation, task status, editing/export, stable asset access and automatic background continuation. The Skill discovers exposed schemas; it cannot enable missing host features or override content checks. The live UI has been inspected for the Question tool, but the new complete paid-media pipeline has not been run end to end here.

## Request reliability

Audition masters, short voice-identity references and exact shot dialogue are separate assets. Requests validate the active model's actual per-file and aggregate audio limits. Real extension inherits its source ratio; it must not submit a conflicting fixed ratio. Voice ownership, approved versions, real asset IDs and shot timings are checked before generation. Policy rejections stop blind retries and use native choices for legitimate asset revision or provider review; successful generation is not promised for blocked material.

Build and validate with:

```sh
python3 tools/build_lumina_skill.py
python3 tools/build_lumina_skill.py --check --zip /path/to/lumina-cinema-atlas-v2.zip
python3 -m unittest discover -s tests -p 'test_lumina_preflight.py' -v
```

`tools/lumina_preflight.py` checks normalized requests and production state without submitting media. These Python helpers and tests remain outside the import folder.

The `xianlin-lu/` directory holds the filmmaking toolkit project. Its style specifications and catalog have been refreshed to 59 entries. The Lumina import does not include all demo engines, images or audio; the rest of the toolkit is a separately preserved project snapshot. Follow the corresponding license notices when reusing materials.

## 中文介绍

**Cinema Atlas Video Director** 是 Xianlin-lu 面向 Lumina 制作的视频创作工作流。用户给出一句想法，Agent 先写完整剧本，按照原生 **Question 选项卡**完成关键审批，再自动生成全部分镜并合成可播放成片。确认后立即推进下一阶段，常规流程无需用户反复在输入框中写“继续”。

流程为：**完整剧本确认 → 16:9 角色三视图确认 → 逐角色试音要求选择 → 20–30 秒真实试音确认 → 镜头生产总表确认 → 自动生成全部分镜、配音对齐、剪辑与交付**。片长按剧本节奏估计，再依据逐镜音频实测和镜头时间轴锁定，不强行压缩为固定短片时长。

导入包完整收录 **59 种风格规范**，共 **49 个文件**，每个文件低于 **19,800 个 UTF-16 代码单元**。Agent 按需读取选定风格，保留材质、色彩、字体、运动、镜头、声音、原生动作及注意事项；原代码引擎示例不会覆盖当前原生视频制作流程。

在 Lumina 中仅导入 `skills/lumina-canvas-film/`，整包替换旧版。不要叠加旧参考文件，也不要上传整个仓库。试音母版、声纹参考片段和镜头实际台词分开管理；每镜绑定正确的角色图、声音版本和实测音频，并在提交前检查参考音频时长、总预算、任务类型、续写画幅和审批状态。版权检测拦截不会被无限重试或规避，而是通过原生选项选择真实的新素材方案或平台复核。

完整自动运行需要 Lumina 实际提供原生 Question、图像/音频/视频生成、任务状态、剪辑导出及后台自动续跑能力。Skill 会识别实际工具参数，但无法开启宿主缺失的能力。当前已只读检查到原生 Question 工具；本次完成了打包、内容一致性和参数/状态检查，尚未在 Lumina 内执行新版完整付费媒体流程。

构建器、参数预检工具和测试文件保留在仓库外层，不随 Skill 上传。完整工具包位于 `xianlin-lu/`，其中风格规范与目录已同步为 59 种；导入包不包含全部演示工程和媒体素材，复用素材时请遵守对应许可。
