---
name: cn-procurement-strategy
description: Activate for Mainland procurement route selection—传统施工招标, EPC/工程总承包, 设计施工总承包, 招标投标法 alignment, contract form mapping, risk allocation, and 不可抗力/极端天气 EOT treatment by route.
user-invocable: true
disable-model-invocation: true
---

# Mainland Procurement Strategy
Selects delivery and contract route before tender issue. Post-award administration routes to `cn-tender-contract-administration`.

Deep comparison: [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md). Weather/EOT: [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md).

---

## 1. Route Decision Guide

| Route | When it fits | Architect risk profile |
|-------|--------------|------------------------|
| 传统施工招标 (设计招标 + 施工招标) | Mature design, competitive market, client wants design control | Design liability clear; longer programme |
| 施工总承包 | Single contractor, design substantially complete | Interface at tender drawings |
| 工程总承包 (EPC) | Client wants single point; performance spec possible | Reduced post-award design role if not EPC designer |
| 设计施工总承包 | Integrated delivery, fast-track | Shared design liability—scope clarity critical |

**Hard stop:** Halt route recommendation if client objectives, risk appetite, and design maturity are unknown.

---

## 2. Comparison Matrix (summary)

| Factor | 传统 | EPC/总承包 |
|--------|------|------------|
| Design control | Client / 设计院 | Contractor-led or dual |
| Programme | Sequential | Compressed potential |
| Price certainty at tender | Higher (defined scope) | Depends on spec quality |
| Variation risk | Client-driven changes | Performance gaps |
| 审图责任 | 设计院 | Must be contractually assigned |

Full matrix: [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md).

---

## 3. Contract Form Map

- Private: 《建设工程施工合同（示范文本）》+ 专用条款.
- Public / 国有资金: 《招标投标法》+ 必须招标范围规定.
- EPC: 示范文本 EPC 专章或项目定制; align with 住建部工程总承包管理办法.
- Collaborative / target cost: growing on mega-projects; pain/gain in special conditions.

Output template: [tender-route-recommendation.md](../../references/templates/tender-route-recommendation.md).

---

## 4. Typhoon / Adverse Weather and EOT

- Contract route affects who bears weather delay risk and notice obligations.
- 不可抗力 clauses: define events, notice period, evidence (气象记录).
- Do not conflate statutory force majeure with commercial EOT entitlements.

See [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md).

---

## 5. Programme and Approval Interface

- EPC fast-track must not skip 施工图审查 / 消防设计审查 where mandatory.
- Align procurement milestones with `cn-consent-scheduling`.
- Early packages (long-lead façade, MEP plant) vs single-stage tender.

---

## 6. Stage-Gate Outputs

| Gate | Output |
|------|--------|
| Feasibility | Route shortlist + risk table |
| Scheme freeze | Recommended route + contract strategy note |
| Pre-tender | Route decision memo + tender strategy |

---

## 7. Output Checklist

- Route recommendation with assumptions.
- Risk allocation table (design, ground, authority, weather).
- Contract form pointer.
- Weather/EOT clause pointers.
- Interface to `cn-tender-contract-administration` for tender execution.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Procurement route / EPC vs traditional | `cn-procurement-strategy` | `cn-tender-contract-administration` |
| Tender / CA duties | `cn-procurement-strategy` | `cn-tender-contract-administration` |
| Cost plan | `cn-procurement-strategy` | `cn-cost-consultancy` |
| Approval programme | `cn-procurement-strategy` | `cn-consent-scheduling` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md) — route comparison
* [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md) — weather and EOT
