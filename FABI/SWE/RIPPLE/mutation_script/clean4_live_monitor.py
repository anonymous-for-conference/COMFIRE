#!/usr/bin/env python3
import json,time,datetime,os
from pathlib import Path
root=Path(os.sys.argv[1]); retry=Path(os.sys.argv[2]) if len(os.sys.argv)>2 else None; agents=('codex','sweagent','opencode')
while True:
 lines=[f'# Clean run 4 Live Process\n',f'- 更新时间：`{datetime.datetime.now().astimezone().isoformat(timespec="seconds")}`\n']
 all_ok=True
 for ag in agents:
  p=(retry/ag if ag=='sweagent' and retry and (retry/ag).exists() else root/ag); total={'codex':149,'sweagent':74,'opencode':144}[ag]; vals=[]
  for f in (p/'interface').glob('**/validation.json') if (p/'interface').exists() else []:
   try:
    x=json.loads(f.read_text()); vals.append(x)
   except: pass
  latest={}
  for x in vals: latest[x.get('instance_id')]=x
  done=len(latest); valid=sum(x.get('valid') is True for x in latest.values()); failed=sum(x.get('valid') is False for x in latest.values())
  proc=None
  if (p/'interface/process.json').exists():
   try: proc=json.loads((p/'interface/process.json').read_text()).get('pid')
   except: pass
  alive=False
  try: os.kill(int(proc),0); alive=True
  except: pass
  lines.append(f'- `{ag}`：inference completed=`{done}/{total}`, valid=`{valid}`, failed=`{failed}`, pid=`{proc}`, pid_alive=`{alive}`\n')
  if valid<1: all_ok=False
 (root/'LIVE_PROCESS.md').write_text('\n'.join(lines))
 if all_ok: break
 time.sleep(30)
