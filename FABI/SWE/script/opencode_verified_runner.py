#!/usr/bin/env python3
"""Four-way OpenCode SWE-bench Verified local inference runner."""
from __future__ import annotations
import datetime as dt, json, os, shutil, subprocess, sys, time
from pathlib import Path

ROOT=Path('<local-data>/coding_agent/EviFuzz')
OUT=ROOT/'opencode_gpt56_luna'
DATA=Path('<local-data>/coding_agent/swe-bench-verified/dataset/swebench_verified_test.json')
BASE=Path('<local-data>/coding_agent/swe-bench-verified/worktrees')
OPENCODE=ROOT/'opencode_env/run_opencode.sh'
RUN=int(os.environ.get('OPENCODE_RUN','1'))
RUN_OUT=OUT/f'run_{RUN}'
WORKERS=int(os.environ.get('OPENCODE_WORKERS','4'))
MAX_ATTEMPTS=int(os.environ.get('OPENCODE_MAX_ATTEMPTS','3'))
PODMAN_SOCKET=Path(os.environ.get('PODMAN_SOCKET','/tmp/swebench-podman.sock'))

def now(): return dt.datetime.now().astimezone().isoformat(timespec='seconds')
def records(): return {x['instance_id']:x for x in json.loads(DATA.read_text())}
def ids(): return list(records())
def source(iid):
    m=list(BASE.glob(f'full-shard*/{iid}'))
    if len(m)!=1: raise RuntimeError(f'source repo not unique: {iid} {m}')
    return m[0]
def official_image(iid):
    return f"docker.io/swebench/sweb.eval.x86_64.{iid.lower().replace('__','_1776_')}:latest"
def prepare_repo(dst, iid, commit):
    """Extract the same official image repository used by SWE-bench eval."""
    env=os.environ.copy(); env['DOCKER_HOST']=f'unix://{PODMAN_SOCKET}'
    image=official_image(iid)
    if subprocess.run(['podman','image','exists',image],env=env).returncode != 0:
        subprocess.run(['podman','--storage-opt','ignore_chown_errors=true','pull',image],env=env,check=True,timeout=3600,
                       stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    cid=subprocess.check_output(['podman','create','--network=none',image,'true'],env=env,text=True).strip()
    try:
        subprocess.run(['podman','cp',f'{cid}:/testbed/.',str(dst)],env=env,check=True,timeout=600,
                       stdout=subprocess.DEVNULL)
    finally:
        subprocess.run(['podman','rm','-f',cid],env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    subprocess.run(['git','restore','.'],cwd=dst,check=True)
    subprocess.run(['git','reset','--hard','HEAD'],cwd=dst,check=True,stdout=subprocess.DEVNULL)
    subprocess.run(['git','cat-file','-e',f'{commit}^{{commit}}'],cwd=dst,check=True,timeout=120)
    subprocess.run(['git','checkout','--detach','-q',commit],cwd=dst,check=True,timeout=120)
    subprocess.run(['git','clean','-fd'],cwd=dst,check=True,stdout=subprocess.DEVNULL)
def case_dir(iid,a): return RUN_OUT/'cases'/iid/f'attempt_{a:02d}'
def valid(p): return (p/'prediction.json').exists() and (p/'validation.json').exists() and (p/'prediction.json').read_text().strip()!=''
def update(phase,done,failed=0,current='',started=None):
    total=len(ids()); rem=total-done-failed
    state={'updated_at':now(),'phase':phase,'run':RUN,'started_at':started or now(),'completed':done+failed,'total':total,'remaining':rem,'success':done,'failed':failed,'current':current,'log':str(RUN_OUT/'logs'/f'opencode_run_{RUN}.log')}
    OUT.mkdir(parents=True,exist_ok=True); RUN_OUT.mkdir(exist_ok=True)
    tmp=RUN_OUT/'status.json.tmp'; tmp.write_text(json.dumps(state,indent=2,ensure_ascii=False)+'\n'); tmp.replace(RUN_OUT/'status.json')
    (RUN_OUT/'LIVE_PROGRESS.md').write_text(f'# OpenCode gpt-5.6-luna Verified run_{RUN} 实时进度\n\n'+''.join(f'- {k}: `{v}`\n' for k,v in state.items()))
def worker(w,subset,started):
    recs=records(); logdir=RUN_OUT/'logs'; logdir.mkdir(parents=True,exist_ok=True)
    with (logdir/f'worker_{w}.log').open('a') as log:
      for iid in subset:
        if any(valid(p) for p in sorted((RUN_OUT/'cases'/iid).glob('attempt_*'),reverse=True)) if (RUN_OUT/'cases'/iid).exists() else False: continue
        ok=False
        for a in range(1,MAX_ATTEMPTS+1):
          p=case_dir(iid,a); repo=p/'repo'; p.mkdir(parents=True,exist_ok=True)
          try:
            prepare_repo(repo, iid, recs[iid]['base_commit'])
            prompt='''Solve this SWE-bench issue. Work directly in the repository, inspect the code and tests, implement the smallest correct fix, and run focused tests if possible. Do not just explain; modify files and leave the final patch in the working tree.\n\nProblem statement:\n'''+recs[iid]['problem_statement']
            out=p/'opencode.log'
            with out.open('w') as fh:
              rc=subprocess.run([str(OPENCODE),'run','--model','openai/gpt-5.6-luna','--variant','medium','--auto',prompt],cwd=repo,stdout=fh,stderr=subprocess.STDOUT,timeout=3600).returncode
            patch_text=subprocess.check_output(['git','diff','--binary'],cwd=repo,text=True)
            (p/'prediction.json').write_text(json.dumps({'instance_id':iid,'model_patch':patch_text},ensure_ascii=False)+'\n')
            (p/'validation.json').write_text(json.dumps({'valid':bool(patch_text.strip()),'returncode':rc,'attempt':a,'model':'openai/gpt-5.6-luna','variant':'medium'},indent=2)+'\n')
            ok=bool(patch_text.strip()); log.write(f'{now()} {iid} attempt={a} valid={ok}\n'); log.flush()
            if ok: break
          except Exception as e:
            (p/'validation.json').write_text(json.dumps({'valid':False,'error':repr(e),'attempt':a},indent=2)+'\n'); log.write(f'{now()} {iid} error={e!r}\n'); log.flush()
        if not ok: log.write(f'{now()} {iid} failed_after_attempts\n'); log.flush()
def main():
    started=now(); allids=ids(); chunks=[allids[i::WORKERS] for i in range(WORKERS)]
    OUT.mkdir(parents=True,exist_ok=True); (RUN_OUT/'logs').mkdir(parents=True,exist_ok=True)
    update('inference',0,started=started)
    ps=[]
    for w,c in enumerate(chunks,1):
      p=subprocess.Popen([sys.executable,__file__,'worker',str(w),','.join(c),started]); ps.append(p)
    while any(p.poll() is None for p in ps):
      done=failed=0
      for iid in allids:
        aps=sorted((RUN_OUT/'cases'/iid).glob('attempt_*'),reverse=True) if (RUN_OUT/'cases'/iid).exists() else []
        if any(valid(p) for p in aps): done += 1
        elif aps and (aps[0]/'validation.json').exists() and json.loads((aps[0]/'validation.json').read_text()).get('attempt',0)>=MAX_ATTEMPTS: failed += 1
      update('inference',done,failed,started=started); time.sleep(30)
    update('inference_complete',done,failed,started=started)
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='worker': worker(int(sys.argv[2]),sys.argv[3].split(','),sys.argv[4]); raise SystemExit
    main()
