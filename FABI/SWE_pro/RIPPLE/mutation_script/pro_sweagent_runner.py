#!/usr/bin/env python3
"""Adapter around the existing SWE-Agent runner for multi-file mutations."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from runner_support import apply_multi_file_mutation


SOURCE = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/naive_mutation/mutation_scripts/pro_sweagent_runner.py")
spec = importlib.util.spec_from_file_location("existing_pro_sweagent_runner", SOURCE)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def apply_mutation(self, row, repo, attempt):
    return apply_multi_file_mutation(
        repo, row, self.args.mutation_root, self.args.mutation_agent,
        attempt / "mutation_applied.json", module.atomic,
    )


module.Runner.apply_mutation = apply_mutation

if __name__ == "__main__":
    raise SystemExit(module.main())
