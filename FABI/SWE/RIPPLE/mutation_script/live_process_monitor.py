#!/usr/bin/env python3
import datetime as dt,json,os,time
from pathlib import Path

def alive(pid):
    try: os.kill(int(pid),0); return True
    except (OSError,TypeError,ValueError): return False

def main(root):
    root=Path(root)
    while True:
        now=dt.datetime.now().astimezone().isoformat(timespec='seconds')
        lines=[f'# Live process\n',f'- 更新时间：`{now}`\n']
        for p in [root,root/'codex',root/'sweagent',root/'opencode']:
            s=p/'status.json'
            if s.exists():
                try:
                    x=json.loads(s.read_text())
                    pid=x.get('pid') or x.get('process_pid')
                    # A stage status may not carry a PID; consult its
                    # interface process.json as the authoritative child.
                    if not pid and (p/'interface/process.json').exists():
                        try: pid=json.loads((p/'interface/process.json').read_text()).get('pid')
                        except Exception: pass
                    lines.append(f'- `{p.name}`：phase=`{x.get("phase")}`, completed=`{x.get("completed",0)}/{x.get("total",0)}`, success=`{x.get("success",0)}`, failed=`{x.get("failed",0)}`, pid=`{pid}`, pid_alive=`{alive(pid)}`\n')
                except Exception: pass
        (root/'LIVE_PROCESS.md').write_text('\n'.join(lines))
        for p in [root/'codex',root/'sweagent',root/'opencode']:
            if (p/'status.json').exists():
                try:
                    x=json.loads((p/'status.json').read_text())
                    (p/'LIVE_PROCESS.md').write_text(f'# Live process\n\n- 更新时间：`{now}`\n- 阶段：`{x.get("phase")}`\n- 完成：`{x.get("completed",0)}/{x.get("total",0)}`\n- 成功：`{x.get("success",0)}`；失败：`{x.get("failed",0)}`\n- 主进程存活：`{alive(x.get("pid"))}`\n')
                except Exception: pass
        if (root/'status.json').exists():
            try:
                if json.loads((root/'status.json').read_text()).get('phase') in ('completed','failed'): break
            except Exception: pass
        time.sleep(30)

if __name__=='__main__': main(Path(os.sys.argv[1]))
