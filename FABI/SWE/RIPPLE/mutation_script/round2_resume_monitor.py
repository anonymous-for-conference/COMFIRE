#!/usr/bin/env python3
"""Maintain user-facing live status for the round-two staged resume."""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import time
from pathlib import Path

from round2_resume_staged import AGENTS, WORKERS, atomic_json, discover, valid_evaluation, valid_prediction


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def read_events(path: Path) -> list[dict]:
    rows = []
    if not path.is_file():
        return rows
    for line in path.read_text(errors="replace").splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--retry", type=Path, required=True)
    parser.add_argument("--repair", type=Path, required=True)
    parser.add_argument("--pid", type=int, required=True)
    args = parser.parse_args()
    args.main = args.main.resolve()
    args.retry = args.retry.resolve()
    args.repair = args.repair.resolve()
    args.output = args.output.resolve()
    output = args.output
    config = json.loads((output / "RUN_CONFIG.json").read_text())
    samples = collections.deque(maxlen=8)
    last_terminal_time = time.monotonic()
    previous_completed = -1

    while True:
        events = read_events(output / "events.jsonl")
        barrier = next((row for row in reversed(events)
                        if row.get("event") == "all_predictions_valid"), None)
        final_path = output / "FINAL_SUMMARY.json"
        final = json.loads(final_path.read_text()) if final_path.is_file() else None
        selected = discover(args.main, args.retry, args.repair)
        phase = "evaluation" if barrier else "inference"
        prediction_keys = {key for key, run in selected.items() if valid_prediction(run)}
        evaluation_keys = {key for key, run in selected.items() if valid_evaluation(run)}
        complete_keys = evaluation_keys if phase == "evaluation" else prediction_keys
        stage_completed = len(complete_keys)
        inference_completed = len(prediction_keys)
        evaluation_completed = len(evaluation_keys)
        terminal_errors = [row for row in events
                           if row.get("stage") == phase and row.get("event") == "failed"]
        failed = len({(row.get("agent"), row.get("instance_id")) for row in terminal_errors})
        latest_by_case = {}
        for row in events:
            if row.get("stage") == phase and row.get("agent") in AGENTS:
                latest_by_case[(row.get("agent"), row.get("instance_id"))] = row
        active_keys = {key for key, row in latest_by_case.items()
                       if row.get("event") == "attempt_started"}
        total = int(config["total_cases"])
        stage_remaining = max(0, total - stage_completed - failed)
        # `completed` is deliberately the end-to-end count. Unlike the old
        # current-stage counter, it cannot fall at the inference/eval barrier.
        completed = evaluation_completed
        remaining = max(0, total - completed - failed)
        if stage_completed != previous_completed:
            last_terminal_time = time.monotonic()
            previous_completed = stage_completed
        samples.append((time.monotonic(), stage_completed))
        eta = "unknown"
        if len(samples) >= 2 and remaining:
            elapsed = samples[-1][0] - samples[0][0]
            advanced = samples[-1][1] - samples[0][1]
            if elapsed > 0 and advanced >= 2:
                eta = f"约 {remaining / (advanced / elapsed) / 3600:.1f} 小时（最近 {len(samples)} 次采样）"
        running = alive(args.pid)
        state_label = "running"
        if time.monotonic() - last_terminal_time > 30 * 60:
            state_label = "stalled_or_long_case"
        if not running:
            state_label = "completed" if final and final.get("phase") == "completed" else "failed"
        updated = now()
        status = {
            "updated_at": updated, "phase": final.get("phase") if final else phase,
            "started_at": config["started_at"], "completed": completed, "total": total,
            "remaining": remaining, "success": completed, "failed": failed,
            "errors": failed, "eta": eta, "pid": args.pid, "pid_alive": running,
            "state": state_label, "log": str(output / "RUN.log"),
            "output_dir": str(output), "cache_hit": (
                barrier.get("evaluation_cache_hit", 0) if barrier
                else config["prediction_cache_hit"]),
            "executed_this_run": max(0, completed - (
                barrier.get("evaluation_cache_hit", 0) if barrier
                else config["prediction_cache_hit"])),
            "inference": {"completed": inference_completed, "total": total,
                          "remaining": total - inference_completed},
            "evaluation": {"completed": evaluation_completed, "total": total,
                           "remaining": total - evaluation_completed},
            "current_stage": {"name": phase, "completed": stage_completed,
                              "total": total, "remaining": stage_remaining},
        }
        atomic_json(output / "status.json", status)
        lines = [
            "# Round 2 Resume Live Progress", "",
            f"- 状态：`{state_label}`；阶段：`{status['phase']}`",
            f"- 开始时间：`{config['started_at']}`；最近更新：`{updated}`",
            f"- Inference：`{inference_completed}/{total}`；剩余：`{total-inference_completed}`",
            f"- Evaluation：`{evaluation_completed}/{total}`；剩余：`{total-evaluation_completed}`",
            f"- 端到端完成：`{evaluation_completed}/{total}`；terminal failure：`{failed}`",
            f"- 当前运行：`{len(active_keys)}` 个 case",
            f"- cache hit：`{status['cache_hit']}`；本次新完成：`{status['executed_this_run']}`",
            f"- Worker：SWE-Agent `1`，Codex `2`，OpenCode `2`",
            f"- 主进程 PID：`{args.pid}`；PID alive：`{str(running).lower()}`",
            f"- ETA：`{eta}`",
            f"- 原始日志：`{output / 'RUN.log'}`",
            f"- 事件流：`{output / 'events.jsonl'}`", "",
            "统计口径：inference 与 evaluation 独立累计，均只增不减；端到端完成以 official evaluation 为准。failed 仅统计本次两次尝试后仍失败的 case。",
        ]
        temporary = output / "LIVE_PROGRESS.md.tmp"
        temporary.write_text("\n".join(lines) + "\n")
        temporary.replace(output / "LIVE_PROGRESS.md")
        canonical_lines = lines + ["", f"当前 retry 控制目录：`{output}`"]
        canonical_tmp = args.main / "LIVE_PROCESS.md.tmp"
        canonical_tmp.write_text("\n".join(canonical_lines) + "\n")
        canonical_tmp.replace(args.main / "LIVE_PROCESS.md")

        for agent in AGENTS:
            agent_dir = output / agent
            agent_dir.mkdir(exist_ok=True)
            agent_total = int(config["per_agent_total"][agent])
            agent_inference = sum(key[0] == agent for key in prediction_keys)
            agent_evaluation = sum(key[0] == agent for key in evaluation_keys)
            agent_completed = agent_evaluation
            agent_failed = len({row.get("instance_id") for row in terminal_errors
                                if row.get("agent") == agent})
            agent_active = sum(key[0] == agent for key in active_keys)
            text = "\n".join([
                f"# {agent} Live Progress", "",
                f"- 阶段：`{status['phase']}`；状态：`{state_label}`",
                f"- Inference：`{agent_inference}/{agent_total}`；剩余：`{agent_total-agent_inference}`",
                f"- Evaluation：`{agent_evaluation}/{agent_total}`；剩余：`{agent_total-agent_evaluation}`",
                f"- 端到端成功：`{agent_completed}`；terminal failure：`{agent_failed}`",
                f"- Worker 配额：`{WORKERS[agent]}`；当前运行：`{agent_active}`",
                f"- 更新时间：`{updated}`；总 ETA：`{eta}`", "",
            ])
            agent_tmp = agent_dir / "LIVE_PROGRESS.md.tmp"
            agent_tmp.write_text(text)
            agent_tmp.replace(agent_dir / "LIVE_PROGRESS.md")
            canonical_agent = args.main / agent / "ROUND2_RETRY_LIVE_PROGRESS.md"
            canonical_agent_tmp = canonical_agent.with_suffix(".md.tmp")
            canonical_agent_tmp.write_text(text + f"\n控制目录：`{output}`\n")
            canonical_agent_tmp.replace(canonical_agent)
        if not running:
            return
        time.sleep(20)


if __name__ == "__main__":
    main()
