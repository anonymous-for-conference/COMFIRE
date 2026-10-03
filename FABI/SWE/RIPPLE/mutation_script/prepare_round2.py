#!/usr/bin/env python3
"""Prepare adaptive round two from round-one exposure and trace evidence."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

ROOT=Path('/data/zlyuaj/coding_agent/EviFuzz')
CLEAN={'codex':ROOT/'original_passed_cases/Codex/gpt54mini_lite/cases','sweagent':ROOT/'original_passed_cases/SWE-Agent/luna_verified/cases','opencode':ROOT/'original_passed_cases/OpenCode/gpt54mini_lite/cases'}
EXT=r'(?:py|pyi|js|ts|tsx|jsx|java|rb|rs|go|c|cc|cpp|h|hpp|rst|md|txt|toml|ya?ml|json|ini|cfg)'
PATH_RE=re.compile(r'(?<![\w.-])(?:/testbed/|/workspace/|(?:a|b)/)?([\w.-]+(?:/[\w.-]+)+\.(?:'+EXT+r'))')
def load(p): return json.loads(Path(p).read_text())
def strings(x):
 if isinstance(x,str): yield x
 elif isinstance(x,dict):
  for v in x.values(): yield from strings(v)
 elif isinstance(x,list):
  for v in x: yield from strings(v)
def paths(vals):
 out=[]
 for s in vals:
  for m in PATH_RE.finditer(s):
   p=m.group(1)
   if p not in out: out.append(p)
 return out
def patch_files(p): return sorted(set(re.findall(r'^diff --git a/(.+?) b/',p or '',re.M)))
def trace_summary(agent,p,pred=None):
 vals=[]; turns=0; patch=''
 if agent=='sweagent':
  d=load(p); tr=d.get('trajectory',[]); turns=len(tr)
  for e in tr: vals.extend(strings({'action':e.get('action',''),'observation':e.get('observation','')}))
  pp=Path(p).with_suffix('.patch'); patch=pp.read_text(errors='replace') if pp.exists() else ''
 else:
  for line in Path(p).read_text(errors='replace').splitlines():
   try: e=json.loads(line)
   except: continue
   if isinstance(e,dict):
    turns += e.get('type') in ('turn.started','step_start','step-start')
   vals.extend(strings(e))
  if pred and Path(pred).exists():
   try: patch=load(pred).get('model_patch','')
   except: pass
 seq=paths(vals); return {'localization_sequence':seq,'localization_files':sorted(set(seq)),'edit_files':patch_files(patch),'turns':turns,'trace':str(p)}
def clean(agent,iid):
 out=[]; case=CLEAN[agent]/iid
 for run in sorted(case.glob('run_*')):
  if agent=='sweagent':
   ts=sorted(run.glob('attempt_*/agent/*/*.traj'))
   if ts: out.append(trace_summary(agent,ts[-1]))
  else:
   p=run/('codex.jsonl' if agent=='codex' else 'opencode.jsonl')
   if p.exists(): out.append(trace_summary(agent,p,run/'prediction.json'))
 return out
def jac(a,b):
 a,b=set(a),set(b); return 1.0 if not a and not b else len(a&b)/len(a|b) if a|b else 0.0
def score(a,b):
 return .5*jac(a['localization_files'],b['localization_files'])+.5*jac(a['edit_files'],b['edit_files'])
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); ap.add_argument('--similarity-threshold',type=float,default=.5); a=ap.parse_args(); root,out=Path(a.root),Path(a.out); out.mkdir(parents=True,exist_ok=True); rows=[]
 for agent in CLEAN:
  for run in sorted((root/agent/'runs').glob('*')):
   mp,tp=run/'mutation/manifest.json',run/'trace_analysis.json'
   if not(mp.exists() and tp.exists()): continue
   man,tr=load(mp),load(tp); iid=man.get('instance_id') or run.name.split('_',1)[-1]; offp=run/'interface/evaluation_summary/official_summary.json'; off=load(offp) if offp.exists() else {}; stopped=bool(off.get('completed_ids')) and iid not in off.get('resolved_ids',[])
   lm={x.get('unit_id'):x for x in tr.get('locations',[])}; clusters=[]; total=exposed=0; repl=[]
   for c in man.get('clusters',[]):
    us=c.get('locations',[]); hit=sum(bool(lm.get(u.get('unit_id'),{}).get('mutated_text_seen')) for u in us); ok=hit>len(us)/2; clusters.append({'cluster_id':c.get('cluster_id'),'level':c.get('level'),'positions':len(us),'exposed_positions':hit,'exposed':ok}); total+=len(us); exposed+=hit; repl += [] if ok else [c.get('cluster_id')]
   mt=None; av=tr.get('attempt');
   apth=Path(av) if av else None
   if not apth or not apth.exists():
    fallback=run/'interface/cases'/iid
    attempts=sorted(fallback.glob('attempt_*'))
    apth=attempts[-1] if attempts else None
   if apth and apth.exists():
    cand=sorted(apth.rglob('*.traj' if agent=='sweagent' else ('codex.jsonl' if agent=='codex' else 'opencode.jsonl')))
    if cand: mt=trace_summary(agent,cand[-1],apth/'prediction.json' if agent!='sweagent' else None)
   cs=clean(agent,iid) if mt else []; comps=[score(mt,c) for c in cs] if mt else []; best=max(comps,default=None); large=None if best is None else best<a.similarity_threshold; majority=exposed>total/2 if total else False
   action='stop_round1_failed' if stopped else ('replace_unexposed_clusters' if not majority else ('add_two_clusters' if large is True else 'upgrade_to_R1_R3'))
   rows.append({'agent':agent,'instance_id':iid,'run_root':str(run),'stopped_after_round1':stopped,'position_count':total,'exposed_positions':exposed,'exposure_ratio':exposed/total if total else 0,'clusters':clusters,'unexposed_clusters':repl,'exposure_majority':majority,'trajectory_large_change':large,'trajectory_best_similarity':best,'trajectory_comparisons':comps,'next_action':action})
 report={'method':{'cluster_exposed':'hits > positions / 2','trajectory_score':'0.50 localization-file Jaccard + 0.50 edit-file Jaccard; access order excluded','similarity_threshold':a.similarity_threshold},'round1_cases':len(rows),'stopped_cases':sum(r['stopped_after_round1'] for r in rows),'exposure_majority_cases':sum(r['exposure_majority'] for r in rows),'exposure_below_half_cases':sum(not r['exposure_majority'] for r in rows),'trajectory_large_change_cases':sum(r['trajectory_large_change'] is True for r in rows),'trajectory_no_large_change_cases':sum(r['trajectory_large_change'] is False for r in rows),'trajectory_unknown_cases':sum(r['trajectory_large_change'] is None for r in rows),'cases':rows}
 (out/'round1_exposure_trajectory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n'); (out/'round1_exposure_trajectory.md').write_text('# 第一轮 Mutation 暴露与轨迹审计\n\n'+json.dumps({k:v for k,v in report.items() if k!='cases'},ensure_ascii=False,indent=2)+'\n'); print(json.dumps({k:v for k,v in report.items() if k!='cases'},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
