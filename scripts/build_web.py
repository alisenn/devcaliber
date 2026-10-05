"""
Embed devcaliber/data/questions.json into docs/index.html so the CLI and the web
app share one question bank.

    python scripts/build_web.py          # rewrite docs/index.html
    python scripts/build_web.py --check  # exit 1 if docs/index.html is out of date
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "devcaliber" / "data" / "questions.json"
TARGET = ROOT / "docs" / "index.html"

START = "/*QUESTIONS_START*/"
END = "/*QUESTIONS_END*/"
PATTERN = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)


def web_questions() -> list:
    """The web app calls the dimension field `dim` and doesn't need `track`."""
    out = []
    for q in json.loads(SOURCE.read_text(encoding="utf-8")):
        item = dict(q)
        item["dim"] = item.pop("dimension")
        out.append(item)
    return out


def render(html: str) -> str:
    payload = json.dumps(web_questions(), ensure_ascii=False, indent=1)
    block = f"{START}\n        const QUESTIONS_BANK = {payload};\n        {END}"
    if PATTERN.search(html):
        return PATTERN.sub(lambda _: block, html)
    # First run: replace the hand-embedded bank.
    legacy = re.compile(r"const QUESTIONS_BANK = \[.*?\n\];\n", re.S)
    if not legacy.search(html):
        raise SystemExit("Could not find the questions block in docs/index.html")
    return legacy.sub(lambda _: block + "\n", html, count=1)


def main() -> int:
    html = TARGET.read_text(encoding="utf-8")
    new_html = render(html)
    if "--check" in sys.argv:
        if new_html != html:
            print("docs/index.html is out of date. Run: python scripts/build_web.py")
            return 1
        print("docs/index.html is in sync with questions.json")
        return 0
    TARGET.write_text(new_html, encoding="utf-8")
    print(f"Wrote {len(web_questions())} questions into docs/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
