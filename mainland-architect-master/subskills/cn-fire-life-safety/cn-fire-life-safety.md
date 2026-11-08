---
name: cn-fire-life-safety
description: Mainland China fire and life safety skill. GB 55037-2022 is the mandatory floor; GB 50016 applies only where it does not conflict. Covers egress, compartmentation, smoke control, refuge, fire lift, and acceptance workflow.
user-invocable: true
disable-model-invocation: true
---

# Mainland Fire Life Safety

Primary baseline: `GB 55037-2022`. Use `GB 50016` only where it does not conflict. Fire-facility systems sit under `GB 55036-2022`. Municipal supplements may be stricter. They cannot weaken the general code.

Regulatory hierarchy:
- Mandatory general code first: `GB 55037`, then `GB 55036` for facilities
- Detailed standards next, only where they do not conflict
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Mandatory Compliance Workflow

1. Determine city context and local fire supplemental standards.
2. Establish occupancy classification and fire hazard category.
3. Validate egress strategy using occupancy load density assumptions.
4. Complete construction drawing fire review package.
5. Confirm the applicable construction fire-review/acceptance authority and acceptance or filing pathway with `cn-fire-acceptance-closeout`; do not substitute a fire-rescue opening check for construction acceptance.

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
| Smoke management | Mechanical and natural smoke control basis. Detailed standard is GB 51251 where GB 55037 does not conflict. Open [GB_51251_Smoke_CS.md](../../../cn_s_reference/Fire%20and%20Rescue/summaries/GB_51251_Smoke_CS.md) |
| Sprinklers | Where a sprinkler system is required, and that the design standard is GB 50084 under GB 55036. Do not quote a threshold from memory |
| Refuge floor | Whether a refuge floor is in the strategy, and which general-code clause is being used |
| Fire lift | Whether a fire lift is in the strategy, kept separate from a passenger lift |
| Exterior insulation combustibility | Facade and insulation reaction-to-fire class for the height and use. A 图集 detail does not set the class |
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

*Baseline reference: GB 55037-2022 first, GB 55036-2022 for facilities, GB 50016 only where it does not conflict. Smoke detail: GB 51251. Sprinkler detail: GB 50084. Performance-based design follows current MOHURD and emergency-management technical requirements where adopted.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Fire strategy, GB 55037, GB 50016 where it does not conflict | `cn-fire-life-safety` | `cn-building-codes` |
| Egress numeric pre-check | `cn-fire-life-safety` | `cn-architect-calculator` |
| Acceptance commissioning | `cn-fire-life-safety` | `cn-fire-acceptance-closeout` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [GB_55037_2022_Building_Fire_CS.md](../../../cn_s_reference/Fire%20and%20Rescue/summaries/GB_55037_2022_Building_Fire_CS.md) — mandatory fire floor
* [GB_50016_Fire_Code_Relationship_CS.md](../../../cn_s_reference/Fire%20and%20Rescue/summaries/GB_50016_Fire_Code_Relationship_CS.md) — what remains of GB 50016
* [GB_51251_Smoke_CS.md](../../../cn_s_reference/Fire%20and%20Rescue/summaries/GB_51251_Smoke_CS.md) — smoke-control routing
* [cn-code-catalog.md](../../references/cn-code-catalog.md) — standards that still need a digest
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
