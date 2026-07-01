---
name: cn-daylighting-design
description: Mainland daylighting design skill for code-compliant natural lighting strategy, glare control, simulation workflow, and climate-zone-specific facade response.
user-invocable: true
disable-model-invocation: true
---

# Mainland Daylighting Design

Use this skill to balance natural lighting quality, energy impact, and envelope constraints under Mainland code and local implementation.

---

## 1. Daylighting Strategy Principles

- Start with function-specific daylight targets, then test against facade and thermal constraints.
- Control glare and overheating together with daylight design; do not optimize in isolation.
- Use simulation for dense urban contexts and deep-plan spaces.

---

## 2. Design Workflow

1. Define target spaces and performance criteria.
2. Build simplified orientation and massing test.
3. Run simulation and identify underlit/glare-prone zones.
4. Iterate aperture, shading, and internal reflectance strategy.
5. Freeze details with envelope and MEP coordination.

---

## 3. Typical Technical Controls

| Issue | Control Direction |
|---|---|
| Deep-plan underlighting | Atrium/lightwell/light-shelf strategies |
| East-west glare | Vertical shading and controlled WWR |
| Internal glare | Surface reflectance and shading operation strategy |
| Daylight-energy conflict | Coordinate with HVAC and envelope thermal strategy |

---

## 4. Review-Ready Deliverables

- Daylight simulation report with assumptions
- Orientation and shading rationale
- Key room daylight/glare compliance matrix
- Coordination notes linking daylight decisions to envelope and MEP

---

## 5. Required Inputs (ask if missing)

- City and climate zone
- Building function and critical room types
- Stage (`方案` / `初设` / `施工图`)
- Existing envelope concept and WWR assumptions
- Simulation method/tool expectations from review team

---

*Baseline references: applicable national daylight/energy requirements and city-level implementation guidance.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Daylight and shading | `cn-daylighting-design` | `cn-spatial-planning` |
| 日照 regulatory analysis | `cn-daylighting-design` | `cn-spatial-planning` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
