#!/usr/bin/env python3
"""Build evidence-backed Chinese case studies for round-1/round-2 unresolved cases."""

from __future__ import annotations

import argparse
import concurrent.futures
import difflib
import json
import os
import re
import threading
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from openai import OpenAI


ROOT = Path("/data/zlyuaj/coding_agent/EviFuzz")
R1 = ROOT / "RIPPLE/mutation_result/all_agents_l12_k5_staged_20260830_145004"
R2 = ROOT / "RIPPLE/mutation_result/all_agents_round2_adaptive_v2_20260901_165815"
OUT = R2 / "failure_case_studies"
API_KEY = "sk-de21c76052d94acbbc3011a71629f36d"
BASE_URL = "https://rightapi.ai/codex/v1"
MODEL = "gpt-5.6-luna"

FAILURES = {
    1: {
        "codex": [
            "django__django-12470", "django__django-12589",
            "matplotlib__matplotlib-25079", "matplotlib__matplotlib-25433",
            "mwaskom__seaborn-2848", "sympy__sympy-15678", "sympy__sympy-16988",
        ],
        "sweagent": [
            "astropy__astropy-14995", "django__django-12908", "django__django-13033",
            "django__django-13710", "django__django-13925",
            "scikit-learn__scikit-learn-13779", "sympy__sympy-16988",
            "sympy__sympy-17139",
        ],
        "opencode": [
            "astropy__astropy-12907", "astropy__astropy-14182", "django__django-11039",
            "django__django-13925", "matplotlib__matplotlib-24149",
            "matplotlib__matplotlib-25442", "pytest-dev__pytest-11148",
            "scikit-learn__scikit-learn-14092", "sphinx-doc__sphinx-11445",
            "sympy__sympy-13773", "sympy__sympy-15345", "sympy__sympy-22714",
        ],
    },
    2: {
        "codex": [
            "django__django-14017", "django__django-15902", "django__django-16400",
            "matplotlib__matplotlib-24149", "matplotlib__matplotlib-26011",
            "sympy__sympy-14396", "sympy__sympy-15345", "sympy__sympy-15609",
        ],
        "sweagent": [
            "django__django-12184", "matplotlib__matplotlib-23562",
            "pydata__xarray-4094", "scikit-learn__scikit-learn-14894",
        ],
        "opencode": [
            "django__django-12125", "django__django-13551", "django__django-16400",
            "matplotlib__matplotlib-23987", "matplotlib__matplotlib-25498",
            "pydata__xarray-4094", "sphinx-doc__sphinx-7975", "sympy__sympy-12481",
            "sympy__sympy-15346", "sympy__sympy-20590",
        ],
    },
}

INFRA_R1 = {
    "codex": {
        "django__django-12708": "offset/source mismatch",
        "django__django-13757": "mutation introduced delimiter/code fence",
        "django__django-15213": "mutation introduced delimiter/code fence",
        "django__django-15851": "K=5 unavailable",
        "sphinx-doc__sphinx-8713": "K=5 unavailable",
    },
    "sweagent": {iid: "K=5 unavailable" for iid in [
        "astropy__astropy-6938", "django__django-11099", "django__django-14238",
        "django__django-14382", "django__django-15851", "django__django-16255",
        "django__django-16595", "matplotlib__matplotlib-25442", "mwaskom__seaborn-3010",
        "pydata__xarray-5131", "pytest-dev__pytest-5227", "pytest-dev__pytest-7373",
        "scikit-learn__scikit-learn-13584", "sphinx-doc__sphinx-8595",
        "sphinx-doc__sphinx-8713", "sympy__sympy-24152",
    ]},
    "opencode": {
        "django__django-11099": "K unavailable", "django__django-11848": "leading indentation",
        "django__django-12700": "JSON decode", "django__django-13158": "trailing newline",
        "django__django-15851": "K unavailable", "sphinx-doc__sphinx-8713": "K unavailable",
        "sympy__sympy-16792": "trailing newline",
    },
}

CLEAN_ROOTS = {
    "codex": ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases",
    "sweagent": ROOT / "original_passed_cases/SWE-Agent/luna_verified/cases",
    "opencode": ROOT / "original_passed_cases/OpenCode/gpt54mini_lite/cases",
}

