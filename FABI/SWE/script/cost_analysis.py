#!/usr/bin/env python3
"""Extract comparable metrics from archived clean runs.

``read_loc`` deliberately comes from the raw execution traces, rather than
placement's filtered function list: it is the number of unique repository
files that the agent actually named in a command or command output.  The
parser also records the complete file list and event count for auditability.
"""
from pathlib import Path
import json, re, statistics, math, csv

ROOT=Path('<local-data>/coding_agent/EviFuzz/original_passed_cases'); OUT=ROOT/'cost_analysis'
AGENTS={'SWE-Agent':ROOT/'SWE-Agent/gpt54mini_lite','Codex':ROOT/'Codex/gpt54mini_lite','OpenCode':ROOT/'OpenCode/gpt54mini_lite'}

def patch_lines(run):
    files=list(run.rglob('*.patch'))
    if not files: files=list(run.glob('prediction.json'))
    text=''
    if files:
        try:
            d=json.loads(files[0].read_text()); text=d.get('model_patch','') or ''
        except: text=files[0].read_text(errors='replace')
    add=delete=0
    for l in text.splitlines():
        if l.startswith('+++') or l.startswith('---') or l.startswith('@@'): continue
        add += l.startswith('+'); delete += l.startswith('-')
    return add+delete

_PATH_RE = re.compile(r"(?<![A-Za-z0-9_.-])(?:/testbed/|/workspace/|/repo/|(?:\./)?)([A-Za-z0-9_.][A-Za-z0-9_./-]*\.(?:py|pyi|js|ts|tsx|jsx|java|c|h|cpp|cc|cxx|rs|go|rb|php|md|rst|yaml|yml|toml|ini|cfg|json|txt))(?![A-Za-z0-9_./-])")
def trace_read_locations(run):
    """Return (unique repository-relative files, number of access events).

    We inspect only action/command and observation/output fields in persisted
    traces.  This avoids counting the task prompt while still capturing cat,
    sed, grep/rg/find output, git diff, and tool output paths.  Repeated reads
    are retained in ``events`` but counted once by the primary ``read_loc``.
    """
    texts=[]
    traj=next(run.rglob('*.traj'),None)
    if traj:
        try:
            d=json.loads(traj.read_text())
            for t in d.get('trajectory',[]):
                for k in ('action','observation'):
                    if isinstance(t.get(k),str): texts.append(t[k])
        except Exception: pass
    for fn in ('codex.jsonl','opencode.jsonl'):
        p=run/fn
        if not p.exists(): continue
        for line in p.read_text(errors='replace').splitlines():
            try: d=json.loads(line)
            except Exception: continue
            if not isinstance(d,dict): continue
            it=d.get('item',d)
            if not isinstance(it,dict): continue
            for k in ('command','aggregated_output','output'):
                if isinstance(it.get(k),str): texts.append(it[k])
            part=d.get('part')
            if isinstance(part,dict):
                for k in ('command','output'):
                    if isinstance(part.get(k),str): texts.append(part[k])
                st=part.get('state')
                if isinstance(st,dict):
                    for k in ('input','output'):
                        if isinstance(st.get(k),str): texts.append(st[k])
    files=[]; events=0
    for txt in texts:
        for m in _PATH_RE.finditer(txt):
            raw=m.group(0)
            # Strip conventional shell punctuation and normalize known roots.
            raw=raw.rstrip(',:;)]}')
            rel=raw.split('/testbed/',1)[-1] if '/testbed/' in raw else raw.split('/workspace/',1)[-1] if '/workspace/' in raw else raw.split('/repo/',1)[-1] if '/repo/' in raw else raw.lstrip('./')
            if rel and rel not in files:
                files.append(rel)
            events += 1
    return files, events

