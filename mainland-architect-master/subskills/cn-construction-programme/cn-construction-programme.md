---
name: cn-construction-programme
description: Mainland construction sequencing for high-rise and podium projects, including swimlanes, hold points, and look-ahead planning. Durations are illustrative, not norms.
user-invocable: true
disable-model-invocation: true
---

# Mainland Construction Programme

Sequences the works. It does not certify a contractor's programme or a statutory duration.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 工序穿插, floor cycle, look-ahead, hold points | `cn-construction-programme` | `cn-project-management` |
| Governance and client reports | `cn-construction-programme` | `cn-project-management` |
| Design-representative inspections | `cn-construction-programme` | `cn-site-supervision` |

## Halt Criteria

- Do not state that a floor cycle "complies" with a code.
- Do not copy a Hong Kong typical cycle as a Mainland norm.
- If ground conditions, crane strategy, or prefabrication scope are unknown, label durations as assumptions.

## 1. Archetype Defaults (Illustrative Only)

| Archetype | Pattern to test | Do not treat as a norm |
|-----------|-----------------|------------------------|
| High-rise residential tower | Core and typical floor, then facade and fit-out follow | "5 days a floor" without a method |
| Podium plus tower | Podium structure may lag or lead the tower; services plant often on the podium roof | Assuming the podium is finished first |
| Basement in a dense city | Excavation, strutting, and neighbours dominate the start | Starting the tower on a calendar date |
| Prefabricated residential | Factory slot and transport govern the cycle | Site-poured assumptions |

Ask for the contractor's method before commenting on a duration.

## 2. Swimlane Index

Use [cn-construction-sequence-swimlanes.md](../../references/cn-construction-sequence-swimlanes.md). Typical lanes:

| Lane | Owner | Architect input |
|------|-------|-----------------|
| Structure | Contractor | Grid, load paths, temporary openings |
| Facade | Specialist | Setting-out, embedments, waterproofing line |
| MEP risers | MEP contractor | Shaft sizes frozen before the floor closes |
| Lifts | Specialist | Shaft dimensions and machine-room access |
| Fit-out | Fit-out contractor | Wet areas and fire compartments frozen |
| External works | Civil | Red line, 绿地率 areas, site levels |
| Inspections | 监理 / design representative | Hold points, not a second programme |

## 3. Substitution Table

| Diagram idea | Mainland reading |
|--------------|------------------|
| Statutory hold before excavation | 施工许可证 and 危大工程 scheme where required |
| Follow-the-structure facade | Embedments issued before the floor is cast |
| Standard-floor learning curve | First three floors are not the sustained cycle |
| Commissioning | Fire, lift, and waterproof tests before acceptance dossiers |
| Partial possession | Contract sectional completion plus a statutory path for the part occupied |

## 4. Early Freezes (Design to Site)

| Freeze | Latest useful point | If late |
|--------|---------------------|---------|
| Basement outline and pile layout | Before excavation tender | Retaining redesign |
| Facade embedments | Before the affected slab | Break-out |
| Fire compartment and exit widths | Before 审图, and again before wall build | Opening-up |
| Shaft and plant sizes | Before riser slabs close | Services clash |
| Prefabricated module geometry | Before factory release | Site rework |
| Landscape levels | Before podium slab edges | 绿地率 and drainage errors |

## 5. Interface Rules

- Structure does not cover a services opening that is still "to be confirmed".
- Facade does not close a floor that has not passed the waterproofing hold point at the slab edge.
- Fit-out does not conceal a fire damper or a compartment line that 监理 has not seen.
- Lift installation does not start until shaft verticality is recorded.
- External works do not finish 绿地 until the planning area calculation method is agreed (`cn-spatial-planning`).

## 6. Programme Artefacts

| Artefact | Use |
|----------|-----|
| Master programme | Permits, design freezes, construction, commissioning, acceptance |
| 90-day look-ahead | Procurement of specialists |
| 4-week look-ahead | Site coordination; template `references/templates/construction-look-ahead.md` |
| Hold-point register | Activities that stop until an inspection or a drawing |
| Information-required schedule | Drawings the contractor needs, with dates |
| Change impact note | Added duration, not only added cost |

## 7. Six Checks Before Accepting a Programme Narrative

1. Permit predecessors are on the critical path.
2. 危大工程 expert review is a predecessor of the dangerous activity, not a footnote.
3. Design-information dates are earlier than the work.
4. Commissioning and statutory acceptance are separate from contract completion.
5. Weather allowance matches the contract, not a Hong Kong typhoon table (`cn-procurement-strategy`).
6. Learning-curve floors are not used as the average cycle.

## 8. Output Checklist

- Durations marked illustrative or taken from the contractor's programme.
- Hold points listed.
- Facade and prefabrication freezes dated.
- Acceptance path not collapsed into "practical completion".
- Look-ahead template offered when the user wants a table.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-construction-sequence-swimlanes.md](../../references/cn-construction-sequence-swimlanes.md) — swimlanes
* [construction-look-ahead.md](../../references/templates/construction-look-ahead.md) — four-week shell
