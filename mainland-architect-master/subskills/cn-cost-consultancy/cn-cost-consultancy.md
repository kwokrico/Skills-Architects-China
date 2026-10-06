---
name: cn-cost-consultancy
description: Mainland cost-consultancy scope for architects working with quantity surveyors, covering cost plans, bills, tender pricing, valuations, and final account interfaces.
user-invocable: true
disable-model-invocation: true
---

# Mainland Cost Consultancy

Architect interface to cost planning and quantity surveying. The cost consultant measures and values. The architect defines scope and specification. Certification of payment follows the contract (`cn-tender-contract-administration`).

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Cost plan, 清单, 招标控制价, valuation, 结算 | `cn-cost-consultancy` | `cn-tender-contract-administration` |
| Whether a variation may be instructed | `cn-cost-consultancy` | `cn-tender-contract-administration` |
| Design-fee invoices | `cn-cost-consultancy` | `cn-fee-proposal-strategy` |

## 1. Scope and Core Position

- Do not invent unit rates or a project budget.
- Do not assert that a figure complies with GB 50500. Name the measurement rules in the contract and the edition the cost consultant is using.
- Separate 投资估算, 设计概算, 施工图预算, 招标控制价, 合同价, and 竣工结算. They are different documents.

## 2. Feasibility, Benchmarking, and Budget

### 2.1 Feasibility

Inputs: site area, target 计容面积, use mix, quality level, city, and inclusions (facade, fit-out, external works, fees, land). Missing land or fit-out scope must be stated.

### 2.2 Benchmarking

Use the client's comparable projects in the same city and year. Adjust for facade system, basement ratio, and prefabrication. A national cost index without a date is not a benchmark.

### 2.3 Project budget

Record inclusions, exclusions, contingency, and the price date. The architect does not "approve" the budget. The architect states whether the design still matches the basis.

## 3. Design-Stage Cost Control

### 3.1 Cost-plan mapping

| Design stage | Cost document | Architect input |
|--------------|---------------|-----------------|
| 方案 | 估算 | Area schedule, system options |
| 初步设计 | 概算 | Outline specification, structural and MEP strategy |
| 施工图 | 预算 / 招标控制价 | Frozen revision, specification, provisional items |
| Tender | 合同价 | Query answers, addenda |
| Construction | 变更估价 / 结算 | Change log, revised details |

### 3.2 Design-to-budget review

When the cost plan exceeds the budget, offer design options (area, specification, programme). Do not silently delete code-required or 控规-required scope to meet a number.

### 3.3 Regulatory cost checks

Flag cost of fire, access, energy, and prefabrication requirements as scope, not as optional VE, once they are mandatory for the project.

## 4. Risk and Value Management

### 4.1 Cost risk register

Ground conditions, 审图 change, currency of imported products, provisional sums, neighbour protection, and utility diversions. Each risk has an owner and a cost range or the words "not priced".

### 4.2 Value management

Run VM before 施工图 freeze. Record options that fail mandatory code or planning conditions as rejected. VM is not a variation after contract unless the client instructs it.

## 5. Cost Plans, Cash Flow, and Bills

### 5.1 Cost-plan structure

Follow the cost consultant's elemental or trade structure. The architect checks that each element matches a specification section.

### 5.2 Cash flow

Construction cash flow is the cost consultant's forecast against the programme. Design-fee cash flow is `cn-cashflow-debt-recovery`. Do not mix them.

### 5.3 Bills of quantities

Architect checks: coverage of drawn scope, correct specification references, and items marked provisional where design is incomplete. The cost consultant owns quantities.

### 5.4 Tender pricing documents

Identify the pricing document (priced bill, schedule of rates, or EPC lump sum against employer's requirements). Ambiguity in what is included becomes a claim.

## 6. Tender Issue, Evaluation, and Award

### 6.1 Tender issue

One drawing revision, one specification revision, one bill revision. Addenda renumber all three.

### 6.2 Evaluation

Cost consultant leads price, arithmetic, and unbalanced bids. Architect leads technical compliance and unacceptable substitutions.

### 6.3 Post-tender

Agreed tender amendments become contract documents. A discount letter that excludes scope is a scope change, not a saving, until the drawings change.

## 7. Post-Contract

### 7.1 Variation estimates

The architect describes the change. The cost consultant prices it. Work proceeds only on the contract's instruction rule.

### 7.2 Interim valuations

Comment on whether claimed work matches the drawings and approved changes. Do not certify an amount unless the appointment says so.

### 7.3 Claims support

Provide factual design and instruction history. Quantum and delay analysis sit with the cost and programme consultants. Legal liability is a halt.

### 7.4 Cost reports

Ask the cost consultant for a monthly report: contract sum, instructed changes, pending changes, claims, and forecast final account. The architect adds design-change causes.

### 7.5 Final account

Inputs: as-built status, change log, provisional-sum outcomes, and claims settled or reserved. The architect does not sign the final account as a cost certificate unless appointed.

## 8. Interfaces

| Role | Boundary |
|------|----------|
| `cn-tender-contract-administration` | Instructions, certificates, claim procedure |
| `cn-procurement-strategy` | Route and contract family |
| `cn-deliverables-workstages` | Which drawing revision is the measurement basis |
| `cn-project-management` | Budget reporting to the client |

## 9. Output Checklist

- Document type named (估算 / 概算 / 预算 / 控制价 / 结算).
- Drawing revision cited.
- Rates not invented.
- Measurement standard named or marked unknown.
- Mandatory scope not removed to hit a budget.
- Payment amounts left to the appointed valuer.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [Construction_Quality_Regulation_CS.md](../../../cn_s_reference/MOHURD/summaries/Construction_Quality_Regulation_CS.md) — quality-regulation digest