SCHEMA = {
    "type": "object",
    "properties": {
        "stage": {"type": "string", "enum": ["localization", "editing", "feedback"]},
        "stage_confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "causality": {"type": "string", "enum": ["caused", "contributed", "not_supported"]},
        "causality_confidence": {"type": "string", "enum": ["high", "medium", "low"]},
        "short_conclusion": {"type": "string"},
        "inconsistency": {"type": "string"},
        "failure_onset": {"type": "string"},
        "causal_chain": {"type": "array", "items": {"type": "string"}},
        "trace_evidence": {"type": "array", "items": {"type": "string"}},
        "clean_comparison": {"type": "string"},
        "correct_vs_wrong": {"type": "string"},
        "feedback_analysis": {"type": "string"},
        "limitations": {"type": "string"},
    },
    "required": [
        "stage", "stage_confidence", "causality", "causality_confidence",
        "short_conclusion", "inconsistency", "failure_onset", "causal_chain",
        "trace_evidence", "clean_comparison", "correct_vs_wrong",
        "feedback_analysis", "limitations",
    ],
    "additionalProperties": False,
}

lock = threading.Lock()


def read_text(path: Path | None, limit: int | None = None) -> str:
    if not path or not path.exists():
        return ""
    value = path.read_text(errors="replace")
    return value if limit is None else clip(value, limit)


