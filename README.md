# Mainland Architect Skills (China)

### A Tier 2 professional skill suite for Mainland China architectural practice

`Skills-Architect-China` is a localized architecture plugin built around one master router (`mainland-architect-master`) and a set of specialist `cn-*` sub-skills. It is tuned for PRC statutory, technical, and delivery workflows: national vs local standards hierarchy (GB/GB-T/JGJ → DB/DGJ/DBJ), planning indicators (容积率/建筑密度/绿地率), 施工图审查 logic, fire and accessibility baselines, and construction-to-acceptance workflows (施工许可证 → 消防验收 → 竣工联合验收/备案).

---

- `mainland-architect-master/SKILL.md`: Main entry skill (`mainland-architect-master`) with routing rules and quick-reference baselines.
- `mainland-architect-master/subskills/`: Domain sub-skills for focused expertise (codes, planning, fire, sustainability, delivery, contract/admin, documentation, etc.).
- `mainland-architect-master/scripts/calculators.py`: Calculation helpers used by calculator workflows.
- `mainland-architect-master/scripts/dispatcher.py`: Runtime entry point for loading sub-skills and tool dispatch.

- [Quick Start](#quick-start)
- [What You Get](#what-you-get)
- [How It Works](#how-it-works)
- [Skill Map](#skill-map)
- [Calculators](#calculators)
- [Folder Structure](#folder-structure)
- [Example Prompts](#example-prompts)
- [Standards and Frameworks](#standards-and-frameworks)
- [Credits](#credits)

---

## Quick Start

### Option 1: Use directly in Claude Desktop

1. Copy or clone this folder into your Claude Desktop skills workspace.
2. Keep the package structure unchanged:
   - `mainland-architect-master/SKILL.md`
   - `mainland-architect-master/subskills/`
   - `mainland-architect-master/scripts/`
   - `mainland-architect-master/references/`
3. Load the skill package from `mainland-architect-master/`.
4. Start a new chat and ask a Mainland China architecture question.

### Option 2: Plugin directory launch

```bash
claude --plugin-dir "/path/to/Skills-Architect-China/mainland-architect-master"
```

### Option 3: Cursor project activation

See [`AGENTS.md`](AGENTS.md) for automatic routing in Cursor.

---

## What You Get

- **1 master router skill**: `mainland-architect-master` in `mainland-architect-master/SKILL.md`
- **A library of `cn-*` sub-skills** across compliance, design, engineering, and delivery
- **Built-in quick-reference layer** for common PRC workflow terms and baselines (GB-first, then local supplements)
- **Calculation support** via `mainland-architect-master/scripts/calculators.py`
- **Structured routing** through `load_sub_skill` and calculator dispatch (`run_arch_calculator`)
- **Eval pack** in `mainland-architect-master/evals/evals.json` with sibling workspace `mainland-architect-master-workspace/`

---

## How It Works

The system follows a progressive flow:

1. **Quick answer first**  
   The master skill uses PRC terminology and a strict hierarchy: national baselines first (GB/GB-T/JGJ), then local supplements (DB/DGJ/DBJ), and always asks for city/stage when needed.

2. **Route to a specialist when needed**  
   For deeper queries, it dispatches to the best-matching sub-skill using `load_sub_skill`.

3. **Run computations for numeric checks**  
   For calculation tasks, it calls calculator workflows through `run_arch_calculator` (legacy `run_hk_calculator` is accepted as a backward-compatible alias and routed internally).

This keeps routine queries fast while preserving deep, domain-specific responses for complex work.

---

## Skill Map

### 1) Regulatory and Statutory

- `cn-building-codes`
- `cn-spatial-planning`
- `cn-fire-life-safety`
- `cn-accessibility-design`
- `cn-minor-works`
- `cn-consent-scheduling`
- `cn-alterations-additions`
- `cn-lease-compliance`
- `cn-unauthorised-building-works`
- `cn-fire-acceptance-closeout` (alias: `cn-fsd-licensing-compliance`)
- `cn-certificate-of-compliance`

### 2) Technical and Performance Design

- `cn-building-sustainability`
- `cn-building-envelope`
- `cn-building-services`
- `cn-structural-systems`
- `cn-acoustic-design`
- `cn-daylighting-design`
- `cn-material-selection`
- `cn-building-programming`
- `cn-building-typology`
- `cn-mic-dfma`

### 3) Design and Documentation

- `cn-concept-design`
- `cn-construction-documentation`
- `cn-design-theory`
- `cn-architect-calculator`

### 4) Delivery, Contract, and Practice Operations

- `cn-site-supervision`
- `cn-tender-contract-administration`
- `cn-fee-proposal-strategy`
- `cn-cashflow-debt-recovery`
- `cn-project-resource-levelling`
- `cn-professional-indemnity`
- `cn-op-submission-strategy`
- `cn-practical-completion-snagging`
- `cn-heritage-conservation`

---

## Calculators

The calculator module currently supports:

- **Egress check** (`egress_gb50016`): travel-distance style compliance logic from room geometry (baseline: GB 50016; verify local amendments)
- **Building area aggregation** (`building_area_gbt50353`): countable vs non-countable building area roll-up logic (baseline: GB/T 50353; verify local amendments)
- **Layout sorting utility** (`layout_sort`): OCR/layout ordering helper by X/Y coordinates

### Optional dependency (schema validation)

If you want schema validation for `mainland-architect-master/scripts/config/translation_map.json`, install:

```powershell
python -m pip install jsonschema
```

If `jsonschema` is not installed, the dispatcher still runs but will skip schema validation and return a warning in `translation_map_status`.

---

## Folder Structure

```text
mainland-architect-master/
├── SKILL.md                      # Master router: mainland-architect-master
├── main.py                       # Backward-compatible shim → scripts/dispatcher.py
├── subskills/
│   └── cn-*/                     # 35 specialist modules
├── references/
│   ├── compliance.md
│   ├── operational.md
│   ├── domain_terms.json
│   ├── config.json
│   ├── heritage-impact-checklist.md
│   └── templates/
├── scripts/
│   ├── dispatcher.py
│   ├── calculators.py
│   └── config/
├── evals/
│   ├── evals.json
│   └── files/
└── docs/
    ├── golden-questions.md
    └── _archive/hk-migration-notes.md

mainland-architect-master-workspace/   # sibling eval outputs (gitignored)
└── iteration-1/
```

Project root: [`AGENTS.md`](AGENTS.md) wires Cursor agents to the master skill.

---

## Example Prompts

- "按 GB/地方 DB 的层级，判断这个项目在上海的主要适用规范清单，并给出审图风险点。"
- "做一个办公楼层的疏散预审：基于房间几何，按 GB 50016 估算疏散距离和楼梯建议。"
- "在方案阶段，容积率/建筑密度/绿地率指标要怎么从控规和出让条件里拆解成可执行检查？"
- "把项目的报批报建流程从 方案→初设→施工图→施工图审查→施工许可证→消防验收→竣工联合验收 梳理成时间线。"
- "请按 GB/T 50353 口径，汇总计容/不计容（如避难空间、开敞阳台等）并输出面积表。"
- "施工阶段出现变更洽商，如何控制风险、界定责任并形成可追溯的审图闭环？"

---

## Standards and Frameworks

This suite is designed around Mainland China practice and frequently references:

- National standards: **GB / GB/T / JGJ** (e.g., `GB 50352`, `GB 50016`, `GB 50763`, `GB/T 50353`, `GB/T 50378`)
- Local supplements: **DB / DGJ / DBJ** and municipal 审查口径 (city-dependent)
- Approval workflow language and checkpoints:
  - `方案设计` → `初步设计` → `施工图设计` → `施工图审查`
  - `施工许可证` → `消防验收` → `竣工联合验收/备案`

Always verify project-specific conditions (控规条文、出让条件、审图意见、主管部门沟通纪要), since those can override rule-of-thumb guidance.

---

## Credits

This project is a Mainland China localization and expansion of the original [Skills-Architects](https://github.com/Amanbh997/Skills-Architects) framework by Abhinav Bhardwaj, adapted for PRC regulations, workflow realities, and delivery practice.
