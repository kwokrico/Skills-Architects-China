---
name: cn-building-services
description: Mainland building services skill for HVAC, electrical, water, drainage, and fire-systems coordination under national baseline and local authority requirements.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Services

Use this skill to structure MEP system strategy and ensure cross-discipline consistency from initial scheme through construction drawing review.

---

## 1. System Coordination Principles

- Lock plant-space and shaft strategy early; late MEP space changes cause major rework.
- Keep fire-system logic synchronized with HVAC smoke-control strategy.
- Coordinate equipment selection with energy target and maintenance capability.
- Ensure MEP drawings, schedules, and control narrative are internally consistent.

---

## 2. HVAC Strategy Checklist

| Topic | Design Output |
|---|---|
| Load baseline | Cooling/heating and fresh-air assumptions by function |
| System route | Chilled water/VRF/heat pump selection with constraints |
| Smoke control link | Mechanical strategy integrated with fire narrative |
| Controls | Zoning and BMS-level control logic |
| Commissioning | Test and balancing path defined at design stage |

---

## 3. Electrical and Power Distribution

- Incoming power strategy and redundancy requirements
- Vertical distribution and riser zoning
- Emergency and life-safety power boundaries
- Metering/sub-metering strategy aligned with operation and ESG needs

---

## 4. Water and Drainage

| Area | Key Requirement Direction |
|---|---|
| Potable and non-potable systems | Clear separation and labeling strategy |
| Drainage zoning | Storm/foul/process-water segregation as required |
| Pumping and backflow | Reliability and maintenance-access checks |
| Roof and podium drainage | Overflow and extreme-weather resilience details |

---

## 5. Fire-System Coordination

- Ensure alarm, hydrant/sprinkler, smoke control, and emergency power assumptions match fire design report.
- Keep equipment-room and shaft requirements consistent across MEP + architecture drawings.
- Track review comments as a single integrated fire-MEP closeout list.

---

## 6. Required Inputs (ask if missing)

- City and climate zone
- Building type and operation profile
- Stage (`方案` / `初设` / `施工图`)
- Utility connection constraints known so far
- Existing review comments or authority pre-consultation notes

---

*Baseline references: relevant national MEP/fire/energy standards and city-level local supplements.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| MEP coordination | `cn-building-services` | `cn-structural-systems` |
| Fire systems acceptance | `cn-building-services` | `cn-fire-acceptance-closeout` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
