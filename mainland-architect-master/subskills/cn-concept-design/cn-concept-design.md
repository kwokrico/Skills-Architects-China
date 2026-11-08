---
name: cn-concept-design
description: Mainland concept design skill covering massing strategy, control-indicator fit, stage-gate decisions, and fast-track delivery alignment under PRC workflows.
user-invocable: true
disable-model-invocation: true
---

# Mainland Concept Design

Concept design should lock planning viability, technical route, and delivery feasibility before deep engineering work starts.

---

## 1. Stage-Gate Logic

| Stage | Key Objective | Typical Output |
|---|---|---|
| 方案设计 | Planning feasibility and value proposition | Massing options + control indicator matrix |
| 初步设计 | Technical route lock and budget confidence | Discipline strategy report + key system selection |
| 施工图设计 | Buildable detail and review closure | Coordinated drawings + 审图-ready package |

---

## 2. Concept-Stage Mandatory Checklist

- [ ] `用地红线` / `建筑红线` confirmed
- [ ] Core indicators aligned: `容积率`, `建筑密度`, `绿地率`, `限高`
- [ ] Sunlight/wind/traffic constraints identified
- [ ] Fire strategy path selected (prescriptive vs performance-based candidate)
- [ ] Construction method and programme constraints reflected in concept options

---

## 3. Option Strategy Framework

| Option Type | Best Use |
|---|---|
| Compliance-first | Tight schedule, high approval certainty needed |
| Value-first | Yield optimization under controllable approval risk |
| Delivery-first | Complex site with construction/logistics constraints |

---

## 4. Cross-Discipline Lock Points at Concept

- Structural system direction and major transfer locations
- MEP plant and shaft strategy
- Fire egress and smoke-control route concept
- Envelope/energy intent and sustainability target level
- Construction and procurement path assumptions

---

## 5. Common Concept Failure Modes

| Failure | Consequence | Mitigation |
|---|---|---|
| Indicator assumptions not unified | Permit-stage redesign | Single indicator source and controlled updates |
| Concept ignores construction logistics | Cost/time blowout | Add contractor-logistics lens before option freeze |
| Fire strategy decided too late | Review delay | Set fire strategy path during concept |
| No city-specific review assumptions | Repeated comment cycles | Add city context and known authority preferences early |

---

## 6. Floor plate and massing tests

Floor-plate layout belongs here. 控规 indicators stay in `cn-spatial-planning`.

Compare central and side cores on the same floor envelope and programme. A central core can serve perimeter spaces with balanced circulation; a side core can release a larger continuous floor area but may lengthen routes and occupy useful facade frontage. Neither is automatically more efficient. Compare usable depth, daylight, tenant subdivision, structural layout, service shafts, and fire egress before selecting an option. Use `cn-building-programming` for a consistently defined net-to-gross comparison; without a dimensioned plan, give the method rather than a project-specific percentage.

| Plate | Use when | Watch |
|---|---|---|
| 板式 | East-west or south-facing residential slabs | Daylight depth and party-wall fire |
| 点式 | A small footprint tower | Core ratio and corner units |
| 核心筒 | Office or hotel typical floors | Lease depth from core to glass; stairs are a fire check in `cn-fire-life-safety` |
| 庭院 | Low-rise courts and schools | Sunlight into the court, and cross-ventilation |
| 中庭 | Deep commercial or public plans | Smoke control with `cn-fire-life-safety` before the void is frozen |

Massing tests to run before an option is frozen. Each test halts for the city. None of them is a pass/fail number from this skill:

- 日照包络, using GB 50180 and the city sunlight rule (`cn-spatial-planning`)
- Podium wind comfort at entrances and walkways
- View corridor named in the 控规 or urban-design guide
- Contextual height against 限高, neighbours, and any aviation or heritage cap

## 7. Required Inputs (ask if missing)

- City and district
- Control-plan indicator extract
- Land-condition highlights
- Commercial target (yield, phasing, product mix)
- Programme constraints and target milestone

---

*Baseline references: current PRC planning and technical workflow requirements, with city-level supplements.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Scheme massing, floor plate, core | `cn-concept-design` | `cn-spatial-planning` for 控规 and 日照间距 |
| Design theory critique | `cn-concept-design` | `cn-design-theory` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
