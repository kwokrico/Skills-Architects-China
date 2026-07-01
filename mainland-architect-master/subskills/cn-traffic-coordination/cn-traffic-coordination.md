---
name: cn-traffic-coordination
description: Activate for Mainland traffic impact assessment (交通影响评价), construction traffic organisation (施工交通组织方案), 交警审批, and highways/municipal interface during planning and construction.
user-invocable: true
disable-model-invocation: true
---

# Mainland Traffic Coordination
Traffic consultant scope, planning-stage TIA, construction-stage traffic organisation, and submission workflows. Do not conflate planning TIA with construction TMP.

Reference: [cn-traffic-submission-types.md](../../references/cn-traffic-submission-types.md).

---

## 1. Scope

- **Planning stage:** 交通影响评价 when triggered by size, location, or planning conditions.
- **Construction stage:** 施工交通组织方案 / 交通疏导方案 for 占道、车辆进出、材料运输.
- **Authorities:** 交警、交通运输、城管 (varies by city).

---

## 2. When to Engage

- New large generator of traffic (office, retail, hospital).
- Planning condition requires TIA.
- Construction affects arterial roads, bus stops, or pedestrian flows.
- Hoarding or crane oversail affects carriageway.

---

## 3. Traffic Consultant Scope

Typical deliverables:

1. Existing traffic survey and peak-hour analysis.
2. Trip generation and distribution (planning).
3. Junction level of service / saturation checks.
4. Mitigation: access design, signal timing, parking supply.
5. Construction-phase accommodation plan (TMP).

---

## 4. TIA (Planning)

- Submit with 方案 or 报建 per local requirement.
- Align access design with `cn-spatial-planning` red lines and fire lanes.
- Condition compliance tracker for post-approval.

---

## 5. TMP (Construction)

- Lane closures, temporary signals, pedestrian diversions.
- Haul route and delivery windows.
- Bus stop relocation and signage.
- Interface with `cn-site-establishment` hoarding permits.

**Hard stop:** Planning-condition TIA ≠ construction TMP—verify which document the authority expects.

---

## 6. Programme and Risk

- TIA review cycles can block planning permit.
- TMP approval before 占道施工.
- Event conflicts (marathon, holiday peaks).

---

## 7. Output Checklist

- Study brief or submission tracker.
- TIA vs TMP scope clearly labelled.
- Authority contact and reference numbers.
- Hoarding-traffic interface notes.
- Programme assumptions stated.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| TIA / 交警 / TMP | `cn-traffic-coordination` | `cn-site-establishment` |
| 控规 / planning | `cn-traffic-coordination` | `cn-spatial-planning` |
| Construction programme | `cn-traffic-coordination` | `cn-construction-programme` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-traffic-submission-types.md](../../references/cn-traffic-submission-types.md) — submission types
