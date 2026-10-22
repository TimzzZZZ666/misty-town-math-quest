#!/usr/bin/env python3
"""Headless-browser smoke test: open index.html, make sure it renders the
start screen without JavaScript errors, enter the map, and import the
example question file through the game's own import logic."""
import json
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
chrome = os.environ.get("CHROME_PATH", "/usr/bin/google-chrome")

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome if Path(chrome).exists() else None)
    page = browser.new_page(viewport={"width": 1366, "height": 1024})
    errors = []
    page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    page.on("console", lambda m: m.type == "error" and errors.append(f"console: {m.text}"))
    page.goto((ROOT / "index.html").as_uri())
    page.wait_for_timeout(1500)
    assert "Math Dress-up Quest" in page.title(), page.title()
    page.click("#btn-start-game", force=True)
    page.wait_for_timeout(1500)
    sample = json.loads((ROOT / "examples" / "sample-stage-5.json").read_text(encoding="utf-8"))
    notes = page.evaluate("(s) => overlayCustomStages(emptyQuestionBank(), s.stages).notes", sample)
    print("import notes:", notes)
    assert any(n.startswith("已装入第 5 关") for n in notes), notes
    browser.close()

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("smoke test passed")
