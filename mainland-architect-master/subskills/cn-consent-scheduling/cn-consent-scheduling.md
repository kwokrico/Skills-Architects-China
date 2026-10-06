---
name: cn-consent-scheduling
description: Builds Mainland approval programmes from scheme design through construction permit, including review cycles, resubmission, and what must not be confused with statutory acceptance.
user-invocable: true
disable-model-invocation: true
---

# Mainland Approval Scheduling

Programmes the path from 方案 to 施工许可证. It does not certify that a city will meet a duration. City rules differ. Ask for the city and the current stage before giving a timeline.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Critical path of permits and 审图 | `cn-consent-scheduling` | `cn-op-submission-strategy` |
| Mobilisation after the permit | `cn-consent-scheduling` | `cn-site-establishment` |
| Code interpretation | `cn-consent-scheduling` | `cn-building-codes` |

## 1. Statutory Sequence (National Pattern)

| Step | Typical authority | Output that unlocks the next step |
|------|-------------------|-------------------------------------|
| Land grant or allocation | 自然资源 | 出让合同 / 划拨决定 |
| 方案 and planning permit | 规自局 | 建设工程规划许可证 (and 用地规划许可 if still separate) |
| 初步设计 | Client / industry authority where required | Approved preliminary design or client freeze |
| 施工图 + 审图 | 审图机构 | 审图合格书 |
| Fire design review | 住建 / 消防审查 window for 特殊建设工程 | Fire design review opinion when the project is special |
| 施工许可 | 住建主管部门 | 施工许可证 |
| Construction | Contractor under 监理 | Quality and safety supervision registration |
| Fire acceptance or filing | Fire acceptance body | Acceptance opinion or filing voucher |
| 规划核实 and joint acceptance | 规自 + 住建 and others | Filing / 备案 |

Do not start construction on a planning permit alone. Do not treat 审图合格 as 施工许可.

## 2. Construction Permit Prerequisites

Confirm the city's checklist. Common items:

- Planning permit in force.
- 审图合格 for the construction drawings.
- Contractor, 监理, and design-institute appointments.
- Quality and safety supervision procedures opened.
- Funds and schedule statements the local 住建局 requires.
- Fire design review opinion when the building is a 特殊建设工程.

If any item is missing, the programme shows it as a predecessor, not as a float activity.

## 3. Fast-Track and Parallel Work

Parallel work is possible only where the city allows it:

- Design development of a later package while an early package is in 审图, if the permit regime allows phased permits.
- Tender documentation marked "subject to 审图" is a commercial risk, not an approval.
- "Concurrent approval and consent" in the Hong Kong sense does not exist as a national Mainland procedure. Do not copy PNAP ADM-19 durations.

## 4. Realistic Programming

### 4.1 Milestones to put on the programme

1. Survey and red-line confirmation.
2. 方案 freeze and planning submission.
3. Planning permit.
4. 初设 freeze.
5. 施工图 coordination freeze.
6. First 审图 comments.
7. Resubmission and 审图合格.
8. Fire design review if special.
9. Contractor procurement (may overlap steps 6–8; see `cn-procurement-strategy`).
10. 施工许可证.
11. Site establishment (`cn-site-establishment`).

### 4.2 Durations

Do not publish a national "statutory day count" as a promise. Record the city's published review period if the user supplies it, and add a resubmission cycle. A single comment round is an assumption, not a rule.

### 4.3 Referral departments

Planning referrals often include heritage, civil aviation (obstacle limitation), traffic, education or health for those uses, and municipal utilities. Each referral is a predecessor when the 规自局 says so.

## 5. Electronic Submission

Many cities use a local online construction-administration platform. Record the platform name, account owner, and file-format rules for that city. There is no single national equivalent of the Hong Kong Electronic Submission Hub. Do not assume a file accepted in one city uploads in another.

## 6. Renewal and Resubmission

- A refused or commented 审图 cycle returns to the discipline that owns the comment. Track ageing comments.
- A lapsed planning permit or land-grant condition is a stop. Ask for the expiry date.
- Changing 容积率, use, or height after submission usually restarts planning, not just 审图.
- Minor drawing corrections after 审图合格 may still need a review delta. Ask the 审图机构; do not assume a "record plan only" Hong Kong threshold.

## 7. What This Skill Does Not Schedule as "Consent"

| Event | Skill |
|-------|-------|
| 消防验收 / 备案抽查 | `cn-fire-acceptance-closeout` |
| 规划核实 | `cn-certificate-of-compliance` |
| 竣工联合验收 / 备案 | `cn-op-submission-strategy` |
| Contract practical completion | `cn-practical-completion-snagging` |

## 8. Record Drawings and Deviations

During construction, deviations are either:

- within the approved envelope and recorded for as-built, or
- a change that needs a new review before the affected work proceeds.

There is no national "minor deviation" millimetre table in this skill. Use the city's 审图 change rule and `cn-site-supervision`.

## 9. Programming Tips

- Put 审图 comments and client decisions on the critical path explicitly.
- Separate "drawing issued" from "approval received".
- Link long-lead procurement (lifts, curtain wall, prefabricated elements) to the revision that 审图 has accepted.
- Weather and holiday calendars affect site start, not the legal effect of a permit.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-pow-stages.md](../../references/cn-pow-stages.md) — stage checklists
* [Construction_Permit_CS.md](../../../cn_s_reference/MOHURD/summaries/Construction_Permit_CS.md) — permit digest
* [Fire_Design_Review_and_Acceptance_Provisions_CS.md](../../../cn_s_reference/Fire%20and%20Rescue/summaries/Fire_Design_Review_and_Acceptance_Provisions_CS.md) — fire review path
