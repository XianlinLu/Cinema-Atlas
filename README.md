# Cinema-Atlas

**Cinema Atlas Native Video Director — a Lumina workflow by Xianlin-lu.**

One idea → a full script → consistent characters and voices → all video shots → native editing choices → a reviewed, downloadable result. Creative decisions use Lumina's native **Question** cards; execution uses native canvas nodes and the **Video Editor**. After each returned approval, the agent advances automatically.

## 中文介绍

主入口负责阶段导航，专项操作按需读取。新增持久执行循环：**读取当前状态 → 接收真实卡片结果 → 选择就绪动作 → 调用原生工具 → 检查结果 → 保存下一动作 → 自动继续**。普通进度说明不会被当成任务结束；只有原生创意决策、明确暂停、真实不可恢复阻塞或已验证交付才返回控制权。

同场景续写区分技术 QC 与用户成片批准，避免在生成队列中提前等待后置确认。原生产总表与后期时间轴分开版本化，裁切素材头尾、音乐卡点和字幕重定位不会无故重做整个影片。模型背景音乐与最终独立配乐、对白字幕与风格必要文字也明确区分。

本版完整需求见 [需求基线](docs/requirements.md)，调整依据见 [v5 审查记录](docs/v5-review.md)。

**v5.1 声音修正：去配乐不等于全静音。** Agent 依据剧本和动作判断每镜应有的对白、旁白、音效与环境声；只有这些内容在实际分镜中可听、同步且模型配乐已移除，才交给用户确认。后期按视频内容自动选择或生成原创／已获许可的配乐，在原生 Video Editor 中分轨制作，最终确认后再导出。详见 [声音修正说明](docs/v5-1-sound-review.md)。

**v5.2 同步恢复：节点创建、任务受理与真实产物分开。** 先完成第一个真实角色，再自动推进其余队列；画布同步失败先有限读取／对账恢复，复用原节点与已有任务，受理不明不重复提交。临时恢复不增加用户问答，持续的宿主故障保留断点并通过真实原生恢复选项处理；工具卡片显示完成不冒充媒体生成完成。详见 [同步恢复说明](docs/v5-2-sync-review.md)。

用户只需要给出想法，Agent 会推理故事与风格、写完整剧本，再依次生成角色三视图、试音、镜头总表与全部分镜。用户在关键节点用原生选项卡决定；通过后自动推进，无需反复在聊天框输入“继续”。

### 完整流程

1. **完整剧本 → 剧本确认。** 片长由故事节奏、自然语速和动作决定；风格与剧本一起确认。
2. **16:9 角色三视图 → 角色确认。** 每个需明确身份的出镜剧情角色（含只出现一次的发声角色）包含同一身份的正面、侧面、背面。
3. **逐角色声音选项 → 20–30 秒真实试音 → 试音确认。** 角色、音色、实际音频与版本明确对应；旁白独立管理。
4. **镜头生产总表 → 总表确认。** 保留确切台词、角色与声音引用、实测音频时长、分镜、时间轴及任务依赖。
5. **自动生成全部分镜 → 逐段成片确认。** 每段实际视频都需要用户确认当前版本，修改后仅重新确认受影响内容。
6. **后期制作选项。** 原生卡片提供“仅剪辑拼接”“仅添加字幕”“剪辑拼接＋字幕（推荐）”及 Other 自定义入口。
7. **原生 Video Editor 分轨制作。** 选“两者都需要”立即执行拼接和字幕；仅拼接不额外添加字幕，仅字幕不擅自拼接。真实视频轨、背景音乐轨、文字字幕轨（选中时）和音效轨分别可编辑；对白／旁白保留正确源声或使用独立人声轨，避免重复播放。
8. **自动配乐与卡点。** Agent 根据实际剧情、风格、情绪和节奏，在原生工具支持下选择或生成原创／已获许可的配乐，作为整片独立轨道；尊重明确不配乐的要求。按真实节拍／乐句安排硬切，并降低对白下的音乐音量，保留完整人声、关键音效、动作和口型，不为了卡点强行加速或删词。
9. **剪辑成片确认 ↔ 继续修改。** 展示实际预览后，通过原生卡片确认或修改。选择修改后，在卡片内填写“哪段／哪个时间点、修改什么、怎么修改”；Agent 在同一 Video Editor 项目中修改、检查、重新预览与确认，保留无关的人工作业。
10. **最终确认 → 原生导出 → 下载交付。** 只有已批准当前版本真实导出且可下载后，才返回最终剪辑视频。云草稿地址和任务提交成功不等于可下载视频。

