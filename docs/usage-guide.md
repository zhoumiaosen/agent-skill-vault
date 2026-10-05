# Task-based usage guide / 按任务使用指南

Start with the task you need to complete, then read the relevant skill package.
The [catalog](../README.md) remains the list of available skills; this guide shows
how to choose and combine them. These are instructions and supporting material,
not an installed game framework. No engine or model execution is claimed here.

先明确要完成的任务，再阅读相关技能包。[目录](../README.md)列出已有技能；本指南
说明怎样选用和组合。技能是指令与辅助材料，不是已安装的游戏框架。这里不声称
运行过引擎或模型。

## Start with a small scope

Choose one primary skill. Add another only when the task crosses its boundary;
do not load every skill into every request. Read its `SKILL.md`, `SOURCE.md` and
needed references/resources before acting. When copying a package, retain all
supporting files and its license/NOTICE. Your host determines how instructions
are loaded; mentioning a skill name in a prompt does not install it or prove the
host discovered it. If discovery is unavailable, provide the package as context.

先选一个主技能，只在任务跨越职责边界时补充另一个。阅读入口、来源说明和所需
参考材料；复制时保留完整辅助文件及许可声明。宿主决定加载方式；提示中写出名字
不等于安装或成功发现技能。没有自动发现功能时，将完整技能包作为上下文提供。

Include the actual project root, engine/package versions, target platform,
reproduction or desired behavior, affected files, and available test tools.
The prompts below are starting requests: replace bracketed inputs with real
values and keep the work inside the permissions you granted.

提供真实项目路径、引擎与包版本、目标平台、复现步骤或目标行为、相关文件，以及
可用测试工具。下面的提示是起点；用真实信息替换方括号，并限定授权范围。

