---
name: cn-fire-acceptance-closeout
description: >
  Closes Mainland fire acceptance (消防验收) with commissioning evidence, integrated testing,
  authority inspection readiness, and comment-closure governance. Use for fire system handover,
  test records, and 消防救援局 inspection prep. Legacy alias: cn-fsd-licensing-compliance.
user-invocable: true
disable-model-invocation: true
---

# Mainland Fire Acceptance Closeout
Execution guide for closing out fire systems and achieving `消防验收` readiness under Mainland workflows.

---

## 1. Scope and Outcome
- This sub-skill focuses on the practical route from installed fire systems to authority sign-off.
- It centers on:
  - Integrated fire-system commissioning and evidence governance.
  - Hydrant/sprinkler/alarm/smoke-control tests and associated records.
  - `消防救援局` inspection readiness and follow-up.
  - Acceptance filing package quality and traceability.

---

## 2. Typical Handover Sequence
1. Confirm as-built fire services installation matches approved submissions.
2. Complete pre-test and witness test planning with specialist contractor.
3. Prepare acceptance evidence pack (as-built, test logs, commissioning evidence).
4. Submit for authority inspection booking (per local process).
5. Conduct inspection and close comments/punch items immediately.
6. Re-submit rectification evidence where required.
7. Finalize fire acceptance completion evidence and filing package.

---

## 3. Evidence Package (Core)
Minimum evidence set is city-dependent, but should always include:
- Fire system as-built drawings (latest, controlled revision).
- Cause-and-effect matrix and functional test results.
- Pump room and water supply test evidence.
- Alarm and linkage testing evidence (interfaces with MEP).
- Smoke control commissioning evidence (where applicable).
- Comment closeout tracker with photo/video proof where needed.

---

## 4. Inspection Readiness Checklist
- System zoning and labeling match approved layout and plant schedules.
- Fire pump, jockey pump, valves, and alarm interfaces are fully commissioned.
- Hydrant/hose reel pressure and flow test records are complete and signed.
- Pump room and critical controls are accessible, labeled, and safe for inspection walkdown.
- Cause-and-effect matrix matches functional test outcomes.
- Defect log is closed or reduced to non-safety cosmetic issues only.
- Competent representatives (AP/main contractor/fire services contractor) attend inspection.

---

## 5. Hydrant and Hose Reel Test Control
- Confirm test method, acceptance criteria, and witness protocol before testing day.
- Calibrate test gauges/meters and keep calibration proof with test package.
- Record:
  - test location and zone
  - static and running pressure
  - flow readings
  - pump auto-start behavior
  - any anomalies and corrective action
- Capture photos/videos for key readings and equipment states for dispute-proof evidence.
- Re-test immediately after rectification and maintain clear superseded-vs-current log status.

---

## 6. Common Failure Modes to Prevent
- Mismatch between as-built drawings and site installation.
- Test sheets without signatures, dates, or instrument references.
- Unclosed punch items carried into authority inspection.
- Inconsistent document revisions submitted by different parties.
- Late discovery of interface issues between fire alarm and mechanical/electrical systems.

---

## 7. Fast Escalation Model
### Stage A: Pre-inspection (internal)
- Resolve all high-risk non-conformities before booking FSD inspection.
- Hold a 30-minute closeout meeting with named owners and deadlines.

### Stage B: During inspection
- Keep one recorder for all comments; log wording exactly.
- Agree rectification intent on-site where possible to reduce re-interpretation risk.

### Stage C: Post-inspection
- Issue comment tracker within same day.
- Submit rectification evidence in structured bundles by item number.
- Request re-inspection or closeout confirmation without delay.

---

## 8. Minimum Deliverable Set
- Final fire systems as-built drawings.
- Hydrant/hose reel test reports with calibration references.
- Commissioning and integrated test records.
- Comment closeout log (if inspection comments were issued).
- Acceptance filing bundle per city requirements.

---

## 9. Output Format for User Support
When responding to project teams, provide:
1. Current stage in handover sequence.
2. Missing evidence list (document-by-document).
3. Inspection risk rating: `Low / Medium / High`.
4. Next 3 actions with owners and deadlines.
5. Fire acceptance readiness verdict with blockers clearly stated.

---

## 10. Required Inputs (ask if missing)

- City and district
- Fire system scope (sprinkler/hydrant/alarm/smoke control)
- Current stage and target acceptance date
- Existing inspection comments (if any)
- Delivery mode and main contractor/fire subcontractor responsibility boundaries

---

*Use this guidance with project-specific approved plans, contract requirements, and current local fire acceptance expectations.*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 消防验收 closeout | `cn-fire-acceptance-closeout` | `cn-fire-life-safety` |
| Joint acceptance strategy | `cn-fire-acceptance-closeout` | `cn-op-submission-strategy` |
| Legacy ID cn-fsd-licensing-compliance | `cn-fire-acceptance-closeout` | `— (same module)` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
