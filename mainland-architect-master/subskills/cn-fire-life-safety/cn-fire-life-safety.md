---
name: cn-fire-life-safety
description: Mainland China fire and life safety skill using GB 50016 baseline with local fire-review supplements, including egress strategy, fire compartmentation, smoke control, and acceptance workflow.
user-invocable: true
disable-model-invocation: true
---

# Mainland Fire Life Safety

Primary baseline: `GB 50016` plus municipal supplements and local fire review practice.

Regulatory hierarchy:
- National baseline first: `GB / GB-T / JGJ`
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Mandatory Compliance Workflow

1. Determine city context and local fire supplemental standards.
2. Establish occupancy classification and fire hazard category.
3. Validate egress strategy using occupancy load density assumptions.
4. Complete construction drawing fire review package.
5. Align design with `消防救援局` acceptance expectations.

---

## 2. Egress Strategy Rules

- Do not hardcode fixed travel distances without project occupancy and sprinkler assumptions.
- Stair count and width must be derived from occupant load and functional type (office/commercial/assembly/residential).
- Treat `袋形走道`, refuge strategy, and smoke control as linked checks.
- For atypical typologies (large atria, transport hubs, super-tall), assess need for performance-based fire design (`性能化防火设计`).

---

## 3. Fire Design Scope Checklist

| Topic | Deliverable |
|---|---|
| Occupancy and fire category | Basis of design statement |
| Egress layout | Route, distance, and stair capacity table |
| Fire compartmentation | Fire zone partition schedule |
| Fire resistance | Structural/fireproofing strategy |
| Smoke management | Mechanical and natural smoke control basis |
| Firefighting access | Fire engine and rescue operations interface |
| System integration | Alarm, hydrant, sprinkler, smoke control consistency |

---

## 4. Authorities and Stage Gates

| Stage | Main Focus |
|---|---|
| 方案设计 | High-level fire strategy feasibility and planning fit |
| 初步设计 | System selection and coordination with structural/MEP |
| 施工图设计 | Third-party审图 fire compliance closure |
| 施工阶段 | Design changes and variation fire impact checks |
| 竣工验收 | Fire acceptance documentation and test evidence |

---

## 5. High-Risk Failure Patterns

| Risk Pattern | Typical Consequence | Mitigation |
|---|---|
| Egress assumptions copied from another city | 审图退件 or authority challenge | Confirm local supplements before final fire narrative |
| Occupant load not tied to function | Under-sized stairs/exits | Use function-specific load-density basis and record assumptions |
| Incomplete smoke-control coordination | Major rework in审图 | Freeze smoke-control strategy before IFC-level drawings |
| Fire and MEP inconsistency | Acceptance failure | Cross-discipline fire matrix and pre-submission check |

---

## 6. Mandatory Inputs (ask if missing)

- City and district
- Building type(s) and occupancy assumptions
- Current stage (`方案` / `初设` / `施工图` / site)
- Sprinkler and smoke-control strategy status
- Any existing审图/消防意见
- Whether performance-based approach is being considered

---

*Baseline reference: GB 50016 and applicable local fire supplements; performance-based design to follow current MOHURD and emergency-management technical requirements where adopted.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Fire strategy and GB 50016 | `cn-fire-life-safety` | `cn-building-codes` |
| Egress numeric pre-check | `cn-fire-life-safety` | `cn-architect-calculator` |
| Acceptance commissioning | `cn-fire-life-safety` | `cn-fire-acceptance-closeout` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
