---
name: cn-building-codes
description: Mainland China building code skill for GB 550xx general codes, older GB/GB-T/JGJ where they do not conflict, and local DB/DGJ/DBJ supplements. Covers planning indicators, building area, fire and accessibility baselines, and authority workflow.
user-invocable: true
disable-model-invocation: true
---

# Mainland Building Codes

Use this skill for code applicability, compliance logic, and code-citation discipline in Mainland China projects.

---

## 1. Regulatory Hierarchy (must follow)

| Level | Typical References | Usage Rule |
|---|---|---|
| Mandatory general codes | `GB 550xx` | Prevail over conflicting older mandatory clauses |
| Other national standards | GB, GB/T, JGJ | Cite only where the general code does not conflict |
| Ministry guidance | MOHURD circulars, technical guides | Use where mandatory or explicitly adopted |
| Local supplement | DB, DBJ, DGJ, local审查口径 | Apply after confirming project city. May be stricter. Cannot weaken a general code |

Force ranking when two texts disagree:

1. Mandatory general code and any remaining 强条.
2. Recommended standards (`GB/T`, many JGJ) where the general code still points at them.
3. Guides and 图集. A 图集 shows a construction method. It does not discharge a mandatory clause.
4. 主管口径. Record it, and still cite the clause it sits beside.

A number in a conclusion names the standard, the edition, and the clause. If any of the three is missing, mark the number unverified. Full citation rules are in [compliance.md](../../references/compliance.md).

---

## 2. Core National Standards (high frequency)

Open the general code first. The older standard in the same row applies only where it does not conflict.

| General code | Topic | Older standard, where it does not conflict |
|---|---|---|
| `GB 55031-2022` | Civil building design | `GB 50352` |
| `GB 55037-2022` | Building fire | `GB 50016` |
| `GB 55036-2022` | Fire facilities | Specialist fire-system standards |
| `GB 55015-2021` | Energy | `GB 50189` and the climate-zone residential energy standards |
| `GB 55016-2021` | Indoor environment (sound, light, thermal) | The detailed environment standards |
| `GB 55019-2021` | Accessibility | `GB 50763` |
| `GB 55030-2022` | Waterproofing | The detailed waterproofing standards |
| — | Seismic | `GB 50011` |
| — | Geotechnical and foundations | `GB 50007` |
| — | Concrete structures | `GB 50010` |
| — | Building area | `GB/T 50353`, with area rules in `GB 55031` |
| — | Green-building stars | `GB/T 50378` (a rating above the energy floor, not a substitute for `GB 55015`) |

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
| Fire strategy | `GB 55037` first; `GB 50016` only where it does not conflict; facilities under `GB 55036` |
| Accessibility | `GB 55019` first; `GB 50763` where it does not conflict |
| Green building | `GB 55015` mandatory floor, then `GB/T 50378` star target |

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

*Baseline references: GB 55031, GB 55037, GB 55036, GB 55015, GB 55016, GB 55019, GB 55030, then GB 50352, GB 50016, GB 50011, GB 50010, GB 50007, GB/T 50353, GB 50763, GB 50189, GB/T 50378 where they do not conflict, plus applicable local DB/DGJ/DBJ standards. See [cn-code-catalog.md](../../references/cn-code-catalog.md).*

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| 控规 / FAR / red lines | `cn-building-codes` | `cn-spatial-planning` |
| Fire egress strategy | `cn-building-codes` | `cn-fire-life-safety` (GB 55037 first) |
| Numeric egress/area only | `cn-building-codes` | `cn-architect-calculator` |
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [cn-code-catalog.md](../../references/cn-code-catalog.md) — standards still missing a digest, and city series
* [cn-statutory-source-register.md](../../references/cn-statutory-source-register.md) — collection list; do not quote a row as a clause
* [GB_55038_2025_Residential_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_55038_2025_Residential_CS.md) — residential announcement and repeal list
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
