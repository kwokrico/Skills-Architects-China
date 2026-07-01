---
name: cn-construction-documentation
description: Mainland construction documentation skill covering stage deliverables, drawing review packages, authority submission sequencing, and acceptance documentation closure.
user-invocable: true
disable-model-invocation: true
---

# Mainland Construction Documentation

This skill manages documentation strategy from concept through construction drawing review and completion filing.

---

## 1. Stage Deliverables Framework

| Stage | Core Documentation Package |
|---|---|---|
| 方案设计 | Concept report, key planning metrics, preliminary system narrative |
| 初步设计 | Discipline basis reports, investment alignment, technical route lock |
| 施工图设计 | Coordinated IFC-level drawing set +审图 calculation package |
| 施工配合 | Variation records, RFI responses, site coordination documents |
| 竣工阶段 | As-built package, test/commissioning records, acceptance filing set |

---

## 2. Mandatory Submission and Review Logic

| Milestone | Main Interface |
|---|---|---|
| Planning permit support | 规自局 planning compliance material |
| Preliminary design review | Local authority or delegated review route |
| Construction drawing review | Mandatory third-party `施工图审查` package |
| Construction permit | 住建相关 permit submission package |
| Completion filing | Joint acceptance and备案 documentation set |

---

## 3. Typical Drawing/Document Matrix

| Discipline | Typical Deliverables |
|---|---|---|
| Architecture | Plans/sections/elevations/details/room data sheets |
| Structure | Structural plans, key calculations, design assumptions |
| MEP | System schematics, coordinated layouts, equipment schedules |
| Fire | Fire strategy and code-compliance schedules |
| Sustainability | Green target matrix and compliance evidence |
| Completion | As-built drawing set + test and acceptance records |

---

## 4. Quality-Control Rules for Documentation

- Keep one source of truth for indicators (`容积率`, `建筑密度`, `绿地率`, `限高`).
- Freeze naming and drawing numbering rules before multi-discipline issue.
- Track审图 comments with responsible discipline and closure evidence.
- Maintain issue history (IFC/for-review/for-construction/as-built) with version governance.

---

## 5. Common Failure Modes

| Failure | Consequence | Mitigation |
|---|---|---|
| Discipline assumptions inconsistent | Review rejection and reissue cycle | Run cross-discipline consistency gate before submission |
| City supplement standards not reflected |审图退件 | Add city-specific checklist on first page of submission set |
| Change control unmanaged | Site disputes and as-built divergence | Formal revision log with approval signatures |
| Completion docs prepared too late | Delay in acceptance and handover | Start completion dossier structure during construction phase |

---

## 6. Required Inputs (ask if missing)

- City and district
- Current design stage
- Intended submission milestone
- Existing审图 comments and closure status
- Delivery mode (`传统施工`, `EPC`, `设计施工总承包`)

---

*Baseline references: national documentation requirements under current PRC regulatory framework and applicable local authority submission templates.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 审图 package and comment closure | `cn-construction-documentation` | `cn-building-codes` |
| Approval programme | `cn-construction-documentation` | `cn-consent-scheduling` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
