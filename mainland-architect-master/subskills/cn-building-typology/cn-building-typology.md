---
name: cn-building-typology
description: Mainland building typology skill covering high-rise residential, office/commercial, mixed-use complexes, institutional projects, industrial parks, and urban-regeneration patterns.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Typology

Use this skill to choose appropriate design and delivery logic by typology and city context.

---

## 1. High-Rise Residential Communities

Key focus:
- Product mix versus market position
- Core efficiency and sellable/usable balance
- Fire and egress strategy for height class
- Delivery speed versus quality consistency

---

## 2. Office and Commercial Towers

Key focus:
- Large, efficient floor plates and leasing flexibility
- Vertical transportation strategy and lobby throughput
- Envelope-performance and operating-cost control
- Intelligent system integration for high-spec tenancy

---

## 3. Mixed-Use Complexes (综合体)

Key focus:
- Vertical zoning and circulation separation
- Transfer structure and MEP zoning complexity
- Phased opening and operational interface
- Commercial viability and footfall management

---

## 4. Institutional and Civic Buildings

Key focus:
- Public-service workflow and safety compliance
- Functional adjacency and lifecycle maintainability
- Multi-agency acceptance and operational handover readiness

---

## 5. Industrial Parks and Advanced Manufacturing

Key focus:
- Process-flow compatibility and expansion flexibility
- Utility capacity and reliability
- Heavy-load and logistics integration
- Environmental and safety compliance for process uses

---

## 6. Urban Regeneration and Existing-Asset Transformation

Key focus:
- Existing-condition constraints and retrofit strategy
- Change-of-use compliance path
- Construction sequencing under occupied conditions
- Value uplift versus technical risk

---

## 7. Typology Selection Matrix

| If the project priority is... | Prioritize typology strategy... |
|---|---|
| Fast delivery | Standardized structural/MEP modules and low-complexity interfaces |
| Yield maximization | High-efficiency product mix with strict indicator governance |
| City landmark quality | High-performance envelope and integrated public-realm strategy |
| Operational resilience | Strong lifecycle maintenance and facility-management logic |

---

## 8. Required Inputs (ask if missing)

- City and district
- Target typology and business model
- Stage and programme pressure
- Known planning/land constraints
- Delivery mode (`传统施工` / `EPC` / `设计施工总承包`)

---

*Baseline references: applicable national/local standards and project-specific planning/contract constraints by typology.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Typology and standard floors | `cn-building-typology` | `cn-concept-design` |
| Code applicability | `cn-building-typology` | `cn-building-codes` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
