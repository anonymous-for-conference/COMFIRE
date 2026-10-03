#!/usr/bin/env python3
import json,subprocess
from pathlib import Path
from experiment import prepare_local_worktree
from mutation_pipeline import generate
ROOT=Path('/data/zlyuaj/coding_agent/EviFuzz'); CASE=ROOT/'original_passed_cases/Codex/gpt54mini_lite/cases/astropy__astropy-12907'; BASE=Path('/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories/astropy'); OUT=ROOT/'RIPPLE/mutation_result/round2_relational_smoke/R3_relation'; task=json.loads((CASE/'task.json').read_text()); OUT.mkdir(parents=True,exist_ok=True); repo=prepare_local_worktree(OUT,BASE,task['base_commit'])
try:
 generate(CASE,repo,OUT/'mutation','level_1,level_2',13000,None,forced_operator='R3',enabled_operators=('R1','R2','R3'),selected_cluster_ids=('astropy__astropy-12907:level_2:cluster_0005',))
finally:
 subprocess.run(['git','reset','--hard',task['base_commit']],cwd=repo,stdout=subprocess.DEVNULL); subprocess.run(['git','clean','-fd'],cwd=repo,stdout=subprocess.DEVNULL)
