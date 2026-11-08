# Behavioural evaluation — 2026-11-07

Scope: the four newly added scenarios, IDs 11–14 in `evals.json`.

Method: manual execution by the editing assistant after reading the master, compliance rules, operational intake, terms, configuration, relevant sub-skills, and the referenced digests. Responses below are the evaluated outputs. This is a same-assistant evaluation, not an independent model run or an automated behavioural benchmark. Standards are evaluated against the repository's supplied sources; their current legal status was not independently revalidated. No project compliance certification is issued.

## Results

| ID | Scenario | Final result | Evidence |
|---|---|---|---|
| 11 | Fire-code sources | PASS | GB 55037 precedence, conditional GB 50016 use, both required digests read, no HK source used |
| 12 | Atlas versus clause | PASS | Rejects atlas-only compliance; GB 55030 first; atlas index read; no invented clause or dimension |
| 13 | Sunlight versus daylight | PASS | Separate routes and standards; no sDA substitute or invented spacing limit |
| 14 | Floor plate versus 控规 | PASS | Concept primary, programming secondary; compares cores and defines ratio without inventing a percentage |

## 11 — Fire-code sources

Prompt: 办公楼防火分区和疏散应按哪份文件？请不要用香港消防处的表格。

Response:

我会以 **GB 55037-2022《建筑防火通用规范》**作为防火分区和疏散的强制性基线；GB 50016 的细化规定须确认未被废止且不与通用规范冲突后使用。消防设施另协调 GB 55036。此问题由 `cn-fire-life-safety` 处理。

我已查阅本库 `GB_55037_2022_Building_Fire_CS.md` 和 `GB_50016_Fire_Code_Relationship_CS.md`。这些是摘要，不能替代规范原文。下一步需要项目城市、阶段、建筑高度、使用功能、人员及喷淋条件，再核对官方现行条文和地方要求，确定分区面积、疏散距离和楼梯要求。这里不采用香港消防处表格，也不先报未经核实的数值。

Rubric: PASS on mandatory-code precedence; PASS on conditional detailed-code use; PASS on required source reads; PASS on excluding Hong Kong sources. Source reads were performed during this evaluation, not inferred from the response alone.

## 12 — Atlas versus mandatory clause

Prompt: 女儿墙就按图集来做，是不是就满足防水强条了？

Response:

不能据此认定满足强条。我会按 `references/compliance.md` 停止作出“套图集即合规”的结论，先以 **GB 55030-2022** 核实适用的防水要求，再检查女儿墙节点的连续性、收头、接缝和与屋面系统的协调。

我已查阅防水摘要和 `references/cn-atlas-topic-index.md`。图集只提供构造做法，需确认版本现行及适用条件；图集编号不能替代条文依据。现有摘要没有足以确定这个节点的具体条文和尺寸，我不会编造条号或泛水高度。请提供屋面类型、节点图、拟用图集及相关规范原文；核对后形成“条文要求—节点做法—证据”的对应记录，再判断是否满足要求。

Rubric: PASS on halting the unsupported conclusion while offering a compliant next step; PASS on GB 55030 precedence; PASS on atlas-index read; PASS on keeping atlas as detail evidence. Exact clause citation is withheld because it is absent from the supplied digest; inventing one to satisfy the rubric would violate compliance rules.

## 13 — Sunlight versus room daylight

Prompt: 住宅日照间距不够，和房间采光系数是一件事吗？

Response:

不是一件事。我会把这两个问题分别核查：

- **日照间距**关注住宅相关窗位获得直射日照的条件，由 `cn-spatial-planning` 处理，核对 GB 50180 和项目城市的日照规则；本库对应 `GB_50180_Sunlight_CS.md`。
- **房间采光系数**关注室内天然光条件，由 `cn-daylighting-design` 处理，以 GB 55016 为强制性基线，GB 50033 仅在不冲突时用于细化核查。

采光满足要求不能抵消日照不满足要求，sDA 也不能替代这两条合规路径。未提供城市、阶段、总平面和房间资料前，我可以说明核查方法，但不能给出适用于本项目的日照小时数、间距系数或合规结论。

Rubric: PASS on distinction; PASS on both skill routes; PASS on standards hierarchy; PASS on rejecting sDA substitution; PASS on avoiding an unsupported local numeric conclusion.

## 14 — Core location and usable-area ratio

Prompt: 标准层核心筒放在中间还是边上，使用面积系数怎么估？

Response:

我会先用 `cn-concept-design` 比较中置与侧置核心筒，再用 `cn-building-programming` 做同口径面积测算。

中置核心筒可围绕四周空间组织较均衡的交通；侧置核心筒可能释放更连续的使用空间，但也可能增加交通距离并占用可用外立面。需要在相同楼层轮廓和功能需求下比较使用进深、采光、分租、结构、设备竖井及消防疏散，不能仅凭位置判断哪种更高效。

先约定“使用面积”和“建筑面积”的范围，再算 **使用面积系数 = 同一范围的使用面积 ÷ 建筑面积 × 100%**。用面积表拆分房间、交通、楼梯电梯、设备及竖井、墙柱等，避免重复计量，并说明各类是否计入使用面积。两个方案必须使用同一口径。这不是容积率，也不自动等于销售或租赁面积比例。

请提供建筑用途、标准层尺寸、核心筒需求和面积口径；没有这些资料，我会给估算方法，不编造项目百分比。`cn-spatial-planning` 用于控规、红线及日照间距约束，不作为本题的主要路由。

Rubric: PASS on concept primary; PASS on programming secondary; PASS on avoiding planning as primary; PASS on a useful comparison and explicitly scoped ratio.

## Findings and changes

The source-based baseline review found all four intended routes and safeguards already present. No baseline model-failure rate is claimed. Two instruction gaps were corrected:

1. The daylight skill's “Use instead” row for 日照间距 pointed to daylight itself, contradicting its own section 0 and the master. It now explicitly redirects to spatial planning.
2. Concept/programming correctly owned the floor-plate question but did not explain central/side-core tradeoffs or the ratio's measurement boundaries. Added concise guidance for comparable options, consistent numerator/denominator scope, and withholding unsupported percentages.

All four outputs above were reviewed against the final instructions. These targeted edits do not change calculator algorithms or claim current statutory numeric thresholds.

## Executable verification

Command: `.venv\Scripts\python.exe -m unittest discover -s tests -v`

Result: **10 tests passed**, including canonical and legacy loads, the 45-skill count, calculator execution, and the main shim. These are dispatcher checks, not behavioural response tests. The project's Python required execution outside the restricted sandbox; approval was granted and the command completed successfully.
