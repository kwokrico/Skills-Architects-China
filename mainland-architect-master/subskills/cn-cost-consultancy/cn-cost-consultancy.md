---
name: cn-cost-consultancy
description: Activate for Mainland QS scope—feasibility, benchmarking, cost plans, GB 50500 BoQ, tender evaluation support, variations, valuations, claims support, and final account—with architect–造价 interface.
user-invocable: true
disable-model-invocation: true
---

# Mainland Cost Consultancy (QS Interface)
Architect-facing guidance on cost consultant scope, measurement rules, and design–cost coordination. Certification and formal valuation sign-off remain with appointed 造价咨询 / CA per contract.

---

## 1. Scope

- Feasibility and benchmarking (单方造价、业态对比).
- Design-stage cost control and cash-flow forecasting.
- Risk allowance and VM support with `cn-project-management`.
- Cost plans by stage (估算、概算、预算).
- BoQ per **GB 50500** 工程量清单计价规范.
- Tender pricing review and comparison reports.
- Post-contract variations, interim valuations, claims support, final account.

**Hard stop:** Do not issue formal payment certificates or binding valuation—cross-check `cn-tender-contract-administration` and appointed QS.

---

## 2. Feasibility and Benchmarking

- Confirm measurement basis (建筑面积 GB/T 50353, 套内, 可租).
- Use local cost databases with city and date stamp.
- Separate 建安工程费、工程建设其他费、预备费.
- Flag indicator risk if FAR or standard floor efficiency shifts.

---

## 3. Design-Stage Cost Control

| Stage | Typical deliverable | Architect interface |
|-------|---------------------|---------------------|
| 方案 | 投资估算 | 面积表、装修标准、系统等级 |
| 初设 | 概算 | 技术路线、主要材料档次 |
| 施工图 | 预算 / 招标控制价 | 规格一致性、界面完整 |

---

## 4. BoQ Coordination

- QS leads measurement; architect validates technical scope and descriptions.
- One design intent language across drawings, specs, and BoQ.
- Record clarifications in auditable issue log.
- Interface items (幕墙、人防、装配式) explicitly split.

---

## 5. Tender Evaluation

- Arithmetic check; scope gaps and qualifications.
- Abnormal low bid flags per 招标投标法 practice.
- Technical–commercial matrix support (architect technical, QS commercial).

---

## 6. Post-Contract

- Variation estimate: scope + drawing reference + time impact note.
- Interim valuation: completed work vs BoQ lines.
- Claims: extension only with programme records; quantum QS-led.
- Final account: defect retention, provisional sums close-out.

---

## 7. Interfaces

| Party | Interface |
|-------|-----------|
| 设计院 | Scope, specs,变更图纸 |
| 造价咨询 | Measurement, pricing, reports |
| 监理 / 业主 | Progress, certification chain |
| CA | Certificates, EOT notices |

---

## 8. Output Checklist

- Cost plan stage and basis stated.
- Measurement rules referenced (GB 50500 / 地方补充).
- Variance vs budget with drivers.
- Open scope gaps listed.
- Certification boundary disclaimer where applicable.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Cost plan / BoQ / 概算预算 | `cn-cost-consultancy` | `cn-tender-contract-administration` |
| Procurement route | `cn-cost-consultancy` | `cn-procurement-strategy` |
| Fee proposal | `cn-cost-consultancy` | `cn-fee-proposal-strategy` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
