---
name: cn-alterations-additions
description: >
  Existing building retrofit / alterations in Mainland China. Covers scope triage, structural/fire triggers, property/management constraints, permitting/审图/acceptance impacts, and non-compliance rectification.
user-invocable: true
disable-model-invocation: true
---

# Mainland Existing Building Retrofit (既有建筑改造/装修/改扩建)
Expert guidance on modifying existing building stock in Mainland China, focusing on compliance triggers, structural safety, and fire safety baseline under national standards with city variance.

Regulatory hierarchy:
- National baseline first: `GB / GB-T / JGJ`
- Then local supplements: `DB / DGJ / DBJ` (city/province)

If city is not specified, treat guidance as national baseline pre-check and request local supplement confirmation.

---

## 1. Regulatory Pathways (Mainland framing)
Determining the compliance route is the first critical step in any retrofit project.

Typical routes:
- **Interior fit-out (non-structural)**: still must not weaken fire compartments/egress; may be governed by property/management filing.
- **Retrofit affecting structure or life safety**: treat as serious; often needs engineering design, coordinated drawings, and may trigger审图/permits.
- **Change of use / major functional change**: triggers a fresh code check and acceptance implications.
- **Extension/addition**: planning red line, FAR, height and setbacks become central; can trigger new planning approvals.

---

## 2. Structural & GFA Considerations
A retrofit must not overstress existing structure/foundations or create illegal area/indicator breaches.

### 2.1 Structural Justification
* **Loading verification:** Any increase in live loads (e.g., warehouse → retail) requires structural verification and strengthening design where needed.
* **Structural Strengthening:** Carbon fiber wrapping (FRP) or steel plate bonding must be detailed and submitted for 审图机构 / 住建局 structural review if modifying structural elements.
* **Non-compliance in affected zone:** existing illegal works inside the affected area often must be rectified before acceptance/permits can close.

### 2.2 GFA and Site Coverage
* **Building area calculation:** baseline per `GB/T 50353`; verify local supplements.
* **Planning indicators:** FAR/coverage/green ratio/height are city-defined; do not assume exemptions.

---

## 3. Fire Safety Triggers (GB 50016 baseline)
Retrofits often trigger upgrades when they materially change fire load, occupant load, compartmentation, or protected routes.

### 3.1 Egress / escape
* **Do not degrade protected routes:** partitions and doors must preserve compartment and escape logic.
* **Occupant load:** recalc occupant load assumptions and stair/exit capacity where function changes.

### 3.2 Fire resisting construction / compartments
* **Compartmentation:** new openings across fire separations must have compliant protection and fire stopping.
* **Facade risk:** material combustibility and vertical fire spread risk must be checked; avoid “decorative” changes that create major fire exposure.

---

## 4. Coordination & Management
### 4.1 Property management + common parts
* Works involving facade, structure, roof, shafts, or public interfaces usually require property/management approvals and method statements.
* Clarify boundaries (exclusive-use vs common parts) before design freeze.

### 4.2 Acceptance impacts
* Major retrofits/change of use often impacts fire acceptance and joint acceptance requirements.
* Plan for evidence governance (as-built + tests) early, not at the end.

---

## 5. Required Inputs (ask if missing)

- City and district
- Existing building type, year, current occupancy
- Retrofit scope (structure/fire compartments/facade/MEP)
- Whether change of use is involved
- Existing approvals and any acceptance constraints

---

*Baseline references: GB 50016 and GB/T 50353 as national baselines; verify local supplements and building-specific acceptance constraints.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Fit-out / alteration approvals | `cn-alterations-additions` | `cn-minor-works` |
| Unauthorized works enforcement | `cn-alterations-additions` | `cn-unauthorised-building-works` |
| Full new-build codes | `cn-alterations-additions` | `cn-building-codes` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
