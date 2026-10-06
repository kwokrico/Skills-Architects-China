---
name: cn-construction-health-safety
description: Guides Mainland construction health and safety strategy, risk assessment, accident reporting, and 危大工程 coordination for architects and project managers. Building fire-code design stays in cn-fire-life-safety.
user-invocable: true
disable-model-invocation: true
---

# Mainland Construction Health and Safety

Site safety and design-stage hazard information. Building fire strategy (compartments, egress, GB 55037) is `cn-fire-life-safety`, not this skill.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 危大工程, site safety plan, accident response | `cn-construction-health-safety` | `cn-fire-life-safety` |
| Fire compartments and travel distance | `cn-construction-health-safety` | `cn-fire-life-safety` |
| Daily site inspection of design conformance | `cn-construction-health-safety` | `cn-site-supervision` |

## Halt Criteria

- Do not approve a method statement or sign a 专项施工方案.
- Do not investigate an incident as the statutory employer or contractor.
- Do not quote a height or depth threshold for 危大工程 from memory. Use the current ministry list and mark unverified numbers as unverified.

## 1. Scope and Core Position

| Party | Safety duty (typical) |
|-------|------------------------|
| 建设单位 | Provide a safe environment for the works they control; do not force unsafe programme |
| 施工单位 | Primary site safety responsibility and method statements |
| 监理 | Statutory supervision of safety per its appointment |
| 设计单位 | Design that can be built safely; provide information for dangerous work; do not direct crane operations |
| Architect in this suite | Advisory coordination and design-risk notes only |

## 2. Health and Safety Strategy

### 2.1 Early project plan

- Major hazards: deep excavation, high formwork, scaffolding, demolition, crane, confined space, adjacent metro or buildings.
- Design information needed before those activities.
- Temporary works that change the permanent design.
- Emergency access for the fire service during construction, separate from the permanent fire strategy.

### 2.2 Design-stage inputs

- Note hazardous sequences (cantilever, temporary stability, facade installation).
- Avoid details that require unsafe access if a safer detail meets the brief.
- Flag residual risks that the contractor cannot see from the drawings (prestress, post-fixed anchors, fragile roof).
- Do not specify contractor means and methods unless the design genuinely depends on them.

## 3. Risk Assessments

### 3.1 Types

- Design hazard log (architect / design manager).
- Contractor construction risk assessment and 专项方案.
- 监理 inspection focus list.

### 3.2 Minimum content of a design hazard note

Activity, hazard, who is at risk, design mitigation already in the drawings, residual risk for the contractor, and the drawing reference.

### 3.3 Review cycle

Update at 初设 freeze, 施工图 issue, and whenever a change affects temporary stability, excavation, or facade installation.

## 4. Regulatory Liaison

### 4.1 Authorities

| Body | Topic |
|------|--------|
| 住建主管部门 / 安监站 | Construction safety supervision |
| 应急管理部门 | Work-safety incidents above reporting thresholds |
| 消防救援 | Construction fire-safety checks where the city assigns them |
| Metro / railway protection office | Works inside a protection zone |
| 生态环境 | Dust, noise, wastewater |

### 4.2 Compliance actions

- Identify whether the activity is on the current 危大工程 catalogue (see the MEM/MOHURD digest).
- 超过一定规模的危大工程 needs the expert argument the rule requires. The architect does not replace that expert.
- Stop advice that tells the user to skip a 专项方案.

## 5. Accident Investigation and Reporting

### 5.1 Immediate response

Protect people, call emergency services, and preserve the scene as the site rules require. The architect does not lead rescue.

### 5.2 Investigation

The employer and contractor investigate under work-safety law. If the design is implicated, preserve the issued revision and RFI trail. Do not alter drawings during an investigation without legal advice.

### 5.3 Outputs

Factual note: drawing revision, instruction numbers, and what the design did and did not specify. No admission of liability. Halt on blame or damages.

## 6. Site Inspections

### 6.1 Programme

Design-representative visits are not a substitute for the contractor's daily checks or 监理's statutory inspections. Agree frequency in the appointment.

### 6.2 Record

Date, area, drawing revision, deviation, and whether work stopped. Photos are evidence of what was seen, not a certificate.

### 6.3 Policy check

Confirm the site induction exists and that design visitors follow it. Do not enter an exclusion zone to "have a look".

## 7. Design and Management Coordination

Mainland projects do not use UK CDM as the legal system. Apply:

- Design hazard information issued with the drawings.
- Contractor safety documentation reviewed only for conflict with the permanent design.
- 监理 and the client safety lead as the site coordination roles named in the appointments.
- Interface with `cn-project-management` for programme pressure that creates unsafe overlap.

### 7.1 Review of contractor documents

State the limit: "reviewed for conflict with drawing X, not approved as a safe method".

### 7.2 Project liaison

Escalate unresolved dangerous conditions to the client and 监理 in writing the same day.

## 8. Interfaces

| Topic | Skill |
|-------|-------|
| Permanent fire strategy | `cn-fire-life-safety` |
| Site logistics | `cn-site-establishment` |
| Design conformance on site | `cn-site-supervision` |
| Programme pressure | `cn-project-management`, `cn-construction-programme` |

## 9. Output Checklist

- This note is not a 专项方案 approval.
- 危大工程 candidates listed with "threshold to be confirmed against the current catalogue".
- Design hazard log has drawing references.
- Incident advice stops at facts and preservation.
- Fire-code questions redirected.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [Work_Safety_Law_CS.md](../../../cn_s_reference/MEM/summaries/Work_Safety_Law_CS.md) — work-safety digest
* [Hazardous_Divisional_Works_CS.md](../../../cn_s_reference/MEM/summaries/Hazardous_Divisional_Works_CS.md) — 危大工程 digest
