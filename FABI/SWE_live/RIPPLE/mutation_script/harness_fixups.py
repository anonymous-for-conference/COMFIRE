"""Apply run-private reliability fixes without editing the clean LIVE harness."""
from __future__ import annotations

from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if new in text:
        return
    if text.count(old) != 1:
        raise RuntimeError(f"private harness marker mismatch: {path.name}: {old[:60]!r}")
    path.write_text(text.replace(old, new, 1))


def apply_private_harness_fixups(harness: Path) -> None:
    worker = harness / "agent_worker.py"
    replace_once(worker,
        '            for row in self.rows:\n'
        '                self.current = row["instance_id"]\n'
        '                self.update()\n'
        '                if not self.run_case(row):\n'
        '                    raise RuntimeError(f"infrastructure retries exhausted: {self.current}")\n',
        '            deferred = []\n'
        '            for row in self.rows:\n'
        '                self.current = row["instance_id"]\n'
        '                self.update()\n'
        '                if not self.run_case(row):\n'
        '                    self.log(f"deferred infrastructure retry: {self.current}")\n'
        '                    deferred.append(row)\n'
        '            for retry_round in range(1, 3):\n'
        '                if not deferred:\n'
        '                    break\n'
        '                self.log(f"deferred retry round {retry_round}: {len(deferred)} case(s)")\n'
        '                time.sleep(30 * retry_round)\n'
        '                remaining = []\n'
        '                for row in deferred:\n'
        '                    self.current = row["instance_id"]\n'
        '                    self.update()\n'
        '                    if not self.run_case(row):\n'
        '                        remaining.append(row)\n'
        '                deferred = remaining\n'
        '            if deferred:\n'
        '                raise RuntimeError("infrastructure retries exhausted after deferred rounds: "\n'
        '                                   + ", ".join(row["instance_id"] for row in deferred))\n')

    orchestrator = harness / "orchestrate.py"
    replace_once(orchestrator,
        '        atomic_text(self.root / "RUN_CONFIG.md", "\\n".join([',
        '        config_name = f"RUN_CONFIG_{self.args.attempt_label}.md" if self.args.attempt_label else "RUN_CONFIG.md"\n'
        '        atomic_text(self.root / config_name, "\\n".join([')
    replace_once(orchestrator,
        '        log = (self.root / "logs/podman-service.log").open("a")',
        '        suffix = f"_{self.args.attempt_label}" if self.args.attempt_label else ""\n'
        '        log = (self.root / "logs" / f"podman-service{suffix}.log").open("a")')
    replace_once(orchestrator,
        '        log = (self.root / "logs" / f"{agent}-coordinator.log").open("a")',
        '        suffix = f"_{self.args.attempt_label}" if self.args.attempt_label else ""\n'
        '        log = (self.root / "logs" / f"{agent}-coordinator{suffix}.log").open("a")')
    replace_once(orchestrator,
        '        if agent in self.selection_files:\n'
        '            command.extend(["--selection-file", str(self.selection_files[agent])])',
        '        if agent in self.selection_files:\n'
        '            command.extend(["--selection-file", str(self.selection_files[agent])])\n'
        '        if self.args.attempt_label:\n'
        '            command.extend(["--attempt-label", self.args.attempt_label])')
    replace_once(orchestrator,
        '    parser.add_argument("--prepare-only", action="store_true")',
        '    parser.add_argument("--prepare-only", action="store_true")\n'
        '    parser.add_argument("--attempt-label", default="")')
    replace_once(orchestrator,
        '            "log": str(self.root / "RUN.log"), "output_dir": str(self.root),',
        '            "log": str(self.root / (f"RUN_{self.args.attempt_label}.log" if self.args.attempt_label else "RUN.log")),\n'
        '            "output_dir": str(self.root),')

    coordinator = harness / "agent_coordinator.py"
    replace_once(coordinator,
        '            run_id = f"{self.args.run}-{self.args.agent}"',
        '            run_id = f"{self.args.run}-{self.args.agent}"\n'
        '            if self.args.attempt_label:\n'
        '                run_id += f"-{self.args.attempt_label}"')
    replace_once(coordinator,
        '            log_path = self.out / "evaluation.log"',
        '            log_name = f"evaluation_{self.args.attempt_label}.log" if self.args.attempt_label else "evaluation.log"\n'
        '            log_path = self.out / log_name')
