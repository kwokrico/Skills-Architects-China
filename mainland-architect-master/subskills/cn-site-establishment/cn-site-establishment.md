---
name: cn-site-establishment
description: Coordinates Mainland pre-construction mobilisation, including 三通一平, hoarding, temporary works, utility diversion, and neighbour interfaces after the construction permit path is clear.
user-invocable: true
disable-model-invocation: true
---

# Mainland Site Establishment

Pre-construction mobilisation. Approval timing stays in `cn-consent-scheduling`. Traffic submissions stay in `cn-traffic-coordination`. Carrier diversions stay in `cn-telecom-coordination`. Hazardous temporary works stay in `cn-construction-health-safety`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 三通一平, hoarding, temporary site, neighbour liaison | `cn-site-establishment` | `cn-consent-scheduling` |
| 占道 permit drawings | `cn-site-establishment` | `cn-traffic-coordination` |
| 危大工程 method statement | `cn-site-establishment` | `cn-construction-health-safety` |

## 1. Scope and Position

Site establishment starts only when the legal start condition is identified: usually a 施工许可证, or a written city rule for preparatory works that are allowed earlier. Do not treat a planning permit as permission to excavate.

The architect coordinates design information. The contractor owns means and methods. 监理 inspects. The client obtains land possession.

## 2. Pre-Construction Readiness Gate

| Gate | Evidence | If missing |
|------|----------|------------|
| Land possession | Handover record, boundary survey | Stop excavation |
| Permits | 施工许可证 or documented early-works authority | Stop |
| 审图 | Qualified drawings for the works being started | Do not build from tender-only sheets |
| Appointments | Contractor, 监理, design representative | Stop |
| Utilities | Existing-services survey | Stop breaking ground |
| Safety | Site safety plan and 危大工程 list | `cn-construction-health-safety` |
| Neighbours | Party-wall / adjacent-building condition survey where the city or contract requires it | Record the gap |
| Environment | Drainage, dust, noise, and waste arrangements | City enforcement risk |

## 3. Hoarding and Site Enclosure

### 3.1 Design information the architect may need to show

- Hoarding line relative to 用地红线, pavement, and sight lines.
- Gates, vehicle sweep, and pedestrian diversion.
- Height, lighting, and drainage of the enclosure.
- Graphic or civic requirements if the city publishes a hoarding guide.
- Protection of existing trees that the planning permit retains.

### 3.2 Permits

占道, road occupation, and excavation permits are municipal or traffic-police approvals. They are not part of the 施工许可证 by default. Route the traffic drawing to `cn-traffic-coordination`.

## 4. Temporary Works

| Item | Design information | Specialist owner |
|------|--------------------|------------------|
| Tower crane base | Location, slewing, load assumptions | Contractor engineer; structure reviews interface |
| Scaffold and formwork | Not an architectural design unless specified | 危大工程 if the threshold is met |
| Dewatering | Drawdown and adjacent settlement | Geotechnical / contractor |
| Site offices and dormitories | Planning and fire constraints on temporary buildings | Contractor; architect flags use and location |
| Protection decks | Load and headroom | Contractor |

The architect does not approve a method statement by reviewing a plan for "design intent" only. Say what was reviewed.

## 5. Utility and Undertaker Liaison

Typical undertakers: power, water, drainage, gas, heating, and the three telecom carriers. Sequence:

1. Existing-services CCTV or radar survey.
2. Conflict schedule against piling and basement.
3. Diversion design by the undertaker or a qualified designer.
4. Outage windows and temporary supplies (水通, 电通, 路通).
5. As-built of diversions before permanent works cover them.

Telecom detail: `cn-telecom-coordination`.

## 6. Authority, Neighbour, and Stakeholder Interfaces

Use [cn-construction-stakeholder-register.md](../../references/cn-construction-stakeholder-register.md).

| Interface | Architect action |
|-----------|------------------|
| 住建 quality/safety station | Confirm supervision registration is the contractor's and client's task; provide drawings |
| 交警 / 城管 | Support 占道 drawings; do not negotiate enforcement |
| Adjacent owners | Condition survey and access agreement via the client |
| Metro or railway operator | Clearance and monitoring if within the protection zone |
| Heritage authority | Stop if the hoarding or excavation enters a protected area without approval |
| Schools, hospitals | Noise and access constraints in the programme |

## 7. Mobilisation Pack

Issue pack contents:

- Site logistics plan and hoarding line.
- Existing-services drawing and diversion status.
- Temporary drainage and environmental controls.
- Tree and heritage constraints.
- Contact register.
- Open permits list with owners and dates.
- First four-week look-ahead pointer (`cn-construction-programme`).

## 8. Programme Hooks

- Hoarding and diversions are predecessors of piling, not parallel activities, unless the method says so.
- Crane erection may be a 危大工程 hold point.
- Power for the tower crane is a utility predecessor.
- Do not show "site start" on the date the permit is submitted.

## 9. Cross-References

- Permit path: `cn-consent-scheduling`.
- Traffic: `cn-traffic-coordination`.
- Telecom: `cn-telecom-coordination`.
- Safety: `cn-construction-health-safety`.
- Sequence: `cn-construction-programme`.
- Checklist shell: [cn-site-establishment-checklist.md](../../references/cn-site-establishment-checklist.md).

## 10. Output Checklist

- Legal start authority named.
- Red line and hoarding line distinguished.
- Services survey status stated.
- 占道 and carrier diversions assigned to the right skill.
- 危大工程 items flagged, not designed in this note.
- Neighbour and metro constraints listed or marked missing.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-site-establishment-checklist.md](../../references/cn-site-establishment-checklist.md) — mobilisation checklist
* [cn-construction-stakeholder-register.md](../../references/cn-construction-stakeholder-register.md) — authority map
* [Construction_Permit_CS.md](../../../cn_s_reference/MOHURD/summaries/Construction_Permit_CS.md) — permit digest
