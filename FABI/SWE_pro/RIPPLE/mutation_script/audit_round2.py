#!/usr/bin/env python3
"""Audit relational-round inference artifacts without changing experiment data."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

DIFF_FILE_RE = re.compile(r"^diff --git a/(.+?) b/(.+?)$", re.M)
ISO_RE = re.compile(r"(instance_[^ ]+?) ERROR .*cannot isolate agent patch")

def sha(text): return hashlib.sha256(text.encode()).hexdigest()
def files_from_patch(text):
    return sorted({x for pair in DIFF_FILE_RE.findall(text) for x in pair})
def load(path):
    try: return json.loads(path.read_text())
    except Exception: return {}

def audit_agent(root, agent):
    base, cases = root/agent, {}
    manifests = list(base.glob('workers/worker_*/cases/*/mutation_applied.json'))
    manifests += list(base.glob('cases/*/run_1/mutation_applied.json'))
    for p in manifests:
        instance, d = (p.parent.parent.name if p.parent.name == 'run_1' else p.parent.name), load(p)
        if d.get('applied') and instance not in cases:
            pp = Path(d.get('patch',''))
            text = pp.read_text(errors='replace') if pp.exists() else ''
            cases[instance] = {'instance_id':instance, 'mutation_files':sorted(d.get('files',[])), 'mutation_sha256':d.get('sha256') or sha(text)}
    for p in base.glob('cases/*/run_1/prediction.json'):
        instance, d = p.parent.parent.name, load(p)
        c = cases.setdefault(instance, {'instance_id':instance, 'mutation_files':[], 'mutation_sha256':None})
        patch = d.get('model_patch') or ''
        c.update(final_patch_sha256=sha(patch), final_patch_bytes=len(patch.encode()), final_files=files_from_patch(patch), final_patch_empty=not bool(patch.strip()))
        c['final_equals_mutation'] = bool(c['mutation_sha256'] and sha(patch)==c['mutation_sha256'])
        val = load(p.parent/'validation.json'); c.update(validation_valid=val.get('valid'), validation_empty_patch=val.get('empty_patch'), returncode=val.get('returncode'))
        out = load(p.parent.parent/'outcome.json'); run=(out.get('runs') or {}).get('run_1') or {}; c['resolved']=run.get('official_resolved')
        mf, ff = set(c['mutation_files']), set(c['final_files']); c['mutation_only']=bool(ff) and ff <= mf; c['agent_extra_files']=sorted(ff-mf)
    for log in base.glob('logs/worker_*.log'):
        for line in log.read_text(errors='replace').splitlines():
            m=ISO_RE.search(line)
            if m:
                inst=m.group(1); cases.setdefault(inst, {'instance_id':inst, 'mutation_files':[]})['isolation_error']=True
    for c in cases.values(): c.setdefault('isolation_error',False)
    for p in base.glob('workers/worker_*/cases/*/opencode.jsonl'):
        c=cases.get(p.parent.name)
        if not c: continue
        reasons=[]
        for line in p.read_text(errors='replace').splitlines():
            try:
                o=json.loads(line)
                if o.get('type')=='step_finish': reasons.append((o.get('part') or {}).get('reason'))
            except Exception: pass
        c['last_step_reason']=reasons[-1] if reasons else None; c['step_count']=len(reasons)
    vals=list(cases.values())
    return {'agent':agent,'cases':len(vals),'isolation_cases':sum(x.get('isolation_error',False) for x in vals),'mutation_only_cases':sum(x.get('mutation_only',False) for x in vals),'final_equals_mutation_cases':sum(x.get('final_equals_mutation',False) for x in vals),'empty_final_patch_cases':sum(x.get('final_patch_empty',False) for x in vals),'validation_invalid_cases':sum(x.get('validation_valid') is False for x in vals),'returncode_nonzero_cases':sum(x.get('returncode') not in (None,0) for x in vals),'resolved_mutation_only':sum(x.get('mutation_only',False) and x.get('resolved') is True for x in vals),'unresolved_mutation_only':sum(x.get('mutation_only',False) and x.get('resolved') is not True for x in vals),'cases_detail':sorted(vals,key=lambda x:x['instance_id'])}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('run',type=Path); ap.add_argument('--out',type=Path); a=ap.parse_args()
    result={x:audit_agent(a.run,x) for x in ('swe-agent','opencode','codex')}
    for agent, data in result.items():
        resolved = set(load(a.run/agent/'evaluation_result.json').get('resolved_ids', []))
        for case in data['cases_detail']:
            case['resolved'] = case['instance_id'] in resolved
        data['resolved_mutation_only'] = sum(x.get('mutation_only', False) and x['resolved'] for x in data['cases_detail'])
        data['unresolved_mutation_only'] = sum(x.get('mutation_only', False) and not x['resolved'] for x in data['cases_detail'])
    out=a.out or a.run/'ROUND2_PATCH_AUDIT.json'; out.write_text(json.dumps(result,indent=2,sort_keys=True))
    md=out.with_suffix('.md'); lines=['# Round 2 patch audit','',f'Run: `{a.run}`','', '| agent | cases | isolation | mutation-only | final=mutation | empty final | invalid validation |','|---|---:|---:|---:|---:|---:|---:|']
    for ag,d in result.items(): lines.append(f"| {ag} | {d['cases']} | {d['isolation_cases']} | {d['mutation_only_cases']} | {d['final_equals_mutation_cases']} | {d['empty_final_patch_cases']} | {d['validation_invalid_cases']} |")
    lines += ['', '`mutation-only` is a suspicion signal: every final patch file is in the mutation file set.','']
    for ag,d in result.items():
        ss=[x for x in d['cases_detail'] if x.get('mutation_only') or x.get('isolation_error') or x.get('final_patch_empty')]; lines += [f'## {ag} suspicious cases ({len(ss)})','']
        lines += [f"- `{x['instance_id']}`: isolation={x.get('isolation_error')}, mutation_only={x.get('mutation_only')}, resolved={x.get('resolved')}, final_files={len(x.get('final_files',[]))}, extra={x.get('agent_extra_files',[])}" for x in ss]+['']
    md.write_text('\n'.join(lines)); print(json.dumps({ag:{k:v for k,v in d.items() if k!='cases_detail'} for ag,d in result.items()},indent=2))
if __name__=='__main__': main()
