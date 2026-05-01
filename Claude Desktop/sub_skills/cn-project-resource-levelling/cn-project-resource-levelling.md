---
name: cn-project-resource-levelling
description: Activate for project manpower resource levelling, burn-rate control, and profit-versus-progress tracking in Mainland China practice, including break-even rate calculations and drawdown alignment.
user-invocable: true
---

# Mainland Project Resource Levelling
Execution playbook for balancing manpower deployment, protecting project margin, and keeping fee drawdown in sync with delivery progress.

---

## 1. Core Position
- Track `Profit vs Progress` weekly, not only at month-end.
- Resource levelling is a commercial control function: staffing decisions must follow fee recovery reality.
- Compute and update `break-even hourly rates` by role before assigning workload.
- Burn rate must stay within planned drawdown capacity; otherwise trigger corrective action immediately.

---

## 2. Profit vs Progress Framework
Use a dual-axis control:
1. **Progress axis**: % of scope actually completed (deliverables accepted, authority milestones achieved).
2. **Profit axis**: earned fee minus loaded labor cost (and controllable project overhead where applicable).

Minimum weekly dashboard:
- Planned progress vs actual progress (%).
- Planned fee drawdown vs invoiced vs cash collected.
- Hours spent vs hours budgeted by role.
- Gross margin to date and forecast margin at completion.
- Variance drivers (scope change, rework, approval delay, staffing mismatch).

Interpretation rules:
- High progress, low profit -> underpriced effort / inefficient staffing / unbilled variation.
- High profit, low progress -> deferred cost recognition risk or unrealistic completion forecast.
- Low progress, high burn -> immediate resource replan and commercial escalation.

---

## 3. Break-even Hourly Rate Calculation
For each role, define:
- `Annual loaded cost` = salary + bonus + social insurance/housing fund + benefits + software + overhead allocation.
- `Practical billable hours` = available hours minus leave, training, admin, business development, internal QA.

Formula:
- `Break-even hourly rate = Annual loaded cost / Practical billable hours`

Project usage:
1. Build a blended break-even rate for the planned team mix.
2. Compare blended break-even against contracted effective recovery rate.
3. Add target margin buffer to derive minimum sustainable charge-out equivalent.
4. Recalculate when staffing mix changes (for example, replacing senior staff with junior teams plus additional QA hours).

Control thresholds:
- If forecast recovery falls below break-even for 2 consecutive reporting periods, mandatory intervention.
- Do not approve prolonged overtime unless its cost is contractually recoverable or margin impact is explicitly accepted.

---

## 4. Burn Rate Monitoring Against Drawdown
Definitions:
- `Burn rate` = labor cost consumed per week (or month).
- `Drawdown` = fee value that can be recognized/invoiced/collected based on achieved milestone.

Weekly control checks:
1. Burn-to-drawdown ratio (`burn / collectible drawdown`).
2. Cash conversion lag (invoice-to-cash days).
3. Forward visibility of next billable milestone.
4. Unbilled approved variation value.

Practical guardrails:
- Green: burn <= planned collectible drawdown.
- Amber: burn exceeds drawdown by up to 10% for one cycle -> tighten staffing and accelerate invoicing evidence.
- Red: burn exceeds drawdown by >10% or persists >2 cycles -> freeze non-critical effort, reset staffing plan, escalate commercially.

---

## 5. Resource Levelling Actions
When over-burn is detected:
1. Re-sequence deliverables toward near-term billable milestones.
2. Shift routine production to lower-cost roles with defined QA gates.
3. Ring-fence senior time for high-risk approvals, client decisions, and regulatory interfaces.
4. Convert ambiguous requests into formally instructed additional services.
5. Reduce rework loop by locking decision logs, version control, and client sign-off gates.

When under-utilization is detected:
1. Pull forward technical coordination tasks that reduce future schedule risk.
2. Support adjacent projects with higher recovery potential (without damaging critical path).
3. Use spare capacity for template automation only when payback horizon is clear.

---

## 6. Reporting Cadence and Ownership
- **Weekly PM review**: manpower mix, burn variance, milestone risk.
- **Fortnightly commercial review**: drawdown, invoicing status, aged receivables impact on resourcing.
- **Monthly leadership review**: margin forecast, staffing strategy, go/no-go on continued acceleration.

Recommended owners:
- Project Manager: progress integrity and staffing deployment.
- Commercial/Finance lead: drawdown integrity, recovery forecast, aging risk.
- Director/Partner: intervention authority for scope, fee, and escalation decisions.

---

## 7. Red Flags
- Team hours rising while milestone acceptance repeatedly slips.
- Senior staff performing prolonged production tasks due to unresolved coordination issues.
- Repeated client revisions with no additional service instruction.
- Billing lag created by incomplete submission evidence package.
- Drawdown assumptions based on expected approvals rather than achieved approvals.
- Persistent reliance on overtime to maintain baseline programme.

---

## 8. Practical Output Checklist
- Role-based break-even table completed and current.
- Weekly burn-to-drawdown dashboard active with threshold flags.
- Profit-vs-progress variance commentary issued and actioned.
- Resource levelling decisions logged with owner and due date.
- Additional services register linked to hours and recovery status.
- Forecast margin at completion updated after every major scope or staffing change.

---

*Teams should align this framework with executed consultancy agreements, project-specific fee schedules, and internal financial policies before taking contractual or staffing actions.*
