---
name: cn-architect-foundations
description: >
  Provides Mainland China context defaults (regulatory hierarchy, stage language, rules of thumb,
  and practice references) when architecture queries need baseline framing. Routing and compliance
  stay in mainland-architect-master SKILL.md.
user-invocable: false
auto-activate: false
disable-model-invocation: true
---

# Mainland Architect Foundations

Context layer for Mainland practice. The master router in [`SKILL.md`](../../SKILL.md) owns halt rules, the decision tree, and sub-skill dispatch. This file does not duplicate that tree.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Rules of thumb, stage language, practice map | `cn-architect-foundations` | Specialist `cn-*` skill |
| Which skill handles a topic | `cn-architect-foundations` | Master §5D and §8 |
| Binding code conclusion | `cn-architect-foundations` | `cn-building-codes` and `cn_s_reference` |

## 1. Practice Reference (Non-Statutory)

Use these as design-culture pointers only. They are not approval criteria.

| Practice pattern | What to look at | When it helps |
|------------------|-----------------|---------------|
| Regional modernism | Wang Shu / Amateur Architecture; Liu Jiakun | Cultural and civic projects, material memory |
| High-density podium-tower | Contemporary Shenzhen and Shanghai commercial practice | Mixed-use efficiency, public realm at podium |
| Courtyard and climate | Lingnan and Jiangnan courtyard traditions read through modern codes | Ventilation, shading, and site grain |
| Infrastructural urbanism | Metro depot and TOD upper-development projects | Programme stacking over transit |
| Social housing standardisation | Local 保障房 modules and prefabrication policy | Repetition, cost, and assembly ratio |

Theorists often cited in Mainland schools (Frampton on critical regionalism, Koolhaas on density) are discussion tools. Do not treat them as 控规.

## 2. Quantitative Rules of Thumb

These are coordination defaults, not code limits. Confirm the project city and the current general code before calling anything compliant.

### 2.1 Floor-to-floor heights

| Type | Coordination default | Check in |
|------|----------------------|----------|
| Residential | About 2.9–3.0 m floor-to-floor | GB 55031 and the local residential code |
| Office | About 4.0–4.5 m slab-to-slab | Raised floor and services zone |
| Retail podium | About 4.5–6.0 m | Tenant services and fire compartment |
| Basement car park | Clear height set by the local garage code and services | Do not assume a Hong Kong BO figure |
| Plant | Project-specific | Coordinate with MEP before freezing structure |

### 2.2 Development intensity

There is no national plot-ratio table that replaces 控规. Read, in order:

1. 控制性详细规划 for the plot.
2. 国有建设用地使用权出让合同.
3. Planning permit and any adjustment approval.
4. Local urban-design guidelines if they bind.

Metrics: 容积率, 建筑密度, 绿地率, 建筑限高, setbacks, and 日照. Missing any one of these is a halt for a massing conclusion (`cn-spatial-planning`).

### 2.3 Area language

- Use 建筑面积 under GB/T 50353 and the area rules in GB 55031.
- 计容 versus 不计容 is a local planning rule. Do not apply Hong Kong GFA exemption lists.
- State the city before concluding that a balcony, refuge floor, or equipment floor is excluded.

### 2.4 Fire and access

- Mandatory fire floor: GB 55037-2022. GB 50016 applies only where it does not conflict.
- Mandatory access floor: GB 55019-2021. GB 50763 is the detailed recommended standard where it does not conflict.
- Do not quote a travel distance, stair width, or ramp slope from memory. Open the official table or mark the number unverified.

### 2.5 Environmental performance

- Mandatory energy floor: GB 55015-2021.
- Acoustic, light, and thermal baselines: GB 55016-2021.
- Green-building stars are a rating choice under GB/T 50378 plus local rules, not an automatic permit condition.

## 3. Stage Language

| Stage | Purpose | Not the same as |
|-------|---------|-----------------|
| 方案设计 | Massing and planning alignment | 施工图 |
| 初步设计 | Systems and budget | Tender issue, unless the contract says so |
| 施工图设计 | Coordinated production information | 审图合格 |
| 施工图审查 | Third-party mandatory review | Authority planning approval |
| 施工许可 | Legal start of construction | Site possession alone |
| 消防验收 or 备案抽查 | Fire closeout | Contract practical completion |
| 竣工联合验收 / 备案 | Multi-department completion | Defect-liability certificate |

## 4. Units and Defaults

- Area in m². Land area may also be stated in 亩 (1 亩 = 666.7 m²) when the land contract uses it.
- Levels in metres. State the vertical datum the survey uses.
- If the city is unknown: national baseline only, and list the local supplement as a gap.

## 5. Routing Reminder

Load the specialist with `load_sub_skill` per master §8. This file is not a second router.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [cn-human-scale-dimensions.md](../../references/cn-human-scale-dimensions.md) — anthropometric coordination
* [GB_55031_2022_Civil_Buildings_CS.md](../../../cn_s_reference/MOHURD/summaries/GB_55031_2022_Civil_Buildings_CS.md) — civil-buildings general code digest
