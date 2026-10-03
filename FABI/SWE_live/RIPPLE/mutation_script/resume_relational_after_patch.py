#!/usr/bin/env python3
"""Finish the one missing relational patch, then enter the private harness."""
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

import mutation_pipeline as mp
import full_run as fr

RUN = Path(sys.argv[1]).resolve()
MISSING = ("SWE_Agent", "deepset-ai__haystack-8799")


def selected_rows():
    rows = []
    for row in csv.DictReader(mp.CSV_PATH.open()):
        if (row["agent"], row["instance_id"]) == MISSING:
            task = json.loads((Path(row["round_1_artifact"]) / "task.json").read_text())
            row = dict(row)
            row.update(repo=task["repo"], base_commit=task["base_commit"])
            rows.append(row)
    if len(rows) != 1:
        raise RuntimeError(f"missing case lookup returned {len(rows)} rows")
    return rows[0]


def main() -> int:
    row = selected_rows()
    target = RUN / "patches" / row["agent"] / row["instance_id"]
    last = None
    # Seeds after the failed attempt select different clusters.  A successful
    # make_patch writes and checksum records the patch atomically at the end.
    for seed in range(20260932, 20260945):
        try:
            clusters, docs = mp.clusters_for(row, 3, seed)
            print(f"trying seed={seed} clusters={[c['cluster_id'] for c in clusters]}", flush=True)
            meta = mp.make_patch(row, clusters, docs, RUN, ("R1", "R2", "R3"))
            patch = Path(meta["patch"])
            if not patch.is_file() or hashlib.sha256(patch.read_bytes()).hexdigest() != meta["sha256"]:
                raise RuntimeError("target patch checksum verification failed")
            print(f"patch ready seed={seed} bytes={patch.stat().st_size}", flush=True)
            break
        except Exception as exc:
            last = exc
            print(f"seed={seed} failed: {type(exc).__name__}: {exc}", flush=True)
    else:
        raise RuntimeError(f"could not generate missing patch: {last}")

    flat = RUN / "worker_patches" / "swe-agent" / row["instance_id"]
    flat.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target / "mutation.patch", flat / "mutation.patch")
    shutil.copy2(target / "mutation.json", flat / "mutation.json")
    patches = list((RUN / "worker_patches").glob("*/*/mutation.patch"))
    if len(patches) != 172:
        raise RuntimeError(f"patch count mismatch: {len(patches)}/172")
    fr.event(RUN, kind="repair", stage="mutation", result="success",
             agent=row["agent"], instance_id=row["instance_id"], seed=seed,
             patch=str(target / "mutation.patch"))
    fr.event(RUN, kind="phase", phase="inference_evaluation", total=172,
             repaired_missing_case=row["instance_id"])
    print("starting six inference/evaluation workers", flush=True)
    rc = mp.run_harness(fr.selected_rows(), RUN, RUN / "worker_patches")
    fr.event(RUN, kind="terminal", phase="complete" if rc == 0 else "harness_failed", exit_code=rc)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
