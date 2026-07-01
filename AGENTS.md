# Agent instructions — Skills-Architect-China

## Professional skill activation

When the user's request involves **Mainland China** architectural practice—planning indicators (容积率/建筑密度/绿地率), GB/GB-T/JGJ codes, 施工图审查, 消防验收, 竣工联合验收, design delivery, contracts, or site supervision—read and follow:

[`mainland-architect-master/SKILL.md`](mainland-architect-master/SKILL.md) (`mainland-architect-master`)

Include:

- Sub-skill routing per master §5A–§8 (`load_sub_skill` or `subskills/cn-*/`) — **45 sub-skills** (HK blueprint parity; `cn-fire-acceptance-closeout` replaces legacy FSD licensing)
- Compliance halt rules in [`mainland-architect-master/references/compliance.md`](mainland-architect-master/references/compliance.md)
- Operational intake in [`mainland-architect-master/references/operational.md`](mainland-architect-master/references/operational.md)
- Terms in [`mainland-architect-master/references/domain_terms.json`](mainland-architect-master/references/domain_terms.json)
- Output templates in [`mainland-architect-master/references/templates/`](mainland-architect-master/references/templates/) when the user needs submission tables

## Dispatcher (optional)

For programmatic load or calculators, use [`mainland-architect-master/scripts/dispatcher.py`](mainland-architect-master/scripts/dispatcher.py) (or root [`mainland-architect-master/main.py`](mainland-architect-master/main.py) shim):

- `load_sub_skill` with `skill_id` (`cn-*` or legacy `hk-*`)
- `run_arch_calculator` with `calc_type`: `egress_gb50016`, `building_area_gbt50353`, `layout_sort`

## Verification

See [`mainland-architect-master/docs/golden-questions.md`](mainland-architect-master/docs/golden-questions.md) and [`mainland-architect-master/evals/evals.json`](mainland-architect-master/evals/evals.json) for expected routing and halt behaviors.
