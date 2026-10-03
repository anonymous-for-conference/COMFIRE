#!/usr/bin/env python3
"""Run mutation, six-lane inference, and official evaluation in stage order."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXISTING = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/naive_mutation/mutation_scripts")
AGENTS = ("swe-agent", "opencode", "codex")


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text)
    temporary.replace(path)


class Pipeline:
    def __init__(self, run_root: Path, socket: Path, api_path: Path, attempt: int = 1):
        self.root = run_root.resolve()
        self.socket = socket.resolve()
        self.api_path = api_path
        self.attempt = attempt
        self.run_log = self.root / ("RUN.log" if attempt == 1 else f"RUN_attempt_{attempt:02d}.log")
        raw_selection = json.loads((self.root / "SELECTION.json").read_text())
        self.input_total = sum(len(cases) for cases in raw_selection.values())
        self.selection, self.excluded = self.eligible_selection(raw_selection)
        self.write_eligible_datasets()
        self.started = now()
        self.phase = "starting"
        self.completed = self.success = self.failed = 0
        self.total = sum(len(cases) for cases in self.selection.values())
        self.errors: list[dict] = []
        self.active: dict[str, int] = {}
        self.mutation_active: dict[str, dict[str, int]] = {agent: {} for agent in AGENTS}
        self.children: list[subprocess.Popen] = []
        self.lock = threading.Lock()
        self.status_lock = threading.Lock()
        self.stop = threading.Event()
        self.run_id = f"ripple-{self.root.name.replace('_', '-')}"

    def event(self, event: str, **details) -> None:
        record = {"timestamp": now(), "event": event, **details}
        with self.lock:
            with (self.root / "events.jsonl").open("a") as handle:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            with self.run_log.open("a") as handle:
                handle.write(f"[{record['timestamp']}] {event} {json.dumps(details, ensure_ascii=False)}\n")

    def refresh(self) -> None:
        if self.phase == "mutation":
            by_agent = self.mutation_progress()
            self.success = sum(item["success"] for item in by_agent.values())
            self.failed = sum(item["failed"] for item in by_agent.values())
            self.completed = self.success + self.failed
        elif self.phase == "inference":
            states = []
            for agent in AGENTS:
                try:
                    states.append(json.loads((self.root / agent / "status.json").read_text()))
                except (OSError, json.JSONDecodeError):
                    pass
            self.completed = min(self.total, sum(int(state.get("completed", 0)) for state in states))
            self.success = min(self.total, sum(int(state.get("success", 0)) for state in states))
            self.failed = min(self.total, sum(int(state.get("failed", 0)) for state in states))
        elif self.phase == "evaluation":
            results = []
            for agent in AGENTS:
                try:
                    results.append(json.loads((self.root / agent / "evaluation_result.json").read_text()))
                except (OSError, json.JSONDecodeError):
                    pass
            self.completed = min(self.total, sum(int(item.get("completed", 0)) for item in results))
            self.success = self.completed
            self.failed = 0

    def evaluation_summary(self) -> dict:
        agents = {}
        for agent in AGENTS:
            try:
                result = json.loads((self.root / agent / "evaluation_result.json").read_text())
            except (OSError, json.JSONDecodeError):
                continue
            agents[agent] = {
                "status": result.get("status"),
                "completed": int(result.get("completed", 0)),
                "total": int(result.get("total", 0)),
                "input_total": int(result.get("input_total", result.get("total", 0))),
                "officially_excluded": int(result.get("officially_excluded", 0)),
                "resolved": int(result.get("resolved", 0)),
                "unresolved": int(result.get("unresolved", 0)),
                "errors": int(result.get("errors", 0)),
            }
        return {
            "agents": agents,
            "completed": sum(item["completed"] for item in agents.values()),
            "total": sum(item["total"] for item in agents.values()),
            "input_total": sum(item["input_total"] for item in agents.values()),
            "officially_excluded": sum(item["officially_excluded"] for item in agents.values()),
            "resolved": sum(item["resolved"] for item in agents.values()),
            "unresolved": sum(item["unresolved"] for item in agents.values()),
            "errors": sum(item["errors"] for item in agents.values()),
        }

    def publish(self) -> None:
        with self.status_lock:
            self.refresh()
            mutation_by_agent = self.mutation_progress()
            state = {
                "updated_at": now(), "phase": self.phase, "started_at": self.started,
                "completed": self.completed, "total": self.total,
                "remaining": max(0, self.total - self.completed),
                "success": self.success, "failed": self.failed, "errors": len(self.errors),
                "error_details": self.errors, "eta": "unknown", "pid": os.getpid(),
                "worker_pids": self.active, "log": str(self.run_log),
                "mutation_by_agent": mutation_by_agent,
                "evaluation": self.evaluation_summary(),
                "input_total": self.input_total, "excluded": self.excluded,
                "output_dir": str(self.root), "last_event_time": now(),
                "accounting": (
                    "completed/total describe the current stage; inference and evaluation "
                    f"each total {self.total} agent-case pairs"
                ),
            }
            atomic(self.root / "status.json", json.dumps(state, ensure_ascii=False, indent=2) + "\n")

    def eligible_selection(self, selection: dict[str, list[dict]]) -> tuple[dict[str, list[dict]], list[dict]]:
        eligible = {agent: [] for agent in AGENTS}
        excluded = []
        for agent in AGENTS:
            for case in selection[agent]:
                clustered = Path(case["case_dir"]) / "clustered_doc.jsonl"
                rows = [json.loads(line) for line in clustered.read_text().splitlines() if line.strip()]
                preserve = int(self.config.get("preserve_documents_per_cluster", 0))
                counts = {}
                for row in rows:
                    if row.get("mutable", True):
                        counts[row["cluster_id"]] = counts.get(row["cluster_id"], 0) + 1
                has_mutable = any(count > preserve for count in counts.values())
                if has_mutable:
                    eligible[agent].append(case)
                else:
                    excluded.append({
                        "agent": agent, "instance_id": case["instance_id"],
                        "reason": "no mutable documentation in placement",
                    })
        return eligible, excluded

    def write_eligible_datasets(self) -> None:
        for agent in AGENTS:
            ids = {case["instance_id"] for case in self.selection[agent]}
            rows = [json.loads(line) for line in (self.root / agent / "dataset.jsonl").read_text().splitlines()
                    if line.strip()]
            selected = [row for row in rows if row["instance_id"] in ids]
            if {row["instance_id"] for row in selected} != ids:
                raise RuntimeError(f"eligible dataset mismatch for {agent}")
            atomic(self.root / agent / "dataset_eligible.jsonl", "".join(
                json.dumps(row, ensure_ascii=False) + "\n" for row in selected
            ))

    def mutation_progress(self) -> dict[str, dict]:
        progress = {}
        with self.lock:
            active = {agent: dict(cases) for agent, cases in self.mutation_active.items()}
        for agent in AGENTS:
            success = 0
            root = self.root / "mutations" / agent
            for path in root.glob("*/mutation.json"):
                case = next(
                    (item for item in self.selection[agent]
                     if item["instance_id"] == path.parent.name),
                    None,
                )
                if case is not None:
                    success += self.validated_mutation(case)
            failed = sum(
                error.get("stage") == "mutation" and error.get("agent") == agent
                for error in self.errors
            )
            total = len(self.selection[agent])
            progress[agent] = {
                "completed": success + failed, "total": total,
                "remaining": max(0, total - success - failed),
                "success": success, "failed": failed,
                "active": len(active[agent]), "active_cases": active[agent],
            }
        return progress

    def heartbeat(self) -> None:
        while not self.stop.wait(20):
            self.publish()

    def set_stage(self, phase: str) -> None:
        self.phase = phase
        self.completed = self.success = self.failed = 0
        self.active = {}
        self.publish()
        self.event("stage_started", phase=phase)

    def environment(self) -> dict[str, str]:
        content = self.api_path.read_text()
        key = content.splitlines()[0].strip()
        match = re.search(r"base_url\s*=\s*['\"]([^'\"]+)", content)
        if not key or not match:
            raise RuntimeError("invalid Luna API config")
        env = os.environ.copy()
        env.update(OPENAI_API_KEY=key, OPENAI_BASE_URL=match.group(1),
                   PRO_DOCKER_SOCKET=str(self.socket), SWE_PODMAN_SOCKET=str(self.socket))
        return env

    def archive_partial_mutation(self, agent: str, case: dict, case_attempt: int) -> None:
        output = Path(case["mutation_output"])
        if not output.exists() or (output / "mutation.json").is_file():
            return
        archive = self.root / "mutation_failed_attempts" / agent / case["instance_id"]
        archive.mkdir(parents=True, exist_ok=True)
        destination = archive / f"run_{self.attempt:02d}_attempt_{case_attempt:02d}"
        suffix = 1
        while destination.exists():
            suffix += 1
            destination = archive / f"run_{self.attempt:02d}_attempt_{case_attempt:02d}_{suffix:02d}"
        output.rename(destination)
        self.event("mutation_partial_archived", agent=agent, instance_id=case["instance_id"],
                   destination=str(destination))

    def validated_mutation(self, case: dict) -> bool:
        output = Path(case["mutation_output"])
        manifest_path = output / "mutation.json"
        patch_path = output / "mutation.patch"
        try:
            manifest = json.loads(manifest_path.read_text())
            patch = patch_path.read_bytes()
        except (OSError, json.JSONDecodeError):
            return False
        selected = {cluster.get("selected_operator") for cluster in manifest.get("clusters", [])}
        enabled = set(self.config.get("enabled_mutation_operators", ["L1", "L2", "L3"]))
        return bool(
            manifest.get("status") == "validated"
            and selected
            and selected <= enabled
            and manifest.get("patch_sha256") == hashlib.sha256(patch).hexdigest()
        )

    @staticmethod
    def mutation_error(log: Path) -> dict:
        try:
            tail = log.read_text(errors="replace")[-12000:]
        except OSError as exc:
            return {"category": "missing_log", "summary": str(exc)}
        lowered = tail.lower()
        categories = (
            ("exploration_budget", ("exceeded", "tool executions")),
            ("provider_transient", ("429", "502", "503", "concurrency limit", "rate limit", "upstream")),
            ("timeout", ("timeoutexpired", "timed out")),
            ("model_output", ("relational response", "mutation is unchanged", "mutation is empty", "jsondecodeerror")),
            ("patch_validation", ("diff --check", "documentation source mismatch", "non-documentation")),
        )
        category = "unknown"
        for name, markers in categories:
            if any(marker in lowered for marker in markers):
                category = name
                break
        lines = [line for line in tail.splitlines() if line.strip()]
        return {"category": category, "summary": lines[-1][-2000:] if lines else "empty log"}

    def mutation_one(self, agent: str, case: dict, case_attempt: int) -> tuple[str, str, int]:
        iid = case["instance_id"]
        seed_material = f"{json.loads((self.root / 'RUN_CONFIG.md').read_text().split('```json\n', 1)[1].split('\n```', 1)[0])['random_seed']}:{agent}:{iid}"
        seed = int(hashlib.sha256(seed_material.encode()).hexdigest()[:8], 16)
        self.archive_partial_mutation(agent, case, case_attempt)
        log = (self.root / agent / "logs" /
               f"mutation_{iid}_run_{self.attempt:02d}_attempt_{case_attempt:02d}.log")
        command = [sys.executable, str(HERE / "mutation_pipeline.py"),
                   "--case-dir", case["case_dir"], "--task", case["task"],
                   "--output", case["mutation_output"], "--api-config", str(self.api_path),
                   "--seed", str(seed), "-k", str(self.config["clusters_per_case"]),
                   "--operators", *self.config.get("enabled_mutation_operators", ["L1", "L2", "L3"]),
                   "--relational-attempts", str(self.config.get("relational_cluster_attempts", 5)),
                   "--relational-tool-budget", str(self.config.get("relational_initial_tool_budget", 8)),
                   "--relational-max-tool-budget", str(self.config.get("relational_max_tool_budget", 24)),
                   "--documents-per-cluster", str(self.config.get("documents_per_cluster", 0))]
        command.extend(["--preserve-documents-per-cluster",
                        str(self.config.get("preserve_documents_per_cluster", 0))])
        with log.open("w") as handle:
            child = subprocess.Popen(command, cwd=HERE, stdout=handle, stderr=subprocess.STDOUT,
                                     stdin=subprocess.DEVNULL, start_new_session=True)
            with self.lock:
                self.children.append(child)
                self.mutation_active[agent][iid] = child.pid
            self.publish()
            try:
                returncode = child.wait(timeout=int(self.config.get("mutation_case_timeout_seconds", 7200)))
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGTERM)
                child.wait(timeout=30)
                returncode = 124
            finally:
                with self.lock:
                    self.mutation_active[agent].pop(iid, None)
        return agent, iid, returncode

    @property
    def config(self) -> dict:
        text = (self.root / "RUN_CONFIG.md").read_text()
        return json.loads(text.split("```json\n", 1)[1].split("\n```", 1)[0])

    def mutations(self) -> None:
        self.set_stage("mutation")
        pending = {
            agent: [case for case in self.selection[agent]
                    if not self.validated_mutation(case)]
            for agent in AGENTS
        }
        cached = self.total - sum(len(cases) for cases in pending.values())
        self.event("mutation_resume", cached_validated=cached,
                   pending=sum(len(cases) for cases in pending.values()), excluded=self.excluded)
        max_attempts = int(self.config.get("mutation_case_attempts", 3))
        workers = int(self.config.get("mutation_workers_per_agent", 2))
        for case_attempt in range(1, max_attempts + 1):
            if not any(pending.values()):
                break
            executors = {agent: ThreadPoolExecutor(max_workers=workers, thread_name_prefix=f"mutation-{agent}")
                         for agent in AGENTS}
            futures = []
            for agent in AGENTS:
                for case in pending[agent]:
                    futures.append(executors[agent].submit(self.mutation_one, agent, case, case_attempt))
            failed_ids = {agent: set() for agent in AGENTS}
            try:
                for future in as_completed(futures):
                    agent, iid, returncode = future.result()
                    if returncode:
                        failed_ids[agent].add(iid)
                        log = (self.root / agent / "logs" /
                               f"mutation_{iid}_run_{self.attempt:02d}_attempt_{case_attempt:02d}.log")
                        error = self.mutation_error(log)
                        self.event("mutation_attempt_failed", agent=agent, instance_id=iid,
                                   attempt=case_attempt, returncode=returncode, **error)
                    else:
                        self.event("mutation_complete", agent=agent, instance_id=iid,
                                   attempt=case_attempt)
                    self.publish()
            finally:
                for executor in executors.values():
                    executor.shutdown(wait=True, cancel_futures=True)
            pending = {agent: [case for case in pending[agent]
                               if case["instance_id"] in failed_ids[agent]] for agent in AGENTS}
            if any(pending.values()) and case_attempt < max_attempts:
                self.event("mutation_retry_scheduled", attempt=case_attempt + 1,
                           pending={agent: len(cases) for agent, cases in pending.items()})
                time.sleep(30 * case_attempt)
        for agent, cases in pending.items():
            for case in cases:
                self.errors.append({"stage": "mutation", "agent": agent,
                                    "instance_id": case["instance_id"], "attempts": max_attempts})
        if self.errors:
            raise RuntimeError(f"mutation failed for {len(self.errors)} cases")
        self.event("stage_complete", phase="mutation", completed=self.total)

    def run_wave(self, commands: dict[str, list[str]], stage: str, attempt: int) -> dict[str, int]:
        running = {}
        env = self.environment()
        for agent, command in commands.items():
            log = (self.root / agent / "logs" /
                   f"{stage}_run_{self.attempt:02d}_attempt_{attempt:02d}.log")
            handle = log.open("w")
            child = subprocess.Popen(command, cwd=HERE, env=env, stdout=handle,
                                     stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                     start_new_session=True)
            self.children.append(child)
            self.active[agent] = child.pid
            running[agent] = (child, handle, log)
            self.event(f"{stage}_started", agent=agent, attempt=attempt, pid=child.pid, log=str(log))
        self.publish()
        while any(child.poll() is None for child, _, _ in running.values()):
            if self.stop.wait(10):
                raise RuntimeError("pipeline interrupted")
            self.publish()
        results = {}
        for agent, (child, handle, _) in running.items():
            handle.close()
            results[agent] = child.returncode
            self.active.pop(agent, None)
            self.event(f"{stage}_attempt_complete", agent=agent, attempt=attempt, returncode=child.returncode)
        self.publish()
        return results

    def concurrent_stage(self, commands: dict[str, list[str]], stage: str, max_attempts: int) -> None:
        pending = commands
        for attempt in range(1, max_attempts + 1):
            results = self.run_wave(pending, stage, attempt)
            failed = {agent: commands[agent] for agent, returncode in results.items() if returncode != 0}
            if not failed:
                self.event("stage_complete", phase=stage, completed=self.total)
                return
            for agent in failed:
                self.event(f"{stage}_retry_scheduled", agent=agent, attempt=attempt + 1)
            pending = failed
            if attempt < max_attempts:
                time.sleep(min(60 * attempt, 120))
        for agent in pending:
            self.errors.append({"stage": stage, "agent": agent, "error": "attempts exhausted"})
        raise RuntimeError(f"{stage} failed after {max_attempts} attempts: {sorted(pending)}")

    def inference(self) -> None:
        self.set_stage("inference")
        commands = {
            agent: [sys.executable, str(HERE / "parallel_agent_runner.py"),
                    "--run", self.run_id, "--agent", agent,
                    "--dataset", str(self.root / agent / "dataset_eligible.jsonl"),
                    "--output", str(self.root / agent), "--workers", "2", "--no-eval",
                    "--require-nonempty", "--mutation-root", str(self.root / "mutations")]
            for agent in AGENTS
        }
        # Empty model submissions can be transient, especially for OpenCode.
        # Keep the retry budget configurable so a run can recover without
        # restarting already validated agent cases.
        self.concurrent_stage(commands, "inference", int(self.config.get("inference_attempts", 3)))

    def evaluation(self) -> None:
        self.set_stage("evaluation")
        commands = {
            agent: [sys.executable, str(HERE / "evaluate_agent.py"),
                    "--run-id", self.run_id, "--agent", agent,
                    "--dataset", str(self.root / agent / "dataset_eligible.jsonl"),
                    "--output", str(self.root / agent), "--socket", str(self.socket)]
            for agent in AGENTS
        }
        # The evaluator receives its attempt number from this wave. Build a fresh
        # command dictionary per retry so logs and official run IDs never collide.
        pending = commands
        for attempt in range(1, int(self.config.get("evaluation_attempts", 2)) + 1):
            wave = {agent: command + ["--attempt", str(attempt)] for agent, command in pending.items()}
            results = self.run_wave(wave, "evaluation", attempt)
            failed = {agent: commands[agent] for agent, returncode in results.items() if returncode != 0}
            if not failed:
                self.event("stage_complete", phase="evaluation", completed=self.total)
                return
            pending = failed
            if attempt < int(self.config.get("evaluation_attempts", 2)):
                time.sleep(60)
        for agent in pending:
            self.errors.append({"stage": "evaluation", "agent": agent, "error": "attempts exhausted"})
        raise RuntimeError(f"evaluation failed after two attempts: {sorted(pending)}")

    def terminate(self) -> None:
        self.stop.set()
        for child in self.children:
            if child.poll() is None:
                try:
                    os.killpg(child.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass

    def run(self) -> int:
        heartbeat = threading.Thread(target=self.heartbeat, daemon=True)
        heartbeat.start()
        self.publish()
        try:
            self.mutations()
            if self.config.get("stop_after", "evaluation") != "mutation":
                self.inference()
                self.evaluation()
            self.phase = "complete"
            self.completed = self.success = self.total
            self.failed = 0
            self.publish()
            self.event("pipeline_complete")
            atomic(self.root / ("EXIT_CODE" if self.attempt == 1 else f"EXIT_CODE_attempt_{self.attempt:02d}"), "0\n")
            return 0
        except Exception as exc:
            self.errors.append({"stage": self.phase, "error": f"{type(exc).__name__}: {exc}"})
            self.phase = "failed"
            self.publish()
            self.event("pipeline_failed", error=str(exc))
            atomic(self.root / ("EXIT_CODE" if self.attempt == 1 else f"EXIT_CODE_attempt_{self.attempt:02d}"), "1\n")
            return 1
        finally:
            self.terminate()
            heartbeat.join(timeout=30)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--socket", type=Path, required=True)
    parser.add_argument("--api-config", type=Path, default=Path("/data/zlyuaj/coding_agent/luna_key.txt"))
    parser.add_argument("--attempt", type=int, default=1)
    args = parser.parse_args()
    pipeline = Pipeline(args.run_root, args.socket, args.api_config, args.attempt)
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: pipeline.terminate())
    return pipeline.run()


if __name__ == "__main__":
    raise SystemExit(main())
