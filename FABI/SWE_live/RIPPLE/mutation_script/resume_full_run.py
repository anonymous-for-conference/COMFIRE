#!/usr/bin/env python3
"""Resume the current run from verified mutation patches and terminal inference cache."""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mutation_pipeline as mp


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--attempt-label", required=True)
    args = parser.parse_args()
    root = args.run_root.resolve()
    lock = root / "locks" / "resume.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open("a+") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        manifest = json.loads((root / "selection_manifest.json").read_text())
        cases = manifest["cases"] if "cases" in manifest else None
        if cases is None:
            # The harness overwrites the manifest with its selection summary.
            cases = []
            for slug, agent in (("swe-agent", "SWE_Agent"), ("opencode", "OpenCode"), ("codex", "Codex")):
                selection = json.loads((root / "selections" / f"{slug}.json").read_text())
                cases.extend({"agent": agent, "instance_id": iid} for iid in selection["instance_ids"])
        if len(cases) != 172:
            raise RuntimeError(f"selection is not 172 cases: {len(cases)}")
        slugs = {"SWE_Agent": "swe-agent", "OpenCode": "opencode", "Codex": "codex"}
        cached = 0
        for row in cases:
            slug, iid = slugs[row["agent"]], row["instance_id"]
            patch_dir = root / "worker_patches" / slug / iid
            meta = json.loads((patch_dir / "mutation.json").read_text())
            patch = patch_dir / "mutation.patch"
            if hashlib.sha256(patch.read_bytes()).hexdigest() != meta["sha256"]:
                raise RuntimeError(f"mutation checksum mismatch: {slug} {iid}")
            if not patch.stat().st_size and meta.get("status") != "no_documentation":
                raise RuntimeError(f"unexpected empty mutation patch: {slug} {iid}")
            for validation in (root / slug / "workers").glob(f"worker_*/cases/{iid}/validation.json"):
                value = json.loads(validation.read_text())
                if value.get("terminal") is True:
                    prediction = validation.parent / f"attempt_{value['attempt']:02d}" / "prediction.json"
                    if not prediction.is_file() or json.loads(prediction.read_text()).get("instance_id") != iid:
                        raise RuntimeError(f"invalid cached prediction: {slug} {iid}")
                    cached += 1
                    break
        print(f"[{mp.now()}] verified mutation patches=172; valid terminal inference cache={cached}; pending={172-cached}", flush=True)
        key, base = mp.read_key()
        env = os.environ.copy()
        env.update(OPENAI_API_KEY=key, OPENAI_BASE_URL=base, RIPPLE_MUTATION_PATCH_ROOT=str(root / "worker_patches"))
        command = [sys.executable, str(root / "harness" / "orchestrate.py"),
                   "--run", root.name, "--output", str(root), "--export", str(root / "export"),
                   "--selection-dir", str(root / "selections"), "--agent-parallelism", "3",
                   "--inference-workers", "2", "--eval-workers", "2", "--ignore-external-load",
                   "--podman-socket", f"/tmp/ripple-{root.name}-{args.attempt_label}-podman.sock",
                   "--attempt-label", args.attempt_label]
        print(f"[{mp.now()}] starting private harness attempt={args.attempt_label} pid={os.getpid()}", flush=True)
        rc = subprocess.run(command, cwd=root / "harness", env=env).returncode
        print(f"[{mp.now()}] private harness exit={rc}", flush=True)
        return rc


if __name__ == "__main__":
    raise SystemExit(main())
