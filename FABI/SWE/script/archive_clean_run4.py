#!/usr/bin/env python3
"""Archive validated run-4 attempts into the three clean-case collections."""
from pathlib import Path
import json, shutil, sys

ROOT=Path('<local-data>/coding_agent/EviFuzz'); ARCH=ROOT/'original_passed_cases'
spec={'swe_lite': ('sweagent_gpt54_mini_run4', ARCH/'SWE-Agent/gpt54mini_lite'), 'codex': ('codex_gpt54_mini_run4', ARCH/'Codex/gpt54mini_lite'), 'opencode': ('opencode_gpt54_mini_run4', ARCH/'OpenCode/gpt54mini_lite')}
agent=sys.argv[1] if len(sys.argv)>1 else None
if agent not in spec: raise SystemExit('usage: archive_clean_run4.py swe|codex|opencode')
srcname,dest=spec[agent]; src=ROOT/srcname
if agent == 'swe_lite' and not (src/'cases').exists():
    src = ROOT/'sweagent_gpt54_mini_run4_retry3'
case_root = src/'run_4'/'cases' if agent == 'swe_lite' else src/'cases'
ids=[p.name for p in sorted(case_root.iterdir()) if p.is_dir()]
done=0
for iid in ids:
    attempts=sorted((case_root/iid).glob('attempt_*'), reverse=True)
    selected=None
    for a in attempts:
        try:
            if json.loads((a/'validation.json').read_text()).get('valid') is True: selected=a; break
        except Exception: pass
    if selected is None: continue
    out=dest/'cases'/iid/'run_4'; out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists(): shutil.rmtree(out)
    shutil.copytree(selected,out,copy_function=shutil.copy2); done+=1
if (src/'evaluation_summary/official_summary.json').exists(): shutil.copy2(src/'evaluation_summary/official_summary.json', dest/'run_4_official_summary.json')
print(json.dumps({'agent':agent,'archived':done,'source':str(src),'destination':str(dest)}))
