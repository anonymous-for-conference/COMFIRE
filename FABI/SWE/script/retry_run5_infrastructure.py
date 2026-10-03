#!/usr/bin/env python3
"""Retry one known SWE-bench infrastructure-error instance in isolation.

The original run and its summary are never modified.  A dedicated podman
socket, run id, report directory, log, and progress file make this safe to
run beside clean-run-6.
"""
from pathlib import Path
import argparse, json, os, subprocess, time, datetime

ROOT=Path('<local-data>/coding_agent/EviFuzz')
EVAL=Path('<local-data>/coding_agent/SWE-bench-eval')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--agent',required=True)
    ap.add_argument('--instance',required=True); ap.add_argument('--source',required=True)
    ap.add_argument('--model-name',required=True); ap.add_argument('--socket',required=True)
    ns=ap.parse_args()
    out=ROOT/({'sweagent':'sweagent_gpt54_mini_run5','codex':'codex_gpt54_mini_run5'}[ns.agent])/f'infrastructure_retry_{ns.instance}'
    out.mkdir(parents=True,exist_ok=True); report=out/'evaluation_summary'; report.mkdir(exist_ok=True)
    pred=out/'predictions.jsonl'
    src=Path(ns.source)
    rows=[json.loads(x) for x in src.read_text().splitlines() if x.strip()]
    rows=[x for x in rows if x.get('instance_id')==ns.instance]
    if len(rows)!=1: raise SystemExit(f'expected one prediction, found {len(rows)}')
    pred.write_text(json.dumps(rows[0],ensure_ascii=False)+'\n')
    run_id=f'evifuzz-{ns.agent}-run5-retry-{ns.instance.replace("__","-")}'
    (out/'RUN_CONFIG.md').write_text(f'''# Run 5 infrastructure retry\n- agent: {ns.agent}\n- instance: {ns.instance}\n- started_at: {datetime.datetime.now().astimezone().isoformat(timespec="seconds")}\n- model_name: {ns.model_name}\n- workers: 1\n- source prediction: {src}\n- run_id: {run_id}\n- podman socket: {ns.socket}\n''')
    (out/'LIVE_PROGRESS.md').write_text(f'# Infrastructure retry: {ns.agent} / {ns.instance}\n\n- phase: starting\n- completed: 0/1\n- updated_at: {datetime.datetime.now().astimezone().isoformat(timespec="seconds")}\n- log: {out/"evaluation.log"}\n')
    env=os.environ.copy(); env['DOCKER_HOST']='unix://'+ns.socket
    service=subprocess.Popen(['podman','system','service','--time=0','unix://'+ns.socket],stdout=(out/'podman_service.log').open('w'),stderr=subprocess.STDOUT)
    try:
      for _ in range(100):
        if Path(ns.socket).exists(): break
        time.sleep(.2)
      cmd=['<local-data>/anaconda3/bin/conda','run','--no-capture-output','-n','swebench-eval','python','-m','swebench.harness.run_evaluation','--dataset_name','SWE-bench/SWE-bench_Lite','--split','test','--predictions_path',str(pred),'--max_workers','1','--cache_level','instance','--clean','False','--run_id',run_id,'--report_dir',str(report)]
      with (out/'evaluation.log').open('w') as log:
        (out/'LIVE_PROGRESS.md').write_text(f'# Infrastructure retry: {ns.agent} / {ns.instance}\n\n- phase: evaluation\n- completed: running/1\n- started_at: {datetime.datetime.now().astimezone().isoformat(timespec="seconds")}\n- log: {out/"evaluation.log"}\n')
        p=subprocess.run(cmd,cwd=EVAL,env=env,stdout=log,stderr=subprocess.STDOUT)
      summary=next(report.glob('*.json'),None)
      status=json.loads(summary.read_text()) if summary else {}
      (out/'status.json').write_text(json.dumps({'returncode':p.returncode,'summary':status},ensure_ascii=False,indent=2)+'\n')
      (out/'LIVE_PROGRESS.md').write_text(f'# Infrastructure retry: {ns.agent} / {ns.instance}\n\n- phase: complete\n- completed: 1/1\n- returncode: {p.returncode}\n- error_ids: {status.get("error_ids",[])}\n- resolved: {status.get("resolved_instances")}\n- unresolved: {status.get("unresolved_instances")}\n- updated_at: {datetime.datetime.now().astimezone().isoformat(timespec="seconds")}\n- log: {out/"evaluation.log"}\n')
      return p.returncode
    finally:
      service.terminate(); service.wait(timeout=10)
      try: Path(ns.socket).unlink()
      except FileNotFoundError: pass

if __name__=='__main__': raise SystemExit(main())
