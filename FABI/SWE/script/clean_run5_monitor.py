#!/usr/bin/env python3
"""Independently maintain authoritative, visible run-5 progress summaries."""
from pathlib import Path
from datetime import datetime
import json, os, subprocess, time, tempfile

ROOT=Path('<local-data>/coding_agent/EviFuzz')
SPECS={
 'sweagent_gpt54_mini_run5':('SWE-Agent',74,'evifuzz_clean5_swe_lite','clean5_swe'),
 'codex_gpt54_mini_run5':('Codex',149,'evifuzz_clean5_codex','clean5_codex'),
 # OpenCode was resumed after the original tmux/podman namespace died.  Track
 # the retry namespace so ``experiment alive`` reflects the actual process.
 'opencode_gpt54_mini_run5':('OpenCode',144,'evifuzz_clean5_opencode_retry2','clean5_opencode_retry2'),
}
START=datetime.now().astimezone(); samples={k:[] for k in SPECS}
def now(): return datetime.now().astimezone().isoformat(timespec='seconds')
def alive(sock,session):
 return subprocess.run(['tmux','-L',sock,'has-session','-t',session],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0
def atomic(p,text):
 # Use a unique temporary file: multiple monitor instances may overlap during
 # restart.  A fixed ``.tmp`` lets one writer replace the file belonging to
 # another writer and raises FileNotFoundError, silently killing monitoring.
 fd, name = tempfile.mkstemp(prefix=p.name+'.', suffix='.tmp', dir=str(p.parent))
 try:
  with os.fdopen(fd, 'w') as f:
   f.write(text); f.flush(); os.fsync(f.fileno())
  os.replace(name, p)
 finally:
  try: os.unlink(name)
  except FileNotFoundError: pass
def scan(root):
 valid=invalid=0; current=[]; latest=None
 for c in sorted((root/'cases').glob('*')) if (root/'cases').exists() else []:
  terminal=False
  for a in sorted(c.glob('attempt_*'),reverse=True):
   v=a/'validation.json'
   if v.exists():
    try: ok=json.loads(v.read_text()).get('valid') is True
    except Exception: ok=False
    valid += ok; invalid += not ok; terminal=True; break
  if not terminal and any(c.rglob('*')): current.append(c.name)
  for f in c.rglob('*'):
   if f.is_file() and (latest is None or f.stat().st_mtime>latest): latest=f.stat().st_mtime
 # SWE layout has run_5/cases.
 if (root/'run_5'/'cases').exists():
  shadow=root/'run_5'; return scan(shadow)
 return valid,invalid,current[:4],latest
while True:
 all_done=True
 for dirname,(label,total,session,sock) in SPECS.items():
  root=ROOT/dirname; valid,invalid,current,latest=scan(root); completed=valid+invalid
  running=alive(sock,session); all_done &= (completed>=total or not running)
  ts=time.time(); samples[dirname].append((ts,completed)); samples[dirname]=samples[dirname][-20:]
  eta='unknown'
  moving=[x for x in samples[dirname] if x[1]!=samples[dirname][0][1]]
  if completed>=total: eta='0s'
  elif len(moving)>=2 and moving[-1][1]>moving[0][1]:
   eta=f"{int((total-completed)*(moving[-1][0]-moving[0][0])/(moving[-1][1]-moving[0][1]))}s"
  # A stopped process with all cases terminal is complete; a stopped process
  # with missing cases is an error.  Do not overwrite a stronger authoritative
  # complete/evaluation state emitted by the orchestrator.
  phase='inference' if running else ('complete' if completed>=total else 'stopped/error')
  existing = root/'orchestrator_status.json'
  if existing.exists():
   try:
    old=json.loads(existing.read_text())
    if old.get('phase') in ('complete','evaluation_complete') and completed>=total:
     phase=old['phase']
   except Exception: pass
  last=datetime.fromtimestamp(latest).astimezone().isoformat(timespec='seconds') if latest else 'none'
  old_status={}
  try: old_status=json.loads((root/'status.json').read_text())
  except Exception: pass
  started=old_status.get('started_at', START.isoformat(timespec='seconds'))
  # Preserve an authoritative evaluation failure instead of downgrading it to
  # generic complete merely because all inference artifacts exist.
  if old_status.get('phase') == 'failed' and not running:
   phase='failed'
  status={'updated_at':now(),'phase':phase,'started_at':started,'completed':completed,'total':total,'remaining':max(0,total-completed),'success':valid,'failed':invalid,'errors':old_status.get('errors',0) if phase=='failed' else (0 if running or completed>=total else 1),'eta':eta,'pid':os.getpid(),'process_alive':running,'current_cases':current,'last_event_at':last,'log':str(root/'RUN.log'),'output_dir':str(root)}
  atomic(root/'status.json',json.dumps(status,ensure_ascii=False,indent=2)+'\n')
  md=f"""# {label} clean run 5 live progress

- updated_at: `{status['updated_at']}`
- phase: **{phase}**
- started_at: `{status['started_at']}`
- completed: `{completed}/{total}`
- remaining: `{status['remaining']}`
- successful inference: `{valid}`
- invalid/failed inference: `{invalid}`
- infrastructure errors: `{status['errors']}`
- current cases: `{', '.join(current) if current else 'none/waiting'}`
- last artifact event: `{last}`
- ETA: `{eta}`
- experiment alive: `{running}`
- tmux: `tmux -L {sock} attach -t {session}`
- RUN log: `{root/'RUN.log'}`

`completed` means a case has a persisted validation artifact; `success` means validation.valid=true. This file is atomically refreshed every 20 seconds by an independent monitor.
"""
  atomic(root/'LIVE_PROGRESS.md',md)
 if all_done: break
 time.sleep(20)
