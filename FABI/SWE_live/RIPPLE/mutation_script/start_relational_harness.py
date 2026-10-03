#!/usr/bin/env python3
import json
from pathlib import Path
import full_run as fr
import mutation_pipeline as mp

run = Path('/data/zlyuaj/coding_agent/EviFuzz_SWE_live/RIPPLE/mutation_result/live-relational-20260928-g')
rows = fr.selected_rows()
patches = list((run / 'worker_patches').glob('*/*/mutation.patch'))
if len(patches) != 172:
    raise RuntimeError(f'patch count mismatch: {len(patches)}/172')
fr.event(run, kind='phase', phase='inference_evaluation', total=172, repaired_missing_case='deepset-ai__haystack-8799')
print('starting six inference/evaluation workers', flush=True)
rc = mp.run_harness(rows, run, run / 'worker_patches')
fr.event(run, kind='terminal', phase='complete' if rc == 0 else 'harness_failed', exit_code=rc)
state = json.loads((run / 'status.json').read_text()) if (run / 'status.json').exists() else {}
state.update({'phase': 'complete' if rc == 0 else 'harness_failed', 'exit_code': rc,
              'updated_at': mp.now(), 'completed': 172, 'total': 172, 'remaining': 0,
              'success': 172 if rc == 0 else 0, 'failed': 0 if rc == 0 else 1,
              'errors': 0, 'pid': None, 'log': str(run / 'RUN.log'), 'output_dir': str(run)})
mp.write_json(run / 'status.json', state)
raise SystemExit(rc)
