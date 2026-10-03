#!/usr/bin/env python3
"""Build an evidence-based summary for the completed level-2 batch."""
import glob, json, os, re

BATCH = "/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_result/level2_l123_first10_20260829_231906"
CLEAN = "/data/zlyuaj/coding_agent/EviFuzz/original_passed_cases/Codex/gpt54mini_lite/cases"
OUT = os.path.join(BATCH, "总分析.md")

def files(patch):
    return re.findall(r"^diff --git a/(.*?) b/", patch, re.M)

def patch_lines(patch):
    return [x for x in patch.splitlines() if x.startswith(("+", "-")) and not x.startswith(("+++", "---"))]

batch = json.load(open(os.path.join(BATCH, "BATCH_SUMMARY.json")))
rows = []
for item in batch["results"]:
    iid, run = item["instance_id"], item["run_root"]
    trace = json.load(open(os.path.join(run, "trace_analysis.json")))
    pred = json.load(open(os.path.join(run, "interface", "cases", iid, "attempt_01", "prediction.json")))
    mutated_patch = pred.get("model_patch", "")
    clean_patches = []
    for p in sorted(glob.glob(os.path.join(CLEAN, iid, "run_*", "prediction.json"))):
        clean_patches.append(json.load(open(p)).get("model_patch", ""))
    mutated_files = set(files(mutated_patch))
    clean_file_sets = [set(files(p)) for p in clean_patches]
    same_file_set = any(mutated_files == s for s in clean_file_sets)
    exact = any(mutated_patch == p for p in clean_patches)
    seen = sum(bool(x.get("mutated_text_seen")) for x in trace.get("locations", []))
    official = json.load(open(os.path.join(run, "interface", "evaluation_summary", "official_summary.json")))
    rows.append({"iid": iid, "count": item["mutation_count"], "seen": seen,
                 "total": len(trace.get("locations", [])), "exact": exact,
                 "same_files": same_file_set, "mutated_files": sorted(mutated_files),
                 "resolved": iid in official.get("resolved_ids", []),
                 "patch_lines": len(patch_lines(mutated_patch)),
                 "ops": [(c["label"], c["operator"], c["locations"]) for c in item["clusters"]]})

counts = [r["count"] for r in rows]
with open(OUT, "w") as f:
    f.write("# Level 2（L1/L2/L3）十个 clean case 总分析\n\n")
    f.write("## 结论\n\n")
    f.write("批处理已于 `2026-08-30 00:13:47 +08:00` 完成。十个 case 均完成 mutation、local inference 和 official Docker evaluation；每个 case 均 `submitted=1`、`completed=1`、`resolved=1`，没有 unresolved 或 error。\n\n")
    f.write("这说明本轮文档 mutation 没有使稳定成功 case 在该次运行中失效。它不是‘mutation 无影响’的充分证明：每个 case 只有一次 mutation run，且 Agent 可能依靠源码、测试和运行时事实纠正错误文档。\n\n")
    f.write("## 位置数量与算子\n\n")
    f.write("| case | mutation 位置数 | 读到变异文档的位置数 | 选中 cluster / operator / 位置数 | resolved |\n|---|---:|---:|---|---|\n")
    for r in rows:
        ops = "; ".join(f"{label} / {op} / {n}" for label, op, n in r["ops"])
        f.write(f"| `{r['iid']}` | {r['count']} | {r['seen']}/{r['total']} | {ops} | {'是' if r['resolved'] else '否'} |\n")
    f.write(f"\n总位置数为 **{sum(counts)}**，最大值 **{max(counts)}**，最小值 **{min(counts)}**，平均值 **{sum(counts)/len(counts):.1f}**。\n\n")
    f.write("## 与 clean run 的变化\n\n")
    f.write("比较对象是每个 clean case 的三次 `prediction.json` 与 mutation run 的 `model_patch`。`exact_patch` 表示完整 patch 文本与任一 clean run 相同；`same_file_set` 表示修改文件集合与任一 clean run 相同。\n\n")
    f.write("| case | exact patch | 相同文件集合 | mutation patch 文件 | 变异文档命中 |\n|---|---|---|---|---|\n")
    for r in rows:
        f.write(f"| `{r['iid']}` | {'是' if r['exact'] else '否'} | {'是' if r['same_files'] else '否'} | {', '.join('`'+x+'`' for x in r['mutated_files'])} | {r['seen']}/{r['total']} |\n")
    f.write("\n完整的句子级 before/after、prompt、mutation patch 和 agent trace 位于各 case 目录的 `分析.md`、`mutation/`、`mutation/mutation.patch` 与 `trace_analysis.json`。\n\n")
    f.write("### 解释\n\n")
    f.write("多数 mutation run 的最终 patch 与 clean run 不完全相同，部分 case 的修改文件集合也发生变化；这证明 mutation run 的 Agent 行为轨迹存在可观测差异。但差异同时可能来自模型随机性，因此不能仅凭一次 run 将全部差异归因于文档 mutation。`trace_analysis.json` 中的命中数是当前日志匹配器能确认的下界；命中为 0 不等于 Agent 一定没有读文档。\n\n")
    f.write("## 实现与复现位置\n\n")
    f.write("前三个 operator 的定义和结构化 mutation prompt 在 [prompts.py](/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_script/prompts.py)，算子过滤、cluster 选择、句子级 patch 在 [mutation_pipeline.py](/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_script/mutation_pipeline.py)，十 case 串行批处理在 [batch_level2_l123.py](/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_script/batch_level2_l123.py)。\n")

print(OUT)
