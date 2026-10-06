"""One-off maintainer script: inject 'When to Use This Skill' tables into cn-* sub-skills."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "mainland-architect-master" / "subskills"

# skill_id -> list of (question, this_skill, use_instead)
ROUTING = {
    "cn-accessibility-design": [
        ("GB 50763 and accessibility design", "cn-accessibility-design", "cn-building-codes"),
        ("Planning indicators only", "cn-accessibility-design", "cn-spatial-planning"),
        ("审图 drawing package structure", "cn-accessibility-design", "cn-construction-documentation"),
    ],
    "cn-acoustic-design": [
        ("Acoustic criteria and layout", "cn-acoustic-design", "cn-building-services"),
        ("Code hierarchy for building", "cn-acoustic-design", "cn-building-codes"),
    ],
    "cn-alterations-additions": [
        ("Fit-out / alteration approvals", "cn-alterations-additions", "cn-minor-works"),
        ("Unauthorized works enforcement", "cn-alterations-additions", "cn-unauthorised-building-works"),
        ("Full new-build codes", "cn-alterations-additions", "cn-building-codes"),
    ],
    "cn-architect-calculator": [
        ("Egress/area numeric pre-check", "cn-architect-calculator", "cn-fire-life-safety"),
        ("Fire strategy narrative", "cn-architect-calculator", "cn-fire-life-safety"),
        ("Planning FAR check", "cn-architect-calculator", "cn-spatial-planning"),
    ],
    "cn-architect-foundations": [
        ("Any routed domain task", "cn-architect-foundations", "mainland-architect-master (SKILL.md)"),
        ("Deep compliance", "cn-architect-foundations", "cn-building-codes"),
    ],
    "cn-building-codes": [
        ("控规 / FAR / red lines", "cn-building-codes", "cn-spatial-planning"),
        ("Fire egress strategy", "cn-building-codes", "cn-fire-life-safety"),
        ("Numeric egress/area only", "cn-building-codes", "cn-architect-calculator"),
    ],
    "cn-building-envelope": [
        ("Façade / envelope performance", "cn-building-envelope", "cn-material-selection"),
        ("MEP plant coordination", "cn-building-envelope", "cn-building-services"),
    ],
    "cn-building-programming": [
        ("Functional brief and areas", "cn-building-programming", "cn-building-typology"),
        ("Planning compliance", "cn-building-programming", "cn-spatial-planning"),
    ],
    "cn-building-services": [
        ("MEP coordination", "cn-building-services", "cn-structural-systems"),
        ("Fire systems acceptance", "cn-building-services", "cn-fire-acceptance-closeout"),
    ],
    "cn-building-sustainability": [
        ("Green / 双碳 / 三星", "cn-building-sustainability", "cn-building-codes"),
        ("Energy modelling detail", "cn-building-sustainability", "cn-building-envelope"),
    ],
    "cn-building-typology": [
        ("Typology and standard floors", "cn-building-typology", "cn-concept-design"),
        ("Code applicability", "cn-building-typology", "cn-building-codes"),
    ],
    "cn-cashflow-debt-recovery": [
        ("Invoicing and collections", "cn-cashflow-debt-recovery", "cn-fee-proposal-strategy"),
        ("Contract variations", "cn-cashflow-debt-recovery", "cn-tender-contract-administration"),
    ],
    "cn-certificate-of-compliance": [
        ("Filing and land-condition closeout", "cn-certificate-of-compliance", "cn-op-submission-strategy"),
        ("Snagging / DLP", "cn-certificate-of-compliance", "cn-practical-completion-snagging"),
        ("Fire test evidence", "cn-certificate-of-compliance", "cn-fire-acceptance-closeout"),
    ],
    "cn-concept-design": [
        ("Scheme massing and concept", "cn-concept-design", "cn-spatial-planning"),
        ("Design theory critique", "cn-concept-design", "cn-design-theory"),
    ],
    "cn-construction-documentation": [
        ("审图 package and comment closure", "cn-construction-documentation", "cn-building-codes"),
        ("Approval programme", "cn-construction-documentation", "cn-consent-scheduling"),
    ],
    "cn-consent-scheduling": [
        ("Approval timeline / critical path", "cn-consent-scheduling", "cn-op-submission-strategy"),
        ("Post-permit mobilisation / 占道", "cn-consent-scheduling", "cn-site-establishment"),
        ("Code interpretation", "cn-consent-scheduling", "cn-building-codes"),
    ],
    "cn-daylighting-design": [
        ("Daylight and shading", "cn-daylighting-design", "cn-spatial-planning"),
        ("日照 regulatory analysis", "cn-daylighting-design", "cn-spatial-planning"),
    ],
    "cn-design-theory": [
        ("Critical design discourse", "cn-design-theory", "cn-concept-design"),
        ("Code compliance", "cn-design-theory", "cn-building-codes"),
    ],
    "cn-fee-proposal-strategy": [
        ("Fee scope and proposal", "cn-fee-proposal-strategy", "cn-tender-contract-administration"),
        ("Cashflow collection", "cn-fee-proposal-strategy", "cn-cashflow-debt-recovery"),
    ],
    "cn-fire-acceptance-closeout": [
        ("消防验收 closeout", "cn-fire-acceptance-closeout", "cn-fire-life-safety"),
        ("Joint acceptance strategy", "cn-fire-acceptance-closeout", "cn-op-submission-strategy"),
        ("Legacy ID cn-fsd-licensing-compliance", "cn-fire-acceptance-closeout", "— (same module)"),
    ],
    "cn-fire-life-safety": [
        ("Fire strategy and GB 50016", "cn-fire-life-safety", "cn-building-codes"),
        ("Egress numeric pre-check", "cn-fire-life-safety", "cn-architect-calculator"),
        ("Acceptance commissioning", "cn-fire-life-safety", "cn-fire-acceptance-closeout"),
    ],
    "cn-heritage-conservation": [
        ("Heritage / 文物 / 历史建筑", "cn-heritage-conservation", "cn-spatial-planning"),
        ("Unauthorized works", "cn-heritage-conservation", "cn-unauthorised-building-works"),
    ],
    "cn-lease-compliance": [
        ("Lease and land-use", "cn-lease-compliance", "cn-spatial-planning"),
        ("Building codes general", "cn-lease-compliance", "cn-building-codes"),
    ],
    "cn-material-selection": [
        ("Materials and fire rating", "cn-material-selection", "cn-fire-life-safety"),
        ("Envelope build-up", "cn-material-selection", "cn-building-envelope"),
    ],
    "cn-mic-dfma": [
        ("MiC / prefabrication", "cn-mic-dfma", "cn-structural-systems"),
        ("Contract delivery model", "cn-mic-dfma", "cn-tender-contract-administration"),
    ],
    "cn-minor-works": [
        ("Small works scope", "cn-minor-works", "cn-alterations-additions"),
        ("Full new-build approval", "cn-minor-works", "cn-consent-scheduling"),
    ],
    "cn-op-submission-strategy": [
        ("竣工联合验收 strategy", "cn-op-submission-strategy", "cn-certificate-of-compliance"),
        ("Snagging / PC", "cn-op-submission-strategy", "cn-practical-completion-snagging"),
        ("Fire acceptance evidence", "cn-op-submission-strategy", "cn-fire-acceptance-closeout"),
    ],
    "cn-practical-completion-snagging": [
        ("DLP and snagging", "cn-practical-completion-snagging", "cn-tender-contract-administration"),
        ("Authority filing", "cn-practical-completion-snagging", "cn-certificate-of-compliance"),
    ],
    "cn-professional-indemnity": [
        ("PI insurance and liability", "cn-professional-indemnity", "cn-tender-contract-administration"),
        ("Contract legal interpretation", "cn-professional-indemnity", "— (halt; legal counsel)"),
    ],
    "cn-project-resource-levelling": [
        ("Staffing and peaks", "cn-project-resource-levelling", "cn-consent-scheduling"),
        ("Fee and scope", "cn-project-resource-levelling", "cn-fee-proposal-strategy"),
    ],
    "cn-site-supervision": [
        ("Site supervision / RFI", "cn-site-supervision", "cn-tender-contract-administration"),
        ("Construction sequence / 穿插", "cn-site-supervision", "cn-construction-programme"),
        ("Site safety / 危大工程", "cn-site-supervision", "cn-construction-health-safety"),
        ("Acceptance closeout", "cn-site-supervision", "cn-op-submission-strategy"),
    ],
    "cn-spatial-planning": [
        ("Planning indicators / 控规", "cn-spatial-planning", "cn-building-codes"),
        ("Fire egress", "cn-spatial-planning", "cn-fire-life-safety"),
    ],
    "cn-structural-systems": [
        ("Structural system selection", "cn-structural-systems", "cn-building-codes"),
        ("Seismic / foundation detail", "cn-structural-systems", "cn-building-codes"),
    ],
    "cn-tender-contract-administration": [
        ("Procurement route / EPC vs traditional", "cn-tender-contract-administration", "cn-procurement-strategy"),
        ("Cost plan / BoQ measurement", "cn-tender-contract-administration", "cn-cost-consultancy"),
        ("Contract / variations", "cn-tender-contract-administration", "cn-fee-proposal-strategy"),
        ("Site supervision", "cn-tender-contract-administration", "cn-site-supervision"),
    ],
    "cn-unauthorised-building-works": [
        ("违建认定与整改", "cn-unauthorised-building-works", "cn-alterations-additions"),
        ("Planning regularization", "cn-unauthorised-building-works", "cn-spatial-planning"),
    ],
    "cn-plan-of-work": [
        ("Stage gates / GB/T 50326", "cn-plan-of-work", "cn-deliverables-workstages"),
        ("Issue pack / transmittal", "cn-plan-of-work", "cn-deliverables-workstages"),
        ("Approval timeline", "cn-plan-of-work", "cn-consent-scheduling"),
        ("Project delivery plan", "cn-plan-of-work", "cn-project-management"),
    ],
    "cn-deliverables-workstages": [
        ("Deliverables register / issue pack", "cn-deliverables-workstages", "cn-plan-of-work"),
        ("Stage gate only", "cn-deliverables-workstages", "cn-plan-of-work"),
        ("审图 package", "cn-deliverables-workstages", "cn-construction-documentation"),
        ("PM delivery plan", "cn-deliverables-workstages", "cn-project-management"),
    ],
    "cn-project-management": [
        ("Delivery plan / client reporting", "cn-project-management", "cn-plan-of-work"),
        ("Stage checklist only", "cn-project-management", "cn-plan-of-work"),
        ("Contract variations", "cn-project-management", "cn-tender-contract-administration"),
        ("Cost plan / BoQ", "cn-project-management", "cn-cost-consultancy"),
    ],
    "cn-procurement-strategy": [
        ("Procurement route / EPC vs traditional", "cn-procurement-strategy", "cn-tender-contract-administration"),
        ("Tender / CA duties", "cn-procurement-strategy", "cn-tender-contract-administration"),
        ("Cost plan", "cn-procurement-strategy", "cn-cost-consultancy"),
        ("Approval programme", "cn-procurement-strategy", "cn-consent-scheduling"),
    ],
    "cn-cost-consultancy": [
        ("Cost plan / BoQ / 概算预算", "cn-cost-consultancy", "cn-tender-contract-administration"),
        ("Procurement route", "cn-cost-consultancy", "cn-procurement-strategy"),
        ("Fee proposal", "cn-cost-consultancy", "cn-fee-proposal-strategy"),
    ],
    "cn-site-establishment": [
        ("Mobilisation / 三通一平 / 占道", "cn-site-establishment", "cn-consent-scheduling"),
        ("施工许可证 timeline", "cn-site-establishment", "cn-consent-scheduling"),
        ("Traffic TMP", "cn-site-establishment", "cn-traffic-coordination"),
        ("Telecom diversion", "cn-site-establishment", "cn-telecom-coordination"),
    ],
    "cn-traffic-coordination": [
        ("TIA / 交警 / TMP", "cn-traffic-coordination", "cn-site-establishment"),
        ("控规 / planning", "cn-traffic-coordination", "cn-spatial-planning"),
        ("Construction programme", "cn-traffic-coordination", "cn-construction-programme"),
    ],
    "cn-telecom-coordination": [
        ("三大运营商 / 管线迁改", "cn-telecom-coordination", "cn-site-establishment"),
        ("General mobilisation", "cn-telecom-coordination", "cn-site-establishment"),
        ("MEP design", "cn-telecom-coordination", "cn-building-services"),
    ],
    "cn-construction-programme": [
        ("Sequence / 穿插 / 标准层", "cn-construction-programme", "cn-site-supervision"),
        ("Site RFI", "cn-construction-programme", "cn-site-supervision"),
        ("Approval programme", "cn-construction-programme", "cn-consent-scheduling"),
    ],
    "cn-construction-health-safety": [
        ("Site safety / 危大工程", "cn-construction-health-safety", "cn-fire-life-safety"),
        ("Fire egress design", "cn-construction-health-safety", "cn-fire-life-safety"),
        ("Site supervision", "cn-construction-health-safety", "cn-site-supervision"),
    ],
}

MARKER = "## When to Use This Skill"


def build_table(skill_id: str, rows: list) -> str:
    lines = [
        MARKER,
        "",
        "| Question type | This skill | Use instead |",
        "|---------------|------------|-------------|",
    ]
    for q, this, instead in rows:
        lines.append(f"| {q} | `{this}` | `{instead}` |")
    lines.append("")
    return "\n".join(lines)


def inject(content: str, table: str) -> str:
    if MARKER in content:
        # Replace existing section up to next ## or end
        start = content.index(MARKER)
        rest = content[start + len(MARKER) :]
        next_h2 = rest.find("\n## ")
        if next_h2 == -1:
            return content[:start] + table
        return content[:start] + table + rest[next_h2 + 1 :]

    # Insert after closing frontmatter and first heading block (after first --- following title)
    parts = content.split("---", 2)
    if len(parts) >= 3 and parts[0].strip().startswith("---"):
        # parts[0] empty, parts[1] yaml, parts[2] body
        body = parts[2]
        if body.startswith("\n"):
            body = body[1:]
        # After first # heading line and optional intro paragraph ending before ---
        lines = body.splitlines()
        insert_at = 0
        for i, line in enumerate(lines):
            if line.startswith("# "):
                insert_at = i + 1
                break
        # Skip blank lines and one intro line block until --- or ##
        while insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1
        if insert_at < len(lines) and not lines[insert_at].startswith("##"):
            while insert_at < len(lines) and not lines[insert_at].startswith("##") and lines[insert_at].strip() != "---":
                insert_at += 1
        new_body = "\n".join(lines[:insert_at]) + "\n\n" + table + "\n" + "\n".join(lines[insert_at:])
        return "---" + parts[1] + "---\n" + new_body
    # Fallback: after first line
    return content + "\n\n" + table


def main():
    for skill_id, rows in ROUTING.items():
        path = ROOT / skill_id / f"{skill_id}.md"
        if not path.exists():
            print(f"SKIP missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        table = build_table(skill_id, rows)
        path.write_text(inject(text, table), encoding="utf-8")
        print(f"OK {skill_id}")


if __name__ == "__main__":
    main()
