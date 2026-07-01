---
name: cn-site-supervision
description: Activate for Mainland construction-stage design supervision, variation control, inspection governance, acceptance readiness, and handover documentation under PRC delivery frameworks.
user-invocable: true
disable-model-invocation: true
---

# Mainland Site Supervision
Covers the design-side supervision role during construction, including inspection planning, design-change control, quality-risk governance, and preparation for completion acceptance.

---

## 1. Mainland Role Framework During Construction
- **项目负责人 / 设计总工:** Overall technical governance, approval-alignment decisions, and high-risk signoff.
- **专业负责人:** Discipline-level compliance for architecture/structure/MEP/fire.
- **总承包单位:** Construction execution, QA records, and as-built responsibility.
- **监理单位:** Third-party quality/schedule/safety witness role per contract scope.

Core principle: supervision is risk and acceptance management, not only drawing clarification.

---

## 2. Supervision Plan Framework
Typical supervision plan should define:
1. **Inspection levels and frequency** (critical hold points vs routine checks).
2. **Responsible parties** (design team, contractor, supervising engineer, owner representative).
3. **Records and evidence** (site photos, test reports, checklists, marked-up drawings).
4. **Escalation paths** for non-conforming works.
5. **Acceptance linkage** to专项验收/联合验收 submission requirements.

Practical baseline:
- Increase frequency for structural critical zones, fire compartment interfaces, and concealed works.
- Keep supervision plan aligned with latest审图意见 and approved drawing set.

---

## 3. Site Meeting and Reporting Protocol
Maintain a structured cadence:
- **Weekly site meeting:** progress, safety interfaces, quality deviations, pending inspections.
- **Technical coordination meeting:** 设计总工/专业负责人与施工、监理解决设计冲突.
- **Regulatory tracker:** open 审图/消防/规划 comments and deadlines.
- **Programme interface:** align site progress with `cn-construction-programme` hold points.
- **Safety interface:** escalate site H&S issues to `cn-construction-health-safety` (not fire design code).

Minimum meeting outputs:
- Clear action owner and due date.
- Classification of issues: informational, minor deviation, major deviation, safety-critical.
- Updated risk log tied to permit milestones and acceptance nodes.

---

## 4. Deviation Handling (As-built vs Approved Drawings)
Use a triage approach:
1. **Identify deviation** from approved plan.
2. **Assess impact** on building area, egress, structure, fire safety, accessibility, and permit compliance.
3. **Classify** as field correction, design variation, or approval-impacting change.
4. **Implement corrective action** and submit formal change where required before acceptance.

High-risk triggers that usually need prior formal action:
- Changes reducing exit width or increasing travel distance.
- Structural member size/detail changes affecting load path.
- Changes affecting approved key indicators (`容积率`, `建筑密度`, `限高`).
- Material substitutions affecting FRR or code compliance.

---

## 5. Completion and Acceptance Path
Key closeout logic:
1. Close major non-conformities and technical punch list.
2. Reconcile as-built records with approved and changed drawings.
3. Complete discipline-level acceptance evidence packages.
4. Support fire and special-system acceptance.
5. Enter `竣工联合验收/备案` process.

Typical sequence logic:
1. Construction completion of agreed scope.
2. Internal pre-acceptance audit.
3. External acceptance interfaces and authority coordination.
4. Final filing and handover package issuance.

---

## 6. Audit and Compliance Checks
Before completion filing, run a pre-audit pack:
- Approved vs as-built drawing reconciliation.
- Test certificates and inspection logs completeness.
- Fire systems and egress consistency.
- Accessibility and statutory dimensional checks.
- Outstanding RFI/defect/variation closure status.

Recommended output:
- Signed compliance matrix linking each requirement to evidence and file location.

---

## 7. Handover to Acceptance Stage
Handover package should include:
- Final record drawings and revision control log.
- Completion certifications and test report index.
- Outstanding punch list with responsible party and closeout date.
- Operational limitations and maintenance cautions for O&M handover.

Programme tip: include float between practical completion and joint acceptance windows for comment closure and file reconciliation.

---

*Project baseline: approved design/variation set, current local authority requirements,审图闭环 records, and contract supervision obligations.*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Site supervision / RFI | `cn-site-supervision` | `cn-tender-contract-administration` |
| Construction sequence / 穿插 | `cn-site-supervision` | `cn-construction-programme` |
| Site safety / 危大工程 | `cn-site-supervision` | `cn-construction-health-safety` |
| Acceptance closeout | `cn-site-supervision` | `cn-op-submission-strategy` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
