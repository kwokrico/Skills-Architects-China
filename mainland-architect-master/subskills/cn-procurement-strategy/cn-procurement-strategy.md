---
name: cn-procurement-strategy
description: Selects a Mainland procurement route and contract family, including traditional tender, EPC, and how weather delay is treated. Tender administration stays in cn-tender-contract-administration.
user-invocable: true
disable-model-invocation: true
---

# Mainland Procurement Strategy

Chooses the route and the risk split. Executing the tender and administering changes stay in `cn-tender-contract-administration`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 传统 vs EPC, risk allocation, contract family | `cn-procurement-strategy` | `cn-tender-contract-administration` |
| Tender queries and payment certificates | `cn-procurement-strategy` | `cn-tender-contract-administration` |
| Cost-plan content | `cn-procurement-strategy` | `cn-cost-consultancy` |

## Halt Criteria

- Do not recommend a route when the client has not stated time, cost certainty, design control, and whether public tendering law applies.
- Do not draft particular conditions that transfer statutory design duty.
- Weather delay: identify the contract clause. Do not apply a Hong Kong typhoon signal.

## 1. Route Decision Guide

| Client priority | Route that often fits | Main risk left with the client |
|-----------------|----------------------|--------------------------------|
| Design control, competitive construction price | 传统: design to 施工图, then construction tender | Design coordination and 审图 before price certainty |
| Single point, faster overlap of design and construction | EPC / 工程总承包 | Employer's requirements quality; changes after freeze are expensive |
| Early contractor input, design still with the design institute | 设计施工总承包 or a managed package split | Interface between packages |
| Public money or mandated tender | Route required by the tendering law and local rules | Process compliance |

Ask which priority dominates before recommending one route.

## 2. Summary Comparison

| Topic | 传统施工招标 | EPC / 工程总承包 |
|-------|----------------|------------------|
| Who develops design after award | Design institute under client | Contractor's design team within employer's requirements |
| Price certainty | After 施工图 tender | Earlier, but scope gaps become variations |
| 审图 responsibility | Client's design institute | Must be assigned in the contract; statutory duty is not waived |
| Change control | Drawing change and valuation | Change versus design development |
| Client control of products | High | Lower unless specified |

Full matrix: [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md).

## 3. Contract Form Map

| Route | Form to identify | Note |
|-------|------------------|------|
| Traditional building | 建设工程施工合同示范文本 (confirm the executed year; GF-2017-0201 is the commonly cited 2017 model) | Architect administers only if appointed |
| EPC | 工程总承包合同示范文本 (confirm the executed edition) | Employer's requirements are the scope baseline |
| Public procurement | Government or state-owned rules plus the construction contract | Extra approvals before instruction |
| International | FIDIC or NEC only if executed | Do not translate those procedures into 示范文本 steps |

## 4. Weather and Force Majeure

| Event | What to check | What not to do |
|-------|---------------|----------------|
| Typhoon, rainstorm, heat | Contract definition, local warning threshold, and whether the activity was on the critical path | Import Hong Kong T8/T10 rules |
| 不可抗力 | Notice, mitigation, and which party bears time and money | Assume both time and money automatically |
| Concurrent delay | Contract and facts | Give a legal conclusion |

Detail: [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md). If the user is already the contract administrator, continue in `cn-tender-contract-administration`.

## 5. Programme and Permit Interface

- Traditional: 审图合格 is normally a predecessor of a firm construction price and of 施工许可.
- EPC: the contract must say who submits 审图 and who carries comment-cycle delay.
- Long-lead orders before 审图合格 are a client risk. Record it.
- Prefabrication factories need a frozen module. That freeze is a procurement decision (`cn-mic-dfma`).

## 6. Stage-Gate Outputs

| Gate | Procurement output |
|------|--------------------|
| End of 方案 | Route recommendation and risk table |
| End of 初设 | Contract family, packaging, and employer's-requirements outline if EPC |
| Before tender | Tender-route sheet `references/templates/tender-route-recommendation.md` |
| Award | Contract document list handed to the administrator |

## 7. Cross-References

- Tender mechanics: `cn-tender-contract-administration`.
- Cost: `cn-cost-consultancy`.
- Programme: `cn-construction-programme` and `cn-project-management`.
- Permits: `cn-consent-scheduling`.

## 8. How to Use the References

1. Fill the route template with the client's priorities.
2. Name the contract family or write "not selected".
3. Point weather questions at the weather note and the contract clause.
4. Stop before particular-condition drafting.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md) — route matrix
* [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md) — weather delay
* [tender-route-recommendation.md](../../references/templates/tender-route-recommendation.md) — output shell
* [Tendering_and_Bidding_Law_CS.md](../../../cn_s_reference/MOHURD/summaries/Tendering_and_Bidding_Law_CS.md) — bidding-law digest