def load_json(path: Path | None, default: Any = None) -> Any:
    if not path or not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def clip(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    head = limit * 3 // 5
    tail = limit - head
    return value[:head] + f"\n... [中间截断 {len(value)-limit} 字符] ...\n" + value[-tail:]


def find_case(root: Path, agent: str, iid: str) -> Path:
    matches = sorted((root / agent / "runs").glob(f"*_{iid}"))
    if len(matches) != 1:
        raise FileNotFoundError(f"case path count={len(matches)} for {root.name}/{agent}/{iid}")
    return matches[0]


def trace_file(agent: str, base: Path, clean: bool = False) -> Path | None:
    if agent == "codex":
        pats = ["**/rollout-*.jsonl", "codex.jsonl"] if not clean else ["codex.jsonl", "**/rollout-*.jsonl"]
    elif agent == "sweagent":
        pats = ["**/*.traj"]
    else:
        pats = ["opencode.jsonl", "**/opencode.jsonl"]
    found: list[Path] = []
    for pat in pats:
        found.extend(base.glob(pat))
    found = [p for p in found if "failed_attempt" not in str(p) and "smoke" not in str(p)]
    return max(found, key=lambda p: p.stat().st_size) if found else None


def stringify(value: Any, limit: int = 1800) -> str:
    if isinstance(value, str):
        return clip(value, limit)
    return clip(json.dumps(value, ensure_ascii=False), limit)


def condense_codex(path: Path) -> str:
    items: list[str] = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            row = json.loads(line)
        except Exception:
            continue
        # Older clean runs were captured from `codex exec --json` and use
        # item.completed records rather than rollout response_item records.
        if row.get("type") in {"item.completed", "item.started"}:
            item = row.get("item", {})
            typ = item.get("type")
            if typ == "agent_message" and item.get("text"):
                items.append("ASSISTANT: " + stringify(item["text"], 2400))
            elif typ == "command_execution" and row.get("type") == "item.completed":
                items.append(
                    f"TOOL CALL command: {stringify(item.get('command'), 1800)}\n"
                    f"TOOL OUTPUT exit={item.get('exit_code')}: {stringify(item.get('aggregated_output'), 2400)}"
                )
            continue
        if row.get("type") != "response_item":
            continue
        p = row.get("payload", {})
        typ = p.get("type")
        if typ == "message" and p.get("role") == "assistant":
            text = "\n".join(x.get("text", "") for x in p.get("content", []) if isinstance(x, dict))
            if text.strip():
                items.append("ASSISTANT: " + stringify(text, 2400))
        elif typ in {"function_call", "custom_tool_call"}:
            items.append(f"TOOL CALL {p.get('name','')}: {stringify(p.get('arguments') or p.get('input'), 1800)}")
        elif typ in {"function_call_output", "custom_tool_call_output"}:
            items.append("TOOL OUTPUT: " + stringify(p.get("output"), 2400))
    return "\n\n".join(items)


def condense_swe(path: Path) -> str:
    data = load_json(path, {})
    rows = data.get("trajectory") or data.get("history") or []
    items = []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        bits = []
        for key in ("thought", "response", "action", "observation"):
            if row.get(key):
                bits.append(f"{key.upper()}: {stringify(row[key], 2000)}")
        if bits:
            items.append(f"STEP {i+1}\n" + "\n".join(bits))
    return "\n\n".join(items)


def condense_opencode(path: Path) -> str:
    items = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            row = json.loads(line)
        except Exception:
            continue
        typ = row.get("type")
        p = row.get("part", {})
        if typ == "text" and p.get("text"):
            items.append("ASSISTANT: " + stringify(p["text"], 2400))
        elif typ == "tool_use":
            state = p.get("state", {})
            items.append(
                f"TOOL {p.get('tool')}: input={stringify(state.get('input'), 1600)}\n"
                f"OUTPUT={stringify(state.get('output'), 2400)}"
            )
    return "\n\n".join(items)


def condense_trace(agent: str, path: Path | None, limit: int) -> str:
    if not path:
        return "[轨迹文件缺失]"
    try:
        value = {"codex": condense_codex, "sweagent": condense_swe, "opencode": condense_opencode}[agent](path)
    except Exception as exc:
        value = f"[轨迹解析失败: {exc}]\n" + read_text(path, limit)
    return clip(value, limit)


def patch_files(patch: str) -> list[str]:
    return sorted(set(re.findall(r"^diff --git a/(\S+) b/", patch, re.M)))


def get_prediction_patch(run_dir: Path, agent: str) -> str:
    preferred = run_dir / "interface/evaluation_compose/agent.patch"
    if preferred.exists():
        return read_text(preferred)
    candidates = list((run_dir / "interface").glob("**/predictions.jsonl"))
    for path in sorted(candidates, key=lambda p: len(str(p))):
        for line in path.read_text(errors="replace").splitlines():
            try:
                return json.loads(line).get("model_patch", "")
            except Exception:
                pass
    return ""


def get_clean_patch(case_dir: Path, run_no: int, agent: str) -> str:
    base = case_dir / f"run_{run_no}"
    candidates = [base / "prediction.json"] + list(base.glob("**/*.pred")) + list(base.glob("**/preds.json"))
    for p in candidates:
        if not p.exists():
            continue
        if p.suffix == ".pred":
            data = load_json(p, {})
            if isinstance(data, dict):
                return data.get("model_patch", "") or data.get("model_patch", "")
        data = load_json(p)
        if isinstance(data, dict):
            if "model_patch" in data:
                return data["model_patch"]
            # SWE-Agent preds.json is keyed by instance id.
            for value in data.values():
                if isinstance(value, dict) and value.get("model_patch"):
                    return value["model_patch"]
    return ""


def mutation_summary(manifest: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    rows, afters = [], []
    for cluster in manifest.get("clusters", []):
        locs = []
        for loc in cluster.get("locations", []):
            before = loc.get("original_unit_source", "")
            after = loc.get("mutated_unit_source", "")
            afters.append(after)
            locs.append({
                "file": loc.get("file"), "line": loc.get("file_line_start"),
                "symbol": loc.get("symbol"), "before": before, "after": after,
                "changed_contract": loc.get("changed_contract", ""),
            })
        rows.append({
            "cluster_id": cluster.get("cluster_id"), "label": cluster.get("label"),
            "operator": cluster.get("selected_operator"), "locations": locs,
        })
    return rows, [x for x in afters if x]


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return round(difflib.SequenceMatcher(None, a, b).ratio(), 4)


def build_evidence(round_no: int, agent: str, iid: str) -> tuple[dict[str, Any], Path]:
    root = R1 if round_no == 1 else R2
    run_dir = find_case(root, agent, iid)
    clean_dir = CLEAN_ROOTS[agent] / iid
    task = load_json(clean_dir / "task.json", {})
    if not task:
        selected = load_json(run_dir / "interface/selected_tasks.json", [])
        task = selected[0] if selected else {}
    manifest = load_json(run_dir / "mutation/manifest.json", {})
    mutations, mutated_afters = mutation_summary(manifest)
    mutant_trace_path = trace_file(agent, run_dir / "interface")
    mutant_trace = condense_trace(agent, mutant_trace_path, 22000)
    full_mutant_trace = read_text(mutant_trace_path)
    exposures = []
    for cluster in mutations:
        hit, total = 0, 0
        hit_locations = []
        for loc in cluster["locations"]:
            total += 1
            text = loc["after"].strip()
            exposed = bool(text and text in full_mutant_trace)
            hit += int(exposed)
            if exposed:
                hit_locations.append(f"{loc['file']}:{loc['line']}")
        exposures.append({
            "cluster_id": cluster["cluster_id"], "operator": cluster["operator"],
            "exact_text_hits": hit, "locations": total, "hit_locations": hit_locations,
        })
    agent_patch = get_prediction_patch(run_dir, agent)
    clean_runs = []
    for n in (1, 2, 3):
        cbase = clean_dir / f"run_{n}"
        cpatch = get_clean_patch(clean_dir, n, agent)
        ctrace_path = trace_file(agent, cbase, clean=True)
        clean_runs.append({
            "run": n, "patch": clip(cpatch, 9000), "patch_files": patch_files(cpatch),
            "trace_file": str(ctrace_path) if ctrace_path else None,
            "trace": condense_trace(agent, ctrace_path, 6500),
            "agent_patch_similarity": similarity(agent_patch, cpatch),
        })
    official = load_json(run_dir / "interface/evaluation_summary/official_summary.json", {})
    decision = load_json(run_dir / "round2_decision.json", {}) if round_no == 2 else {}
    evidence = {
        "round": round_no, "agent": agent, "instance_id": iid,
        "problem_statement": clip(task.get("problem_statement", ""), 7000),
        "gold_patch": clip(task.get("patch", ""), 14000),
        "gold_patch_files": patch_files(task.get("patch", "")),
        "mutation": mutations,
        "exposure_exact_string_check": exposures,
        "round2_decision": decision,
        "mutated_trace_file": str(mutant_trace_path) if mutant_trace_path else None,
        "mutated_trace": mutant_trace,
        # The interface's so-called agent.patch is a final-tree diff against the
        # pristine base and therefore still contains the pre-applied doc mutation.
        # Keep that provenance explicit; the semantic analyzer must separate
        # manifest-listed documentation edits from edits made in the trace.
        "final_combined_patch": clip(agent_patch, 16000),
        "final_combined_patch_files": patch_files(agent_patch),
        "clean_runs": clean_runs,
        "official_evaluation": {
            "resolved_ids": official.get("resolved_ids", []),
            "unresolved_ids": official.get("unresolved_ids", []),
            "error_ids": official.get("error_ids", []),
            "note": "保存的 official summary 只有 resolved/unresolved 状态，没有逐测试 assertion 输出；本地测试反馈从 Agent trace 提取。",
        },
    }
    case_out = OUT / f"round{round_no}" / agent / iid
    case_out.mkdir(parents=True, exist_ok=True)
    (case_out / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")
    return evidence, case_out


SYSTEM_PROMPT = """你是一名严谨的软件工程实验分析员。分析 documentation mutation 后原本能通过 SWE-bench 的 Agent 为何 unresolved。只能依据证据，不得臆测不可见的 reasoning 或 official assertion。

重要 provenance：final_combined_patch 是最终工作树相对 pristine base 的 diff，既包含预先注入、列在 mutation manifest 中的 documentation mutation，也包含 Agent 自己的编辑。绝不能把 manifest 中的文档变化算作 Agent 编辑；Agent 实际编辑必须结合 trace 和 manifest 做差分判断。

阶段分类必须且只能选择一个，按“最早足以导致最终失败的偏离”判定：
1. localization：主要责任文件/符号定位错误，或没有进入 gold fix 的责任区域；clean 至少一次进入正确区域。
2. editing：进入了正确文件/责任区域，但在得到决定性测试反馈以前，代码语义、条件、边界或修改对象已经错误/不完整。
3. feedback：初始编辑本来正确或接近 gold/成功 clean patch，但 Agent 因测试反馈误判而回退、追加错误修改或未根据清楚反馈修正。仅仅“运行过测试”不能判 feedback。

Mutation 因果分级：
- caused：trace 确认读到 mutated documentation，且后续文字或操作明确采用错误 contract，形成连续因果链。
- contributed：mutation 被读到且行为偏离三次 clean，但缺少明确引用；或它增强了已有错误倾向。
- not_supported：未暴露，错误与 clean 随机波动同样可解释，或没有证据连接 mutation 和错误。

exact string 未命中不等于一定未读到（工具可能截断/格式化）；命中只证明 exposure，不自动证明因果。比较 gold patch 是为了识别正确责任与语义，但不要要求 Agent patch 文本完全一致。输出中文，给出具体文件、符号、命令/反馈和时间顺序。"""


def call_analysis(evidence: dict[str, Any]) -> dict[str, Any]:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL, timeout=600, max_retries=0)
    prompt = SYSTEM_PROMPT + "\n\n以下是该 case 的结构化证据：\n" + json.dumps(evidence, ensure_ascii=False)
    last = None
    for attempt in range(1, 6):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                reasoning_effort="medium",
                max_tokens=7000,
                response_format={
                    "type": "json_schema",
                    "json_schema": {"name": "failure_case_study", "strict": True, "schema": SCHEMA},
                },
            )
            text = (response.choices[0].message.content or "").strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1].rsplit("```", 1)[0]
            return json.loads(text)
        except Exception as exc:
            last = exc
            if attempt == 5:
                break
            time.sleep(min(90, 8 * 2 ** (attempt - 1)))
    raise RuntimeError(f"analysis model failed after retries: {last}")


