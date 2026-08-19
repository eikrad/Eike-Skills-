#!/usr/bin/env python3
"""Validate every skill in skills/.

Checks that each skill is a well-formed Agent Skill: parseable YAML frontmatter,
a name that matches its directory, a description within the limit agents read,
working relative links, and an entry in the README table.

Usage: python3 scripts/validate_skills.py
Exits non-zero if any check fails.
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DESCRIPTION_LIMIT = 1024
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

errors: list[str] = []


def fail(where: str, message: str) -> None:
    errors.append(f"{where}: {message}")


def check_frontmatter(skill_dir: Path, text: str) -> None:
    where = f"skills/{skill_dir.name}/SKILL.md"

    match = FRONTMATTER.match(text)
    if not match:
        fail(where, "no YAML frontmatter found (file must start with a --- block)")
        return

    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        fail(where, f"frontmatter is not valid YAML: {exc}")
        return

    if not isinstance(meta, dict):
        fail(where, "frontmatter must be a YAML mapping")
        return

    name = meta.get("name")
    if not name:
        fail(where, "frontmatter is missing 'name'")
    elif not isinstance(name, str):
        fail(where, "'name' must be a string")
    else:
        if name != skill_dir.name:
            fail(where, f"'name' is {name!r} but the directory is {skill_dir.name!r}")
        if not NAME_PATTERN.match(name):
            fail(where, f"'name' {name!r} must be lowercase words separated by hyphens")

    description = meta.get("description")
    if not description:
        fail(where, "frontmatter is missing 'description' — agents use it to decide when to load the skill")
    elif not isinstance(description, str):
        fail(where, "'description' must be a string")
    elif len(description) > DESCRIPTION_LIMIT:
        fail(where, f"'description' is {len(description)} characters, limit is {DESCRIPTION_LIMIT}")


def check_links(skill_dir: Path, text: str) -> None:
    where = f"skills/{skill_dir.name}/SKILL.md"
    for target in MD_LINK.findall(text):
        target = target.split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (skill_dir / target.split("#")[0]).resolve()
        if not resolved.exists():
            fail(where, f"relative link {target!r} does not resolve")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("skills/ directory not found", file=sys.stderr)
        return 1

    stray = [p.name for p in SKILLS_DIR.iterdir() if p.is_file()]
    if stray:
        fail("skills/", f"unexpected files at the top level: {', '.join(sorted(stray))}")

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        fail("skills/", "no skills found")

    readme_text = README.read_text(encoding="utf-8") if README.exists() else ""
    if not readme_text:
        fail("README.md", "not found")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(f"skills/{skill_dir.name}", "has no SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        check_frontmatter(skill_dir, text)
        check_links(skill_dir, text)

        if readme_text and skill_dir.name not in readme_text:
            fail("README.md", f"does not mention the {skill_dir.name!r} skill")

    print(f"Checked {len(skill_dirs)} skill(s): {', '.join(d.name for d in skill_dirs)}")
    if errors:
        print(f"\n{len(errors)} problem(s) found:\n", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
