---
name: cn-architect-foundations
description: >
  Provides thin Mainland China context defaults (regulatory hierarchy, stage language, units) when
  architecture queries need baseline framing. Use only when the master router is not already active;
  for routing and compliance, use mainland-architect-master in SKILL.md instead.
user-invocable: false
auto-activate: false
disable-model-invocation: true
---

# Mainland Architect Foundations (Thin Layer)

**Orchestration:** The master router [`SKILL.md`](../../SKILL.md) (`mainland-architect-master`) owns identity, halt rules, cognitive workflow, and the full sub-skill table. This module does not duplicate that content.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Any routed domain task | `cn-architect-foundations` | `mainland-architect-master (SKILL.md)` |
| Deep compliance | `cn-architect-foundations` | `cn-building-codes` |
## Defaults (if master not loaded)

- National baseline first (`GB` / `GB-T` / `JGJ`), then local `DB` / `DGJ` / `DBJ`.
- Stages: 方案设计 → 初步设计 → 施工图设计 → 施工配合 → 竣工联合验收/备案.
- Units: `m²`, `亩`; state assumptions when city is unknown.

Load specialized modules via `load_sub_skill` per master §8.
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
