---
name: cn-deliverables-workstages
description: Activate for Mainland deliverables registers, issue-pack discipline, transmittals, drawing scales, consultant RACI, stage-freeze change control, and lead-consultant coordination by workstage.
user-invocable: true
disable-model-invocation: true
---

# Mainland Deliverables & Workstages
Defines who receives what by workstage, issue-pack structure, presentation rules, and lead-consultant coordination. Extends the master deliverables template with operational discipline.

---

## 1. Issue-Pack Ready Rule

An issue pack is **ready** only when:

1. Revision code and date are consistent across all sheets and transmittal.
2. Recipient list and purpose (报审 / 招标 / 施工 / 信息) are stated.
3. Assumptions and exclusions block is attached.
4. Status is defined: `PRELIMINARY` / `FOR REVIEW` / `FOR APPROVAL` / `FOR CONSTRUCTION` / `AS-BUILT`.
5. Registered professional sign-off requirements are identified (do not imply statutory certification).

Master index: [deliverables.md](../../references/templates/deliverables.md).

---

## 2. Stakeholder Groups

| Group | Typical recipients | Pack focus |
|-------|-------------------|------------|
| 业主 / 建设单位 | 方案至竣工各阶段 | 决策版、指标、投资 |
| 规自局 / 审批部门 | 方案、报建、核实 | 报建图、指标表 |
| 审图机构 | 施工图 | 全套图纸 + 计算书 + 专篇 |
| 施工单位 / EPC | 招标、施工 | FOR CONSTRUCTION 版 |
| 监理 | 施工 | 变更、RFI 回复 |
| 专项咨询 | 全程 | 接口图、负荷、模型 |

---

## 3. Workstage Deliverable Definitions

| Stage | Minimum architect-led pack |
|-------|---------------------------|
| 方案 | 说明、总图、指标、体量、消防策略说明 |
| 初设 | 各专业技术说明、系统路线、主要图纸 |
| 施工图 | 协调目录、建筑全套、专篇索引、版本说明 |
| 招标 | 招标图深度清单、规格边界、接口表 |
| 施工配合 | 变更单、联系单、现场指令回复 |
| 竣工 | 竣工图目录、As-built 差异说明 |

Full tables: [deliverables.md](../../references/templates/deliverables.md) §§2–7.

---

## 4. Presentation Rules

- **Drawing scales:** 总图 1:500/1:1000; 平面图 1:100/1:200; 详图 1:5–1:20 (project convention in BIM/CAD standard).
- **Numbering:** Discipline prefix (A/S/P/M/E) + sequential; no duplicate sheet numbers across revisions.
- **Language:** 中文为主; bilingual sheet titles where owner or JV requires.
- **Electronic issue:** PDF for approval; native CAD/BIM per contract; transmittal records mandatory.

---

## 5. Lead Consultant Coordination

### 5.1 RACI (simplified)

| Activity | 项目负责人 | 专业负责人 | 业主 | 造价 |
|----------|-----------|-----------|------|------|
| 成果目录 | A | R | C | I |
| 报审版本冻结 | A | R | C | I |
| 审图意见分发 | A | R | I | I |
| 招标图一致性 | A | R | C | C |
| 变更影响评估 | A | R | C | C |

A = Accountable, R = Responsible, C = Consulted, I = Informed.

### 5.2 Meetings and stage freeze

- Weekly design coordination during 施工图 peak.
- Stage-freeze memo before 审图报审 and before FOR CONSTRUCTION issue.
- VM sessions logged with cost impact flag to `cn-cost-consultancy` when applicable.

### 5.3 Change control after freeze

1. Log change request with trigger (client / site / authority).
2. Classify: cosmetic / coordination / approval-impacting.
3. Update deliverables register before re-issue.
4. Route approval-impacting changes to `cn-consent-scheduling` and `cn-construction-documentation`.

---

## 6. Output Checklist

- Deliverables register with status codes.
- Issue pack cover and transmittal.
- RACI or meeting action log for open items.
- Freeze log reference.
- Recipient acknowledgment trail (email / 签收).

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Deliverables register / issue pack | `cn-deliverables-workstages` | `cn-plan-of-work` |
| Stage gate only | `cn-deliverables-workstages` | `cn-plan-of-work` |
| 审图 package | `cn-deliverables-workstages` | `cn-construction-documentation` |
| PM delivery plan | `cn-deliverables-workstages` | `cn-project-management` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [deliverables.md](../../references/templates/deliverables.md) — full deliverables index
