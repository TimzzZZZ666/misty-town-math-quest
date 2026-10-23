# Misty Town: Math Dress-up Quest · 迷雾小镇数学换装闯关

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**▶️ Play online / 在线试玩：<https://timzzzzz666.github.io/misty-town-math-quest/>**  
No install — opens in the browser. Progress stays in *your* browser only.  
无需安装，浏览器直接打开；进度只保存在你自己的浏览器里。

<p align="center">
  <img src="docs/screenshot.png" alt="Start screen / 开始界面" width="48%">
  <img src="docs/screenshot-map.png" alt="35-level map / 35 关地图" width="48%">
</p>

**English:** A single-file, zero-dependency browser game for **Grade 1 math practice with English question prompts**. Kids clear stages on a 35-level map, earn points, and redeem outfits in a wardrobe. Parents export a Markdown learning report, paste it into any AI assistant for follow-up questions, then import the JSON back as stages 5–35.

**中文：** 面向小学一年级、**全英文题干**的数学「错题订正 + 换装闯关」网页小游戏。孩子在地图上一关一关答题，答对攒积分，在「魔法衣橱」兑换服装；家长一键导出学情报告，交给任意 AI 生成弱项变式题，再导入游戏变成新关卡。

---

## Features · 功能

- **35-level map / 35 关闯关地图** — hand-drawn style; character walks along the path; locked areas stay in mist until the previous stage is cleared.
- **4 built-in stages / 内置 4 个示例关卡** (English prompts, Grade 1):
  1. Bakery — cardinal vs. ordinal (how many vs. which position)
  2. Windmill — one-to-one correspondence (more / fewer)
  3. Clock Tower — Venn diagram / intersection
  4. Cozy Cottage — sequence position and recount after removing a card
- **Visual question types / 图示题型:** `icons`, `lineup`, `pairing`, `venn_diagram`, `card_train`
- **Points & wardrobe / 积分与衣橱** — correct answers, mastery bonuses, full-star clears; 10 outfit skins (including layered winged skins) redeemable with points
- **Gentle hints on miss; fireworks on clear;** optional Web Audio music-box BGM
- **Parent zone / 家长区:**
  - **Copy for AI** — Markdown learning report (accuracy, weak topics, machine-readable JSON, instructions for a question-writing AI)
  - **Import questions** — JSON into stages 5–35 (stages 1–4 are built-in and never overwritten)
  - **Export / import save** `.json` for device switches
- **Local save / 本地存档** — `localStorage`, multi-tab sync, auto-backup on corruption
- **Zero-dependency single file** — assets embedded in `index.html`; works offline
- Optimized for **iPad landscape**; desktop browsers work too

## Play & run locally · 试玩与本地运行

**Fastest:** open the live Pages link above.

Local:

```bash
git clone https://github.com/TimzzZZZ666/misty-town-math-quest.git
cd misty-town-math-quest
# open index.html in Chrome / Safari / Edge
# or: python3 -m http.server
```

- iPad: AirDrop / Files app → open `index.html` in Safari.
- Debug mode: append `?debug=1` for point-debug controls and a separate debug save (does not touch normal progress).

> **Note / 注意:** Opening via `file://` isolates `localStorage` by full path. If you move or rename the file, export the save from the parent zone first, then import it in the new location.

## Import questions · 导入新题

In the parent zone, click **导入错题 / Import**, paste JSON or pick a `.json` file. See [`examples/sample-stage-5.json`](examples/sample-stage-5.json):

```json
{
  "stages": [
    {
      "id": 5,
      "title": "Stage 5: Fruit Market",
      "topicTag": "compare_more_fewer",
      "questions": [
        {
          "id": "Q5_1",
          "prompt": "There are 5 apples 🍎 and 3 pears 🍐. How many more apples than pears?",
          "visualType": "icons",
          "visualData": ["🍎", "🍎", "🍎", "🍎", "🍎", "🍐", "🍐", "🍐"],
          "options": ["2", "3", "8"],
          "correctAnswer": "2",
          "hint": "Match each pear with one apple. How many apples are left?"
        }
      ]
    }
  ]
}
```

