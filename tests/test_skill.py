"""Validate SKILL.md so a malformed skill fails CI instead of silently not loading."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def parse_frontmatter(raw: bytes) -> dict[str, str]:
    text = raw.decode("utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("SKILL.md must start with a '---' frontmatter block")
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


class SkillManifestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = SKILL.read_bytes()
        self.meta = parse_frontmatter(self.raw)

    def test_no_bom(self) -> None:
        # A UTF-8 BOM hides the frontmatter from Claude Code's skill loader.
        self.assertFalse(self.raw.startswith(b"\xef\xbb\xbf"))

    def test_name_matches_repo(self) -> None:
        self.assertRegex(self.meta.get("name", ""), r"^[a-z0-9-]{1,64}$")
        self.assertEqual(self.meta["name"], "codebase-dojo")

    def test_description_present_and_bounded(self) -> None:
        description = self.meta.get("description", "")
        self.assertTrue(description, "description is required")
        self.assertLessEqual(len(description), 1024)

    def test_example_journal_exists(self) -> None:
        self.assertTrue((ROOT / "examples" / "sample-journal.md").is_file())


if __name__ == "__main__":
    unittest.main()