def metrics(agent, run):
    m={'tokens':None,'input_tokens':None,'cached_input_tokens':None,'cache_write_input_tokens':None,
       'output_tokens':None,'reasoning_output_tokens':None,'cost':None,'rounds':None,
       'read_loc':None,'read_event_count':0,'read_files':[],'edit_lines':patch_lines(run),'source':[]}
    p=next(run.glob('metrics.json'),None)
    if p:
        d=json.loads(p.read_text()); m.update(tokens=d.get('input_tokens',0)+d.get('output_tokens',0),input_tokens=d.get('input_tokens'),output_tokens=d.get('output_tokens'),cost=d.get('reported_cost'),rounds=d.get('api_calls')); m['source']+=['metrics.json']
    traj=next(run.rglob('*.traj'),None)
    if traj:
        d=json.loads(traj.read_text()); s=d.get('info',{}).get('model_stats',{}); m.update(tokens=s.get('tokens_sent',0)+s.get('tokens_received',0),input_tokens=s.get('tokens_sent'),output_tokens=s.get('tokens_received'),cost=s.get('instance_cost'),rounds=s.get('api_calls')); m['source']+=['trajectory.model_stats']
    ev=next((run/f'{agent.lower()}.jsonl' for _ in [0] if (run/f'{agent.lower()}.jsonl').exists()),None)
    if not ev: ev=next((run/x for x in ('codex.jsonl','opencode.jsonl') if (run/x).exists()),None)
    if ev:
        total=cost=0; rounds=0; codex_actions=0; inp=cache=write=out=reason=0
        for line in ev.read_text(errors='replace').splitlines():
            try: d=json.loads(line)
            except: continue
            if not isinstance(d, dict): continue
            it=d.get('item') if isinstance(d.get('item'),dict) else {}
            if it.get('type') in ('command_execution','file_change'):
                codex_actions += 1
            part=d.get('part',{}); part = part if isinstance(part,dict) else {}; tok=part.get('tokens') or {}
            usage=d.get('usage') or {}
            if d.get('type')=='turn.completed' and usage:
                inp += int(usage.get('input_tokens',0) or 0); cache += int(usage.get('cached_input_tokens',0) or 0); write += int(usage.get('cache_write_input_tokens',0) or 0); out += int(usage.get('output_tokens',0) or 0); reason += int(usage.get('reasoning_output_tokens',0) or 0)
            if d.get('type')=='step_finish': rounds+=1
            # OpenCode emits cumulative token totals per step, whereas cost is
            # incremental; retain the last/largest total and sum step costs.
            total = max(total, int(tok.get('total',0) or 0)); cost += float(part.get('cost',0) or 0)
        if rounds: m['rounds']=rounds
        elif agent == 'Codex' and codex_actions: m['rounds']=codex_actions
        if total: m['tokens']=total
        if inp or out: m.update(input_tokens=inp, cached_input_tokens=cache, cache_write_input_tokens=write, output_tokens=out, reasoning_output_tokens=reason, tokens=inp+out)
        if cost: m['cost']=cost
        m['source']+= [ev.name]
    rf,revents=trace_read_locations(run); m.update(read_files=rf,read_event_count=revents,read_loc=len(rf)); m['source']+=['trace_commands_and_outputs_v2']
    return m

def fmt(v,flag=False):
    if v is None:return 'N/A'
    s=str(round(v,6) if isinstance(v,float) else v)
    return f'<span style="color:red">{s}</span>' if flag else s

