#!/usr/bin/env python3
"""Run Codex or OpenCode on SWE-bench Lite in isolated official containers."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path("<local-data>/coding_agent/EviFuzz")
DATASET = Path("<local-data>/coding_agent_big_files/swe-bench-lite/dataset/swebench_lite_test.json")
EVAL_ROOT = Path("<local-data>/coding_agent/SWE-bench-eval")
KEY_FILE = Path("<local-data>/coding_agent/key.txt")
CODEX_BIN = Path("<local-data>/.nvm/versions/node/v24.18.0/lib/node_modules/@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex")
OPENCODE_BIN = Path("<local-data>/coding_agent/EviFuzz/opencode_env/node_modules/opencode-linux-x64/bin/opencode")
MODEL = os.environ.get("EVIFUZZ_MODEL", "gpt-5.6-luna")
EFFORT = os.environ.get("EVIFUZZ_REASONING_EFFORT", "")
MODEL_PROVIDER = os.environ.get("EVIFUZZ_MODEL_PROVIDER", "rightcode")
OPENCODE_PROVIDER = os.environ.get("EVIFUZZ_OPENCODE_PROVIDER", "openai")
WORKERS = int(os.environ.get("EVIFUZZ_WORKERS", "2"))
MAX_ATTEMPTS = int(os.environ.get("EVIFUZZ_MAX_ATTEMPTS", "6"))
CASE_TIMEOUT = int(os.environ.get("EVIFUZZ_CASE_TIMEOUT", "900"))


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path):
    return json.loads(path.read_text())


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def atomic_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(value)
    tmp.replace(path)


def credentials() -> tuple[str, str]:
    env_key = os.environ.get("OPENAI_API_KEY", "").strip()
    env_base = os.environ.get("OPENAI_BASE_URL", "").strip()
    if env_key or env_base:
        if not env_key or not env_base:
            raise RuntimeError("OPENAI_API_KEY and OPENAI_BASE_URL must be set together")
        return env_key, env_base
    text = KEY_FILE.read_text()
    key = re.search(r"api_key\s*=\s*['\"]([^'\"]+)['\"]", text)
    base = re.search(r"base_url\s*=\s*['\"]([^'\"]+)['\"]", text)
    if not key or not base:
        raise RuntimeError("key.txt does not contain api_key and base_url")
    return key.group(1), base.group(1)


def records() -> dict[str, dict]:
    override = os.environ.get("EVIFUZZ_RECORDS_FILE", "")
    if override:
        data = json.loads(Path(override).read_text())
        return {row["instance_id"]: row for row in data}
    return {row["instance_id"]: row for row in read_json(DATASET)}


def image(instance_id: str) -> str:
    normalized = instance_id.lower().replace("__", "_1776_")
    return f"docker.io/swebench/sweb.eval.x86_64.{normalized}:latest"


class Run:
    def __init__(self, agent: str, run: int, socket: Path, workers: int = WORKERS):
        if agent not in ("codex", "opencode"):
            raise ValueError(agent)
        self.agent = agent
        self.run = run
        self.socket = socket
        if workers < 1:
            raise ValueError("workers must be positive")
        self.workers = workers
        run_namespace = os.environ.get("EVIFUZZ_RUN_ID", f"{agent}-run{run}")
        self.attempt_namespace = hashlib.sha256(run_namespace.encode()).hexdigest()[:10]
        self.root = Path(os.environ.get("EVIFUZZ_OUTPUT_ROOT", str(ROOT / f"{agent}_gpt54_mini" / f"run_{run}")))
        self.sandbox = Path(os.environ.get(
            "EVIFUZZ_SANDBOX_ROOT", f"<local-data>/efl_{agent}_lite54_run{run}"
        ))
        overrides = os.environ.get("EVIFUZZ_REPO_OVERRIDES", "")
        try:
            self.repo_overrides = {str(k): Path(v) for k, v in json.loads(overrides).items()} if overrides else {}
        except (TypeError, ValueError, json.JSONDecodeError) as exc:
            raise ValueError("EVIFUZZ_REPO_OVERRIDES must be a JSON object of instance_id to repository path") from exc
        prior_status = self.root / "status.json"
        self.started_at = now()
        if prior_status.exists():
            try:
                self.started_at = read_json(prior_status).get("started_at", self.started_at)
            except Exception:
                pass
        self.events = self.root / "events.jsonl"
        self.main_log = self.root / "RUN.log"
        self._evaluation_log = self.root / "evaluation.log"
        self._samples: list[tuple[float, int]] = []

    @property
    def env(self) -> dict[str, str]:
        value = os.environ.copy()
        value["DOCKER_HOST"] = f"unix://{self.socket}"
        return value

    def attempt(self, iid: str, number: int) -> Path:
        return self.root / "cases" / iid / f"attempt_{number:02d}"

    def valid_attempt(self, iid: str) -> Path | None:
        case = self.root / "cases" / iid
        for attempt in sorted(case.glob("attempt_*"), reverse=True) if case.exists() else []:
            validation = attempt / "validation.json"
            prediction = attempt / "prediction.json"
            if validation.exists() and prediction.exists():
                try:
                    if read_json(validation).get("valid") is True:
                        return attempt
                except Exception:
                    pass
        return None

    def terminal_attempt(self, iid: str) -> Path | None:
        valid = self.valid_attempt(iid)
        if valid:
            return valid
        last = self.attempt(iid, MAX_ATTEMPTS)
        return last if (last / "validation.json").exists() and (last / "prediction.json").exists() else None

    def emit(self, event: str, **fields) -> None:
        self.events.parent.mkdir(parents=True, exist_ok=True)
        with self.events.open("a") as handle:
            handle.write(json.dumps({"time": now(), "event": event, **fields}, ensure_ascii=False) + "\n")

    def counts(self) -> tuple[int, int, int]:
        success = failed = 0
        for iid in records():
            attempt = self.terminal_attempt(iid)
            if not attempt:
                continue
            if read_json(attempt / "validation.json").get("valid") is True:
                success += 1
            else:
                failed += 1
        return success + failed, success, failed

    def update(self, phase: str, current_cases: list[str] | None = None, error: str | None = None) -> None:
        completed, success, failed = self.counts()
        total = len(records())
        stamp = time.time()
        if not self._samples or self._samples[-1][1] != completed:
            self._samples.append((stamp, completed))
            self._samples = self._samples[-10:]
        eta = "unknown"
        if completed == total:
            eta = "0s"
        elif len(self._samples) >= 2:
            elapsed = self._samples[-1][0] - self._samples[0][0]
            delta = self._samples[-1][1] - self._samples[0][1]
            if elapsed > 0 and delta > 0:
                eta = f"{int((total - completed) * elapsed / delta)}s"
        state = {
            "updated_at": now(), "phase": phase, "agent": self.agent, "run": self.run,
            "started_at": self.started_at, "completed": completed, "total": total,
            "remaining": total - completed, "success": success, "failed": failed,
            "errors": 0, "inference_completed": completed, "inference_success": success,
            "inference_invalid_or_empty": failed, "eta": eta, "pid": os.getpid(), "process_alive": True,
            "log": str(self.main_log), "output_dir": str(self.root),
            "current_cases": current_cases or [], "last_event_at": self._last_event(),
        }
        if phase == "evaluation":
            metrics = self.evaluation_metrics()
            state.update({
                "completed": metrics["completed"], "total": metrics["total"],
                "remaining": metrics["total"] - metrics["completed"],
                "success": metrics["resolved"], "failed": metrics["unresolved"],
                "errors": metrics["errors"], "eta": metrics["eta"],
                "evaluation_completed": metrics["completed"],
                "evaluation_total": metrics["total"],
            })
            state["evaluation_log"] = str(self._evaluation_log)
        if phase == "complete":
            summary_path = self.root / "evaluation_summary/official_summary.json"
            if summary_path.exists():
                summary = read_json(summary_path)
                resolved = int(summary.get("resolved_instances", 0))
                unresolved = int(summary.get("unresolved_instances", 0))
                empty_patches = int(summary.get("empty_patch_instances", 0))
                evaluation_errors = int(summary.get("error_instances", 0))
                state.update({
                    "completed": resolved + unresolved + empty_patches + evaluation_errors,
                    "remaining": total - resolved - unresolved - empty_patches - evaluation_errors,
                    "success": resolved, "failed": unresolved, "errors": evaluation_errors,
                    "evaluation_resolved": resolved, "evaluation_unresolved": unresolved,
                    "evaluation_empty_patches": empty_patches,
                    "evaluation_errors": evaluation_errors, "eta": "0s",
                })
        if error:
            state["last_error"] = error
        atomic_json(self.root / "status.json", state)
        with self.main_log.open("a") as run_log:
            run_log.write(json.dumps({
                # Log the same authoritative counters written to status.json.
                # During evaluation these are harness counters, not the already
                # completed inference counters calculated at the top of update().
                "time": state["updated_at"], "phase": phase,
                "completed": state["completed"], "total": state["total"],
                "remaining": state["remaining"], "success": state["success"],
                "failed": state["failed"], "errors": state["errors"],
                "current_cases": current_cases or [], "eta": state["eta"],
                "error": error,
            }, ensure_ascii=False) + "\n")
        lines = [
            f"# {self.agent.title()} {MODEL} SWE-bench Lite run_{self.run} Live Progress", "",
            f"- updated_at: `{state['updated_at']}`", f"- started_at: `{self.started_at}`",
            f"- phase: **{phase}**", f"- completed: `{completed}/{total}`",
            f"- remaining: `{total - completed}`", f"- successful inference artifacts: `{success}`",
            f"- invalid/empty inference artifacts after retries: `{failed}`",
            "- infrastructure errors: `not inferred from CLI validation status`",
            f"- current cases: `{', '.join(current_cases or []) or 'none'}`", f"- ETA: `{eta}`",
            f"- last event: `{state['last_event_at']}`", f"- PID: `{os.getpid()}`",
            f"- RUN log: `{self.main_log}`", f"- output: `{self.root}`", "",
            "`completed` counts cases with a terminal prediction artifact. Empty patches are retained and evaluated after bounded retries.",
        ]
        if phase == "evaluation":
            lines = [
                f"# {self.agent.title()} {MODEL} SWE-bench Lite run_{self.run} Live Progress", "",
                f"- updated_at: `{state['updated_at']}`", f"- started_at: `{self.started_at}`",
                "- phase: **evaluation**",
                f"- official evaluation completed: `{state['completed']}/{state['total']}`",
                f"- remaining: `{state['remaining']}`", f"- resolved: `{state['success']}`",
                f"- unresolved: `{state['failed']}`", f"- infrastructure errors: `{state['errors']}`",
                f"- current: `{', '.join(current_cases or []) or 'waiting for harness output'}`",
                f"- ETA: `{state['eta']}`", f"- PID: `{os.getpid()}`",
                f"- evaluation log: `{self._evaluation_log}`", f"- RUN log: `{self.main_log}`",
                f"- output: `{self.root}`", "",
                "Evaluation counters are parsed from the current official harness attempt only.",
            ]
        if phase == "complete" and (self.root / "evaluation_summary/official_summary.json").exists():
            lines = [
                f"# {self.agent.title()} {MODEL} SWE-bench Lite run_{self.run} Live Progress", "",
                f"- updated_at: `{state['updated_at']}`", f"- started_at: `{self.started_at}`",
                "- phase: **complete**", f"- official evaluation classified: `{state['completed']}/{total}`",
                f"- remaining: `{state['remaining']}`", f"- resolved: `{state['evaluation_resolved']}`",
                f"- unresolved: `{state['evaluation_unresolved']}`",
                f"- empty patches: `{state['evaluation_empty_patches']}`",
                f"- official evaluation errors: `{state['evaluation_errors']}`",
                f"- inference valid artifacts: `{success}`",
                f"- inference invalid/empty artifacts after retries: `{failed}`",
                "- ETA: `0s`", f"- PID: `{os.getpid()}`", f"- RUN log: `{self.main_log}`",
                f"- official summary: `{self.root / 'evaluation_summary/official_summary.json'}`",
                f"- output: `{self.root}`", "",
                "Official evaluation and inference validation are reported separately.",
            ]
        if error:
            lines += ["", f"- last error: `{error}`"]
        atomic_text(self.root / "LIVE_PROGRESS.md", "\n".join(lines) + "\n")

    def evaluation_progress(self) -> tuple[int, int]:
        metrics = self.evaluation_metrics()
        return metrics["completed"], metrics["total"]

    def evaluation_metrics(self) -> dict[str, int | str]:
        log = self._evaluation_log
        run_id = os.environ.get("EVIFUZZ_RUN_ID", f"evifuzz-lite-{self.agent}-gpt54mini-run{self.run}")
        model_name = f"evifuzz-{self.agent}-{MODEL}-run{self.run}"
        report_root = EVAL_ROOT / "logs" / "run_evaluation" / run_id / model_name
        expected_ids = set(records())
        resolved = unresolved = 0
        if report_root.exists():
            for report_path in report_root.glob("*/report.json"):
                try:
                    report = read_json(report_path)
                    iid = report_path.parent.name
                    if iid not in expected_ids:
                        continue
                    if report[iid]["resolved"]:
                        resolved += 1
                    else:
                        unresolved += 1
                except Exception:
                    continue
        base = {
            "completed": resolved + unresolved, "total": len(records()),
            "resolved": resolved, "unresolved": unresolved, "errors": 0, "eta": "unknown",
        }
        if not log.exists():
            return base
        lines = re.split(r"[\r\n]", log.read_text(errors="replace"))
        for line in reversed(lines):
            if "Evaluation:" not in line:
                continue
            progress = re.search(r"(\d+)\s*/\s*(\d+)", line)
            if not progress:
                continue
            values = {}
            for name, pattern in (
                ("resolved", r"✓=(\d+)"), ("unresolved", r"✖=(\d+)"), ("errors", r"error=(\d+)"),
            ):
                match = re.search(pattern, line)
                values[name] = int(match.group(1)) if match else 0
            eta_match = re.search(r"\[[^\]]*<([^,\]]+)", line)
            base["errors"] = values["errors"]
            base["eta"] = eta_match.group(1).strip() if eta_match else "unknown"
            # The first progress fraction is the harness processed count;
            # report files may be absent for unresolved/error cases and must
            # not be used as the evaluation denominator while the run is live.
            base["completed"] = int(progress.group(1))
            base["total"] = int(progress.group(2))
            return base
        return base

    def _last_event(self) -> str:
        if not self.events.exists():
            return self.started_at
        lines = self.events.read_text(errors="replace").splitlines()
        if not lines:
            return self.started_at
        try:
            return json.loads(lines[-1])["time"]
        except Exception:
            return now()

    def write_config(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        atomic_text(self.root / "RUN_CONFIG.md", f"""# Run Configuration

