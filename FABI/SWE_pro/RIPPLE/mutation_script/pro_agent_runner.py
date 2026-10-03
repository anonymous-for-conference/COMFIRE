#!/usr/bin/env python3
"""Adapter around the existing Codex/OpenCode runner for multi-file mutations."""

from __future__ import annotations

import importlib.util
from pathlib import Path

from runner_support import apply_multi_file_mutation


SOURCE = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/naive_mutation/mutation_scripts/pro_agent_runner.py")
spec = importlib.util.spec_from_file_location("existing_pro_agent_runner", SOURCE)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


def apply_mutation(repo, row, mutation_root, agent, case):
    return apply_multi_file_mutation(repo, row, mutation_root, agent, case / "mutation_applied.json", module.atomic)


module.apply_mutation = apply_mutation

if __name__ == "__main__":
    module.main()
