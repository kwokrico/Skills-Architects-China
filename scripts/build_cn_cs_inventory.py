"""Build cn_s_reference/_CS_INVENTORY.md from *_CS.md files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "cn_s_reference"
OUT = ROOT / "_CS_INVENTORY.md"


def title_of(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def main() -> None:
    files = sorted(ROOT.rglob("*_CS.md"))
    by_folder: dict[str, list[Path]] = {}
    for path in files:
        # summaries/<file> -> topic folder is parent of summaries
        folder = path.parent.parent.relative_to(ROOT).as_posix()
        by_folder.setdefault(folder, []).append(path)

    lines = [
        "# Critical Summary Inventory",
        "",
        "Digests for routing. They are not copies of the official texts.",
        "",
        f"Total: **{len(files)}** files",
        "",
        "| Folder | CS |",
        "|---|---:|",
    ]
    for folder in sorted(by_folder):
        lines.append(f"| {folder} | {len(by_folder[folder])} |")
    lines.append("")

    for folder in sorted(by_folder):
        lines.append(f"## {folder} ({len(by_folder[folder])})")
        lines.append("")
        lines.append("| CS |")
        lines.append("|---|")
        for path in by_folder[folder]:
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"| [{title_of(path)}]({rel}) |")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(files)} summaries)")


if __name__ == "__main__":
    main()
