# 游戏工程技能改写草案 / Game engineering skill drafts

为 Unity RPG 工作流改写的三个工程技能，保留可迁移到 Godot、Unreal Engine 和后端项目的原则。技能正文使用英文，便于跨工具复用。本包是待审阅草案；未安装、未推送到 GitHub。

## 先看什么

1. [source-driven-development](../../skills/source-driven-development/SKILL.md)：确认项目实际引擎和包版本，再依据对应官方文档作 API 决策；区分文档依据、编译检查和运行时验证
2. [constraint-driven-development](../../skills/constraint-driven-development/SKILL.md)：用项目认可的场景、硬件、单位、阈值和检查方法定义质量门槛；不套用统一 FPS/覆盖率/内存指标
3. [api-and-interface-design](../../skills/api-and-interface-design/SKILL.md)：以 Unity C# 模块、命令/事件、生命周期、资源所有权、存档兼容和重复奖励处理为中心；后端规则按需启用

## 审阅重点

- 是否符合现有项目分层、异步方案和存档策略，而非强迫引入新框架
- 项目版本、目标平台、最低硬件和预算是否有真实依据
- 无引擎、设备或测试结果时，能否清楚说明哪些验证没有执行
- 接口设计是否覆盖重复触发、场景卸载、迟到回调、资源释放和旧存档
- 每个技能文件夹的 `LICENSE` 和 `SOURCE.md` 是否随正文一起保留

使用时只读取当前任务需要的技能；三者不存在强制加载顺序。可分别复制整个文件夹，不依赖其他技能或共享私有文件。是否安装或加入技能仓库应在审阅后另行决定。

## What changed

These are substantial adaptations, not verbatim upstream packages. The source-driven skill now starts with resolved game-engine/package evidence. The constraint-driven skill uses project-owned budgets and explicit measurement protocols; it includes no executable floor guard. The API skill focuses on game module contracts, persistence and lifetime semantics rather than defaulting to HTTP endpoints.

Each package is self-contained and includes its own MIT license and provenance record. There are no installers, hooks, plugin manifests, executable examples or dependencies on another skill. The original constraint floor-guard reference was read, but its JavaScript implementation is intentionally not bundled or represented as Unity-ready.

## Verification and limits

See [VALIDATION.md](VALIDATION.md) for the completed checks and their scope. Static checks and fictional scenario reviews assess document structure and instruction usability. They do not prove game correctness or reliable behavior across models. No Unity/Godot/Unreal project, player, device benchmark or production backend was run. Example approaches and runtime test suggestions remain unimplemented and untested in an actual game project.

## Provenance

Adapted on 2026-10-04 (UTC) from [addyosmani/agent-skills at revision 1401c8b8030e023baeebb31781a6653fe8e93026](https://github.com/addyosmani/agent-skills/commit/1401c8b8030e023baeebb31781a6653fe8e93026). Original copyright: 2025 Addy Osmani. The full [MIT license](LICENSE) is retained at the bundle root and in each package. Per-package `SOURCE.md` records exact source links and changes. New adaptation text uses the same MIT terms. No upstream author or vendor endorsement is implied.
