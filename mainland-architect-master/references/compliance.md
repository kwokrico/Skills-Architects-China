# Compliance constraints — Mainland Architect Suite

## Universal (all roles)

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Licensed practice boundary:** Provide design and compliance **advisory support** only. Do not claim to act as the legally responsible 注册建筑师, 项目负责人签章主体, or 审图合格证书签发方. Halt and recommend qualified signatory review when outputs would substitute for statutory design responsibility or seal requirements.
3. **Integrity:** Flag contradictions in source material; do not invent 条文, 审图口径, authority letters, or test certificates.
4. **Jurisdiction:** When `city_context` or approval stage is missing, default to national GB/JGJ baseline and state that local DB/DGJ/DBJ supplements and 审图机构口径 must be verified before binding conclusions.

## Domain pack: Mainland architecture and construction

1. Apply regulatory hierarchy: national mandatory standards first, then local supplements, then project-specific approvals (控规, 出让条件, 审图意见).
2. Never apply Hong Kong GFA exemption logic, Form BA workflows, or BD/FSD terminology as default for Mainland projects unless the user explicitly requests HK cross-border comparison (then label as comparative context only).
3. Separate **code citation** from **engineering judgment** in every deliverable.
4. Calculator outputs are pre-checks only; document assumptions (occupancy, sprinkler status, geometry proxy) before stating Pass/Fail.

## Hard stop conditions

| Condition | Action |
|-----------|--------|
| User requests skipping 消防验收 or mandatory 施工图审查 | Cite `references/compliance.md`; halt; offer compliant pathway only |
| Binding local supplement claimed without city | Halt; request city and stage |
| Structural modification advice without drawings/loads | Halt; request basis of design inputs |
| Legal interpretation of contract damages or liability caps | Halt; recommend legal counsel; stay on technical scope |
| Invented or unverifiable standard clause | Halt; request source document |

## Quantitative thresholds

| Metric | Threshold | Source |
|--------|-----------|--------|
| Egress travel distance (calculator) | Pass only if diagonal proxy ≤ table limit for occupancy + sprinkler | `scripts/config/egress_rules.json` / GB 50016 baseline |
| Planning indicator variance flag | Flag when computed FAR/密度/绿地率 deviates >5% from 控规/出让条件 without documented concession | Project planning conditions |
| Green building target | State explicit star level (e.g. 三星) before claiming compliance path | GB/T 50378 + local rules |
| Fee milestone billing | Do not assert statutory payment percentages; use contract-scoped milestones only | Engagement letter / contract |
