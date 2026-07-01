---
name: cn-project-management
description: Activate for Mainland project leadership—delivery plan, consultant appointments, risk/VM, contractor selection support, payment validation, disputes, programme/budget monitoring, and construction-to-occupation transition under 全过程工程咨询 framing where applicable.
user-invocable: true
disable-model-invocation: true
---

# Mainland Project Management
Covers architect-led or design-team project leadership: strategic brief through occupation transition. Advisory only—contractual CA decisions route to `cn-tender-contract-administration` and legal counsel.

---

## 1. Scope

- Business case and strategic brief alignment (立项、可研、投资边界).
- Consultant selection, appointments, and RACI.
- Delivery plan, risk register, design review and VM cadence.
- Contractor selection support (with procurement and cost skills).
- Programme and budget monitoring; client reporting.
- Dispute escalation framework (not legal interpretation).
- Construction-to-occupation transition with acceptance skills.

**全过程工程咨询:** When the firm holds PMO or 项目管理 role, align tasks with contract and local pilot requirements; do not conflate with pure design scope.

---

## 2. Business Case and Strategic Brief

Confirm or document:

- Client objectives, success criteria, and decision-makers.
- Site, scale, typology, and approval pathway assumptions.
- Budget and programme envelopes.
- Procurement path (`cn-procurement-strategy`).
- Insurance and liability boundaries (`cn-professional-indemnity`).

---

## 3. Consultant Selection and Appointments

- Define scope packages (建筑、结构、机电、消防、幕墙、BIM、绿建).
- Issue briefs with deliverables tied to `cn-plan-of-work` stages.
- Track dependencies: geotech, traffic, heritage, utilities.
- Fee and scope alignment via `cn-fee-proposal-strategy`.

---

## 4. Delivery Plan

Minimum contents:

1. Stage milestones mapped to statutory gates.
2. Critical path (often 审图闭环)—see `cn-consent-scheduling`.
3. Resource plan—see `cn-project-resource-levelling`.
4. Risk register (likelihood, impact, owner, mitigation).
5. Communication plan (client, authorities, contractors).

---

## 5. Risk, VM, and Design Review

- Risk workshops at scheme, preliminary, and pre-tender gates.
- VM targets cost, programme, and constructability—coordinate with `cn-cost-consultancy`.
- Design review minutes with action owners and due dates.
- Escalate regulatory ambiguity per [operational.md](../../references/operational.md).

---

## 6. Contractor Selection and Commercial Control

- Support PQ/tender review; technical consistency checks.
- Payment validation interface with CA/QS—do not certify without authority.
- Change control: log, classify, route approval-impacting items.

---

## 7. Disputes

| Situation | Escalate to |
|-----------|-------------|
| Contract interpretation | Legal counsel + `cn-tender-contract-administration` |
| EOT / claim quantum | CA + QS + legal |
| Authority interpretation | 项目负责人 + specialist consultant |
| PI incident | Firm risk manager + broker |

---

## 8. Programme and Budget Monitoring

- Rolling status: stage, % design complete, open risks, approval status.
- Budget vs cost plan variance—QS-led with architect technical input.
- Fast-track flags: parallel paths only where truly independent.

---

## 9. Construction to Occupation

- Align site supervision (`cn-site-supervision`) with acceptance dossier (`cn-op-submission-strategy`).
- Snagging and DLP handover (`cn-practical-completion-snagging`).
- Client reporting through 竣工备案.

---

## 10. Output Checklist

- Delivery plan or progress report with RAG status.
- Risk register update.
- Consultant RACI current.
- Open authority / 审图 actions tracked.
- Next gate date and missing inputs listed.

---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Delivery plan / client reporting | `cn-project-management` | `cn-plan-of-work` |
| Stage checklist only | `cn-project-management` | `cn-plan-of-work` |
| Contract variations | `cn-project-management` | `cn-tender-contract-administration` |
| Cost plan / BoQ | `cn-project-management` | `cn-cost-consultancy` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
