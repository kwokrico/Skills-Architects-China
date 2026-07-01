---
name: cn-telecom-coordination
description: Activate for Mainland licensed telecommunications works—三大运营商管线保护, fibre/cable diversion, excavation near plant, and municipal coordination during site establishment and construction.
user-invocable: true
disable-model-invocation: true
---

# Mainland Telecom Coordination
Licensed telecom and cable protection during demolition, excavation, and construction. Do not conflate with general municipal water/power diversion.

Guide: [cn-telecom-coordination-guide.md](../../references/cn-telecom-coordination-guide.md).

---

## 1. Scope (Do Not Conflate)

| Works | Skill |
|-------|-------|
| 移动/联通/电信 通信管线 | This skill |
| 给水排水燃气电力 | `cn-building-services` / utility liaison in `cn-site-establishment` |
| 弱电智能化设计 | `cn-building-services` |

---

## 2. When Triggered

- Excavation within protection zones of existing telecom plant.
- Basement or trench crossing carrier routes.
- Tower crane or pile works near overhead/underground cables.
- Demolition of buildings with active carrier equipment.

---

## 3. Licensed Works Framework

- Carriers (三大运营商及广电等) require approved contractors for plant touch.
- Protection standards: 查明管线、签订保护协议、专人监护.
- **Hard stop:** Do not advise unlicensed excavation near active plant.

---

## 4. Site Establishment Interface

- Survey and mark telecom routes before bulk earthworks.
- Sequence diversion before deep excavation.
- Link to `cn-site-establishment` PCI pack.

---

## 5. Construction Coordination

- Weekly coordination when working within 1–3 m of marked plant (project-specific buffer per carrier).
- As-built of new routes before backfill.
- Record carrier sign-off.

---

## 6. Risk Hotspots

- Incomplete as-built of legacy routes.
- Parallel excavation by multiple trades.
- Night works without carrier standby.
- Damage liability and service outage claims.

---

## 7. Output Checklist

- Telecom protection plan.
- Undertaker liaison log.
- Diversion sequencing note.
- Carrier approval status.
- Cross-reference site establishment pack.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 三大运营商 / 管线迁改 | `cn-telecom-coordination` | `cn-site-establishment` |
| General mobilisation | `cn-telecom-coordination` | `cn-site-establishment` |
| MEP design | `cn-telecom-coordination` | `cn-building-services` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-telecom-coordination-guide.md](../../references/cn-telecom-coordination-guide.md) — coordination guide
