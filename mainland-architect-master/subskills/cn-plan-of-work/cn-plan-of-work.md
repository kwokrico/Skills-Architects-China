---
name: cn-plan-of-work
description: Activate for Mainland project stage mapping (方案/初设/施工图/施工配合/验收), GB/T 50326 alignment, stage gates, role routing, and per-stage statutory reminders. Do not apply RIBA or UK Building Regs by default.
user-invocable: true
disable-model-invocation: true
---

# Mainland Plan of Work
Maps project delivery stages to Mainland statutory milestones, consultant responsibilities, and gate criteria. Use when the user asks about stage gates, workstage checklists, or GB/T 50326 alignment.

---

## 1. When to Use

- Stage 0–7 or RIBA terminology appears but project is Mainland China — **substitute Mainland stages**, do not import UK PSC or Approved Documents by default.
- User needs a stage gate checklist, freeze criteria, or "what must be done before 施工图审查".
- Consultant RACI or deliverable timing by stage.

For issue-pack structure and transmittals, route to `cn-deliverables-workstages`. For approval programme, route to `cn-consent-scheduling`.

---

## 2. Stage Mapping (Mainland ↔ neutral)

| Mainland stage | Neutral / RIBA analogue | Primary statutory / commercial outputs |
|----------------|-------------------------|--------------------------------------|
| 项目策划 / 可研 | Stage 0–1 | 立项、用地、控规核对、投资估算 |
| 方案设计 | Stage 2 | 方案审批、指标合规、消防策略初判 |
| 初步设计 | Stage 3 | 系统路线、概算、初设审查（视地方） |
| 施工图设计 | Stage 4 | 协调施工图、专篇、审图报审 |
| 施工许可 / 招标 | Stage 4–5 bridge | 审图合格书、施工许可证、招标定标 |
| 施工配合 | Stage 5 | 变更控制、现场签证、隐蔽验收 |
| 竣工验收 | Stage 6–7 | 专项验收、竣工联合验收/备案、移交 |

Deep per-stage checklists: [cn-pow-stages.md](../../references/cn-pow-stages.md).

---

## 3. Mainland Substitution Guide

| Do not default to | Use instead |
|-------------------|-------------|
| RIBA Plan of Work 2020 task lists verbatim | GB/T 50326 + local 报建阶段要求 |
| UK Building Regulations approval stages | 施工图审查 + 消防设计审查 + 施工许可证 |
| HK consent-to-commence (s.14) | 施工许可证 + 开工前条件检查 |
| Occupation Permit (OP) alone | 消防验收 → 规划核实 → 竣工联合验收/备案 chain |

---

## 4. Stage Gate Procedure

1. **Confirm inputs** — drawings, indicators, prior authority comments, contract stage definition.
2. **Run gate checklist** — use [stage-gate-checklist.md](../../references/templates/stage-gate-checklist.md).
3. **Record freeze** — scope, GFA/指标, structural system, core/MOE, major MEP plant.
4. **Sign-off roles** — 项目负责人 / 设计总工 / 专业负责人 per discipline.
5. **Issue pack** — only after gate pass; see `cn-deliverables-workstages`.

**Hard stop:** Do not declare a stage "complete" for permit purposes without the relevant authority acceptance or client contractual acceptance documented.

---

## 5. Role Routing by Stage

| Stage | Lead | Key supports |
|-------|------|--------------|
| 方案 | 建筑 专业负责人 | 规划 `cn-spatial-planning`, 消防 `cn-fire-life-safety` |
| 初设 | 项目负责人 | 结构/MEP 专业负责人, `cn-building-services` |
| 施工图 | 各专业负责人 | `cn-construction-documentation`, 审图闭环 |
| 施工 | 项目负责人 + 现场代表 | `cn-site-supervision`, `cn-construction-programme` |
| 验收 | 项目负责人 | `cn-op-submission-strategy`, `cn-fire-acceptance-closeout` |

---

## 6. Per-Stage Reminders (Mainland)

- **方案:** 红线/退界、容积率/密度/绿地率/限高、日照（如强制）、消防扑救面与车道意向。
- **初设:** 结构体系与超限判定、机房与竖井、绿建/节能路径、概算与投资偏差控制。
- **施工图:** 审图一次通过率策略、专篇与图纸版本一致、消防/人防/节能联动。
- **施工:** 变更分级、隐蔽工程见证、与审图/消防变更联动。
- **验收:** 专项验收顺序、竣工图与现场一致、备案资料索引。

---

## 7. Output Checklist

- Stage mapping table with current project position marked.
- Gate pass/fail with missing inputs listed.
- Freeze log (what is locked vs pending).
- Next-stage statutory dependencies with owners.
- Cross-reference to `cn-consent-scheduling` if programme critical.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Stage gates / GB/T 50326 | `cn-plan-of-work` | `cn-deliverables-workstages` |
| Issue pack / transmittal | `cn-plan-of-work` | `cn-deliverables-workstages` |
| Approval timeline | `cn-plan-of-work` | `cn-consent-scheduling` |
| Project delivery plan | `cn-plan-of-work` | `cn-project-management` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-pow-stages.md](../../references/cn-pow-stages.md) — per-stage deep checklists
