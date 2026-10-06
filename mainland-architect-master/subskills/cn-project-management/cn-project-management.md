---
name: cn-project-management
description: Mainland architectural project-management guidance for delivery plans, consultant appointments, risk, reporting, and the boundary between contract administration and statutory acceptance.
user-invocable: true
disable-model-invocation: true
---

# Mainland Project Management

Client-side delivery management for design and construction. It does not replace 监理, the contract administrator, or the statutory 项目负责人.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Delivery plan, risk, client reports, dispute path | `cn-project-management` | `cn-tender-contract-administration` |
| Stage-gate task list | `cn-project-management` | `cn-plan-of-work` |
| Issue-pack contents | `cn-project-management` | `cn-deliverables-workstages` |

## 1. Scope and Core Position

The project manager integrates time, cost, risk, and decisions. Design responsibility stays with the licensed design institute. Site safety responsibility stays with the contractor. This suite gives advisory plans only.

## 2. Business Case and Strategic Brief

### 2.1 Business case

Site, use, area target, budget, opening date, funding source, and success criteria. Mark land status and 控规 as confirmed or unknown.

### 2.2 Strategic brief

- Objectives and non-negotiables (star rating, prefabrication ratio, public realm).
- Area brief (`cn-building-programming`).
- Approval route (`cn-consent-scheduling`).
- Procurement preference (`cn-procurement-strategy`).
- Risks that can stop the project: heritage, airport, flood, metro protection, unresolved land.

## 3. Consultant Selection and Appointments

### 3.1 Selection

Scope, fee basis, professional liability insurance, and local qualification (设计资质, 注册建筑师 for the seal). Fee tactics: `cn-fee-proposal-strategy`.

### 3.2 Roles

Write a RACI before 方案 freeze. At minimum: client decision maker, design 项目负责人, cost lead, 监理, contract administrator, and this project manager. One person may hold two roles only if the appointments allow it and the conflict is stated.

## 4. Project Delivery Plan

### 4.1 Contents

- Stage plan aligned to 方案 / 初设 / 施工图 / 施工 / 验收.
- Permit predecessors.
- Design-information schedule.
- Procurement and tender windows.
- Risk register.
- Meeting and report calendar.
- Change-control rule.
- Handover and acceptance definition (contract versus statutory).

### 4.2 Issue

The delivery plan is a client document. Consultants comment. The client approves. Update it when a permit or a budget assumption fails.

## 5. Risk, Value, and Design Review

### 5.1 Risk

Score probability and impact. Escalate red risks that affect permit, safety, or opening date. Do not hide a 审图 rejection inside a technical risk with a green score.

### 5.2 Value management

Sponsor workshops at 方案 and 初设. Reject options that break mandatory codes or planning conditions.

### 5.3 Design reviews

Gate reviews check completeness against `cn-plan-of-work`, coordination, and cost-plan alignment. They are not a substitute for 审图.

## 6. Contractor Selection and Commercial Control

### 6.1 Selection

Follow `cn-procurement-strategy` and the tendering law when it applies. The project manager coordinates the process. The cost consultant evaluates price.

### 6.2 Payment validation

The project manager checks that a payment recommendation matches the contract process. The valuer recommends the amount. Do not create a second certificate.

### 6.3 Change control

No change without a number, a drawing, a cost/time flag, and the authorised instruction. Track pending changes that are being built without an instruction as a commercial risk.

## 7. Disputes and Escalation

### 7.1 Early resolution

Facts, contract clause, and a without-prejudice meeting. Keep the site safe while the commercial dispute continues.

### 7.2 Pathways

Negotiation, mediation or dispute board if the contract provides it, then arbitration or court as the contract states. Do not promise an outcome.

### 7.3 Project-manager role

Keep the decision log, instruct consultants to prepare facts, and send legal questions to counsel. Halt on a legal opinion.

## 8. Programme and Budget Monitoring

### 8.1 Programme

Monthly: critical path, permit float, design-information delays, and construction look-ahead (`cn-construction-programme`). A percent-complete figure needs a basis.

### 8.2 Budget

Monthly: approved budget, contract sum, instructed changes, pending changes, and forecast. The cost consultant owns the numbers. The project manager owns the narrative and the decisions requested.

## 9. Transition from Construction to Occupation

### 9.1 Handover planning

Start at least one stage before completion: training, O&M, spare parts, 物业, and partial possession rules.

### 9.2 Occupation readiness

Statutory path: fire acceptance or filing, 规划核实, special-equipment certificates, and joint acceptance / 备案 (`cn-op-submission-strategy`). Contract completion may be earlier or later. State both dates.

## 10. Client Reporting

### 10.1 Cadence

Monthly report, plus an exception note within one working day for permit refusal, safety incident, or a forecast overrun beyond the contingency rule.

### 10.2 Report structure

1. Decisions required.
2. Stage and permit status.
3. Programme (baseline versus forecast).
4. Cost (baseline versus forecast).
5. Risks and changes.
6. Safety and quality exceptions.
7. Next month.

## 11. Interfaces

| Duty | Skill |
|------|-------|
| Stage checklists | `cn-plan-of-work` |
| Issue packs and RACI detail | `cn-deliverables-workstages` |
| Instructions and claims | `cn-tender-contract-administration` |
| Cost numbers | `cn-cost-consultancy` |
| Site start | `cn-site-establishment` |
| Acceptance pathway | `cn-op-submission-strategy` |

## 12. Output Checklist

- Client decision maker named.
- Contract completion and statutory acceptance separated.
- Risk register includes permit and safety items.
- Report requests a decision, not only a status.
- Legal and safety-sign-off questions halted.
- 监理 scope not absorbed into the project manager's role.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-pow-stages.md](../../references/cn-pow-stages.md) — stage outline
* [GB_T_50326_Project_Management_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_T_50326_Project_Management_CS.md) — project-management standard digest
