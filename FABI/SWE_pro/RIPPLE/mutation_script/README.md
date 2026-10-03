# RIPPLE SWE-bench Pro mutation smoke test

This implementation reads each selected case's `clustered_doc.jsonl` without a
level filter, samples three non-overlapping clusters, chooses one of L1-L3/R1-R3
per cluster, and mutates every location in that cluster. L1-L3 use a structured
`gpt-5.6-luna` medium request per location. R1-R3 use a read-only Codex agent with
`gpt-5.6-luna` high reasoning with a bounded, retry-adaptive repository exploration budget.

Each generated patch is validated against the task base commit and is restricted
to documentation tokens. The inference adapters call the existing, unchanged
clean-run implementations. Those implementations clone the base commit into a
private per-case repository, apply the mutation there, run the agent, and retain
the isolated repository as an audit artifact. Source repositories are never
patched in place.

The smoke set is the first two qualifying CSV rows for each of Codex, OpenCode,
and SWE-Agent. All three agents run concurrently, each with two inference workers.
Evaluation begins only after all inference completes, then runs concurrently with
two official-harness workers per agent.

Launch a timestamped long run:

```bash
bash mutation_script/launch_smoke.sh
```

Launch all 256 token-stable agent-case pairs:

```bash
bash mutation_script/launch_full.sh
```

The full run contains 118 Codex, 87 OpenCode, and 51 SWE-Agent cases. Mutation
generation uses three agent-specific two-worker pools (six concurrent cases);
inference and evaluation retain the same three-agent, two-worker-per-agent schedule.

Launch an R1-R3-only full run:

```bash
bash mutation_script/launch_relational_full.sh
```

Relational generation uses a read-only Codex repository agent at high reasoning.
Each cluster keeps independent attempt prompts, JSONL traces, responses, and
classified error records. Exploration starts with eight tool executions and can
grow to 24 on later attempts; a case can be regenerated up to five times while
validated manifests are reused on a run-level resume.

The command prints the run directory. Inspect `LIVE_PROGRESS.md`, `status.json`,
and `RUN.log` there. The tmux socket/session names and PIDs are in `PROCESS.json`.

Run the fast tests:

```bash
pytest -q mutation_script/test_mutation_pipeline.py
```
