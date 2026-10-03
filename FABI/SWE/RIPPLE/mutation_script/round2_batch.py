#!/usr/bin/env python3
"""Adaptive round-two staged runner; one worker per agent and isolated case worktrees."""
from __future__ import annotations
import argparse,concurrent.futures as cf,hashlib,json,os,random,subprocess,threading,traceback
from pathlib import Path
from batch_staged import inference_stage,evaluation_stage,finalize,parallel_stage
from experiment import atomic_json,now,prepare_local_worktree
from mutation_pipeline import apply_mutations,atomic_text,generate,jsonl,load_levels_priority
ROOT=Path('/data/zlyuaj/coding_agent/EviFuzz')
CASE_ROOTS={'codex':ROOT/'original_passed_cases/Codex/gpt54mini_lite/cases','sweagent':ROOT/'original_passed_cases/SWE-Agent/luna_verified/cases','opencode':ROOT/'original_passed_cases/OpenCode/gpt54mini_lite/cases'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--prep',required=True); ap.add_argument('--out',required=True); ap.add_argument('--ids'); ap.add_argument('--codex-workers',type=int,default=2); ap.add_argument('--sweagent-workers',type=int,default=1); ap.add_argument('--opencode-workers',type=int,default=2); ap.add_argument('--stop-after',choices=('mutation','inference','evaluation'),default='evaluation'); a=ap.parse_args(); prep=json.loads(Path(a.prep).read_text()); out=Path(a.out); out.mkdir(parents=True,exist_ok=True); worker_counts={'codex':a.codex_workers,'sweagent':a.sweagent_workers,'opencode':a.opencode_workers}; selected=set(a.ids.split(',')) if a.ids else None
 items=[]
 for row in prep['cases']:
  if selected is not None and row['instance_id'] not in selected and f"{row['agent']}:{row['instance_id']}" not in selected: continue
  if row['stopped_after_round1']: continue
  agent,iid=row['agent'],row['instance_id']; old=Path(row['run_root']).resolve(); source=old/'source_repo.json'
  if not source.exists(): continue
  src=json.loads(source.read_text()); case=CASE_ROOTS[agent]/iid
  if not (case/'task.json').exists():
   case=ROOT/'original_passed_cases/SWE-Agent/gpt54mini_lite/cases'/iid
  if not (case/'task.json').exists():
   case=ROOT/'original_passed_cases/Codex/gpt54mini_lite/cases'/iid
  if not (case/'task.json').exists(): continue
  # <= half exposure replaces clusters; large change adds two, otherwise upgrade relational operators.
  action=row['next_action'];
  if action=='hold_missing_trace': action='upgrade_to_R1_R3'
  k=7 if action=='add_two_clusters' else 5; level='level_1,level_2,level_3' if action=='replace_unexposed_clusters' else 'level_1,level_2'; relational=action in ('upgrade_to_R1_R3','add_two_clusters')
  items.append({'agent':agent,'instance_id':iid,'case_dir':str(case),'base_repo':src['base_repo'],'base_commit':src['base_commit'],'run_root':str(out/agent/'runs'/f"{len(items)+1:03d}_{iid}"),'old_run_root':str(old),'unexposed_clusters':row['unexposed_clusters'],'seed':90000+len(items),'k':k,'level':level,'forced_operator':None,'enabled_operators':('R1','R2','R3') if relational else ('L1','L2','L3'),'round1_action':action})
 atomic_json(out/'RUN_CONFIG.json',{'run_id':out.name,'started_at':now(),'stage':'mutation,inference,evaluation','worker_counts':worker_counts,'items':len(items),'api_key':'configured via environment','adaptive_rules':'round1 exposure/trajectory report v2; access order excluded'})
 (out/'RUN.log').write_text('')
 atomic_json(out/'status.json',{'phase':'mutation','updated_at':now(),'completed':0,'total':len(items),'remaining':len(items),'success':0,'failed':0,'errors':0,'eta':'unknown','pid':os.getpid(),'log':str(out/'RUN.log'),'output_dir':str(out)})
 (out/'LIVE_PROGRESS.md').write_text(f'# RIPPLE 第二轮进度\n\n- 当前阶段：mutation\n- 已完成：0/{len(items)}\n- 主进程 PID：{os.getpid()}\n- 原始日志：`{out}/RUN.log`\n')
 def mutate(item):
  root=Path(item['run_root']); root.mkdir(parents=True); case=Path(item['case_dir']); task=json.loads((case/'task.json').read_text()); repo=prepare_local_worktree(root,Path(item['base_repo']),task['base_commit']); atomic_json(root/'source_repo.json',{'base_repo':item['base_repo'],'private_worktree':str(repo),'base_commit':task['base_commit'],'source_repo_was_modified':False});
  old=json.loads((Path(item['old_run_root'])/'mutation/manifest.json').read_text()); old_ids=[c['cluster_id'] for c in old['clusters']]; action=item['round1_action']; generated=root/'mutation/generated'; retained=[]
  clusters,docs=load_levels_priority(case,['level_1','level_2','level_3']); by_id={c[0]['cluster_id']:c for c in clusters}; rng=random.Random(item['seed'])
  if action=='upgrade_to_R1_R3':
   man=generate(case,repo,generated,'level_1,level_2,level_3',item['seed'],None,enabled_operators=('R1','R2','R3'),selected_cluster_ids=tuple(old_ids))
  else:
   if action=='add_two_clusters': retained=old['clusters']; need=2
   else:
    retained=[c for c in old['clusters'] if c['cluster_id'] not in set(item['unexposed_clusters'])]; need=len(item['unexposed_clusters'])
   old_unit_ids={x['unit_id'] for c in old['clusters'] for x in c['locations']}
   available={level:[cid for cid,c in by_id.items() if cid not in old_ids and c[0]['level']==level and all(x['unit_id'] not in old_unit_ids for x in c)] for level in ('level_1','level_2','level_3')}; chosen=[]
   if action=='add_two_clusters':
    for level in ('level_1','level_2','level_3'):
     rng.shuffle(available[level]); take=min(need-len(chosen),len(available[level])); chosen.extend(available[level][:take])
     if len(chosen)==need: break
   else:
    old_level={c['cluster_id']:(c['locations'][0].get('level') or c['cluster_id'].split(':')[-2]) for c in old['clusters']}
    for replaced in item['unexposed_clusters']:
     start=('level_1','level_2','level_3').index(old_level[replaced]); picked=None
     for level in ('level_1','level_2','level_3')[start:]:
      choices=[cid for cid in available[level] if cid not in chosen]
      if choices: picked=rng.choice(choices); break
     if picked: chosen.append(picked)
   if len(chosen)!=need: raise ValueError(f'cannot select {need} replacement/additional clusters; selected {len(chosen)}')
   new=generate(case,repo,generated,'level_1,level_2,level_3',item['seed'],None,enabled_operators=('R1','R2','R3') if action=='add_two_clusters' else ('L1','L2','L3'),selected_cluster_ids=tuple(chosen))
   # The retained and new sentences can belong to the same complete docstring. Build
   # their final patch together from pristine source so full-document validation is valid.
   subprocess.run(['git','apply','-R',str(generated/'mutation.patch')],cwd=repo,check=True)
   combined_locations=[x for c in retained+new['clusters'] for x in c['locations']]
   apply_mutations(repo,docs,combined_locations)
   man={**new,'selected_cluster_count':len(retained)+len(new['clusters']),'mutation_count':len(combined_locations),'clusters':retained+new['clusters']}
  patch=subprocess.check_output(['git','diff','--binary','--'],cwd=repo,text=True); man['patch_sha256']=hashlib.sha256(patch.encode()).hexdigest(); (root/'mutation').mkdir(exist_ok=True); atomic_text(root/'mutation/mutation.patch',patch); atomic_json(root/'mutation/manifest.json',man); atomic_json(root/'repo_map.json',{item['instance_id']:str(repo)}); atomic_json(root/'round2_decision.json',{'round1_action':action,'old_cluster_ids':old_ids,'final_cluster_ids':[c['cluster_id'] for c in man['clusters']],'enabled_operators':item['enabled_operators']}); return item
 def stage(name,fn,vals):
  ok=[]; errs={}; lock=threading.Lock()
  atomic_json(out/'status.json',{'phase':name,'updated_at':now(),'started_at':json.loads((out/'RUN_CONFIG.json').read_text())['started_at'],'completed':0,'total':len(vals),'remaining':len(vals),'success':0,'failed':0,'errors':0,'eta':'unknown','pid':os.getpid(),'log':str(out/'RUN.log'),'output_dir':str(out)})
  groups={ag:[x for x in vals if x['agent']==ag] for ag in CASE_ROOTS}
  for agent,group in groups.items():
   (out/agent).mkdir(parents=True,exist_ok=True); atomic_json(out/agent/'status.json',{'phase':name,'updated_at':now(),'completed':0,'total':len(group),'remaining':len(group),'success':0,'failed':0,'errors':0,'workers':worker_counts[agent],'output_dir':str(out/agent)}); atomic_text(out/agent/'LIVE_PROGRESS.md',f'# {agent} live progress\n\n- 阶段：`{name}`\n- 完成：0/{len(group)}\n- Worker：{worker_counts[agent]}\n')
  def record(event):
   with lock:
    with (out/'events.jsonl').open('a') as handle: handle.write(json.dumps(event,ensure_ascii=False)+'\n')
    all_events=[json.loads(x) for x in (out/'events.jsonl').read_text().splitlines()]; current=[x for x in all_events if x.get('phase')==name]; done=len(current); failed=sum(x['status']=='failed' for x in current); atomic_json(out/'status.json',{'phase':name,'updated_at':now(),'started_at':json.loads((out/'RUN_CONFIG.json').read_text())['started_at'],'completed':done,'total':len(vals),'remaining':max(0,len(vals)-done),'success':done-failed,'failed':failed,'errors':failed,'eta':'unknown','pid':os.getpid(),'log':str(out/'RUN.log'),'output_dir':str(out)})
    agent=event['agent']; ae=[x for x in current if x['agent']==agent]; af=sum(x['status']=='failed' for x in ae); total=len(groups[agent]); state={'phase':name,'updated_at':now(),'completed':len(ae),'total':total,'remaining':max(0,total-len(ae)),'success':len(ae)-af,'failed':af,'errors':af,'workers':worker_counts[agent],'last_instance_id':event['instance_id'],'output_dir':str(out/agent)}; atomic_json(out/agent/'status.json',state); atomic_text(out/agent/'LIVE_PROGRESS.md',f"# {agent} live progress\n\n- 阶段：`{name}`\n- 完成：{len(ae)}/{total}\n- 成功：{len(ae)-af}\n- 失败：{af}\n- 剩余：{max(0,total-len(ae))}\n- Worker：{worker_counts[agent]}\n- 最近 case：`{event['instance_id']}`\n- 更新时间：`{state['updated_at']}`\n")
  def worker(group):
   good=[]; bad={}
   for item in group:
    try:
     good.append(fn(item)); event={'time':now(),'phase':name,'instance_id':item['instance_id'],'agent':item['agent'],'status':'success'}
    except Exception as e:
     bad[item['instance_id']]=f'{type(e).__name__}: {e}'; (Path(item['run_root'])/f'{name.upper()}_FAILURE.log').write_text(traceback.format_exc()); event={'time':now(),'phase':name,'instance_id':item['instance_id'],'agent':item['agent'],'status':'failed','error':str(e)}
    record(event)
   return good,bad
  chunks=[]
  for agent,group in groups.items():
   count=worker_counts[agent]; chunks.extend([group[index::count] for index in range(count)])
  with cf.ThreadPoolExecutor(max_workers=sum(worker_counts.values())) as ex:
   for good,bad in ex.map(worker,chunks): ok.extend(good); errs.update(bad)
  return ok,errs
 active,errs=stage('mutation',mutate,items)
 if a.stop_after != 'mutation':
  active,e=stage('inference',inference_stage,active); errs.update(e)
 if a.stop_after == 'evaluation':
  active,e=stage('evaluation',evaluation_stage,active); errs.update(e)
 results=[finalize(x,errs.get(x['instance_id'])) for x in items]; atomic_json(out/'BATCH_SUMMARY.json',{'finished_at':now(),'total':len(items),'results':results,'errors':errs}); atomic_json(out/'status.json',{'phase':'completed','updated_at':now(),'completed':len(results),'total':len(items),'success':sum(not r.get('error') for r in results),'failed':sum(bool(r.get('error')) for r in results),'output_dir':str(out)})
if __name__=='__main__': main()
