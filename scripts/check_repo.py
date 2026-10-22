#!/usr/bin/env python3
"""Repository checks run in CI and locally.

1. Validate every examples/*.json file against the question-import rules
   enforced by index.html (stage number 5-35, prompt/options/correctAnswer,
   correctAnswer must be one of the options, known visualType values).
2. Privacy scan: fail if tracked text files contain local absolute paths,
   mainland-China mobile numbers, e-mail addresses or common secret patterns.
   Base64 data URIs inside index.html are stripped before scanning so that
   random base64 noise does not cause false positives.
"""
import glob
import json
import re
import subprocess
import sys

KNOWN_VISUALS = {"icons", "lineup", "pairing", "venn_diagram", "card_train"}
errors = []


def check_examples():
    files = sorted(glob.glob("examples/*.json"))
    if not files:
        errors.append("no example JSON files found")
    for path in files:
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: invalid JSON ({exc})")
            continue
        stages = data if isinstance(data, list) else data.get("stages")
        if not isinstance(stages, list) or not stages:
            errors.append(f"{path}: needs a non-empty 'stages' array")
            continue
        for st in stages:
            sid = st.get("id")
            n = int(sid) if str(sid).isdigit() else None
            if n is None or not 5 <= n <= 35:
                errors.append(f"{path}: stage id {sid!r} must be a number in 5-35")
            qs = st.get("questions") or []
            if not qs:
                errors.append(f"{path}: stage {sid} has no questions")
            for i, q in enumerate(qs, 1):
                where = f"{path}: stage {sid} question {i}"
                opts = q.get("options")
                if not q.get("prompt"):
                    errors.append(f"{where}: missing prompt")
                if not isinstance(opts, list) or len(opts) < 2:
                    errors.append(f"{where}: needs at least 2 options")
                    continue
                ans = q.get("correctAnswer", q.get("answer"))
                if ans is None or str(ans).strip() not in [str(o).strip() for o in opts]:
                    errors.append(f"{where}: correctAnswer must be one of the options")
                vt = q.get("visualType")
                if vt is not None and vt not in KNOWN_VISUALS:
                    errors.append(f"{where}: unknown visualType {vt!r}")
        print(f"ok  {path}")


PRIVACY_PATTERNS = {
    "local absolute path": re.compile(r"/Users/|/home/[a-z]|[A-Za-z]:\\\\Users"),
    "mobile phone number": re.compile(r"(?<![\w/+=-])1[3-9]\d{9}(?![\w/+=])"),
    "e-mail address": re.compile(r"[\w.+-]+@[\w-]+\.(?:com|cn|net|org|io|edu)\b"),
    "secret-like token": re.compile(r"sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|github_pat_|AKIA[0-9A-Z]{16}"),
}
DATA_URI = re.compile(r"data:[a-z]+/[a-z+.-]+;base64,[A-Za-z0-9+/=]+")
TEXT_EXT = (".html", ".md", ".json", ".yml", ".yaml", ".py", ".js", ".css", ".txt", ".gitignore")
SKIP = {"scripts/check_repo.py"}  # contains the patterns themselves


def check_privacy():
    files = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    for path in files:
        if path in SKIP or not path.endswith(TEXT_EXT) and path != "LICENSE":
            continue
        text = DATA_URI.sub("DATA_URI", open(path, encoding="utf-8", errors="ignore").read())
        for label, pat in PRIVACY_PATTERNS.items():
            for m in pat.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                errors.append(f"{path}:{line}: possible {label}: {m.group(0)!r}")
    print(f"ok  privacy scan over {len(files)} tracked files")


if __name__ == "__main__":
    check_examples()
    check_privacy()
    if errors:
        print("\n".join("FAIL " + e for e in errors))
        sys.exit(1)
    print("all checks passed")
