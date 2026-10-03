# Agent 分文件平均统计（清理无效行后）

统计文件：
- `resolved/codex-round1.csv`
- `resolved/codex-round2.csv`
- `resolved/opencode-round1.csv`
- `resolved/opencode-round2.csv`
- `resolved/sweagent-round1.csv`
- `resolved/sweagent-round2.csv`
- `failed/codex-round1_round2.csv`
- `failed/opencode-round1_round2.csv`
- `failed/sweagent-round1_round2.csv`

清理规则：

- 删除 `total_tokens` 或 `rounds` 缺失的行（核心统计数据为空）；
- 删除 `rounds ≤ 1` 的行（视为明显异常）；
- 共删除 14 行；统计基于清理后的 CSV 文件。
- 各指标平均值按对应 agent 的有效记录计算，指标自身缺失值会被忽略。

## 分文件统计

| 文件 | Agent | 有效记录数 | 平均 Token 开销（total_tokens） | 平均 Round（rounds） | 平均 Edit（edit_lines） | 平均 Read（read_loc） |
|---|---|---:|---:|---:|---:|---:|
| `failed/codex-round1_round2.csv` | codex | 15 | 1,412,697.47 | 43.13 | 51.12 | 313.33 |
| `failed/opencode-round1_round2.csv` | opencode | 17 | 51,063.24 | 24.53 | 41.50 | 121.94 |
| `failed/sweagent-round1_round2.csv` | sweagent | 12 | 156,582.50 | 17.08 | 6.00 | 70.00 |
| `resolved/codex-round1.csv` | codex | 128 | 887,912.05 | 29.36 | N/A | 188.60 |
| `resolved/codex-round2.csv` | codex | 129 | 676,710.14 | 31.84 | 42.91 | 226.57 |
| `resolved/opencode-round1.csv` | opencode | 125 | 40,173.38 | 20.26 | N/A | 107.58 |
| `resolved/opencode-round2.csv` | opencode | 115 | 37,443.11 | 19.83 | 39.63 | 102.26 |
| `resolved/sweagent-round1.csv` | sweagent | 50 | 93,775.72 | 16.36 | 22.50 | 74.50 |
| `resolved/sweagent-round2.csv` | sweagent | 46 | 88,100.96 | 15.09 | 6.78 | 39.30 |