def render_case(e: dict[str, Any], a: dict[str, Any]) -> str:
    stage_cn = {"localization": "Localization（定位）", "editing": "Editing（编辑）", "feedback": "Feedback（反馈）"}
    cause_cn = {"caused": "由 mutation 直接导致", "contributed": "mutation 有促进作用", "not_supported": "没有足够证据归因于 mutation"}
    mutations = []
    for cluster in e["mutation"]:
        mutations.append(f"- `{cluster['cluster_id']}`，operator `{cluster['operator']}`，{len(cluster['locations'])} 个位置：")
        for loc in cluster["locations"]:
            mutations.append(f"  - `{loc['file']}:{loc['line']}`：`{loc['before'].strip()}` → `{loc['after'].strip()}`")
    chain = "\n".join(f"{i}. {x}" for i, x in enumerate(a["causal_chain"], 1))
    trace = "\n".join(f"- {x}" for x in a["trace_evidence"])
    return f"""# {e['instance_id']} failure case study

## 结论

- 轮次：第 {e['round']} 轮
- Agent：`{e['agent']}`
- official evaluation：`unresolved`
- 最早错误阶段：**{stage_cn[a['stage']]}**（置信度：`{a['stage_confidence']}`）
- Mutation 因果判断：**{cause_cn[a['causality']]}**（置信度：`{a['causality_confidence']}`）
- 一句话结论：{a['short_conclusion']}

## 注入的 inconsistency

{a['inconsistency']}

### Mutation 明细

{chr(10).join(mutations)}

## 错误从哪里开始

{a['failure_onset']}

## 逐步因果链

{chain}

## Trace 证据

{trace}

## 与三次 clean run 的对照

{a['clean_comparison']}

最终 combined patch 文件（包含预置 mutation，不能全部视为 Agent 编辑）：`{e['final_combined_patch_files']}`；gold patch 文件：`{e['gold_patch_files']}`。三次 clean patch 文件分别为：{[x['patch_files'] for x in e['clean_runs']]}。

## 正确做法与错误做法的分叉

{a['correct_vs_wrong']}

## Feedback 分析

{a['feedback_analysis']}

## 证据限制

{a['limitations']}

本 case 的完整机器可读证据见同目录 `evidence.json`，结构化判断见 `analysis.json`。保存的 official evaluation 仅提供 resolved/unresolved 汇总，没有逐 assertion 日志；因此文中具体测试反馈均来自 Agent 自身执行 trace，未把缺失的 official assertion 当作已知事实。
"""


