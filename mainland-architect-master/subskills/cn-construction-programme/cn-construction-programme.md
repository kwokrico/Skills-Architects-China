---
name: cn-construction-programme
description: Activate for Mainland construction sequencing—高层标准层循环, 工序穿插, fast-tracking, hold points, follow-the-structure façade, and 4-week look-ahead programme templates.
user-invocable: true
disable-model-invocation: true
---

# Mainland Construction Programme
Construction sequencing narratives and programme artefacts for architect/PM interface. Durations are illustrative—project-specific programme required.

Swimlanes: [cn-construction-sequence-swimlanes.md](../../references/cn-construction-sequence-swimlanes.md). Look-ahead template: [construction-look-ahead.md](../../references/templates/construction-look-ahead.md).

---

## 1. Archetype Defaults

| Typology | Dominant sequence |
|----------|-------------------|
| 高层混凝土塔楼 | 土方→桩基→地下室→主体标准层循环→幕墙跟随结构→装修穿插 |
| 装配式塔楼 | 标准层拆分吊装节点; 现浇节点与模块吊装交替 |
| 低层公建 | 框架→屋面→幕墙→内装顺序更线性 |

---

## 2. Swimlane Index

Typical lanes: 土方基坑 | 结构 | 幕墙 | 机电 | 精装 | 验收.

Cross-trade rules:

- Concealed MEP before slab close.
- Fire compartment boundaries before ceiling close.
- Façade pressure test before interior wet trades (project-specific).

---

## 3. Mainland Substitution Notes

| HK / generic term | Mainland practice |
|-------------------|-------------------|
| Follow-the-structure curtain wall | 幕墙随结构进度、样板层验收后展开 |
| Standard floor cycle | 标准层5–8天/层 (illustrative; verify locally) |
| Fast-track | 工序穿插、平行作业、提前招采 |

---

## 4. Architect / PM Early Freezes

Freeze before bulk production:

- Standard floor layout and core.
- Façade module and opening schedule.
- MEP shaft and riser routes.
- Lobby and typical floor finish level.

Link freezes to `cn-deliverables-workstages`.

---

## 5. Hold-Point Register

| Hold point | Witness | Typical trigger |
|------------|---------|-----------------|
| 桩基验收 | 监理、检测 | 承载力报告 |
| 隐蔽工程 | 监理、设计 | 钢筋、防水、管线 |
| 消防系统试压 | 监理、消防 | 管网压力 |
| 分部分项 | 住建 | 主体结构验收等 |

---

## 6. Programme Artefacts

- Master schedule (contractor-led).
- 4-week look-ahead (rolling).
- Interface matrix with procurement (`cn-procurement-strategy`).

**Hard stop:** Illustrative durations only—not submission-ready programme certificates.

---

## 7. Output Checklist

- Sequence narrative or swimlane reference.
- Hold-point list with owners.
- Look-ahead template issued.
- Interface assumptions to site supervision.
- Fast-track risks flagged.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Sequence / 穿插 / 标准层 | `cn-construction-programme` | `cn-site-supervision` |
| Site RFI | `cn-construction-programme` | `cn-site-supervision` |
| Approval programme | `cn-construction-programme` | `cn-consent-scheduling` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-construction-sequence-swimlanes.md](../../references/cn-construction-sequence-swimlanes.md) — swimlanes
* [construction-look-ahead.md](../../references/templates/construction-look-ahead.md) — look-ahead shell