### 视频生成默认规则（继续保留）

- **模型：Seedance 2.5。** 解析 Lumina 实际模型标识；不可用时通过原生卡片处理，不静默换模型。
- **画幅：默认 16:9。** 只有用户明确指定其他比例才覆盖，不能凭发布平台或参考图自动改竖屏。
- **分镜只去模型背景音乐，保留人声与音效。** 无配乐时不做整段静音；有混轨时用真实原生分离，或将全静音仅作中间步骤，恢复全部应有对白、旁白、音效与环境声并检查同步。实际分镜在确认前就必须可听，不能等后期再补；没有对白的镜头也不默认无声。缺少真实处理能力时报告受影响镜头的具体阻塞。
- **同 scene 连续 shot 可续写。** 需要时间、动作、角色、服装、光线与机位连续，前镜头就绪、比例一致，且真实工具支持；否则独立生成。不同 scene、时间跳跃或动作断开不做续写。续写继承源比例，移除返回结果中的重复前缀。
- **转场硬切。** 不自动添加叠化、交叉淡化、擦除或变形转场。后期若使用已规划配乐，作为独立轨道统一添加并卡点，不恢复每段模型随机配乐。

### 风格与稳定性

完整收录 **11 类、59 种风格规范**，按需读取完整文本并保持其材质、色彩、字体、构图、运动与声音语言。示例故事、角色和音乐不自动成为可复用素材；纪实与实证题材保留真实来源要求。

- 角色试音采用独立输入记录，默认逐个自动处理；检查真实素材 ID、非空文本和依赖就绪，避免空引用或错误连接引起 `content id is empty`。
- 区分试音母版、声音身份参考与实际镜头台词，使用当前模型真实的音频时长、数量与总预算规则。
- 视频延长继承源比例；只在工具真正支持且内容连续时使用延长。
- 生成前锁定声音路线；视频输出音频拦截与 TTS 输入错误分别处理，停止盲目重试，保留独立成功结果，通过原生选择进行实质性素材修改或平台复核。
- 每镜审批、后期选择、最终审批都按版本保存。旧预览不能批准新剪辑，失败镜头不能被遗漏后冒充整片完成。

### 导入 Lumina

下载 [v5.2 专用导入 ZIP](dist/lumina-cinema-atlas-v5-2.zip)，解压后只导入 [`skills/lumina-canvas-film/`](skills/lumina-canvas-film/) 对应的 **SKILL.md、agents、references**。新建空白 Skill 最稳妥；覆盖旧版时先备份，再整包替换，避免旧参考文件残留。不要上传整个仓库、dist、工具或说明文档。更新 Skill 不代表已停止的旧会话会自行唤醒：恢复时需实际加载新版规则，并在同一画布先对账复用已有节点／任务，无需删除画布重做。

- **36 个文件**，加两个子目录和最外层目录共 **39 项**。
- 当前 Lumina 上限为 **30,000 字符**；本包每个文件不超过 **29,600 个 UTF-16 代码单元**，保留余量。
- 保留全部 59 种风格，分片可重建并逐项核对哈希。
- SKILL.md 开头应为 `Import build: v5.2-resumable`。
- `agents/openai.yaml` 是显示元数据，不能替 Lumina 注册工具。

