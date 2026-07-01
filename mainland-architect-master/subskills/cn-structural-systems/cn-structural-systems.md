---
name: cn-structural-systems
description: Mainland structural systems skill covering seismic-first structural strategy, high-rise systems, foundation selection, and constructability under national + local standards.
user-invocable: true
disable-model-invocation: true
---

# Mainland Structural Systems

Primary baseline includes `GB 50011`, `GB 50010`, and `GB 50007`, with city-specific supplements for seismic and high-rise implementation.

---

## 1. Structural Strategy Principles

- Seismic requirements are a primary design driver in many Mainland regions.
- Lateral system choice must reflect height, function, seismic intensity, and construction capability.
- Structural concept must align with architectural module and MEP shaft logic early.

---

## 2. Typical System Selection

| Building Type | Common Structural Direction |
|---|---|
| Residential towers | Shear-wall + core systems |
| Office/commercial towers | Core + frame / mega-frame / outriggers by height class |
| Podium and large-span zones | PT slab / steel-composite long-span strategy |
| Industrial/logistics | Steel or concrete frame optimized for speed and flexibility |

---

## 3. High-Risk Coordination Topics

- Transfer structures and vertical load-path discontinuities
- Outrigger and belt truss integration with architecture/MEP
- Seismic detailing at weak interfaces
- Foundation solution versus groundwater and adjacent structures

---

## 4. Foundation Strategy Framework

| Geotechnical Context | Typical Direction |
|---|---|
| Good bearing stratum shallow | Raft/strip solutions where feasible |
| Deep bearing layer / high load | Bored piles or deep foundations |
| Soft soil and settlement sensitivity | Composite treatment + differential settlement control |
| Dense urban context | Construction-method impact and adjacent-risk management |

---

## 5. Delivery and Constructability Controls

- Build a structural assumptions register from concept stage.
- Define hold points for critical pour/weld/connection inspections.
- Link design changes to recalculation and drawing revision control.
- Keep acceptance evidence organized by structural subsystem.

---

## 6. Required Inputs (ask if missing)

- City and seismic intensity context
- Building type and target height class
- Current stage and available geotechnical data
- Preferred construction method and programme constraints
- Any existing structural review comments

---

*Baseline references: GB 50011, GB 50010, GB 50007, and corresponding city-level structural supplements.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Structural system selection | `cn-structural-systems` | `cn-building-codes` |
| Seismic / foundation detail | `cn-structural-systems` | `cn-building-codes` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
