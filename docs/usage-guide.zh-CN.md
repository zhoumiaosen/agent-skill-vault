# 按任务使用指南

[英文版](usage-guide.md)

先明确要完成的任务，再阅读相关技能包。[目录](../README.md)列出已有技能；
本指南说明怎样选用和组合。技能是指令与辅助材料，不是已安装的游戏框架。
这里不声称运行过引擎或模型。

## 从小范围开始

先选一个主技能，只在任务跨越职责边界时补充另一个，不要为每个请求加载全部技能。
行动前阅读 `SKILL.md`、`SOURCE.md` 及所需参考或资源文件；复制包时保留完整辅助文件
与许可证，以及包中存在的 NOTICE。宿主决定加载方式；提示中写出名字不等于安装，
也不能证明宿主已发现技能。没有自动发现功能时，将完整技能包作为上下文提供。

提供真实项目根路径、引擎与包版本、目标平台、复现步骤或目标行为、相关文件，
以及可用测试工具。下面的提示是起点；用真实信息替换方括号，并限定在授权范围内。

| 要做什么 | 从这里开始 |
|---|---|
| 确定要制作的内容 | [游戏方向](#游戏方向) |
| 规划改动 | [映射与计划](#映射与计划)、[版本与契约](#版本与契约) |
| 制作角色扮演游戏系统 | [背包与存档](#背包与存档)、[战斗与敌人](#战斗与敌人)、[对话本地化与音频](#对话本地化与音频) |
| 制作玩家交互 | [界面与无障碍](#界面与无障碍)、[输入](#输入)、[动画与过场](#动画与过场) |
| 制作世界与素材 | [关卡与生成](#关卡与生成)、[瓦片地图像素画与素材](#瓦片地图像素画与素材) |
| 排查或验证 | [调试还是性能分析](#调试还是性能分析)、[测试与代码审查](#测试与代码审查) |
| Godot 入门、编写文档或分工 | [Godot 入门](#godot-入门)、[文档](#文档)、[并行工作](#并行工作) |

## 游戏方向

先用 [game-design](../skills/game-design/SKILL.md)
（[使用限制](../skills/game-design/SOURCE.md)）明确机制、成长与小型可玩循环。
需要角色扮演游戏的属性、装备、战斗或任务模型时，选
[rpg](../skills/rpg/SKILL.md)（[使用限制](../skills/rpg/SOURCE.md)）。
技术方案还不确定时，用
[create-technical-spike](../skills/create-technical-spike/SKILL.md)
（[使用限制](../skills/create-technical-spike/SOURCE.md)）进行有边界的实验。

**上下文：** 玩家目标、代表性遭遇、已有规则与范围；技术探索还需要问题、时限
与可用沙盒。

**证据：** 明确的循环与验收例子；有工具时记录真实试玩观察或实验输出。
公式草稿不能证明平衡性。

> 示例：阅读 game-design，为[角色扮演游戏概念]提出一个可玩循环，给出具体遭遇和验收标准。列出需要试玩的内容，不要声称已经测试过设计。

## 映射与计划

用 [context-map](../skills/context-map/SKILL.md)
（[使用限制](../skills/context-map/SOURCE.md)）定位相关文件与职责；再用
[create-implementation-plan](../skills/create-implementation-plan/SKILL.md)
（[使用限制](../skills/create-implementation-plan/SOURCE.md)）安排工作与验证。
影响长期结构的选择可用
[create-architectural-decision-record](../skills/create-architectural-decision-record/SKILL.md)
（[使用限制](../skills/create-architectural-decision-record/SOURCE.md)）记录；
不必为每个小改动创建决策记录。映射审阅是 context-map 流程的一部分。

**上下文：** 仓库访问、真实任务、当前测试、相关资源或程序集与约束。
将上游输入占位符与文档路径替换为项目约定。

**证据：** 以文件为依据的依赖映射、已审阅计划、明确验收命令与决策备选方案。
计划不等于已实现，也不代表获准合并。

> 示例：阅读 context-map，映射[任务系统改动]涉及的文件和测试，解释依赖关系，并在实现前停下来审阅映射。保留无关改动。

## 版本与契约

陌生或版本敏感的 API 选
[source-driven-development](../skills/source-driven-development/SKILL.md)
（[改写说明](../skills/source-driven-development/SOURCE.md)）。
状态所有权、模块、事件、生命周期与存档契约选
[api-and-interface-design](../skills/api-and-interface-design/SKILL.md)
（[改写说明](../skills/api-and-interface-design/SOURCE.md)）。
需要定义或保护项目自身的正确性、性能门槛时，选
[constraint-driven-development](../skills/constraint-driven-development/SKILL.md)
（[改写说明](../skills/constraint-driven-development/SOURCE.md)）。
它们是改写后的指令，不是已安装的守卫或钩子。

**上下文：** Unity 项目与版本文件、包解析证据、目标平台、当前调用者、存档样例
和已批准预算。文档要匹配实际环境，不能用记忆中的版本代替。

**证据：** 声明与解析版本、来源引用、契约验收用例及门槛产物。分别记录文档支持、
编译与运行观察。未知阈值保持为建议或测量项，不能自行编成发布门槛。

> 示例：阅读 source-driven-development，检查[Unity 包集成]的声明版本与解析版本，并引用匹配的 API 文档。区分已验证事实和缺失的编译、运行证据；不要安装任何内容。

## 背包与存档

容量、堆叠、装备与奖励先看上面的角色扮演游戏规则。共享物品或任务定义可用
[unity-scriptableobjects](../skills/unity-scriptableobjects/SKILL.md)
（[使用限制](../skills/unity-scriptableobjects/SOURCE.md)）；持久玩家状态、版本与恢复选
[save-systems](../skills/save-systems/SKILL.md)
（[使用限制](../skills/save-systems/SOURCE.md)）。角色可变状态应与共享定义分离。
重试可能重复发奖时，明确操作及存档契约。

**上下文：** 物品 ID 与资源、当前背包状态所有者、序列化器、旧存档样例和临时
存档位置；如有条件，提供 Unity 编辑器与测试工具。

**证据：** 存取往返与迁移结果、背包满时拒绝、重复领取行为、写入中断恢复，
以及共享定义不被污染。静态通道或运行时集合还需按项目域重载设置验证场景切换
及第二次 Play。

> 示例：阅读完整 save-systems 包，为[旧存档样例]设计迁移，失败时保留原始存档。列出往返、重复奖励和中断写入检查，并说明这里实际能运行哪些。

## 战斗与敌人

伤害与资源不变量看角色扮演游戏规则。敌人决策和路径选
[game-ai](../skills/game-ai/SKILL.md)（[使用限制](../skills/game-ai/SOURCE.md)）；
允许或阻止的交互类别选
[collision-layers](../skills/collision-layers/SKILL.md)
（[使用限制](../skills/collision-layers/SOURCE.md)）；命中反馈选
[game-feel](../skills/game-feel/SKILL.md)（[使用限制](../skills/game-feel/SOURCE.md)）。
按实际改动选择职责层，允许碰撞不等于应结算伤害。

**上下文：** 战斗规则、决策状态、二维或三维层分配、移动或导航集成与可复现遭遇。
技能不附带引擎导航或物理实现。

**证据：** 允许与拒绝的命中、单次伤害、状态中断、可达性或卡住行为，以及暂停
或叠加后的反馈。保留序列化层 ID，确认顿帧后恢复的是预期时间状态。

> 示例：阅读 collision-layers，为[2D 战斗场景]用现有层 ID 提出交互矩阵，包含应阻止的友方命中。区分碰撞候选与伤害规则，并列出仍需进行的引擎测试。

## 对话、本地化与音频

分支与叙事状态选
[dialogue-systems](../skills/dialogue-systems/SKILL.md)
（[使用限制](../skills/dialogue-systems/SOURCE.md)）；稳定文本 ID、回退与实时语言切换选
[game-localization](../skills/game-localization/SKILL.md)
（[使用限制](../skills/game-localization/SOURCE.md)）；混音、压低其他声音与过渡选
[audio-design](../skills/audio-design/SKILL.md)
（[使用限制](../skills/audio-design/SOURCE.md)）。仓库不提供 Ink/Yarn、音频中间件或
运行时集成。

**上下文：** 对话图、状态变化、语言表与字体、现有运行器和音频系统，以及代表性
对话。Unity 音频需要将偏向 Godot 的示例适配到项目实际音频 API。

**证据：** 选项可达性、明确的继续输入、奖励或标志不重复变更、字体回退、切换语言
不重置游戏状态，以及真实测量或听测的音频过渡。对话图检查不能代替实际播放，
也不能证明采样级同步。

> 示例：阅读 game-localization，为[任务对话]设计英中切换，保留稳定任务与台词 ID。列出字体回退和状态保持检查，不要声称已测试运行时切换。

## 界面与无障碍

游戏 HUD、菜单、安全区、焦点和界面流程选
[game-ui-ux](../skills/game-ui-ux/SKILL.md)
（[使用限制](../skills/game-ui-ux/SOURCE.md)）。输入、可读性或运动效果偏好按需要补充
[a11y-controls](../skills/a11y-controls/SKILL.md)
（[使用限制](../skills/a11y-controls/SOURCE.md)）。浏览器网站或启动器网页的视觉方向选
[frontend-design](../skills/frontend-design/SKILL.md)
（[使用限制](../skills/frontend-design/SOURCE.md)）。网页设计审阅不能验证原生游戏界面。

**上下文：** 所选界面系统、视口与安全区缩放、界面栈、状态事件、设备、字体与
相关偏好。浏览器工具只适用于网页界面。技能不附带具体引擎控件或重映射器。

**证据：** 相关尺寸下的截图、手柄或键盘焦点遍历、返回与暂停恢复、事件更新及
非颜色提示。评估无障碍效果时加入代表性用户检查；这不是认证。

> 示例：阅读 game-ui-ux，检查[背包菜单]的安全区布局和手柄焦点，包括从设置返回。区分实际截图或输入轨迹、修复建议和无法执行的运行检查。

## 输入

动作映射、设备与改键选
[unity-input-system](../skills/unity-input-system/SKILL.md)
（[使用限制](../skills/unity-input-system/SOURCE.md)），从项目已有的包和 Input Actions
开始。仓库不会安装 `com.unity.inputsystem`。

**上下文：** 已解析的 Input System 版本、动作资源、映射所有者、偏好存储，以及
可用键盘、手柄或 Input Debugger。

**证据：** 游戏与菜单映射隔离、按下与持续输入语义、取消与重叠改键行为、禁用或
销毁时的清理，以及持久化。上游改键草稿还需要生命周期与取消处理。

> 示例：阅读 unity-input-system，按已安装版本检查[改键流程]的取消、操作重叠和禁用或销毁清理。保留当前绑定，并报告实际进行的测试。

## 动画与过场

Animator 过渡、层与 IK 选
[unity-animation](../skills/unity-animation/SKILL.md)
（[使用限制](../skills/unity-animation/SOURCE.md)）。过场期间输入、相机、界面或
游戏状态改变所有者时，选
[cutscene-handoff](../skills/cutscene-handoff/SKILL.md)
（[使用限制](../skills/cutscene-handoff/SOURCE.md)）。不附带动画片段、骨骼或 Timeline
集成；经过动画时长不能证明战斗操作完成。

**上下文：** 控制器参数与动画、骨骼或 Avatar、根运动策略、过场前后的控制权归属，
以及跳过或中断规则。

**证据：** 真实过渡与中断轨迹、所需 IK 配置、跳过、失焦或场景卸载时的恢复，
以及幂等回调。跳过或重复完成回调不能重复发奖或改变标志。

> 示例：阅读 cutscene-handoff，为[任务过场]定义进入、跳过和场景卸载时输入、相机与 UI 的恢复，以及单次奖励处理。列出运行用例，不要另造过场框架。

## 关卡与生成

手工关卡的通行、遭遇与门槛选
[level-design](../skills/level-design/SKILL.md)
（[使用限制](../skills/level-design/SOURCE.md)）；种子生成与验证选
[procedural-gen](../skills/procedural-gen/SKILL.md)
（[使用限制](../skills/procedural-gen/SOURCE.md)）。图连通不等于玩家可通行，
也不证明每把钥匙都能拿到。

**上下文：** 移动尺度、碰撞与相机规则、钥匙和门的位置、种子、边界及生成重试上限。
仓库不提供关卡资源或完整生成器。

**证据：** 可复现种子、真实通行规则下的目标可达性、钥匙先于门、受限失败和试玩
节奏。保留失败种子用于回归，不能重掷到成功就算通过。

> 示例：阅读 procedural-gen，为[种子地牢]定义验证，包括先拿钥匙再过锁门的可达性和受限重试。保留失败种子，区分图检查与引擎通行测试。

## 瓦片地图、像素画与素材

瓦片调色板与 RuleTile 选
[unity-tilemap](../skills/unity-tilemap/SKILL.md)
（[使用限制](../skills/unity-tilemap/SOURCE.md)）；像素采样、相机、导入或管线问题选
[unity-2d-pixel-perfect](../skills/unity-2d-pixel-perfect/SKILL.md)
（[使用限制](../skills/unity-2d-pixel-perfect/SOURCE.md)）；美术方向、来源和可选栅格
检查选 [create-game-assets](../skills/create-game-assets/SKILL.md)
（[使用限制](../skills/create-game-assets/SOURCE.md)）。它们不提供美术素材、生成器或引擎。

**上下文：** Unity 版本、实际渲染管线、相机、精灵设置、网格或瓦片和素材权属。
RuleTile 模板需要项目中的 Tilemap Extras 包；可选栅格工具需要文档指定的
Python/Pillow 环境。执行前先检查，并指定临时输出位置。

**证据：** 素材尺寸与许可、导入差异、瓦片相邻拼接与碰撞体，以及目标分辨率下
的静图和运动。静态 PNG 不能证明闪烁已修复。素材检查器有已记录的差一错误，
所以颜色限制需独立核实。

> 示例：阅读 unity-2d-pixel-perfect，按项目实际管线和相机排查[移动精灵闪烁]。提出最小改动和运动捕获检查；除必要改动外，保留素材导入设置。

## 调试还是性能分析

功能故障与可信运行证据选
[unity-debug](../skills/unity-debug/SKILL.md)
（[使用限制](../skills/unity-debug/SOURCE.md)）。功能正常但需要可比较的帧耗时或
工作量测量时，选 [unity-profiling](../skills/unity-profiling/SKILL.md)
（[使用限制](../skills/unity-profiling/SOURCE.md)）。如果“感觉不对”可能指两者，
先获取可复现症状再选择。既慢又失效的情况可能需要分阶段配合，但先确认运行本身可信。

**上下文：** 与本次运行关联的新日志与结果、复现步骤、项目版本和可用编辑器或
测试工具。性能工作还需测量模式、构建、设备、种子、负载和可比较窗口。
可选实时编辑器命令需要另外的工具，仓库不会安装。

**证据：** 调试需真实发现与执行的测试及新产物，退出码 0 或陈旧 XML 不够。
性能需可比较条件下的前后窗口、分布和缺失计数器说明。
编辑器诊断不能证明目标设备上的 Player 构建性能。

> 示例：阅读 unity-debug，诊断[复现步骤]，确认测试工具产生了本次运行日志与结果。报告已观察证据、缺失工具和未运行检查，不要仅凭退出码 0 推断成功。

## 测试与代码审查

配合项目现有测试工具的行为改动选
[test-driven-development](../skills/test-driven-development/SKILL.md)
（[使用限制](../skills/test-driven-development/SOURCE.md)）；声称通过或完成前选
[verification-before-completion](../skills/verification-before-completion/SKILL.md)
（[使用限制](../skills/verification-before-completion/SOURCE.md)）。准备独立审查选
[requesting-code-review](../skills/requesting-code-review/SKILL.md)
（[使用限制](../skills/requesting-code-review/SOURCE.md)）；评估已收到的意见选
[receiving-code-review](../skills/receiving-code-review/SKILL.md)
（[使用限制](../skills/receiving-code-review/SOURCE.md)）。这是不同审查阶段。

**上下文：** 需求、失败用例、真实测试命令、明确的 base/head 修订，以及计划包含
的已暂存或未暂存工作。独立审查需要受支持的审查机制或人类；不可用时说明限制。
不能假设 `HEAD~1` 覆盖完整改动。

**证据：** 相关失败与通过测试输出、本次完整检查、审查范围，以及对反馈的技术核实。
审查就绪不等于获准合并或发布。

> 示例：阅读 requesting-code-review，按[需求]准备从[base SHA]到[head SHA]的审查，附测试证据，并说明范围外的未提交改动。没有独立审查者时提供请求材料，标记审查未运行。

## Godot 入门

Godot 4.x 项目、节点、场景、资源、Input Map 与编辑器流程选
[godot-fundamentals](../skills/godot-fundamentals/SKILL.md)
（[使用限制](../skills/godot-fundamentals/SOURCE.md)）。只为当前功能补充引擎通用的
角色扮演游戏、存档或界面技能；Unity 包不能直接当作 Godot 实现。

**上下文：** 已有 `project.godot`、安装的引擎版本、场景树、资源所有权和相关输入
动作。仓库不会安装引擎或插件。

**证据：** 真实解析或导入结果，再验证场景启动、输入和节点生命周期。
无界面导入本身不能证明玩法。

> 示例：阅读 godot-fundamentals，检查[已有 Godot 项目]，为[功能]提出最小场景与输入配置。使用已安装版本，保留资源，区分导入检查与未运行玩法检查。

## 文档

功能需要教程、操作指南、参考或解释文档时，选
[documentation-writer](../skills/documentation-writer/SKILL.md)
（[使用限制](../skills/documentation-writer/SOURCE.md)）。遵循澄清与提纲审阅步骤，
描述当前项目真实具备的行为。

**上下文：** 读者、当前实现、支持版本、已有文档和已核实命令。
仓库不附带 PDF/Word 转换工具。

**证据：** 有源码依据的步骤、已检查的链接，以及实际运行或明确标记未运行的例子。
文档不是运行认证。

> 示例：阅读 documentation-writer，为[读者]编写[已实现功能]的操作指南，先提交提纲审阅。使用已核实命令，标记未运行的例子。

## 并行工作

只有任务独立、宿主支持且已授权子代理时，才选
[dispatching-parallel-agents](../skills/dispatching-parallel-agents/SKILL.md)
（[使用限制](../skills/dispatching-parallel-agents/SOURCE.md)）。避免同时修改同一资源
或共享状态。不能派发时顺序完成或提供交接计划，不要声称启动了代理。

**上下文：** 明确边界、文件归属、共享约束、可用派发机制与集成所有者。

**证据：** 每个任务的真实产物与检查，再核实集成后的差异和测试。
分工计划不等于已完成的委派工作。

> 示例：阅读 dispatching-parallel-agents，判断[任务列表]是否独立并识别共享文件风险。提出归属与集成检查；只有这里支持且已授权时才派发。

## 缺少技能或测试工具时

上游提到的配套技能不一定在仓库内。例如不附带 Unity CLI 安装器、通用 Unity C#
实现技能、NavMesh 运行时、Timeline 集成或引擎专用界面适配器。
缺失的实现职责应交给项目现有所有者与匹配版本的文档，或明确提出缺少的能力。
不能假装相关概念技能已补齐所有空缺，也不能自动安装工具。

缺少引擎、设备、浏览器、测试工具或独立审查者时，仍可完成有用的静态工作：
映射代码、检查样例、起草契约和精确验证流程。报告具体缺失工具，并标记相关检查
**未运行**。文档支持、编译、自动测试、人工观察与目标设备测量应分别报告。

例如：“已检查存档迁移样例；没有可用编辑器，Unity PlayMode 测试未运行。
下一步需要在目标环境执行指定的往返与中断写入测试。”这说明了真实边界，
不是宣称功能已经正确。

[仓库验证](validation.md)检查静态打包与来源；
[双语评估流程](evaluations.md)提供人工编写的路由、合成证据样例与真实状态记录。
两者都不能证明真实代理路由质量或引擎行为。本指南提示为原创文档例子，只经过
静态审阅，没有用模型或引擎运行验证。
