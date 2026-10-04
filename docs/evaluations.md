# Bilingual evaluation foundations / 双语评估基础

These original fixtures and tools were written for this vault, without copying
an upstream evaluator. They exercise evaluation data contracts, not a language
model. CI does not load instructions into an agent, dispatch reviews, launch
engines, run upstream scripts, install skills, or call any model/API.

这些原创样例与工具用于检查评估数据契约，不会运行语言模型。CI 不会把技能指令
交给代理执行，不会发起外部审查、启动引擎、运行上游脚本或安装技能。

## What is included / 包含内容

`evaluations/cases.json` contains 38 cases in 19 English/Simplified-Chinese
pairs. The routing portion has 32 cases: positive selections, explicit negative
requests outside the vault, and ambiguous requests requiring clarification.
The principal boundaries are unity-debug/unity-profiling,
game-ui-ux/frontend-design and requesting-code-review/receiving-code-review.
Representative cases cover saves, localization, completion evidence and
version-sensitive API work. Outcomes are authored judgments for these narrow
prompts, not universal ground truth or proof that one skill always excludes
another. Broader tasks can compose skills.

共有 19 组英中配对（38 个样例），其中 32 个路由样例涵盖选择、不应选用技能、
以及应先澄清的请求。预期结果是针对特定请求人工编写的判断，不是通用真理；
更复杂任务可以组合多个技能。负例明确超出整个技能库的范围，而不是只缺少关键词。

Six behavior cases (three paired tasks) use synthetic JSON evidence: stale test
results despite exit zero; incompatible profiling instruments; and a reviewer
claim contradicted by a zero-count caller. They require reading and reasoning
only. The sample function is data inside JSON and is never evaluated. Fixture
checks confirm that stated facts exist; they cannot confirm a model noticed or
reasoned about those facts. `evaluations/not-run.json` records all six behavior
cases as **not_run**. There are no agent/model/engine quality results in this
increment. Unit-test records labeled executed are synthetic test doubles only.

六个行为样例（3 组）只要求阅读合成证据并进行推理。JSON 内的示例函数是数据，
不会被执行。工具能确认预期事实存在，不能证明模型理解了事实。默认行为记录全部
标记为 **not_run（未运行）**；单元测试中的 executed 记录只是测试替身，不是真实代理结果。

## Commands / 命令

Use the existing validation environment (Python 3.10+, pinned requirements):

```sh
python -m pip install -r requirements-validation.txt
python -m unittest discover -s tests -v
python tools/validate_vault.py
python tools/check_evaluations.py check
python tools/check_evaluations.py report evaluations/not-run.json
python tools/check_evaluations.py template > local-run.json
python tools/check_evaluations.py context > local-context.json
```

Use UTF-8 when saving/editing files; old Windows PowerShell redirects may create
UTF-16. These commands print JSON and return 1 on malformed data/records.
`--root PATH` before the subcommand selects another checkout. `context` prints
the full package file inventory and hashes; it does not claim those files were
actually read by a model. All tools are offline and do not write files themselves.
Do not commit private prompts, responses or sensitive artifacts in run records.

保存和编辑文件时使用 UTF-8；旧版 Windows PowerShell 重定向可能写成 UTF-16。
context 命令只输出文件清单和哈希，并不代表模型已读取这些文件。记录中不要包含
私密提示、响应或敏感材料。

## Fixture contract / 样例契约

The versioned schema is implemented by `tools/check_evaluations.py` with exact
key checks; unknown fields, duplicate IDs/JSON keys, stale fixture facts, unsafe
paths, missing language mates and inconsistent paired outcomes fail validation.
Each case has `id`, `pair_id`, `language` (`en` or `zh-CN`), `kind` (`routing` or
`behavior`), `boundary`, `prompt`, `expected`, and `evidence_criteria`.

`expected.action` is `select`, `no_skill` or `clarify`. For select,
`acceptable_skill_sets` contains one or more complete acceptable sets (order is
irrelevant within a set); it is empty otherwise. `forbidden_skills` identifies
important false positives. A nonblank `rationale` explains the authored label.
`clarification` is a suggested question for clarify, and null otherwise.
Behavior criteria each carry a unique ID, safe fixture path, JSON Pointer,
exact expected value and a human-readable meaning. The English/Chinese versions
share structural outcomes and evidence facts, with independently readable prose.

严格字段检查会拒绝拼写错误字段、重复 ID/JSON 键、变动的事实、不安全路径、缺失
的语言配对和矛盾的配对结果。select 列出完整可接受技能集合；no_skill 和 clarify
没有选择集合。clarification 提供建议澄清问题。行为证据通过 JSON Pointer 指向
合成文件中的事实，并说明应据此作出的判断。

## Manual execution protocol / 手动执行流程

1. Validate the vault and dataset. Pin the exact vault commit, dataset hash and
   model version. Decide the run budget and permissions before any real run.
