#!/usr/bin/env python3
import datetime,json,os,time
from pathlib import Path

base=Path('/data/zlyuaj/coding_agent/EviFuzz/RIPPLE/mutation_result')
main=base/'all_agents_round2_adaptive_v2_20260901_165815'
mutation=base/'round2_missing_mutation_retry9_rightapi_20260902_151500'
while True:
    lines=[]
    log=main/'MISSING_INFERENCE_RIGHTAPI_RETRY.log'
    if log.exists():
        lines=[x for x in log.read_text(errors='ignore').splitlines() if x[:1].isdigit()]
    ok=sum('prediction True' in x for x in lines)
    state={}
    try: state=json.loads((mutation/'status.json').read_text())
    except Exception: pass
    now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    text=f'''# 第二轮 RightAPI Retry Live Process

- 更新时间：`{now}`
- API key：`sk-de21...f36d`
- Base URL：`https://rightapi.ai/codex/v1`
- 缺失 inference 全量重跑：`{len(lines)}/60`，成功生成 prediction：`{ok}`
- 9 个缺失 mutation 重跑：`{state.get('completed',0)}/{state.get('total',9)}`，成功：`{state.get('success',0)}`，失败：`{state.get('failed',0)}`，阶段：`{state.get('phase','starting')}`
- Clean run 4：`paused`
'''
    (main/'LIVE_PROCESS.md').write_text(text)
    time.sleep(30)