def update_progress(started: str, completed: int, failed: int, total: int, current: str = "") -> None:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    elapsed = max(0.001, time.time() - datetime.fromisoformat(started).timestamp())
    rate = completed / elapsed
    eta = "unknown" if not rate else f"{(total-completed)/rate/60:.1f} min"
    status = {
        "updated_at": now, "phase": "running" if completed < total else "completed",
        "started_at": started, "completed": completed, "total": total,
        "remaining": total - completed, "success": completed - failed, "failed": failed,
        "errors": failed, "eta": eta, "pid": os.getpid(), "log": str(OUT / "RUN.log"),
        "output_dir": str(OUT), "current": current,
    }
    tmp = OUT / f"status.json.{os.getpid()}.tmp"
    tmp.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(OUT / "status.json")
    live = f"""# Failure case study live progress

- 更新时间：{now}
- 阶段：{status['phase']}
- 统计口径：completed = 已产出 evidence.json 且 analysis.md 成功写入；failed = 本轮分析调用最终失败
- 已完成：{completed}/{total}
- 成功：{completed-failed}
- 失败：{failed}
- 剩余：{total-completed}
- 当前：{current or '无'}
- ETA：{eta}
- PID：{os.getpid()}
- 日志：`{OUT / 'RUN.log'}`
"""
    tmp = OUT / f"LIVE_PROGRESS.md.{os.getpid()}.tmp"
    tmp.write_text(live)
    tmp.replace(OUT / "LIVE_PROGRESS.md")


