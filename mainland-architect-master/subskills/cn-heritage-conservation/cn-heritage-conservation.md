---
name: cn-heritage-conservation
description: Activate for Mainland heritage conservation workflows, including 文物保护单位/历史建筑 processes, 文物影响评估, adaptive reuse submissions, intervention strategy, and conservation governance with city variance.
user-invocable: true
disable-model-invocation: true
---

# Mainland Heritage Conservation

Advanced guidance for Mainland China heritage conservation projects: statutory context, 文物主管部门 engagement, 文物影响评估, adaptive reuse submission strategy, and technical conservation principles for design and approvals.

---

## 1. Conservation Governance in Mainland China

### 1.1 Key Bodies and Their Roles (typical)
- **文物主管部门**: 文物保护行政主管部门 (often via local 文物局/文旅局体系).
- **规划与住建**: 规自局/住建局 workflow still applies for planning and building compliance.
- **消防救援**: fire acceptance/consultation for life-safety constraints.
- **审图机构**: construction drawing review for compliance items (project-dependent).

### 1.2 Main Legal / Governance Framework (baseline)
- **文物保护法** (and local implementation rules) as the core statutory framework
- **Historical building / conservation control**: city-level rules for 历史建筑/历史风貌区
- **Planning + land conditions**: land grant and planning indicators still apply
- **Building compliance**: fire/structure/accessibility still must be resolved (baseline GB standards + local supplements)

Important distinction (Mainland):
- **文物保护单位**: national/provincial/municipal/county levels with different approval thresholds.
- **历史建筑/风貌保护对象**: often managed under urban conservation rules; procedural requirements vary by city.

---

## 2. Heritage Level and Project Implications

### 2.1 Practical meaning (general)
- Higher protection level means:
  - earlier authority engagement
  - tighter constraints on intervention and demolition
  - stronger documentation and method statements

### 2.2 Design / Submission Expectations by Grade
- Higher grades generally require:
  - More conservative intervention strategy
  - Stronger evidence of minimal and reversible works
  - Earlier and deeper AMO consultation
  - More robust statement of significance and impact mitigation

Use current AMO/AAB published lists at project start and before final submission, as status can change.

---

## 3. 文物影响评估 / Heritage Impact Assessment Workflow

### 3.1 Typical structure
1. **Baseline and significance assessment**
   - Historical development, architectural value, social value
   - Identify character-defining elements (CDEs)
2. **Condition and vulnerability survey**
   - Fabric mapping, defects, previous alterations
3. **Impact assessment**
   - Direct, indirect, temporary, cumulative impacts from proposed works/use
4. **Mitigation and design response**
   - Avoid, minimize, repair, compensate hierarchy
5. **Implementation and monitoring plan**
   - Method statements, hold points, supervision, post-work review

### 3.2 Character-defining elements (CDEs)
Common CDEs include:
- Primary facades, roof forms, structural bays
- Original staircases, verandahs, timber windows/doors
- Significant finishes, inscriptions, craftsman details
- Courtyard and circulation patterns

Rule: alterations to CDEs need explicit justification and strongest mitigation.

---

## 4. Adaptive Reuse Submission Strategy

### 4.1 Core Submission Pack
- Statement of significance and conservation objectives
- Existing condition survey and measured drawings
- Conservation management / intervention plan
- HIA report with mitigation schedule
- Proposed architectural/structural/MEP/fire upgrades
- Phasing and method statements (especially for fragile fabric)

### 4.2 Reconciliation Strategy (Conservation vs Compliance)
Major friction points:
- **Fire safety upgrades** vs retention of historic stairs/doors
- **Barrier-free access** vs limited space and original level changes
- **Building services retrofits** vs heritage fabric intrusion
- **Structural strengthening** vs material authenticity

Common approach:
- Prioritize low-intrusion, reversible solutions first
- Use performance-based or alternative compliance pathways where accepted
- Record rationale for each intervention against significance hierarchy

---

## 5. Conservation Intervention Principles

Apply these in sequence:
1. **Minimum intervention** - do only what is necessary.
2. **Reversibility** - prefer works that can be undone without major damage.
3. **Like-for-like repair first** - retain and repair original fabric before replacement.
4. **Distinguish new from old** - compatible but identifiable additions.
5. **Full documentation** - before/during/after records for accountability.

Avoid:
- Unnecessary facade stripping
- Concealed irreversible service routing through key heritage fabric
- Over-standardized finishes that erase patina and authenticity

---

## 6. Construction Stage Controls for Heritage Works

- Require conservation method statements for sensitive items.
- Establish mock-ups for repair techniques and material matching.
- Set inspection hold points before irreversible steps.
- Maintain photographic and written site logs tied to drawings.
- Ensure specialist contractors (stone, timber, plaster, metalwork) are pre-qualified.

Site governance should include both statutory supervision and conservation supervision.

---

## 7. Quick Decision Guide

Use this skill when the query involves:
- AMO / AAB consultation strategy
- HIA scoping, structure, or mitigation logic
- Graded building intervention decisions
- Adaptive reuse authority submission packaging
- Conservation principles beyond basic "is it listed?" checks

Route related topics:
- Building code deep checks -> `cn-building-codes`
- Fire strategy and egress trade-offs -> `cn-fire-life-safety`
- Planning permission path -> `cn-spatial-planning`
- Existing-building documentation execution -> `cn-alterations-additions`

---

## 8. Required Inputs (ask if missing)

- City and heritage designation level (文保单位/历史建筑/风貌区等)
- Current approvals and any heritage authority correspondence
- Statement of significance / CDE list (or measured drawings + photos)
- Proposed use change and life-safety strategy constraints
- Time constraints (fast-track vs normal)

---

*Reference baseline: PRC heritage governance and city-level implementation rules; always validate local authority process and required deliverables.*


## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Heritage / 文物 / 历史建筑 | `cn-heritage-conservation` | `cn-spatial-planning` |
| Unauthorized works | `cn-heritage-conservation` | `cn-unauthorised-building-works` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [heritage-impact-checklist.md](../../references/heritage-impact-checklist.md) — impact assessment checklist
