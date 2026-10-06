---
name: cn-tender-contract-administration
description: Activate for Mainland tender and contract administration strategy, EPC/traditional procurement alignment, variation control, progress payment governance, and dispute-risk reduction.
user-invocable: true
disable-model-invocation: true
---

# Mainland Tender and Contract Administration

Covers pre-tender preparation, contract identification, and post-award administration for Mainland projects. Procurement-route selection belongs to `cn-procurement-strategy`. Measurement and cost plans belong to `cn-cost-consultancy`.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Tender set, 示范文本, 变更/签证/索赔, 进度款, 竣工结算 | `cn-tender-contract-administration` | `cn-procurement-strategy` |
| Which route (传统 vs EPC) | `cn-tender-contract-administration` | `cn-procurement-strategy` |
| BoQ measurement rules | `cn-tender-contract-administration` | `cn-cost-consultancy` |
| 缺陷责任期 snagging procedure | `cn-tender-contract-administration` | `cn-practical-completion-snagging` |

## 1. Scope and Role

- Treat tender and contract administration as commercial-risk control, not as legal advice.
- Coordinate owner, design institute, cost consultant, legal counsel, supervisor (监理), and contractor.
- Halt if the user asks for a damages opinion, liability-cap interpretation, or a certificate the appointment does not authorise.
- Name the contract family before giving a procedure. Do not import Hong Kong SFBC or NEC certificate sequences unless the contract is actually that form.

## 2. Pre-Tender Documentation

Typical tender set:

