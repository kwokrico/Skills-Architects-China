---
name: cn-material-selection
description: Mainland material selection skill for durability, compliance, embodied-carbon awareness, supply-chain risk control, and constructability across regions and climates.
user-invocable: true
disable-model-invocation: true
---

# Mainland Material Selection

Use this skill to select materials that balance compliance, lifecycle performance, procurement reliability, and low-carbon objectives.

---

## 1. Material Selection Priorities

| Priority | Intent |
|---|---|
| Compliance | Meet fire, health, structural, and environmental requirements |
| Durability | Match local climate and pollution/corrosion conditions |
| Constructability | Fit local supply chain and site installation capability |
| Carbon and ESG | Improve embodied-carbon and material traceability |
| Lifecycle cost | Balance initial cost with maintenance/replacement profile |

---

## 2. Regional Durability Strategy

| Region Type | Material Risk Focus |
|---|---|
| Coastal/high humidity | Corrosion, sealant aging, moisture ingress |
| Cold/freeze-thaw regions | Crack resistance and freeze-thaw durability |
| Industrial pollution zones | Surface degradation and cleanability |
| High-solar/high-heat zones | UV stability and thermal movement accommodation |

---

## 3. Specification and Substitution Control

- Define approved material baseline and alternates at tender stage.
- Require substitution evidence: performance, compliance, lifecycle impact.
- Lock critical fire/acoustic/durability materials against uncontrolled change.
- Track sample/mock-up approval status as part of quality gateway.

---

## 4. Typical High-Risk Material Interfaces

| Interface | Risk |
|---|---|
| Facade system + fixing | Corrosion and movement incompatibility |
| Waterproofing + substrate | Bond failure and leakage |
| Fire-stop + service penetration | Fire-compartment integrity breakdown |
| Acoustic layer + structural frame | Flanking transmission due to poor detailing |

---

## 5. Required Inputs (ask if missing)

- City and climate context
- Building use and durability class expectations
- Fire/acoustic/performance constraints
- Procurement constraints (supplier and lead time)
- Sustainability target level and ESG reporting needs

---

*Baseline references: national material/fire/environment standards plus local implementation requirements and project-specific performance specs.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Materials and fire rating | `cn-material-selection` | `cn-fire-life-safety` |
| Envelope build-up | `cn-material-selection` | `cn-building-envelope` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
