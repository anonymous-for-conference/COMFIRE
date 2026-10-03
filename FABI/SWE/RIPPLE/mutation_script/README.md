# RIPPLE documentation mutation

`mutation_pipeline.py` reads `clustered_doc.jsonl`, joins complete locations from
`all_doc.jsonl`, selects one operator per cluster, mutates every selected unit,
validates documentation-only changes, and writes `mutation.patch`.

`experiment.py` clones the existing local Astropy repository into a run-private
worktree at the task base commit, mutates that local worktree, supplies it through
the existing interface's `repo_map`, analyzes whether Codex read the mutated text,
and restores the private worktree. `launch.sh RUN_ROOT RUN_ID` supplies tmux,
separate logs, status, and a live monitor.

Default experiment:

```bash
bash RIPPLE/mutation_script/launch.sh \
  RIPPLE/mutation_result/astropy6938_l1_<timestamp> \
  astropy6938_l1_<timestamp>
```

If inference has already produced a valid `predictions.jsonl` but official
evaluation needs to be retried, use the evaluation-only recovery path. It
reuses the existing prediction and does not regenerate a mutation or run the
inference agent again:

```bash
python RIPPLE/mutation_script/experiment.py \
  --output RIPPLE/mutation_result/<run> \
  --resume-evaluation
```

The interface also exposes the lower-level evaluation-only operation:

```bash
python RIPPLE/swe-bench-lite_interface.py evaluate \
  --agent codex --output RIPPLE/mutation_result/<run>/interface
```