1. Drawings and specifications at the agreed tender stage (often 施工图 after 审图, or a defined EPC employer's requirements set).
2. Bills of quantities or a schedule of rates prepared by the cost consultant, with architect coordination comments closed.
3. Employer's requirements, preliminaries, and particular conditions.
4. Form of tender, return schedules, and tender instructions.
5. Proposed contract form and appendices (price, duration, defect-liability period, insurance, advance payment).

Quality checks before issue:

- Drawing revision matches the 审图合格 version, or the pack is explicitly marked "for tender, not for construction".
- Interfaces (civil, facade, MEP, lift, fit-out) have a responsibility matrix.
- Provisional sums and prime-cost sums are listed with who designs and who procures.
- Weather and 不可抗力 wording points to `cn-procurement-strategy`, not a copied typhoon table.

## 3. BoQ Coordination (Architect Interface)

| Architect does | Cost consultant does |
|----------------|----------------------|
| Confirm scope, specification, and drawing basis | Measure quantities and write item descriptions |
| Flag incomplete design and provisional items | Price risk and produce 招标控制价 where appointed |
| Answer technical tender queries | Evaluate arithmetic and unbalanced rates |
| Record design changes that affect quantities | Value variations against the contract rates |

Do not sign a bill as if it were an architectural drawing. Do not invent GB 50500 measurement rules; cite the contract's measurement standard and ask for the edition.

## 4. Contract Form Strategy

Identify the form before administering it.

| Family | Typical use | Architect watch-points |
|--------|-------------|------------------------|
| 建设工程施工合同示范文本 (GF-2017-0201 is the commonly cited 2017 construction model; confirm the executed edition) | Traditional design-bid-build | Variation instruction path, payment milestones, defect liability, dispute step |
| EPC / 工程总承包合同示范文本 | Single point for design and construction | Employer's requirements freeze, design development limits, change versus design development |
| 政府采购 / 国有资金施工合同 | Public clients | Tendering law process; extra approval before instruction |
| FIDIC or NEC (only if executed) | International or pilot projects | Use that form's clause map; do not translate it into 示范文本 steps |

## 5. Tender Queries, Addenda, and Assessment

1. Log queries with date, author, and whether the answer changes price or time.
2. Issue addenda to all tenderers. Do not give one tenderer a private clarification that changes scope.
3. Assessment criteria: compliance with employer's requirements, exclusions, programme, key subcontractors, and unbalanced rates (cost consultant leads the commercial score).
4. Architect technical report: deviations from drawings, unacceptable product substitutions, and missing coordinated services.
5. Award recommendation is the client's decision. Record the basis. Do not declare a tender "compliant with code".

## 6. Post-Contract Architect Duties

Only the duties in the appointment and the contract. Typical design-institute or employer's-consultant duties:

- Issue clarified drawings and respond to RFIs within the agreed period.
- Attend site meetings; record decisions that change the drawings.
- Review shop drawings and material samples for design intent, not for construction means and methods.
- Notify the contract administrator or employer when a site condition differs from the tender information.
- Keep a change log that the cost consultant can value.

监理 inspects construction quality under its own appointment. Do not merge 设计代表 and 总监 roles.

## 7. Variations and Change Control

| Instrument | Typical meaning | Control |
|------------|-----------------|---------|
| 设计变更 | Change to issued design | Numbered instruction, drawing revision, reason, cost/time flag |
| 工程签证 | Site fact confirmed for later valuation | Facts, quantities, date, photos; not a blank approval of price |
| 洽商 | Negotiated technical agreement | Convert into a formal instruction before work proceeds |
| 索赔 | Time or money claim | Notice periods in the contract; acknowledge receipt; do not admit liability |

Rules:

- No oral instruction. Confirm in writing the same day.
- Separate "design development inside the employer's requirements" from "employer change" on EPC jobs.
- Stop work that would breach 审图 scope until a review path is identified (`cn-construction-documentation`).

## 8. Certification and Payment Interfaces

| Topic | Who usually acts | Architect limit |
|-------|------------------|-----------------|
| 进度款 / interim valuation | Cost consultant and/or 监理, per contract | Comment on work that matches drawings; do not certify money unless appointed |
| 预付款 / 扣回 | Contract appendix | Track, do not invent statutory percentages |
| 竣工结算 | Cost consultant | Supply change log and as-built design status |
| 缺陷责任期 | Contract administrator | Route snagging method to `cn-practical-completion-snagging` |
| 保修 | Statutory and contract warranty | Do not shorten statutory quality warranty by a private letter |

## 9. Practical Compliance Checklist

- Contract form and edition identified.
- Tender drawings tied to a revision register.
- Provisional and prime-cost sums listed.
- Change log opened before site start.
- Payment comments separated from payment certificates.
- Weather delay routed to the contract clause, not a Hong Kong T8 table.
- Legal damages questions halted.

## 10. Collaborative and Target-Cost Forms

Use this section only when the executed contract is NEC, a target-cost EPC, or an alliance form.

- Pain/gain and compensation events follow that contract, not GF-2017 defaults.
- Early-warning register is a project-management tool (`cn-project-management`), not a variation by itself.
- Design development after the employer's requirements baseline needs a defined change gate.

## 11. Contract Administrator Playbook

### 11.1 Role clarity

State in the first meeting: who may instruct the contractor, who may value, who may extend time, and who signs 竣工验收 documents. If the architect is not the contract administrator, say so in every instruction.

### 11.2 Client instructions

Record client instructions that change scope, quality, or programme. Flag cost and time before the contractor proceeds when the contract requires a quotation first.

### 11.3 Documents for execution

Drawings, specification, priced bill or schedule, programme, and employer's requirements must be listed in the contract. Later "latest model" is not a contract document until issued as a revision.

### 11.4 Issuing instructions

Number, date, drawing references, clause relied on, and whether the contractor must quote before starting. Copy the cost consultant and 监理.

### 11.5 Progress meetings and reports

Agenda: safety hold points, design information due, RFIs, changes, quality, look-ahead (`cn-construction-programme`), and payment status. Decisions go in the minutes the same day.

### 11.6 Site inspectors

设计代表 observes design conformance. 监理 inspects statutory quality. Neither replaces the contractor's method statements for 危大工程 (`cn-construction-health-safety`).

### 11.7 Commissioning and defects

Fire, lift, waterproofing, and envelope tests are acceptance evidence, not a reason to skip 消防验收 or 规划核实. Defect lists during the defect-liability period go to `cn-practical-completion-snagging`.

### 11.8 Claims — time and money

1. Check whether notice was given inside the contract period.
2. Separate delay (critical path) from disruption (productivity).
3. Weather and 不可抗力: identify the contract clause and the local warning threshold. Do not apply a Hong Kong signal number.
4. Acknowledge the claim. Assess time with the programme owner and money with the cost consultant.
5. Halt if the user wants a legal conclusion on concurrent delay or liquidated damages.

### 11.9 Certificate sequence (traditional private works — typical, not statutory)

| Step | Usual evidence | Do not confuse with |
|------|----------------|---------------------|
| Commencement | 施工许可证, site possession, insurances | 规划许可 |
| Interim payment | Measured work and materials on site per contract | 竣工结算 |
| Sectional or practical completion | Contract definition of completion | 消防验收 or 竣工备案 |
| Defect-liability end | Closed snag list | Statutory 保修 which may be longer |
| Final account | Agreed variations and claims | Court or arbitration award |

### 11.10 Documentation to the client

Monthly: change log, information due, claims received, and decisions needed. Do not bury a scope change inside a drawing transmittal.

### 11.11 Output checklist

- Contract family named.
- Instruction template used.
- Change versus design-development called correctly on EPC.
- Claim notice date recorded.
- Money certification only if the appointment allows it.
- Statutory acceptance path left to `cn-fire-acceptance-closeout` and `cn-op-submission-strategy`.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-procurement-routes-comparison.md](../../references/cn-procurement-routes-comparison.md) — route comparison
* [cn-adverse-weather-eot.md](../../references/cn-adverse-weather-eot.md) — weather delay by route
* [招标投标法_CS.md](../../../cn_s_reference/MOHURD/summaries/Tendering_and_Bidding_Law_CS.md) — bidding-law digest
