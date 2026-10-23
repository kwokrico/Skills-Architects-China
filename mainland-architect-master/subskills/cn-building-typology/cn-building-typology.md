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

Organization, before product mix:

| Type | What it is | First check |
|---|---|---|
| 单元式 | Stairs and lifts shared by a handful of flats per floor | Party walls and the number of flats on the public corridor |
| 通廊 | A long shared corridor serving many flats | Corridor smoke and daylight to the units |
| 板式 | A slab, usually with a preferred orientation | Sunlight spacing and end-unit wind |
| 点式 | A tower on a small plate | Core ratio and corner rooms |

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

## 7. School, hospital, and hotel

Civic section 4 stays the general public-building note. These three need their own organization:

| Use | Organization to settle first | Do not collapse into |
|---|---|---|
| School | Teaching cluster, separate student and service entries, outdoor play next to classrooms | An office plate with classrooms renamed |
| Hospital | Department adjacency, clean and soiled routes, outpatient versus inpatient vertical split | A 综合体 with a clinic on the ground floor |
| Hotel | Guest floor efficiency, back-of-house spine, and a separate service core where the star level needs it | A residential tower with a lobby |

Room areas for each use go to `cn-building-programming` and the current sector code under GB 55031.

## 8. Typology Selection Matrix

| If the project priority is... | Prioritize typology strategy... |
|---|---|
| Fast delivery | Standardized structural/MEP modules and low-complexity interfaces |
| Yield maximization | High-efficiency product mix with strict indicator governance |
| City landmark quality | High-performance envelope and integrated public-realm strategy |
| Operational resilience | Strong lifecycle maintenance and facility-management logic |

---

## 9. Required Inputs (ask if missing)

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