Rules:

- Stage `id` must be **5–35**
- Each question needs `prompt`, `options` (≥ 2), and `correctAnswer` (must be one of the options)
- `visualType` (optional): `icons` | `lineup` | `pairing` | `venn_diagram` (needs `visualData.squareOnly` / `overlap` / `circleOnly`) | `card_train`

## Contribute · 参与贡献

PRs and Issues welcome. Useful entry points:

- Open Issues tagged [`good first issue`](https://github.com/TimzzZZZ666/misty-town-math-quest/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) or [`help wanted`](https://github.com/TimzzZZZ666/misty-town-math-quest/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
- Before opening a PR, run:

```bash
python3 scripts/check_repo.py
```

- Keep saves and learning reports out of the repo (`.gitignore` already ignores `math_quest_save_*.json`)
- Roadmap work is tracked as Issues labeled `roadmap` — comment on an Issue before large changes

## Dev checks · 开发与检查

- `scripts/check_repo.py` — validates `examples/*.json` against import rules; privacy-scans tracked text files (local absolute paths, phone numbers, emails, secret-like tokens)
- `scripts/smoke_test.py` — headless Chrome: no JS errors, can reach the map, can import the sample stage via game logic

```bash
python3 scripts/check_repo.py
pip install playwright && python3 scripts/smoke_test.py   # needs Chrome; override with CHROME_PATH
```

GitHub Actions wiring for these scripts is on the roadmap (see below).

## Tech stack · 技术栈

- Vanilla **HTML + CSS + JavaScript** (no framework, no build step, no third-party deps)
- **Canvas** fireworks / confetti; **SVG** intro castle & map path
- **Web Audio API** BGM / SFX
- **localStorage** persistence
- Clay-style art (AI-assisted), embedded as WebP Base64

## Status & roadmap · 项目状态与路线图

**Status:** early but playable — public `v0.1.0`, actively maintained.  
**当前状态：** 可玩的早期版本（`v0.1.0` 已公开发布），作者持续维护。

See [CHANGELOG.md](CHANGELOG.md) and [Issues](https://github.com/TimzzZZZ666/misty-town-math-quest/issues).

### Done · 已完成

- Single-file game: 35-level map, 4 built-in Grade-1 English stages, 5 visual types
- Points + wardrobe (10 outfits, including layered winged skins)
- Parent zone: AI learning report, JSON import (stages 5–35), save export/import
- Local `localStorage` save, multi-tab sync, corruption backup; `?debug=1`
- `examples/sample-stage-5.json`, MIT license, GitHub Pages live demo
- Repo check scripts: `check_repo.py`, `smoke_test.py`

### In progress · 进行中

- Docs / OSS storefront polish (this pass): clearer bilingual README, executable roadmap
- Wire `check_repo.py` / `smoke_test.py` into GitHub Actions on push

### Next · 下一步

| Item | Issue |
|------|-------|
| Split `index.html` into modules + build that still emits one offline file | [#1](https://github.com/TimzzZZZ666/misty-town-math-quest/issues/1) |
| Parent-facing visual level editor (stages 5–35 without hand-written JSON) | [#2](https://github.com/TimzzZZZ666/misty-town-math-quest/issues/2) |
| More visual types: number line, ten frame, clock, shapes, free input | [#3](https://github.com/TimzzZZZ666/misty-town-math-quest/issues/3) |
| i18n: extract UI strings; zh-CN / English interface (question prompts stay as authored) | [#4](https://github.com/TimzzZZZ666/misty-town-math-quest/issues/4) |

Ideas welcome as new Issues. Prefer linking work to an Issue before large PRs.

## Privacy · 隐私说明

The game does not phone home and collects no data; progress stays in your browser. Exported saves and learning reports may contain a child's answer history — keep them private; do not commit them (`.gitignore` already ignores `math_quest_save_*.json`).

游戏不联网、不收集数据；导出的存档与学情报告请自行保管，勿提交到公开仓库。

## License · 许可

[MIT](LICENSE)
