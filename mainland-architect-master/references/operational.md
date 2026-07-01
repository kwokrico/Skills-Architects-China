# Operational SOPs — Mainland Architect Suite

## Intake checklist (Phase 1)

Before deep analysis, confirm or request:

- Project city and district
- Current stage: 方案 / 初设 / 施工图 / 施工 / 验收
- Building typology and approximate scale
- Available drawings or indicator tables (红线, 控规, 出让条件)
- Whether 施工图审查 or 消防专项已 issued comments

## Escalation paths

| Situation | Escalate to |
|-----------|-------------|
| Cross-discipline fire/MEP conflict | 专业负责人 + fire sub-skill |
| Planning indicator dispute | 规自局 alignment + `cn-spatial-planning` |
| Contract variation with cost impact | `cn-tender-contract-administration` + `cn-cost-consultancy` + client commercial team |
| Site safety / 危大工程 incident | `cn-construction-health-safety` + contractor safety officer + 安监 |
| Traffic / 占道 dispute | `cn-traffic-coordination` + municipal liaison |
| Telecom plant damage risk | `cn-telecom-coordination` + carrier protection contractor |
| Heritage or conservation controls | `cn-heritage-conservation` + authority pre-consultation |
| Unauthorized works risk | `cn-unauthorised-building-works` + legal survey |

## Review gates

1. **Scheme gate:** indicators + red lines + fire strategy feasibility
2. **Preliminary gate:** system selection + budget alignment
3. **Construction drawing gate:** 审图闭环 complete before 施工许可证 dependency claims
4. **Acceptance gate:** evidence index ready before 竣工联合验收 booking

## Artifact naming

- Use revision codes aligned with project BIM/document control
- Prefix outputs with stage tag: `方案-`, `初设-`, `施工图-`, `验收-`
- Store calculator runs with `calc_type`, `city_context`, and assumption block

## Dispatcher usage

- `load_sub_skill`: use when topic exceeds master quick reference
- `run_arch_calculator`: use for egress and area roll-ups; always attach disclaimer from `translation_map` city context
