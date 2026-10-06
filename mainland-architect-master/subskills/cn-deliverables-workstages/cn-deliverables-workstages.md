---
name: cn-deliverables-workstages
description: Defines Mainland design deliverables by approval stage, issue-pack discipline, transmittals, and lead-consultant RACI from scheme design through handover.
user-invocable: true
disable-model-invocation: true
---

# Mainland Deliverables by Workstage

Defines what is issued, to whom, and at what status. Stage-gate checklists live in `cn-plan-of-work`. This skill owns the issue pack.

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Issue packs, transmittals, drawing status, RACI | `cn-deliverables-workstages` | `cn-plan-of-work` |
| Whether the stage may freeze | `cn-deliverables-workstages` | `cn-plan-of-work` |
| 审图 comment wording | `cn-deliverables-workstages` | `cn-construction-documentation` |

## 0. Deliverables Must Always Be Issue-Pack Ready

An issue pack contains:

1. Cover note: project, stage, purpose, revision, and "not for construction" or "for construction" status.
2. Drawing and document register with revision, date, author, and scale.
3. The files themselves, named to match the register.
4. Open-issues list and assumptions.
5. Distribution list.

Do not send a loose WeChat image as the contract or submission set. File the formal pack the same day.

## 1. Stakeholder Groups and What "Good" Looks Like

| Recipient | Good pack |
|-----------|-----------|
| Client / 建设单位 | Decision sheet, cost and programme flags, options closed |
| 规自局 | Indicator table, red-line drawings, 日照 if required |
| 审图机构 | Full 施工图 set, calculation index, response-to-comments matrix |
| 住建 / 施工许可 | 审图合格 evidence, consultant seals as required by the city |
| Contractor / 监理 | Construction status drawings, specification, RFI channel |
| Cost consultant | Measured scope basis and change cloud |
| Facilities / 物业 | As-built, O&M, training, spare parts |

Authority names vary by city. Use [cn-construction-stakeholder-register.md](../../references/cn-construction-stakeholder-register.md).

## 2. Workstages and Deliverable Definition

### Stage A — Brief / Feasibility

- Site facts, red-line status, 控规 extract, target 容积率 / 密度 / 绿地率 / 限高.
- Area brief and constraints log.
- Risk note: missing city supplements, heritage, airport, flood.
- Not a statutory submission.

### Stage B — 方案设计

- Massing, site plan, typical floors, elevations, area schedule against 控规.
- Planning-indicator check from `references/templates/planning-indicator-check.md`.
- Concept structure and MEP strategy in one-page form.
- Status: "for planning discussion" until the client freezes the option.

### Stage C — 初步设计

- Coordinated plans, sections, elevations, outline specification.
- System descriptions (structure, envelope, fire strategy principle, MEP).
- Cost-plan basis for the cost consultant.
- Interdisciplinary clash list with owners and due dates.
- Status: "for preliminary approval / budget", not for construction.

### Stage D — Statutory and review submissions

- Planning drawing set and statements required by the local 规自局.
- 施工图 set for 审图, including the response matrix `references/templates/review-comment-response.md`.
- Fire design content aligned with GB 55037 / GB 50016 as applicable (`cn-fire-life-safety`).
- Do not mark the pack "approved" before the authority or 审图机构 says so.

### Stage E — Tender documentation

- Tender drawings, specification, schedule of provisional items.
- Interface matrix and employer's requirements if EPC.
- Register states the 审图 revision the tender is based on.
- Route commercial content to `cn-tender-contract-administration`.

### Stage F — Construction information

- "For construction" revision after tender-award addenda.
- Shop-drawing review status (reviewed / reviewed with comments / rejected).
- RFI log. Site sketches get a revision number within two working days.
- Hold points that affect sequence go to `cn-construction-programme`.

### Stage G — Completion evidence

- Record drawings, test index, fire acceptance dossier pointer (`cn-fire-acceptance-closeout`).
- 规划核实 drawing set (`cn-certificate-of-compliance`).
- Joint-acceptance index `references/templates/joint-acceptance-index.md`.
- Contract completion is separate from statutory acceptance.

### Stage H — Handover

- As-built model or CAD, O&M manuals, training records, spare-parts schedule.
- Warranty start dates by system.
- Unresolved snags listed, not hidden.

### Stage I — Defect-liability closeout

- Snag register with close dates.
- Final account information for the cost consultant.
- Statutory 保修 periods stated separately from the contract defect-liability period.

## 3. Delivery Reference Table

