#!/usr/bin/env python3
"""Run Level-2 mutation for the first ten Codex clean cases serially."""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path("/data/zlyuaj/coding_agent/EviFuzz")
CASES = ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases"
RESULTS = ROOT / "RIPPLE/mutation_result"
LAUNCH = ROOT / "RIPPLE/mutation_script/launch.sh"
REPOS = Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories")


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    cases = sorted(p for p in CASES.iterdir() if (p / "clustered_doc.jsonl").exists())[:10]
    batch_id = dt.datetime.now().strftime("level2_l123_first10_%Y%m%d_%H%M%S")
    batch_root = RESULTS / batch_id
    batch_root.mkdir(parents=True)
    config = {
        "batch_id": batch_id, "started_at": now(), "level": "level_2",
        "enabled_operators": ["L1", "L2", "L3"], "k": 3,
        "selection": "lexicographically first ten Codex clean cases",
        "cases": [p.name for p in cases], "workers": 1,
        "evaluation": "official SWE-bench Lite harness via RIPPLE interface",
    }
    (batch_root / "BATCH_CONFIG.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    (batch_root / "BATCH.log").write_text("")
    results = []
    first_success_written = False
    for index, case_dir in enumerate(cases, 1):
        iid = case_dir.name
        slug = iid.split("__", 1)[0]
        base_repo = REPOS / slug
        run_id = f"{slug.replace('-', '')}{iid.split('-')[-1]}_l2_l123_{index:02d}"
        run_root = RESULTS / run_id
        cmd = [str(LAUNCH), str(run_root), run_id, "level_2", "3", iid, str(base_repo)]
        with (batch_root / "BATCH.log").open("a") as log:
            log.write(f"[{now()}] START {index}/10 {iid} {' '.join(cmd)}\n")
        try:
            subprocess.run(cmd, check=True)
        except Exception as exc:
            results.append({"index": index, "instance_id": iid, "status": "launch_failed", "error": repr(exc)})
            continue
        while True:
            status_path = run_root / "status.json"
            status = json.loads(status_path.read_text()) if status_path.exists() else {}
            phase = status.get("phase")
            if phase in {"completed", "failed"}:
                break
            time.sleep(20)
        outcome = {
            "index": index, "instance_id": iid, "run_root": str(run_root),
            "phase": status.get("phase"), "success": status.get("success", 0),
            "failed": status.get("failed", 0), "errors": status.get("errors", 0),
            "finished_at": status.get("finished_at", now()),
        }
        manifest = run_root / "mutation/manifest.json"
        if manifest.exists():
            data = json.loads(manifest.read_text())
            outcome.update({"mutation_count": data.get("mutation_count"), "clusters": [
                {"cluster_id": c["cluster_id"], "label": c["label"],
                 "operator": c["selected_operator"], "locations": len(c["locations"])}
                for c in data["clusters"]
            ]})
        results.append(outcome)
        with (batch_root / "BATCH.log").open("a") as log:
            log.write(f"[{now()}] END {index}/10 {json.dumps(outcome, ensure_ascii=False)}\n")
        if outcome["phase"] == "completed" and not first_success_written:
            (batch_root / "FIRST_SUCCESS.json").write_text(json.dumps(outcome, ensure_ascii=False, indent=2) + "\n")
            first_success_written = True
    summary = {"batch_id": batch_id, "finished_at": now(), "total": len(cases), "results": results}
    (batch_root / "BATCH_SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    return 0 if len(results) == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