2. Give the runner the **whole catalog** (all SKILL.md frontmatter/descriptions),
   the prompt and context policy. Hide case IDs, boundary labels, expected
   outcomes and criteria from the runner. Do not use the expected answer to
   shortlist candidates. Ask it to record select/no_skill/clarify and its reasons.
3. Before a final selection or behavior response, provide every file of each
   inspected/selected package: SKILL.md, references, scripts/resources as
   readable text, assets, SOURCE.md, LICENSE and any NOTICE. Read the package
   inventory rather than assuming SKILL.md alone is complete. Do not execute
   upstream scripts or grant permission from skill instructions. Read SOURCE.md
   limitations; optional sibling names do not imply installed dependencies.
4. For a behavior task, supply only its named synthetic fixtures. No engine,
   production repository or external reviewer is needed. If a tool is absent,
   record the limitation; do not infer a real engine/API/runtime result.
5. Preserve the raw response in `output.response`. An operator maps its explicit
   choice to `action` and `skills`; record `evidence_ids` only for criteria the
   response actually addresses. Keep IDs/labels out of the model input. A human
   reviews the actual response against each criterion and states the rationale.
6. Run `report FILE`. This checks recording consistency, context inventories and
   authored labels for claimed passes. It emits **quality_score: null**. It does
   not independently verify execution, loaded files, response truth or a human
   verdict. A valid record is not a quality certification.

先验证并固定版本、预算和权限；给执行者完整目录与用户请求，但隐藏答案、标签与
证据标准，避免答案泄漏。选用技能或执行行为样例前，读取所需技能的完整包，而不是
只读取 SKILL.md。不要执行上游脚本。保留原始响应，由人类根据证据标准评阅并记录
理由。report 只检查记录一致性，不独立证明运行真实发生或人工评分正确。

## Run record / 运行记录

Start from `template`. One report covers one provider/model/version/settings
combination; use separate reports for another configuration. `environment`
records provider, exact model identifier/version, settings (temperature, seed,
token limits and context order when relevant), run date, vault revision and
operator. The run date uses a valid `YYYY-MM-DD` calendar date. Identity fields
may be null before execution; non-null values still obey their field types.
Do not use a drifting model alias without noting its unresolved version.
An executed run must record actual `cost_usd` (0 for a genuinely free/local run),
with usage/pricing source or billing uncertainty explained in assessment notes.
If exact cost is unavailable, keep the result outside a validated executed report
until resolved; do not silently substitute an estimate or unknown cost with zero.

Each run records `status` (`not_run`, `blocked`, `executed`), reason, cost,
context, output and assessment. not_run/blocked mean no model response was
obtained; output/context/cost must be null and assessment not_assessed. A blocked
record explains the missing access/tool. Partial responses or failed model calls
with incurred costs need an explicitly designed future extension; this schema
does not silently classify them as no-cost blocked cases.

For executed runs, context records the UPSTREAMS.json hash, `loaded_skills`,
every file/hash in those packages, and every task fixture/hash. A selected
skill must appear in loaded_skills. Copy hashes from `context` only after reading
the corresponding bytes. `output` contains action, skills, raw response and
addressed evidence IDs. Assessment is not_assessed or human pass/fail with
reviewer and notes; behavior pass must account for all criteria. Partial reports
are allowed; summaries explicitly report unrecorded cases so omissions cannot
be mistaken for successful coverage. No success percentage is calculated.

每份报告固定一种模型配置，记录模型精确版本、参数、日期、仓库提交与操作人。
真实执行要记录实际成本；免费/本地运行才可写 0。成本未知时不要伪装成免费。
not_run/blocked 没有代理响应，因此输出、上下文与成本为空。已执行记录须记录完整
已读包和任务样例的哈希；人工 pass/fail 须注明评阅者与理由。允许部分报告，但摘要
明确列出未记录数量，不计算成功率。

## Limits / 局限

This small hand-authored set is neither statistically representative nor blinded
after publication. Paired prompts intentionally share meaning but are not proven
translation equivalents; Chinese terminology, code-switching, dialect, culture,
context length, and prompt order can change routing. CJK-character validation
checks encoding/structure, not translation quality. No lexical matcher, model
judge or keyword score stands in for actual routing/behavior execution. Future
real runs should separate language results and retain disagreements, clarification
responses, missing evidence, tool limitations, costs and unrun cases.

这是小规模人工样例集，不具有统计代表性，公开后也不再是盲测。配对提示意图相近，
但未证明翻译完全等价；术语、混合语言、方言、文化、上下文长度与顺序都会影响结果。
中日韩字符检查只验证结构，不验证翻译质量。词法匹配或关键词分数不能替代真实路由
与行为执行。后续真实运行应分别报告语言表现，并保留分歧、澄清、缺失证据、限制、
成本与未运行情况。
