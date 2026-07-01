---
name: cn-tender-contract-administration
description: Activate for Mainland tender and contract administration strategy, EPC/traditional procurement alignment, variation control, progress payment governance, and dispute-risk reduction.
user-invocable: true
disable-model-invocation: true
---

# Mainland Tender and Contract Administration
Covers pre-tender preparation, contract strategy, and post-award administration in Mainland delivery contexts.

---

## 1. Scope and Role
- Treat tender and contract administration as a commercial-risk control system.
- Coordinate owner, design team, cost team, legal advisors, and contractor interfaces.
- **Procurement route selection** (传统 vs EPC/总承包, risk allocation, weather EOT by route) → load `cn-procurement-strategy` first; this skill covers tender execution and post-award CA duties.
- Align procurement path with delivery mode (`传统施工招标`, `EPC`, `设计施工总承包`).
- **BoQ measurement and cost plans** → `cn-cost-consultancy` for QS scope; this skill covers architect interface at tender and variation stages.

---

## 2. Pre-Tender Documentation
Typical tender set should include:
1. Architect's drawings and specifications at suitable tender detail.
2. Bills of Quantities (BoQ) prepared by QS, with architect-led design coordination inputs.
3. Employer requirements, preliminaries, and particular conditions.
4. Form of tender, return schedules, and tender instructions.
5. Proposed form of contract and appendices.

Quality checks before issue:
- Scope completeness and consistency between drawings, specs, and BoQ.
- Clear assumptions and exclusions to reduce post-award dispute risk.
- Practical tender period and bidder query protocol.

---

## 3. BoQ Coordination (Architect Interface)
- Design team defines technical scope and quality baselines.
- Cost team leads measurement and pricing structure; design team validates technical consistency.
- Resolve inconsistencies early (dimensions, material descriptions, interface items).

BoQ coordination principles:
- One design intent, one description language across all documents.
- Avoid "double counting" or scope gaps across trades.
- Record all clarifications with auditable issue history.

---

## 4. Contract Form Strategy
Common approach:
- Use project-approved PRC contract form strategy (including MOHURD/SAMR model forms where applicable) with project-specific amendments.
- Ensure contract particulars reflect programme, LD/EOT rules, insurance, defect liability, and sectional handover conditions.

Design-team review focus:
- Variation procedure clarity and evidence standards.
- Payment milestones aligned with real deliverables.
- Notice periods and entitlement rules are operable in practice.

---

## 5. Tender Queries, Addenda, and Assessment
During tender period:
1. Receive and log tender queries.
2. Coordinate technical responses with consultants/QS.
3. Issue addenda in controlled revisions to all tenderers.

Assessment support:
- Check compliance against mandatory technical requirements.
- Flag exclusions, qualifications, and departures.
- Support tender report drafting with clear recommendation rationale.

---

## 6. Post-Contract Administration Duties
Core duties after award:
- Administer contract procedures in accordance with the agreed form.
- Issue design/change instructions with clear scope, basis, and revision control.
- Monitor progress and quality through regular meetings and records.
- Coordinate with cost team for interim payment and adjustment inputs.

Deliverables baseline:
- Site instruction logs.
- Drawing and document revision tracker.
- Progress and issue registers tied to contractual milestones.

---

## 7. Variations and Change Control
Variation workflow:
1. Identify and define change scope.
2. Confirm reason (client change, statutory requirement, coordination issue, unforeseen condition).
3. Issue formal instruction/change record.
4. Obtain valuation input and track time/cost effect.
5. Update contract sum/time records and maintain audit trail.

Risk controls:
- No verbal-only scope changes.
- Keep causation and chronology evidence.
- Distinguish provisional design development from instructed change.

---

## 8. Certification and Payment Interfaces
- Design team and cost team must keep payment basis auditable.
- Keep interim payment records consistent with measured/proven progress.
- Track retention, defect deductions, and adjustment events transparently.

Good practice:
- Maintain a single source register for certificates, dates, and associated backups.
- Confirm contractual notice periods are met for entitlement-related events.

---

## 9. Practical Compliance Checklist
- Tender package internally coordinated and issue-controlled.
- BoQ and design information technically aligned.
- Contract particulars and amendments reviewed for operability.
- Tender clarifications/addenda fully logged.
- Variation and instruction records auditable from instruction to valuation.
- Payment/certification timeline maintained with supporting evidence.

---

*Reference baseline: project contract conditions, applicable PRC model contracts, owner governance requirements, and dispute-resolution framework (including arbitration pathways where agreed).*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Procurement route / EPC vs traditional | `cn-tender-contract-administration` | `cn-procurement-strategy` |
| Cost plan / BoQ measurement | `cn-tender-contract-administration` | `cn-cost-consultancy` |
| Contract / variations | `cn-tender-contract-administration` | `cn-fee-proposal-strategy` |
| Site supervision | `cn-tender-contract-administration` | `cn-site-supervision` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