def main():
 OUT.mkdir(parents=True,exist_ok=True); case_studies=[]
 for name,base in AGENTS.items():
  cases=sorted(p for p in (base/'cases').iterdir() if p.is_dir()); rows=[]; allvals=[]
  for c in cases:
   vals={}; runs=[]
   for i in range(1,5):
    r=c/f'run_{i}'; x=metrics(name,r) if r.exists() else {'tokens':None,'cost':None,'rounds':None,'read_loc':None,'edit_lines':None}; vals[i]=x; runs.append(x)
   allvals.append((c.name,runs)); rows.append((c.name,runs))
  headers=['instance_id']+[f'run_{i}_{k}' for i in range(1,5) for k in ('cost','tokens','rounds','read_loc','edit_lines')]
  lines=['# '+name+' four-run cost and trajectory metrics','', 'Values are per case/run. Red marks a within-case outlier (>=3x the nonzero minimum or <= one-third of the nonzero maximum) for that metric. `N/A` means the artifact did not persist that metric.','', '| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
  for iid,rs in rows:
   flags=[]
   for k in ('cost','tokens','rounds','read_loc','edit_lines'):
    nums=[x[k] for x in rs if isinstance(x[k],(int,float)) and x[k] is not None]
    lo=min(nums) if nums else 0; hi=max(nums) if nums else 0; flags.append((k,lo,hi))
   cells=[iid]
   for x in rs:
    for k,lo,hi in flags:
     v=x[k]; out=bool(v is not None and hi>0 and lo>0 and (v>=3*lo or v*3<=hi))
     cells.append(fmt(v,out))
   lines.append('| '+' | '.join(cells)+' |')
   # case study if at least 3 metrics have >=3x spread
   spreads=sum(hi>=3*lo and lo>0 for _,lo,hi in flags)
   if spreads>=3: case_studies.append({'agent':name,'instance_id':iid,'metrics':{k:[x[k] for x in rs] for k in ('cost','tokens','rounds','read_loc','edit_lines')}})
  (OUT/f'{name.replace("-","_")}.md').write_text('\n'.join(lines)+'\n')
  # Machine-readable spreadsheet-compatible table.  One row is one case and
  # each run contributes the five requested metrics.  Empty cells represent
  # genuinely missing persisted values (never silently converted to zero).
  with (OUT/f'{name.replace("-","_")}.csv').open('w', newline='') as f:
   w=csv.writer(f)
   w.writerow(headers)
   for iid,rs in rows:
    row=[iid]
    for x in rs:
     for k in ('cost','tokens','rounds','read_loc','edit_lines'):
      row.append('' if x[k] is None else x[k])
    w.writerow(row)
  # JSON retains the full per-run audit (including read_files), while the
  # Markdown table is intentionally compact for visual inspection.
  summary={'agent':name,'cases':len(rows),'case_studies':sum(x['agent']==name for x in case_studies),
           'read_loc_definition':'unique repository-relative files named in raw trace commands/outputs',
           'rows':[{'instance_id':iid,'runs':rs} for iid,rs in rows]}
  (OUT/f'{name.replace("-","_")}.json').write_text(json.dumps(summary,indent=2)+'\n')
 (OUT/'case_studies.json').write_text(json.dumps(case_studies,ensure_ascii=False,indent=2)+'\n')
 # Cross-agent overview: preserve per-run distributions and missingness.
 overview=[]
 for name,base in AGENTS.items():
  for i in range(1,5):
   vals=[metrics(name,c/f'run_{i}') for c in sorted((base/'cases').iterdir()) if (c/f'run_{i}').exists()]
   row={'agent':name,'run':i,'cases':len(vals)}
   for k in ('cost','tokens','rounds','read_loc','edit_lines'):
    a=[v[k] for v in vals if isinstance(v[k],(int,float)) and v[k] is not None]
    row[k]={'count':len(a),'mean':statistics.mean(a) if a else None,'median':statistics.median(a) if a else None,'min':min(a) if a else None,'max':max(a) if a else None}
   overview.append(row)
 (OUT/'ALL_AGENTS_SUMMARY.json').write_text(json.dumps(overview,ensure_ascii=False,indent=2)+'\n')
 lines=['# All-agent four-run metric summary','', '| agent | run | cases | cost mean/median | tokens mean/median | rounds mean/median | read_loc mean/median | edit lines mean/median |','|---|---:|---:|---:|---:|---:|---:|---:|']
 for r in overview:
  def pair(k):
   x=r[k]; return 'N/A' if x['count']==0 else f"{x['mean']:.2f} / {x['median']:.2f}"
  lines.append(f"| {r['agent']} | {r['run']} | {r['cases']} | {pair('cost')} | {pair('tokens')} | {pair('rounds')} | {pair('read_loc')} | {pair('edit_lines')} |")
 (OUT/'ALL_AGENTS_SUMMARY.md').write_text('\n'.join(lines)+'\n')
 # Fourth table: cross-agent/run distribution summary.
 with (OUT/'ALL_AGENTS_SUMMARY.csv').open('w', newline='') as f:
  w=csv.writer(f)
  w.writerow(['agent','run','cases','cost_count','cost_mean','cost_median','cost_min','cost_max',
              'tokens_count','tokens_mean','tokens_median','tokens_min','tokens_max',
              'rounds_count','rounds_mean','rounds_median','rounds_min','rounds_max',
              'read_loc_count','read_loc_mean','read_loc_median','read_loc_min','read_loc_max',
              'edit_lines_count','edit_lines_mean','edit_lines_median','edit_lines_min','edit_lines_max'])
  for r in overview:
   row=[r['agent'],r['run'],r['cases']]
   for k in ('cost','tokens','rounds','read_loc','edit_lines'):
    x=r[k]; row += [x['count'],x['mean'],x['median'],x['min'],x['max']]
   w.writerow(row)
 md=['# Four-run cross-run case studies','',f'Cases with >=3 metrics showing a >=3x within-case spread: **{len(case_studies)}**.']
 for x in case_studies: md += ['',f"## {x['agent']} — `{x['instance_id']}`",'', '| metric | run1 | run2 | run3 | run4 |','|---|---:|---:|---:|---:|']+[f"| {k} | "+' | '.join('N/A' if v is None else str(v) for v in vs)+' |' for k,vs in x['metrics'].items()]
 (OUT/'CASE_STUDIES.md').write_text('\n'.join(md)+'\n')
 print(json.dumps({'output':str(OUT),'case_studies':len(case_studies)}))
if __name__=='__main__': main()