| Pack ID | Stage | Purpose | Status word | Primary owner |
|---------|-------|---------|-------------|---------------|
| IP-A | Brief | Decision to proceed | Information | Project manager |
| IP-B | 方案 | Planning alignment | For discussion | Architect |
| IP-C | 初设 | Budget and systems | For coordination | Lead consultant |
| IP-D | 审图 | Mandatory review | For review | Architect of record |
| IP-E | Tender | Price | For tender | Architect + QS |
| IP-F | Site | Build | For construction | Architect |
| IP-G | Acceptance | Statutory closeout | Record | Lead consultant |
| IP-H | Handover | Operate | As-built | Architect |
| IP-I | DLP | Close | Defects | Contract administrator |

## 4. How to Present Deliverables

- One purpose per transmittal. Do not mix tender and construction status.
- Cloud changes and list them in the cover note.
- Chinese drawing titles and numbers follow the project standard; English may be added, not substituted, when the authority requires Chinese.
- Superseded files are marked superseded in the register the same day.
- Model issues state the federated version and which discipline is included.

## 5. Drawing Scale Guidance

| Drawing | Typical scale | Note |
|---------|---------------|------|
| Location / context | 1:500–1:2000 | North point, red line, site boundary |
| Site plan | 1:200–1:500 | 用地红线 and 建筑红线 labelled |
| Floor plan | 1:100 (1:50 for toilets, cores) | Dimensions to structure grids |
| Section / elevation | 1:100–1:200 | Levels in metres |
| Detail | 1:5–1:20 | Material and waterproofing principle |
| Fire compartment plan | 1:100 | Compartment boundaries and exits readable at print size |

Scales are coordination practice, not a code clause. Follow the local 审图 drawing-depth guide when the city publishes one.

## 6. Lead Consultant Coordination

### 6.1 Consultant team RACI

| Activity | Lead consultant | Architecture | Structure | MEP | QS | 监理 |
|----------|-----------------|--------------|-----------|-----|----|------|
| Stage freeze | A | R | C | C | C | I |
| Issue pack | A | R | R | R | C | I |
| 审图 response | A | R | R | R | I | I |
| Cost plan | C | C | C | C | A/R | I |
| Site instruction | C | R | C | C | C | A if contract says so |

R = responsible, A = accountable, C = consulted, I = informed. Replace the last column with the contract administrator when 监理 is not that person.

### 6.2 Meeting cadence

- Design stages: weekly coordination, fortnightly client.
- 审图: comment workshop within three working days of receipt.
- Construction: weekly site meeting plus a design-information meeting if RFIs exceed the agreed backlog.

### 6.3 Progress reports

One page: stage, decisions needed, issues, change log count, information due in the next two weeks, and cost/programme flags from others. No unexplained "percent complete".

### 6.4 Client instructions

Write them into the decision log. A meeting comment is not an instruction until the client confirms scope, quality, and that cost/time may change.

### 6.5 Stage-freeze change control

Freeze means the issue pack revision is the baseline. Later changes get a change number, a drawing cloud, and a cost/time flag before the next stage starts. Do not silently edit a frozen 方案 after planning submission.

### 6.6 Value management

Workshops at the end of 方案 and 初设. Record options rejected. VM does not override mandatory codes or 控规.

### 6.7 Procurement and contract advice

Recommend the route via `cn-procurement-strategy`. Do not draft particular conditions that shift statutory design responsibility.

### 6.8 QS deliverables by stage

| Stage | QS output the architect must enable |
|-------|-------------------------------------|
| 方案 | Area schedule and system options |
| 初设 | Outline spec and major quantities drivers |
| 施工图 / tender | Stable drawing revision for measurement |
| Construction | Change log and revised details |
| Closeout | As-built status for the final account |

### 6.9 Designer duties index

- Massing and brief: `cn-concept-design`, `cn-building-programming`.
- Production information: `cn-construction-documentation`.
- Site establishment: `cn-site-establishment`.
- Checking work on site: `cn-site-supervision`.

### 6.10 Plan of work versus deliverables

`cn-plan-of-work` says whether the gate is open. This skill says what is inside the pack. Use both.

## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
* [stage-gate-checklist.md](../../references/templates/stage-gate-checklist.md) — gate shell
* [deliverables.md](../../references/templates/deliverables.md) — transmittal shell
* [Construction_Drawing_Review_Measures_CS.md](../../../cn_s_reference/MOHURD/summaries/Construction_Drawing_Review_Measures_CS.md) — drawing-review digest
