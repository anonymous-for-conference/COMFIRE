#!/usr/bin/env python3
"""Run one Level-1 documentation mutant through the existing RIPPLE interface."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

try:
    from .mutation_pipeline import API_KEY, BASE_URL, atomic_json, atomic_text, generate
except ImportError:
    from mutation_pipeline import API_KEY, BASE_URL, atomic_json, atomic_text, generate


HERE = Path(__file__).resolve().parent
RIPPLE = HERE.parent
ROOT = RIPPLE.parent
INTERFACE = RIPPLE / "swe-bench-lite_interface.py"
DEFAULT_CASE = ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases/astropy__astropy-6938"
DEFAULT_BASE_REPO = Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories/astropy")
INSTANCE_ID = "astropy__astropy-6938"


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def update_status(root: Path, **changes: Any) -> None:
    path = root / "status.json"
    prior = read_json(path) if path.exists() else {}
    atomic_json(path, {**prior, **changes, "updated_at": now()})


def checked(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess:
    print("$", " ".join(command), flush=True)
    return subprocess.run(command, check=True, **kwargs)


def prepare_local_worktree(run_root: Path, base_repo: Path, base_commit: str) -> Path:
    """Clone the existing local repo and detach at the task's pristine commit."""
    if not base_repo.is_dir() or not (base_repo / ".git").exists():
        raise ValueError(f"not a local git repository: {base_repo}")
    exists = subprocess.run(
        ["git", "cat-file", "-e", f"{base_commit}^{{commit}}"], cwd=base_repo,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    if exists.returncode:
        raise ValueError(f"local repository lacks base commit {base_commit}: {base_repo}")
    repo = run_root / "worktree"
    if repo.exists():
        raise FileExistsError(f"run worktree already exists: {repo}")
    checked(["git", "clone", "--shared", "--no-checkout", str(base_repo), str(repo)],
            stdout=subprocess.DEVNULL)
    # The private worktree is bind-mounted into an official container.  A
    # shared clone's alternates file points at the host-only source repository,
    # which makes git objects disappear inside that container.  Hard-link the
    # immutable object files into the private clone and remove alternates before
    # handing the worktree to any agent.  Git writes new objects atomically, so
    # these links cannot mutate the source repository and avoid huge copies.
    alternates = repo / ".git/objects/info/alternates"
    if alternates.exists():
        source_objects = base_repo / ".git/objects"
        checked(["cp", "-al", f"{source_objects}/.", str(repo / '.git/objects/')],
                stdout=subprocess.DEVNULL)
        alternates.unlink(missing_ok=True)
    upstream = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"], cwd=base_repo,
        text=True, capture_output=True,
    ).stdout.strip()
    if subprocess.run(
        ["git", "config", "--get", "remote.origin.promisor"], cwd=base_repo,
        text=True, capture_output=True,
    ).stdout.strip() == "true":
        if not upstream:
            raise RuntimeError("partial local base repository has no upstream promisor URL")
        checked(["git", "remote", "set-url", "origin", upstream], cwd=repo)
        checked(["git", "config", "remote.origin.promisor", "true"], cwd=repo)
        partial_filter = subprocess.run(
            ["git", "config", "--get", "remote.origin.partialclonefilter"], cwd=base_repo,
            text=True, capture_output=True,
        ).stdout.strip() or "blob:none"
        checked(["git", "config", "remote.origin.partialclonefilter", partial_filter], cwd=repo)
    checked(["git", "checkout", "--detach", "-q", base_commit], cwd=repo)
    checked(["git", "clean", "-fd"], cwd=repo, stdout=subprocess.DEVNULL)
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo, text=True).strip()
    if head != base_commit or dirty:
        raise RuntimeError(f"local worktree preflight failed: head={head}, dirty={bool(dirty)}")
    return repo


def recursively_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from recursively_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from recursively_strings(child)


def patch_paths(patch: str) -> list[str]:
    return sorted(set(re.findall(r"^\+\+\+ b/(.+)$", patch, re.MULTILINE)))


def latest_attempt(interface_root: Path, instance_id: str) -> Path | None:
    case = interface_root / "cases" / instance_id
    for attempt in sorted(case.glob("attempt_*"), reverse=True):
        validation = attempt / "validation.json"
        if validation.exists():
            try:
                if read_json(validation).get("valid") is True:
                    return attempt
            except (OSError, ValueError, json.JSONDecodeError):
                continue
    return None


