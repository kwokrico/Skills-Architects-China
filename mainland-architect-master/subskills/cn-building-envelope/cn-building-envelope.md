---
name: cn-building-envelope
description: Mainland building envelope skill covering climate-zone strategy, facade performance, durability, thermal control, and constructability under national and local standards.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Envelope

Use this skill for facade and roof strategy decisions across different Chinese climate zones and city-specific implementation requirements.

Regulatory hierarchy:
- National baseline first: `GB / GB-T / JGJ`
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Climate-Zone First Strategy

- Severe cold / cold: prioritize insulation continuity and condensation control.
- Hot summer cold winter: balance summer solar control and winter heat retention.
- Hot summer warm winter: reduce cooling load with shading, glazing selection, and ventilation control.

Always state project city and climate zone before final envelope recommendation.

---

## 2. Envelope Design Checklist

| Topic | Typical Output |
|---|---|
| Thermal control | U-value and shading strategy by orientation |
| Airtightness and moisture | Joint/air barrier/waterproof layer coordination |
| Fire interface | Fire-stop and facade fire-spread control details |
| Structural movement | Drift/thermal movement accommodation details |
| Maintenance | Access and replacement strategy for lifecycle reliability |

---

## 3. Facade System Selection Guidance

| Building Context | Preferred System Direction |
|---|---|
| High-rise office/commercial | Unitized curtain wall with strict movement/water testing |
| Residential towers | Window wall or hybrid facade with thermal-bridge control |
| Podium and mixed-use | Durable ventilated rainscreen where possible |
| Industrial/logistics | Robust, maintainable panelized systems with clear replacement paths |

---

## 4. Durability and Regional Adaptation

- Coastal/high humidity regions: stronger corrosion protection and sealant durability planning.
- Cold regions: freeze-thaw detailing and thermal bridge minimization.
- High-pollution urban cores: facade cleanability and maintenance frequency planning.
- Fast-track projects: pre-approved material/system catalog to reduce substitution risk.

---

## 5. Layer order and glazing

State the climate zone from GB 50176 before choosing a build-up. Digest: [GB_50176_Thermal_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_50176_Thermal_CS.md). Energy limits that conflict with GB 55015 follow GB 55015. Waterproofing continuity follows GB 55030.

Name the layer order in the wall and roof: structure, waterproofing, insulation, air barrier, and the finish. Do not publish a U-value table from this skill. Confirm U and shading coefficient in the official climate-zone table for the project city.

## 6. Required Inputs (ask if missing)

- City and climate zone
- Building type and height band
- Performance target (baseline / green-star target / near-zero energy ambition)
- Construction system and programme constraints
- Local review comments already received

---

*Baseline references: applicable national envelope/energy standards and local city supplements (DB/DGJ/DBJ) by climate zone.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Façade / envelope performance | `cn-building-envelope` | `cn-material-selection` |
| MEP plant coordination | `cn-building-envelope` | `cn-building-services` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [GB_50176_Thermal_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_50176_Thermal_CS.md) — climate zones
* [cn-atlas-topic-index.md](../../references/cn-atlas-topic-index.md) — roof, waterproofing, and curtain-wall details
* [cn-statutory-source-register.md](../../references/cn-statutory-source-register.md) — JGJ 102, JGJ 133, GB/T 21086, and GB 8624 are not ingested
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
