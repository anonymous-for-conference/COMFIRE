#!/usr/bin/env python3
"""Extract reproducible per-case cost/read/edit metrics for Ripple runs."""
import csv,json,re,os,glob,argparse
from pathlib import Path

def jload(p):
    try:
        with open(p,encoding='utf-8') as f:return json.load(f)
    except Exception:return None

def patch_lines(root):
    cands=list(Path(root).glob('interface/evaluation_compose/combined.patch'))+list(Path(root).glob('interface/evaluation_compose/agent.patch'))
    for p in cands:
        try:
            add=dele=0
            for l in p.read_text(errors='ignore').splitlines():
                if l.startswith('+++') or l.startswith('---'):continue
                if l.startswith('+'):add+=1
                elif l.startswith('-'):dele+=1
            return add+dele
        except OSError: pass
    return None

def files_in_text(s):
    if not isinstance(s,str): return set()
    out=set()
    # paths appearing in shell commands, git output, and common tool output
    for x in re.findall(r'(?<![\w.-])([\w@.+-]+(?:/[\w@.+-]+)+\.(?:py|js|ts|java|go|rs|md|rst|yaml|yml|json|toml|c|h|cpp))',s):
        if not x.startswith(('/', 'http')): out.add(x)
    for x in re.findall(r'(?:^|\s)([A-Za-z0-9_.-]+\.(?:py|js|ts|java|go|rs|md|rst|yaml|yml|json|toml|c|h|cpp))(?=[:\s])',s):out.add(x)
    return out

