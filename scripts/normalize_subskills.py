"""Normalize subskill frontmatter and references footers per GUIDELINE.md."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "mainland-architect-master" / "subskills"

REFERENCES_FOOTER = """
## References

Load from parent `references/` when needed (one hop):

* [compliance.md](../../references/compliance.md) — non-negotiable rules
* [operational.md](../../references/operational.md) — intake and escalation
* [domain_terms.json](../../references/domain_terms.json) — vocabulary
* [templates/](../../references/templates/) — output structures
"""

HERITAGE_EXTRA = "* [heritage-impact-checklist.md](../../references/heritage-impact-checklist.md) — impact assessment checklist\n"


def normalize_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("---", 3)
    if end == -1:
        return text
    fm = text[3:end].strip()
    body = text[end + 3 :].lstrip("\n")
    if "disable-model-invocation:" not in fm:
        fm += "\ndisable-model-invocation: true"
    return f"---\n{fm}\n---\n\n{body}"


def add_references_footer(text: str, skill_id: str) -> str:
    if "## References" in text:
        return text
    footer = REFERENCES_FOOTER
    if skill_id == "cn-heritage-conservation":
        footer = footer.replace(
            "* [templates/](../../references/templates/) — output structures\n",
            "* [templates/](../../references/templates/) — output structures\n" + HERITAGE_EXTRA,
        )
    return text.rstrip() + footer


def main():
    for path in sorted(ROOT.glob("cn-*/*.md")):
        original = path.read_text(encoding="utf-8")
        updated = normalize_frontmatter(original)
        updated = add_references_footer(updated, path.parent.name)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT.parent)}")


if __name__ == "__main__":
    main()
