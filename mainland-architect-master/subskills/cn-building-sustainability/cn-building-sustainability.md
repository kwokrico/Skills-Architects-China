---
name: cn-building-sustainability
description: Mainland sustainability skill covering GB/T 50378, three-star green building, dual-carbon targets, near-zero energy pathways, and city-level implementation differences.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Sustainability

Use for sustainability strategy, compliance planning, and practical low-carbon delivery in Mainland projects.

Regulatory hierarchy:
- National baseline first: `GB / GB-T / JGJ`
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Policy and Standard Baseline

| Layer | Reference |
|---|---|---|
| National green standard | `GB/T 50378` |
| Carbon strategy | 双碳目标 related construction-sector policy |
| Building energy pathway | Near-zero/low-energy standards and local implementation |
| Market expectation | ESG disclosure and REIT/institutional investor reporting requirements |

---

## 2. Green Certification Strategy

| Goal | Typical Positioning |
|---|---|
| Baseline compliance | Meet mandatory energy and green requirements |
| Market differentiation | Target higher green-star rating or advanced low-carbon package |
| International interface | Add LEED/WELL only when investor/tenant requires |

---

## 3. Technical Focus Areas

| Area | Typical Design Concern |
|---|---|
| Envelope | Climate-zone-sensitive heat gain/loss control |
| HVAC and systems | Efficiency baseline + operational carbon reduction |
| Water | Water-saving fixtures, reuse strategy, landscape demand control |
| Materials | Embodied-carbon aware selection and supply-chain traceability |
| Operations | Metering, commissioning, and post-occupancy performance tracking |

---

## 4. Stage-Based Delivery Framework

| Stage | Sustainability Work Package |
|---|---|
| 方案设计 | Target setting, massing/orientation, passive strategy baseline |
| 初步设计 | System strategy, energy/water model assumptions, capex-opex trade-offs |
| 施工图设计 | Detail-level compliance closure and submission package |
| 施工阶段 | Product substitution control and commissioning plan |
| 运营准备 | KPI baseline and monitoring framework |

---

## 5. Common Risks and Mitigation

| Risk | Consequence | Mitigation |
|---|---|
| Green target set too late | Cost increase and schedule pressure | Lock target and compliance path at concept stage |
| Over-reliance on generic benchmarks | Poor city-level fit | Use city climate and local审查 requirements |
| Design-build substitution drift | Performance downgrade | Create protected sustainability control list |
| ESG reporting not considered | Weak investor communication | Define reportable metrics during design stage |

---

## 6. Required Inputs (ask if missing)

- City and climate zone
- Project type and target certification level
- Stage and remaining programme
- Investor or tenant ESG constraints
- Existing energy model assumptions (if any)

---

*Baseline references: GB/T 50378, national and local green-building implementation policies, and applicable low-energy/near-zero-energy standards.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Green / 双碳 / 三星 | `cn-building-sustainability` | `cn-building-codes` |
| Energy modelling detail | `cn-building-sustainability` | `cn-building-envelope` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
