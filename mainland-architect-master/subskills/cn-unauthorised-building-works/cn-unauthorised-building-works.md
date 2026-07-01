---
name: cn-unauthorised-building-works
description: Activate for Mainland non-compliant works (违建/违法建设/未批先建/擅自变更) triage, rectification strategy, authority risk, and transaction/acceptance impacts with city variance.
user-invocable: true
disable-model-invocation: true
---

# Mainland Non-compliant Works (违建/未批先建/擅自变更)
Supports assessment and handling of non-compliant works in Mainland China practice, from initial identification through enforcement response, compliance strategy, and transaction/acceptance impacts.

---

## 1. Scope and Practical Definition
In this context, non-compliant works generally include:
- Works without required approvals/permits (未批先建)
- Works deviating materially from approved/accepted drawings (擅自变更)
- Works violating planning red lines, setbacks, height, FAR, or fire/structural mandatory items
- Unauthorized enclosures/additions affecting safety or planning indicators

Core risk areas:
- Structural safety and loading changes.
- Means of escape and fire safety impairment.
- Drainage and waterproofing defects.
- Encroachment beyond land red line / construction control lines.
- Transaction and financing risk (sale, mortgage, due diligence).

---

## 2. Identification and Initial Screening
Run an early triage before advising on rectification:
1. **Document check:** compare as-built condition with approved plans, latest consent records, and occupation status.
2. **Type check:** identify whether works are likely major works, minor works, exempted works, or clearly non-compliant.
3. **Safety check:** flag immediate life safety concerns (escape routes, structural alteration, fire compartment breaches).
4. **Evidence pack:** collect photos, dimensions, dates (if known), ownership responsibility boundaries, and affected units/common areas.

Typical examples:
- Enclosure of balconies or utility platforms.
- Addition of rooftop structures/canopies.
- Unauthorized internal alteration affecting escape layout.
- Unauthorized drainage diversion or discharge arrangement.

---

## 3. Authority Actions and Response
When authority issues enforcement directions, treat deadlines and scope strictly.

Good practice response path:
1. Parse the order wording into a precise scope matrix (what must be removed, rectified, certified, and when).
2. Confirm party responsibilities (owners' corporation, individual owners, manager, AP/RSE/RGBC as applicable).
3. Sequence emergency stabilization first if safety risk exists.
4. Submit required proposals, method statements, and completion evidence in the expected format.

Do not assume partial rectification satisfies the order; closure requires objective compliance evidence accepted by the authority.

---

## 4. Enforcement and Escalation Risk
Escalation can include prosecution, default works, and transaction restrictions if orders remain outstanding.

Track enforcement exposure via:
- Outstanding order register.
- Deadline calendar with responsible owner.
- Dependencies (access, contractor appointment, statutory submission timing).
- Status evidence (submitted, queried, accepted, completed).

Aging unresolved UBW often increases legal and commercial risk even where immediate physical danger is low.

---

## 5. Rectification and Regularization Strategies
Choose strategy by risk and legal feasibility:
1. **Removal and reinstatement** to approved condition.
2. **Alter-and-comply** redesign that can be regularized with proper submissions.
3. **Small works route** where applicable and legally valid for the specific scope (city-specific).
4. **Staged compliance** for complex buildings where safety-critical items are closed first.

Decision factors:
- Safety criticality.
- Submission complexity and lead time.
- Access constraints in occupied premises.
- Cost vs transaction urgency.

If regularization is uncertain, provide a dual-track plan: immediate risk reduction plus fallback removal strategy.

---

## 6. Implications for Sale, OP, and Consent
Non-compliance may materially affect transaction, lending, and acceptance/permit approvals.

- **Sale/purchase:** outstanding UBW and orders can trigger price adjustment, retention, or failed transactions.
- **Mortgage/financing:** lenders often require UBW risk disclosure and may refuse lending on unresolved serious issues.
- **Acceptance stage:** unresolved non-compliance can delay `消防验收` / `竣工联合验收` / filing.
- **New permits:** existing non-compliance can complicate new approvals and sequencing.

Always include a disclosure-ready summary for legal and transaction teams: issue list, statutory status, proposed remedy, timeline, and residual risk.

---

## 7. Working Protocol for Advising Teams
Use this standard structure in advice notes:
1. **Facts established** (location, type, extent, records checked).
2. **Regulatory position** (suspected breach category and order status).
3. **Risk rating** (life safety, legal, commercial).
4. **Recommended path** (rectify/regularize/remove with timeline).
5. **Dependencies** (access, ownership alignment, consultants, 规自局/城管执法 interaction).
6. **Decision points** for owner/client sign-off.

---

## 8. Required Inputs (ask if missing)

- City and district
- Land status and red-line constraints (用地红线/建筑控制线)
- Current approvals held (planning permit / construction permit / drawing review result)
- As-built evidence (photos, measurements) and key deviations
- Any authority notices/orders and deadlines
- Target objective (acceptance closeout vs transaction vs re-permitting)

---

*Reference anchors: city-level enforcement rules and PRC permitting/acceptance workflows; always validate local implementation details.*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 违建认定与整改 | `cn-unauthorised-building-works` | `cn-alterations-additions` |
| Planning regularization | `cn-unauthorised-building-works` | `cn-spatial-planning` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
