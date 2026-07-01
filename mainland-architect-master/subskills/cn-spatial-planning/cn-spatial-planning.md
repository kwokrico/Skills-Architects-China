---
name: cn-spatial-planning
description: Mainland spatial planning skill for 控规 interpretation, red-line controls, planning permit path, and multi-authority coordination under national + local standards.
user-invocable: true
disable-model-invocation: true
---

# Mainland Spatial Planning

Covers PRC control-plan logic, land and planning constraints, and approval sequencing.

Regulatory hierarchy:
- National baseline first (standards/guides): `GB / GB-T / JGJ`
- Then local supplements and implementation口径: `DB / DGJ / DBJ` + municipal planning rules

If city is not specified, treat guidance as national baseline pre-check and request local procedural confirmation.

---

## 1. Planning Control Framework (Mainland)

| Layer | Typical Instrument | Main Control Targets |
|---|---|---|
| Macro/territorial | Master plans and territorial strategies | Growth direction and major infrastructure |
| Statutory urban-rural planning | City-level statutory plans | Functional zoning and policy constraints |
| Detailed regulatory layer | `控制性详细规划` | FAR, density, green ratio, height, setbacks, access |
| Land transfer layer | 出让条件 and contract terms | Use, phasing, key technical obligations |

---

## 2. Red-Line and Indicator Logic

- `用地红线`: legal land boundary and ownership scope.
- `建筑红线`: building control boundary and setback envelope.
- `道路红线`: road planning boundary influencing access and retreat distance.

Core indicator checks:
- `容积率`
- `建筑密度`
- `绿地率`
- `建筑限高`
- `退界控制`
- `日照分析`

---

## 3. Authority Workflow

| Stage | Main Authority/Output |
|---|---|
| Land and planning permit | `自然资源局/规自局` (land-use + construction planning permit path) |
| Technical review | Sector authorities + third-party technical opinions as required |
| Construction readiness | `住建局` related construction permit path |
| Completion | Multi-department joint acceptance and filing |

If city context is unknown, output national baseline + request local procedural confirmation.

## 4. Typical Planning Package Components

- Site red-line and current-condition map
- Control-indicator compliance matrix
- Total site plan and phasing strategy
- Traffic/municipal interface assumptions
- Sunlight and wind-environment assessments where required
- Risk note on local policy sensitivities (industrial transformation, urban renewal, etc.)

---

## 5. Common Failure Modes and Mitigation

| Failure Mode | Consequence | Mitigation |
|---|---|---|
| Red-line misunderstanding | Invalid indicator calculations | Verify `用地红线/建筑红线/道路红线` before massing |
| FAR and building density calculated from outdated control data | Rework at permit stage | Build a single source of truth indicator table |
| Land-transfer terms ignored | Commercial/legal risk | Cross-check design assumptions against出让条件 |
| City supplement standards omitted | 审查退件 | Force city-context check in every planning response |
| Unrealistic phasing under fast-track pressure | Delay in permit and procurement | Add phase-by-phase permit dependency chart |

---

## 6. Required Inputs (ask when missing)

- Project city and district
- Latest 控规 extracts and key indicator tables
- Land transfer terms (出让条件)
- Current planning permit status
- Constraints from transport/municipal agencies
- Whether project uses EPC / design-build route

---

*Baseline references: Urban and Rural Planning Law, Land Administration Law, local control-plan regulations, and relevant DB/DGJ/DBJ municipal supplements.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Planning indicators / 控规 | `cn-spatial-planning` | `cn-building-codes` |
| Fire egress | `cn-spatial-planning` | `cn-fire-life-safety` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
