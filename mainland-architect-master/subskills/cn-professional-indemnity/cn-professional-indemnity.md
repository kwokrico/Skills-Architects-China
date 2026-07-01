---
name: cn-professional-indemnity
description: Activate for professional indemnity (PI) insurance and liability control strategy in Mainland China projects, including PI limit sizing, limitation of liability clauses, and third-party reliance controls.
user-invocable: true
disable-model-invocation: true
---

# Mainland Professional Indemnity
Guidance for architect-side PI risk management, focused on insurance adequacy, contractual liability caps, and third-party reliance risk in Mainland project delivery.

---

## 1. Core Position
- Treat PI insurance, limitation wording, and duty-of-care letters as one risk system.
- Align contract risk with available PI cover; avoid taking contractual liability that exceeds insurable risk.
- Keep language precise: who can rely, what services are covered, and where the liability boundary sits.

---

## 2. PI Insurance for High-Rise Projects
High-rise and mixed-use towers usually carry elevated exposure because of:
- multi-party interfaces and long design chains,
- high consequence of design error,
- phased handovers and tenant fit-out dependencies.

Practical considerations:
1. Confirm required PI limits in appointment, consultancy schedule, and client-side tender conditions.
2. Check whether the required limit is per-claim or in the aggregate for the policy period.
3. Verify excess/deductible level and who bears it contractually.
4. Confirm policy retroactive date and run-off requirements after project completion.

---

## 3. Understanding Limit of Liability Clauses
Purpose: cap contractual exposure to a defined maximum.

Common cap bases:
- fixed sum,
- linked to fee multiple,
- linked to PI policy limit.

Review checklist:
- Is the cap clearly stated as aggregate liability or per claim?
- Are key heads of claim excluded (for example, consequential or indirect loss)?
- Does the clause preserve statutory non-excludable obligations?
- Is there a mismatch between contract cap and insurance terms?

Preferred risk alignment:
- cap amount should be commercially realistic and insurable,
- wording should avoid open-ended liability or uncapped third-party exposure.

---

## 4. Duty of Care Letters
Purpose: provide limited reliance rights to a third party (commonly funder, purchaser, or tenant) without broadening risk beyond control.

Key controls:
1. Identify the exact beneficiary; avoid broad class reliance.
2. Limit scope to named services and specific project documents.
3. Include liability cap and exclusions consistent with the main appointment.
4. Restrict assignment rights unless expressly agreed.
5. Avoid creating fitness-for-purpose obligations; maintain reasonable skill and care standard.

---

## 5. Risk Coordination Workflow
When asked to advise on PI and contract risk:
1. Extract contract liability provisions (cap, exclusions, third-party rights, survival period).
2. Compare against PI policy structure (limit, basis, deductible, run-off).
3. Flag mismatches and propose aligned wording options.
4. Confirm whether duty-of-care letters are required and define permitted form.

---

## 6. Red Flags
- Contract cap higher than PI limit with no commercial rationale.
- "Unlimited liability" wording hidden in bespoke amendments.
- Duty-of-care letter allowing unrestricted onward reliance.
- Third-party reliance for documents outside agreed scope.
- Long survival periods without matching run-off insurance.

---

## 7. Practical Output Checklist
- PI limit requirement captured and policy basis verified.
- Liability cap basis and amount clearly defined.
- Exclusion language and third-party rights reviewed.
- Duty-of-care template aligned with main appointment.
- Residual uninsured risk identified for commercial decision.

---

## 8. Required Inputs (ask if missing)

- Delivery mode (traditional vs EPC) and role scope boundary
- Required PI limits in tender/appointment and whether per-claim vs aggregate
- Survival period / run-off requirements
- Any required third-party reliance letters (funder/purchaser/tenant)

---

*Project teams should align this guidance with the executed appointment terms, insurance broker advice, and project-specific procurement requirements.*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| PI insurance and liability | `cn-professional-indemnity` | `cn-tender-contract-administration` |
| Contract legal interpretation | `cn-professional-indemnity` | `— (halt; legal counsel)` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