def analyze_one(spec: tuple[int, str, str], force: bool) -> dict[str, Any]:
    round_no, agent, iid = spec
    evidence, case_out = build_evidence(round_no, agent, iid)
    result_path = case_out / "analysis.json"
    if result_path.exists() and not force:
        analysis = load_json(result_path)
    else:
        analysis = call_analysis(evidence)
        result_path.write_text(json.dumps(analysis, ensure_ascii=False, indent=2) + "\n")
    (case_out / "analysis.md").write_text(render_case(evidence, analysis))
    return {"round": round_no, "agent": agent, "instance_id": iid, **analysis}


def aggregate(results: list[dict[str, Any]]) -> None:
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    causal: dict[str, Counter[str]] = defaultdict(Counter)
    for row in results:
        counts[row["agent"]][row["stage"]] += 1
        counts["overall"][row["stage"]] += 1
        causal[row["agent"]][row["causality"]] += 1
        causal["overall"][row["causality"]] += 1
    labels = {"sweagent": "SWE-Agent", "opencode": "OpenCode", "codex": "Codex", "overall": "Overall"}
    table_rows = []
    for agent in ("sweagent", "opencode", "codex", "overall"):
        n = sum(counts[agent].values())
        vals = [100 * counts[agent][s] / n for s in ("localization", "editing", "feedback")]
        table_rows.append((labels[agent], n, *vals))
    index = sorted(results, key=lambda x: (x["round"], x["agent"], x["instance_id"]))
    (OUT / "case_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    dist = {a: {**dict(counts[a]), "total": sum(counts[a].values()), "causality": dict(causal[a])} for a in counts}
    (OUT / "stage_distribution.json").write_text(json.dumps(dist, ensure_ascii=False, indent=2) + "\n")
    case_lines = []
    for row in index:
        rel = f"round{row['round']}/{row['agent']}/{row['instance_id']}/analysis.md"
        case_lines.append(
            f"- 第 {row['round']} 轮 / `{row['agent']}` / [{row['instance_id']}]({rel})："
            f"`{row['stage']}`；`{row['causality']}`；{row['short_conclusion']}"
        )
    latex = "\n".join([
        r"\begin{table}[htbp]", r"  \centering",
        r"  \caption{Distribution of mutation effects across agent stages.}",
        r"  \label{tab:mutation_stage}", r"  \begin{tabular}{c|ccc}", r"    \toprule",
        r"    Agent & Localization (\%) & Editing (\%) & Feedback (\%) \\", r"    \midrule",
        *[f"    {name} & {loc:.1f} & {edit:.1f} & {feed:.1f} \\\\" for name, _, loc, edit, feed in table_rows[:3]],
        r"    \midrule",
        f"    Overall & {table_rows[3][2]:.1f} & {table_rows[3][3]:.1f} & {table_rows[3][4]:.1f} \\\\",
        r"    \bottomrule", r"  \end{tabular}", r"\end{table}",
    ])
    mdtable = "\n".join(
        ["| Agent | n | Localization | Editing | Feedback |", "|---|---:|---:|---:|---:|"] +
        [f"| {name} | {n} | {loc:.1f}% | {edit:.1f}% | {feed:.1f}% |" for name, n, loc, edit, feed in table_rows]
    )
    report = f"""# 第一轮与第二轮 failure case study 汇总

## 口径

本报告把 official evaluation 的 `unresolved` 作为 task failure：第一轮 27 个，第二轮 22 个，共 49 个 Agent-case。每个 case 恰好按“最早足以导致最终失败的偏离”归入 Localization、Editing 或 Feedback。第一轮另有 28 个基础设施失败，因为没有完整有效的 Agent execution + official unresolved 证据，不纳入三阶段分母，见 `第一轮基础设施失败附录.md`。

Mutation 因果判断与阶段分类是两个正交维度：一个 case 可以在 editing 阶段失败，但 mutation 因果仍为 `not_supported`。

## 阶段分布

{mdtable}

```latex
{latex}
```

## 因果强度统计

```json
{json.dumps({labels.get(a,a): dict(causal[a]) for a in ('sweagent','opencode','codex','overall')}, ensure_ascii=False, indent=2)}
```

## 全部 case 索引

{chr(10).join(case_lines)}

## 证据限制

保存产物中 official harness 仅保留每个 case 的 resolved/unresolved 汇总，没有逐测试 assertion 输出。因此，case study 对“feedback”的判定只使用 Agent trace 中有时间顺序的本地测试/命令反馈；若看不到“初始正确编辑 → 反馈 → 错误改动”的链条，就不会仅因 Agent 跑过测试而归类为 feedback。Codex 的隐藏 reasoning 是加密字段，分析只使用可见 commentary、tool call、tool output、patch 与三次 clean 对照。
"""
    (OUT / "汇总分析.md").write_text(report)
    appendix = ["# 第一轮基础设施失败附录", "", "这些 case 不属于 official unresolved 的三阶段行为失败，故不进入百分比分母。", ""]
    for agent in ("codex", "sweagent", "opencode"):
        appendix += [f"## {labels[agent]}", ""]
        appendix += [f"- `{iid}`：{reason}" for iid, reason in INFRA_R1[agent].items()]
        appendix.append("")
    (OUT / "第一轮基础设施失败附录.md").write_text("\n".join(appendix))
    # Put a lightweight pointer in the round-1 result tree as requested.
    r1_index = R1 / "failure_case_studies_index.md"
    r1_index.write_text(
        "# 第一轮 failure case studies\n\n"
        f"逐 case 分析统一保存在 `{OUT}`，其中第一轮位于 `round1/`；总汇总见 `{OUT / '汇总分析.md'}`。\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    started = datetime.now().astimezone().isoformat(timespec="seconds")
    specs = [(r, a, iid) for r in (1, 2) for a in ("codex", "sweagent", "opencode") for iid in FAILURES[r][a]]
    (OUT / "RUN_CONFIG.md").write_text(f"""# RUN CONFIG

- 任务：第一轮与第二轮全部 official unresolved case 的三阶段 case study
- run id：failure_case_studies_round1_round2_v1
- 启动时间：{started}
- 工作目录：{ROOT}
- 输入：`{R1}` 与 `{R2}`，以及 `original_passed_cases` 中 run 1–3
- 模型/API 配置：`{MODEL}` medium，`{BASE_URL}`（密钥不落盘）
- 并发数：{args.workers}
- 超时：单调用 600 秒
- 重试上限：5
- 缓存：已有 `analysis.json` 默认复用；`--force` 可重算
- 总 case：{len(specs)}（仅 official unresolved；infra failure 单列附录）
- 输出：`{OUT}`
""")
    completed = failed = 0
    results = []
    update_progress(started, 0, 0, len(specs), "初始化")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(analyze_one, spec, args.force): spec for spec in specs}
        for future in concurrent.futures.as_completed(futures):
            spec = futures[future]
            completed += 1
            try:
                row = future.result()
                results.append(row)
                line = f"OK round={spec[0]} agent={spec[1]} iid={spec[2]} stage={row['stage']} causality={row['causality']}"
            except Exception as exc:
                failed += 1
                line = f"ERROR round={spec[0]} agent={spec[1]} iid={spec[2]} error={exc!r}"
            with lock:
                with (OUT / "RUN.log").open("a") as fh:
                    fh.write(f"{datetime.now().astimezone().isoformat(timespec='seconds')} {line}\n")
                update_progress(started, completed, failed, len(specs), f"round{spec[0]}/{spec[1]}/{spec[2]}")
    # Include cached successful reports even if a subset failed this attempt.
    all_results = []
    for r, a, iid in specs:
        p = OUT / f"round{r}" / a / iid / "analysis.json"
        value = load_json(p)
        if value:
            all_results.append({"round": r, "agent": a, "instance_id": iid, **value})
    if len(all_results) == len(specs):
        aggregate(all_results)
    update_progress(started, completed, failed, len(specs), "聚合完成" if len(all_results) == len(specs) else "存在未完成 case")
    return 0 if len(all_results) == len(specs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
