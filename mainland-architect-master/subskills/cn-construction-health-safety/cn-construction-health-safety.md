---
name: cn-construction-health-safety
description: Activate for Mainland construction H&S—建设工程安全生产管理条例, 危大工程专项方案, 安监站 interface, risk assessments, accident reporting, and site safety audits. Not building fire code—route fire strategy to cn-fire-life-safety.
user-invocable: true
disable-model-invocation: true
---

# Mainland Construction Health & Safety
Construction-phase safety strategy and regulatory liaison. Distinct from **fire life safety design** (`cn-fire-life-safety`) and **fire acceptance** (`cn-fire-acceptance-closeout`).

---

## 1. Scope

- Site safety plan framework and risk assessments.
- Regulatory liaison with 住建安监、应急管理部门 (per local practice).
- Accident investigation support and reporting triggers.
- Site safety inspections and audit records.
- Coordination with监理 and contractor safety officers.

**Hard stop:** Not building fire code compliance design—route sprinkler/MOE strategy to `cn-fire-life-safety`.

---

## 2. H&S Strategy

Minimum elements:

1. Project safety organisation chart.
2. Hazard register (基坑、塔吊、高处作业、有限空间).
3. Training and induction records.
4. PPE and perimeter control.
5. Emergency response and evacuation (site-level).

---

## 3. 危大工程 (High-Risk Works)

Typical categories requiring专项方案 and expert论证 (when triggered):

- Deep excavation and foundation pits.
- Template supports and tall falsework.
- Crane installation and dismantling.
- Scaffold, hanging basket, curtain wall install at height.

Architect interface: design information for temporary works loads; do not approve contractor safety designs unless contractually appointed.

---

## 4. Regulatory Liaison

- 安全监督登记 with 住建部门.
- Stop-work orders and rectification notices—document and escalate.
- Align with `cn-site-supervision` for design-related safety interfaces.

---

## 5. Accident Investigation

- Preserve scene; notify per statutory timelines.
- Fact log: time, location, persons, equipment, weather.
- Do not admit liability—route legal/insurance per firm protocol.

---

## 6. Site Inspections

- Scheduled safety walks with contractor and监理.
- Photographic evidence for non-conformances.
- Close-out verification before next trade mobilisation.

---

## 7. Interfaces

| Interface | Skill |
|-----------|-------|
| Site establishment PCI | `cn-site-establishment` |
| Design supervision | `cn-site-supervision` |
| Programme sequencing | `cn-construction-programme` |
| PM reporting | `cn-project-management` |

---

## 8. Output Checklist

- Hazard register or inspection report.
- 危大工程清单 with status of专项方案.
- Open regulatory notices tracked.
- Interface actions to contractor/监理.
- Fire-design boundary disclaimer where query mixes topics.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site safety / 危大工程 | `cn-construction-health-safety` | `cn-fire-life-safety` |
| Fire egress design | `cn-construction-health-safety` | `cn-fire-life-safety` |
| Site supervision | `cn-construction-health-safety` | `cn-site-supervision` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
