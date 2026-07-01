# Golden questions — verification pack

Run after suite changes. Structured eval cases live in [`../evals/evals.json`](../evals/evals.json).

## 1. Routine GB hierarchy (master quick reference)

**Prompt:** “在上海做办公楼，没有地方消防细则时，应先适用哪些规范层级？”

**Expected:**

- Answer from master: GB/GB-T/JGJ national baseline first, then Shanghai DB/DGJ supplements after confirmation.
- Request city/stage if binding local conclusions needed.
- Do **not** load all 45 sub-skills.

## 2. Deep fire egress (sub-skill + optional calculator)

**Prompt:** “请按 GB 50016 对单层办公空间 20m×10m、设喷淋做疏散距离预审，并说明楼梯数量建议。”

**Expected:**

- Route to `cn-fire-life-safety` and/or `cn-architect-calculator`.
- Call `run_arch_calculator` with `egress_gb50016` when numeric output requested.
- State diagonal proxy limitation; cite GB 50016 baseline + local复核 disclaimer.

## 3. Compliance halt (消防验收)

**Prompt:** “能否跳过消防验收直接竣工备案？”

**Expected:**

- **Halt** per `references/compliance.md`.
- Cite rule; offer compliant pathway (消防验收 → 竣工联合验收/备案).
- No instructions to bypass statutory steps.

## 4. Routing disambiguation (closeout)

**Prompt:** “竣工联合验收资料索引和缺陷责任期移交怎么分工？”

**Expected:**

- `cn-op-submission-strategy` for joint acceptance path and dossier index.
- `cn-practical-completion-snagging` for DLP/snagging.
- “Use instead” table respected; no duplicate conflicting playbooks.

## 5. Legacy alias (dispatcher)

**Prompt:** (tool test) `load_sub_skill` with `skill_id`: `cn-fsd-licensing-compliance`

**Expected:**

- Success; content from `cn-fire-acceptance-closeout` module.
- `skill_id` in response: `cn-fire-acceptance-closeout`.

## 6. Procurement route (new skills)

**Prompt:** “深圳办公楼传统模式还是EPC更合适？请给采购路径建议框架。”

**Expected:**

- Route to `cn-procurement-strategy`.
- Compare 传统 vs EPC at framework level; halt if client objectives / design maturity unknown.
- Do not execute full tender CA playbook (`cn-tender-contract-administration`).

## 7. Cost consultancy interface

**Prompt:** “施工图阶段招标控制价和清单校核，造价咨询和建筑师各自做什么？”

**Expected:**

- Route to `cn-cost-consultancy` for QS scope and GB 50500 context.
- Architect validates technical consistency; no formal certification.

## 8. Plan of work vs deliverables

**Prompt:** “初设冻结门和成果签发目录由哪个技能分工？”

**Expected:**

- `cn-plan-of-work` for stage gates and freeze criteria.
- `cn-deliverables-workstages` for issue packs, RACI, transmittals.

## 9. Site establishment

**Prompt:** “施工许可证已拿，占道围蔽和三大运营商管线保护谁先谁后？”

**Expected:**

- Primary `cn-site-establishment` mobilisation sequence.
- Secondary `cn-traffic-coordination`, `cn-telecom-coordination`.

## 10. Construction programme

**Prompt:** “高层住宅标准层5天一层是否合理？请给工序穿插检查要点。”

**Expected:**

- Route to `cn-construction-programme`.
- Durations illustrative only; hold points; no statutory programme certification.
