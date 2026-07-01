---
name: cn-site-establishment
description: Activate for Mainland pre-construction mobilisation—三通一平, 占道施工/围蔽, 临时用地, utility liaison, neighbour interfaces, 开工前条件检查, and PCI-style readiness before main works.
user-invocable: true
disable-model-invocation: true
---

# Mainland Site Establishment
Mobilisation between 施工许可证 and main construction start. Statutory approval sequencing: `cn-consent-scheduling`. Traffic and telecom depth: `cn-traffic-coordination`, `cn-telecom-coordination`.

Checklist: [cn-site-establishment-checklist.md](../../references/cn-site-establishment-checklist.md).

---

## 1. Scope and Position

- Site establishment is **not** main construction—it is readiness for safe, lawful start.
- **Hard stop:** Valid 施工许可证 and 开工前条件检查 (or local equivalent) before main works.
- Coordinate with contractor,监理, and municipal interfaces.

---

## 2. Pre-Construction Readiness Gate

Confirm:

1. 施工许可证 issued and posted.
2. 审图合格书 and baseline FOR CONSTRUCTION drawing set frozen.
3. 质安监 registration complete.
4. 三通一平 and temporary works designed.
5. Utility / 管线迁改 programmes agreed.
6. 占道 / 围蔽 approvals where applicable.
7. Neighbour and traffic interfaces briefed.

---

## 3. Hoarding and 占道施工

- 围蔽方案: height, stability, lighting, signage per municipal code.
- 占道施工许可: lane closure, pedestrian diversion, 交警意见.
- Link hoarding layout to `cn-traffic-coordination` TMP/TIA outputs.

---

## 4. Temporary Works

- Site offices, cranes, material stacks, excavation support.
- Design responsibility per contract (contractor vs designer).
- Stormwater and dust control measures.

---

## 5. Utility Liaison

- Power, water, sewer, gas connection or diversion.
- **Telecom / 三大运营商** → `cn-telecom-coordination`.
- Record undertaker contacts and protection zones.

---

## 6. Authority and Neighbour Interfaces

- Pre-start meeting with 住建、交警、街道 (as required).
- Noise and dust notification to neighbours.
- Night-work permits if applicable.

---

## 7. Programme Hooks

- Mobilisation duration in master programme (`cn-construction-programme`).
- Long-lead temporary power and tower crane erection on critical path.
- Do not promise uniform municipal response times—use `city_context`.

---

## 8. Output Checklist

- Mobilisation checklist complete.
- Hoarding / 占道 permit status.
- Utility diversion schedule.
- PCI / 开工条件自检表 index.
- Cross-reference to consent and traffic/telecom skills.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Mobilisation / 三通一平 / 占道 | `cn-site-establishment` | `cn-consent-scheduling` |
| 施工许可证 timeline | `cn-site-establishment` | `cn-consent-scheduling` |
| Traffic TMP | `cn-site-establishment` | `cn-traffic-coordination` |
| Telecom diversion | `cn-site-establishment` | `cn-telecom-coordination` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-site-establishment-checklist.md](../../references/cn-site-establishment-checklist.md) — mobilisation checklist
