# Changelog

本项目的版本变更记录。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [0.1.0] - 2026-10-22

首次公开发布。

### Added
- 单文件游戏 `index.html`：35 关闯关地图、4 个内置一年级英文数学关卡、5 种图示题型。
- 积分与「魔法衣橱」：10 套整装皮肤（含分层翅膀动态皮肤）用积分兑换。
- 家长区：一键复制 Markdown 学情报告（供任意 AI 助手出变式题）、导入题目 JSON（第 5–35 关）、导出/导入存档。
- 本地 `localStorage` 存档、多标签页同步、存档损坏自动备份；`?debug=1` 调试模式。
- `examples/sample-stage-5.json` 示例题目文件。
- README（中文 + English summary）、截图、MIT License、`.gitignore`。
- GitHub Pages 在线试玩。
- 检查脚本：`scripts/check_repo.py`（示例 JSON 校验 + 隐私扫描）、`scripts/smoke_test.py`（无头 Chrome 冒烟测试）。

[0.1.0]: https://github.com/TimzzZZZ666/misty-town-math-quest/releases/tag/v0.1.0
