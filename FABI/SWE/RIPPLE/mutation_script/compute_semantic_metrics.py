#!/usr/bin/env python3
import csv,json,re,statistics
from pathlib import Path
B=Path('/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_result/local4r1_repo4r2'); R=B/'all_agents_round2_adaptive_v2_20260901_165815'; C=Path('/data/zlyuaj/coding_agent/EviFuzz/original_passed_cases')
def fl(s): return set(re.findall(r'(?<![\w.-])([\w@.+-]+(?:/[\w@.+-]+)+\.(?:py|js|ts|java|go|rs|md|rst|yaml|yml|json|toml|c|h|cpp))',s or ''))
def pl(p):
 try:
  s=json.load(open(p)).get('model_patch',''); return sum(x.startswith(('+','-')) and not x.startswith(('+++','---')) for x in s.splitlines())
 except: return None
def cm(a,i):
 h=list((C/{'codex':'Codex','opencode':'OpenCode','sweagent':'SWE-Agent'}[a]).glob(f'*/cases/{i}/run_4'))
 if not h:return None,None
 r=h[0]; t=''.join(p.read_text(errors='ignore') for p in r.glob('*jsonl')); return len(fl(t)),pl(r/'prediction.json')
rows=[]
for a in ('codex','sweagent','opencode'):
 d=json.load(open(R/a/'BATCH_SUMMARY.json')); cp=B/'cost_analysis'/'resolved'/f'{a}-round2.csv'; costs={x['case']:x for x in csv.DictReader(open(cp))} if cp.exists() else {}
 for x in d['results']:
  i=x['instance_id']; q=costs.get(i,{}); rr=float(q['read_loc']) if q.get('read_loc') not in (None,'','N/A') else None; ee=float(q['edit_lines']) if q.get('edit_lines') not in (None,'','N/A') else None; br,be=cm(a,i); dr=(rr-br)/br if br not in (None,0) and rr is not None else None; de=(ee-be)/be if be not in (None,0) and ee is not None else None; af=bool((dr is not None and abs(dr)>=.5) or (de is not None and abs(de)>=.5) or (be==0 and ee not in (None,0))) if br is not None else None
  rows.append({'agent':a,'case':i,'status':'resolved' if x.get('resolved') else 'failed','read_loc':rr,'edit_lines':ee,'clean_read_loc':br,'clean_edit_lines':be,'delta_read_loc':dr,'delta_edit_lines':de,'affected':af,'recovered':(af and bool(x.get('resolved'))) if af is not None else None})
  ops=[]
  try: ops=[c.get('selected_operator') for c in json.load(open(str(Path(x.get('run_root','')).as_posix().replace('/mutation_result/all_agents_round2_adaptive_v2_20260901_165815','/mutation_result/local4r1_repo4r2/all_agents_round2_adaptive_v2_20260901_165815')+'/mutation/manifest.json'))).get('clusters',[])]
  except: pass
  lc=sum(o in {'L1','L2','L3'} for o in ops); rc=sum(o in {'R1','R2','R3'} for o in ops); cat='entity-local' if lc>rc else ('repo-relational' if rc>lc else 'mixed/unknown')
  rows[-1]['category']=cat
fields=['agent','case','category','status','read_loc','edit_lines','clean_read_loc','clean_edit_lines','delta_read_loc','delta_edit_lines','affected','recovered']
with open(R/'semantic_operator_metrics.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
with open(R/'semantic_operator_summary.md','w') as f:
 f.write('# 第二轮 mutation：语义 operator 指标\n\nAffected 阈值为 Read Loc 或 Edit Length 相对 clean run 4 变化达到 50%。Recover 指 affected 且 evaluation resolved。\n\n|类别|case|正确|错误|affected|affected正确|recover率|平均ΔRead|平均ΔEdit|\n|---|---:|---:|---:|---:|---:|---:|---:|---:|\n')
 for k in ('entity-local','repo-relational'):
  g=[x for x in rows if x['category']==k]; a=[x for x in g if x['affected'] is True]; z=[x for x in a if x['recovered'] is True]; dr=[x['delta_read_loc'] for x in a if x['delta_read_loc'] is not None]; de=[x['delta_edit_lines'] for x in a if x['delta_edit_lines'] is not None]; f.write(f'|{k}|{len(g)}|{sum(x["status"]=="resolved" for x in g)}|{sum(x["status"]=="failed" for x in g)}|{len(a)}|{len(z)}|{len(z)/len(a) if a else "N/A"}|{statistics.mean(dr) if dr else "N/A"}|{statistics.mean(de) if de else "N/A"}|\n')
print('updated',R/'semantic_operator_metrics.csv')