| What you need / 要做什么 | Start here / 从这里开始 |
|---|---|
| Decide what to build / 确定设计 | [Game direction](#game-direction) |
| Plan a change / 规划改动 | [Map and plan](#map-and-plan), [versions and contracts](#versions-and-contracts) |
| Build RPG systems / 制作 RPG 系统 | [Inventory and saves](#inventory-and-saves), [combat and enemies](#combat-and-enemies), [dialogue and audio](#dialogue-localization-and-audio) |
| Build player-facing controls / 制作交互 | [UI](#ui-and-accessibility), [input](#input), [animation](#animation-and-cutscenes) |
| Build worlds and assets / 制作世界与素材 | [Levels](#levels-and-generation), [tilemaps and pixel art](#tilemaps-pixel-art-and-assets) |
| Investigate or verify / 排查与验证 | [Debugging or profiling](#debugging-or-profiling), [tests and review](#tests-and-code-review) |
| Start in Godot, document, or split work / Godot 入门、文档或分工 | [Godot](#godot-starter), [documentation](#documentation), [parallel work](#parallel-work) |

## Game direction

Start with [game-design](../skills/game-design/SKILL.md)
([caveats](../skills/game-design/SOURCE.md)) for mechanics, progression and a
small playable loop. Use [rpg](../skills/rpg/SKILL.md)
([caveats](../skills/rpg/SOURCE.md)) when stats, equipment, combat or quest rules
need an RPG model. If a technical choice is unresolved, use
[create-technical-spike](../skills/create-technical-spike/SKILL.md)
([caveats](../skills/create-technical-spike/SOURCE.md)) for a bounded experiment.

先用 game-design 明确核心循环；涉及属性、装备和任务规则时再选 rpg。
技术方案还不确定时，用限时技术探索收集证据，不要直接扩成完整系统。

**Context / 上下文:** Player goals, one representative encounter, existing
rules and scope; for a spike, the question, time limit and available sandbox.
提供玩家目标、代表性遭遇、已有规则和范围；探索还需要问题、时限与可用沙盒。

**Evidence / 证据:** A concrete loop and acceptance examples; then actual
playtest observations or experiment output when tools exist. Formula sketches
alone do not establish balance. 明确循环与验收例子；有工具时记录真实试玩或实验结果。
公式草稿不能证明平衡性。

> EN: Read game-design. Propose one playable loop for [RPG concept], with a concrete encounter and acceptance criteria. List what needs a playtest; do not claim the design has been tested.
>
> 中文：阅读 game-design，为[角色扮演游戏概念]提出一个可玩循环，给出具体遭遇和验收标准。列出需要试玩的内容，不要声称已经测试过设计。

## Map and plan

Use [context-map](../skills/context-map/SKILL.md)
([caveats](../skills/context-map/SOURCE.md)) to find affected files and owners;
then [create-implementation-plan](../skills/create-implementation-plan/SKILL.md)
([caveats](../skills/create-implementation-plan/SOURCE.md)) for ordered work and
verification. Record a consequential choice with
[create-architectural-decision-record](../skills/create-architectural-decision-record/SKILL.md)
([caveats](../skills/create-architectural-decision-record/SOURCE.md)), rather than
creating an ADR for every small edit. Map review is part of context-map's process.

先定位文件与职责，再规划步骤和验证。影响长期结构的选择才需要 ADR；小改动
不必都写决策记录。context-map 要求先审阅映射，再进入实现。

**Context / 上下文:** Repository access, actual task, current tests, relevant
assets/assemblies and constraints. Replace upstream input placeholders and
document paths with your project's conventions. 提供仓库、真实任务、测试、相关资源与
程序集约束；将上游输入占位符与文档路径替换为项目约定。

**Evidence / 证据:** File-backed dependency map, reviewed plan, explicit
acceptance commands and decision alternatives. A plan is not implementation or
permission to merge. 以文件为依据的依赖映射、已审阅计划、验收命令与备选方案；计划
不等于已实现，也不代表获准合并。

> EN: Read context-map. Map the files and tests affected by [quest change], explain the dependencies, and stop for map review before implementation. Preserve unrelated work.
>
> 中文：阅读 context-map，映射[任务系统改动]涉及的文件和测试，解释依赖关系，并在实现前停下来审阅映射。保留无关改动。

## Versions and contracts

Use [source-driven-development](../skills/source-driven-development/SKILL.md)
([adaptation notes](../skills/source-driven-development/SOURCE.md)) for unfamiliar
or version-sensitive APIs. Use [api-and-interface-design](../skills/api-and-interface-design/SKILL.md)
([adaptation notes](../skills/api-and-interface-design/SOURCE.md)) for state
ownership, module/event/lifetime and save contracts. Use
[constraint-driven-development](../skills/constraint-driven-development/SKILL.md)
([adaptation notes](../skills/constraint-driven-development/SOURCE.md)) when
project-owned correctness or performance gates need definition or protection.
These are adapted instructions, not installed guards or hooks.

陌生或版本敏感 API 需要来源证据；模块、事件、生命周期和存档边界需要明确契约；
质量门槛由项目决定。三个技能是改写后的指令，不包含已安装的守卫或钩子。

**Context / 上下文:** Unity project/version files and resolved package evidence,
target platform, current callers, save fixtures and approved budgets. Use
documentation matching the actual stack; do not substitute a remembered version.
提供版本与包解析证据、平台、调用者、旧存档样例和已批准预算；文档要匹配实际环境。

**Evidence / 证据:** Requested/resolved versions, source citations, contract
acceptance cases and gate artifacts. Separate documented support, compilation
and runtime observations. Unknown thresholds stay proposals or measurements,
not invented delivery gates. 分开记录文档支持、编译与运行结果；未知阈值保持为建议或
测量项，不能自行编成发布门槛。

> EN: Read source-driven-development. For [Unity package integration], inspect requested and resolved versions and cite matching API documentation. Separate verified facts from missing compile/runtime evidence; do not install anything.
>
> 中文：阅读 source-driven-development，检查[Unity 包集成]的声明版本与解析版本，并引用匹配的 API 文档。区分已验证事实和缺失的编译、运行证据；不要安装任何内容。

## Inventory and saves

Start with the RPG rules above for capacity, stacking, equipment and rewards.
Use [unity-scriptableobjects](../skills/unity-scriptableobjects/SKILL.md)
([caveats](../skills/unity-scriptableobjects/SOURCE.md)) for shared item/quest
definitions, and [save-systems](../skills/save-systems/SKILL.md)
([caveats](../skills/save-systems/SOURCE.md)) for durable player state, versioning
and recovery. Keep per-character mutable state separate from shared definitions.
Use an explicit operation/save contract when retries could grant a reward twice.

容量、堆叠、装备与奖励先看 RPG 规则。共享定义可用 ScriptableObject；角色可变状态、
版本与恢复属于存档系统。重试可能重复发奖时，要明确操作及存档契约。

**Context / 上下文:** Item IDs/assets, current inventory owner, serializer, old
save samples and a disposable save location; Unity Editor/tests if available.
提供物品 ID、状态所有者、序列化器、旧存档与临时存档位置，以及可用编辑器和测试。

**Evidence / 证据:** Round trip and migration outcomes, full-inventory rejection,
repeat-claim behavior, interrupted-write recovery and unchanged shared definitions.
For static channels/runtime sets, test scene changes and a second Play session
with the project's domain-reload settings. 存取往返、迁移、背包满时拒绝、重复领取、写入
中断恢复及共享定义不被污染；静态通道还需验证场景切换与重复 Play。

> EN: Read the complete save-systems package. Design migration for [old save fixture] and preserve the original on failure. Specify round-trip, duplicate-reward and interrupted-write checks; report which can actually run here.
>
> 中文：阅读完整 save-systems 包，为[旧存档样例]设计迁移，失败时保留原始存档。列出往返、重复奖励和中断写入检查，并说明这里实际能运行哪些。

## Combat and enemies

Use RPG rules for damage/resource invariants. Select
[game-ai](../skills/game-ai/SKILL.md) ([caveats](../skills/game-ai/SOURCE.md)) for
enemy decisions and paths; [collision-layers](../skills/collision-layers/SKILL.md)
([caveats](../skills/collision-layers/SOURCE.md)) for allowed/blocked interaction
categories; or [game-feel](../skills/game-feel/SKILL.md)
([caveats](../skills/game-feel/SOURCE.md)) for hit feedback. Choose the layer that
is actually changing. A collision permission does not itself authorize damage.

伤害与资源不变量看 RPG 规则；敌人决策和路径、碰撞类别、命中反馈是不同职责。
按实际改动选择，不要把“允许碰撞”当成“应结算伤害”。

**Context / 上下文:** Combat rules, decision states, 2D/3D layer assignments,
movement/navigation integration and a reproducible encounter. Engine navigation
or physics implementations are not bundled by these skills. 提供战斗规则、状态、
层分配、移动或导航集成与可复现遭遇；技能不附带引擎导航或物理实现。

**Evidence / 证据:** Allowed and rejected hits, one-time damage, state
interruptions, reachability/stuck behavior and feedback after pause/overlap.
Preserve serialized layer IDs. Verify hit-stop restores the intended time state.
验证允许与拒绝的命中、单次伤害、中断、可达性及暂停或叠加后的反馈；保留序列化层 ID，
确认顿帧后恢复的是正确时间状态。

> EN: Read collision-layers. For [2D combat scene], propose an interaction matrix using existing layer IDs, including blocked friendly hits. Distinguish collision candidates from damage rules and list engine tests still needed.
>
> 中文：阅读 collision-layers，为[2D 战斗场景]用现有层 ID 提出交互矩阵，包含应阻止的友方命中。区分碰撞候选与伤害规则，并列出仍需进行的引擎测试。

## Dialogue, localization and audio

Select [dialogue-systems](../skills/dialogue-systems/SKILL.md)
([caveats](../skills/dialogue-systems/SOURCE.md)) for branches and narrative
state; [game-localization](../skills/game-localization/SKILL.md)
([caveats](../skills/game-localization/SOURCE.md)) for stable text IDs, fallback
and live language switching; [audio-design](../skills/audio-design/SKILL.md)
([caveats](../skills/audio-design/SOURCE.md)) for mix, ducking and transitions.
Ink/Yarn, audio middleware and runtime integrations are not supplied.

分支与叙事状态、稳定文本 ID 与语言切换、混音与过渡分别选对应技能。
仓库不提供 Ink/Yarn、音频中间件或运行时集成。

**Context / 上下文:** Dialogue graph, state mutations, locale tables/fonts,
existing runner/audio system and representative conversation. For Unity audio,
adapt the Godot-oriented sketches to the project's actual audio APIs.
提供对话图、状态变化、语言表与字体、现有运行器和音频系统；Unity 音频示例需要适配。

**Evidence / 证据:** Reachable choices, explicit continue input, no repeated
reward/flag mutation, fallback glyphs, language switching without resetting game
state, and measured/listened-to audio transitions. Separate a dialogue graph
inspection from actual playback or sample-accurate synchronization claims.
检查选项可达性、继续输入、状态不重复变更、字体回退与切语言不重置游戏；实际播放和
音频同步结论需要真实听测或测量。

> EN: Read game-localization. Design an English/Chinese switch for [quest dialogue], preserving stable quest and line IDs. Specify font fallback and state-preservation checks; do not claim a runtime switch was tested.
>
> 中文：阅读 game-localization，为[任务对话]设计英中切换，保留稳定任务与台词 ID。列出字体回退和状态保持检查，不要声称已测试运行时切换。

## UI and accessibility

Use [game-ui-ux](../skills/game-ui-ux/SKILL.md)
([caveats](../skills/game-ui-ux/SOURCE.md)) for HUDs, menus, safe areas, focus and
screen flow. Add [a11y-controls](../skills/a11y-controls/SKILL.md)
([caveats](../skills/a11y-controls/SOURCE.md)) for scoped input/readability/motion
preferences. Use [frontend-design](../skills/frontend-design/SKILL.md)
([caveats](../skills/frontend-design/SOURCE.md)) for a browser site or launcher web
page's visual direction. A web-design review does not verify native game UI.

游戏 HUD、菜单、焦点与流程选 game-ui-ux；无障碍偏好按需要补充。
浏览器页面视觉设计选 frontend-design，网页检查不能验证原生游戏 UI。

**Context / 上下文:** Chosen UI system, viewport/safe-area scale, screen stack,
state events, devices, fonts and relevant preferences; browser tools only for a
web surface. Concrete engine widgets/remappers are not bundled. 提供 UI 系统、
视口缩放、界面栈、事件、设备、字体和偏好；技能不附带具体引擎控件或重映射器。

**Evidence / 证据:** Screenshots at relevant sizes, controller/keyboard focus
traversal, back/pause restoration, event updates and non-color cues. Include
representative user checks when evaluating accessibility; this is not certification.
记录尺寸截图、焦点遍历、返回或暂停恢复、事件更新及非颜色提示；无障碍效果还需
代表性用户验证，不是认证。

> EN: Read game-ui-ux. Review [inventory menu] for safe-area layout and controller focus, including return from settings. Separate observed screenshots/input traces from proposed fixes and unavailable runtime checks.
>
> 中文：阅读 game-ui-ux，检查[背包菜单]的安全区布局和手柄焦点，包括从设置返回。区分实际截图或输入轨迹、修复建议和无法执行的运行检查。

## Input

Use [unity-input-system](../skills/unity-input-system/SKILL.md)
([caveats](../skills/unity-input-system/SOURCE.md)) for action maps, devices and
rebinding. Start from the project's existing package and Input Actions; this
vault does not install `com.unity.inputsystem`.

动作映射、设备与改键选 unity-input-system，从现有包和 Input Actions 开始。
仓库不会安装输入包。

**Context / 上下文:** Resolved Input System version, action assets, map owners,
save preferences and available keyboard/controller or Input Debugger.
提供解析版本、动作资源、映射所有者、偏好存储与可用设备或调试工具。

**Evidence / 证据:** Gameplay/menu map isolation, press/hold semantics, cancel
and overlapping-rebind behavior, disable/destroy cleanup and persistence.
The upstream rebinding sketch needs lifecycle/cancellation handling.
验证游戏与菜单隔离、按下与持续语义、取消或重叠改键、生命周期清理及持久化。

> EN: Read unity-input-system. Audit [rebinding flow] for cancel, overlapping operations and disable/destroy cleanup using the installed package. Preserve current bindings and report tests actually performed.
>
> 中文：阅读 unity-input-system，按已安装版本检查[改键流程]的取消、操作重叠和禁用或销毁清理。保留当前绑定，并报告实际进行的测试。

## Animation and cutscenes

Use [unity-animation](../skills/unity-animation/SKILL.md)
([caveats](../skills/unity-animation/SOURCE.md)) for Animator transitions, layers
and IK. Use [cutscene-handoff](../skills/cutscene-handoff/SKILL.md)
([caveats](../skills/cutscene-handoff/SOURCE.md)) when input, camera, UI or game
state changes owners during a cinematic. Clips, rigs and Timeline integrations
are not bundled; elapsed animation length is not proof of combat completion.

Animator 过渡、层与 IK 选动画技能；过场期间控制权交接选 cutscene-handoff。
不附带动画、骨骼或 Timeline 集成，经过动画时长不能证明战斗操作完成。

**Context / 上下文:** Controller parameters/clips, rig/Avatar, root-motion
policy, ownership before/after the cutscene and skip/interruption policy.
提供控制器、动画、骨骼、根运动策略、控制权归属与跳过或中断规则。

**Evidence / 证据:** Actual transition/interruption traces, required IK setup,
skip/focus-loss/scene-unload restoration and idempotent callbacks. Rewards and
flags must not be duplicated by skip or repeated completion callbacks.
记录真实过渡、中断、IK 配置、跳过或失焦恢复；重复回调不能重复发奖或改状态。

> EN: Read cutscene-handoff. For [quest cinematic], define entry, skip and scene-unload restoration of input/camera/UI, with one-time reward handling. List the runtime cases; do not implement a new cinematic framework.
>
> 中文：阅读 cutscene-handoff，为[任务过场]定义进入、跳过和场景卸载时输入、相机与 UI 的恢复，以及单次奖励处理。列出运行用例，不要另造过场框架。

## Levels and generation

Use [level-design](../skills/level-design/SKILL.md)
([caveats](../skills/level-design/SOURCE.md)) for authored traversal, encounters
and gates; [procedural-gen](../skills/procedural-gen/SKILL.md)
([caveats](../skills/procedural-gen/SOURCE.md)) for seeded generation and validation.
A connected graph is not proof that a player can traverse it or obtain every key.

手工关卡的路线、遭遇与门槛选 level-design；种子生成与验证选 procedural-gen。
图连通不等于玩家可通行，也不证明每把钥匙都能拿到。

**Context / 上下文:** Movement metrics, collision/camera rules, gate/key
locations, seed, bounds and generation retry limits. No level assets or complete
generator are supplied. 提供移动尺度、碰撞与相机规则、钥匙与门的位置、种子、边界及
重试上限；仓库不提供关卡资源或完整生成器。

**Evidence / 证据:** Reproducible seeds, reachable objectives under actual
traversal rules, key-before-gate ordering, bounded failures and playtest pacing.
Retain failing seeds for regression rather than rerolling until one succeeds.
保留可复现种子、真实规则下的可达性、钥匙先于门、受限失败与试玩节奏；保留失败
种子，不能重掷到成功就算通过。

> EN: Read procedural-gen. Specify validation for [seeded dungeon], including key-before-lock reachability and bounded retries. Keep failing seeds as fixtures and distinguish graph checks from engine traversal tests.
>
> 中文：阅读 procedural-gen，为[种子地牢]定义验证，包括先拿钥匙再过锁门的可达性和受限重试。保留失败种子，区分图检查与引擎通行测试。

## Tilemaps, pixel art and assets

Use [unity-tilemap](../skills/unity-tilemap/SKILL.md)
([caveats](../skills/unity-tilemap/SOURCE.md)) for palettes/RuleTiles;
[unity-2d-pixel-perfect](../skills/unity-2d-pixel-perfect/SKILL.md)
([caveats](../skills/unity-2d-pixel-perfect/SOURCE.md)) for pixel sampling,
camera/import/pipeline issues; [create-game-assets](../skills/create-game-assets/SKILL.md)
([caveats](../skills/create-game-assets/SOURCE.md)) for art direction, provenance
and optional raster inspection. They do not supply art, a generator or an engine.

瓦片调色板与 RuleTile、像素采样或相机导入问题、美术方向与来源管理分别选对应技能。
技能不提供美术素材、生成器或引擎。

**Context / 上下文:** Unity version, actual render pipeline, camera setup,
sprite settings, grid/tiles and asset ownership. RuleTile templates need the
project's Tilemap Extras package. Optional raster utilities need their documented
Python/Pillow environment; inspect before running and choose disposable outputs.
提供实际管线、相机、精灵设置、网格和素材权属；RuleTile 与可选栅格工具需核对项目
已有依赖，执行前先检查，并指定临时输出。

**Evidence / 证据:** Asset dimensions/licenses, import diff, tile adjacency and
colliders, still captures plus motion at target resolution. Do not treat a still
PNG as proof that shimmering is fixed. Independently check color limits because
the bundled asset checker has a documented off-by-one caveat.
记录尺寸与许可、导入差异、相邻拼接与碰撞体、目标分辨率静图及运动；静图不能证明
闪烁已修复，颜色限制需独立核实。

> EN: Read unity-2d-pixel-perfect. Investigate [moving-sprite shimmer] using the project's actual pipeline and camera. Propose a minimal change and a motion capture check; preserve asset import settings unless the change requires them.
>
> 中文：阅读 unity-2d-pixel-perfect，按项目实际管线和相机排查[移动精灵闪烁]。提出最小改动和运动捕获检查；除必要改动外，保留素材导入设置。

## Debugging or profiling

Use [unity-debug](../skills/unity-debug/SKILL.md)
([caveats](../skills/unity-debug/SOURCE.md)) for functional failures and trustworthy
runtime evidence. Use [unity-profiling](../skills/unity-profiling/SKILL.md)
([caveats](../skills/unity-profiling/SOURCE.md)) when behavior works but you need
comparable frame/work measurements. If "it feels wrong" could mean either, ask
for a reproducible symptom before choosing. A slow failure can need both, in
stages, after the run itself is trusted.

功能失效或运行证据不可信时选调试；功能正常但要比较帧耗时或工作量时选性能分析。
“感觉不对”不足以判断，应先获取复现症状。两者可能分阶段配合。

**Context / 上下文:** Fresh logs/results tied to the current run, reproduction,
project version and available Editor/test harness. Performance work also needs
instrument/build/device, seed, workload and comparable windows. Optional live
Editor commands need separate tooling; the vault does not install it.
提供本次运行日志、复现、版本与可用测试工具；性能还需模式、构建、设备、种子和负载。

**Evidence / 证据:** For debugging, actual discovered/executed tests and fresh
artifacts; exit zero or stale XML is insufficient. For profiling, before/after
windows under comparable conditions, distributions and missing-counter notes.
Editor diagnostics do not establish device-player performance.
调试需真实发现与执行的测试及新产物；性能需可比较窗口、分布和缺失计数器说明。
编辑器诊断不能证明目标设备上的 Player 构建性能。

> EN: Read unity-debug. Diagnose [reproduction] and verify the harness produced fresh logs/results for this run. Report observed evidence, missing tools and unrun checks; do not infer success from exit zero.
>
> 中文：阅读 unity-debug，诊断[复现步骤]，确认测试工具产生了本次运行日志与结果。报告已观察证据、缺失工具和未运行检查，不要仅凭退出码 0 推断成功。

## Tests and code review

Use [test-driven-development](../skills/test-driven-development/SKILL.md)
([caveats](../skills/test-driven-development/SOURCE.md)) for a behavior change
with the project's test runner; [verification-before-completion](../skills/verification-before-completion/SKILL.md)
([caveats](../skills/verification-before-completion/SOURCE.md)) before a passing
or completion claim. Use [requesting-code-review](../skills/requesting-code-review/SKILL.md)
([caveats](../skills/requesting-code-review/SOURCE.md)) to prepare an independent
review, and [receiving-code-review](../skills/receiving-code-review/SKILL.md)
([caveats](../skills/receiving-code-review/SOURCE.md)) to evaluate comments already
received. They are different review stages.

行为改动配合现有测试工具；完成声明需要新证据。准备独立审查与评估已有反馈是两个
阶段，分别选 requesting 和 receiving。

**Context / 上下文:** Requirements, failure case, actual test commands, explicit
base/head revisions and intended staged/unstaged work. Independent review needs
a supported reviewer mechanism or a human; name that limitation if unavailable.
Do not assume `HEAD~1` covers the full change. 提供需求、失败例、命令、明确修订范围与
工作区改动；缺少独立审查能力时要说明，不能用自查冒充独立审查。

**Evidence / 证据:** Relevant failing/passing test output, current full-check
results, review coverage and technically verified responses to feedback.
Review readiness does not authorize merge or publication. 记录相关失败与通过输出、
本次完整检查、审查范围及意见核实结果；审查通过不等于获准合并或发布。

> EN: Read requesting-code-review. Prepare a review of [base SHA] through [head SHA] against [requirements], including test evidence and any uncommitted work outside that range. If no independent reviewer is available, provide the request and mark the review not run.
>
> 中文：阅读 requesting-code-review，按[需求]准备从[base SHA]到[head SHA]的审查，附测试证据，并说明范围外的未提交改动。没有独立审查者时提供请求材料，标记审查未运行。

## Godot starter

Use [godot-fundamentals](../skills/godot-fundamentals/SKILL.md)
([caveats](../skills/godot-fundamentals/SOURCE.md)) for a Godot 4.x project,
nodes/scenes/resources, Input Map and editor workflow. Add the relevant
engine-neutral RPG, save or UI skill only for the feature being built; Unity
packages are not drop-in Godot implementations.

Godot 4.x 的节点、场景、资源、Input Map 与编辑器流程选基础技能；只为当前功能补充
通用 RPG、存档或 UI 技能，Unity 包不能直接当作 Godot 实现。

**Context / 上下文:** Existing `project.godot`, installed engine version, scene
tree, resource ownership and relevant input actions. No engine or add-on is
installed by this repository. 提供项目文件、已安装版本、场景树、资源所有者与输入动作。

**Evidence / 证据:** Actual parser/import results, then scene launch, input and
node lifecycle observations. Headless import alone does not prove gameplay.
记录真实解析与导入，再验证场景启动、输入和节点生命周期；无界面导入不能证明玩法。

> EN: Read godot-fundamentals. Inspect [existing Godot project] and propose the smallest scene/input setup for [feature]. Use the installed version, preserve resources, and separate import checks from unrun gameplay checks.
>
> 中文：阅读 godot-fundamentals，检查[已有 Godot 项目]，为[功能]提出最小场景与输入配置。使用已安装版本，保留资源，区分导入检查与未运行玩法检查。

## Documentation

Use [documentation-writer](../skills/documentation-writer/SKILL.md)
([caveats](../skills/documentation-writer/SOURCE.md)) when a feature needs a
tutorial, how-to, reference or explanation. Follow its clarification and outline
review steps; document what the current project actually does.

功能需要教程、操作指南、参考或解释文档时，选 documentation-writer，遵循澄清和
提纲审阅步骤，描述项目现在真实具备的行为。

**Context / 上下文:** Audience, current implementation, supported versions,
existing docs and verified commands. No PDF/Word conversion tools are bundled.
提供读者、实现、支持版本、已有文档与已核实命令；不附带文档转换工具。

**Evidence / 证据:** Source-backed steps, checked links and examples actually
run or clearly marked unrun. Documentation is not runtime certification.
步骤有源码依据、链接已检查；例子运行过或明确标记未运行，不能把文档当作运行认证。

> EN: Read documentation-writer. Draft a how-to for [implemented feature] for [audience], starting with an outline for review. Use verified commands and label examples that have not been run.
>
> 中文：阅读 documentation-writer，为[读者]编写[已实现功能]的操作指南，先提交提纲审阅。使用已核实命令，标记未运行的例子。

## Parallel work

Use [dispatching-parallel-agents](../skills/dispatching-parallel-agents/SKILL.md)
([caveats](../skills/dispatching-parallel-agents/SOURCE.md)) only for independent
tasks when the host supports authorized subagents. Avoid concurrent edits to the
same assets or shared state. If dispatch is unavailable, work sequentially or
provide a handoff plan; do not claim agents were launched.

只有任务独立、宿主支持且已授权子代理时才并行分工；避免同时修改同一资源或共享
状态。不能派发时顺序完成或提供交接计划，不要声称启动了代理。

**Context / 上下文:** Clear boundaries, file ownership, shared constraints,
available dispatch mechanism and integration owner. 提供边界、文件归属、约束、机制和
负责集成的人。

**Evidence / 证据:** Each task's concrete deliverable and checks, then integrated
diff/tests. Separate plans from completed delegated work. 各任务真实产物与检查，以及
集成后的差异与测试；分工计划不等于已完成。

> EN: Read dispatching-parallel-agents. Assess whether [tasks] are independent and identify shared-file risks. Propose ownership and integration checks; dispatch only if authorized and supported here.
>
> 中文：阅读 dispatching-parallel-agents，判断[任务列表]是否独立并识别共享文件风险。提出归属与集成检查；只有这里支持且已授权时才派发。

## When a skill or test tool is missing

A named upstream companion is not automatically in this vault. For example,
there is no bundled Unity CLI installer, general Unity C# implementation skill,
NavMesh runtime, Timeline integration or engine-specific UI adapter. Use the
project's existing owners and version-matched documentation for the missing
implementation boundary, or ask for the specific missing capability. Do not
pretend a related conceptual skill fills every gap or install tools automatically.

上游提到的配套技能不一定在仓库内；例如不附带 Unity CLI 安装器、通用 Unity C#
实现技能、NavMesh 运行时、Timeline 集成或引擎 UI 适配器。缺失的实现职责应交给
项目现有模块与匹配版本的文档，或明确提出缺少的能力，不能假装相关概念技能已补齐。

Without an engine, device, browser, test runner or independent reviewer, finish
the useful static work: map code, inspect fixtures, draft contracts and propose
the exact verification protocol. Report the missing tool and mark the relevant
checks **not run**. Keep documented support, compilation, automated tests,
manual observation and target-device measurements as separate claims.

缺少工具时仍可定位代码、检查样例、起草契约与验证流程，但要报告具体限制，标记
相关检查**未运行**。文档支持、编译、自动测试、人工观察与目标设备测量分别报告。

For example: "Save migration fixture inspection completed; Unity PlayMode tests
not run because no Editor is available. Next evidence needed: execute the named
round-trip and interrupted-write tests on the target environment." This states
an actual boundary rather than claiming the feature works.

例如：“已检查存档迁移样例；没有可用编辑器，Unity PlayMode 测试未运行。
下一步需要在目标环境执行指定的往返与中断写入测试。”这说明了真实边界，不是宣称
功能已经正确。

The [vault validator](validation.md) checks static packaging/provenance. The
[bilingual evaluation protocol](evaluations.md) supplies authored routing and
synthetic evidence cases, with honest run records. Neither establishes real
agent routing quality or engine behavior. The example prompts in this guide are
original documentation examples, statically reviewed; no model or engine runs
were performed to validate them.

[仓库验证](validation.md)检查静态打包与来源；[双语评估流程](evaluations.md)提供
人工编写的路由、合成证据样例和真实状态记录。两者都不能证明真实代理路由质量或
引擎行为。本指南提示为原创文档例子，只经过静态审阅，没有用模型或引擎运行验证。
