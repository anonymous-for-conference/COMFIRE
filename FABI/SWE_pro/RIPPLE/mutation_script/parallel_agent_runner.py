#!/usr/bin/env python3
"""Invoke the existing two-worker coordinator through local runner adapters."""

from __future__ import annotations

import importlib.util
from pathlib import Path


SOURCE = Path("/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/naive_mutation/mutation_scripts/parallel_agent_runner.py")
spec = importlib.util.spec_from_file_location("existing_parallel_agent_runner", SOURCE)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)
module.ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    raise SystemExit(module.main())
