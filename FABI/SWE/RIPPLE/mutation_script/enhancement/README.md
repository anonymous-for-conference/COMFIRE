# Documentation mitigation reruns

The archive contains 77 directories classified as errors. Of those, 28 failed
during mutation generation and never produced a mutation patch or an Agent
result. `EXCLUDED_INPUTS.json` records these pre-inference failures. This
experiment reruns all 49 eligible post-mutation Agent failures once under each
of four mitigations (196 jobs). A repeated agent/case in two rounds remains two
records because its mutation patch differs.

Strategies:

- `remove_docs`: strip Python docstrings/comments and repository prose files in
  the private inference view, preserving Python line structure.
- `ignore_docs`: system instruction to exclude repository documentation as
  evidence.
- `verify_docs`: system instruction to verify documentation against code and
  tests before relying on it.
- `evidence_boundary`: four-level evidence classification plus a mandatory
  documentation-triggered edit-boundary review.

The inference baseline is private. Predictions contain only agent edits. Before
official evaluation, `run_experiment.py` explicitly composes the archived
`mutation.patch` with the agent-only patch. This is especially important for
`remove_docs`: stripped documentation is never included in the evaluated patch.

Run:

```bash
export RIPPLE_ENHANCEMENT_API_KEY='...'
bash mutation_script/enhancement/launch.sh \
  mutation_result/enhancement ripple-enhancement-20260916
```

The job is resumable. A rerun reuses only terminal `result.json` records whose
phase is `completed`; infrastructure errors are attempted again. Results are in
`case_results.csv`, `SUMMARY.json`, and `SUMMARY.md`. Live state is in
`status.json` and `LIVE_PROGRESS.md`.