- agent: `{self.agent}`
- model: `{MODEL}`
- reasoning effort: `{EFFORT}`
- benchmark: `SWE-bench Lite`, split `test`
- dataset: `{DATASET}`
- run: `{self.run}`
- inference workers: `{self.workers}`
- case timeout: `{CASE_TIMEOUT}s`
- maximum attempts: `{MAX_ATTEMPTS}`
- execution: one case-private repo and one official instance container per attempt
- evaluation: official harness, {self.workers} worker(s), `cache_level=instance`, `clean=False`
- Podman socket: `{self.socket}`
- sandbox root: `{self.sandbox}`
- started_at: `{self.started_at}`

The CLIs do not expose temperature or top_p controls. No unsupported value is claimed. API credentials are injected through the process environment and are not stored here.
""")

    def ensure_image(self, iid: str) -> None:
        if subprocess.run(["podman", "image", "exists", image(iid)], env=self.env).returncode:
            subprocess.run(["podman", "--storage-opt", "ignore_chown_errors=true", "pull", image(iid)], env=self.env, check=True, timeout=3600)

    def prepare_repo(self, iid: str, commit: str, dest: Path) -> None:
        override = self.repo_overrides.get(iid)
        if override is not None:
            if not override.is_dir() or not (override / ".git").exists():
                raise RuntimeError(f"mutation repository is not a git worktree: {override}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(override, dest, symlinks=True)
            # The interface deliberately does not reset or checkout here: the
            # caller's repository mutation is the starting state for inference.
            dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=dest, text=True).strip()
            self.emit("repo_override", instance_id=iid, source=str(override), dirty=bool(dirty))
            return
        self.ensure_image(iid)
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        cid = subprocess.check_output(["podman", "create", "--network=none", image(iid), "true"], env=self.env, text=True).strip()
        try:
            subprocess.run(["podman", "cp", f"{cid}:/testbed/.", str(dest)], env=self.env, check=True, timeout=600, stdout=subprocess.DEVNULL)
        finally:
            subprocess.run(["podman", "rm", "-f", cid], env=self.env, timeout=60, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "restore", "."], cwd=dest, check=True)
        subprocess.run(["git", "reset", "--hard", "HEAD"], cwd=dest, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "checkout", "--detach", "-q", commit], cwd=dest, check=True)
        subprocess.run(["git", "clean", "-fd"], cwd=dest, check=True, stdout=subprocess.DEVNULL)
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=dest, text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=dest, text=True).strip()
        if head != commit or dirty:
            raise RuntimeError(f"official repository preflight failed: head={head}, dirty={bool(dirty)}")

    def container_ids(self, label: str) -> list[str]:
        output = subprocess.check_output(["podman", "ps", "-aq", "--filter", f"label=evifuzz.attempt={label}"], env=self.env, text=True)
        return output.split()

    def cleanup_label(self, label: str) -> None:
        for cid in self.container_ids(label):
            subprocess.run(["podman", "rm", "-f", cid], env=self.env, timeout=60, stdout=subprocess.DEVNULL)
        if self.container_ids(label):
            raise RuntimeError(f"containers remain for label {label}")

    def cli_command(self, prompt: str, runtime_in_container: str) -> list[str]:
        if self.agent == "codex":
            return [
                "/opt/evifuzz/codex", "exec", "-m", MODEL,
                *( ["-c", f'model_reasoning_effort="{EFFORT}"'] if EFFORT else [] ),
                "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check",
                "--json", "--output-last-message", f"{runtime_in_container}/final_message.txt", prompt,
            ]
        return [
            "/opt/evifuzz/opencode", "run", "--model", f"{OPENCODE_PROVIDER}/{MODEL}",
            *( ["--variant", EFFORT] if EFFORT else [] ), "--auto", "--format", "json", prompt,
        ]

    def run_case(self, worker: int, iid: str, record: dict) -> None:
        if self.terminal_attempt(iid):
            return
        key, base_url = credentials()
        for number in range(1, MAX_ATTEMPTS + 1):
            out = self.attempt(iid, number)
            if out.exists():
                continue
            out.mkdir(parents=True)
            live = self.sandbox / f"c{list(records()).index(iid):03d}" / f"a{number:02d}"
            repo, runtime = live / "repo", live / "runtime"
            runtime.mkdir(parents=True, exist_ok=True)
            for private_dir in ("codex_home", "config", "data", "cache"):
                (runtime / private_dir).mkdir(exist_ok=True)
            reasoning_line = f"model_reasoning_effort = \"{EFFORT}\"\n" if EFFORT else ""
            (runtime / "codex_home/config.toml").write_text(
                f"model_provider = {json.dumps(MODEL_PROVIDER)}\n"
                f"model = \"{MODEL}\"\n"
                + reasoning_line
                +
                "disable_response_storage = true\n"
                "approval_policy = \"never\"\n"
                "sandbox_mode = \"danger-full-access\"\n\n"
                f"[model_providers.{MODEL_PROVIDER}]\n"
                f"name = {json.dumps(MODEL_PROVIDER)}\n"
                f"base_url = {json.dumps(base_url)}\n"
                "env_key = \"OPENAI_API_KEY\"\n"
                "wire_api = \"responses\"\n"
                "\n[features]\n"
                "code_mode_host = true\n"
            )
            (runtime / "opencode.json").write_text(json.dumps({
                "$schema": "https://opencode.ai/config.json",
                "provider": {OPENCODE_PROVIDER: {
                    "options": {"apiKey": "{env:OPENAI_API_KEY}", "baseURL": "{env:OPENAI_BASE_URL}"},
                    "models": {MODEL: {
                        "name": MODEL,
                        "reasoning": bool(EFFORT),
                        **({"options": {"reasoningEffort": EFFORT}} if EFFORT else {}),
                    }},
                }},
            }, ensure_ascii=False, indent=2) + "\n")
            label = f"{self.agent}-{self.attempt_namespace}-r{self.run}-c{list(records()).index(iid):03d}-a{number:02d}"
            self.emit("case_started", instance_id=iid, worker=worker, attempt=number, label=label)
            started = time.time()
            rc = -1
            error = ""
            patch = ""
            try:
                self.prepare_repo(iid, record["base_commit"], repo)
                hook = os.environ.get("EVIFUZZ_MUTATION_HOOK", "")
                if hook:
                    subprocess.run([sys.executable, hook, str(repo), iid, str(self.run), str(out), os.environ.get("EVIFUZZ_MUTATION_SOURCE_AGENT", self.agent)], env=container_env if 'container_env' in locals() else self.env, check=True, timeout=900)
                prompt = (
                    "Solve this SWE-bench issue. Work directly in /testbed. Inspect the code and tests, "
                    "implement the smallest correct fix, and run focused tests when practical. Do not only explain: "
                    "leave the final solution in the git working tree.\n\nProblem statement:\n" + record["problem_statement"]
                )
                binary = CODEX_BIN if self.agent == "codex" else OPENCODE_BIN
                runtime_container = "/opt/evifuzz/runtime"
                cmd = [
                    "podman", "run", "--rm", "--name", label, "--label", f"evifuzz.attempt={label}",
                    "--volume", f"{repo}:/testbed:rw", "--volume", f"{runtime}:{runtime_container}:rw",
                    "--volume", f"{binary}:/opt/evifuzz/{self.agent}:ro",
                    *(["--volume", f"{CODEX_BIN.parent / 'codex-code-mode-host'}:/opt/evifuzz/codex-code-mode-host:ro"] if self.agent == "codex" else []),
                    "--env", "OPENAI_API_KEY", "--env", "OPENAI_BASE_URL",
                    "--env", f"CODEX_HOME={runtime_container}/codex_home",
                    "--env", f"OPENCODE_CONFIG={runtime_container}/opencode.json",
                    "--env", f"XDG_CONFIG_HOME={runtime_container}/config",
                    "--env", f"XDG_DATA_HOME={runtime_container}/data",
                    "--env", f"XDG_CACHE_HOME={runtime_container}/cache",
                    "--workdir", "/testbed", image(iid), *self.cli_command(prompt, runtime_container),
                ]
                container_env = self.env
                container_env["OPENAI_API_KEY"] = key
                container_env["OPENAI_BASE_URL"] = base_url
                with (out / f"{self.agent}.jsonl").open("w") as log:
                    proc = subprocess.Popen(cmd, env=container_env, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
                    try:
                        rc = proc.wait(timeout=CASE_TIMEOUT)
                    except subprocess.TimeoutExpired:
                        os.killpg(proc.pid, signal.SIGTERM)
                        try:
                            proc.wait(timeout=30)
                        except subprocess.TimeoutExpired:
                            os.killpg(proc.pid, signal.SIGKILL)
                            proc.wait(timeout=30)
                        raise RuntimeError(f"case timeout after {CASE_TIMEOUT}s")
                patch = subprocess.check_output(["git", "diff", "--binary"], cwd=repo, text=True)
                if rc != 0:
                    raise RuntimeError(f"{self.agent} exit={rc}")
                if not patch.strip():
                    raise RuntimeError("model produced an empty patch")
                valid = True
            except Exception as exc:
                valid = False
                error = f"{type(exc).__name__}: {exc}"
                if repo.exists():
                    patch = subprocess.run(["git", "diff", "--binary"], cwd=repo, text=True, capture_output=True).stdout
            finally:
                try:
                    self.cleanup_label(label)
                except Exception as cleanup_exc:
                    valid = False
                    error = f"{error}; cleanup: {cleanup_exc}".strip("; ")
            prediction = {"model_name_or_path": f"evifuzz-{self.agent}-{MODEL}-run{self.run}", "instance_id": iid, "model_patch": patch}
            atomic_json(out / "prediction.json", prediction)
            atomic_json(out / "validation.json", {
                "valid": valid, "instance_id": iid, "agent": self.agent, "model": MODEL,
                "reasoning_effort": EFFORT, "run": self.run, "worker": worker, "attempt": number,
                "returncode": rc, "error": error or None, "empty_patch": not bool(patch.strip()),
                "execution_mode": "official_instance_container_cli_v1", "official_image": image(iid),
                "container_cleanup_confirmed": not self.container_ids(label),
                "elapsed_seconds": round(time.time() - started, 2), "artifact_dir": str(out),
            })
            self.emit("case_attempt", instance_id=iid, worker=worker, attempt=number, valid=valid, error=error or None)
            if valid:
                return

    def worker(self, worker: int) -> int:
        recs = records()
        failures = 0
        for iid in list(recs)[worker - 1::self.workers]:
            self.run_case(worker, iid, recs[iid])
            failures += self.valid_attempt(iid) is None
        return 1 if failures else 0

    def predictions(self) -> Path:
        rows = []
        for iid in records():
            attempt = self.terminal_attempt(iid)
            if not attempt:
                raise RuntimeError(f"missing terminal artifact for {iid}")
            rows.append(read_json(attempt / "prediction.json"))
        expected = len(records())
        if len(rows) != expected or len({row["instance_id"] for row in rows}) != expected:
            raise RuntimeError("prediction cardinality validation failed")
        path = self.root / "predictions.jsonl"
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
        return path

    def cleanup_run_id(self, run_id: str) -> None:
        # Podman can hang or return a 500 when its storage inventory contains
        # a stale layer.  Cleanup is best-effort and must never prevent the
        # official evaluator from starting or finishing.
        try:
            ids = subprocess.check_output(
                ["podman", "ps", "-aq", "--filter", f"name={run_id}"],
                env=self.env, text=True, timeout=20,
            ).split()
        except Exception:
            ids = []
        for cid in ids:
            try:
                subprocess.run(["podman", "rm", "-f", cid], env=self.env, check=False, timeout=60, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

    def evaluate(self) -> None:
        prediction = self.predictions()
        run_id = os.environ.get("EVIFUZZ_RUN_ID", f"evifuzz-lite-{self.agent}-gpt54mini-run{self.run}")
        report = self.root / "evaluation_summary"
        report.mkdir(exist_ok=True)
        self.cleanup_run_id(run_id)
        if (self.root / "evaluation.log").exists():
            attempt = 2
            while (self.root / f"evaluation_attempt_{attempt:02d}.log").exists():
                attempt += 1
            self._evaluation_log = self.root / f"evaluation_attempt_{attempt:02d}.log"
        else:
            self._evaluation_log = self.root / "evaluation.log"
        cmd = [
            "<local-data>/anaconda3/bin/conda", "run", "--no-capture-output", "-n", "swebench-eval",
            "python", "-m", "swebench.harness.run_evaluation", "--dataset_name", "SWE-bench/SWE-bench_Lite",
            "--split", "test", "--predictions_path", str(prediction), "--max_workers", str(self.workers),
            "--cache_level", "instance", "--clean", "False", "--run_id", run_id, "--report_dir", str(report),
        ]
        try:
            with self._evaluation_log.open("w") as log:
                proc = subprocess.Popen(cmd, cwd=EVAL_ROOT, env=self.env, stdout=log, stderr=subprocess.STDOUT)
                while proc.poll() is None:
                    self.update("evaluation", [f"official harness {self.evaluation_progress()[0]}/{self.evaluation_progress()[1]}"])
                    time.sleep(20)
                rc = proc.returncode
        finally:
            self.cleanup_run_id(run_id)
        if rc:
            raise RuntimeError(f"official evaluation exit={rc}")
        candidates = sorted(EVAL_ROOT.glob(f"evifuzz-{self.agent}-{MODEL}-run{self.run}.{run_id}.json"))
        if len(candidates) != 1:
            raise RuntimeError(f"expected one official summary, got {candidates}")
        summary = read_json(candidates[0])
        error_ids = summary.get("error_ids", [])
        resolved = int(summary.get("resolved_instances", 0))
        unresolved = int(summary.get("unresolved_instances", 0))
        empty_patches = int(summary.get("empty_patch_instances", 0))
        expected_ids = set(records())
        submitted = int(summary.get("submitted_instances", len(expected_ids)))
        completed = int(summary.get("completed_instances", submitted))
        submitted_ids = set(summary.get("submitted_ids", expected_ids))
        completed_ids = set(summary.get("completed_ids", submitted_ids))
        if error_ids or int(summary.get("error_instances", 0)):
            raise RuntimeError(f"official evaluation has {len(error_ids)} infrastructure errors")
        # SWE-bench reports total_instances as the full dataset size even when
        # predictions contain only a selected subset.  Validate the submitted
        # and completed subset instead of comparing against that dataset total.
        if (
            submitted != len(expected_ids)
            or completed != len(expected_ids)
            or submitted_ids != expected_ids
            or completed_ids != expected_ids
            or resolved + unresolved + empty_patches != len(expected_ids)
        ):
            raise RuntimeError(
                "official evaluation cardinality invalid: "
                f"submitted={submitted}, completed={completed}, "
                f"submitted_ids={sorted(submitted_ids)}, completed_ids={sorted(completed_ids)}, "
                f"resolved={resolved}, unresolved={unresolved}, empty_patches={empty_patches}"
            )
        shutil.copy2(candidates[0], report / "official_summary.json")

    def evaluate_only(self) -> int:
        self.write_config()
        self.emit("evaluation_started", pid=os.getpid(), evaluation_only=True)
        self.update("evaluation")
        self.evaluate()
        self.emit("run_complete", evaluation_only=True)
        self.update("complete")
        state = read_json(self.root / "status.json")
        state["process_alive"] = False
        state["finished_at"] = now()
        atomic_json(self.root / "status.json", state)
        return 0

    def refresh_complete(self) -> int:
        self.update("complete")
        state = read_json(self.root / "status.json")
        state["process_alive"] = False
        state["finished_at"] = state.get("finished_at", now())
        atomic_json(self.root / "status.json", state)
        return 0

    def orchestrate(self) -> int:
        self.write_config()
        self.emit("run_started", pid=os.getpid())
        self.update("inference")
        logs = self.root / "worker_logs"
        logs.mkdir(exist_ok=True)
        procs = []
        for worker in range(1, self.workers + 1):
            handle = (logs / f"worker_{worker}.log").open("a")
            proc = subprocess.Popen([
                sys.executable, __file__, "worker", self.agent, str(self.run), str(self.socket), str(worker),
                "--workers", str(self.workers),
            ], stdout=handle, stderr=subprocess.STDOUT)
            procs.append((proc, handle))
        while any(proc.poll() is None for proc, _ in procs):
            current_by_worker: dict[int, str] = {}
            for event in self.events.read_text(errors="replace").splitlines() if self.events.exists() else []:
                try:
                    row = json.loads(event)
                    worker = int(row.get("worker", 0))
                    if row.get("event") == "case_started" and worker:
                        current_by_worker[worker] = row["instance_id"]
                    elif row.get("event") == "case_attempt" and worker:
                        current_by_worker.pop(worker, None)
                except Exception:
                    pass
            self.update("inference", [current_by_worker[key] for key in sorted(current_by_worker)])
            time.sleep(20)
        for proc, handle in procs:
            handle.close()
        if self.counts()[0] != len(records()):
            raise RuntimeError(
                f"inference terminal artifacts incomplete: {self.counts()[0]}/{len(records())}"
            )
        if self.counts()[1] != len(records()):
            raise RuntimeError(f"inference valid artifacts incomplete: {self.counts()[1]}/{len(records())}")
        if os.environ.get("EVIFUZZ_SKIP_EVALUATION") == "1":
            self.predictions()
            self.emit("inference_complete", evaluation_skipped=True)
        else:
            self.update("evaluation")
            self.evaluate()
        self.emit("run_complete")
        self.update("complete")
        state = read_json(self.root / "status.json")
        state["process_alive"] = False
        state["finished_at"] = now()
        atomic_json(self.root / "status.json", state)
        return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    worker = sub.add_parser("worker")
    worker.add_argument("agent", choices=("codex", "opencode"))
    worker.add_argument("run", type=int)
    worker.add_argument("socket", type=Path)
    worker.add_argument("worker", type=int)
    worker.add_argument("--workers", type=int, default=WORKERS)
    orchestrate = sub.add_parser("orchestrate")
    orchestrate.add_argument("agent", choices=("codex", "opencode"))
    orchestrate.add_argument("run", type=int)
    orchestrate.add_argument("socket", type=Path)
    orchestrate.add_argument("--workers", type=int, default=WORKERS)
    evaluate = sub.add_parser("evaluate")
    evaluate.add_argument("agent", choices=("codex", "opencode"))
    evaluate.add_argument("run", type=int)
    evaluate.add_argument("socket", type=Path)
    evaluate.add_argument("--workers", type=int, default=WORKERS)
    refresh = sub.add_parser("refresh-complete")
    refresh.add_argument("agent", choices=("codex", "opencode"))
    refresh.add_argument("run", type=int)
    refresh.add_argument("socket", type=Path)
    refresh.add_argument("--workers", type=int, default=WORKERS)
    args = parser.parse_args()
    run = Run(args.agent, args.run, args.socket, args.workers)
    if args.command == "worker":
        return run.worker(args.worker)
    try:
        if args.command == "refresh-complete":
            return run.refresh_complete()
        if args.command == "evaluate":
            return run.evaluate_only()
        return run.orchestrate()
    except Exception as exc:
        run.emit("run_failed", error=f"{type(exc).__name__}: {exc}")
        run.update("failed", error=f"{type(exc).__name__}: {exc}")
        state = read_json(run.root / "status.json")
        state["process_alive"] = False
        atomic_json(run.root / "status.json", state)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
