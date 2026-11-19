---
name: cn-acoustic-design
description: Mainland acoustic design skill for environmental noise control, facade/internal acoustic targets, vibration-risk handling, and construction-phase noise management.
user-invocable: true
disable-model-invocation: true
---

# Mainland Acoustic Design

Use this skill to manage acoustic performance from planning stage through construction and operation handover.

---

## 1. Acoustic Design Scope

Reverberation time for school, assembly, and hotel public rooms is part of this skill. Route it to GB 50118 where GB 55016 does not conflict. Confirm the GB 50118 edition in [cn-code-catalog.md](../../references/cn-code-catalog.md). Do not quote a second from memory. For a residential room, GB 55038-2025's announcement repeals GB 50118-2010 clauses 4.2.1, 4.2.2, and 4.2.5. Open [GB_55038_2025_Residential_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_55038_2025_Residential_CS.md) before reusing those clauses.

Airborne separation, impact noise, and flanking are already in the controls below.

- Environmental noise impact at site boundary and sensitive receivers
- Facade sound insulation strategy
- Internal room-to-room acoustic separation
- Vibration control for rail/mechanical and sensitive spaces
- Construction-phase noise control planning

---

## 2. Design Workflow

1. Identify noise and vibration sources by typology and site context.
2. Set target acoustic criteria by space function.
3. Build envelope and internal-partition acoustic package.
4. Validate with calculations/simulation and adjust details.
5. Track substitutions and on-site installation quality at critical interfaces.

---

## 3. Typical Control Measures

| Problem Type | Control Direction |
|---|---|
| Road/rail external noise | Facade STC/Rw strategy + window system selection |
| Mechanical plant noise | Equipment isolation + plant-room acoustic treatment |
| Floor/partition transmission | Layered assemblies and flanking-path control |
| Vibration-sensitive spaces | Structural isolation and equipment mounting strategy |

---

## 4. Construction-Phase Risk Controls

- Sequence high-noise works with permit and community-impact constraints.
- Define temporary mitigation (barriers, work-hour controls, equipment choice).
- Require contractor method statements for noise-critical operations.
- Keep complaint-response and monitoring logs auditable.

---

## 5. Required Inputs (ask if missing)

- City and district
- Nearby sensitive uses (residential/school/hospital/lab)
- Building function and critical acoustic spaces
- Stage (`方案` / `初设` / `施工图` / `施工`)
- Known complaints or authority conditions already issued

---

*Baseline references: applicable national and local acoustic/noise-control requirements and project-specific environmental approval conditions.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Acoustic criteria and layout | `cn-acoustic-design` | `cn-building-services` |
| Code hierarchy for building | `cn-acoustic-design` | `cn-building-codes` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [cn-code-catalog.md](../../references/cn-code-catalog.md) — GB 50118 under GB 55016
* [GB_55038_2025_Residential_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_55038_2025_Residential_CS.md) — residential clauses the announcement repealed
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
