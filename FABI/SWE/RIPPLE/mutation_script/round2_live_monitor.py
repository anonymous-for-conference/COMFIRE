#!/usr/bin/env python3
import json,time,datetime,os
from pathlib import Path
root=Path(os.sys.argv[1]); total=312; log=root/'EVALUATION_RETRY_BATCH3.log'
while True:
    done=success=failed=0
    if log.exists():
        for line in log.read_text(errors='ignore').splitlines():
            p=line.split()
            if len(p)>=3 and p[0].isdigit() and p[2] in ('0','2','-1'):
                done+=1; success+=p[2]=='0'; failed+=p[2]!='0'
    active=[]
    for ag in ('codex','sweagent','opencode'):
        n=s=f=0
        for run in (root/ag/'runs').glob('*'):
            if (run/'EVALUATION_RETRY.log').exists():
                txt=(run/'EVALUATION_RETRY.log').read_text(errors='ignore')
                if 'official_summary' in txt or (run/'interface/evaluation_summary/official_summary.json').exists(): n+=1
        active.append(f'- `{ag}`: retry artifacts observed `{n}`')
    now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    infer_done=infer_ok=infer_bad=0
    ilog=root/'MISSING_INFERENCE_RETRY.log'
    if ilog.exists():
        for line in ilog.read_text(errors='ignore').splitlines():
            p=line.split()
            if p and p[0].isdigit():
                infer_done+=1
                if 'prediction True' in line: infer_ok+=1
                else: infer_bad+=1
    text=f'# 第二轮 Live Process\n\n- 更新时间：`{now}`\n- 原始批次总数：`312`\n- 首批 evaluation retry：`{done}/243`，成功返回 `{success}`，失败返回 `{failed}`\n- 缺失 inference 串行重跑：`{infer_done}/60`，生成 prediction `{infer_ok}`，失败 `{infer_bad}`，剩余 `{60-infer_done}`\n- 尚无 mutation manifest：`9`（单独 mutation retry）\n- tmux：`ripple_round2_missing_inference`\n'+'\n'.join(active)+'\n'
    (root/'LIVE_PROCESS.md').write_text(text)
    if done>=total: break
    time.sleep(30)
