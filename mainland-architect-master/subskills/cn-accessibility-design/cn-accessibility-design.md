---
name: cn-accessibility-design
description: Mainland accessibility design skill based on GB 50763 and local supplements, covering routes, ramps, lifts, sanitary spaces, signage/tactile systems, and review acceptance focus.
user-invocable: true
disable-model-invocation: true
---

# Mainland Accessibility Design

Primary baseline: `GB 50763` + local implementation supplements.

Regulatory hierarchy:
- National baseline first: `GB / GB-T / JGJ`
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Compliance Principles

1. Provide continuous step-free routes from site entry to key functional spaces.
2. Keep accessibility strategy aligned across architecture, structure, and MEP.
3. Treat signage, tactile guidance, and emergency egress coordination as one system.
4. Confirm local supplement requirements before freezing construction drawings.

---

## 2. Required Design Scope Checklist

| Domain | Typical Deliverable |
|---|---|
| External access | Site arrival and barrier-free entrance strategy |
| Internal route | Horizontal and vertical accessible circulation map |
| Lift and platform interfaces | Dimensioned access details and control heights |
| Sanitary spaces | Accessible toilet layout and transfer clearances |
| Wayfinding | Tactile/visual signage system |
| Parking and drop-off | Accessible parking and boarding/alighting arrangements |

---

## 3. Approval and Review Touchpoints

| Stage | Focus |
|---|---|
| 方案设计 | Accessibility concept and route continuity |
| 初步设计 | System-level coordination and key dimension confirmation |
| 施工图设计 | Third-party审图 acceptance readiness |
| 竣工阶段 | Built-condition compliance and acceptance evidence |

---

## 4. Common Risks and Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| Late accessibility integration | Rework at审图 or construction stage | Lock route strategy at concept phase |
| Dimension coordination gaps | Non-compliant turning/transfer spaces | Add interdisciplinary clearance checks |
| Incomplete tactile/signage logic | Poor usability and review comments | Use route-based signage/tactile matrix |
| Local supplement ignored | City-level rejection | Include city context and local standard checklist |

---

## 5. Required Inputs (ask if missing)

- City and district
- Current stage (`方案` / `初设` / `施工图` / `施工`)
- Building type and user profile (public/private/institutional)
- Existing审图意见 (if any)
- Site constraints affecting step-free route continuity

---

*Baseline reference: GB 50763 and local municipal supplements for accessibility implementation.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| GB 50763 and accessibility design | `cn-accessibility-design` | `cn-building-codes` |
| Planning indicators only | `cn-accessibility-design` | `cn-spatial-planning` |
| 审图 drawing package structure | `cn-accessibility-design` | `cn-construction-documentation` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
