---
name: cn-traffic-coordination
description: Coordinates Mainland traffic-impact assessments and construction traffic management with the planning authority and the traffic police. It does not approve a road closure.
user-invocable: true
disable-model-invocation: true
---

# Mainland Traffic Coordination

Planning-stage traffic impact and construction-stage traffic management. Hoarding design coordination stays in `cn-site-establishment`. Planning conditions stay in `cn-spatial-planning`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 交通影响评价, 交警, construction traffic | `cn-traffic-coordination` | `cn-site-establishment` |
| Whether a TIA is a planning condition | `cn-traffic-coordination` | `cn-spatial-planning` |
| Hoarding line and site logistics drawing | `cn-traffic-coordination` | `cn-site-establishment` |

## 1. Scope

| Document | Stage | Question it answers |
|----------|-------|---------------------|
| 交通影响评价 (TIA) | Planning / 方案 | Whether the completed project is acceptable on the road network |
| 交通组织 or 施工交通疏解 | Construction | How vehicles and pedestrians move while the site is open |
| 占道 / 开挖许可 | Construction | Permission to occupy or open the public road |
| Parking and drop-off layout | Design | Whether the site plan matches the planning condition |

The architect coordinates space and programme. A traffic consultant signs the traffic study when the city requires a qualified author. This suite does not sign it.

## 2. When to Engage

- The 控规, 出让合同, or local rules require a TIA for the use or the size.
- The site plan changes an access, a bus stop, or a metro entrance.
- Construction occupies a footway, a lane, or a bus stop.
- Crane oversailing or hoarding reduces sight distance.
- The user cannot name the city. Ask before describing the approval path.

## 3. Traffic Consultant Scope

Brief the consultant with:

- Site boundary, accesses, and basement ramps.
- Use and floor area by type.
- Construction phases and peak truck numbers if known.
- Neighbours: schools, hospitals, metro exits.
- The planning condition text if it already exists.

The consultant owns trip generation, junction assessment, and the traffic-management drawing. The architect owns the building access geometry and the hoarding line.

## 4. Planning-Stage TIA

1. Confirm the trigger in the city's rules. Do not assume a national floor-area threshold.
2. Submit through the path the 规自局 or the traffic bureau states (they differ by city).
3. Carry conditions into the site plan: access location, sight line, loading bay, and non-motorised parking.
4. A TIA approval is not a construction 占道 permit.

Detail types: [cn-traffic-submission-types.md](../../references/cn-traffic-submission-types.md).

## 5. Construction Traffic Management

| Item | Content |
|------|---------|
| Vehicle route | Approach, gate, and banned streets |
| Pedestrians | Temporary footway width and lighting |
| Buses and metro | Stop relocation if any, with the operator |
| Hours | Match the city's noise and truck-ban rules |
| Emergency | Fire-engine path kept open |
| Duration | Tied to the construction phase, not "for the whole job" if only the basement needs the lane |

The traffic police or the urban administrative bureau accepts or rejects the drawing. The architect does not issue the permit.

## 6. Submission Workflow

1. Identify the accepting body for this city (traffic police, transport bureau, or a combined window).
2. Coordinate the drawing with the hoarding plan.
3. Allow a resubmission cycle in the programme (`cn-consent-scheduling`).
4. File the permit before the occupation starts.
5. Update the drawing if the gate moves.

## 7. Municipal Road Interface

Road opening, reinstatement, and bus-stop civils may sit with the municipal road authority rather than the traffic police. Name both if both must sign. Utility trenches in the same occupation go through `cn-telecom-coordination` and `cn-site-establishment`.

## 8. Programme and Risk

- TIA conditions can move a basement ramp after 方案. Put the TIA before the ramp is frozen.
- 占道 permits expire. Renewal is a predecessor of the next phase.
- A refused lane closure needs a method change, not a quieter drawing of the same closure.
- School-peak bans can remove a month of daytime concrete pours. Ask.

## 9. Output Checklist

- City named.
- TIA trigger confirmed or listed as unknown.
- Construction traffic drawing separated from the planning TIA.
- Accepting authority named or requested.
- Hoarding and telecom excavations cross-referenced.
- No claim that the drawing is approved.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-traffic-submission-types.md](../../references/cn-traffic-submission-types.md) — submission types
* [Urban_Rural_Planning_Law_CS.md](../../../cn_s_reference/MNR/summaries/Urban_Rural_Planning_Law_CS.md) — planning-law digest
