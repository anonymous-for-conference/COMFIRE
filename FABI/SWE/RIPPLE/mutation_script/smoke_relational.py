#!/usr/bin/env python3
import json,subprocess
from pathlib import Path
from experiment import prepare_local_worktree
from mutation_pipeline import generate
ROOT=Path('/data/zlyuaj/coding_agent/EviFuzz')
CASE=ROOT/'original_passed_cases/Codex/gpt54mini_lite/cases/astropy__astropy-12907'
BASE=Path('/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories/astropy')
OUT=ROOT/'RIPPLE/mutation_result/round2_relational_smoke'
task=json.loads((CASE/'task.json').read_text()); OUT.mkdir(parents=True,exist_ok=True)
for index,operator in enumerate(('R1','R2','R3'),1):
 run=OUT/operator; run.mkdir(parents=True,exist_ok=True); repo=prepare_local_worktree(run,BASE,task['base_commit'])
 try:
  generate(CASE,repo,run/'mutation','level_1,level_2',12907+index,1,forced_operator=operator,enabled_operators=('R1','R2','R3'))
 finally:
  subprocess.run(['git','reset','--hard',task['base_commit']],cwd=repo,check=False,stdout=subprocess.DEVNULL); subprocess.run(['git','clean','-fd'],cwd=repo,check=False,stdout=subprocess.DEVNULL)