def metrics(root,agent):
    if not root or not Path(root).exists():
        return dict(input_tokens=None,output_tokens=None,total_tokens=None,cost=None,rounds=None,read_loc=None,edit_lines=None)
    inp=out=cost=rounds=None; reads=set()
    if agent=='sweagent':
        # SWE trajectories are nested below attempt_*/agent/<instance>/<instance>.traj.
        tr=next(iter(Path(root).glob('interface/**/*.traj')),None)
        data=jload(tr) if tr else None
        traj = data.get('trajectory',[]) if isinstance(data,dict) else data
        if isinstance(traj,list):
            for e in traj:
                if isinstance(e,dict):
                    for k in ('action','observation','thought'): reads |= files_in_text(json.dumps(e.get(k,''),ensure_ascii=False))
                    # Actions often start with /testbed; normalize and retain repository-relative paths.
                    for k in ('action','observation'):
                        val=e.get(k,''); val=val if isinstance(val,str) else json.dumps(val,ensure_ascii=False)
                        for mm in re.finditer(r'/testbed/([^\s:\'"`]+)',val): reads.add(mm.group(1).rstrip('.,)'))
                    st=e.get('info',{}).get('model_stats',{}) if isinstance(e.get('info'),dict) else {}
                    if st:
                        inp=st.get('tokens_sent',inp);out=st.get('tokens_received',out);cost=st.get('instance_cost',cost);rounds=st.get('api_calls',rounds)
        m=next(iter(Path(root).glob('interface/**/metrics.json')),None)
        md=jload(m) if m else None
        if md:
            inp=inp if inp is not None else md.get('input_tokens');out=out if out is not None else md.get('output_tokens');cost=cost if cost is not None else md.get('reported_cost');rounds=rounds if rounds is not None else md.get('api_calls')
    elif agent=='codex':
        logs=list(Path(root).glob('interface/cases/*/attempt_*/codex.jsonl'))
        cmdn=filen=0
        for lp in logs:
            for line in lp.read_text(errors='ignore').splitlines():
                try:e=json.loads(line)
                except:continue
                s=json.dumps(e,ensure_ascii=False); reads |= files_in_text(s)
                if e.get('type')=='turn.completed' and isinstance(e.get('usage'),dict):
                    u=e['usage']; inp=(inp or 0)+u.get('input_tokens',0);out=(out or 0)+u.get('output_tokens',0)
                if e.get('type')=='item.completed':
                    it=e.get('item',{}); typ=it.get('type','') if isinstance(it,dict) else ''
                    cmdn += typ=='command_execution'; filen += typ=='file_change'
        rounds=cmdn+filen
    else:
        for lp in Path(root).glob('interface/cases/*/attempt_*/opencode.jsonl'):
            mx=0; n=0; c=0
            for line in lp.read_text(errors='ignore').splitlines():
                try:e=json.loads(line)
                except:continue
                reads |= files_in_text(json.dumps(e,ensure_ascii=False))
                if e.get('type') in ('step_finish','step_finished'):
                    n+=1; part=e.get('part',e); tok=part.get('tokens',{}) if isinstance(part,dict) else {}; tt=tok.get('total',0) or 0
                    if tt>=mx: mx=tt; inp=tok.get('input'); out=tok.get('output')
                    c+=part.get('cost',0) or 0
            # total is cumulative maximum; input/output are the corresponding final cumulative fields.
            cost=c; rounds=n; total_override=mx
    total=locals().get('total_override') if agent=='opencode' else ((inp or 0)+(out or 0) if inp is not None or out is not None else None)
    # A zero-only record means the underlying trace was absent/incomplete, not zero work.
    if total == 0 and inp == 0 and out == 0:
        inp=out=total=None
    if agent in ('codex','opencode') and (('logs' not in locals() or not logs) if agent=='codex' else ('lp' not in locals())):
        rounds=read_loc=None
    return dict(input_tokens=inp,output_tokens=out,total_tokens=total,cost=cost,rounds=rounds,read_loc=len(reads),edit_lines=patch_lines(root))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',required=True);ap.add_argument('--out',required=True);ap.add_argument('--first-root');a=ap.parse_args(); root=Path(a.root); out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    rows=[]; first=Path(a.first_root) if a.first_root else None
    for agent in ('sweagent','opencode','codex'):
      sm=jload(root/agent/'BATCH_SUMMARY.json') or {}; sr={x.get('instance_id'):x for x in sm.get('results',[])}
      fsm=jload(first/agent/'BATCH_SUMMARY.json') if first else None
      fsr={x.get('instance_id'):x for x in (fsm or {}).get('results',[])}
      for x in sm.get('results',[]):
        rr=x.get('run_root'); rr=Path(rr) if rr and Path(rr).exists() else root/agent/'runs'/f"{x['instance_id']}"
        m=metrics(rr,agent); rows.append({'agent':agent,'case':x.get('instance_id'),'status':('resolved' if x.get('resolved') else ('infrastructure' if x.get('error') else 'failed')),**m,'run':'round2'})
        if first:
          # Locate archived first-round run by instance id; summaries may contain stale absolute paths.
          hits=[p for p in (first/agent/'runs').iterdir() if x['instance_id'] in p.name] if (first/agent/'runs').exists() else []
          fr=hits[0] if hits else None
          fm=metrics(fr,agent) if fr else {k:None for k in ('input_tokens','output_tokens','total_tokens','cost','rounds','read_loc','edit_lines')}
          fx=fsr.get(x['instance_id'])
          # Round 1 status must come from the round-1 summary, never from round 2.
          rows.append({'agent':agent,'case':x.get('instance_id'),'status':(('resolved' if fx.get('resolved') else ('infrastructure' if fx.get('error') else 'failed')) if fx else 'N/A'),**fm,'run':'round1'})
      # Preserve round-1-only cases (typically round-1 failures that were not rerun).
      if first:
       present={r['case'] for r in rows if r['agent']==agent and r['run']=='round1'}
       for cid,fx in fsr.items():
        if cid in present: continue
        hits=[p for p in (first/agent/'runs').iterdir() if cid in p.name] if (first/agent/'runs').exists() else []
        fr=hits[0] if hits else None; fm=metrics(fr,agent) if fr else {k:None for k in ('input_tokens','output_tokens','total_tokens','cost','rounds','read_loc','edit_lines')}
        rows.append({'agent':agent,'case':cid,'status':'resolved' if fx.get('resolved') else ('infrastructure' if fx.get('error') else 'failed'),**fm,'run':'round1'})
    fields=['case','status','input_tokens','output_tokens','total_tokens','cost','rounds','read_loc','edit_lines']
    for ag in ('sweagent','opencode','codex'):
      agrows=[r for r in rows if r['agent']==ag]; cases=sorted(set(r['case'] for r in agrows)); cols=['case','status_round1','status_round2']
      mets=['input_tokens','output_tokens','total_tokens','cost','rounds','read_loc','edit_lines']
      cols += [f'{run}_{m}' for run in ('round1','round2') for m in mets]
      with open(out/f'{ag}.csv','w',newline='',encoding='utf-8') as f:
       w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
       for case in cases:
        z={'case':case};
        for run in ('round1','round2'):
         q=next((r for r in agrows if r['case']==case and r['run']==run),None);z[f'status_{run}']=q['status'] if q else 'N/A'
         for m in mets:z[f'{run}_{m}']=q[m] if q else 'N/A'
        w.writerow(z)
    with open(out/'failure_costs_round2.csv','w',newline='',encoding='utf-8') as f:
      w=csv.DictWriter(f,fieldnames=['agent']+fields);w.writeheader();w.writerows([dict(agent=r['agent'],**{k:r[k] for k in fields}) for r in rows if r['status']=='failed'])
    # Two-round combined detail tables. A row identifies both case and run.
    for name, predicate in [('failed', lambda r:r['status']=='failed'),('resolved',lambda r:r['status']=='resolved')]:
      td=out/name; td.mkdir(exist_ok=True)
      with open(td/'all_agents.csv','w',newline='',encoding='utf-8') as f:
       w=csv.DictWriter(f,fieldnames=['agent','run']+fields);w.writeheader()
       w.writerows(dict(agent=r['agent'],run=r['run'],**{k:r[k] for k in fields}) for r in rows if predicate(r))
    # Aggregate resolved/failed statistics for each run and agent.
    with open(out/'status_aggregate.csv','w',newline='',encoding='utf-8') as f:
      ms=['input_tokens','output_tokens','total_tokens','cost','rounds','read_loc','edit_lines']; cols=['agent','run','status','cases']+sum(([m+'_sum',m+'_mean'] for m in ms),[])
      w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
      for ag in ('sweagent','opencode','codex'):
       for run in ('round1','round2'):
        for st in ('resolved','failed'):
         qs=[r for r in rows if r['agent']==ag and r['run']==run and r['status']==st]; z={'agent':ag,'run':run,'status':st,'cases':len(qs)}
         for m in ms:
          vals=[r[m] for r in qs if isinstance(r[m],(int,float))]; z[m+'_sum']=sum(vals) if vals else 'N/A';z[m+'_mean']=round(sum(vals)/len(vals),2) if vals else 'N/A'
         w.writerow(z)
    (out/'README.md').write_text('指标按用户给定口径提取。第一轮原始 run_root 已被清理/迁移时，无法恢复的字段标为 N/A；round2 使用当前归档轨迹。\n',encoding='utf-8')
if __name__=='__main__':main()
