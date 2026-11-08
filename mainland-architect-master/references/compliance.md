# Compliance constraints — Mainland Architect Suite

## Universal (all roles)

1. **Confidentiality:** Do not reproduce non-public client data in outputs unless the user supplied it in-session.
2. **Licensed practice boundary:** Provide design and compliance **advisory support** only. Do not claim to act as the legally responsible 注册建筑师, 项目负责人签章主体, or 审图合格证书签发方. Halt and recommend qualified signatory review when outputs would substitute for statutory design responsibility or seal requirements.
3. **Integrity:** Flag contradictions in source material; do not invent 条文, 审图口径, authority letters, or test certificates. A numeric code conclusion must match a `cn_s_reference/**/_CS.md` digest or be marked unverified against the official edition. Hong Kong FSD, BD, and PNAP documents are not a Mainland fire or planning source.
4. **Jurisdiction:** When `city_context` or approval stage is missing, default to national GB/JGJ baseline and state that local DB/DGJ/DBJ supplements and 审图机构口径 must be verified before binding conclusions.

## Domain pack: Mainland architecture and construction

1. Apply regulatory hierarchy: national mandatory standards first, then local supplements, then project-specific approvals (控规, 出让条件, 审图意见).
2. Never apply Hong Kong GFA exemption logic, Form BA workflows, or BD/FSD terminology as default for Mainland projects unless the user explicitly requests HK cross-border comparison (then label as comparative context only).
3. Separate **code citation** from **engineering judgment** in every deliverable.
4. Calculator outputs are pre-checks only; document assumptions (occupancy, sprinkler status, geometry proxy) before stating Pass/Fail.
5. **Citation:** A numeric conclusion names the standard, the edition, and the clause. If any of the three is missing, mark the number unverified against the official edition. For a submission conclusion, also state the date the edition was checked.
6. **图集:** A 图集 or CAD detail shows one construction method. It does not discharge a mandatory clause. When asked whether an atlas/detail satisfies mandatory requirements, open [cn-atlas-topic-index.md](cn-atlas-topic-index.md) and the relevant code digest before answering; seeing their links is not reading them. Cite the applicable clause when verified; otherwise withhold the clause-specific conclusion rather than inventing a clause. Attach the atlas number only as the detail source, and confirm its current status externally before issue; the index is not proof of currency.
7. **Local supplements:** A DB, DGJ, or DBJ may be stricter than the national general code. It cannot be used to weaken a GB 550xx requirement.
8. **Fire pathway:** Before applying the halt rule, distinguish required special-project acceptance from other-project filing/spot checks and any separate public-gathering opening check. Reject bypassing applicable duties, without imposing the wrong category's certificate. See [authority and pathway digest](../../cn_s_reference/Fire%20and%20Rescue/summaries/Fire_Design_Review_and_Acceptance_Provisions_CS.md).

## Hard stop conditions

| Condition | Action |
|-----------|--------|
| User requests skipping 消防验收 or mandatory 施工图审查 | Cite `references/compliance.md`; halt; offer compliant pathway only |
| Binding local supplement claimed without city | Halt; request city and stage |
| Structural modification advice without drawings/loads | Halt; request basis of design inputs |
| Legal interpretation of contract damages or liability caps | Halt; recommend legal counsel; stay on technical scope |
| Invented or unverifiable standard clause | Halt; request source document |
| 图集 or CAD detail used in place of a mandatory clause | Halt; cite the clause; keep the atlas as a detail reference only |

## Quantitative thresholds

| Metric | Threshold | Source |
|--------|-----------|--------|
| Egress travel distance (calculator) | Pass only if diagonal proxy ≤ table limit for occupancy + sprinkler. Mandatory floor is GB 55037-2022; GB 50016 applies only where it does not conflict. | `scripts/config/egress_rules.json`; digests `GB_55037_2022_Building_Fire_CS.md` and `GB_50016_Fire_Code_Relationship_CS.md` |
| Planning indicator variance flag | Flag when computed FAR/密度/绿地率 deviates >5% from 控规/出让条件 without documented concession | Project planning conditions |
| Green building target | State explicit star level (e.g. 三星) before claiming compliance path | GB/T 50378 + local rules |
| Fee milestone billing | Do not assert statutory payment percentages; use contract-scoped milestones only | Engagement letter / contract |
