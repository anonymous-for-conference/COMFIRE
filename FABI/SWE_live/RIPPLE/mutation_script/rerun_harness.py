#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
import mutation_pipeline as m

root = Path(sys.argv[1]).resolve()
rows = []
for agent in ("SWE_Agent", "OpenCode", "Codex"):
    for row in [r for r in csv.DictReader(m.CSV_PATH.open()) if r["agent"] == agent][:2]:
        task = json.loads((Path(row["round_1_artifact"]) / "task.json").read_text())
        row = dict(row); row.update(repo=task["repo"], base_commit=task["base_commit"])
        rows.append(row)
raise SystemExit(m.run_harness(rows, root, root / "worker_patches"))