完整执行依赖 Lumina 实际暴露原生 Question、媒体生成、任务查询／续跑和 Video Editor 编辑、字幕、预览、导出、下载能力。截图仅确认界面存在，不能证明每项操作已向 Agent 开放。缺失能力时 Skill 会保存状态并报告具体阻塞；不会虚报工具调用或保证平台审核通过。

## English overview

Video defaults are **Seedance 2.5** and **16:9** unless the user explicitly requests another ratio. Remove ONLY model-generated background music before shot review; retain or restore all intended dialogue, off-screen speech, narration, sound effects and ambience. Prepared shots must actually play with their required sound before approval; a globally muted intermediate or detached audio is incomplete. Use true extension only for eligible continuous shots in the same scene; separate scenes remain independent. All visual transitions are hard cuts.

The agent turns an idea into a complete script, **16:9 character turnarounds**, role-specific voice choices, real **20–30 second auditions**, a measured shot production table and every planned video shot. Each current shot is then reviewed through a native Question card before post-production begins. A persistent reconcile/dispatch loop advances every ready authorized task after native answers and actual tool results; host callbacks/status APIs provide asynchronous continuation.

Version 5.2 distinguishes prepared nodes, accepted jobs and real outputs. It completes the first required character deliverable before expanding the queue, serializes shared-canvas writes, and handles pre-execution sync faults with bounded non-generating reconciliation. Existing nodes, running tasks and completed media are reused; uncertain acceptance never triggers a blind duplicate paid submission. Persistent host failures retain a precise checkpoint and use actual native recovery rather than promising unsupported background resumption.

The next card offers **stitching only / subtitles only / both / Other**. Choosing both invokes Lumina's native Video Editor for assembly and editable captions. The agent automatically fits original/cleared final scoring to the story, mood and pace through supported native tools, respecting explicit no-music choices. Picture, final background music, selected subtitles and sound effects remain on real separately editable tracks, with correct embedded or dedicated speech and no doubling. Meaningful cuts follow genuine musical markers while preserving dialogue, effects, actions and synchronization. Final scoring is reviewed in the actual preview before export.

Final review offers **confirm and export / continue modifying / preview again**. A modification is specified inside the native card, then applied to the same editor project. The loop repeats for the current revision until approved. The agent exports through the native editor, checks the actual accessible media and returns the downloadable result; an editor draft is not a completed export. If the user explicitly declines post-production, delivery is clearly labeled as approved clips.

All **59 styles** retain their full specifications. The importer package contains **36 text files** (39 items including directories/root) and uses a conservative 29,600 UTF-16-unit cap under the user-confirmed 30,000-character limit. Existing audio-ID, voice ownership, duration, extension-ratio, bounded recovery and policy-rejection rules remain included. Every approval is version-specific; missing host tools or provider failures are reported honestly. Native sound separation, editing/export and the full paid-media pipeline have not been exercised end to end for this version.

## Maintainers

```sh
python3 tools/build_lumina_skill.py
python3 tools/build_lumina_skill.py --check --zip dist/lumina-cinema-atlas-v5-2.zip
# Repack existing verified style text without needing the source library:
python3 tools/build_lumina_skill.py --repack-existing --zip dist/lumina-cinema-atlas-v5-2.zip
# Check/package the current import folder:
python3 tools/build_lumina_skill.py --verify-import --zip dist/lumina-cinema-atlas-v5-2.zip
```

The builder verifies importer counts, filenames, 29,600-unit text lengths, local reference links and reconstructed style hashes. The 59 complete specifications are losslessly repacked into 27 style pages; no style is summarized or removed. `tools/lumina_preflight.py` provides existing normalized media checks; it is not the native runtime orchestrator and does not replace v5 approvals. Helpers, historical tests, documents and ZIPs stay outside the import folder. The separately preserved toolkit and media live in `xianlin-lu/`; follow their corresponding notices.

Editing-method mapping and reference revision: [Native editor workflow](docs/native-editor-workflow.md). The OpenFilm method is adapted to Lumina's native operations; OpenFilm Studio/CLI is not installed or invoked by this Skill. [Source notice](docs/openfilm-notice.md).
