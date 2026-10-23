---
name: cn-building-programming
description: Mainland building programming skill for function mix, area planning, benchmark logic, and stage-based space governance under PRC planning and delivery context.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Programming

Use this skill to convert business/program goals into area schedules and disciplined space-allocation strategy.

---

## 1. Programming Framework

| Layer | Core Question |
|---|---|---|
| Demand | What market/service demand must the project satisfy? |
| Compliance | Which indicator and use constraints limit area allocation? |
| Delivery | Which spaces are critical path for approvals and construction? |

---

## 2. Area Allocation Method

1. Confirm total allowed envelope from planning and land constraints.
2. Allocate mandatory/support spaces before optimization spaces.
3. Build function-by-function schedule with net, gross, and shared-area logic.
4. Stress-test programme against operations and phasing.

---

## 3. Programme by Project Archetype (Directional)

| Archetype | Typical Programming Focus |
|---|---|---|
| Residential community | Product mix, core efficiency, shared amenity strategy |
| Office/commercial | Lease depth, core ratio, flexibility for tenant fit-out |
| Mixed-use complex | Vertical zoning, transfer interfaces, operations separation |
| Institutional/civic | Service standards, flow clarity, lifecycle maintainability |
| Industrial/logistics park | Functional throughput, modular expansion, utility resilience |

## 4. Programming Risk Controls

- Keep one controlled programme table through all stages.
- Flag all assumptions (occupancy, ratio targets, support-space factor).
- Prevent silent area drift by change-log ownership.
- Link programme updates to commercial and approval impacts.

---

## 5. Adjacency, room data, and site capacity

- Build an adjacency matrix before drawing a plan: required, preferred, and must-separate pairs. Vertical stacking of wet rooms and plant is part of the matrix.
- Issue a room data sheet for every repeated room: net area, occupants, daylight, acoustic target, and services. The sheet is a brief, not a code quotation.
- Capacity check: programme gross area against 计容建筑面积 from the 控规 and the land contract. If the programme does not fit, say so before massing options multiply. 计容 rules are `cn-spatial-planning` and `cn-building-codes`.
- Area standards by use (住宅, 办公, 中小学, 医院, 旅馆) come from the current sector code under GB 55031. Confirm the edition in [cn-code-catalog.md](../../references/cn-code-catalog.md). Do not invent a square-metre allowance.

Net-to-gross belongs in this skill. It is not a 控规 question.

## 6. Required Inputs (ask if missing)

- City and project typology
- Current planning indicator limits
- Target business model and phasing
- Stage (`方案` / `初设` / `施工图`)
- Any authority or client programme constraints already fixed

---

*Baseline references: relevant planning and sector standards, plus project-specific owner requirements and local authority conditions.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Functional brief, adjacency, net-to-gross | `cn-building-programming` | `cn-spatial-planning` for 控规 |
| Planning compliance | `cn-building-programming` | `cn-spatial-planning` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