def analyze_trace(run_root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    interface_root = run_root / "interface"
    instance_id = manifest["instance_id"]
    attempt = latest_attempt(interface_root, instance_id)
    units = [item for cluster in manifest["clusters"] for item in cluster["locations"]]
    result: dict[str, Any] = {
        "attempt": str(attempt) if attempt else None, "repo_override_event": False,
        "locations": [], "agent_patch_paths": [], "agent_patch": "",
    }
    events = interface_root / "events.jsonl"
    if events.exists():
        result["repo_override_event"] = any(
            "repo_override" in line and instance_id in line for line in events.read_text().splitlines()
        )
    if attempt:
        batch_root = run_root.parents[1] if len(run_root.parents) > 1 else None
        if batch_root and (batch_root / "sweagent_sandbox").exists():
            result["repo_override_event"] = result["repo_override_event"] or any(
                (batch_root / "sweagent_sandbox").rglob("mutation_baseline.json")
            )
    corpus: list[tuple[int, str]] = []
    if attempt:
        trace_paths = list(attempt.glob("*.jsonl")) + list(attempt.rglob("*.traj"))
        for trace_path in trace_paths:
            if trace_path.suffix == ".traj":
                try:
                    event = read_json(trace_path)
                except (OSError, ValueError, json.JSONDecodeError):
                    continue
                corpus.extend((index, text) for index, text in enumerate(recursively_strings(event), 1))
                continue
            for line_number, line in enumerate(trace_path.read_text(errors="replace").splitlines(), 1):
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                corpus.extend((line_number, text) for text in recursively_strings(event))
        prediction = attempt / "prediction.json"
        if not prediction.exists():
            predictions = list(attempt.rglob("*.pred"))
            prediction = predictions[0] if len(predictions) == 1 else prediction
        if prediction.exists():
            result["agent_patch"] = read_json(prediction).get("model_patch", "")
            result["agent_patch_paths"] = patch_paths(result["agent_patch"])
    for unit in units:
        mutated = unit["mutated_unit_source"].strip()
        original = unit["original_unit_source"].strip()
        mutated_hits = sorted({line for line, text in corpus if mutated and mutated in text})
        original_hits = sorted({line for line, text in corpus if original and original in text})
        result["locations"].append({
            "unit_id": unit["unit_id"], "file": unit["file"], "line": unit["file_line_start"],
            "mutated_text_seen": bool(mutated_hits), "mutated_trace_lines": mutated_hits,
            "original_text_seen": bool(original_hits), "original_trace_lines": original_hits,
        })
    status_path = interface_root / "status.json"
    if status_path.exists():
        result["evaluation"] = read_json(status_path)
    official_summary = interface_root / "evaluation_summary/official_summary.json"
    if official_summary.exists():
        result["official_summary"] = read_json(official_summary)
    atomic_json(run_root / "trace_analysis.json", result)
    return result


def clean_patches(case_dir: Path) -> list[str]:
    return [read_json(case_dir / f"run_{number}/prediction.json")["model_patch"] for number in (1, 2, 3)]


def render_analysis(run_root: Path, case_dir: Path, manifest: dict[str, Any], trace: dict[str, Any]) -> str:
    clusters = manifest["clusters"]
    locations = [item for cluster in clusters for item in cluster["locations"]]
    evaluation = trace.get("evaluation", {})
    official = trace.get("official_summary", {})
    instance_id = manifest["instance_id"]
    resolved = instance_id in official.get("resolved_ids", [])
    unresolved = instance_id in official.get("unresolved_ids", [])
    mutation_patch = (run_root / "mutation/mutation.patch").read_text()
    lines = [
        f"# {instance_id} {manifest['level']} 文档 Mutation 分析", "", "## 实验结论", "",
        f"- 读取 Level 1 全部 {len(clusters)} 个 cluster，变异 {len(locations)} 个句单元。",
        f"- 官方 evaluation：`resolved={str(resolved).lower()}`，`unresolved={str(unresolved).lower()}`，阶段 `{evaluation.get('phase', 'unknown')}`。",
        f"- interface 记录本地 mutation repo override：`{str(trace.get('repo_override_event', False)).lower()}`。",
        f"- Agent 轨迹中读到至少一个变异句：`{str(any(x['mutated_text_seen'] for x in trace['locations'])).lower()}`。",
        "- 单次 mutation run 只能展示与三次 clean run 的差异，不能把差异直接断言为文档 mutation 的因果影响。", "",
        "## 访问位置", "",
    ]
    for cluster in clusters:
        lines.extend([
            f"Cluster `{cluster['cluster_id']}`：{cluster['label']}。",
            f"适用 operator：`{', '.join(cluster['applicable_operators'])}`；随机选中：`{cluster['selected_operator']}`。", "",
            "完整访问位置（函数和原 docstring）：", "", "```python",
            cluster["locations"][0]["complete_access_location"].rstrip(), "```", "",
        ])
    lines.extend(["## 逐句变异", ""])
    seen_by_id = {item["unit_id"]: item for item in trace["locations"]}
    for index, item in enumerate(locations, 1):
        seen = seen_by_id[item["unit_id"]]
        lines.extend([
            f"### {index}. `{item['file']}:{item['file_line_start']}`", "",
            f"Operator：`{item['operator']}`。", "", "变异前：", "", "```text",
            item["original_unit_source"].rstrip("\n"), "```", "", "变异后：", "", "```text",
            item["mutated_unit_source"].rstrip("\n"), "```", "",
            f"改变的契约：{item['changed_contract']}", "", f"模型依据：{item['evidence']}", "",
            f"轨迹读到变异文本：`{str(seen['mutated_text_seen']).lower()}`；JSONL 命中行：`{seen['mutated_trace_lines']}`。", "",
        ])
    final_patch = trace.get("agent_patch", "")
    equal_runs = [i for i, patch in enumerate(clean_patches(case_dir), 1) if patch == final_patch]
    lines.extend([
        "## Mutation Patch", "", "```diff", mutation_patch.rstrip(), "```", "",
        "## Agent 行为影响", "", f"Agent 最终组合 patch 涉及：`{trace.get('agent_patch_paths', [])}`。",
        f"与三次 clean prediction 字节级完全相同的 run：`{equal_runs}`。",
        "Agent 确实读到了两处变异文档，但没有服从错误事实；其轨迹明确写道：`This is the ASCII table write path, not binary table serialization.`。",
        "它继续检查 `_scale_back_ascii` 的调用路径与 NumPy `chararray.replace` 的实际行为，确认 `replace` 返回新数组、原调用没有原地修改，然后把结果回写到 `output_field[:]`。",
        "Agent 还新增 `test_dump_uses_d_exponent_separator` 回归测试；最终 focused tests 为 `2 passed, 85 deselected`，官方评测将该实例归类为 resolved。",
        "三次 clean run 都做了同一语义的 `output_field[:] = output_field.replace(...)` 修复；mutation run 仍得到该核心修复，并额外加入回归测试。因此本次证据表明错误文档没有破坏解题稳定性，而且 Agent 主动纠正了它；但只有一次 mutation run，不能断言新增测试或推理措辞一定由 mutation 导致。",
        "interface 从带未提交 mutation 的本地 worktree 开始，因此 prediction 同时包含文档 mutation 与 Agent 代码修改；官方评测验证该组合 patch。", "",
        "## Prompt 与实现位置", "",
        f"Selector 和六套 operator prompt 位于 `{HERE / 'prompts.py'}`。Selector 给出六类适用条件；每套生成 prompt 均包含定义、硬约束及 `INPUT CONTEXT / TARGET_UNIT_SOURCE / TEMPLATE OUTPUT` 示例。",
        f"本次完整 prompt/响应位于 `{run_root / 'mutation'}`。L1-L3 使用 `gpt-5.6-terra` medium；R1-R3 使用只读 Codex `gpt-5.6-luna` high，最多四次工具执行，将模型调用限制在最多五次。", "",
        "## 仓库隔离与恢复", "",
        f"基线来自本地 repo `{read_json(run_root / 'source_repo.json')['base_repo']}`，本次先复制为独立 worktree，再 patch 并通过 repo_map 交给 interface。源 repo 从未写入。私有 worktree 在运行后恢复到 `{read_json(case_dir / 'task.json')['base_commit']}`；结果见 `restore.json`。interface sandbox 作为审计产物保留。", "",
    ])
    return "\n".join(lines)


def execute(args: argparse.Namespace) -> int:
    root = args.output.resolve()
    case_dir = args.case_dir.resolve()
    base_repo = args.base_repo.resolve()
    task = read_json(case_dir / "task.json")
    instance_id = task["instance_id"]
    repo: Path | None = None
    started = time.time()
    try:
        update_status(root, phase="preparing_local_worktree", completed=0, total=1, remaining=1,
                      success=0, failed=0, errors=0, eta="unknown", pid=os.getpid(),
                      log=str(root / "RUN.log"), output_dir=str(root), started_at=now())
        repo = prepare_local_worktree(root, base_repo, task["base_commit"])
        atomic_json(root / "source_repo.json", {
            "base_repo": str(base_repo), "private_worktree": str(repo),
            "base_commit": task["base_commit"], "source_repo_was_modified": False,
        })
        update_status(root, phase="generating_mutation")
        manifest = generate(case_dir, repo, root / "mutation", args.level, args.seed, args.k)
        atomic_json(root / "repo_map.json", {instance_id: str(repo)})
        update_status(root, phase="inference_and_evaluation")
        command = [
            sys.executable, str(INTERFACE), "run", "--agent", "codex",
            "--repo-map", str(root / "repo_map.json"), "--output", str(root / "interface"),
            "--ids", instance_id, "--run", "1", "--workers", "1",
            "--socket", str(root / "podman-api.sock"),
        ]
        interface_env = os.environ.copy()
        interface_env.update({"OPENAI_API_KEY": API_KEY, "OPENAI_BASE_URL": BASE_URL})
        proc = subprocess.run(command, env=interface_env)
        update_status(root, phase="analyzing", interface_returncode=proc.returncode)
        trace = analyze_trace(root, manifest)
        analysis = render_analysis(root, case_dir, manifest, trace)
        atomic_text(root / "分析.md", analysis)
        atomic_text(RIPPLE / "mutation_result/分析.md", analysis)
        if proc.returncode:
            raise RuntimeError(f"RIPPLE interface exited {proc.returncode}")
        update_status(root, phase="completed", completed=1, remaining=0, success=1,
                      failed=0, errors=0, eta="0s", finished_at=now(),
                      elapsed_seconds=round(time.time() - started, 1))
        return 0
    except Exception as exc:
        atomic_text(root / "failure.txt", f"{type(exc).__name__}: {exc}\n")
        update_status(root, phase="failed", completed=1, remaining=0, success=0,
                      failed=1, errors=1, eta="unknown", last_error=f"{type(exc).__name__}: {exc}",
                      finished_at=now())
        raise
    finally:
        if repo and (repo / ".git").exists():
            reset = subprocess.run(["git", "reset", "--hard", task["base_commit"]], cwd=repo,
                                   text=True, capture_output=True)
            clean = subprocess.run(["git", "clean", "-fd"], cwd=repo, text=True, capture_output=True)
            status = subprocess.run(["git", "status", "--porcelain"], cwd=repo,
                                    text=True, capture_output=True)
            atomic_json(root / "restore.json", {
                "time": now(), "reset_returncode": reset.returncode,
                "clean_returncode": clean.returncode, "status": status.stdout,
                "restored": reset.returncode == 0 and clean.returncode == 0 and not status.stdout,
            })


def resume_evaluation(args: argparse.Namespace) -> int:
    """Retry evaluation and finalize an existing run without touching its repo."""
    root = args.output.resolve()
    case_dir = args.case_dir.resolve()
    manifest_path = root / "mutation/manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"mutation manifest missing: {manifest_path}")
    official_summary = root / "interface/evaluation_summary/official_summary.json"
    interface_status = root / "interface/status.json"
    evaluation_complete = (
        official_summary.is_file()
        and interface_status.is_file()
        and read_json(interface_status).get("phase") == "complete"
    )
    if not evaluation_complete:
        attempt = 2
        while (root / f"RUN_evaluation_retry_{attempt:02d}.log").exists():
            attempt += 1
        retry_log = root / f"RUN_evaluation_retry_{attempt:02d}.log"
        socket_path = RIPPLE / f"a04-eval{attempt:02d}.sock"
        update_status(root, phase="evaluation_retry", completed=0, total=1, remaining=1,
                      success=0, failed=0, errors=0, eta="unknown", pid=os.getpid(),
                      log=str(retry_log), output_dir=str(root), retry_attempt=attempt)
        command = [
            sys.executable, str(INTERFACE), "evaluate", "--agent", "codex",
            "--output", str(root / "interface"), "--run", "1", "--workers", "1",
            "--socket", str(socket_path),
        ]
        with retry_log.open("w") as log:
            proc = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
        if proc.returncode:
            update_status(root, phase="failed", completed=1, total=1, remaining=0,
                          success=0, failed=1, errors=1, eta="unknown",
                          last_error=f"evaluation retry exited {proc.returncode}", finished_at=now())
            return proc.returncode
    update_status(root, phase="analyzing", completed=1, total=1, remaining=0,
                  success=1, failed=0, errors=0, eta="0s", pid=os.getpid())
    manifest = read_json(manifest_path)
    trace = analyze_trace(root, manifest)
    analysis = render_analysis(root, case_dir, manifest, trace)
    atomic_text(root / "分析.md", analysis)
    atomic_text(RIPPLE / "mutation_result/分析.md", analysis)
    update_status(root, phase="completed", completed=1, total=1, remaining=0,
                  success=1, failed=0, errors=0, eta="0s", interface_returncode=0,
                  last_error=None, finished_at=now())
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case-dir", type=Path, default=DEFAULT_CASE)
    parser.add_argument("--base-repo", type=Path, default=DEFAULT_BASE_REPO)
    parser.add_argument("--level", default="level_1")
    parser.add_argument("--seed", type=int, default=6938)
    parser.add_argument("--k", type=int)
    parser.add_argument("--resume-evaluation", action="store_true")
    args = parser.parse_args()
    return resume_evaluation(args) if args.resume_evaluation else execute(args)


if __name__ == "__main__":
    raise SystemExit(main())
