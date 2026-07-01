---
name: cn-building-codes
description: Mainland China building code skill for GB/GB-T/JGJ baseline + local DB/DGJ/DBJ supplements, covering planning indicators, building area measurement, fire/accessibility baseline, and authority workflow.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Codes

Use this skill for code applicability, compliance logic, and code-citation discipline in Mainland China projects.

---

## 1. Regulatory Hierarchy (must follow)

| Level | Typical References | Usage Rule |
|---|---|---|
| National baseline | GB, GB/T, JGJ | Default basis when city not specified |
| Ministry guidance | MOHURD circulars, technical guides | Use where mandatory or explicitly adopted |
| Local supplement | DB, DBJ, DGJ, local审查口径 | Apply after confirming project city |

---

## 2. Core National Standards (high frequency)

| Standard | Topic |
|---|---|
| `GB 50352` | General civil building design baseline |
| `GB 50016` | Fire code baseline |
| `GB 50011` | Seismic design |
| `GB 50007` | Geotechnical and foundations |
| `GB 50010` | Concrete structures |
| `GB 50763` | Accessibility |
| `GB/T 50353` | Building area measurement |
| `GB/T 50378` | Green building evaluation |

---

## 3. Planning and Control Indicators (Mainland)

| Indicator | Mainland Term | Typical Data Source |
|---|---|---|
| Plot ratio | `容积率` | 控规 + 出让条件 |
| Site coverage | `建筑密度` | 控规 |
| Green ratio | `绿地率` | 控规 + local design regulations |
| Height cap | `建筑限高` | 控规 + aviation/urban skyline controls |
| Sunlight requirement | `日照分析` | National method + local variants |

Red-line logic:
- `用地红线`: legal land boundary.
- `建筑红线`: buildable boundary/setback control line.
- Use both before any FAR/density calculation.

---

## 4. Building Area Measurement (GB/T 50353)

Use `建筑面积` terminology, not HK-style exempt-GFA framing.

| Measurement Item | Rule Basis |
|---|---|---|
| Total building area | Sum by standard category definitions |
| Countable/non-countable handling | Per category rules in measurement standard + local审图口径 |
| Submission output | Keep `m²`, normally 2 decimal places unless template differs |

When city-specific category handling is uncertain, explicitly request city and审图机构 feedback.

## 5. Fire and Accessibility Baseline Hooks

| Domain | Baseline |
|---|---|
| Fire strategy | `GB 50016` + local fire review practice |
| Accessibility | `GB 50763` + local implementation details |
| Green building | `GB/T 50378` + local star target requirements |

---

## 6. Approval and Review Checkpoints

| Stage | Key Authority Check |
|---|---|
| 方案设计 | 规自局 planning control alignment |
| 初步设计 | Technical and investment/budget feasibility |
| 施工图设计 | Mandatory third-party `施工图审查` |
| Construction start | `施工许可证` by 住建主管部门 |
| Completion | Fire acceptance + `竣工联合验收/备案` |

---

## 7. Required Input Checklist (ask when missing)

- Project city and district
- Current stage (`方案` / `初设` / `施工图` / `施工`)
- Site red-line drawing (`用地红线` + `建筑红线`)
- Latest planning conditions and land transfer terms
- Any审图意见/authority comments already received

---

*Baseline references: GB 50352, GB 50016, GB 50011, GB 50010, GB 50007, GB/T 50353, GB 50763, GB/T 50378, plus applicable local DB/DGJ/DBJ standards.*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 控规 / FAR / red lines | `cn-building-codes` | `cn-spatial-planning` |
| Fire egress strategy | `cn-building-codes` | `cn-fire-life-safety` |
| Numeric egress/area only | `cn-building-codes` | `cn-architect-calculator` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
